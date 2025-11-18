# CAMPAIGN MODULE TEMPLATE
**System**: D&D 5th Edition (use with ORCHESTRATOR_CORE_DND5E.md)  
**Version**: 3.0  
**Format**: Campaign Module Structure  
**Created**: November 17, 2025

---

## 📋 PURPOSE

This template defines the structure for D&D 5e campaign modules that integrate with the core orchestrator. Use this format when creating new campaign content to ensure compatibility with the universal mechanics system.

**Version 3.0 Improvements**:
- Optional UIDs for cross-referencing when ambiguity exists
- Reusable component library support
- Enhanced state transition markers
- Conditional and temporal logic blocks
- Emotional/narrative beat tagging

---

## 🎯 CAMPAIGN METADATA

```markdown
# [CAMPAIGN NAME] - CAMPAIGN MODULE

**Campaign**: [Full campaign name]
**Source**: [Official adventure book, homebrew, etc.]
**System**: D&D 5th Edition
**Required Orchestrator**: ORCHESTRATOR_CORE_DND5E.md
**Party Level Range**: [Starting level] - [Ending level]
**Expected Duration**: [Number of sessions]
**Module Version**: 1.0
**Created**: [Date]
```

### Campaign Tags

**Style**: [Sandbox / Linear / Semi-Linear / Episodic]  
**Themes**: [Horror, Intrigue, Exploration, Combat, etc.]  
**Setting**: [Region/World where campaign takes place]  
**Tone**: [Serious, Lighthearted, Dark, Heroic, etc.]

---

## 📖 CAMPAIGN OVERVIEW

### Elevator Pitch

**One-sentence summary**: [What is this campaign about?]

**Example**:
"A young white dragon terrorizes the Sword Coast while adventurers take on quests from Phandalin's quest board to protect the region and eventually confront the wyrm."

### Story Summary

**2-3 paragraph overview of the campaign**:
- What is the main conflict?
- Who are the antagonists?
- What is at stake?
- What makes this campaign unique?

### Connection to Other Campaigns (If Applicable)

**Prerequisite campaigns**: [List if any]  
**Sequel campaigns**: [List if any]  
**Standalone**: [Yes/No]

**Continuation Details** (if sequel):
- What should have happened in previous campaign
- What level should party be
- What items/relationships carry forward
- Any time skip between campaigns

---

## 🗺️ CAMPAIGN STRUCTURE

### Acts or Phases

**Act 1: [Name]** (Levels [X-Y])
- Summary of what happens
- Key locations introduced
- Major NPCs introduced
- Objectives
- Approximate sessions: [X]

**Act 2: [Name]** (Levels [X-Y])
- Summary of what happens
- New locations
- Major story developments
- Objectives
- Approximate sessions: [X]

**Act 3: [Name]** (Levels [X-Y])
- Summary of what happens
- Climax setup
- Final confrontations
- Resolution
- Approximate sessions: [X]

### Quest Structure (If Applicable)

**Quest Type**: [Linear / Quest Board / Faction-Based / Episodic / etc.]

**How Quests Work**:
- How do players receive quests?
- Can they choose quest order?
- Are there time pressures?
- Can quests fail?
- How do quests interconnect?

### Campaign Length

**Minimum**: [X sessions / hours]  
**Expected**: [X sessions / hours]  
**Maximum**: [X sessions / hours with all content]

**Pacing Notes**:
- Recommended session length
- How much combat vs roleplay vs exploration
- Suggested rest frequency

---

## 🔧 REUSABLE COMPONENTS LIBRARY

### Purpose

Define commonly-used mechanics, encounters, and hazards once, then reference them throughout the campaign. The orchestrator can handle both explicit references to these components AND inline unique definitions.

### [REUSABLE_MECHANICS]

Define mechanics that appear multiple times across different quests:

```markdown
[MECHANIC: mechanic_identifier]
name: "Mechanic Name"
trigger: "[When does this activate]"
save: "[Type] DC [number]" (if applicable)
on_failure: "[Effect on failed save]"
on_success: "[Effect on successful save]"
duration: "[How long it lasts]"
notes: "[Special conditions or variations]"
```

**Example**:
```markdown
[MECHANIC: psychic_damage_zone]
name: "Psychic Damage Zone"
trigger: "Every 10ft of movement through the zone"
save: "Wisdom DC 15"
on_failure: "2d10 psychic damage + roll on short-term madness table"
on_success: "Half damage, no madness"
duration: "While in the zone"
notes: "DC increases by 2 near artifact sources"
```

### [REUSABLE_ENCOUNTERS]

Define standard enemy groups that appear multiple times:

```markdown
[ENCOUNTER: encounter_identifier]
name: "Encounter Name"
description: "[Brief tactical description]"
composition:
  - [creature_name or creature_id]: [quantity]
  - [creature_name or creature_id]: [quantity]
tactics: "[How they fight]"
variations: "[Optional modifications for different contexts]"
```

**Example**:
```markdown
[ENCOUNTER: drow_hunting_party]
name: "Drow Hunting Party"
description: "Standard House Xaniqos patrol formation"
composition:
  - drow_priestess_of_lolth: 1
  - drow_elite_warrior: 3
tactics: "Priestess stays back casting support, warriors engage in melee"
variations: "Add 2 drow scouts if in open terrain"
```

### [REUSABLE_HAZARDS]

Define environmental dangers that recur:

```markdown
[HAZARD: hazard_identifier]
name: "Hazard Name"
detection: "[Skill] DC [number]"
effect: "[What happens when triggered]"
bypass: "[How to avoid or disable]"
```

### Usage in Quests

When using a reusable component, reference it like this:

**In quest description**:
- "The corridor is affected by [MECHANIC: psychic_damage_zone]"
- "Party encounters [ENCOUNTER: drow_hunting_party]"
- "The bridge contains [HAZARD: collapsing_bridge]"

**Or define inline with modifications**:
```markdown
[INLINE_MECHANIC: based_on psychic_damage_zone]
modifications:
  - save_dc: 18 (instead of 15)
  - damage: 3d10 (instead of 2d10)
context: "Near the artifact's chamber, the psychic pressure intensifies"
```

---

## 🔗 QUEST RELATIONSHIPS

### Purpose

Quest relationships define how completing (or failing) quests affects the world, NPCs, and other quests. This creates a dynamic, interconnected campaign where player choices have visible consequences.

### Quest Relationship Template

For each quest that triggers consequences, provide:

```markdown
### QUEST: [Quest Name]

[QUEST_METADATA]
quest_id: quest_identifier (optional - use when referenced by other quests)
uid: q_unique_id (optional - use only if multiple quests have similar names)
given_by: [NPC name or npc_identifier if using UIDs]
level_range: [X-Y]
[END_QUEST_METADATA]

**Triggers on Completion**:

[STATE_CHANGE: change_identifier]
type: npc_reaction | quest_unlock | world_change | price_change | location_change
target: [NPC/Quest/Location identifier]
condition: [Optional prerequisite flag or quest completion]
effect:
  [specific effect data - relationship changes, flags set, etc.]
visibility: announced | silent | discovered
narrative: "[How this is presented to players]"
[END_STATE_CHANGE]

[Repeat STATE_CHANGE blocks for each trigger]

**Triggers on Failure** (if applicable):

[STATE_CHANGE: failure_identifier]
[Same structure as completion triggers]
[END_STATE_CHANGE]

[CONDITIONAL_LOGIC]
if: [condition]
then: [effect]
else: [alternative effect]
[END_CONDITIONAL_LOGIC]

**Affects Other Quests**:

[QUEST_DEPENDENCY]
related_quest: [quest name or quest_id]
relationship: blocks | enables | modifies | competes_with
modification: "[How the related quest changes]"
[END_QUEST_DEPENDENCY]
```

### Examples

#### Example 1: Simple Quest Unlock with Optional UID

```markdown
### QUEST: Mountain's Toe Gold Mine

[QUEST_METADATA]
quest_id: mountains_toe_mine
given_by: norbus_ironrune
level_range: 2-3
[END_QUEST_METADATA]

**Triggers on Completion**:

[STATE_CHANGE: norbus_partnership]
type: npc_reaction
target: norbus_ironrune
condition: dwarven_excavation_complete
effect:
  relationship_change: +1
  dialogue_unlock: "partnership_offer"
  quest_offer: "joint_mining_venture"
visibility: announced
narrative: "After hearing of your success at the Mountain's Toe Mine, Norbus Ironrune seeks you out at the Stonehill Inn. 'You've got a knack for clearing out troublesome creatures,' he says with a grin. 'I've got a proposition for you...'"
[END_STATE_CHANGE]

[STATE_CHANGE: halia_jealousy]
type: npc_reaction
target: halia_thornton
effect:
  relationship_change: -1
  internal_state: jealous_of_competition
visibility: discovered
narrative: "[Players discover this through Halia's colder demeanor or others mentioning she's upset]"
[END_STATE_CHANGE]
```

#### Example 2: World State Changes with Temporal Markers

```markdown
### QUEST: Butterskull Ranch

[QUEST_METADATA]
quest_id: butterskull_ranch
[END_QUEST_METADATA]

**Triggers on Completion**:

[STATE_CHANGE: ranch_secured]
type: world_change
target: phandalin_region
effect:
  flag: butterskull_ranch_safe
  value: true
  description: "Ranch is secure and can be used as rest point"
visibility: announced
narrative: "With the orcs driven off, Butterskull Ranch is once again a safe haven. The Kalazorn family offers you free lodging anytime you're in the area."
[END_STATE_CHANGE]

**Triggers on Failure**:

[STATE_CHANGE: orc_escalation]
type: world_change
target: phandalin_region
effect:
  flag: orc_aggression_level
  value: increased
  description: "Orc raids become more frequent"
visibility: silent
narrative: "[Manifests as more random orc encounters near Phandalin]"
[END_STATE_CHANGE]

[STATE_CHANGE: family_lost]
type: npc_reaction
target: big_al_kalazorn
effect:
  relationship_change: -3
  emotional_state: grieving
  quest_offer: null
visibility: announced
narrative: "Big Al won't meet your eyes when you return to Phandalin. The weight of loss hangs heavy on the town."
[END_STATE_CHANGE]

[TEMPORAL_TRIGGER]
delay: 2_sessions
condition: butterskull_ranch_safe == true
trigger:
  [STATE_CHANGE: grateful_family]
  type: world_change
  target: phandalin
  effect:
    flag: kalazorn_family_grateful
    value: true
  narrative: "The Kalazorn family has been spreading word of your heroics. You notice friendlier greetings around town."
  [END_STATE_CHANGE]
[END_TEMPORAL_TRIGGER]
```

#### Example 3: Price Changes and Economic Impact

```markdown
### QUEST: Loggers' Camp

[STATE_CHANGE: timber_restored]
type: price_change
target: barthen_provisions
effect:
  merchant: barthen_provisions
  item_type: wooden_items
  modifier: 0.8
visibility: discovered
narrative: "[Players notice lower prices on wooden items at Barthen's Provisions. Elmar mentions lumber is flowing again.]"
[END_STATE_CHANGE]

[STATE_CHANGE: construction_boom]
type: world_change
target: phandalin
effect:
  flag: construction_active
  value: true
  description: "New buildings being constructed in Phandalin"
visibility: discovered
narrative: "[Players notice new construction when they return to town. NPCs mention expansion plans.]"
[END_STATE_CHANGE]
```

#### Example 4: Quest Chains with Conditional Logic

```markdown
### QUEST: Gnomengarde

[QUEST_METADATA]
quest_id: gnomengarde
[END_QUEST_METADATA]

**Triggers on Completion**:

[STATE_CHANGE: gnome_alliance]
type: quest_unlock
target: phandalin
effect:
  quest_id: gnomish_invention_malfunction
  announcement: "A week after resolving the Gnomengarde dispute, a gnome messenger arrives in Phandalin with an urgent request..."
visibility: announced
narrative: "[Provide full hook for new quest]"
[END_STATE_CHANGE]

[CONDITIONAL_LOGIC]
if: gnomengarde_kings_alive
then:
  [STATE_CHANGE: royal_gratitude]
  type: npc_reaction
  target: gnomengarde
  effect:
    relationship_change: +3
    rewards: gnomish_clockwork_amulet
  [END_STATE_CHANGE]
else:
  [STATE_CHANGE: gnome_mourning]
  type: world_change
  target: gnomengarde
  effect:
    flag: gnomes_in_mourning
    mood: somber
  [END_STATE_CHANGE]
[END_CONDITIONAL_LOGIC]

**Affects Other Quests**:

[QUEST_DEPENDENCY]
related_quest: shrine_of_savras
relationship: modifies
modification:
  additional_help: gnome_divination_device
  difficulty_reduction: -2 DC on prophecy puzzle
[END_QUEST_DEPENDENCY]
```

### Quest Relationship Checklist

For each quest in your campaign, consider:
- ☐ Does completion affect any NPCs' attitudes?
- ☐ Does it unlock new quests?
- ☐ Does it change the world state (locations, random encounters, etc.)?
- ☐ Does it affect the economy (prices, availability)?
- ☐ Does it make other quests easier/harder/impossible?
- ☐ What happens if the quest fails?
- ☐ Are there time-delayed consequences?
- ☐ Are there conditional outcomes based on HOW they completed it?

---

## 🎯 INTERACTABLE OBJECTS

### Purpose

Interactable objects add tactical depth and reward creative problem-solving. They give players agency to interact with the environment in ways that affect combat, exploration, and story.

### Interactable Object Template

For each significant interactable object, provide:

```markdown
### OBJECT: [Object Name]

[OBJECT_METADATA]
object_id: object_identifier (optional - for cross-referencing)
location: [Quest/Location where found]
description: "[What it looks like, where it is positioned]"
visible: true | false | {skill: [skill_name], dc: [number]}
[END_OBJECT_METADATA]

**Interactions**:

[INTERACTION: action_identifier]
action: [Action Name] (e.g., Topple, Break, Activate)
requirements:
  skill: [Skill name] (if applicable)
  dc: [Number] (if check required)
  ability: [Special requirement] (if any)
action_cost: [Action / Bonus Action / Reaction / 1 minute]
effects:
  immediate: "[What happens right away]"
  ongoing: "[Lasting effects]" (if applicable)
  area: "[Area of effect]" (if applicable)
tactical_use: "[How this helps in combat/exploration]"
[END_INTERACTION]

[Repeat INTERACTION blocks for each possible action]
```

### Examples

#### Example 1: Combat Tactical Object

```markdown
### OBJECT: Chandelier

[OBJECT_METADATA]
location: Tresendar Manor - Banquet Hall
description: "A heavy iron chandelier hangs 15 feet above the center of the room, suspended by a thick chain. Dozens of candles sit in its holders."
visible: true
[END_OBJECT_METADATA]

**Interactions**:

[INTERACTION: sever_chain]
action: Sever Chain
requirements:
  option_1: "Attack chain (AC 15, 10 HP)"
  option_2: "Dexterity (Acrobatics) DC 15 to climb and release"
action_cost: Action (to attack or climb)
effects:
  immediate: "Chandelier falls, creatures in 10ft radius make DC 13 Dex save or take 3d6 bludgeoning damage and knocked prone"
  area: "10-foot radius beneath chandelier"
  tactical_use: "Can be dropped on clustered enemies or to create difficult terrain"
[END_INTERACTION]

[INTERACTION: swing_across]
action: Swing on Chandelier
requirements:
  skill: Athletics or Acrobatics
  dc: 12
action_cost: Action + 10ft movement
effects:
  immediate: "Swing up to 20 feet horizontally to any point within reach"
  tactical_use: "Bypass enemies, reach elevated positions, or make dramatic entrance"
[END_INTERACTION]
```

#### Example 2: Puzzle Object

```markdown
### OBJECT: Enchanted Mirror

[OBJECT_METADATA]
object_id: tresendar_mirror (multiple mirrors exist - UID needed)
location: Tresendar Manor - Study
description: "An ornate floor-length mirror with silver runes etched into its frame. The reflection seems slightly off, as if delayed by a heartbeat."
visible: true
[END_OBJECT_METADATA]

**Interactions**:

[INTERACTION: examine_runes]
action: Examine Runes
requirements:
  skill: Arcana
  dc: 14
action_cost: 1 minute
effects:
  immediate: "Learn that runes are connected to a planar seal"
  ongoing: "Gain advantage on subsequent checks to activate mirror"
[END_INTERACTION]

[INTERACTION: speak_command_word]
action: Speak Command Word
requirements:
  knowledge: "Must have learned command word from diary or Arcana DC 18"
action_cost: Action
effects:
  immediate: "Mirror becomes portal for 1 minute to [location]"
  tactical_use: "Escape route, shortcut, or access to hidden area"
[END_INTERACTION]

[INTERACTION: break_mirror]
action: Break Mirror
requirements:
  option_1: "Any attack dealing 20+ damage"
action_cost: Action
effects:
  immediate: "Portal sealed permanently, 2d6 force damage to breaker, all glass golems in dungeon activate"
  tactical_use: "Last resort to prevent enemies from using portal"
[END_INTERACTION]
```

#### Example 3: Environmental Hazard Object

```markdown
### OBJECT: Crumbling Pillar

[OBJECT_METADATA]
location: Cragmaw Castle - Great Hall
description: "A 20-foot stone pillar showing significant structural damage. Cracks spider-web across its surface and small chunks of stone occasionally fall."
visible: true
stability_threshold: 15 (cumulative damage before collapse)
[END_OBJECT_METADATA]

**Interactions**:

[INTERACTION: topple_pillar]
action: Topple Pillar
requirements:
  skill: Athletics
  dc: 15 (DC 12 if already damaged)
action_cost: Action
effects:
  immediate: "Pillar falls in chosen direction (30ft line), creatures in line DC 14 Dex save or 4d10 bludgeoning + prone"
  ongoing: "Creates difficult terrain, partial cover, may cause ceiling collapse in that section"
  area: "30-foot line, 5 feet wide"
  tactical_use: "Create barrier, damage clustered enemies, or reshape battlefield"
[END_INTERACTION]

[INTERACTION: damage_pillar]
action: Attack Pillar
requirements:
  note: "Any damage counts toward stability threshold"
action_cost: As per attack
effects:
  immediate: "When cumulative damage reaches 15, pillar becomes unstable"
  ongoing: "Unstable pillar collapses at end of next turn unless supported"
  tactical_use: "Weaken for later use or force enemy movement"
[END_INTERACTION]

[INTERACTION: brace_pillar]
action: Brace Pillar
requirements:
  skill: Athletics
  dc: 12
action_cost: Action
effects:
  immediate: "Prevent imminent collapse for 1 round"
  ongoing: "Must maintain brace (no other actions) or pillar collapses"
  tactical_use: "Hold up ceiling while allies escape or enemy caught underneath"
[END_INTERACTION]
```

### Interactable Objects by Type

**Combat Tactical**:
- Chandeliers, braziers, barrels
- Pillars, scaffolding, bridges
- Siege weapons, portcullises, gates

**Puzzle Elements**:
- Levers, switches, pressure plates
- Mirrors, lenses, prisms
- Statues, pedestals, fonts

**Environmental Navigation**:
- Vines, ropes, chains
- Platforms, elevators, stairs
- Boats, carts, sleds

**Hazards**:
- Unstable structures
- Trapped objects
- Magical phenomena

---

## 🏰 LOCATIONS

### Location Template

For each significant location in your campaign:

```markdown
### LOCATION: [Location Name]

[LOCATION_METADATA]
location_id: location_identifier (optional - use for cross-referencing)
region: [Larger area this location is in]
type: [Town / Dungeon / Wilderness / etc.]
level_range: [Recommended levels for this location]
connected_quests: [List of quest IDs that use this location]
[END_LOCATION_METADATA]

**Description**:
[2-3 paragraphs describing what the location looks like, its atmosphere, and its significance]

**Key Features**:
- [Notable landmark or feature]
- [Another feature]
- [Environmental condition if relevant]

**Inhabitants**:
- [Who lives/works/guards here]
- [Typical population or enemy composition]

**Access**:
- [How do players typically arrive here]
- [Are there restrictions or requirements]

**Services** (if applicable):
- [Shops, inns, services available]

**Secrets**:
- [Hidden areas or information with discovery DC]

**Interactable Objects**:
- [Reference to any significant objects from Interactable Objects section]

**Atmosphere** (for DM guidance):
- [Mood and tone to convey]
- [Sensory details - sounds, smells, etc.]
```

### Location Quick Reference

| Location | Type | Level | Key NPCs | Connected Quests |
|----------|------|-------|----------|------------------|
| [Name] | [Type] | [X-Y] | [Names] | [Quest names] |

---

## 👥 NPC CATALOG

### Purpose

NPCs bring your campaign to life. This section provides personality, motivations, and mechanical details for significant NPCs.

### NPC Template

For each major NPC:

```markdown
### NPC: [Name]

[NPC_METADATA]
npc_id: npc_identifier (optional - use when multiple NPCs might share names)
role: [Quest Giver / Merchant / Ally / Antagonist / etc.]
location: [Where they're typically found]
faction: [If member of a faction]
importance: major | supporting | minor
[END_NPC_METADATA]

**Description**:
[Physical appearance, mannerisms, speech patterns]

**Personality**:
- **Trait**: [Key personality trait]
- **Ideal**: [What they believe in]
- **Bond**: [What they care about]
- **Flaw**: [Their weakness or vice]

**Motivation**:
[What drives this NPC's actions]

**Relationship Web**:
- **[NPC Name]**: [How they feel about this person]
- **[NPC Name]**: [How they feel about this person]

**Information They Know**:
- [Key information they can share]
- [Secrets they hold]
- [DC required to learn secrets] (if applicable)

**Quest Involvement**:
- Gives: [Quest names or IDs]
- Appears in: [Quest names or IDs]

**Stat Block** (if combat possible):
[Reference standard stat block or provide custom one]

**Character Arc** (if applicable):
[How this NPC might change over the campaign]

[EMOTIONAL_BEAT: identifier]
trigger: [What causes this reaction]
emotion: [joy | sorrow | anger | fear | surprise | disgust]
intensity: mild | moderate | intense
narrative_guidance: "[How to roleplay this moment]"
[END_EMOTIONAL_BEAT]

[Repeat EMOTIONAL_BEAT for key moments]
```

### NPC Quick Reference

| Name | Role | Location | Key Info | Related Quests |
|------|------|----------|----------|----------------|
| [Name] | [Role] | [Location] | [Snippet] | [Quest names] |

---

## 🎭 FACTIONS & ORGANIZATIONS

### Faction Template

For each significant faction:

```markdown
### FACTION: [Faction Name]

[FACTION_METADATA]
faction_id: faction_identifier
alignment: [General alignment tendency]
power_level: local | regional | continental | planar
[END_FACTION_METADATA]

**Overview**:
[What this faction is, what they want, why they matter]

**Leadership**:
- **[Leader Name]**: [Brief description and role]

**Goals**:
- Primary: [Main objective]
- Secondary: [Additional objectives]

**Methods**:
[How they pursue their goals - openly, secretly, violently, etc.]

**Resources**:
- Personnel: [Size and type of membership]
- Wealth: [Financial power]
- Influence: [Political or social reach]

**Reputation**:
- **Public View**: [How common folk see them]
- **Reality**: [What they actually are]

**Relationships**:
- **Allied with**: [Other factions]
- **Opposed to**: [Enemy factions]
- **Neutral to**: [Factions they ignore]

**Reputation Tiers**:
```markdown
[REPUTATION_SYSTEM: faction_identifier]
tier_1: -10 to -5 (Hostile)
  - Effect: [What happens at this reputation level]
tier_2: -4 to -1 (Unfriendly)
  - Effect: [What happens at this reputation level]
tier_3: 0 to 4 (Neutral)
  - Effect: [Starting relationship]
tier_4: 5 to 9 (Friendly)
  - Effect: [Benefits and services available]
tier_5: 10+ (Allied)
  - Effect: [Maximum benefits, quest lines, rewards]
[END_REPUTATION_SYSTEM]
```

**Quests Offered**:
[List of quests this faction provides]

**Recognition**:
[What symbols, phrases, or signals identify members]
```

---

## 🗺️ QUEST CATALOG

### Quest Template

For each quest in your campaign:

```markdown
## QUEST: [Quest Name]

[QUEST_METADATA]
quest_id: quest_identifier (optional)
quest_type: Main | Side | Faction | Hidden | Optional
level_range: [X-Y]
party_size: [2-6 or "Scales"]
expected_duration: [X hours/sessions]
location: [Primary location for this quest]
[END_QUEST_METADATA]

[EMOTIONAL_BEAT: quest_start]
emotion: [anticipation | urgency | curiosity | dread]
intensity: moderate
narrative_guidance: "[How to present the quest hook to match the intended emotion]"
[END_EMOTIONAL_BEAT]

**Summary**:
[2-3 sentence overview of what this quest is about]

**Quest Giver**:
- **Name**: [NPC name or npc_id]
- **Location**: [Where they give the quest]
- **Hook**: "[Exact or paraphrased quest pitch from NPC]"

**Objectives**:
1. [Primary objective]
2. [Secondary objective] (optional)
3. [Bonus objective] (optional)

**Rewards**:
- **XP**: [Amount] (or "Milestone: Level [X]")
- **Gold**: [Amount]gp
- **Items**: [Specific items received]
- **Reputation**: [Faction name] +[amount]
- **Other**: [Story rewards, unlocks, etc.]

**Time Pressure** (if applicable):
[TEMPORAL_CONSTRAINT]
type: hard_deadline | soft_deadline | escalating_difficulty
window: [X days/sessions]
consequence: "[What happens if too slow]"
[END_TEMPORAL_CONSTRAINT]

---

### QUEST STRUCTURE

**Phase 1: [Phase Name]**

[NARRATIVE_BEAT: phase1_start]
tone: [investigative | action | suspenseful | mysterious]
pacing: slow | moderate | fast
key_moment: "[What makes this phase memorable]"
[END_NARRATIVE_BEAT]

[Describe what happens in this phase]

**Challenges**:
- [Challenge type]: [Skill] DC [X] or [description]

**Key Information Revealed**:
- [Clue or knowledge gained]

**Phase 1 Conclusion**:
[How this phase ends, transition to next phase]

**Phase 2: [Phase Name]**

[Repeat structure]

---

### ENCOUNTERS

**Encounter 1: [Name]**

[ENCOUNTER_METADATA]
difficulty: Easy | Medium | Hard | Deadly
environment: [Terrain type and special features]
lighting: Bright | Dim | Darkness
[END_ENCOUNTER_METADATA]

**Setup**:
[Description of scene when players arrive]

**Enemies**:
- [Quantity]x [Monster Name] (CR [X], [XP] XP each)
- Total XP: [Adjusted XP for encounter building]

**Tactics**:
[How enemies fight, what they prioritize, when they flee]

**Environmental Features**:
- [Feature]: [How it can be used]
- [Reference to OBJECT: object_id if using interactable object]

**Treasure** (if any):
[Loot found here]

[Repeat for each encounter]

---

### TRAPS & HAZARDS

**[Trap/Hazard Name]**

[HAZARD: hazard_identifier]
location: [Specific area]
detection: [Skill] DC [X]
trigger: "[What sets it off]"
effect: "[What happens]"
save: [Type] DC [X] (if applicable)
damage: [Dice formula and type]
disarm: [Method and DC if possible]
bypass: "[How to avoid without disarming]"
[END_HAZARD]

---

### SUCCESS & FAILURE STATES

**Quest Success**:
[What happens when players complete objectives]

**Quest Failure**:
[What happens if they fail - is quest lost or can they retry]

**Consequences**:
[See Quest Relationships section for detailed state changes]

---

### DM NOTES

**Running This Quest**:
- [Tip for presenting this quest]
- [Common player approach]
- [How to improvise if they go off-script]

**Scaling Guidance**:
- **Easier**: [How to adjust for lower level/smaller party]
- **Harder**: [How to adjust for higher level/larger party]

**Common Pitfalls**:
- [What might go wrong]
- [How to handle it]

**Roleplaying Tips**:
- [How to voice key NPCs]
- [How to maintain atmosphere]

```

---

## 🐉 BESTIARY

### Purpose

Campaign-specific monsters, variants of standard creatures, or notable unique enemies.

### Monster Template

For each custom or notable monster:

```markdown
### [MONSTER NAME]

[MONSTER_METADATA]
monster_id: monster_identifier (optional - if multiple similar creatures exist)
source: [Original stat block or "Custom"]
modifications: [If based on existing creature, list changes]
[END_MONSTER_METADATA]

**[SIZE] [TYPE], [ALIGNMENT]**

**Armor Class** [AC] ([armor type])  
**Hit Points** [HP] ([HD])  
**Speed** [speed]

| STR | DEX | CON | INT | WIS | CHA |
|-----|-----|-----|-----|-----|-----|
| [score] ([mod]) | [score] ([mod]) | [score] ([mod]) | [score] ([mod]) | [score] ([mod]) | [score] ([mod]) |

**Saving Throws** [list saves with bonuses]  
**Skills** [list skills with bonuses]  
**Damage Resistances** [types]  
**Damage Immunities** [types]  
**Condition Immunities** [conditions]  
**Senses** [senses and passive Perception]  
**Languages** [languages]  
**Challenge** [CR] ([XP] XP)

---

**TRAITS**:

**[Trait Name]**. [Trait description]

**[Special Ability]**. [Ability description]

---

**ACTIONS**:

**[Action Name]**: [To-hit bonus or save DC], [Reach or range], [Target]. [Effect]. [Damage formula and type].

**DESCRIPTION**:
[2-3 sentences about the creature's appearance, behavior, and role in the campaign]

**TACTICS**:
[How this creature fights - opening moves, strategy, when it retreats]

**LOOT**:
[What it carries or can be harvested]
```

### Monster Quick Reference

| Monster | CR | XP | Used In | Key Feature |
|---------|----|----|---------|-------------|
| [Name] | [CR] | [XP] | [Quest] | [Ability] |

---

## ✨ MAGIC ITEM CATALOG

### Magic Item Template

For each campaign-specific magic item:

```markdown
### [ITEM NAME]

[ITEM_METADATA]
item_id: item_identifier (optional)
type: [Weapon / Armor / Wondrous Item / etc.]
rarity: Common | Uncommon | Rare | Very Rare | Legendary | Artifact
requires_attunement: Yes | No
found_in: [Quest/location where obtained]
[END_ITEM_METADATA]

**Description**:
[Physical description of the item]

**Properties**:
[Mechanical effects - bonuses, abilities, charges, etc.]

**Lore**:
[Optional backstory or significance]

**Usage Notes**:
[How it works in practice, any DM guidance]

[NARRATIVE_BEAT: item_discovery]
emotion: wonder | triumph | unease
intensity: moderate
narrative_guidance: "[How to present the item when found to create appropriate mood]"
[END_NARRATIVE_BEAT]
```

### Magic Item Distribution

**By Rarity**:
- Common: [X items]
- Uncommon: [X items]
- Rare: [X items]
- Very Rare: [X items]
- Legendary: [X items]

**By Quest/Level**:
| Item Name | Rarity | Found In | Level Range |
|-----------|--------|----------|-------------|
| [Name] | [Rarity] | [Quest] | [X-Y] |

---

## ⚙️ CAMPAIGN-SPECIFIC MECHANICS

### Special Systems (If Any)

If your campaign has unique mechanical systems not covered by core D&D 5e rules, document them here:

```markdown
### [System Name]

[MECHANIC_SYSTEM: system_identifier]
purpose: "[What this system adds to the campaign]"
complexity: simple | moderate | complex
frequency: constant | situational | rare
[END_MECHANIC_SYSTEM]

**How It Works**:
[Detailed explanation of the mechanic]

**When to Use**:
[Circumstances that trigger or utilize this system]

**Integration with Core Rules**:
[How this interacts with standard D&D mechanics]

**Examples**:
[1-2 concrete examples of the system in use]
```

**Common Campaign-Specific Systems**:
- Reputation/faction tracking
- Time pressure mechanics
- Random encounter tables
- Weather systems
- Survival rules
- Chase mechanics
- Mass combat rules
- Crafting systems
- Investigation point systems

### House Rules (If Any)

**Recommended House Rules**:
- [Rule modification with justification]
- [Why it enhances this campaign]

**Optional House Rules**:
- [Alternative rules players might adopt]
- [Effects on gameplay]

---

## 📊 PACING GUIDELINES

### Session Structure

**Typical Session Flow**:
1. [Opening - time estimate]
2. [Development - time estimate]
3. [Challenge - time estimate]
4. [Resolution - time estimate]

### Quest Pacing

**Recommended Quest Order** (if applicable):
1. [Quest name] - [Reason for order]
2. [Quest name] - [Reason for order]
3. [Quest name] - [Reason for order]

**Flexible vs Rigid Ordering**:
- [Which quests must be done in order]
- [Which quests are freely chooseable]
- [Consequences of sequence changes]

### Level Progression

**Expected Leveling Rate**:
| Level | After Quest(s) | Approx. Session |
|-------|---------------|-----------------|
| [X] | [Quest names] | [Session #] |
| [Y] | [Quest names] | [Session #] |

### Milestone Alternative

If using milestone leveling instead of XP:
- Level [X] after [trigger]
- Level [Y] after [trigger]
- Level [Z] after [trigger]

---

## 🎬 SESSION ZERO GUIDE

### Pre-Campaign Checklist

**Discuss with Players**:
- ☐ Campaign premise and expectations
- ☐ Tone and themes
- ☐ Player character connections
- ☐ Party composition needs
- ☐ Scheduling and commitment
- ☐ Safety tools and boundaries

**Character Creation**:
- **Starting Level**: [Level]
- **Ability Scores**: [Method - array, point buy, rolling]
- **Allowed Content**: [PHB, Xanathar's, Tasha's, etc.]
- **Equipment**: [Starting equipment method]
- **Background Integration**: [How backgrounds tie to campaign]

**Campaign-Specific Options**:
- [Any special character options for this campaign]
- [Restricted options if any]
- [Recommended but not required options]

### Opening Scene

**How Campaign Begins**:
[Description of the opening scenario]

**Initial Hooks**:
- [How each character is introduced]
- [What brings the party together]
- [Initial objective or situation]

---

## 💾 SAVE/RESUME ADDITIONS

### Campaign-Specific Save Data

**In addition to standard save file, track**:

```markdown
## Campaign Progress

[CAMPAIGN_STATE]
[Campaign-Specific Tracker 1]: [Status]
[Campaign-Specific Tracker 2]: [Status]

[Example: Quest Board Status, Faction Reputation, Dragon Threat Level, etc.]

**Campaign-Specific Resources**:
- [Special items, currencies, or tracking elements unique to this campaign]

**Story State**:
- [Important plot flags or decision points]
- [NPC status changes]
- [World state alterations]

**Active Temporal Effects**:
- [Any time-delayed triggers waiting to fire]
- [Session counters for temporal events]
[END_CAMPAIGN_STATE]
```

---

## 🎯 DM PREPARATION GUIDE

### Before First Session

**Read**:
- [ ] Core orchestrator (ORCHESTRATOR_CORE_DND5E.md)
- [ ] This entire campaign module
- [ ] First 2-3 quest details thoroughly
- [ ] Reusable Components Library section

**Prepare**:
- [ ] Session zero materials
- [ ] First quest encounter details
- [ ] Initial NPC personalities
- [ ] Opening scene description

**Materials Needed**:
- [ ] Dice
- [ ] Stat block references
- [ ] Maps (if physical)
- [ ] Tracking sheet for XP/resources

### Before Each Session

**Review**:
- [ ] Last session's save file
- [ ] Upcoming quest(s) details
- [ ] Relevant NPC information
- [ ] Monster stat blocks
- [ ] Any pending temporal triggers or state changes

**Prepare**:
- [ ] Opening recap
- [ ] Quest board updates (if applicable)
- [ ] Encounter tactics
- [ ] Potential player paths

---

## 📚 APPENDICES

### Appendix A: Quick Reference Tables

[Any campaign-specific quick reference materials]

### Appendix B: Handouts

[Player-facing documents, maps, quest board postings, letters, etc.]

### Appendix C: Random Tables

[Any random encounter tables, treasure tables, or event tables]

### Appendix D: Adaptation Notes

**For Different Party Sizes**:
- Smaller parties (2-3 players): [Adjustment guidance]
- Larger parties (6+ players): [Adjustment guidance]

**For Different Levels**:
- Starting at different level: [How to adapt]
- Skipping content: [Impact on story]

---

## 🎯 CAMPAIGN COMPLETION

### Ending Variants

**Standard Ending**:
[What happens if party completes main objectives]

[NARRATIVE_BEAT: campaign_climax]
tone: epic
pacing: fast
emotion: triumph
intensity: intense
key_moment: "[The moment that defines the campaign's conclusion]"
[END_NARRATIVE_BEAT]

**Alternative Endings**:
- [Ending variant 1]
- [Ending variant 2]

**Failure State**:
[What happens if party fails main objective]

### Aftermath

**Immediate Results**:
[Short-term consequences of campaign resolution]

**Long-Term Impact**:
[How this campaign affects the world]

**Character Futures**:
[What happens to the party after campaign ends]

### Sequel Hooks (If Applicable)

[Seeds for potential follow-up campaigns]

---

## ✅ CAMPAIGN MODULE CHECKLIST

Before publishing/using this campaign module, ensure:

- [ ] All quests have complete information
- [ ] All locations are detailed
- [ ] All major NPCs have personalities
- [ ] All custom monsters have stat blocks
- [ ] Magic items are specified
- [ ] Pacing guidelines provided
- [ ] Integration with core orchestrator tested
- [ ] Save file additions documented
- [ ] Session zero guide complete
- [ ] DM prep guidance included
- [ ] Reusable components library populated (if applicable)
- [ ] State transitions clearly marked
- [ ] Conditional and temporal logic documented
- [ ] Emotional beats tagged for narrative guidance

---

## 📝 TEMPLATE USAGE NOTES

### When to Use UIDs

Only add unique identifiers (`uid`, `quest_id`, `npc_id`, etc.) when:
- Multiple entities share similar names
- Complex cross-referencing is needed
- Database-style lookups would be helpful

**Don't over-use UIDs** - natural language references work perfectly most of the time.

### Reusable Components Philosophy

Define reusable components when:
- A mechanic appears 3+ times
- An encounter composition is standard/repeated
- A hazard type recurs with minor variations

**Don't force abstraction** - inline definitions are fine for unique or contextual elements.

### State Management Best Practices

Use `[STATE_CHANGE]` blocks to:
- Make consequences explicit and unambiguous
- Track world reactions to player choices
- Enable the orchestrator to update its state database automatically

Use `[CONDITIONAL_LOGIC]` and `[TEMPORAL_TRIGGER]` blocks to:
- Create branching narratives based on HOW quests were completed
- Schedule delayed consequences
- Make the world feel alive and reactive

### Emotional Beat Tagging

Use `[EMOTIONAL_BEAT]` and `[NARRATIVE_BEAT]` blocks to:
- Guide the orchestrator's tone and pacing
- Ensure key moments land with appropriate weight
- Help maintain narrative cohesion across long sessions

---

**END OF CAMPAIGN TEMPLATE**

Version 3.0 - November 17, 2025  
Use this structure for all campaign modules.  
Ensures compatibility with ORCHESTRATOR_CORE_DND5E.md.

**Key Improvements in v3.0**:
- Optional UID system for genuine ambiguity cases
- Reusable component library support
- Enhanced state transition markers
- Conditional and temporal logic blocks
- Emotional/narrative beat tagging for orchestrator guidance
- Maintains AI-native, fault-tolerant format philosophy

---
