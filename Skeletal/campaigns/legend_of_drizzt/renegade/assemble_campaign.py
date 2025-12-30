#!/usr/bin/env python3
"""
Campaign Assembly Script for "Renegade"
Combines modular campaign files into a single complete campaign document.
Uses version.json for dynamic versioning based on file changes.

Usage:
    python assemble_campaign.py                    # Creates full campaign with versioning
    python assemble_campaign.py --output custom.md # Custom output filename
    python assemble_campaign.py --validate         # Validates all parts exist
"""

import os
import sys
import json
import zipfile
from pathlib import Path
from datetime import datetime
from typing import List, Optional

# Campaign configuration
CAMPAIGN_NAME = "Renegade"
VERSION_FILE = "version.json"

# File structure (overview first, then acts in order)
PARTS = [
    "CAMPAIGN_RENEGADE_overview.md",
    "CAMPAIGN_RENEGADE_act_1.md",
    "CAMPAIGN_RENEGADE_act_2.md",
    "CAMPAIGN_RENEGADE_act_3.md",
    "CAMPAIGN_RENEGADE_act_4.md",
    "CAMPAIGN_RENEGADE_act_4_redemption.md",
    "CAMPAIGN_RENEGADE_act_4_darkness.md",
    "CAMPAIGN_RENEGADE_act_4_neutral.md"
]

DEFAULT_OUTPUT = "CAMPAIGN_Renegade.md"


def load_version():
    """Load version information from version.json"""
    if not os.path.exists(VERSION_FILE):
        # Create default version file if it doesn't exist
        default_version = {
            "current_version": {"major": 2, "minor": 0, "patch": 0},
            "last_change_date": datetime.now().isoformat(),
            "output_filename": "CAMPAIGN_Renegade_v2.0.0.md",
            "campaign_name": CAMPAIGN_NAME,
            "part_files": PARTS,
            "versioning_rules": {
                "patch": "0-1 files changed",
                "minor": "2-4 files changed",
                "major": "5-8 files changed"
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
        # 5-8 files: increment major, reset minor and patch
        return {"major": major + 1, "minor": 0, "patch": 0}


def get_version_string(version):
    """Convert version dict to string format"""
    return f"v{version['major']}.{version['minor']}.{version['patch']}"


class CampaignAssembler:
    """Assembles modular campaign files into complete campaign document with versioning."""

    def __init__(self, base_dir: Optional[Path] = None):
        """Initialize assembler with base directory."""
        self.base_dir = base_dir or Path(__file__).parent
        self.parts = PARTS
        self.output_file = DEFAULT_OUTPUT

    def validate_parts(self) -> bool:
        """Validate that all campaign parts exist."""
        print("Validating campaign parts...")
        all_valid = True

        for part in self.parts:
            part_path = self.base_dir / part
            if part_path.exists():
                print(f"  [OK] {part}")
            else:
                print(f"  [MISSING] {part} - NOT FOUND")
                all_valid = False

        return all_valid

    def read_part(self, filename: str) -> str:
        """Read a campaign part file."""
        part_path = self.base_dir / filename
        try:
            with open(part_path, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"  [OK] Read {filename} ({len(content)} chars)")
            return content
        except Exception as e:
            print(f"  [ERROR] Error reading {filename}: {e}")
            return ""

    def assemble(self, version_string: str) -> str:
        """Assemble all parts into complete campaign."""
        print(f"\nAssembling {CAMPAIGN_NAME}...")

        # Start with empty string (no header)
        assembled = ""

        # Add each part
        for i, part in enumerate(self.parts):
            content = self.read_part(part)
            if content:
                # Add double newline between parts (not before first part)
                if i > 0:
                    assembled += "\n\n"
                assembled += content

        # No footer - just return assembled content
        return assembled

    def _build_header(self, version_string: str) -> str:
        """Build campaign file header."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""# ==============================================================================
# ASSEMBLED CAMPAIGN FILE
# ==============================================================================
# Campaign: {CAMPAIGN_NAME}
# Version: {version_string}
# Assembled: {timestamp}
# Generator: assemble_campaign.py (with versioning)
#
# This file was automatically generated from modular campaign parts.
# To edit, modify the individual overview/act files and reassemble.
# ==============================================================================
"""

    def _build_footer(self, version_string: str) -> str:
        """Build campaign file footer."""
        return f"""
# ==============================================================================
# END OF ASSEMBLED CAMPAIGN
# ==============================================================================
# Campaign: {CAMPAIGN_NAME}
# Version: {version_string}
# Total Parts Assembled: {len(self.parts)}
#
# Component Files:
{chr(10).join(f"#   - {part}" for part in self.parts)}
#
# To reassemble: python assemble_campaign.py
# ==============================================================================
"""

    def save(self, content: str, output_file: str) -> bool:
        """Save assembled campaign to file."""
        output_path = self.base_dir / output_file

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            file_size = output_path.stat().st_size
            print(f"\n[SUCCESS] Campaign assembled successfully!")
            print(f"  Output: {output_path}")
            print(f"  Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            return True

        except Exception as e:
            print(f"\n[ERROR] Error saving campaign: {e}")
            return False

    def backup_parts(self, version_string: str, part_files: List[str]) -> bool:
        """Backup part files to versioned archive."""
        try:
            backup_dir = self.base_dir / ".previous_versions"
            backup_dir.mkdir(exist_ok=True)

            zip_filename = f"{version_string}.zip"
            zip_path = backup_dir / zip_filename

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
                for part in part_files:
                    part_path = self.base_dir / part
                    if part_path.exists():
                        zf.write(part_path, arcname=part)

            zip_size = zip_path.stat().st_size
            print(f"  Backup: {zip_path} ({zip_size/1024:.1f} KB)")
            return True

        except Exception as e:
            print(f"  WARNING: Backup creation failed: {e}")
            # Continue execution - assembly succeeded, backup is optional
            return False


def main():
    """Main execution function with versioning."""
    import argparse

    parser = argparse.ArgumentParser(
        description=f"Assemble {CAMPAIGN_NAME} from modular parts with versioning"
    )
    parser.add_argument(
        '--output', '-o',
        help='Output filename (overrides versioned default)',
        default=None
    )
    parser.add_argument(
        '--validate', '-v',
        action='store_true',
        help='Only validate parts, do not assemble'
    )
    parser.add_argument(
        '--base-dir', '-d',
        help='Base directory for campaign files',
        type=Path,
        default=None
    )

    args = parser.parse_args()

    # Create assembler
    assembler = CampaignAssembler(base_dir=args.base_dir)

    # Validate parts
    if not assembler.validate_parts():
        print("\n[ERROR] Validation failed! Some parts are missing.")
        return 1

    print("\n[SUCCESS] All parts validated successfully!")

    # If only validating, exit here
    if args.validate:
        return 0

    # Load version information
    print("\n" + "="*80)
    print("VERSION TRACKING")
    print("="*80)
    version_data = load_version()

    parts = version_data["part_files"]
    current_version = version_data["current_version"]
    last_change_date = version_data["last_change_date"]

    print(f"Current version: {get_version_string(current_version)}")
    print(f"Last assembly: {last_change_date}")

    # Count changed files
    changed_count = count_changed_files(parts, last_change_date)
    print(f"Files changed since last assembly: {changed_count}")

    # Calculate new version
    new_version = calculate_new_version(current_version, changed_count)
    version_string = get_version_string(new_version)

    print(f"New version: {version_string}")
    if changed_count <= 1:
        print(f"  Reason: 0-1 files changed (patch increment)")
    elif changed_count <= 4:
        print(f"  Reason: 2-4 files changed (minor increment)")
    else:
        print(f"  Reason: 5-8 files changed (major increment)")

    # Generate output filename (unless overridden)
    if args.output is None:
        output_file = f"CAMPAIGN_Renegade_{version_string}.md"
    else:
        output_file = args.output

    print(f"\nOutput file: {output_file}")

    # Assemble campaign
    print("\n" + "="*80)
    print("ASSEMBLY")
    print("="*80)
    assembled_content = assembler.assemble(version_string)

    if not assembled_content:
        print("\n[ERROR] Assembly failed!")
        return 1

    # Save assembled campaign
    if not assembler.save(assembled_content, output_file):
        return 1

    # Backup part files to versioned archive
    print("\n" + "="*80)
    print("BACKUP")
    print("="*80)
    assembler.backup_parts(version_string, parts)

    # Update version.json
    version_data["current_version"] = new_version
    version_data["last_change_date"] = datetime.now().isoformat()
    version_data["output_filename"] = output_file
    save_version(version_data)

    print(f"\nVersion updated: {get_version_string(current_version)} -> {version_string}")
    print(f"Version tracking saved to {VERSION_FILE}")

    # Final summary
    print("\n" + "="*80)
    print("ASSEMBLY COMPLETE!")
    print("="*80)
    print(f"\nYour complete campaign is ready: {output_file}")
    print(f"Version: {version_string}")
    print("\nNext steps:")
    print("  1. Load SKELETAL_DM_KERNEL_v1.md in your AI DM")
    print(f"  2. Load {output_file}")
    print("  3. Begin your adventure!")
    print("\n" + "="*80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
