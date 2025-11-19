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
1. CALL: Character_Import_or_Create_Protocol
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

## PROTOCOL: Character_Import_or_Create_Protocol

**TRIGGER**: New session needs characters
**GUARD**: campaign_loaded

**PROCEDURE**:
```
1. OUT:
   "Character Setup:
   1. Import existing character (paste JSON)
   2. Create new character (guided creation)

   Choose option:"

2. ⛔ WAIT: choice

3. IF choice == "1" OR "import" THEN
     CALL: Character_Import_Flow
4. ELSE IF choice == "2" OR "create" THEN
     CALL: Character_Creation_Flow
5. ELSE
     OUT: "Invalid choice."
     GOTO step 1

6. CHECK: character_data AGAINST Character_Schema_v2
7. IF validation_failed THEN
     OUT: "❌ Character data invalid: [errors]"
     GOTO step 1

8. ADD: character TO party_state.characters
9. OUT: "✓ [character_name] added to party."

10. OUT: "Import another character? (yes/no)"
11. ⛔ WAIT: response

12. IF response == "yes" OR "y" THEN
      GOTO step 1
13. ELSE
      RETURN: party_state.characters
```

## PROTOCOL: Character_Import_Flow

**TRIGGER**: Import selected
**GUARD**: none

**PROCEDURE**:
```
1. OUT: "Paste character JSON (or provide Google Drive link):"
2. ⛔ WAIT: input

3. IF input CONTAINS "docs.google.com" THEN
     CALL: google_drive_fetch WITH document_id
     SET: character_json = fetched_content
4. ELSE IF input IS uploaded_file THEN
     READ: file_content
     SET: character_json = file_content
5. ELSE
     SET: character_json = input

6. PARSE: character_json
7. CHECK: character_json AGAINST Character_Schema_v2
8. IF validation_failed THEN
     OUT: "❌ Invalid character format: [detailed_errors]"
     GOTO step 1

9. VERIFY: required_fields_present = true
10. RETURN: parsed_character
```

## PROTOCOL: Character_Creation_Flow

**TRIGGER**: Create new character selected
**GUARD**: none

**PROCEDURE**:
```
1. OUT: "=== Character Creation ==="

2-3. PROMPT name → ⛔ WAIT → SET character.name
4-5. PROMPT race → ⛔ WAIT → SET character.race
6-7. PROMPT class → ⛔ WAIT → SET character.class
8-9. PROMPT background → ⛔ WAIT → SET character.background
10-11. PROMPT level (1-20) → ⛔ WAIT → CHECK range → SET character.level

12-13. OUT "Assign scores (array: 15,14,13,12,10,8)" → FOR ability IN [STR,DEX,CON,INT,WIS,CHA]: PROMPT → ⛔ WAIT → CHECK valid/unused → SET score → CALC modifier

14-15. CALC proficiency_bonus, hp_max → SET hp_current = hp_max
16-17. PROMPT AC → ⛔ WAIT → SET armor_class
18-19. PROMPT gold → ⛔ WAIT → SET inventory.gold
20-21. SET xp_current, xp_next_level FROM xp_table

22. IF character.class IN spellcaster_classes [Wizard, Cleric, Druid, Bard, Sorcerer, Warlock, Paladin, Ranger]:
      a. GET: cantrips_known, spells_known_count FROM class_spell_progression[class][level]
      b. GET: spell_list FOR character.class
      c-d. SPELL_SELECTION: GET ability scores → FOR spell_type IN [cantrips, spells]:
           OUT: "📜 Choose [spell_count] [spell_type] from [class] spell list"
           SHOW: available [spell_type] for class
           PROMPT: "Select [spell_count] (comma-separated):"
           ⛔ WAIT: choices
           VALIDATE: count == spell_count AND all IN spell_list AND all level correct
           IF validation_failed: OUT "Invalid selection" → RETURN to step 22c
           ADD: choices TO character.spells.spells_known (prepared = true for cantrips)
      e. IF class IN prepared_casters [Wizard, Cleric, Druid, Paladin]:
           CALC: max_prepared = ability_modifier + level
           OUT: "You can prepare [max_prepared] spells per day"
           PROMPT: "Which spells do you prepare now? (choose up to [max_prepared]):"
           ⛔ WAIT: prepared_choices
           VALIDATE: count <= max_prepared AND all IN spells_known
           IF validation_failed: OUT "Invalid preparation" → RETURN to step 22e
           FOR spell IN spells_known: SET spell.prepared = (spell IN prepared_choices)
      f. ELSE (spontaneous casters: Bard, Sorcerer, Warlock, Ranger):
           FOR spell IN spells_known: SET spell.prepared = true (always prepared)
      g. CALC: spell_save_dc = 8 + proficiency_bonus + spellcasting_ability_modifier
      h. CALC: spell_attack_bonus = proficiency_bonus + spellcasting_ability_modifier
      i. SET: character.spells.spell_save_dc, character.spells.spell_attack_bonus
      j. OUT: "✓ Spells configured: [cantrips_count] cantrips, [spells_count] spells"
    ELSE:
      SET: character.spells = null (non-spellcaster)

23. OUT: "❤️ HP Confirmation: [character.name] has [hp_max] HP ([class] hit die d[hit_die] + CON [con_mod])"
    PROMPT: "Confirm starting HP? (yes/no)"
    ⛔ WAIT: hp_confirmation
    IF hp_confirmation != "yes":
      PROMPT: "Enter corrected HP max:"
      ⛔ WAIT: new_hp_max
      VALIDATE: new_hp_max > 0 AND new_hp_max <= 50 (sanity check for level 1)
      SET: hp_max = new_hp_max
      SET: hp_current = new_hp_max
      OUT: "✓ HP updated to [new_hp_max]"

24. OUT "✓ Created [character.name] - Level [level] [class]"
    SHOW summary:
      - Name, Race, Class, Level
      - Ability Scores (with modifiers)
      - HP: [hp_current]/[hp_max]
      - AC: [armor_class]
      - Proficiency: +[proficiency_bonus]
      - Gold: [gold]gp
      - Spells (if applicable): [cantrips_count] cantrips, [spells_count] spells known
    RETURN character
```

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
