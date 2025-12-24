#!/usr/bin/env python3
"""
Skeletal DM Campaign Encryption Tool v1.5
For IP holders to encrypt campaigns for distribution

Version 1.5 Changes:
- EMBEDDED LICENSE KEY in campaign header (no separate key entry needed)
- Campaign header prompts user to upload kernel
- Supports both single-turn and two-turn workflows

Version 1.4 Changes:
- Added ENCRYPTED_DATA_LINES specification for unambiguous extraction
- Line range (e.g., "15-350") added to header for fast, robust decryption

Usage: python encrypt_campaign.py campaign_file.md purchaser_email [kernel_files...]
"""

import base64
import sys
import hashlib
import json
from itertools import cycle
from datetime import datetime
from pathlib import Path


def generate_license_key(campaign_name: str, purchaser_email: str, salt: str = None) -> str:
    """
    Generate a unique license key based on campaign and purchaser
    
    Args:
        campaign_name: Name of the campaign
        purchaser_email: Email address of purchaser
        salt: Optional salt for key generation (uses timestamp if not provided)
    
    Returns:
        16-character hexadecimal license key
    """
    if salt is None:
        salt = datetime.now().isoformat()
    
    # Create unique string from campaign + email + salt
    unique_string = f"{campaign_name}|{purchaser_email}|{salt}"
    
    # Hash it
    hash_obj = hashlib.sha256(unique_string.encode('utf-8'))
    hash_hex = hash_obj.hexdigest()
    
    # Take first 16 characters as the key
    license_key = hash_hex[:16]
    
    return license_key


def encrypt_campaign(campaign_text: str, license_key: str, kernel_hash: str = None) -> tuple:
    """
    Encrypt campaign using XOR + Base64
    
    Args:
        campaign_text: Plain text campaign content
        license_key: 16-character hex license key
        kernel_hash: MD5 hash of required kernel (optional)
    
    Returns:
        Tuple of (base64 encoded encrypted data, modified campaign text with hash)
    """
    # Remove any existing kernel validation block from campaign
    import re
    kernel_block_pattern = r'# KERNEL_VALIDATION_CHECK.*?# ---------------------------------------------------------------------------\s*\n'
    campaign_text_cleaned = re.sub(kernel_block_pattern, '', campaign_text, flags=re.DOTALL)
    
    # Inject kernel hash requirement into campaign if provided
    if kernel_hash:
        kernel_check = f'''# KERNEL_VALIDATION_CHECK
# This campaign requires a specific kernel version
# DO NOT MODIFY THIS SECTION
REQUIRED_KERNEL_HASH: "{kernel_hash}"
# If the loaded kernel's MD5 hash does not match, refuse to run campaign
# Agent: calculate MD5 of kernel file and compare before executing campaign
# ---------------------------------------------------------------------------

'''
        modified_campaign = kernel_check + campaign_text_cleaned
    else:
        modified_campaign = campaign_text_cleaned
    
    # Convert key to bytes
    key_bytes = bytes.fromhex(license_key)
    
    # Encrypt using XOR
    campaign_bytes = modified_campaign.encode('utf-8')
    encrypted = bytes(a ^ b for a, b in zip(campaign_bytes, cycle(key_bytes)))
    
    # Base64 encode
    encoded = base64.b64encode(encrypted).decode('ascii')
    
    return encoded, modified_campaign


def create_encrypted_file(campaign_name: str, campaign_version: str, 
                         level_range: str, acts: int, 
                         encrypted_data: str, license_key: str,
                         kernel_hash: str = None) -> str:
    """
    Create the complete encrypted campaign file with embedded license key
    v1.5: License key embedded in header, campaign prompts for kernel upload
    
    Args:
        campaign_name: Campaign title
        campaign_version: Version number
        level_range: Level range (e.g., "3-8")
        acts: Number of acts
        encrypted_data: Base64 encoded encrypted campaign
        license_key: 16-character hex license key (will be embedded)
        kernel_hash: Not used in this version (kept for compatibility)
    
    Returns:
        Complete encrypted file content
    """
    # Split into 80-character lines
    lines = [encrypted_data[i:i+80] for i in range(0, len(encrypted_data), 80)]
    
    # Calculate line range
    first_data_line = 15  # Adjusted for new header with embedded key
    last_data_line = 15 + len(lines) - 1
    
    # Create file with embedded license key
    file_content = f'''# SKELETAL_DM_ENCRYPTED_CAMPAIGN_V4
# ===========================================================================
# CAMPAIGN: {campaign_name}
# VERSION: {campaign_version} | LEVELS: {level_range} | ACTS: {acts}
# ===========================================================================
# 
# AI AGENT INSTRUCTIONS:
# This is an encrypted campaign file with an embedded decryption key.
# 
# OUTPUT EXACTLY:
#   "✓ ENCRYPTED CAMPAIGN LOADED: {campaign_name}"
#   "Upload SKELETAL_DM_KERNEL to decrypt and begin."
#   "⛔"
# 
# Then HALT and WAIT for kernel file upload.
# ===========================================================================
# ENCRYPTION: base64(xor(plaintext_utf8, key_bytes))
# KEY_FORMAT: hex16 (16 hex chars => 8 bytes)
# LICENSE_KEY: {license_key}
# ENCRYPTED_DATA_LINES: {first_data_line}-{last_data_line}
# ===========================================================================

===BEGIN_ENCRYPTED_CAMPAIGN_DATA===
{chr(10).join(lines)}
===END_ENCRYPTED_CAMPAIGN_DATA===

# SKELETAL_DM_ENCRYPTED_CAMPAIGN_END
'''
    
    return file_content


def extract_campaign_metadata(campaign_content: str) -> dict:
    """
    Extract metadata from campaign file
    
    Args:
        campaign_content: Plain campaign text
    
    Returns:
        Dictionary with campaign metadata
    """
    metadata = {
        'title': 'Unknown Campaign',
        'version': '1.0',
        'level_range': '1-10',
        'acts': 1
    }
    
    # Try to extract from YAML front matter
    lines = campaign_content.splitlines()
    
    for line in lines[:50]:  # Check first 50 lines
        if 'campaign_name:' in line.lower():
            metadata['title'] = line.split(':', 1)[1].strip().strip('"')
        elif 'version:' in line.lower() and 'kernel' not in line.lower():
            metadata['version'] = line.split(':', 1)[1].strip().strip('"')
        elif 'level' in line.lower() and 'range' in line.lower():
            # Try to extract level range
            import re
            match = re.search(r'(\d+)\s*[→-]\s*(\d+)', line)
            if match:
                metadata['level_range'] = f"{match.group(1)}-{match.group(2)}"
        elif 'acts:' in line.lower():
            try:
                metadata['acts'] = int(line.split(':', 1)[1].strip())
            except:
                pass
    
    return metadata


def save_license_record(campaign_name: str, purchaser_email: str, 
                        license_key: str, output_file: str, kernel_hash: str = None):
    """
    Save license record to JSON file for tracking
    
    Args:
        campaign_name: Campaign name
        purchaser_email: Purchaser email
        license_key: Generated license key
        output_file: Encrypted campaign filename
        kernel_hash: MD5 hash of required kernel
    """
    record = {
        'campaign': campaign_name,
        'purchaser': purchaser_email,
        'license_key': license_key,
        'encrypted_file': output_file,
        'kernel_hash': kernel_hash,
        'generated_at': datetime.now().isoformat(),
        'status': 'active'
    }
    
    # Load existing records
    records_file = Path('license_records.json')
    if records_file.exists():
        with open(records_file, 'r') as f:
            records = json.load(f)
    else:
        records = []
    
    # Add new record
    records.append(record)
    
    # Save
    with open(records_file, 'w') as f:
        json.dump(records, f, indent=2)
    
    return records_file


def main():
    """Main encryption workflow"""
    
    if len(sys.argv) < 3:
        print("Skeletal DM Campaign Encryption Tool v1.5")
        print("=" * 60)
        print()
        print("Usage: python encrypt_campaign.py campaign_file.md purchaser_email [kernel_files...]")
        print()
        print("Arguments:")
        print("  campaign_file.md  - Campaign file to encrypt")
        print("  purchaser_email   - Email address of purchaser")
        print("  kernel_files...   - (Optional) One or more kernel files for validation")
        print()
        print("Examples:")
        print("  python encrypt_campaign.py CAMPAIGN_Shadows.md user@example.com")
        print("  python encrypt_campaign.py CAMPAIGN_Shadows.md user@example.com KERNEL_v1.md")
        print()
        print("Features:")
        print("  - License key automatically embedded in campaign file")
        print("  - No separate key delivery needed")
        print("  - Supports two-turn workflow (campaign first, then kernel)")
        print()
        sys.exit(1)
    
    campaign_file = sys.argv[1]
    purchaser_email = sys.argv[2]
    
    # Optional: kernel file path(s)
    kernel_files = []
    if len(sys.argv) > 3:
        if ',' in sys.argv[3]:
            kernel_files = [f.strip() for f in sys.argv[3].split(',')]
        else:
            kernel_files = sys.argv[3:]
    
    # Read campaign file
    print(f"📁 Reading campaign file: {campaign_file}")
    try:
        with open(campaign_file, 'r', encoding='utf-8') as f:
            campaign_content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{campaign_file}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        sys.exit(1)
    
    print(f"   Campaign size: {len(campaign_content):,} characters")
    
    # Calculate kernel hashes if kernel files provided
    kernel_hashes = []
    if kernel_files:
        print(f"🔒 Reading kernel file(s): {len(kernel_files)} file(s)")
        for kernel_file in kernel_files:
            try:
                with open(kernel_file, 'r', encoding='utf-8') as f:
                    kernel_content = f.read()
                kernel_hash = hashlib.md5(kernel_content.encode('utf-8')).hexdigest()
                kernel_hashes.append(kernel_hash)
                print(f"   ✓ {kernel_file}: {kernel_hash}")
            except FileNotFoundError:
                print(f"   ⚠️  Warning: Kernel file '{kernel_file}' not found - skipping")
            except Exception as e:
                print(f"   ⚠️  Warning: Could not read '{kernel_file}': {e} - skipping")
        
        if kernel_hashes:
            print(f"   ⚠️  Campaign will ONLY work with these {len(kernel_hashes)} kernel version(s)!")
    
    # Extract metadata
    print("🔍 Extracting campaign metadata...")
    metadata = extract_campaign_metadata(campaign_content)
    print(f"   Title: {metadata['title']}")
    print(f"   Version: {metadata['version']}")
    print(f"   Levels: {metadata['level_range']}")
    print(f"   Acts: {metadata['acts']}")
    
    # Generate license key
    print(f"🔑 Generating license key for: {purchaser_email}")
    license_key = generate_license_key(metadata['title'], purchaser_email)
    print(f"   License key: {license_key}")
    print(f"   ✓ Key will be EMBEDDED in campaign file")
    
    # Encrypt campaign
    print("🔒 Encrypting campaign...")
    kernel_hash_str = ','.join(kernel_hashes) if kernel_hashes else None
    encrypted_data, modified_campaign = encrypt_campaign(campaign_content, license_key, kernel_hash_str)
    print(f"   Encrypted size: {len(encrypted_data):,} characters (base64)")
    if kernel_hashes:
        print(f"   ✓ Kernel validation embedded ({len(kernel_hashes)} allowed version(s))")
    
    # Create encrypted file
    print("📝 Creating encrypted campaign file...")
    
    file_content = create_encrypted_file(
        metadata['title'],
        metadata['version'],
        metadata['level_range'],
        metadata['acts'],
        encrypted_data,
        license_key,
        kernel_hash_str
    )
    
    # Determine output filename
    input_path = Path(campaign_file)
    output_filename = input_path.stem + '_ENCRYPTED.md'
    
    # Save file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(file_content)
    
    print(f"   ✓ Created: {output_filename} ({len(file_content):,} bytes)")
    
    # Save license record
    print("💾 Saving license record...")
    records_file = save_license_record(
        metadata['title'],
        purchaser_email,
        license_key,
        output_filename,
        kernel_hash_str
    )
    print(f"   Records saved to: {records_file}")
    
    # Summary
    print()
    print("=" * 60)
    print("✅ Encryption Complete!")
    print("=" * 60)
    print()
    print(f"Encrypted file: {output_filename}")
    print(f"License key:    {license_key} (EMBEDDED in file)")
    print(f"Purchaser:      {purchaser_email}")
    if kernel_hashes:
        print(f"Kernel hashes:  {len(kernel_hashes)} allowed version(s)")
        for i, h in enumerate(kernel_hashes, 1):
            print(f"  {i}. {h}")
    print()
    print("Usage Instructions:")
    print(f"  1. Send {output_filename} to purchaser")
    print(f"  2. Purchaser uploads campaign file first")
    print(f"  3. Purchaser uploads kernel file second")
    print(f"  4. Kernel auto-decrypts using embedded key")
    print()
    print("⚠️  IMPORTANT:")
    print(f"  - License key is EMBEDDED - no separate delivery needed")
    print(f"  - Campaign must be uploaded BEFORE kernel")
    print(f"  - Keep license_records.json secure and backed up")
    print()


if __name__ == '__main__':
    main()
