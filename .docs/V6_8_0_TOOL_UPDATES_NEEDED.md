# Campaign Creator & Validator Updates for v6.8.0

## Quick Reference

**Files to Update:**
1. `CAMPAIGN_CREATOR_ORCHESTRATOR_v2_0.md` - Add level gating & companion templates
2. `CAMPAIGN_VALIDATOR_TOOL_v2_0.md` - Add validation rules for new features

---

## 1. Campaign Creator Updates

### Location: After "Quest Design Patterns" Section

**Insert This New Section:**

```markdown
## QUEST LEVEL GATING (v6.8.0)

### When to Add Level Gates

**Main Story Quests:** ✅ YES
- Gates prevent players from rushing to endgame content
- Ensures proper power curve and challenge balance
- Respects player agency (warning, not hard block)

**Side Quests:** ❌ NO (usually)
- Players should tackle side content at their own pace
- Exception: If side quest has unique deadly encounter, add warning

**Boss Encounters:** ✅ YES
- Major boss fights should have level gates
- Prevents TPKs from under-leveled parties

### Level Progression Guide

| Act Stage | Recommended Level | Example |
|-----------|-------------------|---------|
| Act Start | Starting level | Act 1 Quest 1 → Level 4 |
| Early Act | Starting + 0-1 | Act 1 Quest 2 → Level 4 |
| Mid Act | Starting + 1 | Act 1 Quest 3 → Level 5 |
| Act Finale | Starting + 1-2 | Act 1 Quest 4 → Level 5 |

**Multi-Act Campaign:**
- Act 1: Levels 4→5
  - Quest 1-2: Level 4
  - Quest 3-4: Level 5
- Act 2: Levels 5→7
  - Quest 5-6: Level 6
  - Quest 7-8: Level 7
- Act 3: Levels 7→9
  - Quest 9-10: Level 8
  - Quest 11-12: Level 9

### Template for Level-Gated Quests

```markdown
### **MAIN QUEST [N]: [Quest Name]**
**[Type] | [XP] | [Sessions]**

\```yaml
recommended_level: [int]
level_warning: "[50-150 character thematic warning or null]"
\```

#### Quest Summary
[Quest description]
```

### Writing Effective Level Warnings

**Good Examples:**
```yaml
# Dark/Gritty Tone
level_warning: "The lich's phylactery is guarded by wraith servants. Weak souls become their slaves."

# Heroic/Epic Tone
level_warning: "Ancient red dragons have ended kingdoms. Your courage will be tested."

# Cosmic Horror Tone
level_warning: "The portal leaks madness. Not all who enter emerge with minds intact."

# Tactical/Realistic Tone
level_warning: "The fortress has 50 veteran soldiers. Frontal assault requires superior numbers."
```

**Bad Examples:**
```yaml
level_warning: "This is hard."  # ❌ Too vague
level_warning: "You'll probably die."  # ❌ Not thematic
level_warning: "The dragon in the fortress guarded by soldiers with the lich's phylactery..."  # ❌ Too long, confusing
```

**Formula:**
1. Identify primary threat (enemy, hazard, consequence)
2. State specific danger in 1-2 sentences
3. Match campaign tone (dark, heroic, comedic, etc.)
4. Keep to 50-150 characters

### Examples by Campaign Type

**Underdark Campaign:**
```yaml
recommended_level: 7
level_warning: "Mind flayers are apex predators. Their psychic assaults shatter minds. Only the strong survive."
```

**Political Intrigue:**
```yaml
recommended_level: 5
level_warning: "The duchess's spies have killed more experienced operatives. One mistake is fatal."
```

**Wilderness Survival:**
```yaml
recommended_level: 6
level_warning: "The northern wastes claim unprepared travelers. Frostbite kills faster than beasts."
```

**Dungeon Crawl:**
```yaml
recommended_level: 8
level_warning: "The vault's wards incinerate tomb robbers. Ancient dwarven runework doesn't forgive weakness."
```

---

## COMPANION BACKGROUND STRUCTURE (v6.8.0)

### Why Keywords Matter

The `Companion_Suggestion` protocol uses background keywords to determine what type of suggestions companions can make:

- **"scout"** → Suggests hidden areas, tracks, dangers
- **"local"** → Suggests NPCs, shortcuts, cultural insights
- **guide"** → Suggests safe routes, environmental hazards
- **"native"** → Provides cultural context, translation
- **"tactical expert"** → Suggests combat strategies
- **"lore keeper"** → Provides historical context

### Template for Recruitable Companions

```yaml
companion_npc:
  # ... stats, class, etc. (existing structure)

  background:
    keywords: [2-4 descriptive tags]  # NEW - for Companion_Suggestion
    description: "One-sentence summary of who they are and what they know"  # NEW
    details:  # EXISTING - narrative backstory
      - Background detail 1
      - Background detail 2
      - Background detail 3

  personal_quest_hook: "One sentence teaser for companion's personal storyline"  # NEW - optional but recommended

  # ... rest of companion definition (existing structure)
```

### Keyword Selection Guide

**For Each Companion, Ask:**
1. What's their profession/role? (scout, merchant, noble, soldier)
2. Are they from this region? (local, native, outsider)
3. What expertise do they offer? (tactical, lore, diplomatic, survival)
4. What's their relationship to the setting? (guide, insider, rebel, exile)

**Example Thought Process:**

*"Thaldrin Ironbeard - Dwarven blacksmith who grew up in these mountains"*
- Profession: blacksmith → "smith", "craftsman"
- Region: native → "local", "mountain native"
- Expertise: knows clans → "clan elder", "cultural guide"
- **Keywords:** `["local", "smith", "clan elder", "mountain native"]`

*"Saria Windwhisper - Elven ranger hired as wilderness guide"*
- Profession: ranger → "scout", "ranger"
- Region: operates here → "guide", "tracker"
- Expertise: survival → "wilderness expert", "pathfinder"
- **Keywords:** `["scout", "guide", "wilderness expert", "tracker"]`

### Personal Quest Hook Guidelines

**Purpose:** Enables Priority 4 companion suggestions (personal storylines)

**Structure:** One sentence that:
1. Hints at unresolved past
2. Connects to campaign setting
3. Creates dramatic tension
4. Gives DM/AI story hook to develop

**Good Examples:**
```yaml
# Revenge Arc
personal_quest_hook: "The bandit who killed my family leads a crew in the Shadowed Hills. I know where they camp."

# Redemption Arc
personal_quest_hook: "I betrayed my order to save a life. Their assassins still hunt me."

# Lost Item/Person
personal_quest_hook: "My brother vanished in the Deep Mine three years ago. His tools are still down there."

# Unfinished Business
personal_quest_hook: "The evidence that framed me is in the palace vault. I need to clear my name."

# Faction Conflict
personal_quest_hook: "My sister leads the enemy patrol. I must warn her before they send her to kill you."
```

**Bad Examples:**
```yaml
personal_quest_hook: "He has a secret."  # ❌ Too vague
personal_quest_hook: "Wants revenge."  # ❌ No specifics
personal_quest_hook: "His past haunts him and he seeks redemption from those he wronged long ago in a distant land."  # ❌ Too long, unfocused
```

### Complete Companion Example

```yaml
#### **Elena Shadowstep** (Halfling Rogue)
**Role:** Infiltrator, City Guide, Comic Relief

\```yaml
elena_shadowstep:
  race: Halfling
  class: Rogue 5 (Thief)
  alignment: Chaotic Good

  stats:
    AC: 16 (leather + DEX)
    HP: 28 (5d8+5)
    Speed: 25 ft

  key_abilities:
    - Cunning Action
    - Sneak Attack +3d6
    - Fast Hands
    - Second-Story Work (climb speed = movement)

  personality:
    traits: [witty, reckless, loyal]
    ideals: "Freedom means nothing if you can't share it."
    bonds: "The Thieves' Guild saved me. I owe them everything."
    flaws: "I can't resist a good heist, even when it's stupid."

  background:
    keywords: ["local", "city insider", "thief", "guide"]  # NEW
    description: "Halfling thief who knows every rooftop, sewer, and secret passage in the capital. Former Thieves' Guild member."  # NEW
    details:
      - Grew up in the capital's slums
      - Joined Thieves' Guild at age 12
      - Expelled for stealing from guildmaster (no regrets)
      - Knows city layout, guard patrols, noble houses
      - Still has contacts in the underground

  personal_quest_hook: "The guildmaster has my sister. She's innocent, but he'll kill her to get to me."  # NEW

  combat_tactics:
    - Flanks for Sneak Attack
    - Uses Fast Hands to deploy ball bearings, caltrops
    - Disengages up walls/buildings
    - Jokes during combat ("Behind you! No, behind YOU!")

  recruitment:
    location: "Capital City - The Rusty Dagger Tavern"
    cost: "Help her steal back a stolen heirloom"
    initial_reputation: 0

  reputation_triggers:
    +3: "Defend the innocent from powerful oppressors"
    +2: "Pull off a clever heist together"
    +1: "Laugh at her jokes"
    -3: "Work with corrupt nobles"
    -2: "Abandon someone in need"

  dialogue_samples:
    greeting: "You look like trouble. I like trouble."
    low_trust: "Watch your back. I'm watching mine."
    high_trust: "You're not half bad for tall folk."
    combat: "I got your six! Wait, which six? You have a lot of sides!"
\```
```

**How This Companion Will Behave in v6.8.0:**

After long rests (20% chance), Elena might suggest:

**Priority 1 - Quest Hints (if active quests):**
- *"I know a fence who can identify that artifact you found. Want an introduction?"*

**Priority 2 - Location Exploration:**
- *"I spotted a sewer grate that leads under the noble district. Could be useful."*

**Priority 3 - Encounter Warnings:**
- *"City guard patrols pass here every hour. We should clear out or lay low."*

**Priority 4 - Personal Hook:**
- *"The guildmaster has my sister in the warehouse by the docks. I need to get her out before he uses her against me."*

---

## WHEN TO PROMPT FOR THESE FEATURES

### During Campaign Creation Dialogue:

```markdown
**After Quest Design Phase:**

AI: "I've designed [N] main quests for this act. Now I'll add level gating..."

FOR EACH main_quest:
  1. Assign recommended_level based on act progression
  2. Write thematic level_warning (or use null for starting quests)
  3. Present to user for approval

AI: "Here are the level gates I've assigned:

- Main Quest 1: Level 4 (starting quest, no warning)
- Main Quest 2: Level 4, Warning: 'The goblin warlord commands 30 warriors. Numbers matter.'
- Main Quest 3: Level 5, Warning: 'The dragon's breath has melted adventurers' armor before they saw it coming.'

Does this progression feel right? (yes/modify/skip)"

⛔ WAIT for user input
```

```markdown
**During Companion NPC Creation:**

AI: "I've designed the companion [Name]. Now I'll enhance their background for v6.8.0 features..."

1. Extract 3-4 keywords from companion role/profession
2. Write one-sentence description
3. Propose personal_quest_hook (or ask user for input)

AI: "For companion [Name], I've added:

**Keywords:** [scout, local, wilderness expert]
**Description:** 'Forest ranger who knows every trail in the Whisperwood.'
**Personal Hook:** 'The beast that killed my mentor still roams the deep forest. I know its lair.'

Does this work for triggering companion suggestions? (yes/modify/skip)"

⛔ WAIT for user input
```
```

---

## 2. Campaign Validator Updates

### Location: After Existing Validation Rules

**Insert These New Validation Rules:**

```markdown
## Validation Rule: Quest Level Gates (v6.8.0)

**Rule ID:** V6.8-QUEST-LEVEL
**Severity:** WARNING (not ERROR - backward compatible)
**Category:** Quest Design

### What It Checks

Validates that main story quests have appropriate level gating to prevent railroading and TPKs.

### Pattern Match

```markdown
### **MAIN QUEST [N]: [Name]**
**[Type] | [XP] | [Sessions]**

\```yaml
recommended_level: [integer]
level_warning: [string or null]
\```
```

### Validation Logic

1. **Detect Main Quests:**
   - Line starts with `### **MAIN QUEST`
   - Exclude side quests, optional quests

2. **Check for Level Gate:**
   - Within next 10 lines, find ``` yaml block
   - Check for `recommended_level: [int]`
   - Check for `level_warning: [string or null]`

3. **Validate Values:**
   - `recommended_level` is integer 1-20
   - `level_warning` is null OR string 30-200 characters
   - Level progression makes sense (Quest 2 not lower than Quest 1)

### Pass Examples

```yaml
# Valid - starting quest
recommended_level: 4
level_warning: null

# Valid - mid-campaign quest
recommended_level: 7
level_warning: "The lich's phylactery is protected by wraith guardians. Weak souls become their slaves."

# Valid - act finale
recommended_level: 9
level_warning: "This is the culmination of everything. There is no turning back."
```

### Fail Examples with Fixes

**Missing Level Gate:**
```markdown
### **MAIN QUEST 3: Assault the Vault**
**Combat Encounter | 2000 XP | Session 5**

#### Quest Summary
[No level gate present]
```
**Error:** `⚠️ WARNING: Main Quest "Assault the Vault" missing recommended_level (Line 345)`
**Fix:** Add level gate after quest header:
```yaml
recommended_level: 7
level_warning: "The vault's wards incinerate tomb robbers. Ancient runework doesn't forgive weakness."
```

**Invalid Level Warning (Too Short):**
```yaml
recommended_level: 6
level_warning: "Hard quest."
```
**Error:** `⚠️ WARNING: Level warning too short (11 chars, minimum 30) (Line 456)`
**Fix:** Make warning more descriptive:
```yaml
level_warning: "The dragon's breath has melted adventurers in their armor. Come prepared with fire resistance."
```

**Level Regression:**
```yaml
# Quest 3
recommended_level: 7

# Quest 4 (later in same act)
recommended_level: 5  # ← PROBLEM!
```
**Error:** `⚠️ WARNING: Level regression detected. Quest 4 (level 5) lower than Quest 3 (level 7) (Line 567)`
**Fix:** Ensure level progression increases or stays same:
```yaml
recommended_level: 7  # Same or higher than previous
```

---

## Validation Rule: Companion Background Structure (v6.8.0)

**Rule ID:** V6.8-COMPANION-BG
**Severity:** INFO (enhancement, not required)
**Category:** NPC Design

### What It Checks

Validates that recruitable companion NPCs have enhanced background structure for `Companion_Suggestion` protocol.

### Pattern Match

```yaml
companion_npc:
  background:
    keywords: [...]  # Should exist
    description: "..."  # Should exist
  personal_quest_hook: "..."  # Optional but recommended
```

### Validation Logic

1. **Detect Companion NPCs:**
   - NPC marked as `**Role:** ...Companion...` OR
   - NPC section contains `recruitment:` field

2. **Check Background Structure:**
   - Has `background:` field
   - Has `keywords:` array with 2-4 entries
   - Has `description:` string (50-200 characters)
   - Optionally has `personal_quest_hook:` string

3. **Validate Keywords:**
   - At least one keyword matches: scout, local, guide, native, tactical, lore, insider
   - Keywords are descriptive (not generic like "character", "person")

### Pass Examples

```yaml
# Full structure
background:
  keywords: ["scout", "drow", "exile", "Underdark guide"]
  description: "Exiled drow scout who knows the deep tunnels like her own heartbeat."
  details: [...]
personal_quest_hook: "My sister leads an enemy patrol. I must warn her."

# Minimal valid
background:
  keywords: ["local", "guide"]
  description: "Dwarven pathfinder familiar with mountain passes."
  details: [...]
# personal_quest_hook optional
```

### Info Messages with Suggestions

**Missing Keywords:**
```yaml
background:
  - "Former soldier who knows the area"
```
**Info:** `ℹ️  INFO: Companion "Marcus Steel" missing background.keywords (Line 789)`
**Impact:** Won't participate in Companion_Suggestion system
**Suggestion:** Restructure as:
```yaml
background:
  keywords: ["local", "soldier", "tactical expert"]
  description: "Former soldier who knows the area's defenses and patrol routes."
  details: ["Former soldier who knows the area"]
```

**Weak Keywords:**
```yaml
background:
  keywords: ["character", "good person", "helpful"]
```
**Info:** `ℹ️  INFO: Companion keywords too generic. Consider: scout, local, guide, native, tactical, lore (Line 890)`
**Suggestion:** Replace with role-specific keywords:
```yaml
keywords: ["healer", "cleric", "lore keeper", "historian"]
```

**Missing Personal Hook:**
```yaml
background:
  keywords: ["scout", "ranger"]
  description: "Forest ranger and tracker."
  # No personal_quest_hook
```
**Info:** `ℹ️  INFO: Companion missing personal_quest_hook (optional but enhances suggestions) (Line 901)`
**Suggestion:** Add a personal storyline teaser:
```yaml
personal_quest_hook: "The poachers who destroyed my village still operate in the eastern woods. I know their camp."
```

---

## Validation Rule: Exploration XP Opportunities (v6.8.0)

**Rule ID:** V6.8-EXPLORE-XP
**Severity:** INFO (informational only)
**Category:** Content Analysis

### What It Checks

Scans campaign for content that will trigger `Exploration_XP_Award` protocol and reports findings.

### Auto-Detection Patterns

1. **Major Discoveries:**
   - New locations with descriptions
   - Dungeon entrances
   - Hidden settlements
   - Pattern: "discover", "find", "reveal", "hidden", "secret"

2. **Environmental Puzzles:**
   - Traps to disarm
   - Mechanisms to solve
   - Riddles, runes, locks
   - Pattern: "puzzle", "trap", "mechanism", "riddle", "locked", "sealed"

3. **Lore Discoveries:**
   - Ancient texts, murals, inscriptions
   - Historical revelations
   - Story clues
   - Pattern: "mural", "inscription", "text", "scroll", "lore", "history"

4. **NPC Alliances:**
   - Faction reputation gains ≥ +3
   - Major NPC trust established
   - Pattern: reputation_changes with value ≥ +3

### Report Format

```
ℹ️  EXPLORATION XP ANALYSIS

Act 1: Found 15 exploration XP opportunities
  - 5 major discoveries
    * "The Sunless Chasm" (Line 456)
    * "Hidden Myconid Grove" (Line 678)
    * "Khar-Morkai Gates" (Line 890)
  - 4 environmental puzzles
    * Dwarven rune lock (Line 234)
    * Chasm bridge mechanism (Line 567)
  - 6 lore discoveries
    * Ancient dwarven tablets (Line 345)
    * Korag's memory vision (Line 901)

Estimated total exploration XP: 1,200-1,500 per character (supplements 3,800 combat/quest XP)

No action needed - this is automatic! Just informing you of XP sources.
```

### No Fixes Needed

This is purely informational. The AI automatically detects and awards exploration XP when players encounter these moments.
```

---

## 3. Testing the Updated Tools

### Test Case 1: Campaign Creator Generates Level Gates

**Input:** "Create a 3-quest arc for levels 5-7 about hunting a vampire"

**Expected Output:**
```markdown
### **MAIN QUEST 1: The Village Murders**
\```yaml
recommended_level: 5
level_warning: null  # Starting quest
\```

### **MAIN QUEST 2: Track the Beast**
\```yaml
recommended_level: 6
level_warning: "Vampire spawn are faster and stronger than you expect. Many hunters never return."
\```

### **MAIN QUEST 3: Assault the Castle**
\```yaml
recommended_level: 7
level_warning: "The vampire lord has ruled for 300 years. His castle is a deathtrap for the unprepared."
\```
```

---

### Test Case 2: Campaign Validator Catches Missing Level Gate

**Input Campaign:**
```markdown
### **MAIN QUEST 5: The Dragon's Lair**
**Boss Encounter | 5000 XP | Session 8**

#### Quest Summary
The party finally reaches the ancient red dragon's lair...
```

**Expected Validation Output:**
```
⚠️  WARNING: Main Quest "The Dragon's Lair" missing recommended_level
   Location: Act 2, Line 1245
   Context: Boss encounter quest without level gate
   Suggestion: Add level gate (recommend level 9-10 for ancient red dragon)

   Fix:
   \```yaml
   recommended_level: 10
   level_warning: "Ancient red dragons have ended kingdoms. Your bones will join the hoard."
   \```
```

---

### Test Case 3: Companion Background Enhancement

**Input (Old Structure):**
```yaml
thaldrin_ironbeard:
  background:
    - Dwarven blacksmith from the mountains
    - Knows every forge and clan
    - Lost his family to orcs
```

**Campaign Creator Prompt:**
```
I notice this companion uses the old background structure.
Shall I enhance it for v6.8.0 Companion_Suggestion support? (yes/no)

Enhanced version:
\```yaml
background:
  keywords: ["local", "smith", "clan elder", "mountain native"]
  description: "Dwarven blacksmith who knows every forge and family in the mountains."
  details:
    - Dwarven blacksmith from the mountains
    - Knows every forge and clan
    - Lost his family to orcs

personal_quest_hook: "The orc chieftain who killed my family wears my father's hammer as a trophy. I'm taking it back."
\```

Use this enhanced version? (yes/no/modify)
```

---

## 4. Rollout Strategy

### Phase 1: Update Tools (Current)
- [ ] Add new sections to Campaign Creator
- [ ] Add new validation rules to Validator
- [ ] Test both tools with sample campaigns

### Phase 2: Update Existing Campaigns
- [ ] Act 1 updated ✅
- [ ] Act 2 level gates
- [ ] Act 3 level gates
- [ ] Run validator on all three acts

### Phase 3: New Campaign Template
- [ ] Create v6.8.0 campaign template with examples
- [ ] Document best practices
- [ ] Generate 1-2 sample campaigns using new tools

---

**Bottom Line:** These tool updates ensure all future campaigns automatically support v6.8.0 features! 🎲✨
