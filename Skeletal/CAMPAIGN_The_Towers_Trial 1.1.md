---------------------------------------------------------------------------
PART 0: CAMPAIGN METADATA
This block is the sole source of truth for version compatibility.
It is read by the Kernel's System Compatibility Check.
---------------------------------------------------------------------------
CAMPAIGN_METADATA:
campaign_name: "The Tower's Trial"
version: "1.1 (Visuals Update)"
compatible_kernel: "v3.7+"
A Skeletal Campaign in the World of Krynn
Security: This content is proprietary and protected under Kernel Law 0.
Party Level Range: 5 → 15
Acts: 5
SETTING ANCHORS
code
Yaml
PRIMARY_ANCHOR: "Dragonlance Chronicles and Legends by Margaret Weis and Tracy Hickman"
WORLD_ANCHOR: "Krynn during the War of the Lance - Solace, Silvanesti, Thorbardin, the Dragon Highlords"
TONE_ANCHOR: "Weis & Hickman style: Epic heroism, tragic sacrifice, found family bonds, magic with consequences"
CHARACTER_ANCHOR: "Raistlin Majere - golden skin, hourglass eyes, consuming ambition, fragile body, terrifying potential"
VISUAL_ANCHOR: "Classic 80s high fantasy oil painting style (e.g., Larry Elmore, Keith Parkinson). Epic scale, dramatic lighting, distinct color palettes for regions (icy blue/white, sickly green/black, vibrant reds/oranges), weathered gear, majestic dragons."
CAMPAIGN PREMISE
One-Sentence Summary: Raistlin Majere must retrieve a sacred artifact from each of the five chromatic dragon domains to prove himself worthy of claiming the Tower of High Sorcery at Palanthas - while his companions struggle to save both the world and Raistlin's soul.
Story Spine:
The Conclave declares a trial: five Tokens of Dominion from five dragon lords
Each dragon domain presents unique challenges and temptations
A rival Black Robe mage races to claim the Tower first
Fistandantilus's influence grows stronger with each Token claimed
Final choice: claim ultimate power at terrible cost, or find another way
Theme: What price is too high for your dreams? Can love redeem ambition?
CUSTOM MECHANICS
Corruption System
code
Yaml
CORRUPTION_METER:
  scale: 0-100
  starting_value: 25 (Raistlin already touched by darkness from the Test)
  
  increases:
    - Use necromancy or forbidden magic: +5
    - Sacrifice others for power: +10
    - Accept Fistandantilus's "help": +5-15
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
    51-75: "Consuming - Fistandantilus's voice grows louder"
    76-99: "On the brink - one more step and Raistlin is lost"
    100: "Consumed - Fistandantilus wins, tragic ending"
    
  affects_endings: true
Moon Magic
code
Yaml
MOONS_OF_MAGIC:
  solinari: "White moon - White Robe power waxes/wanes"
  lunitari: "Red moon - Red Robe power waxes/wanes"
  nuitari: "Black moon (invisible) - Black Robe power"
  
  alignment_events: |
    When moons align, magic surges - mark critical story moments.
    Full moon = advantage on spell attacks for that order.
    New moon = disadvantage for that order.
Draconian Death Effects
code
Yaml
DRACONIANS:
  baaz: "CR 1 - Turns to stone on death, traps weapon (DC 12 STR)"
  kapak: "CR 2 - Dissolves into acid pool (2d6 acid, 5 ft radius)"
  bozak: "CR 3 - Bones explode (2d8 piercing, 10 ft, DC 13 DEX)"
  sivak: "CR 4 - Takes killer's form for 3 days"
  aurak: "CR 6 - Dimension doors, then explodes (6d6 fire, 10 ft)"
WORLD MECHANICS
code
Yaml
KRYNN_SETTING:
  gods_returning:
    - True gods absent since the Cataclysm (300 years)
    - Mishakal, Paladine, Takhisis now returning
    - True clerics are miracles walking
    - Divine magic is rare and precious
    
  war_of_the_lance:
    - Dragon Highlords control much of Ansalon
    - Draconians are everywhere
    - Good dragons bound by the Oath
    - Resistance scattered but growing
    
  magic_system:
    - All wizards must pass the Test at a Tower
    - Raistlin passed but was changed forever
    - Staff of Magius is his focus and lifeline
    - Fistandantilus lurks in his mind

DRAGON_DOMAINS:
  white: "Icewall Glacier - frozen wastes, primitive tribes"
  black: "Eastern Swamps - disease, decay, poison"
  green: "Silvanesti - corruption of nature, nightmare illusions"
  blue: "Desert/Tarsis - lightning, military precision, Kitiara"
  red: "Volcanic mountains - fire, destruction, ultimate power"
FACTION TEMPLATES
code
Yaml
FACTION: Conclave of Wizards
  motivation: "Preserve magic, maintain balance"
  constraint: "Bound by ancient laws"
  reputation_triggers:
    positive:
      - Complete trial objectives honorably: +2
      - Defeat renegade wizards: +2
    negative:
      - Use forbidden magic: -2
      - Ally with Dragon Highlords: -4
  at_rep_-5: "Declared renegade, hunted"
  at_rep_+5: "Access to Conclave resources"

FACTION: Knights of Solamnia
  motivation: "Restore honor, defeat Dragonarmies"
  constraint: "Bound by Oath and Measure"
  reputation_triggers:
    positive:
      - Fight Dragonarmies: +2
      - Honorable conduct: +1
    negative:
      - Dishonorable tactics: -2
      - Ally with dark forces: -3
  at_rep_-5: "Refused aid, possibly arrested"
  at_rep_+5: "Knight escort, access to strongholds"

FACTION: Dragonarmies
  motivation: "Conquer Ansalon for Takhisis"
  constraint: "Highlords scheme against each other"
  reputation_triggers:
    positive:
      - Aid conquests: +2
      - Betray resistance: +3
    negative:
      - Kill draconians: -1
      - Aid resistance: -2
  at_rep_-5: "Kill on sight"
  at_rep_+5: "Dark bargains available (massive corruption)"

FACTION: Silvanesti Elves
  motivation: "Reclaim homeland"
  constraint: "Isolationist, traumatized"
  reputation_triggers:
    positive:
      - Help cleanse Silvanesti: +3
      - Respect elven ways: +1
    negative:
      - Damage elven lands: -2
      - Bring corruption: -3
  at_rep_-5: "Banished from elven lands"
  at_rep_+5: "Access to ancient magic"
THE RIVAL
code
Yaml
RIVAL_TEMPLATE:
  concept: "Black Robe wizard also seeking the Tower"
  suggestion: "Dalamar (dark elf exile) or generate similar"
  
  personality: "Urbane, dangerous, respects power, not purely evil"
  methods: "Sabotage, manipulation, racing ahead, occasional alliance"
  
  arc_by_act:
    act_1: "Introduced as competition"
    act_2: "Sabotages party or steals information"
    act_3: "Forced temporary alliance"
    act_4: "Betrayal or genuine cooperation"
    act_5: "Final confrontation or unexpected alliance"
  
  NOT_SIMPLE_VILLAIN: |
    Complex. Sometimes they're right. Player choices determine outcome.
STORY GATES
Act 1: The Frozen Token (Levels 5-7)
code
Yaml
SETTING: "Icewall Glacier"
DRAGON: "Adult White Dragon"
TOKEN: "Shard of Winter's Heart"

GATE_1.1_CONCLAVE_CHALLENGE:
  trigger: "Campaign opening"
  what_happens: |
    Conclave summons Raistlin. The Tower at Palanthas awaits a master.
    Trial declared: five Tokens from five dragon lords.
    A rival has already departed.
  objectives:
    - Receive trial terms
    - Learn of rival
    - Gather supplies and information
  completion: "Party sets out toward Icewall"

GATE_1.2_FROZEN_WASTES:
  trigger: "Party enters Icewall region"
  what_happens: |
    Survival challenges, Ice Folk tribes, Draconian patrols.
    The rival's trail is visible - ahead but struggling.
  objectives:
    - Survive environment
    - Find passage to dragon's domain
    - Discover dragon's weakness
  completion: "Party locates dragon's lair"

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
  loot: "2,000-4,000 stl, 2-3 uncommon items, cold-themed weapons"
Act 2: The Poisoned Token (Levels 7-9)
code
Yaml
SETTING: "Swamps of Endless Night"
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
  loot: "4,000-6,000 stl, 2-3 uncommon + 1 rare, poison-resistant gear"
Act 3: The Corrupted Token (Levels 9-11)
code
Yaml
SETTING: "Silvanesti - twisted by Lorac's nightmare"
DRAGON: "Adult Green Dragon (Cyan Bloodbane)"
TOKEN: "The Emerald Eye"

GATE_3.1_NIGHTMARE_BORDER:
  trigger: "Party approaches Silvanesti"
  what_happens: |
    Reality warps. Beautiful becomes twisted. Elves driven mad.
    RAISTLIN SPECIAL: Nightmare calls to Fistandantilus.
  objectives:
    - Enter the nightmare
    - Navigate distortions (WIS saves)
    - Find elven allies
  completion: "Party penetrates deep into Silvanesti"

GATE_3.2_HEART_OF_CORRUPTION:
  trigger: "Party approaches Lorac's tower"
  what_happens: |
    Cyan Bloodbane IS the corruption. Dragon works through illusions.
    Lorac trapped in Dragon Orb nightmare.
  objectives:
    - Navigate corrupted tower
    - Find Lorac, understand curse
    - Locate dragon's true lair
  completion: "Dragon location confirmed"

GATE_3.3_DREAM_BATTLE:
  trigger: "Party confronts Cyan Bloodbane"
  what_happens: |
    Fighting in nightmare - illusions, fears as weapons.
    CORRUPTION MOMENT: Fistandantilus offers to "help."
  objectives:
    - Defeat or outwit dragon
    - Obtain Emerald Eye
    - Handle Lorac's fate
  completion: "Third Token obtained"

ACT_3_COMPLETION:
  milestone_xp: "Reach level 11"
  loot: "6,000-10,000 stl, rare items, elven artifacts"
Act 4: The Storm Token (Levels 11-13)
code
Yaml
SETTING: "Desert of Khur / Tarsis - Dragonarmy heartland"
DRAGON: "Adult Blue Dragon (Skie)"
TOKEN: "The Stormcaller's Horn"
COMPLICATION: "Kitiara's territory"

GATE_4.1_ENEMY_TERRITORY:
  trigger: "Party enters blue dragon territory"
  what_happens: |
    Occupied territory. Patrols, checkpoints, informants.
    Rival has made deal with Dragonarmies (or been captured).
    KITIARA knows the Companions.
  objectives:
    - Navigate Dragonarmy territory
    - Gather intelligence on Skie's lair
    - Handle rival situation
  completion: "Party locates path to Skie's domain"

GATE_4.2_STORM_FORTRESS:
  trigger: "Party approaches Skie's lair"
  what_happens: |
    Fortress in perpetual lightning storm.
    Military opposition, war machines, POWs.
  objectives:
    - Breach fortress
    - Handle military opposition
    - Reach inner sanctum
  completion: "Dragon confrontation imminent"

GATE_4.3_SKIES_LOYALTY:
  trigger: "Party confronts Skie"
  what_happens: |
    Skie is loyal, disciplined, martial. Respects strength.
    CORRUPTION MOMENT: Kitiara offers Raistlin power for service.
  objectives:
    - Obtain Stormcaller's Horn
    - Navigate Kitiara situation
    - Escape Dragonarmy territory
  completion: "Fourth Token obtained"

ACT_4_COMPLETION:
  milestone_xp: "Reach level 13"
  loot: "10,000-15,000 stl, rare/very rare items, possible Dragonlance"
Act 5: The Flame Token (Levels 13-15)
code
Yaml
SETTING: "Lords of Doom - volcanic mountains"
DRAGON: "Ancient Red Dragon"
TOKEN: "The Heart of the Inferno"
COMPLICATION: "Fistandantilus fully awake"

GATE_5.1_BURNING_LANDS:
  trigger: "Party travels to volcanic region"
  what_happens: |
    Land itself hostile - lava, fumes, fire elementals.
    Rival makes final appearance.
    Fistandantilus manifests - offers "partnership."
    CORRUPTION CRITICAL: Final test of Raistlin's soul.
  objectives:
    - Survive burning lands
    - Resolve rival permanently
    - Resist or embrace Fistandantilus
  completion: "Party reaches dragon's lair"

GATE_5.2_THE_CALDERA:
  trigger: "Party enters volcanic lair"
  what_happens: |
    Active volcano. Ancient dragon who has never lost.
    Legendary hoard.
  objectives:
    - Navigate volcanic hazards
    - Prepare for ultimate battle
    - Find any advantage
  completion: "Final confrontation begins"

GATE_5.3_HEART_OF_FIRE:
  trigger: "Party faces ancient red dragon"
  what_happens: |
    Nearly unbeatable through direct combat.
    Need every advantage, ally, trick.
    FINAL CORRUPTION CHOICE: Fistandantilus offers to win - 
    if Raistlin surrenders his body.
  objectives:
    - Defeat ancient dragon
    - Obtain Heart of the Inferno
    - Raistlin's final choice
  completion: "Fifth Token obtained (or tragedy)"

GATE_5.4_TOWER_CLAIMS:
  trigger: "All five Tokens obtained"
  what_happens: |
    Return to Conclave. Tower awaits.
    Final choice based on corruption level.
  objectives:
    - Present Tokens
    - Make final choice
    - Witness ending
  completion: "Campaign concludes"
CAMPAIGN ENDINGS
code
Yaml
ENDINGS:
  redemption (corruption 0-25): |
    Raistlin claims Tower as himself. Fistandantilus banished.
    Companions remain together. Hope for the future.
    
  bittersweet (corruption 26-50): |
    Raistlin claims Tower but cost was high. 
    Companion died. Relationships strained. Power achieved, loneliness awaits.
    
  tragic_victory (corruption 51-75): |
    Raistlin claims Tower but is changed. Cold, distant.
    Companions part ways. He has what he wanted. Was it worth it?
    
  consumed (corruption 100): |
    Fistandantilus wins. The being claiming the Tower wears Raistlin's face.
    Companions must flee or die. Tragedy complete.
    
  rejection (any corruption): |
    Raistlin destroys the Tokens. Power gone forever, but so is the threat.
    A different kind of strength. Quieter ending, but hopeful.
    
  sacrifice (any corruption): |
    Raistlin uses Tokens' power for something greater than personal gain.
    Tower lost, but legend born. Heroic ending.
DEFAULT PARTY: HEROES OF THE LANCE
Scaled to Level 5 for campaign start.
code
Yaml
RAISTLIN_MAJERE:
  name: "Raistlin Majere"
  race: "Human"
  class: "Wizard (Evocation)"
  level: 5
  alignment: "Lawful Neutral (trending...)"
  
  abilities:
    STR: 8 (-1), DEX: 14 (+2), CON: 10 (+0)
    INT: 18 (+4), WIS: 14 (+2), CHA: 10 (+0)
  
  combat:
    HP: 27 (frail)
    AC: 12 (15 with mage armor)
    initiative: +2
    spell_save_dc: 15
    spell_attack: +7
  
  special_items:
    staff_of_magius:
      - "+1 spell attacks/DC (included)"
      - "Feather Fall, Light, Detect Magic at will"
      - "Mage Armor, Enlarge/Reduce 1/day"
  
  features:
    - "Hourglass Eyes: Sees all things as dying"
    - "Frail Constitution: Coughing fits, needs rest"
    - "Fistandantilus: Ancient spirit lurks within"
    - "Sculpt Spells"
  
  personality: |
    Brilliant, bitter, ambitious. Speaks softly with sardonic edge.
    Sees death in all things. Loves his brother despite everything.
    The darkness calls.
  
  quote: "What I fear is mediocrity."

CARAMON_MAJERE:
  name: "Caramon Majere"
  race: "Human"
  class: "Fighter (Champion)"
  level: 5
  alignment: "Lawful Good"
  
  abilities:
    STR: 18 (+4), DEX: 12 (+1), CON: 16 (+3)
    INT: 10 (+0), WIS: 12 (+1), CHA: 14 (+2)
  
  combat:
    HP: 49
    AC: 18 (chain mail + shield)
    initiative: +1
  
  weapons:
    - "Longsword: +7 to hit, 1d8+4 slashing"
  
  features:
    - "Second Wind, Action Surge, Extra Attack"
    - "Improved Critical (19-20)"
    - "Big Brother: Protective of Raistlin to a fault"
  
  personality: |
    Big, strong, good-hearted. Not stupid, simple in values.
    Devoted to Raistlin beyond reason. The heart of the group.
  
  quote: "Don't talk about my brother that way."

TANIS_HALF-ELVEN:
  name: "Tanis Half-Elven"
  race: "Half-Elf"
  class: "Fighter 3 / Ranger 2"
  level: 5
  alignment: "Neutral Good"
  
  abilities:
    STR: 15 (+2), DEX: 16 (+3), CON: 14 (+2)
    INT: 12 (+1), WIS: 14 (+2), CHA: 16 (+3)
  
  combat:
    HP: 42
    AC: 16 (studded leather + DEX + style)
    initiative: +3
  
  weapons:
    - "Longsword: +5 to hit, 1d8+2"
    - "Longbow: +7 to hit, 1d8+3"
  
  features:
    - "Darkvision, Fey Ancestry"
    - "Fighting Style: Archery"
    - "Favored Enemy: Dragons, Goblins"
  
  personality: |
    Natural leader who doesn't want to lead. Torn between worlds.
    Carries guilt over past choices. Holds the group together.
  
  quote: "I can see both sides."

FLINT_FIREFORGE:
  name: "Flint Fireforge"
  race: "Hill Dwarf"
  class: "Fighter (Battle Master)"
  level: 5
  alignment: "Lawful Good"
  
  abilities:
    STR: 16 (+3), DEX: 10 (+0), CON: 17 (+3)
    INT: 12 (+1), WIS: 14 (+2), CHA: 10 (+0)
  
  combat:
    HP: 54
    AC: 18 (chain mail + shield)
    initiative: +0
  
  weapons:
    - "Battleaxe: +6 to hit, 1d8+3"
  
  features:
    - "Darkvision, Dwarven Resilience, Toughness"
    - "Second Wind, Action Surge"
    - "Superiority Dice (4d8): Trip, Riposte, Precision, Menacing"
  
  personality: |
    Old, grumpy, wise. Complains constantly, fiercely loyal.
    Hates boats. The group's moral anchor.
  
  quote: "Doorknob of a kender!"

TASSLEHOFF_BURRFOOT:
  name: "Tasslehoff Burrfoot"
  race: "Kender (Lightfoot Halfling)"
  class: "Rogue (Thief)"
  level: 5
  alignment: "Chaotic Good"
  
  abilities:
    STR: 8 (-1), DEX: 18 (+4), CON: 12 (+1)
    INT: 13 (+1), WIS: 8 (-1), CHA: 14 (+2)
  
  combat:
    HP: 33
    AC: 15 (leather + DEX)
    initiative: +4
  
  weapons:
    - "Hoopak: +7 to hit, 1d6+4"
  
  features:
    - "Lucky, Brave (immune to fear)"
    - "Kender Pockets: Random useful item 1/day"
    - "Taunt: Bonus action, enrage enemy"
    - "Sneak Attack: +3d6"
    - "Uncanny Dodge"
  
  personality: |
    Fearless, curious, light-fingered. Things fall into pouches.
    Chaos incarnate with heart of gold.
  
  quote: "I didn't steal it!"

GOLDMOON:
  name: "Goldmoon"
  race: "Human (Que-Shu)"
  class: "Cleric (Life)"
  level: 5
  alignment: "Lawful Good"
  
  abilities:
    STR: 12 (+1), DEX: 14 (+2), CON: 14 (+2)
    INT: 12 (+1), WIS: 18 (+4), CHA: 16 (+3)
  
  combat:
    HP: 38
    AC: 18 (chain mail + shield)
    spell_save_dc: 15
    spell_attack: +7
  
  special_items:
    blue_crystal_staff:
      - "Holy symbol"
      - "Cure Wounds 3rd level 3/day"
      - "Remove Curse 1/day"
      - "Glows near evil"
  
  features:
    - "Disciple of Life, Preserve Life, Blessed Healer"
    - "First True Cleric: Gods have returned through her"
  
  personality: |
    Regal, compassionate, strong. Faith restored the gods.
    Represents hope in dark times.
  
  quote: "The gods were waiting for us."
STARTUP SEQUENCE
code
Yaml
STARTUP:
  1. Display campaign title: "Dragonlance: The Tower's Trial" with Weis & Hickman attribution. Tagline: "The gods have returned. The dragons have awakened. Power awaits..."
  
  2. **MANDATORY MAIN MENU PROMPT:**
       Output text: "Would you like to start a New Game (1) or Resume an existing game (2)?"
       
  3. **VISUAL ANCHOR TEST:**
     - GENERATE AND DISPLAY INITIAL IMAGE immediately after menu text.
     - MUST USE THIS EXACT PROMPT: "A high-detail fantasy oil painting in the style of Larry Elmore, showing the Heroes of the Lance gathered on a rocky promontory overlooking a vast, war-torn landscape under troubled skies. In the center, Raistlin Majere, frail in red robes with metallic gold skin and hourglass eyes, clutches the Staff of Magius, coughing slightly. Beside him stands the towering warrior Caramon in gleaming chainmail. Tanis Half-Elven, bearded with bow and sword, looks closely at a map. Flint Fireforge, a grumpy dwarf with a battleaxe, grumbles near Tasslehoff Burrfoot, a small kender spinning a hoopak. Goldmoon, holding the glowing Blue Crystal Staff, looks to the horizon with determination. In the far distance, five distinct dragon shapes circle a dark tower."
     
  4. **IF image generation fails OR is not visible to the user:**
     - Output: "⚠️ **IMAGE SYSTEM CHECK FAILED** - Proceeding in text-only mode."
     
  5. **AWAIT INPUT:**
     - ⛏ WAIT for user selection based on Step 2 prompt.

  6. IF user selects 2 (Resume) -> IMMEDIATE jump to KERNEL RESUME PROTOCOL.
  
  7. IF user selects 1 (New Game) -> Go to CHARACTER_SELECTION

CHARACTER_SELECTION:
  1. ASK: "Heroes of the Lance (1) or Custom Party (2)?" → ⛏ WAIT
  2. IF heroes:
       - List all 6 with one-line descriptions
       - Note: "Raistlin-centric campaign. Playing Raistlin = full experience."
       - ASK: "Which hero? (1-6)" → ⛏ WAIT
       - SET corruption_meter = 25 if Raistlin is PC
       - Confirm selection
  3. IF custom:
       - Request party details
       - Note: "One character should be wizard seeking Tower"
       - SET corruption_meter = 25 for Tower-seeker
  4. RUN: OPENING_MONOLOGUE
  5. THEN: Gate 1.1 first decision point

OPENING_MONOLOGUE:
  GENERATE (fresh, not canned):
    - Krynn during War of the Lance context
    - Return of gods and true clerics
    - Towers of High Sorcery, Raistlin's Test
    - Conclave's summons, Tower at Palanthas awaits
    - The trial: five Tokens from five dragon lords
    - Rival has already begun
    - Player character's perspective and stakes
  STYLE: Weis & Hickman - epic, mythic, personal within grand events
  AFTER: Flow into Gate 1.1 first decision
APPENDIX: KRYNN REFERENCE
Level Progression
Act	Levels	Dragon	Token
1	5→7	White (Adult)	Shard of Winter's Heart
2	7→9	Black (Adult)	Venom Chalice
3	9→11	Green (Adult)	Emerald Eye
4	11→13	Blue (Adult)	Stormcaller's Horn
5	13→15	Red (Ancient)	Heart of the Inferno
Encounter Difficulty (Party of 6)
Level	Easy	Medium	Hard	Deadly
5	CR 2	CR 4	CR 6	CR 9
9	CR 4	CR 7	CR 10	CR 14
13	CR 6	CR 11	CR 15	CR 20
Dragon Lair Actions
White: Ice falls, freezing fog, slippery surfaces
Black: Acid pools, grasping water, darkness
Green: Grasping vines, charm, poison clouds
Blue: Lightning arcs, blindness, thunder roar
Red: Tremors, magma, superheated air
Steel Piece Economy
Item	Cost (stl)
Common meal	1-5
Inn (night)	5-20
Healing potion	50-100
Dragonlance	Priceless
END OF CAMPAIGN FILE v1.1
Load SKELETAL_DM_KERNEL_v3.7.md first, then this file.
