# VALIDATION SYSTEM - SEPARATION OF CONCERNS
**Created**: November 17, 2025

---

## THE TWO VALIDATION SYSTEMS

### 1. Runtime Validation (In Agent Orchestrator)
**WHO USES IT**: Players running campaigns  
**WHEN**: Every time a campaign loads  
**PURPOSE**: Ensure campaign can run without crashing  
**SCOPE**: Minimal - only critical checks  

### 2. Development Validation (Campaign Validator Tool)
**WHO USES IT**: You (campaign designer)  
**WHEN**: During campaign development, before release  
**PURPOSE**: Catch all design errors, balance issues, quality problems  
**SCOPE**: Comprehensive - every possible check  

---

## WHY SEPARATE THEM?

### Problem with Single Validation System:

**If agent does deep validation at runtime**:
- ❌ Slow campaign loading (players wait)
- ❌ Players see technical errors they can't fix
- ❌ Agent crashes on issues players can't resolve
- ❌ Confusing for players ("What's a broken reference?")

**If agent does minimal validation**:
- ❌ Campaigns with errors reach players
- ❌ Features silently fail
- ❌ Designer doesn't know about problems
- ❌ Players have bad experience

### Solution: Two-Stage Validation

```
┌─────────────────────────────────────────┐
│  DEVELOPMENT TIME (You)                 │
├─────────────────────────────────────────┤
│                                         │
│  1. Create campaign module              │
│  2. Run CAMPAIGN_VALIDATOR (standalone) │
│  3. Get detailed report                 │
│  4. Fix all issues                      │
│  5. Validate again until clean          │
│  6. Campaign ready for release          │
│                                         │
└─────────────────────────────────────────┘
                  │
                  │ Campaign passes validation
                  ▼
┌─────────────────────────────────────────┐
│  RUNTIME (Players)                      │
├─────────────────────────────────────────┤
│                                         │
│  1. Player loads campaign               │
│  2. Agent does minimal validation       │
│  3. Campaign loads quickly              │
│  4. Everything works (already tested)   │
│  5. Player has good experience          │
│                                         │
└─────────────────────────────────────────┘
```

---

## WHAT EACH SYSTEM CHECKS

### Runtime Validation (Agent Orchestrator)

**ONLY CHECKS**:
✓ File can be parsed (valid YAML/Markdown)
✓ Required sections exist (metadata, quests, locations)
✓ Basic schema structure is correct
✓ Can build indexes (quest_id, location_id, etc.)

**Result**: PASS or FAIL (with generic error message)

**Example Output**:
```
Loading campaign: Dragon of Icespire Peak
✓ Schema valid
✓ Core data indexed
✓ Relationships enabled
✓ Objects enabled
Campaign loaded successfully.
```

**If fails**:
```
ERROR: Invalid campaign module format. 
Campaign may not have been validated.
Please contact campaign designer.
```

**Takes**: < 1 second

---

### Development Validation (Campaign Validator Tool)

**CHECKS EVERYTHING**:
✓ Schema structure (like runtime)
✓ All references are valid
✓ No orphaned content
✓ No circular dependencies
✓ Balance issues (XP, CR, treasure)
✓ Quest completeness
✓ NPC personalities exist
✓ Monster stats present
✓ Quest relationships are logical
✓ Interactable objects are balanced
✓ DCs are appropriate for level
✓ Damage is reasonable
✓ Descriptions are complete
✓ Best practices followed

**Result**: Detailed report with:
- Issue severity (Critical/Error/Warning/Info)
- Specific location of each issue
- How to fix it
- Quality score
- Statistics
- Recommendations

**Example Output**:
```
CAMPAIGN VALIDATION REPORT
Campaign: Dragon of Icespire Peak
Status: PASS WITH WARNINGS

Issue Counts:
- CRITICAL: 0
- ERROR: 0
- WARNING: 3
- INFO: 5

Warnings:
⚠️ Quest "mountains_toe_mine" has high XP for level range
   Location: quests[5].rewards.xp_total
   Current: 1200 XP
   Suggestion: Consider reducing to 800-900 XP to prevent overleveling

⚠️ NPC "tibor_wester" has minimal personality
   Location: npcs[8]
   Issue: Only one personality trait defined
   Suggestion: Add ideals, bonds, and flaws for richer roleplay

⚠️ Object "half_cut_tree" deals high damage
   Location: loggers_camp.interactable_objects[0]
   Damage: 3d6 (avg 10.5)
   Suggestion: May one-shot enemies - consider 2d6 instead

QUALITY SCORE: 87/100
DEPLOYMENT READINESS: ✅ Ready (review warnings)
```

**Takes**: 5-10 seconds

---

## YOUR WORKFLOW

### Phase 1: Create Campaign
```
1. Use ORCHESTRATOR_CAMPAIGN_TEMPLATE.md as guide
2. Write CAMPAIGN_your_adventure.md
3. Add quests, NPCs, locations, relationships, objects
```

### Phase 2: Validate Campaign (USE THE VALIDATOR)
```
1. Run: campaign_validator CAMPAIGN_your_adventure.md
2. Read validation report
3. Fix CRITICAL issues (campaign won't load)
4. Fix ERROR issues (features won't work)
5. Review WARNING issues (quality/balance)
6. Consider INFO suggestions (best practices)
7. Re-run validator
8. Repeat until clean
```

### Phase 3: Deploy to Players
```
1. Campaign passes validation
2. Players load ORCHESTRATOR_CORE_DND5E_AGENT.md
3. Players load CAMPAIGN_your_adventure.md
4. Agent does quick runtime validation (passes instantly)
5. Players start playing
6. Everything works because you validated it
```

---

## COMPARISON TABLE

| Aspect | Runtime Validation | Development Validation |
|--------|-------------------|----------------------|
| **Used By** | Players | Campaign Designer (You) |
| **When** | Every campaign load | During development |
| **Speed** | < 1 second | 5-10 seconds |
| **Scope** | Minimal | Comprehensive |
| **Output** | Pass/Fail | Detailed Report |
| **Purpose** | Prevent crashes | Ensure quality |
| **Errors Shown** | Generic | Specific + Fixes |
| **Location** | In agent orchestrator | Standalone tool |

---

## ANALOGY

Think of it like software development:

**Runtime Validation** = Loading a compiled program
- Quick check: "Can this run?"
- Just loads and starts
- Assumes it was tested

**Development Validation** = Compiler + Linter + Tests
- Comprehensive: "Is this code good?"
- Finds bugs, style issues, performance problems
- Runs before release

You wouldn't make users run your full test suite every time they start your app!

---

## FILE STRUCTURE

```
your-dnd-system/
├── ORCHESTRATOR_CORE_DND5E_AGENT.md
│   └── Contains: Minimal runtime validation
│
├── CAMPAIGN_VALIDATOR_TOOL.md
│   └── Contains: Comprehensive dev validation
│
├── campaigns/
│   ├── CAMPAIGN_dragon_of_icespire_peak.md
│   ├── CAMPAIGN_storm_lords_wrath.md
│   └── CAMPAIGN_your_custom_adventure.md
│
└── validation_reports/
    ├── dragon_of_icespire_peak_report.md
    └── your_custom_adventure_report.md
```

---

## COMMAND-LINE USAGE (Conceptual)

### Development (You):
```bash
# Validate your campaign
$ campaign_validator CAMPAIGN_my_adventure.md --strict

# Quick check after fixes
$ campaign_validator CAMPAIGN_my_adventure.md --quick

# Just check balance
$ campaign_validator CAMPAIGN_my_adventure.md --balance-only

# Output to different format
$ campaign_validator CAMPAIGN_my_adventure.md --report-format html
```

### Runtime (Players):
```
# They just load the campaign
Player: "Load Dragon of Icespire Peak campaign"
Agent: [Runs minimal validation automatically]
Agent: "Campaign loaded successfully. Ready to begin!"
```

---

## WHAT THIS MEANS FOR YOU

### Before Each Campaign Release:

1. **Create** campaign using template
2. **Validate** using Campaign Validator tool (standalone)
3. **Fix** all critical and error issues
4. **Review** warnings and improve quality
5. **Re-validate** until report is clean
6. **Release** to players with confidence

### What Players Experience:

1. **Load** campaign (fast, no errors)
2. **Play** campaign (everything works)
3. **Enjoy** quality content (because you validated it)

---

## IMPLEMENTATION OPTIONS

The Campaign Validator can be:

### Option 1: Python Script
```python
python campaign_validator.py CAMPAIGN_file.md --strict
```

### Option 2: Web Tool
```
http://localhost:8000/validate
[Upload campaign file]
[Get HTML report]
```

### Option 3: IDE Extension
```
VS Code extension that validates on save
Shows errors inline in editor
```

### Option 4: CI/CD Integration
```yaml
GitHub Action that validates on commit
Blocks PR if validation fails
```

**Recommendation**: Start with Python script (simplest)

---

## NEXT STEPS

### Immediate:
1. ✅ Runtime validation updated (done)
2. ✅ Validator tool documented (done)
3. ⏳ Implement validator (Python script or other)
4. ⏳ Test on Dragon of Icespire Peak campaign

### Future:
- Add more validation rules as you discover issues
- Build web UI for easier use
- Integrate into your workflow
- Share with other campaign designers

---

## KEY TAKEAWAY

**Two validation systems, two purposes:**

**Campaign Validator** = Your development tool
- Run it while building campaigns
- Catches everything
- Helps you create quality content

**Agent Runtime Validation** = Player protection
- Runs automatically when loading
- Fast and minimal
- Assumes you already validated

**Keep them separate. Players never see the validator. You use it for every campaign.**

---

**Files**:
- [ORCHESTRATOR_CORE_DND5E_AGENT.md](computer:///mnt/user-data/outputs/ORCHESTRATOR_CORE_DND5E_AGENT.md) - Updated with minimal runtime validation
- [CAMPAIGN_VALIDATOR_TOOL.md](computer:///mnt/user-data/outputs/CAMPAIGN_VALIDATOR_TOOL.md) - Standalone validator documentation

---
