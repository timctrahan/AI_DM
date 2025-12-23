#!/usr/bin/env python3
"""
Automated removal of context management features from LEAN orchestrator parts.
Removes: Rest_Refresh_Protocol, Hub_Entry_Protocol, Context_Confidence_Check,
         refresh_state schema, ability reviews, and all protocol calls.
"""

import re
import os

def remove_between_markers(content, start_marker, end_marker, include_end=True):
    """Remove text between two markers (inclusive)"""
    pattern = re.escape(start_marker) + r'.*?' + re.escape(end_marker)
    if include_end:
        # Remove including end marker
        return re.sub(pattern, '', content, flags=re.DOTALL)
    else:
        # Remove up to but not including end marker
        pattern = re.escape(start_marker) + r'.*?(?=' + re.escape(end_marker) + r')'
        return re.sub(pattern, '', content, flags=re.DOTALL)

def remove_lines_containing(content, pattern):
    """Remove entire lines that contain the pattern"""
    lines = content.split('\n')
    filtered = [line for line in lines if pattern not in line]
    return '\n'.join(filtered)

def clean_part1_foundation():
    """Remove context management protocols from Part 1"""
    filepath = "DND_ORCH_PART1_Foundation.md"
    print(f"\n[PART 1] Processing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_lines = len(content.split('\n'))

    # 1. Update execution loop (remove [AMBIENT CONTEXT WEAVING] step)
    print("  - Updating execution loop...")
    content = content.replace(
        'GUARD → RECEIVE → TRANSLATE → VALIDATE → EXECUTE → UPDATE → VALIDATE → CHECKPOINT → [AMBIENT CONTEXT WEAVING] → NARRATE → PRESENT → ⛔ STOP → AWAIT',
        'GUARD → RECEIVE → TRANSLATE → VALIDATE → EXECUTE → UPDATE → VALIDATE → CHECKPOINT → NARRATE → PRESENT → ⛔ STOP → AWAIT'
    )

    # 2. Remove Hub_Entry_Protocol
    print("  - Removing Hub_Entry_Protocol...")
    content = remove_between_markers(
        content,
        '## PROTOCOL: Hub_Entry_Protocol',
        '## PROTOCOL: Rest_Refresh_Protocol'
    )

    # 3. Remove Rest_Refresh_Protocol
    print("  - Removing Rest_Refresh_Protocol...")
    content = remove_between_markers(
        content,
        '## PROTOCOL: Rest_Refresh_Protocol',
        '## PROTOCOL: Context_Confidence_Check'
    )

    # 4. Remove Context_Confidence_Check
    print("  - Removing Context_Confidence_Check...")
    # Find the end marker for this protocol (next section header)
    content = remove_between_markers(
        content,
        '## PROTOCOL: Context_Confidence_Check',
        '---\n\n# SECTION'
    )

    # 5. Remove refresh_state from Party_State_Schema_v2
    print("  - Removing refresh_state from schema...")
    content = remove_lines_containing(content, 'refresh_state:')

    # Clean up any double blank lines or extra separators
    content = re.sub(r'\n\n\n+', '\n\n', content)
    content = re.sub(r'---\n\n---', '---', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    new_lines = len(content.split('\n'))
    print(f"  [OK] Removed {original_lines - new_lines} lines (from {original_lines} to {new_lines})")

def clean_part3_gameloop():
    """Remove ability reviews and protocol calls from Part 3"""
    filepath = "DND_ORCH_PART3_GameLoop.md"
    print(f"\n[PART 3] Processing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_lines = len(content.split('\n'))

    # 1. Remove Context_Confidence_Check call in Movement (around line 136)
    print("  - Removing Context_Confidence_Check call from Movement...")
    content = remove_lines_containing(content, 'CALL: Context_Confidence_Check WITH data_type="location"')

    # 2. Remove Hub_Entry_Protocol call in Movement (around line 141)
    print("  - Removing Hub_Entry_Protocol call from Movement...")
    content = remove_lines_containing(content, 'IF destination.is_hub OR destination.is_town:')
    content = remove_lines_containing(content, 'CALL: Hub_Entry_Protocol WITH destination')

    # 3. Remove Context_Confidence_Check call in NPC_Interaction (around line 210)
    print("  - Removing Context_Confidence_Check call from NPC_Interaction...")
    content = remove_lines_containing(content, 'CALL: Context_Confidence_Check WITH data_type="npc"')

    # 4. Remove Short_Rest ability review section (step 4, lines 503-521)
    print("  - Removing Short_Rest ability review...")
    # Find the ability review section in Short_Rest_Protocol
    content = remove_between_markers(
        content,
        '4. FOR character IN party_state.characters:\n     a. CALC: ability_index = rest_count % 4',
        '\n5. CALL: Time_Tracking_Protocol WITH minutes_to_add=60'
    )

    # Fix step numbering in Short_Rest after removal
    content = content.replace(
        '5. CALL: Time_Tracking_Protocol WITH minutes_to_add=60\n6. OUT: "=== Short Rest Complete ==="\n7. CALL: Rest_Refresh_Protocol WITH rest_type="short"\n8. UPDATE: party_state\n9. RETURN',
        '4. CALL: Time_Tracking_Protocol WITH minutes_to_add=60\n5. OUT: "=== Short Rest Complete ==="\n6. UPDATE: party_state\n7. RETURN'
    )

    # Remove Rest_Refresh_Protocol call from Short_Rest
    content = remove_lines_containing(content, 'CALL: Rest_Refresh_Protocol WITH rest_type="short"')

    # 5. Remove Long_Rest ability review section (step 5, lines 583-607)
    print("  - Removing Long_Rest IMMUTABLE OUTPUT RULES and ability review...")
    # Remove IMMUTABLE OUTPUT RULES
    content = remove_between_markers(
        content,
        '**IMMUTABLE OUTPUT RULES**:\n1. **MANDATORY ABILITY REVIEW**',
        '\n**PROCEDURE**:\n```'
    )

    # Remove the ability review step
    content = remove_between_markers(
        content,
        '5. 🧠 SPELL & ABILITY REVIEW (MANDATORY):',
        '\n6. FINALIZE:'
    )

    # Fix step numbering in Long_Rest after removal
    content = content.replace('6. FINALIZE:', '5. FINALIZE:')
    content = content.replace(
        '5. FINALIZE:\n   CALL: Time_Tracking_Protocol WITH minutes_to_add=480\n   OUT: "=== Long Rest Complete ==="\n   CALL: Rest_Refresh_Protocol WITH rest_type="long"',
        '5. FINALIZE:\n   CALL: Time_Tracking_Protocol WITH minutes_to_add=480\n   OUT: "=== Long Rest Complete ==="'
    )

    # Remove Rest_Refresh_Protocol call from Long_Rest
    content = remove_lines_containing(content, 'CALL: Rest_Refresh_Protocol WITH rest_type="long"')

    # Clean up any double blank lines
    content = re.sub(r'\n\n\n+', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    new_lines = len(content.split('\n'))
    print(f"  [OK] Removed {original_lines - new_lines} lines (from {original_lines} to {new_lines})")

def clean_part6_closing():
    """Remove refresh_state from save output in Part 6"""
    filepath = "DND_ORCH_PART6_Closing.md"
    print(f"\n[PART 6] Processing {filepath}...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_lines = len(content.split('\n'))

    # Remove the Refresh State section from save output (lines 209-213)
    print("  - Removing refresh_state from save output...")
    content = remove_between_markers(
        content,
        'Refresh State (Context Rotation):',
        '\nImmediate Situation:'
    )

    # Clean up any double blank lines
    content = re.sub(r'\n\n\n+', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    new_lines = len(content.split('\n'))
    print(f"  [OK] Removed {original_lines - new_lines} lines (from {original_lines} to {new_lines})")

def main():
    """Execute all cleanup operations"""
    print("=" * 60)
    print("LEAN Orchestrator - Context Management Removal Script")
    print("=" * 60)

    # Check we're in the right directory
    if not os.path.exists("DND_ORCH_PART1_Foundation.md"):
        print("\n[ERROR] Must run from agent_parts_lean/ directory")
        print("   Current directory:", os.getcwd())
        return 1

    print("\nRemoving context management features from LEAN version...")

    # Process each part
    clean_part1_foundation()
    clean_part3_gameloop()
    clean_part6_closing()

    print("\n" + "=" * 60)
    print("[SUCCESS] All context management features removed!")
    print("=" * 60)
    print("\nNext steps:")
    print("  1. Review changes: git diff (if using git)")
    print("  2. Build LEAN orchestrator: python assemble_orchestrator_lean.py")
    print("  3. Verify size reduction (~37-42KB expected)")

    return 0

if __name__ == "__main__":
    exit(main())
