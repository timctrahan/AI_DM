#!/usr/bin/env python3
"""
Assembly script for SKELETAL Campaign Orchestrator
Concatenates 7 modular parts into final orchestrator
Uses version.json for dynamic versioning based on file changes
"""

import os
import sys
import json
from datetime import datetime
import zipfile

VERSION_FILE = "version.json"

def load_version():
    """Load version information from version.json"""
    if not os.path.exists(VERSION_FILE):
        # Create default version file if it doesn't exist
        default_version = {
            "current_version": {"major": 3, "minor": 6, "patch": 0},
            "last_change_date": datetime.now().isoformat(),
            "output_filename": "SKELETAL_CAMPAIGN_ORCHESTRATOR_v3_6.md",
            "part_files": [
                "SKELETAL_PART1_Identity.md",
                "SKELETAL_PART2_OutputFormats.md",
                "SKELETAL_PART3_NewMode.md",
                "SKELETAL_PART4_RefineMode.md",
                "SKELETAL_PART5_InnovatePlaytest.md",
                "SKELETAL_PART6_MechanicalSystems.md",
                "SKELETAL_PART7_Reference.md"
            ],
            "versioning_rules": {
                "patch": "0-1 files changed",
                "minor": "2-4 files changed",
                "major": "5-7 files changed"
            }
        }
        save_version(default_version)
        return default_version

    with open(VERSION_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_version(version_data):
    """Save version information to version.json"""
    with open(VERSION_FILE, "w", encoding="utf-8") as f:
        json.dump(version_data, f, indent=2)

def count_changed_files(part_files, last_change_date):
    """Count how many part files have changed since last assembly"""
    changed_count = 0
    last_timestamp = datetime.fromisoformat(last_change_date)

    for part in part_files:
        if os.path.exists(part):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(part))
            if file_mtime > last_timestamp:
                changed_count += 1

    return changed_count

def calculate_new_version(current_version, changed_count):
    """Calculate new version based on number of changed files (7-part system)"""
    major = current_version["major"]
    minor = current_version["minor"]
    patch = current_version["patch"]

    if changed_count <= 1:
        # 0-1 files: increment patch
        return {"major": major, "minor": minor, "patch": patch + 1}
    elif changed_count <= 4:
        # 2-4 files: increment minor, reset patch
        return {"major": major, "minor": minor + 1, "patch": 0}
    else:
        # 5-7 files: increment major, reset minor and patch
        return {"major": major + 1, "minor": 0, "patch": 0}

def get_version_string(version):
    """Convert version dict to string format"""
    return f"v{version['major']}_{version['minor']}"

def get_friendly_version_string(version):
    """Convert version dict to friendly display format"""
    return f"v{version['major']}.{version['minor']}.{version['patch']}"

def update_part1_version(content, version_string):
    """Update Part 1 header version number to match assembled version"""
    import re

    # Update version in line 1: "# SKELETAL CAMPAIGN ORCHESTRATOR vX.Y" → "vX_Y"
    # Handle both underscore (v3_6) and dot (v3.6) formats in source
    content = re.sub(
        r"# SKELETAL CAMPAIGN ORCHESTRATOR v\d+[._]\d+(?:[._]\d+)?",
        f"# SKELETAL CAMPAIGN ORCHESTRATOR {version_string}",
        content
    )

    return content

def assemble_orchestrator(output_file=None):
    """Assemble orchestrator from parts with dynamic versioning"""

    # Load version information
    print("Loading version information...")
    version_data = load_version()

    parts = version_data["part_files"]
    current_version = version_data["current_version"]
    last_change_date = version_data["last_change_date"]

    print(f"  Current version: {get_friendly_version_string(current_version)}")
    print(f"  Last assembly: {last_change_date}")

    # Check all parts exist
    print("\nChecking part files...")
    for part in parts:
        if not os.path.exists(part):
            print(f"ERROR: Missing part: {part}")
            sys.exit(1)

    # Count changed files
    changed_count = count_changed_files(parts, last_change_date)
    print(f"  Files changed since last assembly: {changed_count}")

    # Calculate new version
    new_version = calculate_new_version(current_version, changed_count)
    version_string = get_version_string(new_version)
    friendly_version = get_friendly_version_string(new_version)

    print(f"  New version: {friendly_version}")
    if changed_count <= 1:
        print(f"    Reason: 0-1 files changed (patch increment)")
    elif changed_count <= 4:
        print(f"    Reason: 2-4 files changed (minor increment)")
    else:
        print(f"    Reason: 5-7 files changed (major increment)")

    # Generate output filename (unless overridden)
    # FIXED FILENAME - user handles their own versioning externally
    if output_file is None:
        output_file = f"SKELETAL_CAMPAIGN_ORCHESTRATOR_{version_string}.md"
        # Write to parent directory (campaigns)
        output_path = os.path.join("..", output_file)
    else:
        output_path = output_file

    print(f"\nAssembling orchestrator...")
    print(f"  Output: {output_path}")

    # Assemble
    with open(output_path, "w", encoding="utf-8") as output:
        for i, part in enumerate(parts, 1):
            print(f"  Adding Part {i}: {part}")
            with open(part, "r", encoding="utf-8") as f:
                content = f.read()

                # Update Part 1 version header to match assembled version
                if i == 1:  # Part 1
                    content = update_part1_version(content, version_string)

                output.write(content)

                # Add separator between parts (not after last part)
                if i < len(parts):
                    output.write("\n\n---\n\n")

    # Verify
    size = os.path.getsize(output_path)
    size_kb = size / 1024

    print(f"\nAssembly complete!")
    print(f"  Output: {output_path}")
    print(f"  Size: {size} bytes ({size_kb:.1f} KB)")

    # Verify size is reasonable (20-30KB expected for SKELETAL)
    if size < 15000:
        print("  WARNING: File smaller than expected (expected ~25KB)")
    elif size > 40000:
        print("  WARNING: File larger than expected (expected ~25KB)")
    else:
        print("  Size looks good")

    # Backup part files to versioned archive
    try:
        backup_dir = ".previous_versions"
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir, exist_ok=True)

        zip_filename = f"{version_string}.zip"
        zip_path = os.path.join(backup_dir, zip_filename)

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for part in parts:
                zf.write(part)

        zip_size = os.path.getsize(zip_path)
        print(f"  Backup: {zip_path} ({zip_size/1024:.1f} KB)")

    except Exception as e:
        print(f"  WARNING: Backup creation failed: {e}")
        # Continue execution - assembly succeeded, backup is optional

    # Update version.json
    version_data["current_version"] = new_version
    version_data["last_change_date"] = datetime.now().isoformat()
    version_data["output_filename"] = output_file
    save_version(version_data)

    print(f"\nVersion updated: {get_friendly_version_string(current_version)} -> {friendly_version}")
    print(f"Version tracking saved to {VERSION_FILE}")
    print(f"\n[OK] Orchestrator assembly complete")

    return output_path

if __name__ == "__main__":
    # Allow optional command-line override of output filename
    output = None
    if len(sys.argv) > 1:
        output = sys.argv[1]

    assemble_orchestrator(output)
