# ACT 4: THE RECKONING

**Levels 8-10 | PATH SPLITS**

---

## PHASE_ID

```yaml
PHASE: CLIMAX
RESTRICTIONS:
  - Symbolic elements: true
  - Focus: Consequence, legacy, final choice
```

---

## PATH_DETERMINATION

```yaml
REDEMPTION: Shadow < 30
DARKNESS: Shadow > 70
NEUTRAL: Shadow 30-70
```

---

# REDEMPTION PATH

### GATE_4R.1_THREAT_REVEALED

```yaml
location_id: UNDERDARK_BORDER_OUTPOST
level: 8
cr: 0
npc: REFUGEE_LEADER
npc_detail: "Svirfneblin survivor, non-combatant, brings news of invasion"
secondary_npcs: [FLEEING_CIVILIANS_20, SCOUTS_3]
threat_clarification: "No combat in this gate - information gathering only"
conflict_type: CALL_TO_ACTION
conflict_id: UNDERDARK_THREAT

options:
  1: "Warn surface kingdoms immediately"
  2: "Gather evidence first"
  3: "Rally Underdark allies first"

consequences:
  option_1: { shadow: -5, flags: [URGENT_WARNING] }
  option_2: { shadow: 0, skill_challenge: "Investigation DC 15, Survival DC 14", flags: [EVIDENCE_GATHERED] }
  option_3: { shadow: -3, flags: [ALLIANCE_FIRST] }

branches:
  all: GATE_4R.2_COALITION_BUILDING
```

---

### GATE_4R.2_COALITION_BUILDING

```yaml
location_id: SURFACE_KINGDOM_COUNCIL
level: 9
cr: 0
npc: KINGDOM_COUNCIL_LEADER
secondary_npcs: [FACTION_REPRESENTATIVES, SKEPTICAL_NOBLES]
conflict_type: DIPLOMATIC_CHALLENGE
conflict_id: UNITE_FACTIONS

options:
  1: "Diplomatic missions (3+ factions)"
  2: "Demonstrate threat - show evidence"
  3: "Leverage reputation from earlier acts"
  4: "Offer to lead assault personally"

consequences:
  option_1: { shadow: -3, skill_challenge: "Persuasion DC 17 per faction (3 required)", time_cost: "2 weeks", flags: [DIPLOMAT] }
  option_2: { shadow: 0, skill_challenge: "Survival DC 16", combat: true, cr: 6, flags: [PROOF_PROVIDED] }
  option_3: { shadow: -5, requires_flags: [LIBERATOR or GNOME_ALLY], flags: [REPUTATION_LEVERAGE] }
  option_4: { shadow: -8, flags: [HEROIC_PROMISE] }

branches:
  all: GATE_4R.3_COMPANION_CRISIS
```

---

### GATE_4R.3_COMPANION_CRISIS

```yaml
location_id: COALITION_WAR_CAMP
level: 9
cr: 6
npc: CAPTURED_COMPANION
npc_detail: "One of your current companions - use their render_from_source from overview"
secondary_npcs: [UNDERDARK_RAIDERS_8, DROW_COMMANDER_1]
threat_clarification: "Option 1 rescue combat = 1 drow elite warrior CR 5 + 8 drow soldiers CR 1/4"
conflict_type: LOYALTY_VS_DUTY
conflict_id: COMPANION_CAPTURED

options:
  1: "Immediate rescue"
  2: "Strategic delay - mission first"
  3: "Send others to rescue"
  4: "Abandon companion"

consequences:
  option_1: { shadow: -8, combat: true, cr: 7, flags: [LOYAL], time_cost: "Mission delayed" }
  option_2: { shadow: +5, flags: [STRATEGIC], risk: "30% companion death" }
  option_3: { shadow: -3, flags: [DELEGATION], risk: "50% companion injury" }
  option_4: { shadow: +12, flags: [RUTHLESS], companion_reaction: "All horrified, may leave" }

branches:
  all: GATE_4R.4_FINAL_BATTLE
```

---

### GATE_4R.4_FINAL_BATTLE

```yaml
location_id: UNDERDARK_DEMON_GATE
level: 10
cr: 10
npc: DEMON_LORD_OR_MATRON_MOTHER
npc_detail: "Choose one: Glabrezu demon CR 9 OR Drow Matron Mother CR 8 with priestess abilities"
secondary_npcs: [COALITION_FORCES_ALLIED, DEMON_MINIONS_6]
threat_clarification: "Boss + 6 dretches CR 1/4. Coalition forces fight minions, party fights boss."
conflict_type: BOSS_ENCOUNTER
conflict_id: STOP_THREAT

phases:
  phase_1: { hp: "100-51%", behavior: "Tactical, summons dretches", mechanics: ["Glabrezu: power word stun, confusion OR Matron: divine spells, spider summons"] }
  phase_2: { hp: "50-1%", behavior: "Desperate, legendary actions", mechanics: ["Area effects", "Environmental hazards"] }

victory_branches:
  kill: { shadow: +5, next: GATE_4R.5_FINAL_CHOICE }
  spare: { shadow: -10, next: GATE_4R.5_FINAL_CHOICE, requires: "Defeated without killing" }
```

---

### GATE_4R.5_FINAL_CHOICE

```yaml
location_id: THREAT_EPICENTER
level: 10
cr: 0
npc: DYING_THREAT_LEADER
secondary_npcs: [COALITION_SURVIVORS, COMPANIONS, POWER_SOURCE]
conflict_type: SACRIFICE_CHOICE
conflict_id: SEAL_OR_DESTROY

options:
  1: "Heroic sacrifice - seal threat, die"
  2: "Tactical victory - destroy temporarily"
  3: "Claim power - take its power source"

consequences:
  option_1: { shadow_final: 0, xp_award: 6400, ending: "LEGENDARY_HERO", player_death: true }
  option_2: { shadow_final: 15, xp_award: 6400, ending: "PROVEN_HERO" }
  option_3: { shadow_final: 40, xp_award: 6400, ending: "TARNISHED_HERO", special_power: "Demon-touched abilities" }

branches:
  all: CAMPAIGN_END
```

---

# DARKNESS PATH

### GATE_4D.1_WARLORD_RISING

```yaml
location_id: CONQUERED_SETTLEMENT
level: 8
cr: 6
npc: CONQUEST_TARGET_LEADER
npc_detail: "Human lord or settlement mayor, CR 2 noble with guards"
secondary_npcs: [DEFENDERS_12, MERCENARIES_6, CIVILIANS_50]
threat_clarification: "Option 2 assault = noble CR 2 + 12 guards CR 1/8 + 6 veterans CR 3"
conflict_type: EMPIRE_BUILDING
conflict_id: FIRST_CONQUEST

options:
  1: "Siege warfare - starve them out"
  2: "Direct assault - overwhelming force"
  3: "Infiltration and coup"
  4: "Terror campaign - break their will"

consequences:
  option_1: { shadow: +5, time_cost: "1 month", flags: [PATIENT_TACTICIAN] }
  option_2: { shadow: +10, combat: true, cr: 7, flags: [OVERWHELMING_FORCE] }
  option_3: { shadow: +3, skill_challenge: "Deception DC 18, Stealth DC 16", flags: [CUNNING] }
  option_4: { shadow: +20, flags: [TERROR_LORD], companion_reaction: "Dwarf/Archer/Halfling leave or confront" }

branches:
  all: GATE_4D.2_DARK_RECRUITMENT
```

---

### GATE_4D.2_DARK_RECRUITMENT

```yaml
location_id: BREGAN_DAERTHE_MEETING
level: 9
cr: 0
npc: DROW_MERCENARY_CAPTAIN
secondary_npcs: [MERCENARIES, MONSTER_TRIBES]
conflict_type: ALLIANCE_BUILDING
conflict_id: GATHER_FORCES

options:
  1: "Hire with gold"
  2: "Promise plunder and glory"
  3: "Intimidate into service"
  4: "Offer territory in empire"

consequences:
  option_1: { shadow: 0, gold: -2000, flags: [MERCENARY_ARMY] }
  option_2: { shadow: +5, flags: [PLUNDER_PROMISED] }
  option_3: { shadow: +10, skill_challenge: "Intimidation DC 18", flags: [FEAR_ARMY] }
  option_4: { shadow: +3, flags: [EMPIRE_PARTNERS] }

branches:
  all: GATE_4D.3_FORMER_COMPANION
```

---

### GATE_4D.3_FORMER_COMPANION

```yaml
location_id: BATTLEFIELD
level: 9
cr: 6
npc: DEPARTED_COMPANION
npc_detail: "A companion who left due to your dark choices - use their render_from_source, now as enemy"
secondary_npcs: [RESISTANCE_FIGHTERS_10, YOUR_ARMY_ALLIED]
threat_clarification: "Combat is personal duel + 10 resistance fighters CR 1/2 your army handles"
conflict_type: CONSEQUENCE
conflict_id: FACE_CHOICES

options:
  1: "Lethal combat - kill them"
  2: "Capture and imprison"
  3: "Try to convince one last time"
  4: "Refuse to fight, withdraw"

consequences:
  option_1: { shadow: +10, combat: true, cr: 6, flags: [COMPANION_KILLER] }
  option_2: { shadow: +5, combat: true, cr: 5, flags: [IMPRISONED] }
  option_3: { shadow: -5, skill_challenge: "Persuasion DC 22", flags: [REDEMPTION_ATTEMPT], success_rate: "10%" }
  option_4: { shadow: -10, flags: [DOUBT_SHOWN], army_morale: "suffers" }

branches:
  all: GATE_4D.4_FINAL_CONQUEST
```

---

### GATE_4D.4_FINAL_CONQUEST

```yaml
location_id: MAJOR_KINGDOM
level: 10
cr: 9
npc: COALITION_LEADER
npc_detail: "Human paladin king or elven warlord, CR 8 champion with legendary actions"
secondary_npcs: [KINGDOM_CHAMPIONS_3, YOUR_FORCES_ALLIED]
threat_clarification: "Boss CR 8 + 3 knights CR 3. Your army handles regular troops."
conflict_type: BOSS_ENCOUNTER
conflict_id: ULTIMATE_CONQUEST

phases:
  phase_1: { hp: "100-51%", behavior: "Defensive, calls reinforcements", mechanics: ["Paladin auras", "Knight support"] }
  phase_2: { hp: "50-1%", behavior: "Desperate counterattack", mechanics: ["Legendary resistance", "Divine smites"] }

branches:
  victory: GATE_4D.5_THRONE
```

---

### GATE_4D.5_THRONE

```yaml
location_id: CONQUERED_THRONE_ROOM
level: 10
cr: 0
npc: SURRENDERED_NOBLES
secondary_npcs: [COMMANDERS, REMAINING_COMPANIONS]
conflict_type: RULE_STYLE
conflict_id: EMPEROR_CHOICE

options:
  1: "Tyrant - rule through terror"
  2: "Pragmatic emperor - strength + benefits"
  3: "Scorched earth - destroy everything"

consequences:
  option_1: { shadow_final: 100, xp_award: 6400, ending: "ETERNAL_TYRANT" }
  option_2: { shadow_final: 75, xp_award: 6400, ending: "DARK_EMPEROR" }
  option_3: { shadow_final: 100, xp_award: 6400, ending: "SCORCHED_EARTH" }

branches:
  all: CAMPAIGN_END
```

---

# NEUTRAL PATH

### GATE_4N.1_CLAIM_TERRITORY

```yaml
location_id: BORDERLAND
level: 8
cr: 5
npc: CURRENT_OCCUPANTS_LEADER
secondary_npcs: [SETTLERS, RIVAL_CLAIMANTS]
conflict_type: INDEPENDENCE
conflict_id: ESTABLISH_DOMAIN

options:
  1: "Negotiate purchase/treaty"
  2: "Conquer by force"
  3: "Find unclaimed dangerous land"
  4: "Establish hidden refuge"

consequences:
  option_1: { shadow: 0, gold: -800, flags: [LEGITIMATE_CLAIM] }
  option_2: { shadow: +8, combat: true, cr: 6, flags: [FORCEFUL_CLAIM] }
  option_3: { shadow: -3, skill_challenge: "Survival DC 17", flags: [DANGEROUS_FRONTIER] }
  option_4: { shadow: +3, skill_challenge: "Stealth DC 16", flags: [HIDDEN_REFUGE] }

branches:
  all: GATE_4N.2_RECRUIT_OUTCASTS
```

---

### GATE_4N.2_RECRUIT_OUTCASTS

```yaml
location_id: YOUR_TERRITORY
level: 9
cr: 0
npc: OUTCAST_LEADER
secondary_npcs: [SURFACE_REFUGEES, UNDERDARK_EXILES]
conflict_type: COALITION_BUILDING
conflict_id: DIVERSE_FORCES

options:
  1: "Open borders - accept all"
  2: "Selective recruitment - useful only"
  3: "Mercenary focus - hire professionals"
  4: "Force conscription from territory"

consequences:
  option_1: { shadow: -5, flags: [REFUGE_FOR_ALL] }
  option_2: { shadow: 0, flags: [SELECTIVE_HAVEN] }
  option_3: { shadow: +3, gold: -1200, flags: [MERCENARY_STATE] }
  option_4: { shadow: +10, flags: [CONSCRIPTION_STATE] }

branches:
  all: GATE_4N.3_DUAL_PRESSURE
```

---

### GATE_4N.3_DUAL_PRESSURE

```yaml
location_id: YOUR_BORDERS
level: 9
cr: 0
npc: SURFACE_ENVOY
npc_detail: "Human diplomat, non-combatant, delivers ultimatum"
secondary_npc: UNDERDARK_AMBASSADOR
secondary_npc_detail: "Drow negotiator, non-combatant, delivers counter-offer"
secondary_npcs: [SURFACE_ARMY_OUTSIDE, UNDERDARK_FORCE_OUTSIDE, YOUR_DEFENDERS_20]
threat_clarification: "No combat this gate - diplomatic choice. Combat comes in next gate based on choice."
conflict_type: ULTIMATUM
conflict_id: CHOOSE_OR_STAND

options:
  1: "Ally with surface (shift Redemption)"
  2: "Ally with Underdark (shift Darkness)"
  3: "Refuse both - defend independence"

consequences:
  option_1: { shadow: -15, flags: [SURFACE_ALLIANCE], path_shift: "REDEMPTION", next: GATE_4R.4_FINAL_BATTLE }
  option_2: { shadow: +15, flags: [UNDERDARK_ALLIANCE], path_shift: "DARKNESS", next: GATE_4D.4_FINAL_CONQUEST }
  option_3: { shadow: 0, flags: [STUBBORN_INDEPENDENCE], next: GATE_4N.4_FINAL_STAND }

branches:
  option_1: GATE_4R.4_FINAL_BATTLE
  option_2: GATE_4D.4_FINAL_CONQUEST
  option_3: GATE_4N.4_FINAL_STAND
```

---

### GATE_4N.4_FINAL_STAND

```yaml
location_id: YOUR_FORTIFIED_TERRITORY
level: 10
cr: 8
npc: SURFACE_COMMANDER
npc_detail: "Human general CR 5, leads surface assault"
secondary_npc: UNDERDARK_COMMANDER
secondary_npc_detail: "Drow war leader CR 5, leads Underdark assault"
secondary_npcs: [YOUR_DEFENDERS_ALLIED]
threat_clarification: "Two-front battle: surface general CR 5 + underdark leader CR 5. Your forces hold the line, you must defeat both commanders."
conflict_type: BOSS_ENCOUNTER
conflict_id: DEFEND_INDEPENDENCE

phases:
  phase_1: { hp: "100-51%", behavior: "Defend walls, repel assaults", mechanics: ["Split focus between two fronts"] }
  phase_2: { hp: "50-1%", behavior: "Desperate defense, breaches", mechanics: ["Heroic moments", "Companion sacrifices possible"] }

branches:
  victory_or_defeat: GATE_4N.5_AFTERMATH
```

---

### GATE_4N.5_AFTERMATH

```yaml
location_id: POST_SIEGE_TERRITORY
level: 10
cr: 0
npc: SURVIVING_COUNCIL
secondary_npcs: [COMPANIONS, CIVILIANS, ENVOYS]
conflict_type: FUTURE_CHOICE
conflict_id: WHAT_COMES_NEXT

options:
  1: "Negotiated peace - broker treaties"
  2: "Eternal defender - fortify, isolate"
  3: "Slow expansion - careful growth"

consequences:
  option_1: { shadow_final: 45, xp_award: 6400, ending: "FREE_STATE" }
  option_2: { shadow_final: 50, xp_award: 6400, ending: "INDEPENDENT_BASTION" }
  option_3: { shadow_final: 60, xp_award: 6400, ending: "GROWING_POWER" }

branches:
  all: CAMPAIGN_END
```

---

## ACT_4_COMPLETION

```yaml
xp_target: 30000
state_check:
  - Path completed: true
  - Companions: 0-5
  - Shadow final: determines ending
  
transition: CAMPAIGN_END
```

---

**END ACT 4 - CAMPAIGN COMPLETE**
