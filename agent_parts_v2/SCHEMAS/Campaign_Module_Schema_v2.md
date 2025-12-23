# Campaign Module Schema v2.0

**Purpose**: Defines the structure for Campaign Data Vault modules

**Format**: Markdown with MODULE_START/END tags wrapping content

---

## Module Format

All modules in the Campaign Data Vault follow this pattern:

```markdown
[MODULE_START: {module_id}]
{module_content}
[MODULE_END: {module_id}]
```

---

## Module ID Conventions

| Entity Type | ID Format | Example |
|-------------|-----------|---------|
| Overview/Intro | `_{act_name}_overview` | `_act2_dead_city_overview` |
| Main Quest | `quest_mq{number}_{name}` | `quest_mq2_three_fragments` |
| Side Quest | `quest_sq{number}_{name}` | `quest_sq1_architects_map` |
| Location | `loc_{location_name}` | `loc_main_street` |
| NPC | `npc_{npc_name}` | `npc_zilvra_shadowveil` |
| Encounter | `enc_{encounter_name}` | `enc_undead_patrol` |
| Item | `item_{item_name}` | `item_soulforge_shard` |
| Faction | `faction_{faction_name}` | `faction_house_shadowveil` |
| Custom | `{type}_{name}` | `timeline_khar_morkai_fall` |

**Normalization Rules**:
- All lowercase
- Spaces → underscores
- Remove special characters
- No leading/trailing underscores

---

## Master Index Structure

Every Campaign Data Vault must start with a `[MASTER_INDEX]`:

```yaml
[MASTER_INDEX]
overview:
  - _act2_dead_city_overview
  - _campaign_intro

main_quests:
  - quest_mq1_mapping_the_dead
  - quest_mq2_three_fragments
  - quest_mq3_hunters_in_dark
  - quest_mq4_outer_sanctum

side_quests:
  - quest_sq1_architects_map
  - quest_sq2_volunteers_plea
  ... (all side quests)

locations:
  - loc_main_street
  - loc_artisan_quarter
  ... (all locations)

npcs:
  - npc_zilvra_shadowveil
  - npc_xalaphex_aberrant_devourer
  ... (all NPCs)

encounters:
  - enc_undead_patrol
  - enc_helmed_horrors
  ... (all encounters)

items:
  - item_soulforge_shard
  ... (all key items)

factions:
  - faction_house_shadowveil
  ... (all factions)
```

---

## Module Content Schemas

### Overview Module

```markdown
[MODULE_START: _act2_dead_city_overview]
### ACT 2: THE DEAD CITY - OVERVIEW

**Campaign**: {campaign_name}
**Act Number**: {number} of {total}
**Recommended Party Level**: {min}-{max}

**Tone**: {tone_keywords} (e.g., moral_corruption | choosing_lesser_evils)

**Core Themes**:
- {theme 1}
- {theme 2}
- {theme 3}

**Story Summary**:
{2-3 paragraphs describing the act's narrative arc}

**Victory Conditions**:
1. {condition 1}
2. {condition 2}
...

**Defeat Conditions**:
1. {condition 1}
2. {condition 2}
...

**Starting Location**: `{location_id}`

**Starting Conditions**:
- {condition 1}
- {condition 2}
...

**Environmental Hazards**:
- **{Hazard Name}**: {description, DC, effect}

**Key Flags for This Act**:
```yaml
act_flags:
  flag_name: default_value
  ...
```

**Reputation System**:
{description of faction/NPC reputation mechanics}

**Act Completion Trigger**:
{conditions that signal act completion}
[MODULE_END: _act2_dead_city_overview]
```

---

### Quest Module

```markdown
[MODULE_START: quest_mq2_three_fragments]
### MAIN QUEST 2: {Quest Title}

**Quest ID**: {quest_id}
**Type**: Main Quest | Side Quest
**Level Range**: {min}-{max}
**Estimated Duration**: {sessions or hours}

**Objective**:
{concise 1-2 sentence objective}

**Structure**: {linear | non-linear | branching}

**Hook**:
{How the party learns about this quest}

**Detailed Steps**:
1. **{Step Name}**:
   - Location: `{location_id}`
   - Objective: {what needs to be done}
   - Non-Combat Solution: {DC checks, persuasion, etc.}
   - Combat Solution: {enemy details, CR, difficulty}
   - Skill Solution: {alternative skill checks}
   - Loot: {rewards for this step}
   - Reputation: {reputation changes}

2. **{Step Name}**:
   ...

**Quest Completion**:
- **Trigger**: {what completes the quest}
- **Effect**: {consequences of completion}
- **XP Award**: {total XP, broken down by objectives}
- **Rewards**: {gold, items, reputation, unlocks}

**Flags Updated**:
```yaml
quest_flags:
  quest_completed: true
  specific_flag: true/false
```

**Failure Conditions**:
- {condition that fails quest}

**Notes**:
{DM guidance on running this quest}
[MODULE_END: quest_mq2_three_fragments]
```

---

### Location Module

```markdown
[MODULE_START: loc_main_street]
### LOCATION: {Location Name}

**ID**: {location_id}
**Region**: {region_name}
**Type**: {urban | dungeon | wilderness | etc.}
**Lighting**: {bright | dim | darkness | magical}
**Atmosphere**: {mood keywords}

**Description**:
{2-3 paragraphs of sensory description}

**Connections**:
- North: {location_name} (`{location_id}`)
- East: {location_name} (`{location_id}`)
- South: {location_name} (`{location_id}`)
- West: {location_name} (`{location_id}`)

**Hazards**:
- **{Hazard Name}**: {DC, save type, damage/effect}

**Points of Interest**:
1. **{POI Name}** - {description}
   - Investigation DC {number}: {what's found}
   - Interaction: {what players can do}

2. **{POI Name}** - {description}
   ...

**NPCs Present**:
- `{npc_id}` - {role/activity}

**Random Encounter Table** (optional):
- Roll 1d6 every {time period}:
  - 1-3: No encounter
  - 4-5: `{enc_id}` ({description})
  - 6: `{enc_id}` ({description})

**First Visit Narrative**:
{What the party sees/experiences on first arrival}

**DM Notes**:
{Guidance on running this location}
[MODULE_END: loc_main_street]
```

---

### NPC Module

```markdown
[MODULE_START: npc_zilvra_shadowveil]
### NPC: {NPC Name}

**ID**: {npc_id}
**Role**: {Ally | Antagonist | Quest Giver | Merchant | Neutral}
**Race**: {race}
**Class**: {class} (if applicable)
**Alignment**: {alignment}
**CR**: {CR} (if combatant)

**Appearance**:
{2-3 sentences of physical description}

**Personality Traits**:
- {trait 1}
- {trait 2}
- {trait 3}

**Goals**:
1. {goal 1}
2. {goal 2}
...

**Relationship to Party**: {starting relationship → potential evolution}

**Relationship to Other NPCs** (if relevant):
- **{npc_name}**: {relationship description}

**Key Dialogue Samples**:

*{Situation 1}:*
> "{dialogue sample 1}"

*{Situation 2}:*
> "{dialogue sample 2}"

*{Situation 3}:*
> "{dialogue sample 3}"

**Combat Behavior** (if combatant):
- **Tactics**: {combat strategy}
- **Fight to Death?**: {yes/no, conditions for retreat}
- **Accompanied by**: {minions/allies}

**Quest Hooks** (if quest giver):
- **{Quest Name}** (`{quest_id}`): {brief description}

**Moral Weight** (for complex NPCs):
{Description of moral dilemma this NPC presents}

**Flags**:
```yaml
npc_flags:
  met: false
  reputation: 0
  quest_given: false
  custom_flag: false
```

**DM Notes**:
{Guidance on roleplaying this NPC}

**Loot** (if defeated):
- {item 1}
- {item 2}
...
[MODULE_END: npc_zilvra_shadowveil]
```

---

### Encounter Module

```markdown
[MODULE_START: enc_undead_patrol]
### ENCOUNTER: {Encounter Name}

**ID**: {enc_id}
**Type**: {combat | trap | puzzle | social}
**Difficulty**: {Easy | Medium | Hard | Deadly | Extreme}
**CR**: {total CR}

**Trigger**:
{What causes this encounter to occur}

**Setup**:
{Initial positioning, environment, conditions}

**Enemies** (if combat):
- **{Enemy Name}** x{count}: CR {CR} ({source} p.{page})
  - HP: {hp}
  - AC: {ac}
  - Key Abilities: {abilities}
  - Tactics: {how this enemy fights}

**Trap** (if trap):
- **Detection**: {Perception/Investigation DC}
- **Trigger**: {what triggers it}
- **Effect**: {damage, save, DC}
- **Disable**: {Thieves' Tools DC, or alternative}

**Puzzle** (if puzzle):
- **Description**: {what players see}
- **Solution**: {how to solve}
- **Hints**: {clues available}
- **Failure**: {what happens if unsolved}

**XP Reward**: {total XP}

**Loot**:
- {item 1}
- {item 2}
- {gold amount}

**Flags Updated**:
```yaml
encounter_flags:
  encounter_defeated: true
  custom_flag: value
```

**DM Notes**:
{Guidance on running this encounter}
[MODULE_END: enc_undead_patrol]
```

---

### Item Module

```markdown
[MODULE_START: item_soulforge_shard]
### ITEM: {Item Name}

**ID**: {item_id}
**Type**: {weapon | armor | wondrous | consumable | key_item}
**Rarity**: {common | uncommon | rare | very rare | legendary | artifact}
**Attunement**: {required | not required}

**Description**:
{Physical description, history, lore}

**Properties**:
- **{Property 1}**: {effect}
- **{Property 2}**: {effect}
...

**Charges** (if applicable):
- Max: {number}
- Recharge: {dawn | dusk | 1d6 charges at dawn | never}

**Quest Relevance**:
{How this item relates to quests or story}

**Value**: {gp value}
**Weight**: {lbs}

**Found**:
{Where/how the party obtains this item}
[MODULE_END: item_soulforge_shard]
```

---

### Faction Module

```markdown
[MODULE_START: faction_house_shadowveil]
### FACTION: {Faction Name}

**ID**: {faction_id}
**Type**: {guild | government | religious | criminal | etc.}
**Alignment**: {faction alignment}
**Size**: {local | regional | kingdom-wide | international}

**Description**:
{2-3 paragraphs about the faction's history, goals, structure}

**Leadership**:
- **{Title}**: `{npc_id}` - {name}
- **{Title}**: `{npc_id}` - {name}

**Goals**:
1. {goal 1}
2. {goal 2}
...

**Methods**:
{How the faction operates, tactics, philosophy}

**Reputation Levels**:
- **-10 to -5 (Enemy)**: {consequences}
- **-4 to +1 (Neutral)**: {standard interaction}
- **+2 to +5 (Affiliated)**: {benefits}
- **+6 to +10 (Leadership)**: {special benefits}

**Quests Offered**:
- `{quest_id}` (available at reputation {threshold})

**Resources**:
{What the faction can provide to allies}

**Enemies**:
- `{faction_id}` - {relationship}

**Allies**:
- `{faction_id}` - {relationship}

**Flags**:
```yaml
faction_flags:
  encountered: false
  reputation: 0
  rank: null
```
[MODULE_END: faction_house_shadowveil]
```

---

## Retrieval Examples

### Retrieving a Module

When the AI needs NPC dialogue:
```yaml
1. Player says: "I want to talk to Zilvra"
2. Execution Loop identifies: target = NPC
3. Kernel calls: Internal_Context_Retrieval("npc_zilvra_shadowveil")
4. Search conversation for: [MODULE_START: npc_zilvra_shadowveil]
5. Extract all content until: [MODULE_END: npc_zilvra_shadowveil]
6. Load into working memory
7. Generate dialogue using personality, goals, and dialogue samples
```

### Cross-Referencing Modules

Modules can reference other modules by ID:

```markdown
**Quest Giver**: `npc_gralk_the_merchant`
**Location**: `loc_artisan_quarter`
**Rewards**: `item_soulforge_shard`
```

When AI encounters these references, it can retrieve those modules for additional context.

---

## Validation Rules

When creating or validating a Campaign Data Vault:

1. **All module IDs in [MASTER_INDEX] must have corresponding MODULE_START/END blocks**
2. **All MODULE_START tags must have matching MODULE_END tags**
3. **Module IDs must be unique** (no duplicates)
4. **Module IDs must follow naming conventions** (lowercase, underscores)
5. **All internal references** (to NPCs, locations, quests) should use valid module IDs
6. **Quest modules must specify XP rewards**
7. **NPC modules should include dialogue samples**
8. **Location modules should specify connections**

---

## Best Practices

### Rich Content
- **NPCs**: Include at least 3 dialogue samples for different situations
- **Locations**: Use sensory details (sight, sound, smell, temperature)
- **Quests**: Provide multiple solution paths (combat, skill, social)

### Consistency
- **Tone keywords**: Use consistent tone descriptors across modules
- **CR ratings**: Ensure encounter difficulty matches recommended level
- **Flags**: Use consistent flag naming (e.g., `{entity}_met`, `{entity}_defeated`)

### Cross-References
- **Link modules**: Reference related NPCs, locations, quests by ID
- **Build connections**: Show how NPCs know each other, locations connect, quests chain

### Flexibility
- **Multiple outcomes**: Design quests with success/failure branches
- **Dynamic NPCs**: NPC behavior can change based on reputation flags
- **Branching paths**: Locations can have multiple entrances/exits

---

**Version**: 2.0.0
**Last Updated**: 2025-12-19
**Compatible With**: Protocol Library v2.0+, Party State Schema v2.0+
