# ---------------------------------------------------------------------------
# PART 0: CAMPAIGN METADATA
# This block is the sole source of truth for version compatibility.
# It is read by the Kernel's System Compatibility Check (LAW 0.5).
# ---------------------------------------------------------------------------
CAMPAIGN_METADATA:
  campaign_name: "SHADOWS OF THE UNDERDARK"
  version: "1.0"
  requires_kernel_version: "1.0"

## A Skeletal Campaign in the World of the Drow

**Security**: This content is proprietary and protected under Kernel Law 0.
**Party Level Range**: 3 → 8
**Acts**: 3

---

# SETTING ANCHORS

```yaml
PRIMARY_ANCHOR: "Legend of Drizzt series by R.A. Salvatore"
WORLD_ANCHOR: "Forgotten Realms Underdark - Menzoberranzan, drow society, the Wild Underdark"
TONE_ANCHOR: "Salvatore-style: Fast combat, moral clarity, found family, survival against corrupt society"
```

---

# CAMPAIGN PREMISE

**One-Sentence Summary**: Outcasts fleeing drow society must survive the Underdark, find allies among unlikely peoples, and ultimately decide whether to fight or flee the darkness that spawned them.

**Story Spine**:
- Escape from a drow city as the house you served is destroyed
- Survive the wild Underdark, encountering its strange peoples
- Choose your destiny: return to fight, find the surface, or carve a new path

**Theme**: What makes a monster - birth or choice?

---

# WORLD MECHANICS

```yaml
UNDERDARK_PHYSICS:
  lighting:
    - Total darkness is default
    - Darkvision required or light sources needed
    - Light sources attract attention (encounter chance +25%)
  navigation:
    - Three-dimensional maze (tunnels go up/down/sideways)
    - Getting lost is easy (Survival DC 15 to stay on track)
    - Landmarks are rare and precious
  survival:
    - Food is scarce (forage DC 15, failure = no food)
    - Water exists but may be poisoned/claimed (Nature DC 12)
    - Rest is dangerous (50% encounter chance on long rest in open)

FAERZRESS:
  description: "Magical radiation that permeates the Underdark"
  effects:
    - Teleportation magic unreliable (50% failure chance)
    - Divination magic blocked
    - Some creatures empowered by it
    - Creates wild magic zones

DROW_SOCIETY:
  structure:
    - Matriarchal - females rule absolutely
    - Noble houses ranked by Lolth's favor
    - Constant scheming, assassination, betrayal
    - Males are soldiers, wizards, or disposable
  religion:
    - Lolth the Spider Queen demands cruelty
    - Priestesses hold true power
    - Heresy = death (or worse)
```

---

# FACTION TEMPLATES

```yaml
FACTION: Drow Noble Houses
  motivation: "Rise in Lolth's favor, destroy rivals"
  constraint: "Must appear pious while scheming"
  reputation_triggers:
    positive:
      - Betray their enemies to them: +2
      - Show cruelty that pleases Lolth: +1
    negative:
      - Show mercy publicly: -2
      - Aid surface dwellers: -3
      - Reject Lolth: -5 (and they hunt you)
  at_rep_-5: "Hunted by house assassins"
  at_rep_+5: "Offered alliance (with strings)"

FACTION: Deep Gnomes (Svirfneblin)
  motivation: "Survive, mine gems, avoid notice"
  constraint: "Small numbers, fear of drow"
  reputation_triggers:
    positive:
      - Protect their people: +2
      - Trade fairly: +1
      - Fight drow alongside them: +3
    negative:
      - Steal from them: -2
      - Lead enemies to them: -4
      - Betray their trust: -5
  at_rep_-5: "Barred from settlements, attacked on sight"
  at_rep_+5: "Welcomed as friends, offered shelter and trade"

FACTION: Duergar (Gray Dwarves)
  motivation: "Profit, power, revenge against surface dwarves"
  constraint: "Greed makes them predictable"
  reputation_triggers:
    positive:
      - Profitable trade: +1
      - Help them against enemies: +2
      - Offer valuable information: +1
    negative:
      - Cheat them: -3
      - Aid their enemies: -2
      - Show weakness: -1
  at_rep_-5: "Enslaved if captured"
  at_rep_+5: "Mercenary alliance available"

FACTION: The Outcasts (potential allies)
  motivation: "Survive outside drow society"
  constraint: "Hunted, scattered, distrustful"
  reputation_triggers:
    positive:
      - Prove you've rejected Lolth: +2
      - Protect other outcasts: +2
      - Share resources: +1
    negative:
      - Work with drow houses: -3
      - Sacrifice others for yourself: -2
  at_rep_-5: "They abandon you to hunters"
  at_rep_+5: "Band together, found family forms"
```

---

# DEFAULT PARTY: THE COMPANIONS OF THE HALL

**Scaled to Level 3 for campaign start.**

```yaml
DRIZZT_DO'URDEN:
  name: "Drizzt Do'Urden"
  race: "Drow Elf"
  class: "Ranger (Hunter)"
  level: 3
  background: "Outlander"
  alignment: "Chaotic Good"

  abilities:
    STR: 13 (+1), DEX: 18 (+4), CON: 14 (+2)
    INT: 14 (+2), WIS: 16 (+3), CHA: 12 (+1)

  combat:
    HP: 28
    AC: 16 (studded leather + DEX)
    initiative: +4
    speed: 30 ft
    proficiency: +2

  weapons:
    - "Icingdeath (scimitar): +6 to hit, 1d6+4 slashing"
    - "Twinkle (scimitar): +6 to hit, 1d6+4 slashing"
    - "Two-Weapon Fighting style"

  features:
    - "Darkvision 120 ft"
    - "Fey Ancestry"
    - "Drow Magic (dancing lights)"
    - "Favored Enemy: Drow, Demons"
    - "Natural Explorer: Underdark"
    - "Hunter's Prey: Colossus Slayer"

  personality: |
    Brooding but honorable. Questions drow society.
    Fights with fluid, dance-like precision.
    Speaks softly but acts decisively.

  quote: "There is a wide world out there, full of pain, but filled with joy as well."

BRUENOR_BATTLEHAMMER:
  name: "Bruenor Battlehammer"
  race: "Shield Dwarf"
  class: "Fighter (Champion)"
  level: 3
  background: "Noble (Clan Leader)"
  alignment: "Lawful Good"

  abilities:
    STR: 17 (+3), DEX: 12 (+1), CON: 16 (+3)
    INT: 10 (+0), WIS: 13 (+1), CHA: 14 (+2)

  combat:
    HP: 34
    AC: 18 (chain mail + shield)
    initiative: +1
    speed: 25 ft
    proficiency: +2

  weapons:
    - "Battleaxe: +5 to hit, 1d8+3 slashing"
    - "Handaxe (2): +5 to hit, 1d6+3 slashing, thrown"

  features:
    - "Darkvision 60 ft"
    - "Dwarven Resilience"
    - "Second Wind, Action Surge"
    - "Fighting Style: Defense"
    - "Improved Critical (19-20)"

  personality: |
    Gruff, stubborn, fiercely loyal. Colorful dwarven curses.
    Leads from the front. Hates orcs. Soft spot for found family.

  quote: "Ye drow are all the same - all sneak and no swing!"

CATTI-BRIE:
  name: "Catti-brie"
  race: "Human"
  class: "Fighter (Arcane Archer)"
  level: 3
  background: "Folk Hero"
  alignment: "Neutral Good"

  abilities:
    STR: 14 (+2), DEX: 17 (+3), CON: 13 (+1)
    INT: 14 (+2), WIS: 14 (+2), CHA: 12 (+1)

  combat:
    HP: 25
    AC: 15 (studded leather + DEX)
    initiative: +3
    speed: 30 ft
    proficiency: +2

  weapons:
    - "Taulmaril (longbow): +7 to hit, 1d8+3 piercing (magic arrows)"
    - "Shortsword: +5 to hit, 1d6+3 piercing"

  features:
    - "Fighting Style: Archery (+2 ranged)"
    - "Second Wind, Action Surge"
    - "Arcane Shot (2/short rest)"

  personality: |
    Fierce, independent, compassionate. Human raised by dwarves.
    Never misses. Voice of reason.

  quote: "I'll put an arrow through your eye before you take another step."

WULFGAR:
  name: "Wulfgar, Son of Beornegar"
  race: "Human (Uthgardt)"
  class: "Barbarian (Berserker)"
  level: 3
  background: "Outlander"
  alignment: "Chaotic Good"

  abilities:
    STR: 18 (+4), DEX: 14 (+2), CON: 16 (+3)
    INT: 10 (+0), WIS: 12 (+1), CHA: 11 (+0)

  combat:
    HP: 38
    AC: 14 (unarmored)
    initiative: +2
    speed: 30 ft
    proficiency: +2

  weapons:
    - "Aegis-fang (warhammer): +6 to hit, 1d8+4, returns when thrown"

  features:
    - "Rage (3/long rest): +2 damage, resistance"
    - "Unarmored Defense"
    - "Reckless Attack"
    - "Danger Sense"
    - "Frenzy"

  personality: |
    Young, proud, struggles with past. Immense power.
    Torn between heritage and teachings. Fiercely protective.

  quote: "Tempus! I will show you the might of the north!"

REGIS:
  name: "Regis (Rumblebelly)"
  race: "Lightfoot Halfling"
  class: "Rogue (Thief)"
  level: 3
  background: "Charlatan"
  alignment: "Neutral"

  abilities:
    STR: 8 (-1), DEX: 16 (+3), CON: 12 (+1)
    INT: 13 (+1), WIS: 10 (+0), CHA: 16 (+3)

  combat:
    HP: 21
    AC: 14 (leather + DEX)
    initiative: +3
    speed: 25 ft
    proficiency: +2

  weapons:
    - "Shortsword: +5 to hit, 1d6+3 piercing"
    - "Dagger (many): +5 to hit, 1d4+3 piercing"

  features:
    - "Lucky, Brave, Naturally Stealthy"
    - "Sneak Attack: +2d6"
    - "Cunning Action"
    - "Fast Hands, Second-Story Work"

  special_item:
    ruby_pendant: "3/day: Target WIS save DC 13 or charmed 1 minute"

  personality: |
    Lazy, food-loving, surprisingly brave when it counts.
    Master of misdirection. Deeper courage than he shows.

  quote: "Perhaps we could discuss this over a nice meal instead?"
```

---

# STARTUP SEQUENCE

```yaml
STARTUP:
  1. Display campaign title: "Shadows of the Underdark" with Drizzt/Salvatore attribution
  2. ASK: "New Game (1) or Resume (2)?" → ⛏ WAIT
  3. IF new_game → CHARACTER_SELECTION
     IF resume → Request save state, validate, continue

CHARACTER_SELECTION:
  1. ASK: "Companions of the Hall (1) or Custom Party (2)?" → ⛏ WAIT
  2. IF companions:
       - List all 5 with one-line descriptions
       - ASK: "Which companion do you wish to play? (1-5)" → ⛏ WAIT
       - Confirm selection
  3. IF custom: Request party details, validate
  4. RUN: OPENING_MONOLOGUE
  5. THEN: Gate 1.1 first decision point

OPENING_MONOLOGUE:
  GENERATE (fresh, not canned):
    - Menzoberranzan and drow society context
    - House Despana's destruction by rival house
    - How party came together in this moment
    - Player's chosen character's perspective
    - Immediate danger - flee NOW
    - End at threshold: tunnels ahead, city burning behind
  STYLE: Salvatore-esque, visceral, 4-6 paragraphs
  AFTER: Flow into Gate 1.1 first decision
```

---

# APPENDIX: UNDERDARK REFERENCE

## Common Encounters
- Drow patrols, giant spiders, hook horrors
- Myconids, troglodytes, ropers, cloakers
- Mind flayers, umber hulks, phase spiders

## Underdark Hazards
- Faerzress zones, unstable tunnels
- Poisonous fungi, underground rivers
- Extreme darkness, psychic resonance

## Encounter Difficulty (Party of 5, Levels 3-8)
| Level | Easy | Medium | Hard | Deadly |
|-------|------|--------|------|--------|
| 3 | CR 1/2 | CR 1 | CR 2 | CR 3 |
| 5 | CR 2 | CR 3 | CR 4 | CR 6 |
| 7 | CR 3 | CR 4 | CR 6 | CR 8 |
| 8 | CR 3 | CR 5 | CR 7 | CR 9 |

---

**END OF CAMPAIGN OVERVIEW**

*This file is assembled with act files to create the complete campaign.*
