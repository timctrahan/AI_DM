# Orchestrator v6.8.0 - Campaign Updates Summary

## Overview

This document summarizes ALL changes needed for campaigns to work with Orchestrator v6.8.0's new features (level gating, exploration XP, companion suggestions).

---

## 1. Campaign File Updates (Acts 1-3)

### ✅ Act 1 - COMPLETED

**Updated Files:**
- `campaigns/Descent into Khar-Morkai/Act_1_Descent_into_Darkness.md`

**Changes Made:**

#### A. Main Quests - Level Gating Added

```yaml
# MAIN QUEST 1: Nightmares from Below
recommended_level: 4
level_warning: null  # Starting quest

# MAIN QUEST 2: The Duergar Market
recommended_level: 4
level_warning: "The duergar are ruthless traders and slavers. Weakness is death in their market."

# MAIN QUEST 3: The Sunless Chasm
recommended_level: 5
level_warning: "The chasm is said to be the grave of entire expeditions. Only experienced adventurers survive the crossing."

# MAIN QUEST 4: Gates of the Dead
recommended_level: 5
level_warning: "Korag Ironvow has stood watch for 800 years. The souls scream warnings through him. Turn back if you fear the dead."
```

#### B. Companions - Enhanced Backgrounds

**Velryn Duskmere (Drow Scout):**
```yaml
background:
  keywords: ["scout", "drow", "exile", "Underdark guide"]
  description: "Exiled drow scout and Underdark survivor..."
personal_quest_hook: "My sister Drissia leads a patrol in these tunnels..."
```

**Gralk Ironjaw (Duergar Fighter):**
```yaml
background:
  keywords: ["local", "duergar", "Underdark native", "tactical expert"]
  description: "Duergar deserter and tactical expert..."
personal_quest_hook: "My old patrol captain Thurgrim still controls the deep mines..."
```

---

### ⏳ Act 2 - PENDING

**File:** `campaigns/Descent into Khar-Morkai/Act_2_The_Dead_City.md`

**Recommended Level Gates:**
- Main Quest 5 (First Vault Fragment): Level 6
- Main Quest 6 (Second Vault Fragment): Level 6-7
- Main Quest 7 (Drow Ambush - Velryn's Past): Level 7
- Main Quest 8 (Mind Flayer Outpost): Level 7

**Level Warnings (Thematic):**
- Vault fragments: *"The priests' wards have killed many looters. Preparation is essential."*
- Drow ambush: *"Drow assassins are relentless. You'll need every advantage."*
- Mind flayers: *"Mind flayers are apex predators. Their psychic assaults shatter minds. Only the strong survive."*

---

### ⏳ Act 3 - PENDING

**File:** `campaigns/Descent into Khar-Morkai/Act_3_The_Vault_of_Souls.md`

**Recommended Level Gates:**
- Main Quest 9 (Breach Vault Wards): Level 8
- Main Quest 10 (Soul Prison Interior): Level 8-9
- Main Quest 11 (Faction Convergence): Level 9
- Main Quest 12 (The Impossible Choice): Level 9

**Level Warnings (Thematic):**
- Breach wards: *"Ten thousand tortured souls guard this place. Turn back if you value your sanity."*
- Soul prison: *"Madness waits within. Not all who enter emerge whole."*
- Final choice: *"This is the culmination of everything. There is no turning back."*

---

## 2. Campaign Creator Updates

**File:** `CAMPAIGN_CREATOR_ORCHESTRATOR_v2_0.md`

### Changes Needed:

#### A. Add to Quest Generation Template (Section ~4)

```markdown
### Quest Level Gating (NEW for v6.8.0)

**For Each Main Quest:**

1. Assign `recommended_level` based on act progression:
   - Act start quests: Starting level
   - Mid-act quests: Starting level + 1
   - Act finale: Starting level + 1-2

2. Write thematic `level_warning` (50-100 characters):
   - Reference specific threat (enemies, hazards, consequences)
   - Match campaign tone (dark/heroic/comedic)
   - Or use `null` for starting quests

**Example:**
```yaml
### MAIN QUEST 3: Assault the Dragon's Lair
recommended_level: 7
level_warning: "Ancient red dragons have ended kingdoms. Your bones will join the hoard."
```

**Side Quests:**
- Generally do NOT need level gates (players can tackle freely)
- Exception: If side quest has deadly unique encounter, add warning
```

#### B. Add to Companion NPC Template (Section ~6)

```markdown
### Companion Background Structure (NEW for v6.8.0)

**Required Fields for Companion_Suggestion Protocol:**

```yaml
companion_npc:
  background:
    keywords: [2-4 descriptive tags]  # REQUIRED for suggestion matching
    description: "One-sentence summary"  # REQUIRED
    details: [narrative backstory list]  # Existing structure

  personal_quest_hook: "One sentence teaser for personal storyline"  # OPTIONAL but recommended
```

**Keyword Guide:**
- **scout**: Tracks, finds hidden areas, warns of dangers
- **local**: Knows the region, suggests NPCs and shortcuts
- **guide**: Hired pathfinder, knows safe routes
- **native**: Cultural insider, translates customs
- **tactical expert**: Suggests combat strategies
- **lore keeper**: Provides historical context

**Examples:**

*Gruff Dwarven Guide:*
```yaml
keywords: ["local", "guide", "mountain native", "tracker"]
description: "Dwarven prospector who knows every tunnel in the Ironpeak Range."
personal_quest_hook: "My brother vanished in the Deep Mine three years ago. His tools are still down there."
```

*Exiled Noble:*
```yaml
keywords: ["noble", "diplomat", "city insider"]
description: "Disgraced noble with connections to the royal court."
personal_quest_hook: "The evidence that framed me is in the palace vault. I need to clear my name."
```
```

---

## 3. Campaign Validator Updates

**File:** `CAMPAIGN_VALIDATOR_TOOL_v2_0.md`

### Changes Needed:

#### A. Add New Validation Rules (Section ~3)

```markdown
## New Validation Rules for v6.8.0

### Rule: Quest Level Gates (WARNING Level)

**Check:** All main quests in acts with level progression have `recommended_level`

**Pattern:**
```yaml
### MAIN QUEST [N]: [Name]
recommended_level: [int]
level_warning: [string or null]
```

**Validation:**
1. Main quests should have `recommended_level` matching act progression
2. `level_warning` can be `null` for starting quests
3. `level_warning` should be 30-150 characters if present
4. Side quests generally should NOT have level gates

**Report Format:**
```
⚠️  WARNING: Main Quest "Assault the Vault" missing recommended_level
   Location: Act 2, Line 456
   Suggestion: Add level gate (party level 6-7 expected at this point)
```

**Fix:**
Add level gate to quest header:
```yaml
recommended_level: 7
level_warning: "The vault's wards have killed many treasure hunters. Come prepared."
```

---

### Rule: Companion Background Keywords (INFO Level)

**Check:** Recruitable companions have `background.keywords` and optionally `personal_quest_hook`

**Pattern:**
```yaml
companion_npc:
  background:
    keywords: [...]
    description: "..."
  personal_quest_hook: "..."  # Optional
```

**Validation:**
1. Keywords array should have 2-4 entries
2. At least one keyword should match: scout, local, guide, native, tactical, lore
3. Description should be 1-2 sentences (50-200 characters)
4. Personal quest hook enhances Companion_Suggestion but is optional

**Report Format:**
```
ℹ️  INFO: Companion "Thaldrin Ironbeard" missing background keywords
   Location: Act 1 NPCs, Line 892
   Impact: Won't participate in Companion_Suggestion system
   Suggestion: Add keywords like ["local", "guide", "mountain native"]
```

**Fix:**
Enhance companion background structure:
```yaml
background:
  keywords: ["local", "smith", "clan elder"]
  description: "Dwarven blacksmith who knows every forge and family in the mountains."
  details: [existing narrative]

personal_quest_hook: "The clan heirloom hammer was stolen. I know who has it."
```

---

### Rule: Exploration XP Opportunities (INFO Level)

**Check:** Campaign has discoverable content for Exploration_XP_Award

**Auto-Detects:**
1. New locations with descriptions → `major_discovery` XP
2. Puzzles, traps, mechanisms → `environmental_puzzle` XP
3. Lore items, ancient texts, murals → `lore_discovery` XP
4. NPC alliances via reputation → `npc_alliance` XP

**Report Format:**
```
ℹ️  INFO: Found 12 exploration XP opportunities in Act 1
   - 4 major discoveries (new locations)
   - 3 environmental puzzles
   - 5 lore discoveries

   These will automatically award XP when players encounter them.
   No action needed - informational only.
```

This is an **automatic feature** - no campaign changes needed!
```

---

## 4. Quick Migration Checklist

### For Existing Campaigns:

**Minimal Compliance (Backward Compatible):**
- [ ] No changes needed - campaign works as-is

**Enhanced Features (Recommended):**
- [ ] Add `recommended_level` to main story quests
- [ ] Add `level_warning` to 3-5 dangerous quests
- [ ] Add `background.keywords` to recruitable companions
- [ ] (Optional) Add `personal_quest_hook` to companions

**Full v6.8.0 Optimization:**
- [ ] Level-gate all main quests with thematic warnings
- [ ] Enhance all companion backgrounds with keywords + hooks
- [ ] Review exploration content for XP opportunities
- [ ] Test in-game with party attempting under-leveled quest

---

## 5. Testing Scenarios

### Test 1: Level Gate Warning
1. Start campaign at level 1 (or appropriate starting level)
2. Attempt to accept a main quest with `recommended_level` higher than party
3. **Expected:** Warning appears, player can choose to proceed or decline
4. **Verify:** Warning text matches `level_warning` field

### Test 2: Exploration XP
1. Discover a new location not previously visited
2. **Expected:** "⭐ Exploration XP: major_discovery discovered!" + XP awarded
3. Solve an environmental puzzle (trap, mechanism, riddle)
4. **Expected:** "⭐ Exploration XP: environmental_puzzle discovered!" + XP awarded

### Test 3: Companion Suggestion
1. Recruit companion with loyalty ≥ 3
2. Take multiple long rests (20% chance per rest)
3. **Expected:** Eventually, companion makes suggestion based on:
   - Active quest hints (if quests exist)
   - Location exploration (if unexplored areas)
   - Encounter warnings (if random encounters defined)
   - Personal hook (if `personal_quest_hook` exists)
4. **Verify:** Suggestion ties to campaign content, not random

---

## 6. Examples from "Descent into Khar-Morkai"

### Example: Well-Designed Main Quest (Act 1, Quest 4)

```yaml
### **MAIN QUEST 4: Gates of the Dead**
**Act Finale | 1500 XP | Sessions 5-6**

```yaml
recommended_level: 5
level_warning: "Korag Ironvow has stood watch for 800 years. The souls scream warnings through him. Turn back if you fear the dead."
```

#### Quest Summary
The party reaches Khar-Morkai's outer gates—massive dwarven doors carved with warnings...

[Quest content continues]
```

**Why This Works:**
- ✅ Level 5 recommended (party should be level 5 by Act 1 finale)
- ✅ Thematic warning (references specific NPC Korag + campaign theme of souls)
- ✅ Dark tone matches campaign ("turn back if you fear the dead")
- ✅ 96 characters (good length for warning)

---

### Example: Enhanced Companion (Velryn Duskmere)

```yaml
velryn_duskmere:
  background:
    keywords: ["scout", "drow", "exile", "Underdark guide"]
    description: "Exiled drow scout and Underdark survivor. Fled House Shadowveil after refusing assassination orders. Knows the deep tunnels like her own heartbeat."
    details:
      - Exiled from House Shadowveil for refusing assassination mission
      - Survived 2 years in Underdark alone
      - Knows Khar-Morkai location from drow archives
      - Hunted by her former house (wants her dead as example)

  personal_quest_hook: "My sister Drissia leads a patrol in these tunnels. I must warn her before House Shadowveil sends her to kill you."
```

**Why This Works:**
- ✅ Keywords include "scout" and "Underdark guide" (triggers location suggestions)
- ✅ Description is concise single sentence
- ✅ Personal hook ties to campaign (drow patrols exist in Act 2)
- ✅ Hook creates dramatic tension (sister vs. loyalty to party)

**Expected Behavior in Game:**
- After long rest in Underdark (20% chance)
- Velryn might say: *"I spotted drow patrol signs to the east. We should clear them before they find us."* (Priority 3: Encounter warning)
- Or if player has active quest: *"I know someone in the fungal groves who might help with [quest_name]. Want an introduction?"* (Priority 1: Quest hint)
- Or if loyalty is high: *"My sister's patrol hunts these tunnels. I need to warn her before it's too late."* (Priority 4: Personal hook)

---

## 7. Common Mistakes to Avoid

### ❌ Level Gates on Side Quests
```yaml
### SIDE QUEST 2: Help the Refugees
recommended_level: 6  # ← WRONG! Side quests should be tackle-at-any-level
level_warning: "..."
```
**Fix:** Remove level gate from side quests (let players choose when to tackle)

---

### ❌ Generic/Boring Level Warnings
```yaml
recommended_level: 7
level_warning: "This quest is hard."  # ← BORING! Not thematic
```
**Fix:** Make it specific to the quest:
```yaml
level_warning: "The lich's phylactery is protected by wraith guardians. Weak souls become their slaves."
```

---

### ❌ Missing Companion Keywords
```yaml
background:
  - "He's a ranger who knows the forest"  # ← Old structure, no keywords
```
**Fix:** Use new structure:
```yaml
background:
  keywords: ["scout", "local", "forest ranger"]
  description: "Forest ranger who knows every trail and hidden grove in the Whisperwood."
  details: [narrative backstory]
```

---

### ❌ Vague Personal Quest Hooks
```yaml
personal_quest_hook: "He has a secret."  # ← Too vague!
```
**Fix:** Be specific and compelling:
```yaml
personal_quest_hook: "The bandit who killed my family leads a crew in the Shadowed Hills. I know where they camp."
```

---

## 8. Timeline & Rollout

### Phase 1: Core Files ✅ COMPLETE
- [x] Orchestrator v6.8.0 assembled
- [x] Update guide created
- [x] Act 1 updated

### Phase 2: Remaining Acts ⏳ IN PROGRESS
- [ ] Act 2 level gates
- [ ] Act 3 level gates
- [ ] Batch test all three acts

### Phase 3: Tools Update ⏳ PENDING
- [ ] Campaign Creator updated
- [ ] Campaign Validator updated
- [ ] New campaign template with examples

### Phase 4: Testing 🔜 NEXT
- [ ] Load Act 1 into orchestrator v6.8.0
- [ ] Test level gate warnings
- [ ] Test exploration XP
- [ ] Test companion suggestions
- [ ] Document any issues

---

## 9. Support & Questions

**Issue:** Quest warnings not showing
- Check: `recommended_level` is integer (not string)
- Check: Quest is in `quests_available` or being accepted

**Issue:** Companion never suggests anything
- Check: Companion has loyalty ≥ 3 in save file
- Check: Companion has `keywords` in background
- Note: 20% chance per rest (may take 5+ rests to trigger)

**Issue:** Exploration XP seems wrong
- Verify: XP scales with party level (level 1 gets ~10-20 XP, level 10 gets ~100-200 XP)
- Check: Discovery type matches achievement (don't award "major_discovery" for finding a single chest)

---

**Bottom Line:** All new features are **optional enhancements**. Your campaigns work perfectly without any changes. Update when ready! 🎲
