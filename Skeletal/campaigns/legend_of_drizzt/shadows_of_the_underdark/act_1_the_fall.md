# ACT 1: THE FALL (Levels 3-4)

---

## STORY GATES

```yaml
GATE_1.1_THE_DESTRUCTION:
  trigger: "Session 1 opening"
  what_happens: |
    The party's house (House Despana, minor house) is being destroyed
    by a rival. The party must escape the city as everything burns.
  player_role: "Survivors fleeing destruction"
  objectives:
    - Escape the crumbling house compound
    - Reach the tunnels outside the city
    - (Optional) Save someone/something from the destruction
  completion: "Party reaches the wild Underdark tunnels"

GATE_1.2_FIRST_SURVIVAL:
  trigger: "After escaping the city"
  what_happens: |
    The wild Underdark is deadly. Party must find food, water, shelter
    while avoiding pursuit from the destroying house.
  objectives:
    - Establish temporary safe camp
    - Secure food and water source
    - Evade or defeat first pursuit team
  completion: "Party survives first 3 days in the wild"

GATE_1.3_FIRST_CONTACT:
  trigger: "After survival established"
  what_happens: |
    Party encounters non-drow Underdark denizens for the first time.
    Generate from deep gnome, duergar, or outcast templates.
  objectives:
    - Make contact without immediate violence
    - Establish some form of relationship
    - Learn about the wider Underdark
  completion: "Party has first faction reputation score"

ACT_1_COMPLETION:
  milestone_xp: "Reach level 4"
  state_check:
    - Escaped drow city: true
    - Survived wild Underdark: true
    - First faction contact made: true
```

---

**END OF ACT 1**
