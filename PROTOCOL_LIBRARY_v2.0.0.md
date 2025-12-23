# PROTOCOL LIBRARY v2.0.0
# D&D 5E AI Orchestrator - Gameplay Protocols

**DO NOT EDIT DURING SESSION** - This is a read-only reference file for the AI Orchestrator

**PURPOSE**: Contains all gameplay logic protocols in indexed, retrievable format

**ASSEMBLY DATE**: 2025-12-19 21:23:20

---

[PROTOCOL_INDEX]
session_management:
  - proto_session_init
  - proto_new_session_flow
  - proto_character_creation_flow
  - proto_session_resume
  - proto_character_import_flow
  - proto_state_validation
  - proto_state_recovery
  - proto_combat_init
  - proto_session_end
game_loop:
  - proto_game_loop
  - proto_exploration
  - proto_movement
  - proto_investigation
  - proto_npc_interaction
combat:
  - proto_combat_round
  - proto_attack_action
  - proto_death_saves
  - proto_combat_end
progression:
  - proto_display_quest_status
  - proto_xp_award
  - proto_level_up
  - proto_quest_accept
  - proto_quest_completion
  - proto_loot_distribution
  - proto_reputation_change
utilities:
  - proto_shopping
  - proto_rest
  - proto_display_inventory
  - proto_rest_short
  - proto_rest_long
meta:
  - proto_game_start
  - proto_handle_freeform_action
  - proto_player_turn
  - proto_enemy_turn
  - proto_asi_or_feat
  - proto_encumbrance_check
  - proto_cast_spell
  - proto_use_item

---

# ============================================================
# SOURCE: PART1_Session_Management.md
# ============================================================

# PROTOCOL LIBRARY - PART 1: SESSION MANAGEMENT

---

[PROTOCOL_START: proto_session_init]
## PROTOCOL: Session_Initialization

**TRIGGER**: First user input contains "Initialize session" or "Start new session"
**GUARD**: No active session state

**PURPOSE**: Bootstrap a new game session from scratch

**PROCEDURE**:
```yaml
Session_Initialization:
  1. VERIFY_PREREQUISITES:
       - Kernel loaded (in system prompt)
       - Protocol Library present (search for [PROTOCOL_INDEX])
       - Campaign Data Vault present (search for [MASTER_INDEX])

       IF any missing:
         OUTPUT: "⛔ INITIALIZATION FAILED"
         OUTPUT: "Missing: {list missing components}"
         OUTPUT: "Required: Kernel (system prompt), Protocol Library, Campaign Data Vault"
         HALT

  2. PARSE_INDEXES:
       a. Search for "[PROTOCOL_INDEX]"
       b. Extract list of all available protocol_ids
       c. LOG: "Protocol Library indexed ({count} protocols found)"

       d. Search for "[MASTER_INDEX]"
       e. Extract list of all available module_ids (NPCs, locations, quests)
       f. LOG: "Campaign Data Vault indexed ({count} modules found)"

  3. DETERMINE_SESSION_TYPE:
       OUTPUT: "Session Initialization"
       OUTPUT: "Select session type:"
       OUTPUT: "1. New Campaign (create new characters)"
       OUTPUT: "2. Resume Existing Session (load party state)"
       OUTPUT: "3. Import Characters (use existing character JSONs)"
       OUTPUT: ""
       OUTPUT: "What do you do?"
       ⛔ WAIT: player_choice

  4. ROUTE_TO_PROTOCOL:
       SWITCH player_choice:
         CASE 1: CALL proto_new_session_flow
         CASE 2: CALL proto_session_resume
         CASE 3: CALL proto_character_import_flow
         DEFAULT:
           OUTPUT: "Invalid choice. Please select 1, 2, or 3."
           RETURN to step 3
```

**OUTPUT**: Session initialized, routed to appropriate sub-protocol
[PROTOCOL_END: proto_session_init]

---

[PROTOCOL_START: proto_new_session_flow]
## PROTOCOL: New_Session_Flow

**TRIGGER**: Called by Session_Initialization (choice 1)
**GUARD**: session_initialized

**PURPOSE**: Create new party from scratch

**PROCEDURE**:
```yaml
New_Session_Flow:
  1. INITIALIZE_EMPTY_PARTY_STATE:
       party_state = {
         characters: [],
         shared_inventory: {gold: 0, items: []},
         location: {current: null, region: null},
         world_state: {day: 1, time: "morning", weather: "clear"},
         flags: {},
         active_quests: []
       }

  2. DETERMINE_PARTY_SIZE:
       OUTPUT: "How many characters in your party? (1-6 recommended)"
       ⛔ WAIT: party_size

       VALIDATE: 1 <= party_size <= 8
       IF invalid:
         OUTPUT: "Please choose 1-8 characters"
         RETURN to step 2

  3. CREATE_CHARACTERS:
       FOR i = 1 TO party_size:
         OUTPUT: "Creating character {i} of {party_size}..."
         CALL: proto_character_creation_flow
         # This will return a complete Character_Schema_v2 object
         ADD: returned_character TO party_state.characters

  4. RETRIEVE_CAMPAIGN_START:
       # Load the campaign overview to get starting location
       CALL: Internal_Context_Retrieval("_campaign_overview")
       # OR if act-specific: Internal_Context_Retrieval("_act1_overview")

       EXTRACT: starting_location_id FROM overview.start_location
       EXTRACT: starting_gold FROM overview.starting_wealth (default: 50 gp per character)

  5. SET_STARTING_CONDITIONS:
       party_state.location.current = starting_location_id
       party_state.shared_inventory.gold = starting_gold * party_size

       FOR EACH character IN party_state.characters:
         # Set starting HP to max
         character.current_hp = character.max_hp
         # Full spell slots
         character.spell_slots_current = character.spell_slots_max
         # Full resources
         character.class_resources_current = character.class_resources_max

  6. OUTPUT_PARTY_SUMMARY:
       OUTPUT: "━━━ PARTY CREATED ━━━"
       FOR EACH character:
         OUTPUT: "- {name}: {race} {class} (Level {level})"
         OUTPUT: "  HP: {max_hp} | AC: {ac} | Gold: {starting_gold} gp"
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━"

  7. CALL: proto_game_start
       # This will load starting location and begin exploration
```

**OUTPUT**: Complete party_state ready for gameplay
[PROTOCOL_END: proto_new_session_flow]

---

[PROTOCOL_START: proto_character_creation_flow]
## PROTOCOL: Character_Creation_Flow

**TRIGGER**: Called by New_Session_Flow for each character
**GUARD**: None (self-contained)

**PURPOSE**: Create a single character using D&D 5E rules

**PROCEDURE**:
```yaml
Character_Creation_Flow:
  # Note: This is a simplified version. Full implementation should support:
  # - Standard array, point buy, or rolling stats
  # - Equipment packages
  # - Spell selection for casters
  # - Background features

  1. GET_BASIC_INFO:
       OUTPUT: "Character Creation"
       OUTPUT: "Name:"
       ⛔ WAIT: name

       OUTPUT: "Race: (human, elf, dwarf, halfling, dragonborn, etc.)"
       ⛔ WAIT: race

       OUTPUT: "Class: (fighter, wizard, rogue, cleric, etc.)"
       ⛔ WAIT: class

       OUTPUT: "Level: (1-20, typically start at 1)"
       ⛔ WAIT: level

  2. GET_ABILITY_SCORES:
       OUTPUT: "Ability Score Method:"
       OUTPUT: "1. Standard Array (15, 14, 13, 12, 10, 8)"
       OUTPUT: "2. Point Buy (27 points)"
       OUTPUT: "3. Manual Entry (you provide all 6 scores)"
       ⛔ WAIT: method_choice

       SWITCH method_choice:
         CASE 1:
           OUTPUT: "Assign standard array to abilities (STR, DEX, CON, INT, WIS, CHA):"
           OUTPUT: "Example: 15,10,14,8,12,13"
           ⛔ WAIT: assignment
           PARSE: scores FROM assignment

         CASE 2:
           # Point buy logic (could be detailed or simplified)
           OUTPUT: "Point Buy not implemented yet. Use Manual Entry."
           # Fall through to case 3

         CASE 3:
           OUTPUT: "Enter six ability scores (STR,DEX,CON,INT,WIS,CHA):"
           OUTPUT: "Example: 16,14,15,8,10,12"
           ⛔ WAIT: scores_input
           PARSE: scores FROM scores_input

  3. APPLY_RACIAL_MODIFIERS:
       # Retrieve race data to get ability score bonuses
       # This is simplified - ideally would retrieve from a race module

       # Example hardcoded (real version should use data):
       IF race == "human":
         ADD 1 to all ability scores
       ELSE IF race == "dwarf":
         ADD 2 to CON
       # ... etc

       OUTPUT: "Racial bonuses applied: {list bonuses}"

  4. CALCULATE_DERIVED_STATS:
       # Hit Points
       CALL: Internal_Context_Retrieval("table_class_hit_dice")
       # Would contain: fighter=d10, wizard=d6, etc.

       hit_die = class_hit_dice[class]

       IF level == 1:
         max_hp = hit_die_max_value + con_modifier
       ELSE:
         # For simplicity, use average HP on level up
         # Real version could ask player to roll or use average
         max_hp = hit_die_max_value + (level - 1) * (hit_die_average + con_modifier) + con_modifier

       # Armor Class (requires equipment choice - simplified)
       OUTPUT: "Starting Equipment/Armor:"
       OUTPUT: "Choose AC calculation method:"
       OUTPUT: "1. Light Armor (AC = 12 + DEX mod)"
       OUTPUT: "2. Medium Armor (AC = 14 + DEX mod, max +2)"
       OUTPUT: "3. Heavy Armor (AC = 16, no DEX)"
       OUTPUT: "4. Unarmored (AC = 10 + DEX mod)"
       ⛔ WAIT: armor_choice

       CALCULATE: ac BASED ON armor_choice and dex_modifier

       # Proficiency Bonus
       proficiency = FLOOR((level - 1) / 4) + 2

       # Initiative
       initiative = dex_modifier

  5. BUILD_CHARACTER_OBJECT:
       character = {
         name: name,
         level: level,
         class: class,
         race: race,

         ability_scores: {
           str: str_score, dex: dex_score, con: con_score,
           int: int_score, wis: wis_score, cha: cha_score
         },

         ability_modifiers: {
           str: FLOOR((str - 10) / 2),
           dex: FLOOR((dex - 10) / 2),
           # ... etc for all 6
         },

         max_hp: max_hp,
         current_hp: max_hp,
         temp_hp: 0,

         ac: ac,
         initiative: initiative,
         speed: 30,  # Could vary by race
         proficiency_bonus: proficiency,

         hit_dice: {
           type: hit_die,
           total: level,
           remaining: level
         },

         death_saves: {successes: 0, failures: 0},

         conditions: [],
         exhaustion: 0,

         equipment: {
           weapons: [],
           armor: [],
           items: []
         },

         gold: 0,  # Set by New_Session_Flow

         spells_known: [],  # Populated if caster
         spell_slots_max: {},  # Populated if caster
         spell_slots_current: {},

         features: [],  # Class and racial features

         personality: "",  # Optional RP info
         backstory: ""
       }

  6. OFFER_CUSTOMIZATION:
       OUTPUT: "Character basics created:"
       OUTPUT: "{name} - Level {level} {race} {class}"
       OUTPUT: "HP: {max_hp} | AC: {ac} | Proficiency: +{proficiency}"
       OUTPUT: ""
       OUTPUT: "Add personality/backstory? (y/n)"
       ⛔ WAIT: add_rp

       IF add_rp == "y":
         OUTPUT: "Personality traits/ideals/bonds/flaws (optional):"
         ⛔ WAIT: personality_input
         character.personality = personality_input

         OUTPUT: "Backstory (optional):"
         ⛔ WAIT: backstory_input
         character.backstory = backstory_input

  7. RETURN: character
```

**OUTPUT**: Complete Character_Schema_v2 object
[PROTOCOL_END: proto_character_creation_flow]

---

[PROTOCOL_START: proto_session_resume]
## PROTOCOL: Session_Resume

**TRIGGER**: Called by Session_Initialization (choice 2)
**GUARD**: session_initialized

**PURPOSE**: Load existing party state from previous session

**PROCEDURE**:
```yaml
Session_Resume:
  1. REQUEST_PARTY_STATE:
       OUTPUT: "Session Resume"
       OUTPUT: "Please paste your complete Party State JSON from previous session."
       OUTPUT: "(This was provided at the end of your last session)"
       ⛔ WAIT: party_state_json

  2. PARSE_AND_VALIDATE:
       TRY:
         party_state = PARSE_JSON(party_state_json)
       CATCH:
         OUTPUT: "⛔ Invalid JSON format"
         OUTPUT: "Please ensure you copied the entire JSON object"
         RETURN to step 1

  3. VALIDATE_STATE_INTEGRITY:
       CALL: proto_state_validation WITH party_state
       # This protocol checks for negative HP, invalid spell slots, etc.

       IF validation_fails:
         OUTPUT: "⚠️ State validation found issues:"
         OUTPUT: "{list all validation errors}"
         OUTPUT: "Attempt to auto-correct? (y/n)"
         ⛔ WAIT: auto_correct

         IF auto_correct == "y":
           CALL: proto_state_recovery WITH party_state
           # Fixes common issues (clamp HP to valid range, etc.)
         ELSE:
           OUTPUT: "Please manually correct the JSON and try again"
           RETURN to step 1

  4. TRIGGER_RESUME_SAFEGUARD:
       # This is also in the Kernel, but we reinforce it here
       OUTPUT: "⚠️ SESSION RESUMING - Verifying integrity..."

       FOR EACH character IN party_state.characters:
         OUTPUT: "- {name}: {current_hp}/{max_hp} HP | {class} Lvl {level}"
         IF character.conditions NOT empty:
           OUTPUT: "  Conditions: {list conditions}"

       OUTPUT: "Location: {party_state.location.current}"
       OUTPUT: "In Combat: {party_state.location.in_combat}"
       OUTPUT: "Active Quests: {count party_state.active_quests}"

  5. REMIND_CORE_RULES:
       OUTPUT: ""
       OUTPUT: "⚠️ CORE RULES REMINDER:"
       OUTPUT: "- I ALWAYS present options and ⛔ STOP"
       OUTPUT: "- I NEVER act without your input"
       OUTPUT: "- I retrieve fresh data for all indexed entities"
       OUTPUT: "- I track ALL resources precisely"
       OUTPUT: "- Checkpoint validates every 5 turns"

  6. CONFIRM_READY:
       OUTPUT: ""
       OUTPUT: "Ready to continue? Any corrections needed?"
       ⛔ WAIT: ready_input

       IF ready_input contains corrections:
         # Parse and apply manual corrections
         OUTPUT: "Applying corrections..."
         # (Implementation depends on correction format)

  7. RETRIEVE_LOCATION_CONTEXT:
       current_location_id = party_state.location.current
       CALL: Internal_Context_Retrieval(current_location_id)
       # Load fresh location data

  8. BEGIN_GAME:
       IF party_state.location.in_combat:
         OUTPUT: "Resuming combat..."
         CALL: proto_combat_resume  # Special combat resume logic
       ELSE:
         OUTPUT: "Resuming exploration..."
         CALL: proto_exploration  # Normal exploration flow
```

**OUTPUT**: Session resumed with validated party state
[PROTOCOL_END: proto_session_resume]

---

[PROTOCOL_START: proto_character_import_flow]
## PROTOCOL: Character_Import_Flow

**TRIGGER**: Called by Session_Initialization (choice 3)
**GUARD**: session_initialized

**PURPOSE**: Import pre-made characters (e.g., from D&D Beyond, previous campaigns)

**PROCEDURE**:
```yaml
Character_Import_Flow:
  1. INITIALIZE_PARTY:
       party_state = {
         characters: [],
         shared_inventory: {gold: 0, items: []},
         location: {current: null, region: null},
         world_state: {day: 1, time: "morning", weather: "clear"},
         flags: {},
         active_quests: []
       }

  2. DETERMINE_IMPORT_COUNT:
       OUTPUT: "How many characters to import? (1-6)"
       ⛔ WAIT: import_count

       VALIDATE: 1 <= import_count <= 8

  3. IMPORT_EACH_CHARACTER:
       FOR i = 1 TO import_count:
         OUTPUT: "Importing character {i} of {import_count}..."
         OUTPUT: "Paste complete Character JSON:"
         ⛔ WAIT: character_json

         TRY:
           character = PARSE_JSON(character_json)
         CATCH:
           OUTPUT: "⛔ Invalid JSON format"
           OUTPUT: "Retry import for this character? (y/n)"
           ⛔ WAIT: retry

           IF retry == "y":
             CONTINUE (retry this iteration)
           ELSE:
             SKIP this character

         # Validate character schema
         CALL: proto_validate_character_schema WITH character

         IF valid:
           ADD character TO party_state.characters
           OUTPUT: "✓ Imported: {character.name}"
         ELSE:
           OUTPUT: "⛔ Invalid character schema"
           OUTPUT: "Retry? (y/n)"
           ⛔ WAIT: retry
           IF retry == "y": CONTINUE

  4. SET_STARTING_LOCATION:
       # Same as New_Session_Flow
       CALL: Internal_Context_Retrieval("_campaign_overview")
       EXTRACT: starting_location_id
       party_state.location.current = starting_location_id

  5. CALL: proto_game_start
```

**OUTPUT**: Party created from imported characters
[PROTOCOL_END: proto_character_import_flow]

---

[PROTOCOL_START: proto_game_start]
## PROTOCOL: Game_Start

**TRIGGER**: Called after party creation/import, before first exploration turn
**GUARD**: party_state.characters NOT empty

**PURPOSE**: Load campaign start and begin exploration

**PROCEDURE**:
```yaml
Game_Start:
  1. RETRIEVE_CAMPAIGN_INTRO:
       # Load the campaign or act intro narrative
       CALL: Internal_Context_Retrieval("_campaign_intro")
       # OR: Internal_Context_Retrieval("_act1_intro")

  2. NARRATE_OPENING:
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
       OUTPUT: intro.title
       OUTPUT: intro.narrative
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

  3. RETRIEVE_STARTING_LOCATION:
       starting_location_id = party_state.location.current
       CALL: Internal_Context_Retrieval(starting_location_id)

  4. SET_SESSION_ACTIVE:
       session_active = true
       player_input_counter = 0  # For checkpoint tracking

  5. BEGIN_GAME_LOOP:
       CALL: proto_game_loop
       # This is the main game loop protocol (from Part 2)
```

**OUTPUT**: Game session started, exploration begins
[PROTOCOL_END: proto_game_start]

---

[PROTOCOL_START: proto_state_validation]
## PROTOCOL: State_Validation

**TRIGGER**: Called during session resume or checkpoint
**GUARD**: None (utility protocol)

**PURPOSE**: Verify party state has no corrupted data

**INPUT**: `party_state` object

**PROCEDURE**:
```yaml
State_Validation:
  errors = []

  FOR EACH character IN party_state.characters:
    # HP validation
    IF character.current_hp < 0:
      ADD "character.current_hp < 0 for {name}" TO errors

    IF character.current_hp > character.max_hp:
      ADD "{name}.current_hp exceeds max_hp" TO errors

    # Spell slot validation
    FOR EACH spell_level IN character.spell_slots_current:
      IF current > character.spell_slots_max[spell_level]:
        ADD "{name} spell slots level {spell_level} exceeds max" TO errors

    # Gold validation (individual gold, if tracked per-character)
    IF character.gold < 0:
      ADD "{name}.gold is negative" TO errors

    # Ability score validation
    FOR EACH ability IN character.ability_scores:
      IF score < 1 OR score > 30:
        ADD "{name}.{ability} is out of valid range (1-30)" TO errors

  # Party-level validations
  IF party_state.shared_inventory.gold < 0:
    ADD "Party gold is negative" TO errors

  IF party_state.location.current == null OR party_state.location.current == "":
    ADD "Party location is null/empty" TO errors

  # Return result
  IF errors NOT empty:
    RETURN: {valid: false, errors: errors}
  ELSE:
    RETURN: {valid: true}
```

**OUTPUT**: Validation result with list of errors (if any)
[PROTOCOL_END: proto_state_validation]

---

[PROTOCOL_START: proto_state_recovery]
## PROTOCOL: State_Recovery

**TRIGGER**: Called when state validation fails or corruption detected
**GUARD**: None (recovery protocol)

**PURPOSE**: Attempt automatic correction of common state issues

**INPUT**: `party_state` object

**PROCEDURE**:
```yaml
State_Recovery:
  corrections_applied = []

  FOR EACH character IN party_state.characters:
    # Clamp HP to valid range
    IF character.current_hp < 0:
      character.current_hp = 0
      ADD "Set {name}.current_hp to 0 (was negative)" TO corrections_applied

    IF character.current_hp > character.max_hp:
      character.current_hp = character.max_hp
      ADD "Clamped {name}.current_hp to max_hp" TO corrections_applied

    # Clamp spell slots
    FOR EACH spell_level IN character.spell_slots_current:
      IF current > max:
        character.spell_slots_current[spell_level] = character.spell_slots_max[spell_level]
        ADD "Clamped {name} spell slots level {spell_level}" TO corrections_applied

    # Fix negative gold
    IF character.gold < 0:
      character.gold = 0
      ADD "Set {name}.gold to 0 (was negative)" TO corrections_applied

  # Fix party gold
  IF party_state.shared_inventory.gold < 0:
    party_state.shared_inventory.gold = 0
    ADD "Set party gold to 0 (was negative)" TO corrections_applied

  # Fix null location (set to default safe location)
  IF party_state.location.current == null:
    party_state.location.current = "loc_starting_area"  # Fallback
    ADD "Set location to default (was null)" TO corrections_applied

  OUTPUT: "State recovery completed:"
  FOR EACH correction IN corrections_applied:
    OUTPUT: "- {correction}"

  RETURN: party_state  # Corrected version
```

**OUTPUT**: Corrected party_state object
[PROTOCOL_END: proto_state_recovery]

---

## END OF PART 1: SESSION MANAGEMENT


---

# ============================================================
# SOURCE: PART2_Game_Loop.md
# ============================================================

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


---

# ============================================================
# SOURCE: PART3_Combat.md
# ============================================================

# PROTOCOL LIBRARY - PART 3: COMBAT

---

[PROTOCOL_START: proto_combat_init]
## PROTOCOL: Combat_Initiation_Protocol

**TRIGGER**: Combat begins (player attacks, enemy ambush, etc.)
**INPUT**: enemies (list of enemy objects from encounter or campaign vault)
**GUARD**: party_conscious

**PURPOSE**: Initialize combat, roll initiative, set up turn order

**PROCEDURE**:
```yaml
Combat_Initiation_Protocol:
  1. ANNOUNCE_COMBAT:
       OUTPUT: "⚔️ COMBAT INITIATED!"
       OUTPUT: ""

  2. ROLL_INITIATIVE:
       initiative_order = []

       FOR character IN party_state.characters:
         ROLL: d20 + character.initiative_bonus
         OUTPUT: "🎲 {character.name} Initiative: {d20} + {bonus} = {total}"
         ADD: {name: character.name, initiative: total, is_enemy: false, hp: character.hp_current, hp_max: character.hp_max} TO initiative_order

       FOR enemy IN enemies:
         ROLL: d20 + enemy.initiative_bonus
         OUTPUT: "🎲 {enemy.name} Initiative: {d20} + {bonus} = {total}"
         ADD: {name: enemy.name, initiative: total, is_enemy: true, hp: enemy.hp_max, hp_max: enemy.hp_max} TO initiative_order

  3. SORT_INITIATIVE:
       SORT initiative_order BY initiative DESC (highest first)

  4. DISPLAY_TURN_ORDER:
       OUTPUT: ""
       OUTPUT: "━━━ TURN ORDER ━━━"
       FOR combatant IN initiative_order:
         OUTPUT: "{combatant.initiative}: {combatant.name}"
       OUTPUT: "━━━━━━━━━━━━━━━━━━━"

  5. SET_COMBAT_STATE:
       party_state.location.in_combat = true
       party_state.combat_state.active = true
       party_state.combat_state.round = 1
       party_state.combat_state.initiative_order = initiative_order
       party_state.combat_state.current_turn = initiative_order[0].name

  6. CALL: proto_combat_round

  7. RETURN
```

**OUTPUT**: Combat initialized, first round begins
[PROTOCOL_END: proto_combat_init]

---

[PROTOCOL_START: proto_combat_round]
## PROTOCOL: Combat_Round_Protocol

**TRIGGER**: Called by Combat_Init or end of previous round
**GUARD**: combat_active

**PURPOSE**: Manage turn order within a combat round

**PROCEDURE**:
```yaml
Combat_Round_Protocol:
  1. CHECK_COMBAT_END:
       all_enemies_dead = ALL(combatant WHERE is_enemy AND hp <= 0)
       all_party_dead = ALL(combatant WHERE NOT is_enemy AND hp <= 0)

       IF all_enemies_dead OR all_party_dead:
         CALL: proto_combat_end
         RETURN

  2. DISPLAY_ROUND_START (if new round):
       OUTPUT: "━━━ ROUND {party_state.combat_state.round} ━━━"

  3. PROCESS_TURNS:
       FOR combatant IN party_state.combat_state.initiative_order:
         IF combatant.hp <= 0:
           SKIP (dead/unconscious)

         party_state.combat_state.current_turn = combatant.name

         IF combatant.is_enemy:
           CALL: proto_enemy_turn WITH combatant
         ELSE:
           CALL: proto_player_turn WITH combatant

         CHECK: combat still active (might end mid-round)
         IF NOT combat_active:
           RETURN

  4. INCREMENT_ROUND:
       party_state.combat_state.round += 1

  5. LOOP:
       CALL: proto_combat_round (recursive until combat ends)

  6. RETURN
```

**OUTPUT**: All combatants take turns, round ends
[PROTOCOL_END: proto_combat_round]

---

[PROTOCOL_START: proto_player_turn]
## PROTOCOL: Player_Combat_Turn_Protocol

**TRIGGER**: Player's turn in combat
**INPUT**: character (combatant object)
**GUARD**: character_conscious

**PURPOSE**: Handle player's combat actions (attack, cast spell, use item, etc.)

**PROCEDURE**:
```yaml
Player_Combat_Turn_Protocol:
  1. ANNOUNCE_TURN:
       OUTPUT: ""
       OUTPUT: "━━━ {character.name}'s TURN ━━━"
       OUTPUT: "❤️ HP: {character.hp_current}/{character.hp_max}"
       IF character.conditions:
         OUTPUT: "🧙 Conditions: {list conditions}"

  2. DISPLAY_ACTIONS:
       OUTPUT: "---"
       OUTPUT: "1. Attack with weapon"
       OUTPUT: "2. Cast a spell"
       OUTPUT: "3. Use an item"
       OUTPUT: "4. Dash / Disengage / Dodge / Help"
       OUTPUT: "5. Other (describe)"
       OUTPUT: ""
       OUTPUT: "What does {character.name} do?"

       ⛔ WAIT: action_choice

  3. RESOLVE_ACTION:
       SWITCH action_choice:
         CASE "attack" OR "1":
           CALL: proto_attack_action WITH character
         CASE "spell" OR "2":
           CALL: proto_cast_spell WITH character
         CASE "item" OR "3":
           CALL: proto_use_item WITH character
         CASE "dash" OR "disengage" OR "dodge" OR "help":
           OUTPUT: "{character.name} uses {action}."
           # Narrate effect
         DEFAULT:
           OUTPUT: "Describe what {character.name} does:"
           ⛔ WAIT: custom_action
           # Resolve based on description

  4. CHECK_REACTIONS:
       # If enemy attacks this character later, opportunity for Shield spell, etc.
       character.reaction_available = true

  5. END_TURN:
       OUTPUT: "--- {character.name}'s turn ends ---"

  6. RETURN
```

**OUTPUT**: Player's turn completed
[PROTOCOL_END: proto_player_turn]

---

[PROTOCOL_START: proto_attack_action]
## PROTOCOL: Attack_Action_Protocol

**TRIGGER**: Player attacks in combat
**INPUT**: character (attacker)
**GUARD**: character has weapon or unarmed

**PURPOSE**: Resolve attack rolls, damage, update enemy HP

**PROCEDURE**:
```yaml
Attack_Action_Protocol:
  1. SELECT_WEAPON:
       OUTPUT: "Attack with:"
       FOR weapon IN character.inventory.equipment WHERE type == "weapon":
         OUTPUT: "- {weapon.name} ({weapon.damage})"
       ⛔ WAIT: weapon_choice

  2. SELECT_TARGET:
       OUTPUT: "Target:"
       FOR enemy IN combat_state.initiative_order WHERE is_enemy AND hp > 0:
         OUTPUT: "- {enemy.name} (AC {enemy.ac}, HP {enemy.hp}/{enemy.hp_max})"
       ⛔ WAIT: target_choice

  3. ROLL_ATTACK:
       OUTPUT: "Roll attack or auto? (self/auto)"
       ⛔ WAIT: roll_choice

       IF roll_choice == "self":
         OUTPUT: "What did you roll? (d20 result)"
         ⛔ WAIT: d20_result
         attack_roll = d20_result
       ELSE:
         ROLL: d20
         attack_roll = roll_result

       attack_bonus = character.proficiency_bonus + character.ability_modifiers[weapon.ability]
       total = attack_roll + attack_bonus

       OUTPUT: "🎲 Attack: {d20} + {attack_bonus} = {total} vs AC {target.ac}"

  4. DETERMINE_HIT:
       IF attack_roll == 20:
         OUTPUT: "💥 CRITICAL HIT!"
         is_crit = true
         hit = true
       ELSE IF attack_roll == 1:
         OUTPUT: "❌ CRITICAL MISS!"
         hit = false
       ELSE IF total >= target.ac:
         OUTPUT: "✓ HIT!"
         hit = true
       ELSE:
         OUTPUT: "❌ MISS!"
         hit = false

  5. ROLL_DAMAGE (if hit):
       IF is_crit:
         # Double damage dice
         damage_dice = weapon.damage + weapon.damage
       ELSE:
         damage_dice = weapon.damage

       ROLL: damage_dice + ability_modifier
       damage = roll_result

       OUTPUT: "💥 Damage: {damage_dice} + {modifier} = {damage} {damage_type}"

       target.hp -= damage

       OUTPUT: "❤️ {target.name}: {old_hp} - {damage} = {target.hp} HP"

       IF target.hp <= 0:
         OUTPUT: "💀 {target.name} is defeated!"
         CALL: proto_handle_creature_death WITH target

  6. RETURN
```

**OUTPUT**: Attack resolved, damage applied
[PROTOCOL_END: proto_attack_action]

---

[PROTOCOL_START: proto_enemy_turn]
## PROTOCOL: Enemy_Combat_Turn_Protocol

**TRIGGER**: Enemy's turn in combat
**INPUT**: enemy (combatant object)
**GUARD**: enemy_alive

**PURPOSE**: AI-controlled enemy takes actions

**PROCEDURE**:
```yaml
Enemy_Combat_Turn_Protocol:
  1. ANNOUNCE_TURN:
       OUTPUT: ""
       OUTPUT: "━━━ {enemy.name}'s TURN ━━━"

  2. DETERMINE_ACTION:
       # Simplified AI - attacks nearest/weakest target
       valid_targets = FILTER party_state.characters WHERE hp_current > 0
       target = SELECT valid_targets ORDER BY hp_current ASC (weakest first)

  3. ATTACK:
       ROLL: d20 + enemy.attack_bonus
       attack_total = roll_result

       OUTPUT: "🎲 {enemy.name} attacks {target.name}"
       OUTPUT: "🎲 Attack: {d20} + {enemy.attack_bonus} = {attack_total} vs AC {target.ac}"

       IF attack_total >= target.ac:
         ROLL: enemy.damage_dice
         damage = roll_result

         OUTPUT: "✓ HIT!"
         OUTPUT: "💥 Damage: {damage} {damage_type}"

         target.hp_current -= damage

         OUTPUT: "❤️ {target.name}: {old_hp} - {damage} = {target.hp_current}/{target.hp_max} HP"

         IF target.hp_current <= 0:
           OUTPUT: "💀 {target.name} is unconscious!"
           CALL: proto_death_saves_init WITH target

       ELSE:
         OUTPUT: "❌ MISS!"

  4. END_TURN:
       OUTPUT: "--- {enemy.name}'s turn ends ---"

  5. RETURN
```

**OUTPUT**: Enemy's turn completed
[PROTOCOL_END: proto_enemy_turn]

---

[PROTOCOL_START: proto_death_saves]
## PROTOCOL: Death_Saves_Protocol

**TRIGGER**: Character at 0 HP at start of their turn
**INPUT**: character
**GUARD**: character.hp_current == 0

**PURPOSE**: Handle death saving throws for unconscious characters

**PROCEDURE**:
```yaml
Death_Saves_Protocol:
  1. ANNOUNCE:
       OUTPUT: "⚠️ {character.name} is UNCONSCIOUS and must make a death saving throw!"
       OUTPUT: "Successes: {character.death_saves.successes}/3"
       OUTPUT: "Failures: {character.death_saves.failures}/3"

  2. ROLL_SAVE:
       OUTPUT: "Roll d20 for death save (or auto):"
       ⛔ WAIT: roll_choice

       IF roll_choice == "auto":
         ROLL: d20
         save_roll = roll_result
       ELSE:
         OUTPUT: "What did you roll?"
         ⛔ WAIT: save_roll

       OUTPUT: "🎲 Death Save: {save_roll}"

  3. RESOLVE:
       IF save_roll == 20:
         OUTPUT: "💚 NATURAL 20! {character.name} regains 1 HP and is conscious!"
         character.hp_current = 1
         character.death_saves.successes = 0
         character.death_saves.failures = 0
         RETURN

       ELSE IF save_roll == 1:
         OUTPUT: "💀 NATURAL 1! Counts as 2 failures!"
         character.death_saves.failures += 2

       ELSE IF save_roll >= 10:
         OUTPUT: "✓ Success!"
         character.death_saves.successes += 1

       ELSE:
         OUTPUT: "❌ Failure!"
         character.death_saves.failures += 1

  4. CHECK_DEATH:
       IF character.death_saves.successes >= 3:
         OUTPUT: "💚 {character.name} is STABLE (unconscious but not dying)"
         # Reset death saves
         character.death_saves.successes = 0
         character.death_saves.failures = 0

       ELSE IF character.death_saves.failures >= 3:
         OUTPUT: "💀💀💀 {character.name} has DIED!"
         # Character is dead (permanent unless resurrected)

  5. RETURN
```

**OUTPUT**: Death save resolved
[PROTOCOL_END: proto_death_saves]

---

[PROTOCOL_START: proto_combat_end]
## PROTOCOL: Combat_End_Protocol

**TRIGGER**: All enemies defeated OR all party members unconscious
**GUARD**: combat_active

**PURPOSE**: End combat, award XP, handle loot

**PROCEDURE**:
```yaml
Combat_End_Protocol:
  1. DETERMINE_OUTCOME:
       IF ALL enemies defeated:
         outcome = "victory"
       ELSE IF ALL party unconscious/dead:
         outcome = "defeat"

  2. ANNOUNCE_END:
       OUTPUT: ""
       OUTPUT: "━━━ COMBAT ENDS ━━━"

       IF outcome == "victory":
         OUTPUT: "✓ Victory!"

       ELSE:
         OUTPUT: "💀 Defeat!"
         # Handle TPK or capture scenario
         RETURN

  3. AWARD_XP (if victory):
       total_xp = SUM(enemy.xp_value FOR enemy IN defeated_enemies)

       CALL: proto_xp_award WITH total_xp

  4. LOOT (if victory):
       FOR enemy IN defeated_enemies:
         IF enemy.loot:
           OUTPUT: "{enemy.name} drops:"
           FOR item IN enemy.loot:
             OUTPUT: "- {item.name}"

           CALL: proto_loot_distribution WITH enemy.loot

  5. RESET_COMBAT_STATE:
       party_state.location.in_combat = false
       party_state.combat_state.active = false
       party_state.combat_state.round = 0
       party_state.combat_state.initiative_order = []
       party_state.combat_state.current_turn = null

       FOR character IN party_state.characters:
         character.death_saves.successes = 0
         character.death_saves.failures = 0

  6. RETURN: to Exploration_Protocol
```

**OUTPUT**: Combat ended, XP awarded, loot distributed
[PROTOCOL_END: proto_combat_end]

---

## END OF PART 3: COMBAT


---

# ============================================================
# SOURCE: PART4_Progression.md
# ============================================================

# PROTOCOL LIBRARY - PART 4: PROGRESSION & QUESTS

---

[PROTOCOL_START: proto_xp_award]
## PROTOCOL: XP_Award_Protocol

**TRIGGER**: Combat ends (victory) OR quest milestone reached
**INPUT**: total_xp (integer)
**GUARD**: party_has_members

**PURPOSE**: Award XP immediately, check for level-ups

**PROCEDURE**:
```yaml
XP_Award_Protocol:
  1. CALCULATE_SHARES:
       num_characters = COUNT(party_state.characters WHERE hp_current > 0)
       xp_per_character = total_xp / num_characters

  2. DISTRIBUTE_XP:
       OUTPUT: "⭐ XP AWARD"
       OUTPUT: "Total: {total_xp} XP ÷ {num_characters} = {xp_per_character} XP each"
       OUTPUT: ""

       FOR character IN party_state.characters WHERE hp_current > 0:
         old_xp = character.identity.xp_current
         character.identity.xp_current += xp_per_character

         OUTPUT: "⭐ {character.name}: {old_xp} + {xp_per_character} = {character.identity.xp_current} XP"

         # Check for level-up
         IF character.identity.xp_current >= character.identity.xp_next_level:
           OUTPUT: "🎉 {character.name} LEVELS UP!"
           CALL: proto_level_up WITH character

  3. UPDATE_STATE:
       party_state.session_history.total_xp_earned += total_xp

  4. RETURN
```

**OUTPUT**: XP distributed, level-ups handled
[PROTOCOL_END: proto_xp_award]

---

[PROTOCOL_START: proto_level_up]
## PROTOCOL: Level_Up_Protocol

**TRIGGER**: Character XP >= XP threshold for next level
**INPUT**: character
**GUARD**: xp_sufficient

**PURPOSE**: Handle character advancement to next level

**PROCEDURE**:
```yaml
Level_Up_Protocol:
  1. INCREMENT_LEVEL:
       old_level = character.identity.level
       character.identity.level += 1
       new_level = character.identity.level

       OUTPUT: "━━━ 🎉 LEVEL UP! ━━━"
       OUTPUT: "{character.name}: Level {old_level} → {new_level}"

  2. UPDATE_THRESHOLDS:
       # From Kernel reference tables
       character.identity.xp_next_level = XP_THRESHOLDS[new_level + 1]
       character.proficiency_bonus = PROFICIENCY_BY_LEVEL[new_level]

  3. ROLL_HP:
       hit_die = character.class_hit_die (e.g., d10 for Fighter)
       con_mod = character.ability_modifiers.constitution

       OUTPUT: "Roll for HP increase:"
       OUTPUT: "1. Roll {hit_die} + {con_mod}"
       OUTPUT: "2. Take average ({(hit_die_max + 1) / 2} + {con_mod})"
       ⛔ WAIT: hp_choice

       IF hp_choice == "1":
         OUTPUT: "Roll {hit_die}:"
         ⛔ WAIT: roll_result
         hp_gain = roll_result + con_mod
       ELSE:
         hp_gain = ((hit_die_max + 1) / 2) + con_mod

       character.combat_stats.hp_max += hp_gain
       character.combat_stats.hp_current += hp_gain

       OUTPUT: "❤️ HP: {old_max} + {hp_gain} = {character.combat_stats.hp_max}"

  4. UPDATE_HIT_DICE:
       character.combat_stats.hit_dice_total += 1
       character.combat_stats.hit_dice_remaining += 1

  5. UPDATE_SPELL_SLOTS (if spellcaster):
       IF character.spells:
         # Update spell slots based on class spell slot table
         # This would reference class-specific progression
         OUTPUT: "Spell slots updated:"
         # Display new spell slot totals

  6. CLASS_FEATURES:
       OUTPUT: "New class features at level {new_level}:"
       # List features gained (would come from class data)
       # Examples: Extra Attack at Fighter 5, 3rd level spells at Wizard 5

  7. ASI_OR_FEAT (if level 4, 8, 12, 16, 19):
       IF new_level IN [4, 8, 12, 16, 19]:
         CALL: proto_asi_or_feat WITH character

  8. FINALIZE:
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━"
       OUTPUT: "Level up complete!"

  9. RETURN
```

**OUTPUT**: Character leveled up with new stats
[PROTOCOL_END: proto_level_up]

---

[PROTOCOL_START: proto_asi_or_feat]
## PROTOCOL: ASI_or_Feat_Protocol

**TRIGGER**: Character reaches level 4, 8, 12, 16, or 19
**INPUT**: character
**GUARD**: applicable_level

**PURPOSE**: Grant Ability Score Improvement or Feat

**PROCEDURE**:
```yaml
ASI_or_Feat_Protocol:
  1. PRESENT_CHOICE:
       OUTPUT: "Ability Score Improvement:"
       OUTPUT: "1. Increase two ability scores by 1 each (max 20)"
       OUTPUT: "2. Increase one ability score by 2 (max 20)"
       OUTPUT: "3. Take a feat (if allowed by DM)"
       ⛔ WAIT: choice

  2. SWITCH choice:
       CASE "1":
         OUTPUT: "First ability to increase:"
         ⛔ WAIT: ability1
         OUTPUT: "Second ability to increase:"
         ⛔ WAIT: ability2

         character.abilities[ability1].score += 1
         character.abilities[ability2].score += 1

         # Recalculate modifiers
         character.abilities[ability1].modifier = FLOOR((score - 10) / 2)
         character.abilities[ability2].modifier = FLOOR((score - 10) / 2)

         OUTPUT: "✓ {ability1}: +1, {ability2}: +1"

       CASE "2":
         OUTPUT: "Which ability to increase by 2?"
         ⛔ WAIT: ability

         character.abilities[ability].score += 2
         character.abilities[ability].modifier = FLOOR((score - 10) / 2)

         OUTPUT: "✓ {ability}: +2"

       CASE "3":
         OUTPUT: "Which feat? (DM must approve)"
         ⛔ WAIT: feat_name

         ADD feat_name TO character.features.feats
         OUTPUT: "✓ Gained feat: {feat_name}"

  3. UPDATE_DERIVED_STATS:
       # If CON increased, recalculate HP
       IF ability == "constitution":
         hp_retroactive = (new_con_mod - old_con_mod) * character.identity.level
         character.combat_stats.hp_max += hp_retroactive
         character.combat_stats.hp_current += hp_retroactive
         OUTPUT: "❤️ HP adjusted: +{hp_retroactive}"

  4. RETURN
```

**OUTPUT**: ASI or feat applied
[PROTOCOL_END: proto_asi_or_feat]

---

[PROTOCOL_START: proto_quest_accept]
## PROTOCOL: Quest_Accept_Protocol

**TRIGGER**: Player accepts quest from NPC or location
**INPUT**: quest_id
**GUARD**: quest_available

**PURPOSE**: Add quest to active quests, narrate quest details

**PROCEDURE**:
```yaml
Quest_Accept_Protocol:
  1. RETRIEVE_QUEST:
       CALL: Internal_Context_Retrieval(quest_id)
       # Loads full quest: objectives, rewards, structure

  2. NARRATE_QUEST:
       OUTPUT: "━━━ 📜 NEW QUEST ━━━"
       OUTPUT: "Quest: {quest.name}"
       OUTPUT: ""
       OUTPUT: quest.description
       OUTPUT: ""
       OUTPUT: "Objectives:"
       FOR objective IN quest.objectives:
         OUTPUT: "☐ {objective.description}"
       OUTPUT: ""
       OUTPUT: "Rewards: {quest.rewards.xp} XP, {quest.rewards.gold} gp"
       IF quest.rewards.items:
         OUTPUT: "Items: {list items}"
       OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━"

  3. ADD_TO_ACTIVE_QUESTS:
       quest_entry = {
         quest_id: quest_id,
         status: "in_progress",
         objectives_completed: [],
         notes: ""
       }
       ADD quest_entry TO party_state.campaign_state.quests_active

       REMOVE quest_id FROM party_state.campaign_state.quests_available

  4. UPDATE_STATE:
       party_state.session_history.major_events.APPEND("Accepted quest: {quest.name}")

  5. RETURN
```

**OUTPUT**: Quest accepted and added to log
[PROTOCOL_END: proto_quest_accept]

---

[PROTOCOL_START: proto_quest_completion]
## PROTOCOL: Quest_Completion_Protocol

**TRIGGER**: All quest objectives completed
**INPUT**: quest_id
**GUARD**: all_objectives_complete

**PURPOSE**: Award quest rewards, move quest to completed

**PROCEDURE**:
```yaml
Quest_Completion_Protocol:
  1. RETRIEVE_QUEST:
       CALL: Internal_Context_Retrieval(quest_id)

  2. ANNOUNCE_COMPLETION:
       OUTPUT: "━━━ 🎉 QUEST COMPLETE! ━━━"
       OUTPUT: "{quest.name}"
       OUTPUT: ""
       OUTPUT: quest.completion_narrative
       OUTPUT: ""

  3. AWARD_XP:
       CALL: proto_xp_award WITH quest.rewards.xp

  4. AWARD_GOLD:
       IF quest.rewards.gold_shared:
         party_state.party_resources.shared_gold += quest.rewards.gold
         OUTPUT: "💰 Party gold: +{quest.rewards.gold} gp"
       ELSE:
         # Divide among party
         gold_each = quest.rewards.gold / COUNT(party_state.characters)
         FOR character IN party_state.characters:
           character.gold += gold_each
           OUTPUT: "💰 {character.name}: +{gold_each} gp"

  5. AWARD_ITEMS (if any):
       IF quest.rewards.items:
         CALL: proto_loot_distribution WITH quest.rewards.items

  6. UPDATE_REPUTATION (if applicable):
       IF quest.rewards.reputation_changes:
         FOR rep_change IN quest.rewards.reputation_changes:
           CALL: proto_reputation_change WITH rep_change.target, rep_change.value

  7. MOVE_TO_COMPLETED:
       REMOVE quest FROM party_state.campaign_state.quests_active
       ADD quest_id TO party_state.campaign_state.quests_completed

  8. TRIGGER_FOLLOW_UP (if any):
       IF quest.unlocks_quest:
         ADD quest.unlocks_quest TO party_state.campaign_state.quests_available
         OUTPUT: "(New quest available: {unlocked_quest.name})"

  9. UPDATE_HISTORY:
       party_state.session_history.major_events.APPEND("Completed quest: {quest.name}")

  10. OUTPUT: "━━━━━━━━━━━━━━━━━━━━━━━━━━"

  11. RETURN
```

**OUTPUT**: Quest completed, rewards distributed
[PROTOCOL_END: proto_quest_completion]

---

[PROTOCOL_START: proto_loot_distribution]
## PROTOCOL: Loot_Distribution_Protocol

**TRIGGER**: Loot found (from combat, chest, quest reward)
**INPUT**: loot (list of items)
**GUARD**: loot_exists

**PURPOSE**: Present loot to party, handle distribution

**PROCEDURE**:
```yaml
Loot_Distribution_Protocol:
  1. DISPLAY_LOOT:
       OUTPUT: "━━━ 💰 LOOT ━━━"
       FOR item IN loot:
         OUTPUT: "- {item.name} ({item.type}, {item.weight} lbs)"
         IF item.value:
           OUTPUT: "  Value: {item.value} gp"
       OUTPUT: "━━━━━━━━━━━━━━━"

  2. PROMPT_DISTRIBUTION:
       OUTPUT: "Who takes what? (or 'party' for shared items)"
       ⛔ WAIT: distribution_input

  3. PARSE_DISTRIBUTION:
       # Example input: "Thorin takes sword, Mira takes gold, party takes rope"
       # Parse and assign items

       FOR assignment IN distribution_input:
         IF assignment.recipient == "party":
           ADD item TO party_state.party_resources.shared_items
         ELSE:
           character = FIND character WHERE name == assignment.recipient
           ADD item TO character.inventory
           character.carrying_weight += item.weight

           # Check encumbrance
           CALL: proto_encumbrance_check WITH character

  4. UPDATE_STATE:
       # Items distributed

  5. RETURN
```

**OUTPUT**: Loot distributed to characters
[PROTOCOL_END: proto_loot_distribution]

---

[PROTOCOL_START: proto_reputation_change]
## PROTOCOL: Track_Reputation_Change

**TRIGGER**: Player action affects NPC/faction reputation
**INPUT**: target_type ("npc" | "faction"), target_id, value_change
**GUARD**: None

**PURPOSE**: Modify and track reputation standings

**PROCEDURE**:
```yaml
Track_Reputation_Change:
  1. FIND_OR_CREATE_ENTRY:
       IF target_type == "npc":
         reputation_list = party_state.world_state.reputation.npcs
       ELSE:
         reputation_list = party_state.world_state.reputation.factions

       entry = FIND entry IN reputation_list WHERE entry.target_id == target_id

       IF entry NOT found:
         entry = {target_id: target_id, value: 0, notes: ""}
         ADD entry TO reputation_list

  2. UPDATE_VALUE:
       old_value = entry.value
       entry.value += value_change

       # Clamp to -10 to +10
       entry.value = CLAMP(entry.value, -10, +10)

  3. ANNOUNCE_CHANGE:
       IF value_change > 0:
         OUTPUT: "📈 Reputation with {target_id}: {old_value} → {entry.value} (+{value_change})"
       ELSE IF value_change < 0:
         OUTPUT: "📉 Reputation with {target_id}: {old_value} → {entry.value} ({value_change})"

  4. CHECK_THRESHOLD_CROSSED:
       # From Kernel reference: -5, +2, +6 are key thresholds
       IF old_value < -5 AND entry.value >= -5:
         OUTPUT: "  (No longer Hostile)"
       ELSE IF old_value < +2 AND entry.value >= +2:
         OUTPUT: "  (Now Friendly)"
       ELSE IF old_value < +6 AND entry.value >= +6:
         OUTPUT: "  (Now Beloved/Leadership)"

  5. RETURN
```

**OUTPUT**: Reputation updated and announced
[PROTOCOL_END: proto_reputation_change]

---

## END OF PART 4: PROGRESSION & QUESTS


---

# ============================================================
# SOURCE: PART5_Utilities.md
# ============================================================

# PROTOCOL LIBRARY - PART 5: UTILITIES & REST

---

[PROTOCOL_START: proto_rest_short]
## PROTOCOL: Short_Rest_Protocol

**TRIGGER**: Player chooses short rest (called by proto_rest)
**GUARD**: Party not in immediate danger

**PURPOSE**: 1-hour rest, spend hit dice to recover HP, restore short-rest resources

**PROCEDURE**:
```yaml
Short_Rest_Protocol:
  1. ANNOUNCE:
       OUTPUT: "━━━ ⏱️ SHORT REST (1 hour) ━━━"

  2. HIT_DICE_RECOVERY:
       FOR character IN party_state.characters:
         OUTPUT: "{character.name}: HP {character.hp_current}/{character.hp_max}"
         OUTPUT: "Hit Dice: {character.hit_dice_remaining}/{character.hit_dice_total} {character.hit_dice_type}"

         OUTPUT: "Spend hit dice to recover HP? (yes/no)"
         ⛔ WAIT: response

         IF response == "yes":
           WHILE character.hit_dice_remaining > 0:
             OUTPUT: "Roll how many hit dice? (0 to stop)"
             ⛔ WAIT: num_dice

             IF num_dice == 0:
               BREAK

             IF num_dice > character.hit_dice_remaining:
               OUTPUT: "Only have {character.hit_dice_remaining} remaining."
               CONTINUE

             FOR i IN range(num_dice):
               ROLL: character.hit_dice_type + character.ability_modifiers.constitution
               hp_gained = MAX(1, roll_result)

               character.hp_current = MIN(character.hp_max, character.hp_current + hp_gained)
               character.hit_dice_remaining -= 1

               OUTPUT: "🎲 {character.hit_dice_type} + {con_mod} = {hp_gained} HP recovered"

             OUTPUT: "❤️ {character.name}: {character.hp_current}/{character.hp_max} HP"
             OUTPUT: "Hit Dice: {character.hit_dice_remaining}/{character.hit_dice_total} remaining"

             IF character.hp_current < character.hp_max:
               OUTPUT: "Continue? (yes/no)"
               ⛔ WAIT: continue_choice
               IF continue_choice == "no":
                 BREAK
             ELSE:
               BREAK (already at max HP)

  3. RESTORE_SHORT_REST_RESOURCES:
       FOR character IN party_state.characters:
         # Restore resources that reset on short rest
         FOR resource IN character.resources.class_resources:
           IF resource.reset_on == "short_rest":
             resource.current = resource.max
             OUTPUT: "✓ {character.name}: {resource.name} restored"

         # Specific class features:
         # - Fighter: Action Surge, Second Wind
         # - Warlock: Spell slots
         # - Monk: Ki points
         # - Bard (level 5+): Bardic Inspiration

  4. TRACK_TIME:
       party_state.world_state.time_minutes += 60
       # Update time_of_day based on minutes

  5. ANNOUNCE_COMPLETE:
       OUTPUT: "━━━ Short Rest Complete ━━━"

  6. RETURN
```

**OUTPUT**: Short rest completed, HP/resources recovered
[PROTOCOL_END: proto_rest_short]

---

[PROTOCOL_START: proto_rest_long]
## PROTOCOL: Long_Rest_Protocol

**TRIGGER**: Player chooses long rest (called by proto_rest)
**GUARD**: Party not in immediate danger

**PURPOSE**: 8-hour rest, full HP/resource recovery, spell preparation

**PROCEDURE**:
```yaml
Long_Rest_Protocol:
  1. ANNOUNCE:
       OUTPUT: "━━━ ⛺ LONG REST (8 hours) ━━━"

  2. FULL_RECOVERY:
       FOR character IN party_state.characters:
         # HP to max
         character.hp_current = character.hp_max

         # Hit dice: recover half (minimum 1)
         dice_recovered = MAX(1, FLOOR(character.hit_dice_total / 2))
         character.hit_dice_remaining = MIN(character.hit_dice_total, character.hit_dice_remaining + dice_recovered)

         # All spell slots restored
         IF character.spells:
           FOR spell_level IN character.resources.spell_slots:
             character.resources.spell_slots[spell_level].current = character.resources.spell_slots[spell_level].max

         # All class resources restored
         FOR resource IN character.resources.class_resources:
           IF resource.reset_on == "long_rest":
             resource.current = resource.max

         # Reduce exhaustion by 1 level
         IF character.conditions CONTAINS "exhaustion":
           # Reduce exhaustion level by 1 (minimum 0)
           # Remove exhaustion condition if reaches 0

         OUTPUT: "✓ {character.name}: Fully rested"

  3. CONSUME_PROVISIONS:
       FOR character IN party_state.characters:
         IF character.survival.provisions > 0:
           character.survival.provisions -= 1
         ELSE:
           # Starvation - gain exhaustion
           OUTPUT: "⚠️ {character.name} has no food (exhaustion +1)"
           # Add exhaustion level

         IF character.survival.water > 0:
           character.survival.water -= 1
         ELSE:
           # Dehydration - gain exhaustion
           OUTPUT: "⚠️ {character.name} has no water (exhaustion +1)"
           # Add exhaustion level

  4. SPELL_PREPARATION (for prepared casters):
       FOR character IN party_state.characters:
         IF character.class IN ["Wizard", "Cleric", "Druid", "Paladin", "Ranger"]:
           max_prepared = character.ability_modifiers[character.spellcasting_ability] + character.identity.level

           # Class-specific adjustments
           IF character.class IN ["Paladin", "Ranger"]:
             max_prepared = FLOOR(max_prepared / 2)

           OUTPUT: "📜 {character.name} can prepare {max_prepared} spells."
           OUTPUT: "Current prepared: {list currently prepared spells}"
           OUTPUT: "Change prepared spells? (yes/no)"
           ⛔ WAIT: change_prep

           IF change_prep == "yes":
             OUTPUT: "List spells to prepare (comma-separated, max {max_prepared}):"
             OUTPUT: "Available spells: {list all known spells except cantrips}"
             ⛔ WAIT: new_prep_list

             # Parse and validate
             new_spells = PARSE new_prep_list

             IF COUNT(new_spells) > max_prepared:
               OUTPUT: "⚠️ Too many spells (max {max_prepared})"
               # Retry or keep current
             ELSE:
               # Update prepared flags
               FOR spell IN character.spells.spells_known:
                 IF spell.level > 0:
                   spell.prepared = (spell.name IN new_spells)

               OUTPUT: "✓ Spells prepared"

  5. TRACK_TIME:
       party_state.world_state.time_minutes += 480 (8 hours)
       party_state.world_state.time_elapsed += 1 (1 day)
       # Update date and time_of_day

  6. ANNOUNCE_COMPLETE:
       OUTPUT: "━━━ Long Rest Complete ━━━"
       OUTPUT: "All HP, spell slots, and resources restored."
       OUTPUT: "Rations and water consumed."

  7. RETURN
```

**OUTPUT**: Long rest completed, full recovery
[PROTOCOL_END: proto_rest_long]

---

[PROTOCOL_START: proto_session_end]
## PROTOCOL: Session_End_Protocol

**TRIGGER**: Player requests session end
**GUARD**: None

**PURPOSE**: Save party state, provide download link

**PROCEDURE**:
```yaml
Session_End_Protocol:
  1. ANNOUNCE:
       OUTPUT: "━━━ 📝 SESSION ENDING ━━━"

  2. GENERATE_SESSION_SUMMARY:
       OUTPUT: "Session {party_state.metadata.session_number} Summary:"
       OUTPUT: "- XP Earned this session: {total_xp_this_session}"
       OUTPUT: "- Gold Earned: {total_gold_this_session}"
       OUTPUT: "- Quests Completed: {list quest names}"
       OUTPUT: "- Major Events: {list from session_history.major_events}"
       OUTPUT: ""

  3. PREPARE_SAVE_FILE:
       party_state.metadata.session_number += 1
       party_state.metadata.date = CURRENT_TIMESTAMP()

       # Serialize party_state to JSON
       save_json = JSON.stringify(party_state, indent=2)

       filename = "party_state_session_{session_number}.json"

  4. OUTPUT_DOWNLOAD_LINK:
       OUTPUT: "Save file ready:"
       OUTPUT: "computer:///outputs/{filename}"
       OUTPUT: ""
       OUTPUT: "(Download this file to resume next session)"

  5. FAREWELL:
       OUTPUT: "Thanks for playing! See you next session. 🎲"

  6. SET: session_active = false

  7. RETURN
```

**OUTPUT**: Session ended, save file provided
[PROTOCOL_END: proto_session_end]

---

[PROTOCOL_START: proto_encumbrance_check]
## PROTOCOL: Encumbrance_Check

**TRIGGER**: Item added/removed from inventory
**INPUT**: character
**GUARD**: None

**PURPOSE**: Check if character is encumbered, update status

**PROCEDURE**:
```yaml
Encumbrance_Check:
  1. CALCULATE_WEIGHT:
       total_weight = SUM(item.weight FOR item IN character.inventory.equipment)
       character.carrying_weight = total_weight

  2. DETERMINE_THRESHOLDS:
       strength = character.abilities.strength.score
       capacity = strength * 15
       encumbered_at = strength * 5
       heavily_encumbered_at = strength * 10

  3. DETERMINE_STATUS:
       IF total_weight > capacity:
         new_status = "over_capacity"
       ELSE IF total_weight > heavily_encumbered_at:
         new_status = "heavily_encumbered"
       ELSE IF total_weight > encumbered_at:
         new_status = "encumbered"
       ELSE:
         new_status = "normal"

  4. COMPARE_TO_PREVIOUS:
       IF new_status != character.current_encumbrance_status:
         SWITCH new_status:
           CASE "over_capacity":
             OUTPUT: "❌ {character.name} CANNOT carry this (over capacity by {total_weight - capacity} lbs)"
             RETURN: false

           CASE "heavily_encumbered":
             OUTPUT: "⚠️ {character.name} is HEAVILY ENCUMBERED"
             OUTPUT: "  Speed -20ft, Disadvantage on STR/DEX/CON checks and saves"

           CASE "encumbered":
             OUTPUT: "⚠️ {character.name} is ENCUMBERED"
             OUTPUT: "  Speed -10ft"

           CASE "normal":
             OUTPUT: "✓ {character.name} is no longer encumbered"

         character.current_encumbrance_status = new_status

  5. RETURN: true
```

**OUTPUT**: Encumbrance status updated
[PROTOCOL_END: proto_encumbrance_check]

---

[PROTOCOL_START: proto_cast_spell]
## PROTOCOL: Cast_Spell (Combat/Exploration)

**TRIGGER**: Character casts spell
**INPUT**: character, spell_name (optional)
**GUARD**: character_has_spells

**PURPOSE**: Handle spell casting, slot usage, spell effects

**PROCEDURE**:
```yaml
Cast_Spell:
  1. SELECT_SPELL:
       IF spell_name NOT provided:
         OUTPUT: "Which spell to cast?"
         OUTPUT: "Prepared spells:"
         FOR spell IN character.spells.spells_known WHERE spell.prepared:
           OUTPUT: "- {spell.name} (Level {spell.level})"
         ⛔ WAIT: spell_name

  2. FIND_SPELL:
       spell = FIND spell IN character.spells.spells_known WHERE spell.name == spell_name

       IF spell NOT found OR NOT spell.prepared:
         OUTPUT: "⚠️ That spell is not prepared."
         RETURN

  3. CHECK_SPELL_SLOT:
       IF spell.level == 0:
         # Cantrip, no slot needed
         slot_available = true
       ELSE:
         IF character.resources.spell_slots["level_{spell.level}"].current > 0:
           slot_available = true
         ELSE:
           OUTPUT: "⚠️ No level {spell.level} spell slots remaining."
           RETURN

  4. SELECT_TARGET (if applicable):
       IF spell requires target:
         OUTPUT: "Target:"
         # List valid targets (allies, enemies, self)
         ⛔ WAIT: target

  5. RESOLVE_SPELL:
       # This is highly spell-dependent
       # Examples:
       # - Fireball: AOE damage, DEX save
       # - Cure Wounds: Roll healing dice
       # - Shield: +5 AC until next turn

       # Simplified example for damage spell:
       IF spell.type == "damage":
         DC = character.spells.spell_save_dc

         OUTPUT: "{target} must make {spell.save_type} save (DC {DC})"
         ROLL: d20 + target.save_modifier

         IF roll >= DC:
           OUTPUT: "✓ SAVE! Half damage."
           damage_multiplier = 0.5
         ELSE:
           OUTPUT: "❌ FAIL! Full damage."
           damage_multiplier = 1.0

         ROLL: spell.damage_dice
         damage = roll_result * damage_multiplier

         OUTPUT: "💥 {spell.name}: {damage} {spell.damage_type} damage"
         target.hp -= damage
         OUTPUT: "❤️ {target.name}: {target.hp}/{target.hp_max} HP"

  6. CONSUME_SPELL_SLOT:
       IF spell.level > 0:
         character.resources.spell_slots["level_{spell.level}"].current -= 1
         OUTPUT: "📜 Level {spell.level} slots: {current}/{max}"

  7. RETURN
```

**OUTPUT**: Spell cast, effects resolved
[PROTOCOL_END: proto_cast_spell]

---

[PROTOCOL_START: proto_use_item]
## PROTOCOL: Use_Item (Combat/Exploration)

**TRIGGER**: Character uses consumable item
**INPUT**: character, item_name (optional)
**GUARD**: character_has_item

**PURPOSE**: Handle item usage (potions, scrolls, etc.)

**PROCEDURE**:
```yaml
Use_Item:
  1. SELECT_ITEM:
       OUTPUT: "Which item to use?"
       FOR item IN character.inventory.equipment:
         OUTPUT: "- {item.name} ({item.type})"
       ⛔ WAIT: item_name

  2. FIND_ITEM:
       item = FIND item IN character.inventory.equipment WHERE item.name == item_name

       IF item NOT found:
         OUTPUT: "⚠️ You don't have that item."
         RETURN

  3. RESOLVE_ITEM_EFFECT:
       SWITCH item.type:
         CASE "potion":
           # Example: Potion of Healing
           ROLL: item.healing_dice
           hp_restored = roll_result

           character.hp_current = MIN(character.hp_max, character.hp_current + hp_restored)

           OUTPUT: "🧪 {item.name}: {hp_restored} HP restored"
           OUTPUT: "❤️ {character.name}: {character.hp_current}/{character.hp_max} HP"

         CASE "scroll":
           # Cast spell from scroll
           OUTPUT: "Casting {item.spell_name} from scroll..."
           CALL: proto_cast_spell WITH character, item.spell_name
           # Scroll is consumed after casting

         DEFAULT:
           OUTPUT: "Using {item.name}..."
           # Custom item effects

  4. CONSUME_ITEM (if consumable):
       IF item.consumable:
         REMOVE item FROM character.inventory
         character.carrying_weight -= item.weight
         OUTPUT: "({item.name} consumed)"

  5. RETURN
```

**OUTPUT**: Item used, effects applied
[PROTOCOL_END: proto_use_item]

---

## END OF PART 5: UTILITIES & REST
## END OF PROTOCOL LIBRARY


---

