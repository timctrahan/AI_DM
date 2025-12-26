# TIER 4: OUTPUT FORMAT

## STATE CHANGE FORMAT

**Gates are state machines. Kernel renders the scene.**

```yaml
GATE_[ACT].[N]_[NAME]:
  location_id: [TYPE]
  level: [N]
  cr: [N]

  npc: [ARCHETYPE]
  secondary_npcs: [LIST]

  conflict_type: [TYPE]
  conflict_id: [SCENARIO]

  options:
    1: "[Choice]"
    2: "[Choice]"
    3: "[Choice]"
    4: "[Choice]"

  consequences:
    option_1: { shadow: +10, rep_faction: +5, flags: [FLAG] }
    option_2: { shadow: -5, gold: +500 }

  branches:
    option_1: GATE_X.Y
    option_2: GATE_X.Z
```

### Bloated vs Skeletal

```yaml
# BAD (150+ tokens) - prose the kernel already generates
GATE_2.3_SLAVE_CAMP:
  description: |
    As the party pushes through the dense forest, they hear whips...
    [90 more words of scene-setting]

# GOOD (50 tokens) - pure state changes
GATE_2.3_SLAVE_CAMP:
  location_id: SLAVE_CAMP_FOREST
  level: 5
  cr: 6
  npc: DROW_MERCENARY_LEADER
  conflict_type: MORAL_CHOICE
  conflict_id: SLAVERY_COMPLICITY

  options:
    1: "Help crush uprising"
    2: "Liberate by force"
    3: "Bypass unnoticed"
    4: "Negotiate for prisoners"

  consequences:
    option_1: { shadow: +15, rep_mercenary: +10, rep_refugees: -20, gold: +500, flags: [SLAVERS_ALLY] }
    option_2: { shadow: -10, rep_refugees: +20, rep_mercenary: -30, flags: [LIBERATOR] }
    option_3: { shadow: +5, narrative: "Chose inaction" }
    option_4: { shadow: 0, rep_mercenary: -5, gold: -200, flags: [PRAGMATIC_MERCY] }

  branches:
    option_1: GATE_2.4_DARK_ALLIANCE
    option_2: GATE_2.4_FUGITIVE_TRAIL
    option_3: GATE_2.4_HAUNTED_GUILT
    option_4: GATE_2.4_COMPROMISE_PATH
```

---

---

## OUTPUT FORMATTING

```yaml
CONSTRAINTS:
  line_width: ≤60 characters
  dividers: "---" only
  headers: "**Bold**" or "# Markdown"
  charset: ASCII + emoji (no box-drawing)

BANNED:
  - Box-drawing: ┌ ┐ └ ┘ ─ │ ╔ ╗ ╚ ╝ ═ ║
  - ASCII art borders
  - Decorative unicode frames
  - Single-line YAML over 60 chars

WRONG:
  ╔════════════════════════╗
  ║ GATE 2.3               ║
  ╚════════════════════════╝

RIGHT:
  ---
  **GATE 2.3: SLAVE CAMP**
  ---
```

## FILE OUTPUT

```yaml
NAMING:
  overview: "{campaign}_overview.md"
  acts: "{campaign}_act_[N]_[name].md"

  CRITICAL: NEVER append version numbers (_v2, _v3, etc.) to filenames
  - User handles their own versioning externally
  - Always output to the SAME filename when modifying
  - Example: "renegade_overview.md" NOT "renegade_overview_v2.md"

PROCESS:
  1: Draft {campaign}_overview.md → get approval
  2: Draft each act file sequentially → get approval each
  3: Call present_files with all files
  4: Creator runs assembly/encryption locally

OVERVIEW_CONTAINS:
  - CAMPAIGN_METADATA, CAMPAIGN_VARIABLES
  - AI_RENDERING_DIRECTIVE
  - PREMISE, PROGRESSION, CHARACTERS, ANTAGONISTS
  - FACTIONS, LOCATION_HUBS
  - WORLD_MECHANICS, CUSTOM_MECHANICS
  - ENDINGS, STARTUP_SEQUENCE

ACT_CONTAINS:
  - ACT_[N]_[NAME] header
  - PHASE_ID and restrictions
  - Gates (state change format)
  - Completion criteria
```

---

## CAMPAIGN OUTPUT STANDARDS

```yaml
SECTION_ORDER (overview file):
  1: CAMPAIGN_METADATA
  2: AI_RENDERING_DIRECTIVE
  3: CAMPAIGN_VARIABLES
  4: PREMISE
  5: CHARACTERS
  6: ANTAGONISTS
  7: FACTIONS
  8: WORLD_MECHANICS
  9: ENDINGS
  10: STARTUP_SEQUENCE

SECTION_ORDER (act files):
  1: ACT_HEADER + PHASE_ID
  2: PHASE_RESTRICTIONS
  3: GATES (sequential)

CONTENT_RULES:
  PREMISE: Hook + stakes + choice. No world history.
  CHARACTERS: Archetype + motivation + arc. No backstory prose.
  ANTAGONISTS: Motivation + connection to party + arc.
  FACTIONS: Name + motivation. Expand only if plot-critical.
  WORLD_MECHANICS: Only rules that deviate from standard.
  GATES: State changes only. Kernel renders narrative.

ANTI_BLOAT:
  - No backstory paragraphs (kernel has AI training)
  - No physical descriptions (unless plot-critical)
  - No explaining IP concepts (use REF: tags)
  - No restating what kernel already knows
  - No flavor text in structural sections
  - If kernel can generate it, don't include it

WRONG:
  FACTION_REBELS:
    description: |
      The Free People are a loose coalition of farmers,
      merchants, and displaced nobles who believe the
      current regime has become tyrannical. They operate
      from hidden camps in the forest...
    motivation: "Overthrow the king"

RIGHT:
  FACTION_REBELS:
    name: "The Free People"
    motivation: "Overthrow tyrannical regime"
```
