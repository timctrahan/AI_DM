# SECTION 7: COMBAT PROTOCOLS

## PROTOCOL: Combat_Initiation_Protocol

**TRIGGER**: Combat encounter
**INPUT**: enemy_group
**GUARD**: not_already_in_combat AND enemy_group_valid

**PROCEDURE**:
```
1. OUT: "⚔️ COMBAT INITIATED!"
2. DESCRIBE: enemies and tactical situation

3. SET: party_state.location.in_combat = true
4. SET: party_state.combat_state.active = true
5. SET: party_state.combat_state.round = 1

6. ROLL initiative: FOR character: d20 + bonus → OUT 🎲; FOR enemy: same

7-9. SORT by initiative → SET combat_state.initiative_order + current_turn

10-11. OUT "Initiative Order:" → SHOW list

12. OUT: "---"
13. PROMPT: "You have the initiative. What is your opening move?"
14. ⛔ STOP AND WAIT for player action

15. CALL Combat_Round_Protocol
```

## PROTOCOL: Combat_Round_Protocol

**TRIGGER**: Combat active
**GUARD**: combat_active AND initiative_order_exists

**PROCEDURE**:
```
1. RESET: all combatants reaction_available = true

2. OUT: "--- ⚔️ COMBAT STATUS: ROUND [round] ---"
   OUT: "ENEMIES:"
   FOR enemy IN initiative_order WHERE enemy.is_enemy AND enemy.hp > 0:
     CALC: status = (enemy.hp/enemy.max_hp > 0.7) ? "Healthy" : (> 0.3) ? "Bloody" : "Critical"
     OUT: "- [enemy.name]: [enemy.hp]/[enemy.max_hp] HP (Status: [status])" + (conditions ? " [conditions]" : "")

   OUT: "ALLIES:"
   FOR ally IN initiative_order WHERE ally.is_player AND ally.hp > 0:
     GET: spell_slots_display = ""
     IF ally.spells EXISTS:
       SET: spell_slots_display = " | Slots: "
       FOR level IN [1-9]:
         IF ally.spell_slots.level_[level].max > 0:
           spell_slots_display += "[level]:[current]/[max] "
     OUT: "- [ally.name] (AC [ally.armor_class]): [ally.hp]/[ally.max_hp] HP[spell_slots_display]" + (conditions ? " | [conditions]" : "")
   OUT: "---"

3. FOR combatant IN initiative_order:
     SKIP if hp <= 0
     SET current_turn = combatant
     OUT "[Name]'s turn"
     IF player: CALL Player_Combat_Turn_Protocol; ELSE: CALL Enemy_Combat_Turn_Protocol
     CHECK combat_end → IF all_defeated: CALL Combat_End_Protocol → RETURN

4. INC combat_state.round
5. RETURN to Game_Loop
```

## PROTOCOL: Player_Combat_Turn_Protocol

**TRIGGER**: Player's turn in combat
**INPUT**: character
**GUARD**: character.hp_current > 0 AND character_not_incapacitated

**PROCEDURE**:
```
1. OUT: "--- 1. Attack 2. Dodge 3. Disengage 4. Dash 5. Help 6. Hide 7. Ready 8. Use item 9. Other --- What does [Name] do?"

2. ⛔ WAIT: player_action

3-4. PARSE + SWITCH action_type:
     attack: PROMPT weapon/spell → ⛔ WAIT → PROMPT target → ⛔ WAIT → CALL Attack_Action_Protocol
     cast_spell: SHOW spells → PROMPT which → ⛔ WAIT → PROMPT target → ⛔ WAIT → CALL Spellcasting_Protocol
     dodge: OUT "✓ Dodging" → SET dodging condition
     disengage: OUT "✓ Disengaged" → SET condition
     dash: OUT "✓ Dashing" → SET movement_doubled
     help: PROMPT who → ⛔ WAIT → PROMPT what → ⛔ WAIT → OUT "✓ Advantage" → SET advantage
     hide: ROLL stealth → OUT 🎲 result → SET hidden
     use_item: SHOW inventory → PROMPT which → ⛔ WAIT → EXECUTE → UPDATE
     DEFAULT: OUT "Describe" → ⛔ WAIT → CALC check → IF needed: PROMPT roll → RESOLVE → NARRATE

5-7. CLEAR temp_conditions → UPDATE combat_state → RETURN
```

## PROTOCOL: Attack_Action_Protocol

**TRIGGER**: Character attacks
**INPUT**: attacker, target, weapon_or_spell
**GUARD**: attacker_conscious AND target_valid AND weapon_available

**PROCEDURE**:
```
1. CALC: attack_bonus = attacker.attack_bonus_for_weapon

2. CHECK: ammo (if ranged weapon) → IF out of ammo: OUT "❌ Out of [ammo_type]!" RETURN → DEC ammo.count → OUT "🏹 Used 1 [ammo_type] ([remaining])"

3. CHECK: lighting → IF darkness AND NOT darkvision: SET disadvantage, OUT "⚠️ Attacking in darkness - Disadvantage!"

3. ROLL: d20
4. APPLY: advantage/disadvantage if applicable
4. STORE: natural_roll = d20_result
5. CALC: total = d20 + attack_bonus

6. OUT: 🎲 Attack: [d20] + [bonus] = [total] vs AC [target.ac]

7. CHECK: natural_roll for automatic results
8. IF natural_roll == 1:
     OUT: "→ CRITICAL MISS!"
     GOTO step 14

9. IF natural_roll == 20:
     OUT: "→ CRITICAL HIT!"
     ROLL: damage_dice TWICE + ability_modifier
     OUT: 💥 Critical Damage: [total] [type]
     SUB: damage FROM target.hp_current
     OUT: ❤️ [Target]: [new_hp]/[max_hp] HP
     IF target.hp_current <= 0: CALL Handle_Creature_Death
     GOTO step 15

10. IF total >= target.ac:
      OUT: "→ HIT!"
      ROLL: damage_dice + ability_modifier
      OUT: 💥 Damage: [total] [type]
      SUB: damage FROM target.hp_current
      OUT: ❤️ [Target]: [new_hp]/[max_hp] HP
      IF target.hp_current <= 0: CALL Handle_Creature_Death

11. ELSE:
      OUT: "→ MISS!"

12. UPDATE: combat_state
13. RETURN
```

## PROTOCOL: Enemy_Combat_Turn_Protocol

**TRIGGER**: Enemy's turn
**INPUT**: enemy
**GUARD**: enemy.hp_current > 0

**PROCEDURE**:
```
1. CALC: best_action based on enemy.tactics
2. SELECT: target based on tactics (lowest HP, nearest, highest threat, etc.)

3. SWITCH action:
     CASE attack:
       CALL: Attack_Action_Protocol WITH enemy, target, enemy.weapon

     CASE special_ability:
       EXECUTE: ability (with saves if applicable)
       IF save_required THEN
         FOR EACH affected_target:
           PROMPT: "Roll [save_type] save (DC [dc]):"
           ⛔ WAIT: roll
           RESOLVE: based on result

     CASE move:
       DESCRIBE: movement
       UPDATE: position

4. NARRATE: enemy action and result
5. UPDATE: combat_state
6. RETURN to Combat_Round_Protocol
```

## PROTOCOL: Handle_Creature_Death

**TRIGGER**: Creature reaches 0 HP
**INPUT**: creature
**GUARD**: creature.hp_current <= 0

**PROCEDURE**:
```
1. IF creature IS player_character:
     a. OUT: "💀 [Name] falls unconscious!"
     b. SET: character.conditions.unconscious = true
     c. SET: character.death_saves = {successes: 0, failures: 0}
     d. CALL: Death_Saves_Protocol WITH character ON their turns

2. ELSE IF creature IS enemy:
     a. OUT: "💀 [Enemy] is defeated!"
     b. SET: enemy.hp_current = 0
     c. SET: enemy.defeated = true
     d. REMOVE: enemy FROM initiative_order
     e. ADD: enemy TO combat_state.defeated_enemies

3. RETURN
```

## PROTOCOL: Death_Saves_Protocol

**TRIGGER**: Unconscious character's turn
**INPUT**: character
**GUARD**: character.unconscious AND character.hp_current == 0

**PROCEDURE**:
```
1. OUT: "[Name]'s turn - Rolling death save..."
2. ROLL: d20

3. IF roll >= 10:
     SUCCESS: character.death_saves.successes += 1
     OUT: "🎲 Death Save: [d20] → SUCCESS ([successes]/3)"
4. ELSE:
     FAILURE: character.death_saves.failures += 1
     OUT: "🎲 Death Save: [d20] → FAILURE ([failures]/3)"

5. IF roll == 20:
     character.hp_current = 1
     character.unconscious = false
     character.death_saves = {successes: 0, failures: 0}
     OUT: "✓ [Name] regains consciousness with 1 HP!"
     RETURN

6. IF roll == 1:
     character.death_saves.failures += 1 (counts as 2 failures)
     OUT: "💀 Critical failure! That's 2 failures."

7. IF character.death_saves.successes >= 3:
     character.unconscious = false
     character.death_saves = {successes: 0, failures: 0}
     OUT: "✓ [Name] stabilizes but remains at 0 HP."

8. IF character.death_saves.failures >= 3:
     OUT: "💀 [Name] has died."
     SET: character.dead = true
     REMOVE: character FROM initiative_order

9. RETURN to Combat_Round_Protocol
```

## PROTOCOL: Opportunity_Attack_Protocol

**TRIGGER**: Enemy/ally moves out of melee reach without Disengage
**INPUT**: moving_creature, threatening_creature
**GUARD**: threatening_creature.reaction_available AND threatening_creature IN melee_range

**PROCEDURE**:
```
1. CHECK: moving_creature action_this_turn
2. IF action_this_turn == "disengage":
     OUT: "[Moving_creature] disengaged safely - no opportunity attack"
     RETURN

3. IF NOT threatening_creature.reaction_available:
     OUT: "[Threatening_creature] already used reaction this round"
     RETURN

4. IF threatening_creature.is_player:
     OUT: "⚔️ Opportunity Attack Available!"
     OUT: "[Moving_creature] is leaving your reach."
     PROMPT: "Take opportunity attack? (yes/no)"
     ⛔ WAIT: choice

     IF choice != "yes":
       OUT: "✓ Opportunity attack declined"
       RETURN

5. ELSE IF threatening_creature.is_enemy:
     OUT: "⚔️ [Enemy] takes opportunity attack against [moving_creature]!"

6. SET: threatening_creature.reaction_available = false
7. OUT: "🛡️ Reaction used - [threatening_creature] uses opportunity attack"

8. CALL: Attack_Action_Protocol WITH attacker=threatening_creature, target=moving_creature, weapon=threatening_creature.equipped_weapon

9. UPDATE: combat_state
10. RETURN
```

⚠️ **SENTINEL**: Opportunity attacks consume reactions, only one per round per creature

## PROTOCOL: Combat_End_Protocol

**TRIGGER**: Combat victory conditions met
**GUARD**: all_enemies_defeated OR all_players_defeated

**PROCEDURE**:
```
1. IF all_players_defeated:
     OUT: "💀 DEFEAT - The party has fallen."
     CALL: Handle_TPK_Protocol
     RETURN

2. OUT: "⚔️ COMBAT VICTORY!"

3. SET: party_state.location.in_combat = false
4. SET: party_state.combat_state.active = false

5. CALC: total_xp FROM defeated_enemies
6. ⚠️ MUST EXECUTE: XP_Award_Protocol WITH total_xp
7. CHECK: xp_awarded = true

8. ROLL: loot FROM defeated_enemies.loot_tables
9. IF loot_exists THEN
     CALL: Loot_Distribution_Protocol WITH loot

10. CLEAR: temporary combat conditions
11. RESET: all character.reaction_available = true
11. RESET: combat_state
12. UPDATE: party_state

13. RETURN to Game_Loop
```

## PROTOCOL: Spellcasting_Protocol

**TRIGGER**: Player chooses to cast a spell during their turn
**GUARD**: character has spell slots available OR spell is cantrip

**PROCEDURE**:
```
1. FILTER available_spells: combat ∧ prepared ∨ cantrip ∨ (level ≥ 1 ∧ slots_available)
   SHOW: available_spells
   ⛔ WAIT: spell_choice
   IF spell_choice ∉ available_spells: OUT "⚠️ Invalid spell" → RETURN

2. IF spell.level > 0:
     GET available_slot_levels
     IF multiple_levels: PROMPT slot_level → ⛔ WAIT → VALIDATE
     ELSE: SET slot_level = spell.level
     CONSUME slot_level → OUT "💫 Slot consumed: Level [slot_level]"

3. IF spell requires concentration:
     IF character already concentrating:
       PROMPT "Drop [current_spell]? (yes/no)" → ⛔ WAIT
       IF NO: RETURN (cancel)
       ELSE: CLEAR current_concentration
     SET character.concentration = spell

4. GET spell.targets
   SWITCH targeting:
     area_effect: PROMPT location → ⛔ WAIT → CALC affected → OUT "Targets: [list]" → PROMPT confirm → ⛔ WAIT
     single/multi: PROMPT selection → ⛔ WAIT → VALIDATE range/count
   SET spell_targets

5. SWITCH spell.resolution:
     attack_roll:
       FOR target IN spell_targets:
         ROLL d20 + spell_attack
         OUT "🎲 [result] vs AC [target.ac]"
         IF hit: APPLY damage + effects
         ELSE: OUT "Miss"
     saving_throw:
       FOR target IN spell_targets:
         PROMPT target: "Roll [save_type] save (DC [dc])" → ⛔ WAIT
         OUT "🎲 [result] vs DC [dc]"
         APPLY: result < dc ? full_effect : half_effect
     automatic:
       APPLY spell effects to targets
   UPDATE target HP/conditions

6. IF duration > instantaneous: ADD spell TO active_effects WITH duration

7. OUT "✓ [Spell name] cast"
8. RETURN to Player_Combat_Turn_Protocol
```

