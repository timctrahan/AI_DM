# SKELETAL Campaign Orchestrator - Modular Parts System

## Overview

The SKELETAL Campaign Orchestrator uses a **7-part modular architecture** split by **logical domain and modification frequency**. Parts are concatenated automatically by `assemble_orchestrator.py` with semantic versioning based on file change count.

## Quick Start

```bash
# From skeleton_orchestrator_parts/ directory
python assemble_orchestrator.py

# Output: ../SKELETAL_CAMPAIGN_ORCHESTRATOR_vX_Y_Z.md
# Backup: .previous_versions/vX_Y_Z.zip
```

## Part Structure

| Part | File | Size | Domain | Modification Frequency |
|------|------|------|--------|----------------------|
| **1** | `SKELETAL_PART1_Identity.md` | ~4 KB | **Core Identity & Constraints** | RARELY |
| **2** | `SKELETAL_PART2_OutputFormats.md` | ~5 KB | **Gate Format & Standards** | OCCASIONALLY |
| **3** | `SKELETAL_PART3_NewMode.md` | ~2 KB | **New Campaign Creation** | RARELY |
| **4** | `SKELETAL_PART4_RefineMode.md` | ~3 KB | **Modification & Legacy** | FREQUENTLY |
| **5** | `SKELETAL_PART5_InnovatePlaytest.md` | ~3 KB | **Advanced Features** | OCCASIONALLY |
| **6** | `SKELETAL_PART6_MechanicalSystems.md` | ~2 KB | **Progression & Quests** | OCCASIONALLY |
| **7** | `SKELETAL_PART7_Reference.md` | ~2 KB | **Templates & Validation** | RARELY |

**Total:** ~21 KB split across 7 parts
**Assembled:** ~25 KB (plus markdown separators)

## Logical Split Rationale

### Part 1: Identity (RARELY Modified)
**Contents:**
- TIER 1: IDENTITY & IMMEDIATE ACTION
- EXECUTE NOW, STARTUP SEQUENCE
- TIER 2: HARD CONSTRAINTS (FORBIDDEN, IP-CLEAN)
- TIER 3: OPERATING PRINCIPLES

**When to modify:** System-level philosophy changes, startup sequence adjustments, constraint updates

**Size expectations:** 3-5 KB

### Part 2: Output Formats (OCCASIONALLY Modified)
**Contents:**
- TIER 4: OUTPUT FORMAT
- STATE CHANGE FORMAT (gate structure)
- OUTPUT FORMATTING (line width, dividers)
- FILE OUTPUT (naming, process)
- CAMPAIGN OUTPUT STANDARDS (section order, anti-bloat rules)

**When to modify:** Gate template evolution, new output standards, format refinements

**Size expectations:** 4-6 KB

### Part 3: New Mode (RARELY Modified)
**Contents:**
- TIER 5: MODE WORKFLOWS → NEW MODE
- Workflow steps
- Example conversation flow

**When to modify:** Changes to new campaign creation process

**Size expectations:** 2-3 KB

### Part 4: Refine Mode (FREQUENTLY Modified)
**Contents:**
- TIER 5: MODE WORKFLOWS → REFINE MODE
- Workflow steps
- Example revision
- Legacy Handling (migration rules)
- Output Normalization (cleanup principles)

**When to modify:** Migration strategies update, new cleanup rules, normalization logic changes

**Size expectations:** 3-4 KB

**NOTE:** This is the "hot" part - expect frequent updates as legacy handling evolves.

### Part 5: Innovate & Playtest (OCCASIONALLY Modified)
**Contents:**
- TIER 5: MODE WORKFLOWS → INNOVATE MODE
- TIER 5: MODE WORKFLOWS → PLAYTEST MODE
- Party generation, targeted launch, commands

**When to modify:** New kernel capabilities, playtest feature additions

**Size expectations:** 3-4 KB

### Part 6: Mechanical Systems (OCCASIONALLY Modified)
**Contents:**
- MECHANICAL SYSTEMS
- Progression types (gate/XP/milestone)
- Quest discovery (linear/hub-based)
- Bulletin board templates
- Conversion processes

**When to modify:** New progression systems, quest paradigm updates

**Size expectations:** 2-3 KB

### Part 7: Reference (RARELY Modified)
**Contents:**
- TIER 6: REFERENCE & QA
- Templates (boss encounter, act phase)
- VALIDATION CHECKLIST
- STYLE

**When to modify:** New templates, validation criteria updates

**Size expectations:** 2-3 KB

## Semantic Versioning Rules

Version format: `vMAJOR_MINOR_PATCH`

| Changed Files | Version Bump | Example |
|---------------|-------------|---------|
| 0-1 files | **Patch** | v3_6_0 → v3_6_1 |
| 2-4 files | **Minor** | v3_6_0 → v3_7_0 |
| 5-7 files | **Major** | v3_6_0 → v4_0_0 |

**Rationale:**
- **Patch:** Small fixes to single domain
- **Minor:** Multi-domain updates (moderate scope)
- **Major:** Comprehensive overhaul affecting most/all parts

**NOTE:** Uses underscore format (v3_6_0) to match existing SKELETAL naming convention.

## Development Workflow

### 1. Modify Part Files

```bash
# Edit the part you need to change
code SKELETAL_PART4_RefineMode.md
```

**Best practice:** Only modify what's necessary in the specific part.

### 2. Assemble

```bash
python assemble_orchestrator.py
```

**Script actions:**
1. Counts changed files since last assembly (mtime comparison)
2. Calculates new version based on change count
3. Concatenates all 7 parts with `---` separators
4. Updates Part 1 header with new version number
5. Writes to `../SKELETAL_CAMPAIGN_ORCHESTRATOR_vX_Y_Z.md`
6. Creates ZIP backup in `.previous_versions/`
7. Updates `version.json` with new timestamp

### 3. Verify Output

```bash
# Check assembled file size
ls -lh ../SKELETAL_CAMPAIGN_ORCHESTRATOR_v*.md

# Expected: ~25 KB

# Verify all parts present (search for part boundaries)
grep -c "^---$" ../SKELETAL_CAMPAIGN_ORCHESTRATOR_v*.md
# Expected: 6 separators (between 7 parts)
```

### 4. Test with Claude

Load the assembled orchestrator and test behavior:

```
"I want to create a Legend of Drizzt campaign"
→ Should trigger NEW MODE workflow
→ Should use sequential questioning
→ Should enforce IP-clean output standards
```

## Version History

Stored in `.previous_versions/` as ZIP archives:

```
.previous_versions/
├── v3_6_1.zip    (Part 4 hotfix - new legacy handling)
├── v3_7_0.zip    (Parts 2, 4, 5 updated - format improvements)
├── v4_0_0.zip    (Major overhaul - all 7 parts)
```

Each ZIP contains all 7 part files from that version.

## Troubleshooting

### Assembly Fails: "Missing part"

**Problem:** One of the 7 part files doesn't exist.

**Solution:**
```bash
# Check which parts exist
ls SKELETAL_PART*.md

# If missing, extract from previous version
unzip .previous_versions/v3_6_0.zip
```

### Output File Too Small

**Problem:** Assembly output <20 KB (expected ~25 KB).

**Possible causes:**
- Part file corrupted or truncated
- Encoding issue (non-UTF-8)

**Solution:**
```bash
# Check each part size
ls -lh SKELETAL_PART*.md

# Re-extract from backup if needed
unzip .previous_versions/vX_Y_Z.zip
```

### Version Not Incrementing

**Problem:** Running assembly but version stays the same.

**Cause:** No parts modified since last assembly (all mtimes older than `last_change_date` in version.json).

**Solution:** This is correct behavior - version only increments when parts change.

### ZIP Backup Failed

**Problem:** Warning during assembly: "Backup creation failed".

**Impact:** Assembly succeeded, but no ZIP created.

**Solution:**
- Check `.previous_versions/` directory exists and is writable
- Check disk space
- Re-run assembly after fixing permissions

## Maintenance

### Adding a New Part

If you need to split further (e.g., Part 8):

1. **Create the new part file:** `SKELETAL_PART8_NewDomain.md`
2. **Update `version.json`:**
   ```json
   "part_files": [
     ...
     "SKELETAL_PART7_Reference.md",
     "SKELETAL_PART8_NewDomain.md"
   ],
   "versioning_rules": {
     "patch": "0-1 files changed",
     "minor": "2-5 files changed",
     "major": "6-8 files changed"
   }
   ```
3. **Update this README**
4. **Run assembly** to verify

### Removing a Part

If consolidating (e.g., merge Part 7 into Part 6):

1. **Merge content** from Part 7 into Part 6
2. **Delete** `SKELETAL_PART7_Reference.md`
3. **Update `version.json`** (remove from part_files list)
4. **Renumber** remaining parts if gaps created
5. **Run assembly** to verify

## Best Practices

### When Modifying Multiple Parts

**Scenario:** Need to update refine mode (Part 4) and mechanical systems (Part 6).

**Approach:**
1. Edit Part 4
2. Edit Part 6
3. Run `assemble_orchestrator.py` **once**
4. Script will detect 2 files changed → Minor version bump (v3_6_0 → v3_7_0)

**Don't:** Run assembly after each part edit (creates unnecessary versions).

### Size Management

**Target sizes per part:**
- Keep parts under 10 KB each
- Total assembled should be 20-30 KB
- If a part exceeds 10 KB, consider splitting

**Example:** If Part 4 (Refine Mode) grows to 8 KB:
- May be okay (still under 10 KB)
- If legacy handling grows significantly, split into Part 4a/4b

### Testing Changes

**Before committing:**
1. Run assembly
2. Load assembled file in Claude
3. Test affected workflows
4. Verify no regressions

**Example test scenarios:**
- Part 1 changes: Test startup sequence
- Part 2 changes: Verify gate format compliance
- Part 4 changes: Test legacy file migration
- Part 5 changes: Test playtest mode

## Integration with SKELETAL System

SKELETAL Campaign Orchestrator works with:

```
SKELETAL_DM_KERNEL → Campaign Orchestrator (you are here) → Campaign Files
```

**Interface points:**
- Part 1 enforces kernel compatibility check
- Part 2 defines format consumed by kernel
- Part 2 uses IP-clean tokens that kernel renders

**When updating:** Verify kernel compatibility is maintained.

## Comparison with LEASH

| Aspect | SKELETAL (7 parts) | LEASH (6 parts) |
|--------|-------------------|----------------|
| **Total size** | ~25 KB | ~35 KB |
| **Parts** | 7 | 6 |
| **Largest part** | Part 2: 5 KB | Part 3: 12 KB |
| **Unique feature** | Playtest Mode (Part 5) | Sequential Clarification (Part 2) |
| **Versioning** | 0-1/2-4/5-7 | 0-1/2-3/4-6 |
| **Focus** | D&D campaign creation | Software planning |

## Questions & Support

**Q: Can I change the versioning rules?**
A: Yes, edit `version.json` versioning_rules. Common alternative: 0-2/3-5/6-7.

**Q: Can I skip version increments?**
A: No - semantic versioning is automatic based on file changes. To force a specific version, manually edit `version.json` current_version.

**Q: Should I commit ZIP files to git?**
A: Optional. ZIPs provide rollback capability but increase repo size. Add `.previous_versions/` to `.gitignore` if preferred.

**Q: How do I rollback to a previous version?**
A:
```bash
# Extract previous version parts
unzip .previous_versions/v3_6_0.zip

# Re-run assembly
python assemble_orchestrator.py

# This creates v3_6_1 with content from v3_6_0
```

**Q: Why 7 parts instead of 6 like LEASH?**
A: SKELETAL has different domain boundaries. MODE WORKFLOWS split into 3 parts (New/Refine/Innovate+Playtest) due to distinct responsibilities.

**Q: Which part changes most frequently?**
A: Part 4 (Refine Mode) - expect updates as legacy handling and migration strategies evolve.

**Q: Why underscore version format (v3_6_0) instead of dots (v3.6.0)?**
A: Matches existing SKELETAL naming convention for consistency with current file naming.

---

**Last updated:** 2025-12-25
**Current version:** v3.6.0
**Total parts:** 7
**Assembly time:** ~2 seconds
