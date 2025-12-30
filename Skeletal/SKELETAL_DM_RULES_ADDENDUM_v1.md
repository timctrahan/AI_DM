# SKELETAL DM RULES ADDENDUM v1.0

## Purpose
Rules system pointers for campaigns not using D&D 5e default.
Copy relevant RULES_SYSTEM block into campaign file to override kernel defaults.
AI applies rules from its training - these blocks just identify WHICH system to use.

---

# D&D 5th EDITION (Kernel Default)

```yaml
RULES_SYSTEM:
  base: "D&D 5th Edition"
  health: "HP"
  resources: "Spell slots, class abilities"
  combat: "Initiative, action/bonus/reaction economy"
  progression: "XP thresholds or milestone"
  death: "Death saves DC 10"
  currency: "gp, sp, cp"
```

---

# CALL OF CTHULHU 7e

```yaml
RULES_SYSTEM:
  base: "Call of Cthulhu 7th Edition"
  health: "HP + Sanity"
  resources: "Luck points, ammo"
  combat: "Opposed percentile, simultaneous"
  progression: "Skill improvement through use"
  death: "Major Wound, Dying, Dead"
  currency: "Era-appropriate (1920s dollars, etc.)"
  special: "Sanity checks, temporary/indefinite insanity"
```

---

# BLADES IN THE DARK

```yaml
RULES_SYSTEM:
  base: "Blades in the Dark"
  health: "Harm track (4 levels)"
  resources: "Stress (0-9), Load, Coin"
  combat: "Position/Effect, action rolls (d6 pool)"
  progression: "XP triggers → playbook advances"
  death: "Level 4 harm, or trauma out"
  currency: "Coin (abstract)"
  special: "Flashbacks, Devil's Bargains, Resistance rolls, Clocks"
```

---

# CYBERPUNK RED

```yaml
RULES_SYSTEM:
  base: "Cyberpunk RED"
  health: "HP + Humanity"
  resources: "Ammo, Luck, Eddies"
  combat: "Initiative, Skill+STAT+d10 vs DV"
  progression: "IP → buy skill ranks"
  death: "Death Saves at 0 HP, critical injuries"
  currency: "Eurodollars (eddies)"
  special: "Netrunning, cyberware, autofire rules"
```

---

# VAMPIRE: THE MASQUERADE 5e

```yaml
RULES_SYSTEM:
  base: "Vampire: The Masquerade 5th Edition"
  health: "Health track + Willpower track (Superficial/Aggravated)"
  resources: "Hunger (0-5), Humanity"
  combat: "Contested pools, d10s"
  progression: "XP → traits"
  death: "Torpor, Final Death"
  currency: "Resources background or narrative"
  special: "Hunger dice, Messy Criticals, Bestial Failures, Frenzy"
```

---

# STAR WARS (FFG Narrative Dice)

```yaml
RULES_SYSTEM:
  base: "Star Wars FFG (Edge/Age/Force)"
  health: "Wounds + Strain"
  resources: "Destiny pool, credits"
  combat: "Initiative slots, narrative dice"
  progression: "XP → talents and skills"
  death: "Exceed threshold → incapacitated, crits can kill"
  currency: "Credits"
  special: "Narrative dice (Success/Advantage/Triumph/Despair), Force dice"
```

---

# PATHFINDER 2e

```yaml
RULES_SYSTEM:
  base: "Pathfinder 2nd Edition"
  health: "HP"
  resources: "Focus points, spell slots, Hero Points"
  combat: "Initiative, 3-action economy, MAP"
  progression: "XP thresholds (1000/level) or milestone"
  death: "Dying condition (1-4), Recovery checks"
  currency: "gp, sp, cp"
  special: "Degrees of success (crit/success/fail/crit fail), proficiency ranks"
```

---

# MONSTER OF THE WEEK

```yaml
RULES_SYSTEM:
  base: "Monster of the Week (PbtA)"
  health: "Harm (7 boxes)"
  resources: "Luck (7 uses lifetime), gear"
  combat: "Fiction-first, 2d6+stat moves"
  progression: "XP on 6- rolls → advances"
  death: "7 harm or luck out"
  currency: "Narrative"
  special: "Basic moves, playbook moves, mystery structure, Keeper moves"
```

---

# DREAD

```yaml
RULES_SYSTEM:
  base: "Dread (Jenga)"
  health: "Tower stability"
  resources: "None"
  combat: "Pull from tower for risky actions"
  progression: "None"
  death: "Tower falls = character dies"
  currency: "None"
  special: "Questionnaire characters, no dice"
```

---

# FATE CORE

```yaml
RULES_SYSTEM:
  base: "Fate Core"
  health: "Stress boxes + Consequences"
  resources: "Fate points, refresh"
  combat: "4dF + skill vs opposition"
  progression: "Milestones (minor/significant/major)"
  death: "Taken out when no stress/consequences remain"
  currency: "Resources skill or narrative"
  special: "Aspects, Fate points, Create Advantage, Compels"
```

---

# USAGE

To use an alternate rules system:

1. Copy the relevant RULES_SYSTEM block
2. Paste into your campaign file
3. Kernel detects override, AI applies that system's rules from training

The AI knows these systems. You're just telling it which one to use.

---

**END RULES ADDENDUM v1.0**
