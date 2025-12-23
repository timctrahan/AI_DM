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
