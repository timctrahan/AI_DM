# D&D 5E Orchestrator - Modular Parts

## Structure

The orchestrator is broken into 6 modular parts for easier modification:

| Part | Size | Frequency | Contents |
|------|------|-----------|----------|
| Part 1 | ~8KB | RARELY | Foundation (Section 0, Meta-protocols, Schemas, Tables) |
| Part 2 | ~6KB | OCCASIONALLY | Session Management |
| Part 3 | ~10KB | FREQUENTLY | Game Loop & Exploration |
| Part 4 | ~7KB | OCCASIONALLY | Combat |
| Part 5 | ~9KB | OCCASIONALLY | Progression & Quests |
| Part 6 | ~4KB | RARELY | Session End & Error Handling |

## Usage

### Modifying a Part

1. Upload the specific part + UpdateProtocol to Claude
2. Request modification: "Add X to protocol Y in Part 3"
3. Claude modifies ONLY that part
4. Download modified part

### Assembling Final Orchestrator
```bash
# Place all 6 parts in same directory with version.json
python3 assemble_orchestrator.py

# Output: CORE_DND5E_AGENT_ORCHESTRATOR_v{version}.md in parent directory
# Version is automatically incremented based on number of changed files
```

**Dynamic Versioning**:
- Script reads `version.json` to get current version
- Compares file modification times to detect changes
- Version increment rules:
  - **0-1 files changed**: Patch increment (v4.0.0 → v4.0.1)
  - **2-4 files changed**: Minor increment (v4.0.0 → v4.1.0)
  - **5-6 files changed**: Major increment (v4.0.0 → v5.0.0)
- Updates `version.json` with new version and timestamp

**Override Version** (optional):
```bash
# Force specific filename
python3 assemble_orchestrator.py custom_output.md
```

### Verification
```bash
# Check assembly (use wildcard or latest version)
wc -c ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Should be ~43KB

# Verify all protocols present
grep -c "^### PROTOCOL:" ../CORE_DND5E_AGENT_ORCHESTRATOR_v5.0.0.md  # Should be ~40
```

## Benefits

- **Isolated modifications**: Change one part without risking others
- **Clear context**: Each part fits comfortably in Claude's context window
- **Easy verification**: Check individual part sizes
- **Version control**: Track changes per part
- **Reduced errors**: Can't accidentally drop Part 4 when modifying Part 3

## When to Modify Each Part

- **Part 1**: Changing priority rules, adding meta-protocols, schema updates
- **Part 2**: Character creation changes, session management updates
- **Part 3**: New exploration mechanics, NPC interactions, shopping changes (MOST COMMON)
- **Part 4**: Combat rule changes, new combat mechanics
- **Part 5**: XP/leveling changes, quest system updates
- **Part 6**: Save/load changes, execution rule updates

## File Descriptions

### Part 1: Foundation
- **Section 0**: Execution Constraints (Priority 0 rules)
- **Section 1**: Meta-Protocols (Correction_Protocol, State_Recovery_Protocol)
- **Section 2**: System Role and Execution Model
- **Section 3**: Data Schemas (Character, Party, Campaign)
- **Section 4**: Reference Tables (XP, Proficiency, Reputation)

### Part 2: Session Management
- **Section 5**: Session Management Protocols
  - Session_Initialization
  - Session_Start_Decision
  - New_Session_Flow
  - Character_Import_or_Create_Protocol
  - Character_Import_Flow
  - Character_Creation_Flow
  - Resume_Session_Protocol

### Part 3: Game Loop & Exploration
- **Section 6**: Game Loop & Exploration
  - Game_Loop (with checkpoint)
  - Exploration_Protocol
  - Movement_Protocol
  - Investigation_Protocol
  - NPC_Interaction_Protocol
  - Shopping_Protocol
  - Rest_Protocol
  - Short_Rest_Protocol
  - Long_Rest_Protocol

### Part 4: Combat
- **Section 7**: Combat Protocols
  - Combat_Initiation_Protocol
  - Combat_Round_Protocol
  - Player_Combat_Turn_Protocol
  - Attack_Action_Protocol
  - Enemy_Combat_Turn_Protocol
  - Handle_Creature_Death
  - Death_Saves_Protocol
  - Combat_End_Protocol

### Part 5: Progression & Quests
- **Section 8**: XP & Leveling
  - XP_Award_Protocol
  - Level_Check_Protocol
  - Level_Up_Protocol
  - ASI_or_Feat_Protocol
- **Section 9**: Quest & Loot
  - Quest_Accept_Protocol
  - Quest_Completion_Protocol
  - Loot_Distribution_Protocol
  - Handle_Quest_Chain_Trigger
  - Track_Reputation_Change

### Part 6: Closing
- **Section 10**: Session End & Persistence
  - Session_End_Protocol
  - Save_State_Protocol
- **Section 11**: Error Handling
- **Section 12**: Execution Rules Summary

## Example Workflows

### Example 1: Add New Exploration Action
```
1. Upload Part 3 (GameLoop) to Claude
2. "Add a 'Trade_Protocol' to the Exploration_Protocol switch case"
3. Claude modifies Part 3 only
4. Download updated Part 3
5. Run assemble_orchestrator.py
```

### Example 2: Modify Combat Mechanics
```
1. Upload Part 4 (Combat)
2. "Add critical hit rules to Attack_Action_Protocol"
3. Claude modifies Part 4 only
4. Download updated Part 4
5. Run assemble_orchestrator.py
```

### Example 3: Update Character Schema
```
1. Upload Part 1 (Foundation)
2. "Add 'exhaustion_level' field to Character_Schema_v2"
3. Claude modifies Part 1 only
4. May also need to update Part 3 (Long_Rest_Protocol)
5. Run assemble_orchestrator.py
```

## Assembly Details

The assembly script:
1. Checks all 6 parts exist
2. Concatenates them in order
3. Adds `---` separators between parts
4. Verifies final size (~43KB)
5. Reports any size warnings

## Troubleshooting

**Problem**: Assembly script reports missing file
- **Solution**: Ensure all 6 parts are in the same directory

**Problem**: Final file is much smaller than 43KB
- **Solution**: Check if any parts are empty or truncated

**Problem**: Final file is much larger than 43KB
- **Solution**: Check for duplicate content or incorrect concatenation

**Problem**: Protocols seem to be missing
- **Solution**: Use `grep "^## PROTOCOL:" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md | wc -l` to count protocols

**Problem**: Version not incrementing correctly
- **Solution**: Check `version.json` for correct last_change_date and current_version values

## Version History

- **v4.0**: Initial modular breakdown (6 parts)
  - Created from CORE_DND5E_AGENT_ORCHESTRATOR_v4.md (44KB)
  - Organized by modification frequency
  - Added assembly automation
  - Implemented dynamic versioning system with version.json tracking
