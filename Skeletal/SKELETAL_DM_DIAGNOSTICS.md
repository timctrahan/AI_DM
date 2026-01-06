# SKELETAL DM DIAGNOSTIC COMMANDS

```yaml
VALIDATION:
  type: "diagnostics"
  version: "1.0"
  echo: "✅ DIAGNOSTICS: Skeletal DM Diagnostic Commands v1.0 | Status: READY"
```

---

## /validate

```yaml
VALIDATE_COMMAND:
  purpose: "Verify all files loaded correctly"
  output: |
    ═══════════════════════════════════════
    📋 FILE VALIDATION
    ═══════════════════════════════════════
    KERNEL: [Echo VALIDATION block]
    CAMPAIGN CORE: [Echo VALIDATION block]
    ACT FILE: [Echo VALIDATION block]
    SAVE FILE: [If present]
    ENCODING TEST: ⚠️ ⛔ ⭐ 💎 🎲 → 🌑 🌫️ ⬛ ⬜ 🥷 🐆
    ═══════════════════════════════════════
    RESULT: [ALL VALID / ISSUES FOUND]
```

---

## /calibrate

```yaml
CALIBRATE_COMMAND:
  purpose: "System self-check for rule compliance"
  checks: [rules, xp, source, gates, agency, combat, output, variables]
  output: |
    ═══════════════════════════════════════
    🔧 CALIBRATION
    ═══════════════════════════════════════
    ✅ Rules: D&D 5e active
    ✅ XP: CR-based, awarded after combat
    ✅ Gates: [current] | sequential
    ✅ Agency: wait cycle enforced
    ═══════════════════════════════════════
```

---

## /debug

```yaml
DEBUG_COMMAND:
  purpose: "Analyze what went wrong"
  output: |
    ═══════════════════════════════════════
    🐛 DEBUG ANALYSIS
    ═══════════════════════════════════════
    WHAT HAPPENED: [description]
    WHY: [root cause]
    CURRENT STATE: [relevant state]
    ═══════════════════════════════════════
  ends_with: "What do you do? ⛔"
```

---

**END DIAGNOSTICS v1.0**
