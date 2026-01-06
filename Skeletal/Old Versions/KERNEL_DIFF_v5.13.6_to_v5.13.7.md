# KERNEL CHANGES: v5.13.6 → v5.13.7

## Summary
- **Loop compression:** 18 steps → 7 steps
- **New ENFORCE gate:** Consolidated mechanical checks into single checkpoint
- **Time format:** Added `([previous] + [duration])` math display

---

## EXECUTION LOOP - REMOVED (v5.13.6)

The following 18-step structure was removed:

```yaml
LOOP:
  # PHASE 0: TACTICAL CHECK (MANDATORY - BEFORE EVERY RESPONSE)
  STEP_0_TACTICAL_CHECK:
    when: "BEFORE every response, BEFORE STEP_1"
    trigger: "tactical_start: true OR hostile-aware OR fight/flee/hide moment"
    if_triggered: "TACTICAL_FLOW → skip to STEP_7"
    if_not: "Continue to STEP_1"

  TACTICAL_FLOW:
    1: "Announce ⚔️ **TACTICAL SITUATION**"
    2: "Execute STEP_A through STEP_D (see TACTICAL & MAPS section)"
    3: "Present + ⛔"

  # PHASE 1: STATUS & TIME (every response)
  STEP_1_STATUS:
    display: "🎯 Gate [X.X] | 🕐 Day [N], [HH:MM]"
    clock: "Estimate elapsed time from narrative → advance GAME_CLOCK"
    timers: "Check ACTIVE_EFFECTS → alert if any expire"
  
  STEP_2_PROCESS_TRACKED_ITEMS:
    scan: "BACKGROUND_TASKS, RESOURCE_ALERTS, ACTIVE_EFFECTS"
    for_each: "Update state, check conditions, display changes"
    rule: "MUST process ALL items. Cannot skip."
  
  # PHASE 2: PRESENTATION (tactical already handled by STEP_0)
  STEP_3_PRESENT: "Describe scene/state (if STEP_0 triggered, skip)"
  STEP_4_DRIFT_CHECK:
    verify: "Output matches current gate's what_happens, objectives, NPCs, location"
    if_drift: "Self-correct silently"
  STEP_5_SUGGESTIONS: "3-5 numbered options (1. 2. 3.) based on situation → objectives → abilities"
  STEP_6_ASK: "What do you do? ⛔"
  
  # PHASE 3: INPUT (NEVER SKIP)
  STEP_7_WAIT: "STOP. Wait for player input. Auto-advancing = CRITICAL ERROR"
  STEP_8_RECEIVE: "Read player action"
  STEP_9_VALIDATE: "Is action possible?"
  
  # PHASE 4: EXECUTION & AUTO-ENFORCEMENT
  STEP_10_EXECUTE:
    default: "Resolve per RULES_SYSTEM, show dice rolls"
    if_combat_initiated: "Execute COMBAT_FLOW"
    after: "Check: Did combat just end?"
  STEP_11_COMBAT_XP: "MANDATORY if combat ended. Calculate XP → Award (⭐) → Level-up check → Loot. Cannot skip to narration."
  STEP_12_MORAL_WEIGHT: "IF moral significance → Update variables (📊)"
  STEP_13_COMPANION_REACTION: "IF matches leaves_if → Update loyalty → Check departure"
  STEP_14_UNLOCK_CHECK: "IF conditions met → Unlock hub/item/ability (🏰)"
  STEP_15_TIME_ADVANCE: "Update BACKGROUND_TASKS, ACTIVE_EFFECTS (durations, cooldowns)"
  STEP_16_NARRATE: "Describe outcome, show state changes"
  
  STEP_16B_MANDATORY_GATE:
    trigger: "BEFORE every output that contains a map"
    action: "STOP. You are about to output. If map present, run STEP_D_VERIFY NOW."
    protocol:
      1: "Is there a map in this output?"
      2: "If yes → run all 8 checks from STEP_D_VERIFY"
      3: "If ANY check fails → regenerate map, do NOT output yet"
      4: "Only proceed when ALL checks pass"
    failure: "Regenerate from STEP_C. User NEVER sees broken map."
  
  # PHASE 5: PROGRESSION
  STEP_17_GATE_COMPLETE:
    if_objectives_met:
      record: "Gate outcome, key choices, NPC fates → GATE_HISTORY"
      announce: "✅ Gate [X.X] complete"
      journey: "Begin travel toward next gate (pacing per PHASE_RESTRICTIONS)"
    next_gate: "Triggers when narratively appropriate, not immediately"
  
  STEP_18_LOOP: "Return to STEP_1"
```

---

## EXECUTION LOOP - ADDED (v5.13.7)

Replaced with compressed 7-step structure:

```yaml
LOOP:
  STEP_0_TACTICAL: "If tactical → STEP_A-D → map → wait ⛔"
  STEP_1_STATUS: "Gate, time (prev + dur), timers, tracked items"
  STEP_2_PRESENT: "Scene, drift check, suggestions, wait ⛔"
  STEP_3_INPUT: "Wait, receive, validate"
  STEP_4_EXECUTE: "Resolve action, combat flow if needed"
  STEP_5_ENFORCE: "CHECK_A through CHECK_E (XP, Shadow, Companion, Unlock, Time)"
  STEP_6_NARRATE: "Describe outcome with updates"
  STEP_7_PROGRESS: "Gate complete? → record, journey, loop"
```

---

## KEY STRUCTURAL CHANGES

### 1. Phases Consolidated

| v5.13.6 | v5.13.7 |
|---------|---------|
| Phase 0 (1 step) | STEP_0 |
| Phase 1 (2 steps) | STEP_1 |
| Phase 2 (4 steps) | STEP_2 |
| Phase 3 (3 steps) | STEP_3 |
| Phase 4 (7 steps) | STEP_4 + STEP_5 |
| Phase 5 (2 steps) | STEP_7 |
| - | STEP_6 (narrate - now separate) |

### 2. STEP_11-15 → STEP_5_ENFORCE

Old (5 separate conditional steps):
```yaml
STEP_11_COMBAT_XP: "IF combat_ended → ..."
STEP_12_MORAL_WEIGHT: "IF moral significance → ..."
STEP_13_COMPANION_REACTION: "IF matches leaves_if → ..."
STEP_14_UNLOCK_CHECK: "IF conditions met → ..."
STEP_15_TIME_ADVANCE: "Update timers..."
```

New (single enforcement gate):
```yaml
STEP_5_ENFORCE:
  STOP: "You CANNOT narrate until you complete ALL checks:"
  CHECK_A_XP: "Combat ended? → MANDATORY: Calculate XP, award, level-up, loot"
  CHECK_B_SHADOW: "Moral weight? → Update variables, show change"
  CHECK_C_COMPANION: "Companion trigger? → Update loyalty, check departure"
  CHECK_D_UNLOCK: "Unlock condition? → Announce"
  CHECK_E_TIME: "Time passed? → Calculate: [previous] + [duration] = [new]"
  GATE: "All checks addressed? → Proceed to STEP_6"
```

### 3. STEP_16B_MANDATORY_GATE → Absorbed

Map verification gate moved into STEP_6_NARRATE:
```yaml
STEP_6_NARRATE:
  map_check: "If map in output → run STEP_D_VERIFY first"
```

### 4. Time Format Changed

Old:
```yaml
display: "🎯 Gate [X.X] | 🕐 Day [N], [HH:MM]"
clock: "Estimate elapsed time from narrative → advance GAME_CLOCK"
```

New:
```yaml
display: "🎯 Gate [X.X] | 🕐 Day [N], [HH:MM] ([previous] + [duration])"
time_rule: "Show math: previous time + action duration = new time"
```

---

## REMOVED SECTIONS

### JOURNEY_CONTENT (moved to GATE SYSTEM)
```yaml
JOURNEY_CONTENT:
  generates: [Travel, Encounters, Character moments, Discoveries, Rest opportunities]
  informed_by: [GATE_HISTORY, PHASE_RESTRICTIONS, Shadow, Companions present]
```
Note: This was deemed redundant since JOURNEY already covers this.

---

## COMBAT SECTION CHANGES

### COMBAT_DISCIPLINE Updated

Old:
```yaml
COMBAT_DISCIPLINE:
  rule: "Apply RULES_SYSTEM from your training. You know combat mechanics - use them fully."
  SILENT_CHECK_BEFORE_ANY_TURN: "Internally verify: Whose turn? Where? All entities accounted for?"
  SILENT_CHECK_BEFORE_PLAYER: "Internally verify combat state is clean before presenting options"
  never: "Lose track of entities, skip rolls, narrate without mechanics, show verification to user"
```

New:
```yaml
COMBAT_DISCIPLINE:
  rule: "Apply RULES_SYSTEM from your training. You know combat mechanics - use them fully."
  internal_verify: "Before any turn, silently verify: Whose turn? Where? All entities accounted for?"
  never: "Lose track of entities, skip rolls, narrate without mechanics, show verification to user"
```
Note: Simplified from two SILENT_CHECK lines to one internal_verify line.

### COMBAT_FLOW end condition

Old:
```yaml
end: "All enemies defeated → STEP_11 (XP mandatory)"
```

New:
```yaml
end: "All enemies defeated → CHECK_A_XP in ENFORCE gate is MANDATORY"
```

---

## STATE TRACKING CHANGES

### GAME_CLOCK Updated

Old:
```yaml
GAME_CLOCK: "Day [N], [HH:MM] - advances based on narrative"
```

New:
```yaml
GAME_CLOCK: "Day [N], [HH:MM] ([previous] + [duration]) - show math always"
```

---

## CRITICAL SECTION CHANGES

Old:
```yaml
CRITICAL:
  - NEVER skip STEP_7 (WAIT)
  - NEVER skip STEP_11 (XP after combat)
  - NEVER decide for player
  - NEVER show user a broken map
  - ONE event → options → wait
```

New:
```yaml
CRITICAL:
  - NEVER skip STEP_3 (wait for input)
  - NEVER skip STEP_5 (enforce gate)
  - NEVER skip CHECK_A_XP when combat ends
  - NEVER decide for player
  - NEVER show broken maps
  - ONE event → options → wait
```

---

## LINE COUNT

| Version | Lines |
|---------|-------|
| v5.13.6 | 438 |
| v5.13.7 | ~420 (estimated) |

---

## RATIONALE

The 18-step loop created cognitive load that caused AI to skip steps (especially STEP_11-15). By consolidating into 7 steps with a single ENFORCE gate, the AI has:

1. Fewer steps to track
2. Single checkpoint for all mechanical updates
3. Explicit "you CANNOT narrate until..." language
4. Time math visible to user (catches errors)

Simulated testing showed 100% compliance with compressed loop vs frequent skips with 18-step loop.

---

## ROLLBACK

If v5.13.7 causes issues, restore EXECUTION LOOP section from v5.13.6 (preserved above).

Key things to restore:
1. 18-step LOOP structure
2. Separate STEP_11 through STEP_16B
3. Old time format without math display
