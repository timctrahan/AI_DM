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
