#!/usr/bin/env python3
"""
Campaign Data Vault Generator v2.0

Converts existing campaign markdown files into indexed Campaign Data Vault format
for the D&D 5E AI Orchestrator v2.0.

Usage:
    python create_campaign_vault.py <input_campaign.md> [output_vault.md]

Example:
    python create_campaign_vault.py "../../campaigns/Descent into Khar-Morkai/Act_2_The_Dead_City.md"

This will create: Act_2_Data_Vault.md
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path


def normalize_id(name):
    """Convert a name to a normalized module ID

    Examples:
        'Zilvra Shadowveil' → 'zilvra_shadowveil'
        'Main Street' → 'main_street'
        'MQ1: Mapping the Dead' → 'mq1_mapping_the_dead'
    """
    # Remove special characters and convert to lowercase
    normalized = re.sub(r'[^a-zA-Z0-9\s]', '', name).lower()
    # Replace spaces with underscores
    normalized = re.sub(r'\s+', '_', normalized)
    # Remove leading/trailing underscores
    normalized = normalized.strip('_')
    return normalized


def extract_sections(content):
    """Extract major sections from campaign markdown

    Returns dict with:
        - overview: Act overview content
        - quests: List of (quest_name, quest_content) tuples
        - locations: List of (location_name, location_content) tuples
        - npcs: List of (npc_name, npc_content) tuples
        - encounters: List of (encounter_name, encounter_content) tuples
    """
    sections = {
        'overview': None,
        'quests': [],
        'locations': [],
        'npcs': [],
        'encounters': [],
        'items': [],
        'misc': []
    }

    # Split by major headers (## or ###)
    # This is a simplified parser - real implementation should be more robust
    header_pattern = re.compile(r'^(#{2,3})\s+(.+)$', re.MULTILINE)

    # Find all headers
    headers = []
    for match in header_pattern.finditer(content):
        level = len(match.group(1))
        title = match.group(2).strip()
        position = match.start()
        headers.append((position, level, title))

    # Extract content between headers
    for i, (pos, level, title) in enumerate(headers):
        # Find next header of same or higher level
        next_pos = len(content)
        for next_p, next_l, next_t in headers[i+1:]:
            if next_l <= level:
                next_pos = next_p
                break

        section_content = content[pos:next_pos].strip()

        # Categorize based on title keywords
        title_lower = title.lower()

        if 'overview' in title_lower or 'introduction' in title_lower or title_lower.startswith('act'):
            sections['overview'] = (title, section_content)

        elif 'quest' in title_lower or 'main quest' in title_lower or 'side quest' in title_lower or title.startswith('MQ') or title.startswith('SQ'):
            sections['quests'].append((title, section_content))

        elif 'location' in title_lower or 'district' in title_lower or 'street' in title_lower or 'quarter' in title_lower:
            sections['locations'].append((title, section_content))

        elif 'npc' in title_lower or 'character:' in title_lower or any(keyword in title_lower for keyword in ['priestess', 'ghost', 'merchant', 'companion', 'drow', 'dwarf']):
            sections['npcs'].append((title, section_content))

        elif 'encounter' in title_lower or 'combat' in title_lower or 'patrol' in title_lower or 'ambush' in title_lower:
            sections['encounters'].append((title, section_content))

        elif 'item' in title_lower or 'loot' in title_lower or 'treasure' in title_lower or 'artifact' in title_lower:
            sections['items'].append((title, section_content))

        else:
            sections['misc'].append((title, section_content))

    return sections


def generate_master_index(sections, act_name):
    """Generate the [MASTER_INDEX] for the vault"""
    index_lines = ["[MASTER_INDEX]"]

    # Overview
    if sections['overview']:
        title, _ = sections['overview']
        module_id = f"_{normalize_id(act_name)}_overview"
        index_lines.append("overview:")
        index_lines.append(f"  - {module_id}")
        index_lines.append("")

    # Quests
    if sections['quests']:
        index_lines.append("main_quests:")
        for title, _ in sections['quests']:
            if 'main quest' in title.lower() or title.startswith('MQ'):
                module_id = f"quest_{normalize_id(title)}"
                index_lines.append(f"  - {module_id}")
        index_lines.append("")

        index_lines.append("side_quests:")
        for title, _ in sections['quests']:
            if 'side quest' in title.lower() or title.startswith('SQ'):
                module_id = f"quest_{normalize_id(title)}"
                index_lines.append(f"  - {module_id}")
        index_lines.append("")

    # Locations
    if sections['locations']:
        index_lines.append("locations:")
        for title, _ in sections['locations']:
            module_id = f"loc_{normalize_id(title)}"
            index_lines.append(f"  - {module_id}")
        index_lines.append("")

    # NPCs
    if sections['npcs']:
        index_lines.append("npcs:")
        for title, _ in sections['npcs']:
            module_id = f"npc_{normalize_id(title)}"
            index_lines.append(f"  - {module_id}")
        index_lines.append("")

    # Encounters
    if sections['encounters']:
        index_lines.append("encounters:")
        for title, _ in sections['encounters']:
            module_id = f"enc_{normalize_id(title)}"
            index_lines.append(f"  - {module_id}")
        index_lines.append("")

    # Items
    if sections['items']:
        index_lines.append("items:")
        for title, _ in sections['items']:
            module_id = f"item_{normalize_id(title)}"
            index_lines.append(f"  - {module_id}")
        index_lines.append("")

    return '\n'.join(index_lines)


def wrap_module(module_id, content):
    """Wrap content with [MODULE_START/END] tags"""
    return f"""[MODULE_START: {module_id}]
{content}
[MODULE_END: {module_id}]"""


def create_campaign_vault(input_file, output_file=None):
    """Main conversion function"""
    print("=" * 60)
    print("D&D 5E Orchestrator v2.0 - Campaign Vault Generator")
    print("=" * 60)
    print()

    # Validate input file
    if not os.path.exists(input_file):
        print(f"ERROR: Input file not found: {input_file}")
        return False

    # Determine output filename
    if output_file is None:
        input_path = Path(input_file)
        # Replace .md with _Data_Vault.md
        output_file = str(input_path.parent / f"{input_path.stem}_Data_Vault.md")

    print(f"Input:  {input_file}")
    print(f"Output: {output_file}")
    print()

    # Read input
    print("Reading campaign file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    input_size_kb = len(content.encode('utf-8')) / 1024
    print(f"  Input size: {input_size_kb:.1f} KB")
    print()

    # Extract act name from filename or content
    input_filename = Path(input_file).stem
    act_name = input_filename  # e.g., "Act_2_The_Dead_City"

    # Parse content into sections
    print("Parsing campaign content...")
    sections = extract_sections(content)

    print(f"  Overview sections: {1 if sections['overview'] else 0}")
    print(f"  Quests: {len(sections['quests'])}")
    print(f"  Locations: {len(sections['locations'])}")
    print(f"  NPCs: {len(sections['npcs'])}")
    print(f"  Encounters: {len(sections['encounters'])}")
    print(f"  Items: {len(sections['items'])}")
    print(f"  Misc sections: {len(sections['misc'])}")
    print()

    # Build vault content
    print("Building Campaign Data Vault...")
    vault_lines = []

    # Header
    vault_lines.append(f"# CAMPAIGN DATA VAULT: {act_name.replace('_', ' ')}")
    vault_lines.append("")
    vault_lines.append("**DO NOT EDIT DURING SESSION** - This is a read-only reference file for the AI Orchestrator")
    vault_lines.append("")
    vault_lines.append("**PURPOSE**: Contains all campaign-specific content (NPCs, locations, quests, loot) in indexed, retrievable format")
    vault_lines.append("")
    vault_lines.append(f"**GENERATED**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    vault_lines.append("")
    vault_lines.append("---")
    vault_lines.append("")

    # Master Index
    master_index = generate_master_index(sections, act_name)
    vault_lines.append(master_index)
    vault_lines.append("")
    vault_lines.append("---")
    vault_lines.append("")

    # Overview
    if sections['overview']:
        title, content = sections['overview']
        module_id = f"_{normalize_id(act_name)}_overview"
        vault_lines.append(wrap_module(module_id, content))
        vault_lines.append("")
        vault_lines.append("---")
        vault_lines.append("")
        print(f"  ✓ Overview: {module_id}")

    # Quests
    for title, content in sections['quests']:
        module_id = f"quest_{normalize_id(title)}"
        vault_lines.append(wrap_module(module_id, content))
        vault_lines.append("")
        vault_lines.append("---")
        vault_lines.append("")
        print(f"  ✓ Quest: {module_id}")

    # Locations
    for title, content in sections['locations']:
        module_id = f"loc_{normalize_id(title)}"
        vault_lines.append(wrap_module(module_id, content))
        vault_lines.append("")
        vault_lines.append("---")
        vault_lines.append("")
        print(f"  ✓ Location: {module_id}")

    # NPCs
    for title, content in sections['npcs']:
        module_id = f"npc_{normalize_id(title)}"
        vault_lines.append(wrap_module(module_id, content))
        vault_lines.append("")
        vault_lines.append("---")
        vault_lines.append("")
        print(f"  ✓ NPC: {module_id}")

    # Encounters
    for title, content in sections['encounters']:
        module_id = f"enc_{normalize_id(title)}"
        vault_lines.append(wrap_module(module_id, content))
        vault_lines.append("")
        vault_lines.append("---")
        vault_lines.append("")
        print(f"  ✓ Encounter: {module_id}")

    # Items
    for title, content in sections['items']:
        module_id = f"item_{normalize_id(title)}"
        vault_lines.append(wrap_module(module_id, content))
        vault_lines.append("")
        vault_lines.append("---")
        vault_lines.append("")
        print(f"  ✓ Item: {module_id}")

    # Misc (if any - these might need manual categorization)
    if sections['misc']:
        print()
        print("  ⚠️  Uncategorized sections found:")
        for title, content in sections['misc']:
            module_id = f"misc_{normalize_id(title)}"
            vault_lines.append(wrap_module(module_id, content))
            vault_lines.append("")
            vault_lines.append("---")
            vault_lines.append("")
            print(f"      - {title} → {module_id}")
        print("      (These may need manual review and re-categorization)")

    # Footer
    vault_lines.append("")
    vault_lines.append("## END OF CAMPAIGN DATA VAULT")

    # Write output
    print()
    print(f"Writing to: {output_file}")
    vault_text = '\n'.join(vault_lines)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(vault_text)

    output_size_kb = len(vault_text.encode('utf-8')) / 1024
    module_count = vault_text.count('[MODULE_START:')

    print()
    print("=" * 60)
    print("Vault Generation Complete!")
    print("=" * 60)
    print(f"Output file: {output_file}")
    print(f"Output size: {output_size_kb:.1f} KB")
    print(f"Total modules: {module_count}")
    print()

    print("Next steps:")
    print("1. Review the generated vault for correct categorization")
    print("2. Manually edit module IDs if needed (e.g., rename npc_xyz)")
    print("3. Add any missing modules (items, custom mechanics, etc.)")
    print("4. Update [MASTER_INDEX] to match any changes")
    print("5. Test with Kernel and Protocol Library")
    print()
    print("Verification commands:")
    print(f"  grep -c '\\[MODULE_START:' {output_file}   # Count modules")
    print(f"  grep '\\[MODULE_START:' {output_file}        # List all module IDs")

    return True


def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python create_campaign_vault.py <input_campaign.md> [output_vault.md]")
        print()
        print("Example:")
        print('  python create_campaign_vault.py "../../campaigns/Descent into Khar-Morkai/Act_2_The_Dead_City.md"')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    success = create_campaign_vault(input_file, output_file)

    if success:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
