# ACT 1: BLOOD AND DARKNESS

**Levels 1-2**

---

## PHASE_ID

```yaml
PHASE: ESCAPE
RESTRICTIONS:
  - Symbolic elements: false
  - Focus: Survival, immediate danger, action
```

---

## GATES

### GATE_1.1_HOUSE_FALL

```yaml
location_id: DROW_CITY_HOUSE_COMPOUND
level: 1
cr: 1
npc: RIVAL_PRIESTESS
secondary_npcs: [ATTACKING_DROW, HOUSE_SURVIVORS]
conflict_type: ESCAPE
conflict_id: HOUSE_DESTRUCTION

options:
  1: "Fight through main gate"
  2: "Sneak through servant tunnels"
  3: "Save heirloom/person first (risky)"
  4: "Flee immediately, abandon all"

consequences:
  option_1: { shadow: +2, combat: true, cr: 1, gold: +50, flags: [WARRIOR_SPIRIT] }
  option_2: { shadow: 0, skill_challenge: "Stealth DC 12", flags: [CUNNING] }
  option_3: { shadow: -3, combat: true, cr: 2, gold: +200, flags: [COMPASSIONATE, SAVED_HEIRLOOM] }
  option_4: { shadow: +5, flags: [PRAGMATIC] }

branches:
  all: GATE_1.2_PURSUIT
```

---

### GATE_1.2_PURSUIT

```yaml
location_id: UNDERDARK_OUTER_TUNNELS
level: 1
cr: 2
npc: DROW_PATROL_LEADER
secondary_npcs: [DROW_WARRIORS, SPIDER_MOUNT]
conflict_type: SURVIVAL
conflict_id: DROW_PURSUIT

options:
  1: "Ambush pursuers in narrow tunnel"
  2: "Lead them into natural hazard"
  3: "Hide and wait them out"
  4: "Negotiate - offer information"

consequences:
  option_1: { shadow: 0, combat: true, cr: 2, flags: [FOUGHT_PATROL] }
  option_2: { shadow: -2, skill_challenge: "Survival DC 13, Nature DC 12", flags: [UNDERDARK_SAVVY] }
  option_3: { shadow: 0, skill_challenge: "Stealth DC 14", time_cost: "8 hours", flags: [PATIENT] }
  option_4: { shadow: +8, skill_challenge: "Deception DC 15 or Persuasion DC 18", flags: [INFORMANT], rep_drow_houses: +1 }

branches:
  all: GATE_1.3_DWARF_ENCOUNTER
```

---

### GATE_1.3_DWARF_ENCOUNTER

```yaml
location_id: COLLAPSED_TUNNEL
level: 1
cr: 0
npc: DWARF_LEADER
secondary_npcs: [HOOK_HORRORS_OUTSIDE]
conflict_type: SOCIAL_CHOICE
conflict_id: ENEMY_ALLIANCE

options:
  1: "Cooperate to dig out together"
  2: "Kill dwarf, take tools, escape alone"
  3: "Temporary truce, part ways after"
  4: "Wait for dwarf to solve it"

consequences:
  option_1: { shadow: -5, companion_join: DWARF_LEADER, skill_challenge: "Athletics DC 13", flags: [DWARF_ALLY] }
  option_2: { shadow: +10, combat: true, cr: 1, gold: +150, flags: [DWARF_KILLER, ALONE] }
  option_3: { shadow: 0, skill_challenge: "Persuasion DC 14", flags: [DWARF_NEUTRAL] }
  option_4: { shadow: +3, flags: [OPPORTUNIST] }

branches:
  all: GATE_1.4_SLAVE_CAMP
```

---

### GATE_1.4_SLAVE_CAMP

```yaml
location_id: DUERGAR_MINE_OUTPOST
level: 2
cr: 3
npc: DUERGAR_SLAVEMASTER
secondary_npcs: [DUERGAR_GUARDS, GNOME_SLAVES, HALFLING_PRISONER]
conflict_type: MORAL_CHOICE
conflict_id: SLAVERY_INTERVENTION

options:
  1: "Attack slavers, free all slaves"
  2: "Negotiate passage with payment"
  3: "Raid supplies, ignore slaves"
  4: "Offer services to slavers"
  5: "Free only halfling, leave others"

consequences:
  option_1: { shadow: -10, combat: true, cr: 4, xp_award: 300, rep_deep_gnomes: +20, rep_duergar: -30, companion_join: HALFLING_ROGUE, gold: -100, flags: [LIBERATOR, HALFLING_ALLY] }
  option_2: { shadow: 0, xp_award: 300, gold: -200, flags: [NEUTRAL_TRADER] }
  option_3: { shadow: +5, combat: true, cr: 3, xp_award: 300, rep_duergar: -10, gold: +150, flags: [OPPORTUNIST] }
  option_4: { shadow: +15, xp_award: 300, rep_deep_gnomes: -50, rep_duergar: +15, gold: +500, flags: [SLAVER_ALLY] }
  option_5: { shadow: -3, combat: true, cr: 2, xp_award: 300, companion_join: HALFLING_ROGUE, rep_duergar: -5, flags: [SELECTIVE_MERCY, HALFLING_ALLY] }

branches:
  all: ACT_2
```

---

## ACT_1_COMPLETION

```yaml
xp_target: 300
state_check:
  - Escaped drow city: true
  - Companions: 0-2
  - Shadow: 35-70 likely
  
transition: ACT_2_DEPTHS
```

---

**END ACT 1**
