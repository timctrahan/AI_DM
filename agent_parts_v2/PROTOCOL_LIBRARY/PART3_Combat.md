# PROTOCOL LIBRARY - PART 3: COMBAT

---

[PROTOCOL_START: proto_combat_init]
## PROTOCOL: Combat_Initiation_Protocol

**TRIGGER**: Combat begins (player attacks, enemy ambush, etc.)
**INPUT**: enemies (list of enemy objects from encounter or campaign vault)
**GUARD**: party_conscious

**PURPOSE**: Initialize combat, roll initiative, set up turn order

**PROCEDURE**:
```yaml
Combat_Initiation_Protocol:
  1. ANNOUNCE_COMBAT:
       OUTPUT: "⚔️ COMBAT INITIATED!"
       OUTPUT: ""

  2. ROLL_INITIATIVE:
       initiative_order = []

       FOR character IN party_state.characters:
         ROLL: d20 + character.initiative_bonus
         OUTPUT: "🎲 {character.name} Initiative: {d20} + {bonus} = {total}"
         ADD: {name: character.name, initiative: total, is_enemy: false, hp: character.hp_current, hp_max: character.hp_max} TO initiative_order

       FOR enemy IN enemies:
         ROLL: d20 + enemy.initiative_bonus
         OUTPUT: "🎲 {enemy.name} Initiative: {d20} + {bonus} = {total}"
         ADD: {name: enemy.name, initiative: total, is_enemy: true, hp: enemy.hp_max, hp_max: enemy.hp_max} TO initiative_order

  3. SORT_INITIATIVE:
       SORT initiative_order BY initiative DESC (highest first)

  4. DISPLAY_TURN_ORDER:
       OUTPUT: ""
       OUTPUT: "━━━ TURN ORDER ━━━"
       FOR combatant IN initiative_order:
         OUTPUT: "{combatant.initiative}: {combatant.name}"
       OUTPUT: "━━━━━━━━━━━━━━━━━━━"

  5. SET_COMBAT_STATE:
       party_state.location.in_combat = true
       party_state.combat_state.active = true
       party_state.combat_state.round = 1
       party_state.combat_state.initiative_order = initiative_order
       party_state.combat_state.current_turn = initiative_order[0].name

  6. CALL: proto_combat_round

  7. RETURN
```

**OUTPUT**: Combat initialized, first round begins
[PROTOCOL_END: proto_combat_init]

---

[PROTOCOL_START: proto_combat_round]
## PROTOCOL: Combat_Round_Protocol

**TRIGGER**: Called by Combat_Init or end of previous round
**GUARD**: combat_active

**PURPOSE**: Manage turn order within a combat round

**PROCEDURE**:
```yaml
Combat_Round_Protocol:
  1. CHECK_COMBAT_END:
       all_enemies_dead = ALL(combatant WHERE is_enemy AND hp <= 0)
       all_party_dead = ALL(combatant WHERE NOT is_enemy AND hp <= 0)

       IF all_enemies_dead OR all_party_dead:
         CALL: proto_combat_end
         RETURN

  2. DISPLAY_ROUND_START (if new round):
       OUTPUT: "━━━ ROUND {party_state.combat_state.round} ━━━"

  3. PROCESS_TURNS:
       FOR combatant IN party_state.combat_state.initiative_order:
         IF combatant.hp <= 0:
           SKIP (dead/unconscious)

         party_state.combat_state.current_turn = combatant.name

         IF combatant.is_enemy:
           CALL: proto_enemy_turn WITH combatant
         ELSE:
           CALL: proto_player_turn WITH combatant

         CHECK: combat still active (might end mid-round)
         IF NOT combat_active:
           RETURN

  4. INCREMENT_ROUND:
       party_state.combat_state.round += 1

  5. LOOP:
       CALL: proto_combat_round (recursive until combat ends)

  6. RETURN
```

**OUTPUT**: All combatants take turns, round ends
[PROTOCOL_END: proto_combat_round]

---

[PROTOCOL_START: proto_player_turn]
## PROTOCOL: Player_Combat_Turn_Protocol

**TRIGGER**: Player's turn in combat
**INPUT**: character (combatant object)
**GUARD**: character_conscious

**PURPOSE**: Handle player's combat actions (attack, cast spell, use item, etc.)

**PROCEDURE**:
```yaml
Player_Combat_Turn_Protocol:
  1. ANNOUNCE_TURN:
       OUTPUT: ""
       OUTPUT: "━━━ {character.name}'s TURN ━━━"
       OUTPUT: "❤️ HP: {character.hp_current}/{character.hp_max}"
       IF character.conditions:
         OUTPUT: "🧙 Conditions: {list conditions}"

  2. DISPLAY_ACTIONS:
       OUTPUT: "---"
       OUTPUT: "1. Attack with weapon"
       OUTPUT: "2. Cast a spell"
       OUTPUT: "3. Use an item"
       OUTPUT: "4. Dash / Disengage / Dodge / Help"
       OUTPUT: "5. Other (describe)"
       OUTPUT: ""
       OUTPUT: "What does {character.name} do?"

       ⛔ WAIT: action_choice

  3. RESOLVE_ACTION:
       SWITCH action_choice:
         CASE "attack" OR "1":
           CALL: proto_attack_action WITH character
         CASE "spell" OR "2":
           CALL: proto_cast_spell WITH character
         CASE "item" OR "3":
           CALL: proto_use_item WITH character
         CASE "dash" OR "disengage" OR "dodge" OR "help":
           OUTPUT: "{character.name} uses {action}."
           # Narrate effect
         DEFAULT:
           OUTPUT: "Describe what {character.name} does:"
           ⛔ WAIT: custom_action
           # Resolve based on description

  4. CHECK_REACTIONS:
       # If enemy attacks this character later, opportunity for Shield spell, etc.
       character.reaction_available = true

  5. END_TURN:
       OUTPUT: "--- {character.name}'s turn ends ---"

  6. RETURN
```

**OUTPUT**: Player's turn completed
[PROTOCOL_END: proto_player_turn]

---

[PROTOCOL_START: proto_attack_action]
## PROTOCOL: Attack_Action_Protocol

**TRIGGER**: Player attacks in combat
**INPUT**: character (attacker)
**GUARD**: character has weapon or unarmed

**PURPOSE**: Resolve attack rolls, damage, update enemy HP

**PROCEDURE**:
```yaml
Attack_Action_Protocol:
  1. SELECT_WEAPON:
       OUTPUT: "Attack with:"
       FOR weapon IN character.inventory.equipment WHERE type == "weapon":
         OUTPUT: "- {weapon.name} ({weapon.damage})"
       ⛔ WAIT: weapon_choice

  2. SELECT_TARGET:
       OUTPUT: "Target:"
       FOR enemy IN combat_state.initiative_order WHERE is_enemy AND hp > 0:
         OUTPUT: "- {enemy.name} (AC {enemy.ac}, HP {enemy.hp}/{enemy.hp_max})"
       ⛔ WAIT: target_choice

  3. ROLL_ATTACK:
       OUTPUT: "Roll attack or auto? (self/auto)"
       ⛔ WAIT: roll_choice

       IF roll_choice == "self":
         OUTPUT: "What did you roll? (d20 result)"
         ⛔ WAIT: d20_result
         attack_roll = d20_result
       ELSE:
         ROLL: d20
         attack_roll = roll_result

       attack_bonus = character.proficiency_bonus + character.ability_modifiers[weapon.ability]
       total = attack_roll + attack_bonus

       OUTPUT: "🎲 Attack: {d20} + {attack_bonus} = {total} vs AC {target.ac}"

  4. DETERMINE_HIT:
       IF attack_roll == 20:
         OUTPUT: "💥 CRITICAL HIT!"
         is_crit = true
         hit = true
       ELSE IF attack_roll == 1:
         OUTPUT: "❌ CRITICAL MISS!"
         hit = false
       ELSE IF total >= target.ac:
         OUTPUT: "✓ HIT!"
         hit = true
       ELSE:
         OUTPUT: "❌ MISS!"
         hit = false

  5. ROLL_DAMAGE (if hit):
       IF is_crit:
         # Double damage dice
         damage_dice = weapon.damage + weapon.damage
       ELSE:
         damage_dice = weapon.damage

       ROLL: damage_dice + ability_modifier
       damage = roll_result

       OUTPUT: "💥 Damage: {damage_dice} + {modifier} = {damage} {damage_type}"

       target.hp -= damage

       OUTPUT: "❤️ {target.name}: {old_hp} - {damage} = {target.hp} HP"

       IF target.hp <= 0:
         OUTPUT: "💀 {target.name} is defeated!"
         CALL: proto_handle_creature_death WITH target

  6. RETURN
```

**OUTPUT**: Attack resolved, damage applied
[PROTOCOL_END: proto_attack_action]

---

[PROTOCOL_START: proto_enemy_turn]
## PROTOCOL: Enemy_Combat_Turn_Protocol

**TRIGGER**: Enemy's turn in combat
**INPUT**: enemy (combatant object)
**GUARD**: enemy_alive

**PURPOSE**: AI-controlled enemy takes actions

**PROCEDURE**:
```yaml
Enemy_Combat_Turn_Protocol:
  1. ANNOUNCE_TURN:
       OUTPUT: ""
       OUTPUT: "━━━ {enemy.name}'s TURN ━━━"

  2. DETERMINE_ACTION:
       # Simplified AI - attacks nearest/weakest target
       valid_targets = FILTER party_state.characters WHERE hp_current > 0
       target = SELECT valid_targets ORDER BY hp_current ASC (weakest first)

  3. ATTACK:
       ROLL: d20 + enemy.attack_bonus
       attack_total = roll_result

       OUTPUT: "🎲 {enemy.name} attacks {target.name}"
       OUTPUT: "🎲 Attack: {d20} + {enemy.attack_bonus} = {attack_total} vs AC {target.ac}"

       IF attack_total >= target.ac:
         ROLL: enemy.damage_dice
         damage = roll_result

         OUTPUT: "✓ HIT!"
         OUTPUT: "💥 Damage: {damage} {damage_type}"

         target.hp_current -= damage

         OUTPUT: "❤️ {target.name}: {old_hp} - {damage} = {target.hp_current}/{target.hp_max} HP"

         IF target.hp_current <= 0:
           OUTPUT: "💀 {target.name} is unconscious!"
           CALL: proto_death_saves_init WITH target

       ELSE:
         OUTPUT: "❌ MISS!"

  4. END_TURN:
       OUTPUT: "--- {enemy.name}'s turn ends ---"

  5. RETURN
```

**OUTPUT**: Enemy's turn completed
[PROTOCOL_END: proto_enemy_turn]

---

[PROTOCOL_START: proto_death_saves]
## PROTOCOL: Death_Saves_Protocol

**TRIGGER**: Character at 0 HP at start of their turn
**INPUT**: character
**GUARD**: character.hp_current == 0

**PURPOSE**: Handle death saving throws for unconscious characters

**PROCEDURE**:
```yaml
Death_Saves_Protocol:
  1. ANNOUNCE:
       OUTPUT: "⚠️ {character.name} is UNCONSCIOUS and must make a death saving throw!"
       OUTPUT: "Successes: {character.death_saves.successes}/3"
       OUTPUT: "Failures: {character.death_saves.failures}/3"

  2. ROLL_SAVE:
       OUTPUT: "Roll d20 for death save (or auto):"
       ⛔ WAIT: roll_choice

       IF roll_choice == "auto":
         ROLL: d20
         save_roll = roll_result
       ELSE:
         OUTPUT: "What did you roll?"
         ⛔ WAIT: save_roll

       OUTPUT: "🎲 Death Save: {save_roll}"

  3. RESOLVE:
       IF save_roll == 20:
         OUTPUT: "💚 NATURAL 20! {character.name} regains 1 HP and is conscious!"
         character.hp_current = 1
         character.death_saves.successes = 0
         character.death_saves.failures = 0
         RETURN

       ELSE IF save_roll == 1:
         OUTPUT: "💀 NATURAL 1! Counts as 2 failures!"
         character.death_saves.failures += 2

       ELSE IF save_roll >= 10:
         OUTPUT: "✓ Success!"
         character.death_saves.successes += 1

       ELSE:
         OUTPUT: "❌ Failure!"
         character.death_saves.failures += 1

  4. CHECK_DEATH:
       IF character.death_saves.successes >= 3:
         OUTPUT: "💚 {character.name} is STABLE (unconscious but not dying)"
         # Reset death saves
         character.death_saves.successes = 0
         character.death_saves.failures = 0

       ELSE IF character.death_saves.failures >= 3:
         OUTPUT: "💀💀💀 {character.name} has DIED!"
         # Character is dead (permanent unless resurrected)

  5. RETURN
```

**OUTPUT**: Death save resolved
[PROTOCOL_END: proto_death_saves]

---

[PROTOCOL_START: proto_combat_end]
## PROTOCOL: Combat_End_Protocol

**TRIGGER**: All enemies defeated OR all party members unconscious
**GUARD**: combat_active

**PURPOSE**: End combat, award XP, handle loot

**PROCEDURE**:
```yaml
Combat_End_Protocol:
  1. DETERMINE_OUTCOME:
       IF ALL enemies defeated:
         outcome = "victory"
       ELSE IF ALL party unconscious/dead:
         outcome = "defeat"

  2. ANNOUNCE_END:
       OUTPUT: ""
       OUTPUT: "━━━ COMBAT ENDS ━━━"

       IF outcome == "victory":
         OUTPUT: "✓ Victory!"

       ELSE:
         OUTPUT: "💀 Defeat!"
         # Handle TPK or capture scenario
         RETURN

  3. AWARD_XP (if victory):
       total_xp = SUM(enemy.xp_value FOR enemy IN defeated_enemies)

       CALL: proto_xp_award WITH total_xp

  4. LOOT (if victory):
       FOR enemy IN defeated_enemies:
         IF enemy.loot:
           OUTPUT: "{enemy.name} drops:"
           FOR item IN enemy.loot:
             OUTPUT: "- {item.name}"

           CALL: proto_loot_distribution WITH enemy.loot

  5. RESET_COMBAT_STATE:
       party_state.location.in_combat = false
       party_state.combat_state.active = false
       party_state.combat_state.round = 0
       party_state.combat_state.initiative_order = []
       party_state.combat_state.current_turn = null

       FOR character IN party_state.characters:
         character.death_saves.successes = 0
         character.death_saves.failures = 0

  6. RETURN: to Exploration_Protocol
```

**OUTPUT**: Combat ended, XP awarded, loot distributed
[PROTOCOL_END: proto_combat_end]

---

## END OF PART 3: COMBAT
