#!/usr/bin/env python3
"""
Email Template Generator for Skeletal DM License Delivery

Generates email templates for sending encrypted campaigns and license keys
"""

def generate_campaign_email(campaign_name: str, purchaser_name: str, filename: str) -> str:
    """Generate email for sending encrypted campaign file"""
    return f"""Subject: Your Skeletal DM Campaign: {campaign_name}

Dear {purchaser_name},

Thank you for purchasing "{campaign_name}" for Skeletal DM!

Your encrypted campaign file is attached to this email:
📁 {filename}

IMPORTANT: You will receive your license key in a separate email for security purposes.

To use your campaign:
1. Wait for the license key email (arriving separately)
2. Upload the encrypted campaign file to your AI chat (Claude, etc.)
3. When prompted, enter your license key
4. The campaign will decrypt automatically and be ready to play!

System Requirements:
- Skeletal DM Kernel v1.0 (included with purchase or available separately)
- AI chat interface that supports file uploads (Claude, ChatGPT, etc.)

Need help?
- Documentation: [your support URL]
- Support email: [your support email]

Enjoy your adventure in {campaign_name}!

Best regards,
The Skeletal DM Team

---
This is a licensed product for single-user personal use only.
Redistribution or sharing is prohibited.
"""


def generate_license_key_email(campaign_name: str, purchaser_name: str, 
                               license_key: str, purchaser_email: str) -> str:
    """Generate email for sending license key"""
    return f"""Subject: License Key for {campaign_name}

Dear {purchaser_name},

This email contains your license key for "{campaign_name}".

🔑 Your License Key: {license_key}

IMPORTANT SECURITY INFORMATION:
- This key is unique to your purchase
- Keep it secure and do not share it
- You'll need this key to decrypt your campaign file
- If you lose this key, contact support with your order number

How to Use Your License Key:
1. Upload your encrypted campaign file to your AI chat
2. The AI will detect it's encrypted and prompt for your key
3. Enter: {license_key}
4. The campaign will decrypt and load automatically

Your Purchase Details:
- Campaign: {campaign_name}
- Licensed to: {purchaser_email}
- License type: Single-user personal use
- Purchase date: [PURCHASE_DATE]

Terms of Use:
✅ Use for your own D&D games
✅ Share with players in your game sessions
✅ Make personal backups

❌ Do not redistribute the campaign file
❌ Do not share your license key
❌ Do not use for commercial purposes

Questions or issues?
Contact support: [your support email]

Thank you for your purchase!

Best regards,
The Skeletal DM Team

---
Keep this email for your records.
This license key is valid for the lifetime of the product.
"""


def generate_combined_email(campaign_name: str, purchaser_name: str, 
                           filename: str, license_key: str, 
                           purchaser_email: str) -> str:
    """Generate single email with both file and key (less secure)"""
    return f"""Subject: Your Skeletal DM Campaign: {campaign_name}

Dear {purchaser_name},

Thank you for purchasing "{campaign_name}" for Skeletal DM!

📁 CAMPAIGN FILE (attached): {filename}
🔑 LICENSE KEY: {license_key}

Quick Start:
1. Upload the attached campaign file to your AI chat (Claude, etc.)
2. When prompted, enter your license key: {license_key}
3. The campaign will decrypt and load automatically!

Your Purchase Details:
- Campaign: {campaign_name}
- Licensed to: {purchaser_email}
- License type: Single-user personal use

IMPORTANT:
- Keep your license key secure
- Do not share the encrypted file or license key with others
- For personal use only

System Requirements:
- Skeletal DM Kernel v1.0
- AI chat interface with file upload support

Need help?
- Documentation: [your support URL]
- Support: [your support email]

Enjoy your adventure!

Best regards,
The Skeletal DM Team

---
Licensed for single-user personal use only.
"""


def main():
    """Interactive email template generator"""
    import sys
    import json
    
    print("Skeletal DM Email Template Generator")
    print("=" * 60)
    print()
    
    # Check for license records
    try:
        with open('license_records.json', 'r') as f:
            records = json.load(f)
    except FileNotFoundError:
        print("❌ No license_records.json found")
        print("   Run encrypt_campaign.py first to create licenses")
        sys.exit(1)
    
    if not records:
        print("❌ No license records found")
        sys.exit(1)
    
    # Show recent licenses
    print(f"Found {len(records)} license record(s)")
    print()
    
    for i, record in enumerate(records[-10:], 1):  # Show last 10
        print(f"{i}. {record['campaign']} - {record['purchaser']}")
        print(f"   Key: {record['license_key']}")
        print(f"   File: {record['encrypted_file']}")
        print(f"   Date: {record['generated_at'][:10]}")
        print()
    
    # Select record
    if len(records) == 1:
        selection = 0
    else:
        try:
            selection = int(input("Select record number (or 0 to cancel): ")) - 1
            if selection < 0 or selection >= len(records):
                print("Cancelled")
                sys.exit(0)
        except (ValueError, KeyboardInterrupt):
            print("\nCancelled")
            sys.exit(0)
    
    record = records[selection]
    
    # Get purchaser name
    purchaser_name = input(f"Purchaser name (default: {record['purchaser'].split('@')[0]}): ").strip()
    if not purchaser_name:
        purchaser_name = record['purchaser'].split('@')[0].title()
    
    # Choose email type
    print()
    print("Email type:")
    print("1. Campaign file email (separate from key)")
    print("2. License key email (separate from file)")
    print("3. Combined email (both file and key) - less secure")
    print()
    
    choice = input("Select (1-3): ").strip()
    
    print()
    print("=" * 60)
    
    if choice == '1':
        email = generate_campaign_email(
            record['campaign'],
            purchaser_name,
            record['encrypted_file']
        )
        print("CAMPAIGN FILE EMAIL")
    elif choice == '2':
        email = generate_license_key_email(
            record['campaign'],
            purchaser_name,
            record['license_key'],
            record['purchaser']
        )
        print("LICENSE KEY EMAIL")
    elif choice == '3':
        email = generate_combined_email(
            record['campaign'],
            purchaser_name,
            record['encrypted_file'],
            record['license_key'],
            record['purchaser']
        )
        print("COMBINED EMAIL")
    else:
        print("Invalid choice")
        sys.exit(1)
    
    print("=" * 60)
    print()
    print(email)
    print()
    
    # Save option
    save = input("Save to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"email_{record['purchaser'].replace('@', '_').replace('.', '_')}_{choice}.txt"
        with open(filename, 'w') as f:
            f.write(email)
        print(f"✓ Saved to {filename}")


if __name__ == '__main__':
    main()
