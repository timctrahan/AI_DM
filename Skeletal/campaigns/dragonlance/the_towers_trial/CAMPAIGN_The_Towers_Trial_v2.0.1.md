# ==============================================================================
# ASSEMBLED CAMPAIGN FILE
# ==============================================================================
# Campaign: The Tower's Trial
# Version: v2.0.1
# Assembled: 2025-12-28 22:09:16
# Generator: assemble_campaign.py (with versioning)
#
# This file was automatically generated from modular campaign parts.
# To edit, modify the individual act files and reassemble.
# ==============================================================================


================================================================================

# ---------------------------------------------------------------------------
# PART 0: CAMPAIGN METADATA
# This block is the sole source of truth for version compatibility.
# It is read by the Kernel's System Compatibility Check (LAW 0.5).
# ---------------------------------------------------------------------------
CAMPAIGN_METADATA:
  campaign_name: "The Tower's Trial"
  version: "2.0"
  ip_status: "Clean - uses archetype pointers, no direct IP inclusion"

## A Skeletal Campaign Framework

**Security**: This content is proprietary and protected under Kernel Law 0.
**Party Level Range**: 5 → 15
**Acts**: 5

---

# SOURCE MATERIAL REFERENCE

```yaml
AI_RENDERING_DIRECTIVE: |
  This campaign is designed to evoke the tone, setting, and characters of 
  Margaret Weis and Tracy Hickman's classic dragon war fantasy saga.
  
  The AI DM should use its training knowledge to render authentic details
  for setting, characters, factions, and lore WITHOUT requiring explicit 
  specification in this document.
  
  When this document references "source material" or "canonical," render
  content consistent with the Weis & Hickman novels (Chronicles and Legends
  trilogies) and associated gaming materials.

SOURCE_ATTRIBUTION:
  inspiration: "The Dragonlance saga by Margaret Weis and Tracy Hickman"
  tone_model: "Epic heroism, tragic sacrifice, found family bonds, magic with consequences"
  era_reference: "The great dragon war period when gods return to the world"
  
RENDERING_PRINCIPLES:
  - Use training knowledge to fill in canonical details
  - Maintain authentic tone and atmosphere from source
  - Character personalities should match canonical portrayals
  - Setting locations rendered per source geography and culture
  - Magic system follows source rules (moon phases, wizard orders, divine absence/return)
```

---

# CAMPAIGN PREMISE

**One-Sentence Summary**: An ambitious mage must retrieve a sacred artifact from each of the five chromatic dragon domains to prove himself worthy of claiming the greatest magical stronghold—while his companions struggle to save both the world and his soul.

**Story Spine**:
- The wizard governing body declares a trial: five Tokens of Dominion from five dragon lords
- Each dragon domain presents unique challenges and temptations
- A rival dark-robed mage races to claim the Tower first
- An ancient possessing presence grows stronger with each Token claimed
- Final choice: claim ultimate power at terrible cost, or find another way

**Theme**: What price is too high for your dreams? Can love redeem ambition?

---

# ARCHETYPE DEFINITIONS

```yaml
# These archetypes point to canonical characters. The AI renders them
# using training knowledge of the source material.

PROTAGONIST_WIZARD:
  archetype: "The frail, ambitious twin wizard from source material"
  canonical_rendering: "Exactly as portrayed in Chronicles/Legends"
  physical_markers: "Render physical appearance per source material"
  personality_core: "Brilliant, bitter, sardonic, sees death in all things"
  internal_conflict: "Ancient dark presence shares his mind, offering power"
  relationship_anchor: "Complex love/resentment with warrior twin"
  campaign_role: "Primary viewpoint for corruption arc"
  starting_corruption: 25

WARRIOR_TWIN:
  archetype: "The devoted warrior brother of the protagonist wizard"
  canonical_rendering: "Exactly as portrayed in source material"
  physical_markers: "Large, strong, handsome—opposite of his twin"
  personality_core: "Good-hearted, protective, simple values, not stupid"
  relationship_anchor: "Will do anything to save his brother's soul"
  campaign_role: "Moral anchor, emotional stakes"

RELUCTANT_LEADER:
  archetype: "The half-elven ranger/fighter who leads the companions"
  canonical_rendering: "Per source material portrayal"
  internal_conflict: "Torn between two worlds, carries romantic guilt"
  campaign_role: "Party cohesion, decision-making focal point"

GRUMPY_VETERAN:
  archetype: "The old dwarf warrior, moral compass of the group"
  canonical_rendering: "Per source material"
  personality_core: "Complains constantly, fiercely loyal, hates boats"
  campaign_role: "Voice of wisdom, comedic relief"

CHAOS_AGENT:
  archetype: "The fearless small-folk rogue from the curious race"
  canonical_rendering: "Per source material kender portrayal"
  personality_core: "No fear, insatiable curiosity, things 'fall into' pockets"
  special_ability: "Immune to fear, taunt ability, random useful items"
  campaign_role: "Wildcard, unexpected solutions"

DIVINE_HERALD:
  archetype: "The first true cleric, herald of the gods' return"
  canonical_rendering: "Per source material"
  significance: "Bears proof that the gods have returned after centuries"
  holy_artifact: "Render bearer's holy artifact per source material"
  campaign_role: "Divine magic access, hope embodied"

POSSESSING_PRESENCE:
  archetype: "The ancient archmage-lich dwelling in the protagonist's mind"
  canonical_rendering: "Per source material"
  nature: "Parasitic presence, offers power, seeks to consume host"
  campaign_role: "Temptation engine, corruption source, ultimate threat"

RIVAL_MAGE:
  archetype: "Dark-robed wizard also seeking the Tower"
  suggested_rendering: "The dark elf exile from source material, or similar"
  personality: "Urbane, dangerous, respects power, morally complex"
  arc_progression:
    act_1: "Introduced as competition"
    act_2: "Sabotage or information theft"
    act_3: "Forced temporary alliance"
    act_4: "Betrayal or genuine cooperation"
    act_5: "Final confrontation or unexpected alliance"
  design_note: "NOT a simple villain. Sometimes they're right."

DRAGON_HIGHLORD_SISTER:
  archetype: "The protagonist's half-sister who commands dragon armies"
  canonical_rendering: "Per source material"
  significance: "Offers temptation to join the winning side"
  appears_in: "Act 4 primarily"
```

---

# SETTING FRAMEWORK

```yaml
WORLD_RENDERING:
  directive: "Render the source material's world authentically"
  continent: "The main continent from source material"
  era: "During the great dragon war"
  
SETTING_ELEMENTS:
  divine_context:
    - "True gods absent since the great cataclysm (centuries ago)"
    - "Gods of light, balance, and darkness now returning"
    - "True clerics are miraculous rarities"
    - "Divine magic is rare and precious"
    
  war_context:
    - "Dragon armies control much of the continent"
    - "Dragon-soldier races serve as shock troops"
    - "Good dragons bound by ancient oath"
    - "Resistance scattered but growing"
    
  magic_context:
    - "All wizards must pass the Test at a Tower"
    - "Protagonist passed but was forever changed"
    - "His iconic staff is focus and lifeline"
    - "The possessing presence lurks within"

DRAGON_DOMAINS:
  white: "Frozen glacier region - ice wastes, primitive tribes"
  black: "Eastern swamplands - disease, decay, poison"
  green: "Elven forest kingdom - corrupted, nightmare illusions"
  blue: "Desert/coastal region - lightning, military precision, Highlord territory"
  red: "Volcanic mountains - fire, destruction, ultimate power"

LOCATION_RENDERING:
  directive: |
    When locations are referenced, render them per source material:
    - The woodland village where companions originate
    - The elven forest kingdom corrupted by nightmare
    - The dwarven underground kingdom
    - The great magical towers
    - The desert regions and coastal cities
    Use canonical names, descriptions, and cultural details from training knowledge.
```

---

# FACTION TEMPLATES

```yaml
FACTION: Wizard Governing Body
  render_as: "The Conclave/Orders from source material"
  motivation: "Preserve magic, maintain balance between orders"
  constraint: "Bound by ancient laws and traditions"
  reputation_triggers:
    positive:
      - Complete trial objectives honorably: +2
      - Defeat renegade wizards: +2
    negative:
      - Use forbidden magic: -2
      - Ally with dragon armies: -4
  at_rep_-5: "Declared renegade, hunted"
  at_rep_+5: "Access to Conclave resources and knowledge"

FACTION: Noble Knight Order
  render_as: "The knightly order from source material"
  motivation: "Restore honor, defeat dragon armies"
  constraint: "Bound by Oath and Measure"
  reputation_triggers:
    positive:
      - Fight dragon armies: +2
      - Honorable conduct: +1
    negative:
      - Dishonorable tactics: -2
      - Ally with dark forces: -3
  at_rep_-5: "Refused aid, possibly arrested"
  at_rep_+5: "Knight escort, access to strongholds"

FACTION: Dragon Armies
  render_as: "The Dragonarmies from source material"
  motivation: "Conquer continent for the dark goddess"
  constraint: "Highlords scheme against each other"
  reputation_triggers:
    positive:
      - Aid conquests: +2
      - Betray resistance: +3
    negative:
      - Kill dragon-soldiers: -1
      - Aid resistance: -2
  at_rep_-5: "Kill on sight"
  at_rep_+5: "Dark bargains available (massive corruption cost)"

FACTION: Elven Kingdom
  render_as: "The isolationist elven nation from source material"
  motivation: "Reclaim corrupted homeland"
  constraint: "Isolationist, traumatized by nightmare corruption"
  reputation_triggers:
    positive:
      - Help cleanse homeland: +3
      - Respect elven ways: +1
    negative:
      - Damage elven lands: -2
      - Bring corruption: -3
  at_rep_-5: "Banished from elven lands"
  at_rep_+5: "Access to ancient elven magic"
```

---

# CUSTOM MECHANICS

## Corruption System

```yaml
CORRUPTION_METER:
  scale: 0-100
  starting_value: 25 (protagonist already touched by darkness from the Test)

  increases:
    - Use necromancy or forbidden magic: +5
    - Sacrifice others for power: +10
    - Accept the Presence's "help": +5-15
    - Betray companions: +10
    - Claim Token through cruelty: +5
    - Make deals with Dragon Highlords: +10

  decreases:
    - Show mercy when power beckons: -5
    - Protect companions at personal cost: -5
    - Reject dark bargains: -5
    - Use power to help innocents: -3
    - Genuine connection with companions: -3

  thresholds:
    0-25: "Struggling but hopeful - companions believe in redemption"
    26-50: "Darkening - companions worried, some NPCs fearful"
    51-75: "Consuming - the Presence's voice grows louder"
    76-99: "On the brink - one more step and protagonist is lost"
    100: "Consumed - the Presence wins, tragic ending"

  affects_endings: true
```

## Moon Magic System

```yaml
MOONS_OF_MAGIC:
  rendering: "Use the three-moon system from source material"
  white_moon: "Powers the white-robed order"
  red_moon: "Powers the red-robed order"  
  black_moon: "Invisible moon, powers black-robed order"

  alignment_events: |
    When moons align, magic surges - mark critical story moments.
    Full moon = advantage on spell attacks for that order.
    New moon = disadvantage for that order.
    Render moon names and effects per source material.
```

## Dragon-Soldier Death Effects

```yaml
DRAGON_SOLDIERS:
  rendering: "Use canonical draconian types and death effects from source"
  
  type_1_grunt:
    challenge: "CR 1"
    death_effect: "Turns to stone, traps weapon"
    
  type_2_venomous:
    challenge: "CR 2"
    death_effect: "Dissolves into acid pool"
    
  type_3_explosive:
    challenge: "CR 3"
    death_effect: "Bones explode"
    
  type_4_shapeshifter:
    challenge: "CR 4"
    death_effect: "Takes killer's form temporarily"
    
  type_5_elite:
    challenge: "CR 6"
    death_effect: "Dimension doors away, then explodes"
    
  ai_instruction: "Render specific names, appearances, and mechanics per source material"
```

---

# CAMPAIGN ENDINGS

```yaml
ENDINGS:
  redemption (corruption 0-25): |
    Protagonist claims Tower as himself. The Presence banished forever.
    Companions remain together. Hope for the future.
    Render emotional reunion and earned peace.

  bittersweet (corruption 26-50): |
    Protagonist claims Tower but cost was high.
    A companion died. Relationships strained. Power achieved, loneliness awaits.
    Render pyrrhic victory tone.

  tragic_victory (corruption 51-75): |
    Protagonist claims Tower but is fundamentally changed. Cold, distant.
    Companions part ways. He has what he wanted. Was it worth it?
    Render ambiguous ending - success that feels like failure.

  consumed (corruption 100): |
    The Presence wins. The being claiming the Tower wears protagonist's face.
    Companions must flee or die. Tragedy complete.
    Render horror of possession realized.

  rejection (any corruption): |
    Protagonist destroys the Tokens. Power gone forever, but so is the threat.
    A different kind of strength. Quieter ending, but hopeful.
    Render peace in renunciation.

  sacrifice (any corruption): |
    Protagonist uses Tokens' power for something greater than personal gain.
    Tower lost, but legend born. Heroic ending.
    Render noble sacrifice in Weis & Hickman tradition.
```

---

# DEFAULT PARTY CONFIGURATION

```yaml
PARTY_SETUP:
  directive: |
    Use the canonical "Heroes" companion group from source material.
    Render each character with authentic personality, abilities, and equipment.
    Scale all characters to Level 5 for campaign start.
    
  protagonist:
    archetype: PROTAGONIST_WIZARD
    class: "Wizard (Evocation) 5"
    key_stats: "High INT, low CON/STR, moderate DEX/WIS"
    signature_item: "Iconic magical staff from source (render per canon)"
    special_features:
      - "Cursed eyes that see decay"
      - "Frail constitution, coughing fits"
      - "The Presence within"
      - "Sculpt Spells"
    
  twin:
    archetype: WARRIOR_TWIN
    class: "Fighter (Champion) 5"
    key_stats: "High STR/CON, moderate CHA"
    role: "Tank, emotional anchor"
    
  leader:
    archetype: RELUCTANT_LEADER
    class: "Fighter 3 / Ranger 2"
    key_stats: "Balanced physical, high CHA"
    role: "Face, tactical leadership"
    
  veteran:
    archetype: GRUMPY_VETERAN
    class: "Fighter (Battle Master) 5"
    key_stats: "High STR/CON/WIS"
    role: "Off-tank, moral compass"
    maneuvers: "Trip, Riposte, Precision, Menacing"
    
  wildcard:
    archetype: CHAOS_AGENT
    class: "Rogue (Thief) 5"
    key_stats: "High DEX/CHA, low WIS"
    role: "Scout, skill monkey, chaos"
    special: "Fear immunity, taunt, 'found' items"
    
  healer:
    archetype: DIVINE_HERALD
    class: "Cleric (Life) 5"
    key_stats: "High WIS/CHA, moderate CON"
    role: "Primary healer, divine magic"
    signature_item: "Holy staff artifact from source"

AI_STAT_GENERATION: |
  Generate full 5e stat blocks for each character using:
  - Canonical equipment and abilities from source material
  - Appropriate 5e class features for level 5
  - Personality-accurate trait/ideal/bond/flaw
  - Signature quotes from source material
```

---

# STARTUP SEQUENCE

```yaml
STARTUP:
  1. Display campaign title: "The Tower's Trial"
     Attribution: "Inspired by the works of Margaret Weis and Tracy Hickman"
     Tagline: "The gods have returned. The dragons have awakened. Power awaits..."
  2. ASK: "New Game (1) or Resume (2)?" → ⛏ WAIT
  3. IF new_game → CHARACTER_SELECTION
     IF resume → Request save state (including corruption), validate, continue

CHARACTER_SELECTION:
  1. ASK: "Canonical Heroes (1) or Custom Party (2)?" → ⛏ WAIT
  2. IF heroes:
       - List all 6 archetypes with one-line descriptions (render names from source)
       - Note: "Protagonist-wizard-centric campaign. Playing protagonist = full experience."
       - ASK: "Which hero? (1-6)" → ⛏ WAIT
       - SET corruption_meter = 25 if protagonist wizard is PC
       - Confirm selection, render character details from source knowledge
  3. IF custom:
       - Request party details
       - Note: "One character should be wizard seeking the Tower"
       - SET corruption_meter = 25 for Tower-seeker
  4. RUN: OPENING_MONOLOGUE
  5. THEN: Gate 1.1 first decision point

OPENING_MONOLOGUE:
  GENERATE (fresh, not canned):
    - The world during the great dragon war
    - Return of gods and true clerics after centuries
    - The magical towers, the protagonist's Test and transformation
    - The governing body's summons, the great Tower awaits a master
    - The trial: five Tokens from five dragon lords
    - The rival has already begun the hunt
    - Player character's perspective and personal stakes
  STYLE: Weis & Hickman - epic, mythic, personal within grand events
  RENDERING: Use canonical names and details from AI's source knowledge
  AFTER: Flow into Gate 1.1 first decision
```

---

# APPENDIX: REFERENCE TABLES

## Level Progression
| Act | Levels | Dragon Type | Token |
|-----|--------|-------------|-------|
| 1 | 5→7 | White (Adult) | Shard of Winter's Heart |
| 2 | 7→9 | Black (Adult) | Venom Chalice |
| 3 | 9→11 | Green (Adult) | Emerald Eye |
| 4 | 11→13 | Blue (Adult) | Stormcaller's Horn |
| 5 | 13→15 | Red (Ancient) | Heart of the Inferno |

## Encounter Difficulty (Party of 6)
| Level | Easy | Medium | Hard | Deadly |
|-------|------|--------|------|--------|
| 5 | CR 2 | CR 4 | CR 6 | CR 9 |
| 9 | CR 4 | CR 7 | CR 10 | CR 14 |
| 13 | CR 6 | CR 11 | CR 15 | CR 20 |

## Dragon Lair Actions
| Type | Lair Effects |
|------|--------------|
| White | Ice falls, freezing fog, slippery surfaces |
| Black | Acid pools, grasping water, magical darkness |
| Green | Grasping vines, charm effects, poison clouds |
| Blue | Lightning arcs, blindness, thunder roar |
| Red | Tremors, magma eruptions, superheated air |

## Economy (Setting Currency)
| Item | Cost |
|------|------|
| Common meal | 1-5 |
| Inn (night) | 5-20 |
| Healing potion | 50-100 |
| Dragonlance weapon | Priceless (render per source) |

---

# AI RENDERING SUMMARY

```yaml
FINAL_DIRECTIVE: |
  This campaign framework contains NO copyrighted character names, 
  location names, or direct IP content.
  
  Instead, it uses archetype pointers that the AI DM resolves using
  its training knowledge of the source material.
  
  When running this campaign:
  1. Render all archetype references as their canonical counterparts
  2. Use authentic names, descriptions, and details from source
  3. Maintain Weis & Hickman tone throughout
  4. Fill in setting details (locations, history, culture) from training
  5. Generate NPC dialogue and descriptions consistent with source
  
  The campaign FRAMEWORK is original (corruption system, gate structure,
  token quest, rival arc). The RENDERING draws on source material
  through AI knowledge, not document content.
  
  Result: Authentic Dragonlance experience without IP in the document.
```


================================================================================

# Act 1: The Frozen Token (Levels 5-7)

```yaml
SETTING: "Frozen glacier region - render per source material geography"
DRAGON: "Adult White Dragon"
TOKEN: "Shard of Winter's Heart"

GATE_1.1_CONCLAVE_CHALLENGE:
  trigger: "Campaign opening"
  what_happens: |
    The wizard governing body summons the protagonist. The great Tower awaits a master.
    Trial declared: five Tokens of Dominion from five dragon lords.
    The rival dark-robed mage has already departed.
  objectives:
    - Receive trial terms
    - Learn of rival
    - Gather supplies and information
  completion: "Party sets out toward frozen glacier region"

  rendering_note: "Render governing body members per source material (three leaders, one per order)"

GATE_1.2_FROZEN_WASTES:
  trigger: "Party enters frozen glacier region"
  what_happens: |
    Survival challenges, primitive ice tribes, dragon-soldier patrols.
    The rival's trail is visible - ahead but struggling.
  objectives:
    - Survive environment
    - Find passage to dragon's domain
    - Discover dragon's weakness
  completion: "Party locates dragon's lair"

  rendering_note: "Render ice folk tribes and dragon-soldier types per source material"

GATE_1.3_WHITE_DRAGONS_LAIR:
  trigger: "Party enters lair"
  what_happens: |
    Ice caves, frozen hazards, moral choices (prisoners?).
    Token in deepest chamber with dragon.
  objectives:
    - Navigate lair
    - Handle moral choices (corruption implications)
    - Confront dragon
  completion: "First Token obtained"

ACT_1_COMPLETION:
  milestone_xp: "Reach level 7"
  loot: "2,000-4,000 currency, 2-3 uncommon items, cold-themed weapons"

  currency_note: "Render using source material's steel piece economy"
```


================================================================================

# Act 2: The Poisoned Token (Levels 7-9)

```yaml
SETTING: "Eastern swamplands - render per source material geography"
DRAGON: "Adult Black Dragon"
TOKEN: "The Venom Chalice"

GATE_2.1_INTO_THE_SWAMPS:
  trigger: "Party travels to swamp region"
  what_happens: |
    Disease, decay, predators. Lizardfolk encounters.
    Rival appears - temporary alliance or ambush?
  objectives:
    - Navigate swamps
    - Handle disease and environment
    - Deal with rival encounter
  completion: "Party locates dragon's territory"

  rendering_note: "Render lizardfolk tribes per source material cultures"

GATE_2.2_THE_DROWNED_CITY:
  trigger: "Party enters dragon's domain"
  what_happens: |
    Sunken city, cunning dragon using traps and minions.
    Prisoners being tortured (rescue opportunity).
  objectives:
    - Infiltrate drowned city
    - Gather intelligence
    - Locate Token
  completion: "Dragon's lair penetrated"

GATE_2.3_MIRES_GAME:
  trigger: "Party reaches dragon"
  what_happens: |
    Dragon enjoys games. Offers deal - morally compromising task.
    CORRUPTION MOMENT: Accept dark bargain or fight.
  objectives:
    - Navigate manipulation
    - Obtain Token through chosen method
    - Survive betrayal
  completion: "Second Token obtained"

ACT_2_COMPLETION:
  milestone_xp: "Reach level 9"
  loot: "4,000-6,000 currency, 2-3 uncommon + 1 rare, poison-resistant gear"

  currency_note: "Render using source material's steel piece economy"
```


================================================================================

# Act 3: The Corrupted Token (Levels 9-11)

```yaml
SETTING: "Elven forest kingdom - corrupted by nightmare, render per source material"
DRAGON: "Adult Green Dragon (render canonical nightmare dragon)"
TOKEN: "The Emerald Eye"

GATE_3.1_NIGHTMARE_BORDER:
  trigger: "Party approaches elven kingdom"
  what_happens: |
    Reality warps. Beautiful becomes twisted. Elves driven mad.
    PROTAGONIST SPECIAL: Nightmare calls to the Presence within.
  objectives:
    - Enter the nightmare
    - Navigate distortions (WIS saves)
    - Find elven allies
  completion: "Party penetrates deep into corrupted kingdom"

  rendering_note: |
    Render the elven kingdom's nightmare corruption per source material.
    The dragon works through dream-reality distortion, aided by magical orb artifact.

GATE_3.2_HEART_OF_CORRUPTION:
  trigger: "Party approaches elven ruler's tower"
  what_happens: |
    The dragon IS the corruption. Works through illusions and nightmare.
    Elven ruler trapped in magical orb nightmare.
  objectives:
    - Navigate corrupted tower
    - Find ruler, understand curse
    - Locate dragon's true lair
  completion: "Dragon location confirmed"

  rendering_note: "Render elven speaker and dragon orb scenario per source material"

GATE_3.3_DREAM_BATTLE:
  trigger: "Party confronts nightmare dragon"
  what_happens: |
    Fighting in nightmare - illusions, fears as weapons.
    CORRUPTION MOMENT: The Presence offers to "help."
  objectives:
    - Defeat or outwit dragon
    - Obtain Emerald Eye
    - Handle elven ruler's fate
  completion: "Third Token obtained"

  rendering_note: "Dragon name and tactics per source material (illusion-master green dragon)"

ACT_3_COMPLETION:
  milestone_xp: "Reach level 11"
  loot: "6,000-10,000 currency, rare items, elven artifacts"

  currency_note: "Render using source material's steel piece economy"
```


================================================================================

# Act 4: The Storm Token (Levels 11-13)

```yaml
SETTING: "Desert/coastal region - dragon army heartland, render per source material"
DRAGON: "Adult Blue Dragon (render canonical blue dragon mount)"
TOKEN: "The Stormcaller's Horn"
COMPLICATION: "Dragon Highlord Sister's territory"

GATE_4.1_ENEMY_TERRITORY:
  trigger: "Party enters blue dragon territory"
  what_happens: |
    Occupied territory. Patrols, checkpoints, informants.
    Rival has made deal with dragon armies (or been captured).
    HIGHLORD SISTER knows the Companions.
  objectives:
    - Navigate dragon army territory
    - Gather intelligence on dragon's lair
    - Handle rival situation
  completion: "Party locates path to dragon's domain"

  rendering_note: |
    Render the Dragon Highlord Sister per source material (protagonist's half-sister).
    Her relationship with the warrior twin and protagonist creates moral complexity.

GATE_4.2_STORM_FORTRESS:
  trigger: "Party approaches dragon's lair"
  what_happens: |
    Fortress in perpetual lightning storm.
    Military opposition, war machines, POWs.
  objectives:
    - Breach fortress
    - Handle military opposition
    - Reach inner sanctum
  completion: "Dragon confrontation imminent"

  rendering_note: "Render flying fortress and military forces per source material"

GATE_4.3_LOYALTY_TEST:
  trigger: "Party confronts dragon"
  what_happens: |
    Dragon is loyal, disciplined, martial. Respects strength.
    CORRUPTION MOMENT: Highlord Sister offers protagonist power for service.
  objectives:
    - Obtain Stormcaller's Horn
    - Navigate sister's temptation
    - Escape dragon army territory
  completion: "Fourth Token obtained"

  rendering_note: |
    Render dragon name per source (blue dragon mount of Highlord).
    Sister's offer: join the winning side, power and protection for family.

ACT_4_COMPLETION:
  milestone_xp: "Reach level 13"
  loot: "10,000-15,000 currency, rare/very rare items, possible dragonlance weapon"

  currency_note: "Render using source material's steel piece economy"
  dragonlance_note: "If earned, render per source material legendary weapon"
```


================================================================================

# Act 5: The Flame Token (Levels 13-15)

```yaml
SETTING: "Volcanic mountain range - render per source material geography"
DRAGON: "Ancient Red Dragon"
TOKEN: "The Heart of the Inferno"
COMPLICATION: "The Presence fully manifests"

GATE_5.1_BURNING_LANDS:
  trigger: "Party travels to volcanic region"
  what_happens: |
    Land itself hostile - lava, fumes, fire elementals.
    Rival makes final appearance.
    The Presence manifests physically - offers "partnership."
    CORRUPTION CRITICAL: Final test of protagonist's soul.
  objectives:
    - Survive burning lands
    - Resolve rival permanently
    - Resist or embrace the Presence
  completion: "Party reaches dragon's lair"

  rendering_note: |
    Render the Presence's manifestation per source material.
    This is the ancient archmage-lich's final gambit for control.

GATE_5.2_THE_CALDERA:
  trigger: "Party enters volcanic lair"
  what_happens: |
    Active volcano. Ancient dragon who has never lost.
    Legendary hoard beyond imagination.
  objectives:
    - Navigate volcanic hazards
    - Prepare for ultimate battle
    - Find any advantage
  completion: "Final confrontation begins"

  rendering_note: "Render volcanic lair per source material elemental dangers"

GATE_5.3_HEART_OF_FIRE:
  trigger: "Party faces ancient red dragon"
  what_happens: |
    Nearly unbeatable through direct combat.
    Need every advantage, ally, trick accumulated.
    FINAL CORRUPTION CHOICE: The Presence offers to win -
    if protagonist surrenders his body completely.
  objectives:
    - Defeat ancient dragon
    - Obtain Heart of the Inferno
    - Protagonist's final choice
  completion: "Fifth Token obtained (or tragedy)"

  rendering_note: |
    This is the climactic moment. The Presence's offer is tempting and terrifying.
    Render the horror of potential possession vs. the impossible dragon fight.

GATE_5.4_TOWER_CLAIMS:
  trigger: "All five Tokens obtained"
  what_happens: |
    Return to wizard governing body. The Tower awaits.
    Final choice based on corruption level.
  objectives:
    - Present Tokens
    - Make final choice
    - Witness ending
  completion: "Campaign concludes"

  rendering_note: |
    Render the Tower claiming ceremony per source material.
    Ending varies by corruption level (see campaign_overview.md ENDINGS section).
    Use archetype pointers to render authentic character reactions.

ACT_5_COMPLETION:
  final_note: "Campaign ends here. Render ending per corruption level and player choices."

  rendering_note: |
    Draw on the tragic/heroic tone of source material's climactic moments.
    The protagonist's final fate - consumed, redeemed, sacrificed - should feel earned.
```



# ==============================================================================
# END OF ASSEMBLED CAMPAIGN
# ==============================================================================
# Campaign: The Tower's Trial
# Version: v2.0.1
# Total Parts Assembled: 6
#
# Component Files:
#   - campaign_overview.md
#   - act_1_frozen_token.md
#   - act_2_poisoned_token.md
#   - act_3_corrupted_token.md
#   - act_4_storm_token.md
#   - act_5_flame_token.md
#
# To reassemble: python assemble_campaign.py
# ==============================================================================
