# DND Orchestrator UpdateProtocol v1.2.0
**Generic orchestrator governing ALL updates to D&D 5E orchestrator files**

**Purpose**: Prevent data loss, bloat, and drift when modifying D&D orchestrator files

**Load when**: ANY modification to D&D orchestrator files

---

## CATASTROPHIC ERRORS TO PREVENT

### Error 1: Using create_file Instead of str_replace
**Symptom**: New file created, original content lost
**Prevention**: NEVER use create_file for existing orchestrators

### Error 2: Adding Human-Readable Explanations
**Symptom**: File grows unnecessarily (AI doesn't need verbose explanations)
**Prevention**: Instructions only, no "why it works" text

### Error 3: Dropping Content
**Symptom**: Protocols disappear, file shrinks unexpectedly
**Prevention**: Measure before/after EVERY change

### Error 4: Over-Specification
**Symptom**: File grows with unnecessary detail
**Prevention**: High-level logic, not implementation detail

---

## MODULAR ORCHESTRATOR ARCHITECTURE

### 6-Part Structure

Orchestrator split into parts in `agent_parts/`:

| Part | File | Size | Content |
|------|------|------|---------|
| 1 | DND_ORCH_PART1_Foundation.md | ~8KB | Schemas, constraints, meta-protocols, reference tables |
| 2 | DND_ORCH_PART2_SessionMgmt.md | ~6KB | Character creation, session init, import/resume |
| 3 | DND_ORCH_PART3_GameLoop.md | ~10KB | Exploration, NPCs, shopping, resting |
| 4 | DND_ORCH_PART4_Combat.md | ~7KB | Combat rounds, attacks, death saves |
| 5 | DND_ORCH_PART5_Progression.md | ~9KB | XP, leveling, ASI, quests, loot |
| 6 | DND_ORCH_PART6_Closing.md | ~4KB | Session end, save state, error handling |

**Assembled output**: `CORE_DND5E_AGENT_ORCHESTRATOR_vX.Y.Z.md` (~45KB)

### Assembly Process

**CRITICAL**: After editing ANY part, MUST run assembly:

```bash
cd agent_parts
python assemble_orchestrator.py
```

**Automatic versioning** (via `version.json`):
- 0-1 files changed → patch (v5.0.0 → v5.0.1)
- 2-4 files changed → minor (v5.0.0 → v5.1.0)
- 5-6 files changed → major (v5.0.0 → v6.0.0)

### Which Part to Edit

| Change Type | Edit Part | Examples |
|-------------|-----------|----------|
| Schemas (Character, Party, Campaign) | Part 1 | Add field, modify structure |
| Reference tables (XP, proficiency) | Part 1 | Update thresholds, add entries |
| Session initialization | Part 2 | Character creation, import |
| Exploration, NPCs, shopping, resting | Part 3 | New actions, shop prices, rest rules |
| Combat mechanics | Part 4 | Attack rolls, damage, initiative |
| XP, leveling, ASI, quests | Part 5 | Progression rules, loot tables |
| Save/load, error handling | Part 6 | State preservation, recovery |

**Multi-part changes**: If schema change in Part 1, check all other parts for references.

---

## MANDATORY WORKFLOW FOR ALL UPDATES

### Step 1: Baseline Metrics (ALWAYS)

```bash
# Identify which part to edit (PART1-6)
# Measure PART file
wc -c DND_ORCH_PARTX_*.md  # Part size
wc -l DND_ORCH_PARTX_*.md  # Part lines
grep -c "^### PROTOCOL:" DND_ORCH_PARTX_*.md  # Protocols in this part

# Measure current ASSEMBLED output
wc -c ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Assembled size
grep -c "^### PROTOCOL:" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Total protocols

# Record:
# Part X starting size: _____ bytes
# Part X starting lines: _____
# Part X protocols: _____
# Assembled starting size: _____ bytes
# Assembled total protocols: _____
```

### Step 2: Define Scope (ALWAYS)

**User specifies**:
- What to add/remove/modify
- Which protocols affected
- Target size (ONLY if user explicitly provides one)

**You document**:
- Current size: ___ KB (baseline for change detection)
- Expected change type: addition/removal/modification
- Protocols affected: [list]
- Functional goal: [what this achieves]

### Step 3: Use str_replace ONLY (ALWAYS)

```python
# ✅ CORRECT - Surgical modification
str_replace(
    path="/path/to/existing_file.md",
    old_str="[exact existing text]",
    new_str="[modified text]",
    description="[what changed]"
)

# ❌ WRONG - Creates new file, loses content
create_file(path="/path/to/file.md", ...)
```

**RULE**: If file exists, use str_replace. Period.

### Step 4: Measure After EVERY Change (ALWAYS)

```bash
# After each str_replace to PART file
wc -c DND_ORCH_PARTX_*.md

# Calculate part delta
echo "Part X was: [old]KB, now: [new]KB, delta: [diff]KB"

# Verify part protocols intact
grep -c "^### PROTOCOL:" DND_ORCH_PARTX_*.md
# Must match baseline (unless explicitly removing protocol)
```

### Step 5: Assemble and Verify (ALWAYS)

```bash
# After ALL part edits complete, run assembly
cd agent_parts
python assemble_orchestrator.py

# Output shows:
# - Files changed count
# - Version increment (patch/minor/major)
# - New version number
# - Output filename

# Measure ASSEMBLED output
wc -c ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # New assembled size
wc -l ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # New assembled lines
grep -c "^### PROTOCOL:" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Total protocols

# Verify version increment
cat version.json | grep current_version
# Matches expected increment based on files changed?

# Calculate assembled delta
echo "Assembled was: [old]KB, now: [new]KB, delta: [diff]KB"

# Verify critical content in ASSEMBLED output
grep -c "CHECKPOINT" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Must be 1+
grep -c "Correction_Protocol" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Must exist
grep -c "^### PROTOCOL:" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # Must match expected
```

---

## RULES FOR SPECIFIC MODIFICATION TYPES

### Type A: Adding Content

**Examples**: Adding Section 0, adding guards, adding sentinels

**Rules**:
1. Calculate size budget FIRST
2. Create component in /tmp/ first, measure it
3. Add via str_replace
4. Verify size increase = expected

**Format rules**:
- Compact guards: `GUARD: x AND y` NOT `GUARD_CONDITIONS:\n  - x: true\n  - y: true`
- Compact stops: `⛔ WAIT: input` NOT `⛔ FULL STOP - WAIT_FOR: input`
- Compact sentinels: `⚠️ SENTINEL: [brief]` NOT verbose explanations
- NO human explanations: Instructions only

**Efficiency principle**: Use compact formats when they achieve the same functional outcome, but NEVER sacrifice clarity or functionality to hit arbitrary size targets

### Type B: Removing Content

**Examples**: Trimming bloat, removing deprecated sections

**Rules**:
1. Identify EXACTLY what to remove
2. Calculate expected size reduction
3. Remove via str_replace (old_str → new_str="")
4. Verify size decrease = expected
5. Verify no collateral damage

**Safe to remove**:
- Verbose explanations ("Why it works", "Purpose")
- Tautological validations (EXIT_CONDITIONS, VALIDATION_REQUIREMENTS)
- Redundant sentinels (keep ONE per critical protocol)
- Duplicate format specifications
- Human-readable commentary

**NEVER remove**:
- Protocol procedures
- Section 0 (if v4+)
- Meta-protocols (if v4+)
- Checkpoint system (if v4+)
- Required format specifications (gold, XP)

### Type C: Modifying Protocols

**Examples**: Changing protocol logic, reordering sections

**Rules**:
1. View ENTIRE protocol first
2. Copy exact old_str
3. Modify carefully
4. Verify protocol still complete
5. Verify size delta reasonable

**Do NOT**:
- Expand beyond necessary
- Add implementation detail (keep high-level)
- Add human explanations
- Remove critical steps

---

## CHANGE DETECTION (NOT SIZE ENFORCEMENT)

**CRITICAL PRINCIPLE**: Files must be as large as they need to be for functionality. Measurement is for detecting unexpected changes (data loss, accidental bloat), NOT for enforcing arbitrary size targets.

### Purpose of Measurement

**Measure to detect**:
- ✅ Data loss (file shrunk unexpectedly)
- ✅ Content duplication (file grew unexpectedly)
- ✅ Protocol deletion (count dropped unexpectedly)
- ✅ Accidental bloat (verbose formatting crept in)

**DO NOT measure to**:
- ❌ Enforce arbitrary "max recommended" sizes
- ❌ Hit predetermined size targets
- ❌ Reduce size for the sake of reduction
- ❌ Compromise functionality for smaller files

### When Adding Content

**Track functional changes**:
```
Part 3 baseline: 10.2KB, 15 protocols
Added provisions protocol: +2.1KB, 16 protocols ✓
Added foraging protocol: +1.4KB, 17 protocols ✓
Part 3 new size: 13.7KB, 17 protocols ✓

Functional goal achieved: Players can now forage and manage provisions
Size increase justified: Two complete new protocols with full procedures
```

**Alert if**:
- File size changed but protocol count didn't (unexpected)
- Added 1 protocol but file grew by 10KB (possible duplication)
- File size didn't change but protocol count increased (content lost)

### When Removing Content

**Track what was removed and why**:
```
Current: 59KB, 44 protocols
Goal: Remove verbose human explanations, NOT protocols
Removed explanatory text: -1.2KB, 44 protocols ✓
Compacted verbose guards: -1.6KB, 44 protocols ✓
Final: 56.2KB, 44 protocols ✓

Functional goal: Same functionality, less bloat
All protocols preserved: Yes ✓
```

**Alert if**:
- Protocol count dropped unexpectedly
- Removed >50% more content than expected (possible collateral damage)
- Critical content disappeared (checkpoints, sentinels, procedures)

---

## VERIFICATION CHECKLIST

**After EVERY str_replace to PART file**:
```bash
# Part size check
wc -c DND_ORCH_PARTX_*.md
# Is delta expected? If not, investigate immediately

# Part protocol count
grep -c "^### PROTOCOL:" DND_ORCH_PARTX_*.md
# Did count change? Should it have?
```

**After COMPLETING part modifications and ASSEMBLY**:
```bash
# Part final size
wc -c DND_ORCH_PARTX_*.md
# Changed as expected based on modifications?

# Assembled final size
wc -c ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md
# Changed as expected? (No arbitrary target - just detect unexpected changes)

# Assembled line count
wc -l ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md
# Reasonable change from baseline?

# All protocols present in assembled
grep "^### PROTOCOL:" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md | wc -l
# Matches expected? (Should match baseline unless protocols added/removed intentionally)

# Version increment
cat version.json | grep current_version
# Correct increment based on files changed?

# Critical components in assembled
grep -c "CHECKPOINT" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # 1+
grep -c "Correction_Protocol" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # 1
grep -c "State_Recovery_Protocol" ../CORE_DND5E_AGENT_ORCHESTRATOR_v*.md  # 1
```

---

## CONTENT RULES

### What AI Needs (KEEP)

**Instructions**: What to do, when to do it
**Logic**: IF/THEN, SWITCH, FOR EACH
**Enforcement**: Guards, stops, sentinels, checkpoints
**Formats**: Required output formats (gold, XP, HP)
**Procedures**: Step-by-step protocol execution

### What AI Doesn't Need (CUT)

**Explanations**: "Why it works", "Purpose", "This is because"
**Verbose formatting**: Multi-line when single-line works
**Tautologies**: "protocol_complete: true" when protocol completes
**Redundancy**: Multiple sentinels saying same thing
**Human commentary**: Notes for humans analyzing the orchestrator

### Format Efficiency

**Compact vs Verbose**:

```yaml
# ❌ VERBOSE (3 lines, 80 bytes)
GUARD_CONDITIONS:
  - state_valid: true
  - prerequisites_met: true

# ✅ COMPACT (1 line, 35 bytes)
GUARD: state_valid AND prerequisites_met

# ❌ VERBOSE (1 line, 40 bytes)
⛔ FULL STOP - WAIT_FOR: player_choice

# ✅ COMPACT (1 line, 20 bytes)
⛔ WAIT: player_choice

# ❌ VERBOSE (1 line, 80 bytes)
⚠️ SENTINEL: Never auto-assign ability scores or make class feature choices

# ✅ COMPACT (1 line, 35 bytes)
⚠️ SENTINEL: No auto-assignment
```

**Rule**: If compact version has same effect, use compact version.

---

## CRITICAL DONT'S

### NEVER

❌ Use create_file for existing orchestrators  
❌ Add verbose explanations for humans  
❌ Add implementation detail to procedures  
❌ Use verbose formats when compact works  
❌ Add multiple sentinels per protocol  
❌ Keep tautological validations  
❌ Skip size verification after changes  
❌ Proceed if size delta unexpected  
❌ Assume str_replace worked without checking  
❌ Modify without reading section first

---

## EMERGENCY ABORT CONDITIONS

**STOP IMMEDIATELY if**:

1. **Size changed unexpectedly**
   - Added simple guard, file grew by 2KB → ABORT (possible duplication)
   - Removed one explanation, file shrunk by 5KB → ABORT (collateral damage)
   - Expected change direction doesn't match actual (added content but file shrunk)

2. **Protocol count changed unexpectedly**
   - Started with 40, now 35, didn't intend to remove → ABORT
   - Started with 40, now 40, but added new protocol → ABORT (content lost)

3. **Critical content disappeared**
   - Checkpoint missing → ABORT
   - Section 0 gone (if v4+) → ABORT
   - Protocols missing → ABORT
   - Sentinel markers gone → ABORT

4. **File changed dramatically without explanation**
   - Lost >20% of file size unexpectedly → ABORT
   - Line count dropped >30% unexpectedly → ABORT
   - File grew >50% unexpectedly → ABORT

**When aborting**:
1. Tell user: "I made an error: [description]"
2. Ask: "Do you have the previous version?"
3. Wait for user guidance
4. Do NOT try to fix without user input

---

## WORKFLOW SUMMARY

```
EVERY update MUST follow (MODULAR):

1. Identify which part to edit (PART1-6 via mapping table)
2. Record baseline (part size, assembled size, protocols) - for change detection
3. Define scope (what changing, functional goal, protocols affected)
4. Read section to modify in PART file
5. Use str_replace ONLY on PART file
6. Measure PART after change (wc -c) - detect unexpected changes
7. Verify change direction matches expectation (grew/shrunk as expected)
8. Verify protocols intact in PART (count should match unless intentionally changed)
9. Repeat steps 4-8 for each change to parts
10. Run assembly: python assemble_orchestrator.py
11. Measure ASSEMBLED output (size, lines, protocols) - detect unexpected changes
12. Verify version increment (version.json)
13. Verify assembled changed as expected (direction and rough magnitude)
14. Final verification (all checklists - functionality, not size targets)
15. Report results to user (functional goals achieved, protocols preserved)
```

**Remember**:
- Measure for change detection, NOT size targets
- Always assemble after part edits
- Verify version increment matches files changed
- Compact over verbose (when functionally equivalent)
- Instructions not explanations
- str_replace not create_file
- Abort if unexpected changes detected
- Functionality ALWAYS takes priority over file size

---

## VERSION HISTORY

**v1.2.0** (Current - CRITICAL CORRECTION)
- **REMOVED arbitrary size targets** - Files must be as large as needed for functionality
- Reframed "SIZE MANAGEMENT" → "CHANGE DETECTION" - measure for detecting unexpected changes, NOT enforcing targets
- Removed "Part Size Targets" table with arbitrary max sizes
- Removed "Abort if Part exceeds max recommended size" violations
- Updated "Step 2: Define Target" → "Define Scope" - functional goals, not size budgets
- Clarified measurement purpose: detect data loss/duplication, NOT hit size targets
- Added critical principle: **"Functionality ALWAYS takes priority over file size"**
- Updated verification checklists to focus on functional integrity, not arbitrary limits
- Efficiency principle: compact when functionally equivalent, NEVER sacrifice clarity for size

**v1.1.0** (DEPRECATED - contained harmful size targets)
- Added modular orchestrator architecture section
- Added 6-part structure documentation
- Added section mapping table (which part to edit)
- Updated workflow to include assembly step
- Added dual measurement (part + assembled)
- Added version.json tracking verification
- ❌ Added harmful arbitrary size targets (corrected in v1.2.0)
- Updated verification checklist for modular workflow

**v1.0.0**
- Initial release
- Catastrophic error prevention
- Mandatory workflow
- Size management (later corrected in v1.2.0)
- Content rules
- Emergency abort conditions

---

**DND Orchestrator UpdateProtocol v1.2.0: Preventing catastrophic modifications through measurement and discipline. Functionality over arbitrary size constraints.**
