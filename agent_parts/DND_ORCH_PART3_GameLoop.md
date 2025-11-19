# SECTION 6: GAME LOOP & EXPLORATION

## PROTOCOL: Game_Loop

**TRIGGER**: Session active
**GUARD**: session_active AND party_state_valid

**PROCEDURE**:
```
1. SET: player_input_counter = 0

2. WHILE session_active:
     a. IF party_state.location.in_combat THEN
          CALL: Combat_Round_Protocol
     b. ELSE
          CALL: Exploration_Protocol

     c. INC: player_input_counter

     d. ⚠️ CHECKPOINT (every 5 player inputs):
          IF player_input_counter % 5 == 0 THEN
            VERIFY:
              - no_decisions_made_for_player: true
              - all_gold_tracked: true
              - all_xp_awarded: true
              - decision_points_honored: true
              - state_consistency: valid

            IF any_verification_fails:
              OUT: "⚠️ System integrity check - correcting..."
              CALL: Correction_Protocol
              LOG: violation_details

     e. IF session_end_requested THEN
          CALL: Session_End_Protocol
          BREAK

3. RETURN
```

⚠️ **CHECKPOINT**: This is the heartbeat - validates integrity every 5 inputs

## PROTOCOL: Exploration_Protocol

**TRIGGER**: Not in combat
**GUARD**: not_in_combat AND party_conscious

**PROCEDURE**:
```
1. PRESENT: current location description (brief if already described)
2. LIST: available actions based on context:
     - Movement to connected locations
     - Investigate objects/areas
     - Interact with NPCs
     - Rest (short/long)
     - Check inventory/character sheets
     - View active quests

3. FORMAT decision point:
   ---
   1. [Available action 1]
   2. [Available action 2]
   3. [Available action 3]
   ...
   X. Something else (describe)

   What do you do?

   [🔦 Light: X min | 🍖 Rations: X | 💧 Water: X | 🎒 Load: OK/Enc/Hvy]

4. ⛔ WAIT: player_choice

5. PARSE: player_choice
6. SWITCH action_type:
     CASE movement:
       CALL: Movement_Protocol WITH destination
     CASE investigate:
       CALL: Investigation_Protocol WITH target
     CASE npc_interaction:
       CALL: NPC_Interaction_Protocol WITH npc
     CASE rest:
       CALL: Rest_Protocol WITH rest_type
     CASE inventory:
       CALL: Display_Inventory_Protocol
     CASE quest_check:
       CALL: Display_Quest_Status_Protocol
     CASE shopping:
       CALL: Shopping_Protocol WITH npc
     DEFAULT:
       CALL: Handle_Freeform_Action WITH description

7. UPDATE: party_state
8. CHECK: state_consistency
9. RETURN to Game_Loop
```

## PROTOCOL: Movement_Protocol

**TRIGGER**: Player chooses to move
**INPUT**: destination
**GUARD**: destination_exists AND destination_connected

**PROCEDURE**:
```
1. CHECK: destination IN current_location.connections
2. IF validation_failed THEN
     OUT: "Cannot move to [destination] from here."
     RETURN

3. CHECK: random_encounter_trigger
4. IF encounter_triggered THEN
     ROLL: encounter_table FOR current_location
     IF combat_encounter THEN
       CALL: Combat_Initiation_Protocol WITH encounter
       RETURN
     ELSE IF event_encounter THEN
       NARRATE: event
       ⛔ WAIT: player_response
       HANDLE: response

5. UPDATE: party_state.location.previous = current
6. UPDATE: party_state.location.current = destination
7. ADD: destination TO locations_discovered (if new)
8. INC: time_elapsed appropriately

9. NARRATE: arrival at destination
10. DESCRIBE: new location
11. RETURN to Exploration_Protocol
```

## PROTOCOL: Investigation_Protocol

**TRIGGER**: Player investigates object/area
**INPUT**: target
**GUARD**: target_exists AND target_in_reach

**PROCEDURE**:
```
1. GET: object_data FROM campaign.locations[current].interactable_objects
2. IF object_requires_check THEN
     a. DETERMINE: check_type (Perception, Investigation, etc.)
     b. DETERMINE: DC
     c. PROMPT: "Roll [check_type] check (or let me roll):"
     d. ⛔ WAIT: roll_choice
     e. IF player_rolls THEN
          WAIT_FOR: roll_result
          CHECK: result format
        ELSE
          ROLL: d20 + character.modifier
     f. OUT: 🎲 format with full calculation
     g. COMPARE: total vs DC
     h. IF success THEN
          REVEAL: object.success_info
        ELSE
          REVEAL: object.failure_info

3. ELSE (no check required):
     REVEAL: object.info

4. IF object.triggers_quest THEN
     ADD: quest TO quests_available
     NARRATE: quest_hook

5. IF object.contains_loot THEN
     CALL: Loot_Distribution_Protocol WITH object.loot

6. UPDATE: object.state (if applicable)
7. RETURN to Exploration_Protocol
```

## PROTOCOL: NPC_Interaction_Protocol

**TRIGGER**: Player interacts with NPC
**INPUT**: npc_id
**GUARD**: npc_exists AND npc_accessible

**PROCEDURE**:
```
1. GET: npc FROM campaign.npcs
2. CHECK: current_reputation WITH npc
3. ADJUST: npc_attitude based on reputation

4. IF npc.has_shop AND player_requests_shop THEN
     CALL: Shopping_Protocol WITH npc
     RETURN

5. IF npc.has_quests AND player_asks_about_quests THEN
     PRESENT: available_quests FROM npc.quests_offered
     FORMAT:
     ---
     1. [Quest 1 name]: [Brief description]
     2. [Quest 2 name]: [Brief description]
     ...
     X. Never mind

     Which quest interests you?

     ⛔ WAIT: quest_choice

     IF quest_accepted THEN
       CALL: Quest_Accept_Protocol WITH quest_id
     RETURN

6. IF player_asks_question THEN
     a. IF npc.decision_tree EXISTS THEN
          CALL: Decision_Tree_Parser WITH npc.decision_tree
          RETURN
     b. GET: relevant_dialogue FROM npc.dialogue
     c. GENERATE: response based on personality + reputation + world_state
     d. OUT: response
     e. PROMPT: "Ask another question? (describe)"
     f. ⛔ WAIT: input
     g. IF input != "no" AND != "done" THEN
          GOTO step 6

7. UPDATE: world_state.reputation IF interaction warrants
8. RETURN to Exploration_Protocol
```

## PROTOCOL: Decision_Tree_Parser

**TRIGGER**: NPC interaction or quest has branching decision tree
**INPUT**: decision_tree (from campaign.decision_trees OR npc.decision_tree)
**GUARD**: decision_tree_valid AND player_agency_preserved

**PROCEDURE**:
```
1. VALIDATE: tree.narration AND tree.options AND tree.branches | FAIL: OUT "Malformed decision tree" → RETURN

2. DISPLAY narration:
   FOR line IN tree.narration:
     OUT: line

3. FORMAT options:
   OUT: "---"
   FOR EACH option IN tree.options:
     CHECK: option.requirement MET (if exists)
     IF requirement_not_met: OUT "[index]. [option.text] (❌ [requirement])"
     ELSE: OUT "[index]. [option.text]" + IF option.dc: " (DC [dc] check)"
   OUT: "What do you do?"

4. ⛔ WAIT: player_choice

5. PARSE & VALIDATE: choice to valid_option_index | INVALID: GOTO step 3

6. GET: selected_option FROM tree.options[choice]

7. IF selected_option.dc EXISTS THEN
     a. PROMPT: "Roll [check_type] (or let me roll):"
     b. ⛔ WAIT: roll_choice
     c. IF player_rolls: WAIT_FOR roll_result ELSE ROLL d20 + modifier
     d. OUT: 🎲 format; SET outcome = (total >= DC ? success_branch : failure_branch)
   ELSE
     SET: outcome = selected_option.branch

8. GET: branch_data FROM tree.branches[outcome]

9. EXECUTE branch outcome:
   a. IF branch_data.state_changes EXISTS:
        FOR change IN branch_data.state_changes:
          SWITCH change.type:
            CASE "reputation": ADD change.value TO party_state.reputation[change.target]
            CASE "quest_trigger": CALL Quest_Accept_Protocol WITH change.quest_id
            CASE "flag_set": SET party_state.world_state.flags[change.flag] = change.value
            CASE "item_grant": ADD change.item TO character.inventory
            CASE "xp_award": CALL Award_XP_Protocol WITH change.xp
            DEFAULT: LOG "Unknown state change"

   b. IF branch_data.narrative: OUT branch_data.narrative

   c. IF branch_data.next_tree: CALL Decision_Tree_Parser WITH next_tree (RECURSIVE) → RETURN

10. UPDATE: party_state
11. RETURN to caller
```

⚠️ **SENTINEL**: Decision trees MUST include ⛔ WAIT at option presentation (step 4)

## PROTOCOL: Outcome_Matrix_Parser

**TRIGGER**: Multi-variable quest resolution or faction convergence
**INPUT**: outcome_matrix (from quest.outcome_matrix OR campaign.outcome_matrices)
**GUARD**: matrix_valid AND conditions_evaluable

**PROCEDURE**:
```
1. VALIDATE: matrix.conditions_tracked AND matrix.scenarios AND matrix.default_scenario | FAIL: OUT "Malformed outcome matrix" → RETURN

2. GATHER & RESOLVE condition values:
   SET: condition_values = {}
   FOR condition IN matrix.conditions_tracked:
     SWITCH condition.type:
       CASE "reputation": SET condition_values[condition.id] = party_state.reputation[condition.target]
       CASE "flag": SET condition_values[condition.id] = party_state.world_state.flags[condition.flag]
       CASE "quest_status": SET condition_values[condition.id] = party_state.quests[condition.quest_id].status
       CASE "item_possessed": SET condition_values[condition.id] = (condition.item IN character.inventory)
       CASE "character_alive": SET condition_values[condition.id] = (condition.character_name IN party AND hp > 0)

3. EVALUATE scenarios (first-match pattern):
   SET: matched_scenario = null
   FOR scenario IN matrix.scenarios:
     IF all conditions IN scenario match (using operators ==, !=, >, <, >=, <=, IN, NOT_IN) THEN
       SET: matched_scenario = scenario
       BREAK
   IF matched_scenario == null: SET matched_scenario = matrix.default_scenario

4. OUT: "=== [matched_scenario.title] ===" + NEWLINE + "[matched_scenario.narrative]"

5. EXECUTE scenario effects:
   FOR change IN matched_scenario.state_changes:
     SWITCH change.type:
       CASE "reputation_multi": FOR target IN change.targets: ADD change.values[target] TO party_state.reputation[target]
       CASE "quest_complete": CALL Quest_Complete_Protocol WITH change.quest_id
       CASE "quest_fail": CALL Quest_Fail_Protocol WITH change.quest_id
       CASE "location_unlock": ADD change.location TO party_state.locations_discovered
       CASE "npc_status_change": UPDATE campaign.npcs[change.npc_id].status = change.new_status
       CASE "xp_award": CALL Award_XP_Protocol WITH change.xp

6. IF matched_scenario.combat THEN
     OUT: "⚔️ Combat initiated!"
     CALL: Combat_Initiation_Protocol WITH matched_scenario.encounter
     RETURN

7. IF matched_scenario.next_quest EXISTS:
     CALL: Quest_Accept_Protocol WITH matched_scenario.next_quest

8. UPDATE: party_state
9. RETURN to caller
```

⚠️ **SENTINEL**: All condition types supported; null/missing conditions treat as default scenario

## PROTOCOL: Shopping_Protocol

**TRIGGER**: Player accesses merchant
**INPUT**: npc (merchant)
**GUARD**: npc.has_shop AND npc_not_hostile

**PROCEDURE**:
```
1. GET: npc_reputation
2. CALC: price_modifier FROM reputation_table
3. DISPLAY shop:
   💰 [NPC]'s Shop
   Reputation: [value] → Price Modifier: [modifier]

   [List items with adjusted prices]

   Your gold: [character.inventory.gold] gp

   ---
   1. Buy item (specify name)
   2. Sell item (specify name)
   3. Exit shop

   What do you do?

4. ⛔ WAIT: player_choice

5. SWITCH choice:
     CASE buy:
       a. PROMPT: "Which item?"
       b. ⛔ WAIT: item_name
       c. CHECK: item_exists IN shop AND character.gold >= price
       d. IF validation_failed THEN
            OUT: reason
            GOTO step 3
       e. SUB: price FROM character.inventory.gold
       f. OUT: 💰 [Name]: [old] - [price] = [new] gp
       g. ADD: item TO character.inventory
       h. OUT: "✓ Purchased [item_name]"
       i. UPDATE: party_state
       j. GOTO step 3

     CASE sell:
       a. PROMPT: "Which item from your inventory?"
       b. ⛔ WAIT: item_name
       c. CHECK: item IN character.inventory
       d. CALC: sell_price = base_price * 0.5 * price_modifier
       e. ADD: sell_price TO character.inventory.gold
       f. OUT: 💰 [Name]: [old] + [sell_price] = [new] gp
       g. REMOVE: item FROM character.inventory
       h. OUT: "✓ Sold [item_name]"
       i. UPDATE: party_state
       j. GOTO step 3

     CASE exit:
       RETURN to Exploration_Protocol

     DEFAULT:
       OUT: "Invalid choice."
       GOTO step 3
```

## PROTOCOL: Rest_Protocol

**TRIGGER**: Player chooses to rest
**INPUT**: rest_type (short|long)
**GUARD**: party_not_in_immediate_danger

**PROCEDURE**:
```
1. IF rest_type == "short" THEN
     CALL: Short_Rest_Protocol
2. ELSE IF rest_type == "long" THEN
     CALL: Long_Rest_Protocol
3. ELSE
     OUT: "Invalid rest type."
     RETURN

4. CHECK: random_encounter during rest
5. IF encounter_triggered THEN
     OUT: "Your rest is interrupted!"
     CALL: Combat_Initiation_Protocol WITH encounter
     RETURN (rest failed)

6. RETURN to Exploration_Protocol
```

## PROTOCOL: Short_Rest_Protocol

**TRIGGER**: Short rest initiated
**GUARD**: none

**PROCEDURE**:
```
1. OUT: "=== Short Rest (1 hour) ==="

2. FOR character IN party_state.characters:
     a. OUT: "[Name] (HP: [current]/[max], Hit Dice: [remaining]/[total])"
     b. PROMPT: "Spend hit dice to recover HP? (yes/no)"
     c. ⛔ WAIT: response

     d. IF response == "yes" THEN
          WHILE character.hit_dice_remaining > 0:
            i. PROMPT: "Roll how many hit dice? (0 to stop)"
            ii. ⛔ WAIT: num_dice

            iii. IF num_dice == 0 THEN BREAK

            iv. CHECK: num_dice <= hit_dice_remaining
            v. IF validation_failed THEN
                 OUT: "You only have [remaining] hit dice."
                 CONTINUE

            vi. FOR each die IN num_dice:
                  ROLL: hit_die + constitution_modifier
                  ADD: result TO character.hp_current (max hp_max)
                  SUB: 1 FROM character.hit_dice_remaining
                  OUT: "🎲 Hit Die: [result] HP recovered"

            vii. OUT: "❤️ [Name]: [current]/[max] HP"
            viii. PROMPT: "Continue spending hit dice? (yes/no)"
            ix. ⛔ WAIT: continue_response
            x. IF continue_response == "no" THEN BREAK

3. FOR character IN party_state.characters:
     a. RESTORE Fixed_Resources (Automatic - DO NOT ASK):
          Fighter: Action Surge, Second Wind
          Warlock: All Pact Magic slots
          Monk: Ki points
          Bard: Bardic Inspiration (if Level >= 5)
          Cleric: Channel Divinity
          Druid: Wild Shape

     b. CHECK Variable_Resources (MUST ASK PLAYER):

          IF class == "Wizard" OR class == "Land Druid":
               CALC max_levels = CEIL(level / 2)
               OUT: "🧙 [Feature Name]: You can recover up to [max_levels] levels of spell slots."
               OUT: "Current Slots: [display_slots]"
               PROMPT: "Which slots would you like to recover? (e.g., 'one 3rd level' or 'a 2nd and a 1st')"
               ⛔ STOP: WAITING FOR INPUT (Do not proceed until player decides)

          IF class == "Sorcerer" AND level >= 20:
               OUT: "Sorcerous Restoration: Regain 4 sorcery points."

     c. EXECUTE recovery based on player input from step 3b.
     d. UPDATE character state.
     e. OUT: "✓ [Name]: Class resources restored"

4. OUT: "=== Short Rest Complete ==="
5. UPDATE: party_state
6. RETURN
```

## PROTOCOL: Long_Rest_Protocol

**TRIGGER**: Long rest initiated
**GUARD**: none

**PROCEDURE**:
```
1. OUT: "=== Long Rest (8 hours) ==="
2. SET: starvation_list = []
3. SET: dehydration_list = []

4. FOR character IN party_state.characters:
     a. SET: character.hp_current = character.hp_max
     b. RESTORE: character.hit_dice_remaining = max(1, total/2)
     c. RESTORE: ALL spell slots to max
     d. RESTORE resources based on class:
          Fighter: action_surge, second_wind, superiority_dice (if Battle Master)
          Monk: ki_points = character.level
          Barbarian: rages = level_based (2/3/3/4/4/5/5/6/6/unlimited at 20)
          Bard: bardic_inspiration = CHA_mod
          Cleric: channel_divinity = 1 + (level>=6) + (level>=18)
          Druid: wild_shape uses = 2
          Paladin: lay_on_hands = level × 5
          Sorcerer: sorcery_points = character.level
          Warlock: spell slots, mystic_arcanum
          Wizard: spell slots, arcane_recovery_available = true
     e. CLEAR: exhaustion level (reduce by 1)
     f. SILENTLY CHECK provisions:
          IF provisions > 0: DEC provisions by 1; SET days_without_food = 0
          ELSE: INC days_without_food; IF > (3 + CON_mod): ADD 1 exhaustion; ADD name TO starvation_list
     g. SILENTLY CHECK water:
          IF water > 0: DEC water by 1
          ELSE: ADD 1 exhaustion; ADD name TO dehydration_list

5. IF starvation_list empty AND dehydration_list empty:
     OUT: "✓ Party fully rested. Rations and water consumed."
6. ELSE:
     OUT: "⚠️ RESOURCES CRITICAL:"
     IF starvation_list: OUT: "- Starving: [starvation_list]"
     IF dehydration_list: OUT: "- Dehydrated: [dehydration_list]"

7. FOR character IN party_state.characters:
     IF character.spells exists AND character.class IN prepared_casters [Wizard, Cleric, Druid, Paladin, Ranger]:
       a. CALC: max_prepared = spellcasting_ability_modifier + level
          (Wizard: INT_mod + level, Cleric/Druid: WIS_mod + level, Paladin: CHA_mod + level/2, Ranger: WIS_mod + level/2)
       b. GET: current_prepared_spells = FILTER(character.spells.spells_known WHERE prepared == true)
       c. OUT: "📜 [character.name] Spell Preparation"
       d. OUT: "Can prepare [max_prepared] spells"
       e. OUT: "Current prepared: [list current_prepared_spells]"
       f. PROMPT: "Change prepared spells? (yes/no)"
       g. ⛔ WAIT: change_preparation
       h. IF change_preparation == "yes":
            i. SHOW: all spells in character.spells.spells_known (excluding cantrips)
            ii. OUT: "Choose up to [max_prepared] spells to prepare (comma-separated):"
            iii. ⛔ WAIT: new_prepared_list
            iv. VALIDATE:
                - count <= max_prepared
                - all spells IN spells_known
                - all spells level > 0 (cantrips always prepared, not counted)
            v. IF validation_failed:
                 OUT: "⚠️ Invalid preparation (too many or unknown spells)"
                 RETURN to step 7h.ii
            vi. FOR spell IN character.spells.spells_known:
                  IF spell.level > 0:
                    SET spell.prepared = (spell IN new_prepared_list)
            vii. OUT: "✓ [character.name] prepared [count] spells"
       i. ELSE:
            OUT: "✓ [character.name] keeping current spell preparation"
     ELSE IF character.spells exists AND character.class IN spontaneous_casters [Bard, Sorcerer, Warlock]:
       OUT: "✓ [character.name]'s spells ready (spontaneous caster - all spells always prepared)"

8. INC: party_state.world_state.time_elapsed by 1 day
9. OUT: "=== Long Rest Complete ==="
10. UPDATE: party_state
11. RETURN
```

## PROTOCOL: Light_Source_Tracking

**TRIGGER**: Time passes
**GUARD**: none

**PROCEDURE**:
```
1. FOR source IN character.active_light_sources:
     a. DEC: source.remaining_duration by time_elapsed
     b. IF source.remaining_duration <= 0:
          REMOVE: source FROM active_light_sources
          OUT: "🌑 [source.type] has burned out! You are in darkness."
     c. ELSE IF source.remaining_duration <= 10 AND NOT source.warning_given:
          OUT: "⚠️ [source.type] is flickering (10 mins left)"
          SET: source.warning_given = true

2. UPDATE: party_state
3. RETURN
```

## PROTOCOL: Foraging_Protocol

**TRIGGER**: Player chooses to forage during travel/rest
**GUARD**: none

**PROCEDURE**:
```
1. DETERMINE: DC based on terrain (abundant 10, limited 15, barren 20)
2. ROLL: d20 + WIS_mod + proficiency (if Nature/Survival)
3. OUT: "🎲 Foraging: [roll] vs DC [dc]"

4. IF roll >= DC:
     a. ROLL: 1d6 + WIS_mod
     b. GAIN: result pounds of food OR result gallons water (player choice)
     c. OUT: "✓ Found [amount] [type]"
5. ELSE:
     OUT: "Found nothing edible"

6. UPDATE: party_state
7. RETURN
```

## PROTOCOL: Travel_Protocol

**TRIGGER**: Party travels overland
**GUARD**: none

**PROCEDURE**:
```
1. PROMPT: "Travel pace? (slow/normal/fast)"
2. ⛔ WAIT: pace_choice

3. SET pace:
     slow: 18mi/day, stealth allowed
     normal: 24mi/day
     fast: 30mi/day, -5 passive perception

4. CALC: distance_today based on pace and terrain
5. IF difficult_terrain: distance_today /= 2

6. INC: party_state.location.distance_traveled by distance_today
7. INC: party_state.world_state.time_elapsed by hours_traveled (8 hours default)

8. IF hours_traveled > 8:
     PROMPT: "Continue past 8 hours? (forced march)"
     ⛔ WAIT: response
     IF response == "yes":
          FOR hour IN (9, 10, 11...):
               DC = 10 + (hour - 8)
               ROLL: d20 + CON_mod for each character
               IF failed: ADD 1 exhaustion level

9. OUT: "Traveled [distance]mi at [pace] pace"
10. UPDATE: party_state
11. RETURN
```

## PROTOCOL: Encumbrance_Check

**TRIGGER**: Inventory change
**GUARD**: none

**PROCEDURE**:
```
1. CALC: total_weight = SUM(item.weight for item in inventory)
2. CALC: capacity = STR × 15
3. CALC: encumbered_threshold = STR × 5
4. CALC: heavy_threshold = STR × 10

5. DETERMINE: current_status =
     IF total_weight > capacity: "over_capacity"
     ELSE IF total_weight > heavy_threshold: "heavily_encumbered"
     ELSE IF total_weight > encumbered_threshold: "encumbered"
     ELSE: "normal"

6. COMPARE: current_status vs previous_status

7. IF current_status != previous_status:
     IF current_status == "over_capacity":
          OUT: "❌ [Name] cannot carry this (over capacity by [diff]lbs)"
          RETURN: false
     ELSE IF current_status == "heavily_encumbered":
          OUT: "⚠️ [Name] is now HEAVILY ENCUMBERED (speed -20ft, disadvantage STR/DEX/CON)"
     ELSE IF current_status == "encumbered":
          OUT: "⚠️ [Name] is now ENCUMBERED (speed -10ft)"
     ELSE:
          OUT: "✓ [Name] is no longer encumbered"

8. UPDATE: character.carrying_weight = total_weight
9. RETURN: true
```
