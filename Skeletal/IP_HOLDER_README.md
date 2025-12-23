# Skeletal DM Campaign Encryption Tools - IP Holder Guide

## Overview

These tools allow you (the IP holder) to encrypt Skeletal DM campaigns for distribution to purchasers.

## Files

1. **encrypt_campaign.py** - Main encryption tool
2. **generate_email_templates.py** - Email template generator
3. **license_records.json** - Automatic license tracking (created by encrypt_campaign.py)

## Quick Start

### Encrypt a Campaign

```bash
python encrypt_campaign.py CAMPAIGN_MyAdventure.md purchaser@email.com
```

**Output:**
- Encrypted campaign file: `CAMPAIGN_MyAdventure_ENCRYPTED.md`
- License key: (displayed on screen, also saved to license_records.json)
- License record: Added to `license_records.json`

### Generate Email Templates

```bash
python generate_email_templates.py
```

This interactive tool will:
1. Show you recent license records
2. Let you select one
3. Generate appropriate email templates
4. Optionally save templates to files

## Workflow

### For Each Purchase:

1. **Encrypt the campaign**
   ```bash
   python encrypt_campaign.py CAMPAIGN_Shadows.md user@example.com
   ```
   
2. **Note the output:**
   - Encrypted file: `CAMPAIGN_Shadows_ENCRYPTED.md`
   - License key: `c092bab5e8c37aa2` (example)

3. **Send to purchaser:**
   - **Email 1**: Encrypted campaign file (attachment)
   - **Email 2**: License key (separate email for security)
   
   OR use `generate_email_templates.py` to create formatted emails

4. **Archive:**
   - Keep `license_records.json` backed up
   - Optionally keep encrypted files for re-distribution if needed

## How It Works

### License Key Generation

License keys are generated using:
```
SHA256(campaign_name + purchaser_email + timestamp)[:16]
```

This ensures:
- ✅ Unique key per purchase
- ✅ Tied to specific purchaser
- ✅ Reproducible if needed (with same timestamp)
- ✅ 16 hex characters (compatible with encryption)

### Encryption

- **Algorithm**: XOR cipher with Base64 encoding
- **Purpose**: License compliance (not cryptographic security)
- **Key length**: 8 bytes (16 hex characters)
- **Speed**: < 1 second encryption/decryption

### License Records

`license_records.json` tracks all generated licenses:

```json
[
  {
    "campaign": "SHADOWS OF THE UNDERDARK",
    "purchaser": "user@example.com",
    "license_key": "c092bab5e8c37aa2",
    "encrypted_file": "CAMPAIGN_Shadows_ENCRYPTED.md",
    "generated_at": "2025-12-23T02:25:24.710910",
    "status": "active"
  }
]
```

**Keep this file secure and backed up!**

## Advanced Usage

### Batch Processing

```bash
# Encrypt multiple campaigns for the same purchaser
for campaign in CAMPAIGN_*.md; do
    python encrypt_campaign.py "$campaign" user@example.com
done
```

### Custom Metadata

The tool automatically extracts metadata from campaign files:
- Campaign name (from `campaign_name:` field)
- Version (from `version:` field)
- Level range (from text like "3 → 8" or "3-8")
- Acts (from `acts:` field)

Ensure your campaign files have this metadata for best results.

### Re-sending Lost Keys

If a purchaser loses their key:

1. Check `license_records.json` for their email
2. Find their license key
3. Re-send using the email template generator

## Security Notes

### What This Protects:
- ✅ Casual redistribution (file is encrypted)
- ✅ Accidental sharing (clearly marked as licensed)
- ✅ License awareness (users know it's paid content)

### What This Does NOT Protect:
- ❌ Determined attackers (XOR is not cryptographically secure)
- ❌ Key sharing (users can share keys with friends)
- ❌ Redistribution of decrypted content

### Best Practices:
- Always send key in separate email from file
- Track licenses in `license_records.json`
- Back up license records regularly
- Consider watermarking campaigns with purchaser info
- Monitor for unauthorized distribution

## Email Templates

### Recommended: Two-Email Approach

**Email 1 (with encrypted file attachment):**
```
Subject: Your Skeletal DM Campaign: [Campaign Name]

Hi [Name],

Your encrypted campaign is attached!
You'll receive your license key in a separate email shortly.
```

**Email 2 (with license key):**
```
Subject: License Key for [Campaign Name]

Hi [Name],

Your license key: [KEY]

Keep this secure - you'll need it to decrypt your campaign.
```

**Benefit**: More secure, prevents key leakage if file is forwarded

### Alternative: Single-Email Approach

Use `generate_email_templates.py` option 3 for a combined email.

**Benefit**: Simpler for purchaser, one email to manage
**Drawback**: Less secure if email is forwarded

## Troubleshooting

### "Campaign metadata not found"
- Ensure campaign file has proper YAML metadata
- Check for `campaign_name:`, `version:`, etc. in first 50 lines

### "Encryption failed"
- Verify campaign file is valid UTF-8
- Check file exists and is readable

### "License key doesn't work"
- Verify you sent the correct key from `license_records.json`
- Check for typos (keys are case-insensitive)
- Ensure purchaser is using the correct encrypted file

## File Structure

```
your-campaigns/
├── encrypt_campaign.py              # Main tool
├── generate_email_templates.py      # Email generator
├── license_records.json             # License tracking (auto-created)
├── CAMPAIGN_Original.md             # Your source campaigns
├── CAMPAIGN_Original_ENCRYPTED.md   # Encrypted outputs
└── backups/                         # Backup license_records.json here!
```

## Support Workflow

When a purchaser contacts you:

1. **Lost license key**
   - Check `license_records.json`
   - Verify purchase via email
   - Re-send key using email template

2. **Can't decrypt**
   - Verify they have correct encrypted file
   - Verify license key is correct
   - Check they're using compatible AI (Claude, GPT, etc.)

3. **Wants refund/replacement**
   - Update status in `license_records.json` to "refunded" or "replaced"
   - Issue new license if replacement

## Backup Strategy

**Critical files to backup:**
- `license_records.json` - Contains all license keys
- Original campaign files (`.md` source files)
- Encrypted campaign files (for re-distribution)

**Recommended:**
- Daily backup of `license_records.json`
- Version control for campaign source files
- Cloud backup of encrypted distribution files

## Future Enhancements

Possible improvements:
- Online license validation API
- Automatic email sending integration
- Batch encryption UI
- License revocation system
- Analytics dashboard
- Watermarking with purchaser info

## Questions?

This is a complete IP holder toolkit for:
- ✅ Encrypting campaigns
- ✅ Generating unique license keys
- ✅ Tracking all sales
- ✅ Creating customer emails
- ✅ Managing support requests

All with simple command-line tools and automatic record-keeping.
