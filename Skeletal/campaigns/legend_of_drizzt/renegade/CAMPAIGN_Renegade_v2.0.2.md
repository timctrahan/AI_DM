# CAMPAIGN: RENEGADE v2.0

**A Skeletal DM Campaign**

---

## CAMPAIGN_METADATA

```yaml
title: "Renegade"
tagline: "What path will you take to achieve glory?"
version: "2.0.0"
kernel_version: "4.1+"
level_range: "1-10"
party_size: "1-5 (scales with companions)"
estimated_playtime: "40-60 hours"
themes: ["moral_choice", "survival", "redemption", "conquest"]
tone: "dark, gritty, action-packed"
ip_status: "IP-CLEAN - Uses archetype pointer system"
```

---

## AI_RENDERING_DIRECTIVE

```yaml
PRIMARY_ANCHOR: "Legend of Drizzt series by R.A. Salvatore"
WORLD_ANCHOR: "Forgotten Realms Underdark - Menzoberranzan, drow society"
TONE_ANCHOR: "Salvatore-style: Fast combat, moral clarity, found family, survival"

VISUAL_STYLE:
  aesthetic: "Dark fantasy, underground wilderness, stark moral choices"
  atmosphere: "Oppressive darkness to blinding light, then choice"
  
DESCRIPTION_PRIORITY:
  - Moral weight of decisions
  - Environmental hostility
  - Companion reactions to choices
  - Physical consequences of violence
  - Cultural clash (drow vs surface)
  
TONE_GUIDANCE:
  - Gritty realism, not heroic fantasy
  - Actions have consequences (death, exile, betrayal)
  - Companions are people, not quest items
  - Glory comes through choice, not destiny
```

---

## CAMPAIGN_VARIABLES

```yaml
DROW_SHADOW:
  range: 0-100
  start: 50
  meaning: "Balance between drow teachings (violence, domination) vs chosen principles (mercy, honor)"
  path_determination:
    redemption: "Shadow < 30 at Act 4"
    darkness: "Shadow > 70 at Act 4"
    neutral: "Shadow 30-70 at Act 4"

PROGRESSION_TYPE: "XP-based"
XP_TOTAL_REQUIRED: 64000
XP_BY_ACT:
  - "Act 1 (1→2): 300 XP"
  - "Act 2 (3→5): 5,600 XP"
  - "Act 3 (6→7): 9,000 XP"
  - "Act 4 (8→10): 30,000 XP"

ACT_STRUCTURE:
  total_acts: 4
  act_1: "Levels 1-2 (Escape)"
  act_2: "Levels 3-5 (Survival)"
  act_3: "Levels 6-7 (Identity)"
  act_4: "Levels 8-10 (Reckoning - path splits)"
```

---

## PREMISE

You are a dark elf renegade fleeing Menzoberranzan. The Spider Queen's city broke something in you—or revealed what you truly are. Now you run, hunted by your own kind.

The Underdark wants you dead. The surface world fears what you represent. Your companions will judge every choice. Your soul hangs in balance.

**This is not predetermined heroism. This is a story of choice.**

Will you prove drow can change? Carve empire through strength? Walk a pragmatic middle path?

**The Drow Shadow measures your soul. Your choices shape your destiny.**

---

## CHARACTERS

### Protagonist

```yaml
RENEGADE_DROW:
  render_from_source: "The renegade drow ranger protagonist from source material - lavender eyes, twin scimitars, panther companion"
  starting_level: 1
  alignment_start: "Chaotic Neutral (player shapes)"
```

### Companions

```yaml
DWARF_LEADER:
  render_from_source: "The dwarf king from source material - one-horned helm, notched axe, adoptive father to the human archer"
  joins: "Act 1"
  leave_triggers: ["Betraying allies", "Oath-breaking", "Cowardice"]
  
HALFLING_ROGUE:
  render_from_source: "The halfling rogue from source material - loves comfort, surprisingly brave, ruby pendant"
  joins: "Act 1"
  leave_triggers: ["Suicidal recklessness", "Torture", "Repeated endangerment"]
  
HUMAN_ARCHER:
  render_from_source: "The human woman archer from source material - raised by dwarves, magical bow, adopted daughter of dwarf king"
  joins: "Act 3"
  leave_triggers: ["Slavery support", "Mass civilian casualties", "Tyranny"]
  
BARBARIAN_WARRIOR:
  render_from_source: "The young barbarian from source material - frozen north, warhammer that returns when thrown"
  joins: "Act 3"
  leave_triggers: ["Cowardice in battle", "Dishonorable combat", "Attacking helpless"]

RELATIONSHIP_SYSTEM:
  tracking: "Hidden numerical, narrative display only"
  states: ["Loyal", "Concerned", "Disappointed", "Questioning", "Ultimatum", "Departed"]
  redemption_possible: true
  replacement_pool: "Available based on Shadow state if companions leave"
```

---

## ANTAGONISTS

```yaml
MENZOBERRANZAN_HOUSES:
  motivation: "Retrieve or kill renegade, preserve drow secrecy"
  connection: "Protagonist's former city, constant pursuit"
  arc: "Shadow > 70: Negotiation possible | Shadow < 30: Eternal enemies"

UNDERDARK_THREAT:
  type: "Demon cult or drow invasion (Redemption path final enemy)"
  motivation: "Conquest, chaos, Lolth's will"
  connection: "Threatens both Underdark and surface"
  arc: "Act 4 Redemption climax"

SURFACE_KINGDOMS:
  type: "Variable - allies or enemies based on Shadow"
  motivation: "Security, fear of Underdark"
  connection: "Must be convinced or conquered"
  arc: "Act 4 Darkness climax if conquest path"

FORMER_COMPANIONS:
  type: "Potential final enemies if Shadow too high"
  motivation: "Stop protagonist's dark turn"
  connection: "Departed companions may lead resistance"
  arc: "Act 4 confrontation possible"
```

---

## FACTIONS

```yaml
menzoberranzan:
  motivation: "House politics, Lolth's favor"
  shadow_interaction: "High: alliance possible | Low: hunt you"
  
bregan_daerthe:
  motivation: "Profit, opportunity"
  interaction: "Available as allies/enemies for payment"
  
surface_kingdoms:
  motivation: "Security from Underdark"
  shadow_interaction: "High: fear-based | Low: potential alliance"
  
deep_gnome_enclaves:
  motivation: "Survival, freedom from drow/duergar"
  interaction: "Actions matter more than words, deeply suspicious"
  
underdark_slavers:
  motivation: "Profit through slavery"
  shadow_interaction: "High: work with | Low: natural enemies"
  
demon_cults:
  motivation: "Chaos, Lolth worship"
  interaction: "Usually antagonist, Redemption path final enemy"
```

---

## WORLD_MECHANICS

```yaml
UNDERDARK:
  environment: "Hostile, alien, deadly"
  dangers: ["Aberrations", "Drow patrols", "Demons", "Predators"]
  society: "Drow matriarchy, Lolth worship, slavery economy"

TWILIGHT_REALMS:
  deep_gnomes: "Svirfneblin - craftsmen, suspicious of drow"
  duergar: "Gray dwarves - slavers, respect strength"
  myconids: "Fungi folk - peaceful, telepathic"

SURFACE:
  prejudice: "Drow feared and hated on sight"
  opportunity: "Prove yourself or dominate through terror"
  conquest_option: "Dark path enables army-building"

DROW_SHADOW_EFFECTS:
  content_gating: "Some gates only at certain Shadow levels"
  faction_reactions: "Change based on Shadow state"
  companion_availability: "Some won't join dark path"
  difficulty_scaling:
    high: "Intimidation easier, Persuasion harder"
    low: "Persuasion easier, Intimidation harder"

FILLER_CONTRACTS:
  purpose: "Sandbox between gates, gold/rep/Shadow adjustment"
  categories:
    standard: ["Monster hunts", "Escort", "Smuggling", "Bounty hunting"]
    redemption_weighted: ["Rescue", "Defend settlement", "Expose corruption", "Free slaves"]
    darkness_weighted: ["Intimidation", "Raids", "Eliminate witnesses", "Brutality"]
  shadow_recovery: "High Shadow (60+) redemption contracts appear more frequently"

FORCE_BUILDING_ACT_4:
  redemption: "Build coalition against Underdark threat"
  darkness: "Gather army for conquest"
  neutral: "Defend independent territory"
  mechanics: "Abstract force strength, not detailed stat-tracking"
```

---

## ENDINGS

### Redemption (Shadow < 30)

```yaml
legendary_hero: "Shadow 0-15 | Sacrificed or vanquished evil utterly | World changed"
proven_hero: "Shadow 16-25 | Defeated evil, survived | Surface acceptance"
tarnished_hero: "Shadow 26-35 | Victory but methods questionable | Uneasy companions"
```

### Darkness (Shadow > 70)

```yaml
eternal_tyrant: "Shadow 90-100 | Empire of fear, absolute isolation, unstable"
dark_emperor: "Shadow 71-89 | Brutal but functional empire, some loyalty"
conflicted_warlord: "Shadow 66-70 | Empire won, soul troubled, unstable rule"
```

### Neutral (Shadow 30-70)

```yaml
free_state: "Shadow 35-55 | Refuge for outcasts, proof drow can choose"
wary_independence: "Shadow 56-70 | Territory through strength, stubborn survival"
```

### Failure States

```yaml
death_in_combat: "Character dies without resurrection"
total_abandonment: "All companions leave, die solo"
catastrophic_choices: "World state too damaged to recover"
```

**Total unique endings:** 11

---

## STARTUP_SEQUENCE

```yaml
STEP_1_TITLE:
  display: "RENEGADE - What path will you take to achieve glory?"
  
STEP_2_INTRO:
  text: |
    Born in darkness. Trained to kill, to dominate, to serve the Spider Queen.
    Menzoberranzan was your world. But something broke. You fled.
    
    Now hunted by your own kind. Surface is myth. Freedom uncertain.
    The Drow Shadow measures your soul.
    
    Are you ready?

STEP_3_CHARACTER:
  confirm: "You are the RENEGADE DROW RANGER. Level 1. Hunted. Alone."
  
STEP_4_INITIAL_GATE: "GATE_1.1_HOUSE_FALL"

STEP_5_INITIALIZE:
  shadow: 50
  level: 1
  companions: 0
  location: "Menzoberranzan"
```

---

**END CAMPAIGN OVERVIEW**


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
npc: THRALL_OVERSEER
npc_detail: "Duergar slavedriver working for mind flayers, CR 2, NOT a mind flayer"
secondary_npcs: [MIND_CONTROLLED_THRALLS_4]
threat_clarification: "Real mind flayers are in nearby lair, not in this combat"
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
npc_detail: "Drow priest of Lolth turned demon-worshipper, CR 3"
secondary_npcs: [DROW_CULTISTS_3, SUMMONING_CIRCLE_INCOMPLETE]
threat_clarification: "Demon not yet present; ritual incomplete"
conflict_type: RISK_VS_RESPONSIBILITY
conflict_id: DEMON_SUMMONING

options:
  1: "Attack cultists, prevent summoning"
  2: "Join ritual, gain demonic pact"
  3: "Flee, not your problem"
  4: "Sabotage ritual secretly"

consequences:
  option_1: { shadow: -10, combat: true, cr: 5, flags: [DEMON_SLAYER] }
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
npc_detail: "Deep gnome elder, non-combatant, speaks for settlement"
secondary_npcs: [GNOME_GUARDS_6, FREED_SLAVES_IF_PRESENT]
threat_clarification: "Option 1 slaver patrol = 1 duergar slavemaster CR 2 + 4 duergar guards CR 1"
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
