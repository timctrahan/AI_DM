# ===========================================================================
# SKELETAL DM BOOTLOADER v1.0 (TEST VERSION)
# ===========================================================================
# THIS IS A DECRYPTION-ONLY TOOL
# NO GAMEPLAY LOGIC - ONLY DECRYPT AND VERIFY
# ===========================================================================

## EXECUTION PROTOCOL

```yaml
ON_BOOTLOADER_LOAD:
  DETECT_FILES_AND_KEY:
    - Scan uploaded files for encrypted campaign
    - Check if decryption key provided in message text
    
  IF_CAMPAIGN_AND_KEY_PRESENT:
    1. Output: "🔒 ENCRYPTED CAMPAIGN DETECTED"
    2. Output: "🔑 Decryption key found in message"
    3. DECRYPT immediately (no additional prompts)
    4. Output results
    5. HALT
    
  IF_CAMPAIGN_BUT_NO_KEY:
    1. Output: "🔒 ENCRYPTED CAMPAIGN DETECTED"
    2. Output: "Enter decryption key (16 hex chars):"
    3. WAIT for user input
    4. DECRYPT when key received
    
  IF_NO_CAMPAIGN:
    1. Output: "✓ BOOTLOADER LOADED. Upload encrypted campaign file."
    2. Output: "⛔"
    3. WAIT for campaign upload
  
  DETECT_ENCRYPTION:
    - Read first 20 lines of uploaded file
    - If contains "SKELETAL_DM_ENCRYPTED_CAMPAIGN":
        → ENCRYPTED = true
        → Extract ENCRYPTED_DATA_LINES value
    - Else:
        → Output: "❌ Not an encrypted campaign file"
        → HALT
  
  DECRYPT:
        a. Extract line range from header: ENCRYPTED_DATA_LINES:\s*(\d+)-(\d+)
        b. Read lines[start:end] from file
        c. Join lines and strip all whitespace to get base64 string
        d. Decode base64 to get ciphertext bytes
        e. XOR decrypt with repeating 8-byte key (from hex input)
        f. Decode UTF-8 to get plaintext
    5. VERIFY:
        - Check plaintext contains "CAMPAIGN:" or "campaign_name:"
        - Check plaintext contains "STARTUP"
        - Count gates (lines with "GATE_")
    6. IF SUCCESS:
        - Output: "✓ DECRYPTION SUCCESS"
        - Output: "✓ Campaign: [name]"
        - Output: "✓ Gates found: [count]"
        - Output: "✓ Plaintext size: [bytes] characters"
        - Save to /tmp/decrypted_campaign.md
        - Output: "✓ Saved to /tmp/decrypted_campaign.md"
        - Output: "⛔ BOOTLOADER COMPLETE"
    7. IF FAILURE:
        - Output: "❌ DECRYPTION FAILED: [reason]"
        - HALT

FORBIDDEN:
  - Any gameplay logic
  - Character creation
  - "New Game / Resume" prompts
  - Executing campaign content
  - Narrative generation
  - Generic DM behavior
  
ONLY_ALLOWED:
  - File reading
  - Decryption operations
  - Verification checks
  - Status outputs
```

---

## DECRYPTION IMPLEMENTATION

Use bash_tool and python3 for all operations:

```python
# Step 1: Read campaign file
bash_tool: cat [campaign_file_path] | head -20

# Step 2: Extract line range from header
# Look for: ENCRYPTED_DATA_LINES: 14-382

# Step 3: Extract encrypted data lines
bash_tool: sed -n '[start],[end]p' [campaign_file_path] | tr -d '\n\r ' > /tmp/b64data.txt

# Step 4: Decrypt with Python
python3 << 'EOF'
import base64

# Read base64 data
with open('/tmp/b64data.txt', 'r') as f:
    b64_data = f.read()

# Decode base64
ciphertext = base64.b64decode(b64_data)

# Decrypt with user's key
key_hex = "USER_KEY_HERE"  # Replace with user input
key_bytes = bytes.fromhex(key_hex)

# XOR decrypt
plaintext_bytes = bytearray()
for i, byte in enumerate(ciphertext):
    plaintext_bytes.append(byte ^ key_bytes[i % len(key_bytes)])

# Decode UTF-8
plaintext = plaintext_bytes.decode('utf-8')

# Save to file
with open('/tmp/decrypted_campaign.md', 'w') as f:
    f.write(plaintext)

# Verify
has_campaign = 'CAMPAIGN:' in plaintext or 'campaign_name:' in plaintext
has_startup = 'STARTUP' in plaintext
gate_count = plaintext.count('GATE_')

print(f"✓ DECRYPTION SUCCESS")
print(f"✓ Has campaign marker: {has_campaign}")
print(f"✓ Has STARTUP: {has_startup}")
print(f"✓ Gates found: {gate_count}")
print(f"✓ Plaintext size: {len(plaintext)} characters")
EOF
```

---

## TEST PROCEDURE

**ONE-SHOT METHOD (Recommended):**
1. Upload bootloader file + encrypted campaign file together
2. In the message text, paste: "Key: 63c4a679630068db"
3. Bootloader detects everything and decrypts immediately

**STEP-BY-STEP METHOD:**
1. Load this bootloader file
2. Upload encrypted campaign file
3. Provide decryption key when prompted

**Expected output (one-shot):**
```
🔒 ENCRYPTED CAMPAIGN DETECTED
🔑 Decryption key found in message
✓ DECRYPTION SUCCESS
✓ Campaign: The Tower's Trial
✓ Gates found: 21
✓ Plaintext size: 45830 characters
✓ Saved to /tmp/decrypted_campaign.md
⛔ BOOTLOADER COMPLETE
```

---

**END BOOTLOADER TEST v1.0**
