#!/usr/bin/env python3
"""
Protocol Library Assembler v2.0

Assembles modular protocol parts into a single indexed Protocol Library file
for the D&D 5E AI Orchestrator v2.0.

Usage:
    python assemble_protocol_library.py [output_filename]

If no output filename provided, uses: PROTOCOL_LIBRARY_v{version}.md
Version is read from version.json (or created if not exists)
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path

# Configuration
PROTOCOL_PARTS_DIR = "../PROTOCOL_LIBRARY"
OUTPUT_DIR = "../.."  # Two levels up (to project root)
VERSION_FILE = "../version_v2.json"

# Expected protocol part files in assembly order
PROTOCOL_PARTS = [
    "PART1_Session_Management.md",
    "PART2_Game_Loop.md",
    "PART3_Combat.md",
    "PART4_Progression.md",
    "PART5_Utilities.md",
]


def load_version():
    """Load version from JSON or create default version"""
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Create default version
        default_version = {
            "current_version": {"major": 2, "minor": 0, "patch": 0},
            "last_change_date": datetime.now().isoformat(),
            "output_filename": "PROTOCOL_LIBRARY_v2.0.0.md",
            "part_files": PROTOCOL_PARTS,
            "versioning_rules": {
                "patch": "0-1 files changed",
                "minor": "2-3 files changed",
                "major": "4-5 files changed"
            }
        }
        save_version(default_version)
        return default_version


def save_version(version_data):
    """Save version data to JSON"""
    with open(VERSION_FILE, 'w', encoding='utf-8') as f:
        json.dump(version_data, f, indent=2)


def get_version_string(version_dict):
    """Convert version dict to string (e.g., '2.0.0')"""
    return f"{version_dict['major']}.{version_dict['minor']}.{version_dict['patch']}"


def increment_version(version_dict, files_changed):
    """Increment version based on number of files changed"""
    if files_changed == 0:
        # No changes, don't increment
        return version_dict
    elif files_changed == 1:
        # Patch increment
        version_dict['patch'] += 1
    elif 2 <= files_changed <= 3:
        # Minor increment
        version_dict['minor'] += 1
        version_dict['patch'] = 0
    else:  # 4-5 files changed
        # Major increment
        version_dict['major'] += 1
        version_dict['minor'] = 0
        version_dict['patch'] = 0
    return version_dict


def check_files_changed():
    """Check which protocol parts have been modified since last assembly"""
    version_data = load_version()
    last_change_date = datetime.fromisoformat(version_data['last_change_date'])

    changed_files = []
    for part_file in PROTOCOL_PARTS:
        part_path = os.path.join(PROTOCOL_PARTS_DIR, part_file)
        if os.path.exists(part_path):
            file_mtime = datetime.fromtimestamp(os.path.getmtime(part_path))
            if file_mtime > last_change_date:
                changed_files.append(part_file)

    return changed_files


def extract_protocol_index(content):
    """Extract all protocol IDs from content (finds [PROTOCOL_START: id] tags)"""
    pattern = r'\[PROTOCOL_START:\s*([a-zA-Z0-9_]+)\]'
    return re.findall(pattern, content)


def assemble_protocol_library(output_filename=None):
    """Main assembly function"""
    print("=" * 60)
    print("D&D 5E Orchestrator v2.0 - Protocol Library Assembler")
    print("=" * 60)
    print()

    # Load version
    version_data = load_version()

    # Check for changes
    changed_files = check_files_changed()
    print(f"Files changed since last assembly: {len(changed_files)}")
    if changed_files:
        for cf in changed_files:
            print(f"  - {cf}")
    print()

    # Increment version if files changed
    if changed_files:
        old_version = get_version_string(version_data['current_version'])
        version_data['current_version'] = increment_version(
            version_data['current_version'],
            len(changed_files)
        )
        new_version = get_version_string(version_data['current_version'])
        print(f"Version: {old_version} -> {new_version}")
        version_data['last_change_date'] = datetime.now().isoformat()
    else:
        print(f"Version: {get_version_string(version_data['current_version'])} (unchanged)")
    print()

    # Determine output filename
    if output_filename is None:
        version_str = get_version_string(version_data['current_version'])
        output_filename = f"PROTOCOL_LIBRARY_v{version_str}.md"

    version_data['output_filename'] = output_filename

    # Check all parts exist
    print("Checking protocol parts...")
    missing_parts = []
    for part_file in PROTOCOL_PARTS:
        part_path = os.path.join(PROTOCOL_PARTS_DIR, part_file)
        if not os.path.exists(part_path):
            missing_parts.append(part_file)
            print(f"  ✗ {part_file} - NOT FOUND")
        else:
            size_kb = os.path.getsize(part_path) / 1024
            print(f"  OK {part_file} ({size_kb:.1f} KB)")

    if missing_parts:
        print()
        print(f"ERROR: {len(missing_parts)} part(s) missing. Assembly aborted.")
        return False

    print()
    print("Assembling protocol library...")

    # Assemble content
    assembled_content = []
    all_protocol_ids = []

    # Header
    version_str = get_version_string(version_data['current_version'])
    header = f"""# PROTOCOL LIBRARY v{version_str}
# D&D 5E AI Orchestrator - Gameplay Protocols

**DO NOT EDIT DURING SESSION** - This is a read-only reference file for the AI Orchestrator

**PURPOSE**: Contains all gameplay logic protocols in indexed, retrievable format

**ASSEMBLY DATE**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

"""
    assembled_content.append(header)

    # Build master index (will be populated after reading all parts)
    index_placeholder = "[PROTOCOL_INDEX_PLACEHOLDER]\n\n---\n\n"
    assembled_content.append(index_placeholder)

    # Read and concatenate all parts
    for part_file in PROTOCOL_PARTS:
        part_path = os.path.join(PROTOCOL_PARTS_DIR, part_file)

        print(f"  Reading {part_file}...")
        with open(part_path, 'r', encoding='utf-8') as f:
            part_content = f.read()

        # Extract protocol IDs from this part
        protocol_ids = extract_protocol_index(part_content)
        all_protocol_ids.extend(protocol_ids)
        print(f"    Found {len(protocol_ids)} protocols: {', '.join(protocol_ids)}")

        # Add part header
        assembled_content.append(f"# {'=' * 60}\n")
        assembled_content.append(f"# SOURCE: {part_file}\n")
        assembled_content.append(f"# {'=' * 60}\n\n")

        # Add part content
        assembled_content.append(part_content)

        # Add separator
        assembled_content.append("\n\n---\n\n")

    # Build the actual index
    protocol_index = build_protocol_index(all_protocol_ids)

    # Replace placeholder with actual index
    assembled_text = ''.join(assembled_content)
    assembled_text = assembled_text.replace("[PROTOCOL_INDEX_PLACEHOLDER]", protocol_index)

    # Write output
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    print()
    print(f"Writing to: {output_path}")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(assembled_text)

    # Save updated version
    save_version(version_data)

    # Report statistics
    output_size_kb = len(assembled_text.encode('utf-8')) / 1024
    print()
    print("=" * 60)
    print("Assembly Complete!")
    print("=" * 60)
    print(f"Output file: {output_filename}")
    print(f"Output size: {output_size_kb:.1f} KB")
    print(f"Total protocols: {len(all_protocol_ids)}")
    print()

    # Verify size is reasonable
    if output_size_kb < 10:
        print("⚠️  WARNING: Output file is very small (<10 KB). Check for errors.")
    elif output_size_kb > 100:
        print("⚠️  WARNING: Output file is very large (>100 KB). Consider compression.")
    else:
        print("OK - Output size is within expected range (10-100 KB)")

    print()
    print("Next steps:")
    print("1. Review the assembled protocol library")
    print("2. Test with Immutable Kernel and Campaign Data Vault")
    print("3. Run verification: grep -c '\\[PROTOCOL_START:' {output_filename}")

    return True


def build_protocol_index(protocol_ids):
    """Build the master index of all protocols, organized by category"""

    # Categorize protocols by prefix
    categories = {
        'session_management': [],
        'game_loop': [],
        'combat': [],
        'progression': [],
        'utilities': [],
        'meta': []
    }

    for proto_id in protocol_ids:
        # Categorize based on common prefixes
        if 'session' in proto_id or 'character' in proto_id or 'init' in proto_id or 'resume' in proto_id or 'state' in proto_id:
            categories['session_management'].append(proto_id)
        elif 'game_loop' in proto_id or 'exploration' in proto_id or 'movement' in proto_id or 'investigation' in proto_id or 'npc' in proto_id:
            categories['game_loop'].append(proto_id)
        elif 'combat' in proto_id or 'attack' in proto_id or 'death' in proto_id:
            categories['combat'].append(proto_id)
        elif 'xp' in proto_id or 'level' in proto_id or 'quest' in proto_id or 'loot' in proto_id or 'reputation' in proto_id:
            categories['progression'].append(proto_id)
        elif 'shop' in proto_id or 'rest' in proto_id or 'inventory' in proto_id:
            categories['utilities'].append(proto_id)
        else:
            categories['meta'].append(proto_id)

    # Build index text
    index_lines = ["[PROTOCOL_INDEX]"]

    for category_name, protocol_list in categories.items():
        if protocol_list:  # Only include categories that have protocols
            index_lines.append(f"{category_name}:")
            for proto_id in protocol_list:
                index_lines.append(f"  - {proto_id}")

    return '\n'.join(index_lines)


def main():
    """Main entry point"""
    # Get output filename from command line if provided
    output_filename = None
    if len(sys.argv) > 1:
        output_filename = sys.argv[1]
        print(f"Using custom output filename: {output_filename}")
        print()

    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Run assembly
    success = assemble_protocol_library(output_filename)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
