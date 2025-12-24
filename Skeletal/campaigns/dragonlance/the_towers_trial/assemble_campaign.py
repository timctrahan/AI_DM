#!/usr/bin/env python3
"""
Campaign Assembly Script for "The Tower's Trial"
Combines modular campaign files into a single complete campaign document.

Usage:
    python assemble_campaign.py                    # Creates full campaign
    python assemble_campaign.py --output custom.md # Custom output filename
    python assemble_campaign.py --validate         # Validates all parts exist
"""

import os
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Optional

# Campaign configuration
CAMPAIGN_NAME = "The Tower's Trial"
CAMPAIGN_VERSION = "1.0"

# File structure
PARTS = [
    "campaign_overview.md",
    "act_1_frozen_token.md",
    "act_2_poisoned_token.md",
    "act_3_corrupted_token.md",
    "act_4_storm_token.md",
    "act_5_flame_token.md"
]

DEFAULT_OUTPUT = "CAMPAIGN_The_Towers_Trial.md"


class CampaignAssembler:
    """Assembles modular campaign files into complete campaign document."""

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

    def assemble(self) -> str:
        """Assemble all parts into complete campaign."""
        print(f"\nAssembling {CAMPAIGN_NAME}...")

        # Build header
        assembled = self._build_header()

        # Add each part
        for part in self.parts:
            content = self.read_part(part)
            if content:
                # Add section separator
                assembled += "\n\n" + "="*80 + "\n\n"
                assembled += content

        # Add footer
        assembled += "\n\n" + self._build_footer()

        return assembled

    def _build_header(self) -> str:
        """Build campaign file header."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"""# ==============================================================================
# ASSEMBLED CAMPAIGN FILE
# ==============================================================================
# Campaign: {CAMPAIGN_NAME}
# Version: {CAMPAIGN_VERSION}
# Assembled: {timestamp}
# Generator: assemble_campaign.py
#
# This file was automatically generated from modular campaign parts.
# To edit, modify the individual act files and reassemble.
# ==============================================================================
"""

    def _build_footer(self) -> str:
        """Build campaign file footer."""
        return f"""
# ==============================================================================
# END OF ASSEMBLED CAMPAIGN
# ==============================================================================
# Campaign: {CAMPAIGN_NAME}
# Total Parts Assembled: {len(self.parts)}
#
# Component Files:
{chr(10).join(f"#   - {part}" for part in self.parts)}
#
# To reassemble: python assemble_campaign.py
# ==============================================================================
"""

    def save(self, content: str, output_file: Optional[str] = None) -> bool:
        """Save assembled campaign to file."""
        output_path = self.base_dir / (output_file or self.output_file)

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

            file_size = output_path.stat().st_size
            print(f"\n[SUCCESS] Campaign assembled successfully!")
            print(f"  Output: {output_path}")
            print(f"  Size: {file_size:,} bytes")
            return True

        except Exception as e:
            print(f"\n[ERROR] Error saving campaign: {e}")
            return False

    def generate_toc(self, content: str) -> str:
        """Generate table of contents from assembled content."""
        print("\nGenerating table of contents...")

        toc_lines = ["# TABLE OF CONTENTS\n"]

        # Find all major headers
        for line in content.split('\n'):
            if line.startswith('# ') and not line.startswith('# ='):
                # Extract header
                header = line.lstrip('#').strip()
                if header and header != "TABLE OF CONTENTS":
                    # Create TOC entry
                    anchor = header.lower().replace(' ', '-').replace("'", '')
                    toc_lines.append(f"- [{header}](#{anchor})")

        return '\n'.join(toc_lines) + '\n\n'


def main():
    """Main execution function."""
    import argparse

    parser = argparse.ArgumentParser(
        description=f"Assemble {CAMPAIGN_NAME} from modular parts"
    )
    parser.add_argument(
        '--output', '-o',
        help='Output filename (default: CAMPAIGN_The_Towers_Trial.md)',
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
        help='Base directory for campaign files',
        type=Path,
        default=None
    )

    args = parser.parse_args()

    # Create assembler
    assembler = CampaignAssembler(base_dir=args.base_dir)
    assembler.output_file = args.output

    # Validate parts
    if not assembler.validate_parts():
        print("\n[ERROR] Validation failed! Some parts are missing.")
        return 1

    print("\n[SUCCESS] All parts validated successfully!")

    # If only validating, exit here
    if args.validate:
        return 0

    # Assemble campaign
    assembled_content = assembler.assemble()

    if not assembled_content:
        print("\n[ERROR] Assembly failed!")
        return 1

    # Add TOC if requested
    if args.toc:
        toc = assembler.generate_toc(assembled_content)
        # Insert TOC after header
        header_end = assembled_content.find('\n\n', 500)
        assembled_content = (
            assembled_content[:header_end] + '\n\n' +
            toc +
            assembled_content[header_end:]
        )

    # Save assembled campaign
    if not assembler.save(assembled_content):
        return 1

    print("\n" + "="*80)
    print("ASSEMBLY COMPLETE!")
    print("="*80)
    print(f"\nYour complete campaign is ready: {args.output}")
    print("\nNext steps:")
    print("  1. Load SKELETAL_DM_KERNEL_v1.md in your AI DM")
    print(f"  2. Load {args.output}")
    print("  3. Begin your adventure!")
    print("\n" + "="*80)

    return 0


if __name__ == "__main__":
    sys.exit(main())
