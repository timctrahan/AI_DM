# ACTS 1-3

## GATE_LEVELS

```yaml
ACT_1_THE_FALL: # L1-2
  1.1_HOUSE_FALL: 1
  1.2_PURSUIT_AND_SOLITUDE: 1
  1.3_THE_LEGENDARY_BLADES: 1
  1.4_ABERRANT_HAZARDS: 2
  1.5_THE_ESCAPED_PRISONERS: 2
  1.6_FIRST_OUTSIDER_CONTACT: 2

ACT_2_THE_HUNGRY_DARK: # L2-5
  2.1_ABERRATION_TERRITORY: 3
  2.2_THE_STARVING_DARK: 3
  2.3_DEMON_CULT: 4
  2.4_DUERGAR_ENCOUNTER: 4
  2.5_THE_DRIDERS_WARNING: 5
  2.6_DEEP_GNOME_REFUGE: 5

ACT_3_TWILIGHT_REALMS: # L5-8
  3.1_HUNTERS_FROM_HOME: 6
  3.2_DUERGAR_MARKET: 6
  3.3_MERCENARY_OFFER: 7
  3.4_SURFACE_RUMORS: 7
  3.5_SURFACE_APPROACH: 7
  3.6_TRIAL_OF_WORTH: 8
```

## PHASE_RESTRICTIONS

```yaml
ACT_1:
  phase: BETRAYAL_AND_EXILE
  restrictions: [High pursuit risk (50% encounter/rest), Wild magic zones, Solitude pressure (WIS DC 12)]

ACT_2:
  phase: SURVIVAL_AND_TEMPTATION
  restrictions: [Deeper Underdark, Resources scarce (forage DC 15), Moral compromises tempt]

ACT_3:
  phase: IDENTITY_CHOICE
  restrictions: [Faction politics intensify, Surface approaches with prejudice and opportunity]
```

## HUBS

```yaml
DEEP_GNOME_OUTPOST:
  unlocked_at: Gate 1.6
  available_if: "Peaceful contact"
  services: [Safe rest, Basic supplies, Information]
  mission_board: [standard, redemption]

DUERGAR_OUTPOST:
  unlocked_at: Gate 2.4
  available_if: "Not hostile"
  services: [Rest (paid), Black market, Mercenaries, Slave trade]
  mission_board: [standard, darkness]
  warning: "Companions react to services used"

SVIRFNEBLIN_REFUGE:
  unlocked_at: Gate 2.6
  available_if: "Peaceful relations"
  services: [Safe rest, Gem trade, Crafting, Information]
  mission_board: [standard, redemption]
  special: "Only safe hub in Act 2"

FRONTIER_SETTLEMENT:
  unlocked_at: Gate 3.6
  available_if: "Not hostile to surface"
  services: [Safe rest, Supplies, Smithing, Temple]
  mission_board: [standard, redemption]
  special: "First surface hub"

BARBARIAN_CAMP:
  unlocked_at: Gate 3.6
  available_if: "Earned respect through trial"
  services: [Rest, Training, Tribal wisdom, Beast companions]
  mission_board: [standard]
  special: "Combat-focused"
```

---

## ACT 1 GATES

### GATE_1.1_HOUSE_FALL

```yaml
trigger: "Campaign start - house raid erupts"

what_happens: |
  A rival house attacks. Venomous flames, spider swarms, collapsing stone.
  Your kin fall. The dark goddess's favor has shifted elsewhere.
  A mentor figure—blade master who quietly rejected drow cruelty—fights 
  nearby, urging escape while providing cover.
  Something awakens: questioning the senselessness of slaughter.

objectives:
  - Navigate besieged compound to hidden exit tunnel
  - Survive pursuit forces (2-3 rival scouts, environmental hazards)
  - Face moral beat (save someone, abandon valuables, confront betrayer)
  - Witness mentor's fate (varies by player choices)
```

### GATE_1.2_PURSUIT_AND_SOLITUDE

```yaml
trigger: "Fleeing into wild Underdark tunnels"

what_happens: |
  Boots echo behind—hunters track loose ends. Too many to fight.
  Tunnels twist into three-dimensional maze. Darkness absolute.
  Survival means stealth, speed, and knowing when to hide.

objectives:
  - Evade pursuit (4-6 hunters - OVERWHELMING, stealth/chase required)
  - Navigate hazards (unstable tunnel, web trap, predator territory)
  - Endure isolation wave (WIS save, flavored by prior choices)

encounter_note: "NOT a fair fight. Present hide/flee/distract. Combat only if cornered."
```

### GATE_1.3_THE_LEGENDARY_BLADES

```yaml
trigger: "Deeper tunnels, faint magical resonance"

what_happens: |
  Wild magic pulses, distorting reality. Discover a fallen hero's remains—
  surface dweller who ventured too deep. Two extraordinary scimitars 
  lie in the dust: one cold as winter, one faintly glowing. 
  The panther senses their power, seems to approve.

objectives:
  - Investigate the fallen hero (clues to surface world)
  - Claim the twin scimitars (difficulty scales with Shadow)
  - Survive wild magic surge (random magical effects)
  - Test new blades against minor threat (cloaker, phase spider, etc.)

equipment_unlock:
  FROST_SCIMITAR: "Bonus cold damage"
  GLOWING_SCIMITAR: "Glows blue when enemies near"
```

### GATE_1.4_ABERRANT_HAZARDS

```yaml
trigger: "Tunnels open into cavern maze"

what_happens: |
  Skittering grows louder. Aberrations empowered by wild magic—hook 
  horrors, umber hulks, or worse. Panther warns. Fight tests 
  hunter instincts and new bond.

objectives:
  - Resolve aberrant threat (type varies, scaled to party)
  - Navigate maze (Survival DC 15)
  - Strengthen companion bond through shared danger
```

### GATE_1.5_THE_ESCAPED_PRISONERS

```yaml
trigger: "Following faint voices or signs of conflict"

what_happens: |
  Encounter escaped prisoners—a gruff dwarven fighter and clever 
  halfling rogue, fleeing duergar slavers. Wary of drow. Your 
  actions and panther's presence can sway them.

objectives:
  - Make contact without immediate violence
  - Prove trustworthiness (share information, fight slavers, demonstrate mercy)
  - Resolve their escape situation

shadow_range: "Betray +8-10"

companion_potential: [DWARF_LEADER, HALFLING_ROGUE]
```

### GATE_1.6_FIRST_OUTSIDER_CONTACT

```yaml
trigger: "Following gem-light or sounds of mining"

what_happens: |
  Glowing fungi reveal deep gnome scouts—suspicious craftsmen 
  who fear drow above all else. Companions advise based on their 
  experience. First faction reputation established.

objectives:
  - Initiate contact peacefully (or not)
  - Exchange information or trade for safe passage
  - Establish faction standing
```

---

## ACT 2 GATES

### GATE_2.1_ABERRATION_TERRITORY

```yaml
trigger: "Deeper tunnels, signs of aberrant presence"

what_happens: |
  Territory of something worse. Hook horror nests, mind flayer 
  scouts, or beholder kin. The Underdark's true horrors.
  Companions react based on their experience—or lack thereof.

objectives:
  - Cross or clear the territory
  - Protect companions from psychic/aberrant threats
  - Decide: stealth, diplomacy (if possible), or violence
```

### GATE_2.2_THE_STARVING_DARK

```yaml
trigger: "Resources depleted, desperation mounting"

what_happens: |
  Days without proper food. Water tainted by wild magic. The panther 
  hunts but returns empty. Companions weaken. Solutions exist—
  none clean.

objectives:
  - Find sustainable food/water source
  - Decide method: hunt dangerous prey, trade with unsavory factions, raid weaker group, find natural source

shadow_note: "Stealing from peaceful myconids = major shadow increase"
```

### GATE_2.3_DEMON_CULT

```yaml
trigger: "Following dark whispers or fleeing something worse"

what_happens: |
  A corrupted shrine. Drow who've abandoned the dark goddess for something 
  worse—demon worship. They offer power, alliance, or simply attack.
  The air tastes of sulfur and madness.

objectives:
  - Survive initial contact
  - Learn what they know (Underdark politics, pursuit status)
  - Decide: destroy, infiltrate, bargain, or flee

shadow_range: "Join cult +15-20"
```

### GATE_2.4_DUERGAR_ENCOUNTER

```yaml
trigger: "Following trade routes or fleeing pursuit"

what_happens: |
  Gray dwarf outpost. Slavers, merchants, pragmatists who respect 
  only strength and profit. They have supplies, information, 
  and captives. What you do here defines reputation.

objectives:
  - Navigate duergar society
  - Acquire needed resources (trade, theft, or violence)
  - Face slavery directly (ignore, participate, or oppose)

shadow_range: "Liberate slaves -8-10 | Participate +10-15"
```

### GATE_2.5_THE_DRIDERS_WARNING

```yaml
trigger: "Ambushed or sought out by twisted former drow"

what_happens: |
  Driders—drow transformed by the dark goddess's displeasure—lurk here.
  One approaches, not to kill but to warn. It knows your former house,
  knows what hunts you. Information comes at a price.

objectives:
  - Survive initial ambush or approach
  - Learn what the great drow city knows and plans
  - Decide: mercy, alliance, or destruction
```

### GATE_2.6_DEEP_GNOME_REFUGE

```yaml
trigger: "Seeking allies or safer territory"

what_happens: |
  Hidden svirfneblin settlement. Deeply suspicious of drow—they've 
  suffered too much. Trust must be earned through action, not words.
  Companions who've joined can vouch, if they believe in you.

objectives:
  - Gain entry without violence
  - Prove trustworthiness (eliminate slaver patrol, trade fairly, share intel)
  - Establish faction standing

shadow_range: "Intimidate +8 | Raid +12"
```

---

## ACT 3 GATES

### GATE_3.1_HUNTERS_FROM_HOME

```yaml
trigger: "Signs of organized pursuit—not random patrols"

what_happens: |
  The great drow city hasn't forgotten. Elite hunters—perhaps former 
  comrades—track you specifically. They know your tactics.
  Confrontation inevitable.

objectives:
  - Identify the hunters (house affiliation, numbers, methods)
  - Choose: ambush, negotiate, flee and mislead, or stand and fight
  - Learn what the city knows and plans
```

### GATE_3.2_DUERGAR_MARKET

```yaml
trigger: "Following trade rumors or seeking specific supplies"

what_happens: |
  Major duergar trading post. Neutral ground by tradition—even 
  enemies trade here. Surface goods, Underdark rarities, slaves,
  information. Everything has a price.

objectives:
  - Navigate market politics
  - Acquire needed items or information
  - Face moral choices (slavery, stolen goods, etc.)

shadow_range: "Slave trade +10-12 | Disrupt slavery -6-8"
```

### GATE_3.3_MERCENARY_OFFER

```yaml
trigger: "Reputation attracts attention"

what_happens: |
  Drow mercenary band approaches. They know who you are, what 
  you've done. They offer membership—no judgment on your past, 
  only your skills matter. Or perhaps they're hunting you.

objectives:
  - Determine their true intentions
  - Decide: accept contract, refuse, negotiate terms, or attempt to expose them
```

### GATE_3.4_SURFACE_RUMORS

```yaml
trigger: "Information about surface passages spreads"

what_happens: |
  Rumors of a path to the surface—but guarded, dangerous, or both.
  Companions react based on their own histories. Some fear the sun.
  Others long for it. Your choice shapes the party's future.

objectives:
  - Investigate the rumors
  - Prepare for surface transition (equipment, knowledge, psychological)
  - Decide: pursue surface, remain in Underdark, or split the party
```

### GATE_3.5_SURFACE_APPROACH

```yaml
trigger: "Nearing tunnels that lead to daylight"

what_happens: |
  Conflict at the threshold. Surface defenders clashing with 
  Underdark raiders. The human archer archetype leads defenders—
  potential companion or enemy based on your choice.

objectives:
  - Choose a side (or neither)
  - Resolve the conflict
  - Make first surface impression

shadow_range: "Join raiders +12-15"

companion_potential: [HUMAN_ARCHER]
```

### GATE_3.6_TRIAL_OF_WORTH

```yaml
trigger: "Entering surface tribal lands OR emerging from caves"

what_happens: |
  Surface peoples demand proof. Either barbarian trial of combat 
  (if allied with defenders) or militia confrontation (if hostile 
  or unknown). You must prove what you are.

objectives:
  - Face the test (combat, diplomacy, or demonstration)
  - Establish surface reputation
  - Earn or demand respect

companion_potential: [BARBARIAN_WARRIOR]
```

---

## ACT_3_COMPLETION

```yaml
path_determination:
  check: "Shadow value at Act 3 completion"
  REDEMPTION: "Shadow < 30"
  DARKNESS: "Shadow > 70"
  NEUTRAL: "Shadow 30-70"

STATE_SUMMARY_includes:
  active_path: "REDEMPTION | DARKNESS | NEUTRAL"
  note: "Path stored in save allows Act 4 restart"

final_beat: |
  The sun burns. Surface peoples judge. Your companions—those who 
  remain—watch to see who you've become. Now comes consequence.

prompt_user: "Act 3 complete. Save STATE_SUMMARY. Continue with: Kernel + Overview + act_4 + STATE_SUMMARY"
```
