# ACT 4: THE RECKONING

```yaml
VALIDATION: {type: "act_file", acts: [4], paths: [REDEMPTION, DARKNESS, NEUTRAL], gates: 15, echo: "✅ ACT 4 | Paths: 3 | Gates: 15 | Status: READY"}
```

## PATH_DETERMINATION

```yaml
from_save: {REDEMPTION: "<30 Shadow OR active_path", DARKNESS: ">70 Shadow OR active_path", NEUTRAL: "30-70 OR active_path"}
note: "Extreme actions can shift path, but momentum resists"
```

## GATE_LEVELS

```yaml
REDEMPTION: {4R.1: 8, 4R.2: 9, 4R.3: 9, 4R.4: 10, 4R.5: 11, 4R.6: 12}
DARKNESS: {4D.1: 8, 4D.2: 9, 4D.3: 9, 4D.4: 10, 4D.5: 11, 4D.6: 12}
NEUTRAL: {4N.1: 8, 4N.2: 9, 4N.3: 9, 4N.4: 10, 4N.5: 11, 4N.6: 12}
```

## HUBS

```yaml
HUBS:
  coalition_camp: {path: REDEMPTION, services: [Rest, Supplies, War council, Allies], board: [standard, redemption], note: "Contracts support war"}
  warlord_stronghold: {path: DARKNESS, services: [Rest, Black market, Mercs, Slaves], board: [standard, darkness], note: "DARK_REPLACEMENT_POOL available"}
  free_territory: {path: NEUTRAL, services: [Rest, Trading, Militia, Refuge], board: [standard], note: "Contracts defend territory"}
```

## PHASES

```yaml
REDEMPTION: {phase: "HERO_RISING", pacing: medium, feel: "Coalition building takes time.", restrictions: [Political complexity, Fragile trust, War looms]}
DARKNESS: {phase: "CONQUEST", pacing: high, feel: "Rivals plot. Power demands vigilance.", restrictions: [Betrayal risk, Control forces, Enemies multiply]}
NEUTRAL: {phase: "INDEPENDENCE", pacing: medium, feel: "Building and defending.", restrictions: [Two-front pressure, Resources stretched, Trust earned slowly]}
```

---

## REDEMPTION PATH (Shadow < 30)

### 4R.1 THREAT_REVEALED

```yaml
trigger: "Refugees bring dire news"
scene: "Something rises—demon cult, drow invasion, ancient evil. Threatens both realms. Your position makes you invaluable or suspect."
objectives: [Learn threat's nature, Convince surface kingdoms, Choose approach: warn/evidence/rally Underdark first]
```

### 4R.2 COALITION_BUILDING

```yaml
trigger: "Seeking allies"
scene: "Surface distrusts. Old enemies must ally. Your reputation—everything you've done—matters. Companions vouch or doubt."
objectives: [Unite fractious allies, Address drow-nature doubts, Build sufficient force]
```

### 4R.3 DROW_FOLLOWERS

```yaml
trigger: "Word spreads to Underdark"
scene: "Drow exiles seek you—genuine seekers, opportunists, spies. You've become a symbol."
objectives: [Evaluate followers (genuine vs false), Handle responsibility, Address coalition infiltration concerns]
```

### 4R.4 PROVING_GROUND

```yaml
trigger: "Early enemy engagement"
pacing: high
scene: "First battle as coalition commander. Tactical choices and valor cement trust or confirm fears. Companions may fall."
objectives: [Lead forces effectively, Battlefield moral choices, Maintain unity under pressure]
```

### 4R.5 FINAL_BATTLE

```yaml
tactical_start: true
pacing: extreme
trigger: "Climactic confrontation"
scene: "Threat's heart—demon lord, drow matron, awakened evil. Everything tested. Victory requires sacrifice."
objectives: [Defeat ultimate threat, Protect or sacrifice what matters, Determine victory's cost]
```

### 4R.6 AFTERMATH

```yaml
pacing: low
trigger: "Victory, dust settling"
scene: "World changed. Surface must decide—drow hero, uncomfortable proof hatred was too simple. Companions remain or grieve."
objectives: [Determine your place, Honor sacrifices, Choose future]
endings: {legendary: "0-15 | Sacrifice transforms world", proven: "16-25 | Acceptance earned", tarnished: "26-35 | Victory, scarred methods"}
```

---

## DARKNESS PATH (Shadow > 70)

### 4D.1 POWER_BASE

```yaml
trigger: "Establishing dominion"
scene: "Surface fears you—rightfully. Convert fear to power. Territory to claim, forces to gather, examples to make."
objectives: [Establish territorial control, Gather forces, Demonstrate power]
```

### 4D.2 DARK_RECRUITMENT

```yaml
trigger: "Building army"
scene: "Drow mercenaries. Monster tribes. Anyone respecting strength. Gold, promises, intimidation."
objectives: [Recruit sufficient forces, Manage competing interests, Maintain control through strength]
```

### 4D.3 INTERNAL_RIVALS

```yaml
pacing: extreme
trigger: "Lieutenants grow ambitious"
scene: "Power attracts challengers. Capable subordinates see themselves on throne. Poison, assassination, challenges—the dark way."
objectives: [Identify conspirators, Crush rebellion decisively, Establish unquestioned dominance]
```

### 4D.4 FORMER_COMPANIONS

```yaml
trigger: "Those who left now oppose"
scene: "Departed companions lead resistance. Know your tactics, weaknesses. Once friends, now enemies. Personal."
objectives: [Face former companions, Choose: lethal/capture/reconciliation (near impossible), Live with choice]
shadow: "Kill +8-10 | Attempt mercy -8-10"
```

### 4D.5 FINAL_CONQUEST

```yaml
tactical_start: true
pacing: extreme
trigger: "Major kingdom within reach"
scene: "Surface coalition makes final stand. Champions, armies, hope—against your dark tide. Victory = empire. Defeat = death."
objectives: [Defeat surface coalition, Crush or convert resistance, Claim throne]
shadow: "Total annihilation +6-10"
```

### 4D.6 THRONE

```yaml
pacing: low
trigger: "Victory, kingdom yours"
scene: "Crown and carnage. Surface kneels. Remaining companions stand behind—afraid of what you've become. Now: rule."
objectives: [Establish rule style, Deal with remaining resistance, Accept what you've become]
shadow: "Unexpected reform -8-12"
endings: {eternal_tyrant: "90-100 | Terror empire", dark_emperor: "71-89 | Brutal but functional"}
```

---

## NEUTRAL PATH (Shadow 30-70)

### 4N.1 CLAIM_TERRITORY

```yaml
trigger: "Seeking your own place"
scene: "Neither hero nor conqueror—you want freedom. Borderland territory, dangerous but defensible."
objectives: [Identify suitable territory, Acquire it (negotiate/purchase/force), Establish defenses]
```

### 4N.2 RECRUIT_OUTCASTS

```yaml
trigger: "Building community"
scene: "Others who don't fit—surface refugees, Underdark exiles. Your territory: haven or armed camp."
objectives: [Attract population, Establish community norms, Build defense capability]
```

### 4N.3 SPIES_WITHIN

```yaml
trigger: "Suspicious activity, sabotage"
scene: "Independence threatens both realms. Agents infiltrated—surface spies, Underdark saboteurs. Trust difficult."
objectives: [Identify infiltrators, Handle them (execute/exile/turn/use), Maintain cohesion]
shadow: "Torture +8-10"
```

### 4N.4 DUAL_PRESSURE

```yaml
trigger: "Both realms notice you"
scene: "Surface and Underdark demand allegiance. Envoys arrive with ultimatums. Your independence threatens everyone's narrative."
objectives: [Hear both sides, Choose: ally surface/ally Underdark/refuse both, Prepare consequences]
shadow: "Ally surface -8-12 | Ally Underdark +8-12"
path_shift: {ally_surface: "→ Redemption", ally_underdark: "→ Darkness"}
```

### 4N.5 FINAL_STAND

```yaml
tactical_start: true
pacing: extreme
trigger: "Both realms attack"
scene: "Surface army from one direction, Underdark force from another. Two fronts, limited forces, everything at stake."
objectives: [Defend two fronts, Defeat or drive off both, Survive with community intact]
```

### 4N.6 AFTERMATH

```yaml
pacing: low
trigger: "Survival achieved"
scene: "Bloody, exhausted, but free. Both realms know: you cannot be easily claimed. Your choice proved."
objectives: [Establish lasting governance, Negotiate peace or armed neutrality, Choose future]
endings: {free_state: "35-55 | Beacon for outcasts", independent: "45-60 | Fortress of survival", growing_power: "56-70 | Expansion through strength"}
```

---

**END ACT 4 v6.2.1**
