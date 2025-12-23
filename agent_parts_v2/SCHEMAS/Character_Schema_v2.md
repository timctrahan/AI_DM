# Character Schema v2.0

**Purpose**: Defines the structure for a single player character in the D&D 5E AI Orchestrator

**Format**: YAML-like pseudo-code (used in protocols, actual implementation can be JSON)

---

## Complete Schema

```yaml
Character_Schema_v2:
  metadata:
    version: "2.0"
    created: timestamp
    last_modified: timestamp
    campaign_id: string

  identity:
    name: string
    race: string
    class: string
    background: string
    alignment: string
    level: int (1-20)
    xp_current: int
    xp_next_level: int
    darkvision: bool
    darkvision_range: int (0 if false, 60/120 if true)

  abilities:
    strength:
      score: int (1-30)
      modifier: int
      save_proficient: bool
    dexterity:
      score: int (1-30)
      modifier: int
      save_proficient: bool
    constitution:
      score: int (1-30)
      modifier: int
      save_proficient: bool
    intelligence:
      score: int (1-30)
      modifier: int
      save_proficient: bool
    wisdom:
      score: int (1-30)
      modifier: int
      save_proficient: bool
    charisma:
      score: int (1-30)
      modifier: int
      save_proficient: bool

  combat_stats:
    hp_max: int
    hp_current: int
    temp_hp: int
    armor_class: int
    initiative_bonus: int
    speed: int
    proficiency_bonus: int
    hit_dice_total: string (e.g., "5d10")
    hit_dice_remaining: int
    death_saves:
      successes: int (0-3)
      failures: int (0-3)
    reaction_available: bool

  resources:
    spell_slots:
      level_1: {max: int, current: int}
      level_2: {max: int, current: int}
      level_3: {max: int, current: int}
      level_4: {max: int, current: int}
      level_5: {max: int, current: int}
      level_6: {max: int, current: int}
      level_7: {max: int, current: int}
      level_8: {max: int, current: int}
      level_9: {max: int, current: int}

    class_resources:
      - name: string (e.g., "Rage", "Ki Points", "Sorcery Points")
        max: int
        current: int
        reset_on: string ("short_rest" | "long_rest" | "dawn")

  inventory:
    gold: int
    equipment:
      - name: string
        type: string (weapon | armor | tool | misc)
        weight: float
        equipped: bool
        properties: object (weapon damage, armor AC, etc.)
    magic_items:
      - name: string
        type: string
        rarity: string
        attunement_required: bool
        attuned: bool
        charges: {max: int, current: int, recharge: string}
        properties: string
    ammo:
      - type: string (e.g., "arrows", "crossbow bolts")
        count: int
    carrying_weight: int

  survival:
    provisions: int (days of food)
    water: int (days of water)
    days_without_food: int
    days_without_water: int
    active_light_sources:
      - type: string (torch | lantern | magic light)
        remaining_duration: int (in minutes)

  proficiencies:
    armor: [string] (e.g., ["light", "medium", "shields"])
    weapons: [string] (e.g., ["simple", "martial"])
    tools: [string] (e.g., ["thieves' tools", "smith's tools"])
    skills:
      - name: string (e.g., "Perception", "Stealth")
        proficient: bool
        expertise: bool

  spells:
    spellcasting_ability: string ("int" | "wis" | "cha" | null)
    spell_save_dc: int
    spell_attack_bonus: int
    spells_known:
      - name: string
        level: int (0-9, 0 = cantrip)
        school: string
        prepared: bool (always true for cantrips)

  conditions:
    active: [string] (e.g., ["poisoned", "frightened", "exhaustion_1"])

  features:
    racial_features: [string]
    class_features: [string]
    feats: [string]

  notes:
    personality_traits: string
    ideals: string
    bonds: string
    flaws: string
    backstory: string (optional, for RP)
```

---

## Field Descriptions

### Metadata
- `version`: Schema version (for migration tracking)
- `created`: Timestamp when character was created
- `last_modified`: Last update timestamp
- `campaign_id`: Links character to specific campaign

### Identity
- `name`: Character name
- `race`: D&D race (Human, Elf, Dwarf, etc.)
- `class`: D&D class (Fighter, Wizard, Rogue, etc.)
- `background`: Character background (Soldier, Acolyte, Criminal, etc.)
- `alignment`: Two-axis alignment (LG, NG, CG, LN, N, CN, LE, NE, CE)
- `level`: Current character level (1-20)
- `xp_current`: Current XP total
- `xp_next_level`: XP required for next level
- `darkvision`: Whether character has darkvision
- `darkvision_range`: Range in feet (0, 60, or 120)

### Abilities
Standard D&D 5E ability scores with:
- `score`: Raw ability score (1-30)
- `modifier`: Calculated as `FLOOR((score - 10) / 2)`
- `save_proficient`: Whether proficient in this saving throw

### Combat Stats
- `hp_max`: Maximum hit points
- `hp_current`: Current hit points
- `temp_hp`: Temporary hit points
- `armor_class`: AC value
- `initiative_bonus`: Initiative modifier
- `speed`: Movement speed in feet
- `proficiency_bonus`: Based on level (+2 to +6)
- `hit_dice_total`: Hit dice formula (e.g., "5d10" for 5th-level Fighter)
- `hit_dice_remaining`: Unused hit dice
- `death_saves`: Successes and failures (0-3 each)
- `reaction_available`: Whether reaction has been used this round

### Resources
- `spell_slots`: Spell slots per level (max and current)
- `class_resources`: Class-specific resources (Rage, Ki, Bardic Inspiration, etc.)

### Inventory
- `gold`: Gold pieces (individual, not party shared)
- `equipment`: Weapons, armor, tools, misc items
- `magic_items`: Magic items with charges and attunement
- `ammo`: Arrows, bolts, etc.
- `carrying_weight`: Total weight carried (for encumbrance)

### Survival
- `provisions`: Days of food remaining
- `water`: Days of water remaining
- `days_without_food`: Tracker for exhaustion from starvation
- `days_without_water`: Tracker for exhaustion from dehydration
- `active_light_sources`: Torches, lanterns with remaining duration

### Proficiencies
- `armor`: Armor proficiencies
- `weapons`: Weapon proficiencies
- `tools`: Tool proficiencies
- `skills`: Skill proficiencies and expertise

### Spells
- `spellcasting_ability`: Primary stat for spellcasting
- `spell_save_dc`: Save DC for spells
- `spell_attack_bonus`: Attack bonus for spell attacks
- `spells_known`: All spells character knows (prepared status tracked)

### Conditions
- `active`: Array of active conditions (poisoned, frightened, exhaustion levels)

### Features
- `racial_features`: Features from race (e.g., "Dwarven Resilience")
- `class_features`: Features from class (e.g., "Second Wind", "Action Surge")
- `feats`: Feats taken (if any)

### Notes
- `personality_traits`: RP personality
- `ideals`: RP ideals
- `bonds`: RP bonds
- `flaws`: RP flaws
- `backstory`: Optional backstory for RP

---

## Example Character: Thorin Ironforge

```yaml
metadata:
  version: "2.0"
  created: "2025-12-19T10:00:00Z"
  last_modified: "2025-12-19T14:30:00Z"
  campaign_id: "descent_into_khar_morkai"

identity:
  name: "Thorin Ironforge"
  race: "Dwarf (Mountain)"
  class: "Fighter"
  background: "Soldier"
  alignment: "LG"
  level: 5
  xp_current: 7500
  xp_next_level: 14000
  darkvision: true
  darkvision_range: 60

abilities:
  strength:
    score: 16
    modifier: +3
    save_proficient: true
  dexterity:
    score: 14
    modifier: +2
    save_proficient: false
  constitution:
    score: 15
    modifier: +2
    save_proficient: true
  intelligence:
    score: 10
    modifier: 0
    save_proficient: false
  wisdom:
    score: 12
    modifier: +1
    save_proficient: false
  charisma:
    score: 8
    modifier: -1
    save_proficient: false

combat_stats:
  hp_max: 52
  hp_current: 45
  temp_hp: 0
  armor_class: 18
  initiative_bonus: +2
  speed: 25
  proficiency_bonus: +3
  hit_dice_total: "5d10"
  hit_dice_remaining: 3
  death_saves:
    successes: 0
    failures: 0
  reaction_available: true

resources:
  spell_slots: null (non-caster)
  class_resources:
    - name: "Second Wind"
      max: 1
      current: 0
      reset_on: "short_rest"
    - name: "Action Surge"
      max: 1
      current: 1
      reset_on: "short_rest"

inventory:
  gold: 45
  equipment:
    - name: "Longsword +1"
      type: "weapon"
      weight: 3
      equipped: true
      properties: {damage: "1d8+1", type: "slashing", versatile: "1d10+1"}
    - name: "Plate Armor"
      type: "armor"
      weight: 65
      equipped: true
      properties: {ac: 18, stealth_disadvantage: true}
    - name: "Shield"
      type: "armor"
      weight: 6
      equipped: true
      properties: {ac_bonus: +2}
  magic_items: []
  ammo: []
  carrying_weight: 120

survival:
  provisions: 5
  water: 5
  days_without_food: 0
  days_without_water: 0
  active_light_sources:
    - type: "torch"
      remaining_duration: 50

proficiencies:
  armor: ["light", "medium", "heavy", "shields"]
  weapons: ["simple", "martial"]
  tools: ["smith's tools"]
  skills:
    - {name: "Athletics", proficient: true, expertise: false}
    - {name: "Intimidation", proficient: true, expertise: false}
    - {name: "Perception", proficient: true, expertise: false}
    - {name: "Survival", proficient: true, expertise: false}

spells: null (non-caster)

conditions:
  active: ["exhaustion_1"]

features:
  racial_features: ["Dwarven Resilience", "Stonecunning"]
  class_features: ["Fighting Style (Defense)", "Second Wind", "Action Surge", "Extra Attack"]
  feats: []

notes:
  personality_traits: "Loyal to allies, gruff exterior"
  ideals: "Honor above all"
  bonds: "Searching for family heirloom lost in Khar-Morkai"
  flaws: "Stubborn, refuses to retreat"
  backstory: "Former city guard, ventured into the Dead City seeking redemption"
```

---

## Validation Rules

When loading or modifying character state, validate:

1. **HP Constraints**:
   - `0 <= hp_current <= hp_max`
   - `temp_hp >= 0`

2. **Spell Slot Constraints**:
   - `0 <= current <= max` for all spell levels

3. **Ability Score Constraints**:
   - `1 <= score <= 30`

4. **Death Save Constraints**:
   - `0 <= successes <= 3`
   - `0 <= failures <= 3`
   - If `hp_current == 0`, death saves should be active

5. **Level Constraints**:
   - `1 <= level <= 20`
   - `proficiency_bonus` matches level (see reference table)

6. **XP Constraints**:
   - `xp_current >= xp_for_current_level`
   - `xp_current < xp_next_level`

7. **Conditions**:
   - Only valid D&D 5E conditions in `active` array
   - Exhaustion represented as "exhaustion_1" through "exhaustion_6"

---

## Usage in Protocols

### Reading Character Data
```yaml
# Get character HP
current_hp = party_state.characters[0].combat_stats.hp_current
max_hp = party_state.characters[0].combat_stats.hp_max

# Check spell slots
level3_slots = party_state.characters[0].resources.spell_slots.level_3.current
```

### Modifying Character Data
```yaml
# Deal damage
character.combat_stats.hp_current -= damage_taken

# Use spell slot
character.resources.spell_slots.level_3.current -= 1

# Award XP
character.identity.xp_current += xp_gained
IF character.identity.xp_current >= character.identity.xp_next_level:
  CALL proto_level_up
```

---

**Version**: 2.0.0
**Last Updated**: 2025-12-19
**Compatible With**: Protocol Library v2.0+, Campaign Data Vault v2.0+
