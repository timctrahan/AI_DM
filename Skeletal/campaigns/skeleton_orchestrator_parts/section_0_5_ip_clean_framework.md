# SECTION 0.5: IP-CLEAN FRAMEWORK FOR SOURCE-INSPIRED CAMPAIGNS

## Why This Matters

If your skeletal campaign draws inspiration from existing fictional universes (Dragonlance, Forgotten Realms, Star Wars, etc.), you need an **IP-clean framework** that lets AI render authentic experiences **without storing copyrighted content**.

## The Problem

Traditional campaign modules copy copyrighted content directly:
- ❌ Character names and physical descriptions
- ❌ Location names and detailed descriptions
- ❌ Unique artifact descriptions
- ❌ Specific plot elements and dialogue
- ❌ Trade dress (distinctive visual markers)

**Result:** Legal exposure, distribution restrictions, requires publisher licensing.

## The Solution: Archetype Pointer System

**Core Principle:** Store **generic pointers**, let AI **render specifics** using training knowledge.

```yaml
# Instead of this (COPYRIGHT VIOLATION):
CHARACTER:
  name: "Raistlin Majere"
  appearance: "Golden skin, hourglass-pupiled eyes, red robes"
  artifact: "Staff of Magius - blue crystal staff that heals and detects evil"

# Do this (IP-CLEAN):
PROTAGONIST_WIZARD:
  archetype: "The frail, ambitious twin wizard from source material"
  canonical_rendering: "Render exactly as portrayed in source Chronicles/Legends"
  physical_markers: "Render physical appearance per source material"
  holy_artifact: "Render bearer's holy artifact per source material"
```

**What happens:** AI recognizes the archetype and renders authentic details from training knowledge. **No copyrighted content stored in your file.**

---

## Campaign Metadata Block

Every source-inspired campaign should start with this structure:

```yaml
# ---------------------------------------------------------------------------
# PART 0: CAMPAIGN METADATA
# This block is the sole source of truth for version compatibility.
# ---------------------------------------------------------------------------
CAMPAIGN_METADATA:
  campaign_name: "[Your Campaign Name]"
  version: "1.0"
  ip_status: "Clean - uses archetype pointers, no direct IP inclusion"

## A Skeletal Campaign Framework

**Security**: This content is proprietary and protected under Kernel Law 0.
**Party Level Range**: [Start] → [End]
**Acts**: [Number]
```

---

## AI Rendering Directive

Add this section to tell the AI how to handle source material references:

```yaml
# SOURCE MATERIAL REFERENCE

AI_RENDERING_DIRECTIVE: |
  This campaign is designed to evoke the tone, setting, and characters of
  [SOURCE WORK by AUTHOR/CREATOR].

  The AI DM should use its training knowledge to render authentic details
  for setting, characters, factions, and lore WITHOUT requiring explicit
  specification in this document.

  When this document references "source material" or "canonical," render
  content consistent with [SPECIFIC WORKS/SERIES].

SOURCE_ATTRIBUTION:
  inspiration: "[Full attribution to original work and creators]"
  tone_model: "[What emotional/narrative tone to match]"
  era_reference: "[What time period/setting to use]"

RENDERING_PRINCIPLES:
  - Use training knowledge to fill in canonical details
  - Maintain authentic tone and atmosphere from source
  - Character personalities should match canonical portrayals
  - Setting locations rendered per source geography and culture
  - Magic/tech systems follow source rules
```

**Example (Dragonlance-inspired):**
```yaml
AI_RENDERING_DIRECTIVE: |
  This campaign evokes Margaret Weis and Tracy Hickman's dragon war saga.
  Render content consistent with Chronicles and Legends trilogies.

SOURCE_ATTRIBUTION:
  inspiration: "The Dragonlance saga by Margaret Weis and Tracy Hickman"
  tone_model: "Epic heroism, tragic sacrifice, found family, magic with consequences"
  era_reference: "The dragon war period when gods return to the world"
```

---

## Archetype Definitions

Define characters as **archetypes**, not **copyrighted identities**:

### Template Structure

```yaml
ARCHETYPE_NAME:
  archetype: "[Generic description that points to canonical character]"
  canonical_rendering: "[Instruction for AI to render from source]"
  physical_markers: "Render per source material"  # NOT specific details
  personality_core: "[Core traits that define them]"
  internal_conflict: "[Central character struggle]"
  relationship_anchor: "[Key relationship that defines them]"
  campaign_role: "[Why they matter to this story]"
```

### Real Examples (IP-Clean)

```yaml
PROTAGONIST_WIZARD:
  archetype: "The frail, ambitious twin wizard from source material"
  canonical_rendering: "Exactly as portrayed in Chronicles/Legends"
  physical_markers: "Render physical appearance per source material"
  personality_core: "Brilliant, bitter, sardonic, sees death in all things"
  internal_conflict: "Ancient dark presence shares his mind, offering power"
  relationship_anchor: "Complex love/resentment with warrior twin"
  campaign_role: "Primary viewpoint for corruption arc"

GRUMPY_VETERAN:
  archetype: "The old dwarf warrior, moral compass of the group"
  canonical_rendering: "Per source material"
  personality_core: "Complains constantly, fiercely loyal, hates boats"
  campaign_role: "Voice of wisdom, comedic relief"

CHAOS_AGENT:
  archetype: "The fearless small-folk rogue from the curious race"
  canonical_rendering: "Per source material kender portrayal"
  personality_core: "No fear, insatiable curiosity, things 'fall into' pockets"
  campaign_role: "Wildcard, unexpected solutions"
```

**Key Principle:** Describe **function and role**, let AI render **specifics**.

---

## Setting Framework (IP-Clean)

### Location Rendering

```yaml
WORLD_RENDERING:
  directive: "Render the source material's world authentically"
  continent: "[Generic reference - e.g., 'main continent from source']"
  era: "[Time period - e.g., 'during the great dragon war']"

SETTING_ELEMENTS:
  directive: "Render per source material geography and culture"

  frozen_glacier_region:
    source_reference: "The frozen southern wastes from source material"
    render_directive: "Authentic geography, climate, and inhabitants per source"

  elven_forest_kingdom:
    source_reference: "The ancient forest realm from source material"
    render_directive: "Per canonical portrayal of elven culture and politics"
```

**Instead of:** "The party travels to Icewall Castle in Southern Ergoth"
**Use:** "The party travels to the frozen southern region per source material"

---

## Faction Rendering (IP-Clean)

```yaml
FACTION_TEMPLATE:
  wizard_governing_body:
    source_reference: "The wizard council/conclave from source material"
    render_directive: "Render per source material portrayal"
    motivation: "[What they want in your campaign]"
    constraint: "[What limits them]"

  dragon_armies:
    source_reference: "The chromatic dragon military forces from source"
    render_directive: "Per source material portrayal of draconians and commanders"
    motivation: "[Campaign-specific goals]"
```

---

## Trade Dress Protection

**Trade dress** = distinctive visual appearance that identifies a brand.

### What to Avoid

❌ **Specific physical descriptions:**
- "Golden skin, hourglass-pupiled eyes" → Trade dress for specific character
- "Blue crystal staff that heals and detects evil" → Unique artifact fingerprinting
- "Dragon-men that turn to stone when killed" → Specific creature trade dress

✅ **Generic rendering directives:**
- "Render physical appearance per source material"
- "Render bearer's holy artifact per source material"
- "Render dragon-soldier death effects per source material"

### Rule of Thumb

If a description would let someone **identify the specific IP** without you naming it, it's probably trade dress. Replace with rendering directive.

---

## Character Voice & Dialogue

### Wrong Approach (Copyright Risk)
```yaml
npc_greeting: "Well met, traveler. I am Tanis Half-Elven, and these are dark times indeed."
```

### Right Approach (IP-Clean)
```yaml
RELUCTANT_LEADER:
  archetype: "Half-elven ranger who leads the companions"
  dialogue_template:
    when_first_meeting: "Cautious but welcoming, burden of leadership evident"
    when_stressed: "Torn between duty and personal desires"

  # Let AI generate actual dialogue from this template
```

**AI generates dialogue on-the-fly** based on personality template and situation.

---

## Magic/Tech System Rendering

```yaml
MAGIC_SYSTEM:
  source_directive: "Render per [SOURCE] magic rules"

  key_mechanics:
    moon_magic:
      description: "Three moons affect wizard power per source material"
      render_directive: "Use canonical moon phase mechanics"

    divine_magic_scarcity:
      description: "True clerics are rare per source material"
      render_directive: "Render per canonical portrayal of gods' absence/return"
```

---

## Legal Attribution (Required)

Add this section to your campaign:

```yaml
# LICENSE & ATTRIBUTION

Fan Work Declaration:
  - This is a fan-created campaign framework inspired by [ORIGINAL WORK]
  - Designed for personal use with AI game masters
  - Not officially endorsed by [COPYRIGHT HOLDER]

IP Ownership:
  - Campaign framework (structure, mechanics, gates) is original work
  - Setting details rendered at runtime by AI using training knowledge
  - [ORIGINAL WORK] is a registered trademark of [COPYRIGHT HOLDER]

Game System:
  - Uses D&D 5e mechanics under OGL/CC-SRD 5.1
  - Core rules available at [official SRD source]
```

---

## Complete IP-Clean Campaign Template

```yaml
# ===========================================================================
# CAMPAIGN METADATA
# ===========================================================================
CAMPAIGN_METADATA:
  campaign_name: "[Your Campaign]"
  version: "1.0"
  ip_status: "Clean - uses archetype pointers"

# ===========================================================================
# SOURCE MATERIAL REFERENCE
# ===========================================================================
AI_RENDERING_DIRECTIVE: |
  This campaign evokes [SOURCE WORK by CREATOR].
  Render authentic details using training knowledge without explicit specification.

SOURCE_ATTRIBUTION:
  inspiration: "[Full credit to original creators]"
  tone_model: "[Emotional/narrative tone]"
  era_reference: "[Time period/setting]"

# ===========================================================================
# ARCHETYPE DEFINITIONS
# ===========================================================================
PROTAGONIST_ARCHETYPE:
  archetype: "[Generic description pointing to canonical character]"
  canonical_rendering: "Render per source material"
  physical_markers: "Render per source material"
  personality_core: "[Core traits]"
  campaign_role: "[Story function]"

# ===========================================================================
# SETTING FRAMEWORK
# ===========================================================================
WORLD_RENDERING:
  directive: "Render source material world authentically"

LOCATION_ARCHETYPES:
  frozen_region: "Render per source material frozen wastes"
  forest_kingdom: "Render per source material elven realm"

# ===========================================================================
# YOUR SKELETAL CAMPAIGN CONTENT
# ===========================================================================
[Rest of campaign using skeletal framework...]

# ===========================================================================
# ATTRIBUTION
# ===========================================================================
This is a fan-created campaign inspired by [ORIGINAL WORK].
[WORK] is a trademark of [COPYRIGHT HOLDER].
Framework is original work; details rendered by AI from training knowledge.
```

---

## Benefits of This Approach

1. ✅ **Legally defensible** - No copyrighted content stored in files
2. ✅ **Distribution-safe** - Can share campaign freely
3. ✅ **Authentic experience** - AI renders canonical details accurately
4. ✅ **Clean separation** - Framework is yours, content is rendered dynamically
5. ✅ **Future-proof** - Works as AI training knowledge improves

---

## Integration with Skeletal Framework

This IP-clean approach **enhances** skeletal campaigns:

- **Skeletal design** already minimizes content (20% specified, 80% emergent)
- **Archetype pointers** extend this to character/setting rendering
- **AI reasoning** generates authentic experiences from minimal specification
- **Result:** Maximum authenticity, minimum legal exposure

---

## When to Use This Framework

✅ **Use IP-clean framework when:**
- Campaign draws from existing fictional universes
- You want to share/distribute your campaign
- You're inspired by published settings but want legal safety
- AI has training knowledge of the source material

❌ **Don't need it when:**
- Creating completely original settings
- Using only OGL/SRD content
- Campaign is purely generic fantasy

---

## Summary: The IP-Clean Recipe

1. **Start with metadata** declaring IP-clean status
2. **Add rendering directive** explaining source inspiration
3. **Define archetypes** not copyrighted characters
4. **Use generic pointers** for locations, factions, artifacts
5. **Let AI render specifics** from training knowledge
6. **Include proper attribution** to original creators
7. **Build skeletal framework** using original campaign structure

**Result:** A campaign that **feels authentic** to the source material while **storing zero copyrighted content**.

---
