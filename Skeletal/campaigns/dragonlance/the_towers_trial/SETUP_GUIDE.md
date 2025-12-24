# 🎲 The Tower's Trial - Setup Guide

## ✅ What We've Created

Your campaign has been successfully broken into modular parts and is ready to use!

### 📁 File Structure

```
campaigns/dragonlance/the_towers_trial/
│
├── 📄 README.md                        # Commercial "sales pitch" for the campaign
├── 📄 SETUP_GUIDE.md                   # This file - setup instructions
│
├── 🎯 CAMPAIGN PARTS (Modular)
│   ├── campaign_overview.md           # Metadata, setting, mechanics, NPCs (16 KB)
│   ├── act_1_frozen_token.md          # Icewall Glacier, Levels 5-7 (9.5 KB)
│   ├── act_2_poisoned_token.md        # Eastern Swamps, Levels 7-9 (13 KB)
│   ├── act_3_corrupted_token.md       # Silvanesti, Levels 9-11 (15 KB)
│   ├── act_4_storm_token.md           # Desert of Khur, Levels 11-13 (17 KB)
│   └── act_5_flame_token.md           # Lords of Doom, Levels 13-15 (23 KB)
│
├── 🔧 TOOLS
│   └── assemble_campaign.py           # Python script to combine parts (7.6 KB)
│
└── 📦 OUTPUT
    └── CAMPAIGN_The_Towers_Trial.md   # Complete assembled campaign (93 KB)
```

**Total Size**: ~224 KB across all files

---

## 🚀 Quick Start (3 Steps)

### Step 1: Assemble the Campaign

```bash
cd "C:\GitRepos\AI_DM\Skeletal\campaigns\dragonlance\the_towers_trial"
python assemble_campaign.py
```

This creates the complete `CAMPAIGN_The_Towers_Trial.md` file.

### Step 2: Load into AI DM

1. Load your DM kernel first: `SKELETAL_DM_KERNEL_v1.md`
2. Then load: `CAMPAIGN_The_Towers_Trial.md`

### Step 3: Start Playing!

The campaign will guide you through character selection and opening scenes.

---

## 🛠️ Working with Modular Parts

### Why Modular?

The campaign is split into parts so you can:

- ✅ **Edit individual acts** without touching the whole campaign
- ✅ **Customize specific sections** for your table
- ✅ **Replace acts** with your own content
- ✅ **Share specific parts** without the whole campaign
- ✅ **Version control** more easily (smaller diffs)

### How to Edit

1. **Open the part you want to edit** (e.g., `act_2_poisoned_token.md`)
2. **Make your changes**
3. **Save the file**
4. **Reassemble**: `python assemble_campaign.py`
5. **Use the new assembled file** in your AI DM

### Assembly Script Options

```bash
# Validate all parts exist (doesn't assemble)
python assemble_campaign.py --validate

# Assemble to default output
python assemble_campaign.py

# Assemble to custom filename
python assemble_campaign.py --output my_custom_campaign.md

# Generate with table of contents
python assemble_campaign.py --toc

# Show help
python assemble_campaign.py --help
```

---

## 📖 What's in Each Part?

### `campaign_overview.md`
- Campaign metadata and version info
- Setting anchors (Dragonlance lore)
- Custom mechanics (Corruption, Moon Magic, Draconians)
- World mechanics and Dragon Domains
- Faction templates (Conclave, Knights, Dragonarmies, Elves)
- The Rival NPC system
- Campaign endings (6 variants)
- Default party (Heroes of the Lance)
- Startup sequence
- Reference tables

### `act_1_frozen_token.md` (Icewall Glacier)
- Story Gates 1.1-1.3
- White Dragon encounter (Sleetfang)
- Ice hazards and survival mechanics
- Ice Folk barbarians
- Draconian patrols
- Rival introduction
- Token: Shard of Winter's Heart

### `act_2_poisoned_token.md` (Swamps of Endless Night)
- Story Gates 2.1-2.3
- Black Dragon encounter (Onyx Fang)
- Disease and poison mechanics
- Lizardfolk tribes
- Drowned temple infiltration
- Dragon's moral dilemma (the Deal)
- Token: The Venom Chalice

### `act_3_corrupted_token.md` (Silvanesti)
- Story Gates 3.1-3.3
- Green Dragon encounter (Cyan Bloodbane)
- Nightmare reality mechanics
- Lorac's tragedy and the Dragon Orb
- Tower of Stars exploration
- Illusion and dream combat
- Token: The Emerald Eye

### `act_4_storm_token.md` (Desert of Khur)
- Story Gates 4.1-4.3
- Blue Dragon encounter (Skie)
- Kitiara confrontation (if using Heroes of Lance)
- Dragonarmy infiltration
- Storm Keep assault
- Resistance fighters
- Token: The Stormcaller's Horn

### `act_5_flame_token.md` (Lords of Doom)
- Story Gates 5.1-5.4
- Ancient Red Dragon encounter (Pyrothraxus)
- Fistandantilus's final offer
- Volcanic hazards
- Ultimate battle mechanics
- All six campaign endings
- Token: The Heart of the Inferno
- Return to Conclave and final choice

---

## 🎯 Campaign Flow

```
START (Level 5)
    ↓
[CONCLAVE SUMMONS]
    ↓
ACT 1: ICEWALL GLACIER (5→7)
    ↓
ACT 2: EASTERN SWAMPS (7→9)
    ↓
ACT 3: SILVANESTI (9→11)
    ↓
ACT 4: DESERT OF KHUR (11→13)
    ↓
ACT 5: LORDS OF DOOM (13→15)
    ↓
[RETURN TO CONCLAVE]
    ↓
ENDING (based on Corruption)
```

**Total Duration**: 25-35 sessions (3-4 hours each)

---

## ⚙️ Customization Examples

### Example 1: Change Act Order

Edit `assemble_campaign.py`:

```python
PARTS = [
    "campaign_overview.md",
    "act_2_poisoned_token.md",  # Swapped!
    "act_1_frozen_token.md",    # Swapped!
    "act_3_corrupted_token.md",
    "act_4_storm_token.md",
    "act_5_flame_token.md"
]
```

### Example 2: Add Custom Act

1. Create `act_custom_bonus.md`
2. Edit `assemble_campaign.py`:

```python
PARTS = [
    "campaign_overview.md",
    "act_1_frozen_token.md",
    "act_2_poisoned_token.md",
    "act_custom_bonus.md",  # Your addition!
    "act_3_corrupted_token.md",
    "act_4_storm_token.md",
    "act_5_flame_token.md"
]
```

### Example 3: Adjust Dragon Difficulty

Edit the specific act file (e.g., `act_1_frozen_token.md`):

Find the dragon stat block:
```yaml
SLEETFANG:
  HP: 200  # Change to 150 for easier fight
```

Reassemble and use!

---

## 📊 Key Campaign Metrics

| Metric | Value |
|--------|-------|
| **Level Range** | 5 → 15 |
| **Total Acts** | 5 |
| **Story Gates** | 17 |
| **Dragon Fights** | 5 (CR 13-24) |
| **Endings** | 6 unique |
| **Factions** | 4 tracked |
| **Party Size** | 4-6 players |
| **Est. Sessions** | 25-35 |

---

## 🔍 What to Read First

As a DM preparing to run this:

1. **README.md** - Understand the campaign pitch and themes
2. **campaign_overview.md** - Learn mechanics and NPCs
3. **act_1_frozen_token.md** - Prepare the first act
4. **Skim remaining acts** - Get a sense of the arc

Don't try to memorize everything! The modular structure lets you prep act-by-act.

---

## 💡 Pro Tips

### For DMs

- 📌 **Track Corruption Openly** - Let players see the meter, creates tension
- 📌 **Make Fistandantilus Seductive** - Not just evil, *tempting*
- 📌 **Use Rival Consistently** - They should appear every act
- 📌 **Adjust Dragon HP** - Scale based on party performance
- 📌 **Foreshadow Endings** - Let players see where they're heading

### For Customization

- 💾 **Keep Original Files** - Make backups before editing
- 💾 **Comment Changes** - Add notes about what you modified
- 💾 **Version Your Edits** - Use descriptive output filenames
- 💾 **Test Assembly** - Always run `--validate` after editing

### For Players

- 🎲 **Embrace Moral Complexity** - There are no perfect choices
- 🎲 **Roleplay Corruption** - Show gradual changes in behavior
- 🎲 **Use Companion Bonds** - They're your anchor against darkness
- 🎲 **Track Your Choices** - Keep notes on major decisions

---

## ❓ Troubleshooting

### "Python command not found"

Install Python 3.7+ from [python.org](https://python.org)

### "UnicodeEncodeError when running script"

Already fixed! The script now uses `[OK]` instead of Unicode checkmarks.

### "Missing part file"

Run `python assemble_campaign.py --validate` to see which files are missing.

### "Campaign seems unbalanced"

Dragon CR ratings assume:
- Party of 4-6 players
- Standard magic item distribution
- Tactical play

Adjust dragon HP/minions as needed!

---

## 📚 Additional Resources

### Dragonlance References

- **Chronicles Trilogy** - Original novels by Weis & Hickman
- **Legends Trilogy** - Raistlin's story continues
- **DL Campaign Setting** - Official D&D sourcebook

### Game Mechanics

- **Player's Handbook** - Core D&D rules
- **Monster Manual** - Dragon stat blocks (adjust as needed)
- **Dungeon Master's Guide** - Running the game

---

## 🎉 You're Ready!

Everything is set up and ready to go. The campaign is modular, customizable, and assembled.

**Next Steps:**

1. ✅ Files created and organized
2. ✅ Assembly script working
3. ✅ Complete campaign assembled
4. 🎯 **Load into your AI DM and begin!**

---

## 📞 Support

If you modify the campaign and want to share:
- Keep the modular structure
- Document your changes
- Consider sharing your custom acts!

---

<p align="center">
  <strong>The Tower awaits. The dragons are ready. The corruption meter starts at 25.</strong><br>
  <em>What will you become in the pursuit of power?</em>
</p>

---

**Happy Gaming!** 🎲✨
