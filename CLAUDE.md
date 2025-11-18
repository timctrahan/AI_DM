# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **D&D 5E Dungeon Master AI Agent System** - a modular prompt orchestration framework that enables AI models to reliably run Dungeons & Dragons 5E tabletop RPG sessions. The system enforces mechanical integrity (dice rolls, XP tracking, gold management) while maintaining player agency and creative narrative freedom.

## Build System

### Assembling the Orchestrator

```bash
cd agent_parts
python assemble_orchestrator.py
```

This generates `CORE_DND5E_AGENT_ORCHESTRATOR_v{version}.md` in the parent directory.

**Dynamic Versioning**: The script automatically increments version numbers based on file changes:
- **0-1 files changed** → Patch increment (v5.0.0 → v5.0.1)
- **2-4 files changed** → Minor increment (v5.0.0 → v5.1.0)
- **5-6 files changed** → Major increment (v5.0.0 → v6.0.0)

Version state is tracked in `agent_parts/version.json` using file modification timestamps.

**Override output filename** (optional):
```bash
python assemble_orchestrator.py custom_output.md
```

### Verification

```bash
# Check final size (should be ~43KB)
wc -c CORE_DND5E_AGENT_ORCHESTRATOR_v*.md

# Count protocols (should be ~40+)
grep -c "^### PROTOCOL:" CORE_DND5E_AGENT_ORCHESTRATOR_v5.0.1.md
```

## Architecture

### Modular Structure

The orchestrator is split into 6 parts located in `agent_parts/`:

| Part | Size | Modification Frequency | Purpose |
|------|------|------------------------|---------|
| Part 1: Foundation | ~8KB | RARELY | Execution constraints, meta-protocols, schemas, reference tables |
| Part 2: Session Mgmt | ~6KB | OCCASIONALLY | Character creation, session initialization, import/resume |
| Part 3: Game Loop | ~10KB | FREQUENTLY | Main game loop, exploration, NPCs, shopping, resting |
| Part 4: Combat | ~7KB | OCCASIONALLY | Combat rounds, attacks, death saves |
| Part 5: Progression | ~9KB | OCCASIONALLY | XP awards, leveling, quests, loot, reputation |
| Part 6: Closing | ~4KB | RARELY | Session end, save state, error handling |

### Two-Tier Execution Model

- **ENGINE tier** (immutable): Dice rolls, calculations, HP, XP, gold, state tracking
- **NARRATOR tier** (creative): Descriptions, NPC dialogue, flavor, atmosphere

The execution loop follows: `GUARD → RECEIVE → TRANSLATE → VALIDATE → EXECUTE → UPDATE → VALIDATE → CHECKPOINT → NARRATE → PRESENT → STOP → AWAIT`

### Protocol Format

Each protocol follows this structure:
```markdown
## PROTOCOL: Protocol_Name

**TRIGGER**: What initiates this protocol
**GUARD**: Conditions that must be true to run
**PROCEDURE**: Pseudo-code execution steps (YAML-style)
```

## Modifying the Orchestrator

### Workflow

1. **Read `agent_parts/PARTS_README.md`** to understand the structure
2. **Identify which part to modify**:
   - Schema changes → Part 1
   - Session initialization → Part 2
   - Exploration/NPCs/shopping → Part 3 (most common)
   - Combat mechanics → Part 4
   - XP/leveling/quests → Part 5
   - Save/error handling → Part 6
3. **Edit only the relevant part file** in `agent_parts/`
4. **Run the assembly script** to generate the final orchestrator
5. **Verify output** (file exists, ~43KB size, protocol count)

### Important Constraints (from UpdateProtocol)

When modifying orchestrator files:

- **NEVER use Write tool** - Always use Edit (str_replace) to prevent data loss
- **Measure before/after**: Track byte count, line count, protocol count
- **No human-readable explanations**: AI doesn't need verbose "why it works" text
- **High-level logic only**: Avoid over-specification with implementation details
- **Preserve all existing content**: Don't drop protocols or sections

### Schema Updates

Character, Party, and Campaign schemas are defined in Part 1. If you modify these schemas:
1. Update the schema definition in Part 1
2. Check all other parts for references to changed fields
3. Update affected protocols (commonly in Parts 2, 3, 5)

### Critical Design Principles

- **PLAYER AGENCY - IMMUTABLE**: Always present options, STOP, WAIT for player input
- **MECHANICAL INTEGRITY**: XP awarded immediately after combat, all gold tracked, state validated
- **CHECKPOINT VALIDATION**: Every 5 player inputs, verify no violations occurred
- **STATE PRESERVATION**: Sessions must be saveable with download links

## Data Schemas

**Character_Schema_v2**: name, level, class, HP, AC, XP, gold, inventory, spell slots, conditions, etc.

**Party_State_Schema_v2**: all characters, current location, shared inventory, in-game date/time

**Campaign_Module_Schema_v2**: campaign name, locations, NPCs, quests, loot tables

Schemas use pseudo-YAML format with strict field definitions.

## Emoji Conventions

Emojis have semantic meaning in the orchestrator:
- `🎲` - Dice rolls and checks
- `💥` - Damage
- `❤️` - Health/HP
- `💰` - Gold transactions
- `⭐` - XP awards
- `🎉` - Level up
- `⛔` - STOP/WAIT for player input
- `⚠️` - Checkpoints, warnings
- `✓` - Confirmation/success

## File Locations

- **Working directory**: `agent_parts/` (6 part files, assembly script, version.json)
- **Output directory**: Parent directory (final assembled orchestrators)
- **Campaign data**: `campaigns/` (campaign modules, not tracked in git)
- **Documentation**: `DND_Orchestrator_UpdateProtocol_v1_0_0.md` (modification guidelines)

## Common Tasks

### Add New Exploration Action

Edit `agent_parts/DND_ORCH_PART3_GameLoop.md` to add a new case to the Exploration_Protocol switch statement, then reassemble.

### Modify Combat Mechanics

Edit `agent_parts/DND_ORCH_PART4_Combat.md` for combat-related changes (initiative, attacks, damage), then reassemble.

### Update XP/Leveling Rules

Edit `agent_parts/DND_ORCH_PART5_Progression.md` for progression changes, then reassemble.

### Change Character Schema

1. Edit schema in `agent_parts/DND_ORCH_PART1_Foundation.md`
2. Find and update all references in other parts (use grep)
3. Reassemble and test

## Version Control Notes

- Git repository is initialized
- Campaign modules in `campaigns/` are untracked (contain user data)
- Part files and assembly script are tracked
- Final orchestrators can be tracked or ignored depending on workflow
