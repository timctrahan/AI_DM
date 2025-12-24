# Shadows of the Underdark

A **Skeletal Campaign** for AI Dungeon Masters, inspired by R.A. Salvatore's *Legend of Drizzt* series.

---

## 📖 Campaign Overview

**Play as iconic Drizzt characters** fleeing from destroyed drow houses, or **create your own heroes from scratch**.

- **Setting**: The deadly Underdark - Menzoberranzan and the wild depths below
- **Level Range**: 3 → 8
- **Acts**: 3 (The Fall, The Wandering, The Reckoning)
- **Theme**: What makes a monster - birth or choice?
- **Style**: Fast-paced Salvatore combat, moral clarity, found family bonds

---

## 🎭 Pre-Built Characters

Play as one of the **Companions of the Hall**:

1. **Drizzt Do'Urden** - The ranger seeking purpose beyond drow cruelty
2. **Bruenor Battlehammer** - Gruff dwarf clan leader who fights from the front
3. **Catti-brie** - Fierce archer and voice of reason
4. **Wulfgar** - Young barbarian torn between heritage and honor
5. **Regis** - Halfling rogue with deeper courage than he shows

Or create your own party of outcasts escaping the darkness!

---

## 🎯 What Makes This Campaign Special

### ✅ Skeletal Framework Design
- **Story gates** instead of rigid plot - AI adapts to your choices
- **Faction reputation system** - relationships evolve based on actions
- **Multiple endings** - triumphant, bittersweet, pyrrhic, dark, or surface-bound

### ✅ Underdark Survival Mechanics
- **Total darkness** - light attracts danger
- **Three-dimensional navigation** - tunnels twist in all directions
- **Scarce resources** - every meal and safe rest is earned
- **Faerzress zones** - wild magic radiation affects teleportation and divination

### ✅ Dynamic Faction Relationships
- **Drow Noble Houses** - rise through cruelty or fall through mercy
- **Deep Gnomes** - earn trust by protecting their people
- **Duergar** - negotiate through profit and power
- **The Outcasts** - forge found family with other refugees

---

## 🚀 Quick Start

### For AI Dungeon Masters

1. **Load the kernel**: Start with `SKELETAL_DM_KERNEL_v1.md`
2. **Load this campaign**: Then load `CAMPAIGN_Shadows_of_the_Underdark.md`
3. **Follow the startup sequence**: The campaign will guide character selection and opening

### For Players

- Choose a pre-built Companion or create your own character
- Decide whether to flee, fight, or find a new path in the Underdark
- Build relationships with factions through your actions
- Face the ultimate choice: what kind of hero will you become?

---

## 📂 Modular Structure

This campaign uses a **modular design** for easy maintenance:

```
shadows_of_the_underdark/
├── campaign_overview.md       # Setting, mechanics, factions, characters
├── act_1_the_fall.md          # The destruction and escape
├── act_2_the_wandering.md     # Settlement, threats, gathering strength
├── act_3_the_reckoning.md     # Final confrontation and endings
├── assemble_campaign.py       # Builds the complete campaign file
└── README.md                  # This file
```

**To modify**: Edit individual act files, then run `python assemble_campaign.py` to rebuild.

---

## 🎲 Campaign Features

- **3 Major Acts** with flexible story gates
- **4 Faction Templates** with reputation mechanics
- **5 Pre-Built Characters** scaled to level 3 start
- **5 Possible Endings** based on party choices
- **Underdark Survival Rules** for immersive gameplay
- **Faerzress Mechanics** for magical unpredictability

---

## 📜 Attribution

Inspired by **R.A. Salvatore's** *Legend of Drizzt* series, set in the **Forgotten Realms** Underdark.

This is a **fan-created skeletal framework** for AI-driven D&D sessions, designed for personal use. All rights to the Drizzt characters and Forgotten Realms setting belong to Wizards of the Coast and R.A. Salvatore.

---

## 🛠️ Technical Details

- **Campaign Version**: 1.0
- **Requires Kernel**: v1.0+
- **Format**: Markdown with YAML data blocks
- **Character Level**: 3-8 (milestone advancement)

---

## 📝 License

This skeletal campaign framework is provided for personal, non-commercial use. Drizzt, Forgotten Realms, and all related characters are property of Wizards of the Coast and R.A. Salvatore.

---

**Ready to escape the darkness? Your story begins now.**
