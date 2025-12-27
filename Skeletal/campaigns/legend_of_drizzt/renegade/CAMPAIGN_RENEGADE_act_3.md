# ACT 3: TWILIGHT REALMS

**Levels 6-7**

---

## PHASE_ID

```yaml
PHASE: IDENTITY_CHOICE
RESTRICTIONS:
  - Symbolic elements: limited
  - Focus: Reputation, faction politics, identity formation
```

---

## GATES

### GATE_3.1_DUERGAR_MARKET

```yaml
location_id: GRAY_DWARF_FORTRESS_MARKET
level: 6
cr: 5
npc: DUERGAR_MARKET_MASTER
npc_detail: "Duergar merchant lord, CR 3, non-combatant unless attacked"
secondary_npcs: [SLAVE_TRADERS_3, ENSLAVED_PEOPLE_12, DUERGAR_GUARDS_6]
threat_clarification: "Option 1 combat = market master CR 3 + 6 duergar guards CR 1 each"
conflict_type: IDEOLOGICAL_CONFRONTATION
conflict_id: SLAVERY_INSTITUTION

options:
  1: "Mass intimidation - shut down market"
  2: "Incremental liberation - buy and free"
  3: "Participate in market"
  4: "Negotiate reform with leadership"
  5: "Ignore and pass through"

consequences:
  option_1: { shadow: -15, combat: true, cr: 6, skill_challenge: "Intimidation DC 18", rep_duergar: -40, rep_deep_gnomes: +25, rep_surface_kingdoms: +10, flags: [MARKET_DESTROYER], companion_reaction: "Archer approves if present" }
  option_2: { shadow: -8, gold: -800, rep_duergar: -15, rep_deep_gnomes: +15, flags: [GRADUAL_LIBERATOR] }
  option_3: { shadow: +10, gold: +500, rep_duergar: +10, rep_deep_gnomes: -25, flags: [SLAVER_PARTICIPANT], companion_reaction: "Archer leaves if present" }
  option_4: { shadow: -5, skill_challenge: "Persuasion DC 20", rep_duergar: +5, flags: [REFORMER] }
  option_5: { shadow: +5, flags: [APATHETIC] }

branches:
  all: GATE_3.2_SURFACE_RUMORS
```

---

### GATE_3.2_SURFACE_RUMORS

```yaml
location_id: UNDERGROUND_TAVERN
level: 6
cr: 0
npc: INFORMATION_BROKER
secondary_npcs: [TRAVELERS, SURFACE_REFUGEES]
conflict_type: MOTIVATION_DEFINITION
conflict_id: SURFACE_GOAL

options:
  1: "I'll prove drow can be more (redemption)"
  2: "I'll show them drow strength (conquest)"
  3: "I just want freedom (survival)"
  4: "I'll return with power (underdark return)"

consequences:
  option_1: { shadow: -7, flags: [REDEMPTION_SEEKING] }
  option_2: { shadow: +10, flags: [CONQUEST_SEEKING] }
  option_3: { shadow: 0, flags: [NEUTRAL_SEEKING] }
  option_4: { shadow: +8, flags: [RETURN_TO_UNDERDARK] }

branches:
  all: GATE_3.3_ARCHER_ENCOUNTER
```

---

### GATE_3.3_ARCHER_ENCOUNTER

```yaml
location_id: SURFACE_TUNNEL_APPROACH
level: 7
cr: 4
npc: HUMAN_ARCHER
npc_detail: "Potential companion - render from overview HUMAN_ARCHER, currently leading defenders"
secondary_npcs: [SURFACE_DEFENDERS_4, UNDERDARK_RAIDERS_6]
threat_clarification: "Option 1 = fight raiders (6 drow scouts CR 1/2). Option 2 = fight defenders (4 human guards CR 1/8 + archer)"
conflict_type: FIRST_IMPRESSION
conflict_id: SURFACE_CONTACT

options:
  1: "Aid defenders against raiders"
  2: "Join raiders in attack"
  3: "Negotiate cease-fire"
  4: "Flee the conflict"

consequences:
  option_1: { shadow: -8, combat: true, cr: 5, companion_join: HUMAN_ARCHER, rep_surface_kingdoms: +20, flags: [SURFACE_ALLY, ARCHER_ALLY] }
  option_2: { shadow: +15, combat: true, cr: 4, rep_surface_kingdoms: -40, flags: [SURFACE_ENEMY], companion_reaction: "Dwarf/Halfling may leave" }
  option_3: { shadow: 0, skill_challenge: "Persuasion DC 18", flags: [PEACEMAKER] }
  option_4: { shadow: +3, flags: [COWARD] }

branches:
  option_1: GATE_3.4_BARBARIAN_TRIAL
  option_2: GATE_3.4_SURFACE_EMERGENCE
  option_3: GATE_3.4_BARBARIAN_TRIAL
  option_4: GATE_3.4_SURFACE_EMERGENCE
```

---

### GATE_3.4_BARBARIAN_TRIAL

```yaml
location_id: SURFACE_TRIBAL_LANDS
level: 7
cr: 3
npc: NORTHERN_BARBARIAN
npc_detail: "Potential companion - render from overview BARBARIAN_WARRIOR, challenges you to prove worth"
secondary_npcs: [TRIBAL_WARRIORS_8, CHIEFTAIN_1]
threat_clarification: "Duel is 1v1 against barbarian only. Option 4 dishonorable = tribe joins (8 berserkers CR 1/2)"
conflict_type: HONOR_TEST
conflict_id: PROVE_STRENGTH

options:
  1: "Honorable duel - fight fairly"
  2: "Brutal victory - dominate utterly"
  3: "Refuse duel - talk past"
  4: "Dishonorable tactics"

consequences:
  option_1: { shadow: -3, combat: true, cr: 3, xp_award: 700, companion_join: BARBARIAN_WARRIOR, rep_northern_tribes: +15, flags: [HONORABLE, BARBARIAN_ALLY] }
  option_2: { shadow: +7, combat: true, cr: 3, xp_award: 700, companion_join: BARBARIAN_WARRIOR, rep_northern_tribes: +10, flags: [BRUTAL] }
  option_3: { shadow: 0, skill_challenge: "Persuasion DC 15", xp_award: 700, rep_northern_tribes: +5, flags: [CLEVER] }
  option_4: { shadow: +12, combat: true, cr: 4, xp_award: 1100, rep_northern_tribes: -30, flags: [DISHONORABLE] }

branches:
  all: ACT_4
```

---

### GATE_3.4_SURFACE_EMERGENCE

```yaml
location_id: CAVE_MOUTH_SURFACE
level: 7
cr: 2
npc: SURFACE_PATROL_LEADER
npc_detail: "Human militia captain, CR 1, wary but not hostile initially"
secondary_npcs: [GUARDS_6, SETTLERS_10]
threat_clarification: "Option 4 combat = captain CR 1 + 6 guards CR 1/8. Settlers flee."
conflict_type: FIRST_CONTACT
conflict_id: SURFACE_INTRODUCTION

options:
  1: "Peaceful approach - companions vouch"
  2: "Intimidation display"
  3: "Retreat to caves"
  4: "Attack patrol"

consequences:
  option_1: { shadow: -5, skill_challenge: "Persuasion DC 16", xp_award: 700, rep_surface_kingdoms: +10, flags: [PEACEFUL_CONTACT] }
  option_2: { shadow: +8, skill_challenge: "Intimidation DC 14", xp_award: 700, rep_surface_kingdoms: -10, flags: [FEAR_BASED] }
  option_3: { shadow: 0, xp_award: 700, flags: [CAUTIOUS] }
  option_4: { shadow: +15, combat: true, cr: 3, xp_award: 700, rep_surface_kingdoms: -40, flags: [HOSTILE_FIRST_CONTACT] }

branches:
  all: ACT_4
```

---

## ACT_3_COMPLETION

```yaml
xp_target: 9000
state_check:
  - Surface approach: true
  - Companions: 2-4
  - Shadow: 20-80 likely
  
transition: ACT_4_RECKONING
```

---

**END ACT 3**
