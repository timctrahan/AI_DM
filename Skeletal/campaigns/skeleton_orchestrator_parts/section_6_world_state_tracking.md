# SECTION 6: WORLD STATE TRACKING

## Campaign Flag System

```yaml
story_flags:
  [flag_name]: false  # Boolean: has this happened yet?
  [flag_name]: false
  [flag_name]: false

time_sensitive_events:
  [event_name]:
    trigger_date: [In-game day when this activates]
    consequence: "[What happens if party doesn't intervene?]"

active_threats:
  [threat_name]:
    current_danger_level: 1-10
    what_makes_it_worse: "[Party action X increases danger]"
    what_reduces_it: "[Party action Y decreases danger]"
```

## Reputation Score Summary

```yaml
factions:
  [faction_A]: 0
  [faction_B]: 0
  [faction_C]: 0

reputation_gates:
  faction_A_at_5: "[What becomes available?]"
  faction_A_at_-5: "[What becomes hostile?]"
  faction_B_at_3: "[What becomes available?]"
  # etc
```

---
