# CAMPAIGN: RENEGADE

```yaml
VALIDATION: {type: "campaign_core", campaign: "Renegade", kernel_requires: "6.2+", echo: "✅ CORE: Renegade v6.2.6 | Shadow: 0-100 | Acts: 1-4 | Status: READY"}
```

## STARTUP

```yaml
STARTUP:
  diagnostics: "✅ Kernel: [version] | Campaign: Renegade | Acts: [loaded] | Archetypes: Ready | Shadow: 50 | Gates: Active"
  then: "TITLE → INTRO → CHARACTER_CONFIRMATION → FIRST_GATE"
  /boot: |
    ═══════════════════════════════════════
    🎮 SKELETAL DM BOOT SEQUENCE
    ═══════════════════════════════════════
    📁 Kernel: [version] | Campaign: Renegade | Acts: [loaded]
    🎭 Archetypes: Ready | ⚙️ Shadow: 50 | Gates: Active | Dumps: mod 6/12
    ═══════════════════════════════════════

TITLE: "RENEGADE - A Skeletal DM Campaign"

INTRO: |
  Born in darkness. Trained to kill, to serve the dark goddess.
  The great drow city was your world. But something broke. You fled.
  The Drow Shadow measures your soul. Are you ready?

CHARACTER_CONFIRMATION: "Show protagonist using inferred name from ARCHETYPE_MAP"

INITIALIZE: {shadow: 50, level: 1, companions: [astral_panther], location: "drow_city"}

FIRST_GATE: "GATE_1.1_HOUSE_FALL"

FROM_SAVE: {restore: "All values from STATE_SUMMARY", resume: "Gate/location from save"}
```

---

## ARCHETYPE_MAP

```yaml
ARCHETYPE_MAP:
  # Characters
  protagonist: {desc: "iconic renegade drow ranger, dual scimitars, fled great drow city, astral panther companion", emoji: 🥷}
  astral_panther: {desc: "astral panther from onyx figurine, loyal magical beast", emoji: 🐆}
  dwarf_leader: {desc: "iconic dwarven king, steadfast companion, battleaxe, honorable", emoji: 🪓}
  halfling_rogue: {desc: "iconic halfling rogue, clever, quick with knives, self-preservation", emoji: 🗡️}
  human_archer: {desc: "iconic human archer raised by dwarves, hates slavery/tyranny", emoji: 🏹}
  barbarian_warrior: {desc: "iconic redeemed barbarian, massive human seeking redemption", emoji: ⚔️}
  mentor_blademaster: {desc: "legendary drow weapons master who rejected cruelty", emoji: ⚔️}
  # Dark Path
  drow_assassin: {desc: "ruthless drow assassin, respects only strength", emoji: 🗡️}
  demon_bound: {desc: "entity bound through demonic pact", emoji: 👿}
  duergar_mercenary: {desc: "gray dwarf mercenary, loyal to gold", emoji: ⛏️}
  undead_servant: {desc: "undead bound through dark ritual", emoji: 💀}
  # Locations
  drow_city: {desc: "iconic great drow city, vast underground ruled by noble houses and dark goddess"}
  drow_houses: {desc: "iconic drow noble houses, competing matriarchal families"}
  mercenary_band: {desc: "iconic drow mercenary organization, neutral Underdark sellswords"}
```

---

## WEAVE_ROTATION

```yaml
WEAVE_ROTATION:
  T1_CRITICAL: {rotation: [astral_panther, dwarf_leader, halfling_rogue, human_archer, barbarian_warrior], rule: "Active party only"}
  T2_CORE:
    rotation: [drow_pursuit, faction_standing, shadow_consequence, equipment_state]
    refs: {drow_pursuit: "hunters/tracking/paranoia", faction_standing: "reputation affects interactions", shadow_consequence: "NPC reactions/dreams/self-doubt", equipment_state: "twin scimitars/figurine/supplies"}
  T3_THREADS:
    rotation: [mentor_fate, house_politics, surface_rumors, past_sins]
    refs: {mentor_fate: "blademaster guilt/hope", house_politics: "pursuit intensity", surface_rumors: "opportunity/danger", past_sins: "haunting/tempting"}
```

---

## TRACKED_METRICS

```yaml
TRACKED_METRICS:
  format: "🌫️ Shd [VALUE] | 🐆 [STATUS] | 👥 [COUNT]"
  sources: {shadow: "DROW_SHADOW.value", panther: "summon time or 'Ready'", party: "companion count"}
  example: "🌫️ Shd 50 | 🐆 4h | 👥 2"
```

---

## METADATA

```yaml
METADATA: {title: "Renegade", tagline: "What path will you take to achieve glory?", kernel: "6.2+", levels: "1-12+", themes: [moral_choice, survival, redemption, conquest], tone: "dark, gritty, fast-paced"}
```

---

## FILE_STRUCTURE

```yaml
FILES: {core: "CAMPAIGN_RENEGADE_core.md", early: "CAMPAIGN_RENEGADE_acts_1-3.md", endgame: "CAMPAIGN_RENEGADE_act_4.md"}

STARTUP_LOGIC:
  acts_1-3: {no_save: "Fresh start Gate 1.1", with_save: "Resume from save"}
  act_4: {no_save: "ERROR - need Acts 1-3 STATE_SUMMARY", with_save: "Resume - active_path determines gates"}

ACT_4_TRANSITION: {trigger: "Act 3 STATE_SUMMARY", prompt: "Act 3 complete. Save STATE_SUMMARY. Continue: Kernel + core + act_4 + STATE_SUMMARY"}
```

---

## ANCHORS

```yaml
ANCHORS: {primary: "Underdark survival, drow exile, redemption or conquest, found family", tone: "Gritty realism, consequences, companions are people"}
MOMENTUM_THREADS: "Gate start: d20, 15+ = reintroduce unresolved NPC/thread"
```

---

## VARIABLES

```yaml
DROW_SHADOW: {range: "0-100", start: 50, meaning: "violence vs mercy", thresholds: {redemption: "<30@Act4", darkness: ">70@Act4", neutral: "30-70"}, effects: [content_gating, faction_reactions, companion_availability, skill_modifiers]}

MERCY_RISK: "Released enemies: 25% return hostile within 1d4 gates. Track max 5 in TASKS. Oldest drops off."

PROGRESSION: {philosophy: "Earn power. No rubber-banding.", range: "1-12+", gate_access: "±2 levels"}

LEVEL_GATING:
  rule: "Available: (level ± 2) | >2 above = 🔒 LOCKED"
  overleveled: {trigger: "3+ above gate", effects: [half_xp, trivial, no_loot_upgrade]}
  warnings: {⬇️: "Trivial", ⚠️: "Above level", 🔒: "Locked"}

LOYALTY_DISPLAY: {format: "🟥🟥🟥🟨🟨🟨🟩💎🟩 Loyal", states: [Departed, Ultimatum, Questioning, Disappointed, Concerned, Loyal], marker: "💎 inline"}
```

---

## PREMISE

You are a dark elf renegade fleeing the great drow city. The dark goddess's domain broke something in you—or revealed what you truly are. Now you run, hunted by your own kind.

**This is not predetermined heroism. This is a story of choice.**

---

## PROTAGONIST

```yaml
PROTAGONIST: {ref: "protagonist", level: 1, companion: "astral_panther", equipment: ["Basic scimitars", "Onyx figurine"]}
```

---

## COMPANIONS

```yaml
COMPANION_RULES:
  on_join: "Match PC level. DM auto-selects optimal class features, skills, spells."
  xp: "Split among party. Companions level with PC."
  combat: "DM controls. Player may suggest tactics."

COMPANIONS:
  BOUND:
    astral_panther: {ref: "astral_panther", type: "Summoned", limit: "6h/day, 12h rest", loses_if: "figurine lost", dismissal: "Never auto-dismiss"}
  RECRUITED:
    dwarf_leader: {ref: "dwarf_leader", leaves: [Betrayal, Oath-breaking, Cowardice]}
    halfling_rogue: {ref: "halfling_rogue", leaves: [Recklessness, Torture, Repeated endangerment]}
    human_archer: {ref: "human_archer", leaves: [Slavery, Mass casualties, Tyranny]}
    barbarian_warrior: {ref: "barbarian_warrior", leaves: [Cowardice, Dishonorable combat, Attacking helpless]}
  DARK_PATH:
    trigger: "Shadow > 60 AND recruited departed"
    drow_assassin: {ref: "drow_assassin", joins: ">65", leaves: [Weakness, Repeated mercy]}
    demon_bound: {ref: "demon_bound", joins: ">70 + demonic contact", leaves: [Reject power, Redemption]}
    duergar_mercenary: {ref: "duergar_mercenary", joins: ">60 + gold", leaves: [Non-payment, Free slaves]}
    undead_servant: {ref: "undead_servant", joins: ">80 + ritual", type: "Bound"}
```

---

## ANTAGONISTS

```yaml
ANTAGONISTS:
  drow_houses: {ref: "drow_houses", arc: ">70 negotiate | <30 eternal enemies"}
  underdark_threat: {type: "Demon cult or invasion", arc: "Redemption final enemy"}
  surface_kingdoms: {type: "Variable by Shadow", arc: "Darkness conquest target"}
  former_companions: {type: "Departed may oppose", arc: "Act 4 confrontation if high Shadow"}
```

---

## FACTIONS

```yaml
FACTIONS:
  drow_city: {ref: "drow_city", shadow: "High=ally, Low=hunt"}
  mercenary_band: {ref: "mercenary_band", interaction: "Payment"}
  surface_kingdoms: {shadow: "High=fear, Low=alliance"}
  deep_gnomes: {interaction: "Actions > words, suspicious"}
  duergar: {interaction: "Respect power, exploit weakness"}
  slavers: {shadow: "High=work with, Low=enemies"}
  demon_cults: {interaction: "Usually antagonist"}
```

---

## WORLD

```yaml
UNDERDARK: {environment: "Hostile, total darkness, 3D maze", rest_danger: "50% encounter open", wild_magic: "Teleport unreliable, divination blocked", dangers: [Aberrations, Drow patrols, Demons, Predators]}
SURFACE: {prejudice: "Drow feared on sight", opportunity: "Prove yourself or dominate"}
```

---

## MAP_PALETTE

```yaml
MAP_PALETTE:
  walls: {cave: 🪨, worked: 🧱, fungal: 🍄, web: 🕸️, wood: 🪵}
  floors: {stone: ⬛, water: 🟦, lava: 🟧, pit: 🕳️, moss: 🟩, grass: 🌿, river: 🌊}
  terrain: {door: 🚪, chest: 📦, boulder: 🪨, statue: 🗿, altar: ⛩️, crystal: 💎, bones: 🦴, fire: 🔥, stairs: 🪜, grave: 🪦, candle: 🕯️, bed: 🛏️, barrel: 🛢️, tracks: 🐾}
  items: {treasure: 💰, potion: 🧪, scroll: 📜, urn: 🏺}
  humanoid: {generic: 👤, mage: 🧙, guard: 💂, knight: 🛡️, troll: 🧌}
  undead: {skeleton: 💀, zombie: 🧟, ghost: 👻, vampire: 🧛}
  aberration: {mind_flayer: 🐙, beholder: 👁️, hook_horror: 🦂, umber_hulk: 🐜, cloaker: 🦇, grick: 🪱}
  demon: {lesser: 👿, greater: 😈, imp: 👹}
  beast: {spider: 🕷️, bat: 🦇, rat: 🐀, snake: 🐍, scorpion: 🦂, wolf: 🐺, bear: 🐻, frog: 🐸, dragon: 🐉}
  surface: {tree: 🌲, villager: 👤}
  hazards: {fire: 🔥, web: 🕸️, pit: 🕳️, corpse: 💀, gas: 🌫️, trap: ⚠️, poison: ☠️, explosion: 💥, lightning: ⚡, blood: 🩸}
  death: {skull: 💀, crossbones: ☠️, bone: 🦴, blood: 🩸, eliminated: ❌, coffin: ⚰️, grave: 🪦}
  magic: {effect: ✨, orb: 🔮, portal: 🌀}
```

---

## HUBS & MISSIONS

```yaml
HUBS: {purpose: "Rest, resupply, missions", types: [Deep gnome refuge, Duergar outpost, Frontier town, Barbarian camp], backtracking: true}

MISSION_BOARDS:
  PURPOSE: "Side content only. XP, gold, reputation, flavor."
  RULE: "Missions NEVER satisfy gate objectives or overlap current gate content."
  slots: 5-7
  visibility: "(level ± 2) | ⬇️ TRIVIAL | 🔒 LOCKED (>2 above)"
  distribution: "60% at-level | 25% +1-2 (⚠️) | 15% +3+ (🔒)"
  refresh: "1d4/3 days"
  types: {standard: [Hunt, Escort, Smuggle, Bounty], redemption: [Rescue, Defend, Expose, Free], darkness: [Intimidate, Raid, Eliminate]}
```

---

## STRUCTURE

```yaml
ACTS:
  - "Act 1: The Fall (L1-2) - Escape and exile"
  - "Act 2: The Hungry Dark (L2-5) - Survival and temptation"
  - "Act 3: Twilight Realms (L5-8) - Identity and faction politics"
  - "Act 4: The Reckoning (L8-12) - Path splits by Shadow"
```

---

## ENDINGS

```yaml
ENDINGS:
  REDEMPTION: {legendary: "0-15 sacrifice", proven: "16-25 victory", tarnished: "26-35 questionable"}
  DARKNESS: {eternal_tyrant: "90-100 terror", dark_emperor: "71-89 brutal"}
  NEUTRAL: {free_state: "35-55 refuge", wary: "56-70 strength"}
  FAILURE: {death: "No resurrection", catastrophic: "World too damaged"}
```

---

## SAVE_SYSTEM

```yaml
SAVE: {command: "/save", output: "RENEGADE_Save_[Name]_[Date].md"}
```

### SAVE_TEMPLATE

```yaml
# ⚠️ Load kernel + core + acts + this save TOGETHER
FILES: {kernel: "[filename]", core: "[filename]", acts: "[filename]"}
META: {campaign: "Renegade", saved: "[timestamp]", kernel: "[version]", turn: T[N]}

# === CHARACTER ===
PC: {name, class, subclass, level, xp, xp_next}
STATS: {str, dex, con, int, wis, cha, prof: +N, ac, hp: "current/max", hit_dice: "remaining/total"}
SAVES: [proficient saves]
SKILLS: {proficient: [], expertise: []}
CLASS: {fighting_style, favored_enemy: [], favored_terrain: [], archetype, features_chosen: []}
SPELLS: {known: [], slots: "remaining/max per level"}
CONDITIONS: []

# === INVENTORY ===
GOLD: N
EQUIPPED: {armor, weapons: [], shield}
MAGIC: [{item, charges: "N/max", attunement: bool}]
CONSUMABLES: [{item, qty}]
QUEST_ITEMS: []
GEAR: []

# === PARTY ===
HEADER_METRICS: "🌫️ Shd [N] | 🐆 [status] | 👥 [N]"

BOUND:
  astral_panther: {summoned: bool, time_remaining: "Nh", hp: "N/26", figurine: "intact|lost|destroyed"}

RECRUITED:
  # Per companion: {ref, hp: "N/max", loyalty: "🟩|🟨|🟥 [State]", position: N/10, note: "relationship context"}

DEPARTED: []  # Track who left and why for Act 4 confrontations

# === WEAVE ===
WEAVE: {T1_active: [party archetypes], T1_index: N, T2_index: N, T3_index: N, last: "T[N] [archetype]"}

# === CAMPAIGN ===
SHADOW: {value: N, zone: "redemption|neutral|darkness", recent: "+/-N [reason]"}
FACTIONS: {drow_city: "hostile|neutral|ally", deep_gnomes: "...", duergar: "...", surface: "..."}

# === PROGRESS ===
LOCATION: {area: "[name]", hub: "[nearest unlocked]", day: N, time: "HH:MM"}
GATE: {act: N, gate: "N.N", phase: "early|mid|late", objectives: {done: [], remaining: []}}
GATE_HISTORY: ["G1.1: [outcome] Δshd[N]", "G1.2: ..."]  # One line per gate
HUBS_UNLOCKED: []
TASKS: {background: [], alerts: [], timers: [{name, expires: "Day N HH:MM"}]}
DUMPS: {next_light: T[N], next_full: T[N], next_align: T[N]}

# === NARRATIVE ===
THREADS: {active: [], pending: [], resolved: []}
NPCS: [{name, status: "alive|dead|unknown", disposition: "friendly|neutral|hostile", last_seen: "Gate N.N"}]
MENTOR_FATE: "unknown|dead|alive|rescued"  # Campaign-specific tracking

# === SITUATION ===
CONTEXT: "[2-3 sentences: where, doing what, immediate circumstances]"
PARTY_CONDITION: "fresh|tired|wounded|critical"
THREATS: []
```

**Principle:** State only. AI reconstructs mechanics from training + kernel.

---

**END CAMPAIGN CORE v6.2.6**
