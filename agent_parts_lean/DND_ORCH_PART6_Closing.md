# SECTION 10: SESSION END & PERSISTENCE

## PROTOCOL: Session_End_Protocol

**TRIGGER**: Player requests session end
**GUARD**: no_pending_player_decisions AND state_valid

**PROCEDURE**:
```
1. IF party_state.location.in_combat:
     OUT: "⚠️ Cannot save during combat. Finish or flee first."
     RETURN

2. OUT: "Ending session. Create save file? (yes/no)"
3. ⛔ WAIT: response

4. IF response == "yes" OR "y":
     CALL: Save_State_Protocol

5. OUT: "Session ended. Thanks for playing!"
6. SET: session_active = false
7. RETURN
```

## PROTOCOL: Save_State_Protocol

**TRIGGER**: Session end with save requested OR user command "save game"
**GUARD**: party_state_valid AND no_combat_active

**IMMUTABLE OUTPUT RULES**:
1. **NO SUMMARIZATION**: Output MUST include specific values for every character's HP, Slots, XP, Gold, and Inventory.
2. **NO ABBREVIATION**: Do not use "etc" or "rest of items." List EVERYTHING.
3. **FULL FIDELITY**: The output must be sufficient to reconstruct the game state in a completely new chat instance with zero data loss.
4. **FORMAT**: Must match the "Save File Metadata" structure used in loading.

**PROCEDURE**:
```
1. CHECK: party_state AGAINST Party_State_Schema_v2
2. IF validation_failed:
     OUT: "❌ State validation failed. Cannot save."
     OUT: "Errors: [list]"
     RETURN

3. OUT: "💾 GENERATING FULL-FIDELITY SAVE FILE..."
4. OUT: "⚠️ COPY THE TEXT BELOW BETWEEN THE START/END MARKERS"

5. GENERATE OUTPUT BLOCK:

--- START OF FILE [Campaign_Name]_Save_Day[Day]_[Time].md ---

=== CAMPAIGN HEADER ===
Campaign: [campaign_name]
Session: [session_number]
Date: [timestamp]
Location: [current_location] (Previous: [previous_location])
Save Version: 2.0
In-Game Time: Day [time_elapsed], [time_of_day], [time_minutes] total minutes

=== CHARACTER ROSTER ===

FOR EACH character IN party_state.characters:

  CHARACTER: [character.identity.name]
  Race: [race] | Class: [class] [level] | Background: [background]
  Alignment: [alignment] | XP: [xp_current] / [xp_next_level]

  COMBAT STATS:
    HP: [hp_current] / [hp_max] | AC: [armor_class] | Speed: [speed] ft
    Initiative: +[initiative_bonus] | Proficiency: +[proficiency_bonus]
    Hit Dice: [hit_dice_total] ([hit_dice_remaining] remaining)
    Death Saves: Successes [successes], Failures [failures]
    Reaction Available: [reaction_available]

  ABILITY SCORES:
    STR: [score] ([modifier]) [Save Prof: yes/no]
    DEX: [score] ([modifier]) [Save Prof: yes/no]
    CON: [score] ([modifier]) [Save Prof: yes/no]
    INT: [score] ([modifier]) [Save Prof: yes/no]
    WIS: [score] ([modifier]) [Save Prof: yes/no]
    CHA: [score] ([modifier]) [Save Prof: yes/no]

  SPELL SLOTS (if spellcaster):
    Spellcasting Ability: [spellcasting_ability]
    Spell Save DC: [spell_save_dc] | Spell Attack: +[spell_attack_bonus]
    Level 1: [current] / [max]
    Level 2: [current] / [max]
    Level 3: [current] / [max]
    Level 4: [current] / [max]
    Level 5: [current] / [max]
    Level 6: [current] / [max]
    Level 7: [current] / [max]
    Level 8: [current] / [max]
    Level 9: [current] / [max]
    (List ONLY levels where max > 0)

  SPELLS KNOWN (if spellcaster):
    FOR EACH spell IN character.spells.spells_known:
      - [spell.name] (Level [spell.level]) [Prepared: yes/no]

  CLASS RESOURCES:
    FOR EACH resource IN character.resources.class_resources:
      - [resource.name]: [current] / [max] (Resets on: [reset_on])

  INVENTORY:
    Gold: [gold] gp

    EQUIPMENT (Equipped):
      FOR EACH item IN equipment WHERE equipped == true:
        - [item.name] ([item.type], [item.properties])

    MAGIC ITEMS:
      FOR EACH item IN magic_items:
        - [item.name] (Attuned: [attuned yes/no]) - [item.description]

    BACKPACK:
      FOR EACH item IN equipment WHERE equipped == false:
        - [item.name] x[quantity]

    AMMUNITION:
      FOR EACH ammo IN ammo:
        - [ammo.type]: [ammo.count]

    Carrying Weight: [carrying_weight] lbs

  SURVIVAL:
    Provisions: [provisions] days
    Water: [water] days
    Days Without Food: [days_without_food]
    Active Light Sources:
      FOR EACH light IN active_light_sources:
        - [light.type]: [light.remaining_duration] minutes remaining

  PROFICIENCIES:
    Armor: [comma-separated list]
    Weapons: [comma-separated list]
    Tools: [comma-separated list]
    Skills:
      FOR EACH skill IN skills:
        - [skill.name] [Proficient: yes/no] [Expertise: yes/no]

  ACTIVE CONDITIONS: [comma-separated list OR "None"]

  NOTES:
    Personality Traits: [personality_traits]
    Ideals: [ideals]
    Bonds: [bonds]
    Flaws: [flaws]

  ---

END CHARACTER LOOP

=== PARTY RESOURCES ===
Shared Gold: [shared_gold] gp
Shared Items:
  FOR EACH item IN party_resources.shared_items:
    - [item.name] x[quantity]

=== WORLD STATE ===

DISCOVERED LOCATIONS: [comma-separated list]
CLEARED LOCATIONS: [comma-separated list]

NPC REPUTATION:
  FOR EACH npc IN world_state.reputation.npcs:
    - [npc.npc_id]: [npc.value] ([npc.notes])

FACTION STANDING:
  FOR EACH faction IN world_state.reputation.factions:
    - [faction.faction_id]: [faction.value] (Rank: [faction.rank])

REGION REPUTATION:
  FOR EACH region IN world_state.reputation.regions:
    - [region.region_id]: Fame [region.fame], Infamy [region.infamy]
      Known Deeds: [comma-separated known_deeds]

STORY FLAGS:
  FOR EACH flag IN world_state.story_flags:
    - [flag_name]: [value]

=== QUEST LOG ===

ACTIVE QUESTS:
  FOR EACH quest_id IN campaign_state.quests_active:
    - [quest_id] ([quest_name from campaign module])
      Progress: [progress_description]
      Objectives:
        FOR EACH objective IN quest.objectives:
          - [objective.description] [Completed: yes/no]

COMPLETED QUESTS: [comma-separated quest_ids]
AVAILABLE QUESTS: [comma-separated quest_ids]
FAILED QUESTS: [comma-separated quest_ids]

=== COMBAT STATE ===
Active: [yes/no]
IF active == true:
  Round: [round]
  Current Turn: [current_turn]
  Initiative Order:
    FOR EACH combatant IN initiative_order:
      - [combatant.name]: [combatant.initiative]
  Defeated Enemies:
    FOR EACH enemy IN defeated_enemies:
      - [enemy.name] ([enemy.monster_id])

=== SESSION METADATA ===

  [Describe in 2-3 sentences: Where is the party right now? What room/area?
   What just happened in the last action? Are they mid-conversation with an NPC?
   Any immediate threats or opportunities visible?]

Tactical Notes:
  [Resources spent this session, active threats, environmental conditions,
   time-sensitive events, anything that affects immediate next action]

--- END OF FILE ---

6. OUT: "✓ Save Complete. Copy the block above to resume later."
7. OUT: "📋 To resume: Start new session → choose 'Resume' → paste this entire block"
8. RETURN
```

---

# SECTION 11: ERROR HANDLING

## ERROR: Invalid_User_Input

**TRIGGER**: Unparseable input
**PROCEDURE**:
```
1. OUT: "I didn't understand that. Please rephrase."

2. IF context == COMBAT:
     OUT: "Available: Attack, Cast Spell, Dodge, Disengage, Help, Hide, Ready, Dash, Use Item"

3. ELSE IF context == EXPLORATION:
     OUT: "You can: move, investigate, interact, rest, check inventory, view quests"

4. RETURN to last prompt
```

## ERROR: State_Validation_Failure

**TRIGGER**: State consistency check fails
**PROCEDURE**:
```
1. OUT: "⚠️ State inconsistency detected."
2. CALL: State_Recovery_Protocol
3. RETURN
```

---

# SECTION 12: AGENT EXECUTION RULES

⚠️ SENTINEL: Protocol priority hierarchy and execution rules defined in Part 1 Foundation
