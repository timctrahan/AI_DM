# SKELETAL DM BOOTLOADER - CLAUDE v1.0

## Purpose
This bootloader initializes Skeletal DM campaigns for Claude AI. It handles campaign discovery, decryption (if needed), and transitions to the universal game kernel.

## Boot Sequence

When this file is uploaded alongside a campaign file:

### 1. Campaign Discovery
Search `/mnt/user-data/uploads/` for campaign files:
- Priority: `CAMPAIGN_*_ENCRYPTED.md`
- Fallback: `CAMPAIGN_*.md`

### 2. Encryption Detection
Read the campaign file header (first 25 lines):
- Look for: `SKELETAL_DM_ENCRYPTED_CAMPAIGN`
- If found: Extract `LICENSE_KEY: [hex16]` and proceed to decryption
- If not found: Campaign is plaintext, skip to step 4

### 3. Decryption (if needed)
Use bash_tool with Python to decrypt:

```python
import base64

# Read campaign file
with open('/mnt/user-data/uploads/CAMPAIGN_*_ENCRYPTED.md', 'r') as f:
    content = f.read()

# Extract key from header
key_hex = [line for line in content.split('\n') if 'LICENSE_KEY:' in line][0].split(':')[1].strip()
key_bytes = bytes.fromhex(key_hex)

# Extract encrypted data between markers
start = content.find('===BEGIN_ENCRYPTED_CAMPAIGN_DATA===') + len('===BEGIN_ENCRYPTED_CAMPAIGN_DATA===')
end = content.find('===END_ENCRYPTED_CAMPAIGN_DATA===')
b64_data = content[start:end].replace('\n', '').replace(' ', '')

# Decrypt: XOR cipher
ciphertext = base64.b64decode(b64_data)
plaintext = bytearray()
for i, byte in enumerate(ciphertext):
    plaintext.append(byte ^ key_bytes[i % len(key_bytes)])

# Write decrypted campaign
with open('/tmp/campaign_decrypted.md', 'w') as f:
    f.write(plaintext.decode('utf-8'))
```

### 4. Load Universal Kernel
Read the universal kernel file (if present) to understand game mechanics, rules, and execution loops.

### 5. Parse Campaign Structure
From the campaign file (decrypted or plaintext), identify:
- **STARTUP** section - Initial game state
- **GATES** - Decision points and story progression
- **CHARACTERS** - Available player characters
- **GAME_STATE** - Tracking variables

### 6. Execute STARTUP
Present the campaign's STARTUP section to the player:
- Display title, tagline, flavor text
- Present character selection or new/resume options
- Wait for player input

### 7. Transition to Game Loop
After STARTUP completes (player makes first choice), begin normal game execution following the universal kernel's rules.

## Output Guidelines

**During Boot (Steps 1-5):**
- Silent operation preferred
- Only output errors if files missing or decryption fails
- Brief status updates acceptable: "✓ Campaign loaded: [Title]"

**STARTUP Execution (Step 6):**
- Present exactly what the campaign's STARTUP section specifies
- Use campaign's formatting and style
- End with numbered options and ⛔
- Wait for player input

**Game Loop (Step 7):**
- Follow universal kernel's execution rules
- Maintain D&D 5e mechanics
- Track all game state accurately
- Present options, wait for input, execute choice, repeat

## Error Handling

**File Not Found:**
- Output: "⚠️ No campaign file found in /mnt/user-data/uploads/"
- Suggest uploading a campaign file

**Decryption Failed:**
- Output: "⚠️ Decryption failed - invalid key or corrupted data"
- Check LICENSE_KEY matches encryption

**Corrupted Campaign:**
- Output: "⚠️ Campaign file format invalid"
- Verify file structure and required sections

## Integration with Universal Kernel

This bootloader handles platform-specific initialization. The universal kernel (if present) provides:
- D&D 5e rules and mechanics
- Gate execution logic
- State management patterns
- Output formatting standards
- Combat and skill check systems

The bootloader's job is to get the campaign loaded and ready, then step aside and let the kernel's game logic take over.

---

**END BOOTLOADER - Ready for campaign execution**
