# SECTION 5: SESSION MANAGEMENT PROTOCOLS

## PROTOCOL: Session_Initialization

**TRIGGER**: System start
**GUARD**: orchestrator_loaded AND system_ready

**PROCEDURE**:
```
1. LOAD this orchestrator document
2. VERIFY orchestrator version >= 4.0
3. OUT: "Enter campaign module JSON:"
4. ⛔ WAIT: campaign_module_data
5. PARSE AND VALIDATE campaign_module_data AGAINST Campaign_Module_Schema_v2
6. IF validation_failed THEN
     OUT: "❌ Invalid campaign format. Errors: [detailed_list]"
     GOTO step 3
7. INDEX campaign data for fast lookup
8. SET: campaign_loaded = true
9. CALL: Session_Start_Decision
```

## PROTOCOL: Session_Start_Decision

**TRIGGER**: Campaign loaded successfully
**GUARD**: campaign_loaded AND campaign_indexed

**PROCEDURE**:
```
1. OUT:
   "=== D&D 5E SESSION START ===
   Campaign: [campaign_name]
   Version: [campaign_version]

   1. Start New Session (create or import characters)
   2. Resume Previous Session (load save file)

   Choose option:"

2. ⛔ WAIT: choice

3. PARSE: choice
4. IF choice == "1" OR "new" OR "start" THEN
     CALL: New_Session_Flow
5. ELSE IF choice == "2" OR "resume" OR "load" THEN
     CALL: Resume_Session_Protocol
6. ELSE
     OUT: "Invalid choice. Please enter 1 or 2."
     GOTO step 1
```

## PROTOCOL: New_Session_Flow

**TRIGGER**: New session selected
**GUARD**: campaign_loaded AND no_active_session

**PROCEDURE**:
```
1. CALL: Load_Character_Creation_Module
2. CHECK: characters_created >= 1
3. IF validation_failed THEN
     OUT: "At least one character required."
     GOTO step 1

4. INITIALIZE party_state FROM Party_State_Schema_v2:
     - session_number = 1
     - location.current = campaign.starting_location
     - campaign_state.quests_available = campaign.starting_quests
     - All other fields initialized empty/default

5. CHECK: party_state_complete = true
6. IF validation_failed THEN
     OUT: "❌ State initialization failed: [errors]"
     HALT

7. SET: session_active = true
8. NARRATE: opening scene from campaign module
9. CALL: Game_Loop
```

## PROTOCOL: Load_Character_Creation_Module

**TRIGGER**: New_Session_Flow requires character creation
**GUARD**: campaign_loaded AND no_characters_yet

**PROCEDURE**:
```
1. OUT:
   "⚠️ CHARACTER CREATION MODULE REQUIRED

   To create/import characters, I need the character creation module.
   Please paste or upload: 'character_creation_module.md'

   (Located in: agent_parts/character_creation_module.md)"

2. ⛔ WAIT: module_content

3. PARSE: module_content
4. VERIFY: contains "Character_Import_or_Create_Protocol"
5. IF validation_failed THEN
     OUT: "❌ Invalid module. Please provide character_creation_module.md"
     GOTO step 1

6. LOAD: module protocols into context
7. OUT: "✓ Character creation module loaded. Proceeding..."
8. CALL: Character_Import_or_Create_Protocol
9. AFTER characters created:
     OUT: "✓ Characters created. Character creation module can now be unloaded (context saved)."
10. RETURN: party_state.characters
```

**Module Protocols** (available after loading):
- `Character_Import_or_Create_Protocol` - Prompts user to import or create
- `Character_Import_Flow` - Handles JSON import from paste/file/Drive
- `Character_Creation_Flow` - Guided wizard (name, race, class, abilities, spells, HP)

**Context Optimization**:
- Module: 7.3KB (only loaded during character creation)
- After creation: Module can be removed from context
- Saves: ~7KB during gameplay (99% of runtime)

## PROTOCOL: Resume_Session_Protocol

**TRIGGER**: Resume selected
**GUARD**: campaign_loaded

**PROCEDURE**:
```
1. OUT: "Load save: 1. Upload 2. Paste 3. Drive link 4. Search Drive"

2. ⛔ WAIT: choice

3. SWITCH choice:
     CASE "1"/"upload": WAIT_FOR file → READ content → SET save_data
     CASE "2"/"paste": PROMPT paste → ⛔ WAIT content → SET save_data
     CASE "3"/"drive"/"link": PROMPT link → ⛔ WAIT → EXTRACT id → CALL google_drive_fetch → SET save_data
     CASE "4"/"search": PROMPT terms → ⛔ WAIT → CALL google_drive_search → IF found: SHOW list → ⛔ WAIT select → FETCH → SET save_data; ELSE: GOTO step 1
     DEFAULT: OUT "Invalid" → GOTO step 1

4. PARSE save_data
5. CHECK against Party_State_Schema_v2
6. IF invalid: OUT error → GOTO step 1

7. EXTRACT campaign_id
8. IF campaign_id mismatch: OUT warning → PROMPT load new campaign? → IF yes: PROMPT module → CALL Session_Initialization → GOTO step 3; ELSE: GOTO step 1

9. LOAD party_state
10. CHECK integrity
11. SET session_active = true
12. OUT "✓ Session resumed"
13. NARRATE current situation
14. CALL Game_Loop
```
