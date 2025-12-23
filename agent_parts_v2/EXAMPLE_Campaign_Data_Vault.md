# CAMPAIGN DATA VAULT: Act 2 - The Dead City

**DO NOT EDIT DURING SESSION** - This is a read-only reference file for the AI Orchestrator

**PURPOSE**: Contains all campaign-specific content (NPCs, locations, quests, loot) in indexed, retrievable format

---

[MASTER_INDEX]
overview:
  - _act2_overview
  - _campaign_intro

main_quests:
  - quest_mq1_mapping_the_dead
  - quest_mq2_three_fragments
  - quest_mq3_hunters_in_dark
  - quest_mq4_outer_sanctum

side_quests:
  - quest_sq1_architects_map
  - quest_sq2_volunteers_plea
  - quest_sq3_bone_market
  - quest_sq4_velryn_rescue
  - quest_sq5_collectors_obsession
  - quest_sq6_gralk_past
  - quest_sq7_mourner_comfort

locations:
  - loc_main_street
  - loc_artisan_quarter
  - loc_temple_district
  - loc_noble_estates
  - loc_vault_antechamber
  - loc_vault_outer_sanctum
  - loc_forge_ancient
  - loc_temple_ruined
  - loc_crypt_noble

npcs:
  - npc_zilvra_shadowveil
  - npc_xalaphex_aberrant_devourer
  - npc_durin_warden_ghost
  - npc_thalgrim_ghost
  - npc_mourner_spirit
  - npc_velryn_act2
  - npc_gralk_the_merchant

companions:
  - companion_velryn_act2

encounters:
  - enc_undead_patrol
  - enc_helmed_horrors
  - enc_drow_ambush
  - enc_aberrant_swarm
  - enc_stone_golem_final

items:
  - item_soulforge_shard
  - item_wardens_sigil
  - item_mourners_tear
  - item_vault_key_complete

---

[MODULE_START: _act2_overview]
### ACT 2: THE DEAD CITY - OVERVIEW

**Campaign**: Descent into Khar-Morkai
**Act Number**: 2 of 3
**Recommended Party Level**: 4-6

**Tone**: moral_corruption | choosing_lesser_evils | oppressive_isolation

**Core Themes**:
- Every choice has a cost - there are no "clean" solutions
- Desperation drives normally good people to evil acts
- The past's sins haunt the present literally (undead, ghosts)
- Trust is a luxury you cannot afford

**Story Summary**:
The party descends into Khar-Morkai, the Dead City beneath the mountains. Once a thriving dwarven metropolis, it was destroyed 500 years ago by a ritual gone wrong. Now it is filled with undead, wandering spirits, and worse things that have claimed the ruins. The party must navigate three main factions:
1. **The Undead** (mindless servants of the old curse)
2. **House Shadowveil** (drow seeking to capture their renegade, Velryn)
3. **The Aberrant** (mind flayer remnants, alien and incomprehensible)

**Victory Conditions**:
1. Obtain all three key fragments (Soulforge Shard, Warden's Sigil, Mourner's Tear)
2. Gain access to the Vault Outer Sanctum
3. Survive the moral corruption and exhaustion of the Dead City
4. (Optional) Rescue Velryn if captured by the drow

**Defeat Conditions**:
1. TPK (total party kill)
2. Velryn captured and not rescued within 3 in-game days (if you want his help in Act 3)
3. Party succumbs to madness (all members reach 5+ exhaustion levels)
4. Surrender key fragments to hostile faction

**Starting Location**: `loc_main_street`

**Starting Conditions**:
- Party enters via collapsed tunnel from Act 1
- Exhaustion level: 1 (from the descent)
- Provisions: Should have at least 3 days food/water
- Time: Day 1, Late Afternoon (limited exploration time before nightfall)

**Environmental Hazards**:
- **Madness**: DC 12 WIS save every 4 hours or gain 1 exhaustion (oppressive psychic atmosphere)
- **Darkness**: No natural light, torch/light sources required, burns 10 minutes per torch
- **Unsafe Rest**: Long rests in most areas have 50% chance of encounter interruption

**Key Flags for This Act**:
```yaml
act2_flags:
  velryn_with_party: true  # Is Velryn still a companion?
  zilvra_met: false  # Has party encountered Zilvra?
  zilvra_negotiated: false  # Did party make a deal with Zilvra?
  velryn_surrendered: false  # Did party give Velryn to drow?
  velryn_captured: false  # Did drow capture Velryn by force?

  xalaphex_met: false  # Has party encountered the Aberrant Devourer?
  xalaphex_negotiated: false  # Did party make a deal?
  xalaphex_hostile: false  # Is Xalaphex actively hunting party?

  fragments_obtained:
    soulforge_shard: false
    wardens_sigil: false
    mourners_tear: false

  vault_access_granted: false  # All three fragments + passed final test

  thalgrim_pacified: false  # Did party help the ghost find peace?
  durin_approved: false  # Did party pass Durin's moral test?
  mourner_comforted: false  # Did party show compassion?

  # Reputation tracker
  reputation_undead_souls: 0  # -10 to +10, affects final vault guardian
  reputation_drow: 0  # -10 to +10, affects Zilvra's mercy
  reputation_aberrant: 0  # -10 to +10, affects Xalaphex's interest
```

**Reputation System**:
Certain actions modify reputation with the three factions:
- **Undead Souls** (+rep: respectful, help ghosts find peace | -rep: desecration, mocking)
- **Drow** (+rep: honorable combat, keep promises | -rep: deception, insults to Lolth)
- **Aberrant** (+rep: curiosity, interesting behavior | -rep: boring/predictable, refusing communication)

**Act Completion Trigger**:
When party has all three fragments and passes the Vault Outer Sanctum test, they retrieve the MacGuffin (Shard of Khar-Morkai) and unlock the path to Act 3.
[MODULE_END: _act2_overview]

---

[MODULE_START: _campaign_intro]
### CAMPAIGN INTRO: Descent into Khar-Morkai

**First Session Opening Narration**:

The mountain pass behind you has collapsed. There is no going back now.

Before you stretches Khar-Morkai, the Dead City—a name whispered in tavern tales and ancient songs. Once, it was the jewel of the dwarven kingdoms: mile-high spires of stone, forges that sang with celestial fire, libraries carved into living crystal. That was five hundred years ago.

Now, it is a tomb.

The air is wrong here. It presses against your skin like cold water, and every breath tastes of copper and ash. The buildings—those still standing—lean at impossible angles, their windows dark and empty. No wind moves through the streets. No birds call. Even sound seems reluctant to travel far, as though the city itself is holding its breath.

Velryn, the drow ranger who has guided you this far, stands at the edge of the ruined plaza. His usually composed expression is tight with something you haven't seen before: fear.

"This place died screaming," he says quietly. "The stones remember. Try not to listen too closely."

Somewhere in the depths of this necropolis lies the Vault of Khar-Morkai, and within it, the only thing that can stop the Lich King Malachar from completing his ritual of eternal night. To reach it, you will need three keys—fragments of the vault's original seal, scattered across the city in the hands of the dead, the desperate, and the mad.

The sun is setting behind the mountains. In an hour, it will be full dark. Torches burn low in your packs.

**First Decision Point**:
You stand at the entrance to Main Street, the wide central avenue that once served as the city's heart. Ahead, you can make out several districts:
- The Artisan Quarter (forges and workshops, now cold)
- The Temple District (shrines to forgotten gods)
- The Noble Estates (grand manors, crypts beneath)

What do you do?
[MODULE_END: _campaign_intro]

---

[MODULE_START: loc_main_street]
### LOCATION: Main Street (The Dead City's Central Avenue)

**ID**: loc_main_street
**Region**: Central Khar-Morkai
**Type**: Urban ruins (wide avenue)
**Lighting**: Pitch black (no natural light)
**Atmosphere**: Oppressive silence, faint psychic hum

**Description**:
Main Street was once the grand processional avenue of Khar-Morkai, wide enough for twenty dwarves to march abreast. Massive statues of dwarven ancestors line both sides, their faces worn smooth by time and some corrosive force that has pitted the stone. The pavement is cracked, with dead roots pushing through—though nothing living grows here now.

Buildings loom on either side: collapsed shops, their signs unreadable; apartment blocks with gaping windows like empty eye sockets; a fountain in the center of the plaza, long dry, its basin filled with fine gray ash.

**Connections**:
- North: Artisan Quarter (`loc_artisan_quarter`)
- East: Temple District (`loc_temple_district`)
- West: Noble Estates (`loc_noble_estates`)
- South: Collapsed tunnel (exit to surface - BLOCKED)

**Hazards**:
- **Unstable Structures**: DC 12 Perception to notice building about to collapse; DC 14 DEX save to avoid 2d6 bludgeoning damage if collapse triggered
- **Madness Aura**: DC 12 WIS save every 4 hours spent here or gain 1 level of exhaustion

**Points of Interest**:
1. **Dry Fountain** - Can be searched (Investigation DC 14):
   - Success: Find skeletal remains of a dwarf clutching a journal (legible)
   - Journal contains clues about the Vault's location and hints about "three keys"

2. **Gralk's Market Stall** - A ghoul merchant has set up shop:
   - See `npc_gralk_the_merchant` for details
   - Sells basic supplies at 3x normal price (desperate seller's market)

3. **Collapsed Guardhouse** - Old city watch post:
   - Lootable: 2d4 torches, rusty longsword, tattered guard uniform

**Random Encounter Table** (roll 1d6 every hour spent here):
1-3: No encounter
4-5: `enc_undead_patrol` (2d4 skeletons, CR 1/4 each)
6: `npc_zilvra_shadowveil` (drow ambush) OR `enc_aberrant_swarm` (2d6 intellect devourers)

**First Visit Narrative**:
The silence is absolute. Your footsteps echo off stone, then die unnaturally fast, swallowed by the oppressive atmosphere. The statues seem to watch you pass, though their eyes are blank stone. Every instinct screams that you are being observed.

[IF Velryn is with party]:
Velryn's hand rests on his bow, unstrung but ready. "Stay together," he murmurs. "And keep your light sources conserved. We may be here longer than we'd like."

**DM Notes**:
- This is the "hub" location for Act 2 - party will return here frequently
- First visit should feel ominous but not immediately dangerous
- Gralk can provide rumors/hooks for side quests
- Journal in fountain is critical exposition - ensure party finds it
[MODULE_END: loc_main_street]

---

[MODULE_START: npc_zilvra_shadowveil]
### NPC: Zilvra Shadowveil (Drow Priestess of Lolth)

**ID**: npc_zilvra_shadowveil
**Role**: Antagonist (Act 2 primary), Moral Foil
**Race**: Drow (dark elf)
**Class**: Cleric 8 (Trickery Domain, deity: Lolth)
**Alignment**: Lawful Evil
**CR**: 8

**Appearance**:
Zilvra is tall and severe, with silver hair bound in intricate braids threaded with spider silk. Her skin is the deep purple-black of deep Underdark nobility. She wears ceremonial plate armor enameled in deep crimson and black, marked with the spider sigil of House Shadowveil. Her eyes are solid red, without pupils, and seem to see through deception.

**Personality Traits**:
- **Dutiful, Not Cruel**: Zilvra takes no pleasure in violence; she sees it as a necessary tool
- **Honorable (by drow standards)**: Keeps her word, respects strength, despises cowardice
- **Burdened by Responsibility**: Sees Velryn's betrayal as her personal failure as a mentor
- **Theological Devotee**: Truly believes Lolth's justice is perfect and necessary

**Goals**:
1. Capture Velryn alive and return him to House Shadowveil for judgment
2. Retrieve the House secrets Velryn stole (encoded journals about Underdark routes)
3. Restore her personal honor (his escape happened on her watch)
4. (Hidden) Prove to herself that mercy was the wrong choice when she spared Velryn's life years ago

**Relationship to Party**: Neutral → Hostile (only if party protects Velryn)

**Relationship to Velryn**:
Zilvra was Velryn's mentor for 40 years. She taught him ranger craft, theology, and the ways of House Shadowveil. When his crisis of faith came, she had the opportunity to kill him as a heretic but instead let him escape, believing he would return after seeing the surface world's cruelty. His continued defection is proof she was wrong—a fact she cannot accept.

**Key Dialogue Samples**:

*First Encounter (if party has Velryn):*
> "Velryn Duskmere. I taught you everything you know. And you repay me with betrayal and theft."
> [She does NOT immediately attack]
> "The Spider Queen demands your blood, but I am not without mercy. Surrender yourself and the stolen journals. Your... companions may leave."

*If party refuses:*
> "Then you choose to die beside a traitor. So be it. Know that I do this without hatred—only duty."

*If party negotiates:*
> "You speak of honor? Interesting. Most surface-dwellers do not understand the concept. Very well. Prove your worth."

*If party surrenders Velryn:*
> [Zilvra takes Velryn into custody, binds him]
> "You have chosen survival over sentiment. Wise. The Spider Queen teaches: loyalty to the weak is the luxury of the strong. You are not yet strong."
> [She will honor her word and let the party go unharmed]

*If Velryn is not with party:*
> "Where is he? Do not waste my time with lies. I can taste deception, and I am not patient."

**Combat Behavior**:
- **Tactics**: Zilvra uses *Hold Person* to incapacitate melee fighters, then focuses on spellcasters with *Spiritual Weapon* and *Guiding Bolt*
- **Does NOT fight to the death**: If reduced below 30 HP, she will use *Dimension Door* to escape and warn the party: "This is not over. We will meet again, and I will be ready."
- **Accompanied by**: 4 Drow Elite Warriors (CR 5 each) if first ambush; solo if later encounter

**Quest Hooks**:
- **Velryn's Choice**: If party helps Zilvra understand why Velryn left (Persuasion DC 18), she may grant them safe passage and even provide aid against the Aberrant threat
- **The Journals**: If party finds and returns the stolen House Shadowveil journals (hidden in `loc_velryn_cache`), Zilvra will owe them a favor

**Moral Weight**:
This NPC is designed to make the party question easy answers:
- Zilvra is "evil" by alignment but honorable and trustworthy
- Velryn is "good" but did betray his house and steal secrets
- Surrendering Velryn is the "pragmatic" choice but feels like a betrayal
- Fighting Zilvra is the "heroic" choice but may be unnecessary bloodshed

**Flags**:
```yaml
zilvra_flags:
  met: false  # Has party encountered her?
  velryn_surrendered: false  # Did party hand over Velryn?
  velryn_captured: false  # Did she capture him by force?
  negotiated_truce: false  # Did party convince her to stand down?
  journals_returned: false  # Did party return the stolen documents?
  zilvra_hostile: false  # Is she actively hunting the party?
  zilvra_defeated: false  # Did party beat her in combat?
  reputation: 0  # -10 to +10, affects future interactions
```

**DM Notes**:
- Zilvra is NOT a "boss fight" - she's a moral dilemma with stats
- Ideal outcome: Party negotiates, learns about drow culture, questions their assumptions
- Worst outcome: Party kills her reflexively because "drow = evil"
- Her arc can extend into Act 3 if handled well (potential ally against Lich King)

**Loot** (if defeated in combat):
- +1 Spider Silk Armor (AC 16, grants advantage on saves vs. poison)
- Holy Symbol of Lolth (worth 50 gp to collectors, cursed if used by non-drow)
- 3 vials of Drow Poison (DC 13 CON save or poisoned for 1 hour)
- Sending Stone (paired with her commander in the Underdark)

[MODULE_END: npc_zilvra_shadowveil]

---

[MODULE_START: quest_mq2_three_fragments]
### MAIN QUEST 2: The Three Key Fragments

**Quest ID**: quest_mq2_three_fragments
**Type**: Main Quest (Required for Act 2 completion)
**Level Range**: 4-6
**Estimated Duration**: 3-5 game sessions

**Objective**:
Obtain the three mystical fragments needed to unlock the Vault Outer Sanctum:
1. **Soulforge Shard** (from Artisan Quarter)
2. **Warden's Sigil** (from Temple District)
3. **Mourner's Tear** (from Noble Estates)

**Structure**: These can be obtained in any order (non-linear design)

**Hook**:
The journal found in the dry fountain on Main Street reveals:
> "The Vault cannot be opened by force or magic. Only the Three may grant entry: the Smith who built, the Priest who blessed, and the Noble who paid. Seek their echoes in the ruins."

---

## FRAGMENT 1: SOULFORGE SHARD

**Location**: Artisan Quarter → Ancient Forge (`loc_forge_ancient`)

**Guardian**: Ghost of Thalgrim Ironheart (Dwarf Battlesmith, CR 4 Ghost)

**Narrative**:
Thalgrim was the master smith who forged the Vault's original lock. When the cataclysm came, he stayed at his forge, trying to save his life's work. He died of exhaustion, hammer in hand, and his ghost has remained, endlessly trying to repair a cracked anvil that can never be fixed.

**Non-Combat Solution** (Recommended):
- **Persuasion DC 15**: "Your work saved thousands. The weapons you forged protected the innocent. You can rest now."
- **Effect**: Thalgrim stops his labor, looks at his hands, and fades with a smile. The Soulforge Shard appears on the anvil.
- **Reputation**: +2 with Undead Souls

**Combat Solution**:
- **Fight**: Thalgrim (CR 4 Ghost) + 2 Helmed Horrors (CR 4 each) activate if anvil is touched without permission
- **Difficulty**: Deadly encounter for level 4 party
- **Reputation**: -1 with Undead Souls (disturbing the dead)

**Skill Solution**:
- **Arcana DC 16**: Identify the runes on the anvil and complete the repair ritual Thalgrim was attempting
- **Effect**: The anvil is finally repaired, Thalgrim's curse breaks, he thanks the party and fades
- **Reputation**: +3 with Undead Souls (completing his work)

**Loot** (in addition to fragment):
- 1d4 x 100 gp worth of masterwork ingots
- Schematic for +1 Warhammer (requires smith to craft)

---

## FRAGMENT 2: WARDEN'S SIGIL

**Location**: Temple District → Ruined Temple of Moradin (`loc_temple_ruined`)

**Guardian**: Ghost of Durin Stoneshield (Dwarf Cleric, CR 5 Ghost - cannot be fought)

**Narrative**:
Durin was the high priest who blessed the Vault. He died trying to evacuate civilians during the cataclysm. His ghost has become a "trial of intent"—he can sense the party's true motivations and will only grant the Sigil to those he deems worthy.

**The Trial**:
Durin manifests and asks three questions. He can detect lies (treats this as *Zone of Truth*, DC 15 CHA save to resist, but resistance = automatic fail):

1. **"Why do you seek entry to the Vault?"**
   - Acceptable answers: "To stop a great evil," "To save innocent lives," "We were sent by [patron]"
   - Unacceptable: "For treasure," "For power," "We don't know"

2. **"What would you sacrifice to succeed?"**
   - Acceptable: Specific, personal sacrifice ("My life," "My chance at redemption," "My companion's freedom")
   - Unacceptable: Vague ("Whatever it takes"), selfish ("Nothing"), or cruel ("Others' lives")

3. **"If you could save one life or save many, but the one is someone you love, what do you choose?"**
   - Acceptable: Honest answer (even if selfish), shows moral struggle, or "I don't know, but I would try to save both"
   - Unacceptable: Dismissive, flippant, or sociopathic

**Pass**: Durin grants the Sigil, says "May Moradin guide your hammer," and fades
**Fail**: Durin says "You are not ready. Return when you understand the weight of duty" and vanishes for 24 hours

**Reputation**: +3 if passed, 0 if failed (no penalty for honesty)

**DM Notes**:
- This is PURE roleplay, no combat escape
- Designed to force character introspection
- If party fails, they can retry after 24 in-game hours
- DO NOT allow Persuasion/Deception checks to bypass—this is about honest answers

---

## FRAGMENT 3: MOURNER'S TEAR

**Location**: Noble Estates → Crypt of House Durithil (`loc_crypt_noble`)

**Guardian**: The Mourner (Banshee variant, CR 7 - can be avoided)

**Narrative**:
The Mourner is the ghost of Lady Ilyana Durithil, who lost her entire family in the cataclysm. She wails endlessly in grief, and her psychic screams can kill. The Mourner's Tear is a crystallized tear on her cheek—taking it by force will trigger combat.

**Non-Combat Solution** (Recommended):
- **Compassion Approach**: Sit with her, listen to her story, acknowledge her pain (no check, just roleplay)
- **Persuasion DC 14**: "Your family would not want you to suffer. You can join them now."
- **Performance/Religion DC 15**: Sing a funeral dirge or perform last rites
- **Effect**: The Mourner stops wailing, smiles through tears, and willingly gives the party the Tear before fading
- **Reputation**: +3 with Undead Souls

**Combat Solution**:
- **Trigger**: Touch the Tear without permission, attack the Mourner, or insult her grief
- **Enemy**: The Mourner (CR 7 Banshee with custom abilities)
  - **Wail of Grief**: 30ft cone, DC 15 WIS save or 4d8 psychic damage + frightened for 1 minute
  - **Incorporeal**: Resistant to non-magical damage
  - **Death Curse**: If reduced to 0 HP, she curses attacker (disadvantage on CHA checks for 7 days)
- **Difficulty**: DEADLY for level 5 party
- **Reputation**: -3 with Undead Souls

**Loot** (in crypt, not from Mourner):
- 2d6 x 100 gp in noble jewelry
- +1 Amulet of Proof Against Detection and Location

---

## QUEST COMPLETION

**Trigger**: Party has all three fragments

**Effect**:
When the party returns to `loc_vault_antechamber` with all three fragments, they auto-unlock the path to `loc_vault_outer_sanctum` and can proceed to **Main Quest 4: The Outer Sanctum** (final challenge of Act 2).

**XP Award**:
- Soulforge Shard obtained: 400 XP per character
- Warden's Sigil obtained: 500 XP per character (extra for non-combat solution)
- Mourner's Tear obtained: 600 XP per character
- All three obtained + vault unlocked: Bonus 300 XP per character

**Flags Updated**:
```yaml
fragments_obtained:
  soulforge_shard: true
  wardens_sigil: true
  mourners_tear: true

vault_unlocked: true

# Individual flags for how each was obtained
thalgrim_pacified: true/false
durin_passed_trial: true/false
mourner_comforted: true/false
```

[MODULE_END: quest_mq2_three_fragments]

---

## END OF EXAMPLE CAMPAIGN DATA VAULT

**Note**: This is a partial example. A complete Act 2 vault would contain all 45+ modules indexed in the [MASTER_INDEX].
