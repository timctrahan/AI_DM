# D&D 5E CHARACTER CREATION MODULE
**Version**: 1.0 | **Extracted from**: Orchestrator v6.6.0 | **Updated**: Nov 19, 2024

---

## PURPOSE

This module contains character creation and import protocols for the D&D 5E Orchestrator.

**When to load this module**:
- Starting a NEW campaign (first session)
- Adding characters mid-campaign (new player joins)
- Character dies and needs replacement

**When NOT to load this module**:
- Resuming existing session (characters already created)
- During normal gameplay (99% of runtime)
- Character leveling up (handled by Level_Up_Protocol in main orchestrator)

**Usage**:
1. Load main orchestrator (`CORE_DND5E_AGENT_ORCHESTRATOR_vX.X.X.md`)
2. When `New_Session_Flow` is triggered, load THIS module
3. Execute Character_Import_or_Create_Protocol
4. After characters created, unload this module (save context space)
5. Continue with main orchestrator Game_Loop

**Size**: 7,400 bytes (saved from main orchestrator context)

---

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

---

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

---

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

---

## INTEGRATION NOTES

**Dependencies**:
- Requires `Character_Schema_v2` from main orchestrator Part 1
- Requires `xp_table` from main orchestrator Part 1
- Uses standard class spell progression tables (LLM knows PHB rules)

**State Changes**:
- Adds character(s) to `party_state.characters[]`
- Validates all character data against Character_Schema_v2
- Returns control to `New_Session_Flow` in main orchestrator

**Error Handling**:
- Invalid character data → Re-prompt for input
- Missing required fields → Show detailed errors
- Schema validation failure → HALT with error message

**Context Management**:
- Load this module ONLY during character creation
- After characters created, this module can be unloaded
- Saves ~7.4KB of context space during gameplay

---

## VERSION HISTORY

**v1.0 (Nov 19, 2024)**:
- Extracted from Orchestrator v6.6.0
- Contains 3 protocols: Character_Import_or_Create, Character_Import_Flow, Character_Creation_Flow
- Size: 7,400 bytes
- Purpose: Reduce main orchestrator context consumption
