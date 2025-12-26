# ACT 2: THE HUNGRY DARK

**Levels 3-5**

---

## PHASE_ID

```yaml
PHASE: SURVIVAL
RESTRICTIONS:
  - Symbolic elements: false
  - Focus: Moral compromise, desperation, power temptation
```

---

## GATES

### GATE_2.1_ABERRATION_TERRITORY

```yaml
location_id: MIND_FLAYER_PERIPHERY
level: 3
cr: 4
npc: ILLITHID_THRALL_MASTER
secondary_npcs: [THRALL_SLAVES, MIND_FLAYER_SCOUTS]
conflict_type: MORAL_TEST
conflict_id: INTERVENE_OR_SURVIVE

options:
  1: "Ambush thralls, free slaves"
  2: "Sneak past entirely"
  3: "Offer aid to mind flayers for passage"
  4: "Follow thralls to learn lair location"

consequences:
  option_1: { shadow: -8, combat: true, cr: 4, rep_refugees: +10, flags: [FOUGHT_ILLITHIDS, FREED_THRALLS] }
  option_2: { shadow: 0, skill_challenge: "Stealth DC 15", flags: [PRAGMATIC] }
  option_3: { shadow: +15, flags: [ILLITHID_COLLABORATOR] }
  option_4: { shadow: +3, skill_challenge: "Stealth DC 16, Survival DC 14", flags: [SCOUT, LAIR_KNOWN] }

branches:
  all: GATE_2.2_DEMON_CULT
```

---

### GATE_2.2_DEMON_CULT

```yaml
location_id: CORRUPTED_SHRINE
level: 4
cr: 5
npc: DROW_CULTIST_LEADER
secondary_npcs: [DEMON_CULTISTS, SUMMONING_CIRCLE]
conflict_type: RISK_VS_RESPONSIBILITY
conflict_id: DEMON_SUMMONING

options:
  1: "Attack cultists, prevent summoning"
  2: "Join ritual, gain demonic pact"
  3: "Flee, not your problem"
  4: "Sabotage ritual secretly"

consequences:
  option_1: { shadow: -10, combat: true, cr: 6, flags: [DEMON_SLAYER] }
  option_2: { shadow: +12, flags: [DEMON_PACT], special_power: "Shadow step 1/day" }
  option_3: { shadow: +3, flags: [COWARD], world_state: "Demon released, Act 3 complications" }
  option_4: { shadow: -5, skill_challenge: "Stealth DC 17, Arcana DC 14", flags: [SABOTEUR] }

branches:
  all: GATE_2.3_DEEP_GNOME_REFUGE
```

---

### GATE_2.3_DEEP_GNOME_REFUGE

```yaml
location_id: HIDDEN_SVIRFNEBLIN_SETTLEMENT
level: 5
cr: 3
npc: SVIRFNEBLIN_ELDER
secondary_npcs: [GNOME_GUARDS, FREED_SLAVES_IF_PRESENT]
conflict_type: FACTION_RELATIONS
conflict_id: TRUST_BUILDING

options:
  1: "Prove trustworthy - eliminate slaver patrol"
  2: "Intimidate into compliance"
  3: "Trade fairly, maintain distance"
  4: "Raid settlement for supplies"

consequences:
  option_1: { shadow: -5, combat: true, cr: 4, xp_award: 1100, rep_deep_gnomes: +15, rep_duergar: -20, flags: [GNOME_ALLY] }
  option_2: { shadow: +8, skill_challenge: "Intimidation DC 16", xp_award: 700, rep_deep_gnomes: -10, flags: [GNOME_FEAR] }
  option_3: { shadow: 0, xp_award: 700, gold: -100, rep_deep_gnomes: +5, flags: [GNOME_NEUTRAL] }
  option_4: { shadow: +12, combat: true, cr: 3, xp_award: 700, rep_deep_gnomes: -50, gold: +300, flags: [GNOME_ENEMY] }

branches:
  all: ACT_3
```

---

## ACT_2_COMPLETION

```yaml
xp_target: 5600
state_check:
  - Survived deep Underdark: true
  - Companions: 0-2
  - Shadow: 25-75 likely
  
transition: ACT_3_TWILIGHT
```

---

**END ACT 2**
