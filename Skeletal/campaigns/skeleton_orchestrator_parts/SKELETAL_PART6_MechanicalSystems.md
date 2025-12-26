## MECHANICAL SYSTEMS

Convert between campaign paradigms on demand.

```yaml
PROGRESSION_TYPES:
  GATE_BASED:
    structure: "level_up_to: X" in gate definitions
    converts_to_XP: |
      - Add xp_thresholds to CAMPAIGN_VARIABLES
      - Replace level_up_to with xp_award per gate
      - Calculate XP curve from level range

  XP_BASED:
    structure: "xp_award: X" in consequences
    converts_to_GATE: |
      - Remove xp_thresholds
      - Identify level-up gates from XP curve
      - Replace xp_award with level_up_to at key gates

  MILESTONE:
    structure: "milestone: true" flag on narrative gates
    note: Hybrid - can combine with XP or gate-based

QUEST_DISCOVERY:
  LINEAR:
    structure: Gates flow sequentially
    converts_to_HUB: |
      - Identify optional/side content
      - Group into quest_pool
      - Create LOCATION_HUB with BULLETIN_BOARD
      - Main quest remains linear backbone

  HUB_BASED:
    structure: BULLETIN_BOARD with quest_pool
    converts_to_LINEAR: |
      - Flatten quest_pool into gate sequence
      - Assign recommended order
      - Remove bulletin board mechanics

BULLETIN_BOARD_TEMPLATE:
  LOCATION_HUB_[NAME]:
    type: QUEST_HUB

    BULLETIN_BOARD:
      refresh: "per session or X in-world days"
      slots: 3

      quest_pool:
        - QUEST_ID (type, cr, repeatable?)

      generation_rules:
        - "Always 1 combat option"
        - "Always 1 non-combat option"
        - "Third slot random from eligible"

CONVERSION_PROCESS:
  1: Identify current system
  2: Confirm target system
  3: Show conversion impact summary
  4: Execute conversion on approval
  5: Output reformatted file(s)

EXAMPLE_CONVERSION:
  request: "Convert to XP-based progression"

  response: |
    Current: Gate-based (levels at gates 1.5, 2.5, 3.1, 4.2, 5.1)
    Target: XP-based

    Conversion impact:
    - Add xp_thresholds (5e standard or custom?)
    - 23 gates will receive XP awards
    - Level-up gates become high-XP awards

    Proceed with 5e standard XP curve?
```
