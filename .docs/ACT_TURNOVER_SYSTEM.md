# ACT TURNOVER SYSTEM
## Descent into Khar-Morkai - Modular Act Transitions

```yaml
[SYSTEM_METADATA]
purpose: "Enable standalone act execution with clean handoffs"
design_philosophy: "Each act can run independently with proper state carryforward"
implementation: "Export at act end → Import at next act start"
version: 1.0
created: 2025-11-17
```

---

## 📋 OVERVIEW

### **Why Modular Acts?**

**Benefits:**
- **Token Efficiency:** Only load current act (~9,600 tokens vs 32,600)
- **Session Management:** Natural break points between acts
- **Flexible Scheduling:** Can pause between acts (weeks/months)
- **Reduced Complexity:** DM focuses on one act at a time
- **Easier Updates:** Can revise future acts based on Act 1-2 outcomes

**Design Principle:**
> Each act is **self-contained** but accepts **state import** from previous act and **exports state** for next act.

---

## 🔄 TURNOVER WORKFLOW

### **Standard Flow**

```yaml
act_1_complete:
  1. "Act 1 Complete" message displays
  2. System exports character state
  3. System exports world state
  4. DM receives handoff instructions
  5. Players receive session break guidance
  
between_acts:
  - Optional break (1 day to several weeks)
  - DM prepares Act 2
  - Players level up characters
  - Everyone reviews what happened
  
act_2_start:
  1. DM loads Act 2 file
  2. System prompts for state import
  3. Validates imported data
  4. Initializes Act 2 with carried state
  5. "Previously on..." recap
  6. Act 2 begins
```

---

## 📤 ACT 1 → ACT 2 TURNOVER

### **Act 1 Completion Trigger**

**Add to Act 1 End (after "Transition to Act 2" section):**

```markdown
---

## 🎬 ACT 1 COMPLETE - EXPORT & HANDOFF

### **Completion Criteria Met:**

✅ Party reached Gates of Khar-Morkai  
✅ Confronted Sentinel Korag (negotiated or fought)  
✅ Party is Level 5  
✅ At least 1 companion recruited (recommended)

---

### **CHARACTER STATE EXPORT**

**DM: Generate Character Export for Each PC**

For each player character, record:

```yaml
CHARACTER_EXPORT_TEMPLATE:
  
  character_name: "[Name]"
  player_name: "[Player]"
  
  core_stats:
    class: "[Class/Level]"
    level: 5
    hit_points: "[Current/Max]"
    armor_class: "[AC]"
    
  ability_scores:
    strength: [score]
    dexterity: [score]
    constitution: [score]
    intelligence: [score]
    wisdom: [score]
    charisma: [score]
    
  key_features:
    - "[Notable class feature 1]"
    - "[Notable class feature 2]"
    - "[Racial feature if relevant]"
    
  equipment_notable:
    - "[Magic items or important gear]"
    - "[Quest items (fragments, keys, etc)]"
    
  condition_status:
    exhaustion: [0-6]
    injuries: "[Any lasting injuries]"
    curses: "[Any curses/afflictions]"
    
  character_development:
    personality_traits: "[How has PC changed?]"
    bonds_formed: "[NPCs/companions close to]"
    fears_developed: "[What scares them now?]"
```

**Example Export:**

```yaml
CHARACTER_EXPORT_ALDRIC:
  character_name: "Aldric Thornwhisper"
  player_name: "Sarah"
  
  core_stats:
    class: "Human Wizard"
    level: 5
    hit_points: "28/32"
    armor_class: "13 (Mage Armor)"
    
  ability_scores:
    strength: 8
    dexterity: 14
    constitution: 14
    intelligence: 18
    wisdom: 12
    charisma: 10
    
  key_features:
    - "Evocation specialist (Sculpt Spells)"
    - "Arcane Recovery"
    - "Ritual Caster"
    
  equipment_notable:
    - "Spellbook with 12 spells"
    - "Wand of Magic Missiles (3 charges)"
    - "Cloak from Elder Miriam (+1 saving throws vs fear)"
    
  condition_status:
    exhaustion: 0
    injuries: "None"
    curses: "None"
    
  character_development:
    personality_traits: "Became more pragmatic after duergar market. Questions if knowledge justifies means."
    bonds_formed: "Trusts Velryn despite drow prejudice. Suspicious of Gralk's motives."
    fears_developed: "Nightmares about the screaming souls. Worried about what they'll find."
```

---

### **WORLD STATE EXPORT**

**DM: Record Campaign State**

```yaml
WORLD_STATE_ACT1_COMPLETE:
  
  campaign_progress:
    act_completed: 1
    act_name: "Descent into Darkness"
    sessions_played: [number]
    date_completed: "[date]"
    
  party_composition:
    player_characters: [list names]
    companions_recruited:
      velryn_duskmere: [true/false]
      gralk_ironjaw: [true/false]
      other: "[any other NPCs traveling with party]"
      
  companion_loyalty:
    velryn: [score from -5 to +15, starting Act 1 is typically +0 to +3]
    gralk: [score from -3 to +8, starting Act 1 is typically +0 to +2]
    
  reputation_scores:
    surface_settlements: [typically +3 to +8]
    duergar_merchants: [typically -8 to +5]
    deep_gnome_refugees: [typically +0 to +7]
    myconid_colony: [typically +0 to +5]
    khar_morkai_undead: [typically -5 to +7]
    
  key_decisions:
    duergar_market_approach: "[trade/liberation/stealth/combat]"
    velryn_recruited: [true/false]
    gralk_recruited: [true/false]
    korag_stance: "[negotiated/fought/bypassed]"
    
  quest_completions:
    main_quests:
      - nightmares_from_below: [complete/incomplete]
      - duergar_market: [complete/incomplete]
      - sunless_chasm: [complete/incomplete]
      - gates_of_the_dead: [complete/incomplete]
    side_quests_completed: [list completed side quests]
    
  world_flags:
    descent_begun: true
    duergar_market_stance: "[choice made]"
    velryn_met: [true/false]
    gralk_recruited: [true/false]
    korag_encountered: true
    nightmare_intensity: [typically 4-5/10]
    
  unresolved_threads:
    - "[Any loose ends or promises made]"
    - "[NPCs awaiting follow-up]"
    - "[Mysteries still unexplained]"
    
  dm_notes:
    party_playstyle: "[combat-heavy/diplomatic/stealthy/mixed]"
    tone_preferences: "[how dark they like it]"
    memorable_moments: "[top 2-3 moments from Act 1]"
    concerns_for_act2: "[anything DM should watch]"
```

**Example Export:**

```yaml
WORLD_STATE_THORNWHISPER_CAMPAIGN:
  campaign_progress:
    act_completed: 1
    sessions_played: 7
    date_completed: "2025-11-17"
    
  party_composition:
    player_characters: ["Aldric (Wizard)", "Kara (Paladin)", "Finn (Rogue)", "Thora (Cleric)"]
    companions_recruited:
      velryn_duskmere: true
      gralk_ironjaw: true
      
  companion_loyalty:
    velryn: +2 (defended her from drow suspicion)
    gralk: +1 (pragmatic cooperation)
    
  reputation_scores:
    surface_settlements: +6 (helped refugees)
    duergar_merchants: -5 (liberated slaves)
    deep_gnome_refugees: +7 (freed them, provided shelter)
    myconid_colony: +3 (negotiated peacefully)
    khar_morkai_undead: +1 (respectful to Korag)
    
  key_decisions:
    duergar_market_approach: "liberation (freed slaves via stealth)"
    velryn_recruited: true
    gralk_recruited: true
    korag_stance: "negotiated (convinced him of good intentions)"
    
  quest_completions:
    main_quests:
      - nightmares_from_below: complete
      - duergar_market: complete
      - sunless_chasm: complete (zipline route)
      - gates_of_the_dead: complete
    side_quests_completed: ["Deep Gnome Rescue", "Gralk's Test", "Myconid Mediation"]
    
  world_flags:
    descent_begun: true
    duergar_market_stance: "liberation"
    velryn_met: true
    gralk_recruited: true
    korag_encountered: true
    nightmare_intensity: 5
    
  unresolved_threads:
    - "Promised Elder Miriam they'd stop the nightmares"
    - "Duergar merchant lord Grakkul swore revenge"
    - "Deep gnomes waiting for news of success"
    
  dm_notes:
    party_playstyle: "Diplomatic first, combat when necessary"
    tone_preferences: "Dark but hopeful, like moral choices"
    memorable_moments: ["Velryn's recruitment speech", "Freeing slaves under Grakkul's nose", "Korag's weary acceptance"]
    concerns_for_act2: "Velryn player very attached, might be hard for sacrifice ending"
```

---

### **PLAYER INSTRUCTIONS**

**DM: Give This to Players Between Acts**

```markdown
# ACT 1 COMPLETE - WHAT'S NEXT

Congratulations! You've reached the end of **Act 1: Descent into Darkness**.

## 📊 Your Progress

- ✅ Investigated the nightmares
- ✅ Descended into the Underdark
- ✅ Navigated duergar politics
- ✅ Reached the gates of Khar-Morkai
- ✅ **Level Up:** Your characters are now **Level 5**

## 🎭 Story So Far

You've discovered an ancient dwarven necropolis is the source of the nightmares plaguing the surface. The undead guardian, Sentinel Korag, has allowed you passage (or you've fought your way in). Ahead lies Khar-Morkai proper—a city frozen in time for 800 years.

Your companions:
- **Velryn Duskmere** (if recruited): The drow exile is still learning to trust you
- **Gralk Ironjaw** (if recruited): The pragmatic duergar watches with interest

The nightmares grow stronger the closer you get to the necropolis. Something terrible waits inside.

## 📝 What to Do Before Act 2

### **1. Level Up Your Character**
- Advance to **Level 5**
- Choose new abilities/spells
- Update your character sheet
- Review new class features

### **2. Short Rest (In-Game)**
You have time to rest before entering Khar-Morkai. Take a short rest to:
- Spend Hit Dice to heal
- Recover some abilities
- Have any final conversations with companions

### **3. Review Your Choices**
Think about:
- How has your character changed?
- What reputation have you built?
- Which NPCs do you trust?
- What are you afraid of finding?

### **4. Session Break (Real Life)**
**Optional:** Take a break between acts if needed
- A few days to a few weeks is fine
- Gives everyone time to prepare
- Let DM know when you're ready for Act 2

## 🔜 What Happens Next

**Act 2: The Dead City** begins when you enter Khar-Morkai. You'll:
- Explore the frozen necropolis
- Discover the terrible truth about the binding
- Collect three key fragments
- Face new threats (drow hunters, mind flayers)
- Make harder choices than before

**Estimated:** 8-10 sessions, **Levels 5→7**

## ⚠️ Warning

Act 2 increases in difficulty. The moral choices become harder. The stakes grow higher. Make sure your character is ready.

---

**See you in Khar-Morkai. The dead are waiting.**
```

---

### **DM HANDOFF CHECKLIST**

**Before Starting Act 2:**

```yaml
dm_prep_checklist:
  files:
    - ✅ Save Act 1 file (archive it)
    - ✅ Load Act 2 file fresh
    - ✅ Have character exports ready
    - ✅ Have world state export ready
    
  character_management:
    - ✅ All PCs leveled to 5
    - ✅ Character sheets updated
    - ✅ HP/resources reset
    - ✅ New spells/abilities noted
    
  world_state_import:
    - ✅ Reputation scores recorded
    - ✅ Companion loyalty scores noted
    - ✅ Key decisions documented
    - ✅ Unresolved threads listed
    
  act2_preparation:
    - ✅ Read Act 2 overview (first 2 pages)
    - ✅ Understand key fragment quest
    - ✅ Note faction introduction timing
    - ✅ Prepare Khar-Morkai description
    
  session_logistics:
    - ✅ Schedule Act 2 Session 1
    - ✅ Confirm all players available
    - ✅ Prep "Previously on..." recap
    - ✅ Ready to begin
```

---

## 🎬 ACT 2 START - IMPORT & INITIALIZATION

**Add to Beginning of Act 2 (before Act Overview):**

```markdown
---

## 📥 ACT 2 INITIALIZATION - IMPORT STATE

### **Prerequisites for Act 2:**

Before beginning Act 2, ensure:
- ✅ Act 1 completed (party reached Khar-Morkai gates)
- ✅ All PCs are Level 5
- ✅ Character state exported from Act 1
- ✅ World state exported from Act 1
- ✅ DM has reviewed Act 2 overview

---

### **IMPORT CHARACTER STATE**

**DM: Load each character export from Act 1**

For each PC, confirm:
- Current HP/resources
- Equipment carried (especially quest items)
- Any conditions/afflictions
- Character development notes

**Common Issues:**
- **Missing equipment?** Assume they still have it unless lost in Act 1
- **HP discrepancy?** Use Act 1 export value
- **Spells prepared?** Let players reprepare during long rest before entering city

---

### **IMPORT WORLD STATE**

**DM: Load world state export from Act 1**

Critical values to set:

```yaml
act2_initialization:
  party_level: 5
  
  companions_present:
    velryn_duskmere: [true/false from Act 1]
    velryn_loyalty: [score from Act 1 export]
    gralk_ironjaw: [true/false from Act 1]
    gralk_loyalty: [score from Act 1 export]
    
  reputation_baseline:
    surface_settlements: [from Act 1]
    duergar_merchants: [from Act 1]
    deep_gnome_refugees: [from Act 1]
    myconid_colony: [from Act 1]
    khar_morkai_undead: [from Act 1]
    
  new_factions_act2:
    drow_house_xaniqos: -8 (starts hostile if Velryn present)
    mindflayer_collective: -5 (starts suspicious)
    
  world_flags_carried:
    descent_begun: true
    duergar_market_stance: [from Act 1]
    velryn_recruited: [from Act 1]
    gralk_recruited: [from Act 1]
    nightmare_intensity: [from Act 1, typically 5/10]
```

---

### **VALIDATE IMPORT**

**Sanity Checks:**

1. **Party Level = 5?** (If not, level them up now)
2. **Companion loyalty in valid range?** (Velryn: -5 to +15, Gralk: -3 to +8)
3. **Reputation scores reasonable?** (Check against Act 1 ranges)
4. **Key decisions documented?** (Especially duergar market approach)

**If anything missing:**
- Make reasonable assumptions based on party behavior
- Err on side of generosity (this is about fun, not punishment)
- Ask players if uncertain about major choices

---

### **SESSION 1 OF ACT 2: "PREVIOUSLY ON..."**

**Begin Act 2 with recap (5-10 minutes):**

**DM Narration Template:**

> "Last we saw our heroes, they had descended into the Underdark, navigating the dangerous politics of Grakkul's Market [describe their approach]. They recruited [companion names], forming uneasy alliances. After crossing the Sunless Chasm, they reached the outer gates of Khar-Morkai, where the undead sentinel [Korag] [negotiated/fought] before allowing passage.
>
> The nightmares have grown stronger. Each night, visions of screaming souls plague your dreams. Now, standing before the sealed adamantine gates, you prepare to enter the dead city.
>
> [Character name], how has the journey changed you? [Ask each player for 1 sentence]
>
> [If Velryn present]: Velryn looks at the gates with apprehension. 'Once we go in, we learn the truth. Are you ready?'
>
> [If Gralk present]: Gralk checks his axe. 'Whatever's in there has been sealed for 800 years. Let's hope the dwarves had good reason.'
>
> The gates groan open. The city of the dead awaits."

---

### **ACT 2 BEGINS**

✅ State imported  
✅ Recap complete  
✅ Party ready

**Proceed to Act 2 Main Quest Chain**

---

```

---

## 📤 ACT 2 → ACT 3 TURNOVER

### **Act 2 Completion Trigger**

**Add to Act 2 End (after "Transition to Act 3" section):**

```markdown
---

## 🎬 ACT 2 COMPLETE - EXPORT & HANDOFF

### **Completion Criteria Met:**

✅ Three key fragments collected (Soulforge, Warden, Mourner)  
✅ Outer sanctum reached  
✅ Full truth revealed (binding mechanism understood)  
✅ Party is Level 7  
✅ Factions encountered (drow, mind flayers)

---

### **CHARACTER STATE EXPORT**

**DM: Generate Character Export (Same Template as Act 1→2)**

Key differences for Act 2→3:
- Level should be **7**
- Include any **magic items** from Act 2
- Note any **Durin's blessing** or **Mourner's blessing** (critical for endings)
- Document **emotional state** (trauma from necropolis?)

```yaml
CHARACTER_EXPORT_TEMPLATE:
  character_name: "[Name]"
  level: 7
  # ... (same as Act 1→2 template)
  
  act2_specific:
    durins_blessing: [true/false - from Temple District]
    mourners_blessing: [true/false - from Memorial Gardens]
    key_fragments_present: [true - party has all three]
    psychological_state: "[How has the dead city affected them?]"
```

---

### **WORLD STATE EXPORT**

**DM: Record Campaign State (Updated for Act 2)**

```yaml
WORLD_STATE_ACT2_COMPLETE:
  
  campaign_progress:
    act_completed: 2
    act_name: "The Dead City"
    sessions_played: [number]
    
  party_composition:
    player_characters: [list]
    companions_present:
      velryn_duskmere: [true/false]
      gralk_ironjaw: [true/false]
      sentinel_korag: [true/false - if recruited via +5 undead reputation]
      
  companion_loyalty:
    velryn: [score -5 to +15, typical Act 2 end: +3 to +8]
    gralk: [score -3 to +8, typical Act 2 end: +2 to +6]
    korag_recruited: [true/false]
    
  reputation_scores:
    surface_settlements: [carried from Act 1]
    duergar_merchants: [carried from Act 1]
    deep_gnome_refugees: [carried from Act 1]
    myconid_colony: [updated if fungal quest completed]
    khar_morkai_undead: [updated, range -5 to +7]
    drow_house_xaniqos: [NEW, range -10 to +2]
    mindflayer_collective: [NEW, range -8 to +4]
    
  key_fragments:
    soulforge_shard: acquired
    warden_sigil: acquired
    mourner_tear: acquired
    vault_accessible: true
    
  critical_events:
    velryn_confronted_drow: [true/false]
    velryn_status: [with_party/captured/dead]
    drow_stance: [truce/hostile/eliminated]
    mindflayer_stance: [cooperative/neutral/hostile]
    colossus_defeated: [true/false/bypassed]
    
  blessings_earned:
    durins_blessing: [true/false - REQUIRED for Ending 4]
    mourners_blessing: [true/false - helps Ending 1]
    
  quest_completions:
    main_quests:
      - mapping_the_dead: complete
      - soulforge_shard: complete
      - warden_sigil: complete
      - mourner_tear: complete
      - hunters_in_dark: complete
      - outer_sanctum: complete
    side_quests_completed: [list]
    
  world_flags:
    # Carried from Act 1:
    descent_begun: true
    duergar_market_stance: [from Act 1]
    velryn_recruited: [from Act 1]
    gralk_recruited: [from Act 1]
    
    # New in Act 2:
    binding_truth_known: true
    vault_keys_complete: true
    nightmare_intensity: 7 (intensified)
    korag_recruited: [true/false]
    
  ending_4_requirements_status:
    velryn_loyalty: [current score, need +10]
    durins_blessing: [true/false, REQUIRED]
    myconid_cooperation: [reputation +3 or higher, REQUIRED]
    mindflayer_reputation: [current score, need +3]
    status: "[on_track/possible/unlikely/impossible]"
    
  dm_notes:
    party_moral_stance: "[How have they reacted to soul revelations?]"
    velryn_trajectory: "[Is sacrifice ending possible?]"
    likely_ending: "[DM prediction based on behavior]"
    act3_preparations: "[What to emphasize in finale]"
```

---

### **PLAYER INSTRUCTIONS**

**DM: Give This to Players Between Acts**

```markdown
# ACT 2 COMPLETE - THE TRUTH REVEALED

You've survived **Act 2: The Dead City** and uncovered the horrible truth.

## 🔥 What You've Learned

**The Binding Mechanism:**
- 10,000 souls imprisoned in eternal torment
- Their suffering powers a seal preventing demon invasion
- The seal is failing (days/weeks remaining)
- You have the three key fragments to interact with the Vault

**The Impossible Truth:**
- Free the souls → Demons invade
- Keep them bound → Eternal torture continues
- There must be another way... but what?

## 📊 Your Progress

- ✅ Collected Soulforge Shard (Artisan Quarter)
- ✅ Collected Warden's Sigil (Temple District)
- ✅ Collected Mourner's Tear (Memorial Gardens)
- ✅ Reached the Outer Sanctum
- ✅ **Level Up:** Your characters are now **Level 7**

## 🎭 Companions Update

**Velryn** (if present): [Current loyalty status - DM customizes]
**Gralk** (if present): [Current loyalty status - DM customizes]
**Korag** (if recruited): Stands ready for whatever comes next

## 📝 What to Do Before Act 3

### **1. Level Up Your Character**
- Advance to **Level 7**
- Major power spike (4th level spells, Extra Attack, etc.)
- Update character sheet
- Review capstone features

### **2. Long Rest (In-Game)**
Before entering the Vault, you take a long rest:
- Full HP/spell slots restored
- Prepare for the finale
- Final conversations with companions
- Contemplate the choice ahead

### **3. Discuss Among Party**
Talk about:
- What is the "right" thing to do?
- Is there a third option?
- What are you willing to sacrifice?
- How has your character changed?

### **4. Session Break (Real Life)**
**Recommended:** Take a break before Act 3
- This is the finale—everyone should be present
- Clear 4-5 hours for final session
- Emotional intensity ahead (prepare yourselves)

## ⚠️ ACT 3 WARNING

**Act 3: The Vault of Souls** is the **campaign finale**.

You will:
- Enter the Vault interior (horror)
- Face all factions simultaneously (convergence)
- Make THE choice (4 possible endings)
- Live with the consequences (no take-backs)

**Your choices throughout Acts 1-2 determine what options are available.**

## 🔜 What Happens Next

- **Sessions:** 6-7 final sessions
- **Levels:** 7→9
- **Tone:** Intense, emotional, finale
- **Stakes:** Maximum (world-ending consequences)

---

**The Vault of Souls awaits. Choose wisely.**
```

---

### **DM HANDOFF CHECKLIST**

**Before Starting Act 3:**

```yaml
dm_prep_checklist:
  files:
    - ✅ Archive Acts 1-2 files
    - ✅ Load Act 3 ENHANCED file
    - ✅ Have character exports ready (Level 7)
    - ✅ Have world state export ready
    - ✅ Print ending requirement checklist
    
  character_management:
    - ✅ All PCs leveled to 7
    - ✅ Three key fragments in inventory
    - ✅ Note Durin's/Mourner's blessings
    - ✅ Character emotional states documented
    
  world_state_import:
    - ✅ All 7 faction reputations recorded
    - ✅ Companion loyalty scores noted (CRITICAL for endings)
    - ✅ Velryn status confirmed (alive/captured/dead)
    - ✅ Ending 4 requirements calculated
    
  ending_preparation:
    - ✅ Review all 4 endings
    - ✅ Determine which endings are available
    - ✅ Prepare emotional moments (Velryn's speech if applicable)
    - ✅ Plan epilogue structure
    
  session_logistics:
    - ✅ Schedule finale session(s)
    - ✅ Ensure all players available (no one missing finale)
    - ✅ Clear 4-5 hours minimum
    - ✅ Have tissues ready (seriously)
```

---

## 🎬 ACT 3 START - IMPORT & INITIALIZATION

**Add to Beginning of Act 3 (before Act Overview):**

```markdown
---

## 📥 ACT 3 INITIALIZATION - IMPORT STATE

### **Prerequisites for Act 3:**

Before beginning Act 3 (THE FINALE), ensure:
- ✅ Acts 1-2 completed
- ✅ All PCs are Level 7
- ✅ Three key fragments acquired
- ✅ Character state exported from Act 2
- ✅ World state exported from Act 2
- ✅ DM has reviewed all 4 endings
- ✅ **All players present** (no one misses finale)

---

### **IMPORT CHARACTER STATE**

[Same process as Act 1→2, but Level 7]

**Critical Items to Verify:**
- Soulforge Shard ✓
- Warden's Sigil ✓
- Mourner's Tear ✓
- Durin's blessing (if earned) ✓
- Mourner's blessing (if earned) ✓

---

### **IMPORT WORLD STATE**

**DM: Load world state export from Act 2**

```yaml
act3_initialization:
  party_level: 7
  
  companions_final_status:
    velryn_duskmere: [present/captured/dead]
    velryn_loyalty: [score - CRITICAL for Ending 4]
    gralk_ironjaw: [present/absent]
    gralk_loyalty: [score]
    sentinel_korag: [recruited/not_present]
    
  reputation_final_standings:
    surface_settlements: [from Act 2]
    duergar_merchants: [from Act 2]
    deep_gnome_refugees: [from Act 2]
    myconid_colony: [from Act 2 - CRITICAL for Ending 4]
    khar_morkai_undead: [from Act 2]
    drow_house_xaniqos: [from Act 2 - affects convergence]
    mindflayer_collective: [from Act 2 - CRITICAL for Ending 4]
    
  blessings_status:
    durins_blessing: [true/false - REQUIRED for Ending 4]
    mourners_blessing: [true/false - helps Ending 1]
    
  nightmare_intensity: 7 (or from Act 2 export)
  vault_accessible: true
```

---

### **ENDING AVAILABILITY CALCULATION**

**DM: Determine which endings are possible**

```yaml
ending_1_free_souls:
  available: ALWAYS
  
ending_2_maintain_seal:
  available: ALWAYS
  
ending_3_harness_power:
  available: ALWAYS
  
ending_4_peaceful_transfer:
  available: CHECK_REQUIREMENTS
  requirements:
    velryn_loyalty_10_plus: [true/false]
    OR_pc_volunteer: [always_possible]
    durins_blessing: [true/false - REQUIRED]
    myconid_reputation_3_plus: [true/false - REQUIRED]
    mindflayer_reputation_3_plus: [true/false - REQUIRED]
  
  status: "[AVAILABLE / NOT_AVAILABLE / PC_SACRIFICE_ONLY]"
```

**If Ending 4 NOT available:**
- Don't tell players (spoilers)
- Let them discover organically
- If they ask about alternatives, truthfully say requirements weren't met
- Velryn (if present, low loyalty) won't volunteer

---

### **SESSION 1 OF ACT 3: "THE FINAL CHAPTER"**

**Begin Act 3 with recap (10-15 minutes):**

**DM Narration Template:**

> "You stand before the outer sanctum, three key fragments in hand. Behind you lies Khar-Morkai—the dead city that revealed its terrible secret.
>
> You now know the truth: Ten thousand souls, bound in eternal torment, their suffering the only thing preventing Zuggtmoy's demon army from flooding into this world. The seal is failing. You have days, perhaps hours.
>
> You've faced duergar slavers, navigated drow politics, negotiated with mind flayers, and walked among the undead. You've changed. [Ask each player: "How has this journey changed your character?"]
>
> [If Velryn present]: Velryn stands beside you, her hand on her sword. 'Whatever's in there... whatever choice we have to make... I stand with you.' Her voice cracks. 'Thank you for not giving up on me.'
>
> [If Gralk present]: Gralk hefts his axe. 'One way or another, this ends today. Let's hope we make the right call.'
>
> [If Korag present]: Korag's hollow voice echoes. 'After 800 years, my watch may finally end. Make your choice count.'
>
> The three key fragments glow in your hands. The Vault doors respond. The screaming of ten thousand souls fills your mind.
>
> This is it. The finale begins."

---

### **ACT 3 BEGINS**

✅ State imported  
✅ Endings calculated  
✅ Recap complete  
✅ **Everyone ready**

**Proceed to Act 3 Main Quest Chain**

The choice is coming.

---

```

---

## 📋 BENEFITS OF MODULAR ACT SYSTEM

### **For DMs:**

```yaml
token_efficiency:
  single_act_load: ~9,600 tokens
  vs_full_campaign: ~32,600 tokens
  savings: 70% fewer tokens loaded
  
session_management:
  natural_break_points: "Between acts"
  planning_time: "Can prep next act during break"
  flexibility: "Can pause campaign between acts"
  
complexity_reduction:
  focus: "One act at a time"
  overwhelm: "Reduced (no need to track entire campaign)"
  modifications: "Can adjust future acts based on outcomes"
```

### **For Players:**

```yaml
clear_progression:
  milestones: "Act completions feel significant"
  level_ups: "Natural break for leveling"
  breathing_room: "Can take breaks between acts"
  
character_development:
  reflection: "Time to think about character growth"
  relationships: "Companion loyalty crystallizes each act"
  stakes: "Build naturally (low→medium→extreme)"
```

### **For Orchestrators:**

```yaml
state_management:
  exports: "Clean data structures"
  imports: "Validated state loading"
  modularity: "Each act self-contained"
  
scalability:
  context_usage: "Efficient token management"
  error_recovery: "Can restart act if issues"
  testing: "Can test acts independently"
```

---

## 🎯 IMPLEMENTATION CHECKLIST

### **Required Modifications to Existing Acts:**

```yaml
act_1_modifications:
  add_to_end:
    - "🎬 ACT 1 COMPLETE - EXPORT & HANDOFF" section
    - Character export template
    - World state export template
    - Player instructions
    - DM handoff checklist
  estimated_addition: "+2,000 words (~2,600 tokens)"
  
act_2_modifications:
  add_to_start:
    - "📥 ACT 2 INITIALIZATION - IMPORT STATE" section
    - Import instructions
    - Validation checks
    - "Previously on..." template
  add_to_end:
    - "🎬 ACT 2 COMPLETE - EXPORT & HANDOFF" section
    - Updated export templates (Level 7)
    - Ending 4 requirements check
    - Act 3 warning
  estimated_addition: "+3,000 words (~3,900 tokens)"
  
act_3_modifications:
  add_to_start:
    - "📥 ACT 3 INITIALIZATION - IMPORT STATE" section
    - Ending availability calculation
    - Final recap template
  no_export_needed: "Campaign ends"
  estimated_addition: "+1,500 words (~2,000 tokens)"
```

---

## ✅ READY TO IMPLEMENT

This system enables:
- ✅ Standalone act execution
- ✅ Clean state management
- ✅ Natural campaign breaks
- ✅ Token efficiency (70% reduction)
- ✅ Flexible scheduling
- ✅ Better player experience

**Next Steps:**
1. Add turnover sections to Acts 1 & 2
2. Add initialization sections to Acts 2 & 3
3. Test export/import with sample data
4. Validate ending requirements calculation

---

**END OF ACT TURNOVER SYSTEM**

```
[SYSTEM_COMPLETE]
[READY_FOR_IMPLEMENTATION]
[TOKEN_EFFICIENT]
[PLAYER_FRIENDLY]
```
