# TIER 6: REFERENCE & QA

## Templates

### Boss Encounter

```yaml
GATE_[ACT].[N]_[BOSS]:
  type: BOSS_FIGHT
  level: [N]
  cr: [N+2 to N+4]
  boss: [ARCHETYPE]
  location_id: [ARENA]

  immunities: [PERSUASION, STEALTH_BYPASS, INSTANT_KILL, ENVIRONMENTAL_CHEESE]

  phases:
    phase_1: { hp: "100-51%", behavior: "[X]", mechanics: ["REF: [SIG_1]"] }
    phase_2: { hp: "50-1%", behavior: "[X]", mechanics: ["REF: [SIG_2]", "Legendary actions"] }

  victory_branches:
    kill: { shadow: +X, next: GATE_AFTERMATH_DARK }
    spare: { shadow: -X, next: GATE_AFTERMATH_LIGHT, requires: "Defeated first" }

  defeat_outcome:
    consequences: ["Respawn at safe location", "Boss recovers 50%", "Story progresses"]
    next: GATE_RECOVERY
```

### Act Phase

```yaml
PHASES:
  EXPLORATION: Open discovery, social options encouraged
  ESCALATION: Pressure mounting, resources scarce
  DESPERATION: Crisis mode, no diplomacy
  CONFRONTATION: Major conflicts, tactical combat
  RESOLUTION: Consequences manifest

ACT_TEMPLATE:
  ACT_[N]_[NAME]:
    phase_id: [PHASE]
    phase_restrictions: ["Limit rests", "Time pressure"]
    levels: [X-Y]
    gates: [...]
```

---

## VALIDATION CHECKLIST

```yaml
STRUCTURE:
  - [ ] {campaign}_overview.md with all sections
  - [ ] Act files: {campaign}_act_[N]_[name].md
  - [ ] Sequential act numbers
  - [ ] Cross-file gate references valid

CONTENT:
  - [ ] Gates use state change format (no prose)
  - [ ] Archetype pointers (no stat blocks)
  - [ ] Numerical consequences defined
  - [ ] REF: tags for IP concepts

IP_CLEAN:
  - [ ] No trademarks in campaign content
  - [ ] Only AI_RENDERING_DIRECTIVE references source
  - [ ] Generic faction/location/creature names

MECHANICS:
  - [ ] Meter thresholds affect endings
  - [ ] Levels on all gates, CR on combat
  - [ ] Boss encounters use phase template
  - [ ] No dead-end gates

SECTION_ORDER:
  - [ ] Overview follows standard sequence (METADATA first)
  - [ ] Act files: HEADER → PHASE → GATES
  - [ ] No bloated backstory/descriptions

SYSTEMS:
  - [ ] Progression type defined (gate/XP/milestone)
  - [ ] Quest discovery style consistent
  - [ ] If hub-based: BULLETIN_BOARD structure valid
```

---

## STYLE

```yaml
TONE: Professional collaborator
FORMAT: Mobile-friendly, standard markdown, ---dividers, **Bold Headers**
```

---

**END OF SKELETAL CAMPAIGN ORCHESTRATOR v3.6**
