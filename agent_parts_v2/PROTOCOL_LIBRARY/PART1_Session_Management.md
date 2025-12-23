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

[PROTOCOL_START: proto_kernel_integrity_check]
## PROTOCOL: Kernel_Integrity_Check

**TRIGGER**: First input of session (called by proto_session_init)
**GUARD**: None

**PURPOSE**: Verify Kernel and required components loaded correctly

**PROCEDURE**:
```yaml
Kernel_Integrity_Check:
  1. VERIFY_KERNEL:
       CHECK: Player Agency Law understood
       CHECK: Mechanical Integrity Law understood
       CHECK: Context Fidelity Law understood
       CHECK: Execution Loop structure memorized
       CHECK: Internal_Context_Retrieval callable
       CHECK: Checkpoint_Validation callable

       IF any_fail:
         OUTPUT: "⛔ KERNEL INTEGRITY COMPROMISED"
         OUTPUT: "Cannot guarantee protocol adherence"
         HALT_INITIALIZATION

  2. VERIFY_PROTOCOL_LIBRARY:
       SEARCH: "[PROTOCOL_INDEX]" in conversation
       IF not_found:
         OUTPUT: "⛔ PROTOCOL LIBRARY NOT LOADED"
         OUTPUT: "Required: PROTOCOL_LIBRARY_v{version}.md must be in conversation"
         HALT_INITIALIZATION

  3. VERIFY_CAMPAIGN_VAULT:
       SEARCH: "[MASTER_INDEX]" in conversation
       IF not_found:
         OUTPUT: "⛔ CAMPAIGN DATA VAULT NOT LOADED"
         OUTPUT: "Required: Campaign_Data_Vault.md must be in conversation"
         HALT_INITIALIZATION

  4. SUCCESS:
       OUTPUT: "✓ Kernel integrity verified"
       OUTPUT: "✓ Protocol Library indexed"
       OUTPUT: "✓ Campaign Data Vault indexed"
       RETURN: success
```

**OUTPUT**: Integrity check passed or HALT
[PROTOCOL_END: proto_kernel_integrity_check]

---

## END OF PART 1: SESSION MANAGEMENT
