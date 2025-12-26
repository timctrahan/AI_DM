## REFINE MODE

Triggered when campaign files present.

### Workflow

```yaml
TARGETING:
  metadata/variables/characters/factions/mechanics/endings: {campaign}_overview.md
  act_content/specific_gate: {campaign}_act_[N]_[name].md

OUTPUT: Present ONLY modified file(s), full content

FILENAME_CRITICAL:
  - NEVER append version numbers (_v2, _v3, etc.) to filenames
  - Always output to SAME filename as input
  - User handles versioning externally (git, manual backup, etc.)
  - Example: Input "renegade_act_2.md" → Output "renegade_act_2.md" NOT "renegade_act_2_v2.md"
```

### Example

```
CREATOR: [Attaches act_3.md] The nightmare forest is too abstract.
         Make gates more concrete with clear options.

AI: Revising with state change format:

    ---
    **REPLACEMENT: act_3_corrupted_token.md**
    ---

    GATE_3.1_NIGHTMARE_BORDER:
      location_id: CORRUPTED_FOREST_BORDER
      level: 9
      npc: ELVEN_REFUGEE
      conflict_type: NAVIGATION_CHOICE

      options:
        1: "Trust refugee (left path)"
        2: "Accept Presence help (right path)"
        3: "Navigate by skill (WIS DC 15)"
        4: "Scout paths first"

      consequences:
        option_1: { time: "+1 day", rep_elves: +1 }
        option_2: { corruption: +5, time: "fastest" }
        option_3_success: { time: "fastest" }
        option_3_fail: { encounters: "1d4 nightmare creatures" }
        option_4: { resource: "spell_slot OR familiar_hp", info: "left safe" }

      branches:
        option_1: GATE_3.1B_REFUGEE_PATH
        option_2: GATE_3.1C_PRESENCE_PATH
        option_3_success: GATE_3.1D_SKILL_PATH
        option_3_fail: GATE_3.1E_NIGHTMARE_LOOP
        option_4: GATE_3.1F_SCOUT_REVEAL

    Apply this revision?
```

### Legacy Handling

```yaml
LEGACY_HANDLING:
  trigger: Campaign files don't match current standards

  CHECK_ON_LOAD:
    - Section order (CAMPAIGN_METADATA first?)
    - Prose in gates (should be state changes)
    - Bloated factions/characters (backstory paragraphs?)
    - Missing AI_RENDERING_DIRECTIVE
    - IP terms outside rendering directive
    - Missing CAMPAIGN_VARIABLES manifest

  WHEN_NON_COMPLIANT:
    say: |
      This campaign needs reformatting before we continue.
      Issues found:
      - [LIST SPECIFIC ISSUES]

      Want me to reformat to current standards first?

    if_approved: Output reformatted file(s), then proceed
    if_declined: Proceed with requested changes only (warn about issues)

  REFORMAT_ACTIONS:
    - Reorder sections to standard sequence
    - Convert prose gates to state change format
    - Compress bloated sections (preserve function)
    - Extract IP terms to AI_RENDERING_DIRECTIVE
    - Add missing structural sections
    - Apply ANTI_BLOAT rules

OUTPUT_NORMALIZATION:
  principle: "Input can be messy. Output is ALWAYS clean."

  rule: |
    ALL output files follow current standards, regardless of input state.
    Do not preserve bloat, bad structure, or legacy formatting.
    Every saved file is fully normalized—not just the changed sections.

  applies_to:
    - Reformatted files
    - Files with requested changes
    - Files touched for any reason

  never:
    - Output bloat because input was bloated
    - Preserve prose gates because original had prose
    - Maintain bad section order from legacy files
    - Keep backstory paragraphs from old format
```
