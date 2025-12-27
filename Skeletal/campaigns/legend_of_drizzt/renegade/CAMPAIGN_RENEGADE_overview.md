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
