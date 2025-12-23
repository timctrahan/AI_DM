# D&D 5E Orchestrator LEAN Version

## Purpose

This is the LEAN version of the D&D 5E Orchestrator with all context management overhead removed. This version is optimized for LLMs with strong system instruction persistence (like Gemini) that don't require aggressive context refresh mechanisms.

## What Was Removed

### Total Reduction
- **~386 lines removed** (~5.8KB)
- **13% smaller than main version**
- Expected size: ~37-42KB (vs ~93KB main version)

### Removed Features

1. **Ambient_Context_Weaving META-PROTOCOL** (140 lines)
   - Removed from: Part 1, lines 86-226
   - Purpose: Continuous context re-surfacing before every output
   - Impact: No automatic weaving of HP/spells/NPCs into narration

2. **Rest_Refresh_Protocol** (95 lines)
   - Removed from: Part 1, lines 473-567
   - Purpose: Rotation display of NPCs/quests/items/locations during rests
   - Impact: Rests are simpler, no context summaries

3. **Hub_Entry_Protocol** (55 lines)
   - Removed from: Part 1, lines 417-471
   - Purpose: Display NPCs/quests/shops when entering towns
   - Impact: Town entry is minimal description only

4. **Context_Confidence_Check** (40 lines)
   - Removed from: Part 1, lines 571-611
   - Purpose: Prevent hallucination by requesting data repasting
   - Impact: AI can freely narrate NPCs/locations without safety check

5. **Ability Review in Rest Protocols** (50 lines total)
   - Removed from: Part 3, Short_Rest (lines 503-521) and Long_Rest (lines 583-607)
   - Purpose: Rotating ability/spell practice narration
   - Impact: Rests don't include ability review flavor text

6. **refresh_state Schema Fields** (1 line + 5 lines in save output)
   - Removed from: Part 1, line 299 and Part 6, lines 209-213
   - Purpose: Track rotation state for context management
   - Impact: Save files are slightly smaller

7. **Execution Loop Integration** (1 line)
   - Removed from: Part 1, line 234
   - Purpose: Explicit step in main loop
   - Impact: Simplified conceptual model

## Building the LEAN Version

```bash
cd agent_parts_lean
python assemble_orchestrator_lean.py
```

This will create `CORE_DND5E_AGENT_ORCHESTRATOR_LEAN_v1.0.0.md` in the `agent_parts_lean/` folder.

**The main orchestrator in the parent directory remains unchanged.**

## Differences from Main Version

| Feature | Main Version | LEAN Version |
|---------|--------------|--------------|
| Context weaving | Every output | None |
| Rest context refresh | Automatic | None |
| Hub entry summaries | Automatic | None |
| Confidence checks | Before NPC/location narration | None |
| Ability review at rest | Automatic rotation | None |
| File size | ~93KB | ~37-42KB (est.) |
| Context management | Aggressive | Minimal |
| Best for | Claude, GPT-4, models with context decay | Gemini, models with strong system instruction persistence |

## When to Use LEAN vs Main

### Use LEAN When:
- ✅ Using Gemini or LLMs with strong system instruction persistence
- ✅ Want minimal narration overhead
- ✅ Don't need automatic context refresh
- ✅ Prefer cleaner, simpler DM responses

### Use Main When:
- ✅ Using Claude or GPT-4 (context decay)
- ✅ Need automatic context weaving
- ✅ Running very long sessions (100+ exchanges)
- ✅ Want aggressive context retention

## Architecture Notes

The LEAN version removes the entire context management layer but preserves:
- ✅ All core game mechanics (combat, XP, gold, HP)
- ✅ Checkpoint validation (every 5 inputs)
- ✅ Player agency enforcement
- ✅ Save/load functionality
- ✅ All game protocols (exploration, combat, shopping, etc.)

Only the **automatic context re-surfacing mechanisms** are removed. The AI can still naturally include context in narration - it just won't be systematically forced to do so.

## Version Control

The LEAN version has its own independent versioning:
- Main version: `v6.7.4` (with context management)
- LEAN version: `v1.0.0` (without context management)

Changes to LEAN parts increment LEAN version only. Changes to main parts increment main version only.

## Modification Guide

1. **To modify LEAN version:**
   - Edit files in `agent_parts_lean/`
   - Run `python assemble_orchestrator_lean.py`
   - Output goes to `agent_parts_lean/` folder

2. **To modify main version:**
   - Edit files in `agent_parts/`
   - Run `python assemble_orchestrator.py`
   - Output goes to parent directory

3. **To sync changes between versions:**
   - Manually copy relevant protocol changes
   - Be careful not to re-add removed context management features to LEAN

## File Structure

```
AI_DM/
├── agent_parts/                          # Main version (with context management)
│   ├── DND_ORCH_PART1_Foundation.md
│   ├── ... (5 more parts)
│   ├── assemble_orchestrator.py
│   └── version.json
│
├── agent_parts_lean/                     # LEAN version (without context management)
│   ├── DND_ORCH_PART1_Foundation.md      # Modified (removed 4 protocols)
│   ├── DND_ORCH_PART2_SessionMgmt.md     # Unmodified
│   ├── DND_ORCH_PART3_GameLoop.md        # Modified (removed ability reviews + calls)
│   ├── DND_ORCH_PART4_Combat.md          # Unmodified
│   ├── DND_ORCH_PART5_Progression.md     # Unmodified
│   ├── DND_ORCH_PART6_Closing.md         # Modified (removed refresh_state output)
│   ├── assemble_orchestrator_lean.py
│   ├── version.json
│   ├── LEAN_VERSION_README.md            # This file
│   └── .previous_versions_lean/          # Backups
│
└── CORE_DND5E_AGENT_ORCHESTRATOR_v6.7.4.md  # Main assembled (parent directory)
```

## Status

**Current Status:** 🟡 IN PROGRESS

- ✅ Folder structure created
- ✅ Build script created
- ✅ Part files copied
- ✅ Ambient_Context_Weaving removed from Part 1
- ⏳ Still need to remove: Rest_Refresh, Hub_Entry, Context_Confidence_Check, refresh_state schema, ability reviews, protocol calls
- ⏳ Still need to: Test build and verify size reduction

## Next Steps

1. Complete removal of remaining context management features
2. Update execution loop (remove [AMBIENT CONTEXT WEAVING] step)
3. Test build with `python assemble_orchestrator_lean.py`
4. Verify final size is ~37-42KB
5. Test with Gemini to confirm context persistence works without management layer
