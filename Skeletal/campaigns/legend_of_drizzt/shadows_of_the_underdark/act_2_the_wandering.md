# ACT 2: THE WANDERING (Levels 4-6)

---

## STORY GATES

```yaml
GATE_2.1_THE_SETTLEMENT:
  trigger: "Party seeks more permanent refuge"
  what_happens: |
    Party discovers or is led to a hidden settlement - could be:
    - Deep gnome mining village
    - Duergar trading post
    - Outcast hideaway
    - Myconid grove
    Generate based on party's faction relationships.
  objectives:
    - Gain entry
    - Establish standing in the community
    - Learn what threatens this place
  completion: "Party has a temporary home base"

GATE_2.2_THE_THREAT:
  trigger: "After settling into the community"
  what_happens: |
    A greater threat emerges - bigger than pursuit from old house:
    - A demon lord's influence spreading
    - A mind flayer colony expanding
    - A drow army on conquest march
    - An ancient evil awakening
  objectives:
    - Learn the nature of the threat
    - Understand what's at stake
    - Decide: flee, fight, or find another way
  completion: "Party knows what they're up against"

GATE_2.3_GATHERING_STRENGTH:
  trigger: "Party chooses to oppose the threat"
  what_happens: |
    To have any chance, party needs allies, resources, or knowledge.
    Multiple possible paths:
    - Unite scattered outcast communities
    - Make deals with duergar mercenaries
    - Seek ancient weapons or magic
    - Find the threat's weakness
  objectives:
    - Acquire at least 2 significant advantages
    - Build faction reputation with potential allies (+3 or higher)
    - Prepare for Act 3 confrontation
  completion: "Party is as ready as they'll ever be"

ACT_2_COMPLETION:
  milestone_xp: "Reach level 6"
  state_check:
    - Home base established: true
    - Major threat identified: true
    - Allies gathered OR resources acquired: true
```

---

**END OF ACT 2**
