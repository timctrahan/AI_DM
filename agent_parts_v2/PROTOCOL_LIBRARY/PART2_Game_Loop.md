# PROTOCOL LIBRARY - PART 2: GAME LOOP & EXPLORATION

---

[PROTOCOL_START: proto_game_loop]
## PROTOCOL: Game_Loop

**TRIGGER**: Session active (called by proto_game_start)
**GUARD**: session_active AND party_state_valid

**PURPOSE**: Main game loop that delegates to Exploration or Combat and enforces checkpoint validation

**PROCEDURE**:
```yaml
Game_Loop:
  1. SET: player_input_counter = 0

  2. WHILE session_active:
       a. IF party_state.location.in_combat:
            CALL: proto_combat_round
       ELSE:
            CALL: proto_exploration

       b. INC: player_input_counter

       c. CHECKPOINT (every 5 player inputs):
            IF player_input_counter % 5 == 0:
              # This checkpoint is defined in Kernel but reinforced here
              OUTPUT: "(Checkpoint...)" (silent unless issues found)
              # Kernel's Checkpoint_Validation_Protocol handles verification

       d. IF session_end_requested:
            CALL: proto_session_end
            BREAK

  3. RETURN
```

**OUTPUT**: Session continues until player requests end
[PROTOCOL_END: proto_game_loop]

---

[PROTOCOL_START: proto_exploration]
## PROTOCOL: Exploration_Protocol

**TRIGGER**: Not in combat (called by Game_Loop)
**GUARD**: NOT in_combat AND party_conscious

**PURPOSE**: Present location, list actions, handle player choices

**PROCEDURE**:
```yaml
Exploration_Protocol:
  1. RETRIEVE_LOCATION_CONTEXT:
       current_location_id = party_state.location.current
       CALL: Internal_Context_Retrieval(current_location_id)
       # This loads fresh location description, connections, hazards, NPCs, POIs

  2. PRESENT_LOCATION:
       OUTPUT: location.description (brief if already described this session)

       IF location.hazards:
         OUTPUT: "⚠️ Hazards: {list hazards}"

       IF location.npcs_present:
         OUTPUT: "NPCs present: {list names}"

  3. DISPLAY_MANDATORY_HUD:
       GET: active_light = character.active_light_sources[0] IF exists ELSE "None"
       GET: total_rations = SUM(character.survival.provisions FOR character IN party)
       GET: total_water = SUM(character.survival.water FOR character IN party)
       GET: time = party_state.world_state.time_of_day

       OUTPUT: "━━━ 📊 STATUS ━━━"
       OUTPUT: "🕒 Time: Day {day}, {time_of_day}"
       OUTPUT: "🔦 Light: {active_light} | Vision: {light_level}"
       OUTPUT: "🍖 Rations: {total_rations} | 💧 Water: {total_water}"
       OUTPUT: "💰 Gold: {party_gold} gp"
       IF active_effects:
         OUTPUT: "🧙 Effects: {list effects with duration}"
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  4. LIST_AVAILABLE_ACTIONS:
       OUTPUT: "---"

       # Movement options
       FOR direction, connection IN location.connections:
         OUTPUT: "1. Move {direction} to {connection.name}"

       # Investigation options
       IF location.points_of_interest:
         OUTPUT: "2. Investigate {list POI names}"

       # NPC options
       IF location.npcs_present:
         OUTPUT: "3. Talk to {npc_name}"

       # General options
       OUTPUT: "4. Rest (short/long)"
       OUTPUT: "5. Check inventory"
       OUTPUT: "6. View active quests"
       OUTPUT: "X. Something else (describe)"

       OUTPUT: ""
       OUTPUT: "What do you do?"

  5. STOP_AND_WAIT:
       ⛔ WAIT: player_choice

  6. PARSE_INPUT:
       PARSE: action_type, target FROM player_choice

  7. ROUTE_TO_PROTOCOL:
       SWITCH action_type:
         CASE "movement":
           CALL: proto_movement WITH destination
         CASE "investigate":
           CALL: proto_investigation WITH target
         CASE "npc_interaction":
           CALL: proto_npc_interaction WITH npc_id
         CASE "rest":
           CALL: proto_rest WITH rest_type
         CASE "inventory":
           CALL: proto_display_inventory
         CASE "quest_check":
           CALL: proto_display_quest_status
         CASE "shopping":
           CALL: proto_shopping WITH npc_id
         DEFAULT:
           CALL: proto_handle_freeform_action WITH description

  8. UPDATE_STATE:
       # Any state changes from called protocols

  9. CHECK_STATE_VALIDITY:
       # Kernel's validation ensures no negative HP, valid resources

  10. RETURN: to Game_Loop
```

**OUTPUT**: Loops back to Game_Loop after action resolution
[PROTOCOL_END: proto_exploration]

---

[PROTOCOL_START: proto_movement]
## PROTOCOL: Movement_Protocol

**TRIGGER**: Player chooses to move to connected location
**INPUT**: destination (location_id or location_name)
**GUARD**: destination_exists AND destination_connected

**PURPOSE**: Handle party movement between locations

**PROCEDURE**:
```yaml
Movement_Protocol:
  1. RETRIEVE_CURRENT_LOCATION:
       current_location_id = party_state.location.current
       CALL: Internal_Context_Retrieval(current_location_id)

  2. VALIDATE_DESTINATION:
       CHECK: destination IN current_location.connections
       IF NOT valid:
         OUTPUT: "Cannot move to {destination} from here."
         OUTPUT: "Available: {list connections}"
         RETURN

  3. CHECK_RANDOM_ENCOUNTER (optional, based on location):
       # Simplified - full implementation would use encounter tables
       IF current_location.has_encounter_table:
         ROLL: 1d6
         IF roll >= 5:
           # Encounter occurs - combat protocol handles it
           OUTPUT: "⚠️ Encounter!"
           # This would trigger combat, interrupting movement
           RETURN

  4. UPDATE_LOCATION:
       party_state.location.previous = current_location_id
       party_state.location.current = destination_id

       IF destination_id NOT IN party_state.world_state.locations_discovered:
         ADD destination_id TO locations_discovered

  5. TRACK_TIME:
       # Assume 1 hour travel between locations (campaign can customize)
       party_state.world_state.time_minutes += 60
       # Update time_of_day based on minutes

  6. RETRIEVE_NEW_LOCATION:
       CALL: Internal_Context_Retrieval(destination_id)
       # Fresh location data loaded

  7. NARRATE_ARRIVAL:
       OUTPUT: "You travel to {destination.name}."
       OUTPUT: ""
       OUTPUT: destination.description

  8. RETURN: to Exploration_Protocol
```

**OUTPUT**: Party moved to new location, context retrieved
[PROTOCOL_END: proto_movement]

---

[PROTOCOL_START: proto_investigation]
## PROTOCOL: Investigation_Protocol

**TRIGGER**: Player investigates object/area/POI
**INPUT**: target (object name or POI name)
**GUARD**: target_exists AND target_in_reach

**PURPOSE**: Handle skill checks for investigating points of interest

**PROCEDURE**:
```yaml
Investigation_Protocol:
  1. RETRIEVE_LOCATION:
       current_location_id = party_state.location.current
       CALL: Internal_Context_Retrieval(current_location_id)

  2. FIND_TARGET:
       FOR poi IN location.points_of_interest:
         IF poi.name MATCHES target:
           target_object = poi
           BREAK

       IF target_object NOT found:
         OUTPUT: "Cannot find '{target}' here."
         RETURN

  3. CHECK_LIGHTING (if requires sight):
       has_light = ANY(character.active_light_sources) OR location.lighting == "bright"
       is_dark = NOT has_light AND NOT character.darkvision

       IF is_dark:
         OUTPUT: "⚠️ Too dark to see - need light source!"
         RETURN

  4. PERFORM_CHECK (if required):
       IF target_object.requires_check:
         check_type = target_object.check_type (Perception, Investigation, Arcana, etc.)
         DC = target_object.dc

         OUTPUT: "This requires a {check_type} check (DC {DC})."
         OUTPUT: "Roll yourself or let me roll? (self/auto)"
         ⛔ WAIT: roll_choice

         IF roll_choice == "self":
           OUTPUT: "What did you roll? (d20 result)"
           ⛔ WAIT: d20_result
           total = d20_result + character.modifier[check_type]
         ELSE:
           ROLL: d20 + character.modifier[check_type]
           total = roll_result

         OUTPUT: "🎲 {check_type}: {d20} + {modifier} = {total} vs DC {DC}"

         IF total >= DC:
           OUTPUT: target_object.success_info
           success = true
         ELSE:
           OUTPUT: target_object.failure_info
           success = false

  5. HANDLE_OUTCOMES:
       IF target_object.triggers_quest AND success:
         ADD quest_id TO party_state.campaign_state.quests_available
         OUTPUT: "(New quest available: {quest.name})"

       IF target_object.contains_loot AND success:
         CALL: proto_loot_distribution WITH target_object.loot

       IF target_object.quest_progress AND success:
         # Update quest objectives
         FOR quest IN party_state.campaign_state.quests_active:
           IF quest.quest_id == target_object.quest_id:
             ADD objective TO quest.objectives_completed

  6. RETURN: to Exploration_Protocol
```

**OUTPUT**: Investigation resolved, loot/quest updates if applicable
[PROTOCOL_END: proto_investigation]

---

[PROTOCOL_START: proto_npc_interaction]
## PROTOCOL: NPC_Interaction_Protocol

**TRIGGER**: Player interacts with NPC
**INPUT**: npc_id (or npc_name, normalized to npc_id)
**GUARD**: npc_exists AND npc_accessible

**PURPOSE**: Handle dialogue, quests, shop access with NPCs using fresh vault data

**PROCEDURE**:
```yaml
NPC_Interaction_Protocol:
  1. MANDATORY_CONTEXT_RETRIEVAL:
       # This is CRITICAL for V2 - ensures fresh NPC data
       CALL: Internal_Context_Retrieval(npc_id)
       # Loads: personality, goals, dialogue samples, relationships, combat stats

  2. CHECK_REPUTATION:
       FOR npc_rep IN party_state.world_state.reputation.npcs:
         IF npc_rep.npc_id == npc_id:
           reputation = npc_rep.value
           BREAK

       IF reputation NOT found:
         reputation = 0 (neutral)

  3. DETERMINE_ATTITUDE:
       IF reputation <= -5:
         attitude = "hostile"
       ELSE IF reputation <= +1:
         attitude = "neutral"
       ELSE IF reputation <= +5:
         attitude = "friendly"
       ELSE:
         attitude = "beloved"

  4. GENERATE_GREETING:
       # Use NPC's personality traits and dialogue samples from vault
       # Adjust tone based on attitude

       IF npc.dialogue.greeting:
         greeting = npc.dialogue.greeting[attitude]
       ELSE:
         greeting = GENERATE using npc.personality + attitude

       OUTPUT: "> **{npc.name}**: \"{greeting}\""

  5. PRESENT_INTERACTION_OPTIONS:
       OUTPUT: "---"

       IF npc.has_shop:
         OUTPUT: "1. Browse shop"

       IF npc.quests_offered:
         OUTPUT: "2. Ask about available work/quests"

       OUTPUT: "3. Ask a question"
       OUTPUT: "4. End conversation"
       OUTPUT: ""
       OUTPUT: "What do you do?"

       ⛔ WAIT: player_choice

  6. HANDLE_CHOICE:
       SWITCH player_choice:
         CASE "browse_shop" OR "1":
           CALL: proto_shopping WITH npc_id
           RETURN

         CASE "quests" OR "2":
           IF npc.quests_offered:
             OUTPUT: "{npc.name} has these tasks:"
             FOR quest_id IN npc.quests_offered:
               # Retrieve quest summary
               CALL: Internal_Context_Retrieval(quest_id)
               OUTPUT: "- {quest.name}: {quest.brief_description}"

             OUTPUT: "Which quest? (or 'none')"
             ⛔ WAIT: quest_choice

             IF quest_choice != "none":
               CALL: proto_quest_accept WITH quest_id
           ELSE:
             OUTPUT: "> **{npc.name}**: \"I don't have any work for you right now.\""
           RETURN

         CASE "question" OR "3":
           OUTPUT: "What do you ask {npc.name}?"
           ⛔ WAIT: question

           # Generate response using npc.dialogue, npc.personality, world_state
           # This uses fresh NPC data from vault retrieval (step 1)
           response = GENERATE using npc.dialogue + npc.personality + npc.goals

           OUTPUT: "> **{npc.name}**: \"{response}\""

           OUTPUT: "Continue conversation? (yes/no)"
           ⛔ WAIT: continue

           IF continue == "yes":
             GOTO step 5 (present options again)

         CASE "end" OR "4":
           OUTPUT: "> **{npc.name}**: \"{farewell}\""
           RETURN

  7. UPDATE_REPUTATION (if warranted):
       # Certain dialogue choices might modify reputation
       # This would be based on player's responses

  8. RETURN: to Exploration_Protocol
```

**OUTPUT**: NPC interaction completed, potential reputation/quest changes
[PROTOCOL_END: proto_npc_interaction]

---

[PROTOCOL_START: proto_shopping]
## PROTOCOL: Shopping_Protocol

**TRIGGER**: Player accesses merchant
**INPUT**: npc_id (merchant)
**GUARD**: npc.has_shop AND npc_not_hostile

**PURPOSE**: Handle buying/selling items with price modifiers based on reputation

**PROCEDURE**:
```yaml
Shopping_Protocol:
  1. RETRIEVE_NPC:
       CALL: Internal_Context_Retrieval(npc_id)
       # Loads shop inventory, prices

  2. GET_REPUTATION:
       FOR npc_rep IN party_state.world_state.reputation.npcs:
         IF npc_rep.npc_id == npc_id:
           reputation = npc_rep.value
           BREAK

       IF reputation NOT found:
         reputation = 0

  3. CALCULATE_PRICE_MODIFIER:
       # From Kernel reference tables
       IF reputation <= -5:
         price_mod = 2.0 (hostile, 2x prices)
       ELSE IF reputation >= +6:
         price_mod = 0.5 (beloved, half price)
       ELSE IF reputation >= +2:
         price_mod = 0.75 (friendly, 25% off)
       ELSE:
         price_mod = 1.0 (neutral)

  4. DISPLAY_SHOP:
       OUTPUT: "━━━ 💰 {npc.name}'s Shop ━━━"
       OUTPUT: "Reputation: {reputation} → Prices: {price_mod}x"
       OUTPUT: ""

       FOR item IN npc.shop_inventory:
         adjusted_price = item.base_price * price_mod
         OUTPUT: "- {item.name}: {adjusted_price} gp ({item.description})"

       OUTPUT: ""
       OUTPUT: "Your gold: {character.gold} gp"
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━"
       OUTPUT: ""
       OUTPUT: "1. Buy item (specify name)"
       OUTPUT: "2. Sell item (specify name)"
       OUTPUT: "3. Exit shop"
       OUTPUT: ""
       OUTPUT: "What do you do?"

       ⛔ WAIT: shop_choice

  5. HANDLE_TRANSACTION:
       SWITCH shop_choice:
         CASE "buy" OR "1":
           OUTPUT: "Which item?"
           ⛔ WAIT: item_name

           FIND item IN npc.shop_inventory WHERE item.name MATCHES item_name

           IF item NOT found:
             OUTPUT: "{npc.name} doesn't sell that."
             GOTO step 4

           adjusted_price = item.base_price * price_mod

           IF character.gold < adjusted_price:
             OUTPUT: "Not enough gold. ({character.gold} / {adjusted_price} gp)"
             GOTO step 4

           # Check encumbrance
           would_exceed = character.carrying_weight + item.weight > character.capacity

           IF would_exceed:
             OUTPUT: "Cannot carry this item (over capacity)."
             GOTO step 4

           # Complete purchase
           character.gold -= adjusted_price
           ADD item TO character.inventory
           character.carrying_weight += item.weight

           OUTPUT: "💰 {character.name}: {old_gold} - {adjusted_price} = {character.gold} gp"
           OUTPUT: "✓ Purchased {item.name}"

           UPDATE: party_state

           GOTO step 4 (continue shopping)

         CASE "sell" OR "2":
           OUTPUT: "Which item from your inventory?"
           ⛔ WAIT: item_name

           FIND item IN character.inventory WHERE item.name MATCHES item_name

           IF item NOT found:
             OUTPUT: "You don't have that item."
             GOTO step 4

           # Sell price is 50% of base price (adjusted by reputation)
           sell_price = (item.base_price * 0.5) * price_mod

           character.gold += sell_price
           REMOVE item FROM character.inventory
           character.carrying_weight -= item.weight

           OUTPUT: "💰 {character.name}: {old_gold} + {sell_price} = {character.gold} gp"
           OUTPUT: "✓ Sold {item.name}"

           UPDATE: party_state

           GOTO step 4 (continue shopping)

         CASE "exit" OR "3":
           OUTPUT: "> **{npc.name}**: \"Come back anytime!\""
           RETURN to Exploration_Protocol

  6. RETURN: to Exploration_Protocol
```

**OUTPUT**: Shopping session completed, inventory/gold updated
[PROTOCOL_END: proto_shopping]

---

[PROTOCOL_START: proto_rest]
## PROTOCOL: Rest_Protocol

**TRIGGER**: Player chooses to rest
**INPUT**: rest_type ("short" | "long")
**GUARD**: party_not_in_immediate_danger

**PURPOSE**: Delegate to short or long rest protocols

**PROCEDURE**:
```yaml
Rest_Protocol:
  1. VALIDATE_REST_TYPE:
       IF rest_type == "short":
         CALL: proto_rest_short
       ELSE IF rest_type == "long":
         CALL: proto_rest_long
       ELSE:
         OUTPUT: "Invalid rest type. Choose 'short' or 'long'."
         RETURN

  2. CHECK_ENCOUNTER (optional):
       # Simplified - full version uses location encounter tables
       IF location.unsafe_rest:
         ROLL: 1d6
         IF roll == 6:
           OUTPUT: "⚠️ Rest interrupted by encounter!"
           # Combat would initiate, rest fails
           RETURN

  3. RETURN: to Exploration_Protocol
```

**OUTPUT**: Rest completed (via short/long rest protocol)
[PROTOCOL_END: proto_rest]

---

[PROTOCOL_START: proto_display_inventory]
## PROTOCOL: Display_Inventory_Protocol

**TRIGGER**: Player requests inventory display
**GUARD**: None

**PURPOSE**: Show character inventory, encumbrance, resources

**PROCEDURE**:
```yaml
Display_Inventory_Protocol:
  FOR character IN party_state.characters:
    OUTPUT: "━━━ 🎒 {character.name}'s INVENTORY ━━━"
    OUTPUT: "Gold: {character.gold} gp"
    OUTPUT: "Carrying: {character.carrying_weight} / {capacity} lbs"
    OUTPUT: ""
    OUTPUT: "Equipped:"
    FOR item IN character.inventory.equipment WHERE item.equipped:
      OUTPUT: "- {item.name} ({item.type})"
    OUTPUT: ""
    OUTPUT: "Carried:"
    FOR item IN character.inventory.equipment WHERE NOT item.equipped:
      OUTPUT: "- {item.name} ({item.weight} lbs)"
    OUTPUT: ""
    OUTPUT: "Provisions: {character.survival.provisions} days"
    OUTPUT: "Water: {character.survival.water} days"
    OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  RETURN: to Exploration_Protocol
```

**OUTPUT**: Inventory displayed
[PROTOCOL_END: proto_display_inventory]

---

[PROTOCOL_START: proto_display_quest_status]
## PROTOCOL: Display_Quest_Status_Protocol

**TRIGGER**: Player requests quest status
**GUARD**: None

**PURPOSE**: Show active, completed, and available quests

**PROCEDURE**:
```yaml
Display_Quest_Status_Protocol:
  OUTPUT: "━━━ 📜 QUEST LOG ━━━"
  OUTPUT: ""

  IF party_state.campaign_state.quests_active:
    OUTPUT: "ACTIVE QUESTS:"
    FOR quest IN quests_active:
      # Retrieve quest details
      CALL: Internal_Context_Retrieval(quest.quest_id)

      OUTPUT: "- {quest.name}"
      OUTPUT: "  {quest.brief_description}"
      OUTPUT: "  Objectives:"
      FOR objective IN quest.objectives:
        IF objective IN quest.objectives_completed:
          OUTPUT: "    ✓ {objective}"
        ELSE:
          OUTPUT: "    ☐ {objective}"
    OUTPUT: ""

  IF party_state.campaign_state.quests_completed:
    OUTPUT: "COMPLETED QUESTS:"
    FOR quest_id IN quests_completed:
      CALL: Internal_Context_Retrieval(quest_id)
      OUTPUT: "- {quest.name}"
    OUTPUT: ""

  IF party_state.campaign_state.quests_available:
    OUTPUT: "AVAILABLE QUESTS:"
    FOR quest_id IN quests_available:
      CALL: Internal_Context_Retrieval(quest_id)
      OUTPUT: "- {quest.name} (from {quest.quest_giver})"
    OUTPUT: ""

  OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  RETURN: to Exploration_Protocol
```

**OUTPUT**: Quest log displayed
[PROTOCOL_END: proto_display_quest_status]

---

[PROTOCOL_START: proto_handle_freeform_action]
## PROTOCOL: Handle_Freeform_Action

**TRIGGER**: Player describes custom action not in menu
**INPUT**: action_description (string)
**GUARD**: None

**PURPOSE**: Handle creative player actions not covered by standard protocols

**PROCEDURE**:
```yaml
Handle_Freeform_Action:
  1. PARSE_INTENT:
       # Determine what the player is trying to do
       # Examples: "I climb the wall", "I intimidate the guard", "I search for traps"

  2. DETERMINE_RESOLUTION:
       IF action requires skill check:
         skill = IDENTIFY skill type (Athletics, Stealth, Persuasion, etc.)
         DC = ESTIMATE difficulty (easy 10, medium 15, hard 20, very hard 25)

         OUTPUT: "This requires a {skill} check (DC {DC})."
         OUTPUT: "Roll yourself or let me roll? (self/auto)"
         ⛔ WAIT: roll_choice

         RESOLVE roll (same as Investigation_Protocol step 4)

         OUTPUT: result based on success/failure

       ELSE IF action is narrative/roleplay:
         # No check needed, just narrate outcome
         OUTPUT: description of what happens

       ELSE IF action triggers combat:
         OUTPUT: "⚔️ This initiates combat!"
         CALL: proto_combat_init WITH enemies
         RETURN

  3. UPDATE_STATE (if applicable):
       # Some actions might change location, trigger quests, etc.

  4. RETURN: to Exploration_Protocol
```

**OUTPUT**: Freeform action resolved
[PROTOCOL_END: proto_handle_freeform_action]

---

## END OF PART 2: GAME LOOP & EXPLORATION
