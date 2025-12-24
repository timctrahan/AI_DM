#!/usr/bin/env python3
"""
Orchestrator Assembly Script for "Skeletal Campaign Orchestrator"
Combines modular orchestrator files into a single complete orchestrator document.

Usage:
    python assemble_orchestrator.py                    # Creates full orchestrator
    python assemble_orchestrator.py --output custom.md # Custom output filename
    python assemble_orchestrator.py --validate         # Validates all parts exist
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Optional

# Orchestrator configuration
ORCHESTRATOR_NAME = "Skeletal Campaign Orchestrator"
ORCHESTRATOR_VERSION = "1.0"

# File structure - order matters!
PARTS = [
    "orchestrator_header.md",
    "section_0_framework_principles.md",
    "section_0_5_ip_clean_framework.md",
    "section_1_campaign_skeleton.md",
    "section_2_world_rules.md",
    "section_3_character_templates.md",
    "section_4_encounter_framework.md",
    "section_5_decision_points.md",
    "section_6_world_state_tracking.md",
    "section_7_session_prep.md",
    "section_8_dm_reasoning.md",
    "section_8_5_context_weaving.md",
    "section_9_save_file_format.md",
    "section_10_orchestrator_integration.md",
    "section_11_example_campaign.md",
    "section_12_usage_notes.md",
    "section_13_migration_notes.md",
    "orchestrator_footer.md"
]

DEFAULT_OUTPUT = "SKELETAL_CAMPAIGN_ORCHESTRATOR_v1_0.md"


class OrchestratorAssembler:
    """Assembles modular orchestrator files into complete orchestrator document."""

    def __init__(self, base_dir: Optional[Path] = None):
        """Initialize assembler with base directory."""
        self.base_dir = base_dir or Path(__file__).parent
        self.parts = PARTS
        self.output_file = DEFAULT_OUTPUT

    def validate_parts(self) -> bool:
        """Validate that all orchestrator parts exist."""
        print("Validating orchestrator parts...")
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
        """Read an orchestrator part file."""
        part_path = self.base_dir / filename
        try:
            with open(part_path, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"  [OK] Read {filename} ({len(content)} chars)")
            return content
        except Exception as e:
            print(f"  [ERROR] Error reading {filename}: {e}")
            return ""

    def assemble(self) -> str:
        """Assemble all parts into complete orchestrator."""
        print(f"\nAssembling {ORCHESTRATOR_NAME}...")

        # Build assembly header
        assembled = self._build_assembly_header()

        # Add each part
        for part in self.parts:
            content = self.read_part(part)
            if content:
                # Add section separator (except for header)
                if part != "orchestrator_header.md":
                    assembled += "\n\n"
                assembled += content

        return assembled

    def _build_assembly_header(self) -> str:
        """Build orchestrator file assembly header."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""# ==============================================================================
# ASSEMBLED ORCHESTRATOR FILE
# ==============================================================================
# Orchestrator: {ORCHESTRATOR_NAME}
# Version: {ORCHESTRATOR_VERSION}
# Assembled: {timestamp}
# Generator: assemble_orchestrator.py
#
# This file was automatically generated from modular orchestrator parts.
# To edit, modify the individual section files and reassemble.
# ==============================================================================

"""

    def save(self, content: str, output_file: Optional[str] = None) -> bool:
        """Save assembled orchestrator to file."""
        # Save to parent directory (one level up from parts folder)
        output_dir = self.base_dir.parent
        output_path = output_dir / (output_file or self.output_file)

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            file_size = output_path.stat().st_size
            print(f"\n[SUCCESS] Orchestrator assembled successfully!")
            print(f"  Output: {output_path}")
            print(f"  Size: {file_size:,} bytes")
            return True

        except Exception as e:
            print(f"\n[ERROR] Error saving orchestrator: {e}")
            return False

    def generate_toc(self, content: str) -> str:
        """Generate table of contents from assembled content."""
        print("\nGenerating table of contents...")

        toc_lines = ["# TABLE OF CONTENTS\n"]

        # Find all major headers (sections)
        for line in content.split('\n'):
            if line.startswith('# SECTION') or line.startswith('# ⚠️'):
                # Extract header
                header = line.lstrip('#').strip()
                if header:
                    # Create TOC entry
                    anchor = header.lower().replace(' ', '-').replace("'", '').replace(':', '').replace('⚠️', '')
                    toc_lines.append(f"- [{header}](#{anchor})")

        return '\n'.join(toc_lines) + '\n\n'


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description=f"Assemble {ORCHESTRATOR_NAME} from modular parts"
    )
    parser.add_argument(
        '--output', '-o',
        help=f'Output filename (default: {DEFAULT_OUTPUT})',
        default=DEFAULT_OUTPUT
    )
    parser.add_argument(
        '--validate', '-v',
        action='store_true',
        help='Only validate parts, do not assemble'
    )
    parser.add_argument(
        '--toc',
        action='store_true',
        help='Generate table of contents'
    )
    parser.add_argument(
        '--base-dir', '-d',
        help='Base directory for orchestrator files',
        type=Path,
        default=None
    )

    args = parser.parse_args()

    # Create assembler
    assembler = OrchestratorAssembler(base_dir=args.base_dir)
    assembler.output_file = args.output

    # Validate parts
    if not assembler.validate_parts():
        print("\n[ERROR] Validation failed! Some parts are missing.")
        return 1

    print("\n[SUCCESS] All parts validated successfully!")

    # If only validating, exit here
    if args.validate:
        return 0

    # Assemble orchestrator
    assembled_content = assembler.assemble()

    if not assembled_content:
        print("\n[ERROR] Assembly failed!")
        return 1

    # Add TOC if requested
    if args.toc:
        toc = assembler.generate_toc(assembled_content)
        # Insert TOC after assembly header
        header_end = assembled_content.find('\n\n', 500)
        if header_end > 0:
            assembled_content = (
                assembled_content[:header_end] + '\n\n' +
                toc +
                assembled_content[header_end:]
            )

    # Save assembled orchestrator
    if not assembler.save(assembled_content):
        return 1

    print("\n" + "="*80)
    print("ASSEMBLY COMPLETE!")
    print("="*80)
    print(f"\nYour complete orchestrator is ready: {args.output}")
    print("\nNext steps:")
    print("  1. Use this orchestrator as a template for building skeletal campaigns")
    print("  2. Fill in Sections 1-6 with your campaign specifics")
    print("  3. Reference Sections 7-13 during gameplay and prep")
    print("\n" + "="*80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
