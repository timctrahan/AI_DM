# Campaign Build Script - Versioning System

## Overview

The enhanced `assemble_campaign.py` script now includes automatic versioning and backup functionality, similar to the agent_parts orchestrator assembly system.

## Features

### 1. **Automatic Version Tracking**
- Versions are tracked in `version.json`
- Current version: `v2.0.1` (starting version)
- Automatically increments based on file changes

### 2. **Smart Version Incrementing**

The script detects how many campaign files have changed since the last assembly and automatically increments the version:

| Files Changed | Version Increment | Example |
|---------------|-------------------|---------|
| 0-1 files | **Patch** | v2.0.0 → v2.0.1 |
| 2-3 files | **Minor** | v2.0.0 → v2.1.0 |
| 4-6 files | **Major** | v2.0.0 → v3.0.0 |

### 3. **Automatic Backups**

Every time you assemble the campaign:
- Previous version files are backed up to `.previous_versions/` folder
- Backups are stored as ZIP files named by version (e.g., `v2.0.1.zip`)
- Contains all 6 campaign part files from that version

### 4. **Version Metadata Tracking**

The `version.json` file tracks:
- Current version number (major.minor.patch)
- Last assembly date/time
- Output filename with version
- Campaign name
- List of part files
- Versioning rules

## Usage

### Basic Assembly (Automatic Versioning)
```bash
python assemble_campaign.py
```

This will:
1. Validate all campaign parts exist
2. Check which files changed since last assembly
3. Calculate new version number
4. Assemble campaign with version in filename
5. Create backup ZIP of current parts
6. Update `version.json` with new version

**Output**: `CAMPAIGN_The_Towers_Trial_v2.0.X.md` (X increments automatically)

### Validate Parts Only
```bash
python assemble_campaign.py --validate
```

Checks that all 6 campaign files exist without assembling.

### Custom Output Filename (Override Versioning)
```bash
python assemble_campaign.py --output custom_name.md
```

Uses your custom filename instead of the versioned default.

### Specify Base Directory
```bash
python assemble_campaign.py --base-dir /path/to/campaign
```

Runs the assembly from a different directory.

## File Structure

```
the_towers_trial/
├── assemble_campaign.py          # Build script with versioning
├── version.json                   # Version tracking metadata
├── campaign_overview.md           # Part 1
├── act_1_frozen_token.md          # Part 2
├── act_2_poisoned_token.md        # Part 3
├── act_3_corrupted_token.md       # Part 4
├── act_4_storm_token.md           # Part 5
├── act_5_flame_token.md           # Part 6
├── .previous_versions/            # Backup folder (auto-created)
│   ├── v2.0.1.zip
│   ├── v2.0.2.zip
│   └── v2.1.0.zip
└── CAMPAIGN_The_Towers_Trial_v2.0.X.md  # Assembled output
```

## Version History Recovery

To recover a previous version:
1. Navigate to `.previous_versions/` folder
2. Find the version ZIP you want (e.g., `v2.0.1.zip`)
3. Extract the ZIP to get all 6 campaign part files from that version
4. Replace current files with extracted versions
5. Reassemble with `python assemble_campaign.py`

## Example Workflow

### Making Small Edits (Patch Update)

1. Edit one act file (e.g., `act_3_corrupted_token.md`)
2. Run: `python assemble_campaign.py`
3. **Result**: Version increments from v2.0.1 → v2.0.2 (patch)
4. Backup created: `.previous_versions/v2.0.2.zip`

### Making Medium Changes (Minor Update)

1. Edit 3 act files (acts 1, 2, 3)
2. Run: `python assemble_campaign.py`
3. **Result**: Version increments from v2.0.2 → v2.1.0 (minor)
4. Backup created: `.previous_versions/v2.1.0.zip`

### Making Major Revision (Major Update)

1. Edit 5 files (overview + 4 acts)
2. Run: `python assemble_campaign.py`
3. **Result**: Version increments from v2.1.0 → v3.0.0 (major)
4. Backup created: `.previous_versions/v3.0.0.zip`

## Benefits

✅ **Never lose work** - Every assembly creates a backup
✅ **Track changes** - Version numbers indicate scope of changes
✅ **Easy rollback** - Recover any previous version from backups
✅ **Automatic** - No manual version number management
✅ **Timestamped** - Know exactly when each version was created

## Technical Details

### Version Detection Logic

The script uses file modification times (mtime) to detect changes:
1. Reads `last_change_date` from `version.json`
2. Checks mtime of each campaign part file
3. Counts files modified after last assembly
4. Calculates new version based on count

### First Run Behavior

On first run (no `version.json` exists):
- Creates default `version.json` with v2.0.0
- All files count as "changed" (no previous assembly timestamp)
- Increments to v2.0.1 on first assembly

### File Change Threshold Rationale

- **6 total parts** in campaign (overview + 5 acts)
- **0-1 changed** = Small tweaks, bug fixes → Patch
- **2-3 changed** = Moderate updates, content additions → Minor
- **4-6 changed** = Major overhaul, structural changes → Major

## Comparison to Agent Parts System

This implementation mirrors the `agent_parts/assemble_orchestrator.py` versioning system:

| Feature | Agent Parts | Campaign Builder |
|---------|-------------|------------------|
| version.json tracking | ✅ | ✅ |
| Auto version increment | ✅ | ✅ |
| ZIP backups | ✅ | ✅ |
| Modification time detection | ✅ | ✅ |
| Patch/Minor/Major rules | ✅ | ✅ (adapted for 6 files) |
| Header version injection | ✅ (Part 1) | ✅ (Assembly header) |

**Key Difference**: Agent parts has 6 numbered parts, campaign has 1 overview + 5 acts. Versioning rules adjusted accordingly.

## Troubleshooting

### "All files show as changed every time"

**Cause**: Your file system or editor updates mtime even without content changes.

**Solution**: The first assembly after a "touch" will increment version, but subsequent runs with no actual edits will show 0 changes.

### "Version didn't increment"

**Cause**: No files were modified since last assembly.

**Expected**: Version stays the same if content hasn't changed.

### "Backup failed but assembly succeeded"

**Cause**: Permission issues or disk space.

**Impact**: Assembly still succeeds. Backup is optional safeguard.

**Fix**: Check `.previous_versions/` folder permissions.

## Credits

Versioning system adapted from `C:\GitRepos\AI_DM\agent_parts\assemble_orchestrator.py`

Original orchestrator versioning by: [Your attribution here]

Campaign adaptation by: Claude (Anthropic AI)

Date: 2025-12-28
