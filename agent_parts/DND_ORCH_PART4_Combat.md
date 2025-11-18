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

12. CALL Combat_Round_Protocol
```

## PROTOCOL: Combat_Round_Protocol

**TRIGGER**: Combat active  
**GUARD**: combat_active AND initiative_order_exists

**PROCEDURE**:
```
1. OUT: "--- Round [round] ---"

2. FOR combatant IN initiative_order:
     SKIP if hp <= 0
     SET current_turn = combatant
     OUT "[Name]'s turn"
     IF player: CALL Player_Combat_Turn_Protocol; ELSE: CALL Enemy_Combat_Turn_Protocol
     CHECK combat_end → IF all_defeated: CALL Combat_End_Protocol → RETURN

3. INC combat_state.round
4. RETURN to Game_Loop
```

## PROTOCOL: Player_Combat_Turn_Protocol

**TRIGGER**: Player's turn in combat  
**INPUT**: character  
**GUARD**: character.hp_current > 0 AND character_not_incapacitated

**PROCEDURE**:
```
1. SHOW: ❤️ HP, 🛡️ AC, conditions

2. OUT: "--- 1. Attack 2. Dodge 3. Disengage 4. Dash 5. Help 6. Hide 7. Ready 8. Use item 9. Other --- What does [Name] do?"

3. ⛔ WAIT: player_action

4-5. PARSE + SWITCH action_type:
     attack: PROMPT weapon/spell → ⛔ WAIT → PROMPT target → ⛔ WAIT → CALL Attack_Action_Protocol
     cast_spell: SHOW spells → PROMPT which → ⛔ WAIT → PROMPT target → ⛔ WAIT → CALL Spellcasting_Protocol
     dodge: OUT "✓ Dodging" → SET dodging condition
     disengage: OUT "✓ Disengaged" → SET condition
     dash: OUT "✓ Dashing" → SET movement_doubled
     help: PROMPT who → ⛔ WAIT → PROMPT what → ⛔ WAIT → OUT "✓ Advantage" → SET advantage
     hide: ROLL stealth → OUT 🎲 result → SET hidden
     use_item: SHOW inventory → PROMPT which → ⛔ WAIT → EXECUTE → UPDATE
     DEFAULT: OUT "Describe" → ⛔ WAIT → DETERMINE check → IF needed: PROMPT roll → RESOLVE → NARRATE

6-8. CLEAR temp_conditions → UPDATE combat_state → RETURN
```

## PROTOCOL: Attack_Action_Protocol

**TRIGGER**: Character attacks  
**INPUT**: attacker, target, weapon_or_spell  
**GUARD**: attacker_conscious AND target_valid AND weapon_available

**PROCEDURE**:
```
1. DETERMINE: attack_bonus = attacker.attack_bonus_for_weapon
2. ROLL: d20
3. APPLY: advantage/disadvantage if applicable (roll 2d20, take highest/lowest)
4. STORE: natural_roll = d20_result (before modifiers)
5. CALC: total = d20 + attack_bonus

6. OUT: 🎲 Attack: [d20] + [bonus] = [total] vs AC [target.ac]

7. CHECK: natural_roll for automatic results
8. IF natural_roll == 1:
     OUT: "→ CRITICAL MISS! (Natural 1)"
     GOTO step 14

9. IF natural_roll == 20:
     OUT: "→ CRITICAL HIT! (Natural 20)"
     a. DETERMINE: damage_dice FROM weapon
     b. ROLL: damage_dice TWICE (roll all damage dice, then roll them again)
     c. ADD: all dice results together
     d. ADD: ability_modifier + other_bonuses (only once, not doubled)
     e. OUT: 💥 Critical Damage: [total] [type]
     f. SUB: damage FROM target.hp_current
     g. OUT: ❤️ [Target]: [new_hp]/[max_hp] HP
     h. IF target.hp_current <= 0 THEN
          CALL: Handle_Creature_Death WITH target
     i. GOTO step 15

10. IF total >= target.ac:
      a. OUT: "→ HIT!"
      b. DETERMINE: damage_dice FROM weapon
      c. ROLL: damage_dice
      d. ADD: ability_modifier + other_bonuses
      e. OUT: 💥 Damage: [total] [type]
      f. SUB: damage FROM target.hp_current
      g. OUT: ❤️ [Target]: [new_hp]/[max_hp] HP
      h. IF target.hp_current <= 0 THEN
           CALL: Handle_Creature_Death WITH target

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
1. DETERMINE: best_action based on enemy.tactics
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
11. RESET: combat_state
12. UPDATE: party_state

13. RETURN to Game_Loop
```
