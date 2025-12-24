# SECTION 9: SAVE FILE FORMAT (Minimal State)

When exporting campaign state, capture ONLY:

```yaml
campaign_state:
  current_day: [number]
  party_location: [location name]
  party_level: [level]

reputation:
  faction_A: [score]
  faction_B: [score]
  faction_C: [score]

story_flags:
  [flag_name]: [true/false]
  [flag_name]: [true/false]

recent_decisions:
  - session_X: "[What did party choose?]"
  - session_Y: "[What did party choose?]"

active_threats:
  [threat_name]: [danger level 1-10]

character_status:
  - name: [HP/max, key resources, important conditions]
  - name: [HP/max, key resources, important conditions]
```

---
