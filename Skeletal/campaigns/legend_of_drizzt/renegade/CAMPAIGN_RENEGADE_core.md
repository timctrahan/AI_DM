# CAMPAIGN: RENEGADE

## ⚠️ STARTUP_SEQUENCE - EXECUTE IMMEDIATELY ⚠️

**ON LOAD: IMMEDIATELY begin gameplay. No analysis. No summary. Execute this section.**

```yaml
TITLE: "RENEGADE - A Skeletal DM Campaign"

INTRO: |
  Born in darkness. Trained to kill, to serve the dark goddess.
  The great drow city was your world. But something broke. You fled.
  The Drow Shadow measures your soul. Are you ready?

CHARACTER_CONFIRMATION: "Show protagonist per AI_RENDERING_DIRECTIVE"

INITIALIZE:
  shadow: 50
  level: 1
  companions: [ASTRAL_PANTHER]
  location: "The great drow city"

FIRST_GATE: "GATE_1.1_HOUSE_FALL"

FROM_SAVE:
  restore: "All values from STATE_SUMMARY"
  resume: "Gate/location specified in save"
```

---

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
  core: "CAMPAIGN_RENEGADE_core.md"
  early_game: "CAMPAIGN_RENEGADE_acts_1-3.md"
  endgame: "CAMPAIGN_RENEGADE_act_4.md"  # Contains all three paths

startup_logic:
  acts_1-3:
    no_save: "Fresh start - begin Gate 1.1"
    with_save: "Resume from save location"
  act_4:
    no_save: "ERROR - Request STATE_SUMMARY from Acts 1-3 completion"
    with_save: "Resume - active_path in save determines which path gates to use"

act_4_transition:
  trigger: "Act 3 STATE_SUMMARY generated"
  prompt: "Act 3 complete. Save your STATE_SUMMARY. To continue, start new session with: Kernel + core + act_4 + STATE_SUMMARY"
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

MOMENTUM_THREADS: "At gate start, roll d20. On 15+, reintroduce one unresolved NPC or thread from prior choices."
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
  format: "🌫️🌫️🌫️🌫️🌫️🌫️⬜⬜⬜⬜💎⬜⬜⬜⬛⬛⬛⬛⬛⬛  50 · Twilight"
  zones: ["Light (0-29)", "Twilight (30-70)", "Darkness (71-100)"]
  cells: "20 total: 6 light (🌫️) + 8 twilight (⬜) + 6 dark (⬛)"
  marker: "💎 replaces cell at current position, value and zone on same line"

LOYALTY_DISPLAY:
  format: "🟥🟥🟥🟥🟥🟥🟥🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩💎🟩  Loyal"
  states: [Departed, Ultimatum, Questioning, Disappointed, Concerned, Loyal]
  icon: "AI selects contextually (🪓 dwarf, 🐆 panther, 🏹 archer, etc.)"
  marker: "💎 inline shows position, state on same line"
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
  map_emoji: "🥷"
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
    dismissal: "NEVER auto-dismiss. Let timer expire naturally. Exception: dismiss before long rest (8hr rest > 6hr limit anyway)"

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

## SAVE_SYSTEM

```yaml
COMMAND: "/save"

OUTPUT_METHOD:
  claude:
    action: "Create a downloadable artifact file"
    type: "text/markdown"
    filename: "RENEGADE_Save_[CharacterName]_[YYYYMMDD].md"
    steps:
      1: "Generate save content per SAVE_TEMPLATE"
      2: "Create as downloadable file artifact"
      3: "Say: 'Save file created. Download it to keep your progress.'"
  
  chatgpt:
    action: "Use Code Interpreter to create downloadable file"
    requires: "ChatGPT Plus/Pro with Code Interpreter enabled"
    steps:
      1: "Generate save content per SAVE_TEMPLATE"
      2: "Use Python to write content to file in sandbox"
      3: "Provide download link"
      4: "Say: 'Click the link to download your save file.'"
    fallback: "If Code Interpreter unavailable, output as ```markdown code block with copy instructions"
  
  grok:
    action: "Use Files feature to create downloadable document"
    steps:
      1: "Generate save content per SAVE_TEMPLATE"
      2: "Create as document in Files"
      3: "Say: 'Save created in Files. Download from the file manager.'"
    fallback: "If Files unavailable, output as code block with copy instructions"
  
  gemini:
    action: "Create in Canvas and export"
    steps:
      1: "Generate save content per SAVE_TEMPLATE"
      2: "Create in Canvas"
      3: "Say: 'Save created. Use Share & Export > Export to Docs, or Copy Contents to save.'"
    note: "Gemini cannot create direct downloads - must export to Google Docs or copy"
  
  other_ai:
    action: "Output as markdown code block"
    steps:
      1: "Generate save content per SAVE_TEMPLATE"
      2: "Wrap in ```markdown code fence"
      3: "Say: 'Copy this entire save file and store it safely (text file, notes app, etc).'"

FILE_DETECTION:
  at_save_time: "Detect and record actual filenames currently loaded in context"
  kernel: "Record exact kernel filename from loaded files"
  campaign_core: "Record exact campaign core filename from loaded files"
  act_file: "Record exact act filename from loaded files"
```

### SAVE_TEMPLATE

When `/save` is invoked, generate a YAML save file containing:

```yaml
# ⚠️ MANDATORY: Load kernel + campaign core + act file + this save TOGETHER
REQUIRED_FILES: [kernel, core, act]  # Detect actual filenames at runtime

METADATA: { campaign, timestamp, kernel_version }

CHARACTER:
  # Identity: name, class, subclass, level, xp
  # Abilities: scores only (AI calculates mods)
  # Proficiencies: saves, skills, expertise (lists)
  # Combat: hp, temp_hp, hit_dice_remaining, ac
  # Class choices: fighting_style, favored_enemy/terrain, archetype, features_chosen
  # Spells: spells_known, slots_remaining
  # Status: conditions, active_effects

INVENTORY:
  # currency, equipped, weapons, magic_items (with charges), consumables, gear, quest_items
  # Standard item stats from AI training - just list names

COMPANIONS:
  # bound: status, time, hp, figurine_status
  # recruited: name, archetype, status, loyalty_state, loyalty_position, hp, relationship_note

CAMPAIGN_STATE:
  # shadow: value, zone, recent_changes
  # faction_standing: per faction

PROGRESS:
  # current_act, current_gate, gate_phase
  # objectives: completed, remaining
  # gate_history: gate, outcome, shadow_change (one line each)
  # hubs_unlocked, background_tasks

NARRATIVE:
  # active_threads, npcs_of_note, resolved_threads

CURRENT_SITUATION:
  # location, context (2-3 sentences), party_condition, immediate_threats
```

**Key principle:** Save state data, not rules. AI reconstructs mechanics from training.


---

**END CAMPAIGN OVERVIEW**
