# Party State Schema v2.0

**Purpose**: Defines the complete state for a D&D party in the AI Orchestrator

**Format**: YAML-like pseudo-code (actual implementation can be JSON)

---

## Complete Schema

```yaml
Party_State_Schema_v2:
  metadata:
    session_number: int
    date: timestamp
    campaign_id: string
    act_id: string (e.g., "act_2_dead_city")
    save_version: string ("2.0.0")

  characters: [Character_Schema_v2] (array of all party members)

  party_resources:
    shared_gold: int (party treasury, if using shared wealth)
    shared_items:
      - name: string
        quantity: int
        weight: float
        notes: string

  location:
    current: string (location_id from campaign vault)
    previous: string
    in_combat: bool
    region: string (optional, for large world tracking)

  campaign_state:
    quests_completed: [string] (quest_ids)
    quests_active:
      - quest_id: string
        status: string ("in_progress" | "ready_to_complete")
        objectives_completed: [string]
        notes: string
    quests_available: [string] (quest_ids)
    quests_failed: [string] (quest_ids)

  world_state:
    reputation:
      npcs:
        - npc_id: string
          value: int (-10 to +10)
          notes: string
      factions:
        - faction_id: string
          value: int (-10 to +10)
          rank: string (e.g., "initiate", "member", "leader")
      regions:
        - region_id: string
          fame: int (0-100)
          infamy: int (0-100)
          known_deeds: [string]

    locations_discovered: [string] (location_ids)
    locations_cleared: [string] (location_ids, for dungeons)

    story_flags:
      # Custom flags specific to campaign (flexible structure)
      flag_name: value (bool | int | string)

    time_elapsed: int (total in-game days since campaign start)
    time_minutes: int (total in-game minutes for precise tracking)
    time_of_day: string ("morning" | "afternoon" | "evening" | "night")

    date:
      day: int
      month: string
      year: int

  combat_state:
    active: bool
    round: int
    initiative_order:
      - name: string
        initiative: int
        is_enemy: bool
        hp_current: int
        hp_max: int
    current_turn: string (name of character/enemy currently acting)
    defeated_enemies:
      - enemy_id: string
        name: string
        loot: object

  environmental_state:
    weather: string ("clear" | "rain" | "snow" | "fog" | "storm")
    temperature: string ("freezing" | "cold" | "comfortable" | "hot" | "scorching")
    hazards_active: [string] (e.g., "darkness", "difficult_terrain", "poisonous_gas")

  session_history:
    major_events: [string] (narrative summary of key events)
    npcs_met: [string] (npc_ids of all NPCs encountered)
    enemies_defeated: [string] (enemy types/names)
    total_xp_earned: int
    total_gold_earned: int
    deaths: int (number of party deaths)
```

---

## Field Descriptions

### Metadata
- `session_number`: Incrementing session counter
- `date`: Real-world timestamp of last save
- `campaign_id`: Identifier for campaign (e.g., "descent_into_khar_morkai")
- `act_id`: Current act (e.g., "act_2_dead_city")
- `save_version`: Schema version for migration tracking

### Characters
- Array of `Character_Schema_v2` objects (see Character_Schema_v2.md)
- Contains all player characters in the party

### Party Resources
- `shared_gold`: If using shared wealth system (alternative to per-character gold)
- `shared_items`: Items owned by party, not individuals (rope, tents, etc.)

### Location
- `current`: Current location module_id (e.g., `loc_main_street`)
- `previous`: Previous location (for "go back" commands)
- `in_combat`: Whether party is currently in combat
- `region`: Broader region identifier (optional)

### Campaign State
- `quests_completed`: Array of completed quest_ids
- `quests_active`: Active quests with progress tracking
- `quests_available`: Quests available to accept
- `quests_failed`: Quests that were failed

### World State

#### Reputation
- **NPCs**: Individual NPC relationships (-10 to +10)
- **Factions**: Group affiliations with ranks
- **Regions**: Fame (positive) and infamy (negative) in areas

#### Locations
- `locations_discovered`: All locations party has visited
- `locations_cleared`: Locations fully explored/cleared

#### Story Flags
- Flexible key-value pairs for campaign-specific state
- Examples: `velryn_with_party: true`, `zilvra_hostile: false`

#### Time
- `time_elapsed`: Total in-game days
- `time_minutes`: Precise minute tracking
- `time_of_day`: Current time period
- `date`: In-game calendar date

### Combat State
- `active`: Whether combat is ongoing
- `round`: Current combat round
- `initiative_order`: Turn order with HP tracking
- `current_turn`: Whose turn it is
- `defeated_enemies`: Enemies defeated this combat (for loot)

### Environmental State
- `weather`: Current weather conditions
- `temperature`: Temperature extremes
- `hazards_active`: Environmental hazards affecting party

### Session History
- `major_events`: Narrative summary of key moments
- `npcs_met`: All NPCs encountered (for reference)
- `enemies_defeated`: Types of enemies beaten
- `total_xp_earned`: Cumulative XP across all sessions
- `total_gold_earned`: Cumulative gold across all sessions
- `deaths`: Death counter (for stakes tracking)

---

## Example Party State

```yaml
metadata:
  session_number: 15
  date: "2025-12-19T14:30:00Z"
  campaign_id: "descent_into_khar_morkai"
  act_id: "act_2_dead_city"
  save_version: "2.0.0"

characters:
  - (See Character_Schema_v2.md for full character objects)
    name: "Thorin Ironforge"
    level: 5
    hp_current: 45
    hp_max: 52
    ...
  - name: "Mira Shadowstep"
    level: 5
    hp_current: 38
    hp_max: 38
    ...
  - name: "Aldric Stormborn"
    level: 5
    hp_current: 40
    hp_max: 44
    ...
  - name: "Elara Moonsong"
    level: 5
    hp_current: 32
    hp_max: 32
    ...

party_resources:
  shared_gold: 450
  shared_items:
    - name: "Rope (50 ft)"
      quantity: 2
      weight: 10
      notes: ""
    - name: "Tent (2-person)"
      quantity: 2
      weight: 40
      notes: ""

location:
  current: "loc_main_street"
  previous: "loc_collapsed_tunnel"
  in_combat: false
  region: "khar_morkai_central"

campaign_state:
  quests_completed: ["quest_mq1_mapping_the_dead"]
  quests_active:
    - quest_id: "quest_mq2_three_fragments"
      status: "in_progress"
      objectives_completed: ["soulforge_shard_obtained"]
      notes: "Need Warden's Sigil and Mourner's Tear"
  quests_available: ["quest_sq1_architects_map", "quest_sq2_volunteers_plea"]
  quests_failed: []

world_state:
  reputation:
    npcs:
      - npc_id: "npc_zilvra_shadowveil"
        value: -2
        notes: "Tense negotiation, party refused to surrender Velryn"
      - npc_id: "npc_thalgrim_ghost"
        value: +5
        notes: "Helped him find peace, completed his unfinished work"
      - npc_id: "npc_gralk_the_merchant"
        value: +1
        notes: "Made fair purchases"

    factions:
      - faction_id: "faction_house_shadowveil"
        value: -3
        rank: null
        notes: "Protecting Velryn from them"
      - faction_id: "faction_undead_souls"
        value: +4
        rank: null
        notes: "Treated ghosts with respect"

    regions:
      - region_id: "khar_morkai"
        fame: 15
        infamy: 5
        known_deeds: ["Pacified Thalgrim's ghost", "Defeated undead patrol"]

  locations_discovered: ["loc_main_street", "loc_artisan_quarter", "loc_forge_ancient"]
  locations_cleared: ["loc_forge_ancient"]

  story_flags:
    velryn_with_party: true
    zilvra_met: true
    zilvra_negotiated: true
    zilvra_hostile: false
    thalgrim_pacified: true
    soulforge_shard_obtained: true
    wardens_sigil_obtained: false
    mourners_tear_obtained: false
    vault_access_granted: false

  time_elapsed: 3
  time_minutes: 4320
  time_of_day: "evening"
  date:
    day: 3
    month: "Deepwinter"
    year: 1492

combat_state:
  active: false
  round: 0
  initiative_order: []
  current_turn: null
  defeated_enemies: []

environmental_state:
  weather: "none" (underground)
  temperature: "cold"
  hazards_active: ["darkness", "madness_aura"]

session_history:
  major_events:
    - "Descended into Khar-Morkai via collapsed tunnel"
    - "Met Gralk the ghoul merchant on Main Street"
    - "Found journal in dry fountain revealing three key fragments"
    - "Explored Artisan Quarter, encountered Thalgrim's ghost"
    - "Persuaded Thalgrim to find peace, obtained Soulforge Shard"
    - "Ambushed by Zilvra Shadowveil and drow patrol"
    - "Negotiated with Zilvra, refused to surrender Velryn"

  npcs_met: ["npc_gralk_the_merchant", "npc_thalgrim_ghost", "npc_zilvra_shadowveil"]

  enemies_defeated: ["skeleton x4", "zombie x2", "helmed_horror x2"]

  total_xp_earned: 7500
  total_gold_earned: 650
  deaths: 0
```

---

## Validation Rules

When loading or saving party state, validate:

1. **Character Integrity**:
   - All characters valid per Character_Schema_v2
   - At least 1 character in party
   - No duplicate character names

2. **Location Validity**:
   - `location.current` exists in Campaign Data Vault
   - If `in_combat == true`, `combat_state.active == true`

3. **Quest Consistency**:
   - No quest in multiple states (completed AND active)
   - Active quest objectives reference valid quest_ids

4. **Reputation Bounds**:
   - NPC reputation: -10 to +10
   - Faction reputation: -10 to +10
   - Fame/infamy: 0 to 100

5. **Combat State**:
   - If `active == true`, `initiative_order` not empty
   - `current_turn` matches entry in `initiative_order`

6. **Time Constraints**:
   - `time_of_day` is one of: morning, afternoon, evening, night
   - `time_elapsed >= 0`
   - `time_minutes >= 0`

---

## Usage in Protocols

### Reading Party State
```yaml
# Get current location
current_location_id = party_state.location.current

# Check if quest is active
is_quest_active = "quest_mq2_three_fragments" IN party_state.campaign_state.quests_active

# Get NPC reputation
FOR npc_rep IN party_state.world_state.reputation.npcs:
  IF npc_rep.npc_id == "npc_zilvra_shadowveil":
    zilvra_rep = npc_rep.value
```

### Modifying Party State
```yaml
# Update location
party_state.location.previous = party_state.location.current
party_state.location.current = new_location_id

# Complete quest objective
FOR quest IN party_state.campaign_state.quests_active:
  IF quest.quest_id == "quest_mq2_three_fragments":
    ADD "wardens_sigil_obtained" TO quest.objectives_completed

# Modify reputation
FOR npc_rep IN party_state.world_state.reputation.npcs:
  IF npc_rep.npc_id == target_npc_id:
    npc_rep.value += reputation_change
    CLAMP npc_rep.value TO (-10, +10)
```

### Saving State
```yaml
# Update metadata
party_state.metadata.date = CURRENT_TIMESTAMP()
party_state.metadata.session_number += 1

# Serialize to JSON
json_output = SERIALIZE(party_state)

# Output download link
OUTPUT: "Save file ready for download"
OUTPUT: "computer:///outputs/party_state_session_{session_number}.json"
```

---

## Integration with Campaign Data Vault

Party state references Campaign Data Vault modules by ID:

```yaml
# Party is at Main Street
party_state.location.current = "loc_main_street"

# To get location details, AI calls:
Internal_Context_Retrieval("loc_main_street")

# Party has active quest
party_state.campaign_state.quests_active[0].quest_id = "quest_mq2_three_fragments"

# To get quest details, AI calls:
Internal_Context_Retrieval("quest_mq2_three_fragments")

# Party has reputation with NPC
party_state.world_state.reputation.npcs[0].npc_id = "npc_zilvra_shadowveil"

# To get NPC personality/goals, AI calls:
Internal_Context_Retrieval("npc_zilvra_shadowveil")
```

**This is the core V2 mechanism**: Party state stores IDs, AI retrieves full data from vault on-demand.

---

**Version**: 2.0.0
**Last Updated**: 2025-12-19
**Compatible With**: Protocol Library v2.0+, Campaign Data Vault v2.0+, Character Schema v2.0+
