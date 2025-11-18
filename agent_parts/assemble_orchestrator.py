#!/usr/bin/env python3
"""
Assembly script for D&D 5E Orchestrator
Concatenates 6 modular parts into final orchestrator
Uses version.json for dynamic versioning based on file changes
"""

import os
import sys
import json
from datetime import datetime

VERSION_FILE = "version.json"

def load_version():
    """Load version information from version.json"""
    if not os.path.exists(VERSION_FILE):
        # Create default version file if it doesn't exist
        default_version = {
            "current_version": {"major": 4, "minor": 0, "patch": 0},
            "last_change_date": datetime.now().isoformat(),
            "output_filename": "CORE_DND5E_AGENT_ORCHESTRATOR_v4.0.0.md",
            "part_files": [
                "DND_ORCH_PART1_Foundation.md",
                "DND_ORCH_PART2_SessionMgmt.md",
                "DND_ORCH_PART3_GameLoop.md",
                "DND_ORCH_PART4_Combat.md",
                "DND_ORCH_PART5_Progression.md",
                "DND_ORCH_PART6_Closing.md"
            ],
            "versioning_rules": {
                "patch": "0-1 files changed",
                "minor": "2-4 files changed",
                "major": "5-6 files changed"
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
    """Calculate new version based on number of changed files"""
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
        # 5-6 files: increment major, reset minor and patch
        return {"major": major + 1, "minor": 0, "patch": 0}

def get_version_string(version):
    """Convert version dict to string format"""
    return f"v{version['major']}.{version['minor']}.{version['patch']}"

def assemble_orchestrator(output_file=None):
    """Assemble orchestrator from parts with dynamic versioning"""

    # Load version information
    print("Loading version information...")
    version_data = load_version()

    parts = version_data["part_files"]
    current_version = version_data["current_version"]
    last_change_date = version_data["last_change_date"]

    print(f"  Current version: {get_version_string(current_version)}")
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

    print(f"  New version: {version_string}")
    if changed_count <= 1:
        print(f"    Reason: 0-1 files changed (patch increment)")
    elif changed_count <= 4:
        print(f"    Reason: 2-4 files changed (minor increment)")
    else:
        print(f"    Reason: 5-6 files changed (major increment)")

    # Generate output filename (unless overridden)
    if output_file is None:
        output_file = f"CORE_DND5E_AGENT_ORCHESTRATOR_{version_string}.md"
        # Write to parent directory
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

    # Verify size is reasonable (40-50KB expected)
    if size < 40000:
        print("  WARNING: File smaller than expected (expected ~43KB)")
    elif size > 50000:
        print("  WARNING: File larger than expected (expected ~43KB)")
    else:
        print("  Size looks good")

    # Update version.json
    version_data["current_version"] = new_version
    version_data["last_change_date"] = datetime.now().isoformat()
    version_data["output_filename"] = output_file
    save_version(version_data)

    print(f"\nVersion updated: {get_version_string(current_version)} -> {version_string}")
    print(f"Version tracking saved to {VERSION_FILE}")

    return output_path

if __name__ == "__main__":
    # Allow optional command-line override of output filename
    output = None
    if len(sys.argv) > 1:
        output = sys.argv[1]

    assemble_orchestrator(output)
