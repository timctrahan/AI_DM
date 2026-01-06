# ACT 4: THE RECKONING

```yaml
VALIDATION:
  type: "act_file"
  acts: [4]
  paths: [REDEMPTION, DARKNESS, NEUTRAL]
  gates: 15
  echo: "✅ ACT: 4 (The Reckoning) | Paths: 3 | Gates: 15 | Status: READY"
```

## PATH_DETERMINATION

```yaml
from_STATE_SUMMARY:
  REDEMPTION: "Shadow < 30 OR active_path: REDEMPTION"
  DARKNESS: "Shadow > 70 OR active_path: DARKNESS"
  NEUTRAL: "Shadow 30-70 OR active_path: NEUTRAL"

note: "Player can shift through extreme actions, but momentum resists"
```

## GATE_LEVELS

```yaml
REDEMPTION: # L8-12
  4R.1_THREAT_REVEALED: 8
  4R.2_COALITION_BUILDING: 9
  4R.3_DROW_FOLLOWERS: 9
  4R.4_PROVING_GROUND: 10
  4R.5_FINAL_BATTLE: 11
  4R.6_AFTERMATH: 12

DARKNESS: # L8-12
  4D.1_POWER_BASE: 8
  4D.2_DARK_RECRUITMENT: 9
  4D.3_INTERNAL_RIVALS: 9
  4D.4_FORMER_COMPANIONS: 10
  4D.5_FINAL_CONQUEST: 11
  4D.6_THRONE: 12

NEUTRAL: # L8-12
  4N.1_CLAIM_TERRITORY: 8
  4N.2_RECRUIT_OUTCASTS: 9
  4N.3_SPIES_WITHIN: 9
  4N.4_DUAL_PRESSURE: 10
  4N.5_FINAL_STAND: 11
  4N.6_AFTERMATH: 12
```

## HUBS

```yaml
COALITION_CAMP: # Redemption
  services: [Rest, Supplies, War council, Allied forces]
  mission_board: [standard, redemption]
  special: "Contracts support war effort"

WARLORD_STRONGHOLD: # Darkness
  services: [Rest, Black market, Mercenary recruitment, Slave pens]
  mission_board: [standard, darkness]
  special: "Contracts expand power"
  dark_companions: "DARK_REPLACEMENT_POOL available"

FREE_TERRITORY: # Neutral
  services: [Rest, Trading post, Militia training, Outcast refuge]
  mission_board: [standard]
  special: "Contracts defend territory"
```

## PHASE_RESTRICTIONS

```yaml
ACT_4_REDEMPTION:
  phase: HERO_RISING
  pacing: medium
  journey_feel: "Travel and encounters. Rests possible. Coalition building takes time."
  restrictions: [Political complexity, Trust fragile, War looms]

ACT_4_DARKNESS:
  phase: CONQUEST
  pacing: high
  journey_feel: "Brief breathers. Rivals plot. Power demands constant vigilance."
  restrictions: [Betrayal risk, Forces need control, Enemies multiply]

ACT_4_NEUTRAL:
  phase: INDEPENDENCE
  pacing: medium
  journey_feel: "Building and defending. Rests possible but threats persist."
  restrictions: [Two-front pressure, Resources stretched, Trust earned slowly]
```

---

## REDEMPTION GATES

*Shadow < 30 - Prove drow can choose differently*

### GATE_4R.1_THREAT_REVEALED

```yaml
trigger: "Refugees bring dire news"

what_happens: |
  Something rises from the Underdark. Demon cult unleashed, drow 
  invasion force, or ancient evil awakening. Threatens both realms.
  Your unique position makes you invaluable—or suspect.

objectives:
  - Learn the nature of the threat
  - Convince surface kingdoms of the danger
  - Choose approach: warn immediately, gather evidence, rally Underdark allies first

```

### GATE_4R.2_COALITION_BUILDING

```yaml
trigger: "Seeking allies against the threat"

what_happens: |
  Surface kingdoms distrust. Old enemies must become allies. 
  Your reputation—everything you've done—now matters.
  Companions vouch or doubt based on your history.

objectives:
  - Unite fractious allies
  - Address doubts about drow nature
  - Build force strong enough to face the threat

```

### GATE_4R.3_DROW_FOLLOWERS

```yaml
trigger: "Word of your path spreads to the Underdark"

what_happens: |
  Other drow exiles seek you out—some genuine seekers of redemption, 
  others opportunists, a few possible spies. They want to follow 
  your example. You've become a symbol whether you wanted it or not.

objectives:
  - Evaluate the followers (genuine vs. false)
  - Decide how to handle this responsibility
  - Deal with coalition concerns about drow infiltration

```

### GATE_4R.4_PROVING_GROUND

```yaml
trigger: "Early engagement with enemy forces"
pacing: high  # Override: active warfare

what_happens: |
  First battle as coalition commander. Your tactical choices 
  and personal valor either cement trust or confirm fears.
  Companions fight alongside—some may fall.

objectives:
  - Lead coalition forces effectively
  - Make battlefield moral choices (sacrifice few for many, etc.)
  - Maintain coalition unity under pressure

```

### GATE_4R.5_FINAL_BATTLE

```yaml
trigger: "Climactic confrontation"
pacing: extreme  # Override: final battle
tactical_start: true

what_happens: |
  The threat's heart. Demon lord, drow matron, or awakened evil.
  Everything built—allies, reputation, companions—tested utterly.
  Victory requires sacrifice.

objectives:
  - Defeat the ultimate threat
  - Protect what matters (or sacrifice it)
  - Determine the cost of victory

```

### GATE_4R.6_AFTERMATH

```yaml
trigger: "Victory achieved, dust settling"
pacing: low  # Override: denouement

what_happens: |
  The world changed. Surface kingdoms must decide what to do 
  with you—drow hero, uncomfortable proof that their hatred 
  was too simple. Your companions remain—or grieve.

objectives:
  - Determine your place in the new order
  - Honor sacrifices made
  - Choose your future


endings:
  legendary_hero: "Shadow 0-15 | World transformed by sacrifice"
  proven_hero: "Shadow 16-25 | Acceptance earned through deeds"
  tarnished_hero: "Shadow 26-35 | Victory, but methods left scars"
```

---

## DARKNESS GATES

*Shadow > 70 - Strength and dominion*

### GATE_4D.1_POWER_BASE

```yaml
trigger: "Establishing dominion"

what_happens: |
  The surface fears you—rightfully. Time to convert fear into 
  power. Territory to claim, forces to gather, examples to make.

objectives:
  - Establish territorial control
  - Gather forces (mercenaries, monsters, desperate)
  - Demonstrate power to resisters

```

### GATE_4D.2_DARK_RECRUITMENT

```yaml
trigger: "Building an army"

what_happens: |
  Drow mercenary bands. Monster tribes. Anyone who respects 
  strength. Gold, promises, intimidation—whatever works.
  Companions who remain watch uneasily.

objectives:
  - Recruit sufficient forces
  - Manage competing interests
  - Maintain control through strength

```

### GATE_4D.3_INTERNAL_RIVALS

```yaml
trigger: "Lieutenants grow ambitious"
pacing: extreme  # Override: assassination attempts, constant threat

what_happens: |
  Power attracts challengers. Your most capable subordinates 
  see themselves on the throne instead. Poisoned whispers, 
  assassination attempts, outright challenges—the dark way.

objectives:
  - Identify the conspirators
  - Crush the rebellion decisively
  - Establish unquestioned dominance

```

### GATE_4D.4_FORMER_COMPANIONS

```yaml
trigger: "Those who left now oppose"

what_happens: |
  Companions who departed lead resistance. They know your tactics, 
  your weaknesses. Once friends, now enemies. Personal.

objectives:
  - Face former companions
  - Choose: lethal, capture, or attempt reconciliation (near impossible)
  - Live with the choice

shadow_range: "Kill +8-10 | Attempt mercy -8-10"
```

### GATE_4D.5_FINAL_CONQUEST

```yaml
trigger: "Major kingdom falls within reach"
pacing: extreme  # Override: war
tactical_start: true

what_happens: |
  Coalition of surface kingdoms makes final stand. Their champions, 
  their armies, their hope—against your dark tide.
  Victory means empire. Defeat means death.

objectives:
  - Defeat surface coalition
  - Crush or convert resistance
  - Claim the throne

shadow_range: "Total annihilation +6-10"
```

### GATE_4D.6_THRONE

```yaml
trigger: "Victory achieved, kingdom yours"
pacing: low  # Override: you've won, now rule

what_happens: |
  Crown and carnage. The surface kneels. Your remaining companions 
  stand behind you—afraid, perhaps, of what you've become.
  Now: how to rule.

objectives:
  - Establish rule style
  - Deal with remaining resistance
  - Accept what you've become

shadow_range: "Unexpected reform -8-12"

endings:
  eternal_tyrant: "Shadow 90-100 | Empire of absolute terror"
  dark_emperor: "Shadow 71-89 | Brutal but functional dominion"
```

---

## NEUTRAL GATES

*Shadow 30-70 - Independence and pragmatism*

### GATE_4N.1_CLAIM_TERRITORY

```yaml
trigger: "Seeking a place of your own"

what_happens: |
  Neither hero nor conqueror—you want freedom. Borderland territory, 
  dangerous but defensible. Current occupants must be dealt with.

objectives:
  - Identify suitable territory
  - Acquire it (negotiation, purchase, or force)
  - Establish initial defenses

```

### GATE_4N.2_RECRUIT_OUTCASTS

```yaml
trigger: "Building a community"

what_happens: |
  Others who don't fit—surface refugees, Underdark exiles, those 
  caught between. Your territory could be haven or armed camp.

objectives:
  - Attract population
  - Establish community norms
  - Build defensive capability

```

### GATE_4N.3_SPIES_WITHIN

```yaml
trigger: "Suspicious activity, sabotage"

what_happens: |
  Your independence threatens both realms. Agents have infiltrated—
  surface spies, Underdark saboteurs. Trust becomes difficult.

objectives:
  - Identify the infiltrators
  - Decide how to handle them (execute, exile, turn, use)
  - Maintain community cohesion

shadow_range: "Torture +8-10"
```

### GATE_4N.4_DUAL_PRESSURE

```yaml
trigger: "Both realms notice you"

what_happens: |
  Surface kingdoms and Underdark forces both demand allegiance.
  Envoys arrive with ultimatums. Your independence threatens 
  everyone's narrative.

objectives:
  - Hear both sides
  - Choose: ally surface, ally Underdark, or refuse both
  - Prepare for consequences

shadow_range: "Ally surface -8-12 | Ally Underdark +8-12"

path_shift_possible:
  ally_surface: "Shifts toward Redemption"
  ally_underdark: "Shifts toward Darkness"
```

### GATE_4N.5_FINAL_STAND

```yaml
trigger: "Both realms attack"
pacing: extreme  # Override: fighting on two fronts
tactical_start: true

what_happens: |
  Surface army from one direction, Underdark force from another.
  Your territory, your people, your principle—tested utterly.
  Two fronts, limited forces, everything at stake.

objectives:
  - Defend on two fronts
  - Defeat or drive off both forces
  - Survive with community intact

```

### GATE_4N.6_AFTERMATH

```yaml
trigger: "Survival achieved, independence proven"
pacing: low  # Override: resolution

what_happens: |
  Bloody, exhausted, but free. Both realms know now: you cannot 
  be easily claimed. Your territory is real. Your choice proved.

objectives:
  - Establish lasting governance
  - Negotiate peace or armed neutrality
  - Choose the future


endings:
  free_state: "Shadow 35-55 | Beacon for outcasts"
  independent_bastion: "Shadow 45-60 | Fortress of survival"
  growing_power: "Shadow 56-70 | Expansion through strength"
```
