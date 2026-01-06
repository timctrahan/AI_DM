# CAMPAIGN: RENEGADE

```yaml
VALIDATION:
  type: "campaign_core"
  campaign: "Renegade"
  kernel_requires: "6.0+"
  echo: "✅ CORE: Renegade | Shadow: 0-100 | Acts: 1-4 | Status: READY"
```

## ⚠️ STARTUP_SEQUENCE - EXECUTE IMMEDIATELY ⚠️

**ON LOAD: IMMEDIATELY begin gameplay. No analysis. No summary. Execute this section.**

```yaml
STARTUP_DIAGNOSTICS:
  display: "Show this block FIRST before any narrative"
  format: |
    ═══════════════════════════════════════
    🎮 SKELETAL DM BOOT SEQUENCE
    ═══════════════════════════════════════
    
    📁 FILES LOADED
    ✅ Kernel: [version from loaded kernel]
    ✅ Campaign: Renegade
    ✅ Acts: [loaded act files]
    
    🎭 ARCHETYPE SYSTEM
    ✅ Protagonist mapped
    ✅ Companions mapped  
    ✅ Locations mapped
    ✅ Factions mapped
    
    ⚙️ SYSTEMS
    ✅ Rules: D&D 5e
    ✅ Shadow Meter: Active (start: 50)
    ✅ Gate Enforcement: Active
    ✅ Weave Rotation: Active
    ✅ Tracking Dumps: mod 6/12
    
    ═══════════════════════════════════════
    🚀 INITIALIZATION COMPLETE
    ═══════════════════════════════════════
  
  then: "Proceed to TITLE → INTRO → CHARACTER_CONFIRMATION → FIRST_GATE"

TITLE: "RENEGADE - A Skeletal DM Campaign"

INTRO: |
  Born in darkness. Trained to kill, to serve the dark goddess.
  The great drow city was your world. But something broke. You fled.
  The Drow Shadow measures your soul. Are you ready?

CHARACTER_CONFIRMATION: "Show protagonist using inferred name from ARCHETYPE_MAP"

INITIALIZE:
  shadow: 50
  level: 1
  companions: [astral_panther]
  location: "drow_city (infer name from ARCHETYPE_MAP)"

FIRST_GATE: "GATE_1.1_HOUSE_FALL"

FROM_SAVE:
  restore: "All values from STATE_SUMMARY"
  resume: "Gate/location specified in save"
```

---

## ARCHETYPE_MAP

```yaml
ARCHETYPE_MAP:
  # PROTAGONIST
  protagonist:
    archetype_description: "iconic renegade drow ranger who fled the great drow city, dual-wielding scimitars, accompanied by an astral panther"
    map_emoji: "🥷"
  
  # BOUND COMPANION
  astral_panther:
    archetype_description: "astral panther summoned from an onyx figurine, loyal magical beast companion to the renegade drow"
    map_emoji: "🐆"
  
  # RECRUITED COMPANIONS
  dwarf_leader:
    archetype_description: "iconic dwarven king who becomes a steadfast companion, honorable warrior with a battleaxe"
    map_emoji: "🪓"
  
  halfling_rogue:
    archetype_description: "iconic halfling rogue companion, clever and quick with knives, values self-preservation"
    map_emoji: "🗡️"
  
  human_archer:
    archetype_description: "iconic human archer raised by dwarves, skilled with bow, hates slavery and tyranny"
    map_emoji: "🏹"
  
  barbarian_warrior:
    archetype_description: "iconic redeemed barbarian companion, massive human warrior seeking redemption through honorable combat"
    map_emoji: "⚔️"
  
  # DARK PATH COMPANIONS
  drow_assassin:
    archetype_description: "ruthless drow assassin who respects only strength and cunning"
    map_emoji: "🗡️"
  
  demon_bound:
    archetype_description: "entity bound through demonic pact, serves dark masters"
    map_emoji: "👿"
  
  duergar_mercenary:
    archetype_description: "gray dwarf mercenary, loyal only to gold"
    map_emoji: "⛏️"
  
  undead_servant:
    archetype_description: "undead creature bound through dark ritual"
    map_emoji: "💀"
  
  # LOCATIONS
  drow_city:
    archetype_description: "the iconic great drow city, vast underground metropolis ruled by noble houses and the dark goddess"
  
  drow_houses:
    archetype_description: "the iconic drow noble houses, competing matriarchal families vying for power"
  
  mercenary_band:
    archetype_description: "iconic drow mercenary organization, neutral sellswords of the Underdark"
  
  # KEY NPCs
  mentor_blademaster:
    archetype_description: "legendary drow weapons master who quietly rejected cruelty, mentor figure"
    map_emoji: "⚔️"
```

---

## WEAVE_ROTATION

```yaml
WEAVE_ROTATION:
  T1_CRITICAL:
    # Rotate through these every turn - companions present in party
    # AI checks party composition and rotates through active companions
    rotation: [astral_panther, dwarf_leader, halfling_rogue, human_archer, barbarian_warrior]
    rule: "Only include companions currently in party. Skip absent/departed."
    method: "Natural: glance, growl, comment, reaction, combat assist"
  
  T2_CORE:
    # Rotate every 2-3 responses - faction relationships, ongoing threats
    rotation: [drow_pursuit, faction_standing, shadow_consequence, equipment_state]
    drow_pursuit: "Hunters from the great city, signs of tracking, paranoia"
    faction_standing: "Current reputation with nearby factions affects interactions"
    shadow_consequence: "Recent shadow changes manifest in NPC reactions, dreams, self-doubt"
    equipment_state: "Twin scimitars, figurine status, supplies"
    method: "Brief reference, background detail, NPC dialogue"
  
  T3_THREADS:
    # Rotate every 3-4 responses - long-term narrative threads
    rotation: [mentor_fate, house_politics, surface_rumors, past_sins]
    mentor_fate: "What happened to the blademaster? Guilt, hope, uncertainty"
    house_politics: "Shifting alliances in the drow city affect pursuit intensity"
    surface_rumors: "Tales of the world above, opportunity or danger"
    past_sins: "Specific acts from drow life that haunt or tempt"
    method: "Pending reminder, background development, dream sequence"
```

---

## TRACKED_METRICS

```yaml
TRACKED_METRICS:
  format: "🌫️ Shd [VALUE] | 🐆 [STATUS] | 👥 [COUNT]"
  components:
    shadow:
      emoji: "🌫️"
      abbrev: "Shd"
      source: "DROW_SHADOW.value"
    panther:
      emoji: "🐆"
      abbrev: ""
      source: "astral_panther summoned time remaining or 'Ready'"
    party:
      emoji: "👥"
      abbrev: ""
      source: "Active companion count"
  
  example: "🌫️ Shd 50 | 🐆 4h | 👥 2"
```

---

## METADATA

```yaml
title: "Renegade"
tagline: "What path will you take to achieve glory?"
kernel_version: "6.0+"
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
  endgame: "CAMPAIGN_RENEGADE_act_4.md"

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
RENDERING:
  system: "ARCHETYPE_MAP provides descriptions → AI infers canonical names → Render with inferred names"
  rule: "NEVER output archetype descriptions to player. Use inferred names only."

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
  gate_levels: "Minimum recommended - can punch UP (harder), cannot access gates >2 levels above"

LEVEL_GATING:
  rule: "Players can attempt content above their level (harder). Cannot access content >2 levels above."
  formula: "Available gates: (current_level - 2) to (current_level + 2)"
  examples:
    level_2: "Can attempt L1-4 gates. L5+ locked."
    level_5: "Can attempt L3-7 gates. L8+ locked."
  
  overleveled:
    trigger: "Player 3+ levels above gate"
    options: [Auto-succeed (no XP), Skip to appropriate content, Enhanced challenge (normal XP)]
  
  act_locks: "Must complete current act to access next act's gates, regardless of level"
```

---

## METERS

```yaml
SHADOW_DISPLAY:
  format: "🌫️🌫️🌫️⬜💎⬜⬛⬛⬛ 50 · Twilight"
  zones: ["Light (0-29)", "Twilight (30-70)", "Darkness (71-100)"]
  cells: "9 total: 3 light (🌫️) + 3 twilight (⬜) + 3 dark (⬛)"
  marker: "💎 replaces cell at current position, value and zone on same line"

LOYALTY_DISPLAY:
  format: "🟥🟥🟥🟨🟨🟨🟩💎🟩 Loyal"
  states: [Departed, Ultimatum, Questioning, Disappointed, Concerned, Loyal]
  icon: "AI selects contextually from ARCHETYPE_MAP emoji"
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
  archetype_ref: "protagonist"
  starting_level: 1
  starting_companion: "astral_panther"
  equipment: ["Basic scimitars", "Onyx figurine"]
```

---

## COMPANIONS

```yaml
BOUND:
  ASTRAL_PANTHER:
    archetype_ref: "astral_panther"
    type: "Summoned (no loyalty meter)"
    limit: "6 hours/day, 12 hour rest between"
    loses_if: "Figurine destroyed or lost"
    dismissal: "NEVER auto-dismiss. Let timer expire naturally. Exception: dismiss before long rest"

RECRUITED:
  DWARF_LEADER:
    archetype_ref: "dwarf_leader"
    leaves_if: [Betrayal, Oath-breaking, Cowardice]
  
  HALFLING_ROGUE:
    archetype_ref: "halfling_rogue"
    leaves_if: [Recklessness, Torture, Repeated endangerment]
  
  HUMAN_ARCHER:
    archetype_ref: "human_archer"
    leaves_if: [Slavery, Mass casualties, Tyranny]
  
  BARBARIAN_WARRIOR:
    archetype_ref: "barbarian_warrior"
    leaves_if: [Cowardice, Dishonorable combat, Attacking helpless]

DARK_PATH:
  trigger: "Shadow > 60 AND recruited companion departed"
  DROW_ASSASSIN: { archetype_ref: "drow_assassin", joins_if: "Shadow > 65", leaves_if: [Weakness, Repeated mercy] }
  DEMON_BOUND: { archetype_ref: "demon_bound", joins_if: "Shadow > 70 + demonic contact", leaves_if: [Reject power, Redemption] }
  DUERGAR_MERCENARY: { archetype_ref: "duergar_mercenary", joins_if: "Shadow > 60 + gold", leaves_if: [Non-payment, Free slaves] }
  UNDEAD_SERVANT: { archetype_ref: "undead_servant", joins_if: "Shadow > 80 + ritual", type: "Bound (no loyalty meter)" }
```

---

## ANTAGONISTS

```yaml
DROW_HOUSES:
  archetype_ref: "drow_houses"
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
DROW_CITY: { archetype_ref: "drow_city", shadow: "High=ally, Low=hunt" }
MERCENARY_BAND: { archetype_ref: "mercenary_band", interaction: "Payment" }
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
  level_filtering:
    visible_range: "(player_level - 2) to (player_level + 2)"
    below_range: "Show as ⬇️ TRIVIAL (reduced/no XP)"
    above_range: "Show as 🔒 LOCKED (Requires Level X)"
  distribution:
    at_level: "60%"
    above_1-2: "25% (show with ⚠️)"
    above_3+: "15% (show as 🔒 LOCKED if >2 above)"
  refresh: "1d4 per 3 days (time-based, not completion)"
  contract_types:
    standard: [Monster hunts, Escort, Smuggling, Bounty]
    redemption: [Rescue, Defend, Expose corruption, Free slaves]
    darkness: [Intimidation, Raids, Eliminate witnesses]
  warnings: "⚠️ above level, 🔒 locked (>2 above)"
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
  
  other_ai:
    action: "Output as markdown code block"
    steps:
      1: "Generate save content per SAVE_TEMPLATE"
      2: "Wrap in ```markdown code fence"
      3: "Say: 'Copy this entire save file and store it safely.'"

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

HEADER_METRICS: "🌫️ Shd [VALUE] | 🐆 [STATUS] | 👥 [COUNT]"

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
  # recruited: archetype_ref, status, loyalty_state, loyalty_position, hp, relationship_note

WEAVE_STATE:
  # T1_active: [current party companions by archetype_ref]
  # T2_position: current rotation index
  # T3_position: current rotation index
  # last_weave: T[N] archetype_ref

CAMPAIGN_STATE:
  # shadow: value, zone, recent_changes
  # faction_standing: per faction

PROGRESS:
  # current_act, current_gate, gate_phase
  # objectives: completed, remaining
  # gate_history: gate, outcome, shadow_change (one line each)
  # hubs_unlocked, background_tasks
  # next_light_dump: T[N], next_full_dump: T[N]

NARRATIVE:
  # active_threads, npcs_of_note, resolved_threads

CURRENT_SITUATION:
  # location, context (2-3 sentences), party_condition, immediate_threats
```

**Key principle:** Save state data, not rules. AI reconstructs mechanics from training.

---

**END CAMPAIGN CORE v6.0**
