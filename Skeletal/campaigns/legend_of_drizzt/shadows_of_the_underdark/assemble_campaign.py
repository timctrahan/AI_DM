#!/usr/bin/env python3
"""
Assembles the modular Shadows of the Underdark campaign into a single file.
"""

import os
from pathlib import Path

def assemble_campaign():
    """Assembles campaign from modular components."""

    # Get the directory where this script is located
    script_dir = Path(__file__).parent

    # Define the assembly order
    components = [
        "campaign_overview.md",
        "act_1_the_fall.md",
        "act_2_the_wandering.md",
        "act_3_the_reckoning.md"
    ]

    # Output file
    output_file = script_dir / "CAMPAIGN_Shadows_of_the_Underdark.md"

    # Assemble the campaign
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for component in components:
            component_path = script_dir / component

            if not component_path.exists():
                print(f"WARNING: Component not found: {component}")
                continue

            print(f"Adding: {component}")

            with open(component_path, 'r', encoding='utf-8') as infile:
                content = infile.read()
                outfile.write(content)
                outfile.write("\n\n")

        # Add final footer
        outfile.write("---\n\n")
        outfile.write("**END OF CAMPAIGN FILE**\n\n")
        outfile.write("*Load SKELETAL_DM_KERNEL_v1.md first, then this file.*\n")

    # Report results
    file_size = output_file.stat().st_size
    print(f"\nCampaign assembled successfully!")
    print(f"Output: {output_file}")
    print(f"Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")

    return output_file

if __name__ == "__main__":
    assemble_campaign()
