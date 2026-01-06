# ACTS 1-3

```yaml
VALIDATION: {type: "act_file", acts: [1,2,3], gates: 18, kernel: "6.2+", echo: "✅ ACTS 1-3 | Gates: 18 | Status: READY"}
```

## GATE_LEVELS

```yaml
ACT_1: {1.1: 1, 1.2: 1, 1.3: 1, 1.4: 2, 1.5: 2, 1.6: 2}  # L1-2 The Fall
ACT_2: {2.1: 3, 2.2: 3, 2.3: 4, 2.4: 4, 2.5: 4, 2.6: 5, 2.7: 5, 2.8: 5}  # L3-5 Hungry Dark
ACT_3: {3.1: 6, 3.2: 6, 3.3: 7, 3.4: 7, 3.5: 7, 3.6: 8}  # L6-8 Twilight Realms
```

## PHASES

```yaml
ACT_1: {phase: "BETRAYAL_AND_EXILE", pacing: extreme, feel: "No safe rest. Constant tension.", restrictions: [50% encounter/rest, Wild magic, Solitude WIS DC 12]}
ACT_2: {phase: "SURVIVAL_AND_TEMPTATION", pacing: high, feel: "Brief breathers. Short rests risky.", restrictions: [Deeper Underdark, Forage DC 15, Moral compromises]}
ACT_3: {phase: "IDENTITY_CHOICE", pacing: medium, feel: "Rests possible. Exploration allowed.", restrictions: [Faction politics, Surface prejudice]}
```

## HUBS

```yaml
HUBS:
  deep_gnome_outpost: {unlock: 1.6, if: "peaceful", services: [Rest, Supplies, Info], board: [standard, redemption]}
  duergar_outpost: {unlock: 2.4, if: "not hostile", services: [Rest(paid), Black market, Mercs, Slaves], board: [standard, darkness], warn: "Companions react"}
  svirfneblin_refuge: {unlock: 2.6, if: "peaceful", services: [Rest, Gems, Crafting, Info], board: [standard, redemption], note: "Only safe hub Act 2"}
  frontier_settlement: {unlock: 3.6, if: "not hostile to surface", services: [Rest, Supplies, Smith, Temple], board: [standard, redemption], note: "First surface hub"}
  barbarian_camp: {unlock: 3.6, if: "earned respect", services: [Rest, Training, Wisdom, Beasts], board: [standard], note: "Combat-focused"}
```

---

## ACT 1: THE FALL

### 1.1 HOUSE_FALL

```yaml
tactical_start: true
trigger: "Campaign start - house raid"
npcs: {mentor_blademaster: "Fighting nearby, urges escape, covers retreat"}
scene: "Rival house attacks. Venomous flames, spider swarms, collapsing stone. Mentor fights nearby. Something awakens—questioning the slaughter."
objectives: [Navigate to exit tunnel, Survive 2-3 scouts + hazards, Moral beat (save/abandon/confront), Witness mentor's fate]
```

### 1.2 PURSUIT_AND_SOLITUDE

```yaml
trigger: "Fleeing into wild Underdark"
scene: "Hunters track you. Too many to fight. 3D maze tunnels. Absolute darkness."
objectives: [Evade 4-6 hunters (OVERWHELMING—stealth/chase), Navigate hazards, Endure isolation (WIS save)]
note: "NOT fair fight. Present hide/flee/distract."
```

### 1.3 LEGENDARY_BLADES

```yaml
trigger: "Deeper tunnels, magical resonance"
scene: "Wild magic pulses. Fallen surface hero's remains. Twin scimitars: one cold, one glowing. Panther approves."
objectives: [Investigate hero (surface clues), Claim scimitars, Survive wild magic surge, Test blades vs minor threat]
unlock: {frost_scimitar: "+cold damage", glowing_scimitar: "Glows blue near enemies"}
```

### 1.4 ABERRANT_HAZARDS

```yaml
trigger: "Cavern maze opens"
scene: "Skittering louder. Aberrations—hook horrors, umber hulks. Panther warns."
objectives: [Resolve aberrant threat, Navigate maze (Survival DC 15), Strengthen panther bond]
```

### 1.5 ESCAPED_PRISONERS

```yaml
trigger: "Faint voices, signs of conflict"
scene: "Escaped prisoners—gruff dwarf fighter, clever halfling rogue. Fleeing duergar slavers. Wary of drow."
objectives: [Contact without violence, Prove trustworthy, Resolve their escape]
recruit: {mandatory: true, blocked: ">75 Shadow", harder: ">60 (+5 DC)", potential: [dwarf_leader, halfling_rogue]}
shadow: "Betray +8-10"
```

### 1.6 FIRST_OUTSIDER_CONTACT

```yaml
trigger: "Gem-light, mining sounds"
pacing: high
scene: "Glowing fungi reveal deep gnome scouts. Suspicious. Fear drow. First faction rep."
objectives: [Initiate contact, Exchange info/trade, Establish faction standing]
```

---

## ACT 2: THE HUNGRY DARK

### 2.1 ABERRATION_TERRITORY

```yaml
trigger: "Deeper, aberrant signs"
scene: "Hook horror nests, mind flayer scouts, beholder kin. True Underdark horrors."
objectives: [Cross or clear territory, Protect companions from psychic threats, Choose: stealth/diplomacy/violence]
```

### 2.2 STARVING_DARK

```yaml
trigger: "Resources depleted"
scene: "Days without food. Tainted water. Panther returns empty. Companions weaken."
objectives: [Find food/water, Choose method: hunt/trade/raid/natural]
shadow: "Raid myconids = major increase"
```

### 2.3 DEMON_CULT

```yaml
trigger: "Dark whispers, fleeing worse"
scene: "Corrupted shrine. Drow demon-worshippers. Sulfur and madness. Chained massive human warrior among captives."
objectives: [Survive contact, Learn Underdark intel, Choose: destroy/infiltrate/bargain/flee]
npcs: {barbarian_warrior: "Captive, chained, spirit unbroken"}
shadow: "Join cult +15-20"
```

### 2.4 ENSLAVED_WARRIOR

```yaml
trigger: "Cult captive discovered"
scene: "Massive blonde warrior. Demons planned sacrifice. Fierce blue eyes judge you."
objectives: [Free or leave him, Earn trust through action, Survive his drow-distrust]
recruit: {mandatory: true, blocked: ">70 Shadow", harder: ">55 (+5 DC)", potential: [barbarian_warrior]}
shadow: "Leave +5 | Betray +12"
```

### 2.5 DUERGAR_ENCOUNTER

```yaml
trigger: "Trade routes, fleeing pursuit"
scene: "Gray dwarf outpost. Slavers, merchants, pragmatists. Among slaves—human woman, archer's calluses, calculating eyes."
objectives: [Navigate duergar society, Acquire resources, Face slavery directly]
npcs: {human_archer: "Captive, enslaved, defiant"}
shadow: "Liberate -8-10 | Participate +10-15"
```

### 2.6 ARCHER_IN_CHAINS

```yaml
trigger: "Duergar captive, slave pens"
scene: "Human archer fights chains. Speaks dwarvish natively. Recognizes dwarf companion. Sees YOU—hatred burns."
objectives: [Free or leave her, Overcome drow-hatred, Prove through action]
recruit: {mandatory: true, blocked: ">65 Shadow", harder: ">50 (+5 DC)", easier: "dwarf_leader in party (advantage)", potential: [human_archer]}
shadow: "Leave +5 | Sell +15"
```

### 2.7 DRIDERS_WARNING

```yaml
trigger: "Ambushed by transformed drow"
scene: "Driders lurk. One approaches to warn, not kill. Knows your house, what hunts you. Information has price."
objectives: [Survive ambush/approach, Learn city's plans, Choose: mercy/alliance/destruction]
```

### 2.8 DEEP_GNOME_REFUGE

```yaml
trigger: "Seeking allies, safety"
pacing: medium
scene: "Hidden svirfneblin settlement. Deeply suspicious—suffered too much. Trust earned by action."
objectives: [Gain entry peacefully, Prove trustworthy, Establish faction standing]
shadow: "Intimidate +8 | Raid +12"
```

---

## ACT 3: TWILIGHT REALMS

### 3.1 HUNTERS_FROM_HOME

```yaml
trigger: "Organized pursuit signs"
scene: "Elite hunters from the city. Perhaps former comrades. Know your tactics. Confrontation inevitable."
objectives: [Identify hunters (house, numbers, methods), Choose: ambush/negotiate/flee/fight, Learn city's plans]
```

### 3.2 DUERGAR_MARKET

```yaml
trigger: "Trade rumors, seeking supplies"
scene: "Major duergar post. Neutral ground. Surface goods, rarities, slaves, information. Everything priced."
objectives: [Navigate market politics, Acquire items/info, Face moral choices]
shadow: "Slave trade +10-12 | Disrupt slavery -6-8"
```

### 3.3 MERCENARY_OFFER

```yaml
trigger: "Reputation attracts attention"
scene: "Drow mercenary band approaches. They know you. Offer membership—no judgment, only skills. Or hunting you."
objectives: [Determine true intentions, Choose: accept/refuse/negotiate/expose]
```

### 3.4 SURFACE_RUMORS

```yaml
trigger: "Surface passage info spreads"
scene: "Rumors of path to surface—guarded, dangerous. Companions react by history. Some fear sun, others long for it."
objectives: [Investigate rumors, Prepare for transition, Choose: pursue/remain/split party]
```

### 3.5 SURFACE_THRESHOLD

```yaml
trigger: "Nearing daylight tunnels"
scene: "Passage opens. Light ahead—sunlight. Burns your eyes from here. Surface defenders see drow emerge, reach for weapons."
objectives: [First surface contact, Prove not raiders, Navigate blinding transition]
shadow: "Attack +12-15 | Peaceful -3-5"
```

### 3.6 TRIAL_OF_WORTH

```yaml
trigger: "Surface demands proof"
scene: "Drow in daylight. Villages bar doors. Warriors gather. Companions speak—or stay silent—based on GATE_HISTORY."
objectives: [Face tribunal/trial, Let actions speak (companions testify), Establish surface rep]
shadow: "Threaten +10 | Accept judgment -5"
```

---

## ACT_3_COMPLETION

```yaml
path_check: {REDEMPTION: "<30 Shadow", DARKNESS: ">70 Shadow", NEUTRAL: "30-70"}
save_includes: [active_path, weave_state, tracking_state]
final_beat: "Sun burns. Surface judges. Companions watch who you've become. Now: consequence."
prompt: "Act 3 complete. Save STATE_SUMMARY. Continue: Kernel + core + act_4 + save"
```

---

**END ACTS 1-3 v6.2.1**
