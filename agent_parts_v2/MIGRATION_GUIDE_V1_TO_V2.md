# Migration Guide: V1 → V2

**Purpose**: Guide for transitioning existing D&D campaigns from Orchestrator V1 to V2

**Target Audience**: Users currently running campaigns with V1 who want V2's improved reliability

---

## Should You Migrate?

### Migrate if you're experiencing:
- ✓ Context drift (NPCs becoming generic, quests getting vague)
- ✓ Protocol violations (AI skipping STOP, forgetting XP/gold tracking)
- ✓ Long sessions (>2 hours) where quality degrades
- ✓ Need to frequently re-paste campaign data

### Stay on V1 if:
- ✗ Your campaigns are very short (<1 hour sessions)
- ✗ You're in the middle of a critical session (finish first, then migrate)
- ✗ Your campaign has custom modifications to core protocols (needs manual porting)

---

## Migration Paths

### Path A: Fresh Start (Easiest, Recommended)

**Best for**: New acts, new campaigns, or willing to restart current act

**Steps**:
1. Export current party state from V1 (if continuing characters)
2. Assemble V2 Protocol Library
3. Create V2 Campaign Data Vault for your campaign
4. Initialize V2 session with existing party or new party

**Pros**:
- Clean slate, no compatibility issues
- Full benefit of V2 architecture immediately
- Clear testing (can compare V1 vs V2 behavior)

**Cons**:
- Lose current session progress (but keep characters)

---

### Path B: Session Resume (Moderate Difficulty)

**Best for**: Mid-campaign, want to preserve exact current state

**Steps**:
1. Save V1 session state (party JSON)
2. Assemble V2 Protocol Library
3. Create V2 Campaign Data Vault
4. Use V2's `proto_session_resume` to load V1 state

**Pros**:
- Continue exactly where you left off
- Preserve all party state (HP, XP, gold, quest progress)

**Cons**:
- Requires careful state validation
- V1 flags may not map perfectly to V2 (some manual fixes needed)

---

### Path C: Hybrid (Advanced)

**Best for**: Testing V2 while keeping V1 as backup

**Steps**:
1. Duplicate your entire V1 session (save state, campaign files)
2. Run V2 in parallel with same party state
3. Compare outputs, choose which to continue

**Pros**:
- Safe testing, V1 as fallback
- Can identify V2 issues early

**Cons**:
- Requires managing two sessions simultaneously
- More complex setup

---

## Step-by-Step: Path A (Fresh Start)

### Step 1: Export V1 Party (If Continuing Characters)

At the end of your last V1 session:

**User**: "End session and save party state"

**V1 AI**: Outputs party JSON:
```json
{
  "characters": [
    {
      "name": "Thorin",
      "level": 5,
      "class": "Fighter",
      "current_hp": 45,
      "max_hp": 52,
      ...
    }
  ],
  ...
}
```

**Action**: Copy and save this JSON to a file (e.g., `party_from_v1.json`)

### Step 2: Assemble V2 Protocol Library

```bash
cd agent_parts_v2/TOOLS
python assemble_protocol_library.py

# Output: ../../PROTOCOL_LIBRARY_v2.0.0.md
```

Verify:
```bash
# Should show ~40 protocols
grep -c "\[PROTOCOL_START:" ../../PROTOCOL_LIBRARY_v2.0.0.md
```

### Step 3: Create V2 Campaign Data Vault

**If you have a V1 campaign markdown file**:
```bash
python create_campaign_vault.py "../../campaigns/Your_Campaign/Act_2.md"

# Output: Act_2_Data_Vault.md
```

**If you need to create a vault from scratch**:
1. Copy `EXAMPLE_Campaign_Data_Vault.md` as a template
2. Replace example content with your campaign's NPCs, locations, quests
3. Ensure all modules have `[MODULE_START: id]` and `[MODULE_END: id]` tags
4. Update `[MASTER_INDEX]` to list all module IDs

### Step 4: Initialize V2 Session

**User Message to AI**:
```
Initialize a new D&D session with V2 Orchestrator.

[Paste entire KERNEL/IMMUTABLE_KERNEL.md content here]

---

[Paste entire PROTOCOL_LIBRARY_v2.0.0.md content here]

---

[Paste entire Act_2_Data_Vault.md content here]

---

Import existing party from V1:

[Paste party JSON from Step 1 here]
```

**Expected AI Response**:
```
✓ Kernel loaded (from system prompt)
✓ Protocol Library indexed (40 protocols found)
✓ Campaign Data Vault indexed (Act 2: The Dead City - 45 modules found)
✓ Party imported (4 characters)

Party Summary:
- Thorin: Human Fighter (Level 5) - HP: 45/52
- ...

⚠️ CORE RULES REMINDER:
- I ALWAYS present options and ⛔ STOP
- I NEVER act without your input
- I retrieve fresh data for all indexed entities
- Checkpoint validates every 5 turns

Ready to continue? (Current location: Main Street)
```

**Done!** You're now running V2 with your existing party.

---

## Step-by-Step: Path B (Session Resume)

### Step 1: Save Complete V1 State

**User**: "Save complete session state for migration to V2"

**V1 AI**: Outputs:
- Party state JSON (characters, location, flags, quests)
- Current narrative context (where you were, what was happening)
- Active effects, ongoing combats, etc.

**Action**: Save all output to `v1_session_state.txt`

### Step 2: Prepare V2 Components

Same as Path A Steps 2-3:
1. Assemble Protocol Library
2. Create Campaign Data Vault

### Step 3: Map V1 Flags to V2 Format

V1 and V2 may use different flag names. Review your V1 state and update flag names if needed.

**Example V1 flags**:
```json
"flags": {
  "met_zilvra": true,
  "velryn_status": "with_party"
}
```

**Corresponding V2 flags** (from vault):
```json
"flags": {
  "zilvra_met": true,
  "velryn_with_party": true
}
```

**Action**: Manually edit the party JSON to use V2 flag naming conventions (check your vault's flag definitions).

### Step 4: Initialize V2 with Resume Protocol

**User Message to AI**:
```
Initialize D&D session with V2 Orchestrator and resume from V1 save.

[Paste KERNEL/IMMUTABLE_KERNEL.md]

---

[Paste PROTOCOL_LIBRARY_v2.0.0.md]

---

[Paste Campaign_Data_Vault.md]

---

Resume session with this party state:

[Paste edited party JSON with V2 flag names]

Last known situation: [Brief summary of where you were in V1]
```

**Expected AI Response**:
```
✓ Kernel loaded
✓ Protocol Library indexed (40 protocols found)
✓ Campaign Data Vault indexed (45 modules found)
✓ Party state loaded and validated

⚠️ SESSION RESUMING - Verifying state integrity...

Current Party Status:
- Thorin: 45/52 HP | Fighter Level 5
  Location: Main Street
  ...

⚠️ CORE RULES REMINDER:
- I ALWAYS present options and ⛔ STOP
- ...

Ready to continue? Any corrections needed?
```

**User**: "Yes, continue"

**AI**: Retrieves current location module and resumes exploration from where you left off.

---

## Common Migration Issues

### Issue 1: "Module not found" errors

**Symptom**: AI outputs `⛔ CRITICAL ERROR: Module 'npc_xyz' not found`

**Cause**: V2 protocols reference NPCs/locations that aren't in your vault

**Fix**:
1. Identify missing module ID from error message
2. Add module to vault:
   ```markdown
   [MODULE_START: npc_xyz]
   ### NPC: XYZ
   ... (content)
   [MODULE_END: npc_xyz]
   ```
3. Update `[MASTER_INDEX]` to include new module
4. Reload vault (paste updated vault to AI)

### Issue 2: V1 party state validation fails

**Symptom**: AI reports "State validation found issues: negative HP, invalid spell slots"

**Cause**: V1 may have allowed invalid states that V2 catches

**Fix**:
1. Review validation errors
2. Manually correct party JSON:
   - Clamp HP to 0-max_hp range
   - Fix spell slots to valid counts
   - Remove unknown conditions
3. Re-submit corrected JSON

### Issue 3: Quest progress lost

**Symptom**: AI doesn't remember quest objectives or progress

**Cause**: V1 stored quest state differently than V2 expects

**Fix**:
1. Check V1 party JSON for `active_quests` field
2. Map to V2 format:
   ```json
   "active_quests": [
     {
       "quest_id": "quest_mq2_three_fragments",
       "status": "in_progress",
       "objectives_completed": ["soulforge_shard_obtained"],
       "flags": {"thalgrim_pacified": true}
     }
   ]
   ```
3. Ensure quest_id matches module ID in vault

### Issue 4: Custom V1 protocols not working

**Symptom**: A mechanic you added to V1 doesn't exist in V2

**Cause**: V2 is a new protocol set, doesn't include custom V1 modifications

**Fix**:
1. Identify the custom protocol from V1
2. Port it to V2 format:
   - Add to appropriate PROTOCOL_LIBRARY part file
   - Wrap with `[PROTOCOL_START/END]` tags
   - Add to index
3. Reassemble Protocol Library
4. Reload session with updated library

---

## Verification Checklist

After migration, verify V2 is working correctly:

### ✓ Kernel Verification
- [ ] AI acknowledges "Kernel loaded" on init
- [ ] AI presents options and ⛔ STOP every turn
- [ ] AI shows core rules reminder on session start

### ✓ Protocol Library Verification
- [ ] Count protocols: `grep -c "\[PROTOCOL_START:" PROTOCOL_LIBRARY_v2.0.0.md`
- [ ] Should be ~40 protocols
- [ ] AI successfully calls exploration, combat, etc. protocols

### ✓ Campaign Vault Verification
- [ ] AI acknowledges vault loaded with correct module count
- [ ] Test NPC retrieval: "I want to talk to [NPC name]"
- [ ] AI outputs rich, detailed NPC dialogue (not generic)
- [ ] AI maintains personality across multiple interactions

### ✓ Checkpoint Verification
- [ ] Play for 5 turns
- [ ] Checkpoint should trigger automatically (silent if no issues)
- [ ] Deliberately skip a STOP to test: AI should catch and correct

### ✓ State Integrity Verification
- [ ] All character HP values valid
- [ ] All gold/XP tracked correctly
- [ ] Quest progress reflects actual state
- [ ] Location matches current narrative

---

## Rollback Plan (If Migration Fails)

If V2 has critical issues and you need to revert to V1:

### Emergency Rollback Steps

1. **Locate V1 Files**:
   - `agent_parts/` directory (V1 protocol parts)
   - V1 campaign markdown files
   - Last V1 party state JSON

2. **Reassemble V1 Orchestrator**:
   ```bash
   cd agent_parts
   python assemble_orchestrator.py
   # Output: CORE_DND5E_AGENT_ORCHESTRATOR_v6.8.0.md
   ```

3. **Resume V1 Session**:
   ```
   [Paste V1 orchestrator]

   Resume session:
   [Paste last V1 party state]
   ```

4. **Report Issue**:
   - Document what failed in V2
   - Save error messages
   - Create issue for investigation

---

## Side-by-Side Comparison

### V1 Session Initialization
```
[Paste 44 KB orchestrator file]

[User manually pastes campaign module when needed]

"Start a new session"
```

### V2 Session Initialization
```
[Kernel in system prompt - 1 KB]

[Paste 40 KB Protocol Library - once]

[Paste 30 KB Campaign Vault - once]

"Initialize session"
```

**Key Difference**: V2 front-loads all data once, then retrieves silently. V1 requires re-pasting data when AI forgets.

---

## Performance Expectations

### V1 Performance Over Time
- **Turns 1-20**: Excellent (fresh context)
- **Turns 21-50**: Good (some vagueness)
- **Turns 51-100**: Degraded (needs manual re-prompting)
- **Turns 100+**: Poor (frequent context loss)

### V2 Performance Over Time
- **Turns 1-20**: Excellent (fresh retrieval)
- **Turns 21-50**: Excellent (fresh retrieval)
- **Turns 51-100**: Excellent (fresh retrieval)
- **Turns 100+**: Excellent (until conversation history fills context window)

**V2 Limit**: Context window size (~200K tokens = ~800 turns), not memory decay

---

## FAQ

**Q: Can I use V1 and V2 simultaneously for different campaigns?**
A: Yes! They're completely independent. Just keep files organized in separate directories.

**Q: Will my V1 character sheets work in V2?**
A: Yes, V2 uses the same Character_Schema_v2 format.

**Q: Do I need to convert my entire campaign at once?**
A: No, you can convert act-by-act. Create a vault for Act 2, run that, then create Act 3 vault later.

**Q: What if my campaign doesn't fit the vault structure?**
A: The vault is very flexible. You can add custom module types (e.g., `puzzle_`, `faction_`, `timeline_`). Just index them in [MASTER_INDEX].

**Q: Is V2 slower due to retrieval?**
A: No, retrieval from conversation history is <100ms. With working memory cache, it's often instant.

**Q: Can I edit the vault mid-session?**
A: Not currently (V2.0). You'd need to reload the session with updated vault. V2.1 will support dynamic updates.

**Q: What happens if I use a V1 campaign file with V2?**
A: It won't work automatically. You must convert to vault format using `create_campaign_vault.py` first.

---

## Success Stories

### Example: "Descent into Khar-Morkai" Migration

**Original Issue**: V1 session at turn 75, Zilvra becoming generic, quest objectives vague

**Migration**:
1. Exported party (5 characters, level 5)
2. Created Act 2 vault (45 modules)
3. Resumed in V2 at Main Street

**Result**:
- Zilvra's personality restored immediately
- Quest tracking perfect ("You need: Warden's Sigil, Mourner's Tear")
- Ran to turn 200 with zero degradation
- Player feedback: "Feels like the AI is actually reading the campaign notes now"

---

## Next Steps

After successful migration:

1. **Play 5-10 turns** to verify everything works
2. **Test checkpoint** by playing through 5 turns and verifying validation runs
3. **Stress test** NPCs by interacting with same NPC multiple times across many turns
4. **Save often** using V2's session end protocol
5. **Provide feedback** if you find issues or improvements

---

## Support

**Issues?** Check:
1. This migration guide
2. `README.md` for V2 architecture overview
3. `V2_ARCHITECTURE_DESIGN.md` for technical details

**Still stuck?** Create an issue with:
- Migration path used (A/B/C)
- Error messages (exact text)
- V1 version you're migrating from
- Step where migration failed

---

**Good luck with your migration! V2 is designed to be worth the one-time setup effort.**

**Version**: 1.0.0
**Last Updated**: 2025-12-19
