# Campaign Module Update Guide for v6.8.0

## Overview

Orchestrator v6.8.0 adds **optional** new features for quest level-gating, exploration XP, and companion suggestions. Existing campaigns work without changes, but you can enhance them by adding new fields.

---

## 1. Level-Gated Quests (OPTIONAL)

### Schema Changes

```yaml
quests: [{
  quest_id: "vault_assault",
  name: "Assault the Vault of Souls",
  quest_giver: "elder_miriam",
  description: "...",

  # NEW FIELDS (optional):
  recommended_level: 7,  # Party should be this level
  level_warning: "You sense the ancient power within would tear lesser heroes apart. The souls scream warnings in your mind.",

  objectives: [...]
}]
```

### When to Use

Add `recommended_level` to:
- ✅ **Main story quests** that advance the plot (prevents rushing endgame)
- ✅ **Dangerous dungeons** with high-CR enemies
- ✅ **Boss encounters** that could TPK under-leveled parties
- ❌ **Side quests** (let players tackle these at any level)
- ❌ **Social quests** (no combat risk)

### Example: Descent into Khar-Morkai

**Act 1 Quests** (Levels 4-5):
```yaml
- quest_id: "find_passage"
  name: "Find Passage to Khar-Morkai"
  recommended_level: 4  # Starting quest, no gate needed but good practice
  level_warning: null  # Use default warning

- quest_id: "cross_sunless_chasm"
  name: "Cross the Sunless Chasm"
  recommended_level: 5
  level_warning: "The chasm is said to be the grave of entire expeditions. Only experienced adventurers survive."
```

**Act 2 Quests** (Levels 5-7):
```yaml
- quest_id: "retrieve_vault_key_fragment_1"
  name: "The Priest's Sanctum"
  recommended_level: 6
  level_warning: "The sanctum's wards have killed many looters. Preparation is essential."

- quest_id: "confront_velryn_past"
  name: "Drow House Ambush"
  recommended_level: 7
  level_warning: "Drow assassins are relentless. You'll need every advantage."
```

**Act 3 Quests** (Levels 7-9):
```yaml
- quest_id: "breach_vault_wards"
  name: "Breach the Vault of Souls"
  recommended_level: 8
  level_warning: "Ten thousand tortured souls guard this place. Turn back if you value your sanity."

- quest_id: "the_impossible_choice"
  name: "The Final Choice"
  recommended_level: 9
  level_warning: "This is the culmination of everything. There is no turning back."
```

---

## 2. Exploration XP Integration (AUTOMATIC)

### No Campaign Changes Needed!

The `Exploration_XP_Award` protocol works automatically with your existing campaign structure.

### What Triggers Exploration XP

The AI will automatically award XP when players:
1. **Discover new locations** in your `locations[]` array
2. **Solve environmental puzzles** you describe in `interactable_objects[]`
3. **Make NPC alliances** tracked via reputation system
4. **Uncover lore** via `decision_trees[]` or quest objectives

### How to Design for Exploration XP

**In `locations[]`:**
```yaml
locations:
  - location_id: "hidden_myconid_grove"
    name: "Hidden Myconid Grove"
    description: "A secret fungal settlement deep in the caves."
    # Players get 100 XP (major_discovery) when they first find this

    interactable_objects:
      - object_id: "ancient_rune_lock"
        description: "A complex magical lock guards the inner sanctum."
        requires_check: true
        check_type: "Arcana"
        dc: 18
        success_info: "You decipher the runes and unlock the door."
        # Players get 75 XP (environmental_puzzle) when they solve this
```

**In `quests[]` objectives:**
```yaml
objectives:
  - objective_id: "translate_dwarven_tablets"
    description: "Translate the ancient dwarven tablets in the Priest's Sanctum"
    # When completed, players get 50 XP (lore_discovery) in addition to quest completion XP
```

### XP Scaling by Level

| Discovery Type | Level 1 | Level 5 | Level 10 |
|----------------|---------|---------|----------|
| Minor (chest, door) | 10 XP | 50 XP | 100 XP |
| Major (location) | 20 XP | 100 XP | 200 XP |
| Puzzle | 15 XP | 75 XP | 150 XP |

**Design Tip**: Don't worry about over-rewarding. Exploration XP is small compared to combat (a single CR 5 encounter = 1,800 XP).

---

## 3. Companion Suggestions (OPTIONAL)

### Schema Changes for Companions

```yaml
npcs:
  - npc_id: "velryn_duskmere"
    name: "Velryn Duskmere"
    role: "Companion - Scout"

    # EXISTING FIELDS (required):
    personality:
      traits: ["Cautious", "Haunted", "Protective"]
      background: "Drow exile, scout, local guide"  # IMPORTANT: Add keywords like "scout", "local", "guide"

    # NEW FIELD (optional):
    personal_quest_hook: "My sister's patrol hunts these tunnels. I need to warn her before it's too late."
```

### How It Works

After long rests, companions with **loyalty ≥ 3** have a **20% chance** to suggest side content:

**Priority 1 - Quest Hints** (if `active_quests` exist):
- Companion with `"local"` or `"guide"` in background suggests contacts
- Example: *"I know a merchant in Grakkul's Market who can get us into the vault. Want an introduction?"*

**Priority 2 - Location Exploration** (if unexplored areas):
- Companion suggests investigating `interactable_objects` or `connections`
- Example: *"I spotted tracks heading north. Might be worth investigating."*

**Priority 3 - Encounter Warnings** (if `random_encounters` exist):
- Companion warns of nearby threats
- Example: *"Duergar patrols have been spotted nearby. We should clear them before they find us."*

**Priority 4 - Personal Hooks** (if `personal_quest_hook` defined):
- Companion reveals backstory-related content
- Example: *"My sister's patrol hunts these tunnels. I need to warn her before it's too late."*

### Recommended Keywords for `background`

Add these to `personality.background` field:
- **"local"** - Companion knows the area (suggests NPCs, shortcuts)
- **"guide"** - Companion is hired guide (suggests safe paths, dangers)
- **"scout"** - Companion is tracker/ranger (suggests hidden areas, threats)
- **"native"** - Companion is from this region (suggests cultural insights)

### Example: Velryn Updated

```yaml
- npc_id: "velryn_duskmere"
  name: "Velryn Duskmere"
  role: "Companion - Drow Scout"
  location: "khar_morkai_gates"

  personality:
    traits: ["Cautious", "Haunted", "Protective", "Guilt-ridden"]
    background: "Drow exile and Underdark scout. Fled House Xaniqos after refusing assassination orders. Knows the deep tunnels like her own heartbeat."
    motivation: "Redemption through protecting surface-dwellers"
    speech_pattern: "Terse, military efficiency. Rarely jokes. Uses Undercommon curses."

  # LOYALTY TRACKING (already in your campaign):
  loyalty: 0  # Starts neutral, grows to 3+ (Friendly) over Act 1

  # NEW OPTIONAL FIELD:
  personal_quest_hook: "My sister Drissia leads a patrol in these tunnels. I must warn her before House Xaniqos sends her to kill you."

  quests_offered: ["escort_to_myconid_grove"]
```

**When this triggers:**
- After a long rest in Khar-Morkai (20% chance)
- Only if Velryn's loyalty ≥ 3 (player earned her trust)
- Velryn says: *"My sister's patrol hunts these tunnels. I need to warn her before it's too late."*
- Player chooses to pursue or ignore
- If pursued, AI narrates encounter with Drissia (dynamic, not pre-scripted)

---

## 4. Backward Compatibility

### Your Existing Campaigns Work As-Is! ✅

**All new fields are OPTIONAL:**
- ✅ Campaigns without `recommended_level` → No level warnings
- ✅ Campaigns without `personal_quest_hook` → Companions make generic suggestions
- ✅ Exploration XP → Works automatically with existing locations/quests

**No breaking changes. No mandatory updates.**

---

## 5. Recommended Update Strategy

### Step 1: Add Level Gates to Main Quests (5 minutes)

Go through your main story quests and add:
```yaml
recommended_level: [appropriate level]
level_warning: "[thematic warning]"  # Optional, can leave null for generic warning
```

**Quick Guide:**
- Act 1 finale: Starting level + 1
- Act 2 quests: Starting level + 2-3
- Act 3 quests: Starting level + 4-5
- Final boss: Ending level

### Step 2: Enhance Companion Backgrounds (10 minutes)

For each recruitable companion:
1. Add keywords to `background` field: "scout", "local", "guide", "native"
2. (Optional) Add `personal_quest_hook` if you want them to reveal backstory

### Step 3: Test in Game (30 minutes)

1. Load campaign into v6.8.0 orchestrator
2. Accept a quest with `recommended_level` → Verify warning appears
3. Take a long rest with companion loyalty ≥ 3 → Wait for suggestion (20% chance, may take a few rests)
4. Discover a new location → Verify exploration XP awarded

---

## 6. Example: Full Quest with All Features

```yaml
quests:
  - quest_id: "retrieve_vault_key_fragment_2"
    name: "The Mind Flayer Outpost"
    quest_giver: "korag_ironvow"

    # LEVEL GATING:
    recommended_level: 7
    level_warning: "Mind flayers are apex predators. Their psychic assaults shatter minds. Only the strong survive."

    description: "Korag reveals the second vault key fragment was stolen by illithids. Their outpost lies beyond the fungal wastes."

    objectives:
      - objective_id: "infiltrate_outpost"
        description: "Infiltrate the mind flayer outpost"
        # Exploration XP awarded when players first discover the outpost location

      - objective_id: "defeat_illithid_thralls"
        description: "Defeat the thrall guards"
        # Combat XP awarded as normal

      - objective_id: "decipher_elder_brain_visions"
        description: "Survive the Elder Brain's psychic assault and retrieve the fragment"
        # Exploration XP (lore_discovery) awarded when puzzle solved

    rewards:
      xp: 3000  # Quest completion bonus
      gold: 500
      items: ["vault_key_fragment_2"]
      reputation_changes:
        - type: "faction"
          target_id: "mindflayer_collective"
          value: -5  # Now hostile

    # COMPANION TRIGGER:
    # If Gralk (duergar) is in party with loyalty ≥ 3, he might suggest:
    # "I know a back entrance to the illithid outpost. My clan used it for raids. Safer than the front door."
```

---

## 7. FAQ

**Q: Do I HAVE to add `recommended_level` to all quests?**
A: No! It's optional. Only add it to quests you want to level-gate.

**Q: Can players still accept under-leveled quests?**
A: Yes! The orchestrator warns them but respects player agency. They can still say "yes" and proceed.

**Q: How often do companions make suggestions?**
A: 20% chance per long rest (1 in 5). Only companions with loyalty ≥ 3 participate.

**Q: Can I disable exploration XP?**
A: Not currently, but it's very small XP amounts (50-100 per discovery). It won't break progression.

**Q: What if my campaign has no companions?**
A: Companion_Suggestion gracefully skips if no eligible NPCs exist. No errors.

**Q: Can I make `level_warning` messages more dramatic?**
A: Absolutely! Make them thematic to your campaign:
  - Dark/gritty: *"The souls scream warnings. Only fools ignore them."*
  - Heroic/epic: *"Legends are forged by those who dare. Are you ready?"*
  - Cosmic horror: *"Your mind will fracture. Your body will fail. Turn back."*

---

## 8. Migration Checklist

### For "Descent into Khar-Morkai" Campaign

- [ ] Add `recommended_level` to 12 main quests (4 per act)
- [ ] Add `level_warning` to 6 dangerous quests (Chasm, Vault breach, etc.)
- [ ] Update Velryn's `background` with "scout" keyword
- [ ] Add `personal_quest_hook` to Velryn (sister Drissia)
- [ ] Update Gralk's `background` with "local" keyword (knows duergar tunnels)
- [ ] Add `personal_quest_hook` to Gralk (old clan grudge)
- [ ] Test quest acceptance with under-leveled party
- [ ] Test companion suggestion after long rest
- [ ] Verify exploration XP triggers on new location discovery

**Estimated time:** 30-45 minutes for full campaign update

---

## 9. Need Help?

**Issue**: Quest warnings not appearing
**Fix**: Check `recommended_level` is an integer, not string (`7` not `"7"`)

**Issue**: Companion never suggests anything
**Fix**: Verify companion has `loyalty >= 3` in current save file

**Issue**: Too many companion suggestions
**Fix**: This shouldn't happen (20% chance is low), but verify you're not manually triggering the protocol

**Issue**: Exploration XP seems too high/low
**Fix**: XP scales with level. Level 1 gets ~10-20 XP, Level 10 gets ~100-200 XP per discovery

---

**Bottom Line**: All features are **optional enhancements**. Your existing campaigns work perfectly as-is. Update when you have time! 🎲
