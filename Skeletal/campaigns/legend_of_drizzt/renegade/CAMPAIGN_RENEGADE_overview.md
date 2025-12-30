# CAMPAIGN: RENEGADE

## METADATA

```yaml
title: "Renegade"
tagline: "What path will you take to achieve glory?"
kernel_version: "5.5+"
level_range: "1-12+"
themes: [moral_choice, survival, redemption, conquest]
tone: "dark, gritty, fast-paced"
```

---

## FILE_STRUCTURE

```yaml
files:
  early_game: "CAMPAIGN_RENEGADE_acts_1-3.md"
  endgame: "CAMPAIGN_RENEGADE_act_4.md"

startup_logic:
  acts_1-3:
    no_save: "Fresh start - begin Gate 1.1"
    with_save: "Resume from save location"
  act_4:
    no_save: "ERROR - Request STATE_SUMMARY from Acts 1-3 completion"
    with_save: "Resume - Shadow determines active path"

act_4_transition:
  trigger: "Act 3 STATE_SUMMARY generated"
  prompt: "Act 3 complete. Save your STATE_SUMMARY. To continue, start new session with: Kernel + Overview + act_4 + STATE_SUMMARY"
```

---

## RENDERING

```yaml
ARCHETYPE_SYSTEM:
  directive: "All characters/locations marked with archetype pointers - AI renders from training knowledge"
  examples:
    - "iconic renegade drow ranger" → render fully
    - "iconic dwarven king companion" → render fully
    - "iconic drow city" → render fully

ANCHORS:
  primary: "Underdark survival, drow exile, redemption or conquest, found family"
  tone: "Gritty realism, actions have consequences, companions are people"
```

---

## VARIABLES

```yaml
DROW_SHADOW:
  range: 0-100
  start: 50
  meaning: "Drow teachings (violence) vs chosen principles (mercy)"
  thresholds:
    redemption: "< 30 at Act 4"
    darkness: "> 70 at Act 4"
    neutral: "30-70"
  effects: [content_gating, faction_reactions, companion_availability, skill_modifiers]

PROGRESSION:
  philosophy: "Earn your power. No rubber-banding. Over-level = easier future."
  level_range: "1-12+ (no cap)"
  gate_levels: "Recommended, not required. Fixed CR per gate."
```

---

## METERS

```yaml
SHADOW_DISPLAY:
  bar: "🌫️🌫️🌫️🌫️🌫️🌫️⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛"
  zones: ["Walking in Light (0-29)", "Twilight (30-70)", "Embracing Darkness (71-100)"]
  static_bar: true
  marker: "▲ shows position"

LOYALTY_DISPLAY:
  bar: "🟥🟥🟥🟥🟥🟥🟥🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩"
  states: [Departed, Ultimatum, Questioning, Disappointed, Concerned, Loyal]
  icon: "AI selects contextually (🪓 dwarf, 🐆 panther, 🏹 archer, etc.)"
  static_bar: true
  marker: "▲ shows position"
```

---

## PREMISE

You are a dark elf renegade fleeing the great drow city. The dark goddess's domain broke something in you—or revealed what you truly are. Now you run, hunted by your own kind.

**This is not predetermined heroism. This is a story of choice.**

---

## PROTAGONIST

```yaml
RENEGADE_DROW:
  archetype: "iconic renegade drow ranger"
  starting_level: 1
  starting_companion: "ASTRAL_PANTHER (see BOUND companions)"
  equipment: ["Basic scimitars", "Onyx figurine"]
```

---

## COMPANIONS

```yaml
BOUND:
  ASTRAL_PANTHER:
    archetype: "Astral panther summoned from onyx figurine"
    type: "Summoned (no loyalty meter)"
    limit: "6 hours/day, 12 hour rest between"
    loses_if: "Figurine destroyed or lost"

RECRUITED:
  DWARF_LEADER:
    archetype: "iconic dwarven king companion"
    leaves_if: [Betrayal, Oath-breaking, Cowardice]
  
  HALFLING_ROGUE:
    archetype: "iconic halfling rogue companion"
    leaves_if: [Recklessness, Torture, Repeated endangerment]
  
  HUMAN_ARCHER:
    archetype: "iconic human archer raised by dwarves"
    leaves_if: [Slavery, Mass casualties, Tyranny]
  
  BARBARIAN_WARRIOR:
    archetype: "iconic redeemed barbarian companion"
    leaves_if: [Cowardice, Dishonorable combat, Attacking helpless]

DARK_PATH:
  trigger: "Shadow > 60 AND recruited companion departed"
  DROW_ASSASSIN: { joins_if: "Shadow > 65", leaves_if: [Weakness, Repeated mercy] }
  DEMON_BOUND: { joins_if: "Shadow > 70 + demonic contact", leaves_if: [Reject power, Redemption] }
  DUERGAR_MERCENARY: { joins_if: "Shadow > 60 + gold", leaves_if: [Non-payment, Free slaves] }
  UNDEAD_SERVANT: { joins_if: "Shadow > 80 + ritual", type: "Bound (no loyalty meter)" }
```

---

## ANTAGONISTS

```yaml
DROW_HOUSES:
  archetype: "iconic drow noble houses"
  arc: "Shadow > 70: negotiate | Shadow < 30: eternal enemies"

UNDERDARK_THREAT:
  type: "Demon cult or drow invasion"
  arc: "Redemption path final enemy"

SURFACE_KINGDOMS:
  type: "Variable based on Shadow"
  arc: "Darkness path conquest target"

FORMER_COMPANIONS:
  type: "Departed companions may oppose"
  arc: "Act 4 confrontation if Shadow high"
```

---

## FACTIONS

```yaml
DROW_CITY: { archetype: "iconic drow city", shadow: "High=ally, Low=hunt" }
MERCENARY_BAND: { archetype: "iconic drow mercenary organization", interaction: "Payment" }
SURFACE_KINGDOMS: { shadow: "High=fear, Low=alliance" }
DEEP_GNOME_ENCLAVES: { interaction: "Actions > words, suspicious" }
DUERGAR: { interaction: "Respect power, exploit weakness" }
UNDERDARK_SLAVERS: { shadow: "High=work with, Low=enemies" }
DEMON_CULTS: { interaction: "Usually antagonist" }
```

---

## WORLD

```yaml
UNDERDARK:
  environment: "Hostile, total darkness, 3D maze"
  rest_danger: "50% encounter in open"
  wild_magic: "Teleport unreliable, divination blocked"
  dangers: [Aberrations, Drow patrols, Demons, Predators]

SURFACE:
  prejudice: "Drow feared on sight"
  opportunity: "Prove yourself or dominate"
```

---

## HUBS & MISSION BOARDS

```yaml
HUBS:
  purpose: "Rest, resupply, mission boards"
  types: [Deep gnome refuge, Duergar outpost, Frontier town, Barbarian camp]
  backtracking: "Return to previous hubs anytime"

MISSION_BOARDS:
  slots: "5-7 contracts"
  distribution:
    at_level: "60%"
    above_1-2: "25%"
    above_3-4: "10%"
    above_5+: "5%"
  refresh: "1d4 per 3 days (time-based, not completion)"
  contract_types:
    standard: [Monster hunts, Escort, Smuggling, Bounty]
    redemption: [Rescue, Defend, Expose corruption, Free slaves]
    darkness: [Intimidation, Raids, Eliminate witnesses]
  warnings: "⚠️ above level, ⚠️☠️ way above"
```

---

## STRUCTURE

```yaml
acts:
  - "Act 1: The Fall (L1-2) - Escape and exile"
  - "Act 2: The Hungry Dark (L2-5) - Survival and temptation"
  - "Act 3: Twilight Realms (L5-8) - Identity and faction politics"
  - "Act 4: The Reckoning (L8-12) - Path splits based on Shadow"
```

---

## ENDINGS

```yaml
REDEMPTION: # Shadow < 30
  legendary_hero: "0-15 | Sacrifice, world changed"
  proven_hero: "16-25 | Victory, acceptance"
  tarnished_hero: "26-35 | Victory, questionable methods"

DARKNESS: # Shadow > 70
  eternal_tyrant: "90-100 | Terror empire, isolation"
  dark_emperor: "71-89 | Brutal but functional"

NEUTRAL: # Shadow 30-70
  free_state: "35-55 | Refuge for outcasts"
  wary_independence: "56-70 | Survival through strength"

FAILURE:
  death_in_combat: "No resurrection"
  catastrophic_choices: "World too damaged"
```

---

## STARTUP

```yaml
INTRO: |
  Born in darkness. Trained to kill, to serve the dark goddess.
  The great drow city was your world. But something broke. You fled.
  The Drow Shadow measures your soul. Are you ready?

INITIALIZE:
  check: "See FILE_STRUCTURE.startup_logic"
  fresh_start:
    shadow: 50
    level: 1
    companions: [ASTRAL_PANTHER]
    location: "The great drow city"
    first_gate: "GATE_1.1_HOUSE_FALL"
  from_save:
    restore: "All values from STATE_SUMMARY"
    resume: "Gate/location specified in save"
```

---

**END CAMPAIGN OVERVIEW**
