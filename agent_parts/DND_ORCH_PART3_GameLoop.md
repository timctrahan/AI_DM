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
     a. GET: relevant_dialogue FROM npc.dialogue
     b. GENERATE: response based on personality + reputation + world_state
     c. OUT: response
     d. PROMPT: "Ask another question? (describe)"
     e. ⛔ WAIT: input
     f. IF input != "no" AND != "done" THEN
          GOTO step 6

7. UPDATE: world_state.reputation IF interaction warrants
8. RETURN to Exploration_Protocol
```

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

3. OUT: "=== Short Rest Complete ==="
4. UPDATE: party_state
5. RETURN
```

## PROTOCOL: Long_Rest_Protocol

**TRIGGER**: Long rest initiated  
**GUARD**: none

**PROCEDURE**:
```
1. OUT: "=== Long Rest (8 hours) ==="

2. FOR character IN party_state.characters:
     a. SET: character.hp_current = character.hp_max
     b. RESTORE: character.hit_dice_remaining = max(1, total/2)
     c. RESTORE: ALL spell slots to max
     d. RESTORE: ALL class_resources that reset on long rest
     e. CLEAR: exhaustion level (reduce by 1)
     f. OUT: "✓ [Name]: Fully rested (HP: [max], resources restored)"

3. INC: party_state.world_state.time_elapsed by 1 day

4. OUT: "=== Long Rest Complete ==="
5. UPDATE: party_state
6. RETURN
```
