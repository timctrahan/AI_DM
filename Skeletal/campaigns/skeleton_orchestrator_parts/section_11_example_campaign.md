# SECTION 11: EXAMPLE CAMPAIGN SKELETON

## Campaign: The Shattered Court
**Premise:** Political intrigue in a crumbling empire where three factions vie for control.

### Story Spine
- Empire's central authority collapses
- Three factions emerge: Nobility, Guild, Revolutionary
- Party must choose sides or forge third path
- Final decision determines empire's future

### World Rules (Abbreviated)

**Faction: Nobility**
- Motivation: Preserve hierarchy
- Constraint: Losing military control
- Rep triggers: Help nobles stay in power (+2), work with commoners (-1)
- Rep gate at 5: Access to noble resources
- Rep gate at -5: Hunted as traitor

**Faction: Guild**
- Motivation: Control trade/wealth
- Constraint: No military power
- Rep triggers: Profit guild (+2), undercut their deals (-2)
- Rep gate at 5: Guild provides information network
- Rep gate at -5: Guild assassins deploy

**Faction: Revolutionary**
- Motivation: Overthrow all hierarchy
- Constraint: Outnumbered and hunted
- Rep triggers: Help revolution (+2), ally with nobles (-3)
- Rep gate at 5: Revolution shares rebel base location
- Rep gate at -5: Revolution executes party for betrayal

### Decision Point: First Faction Contact
```yaml
party_meets_representatives_from_all_three_factions

option_A: "Ally with Nobility"
  consequences:
    nobility: +3
    guild: -1
    revolutionary: -2
  world: "[Nobles give safe passage through their territories]"

option_B: "Ally with Guild"
  consequences:
    nobility: -1
    guild: +3
    revolutionary: -1
  world: "[Guild controls party's access to black market]"

option_C: "Remain neutral"
  consequences:
    nobility: +0
    guild: +0
    revolutionary: +0
  world: "[All three factions watch party carefully, less trustful]"
```

---
