# SECTION 8: XP, LEVELING & PROGRESSION

## PROTOCOL: XP_Award_Protocol

**TRIGGER**: Combat ends successfully
**INPUT**: total_xp
**GUARD**: combat_ended AND enemies_defeated

**PROCEDURE**:
```
1. CALC: xp_per_pc = total_xp ÷ number_of_conscious_pcs
2. OUT: "⭐ XP Awarded: [total_xp] ÷ [num_pcs] = [xp_per_pc] each"

3. FOR character IN party_state.characters WHERE conscious:
     a. SET: old_xp = character.xp_current
     b. ADD: xp_per_pc TO character.xp_current
     c. OUT: "⭐ [Name]: [old_xp] + [xp_per_pc] = [character.xp_current]"

     d. IF character.xp_current >= character.xp_next_level:
          CALL: Level_Check_Protocol WITH character

4. UPDATE: party_state
5. RETURN
```

## PROTOCOL: Level_Check_Protocol

**TRIGGER**: Character XP exceeds threshold
**INPUT**: character
**GUARD**: character.xp_current >= character.xp_next_level

**PROCEDURE**:
```
1. CALC: new_level = current_level + 1
2. OUT: "🎉 LEVEL UP! [Name] reached level [new_level]!"

3. CALL: Level_Up_Protocol WITH character, new_level

4. RETURN
```

## PROTOCOL: Level_Up_Protocol

**TRIGGER**: Character levels up
**INPUT**: character, new_level
**GUARD**: new_level == current_level + 1

**PROCEDURE**:
```
1. SET: character.level = new_level
2. SET: character.xp_next_level = xp_table[new_level + 1]
3. UPDATE: character.proficiency_bonus FROM proficiency_table

4. PROMPT: "Roll for HP increase (or take average):"
5. ⛔ WAIT: choice
6. IF roll:
     a. PROMPT: "Roll your hit die:"
     b. ⛔ WAIT: roll
     c. ADD: roll + constitution_modifier TO hp_max
7. ELSE:
     a. CALC: average = (hit_die / 2) + 1 + constitution_modifier
     b. ADD: average TO hp_max

8. SET: character.hp_current = character.hp_max
9. SET: character.hit_dice_total += 1

10. ⚠️ VALIDATE: HP Increase
      a. CHECK: character.hp_max > previous_hp_max
      b. CHECK: character.hp_current == character.hp_max
      c. IF validation_failed:
           OUT: "⚠️ HP validation failed - recalculating"
           RETURN to step 5 (retry HP increase)

11. IF new_level IN [4, 8, 12, 16, 19]:
      CALL: ASI_or_Feat_Protocol WITH character

12. IF class_gains_feature_at_this_level:
      OUT: "New class features: [list]"
      ⚠️ SENTINEL: No auto-assign class features
      IF features_require_choices:
        ⚠️ CRITICAL: NEVER auto-assign class feature choices - player agency required
        FOR EACH choice_required:
          PROMPT: "[Choice description] - Choose from: [valid_options]"
          ⛔ WAIT: selection
          VALIDATE: selection IN valid_options
          IF validation_failed:
            OUT: "⚠️ Invalid choice for [feature_name]"
            RETRY current choice
          APPLY: selection
          OUT: "✓ [Feature_name]: [selection] selected"

13. IF spellcaster AND gains_spell_slots:
      UPDATE: spell_slots according to class table
      OUT: "New spell slots: [display]"

      ⚠️ VALIDATE: Spell Slots Match Class Table
      a. GET: expected_slots FROM class_spell_progression[class][new_level]
      b. CHECK: character.spells.spell_slots == expected_slots
      c. IF validation_failed:
           OUT: "⚠️ Spell slot mismatch - recalculating from class table"
           SET: character.spells.spell_slots = expected_slots
           OUT: "✓ Spell slots corrected to match level [new_level]"

      IF gains_new_spells_known:
        PROMPT: "Learn [number] new spells. Which spells?"
        ⛔ WAIT: spell_choices
        VALIDATE:
          - count == number_allowed
          - all spells IN class_spell_list
          - all spells accessible at new_level
        IF validation_failed:
          OUT: "⚠️ Invalid spell selection (count: [count], allowed: [number_allowed])"
          RETURN to "Learn new spells" prompt
        ADD: spells TO character.spells_known

14. OUT: "✓ [Name] is now level [new_level]!"
15. SHOW: updated character sheet summary

16. ⚠️ CHECKPOINT: Level-up integrity validation
    a. VERIFY: character.level == new_level
    b. VERIFY: character.proficiency_bonus matches proficiency_table[new_level]
    c. VERIFY: character.hit_dice_total == new_level
    d. VERIFY: character.hp_current == character.hp_max
    e. IF spellcaster:
         VERIFY: spell_slots match class_spell_progression[class][new_level]
         VERIFY: spells_known count valid for class/level
         VERIFY: all spells have {name, level, prepared/known} fields
    f. IF validation_failed:
         OUT: "⚠️ CRITICAL: Level-up integrity check failed"
         OUT: "Violations detected:"
         FOR EACH failed_check:
           OUT: "  - [check_name]: Expected [expected], Got [actual]"
         PROMPT: "ROLLBACK to level [previous_level]? (yes/no)"
         ⛔ WAIT: rollback_choice
         IF rollback_choice == "yes":
           ROLLBACK: character state to pre-level-up snapshot
           OUT: "✓ Rolled back to level [previous_level]"
           RETURN (level-up aborted)
         ELSE:
           OUT: "⚠️ Proceeding with invalid state - manual correction needed"

17. UPDATE: party_state
18. RETURN
```

## PROTOCOL: ASI_or_Feat_Protocol

**TRIGGER**: Character at ASI level (4, 8, 12, 16, 19)
**INPUT**: character
**GUARD**: character.level IN [4, 8, 12, 16, 19]

**PROCEDURE**:
```
1. OUT:
   "Ability Score Improvement or Feat:
   1. +2 to one ability score (or +1 to two)
   2. Take a feat

   Choose option:"

2. ⛔ WAIT: choice

3. IF choice == "1" OR "asi":
     a. OUT:
        "ASI Options:
        1. +2 to one ability
        2. +1 to two abilities

        Choose:"
     b. ⛔ WAIT: asi_option

     c. IF asi_option == "1":
          PROMPT: "Which ability gets +2? (STR/DEX/CON/INT/WIS/CHA)"
          ⛔ WAIT: ability
          ADD: 2 TO character.abilities[ability].score (max 20)
          RECALC: modifier

     d. ELSE IF asi_option == "2":
          PROMPT: "First ability to increase:"
          ⛔ WAIT: ability1
          PROMPT: "Second ability to increase:"
          ⛔ WAIT: ability2
          ADD: 1 TO character.abilities[ability1].score (max 20)
          ADD: 1 TO character.abilities[ability2].score (max 20)
          RECALC: modifiers

4. ELSE IF choice == "2" OR "feat":
     a. OUT: "Which feat? (provide feat name)"
     b. ⛔ WAIT: feat_name
     c. CHECK: feat_exists AND prerequisites_met
     d. IF validation_failed:
          OUT: "Invalid or prerequisites not met."
          GOTO step 1
     e. APPLY: feat_effects
     f. ADD: feat TO character.feats

5. UPDATE: derived_stats (AC, saves, etc.) based on new scores
6. OUT: "✓ Applied: [choice_description]"
7. UPDATE: party_state
8. RETURN
```

---

# SECTION 9: QUEST & LOOT MANAGEMENT

## PROTOCOL: Quest_Progress_Update_Protocol

**TRIGGER**: Quest objective completed during gameplay
**INPUT**: quest_id, objective_id, progress_description
**GUARD**: quest_id IN party_state.campaign_state.quests_active

**PROCEDURE**:
```
1. GET: quest FROM campaign.quests WHERE quest.quest_id = quest_id
2. IF quest NOT found: OUT "Quest not found" → RETURN

3. IF objective_id PROVIDED:
     FIND: objective IN quest.objectives WHERE objective.objective_id = objective_id
     SET: objective.completed = true
     OUT: "✓ Quest Objective Complete: [objective.description]"

4. IF progress_description PROVIDED:
     SET: quest.progress = progress_description
     OUT: "📝 Quest Progress Updated: [progress_description]"

5. CHECK: all_objectives_complete = ALL(quest.objectives.completed == true)
6. IF all_objectives_complete:
     OUT: "⚠️ All objectives complete! Return to [quest.quest_giver] to complete quest."

7. UPDATE: party_state
8. RETURN
```

⚠️ **SENTINEL**: Always update quest.progress when investigation reveals quest-relevant information

## PROTOCOL: Quest_Accept_Protocol

**TRIGGER**: Player accepts quest
**INPUT**: quest_id
**GUARD**: quest_exists AND quest_available

**PROCEDURE**:
```
1. GET: quest FROM campaign.quests
2. MOVE: quest_id FROM quests_available TO quests_active
3. OUT: "✓ Quest accepted: [quest_name]"
4. SHOW: quest objectives
5. UPDATE: party_state
6. RETURN
```

## PROTOCOL: Quest_Completion_Protocol

**TRIGGER**: Quest objectives met
**INPUT**: quest_id
**GUARD**: quest_active AND objectives_complete

**PROCEDURE**:
```
1. GET: quest FROM campaign.quests
2. MOVE: quest_id FROM quests_active TO quests_completed

3. OUT: "🎉 QUEST COMPLETE: [quest_name]!"

4. IF quest.rewards.xp:
     a. CALC: xp_per_pc = quest.rewards.xp ÷ num_pcs
     b. OUT: "⭐ Quest XP: [total] ÷ [num] = [each]"
     c. FOR EACH character:
          old_xp = character.xp_current
          character.xp_current += xp_per_pc
          OUT: "⭐ [Name]: [old] + [gained] = [new]"
     d. CHECK: level_up_threshold FOR each character

5. IF quest.rewards.gold:
     a. CALC: gold_per_pc = quest.rewards.gold ÷ num_pcs
     b. FOR EACH character:
          old_gold = character.inventory.gold
          character.inventory.gold += gold_per_pc
          OUT: "💰 [Name]: [old] + [gold_per_pc] = [new] gp"

6. IF quest.rewards.items:
     CALL: Loot_Distribution_Protocol WITH quest.rewards.items

7. IF quest.reputation_change:
     FOR reputation_effect IN quest.reputation_change:
       CALL: Track_Reputation_Change WITH effect

8. IF quest.triggers_events:
     CALL: Handle_Quest_Chain_Trigger WITH quest.quest_relationships

9. UPDATE: party_state
10. RETURN
```

## PROTOCOL: Loot_Distribution_Protocol

**TRIGGER**: Loot available for distribution
**INPUT**: loot_list
**GUARD**: loot_exists

**PROCEDURE**:
```
1. SHOW: available loot with descriptions

2. OUT:
   "Loot Distribution:
   [List items]

   ---
   1. Distribute items (who gets what?)
   2. Sell all and split gold
   3. Store in party inventory

   How do you want to handle this?"

3. ⛔ WAIT: choice

4. SWITCH choice:
     CASE "1" OR "distribute":
       FOR item IN loot_list:
         a. PROMPT: "Who takes [item_name]? (character name)"
         b. ⛔ WAIT: recipient
         c. CHECK: recipient IN party
         d. CALL: Encumbrance_Check WITH recipient BEFORE adding item
         e. IF over_capacity: OUT "⚠️ [recipient] cannot carry this!" → PROMPT for different recipient → GOTO step 4.a
         d. ADD: item TO recipient.inventory
         e. OUT: "✓ [Recipient] received [item_name]"

     CASE "2" OR "sell":
       a. CALC: total_value FROM loot_list
       b. CALC: gold_per_pc = total_value ÷ num_pcs
       c. FOR EACH character:
            old_gold = character.inventory.gold
            character.inventory.gold += gold_per_pc
            OUT: "💰 [Name]: [old] + [gold_per_pc] = [new] gp"

     CASE "3" OR "store":
       ADD: loot_list TO party_resources.shared_items
       OUT: "✓ Items stored in party inventory"

     DEFAULT:
       OUT: "Invalid choice."
       GOTO step 2

5. UPDATE: party_state
6. RETURN
```

## PROTOCOL: Handle_Quest_Chain_Trigger

**TRIGGER**: Quest completion triggers other events
**INPUT**: trigger_object
**GUARD**: trigger_object_exists

**PROCEDURE**:
```
1. FOR trigger IN trigger_object.effects:
     a. CHECK: trigger.condition (if any)
     b. IF condition_not_met THEN CONTINUE

     c. SWITCH trigger.type:
          CASE "npc_reaction":
            CALL: Handle_NPC_Reaction_Change WITH trigger

          CASE "quest_unlock":
            GET: new_quest
            ADD: new_quest TO quests_available
            OUT: "New quest available: [quest_name]"

          CASE "world_change":
            SET: story_flag = trigger.value
            IF trigger.announced THEN
              NARRATE: change

          CASE "price_change":
            UPDATE: npc.price_modifier

          CASE "location_change":
            UPDATE: location_state

2. UPDATE: world_state
3. RETURN
```

## PROTOCOL: Player_Action_Reputation_Protocol

**TRIGGER**: Player performs reputation-affecting action
**INPUT**: action_type (heroic|theft|murder|betrayal|charity|intimidation), witnesses_present, location_id
**GUARD**: none

**PROCEDURE**:
```
1. DETERMINE reputation_impacts based on action_type:

   CASE "heroic" (saving life, defeating evil):
     SET: regional_fame_gain = +5
     SET: witness_reputation_gain = +2
     OUT: "✨ Heroic action witnessed!"

   CASE "theft" (stealing, pickpocketing):
     SET: regional_infamy_gain = +10
     SET: witness_reputation_loss = -3
     OUT: "👁️ Witnesses saw the theft!"

   CASE "murder" (killing non-hostile NPC):
     SET: regional_infamy_gain = +25
     SET: witness_reputation_loss = -5
     OUT: "💀 Murder witnessed - authorities alerted!"

   CASE "betrayal" (breaking trust, lying to ally):
     SET: target_reputation_loss = -4
     OUT: "🗡️ Trust broken!"

   CASE "charity" (giving gold/items to poor):
     SET: regional_fame_gain = +3
     SET: witness_reputation_gain = +1
     OUT: "💝 Generous act noticed!"

   CASE "intimidation" (threatening NPCs):
     SET: regional_infamy_gain = +5
     SET: witness_reputation_loss = -2
     OUT: "😨 Intimidation creates fear!"

2. IF witnesses_present:
     FOR witness IN witnesses_present:
       CALL: Track_Reputation_Change WITH type="npc", target_id=witness.npc_id, change_value=[calculated], reason="Witnessed [action_type]"

3. IF location_id PROVIDED:
     GET: region_id FROM campaign.locations[location_id].region
     IF regional_fame_gain: ADD regional_fame_gain TO party_state.reputation.regions[region_id].fame
     IF regional_infamy_gain: ADD regional_infamy_gain TO party_state.reputation.regions[region_id].infamy

4. UPDATE: party_state
5. RETURN
```

⚠️ **SENTINEL**: Player actions have consequences - track reputation changes

## PROTOCOL: Track_Reputation_Change

**TRIGGER**: Action affects reputation
**INPUT**: type (npc|faction|region), target_id, change_value, reason
**GUARD**: valid_reputation_type

**PROCEDURE**:
```
1. SWITCH type:
     CASE "npc":
       a. FIND_OR_CREATE: npc IN reputation.npcs
       b. ADD: change_value (clamp -10 to +10)
       c. UPDATE: notes WITH reason
       d. DETERMINE: attitude FROM reputation_table

     CASE "faction":
       a. FIND_OR_CREATE: faction IN reputation.factions
       b. ADD: change_value (clamp -10 to +10)
       c. UPDATE: rank based on thresholds

     CASE "region":
       a. FIND_OR_CREATE: region IN reputation.regions
       b. IF change_value > 0 THEN
            ADD to fame (clamp 0-100)
          ELSE
            ADD abs(value) to infamy (clamp 0-100)
       c. ADD: reason TO known_deeds

2. IF abs(change_value) >= 3:
     OUT: "Reputation changed: [description]"
3. ELSE:
     LOG: silently

4. UPDATE: party_state
5. RETURN
```
