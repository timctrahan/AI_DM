# SECTION 5: DECISION POINT FRAMEWORK

## Structured Decision Points

Every time party makes a choice that affects world state:

```yaml
decision_point_name: [What's being decided?]
player_options:
  option_A: [Brief description of choice]
  option_B: [Brief description of choice]
  option_C: [Brief description of choice]
  option_D: "[Custom choice allowed]"

consequences_for_reputation:
  option_A:
    faction_X: [+/- amount]
    faction_Y: [+/- amount]

  option_B:
    faction_X: [+/- amount]
    faction_Y: [+/- amount]

consequences_for_world:
  option_A: "[What becomes true? What closes? What opens?]"
  option_B: "[What becomes true? What closes? What opens?]"

immediate_effect:
  option_A: "[What happens RIGHT NOW?]"
  option_B: "[What happens RIGHT NOW?]"

delayed_consequences:
  option_A:
    - "[If X, then Y happens next session]"
    - "[If Z, then W happens later]"
  option_B:
    - "[...]"
```

---
