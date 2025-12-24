# SECTION 2: WORLD RULES

## 2A. Faction Mechanics

### Faction Template
```yaml
faction_name: [Name]
faction_motivation: [One sentence: What do they WANT?]
faction_constraint: [One sentence: What stops them from just taking it?]

reputation_math:
  starting_value: 0
  scale: -10 to +10 (or appropriate range)

reputation_triggers:
  positive:
    - [Action that increases reputation]: +[amount]
    - [Action that increases reputation]: +[amount]

  negative:
    - [Action that decreases reputation]: -[amount]
    - [Action that decreases reputation]: -[amount]

  neutral:
    - [Action that doesn't change it]: +0

world_state_changes:
  at_reputation_5: [What becomes available?]
  at_reputation_-5: [What becomes hostile?]
  at_reputation_10: [What becomes true?]

# Add more factions below
```

### Faction Interaction Matrix
```
        | Faction A | Faction B | Faction C
--------|-----------|-----------|----------
Faction A|     -     |   [+1]    |   [-2]
Faction B|   [+1]    |     -     |   [+0]
Faction C|   [-2]    |   [+0]    |     -
```

*If party gains rep with A, what happens to B and C?*

## 2B. Economy & Resources

### Currency & Pricing
[What's the baseline economy? What does 1gp buy?]

### Supply & Scarcity
[What's abundant? What's rare? What's forbidden?]

### Consequence Chain
[If party spends X gold, what happens? Who notices? What changes?]

## 2C. Magic System Rules

### What Magic Can Do
[Explicit list of what's possible]

### What Magic Cannot Do
[Hard constraints]

### Consequence of Magic Use
[Who detects it? What's the fallout?]

## 2D. Social & Combat Rules

### NPC Reaction Triggers
[What makes NPCs trust/distrust/fear party?]

### Combat Difficulty Scaling
- **Easy:** [What does this feel like in narrative?]
- **Medium:** [What does this feel like?]
- **Hard:** [What does this feel like?]
- **Deadly:** [What does this feel like?]

### Resources That Matter
[HP, spells, gold, ammunition, provisions—which ones actually constrain player choices?]

---
