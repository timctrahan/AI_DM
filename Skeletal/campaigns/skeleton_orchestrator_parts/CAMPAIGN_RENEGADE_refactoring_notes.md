# Campaign Renegade Refactoring Notes

## Session: 2024-12-29

This document captures structural changes made to the Skeletal DM system that affect campaign orchestrator design.

---

## FILE STRUCTURE CHANGES

### Before
```
SKELETAL_DM_KERNEL_v5_4.md
CAMPAIGN_RENEGADE_overview.md
CAMPAIGN_RENEGADE_act_1.md
CAMPAIGN_RENEGADE_act_2.md
CAMPAIGN_RENEGADE_act_3.md
CAMPAIGN_RENEGADE_act_4.md (router)
CAMPAIGN_RENEGADE_act_4_redemption.md
CAMPAIGN_RENEGADE_act_4_darkness.md
CAMPAIGN_RENEGADE_act_4_neutral.md
```

### After
```
SKELETAL_DM_KERNEL_v5_5.md
CAMPAIGN_RENEGADE_core.md          # Renamed from "overview"
CAMPAIGN_RENEGADE_acts_1-3.md      # Combined, optimized
CAMPAIGN_RENEGADE_act_4.md         # Combined all paths, no router
```

### Key Changes
- "overview" renamed to "core"
- Acts 1-3 combined into single file
- Act 4 router eliminated - paths combined into single file
- Individual act files (act_1, act_2, etc.) no longer distributed separately
- Build script needed to concatenate source files into distribution files

---

## KERNEL ADDITIONS (v5.4 → v5.5)

### MISSION_BOARDS
```yaml
MISSION_BOARDS: "If campaign defines hubs with mission boards, generate contracts per campaign rules. Show suggested level, warn on dangerous selections, honor player choice."
```

### STATE_SUMMARY
```yaml
STATE_SUMMARY: "On act completion or /save command, generate FULL state capture: complete character sheet (abilities, HP, AC, attacks, spells, features), full inventory, all companion sheets (bound and recruited), meters, factions, unlocked hubs, flags, key choices, active threads, session notes. Be thorough - this refreshes context and serves as checkpoint."
```

---

## CAMPAIGN CORE STRUCTURE CHANGES

### FILE_STRUCTURE Section (New)
Campaigns must now define:
```yaml
FILE_STRUCTURE:
  files:
    core: "CAMPAIGN_[NAME]_core.md"
    early_game: "CAMPAIGN_[NAME]_acts_1-3.md"
    endgame: "CAMPAIGN_[NAME]_act_4.md"
  
  startup_logic:
    acts_1-3:
      no_save: "Fresh start - begin Gate 1.1"
      with_save: "Resume from save location"
    act_4:
      no_save: "ERROR - Request STATE_SUMMARY"
      with_save: "Resume - active_path determines path"
  
  act_4_transition:
    trigger: "Act 3 STATE_SUMMARY generated"
    prompt: "User instruction to load act_4 + STATE_SUMMARY"
```

### COMPANION Categories
Companions now split into categories:

```yaml
BOUND:
  # No loyalty meter, magical binding
  # Example: Astral panther, undead servants
  loses_if: "Item destroyed or lost"

RECRUITED:
  # Has loyalty meter
  # Example: Bruenor, Regis, Catti-brie, Wulfgar
  leaves_if: [trigger conditions]

DARK_PATH:
  # Available when Shadow > 60 AND recruited companion departed
  # Some are BOUND (undead), some are RECRUITED (assassin)
```

### MOMENTUM_THREADS (New - Campaign-Specific)
```yaml
MOMENTUM_THREADS: "At gate start, roll d20. On 15+, reintroduce one unresolved NPC or thread from prior choices."
```

---

## METER DISPLAY STANDARDIZATION

### Unified Visual System
Both Shadow and Loyalty use same pattern:
- Static bar (doesn't change)
- Moving marker (▲) shows position
- Left = bad, Right = good

### Shadow Meter
```
🌫️🌫️🌫️🌫️🌫️🌫️⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛
          ▲
     [zone name]
```
- 🌫️ = Light (0-29)
- ⬜ = Twilight (30-70)
- ⬛ = Darkness (71-100)

### Loyalty Meter
```
🟥🟥🟥🟥🟥🟥🟥🟨🟨🟨🟨🟨🟨🟩🟩🟩🟩🟩🟩🟩
                              ▲
                          [state]
```
- 🟥 = Danger/Departed (left)
- 🟨 = Warning
- 🟩 = Loyal (right)

### Contextual Companion Emoji
AI selects appropriate emoji per companion:
- 🪓 Dwarf (axe)
- 🐆 Panther
- 🏹 Archer
- 💪 Barbarian
- Not hardcoded in campaign file

---

## PROGRESSION PHILOSOPHY CHANGES

### Before
- Specific XP totals per act
- Level ranges as requirements

### After
```yaml
PROGRESSION:
  philosophy: "Earn your power. No rubber-banding. Over-level = easier future."
  level_range: "1-12+ (no cap)"
  gate_levels: "Recommended, not required. Fixed CR per gate."
```

### Key Principles
1. No level cap enforcement
2. Gates have recommended levels, not requirements
3. Encounters don't scale UP to player level
4. Over-leveling is reward, not punished
5. Bosses have fixed stats
6. Narrative acknowledges player power level

---

## MISSION BOARD SYSTEM

### Defined in Campaign Core
```yaml
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

### Hubs Reference Mission Boards
```yaml
DEEP_GNOME_OUTPOST:
  unlocked_at: Gate 1.6
  mission_board: [standard, redemption]
```

---

## ACT FILE CONSOLIDATION

### Combined Acts 1-3 Structure
```
# ACTS 1-3

## GATE_LEVELS
[All 18 gates in one block]

## PHASE_RESTRICTIONS
[All three acts in one block]

## HUBS
[All early-game hubs consolidated]

## ACT 1 GATES
### GATE_1.1_HOUSE_FALL
...

## ACT 2 GATES
### GATE_2.1_ABERRATION_TERRITORY
...

## ACT 3 GATES
### GATE_3.1_HUNTERS_FROM_HOME
...

## ACT_3_COMPLETION
[Path determination + prompt]
```

### Combined Act 4 Structure
```
# ACT 4: THE RECKONING

## PATH_DETERMINATION
[Shadow thresholds]

## GATE_LEVELS
[All three paths in one block]

## HUBS
[All three path hubs consolidated]

## REDEMPTION GATES
### GATE_4R.1_THREAT_REVEALED
...

## DARKNESS GATES
### GATE_4D.1_POWER_BASE
...

## NEUTRAL GATES
### GATE_4N.1_CLAIM_TERRITORY
...
```

---

## SHADOW_RANGE OPTIMIZATION

### Before
Every gate had explicit shadow_range with all options:
```yaml
shadow_range: "Aid fully -4-6 | Betray +8-10 | Abandon +2 | Contextual"
```

### After
Only big swings specified. AI infers obvious cases.

**Keep:**
- Betray +8-10
- Join cult +15-20
- Slavery participation +10-15 / Liberation -8-10
- Join raiders +12-15
- Raid peaceful settlement +12
- Kill former companions +8-10 / mercy -8-10
- Total annihilation +6-10
- Torture +8-10
- Alliance shifts ±8-12
- Unexpected reform -8-12

**Removed (AI infers):**
- Standard mercy/cruelty ranges
- Combat victory +0
- Neutral options
- Obvious good/evil choices

---

## STATE_SUMMARY FORMAT

### Generated at Act Completion or /save

Full state capture includes:
- Complete character sheet (abilities, HP, AC, attacks, spells, features)
- Full inventory with all items
- All companion sheets (bound and recruited separately)
- Meters (Shadow value, loyalty values)
- Faction standings
- Unlocked hubs
- Flags and story state
- Key choices made
- Active threads
- Session notes
- Current location
- Next gate

### Path Determination in Save
Act 3 completion STATE_SUMMARY includes:
```yaml
active_path: "REDEMPTION | DARKNESS | NEUTRAL"
```
This allows Act 4 restart without recalculating from Shadow.

---

## IP-CLEAN RENDERING

### Archetype System
```yaml
ARCHETYPE_SYSTEM:
  directive: "All characters/locations marked with archetype pointers - AI renders from training knowledge"
```

### Pattern
Instead of proper nouns in file:
```yaml
DWARF_LEADER:
  archetype: "iconic dwarven king companion"
```

AI renders as the actual character from training.

### IP-Clean Replacements Made
- "Menzoberranzan" → "the great drow city"
- "Spider Queen" / "Lolth" → "the dark goddess"
- "Bregan D'aerthe" → "drow mercenary bands"
- "faerzress" → "wild magic zones"
- Character names → archetype descriptions

---

## REMOVED REDUNDANCIES

### From Campaign Files
- `completion: "Award XP"` - AI knows to award XP
- `joins: Act 1` - Gates define when companions can join
- Repeated `render_from_source` per character
- Verbose AI behavior instructions
- Format templates (just show examples)
- `show_on` / `hide_on` rules for meters
- Individual act headers/footers when combined
- Excessive `---` separators

### Token Savings
- Campaign core: 468 → ~270 lines (42% reduction)
- Acts 1-3 combined: 631 → 434 lines (31% reduction)
- Act 4 combined: 494 → 401 lines (19% reduction)

---

## BUILD SCRIPT REQUIREMENTS

### Source Files (in repo)
```
CAMPAIGN_RENEGADE_core.md
CAMPAIGN_RENEGADE_act_1.md
CAMPAIGN_RENEGADE_act_2.md
CAMPAIGN_RENEGADE_act_3.md
CAMPAIGN_RENEGADE_act_4_redemption.md
CAMPAIGN_RENEGADE_act_4_darkness.md
CAMPAIGN_RENEGADE_act_4_neutral.md
```

### Build Output
```
CAMPAIGN_RENEGADE_core.md (copy as-is)
CAMPAIGN_RENEGADE_acts_1-3.md (concatenate act_1 + act_2 + act_3)
CAMPAIGN_RENEGADE_act_4.md (concatenate redemption + darkness + neutral)
```

Note: The optimized combined files were hand-crafted with consolidation. A simple concatenation won't achieve the same token savings. The source files should be updated to match the optimized structure, OR the optimized files become the new source.

---

## STARTUP LOGIC

### New Game (Acts 1-3)
```
Load: Kernel + core + acts_1-3
No save: Fresh start at Gate 1.1
With save: Resume from save location
```

### Continue to Act 4
```
Load: Kernel + core + act_4 + STATE_SUMMARY
No save: ERROR - request STATE_SUMMARY
With save: Resume, active_path determines which gates to use
```

---

## SUMMARY OF BREAKING CHANGES

1. **File names changed** - overview → core
2. **File structure changed** - individual acts → combined packs
3. **Companion categories added** - BOUND vs RECRUITED
4. **STATE_SUMMARY required** for Act 4 start
5. **shadow_range mostly removed** - only big swings remain
6. **XP tracking removed** from gates - just "Award XP"
7. **Mission boards** now campaign-defined system
8. **MOMENTUM_THREADS** new campaign feature

---

## RECOMMENDATIONS FOR ORCHESTRATOR

1. Update file references to new names
2. Handle BOUND vs RECRUITED companions differently
3. Generate STATE_SUMMARY at act completion
4. Include active_path in Act 3+ saves
5. Validate STATE_SUMMARY presence for Act 4
6. Support /save command triggering STATE_SUMMARY
7. Implement MOMENTUM_THREADS roll at gate start
8. Generate mission board contracts per hub type
9. Track hub unlock state
10. Remove XP math - just award appropriate XP per gate difficulty
