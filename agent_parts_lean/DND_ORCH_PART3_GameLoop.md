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

3. DISPLAY MANDATORY HUD:
   GET: active_light = character.active_light_sources[0] IF exists ELSE "None"
   GET: total_rations = SUM(character.survival.provisions FOR character IN party)
   GET: total_water = SUM(character.survival.water FOR character IN party)
   GET: load_status = "OK" OR "Enc" OR "Hvy" (based on Encumbrance_Check)
   GET: time = party_state.world_state.time_of_day (morning/afternoon/evening/night)

   OUT: "━━━ 📊 STATUS ━━━"
   OUT: "🕒 Time: Day [day_num], [time]"
   OUT: "🔦 Light: [active_light.type] ([active_light.remaining] min) | Vision: [Normal/Dim/Dark]"
   OUT: "🎒 Load: [FOR character: [name]: [load_status]]"
   OUT: "🍖 Rations: [total_rations] | 💧 Water: [total_water]"
   OUT: "🏹 Ammo: [FOR character WITH ranged weapons: [name]: [ammo.type] [ammo.count]]"
   OUT: "💰 Gold: [party_gold] gp"
   IF active_effects EXISTS:
     OUT: "🧙 Active Effects: [list effects with duration]"
   OUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
   OUT: ""

4. FORMAT decision point:
   ---
   1. [Available action 1]
   2. [Available action 2]
   3. [Available action 3]
   ...
   X. Something else (describe)

   What do you do?

5. ⛔ WAIT: player_choice

6. PARSE: player_choice
7. SWITCH action_type:
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

8. UPDATE: party_state
9. CHECK: state_consistency
10. RETURN to Game_Loop
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

3. CALL: Random_Encounter_Protocol WITH encounter_context="movement", location_id=current
4. IF encounter_occurred AND in_combat:
     RETURN (encounter protocol handles combat initiation)

5. UPDATE: party_state.location.previous = current
6. UPDATE: party_state.location.current = destination
7. ADD: destination TO locations_discovered (if new)
8. CALL: Time_Tracking_Protocol WITH minutes_to_add=60

10. NARRATE: arrival at destination
11. DESCRIBE: new location

13. RETURN to Exploration_Protocol
```

## PROTOCOL: Investigation_Protocol

**TRIGGER**: Player investigates object/area
**INPUT**: target
**GUARD**: target_exists AND target_in_reach

**PROCEDURE**:
```
1. GET: object_data FROM campaign.locations[current].interactable_objects

2. CHECK lighting_conditions IF check requires sight:
   GET: has_light = ANY(character.active_light_sources) OR location.lighting == "bright"
   GET: is_dim = location.lighting == "dim" OR (NOT has_light AND character.darkvision)
   GET: is_dark = NOT has_light AND NOT character.darkvision

   IF is_dark AND check_requires_sight:
     OUT: "⚠️ Too dark to see - need light source or darkvision!"
     RETURN
   ELSE IF is_dim:
     OUT: "⚠️ Dim light - Disadvantage on Perception checks"
     SET: disadvantage_on_perception = true

3. IF object_requires_check THEN
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

6. IF object.triggers_quest_progress THEN
     CALL: Quest_Progress_Update_Protocol WITH quest_id=object.quest_id, objective_id=object.objective_id, progress_description=object.progress_update

7. UPDATE: object.state (if applicable)
8. RETURN to Exploration_Protocol
```

## PROTOCOL: NPC_Interaction_Protocol

**TRIGGER**: Player interacts with NPC
**INPUT**: npc_id
**GUARD**: npc_exists AND npc_accessible

**PROCEDURE**:
```
2. GET: npc FROM campaign.npcs
3. CHECK: current_reputation WITH npc
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
       e. CALL: Encumbrance_Check WITH character
       f. IF over_capacity: OUT "Cannot carry this item!" → GOTO step 3
       g. SUB: price FROM character.inventory.gold
       h. OUT: 💰 [Name]: [old] - [price] = [new] gp
       i. ADD: item TO character.inventory
       j. OUT: "✓ Purchased [item_name]"
       k. CALL: Encumbrance_Check WITH character (update load status)
       l. UPDATE: party_state
       m. GOTO step 3

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

4. CALL: Random_Encounter_Protocol WITH encounter_context="rest", location_id=party_state.location.current
5. IF encounter_occurred:
     OUT: "⚠️ Rest interrupted by encounter!"
     RETURN (rest failed, handle encounter first)

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
     a. RESTORE: fixed_resources (per PHB short rest - action surge, second wind, warlock slots, ki, channel divinity, wild shape, bardic inspiration if level 5+)

     b. CHECK: variable_resources (MUST ASK PLAYER for choices):
          - Wizard/Land Druid: Arcane Recovery (recover spell slots up to CEIL(level/2) slot levels) → PROMPT which slots → ⛔ WAIT
          - Sorcerer (level 20): Sorcerous Restoration (4 sorcery points) → PROMPT accept → ⛔ WAIT
          - Other class features requiring player choice → PROMPT → ⛔ WAIT

     c. EXECUTE: recovery based on player input
     d. UPDATE: character state
     e. OUT: "✓ [Name]: Resources restored"

6. OUT: "=== Short Rest Complete ==="
8. UPDATE: party_state
9. RETURN
```

## PROTOCOL: Long_Rest_Protocol

**TRIGGER**: Long rest initiated
**GUARD**: none

1. OUT: "=== ⛺ Long Rest (8 hours) ==="

2. MECHANICAL RESTORATION:
   FOR character IN party_state.characters:
     a. SET: character.hp_current = character.hp_max
     b. RESTORE: character.hit_dice_remaining = min(total, current + total/2)
     c. RESTORE: ALL spell slots to max
     d. RESTORE: class resources (per PHB long rest rules - action surge, ki, rages, channel divinity, wild shape, sorcery points, etc.)
     e. CLEAR: exhaustion level (reduce by 1)
     f. CONSUME: 1 ration (DEC provisions by 1; IF provisions <= 0: ADD 1 exhaustion, SET starvation warning)
     g. CONSUME: 1 water (DEC water by 1; IF water <= 0: ADD 1 exhaustion, SET dehydration warning)

3. IF starvation or dehydration warnings triggered:
     OUT: "⚠️ RESOURCES CRITICAL:"
     IF starvation: OUT: "- Characters are starving (no provisions)"
     IF dehydration: OUT: "- Characters are dehydrated (no water)"
   ELSE:
     OUT: "✓ Party fully rested. Rations and water consumed."

4. PREPARED CASTERS (Wizard/Cleric/Druid/Paladin/Ranger):
   FOR character IN party_state.characters WHERE character.class IN prepared_casters:
     a. OUT: "📜 SPELL PREPARATION"
     b. CALC: max_prepared = spellcasting_ability_modifier + level
        (Wizard: INT_mod + level, Cleric/Druid: WIS_mod + level, Paladin: CHA_mod + level/2, Ranger: WIS_mod + level/2)
     c. GET: current_prepared = FILTER(character.spells.spells_known WHERE prepared == true)
     d. OUT: "[character.name]: Can prepare [max_prepared] spells."
     e. OUT: "Current prepared: [list current_prepared]"
     f. PROMPT: "Change prepared spells? (yes/no)"
     g. ⛔ WAIT: change_preparation
     h. IF change_preparation == "yes":
          i. SHOW: all spells in spells_known (excluding cantrips)
          ii. OUT: "Choose up to [max_prepared] spells (comma-separated):"
          iii. ⛔ WAIT: new_prepared_list
          iv. VALIDATE: count <= max_prepared AND all spells IN spells_known
          v. IF validation_failed:
               OUT: "⚠️ Invalid preparation (too many or unknown spells)"
               RETURN to step 4h.ii
          vi. UPDATE: Set prepared flag for selected spells, clear others
          vii. OUT: "✓ [character.name] prepared [count] spells"
     i. ELSE:
          OUT: "✓ [character.name] keeping current spell preparation"

   CALL: Time_Tracking_Protocol WITH minutes_to_add=480
   OUT: "=== Long Rest Complete ==="
   UPDATE: party_state
   RETURN
```

## PROTOCOL: Light_Source_Tracking

**TRIGGER**: Time passes
**INPUT**: minutes_elapsed
**GUARD**: none

**PROCEDURE**:
```
1. FOR source IN character.active_light_sources:
     a. DEC: source.remaining_duration by minutes_elapsed
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
