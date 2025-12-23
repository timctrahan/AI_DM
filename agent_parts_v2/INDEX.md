# D&D 5E AI Orchestrator V2 - Complete File Index

## Quick Navigation

| Document | Purpose | When to Read |
|----------|---------|--------------|
| **README.md** | User-facing guide, quick start | START HERE |
| **V2_SUMMARY.md** | High-level overview, design rationale | Understand the "why" |
| **V2_ARCHITECTURE_DESIGN.md** | Technical specification | Building/extending |
| **MIGRATION_GUIDE_V1_TO_V2.md** | V1→V2 transition guide | Existing V1 users |
| **EXAMPLE_Campaign_Data_Vault.md** | Vault format demonstration | Creating vaults |

---

## Directory Structure

```
agent_parts_v2/
│
├── INDEX.md                              ← You are here
├── README.md                             ← Start here for usage
├── V2_SUMMARY.md                         ← High-level overview
├── V2_ARCHITECTURE_DESIGN.md             ← Technical deep-dive
├── MIGRATION_GUIDE_V1_TO_V2.md           ← V1 to V2 transition
├── EXAMPLE_Campaign_Data_Vault.md        ← Vault format example
│
├── KERNEL/
│   └── IMMUTABLE_KERNEL.md               ← System prompt content (~1KB)
│       • Core laws (Player Agency, Mechanical Integrity, Context Fidelity)
│       • Execution Loop (mandatory steps for every input)
│       • Internal_Context_Retrieval Protocol
│       • Checkpoint_Validation Protocol
│       • Degradation Detection
│       • Session Resume Safeguard
│
├── PROTOCOL_LIBRARY/
│   ├── PART1_Session_Management.md       ← Session init, character creation, resume
│   │   Protocols: proto_session_init, proto_new_session_flow,
│   │              proto_character_creation_flow, proto_session_resume,
│   │              proto_character_import_flow, proto_game_start,
│   │              proto_state_validation, proto_state_recovery
│   │
│   ├── PART2_Game_Loop.md                ⏳ NOT YET CREATED
│   │   Needed: proto_game_loop, proto_exploration, proto_movement,
│   │           proto_investigation, proto_npc_interaction, proto_shopping
│   │
│   ├── PART3_Combat.md                   ⏳ NOT YET CREATED
│   │   Needed: proto_combat_init, proto_combat_round, proto_attack_action,
│   │           proto_death_saves, proto_combat_end
│   │
│   ├── PART4_Progression.md              ⏳ NOT YET CREATED
│   │   Needed: proto_xp_award, proto_level_up, proto_quest_completion,
│   │           proto_loot_distribution, proto_reputation
│   │
│   └── PART5_Utilities.md                ⏳ NOT YET CREATED
│       Needed: proto_rest_short, proto_rest_long, proto_inventory,
│               proto_spell_management, proto_condition_tracking
│
├── SCHEMAS/                              ⏳ NOT YET CREATED
│   ├── Character_Schema_v2.md            ← Character data structure
│   ├── Party_State_Schema_v2.md          ← Party data structure
│   └── Campaign_Module_Schema_v2.md      ← Module format spec
│
└── TOOLS/
    ├── assemble_protocol_library.py      ← Assembles PART1-5 → PROTOCOL_LIBRARY_v{ver}.md
    ├── create_campaign_vault.py          ← Converts campaign.md → vault format
    └── version_v2.json                   ⏳ Created by assembly script
```

---

## File Descriptions

### Core Documentation

#### README.md (10 KB)
**Purpose**: Primary user documentation
**Contents**:
- What's new in V2 vs V1
- Architecture overview (three-layer diagram)
- Quick start guide (3 steps to run a session)
- How Internal_Context_Retrieval works
- Checkpoint system explanation
- Campaign Data Vault format
- File size targets
- Working memory cache
- Benefits summary
- Tools reference
- Troubleshooting
- Best practices
- Roadmap

**Read this if**: You want to use V2 (not build it)

---

#### V2_SUMMARY.md (5 KB)
**Purpose**: Executive summary for stakeholders
**Contents**:
- What was built (high-level)
- The core problem from Gemini conversation
- The V2 solution (three layers)
- How it works (simplified)
- Files created
- What still needs implementation
- Testing plan
- Key innovations
- Expected performance
- Design philosophy
- Comparison table (V1 vs V2)
- Next steps
- Success criteria

**Read this if**: You need to understand V2 in 5 minutes

---

#### V2_ARCHITECTURE_DESIGN.md (15 KB)
**Purpose**: Technical specification and design rationale
**Contents**:
- Executive summary
- Core problem statement
- V2 solution (detailed three-layer architecture)
- Layer 1: Immutable Kernel (full spec)
- Layer 2: Protocol Library (structure)
- Layer 3: Campaign Data Vault (format)
- How this solves context drift (examples)
- Session initialization flow
- Benefits over V1 (detailed table)
- File structure for V2
- Migration path from V1
- Next steps

**Read this if**: You're implementing V2 or extending it

---

#### MIGRATION_GUIDE_V1_TO_V2.md (8 KB)
**Purpose**: Step-by-step guide for V1 users to transition
**Contents**:
- Should you migrate? (decision tree)
- Three migration paths:
  - Path A: Fresh Start (recommended)
  - Path B: Session Resume (preserve state)
  - Path C: Hybrid (parallel testing)
- Step-by-step instructions for each path
- Common migration issues & fixes
- Verification checklist
- Rollback plan (if migration fails)
- Side-by-side comparison
- Performance expectations
- FAQ
- Success stories

**Read this if**: You have an existing V1 campaign

---

#### EXAMPLE_Campaign_Data_Vault.md (8 KB)
**Purpose**: Demonstrates vault format with real content
**Contents**:
- Master index example
- Act 2 overview module
- Campaign intro module
- Location module (Main Street)
- NPC module (Zilvra Shadowveil - detailed)
- Quest module (Three Fragments - detailed)
- Shows all indexing conventions
- Shows module wrapping format
- Includes flags, reputation, quest structure

**Read this if**: You're creating a campaign vault

---

### Core Components

#### KERNEL/IMMUTABLE_KERNEL.md (3 KB)
**Purpose**: The "BIOS" - unforgettable core logic
**Contains**:
- Section 0: Immutable Laws (Player Agency, Mechanical Integrity, Context Fidelity)
- Section 1: The Execution Loop (8 mandatory steps)
- Section 2: Internal_Context_Retrieval Protocol (full implementation)
- Section 3: Checkpoint_Validation Protocol (self-auditing)
- Section 4: Correction Protocol (auto-fix violations)
- Section 5: Degradation Detection (warning signs)
- Section 6: Session Resume Safeguard
- Section 7: Working Memory Cache (performance)
- Section 8: Failure Modes (honest errors)
- Section 9: Kernel Integrity Verification
- Section 10: Glossary

**Placement**: System prompt (NOT conversation)
**Why it works**: AI cannot forget system prompt

---

#### PROTOCOL_LIBRARY/PART1_Session_Management.md (6 KB)
**Purpose**: Session lifecycle protocols
**Contains** (8 protocols):
1. `proto_session_init` - Bootstrap session, load components
2. `proto_new_session_flow` - Create party from scratch
3. `proto_character_creation_flow` - Create single character
4. `proto_session_resume` - Load existing party state
5. `proto_character_import_flow` - Import pre-made characters
6. `proto_game_start` - Load campaign intro, begin exploration
7. `proto_state_validation` - Verify party state integrity
8. `proto_state_recovery` - Auto-correct state corruption

**Format**: Each protocol wrapped with `[PROTOCOL_START: id]` and `[PROTOCOL_END: id]`
**Status**: ✅ Complete

---

#### PROTOCOL_LIBRARY/PART2-5_*.md
**Status**: ⏳ NOT YET CREATED

**Part 2: Game Loop**
- proto_game_loop (main loop with checkpoint)
- proto_exploration (list actions, present options)
- proto_movement (travel between locations)
- proto_investigation (search, perception checks)
- proto_npc_interaction (**CRITICAL**: calls Internal_Context_Retrieval)
- proto_shopping (merchant interactions, purchases)
- proto_rest_short, proto_rest_long

**Part 3: Combat**
- proto_combat_init (roll initiative, set up encounter)
- proto_combat_round (turn order, status effects)
- proto_attack_action (attack rolls, damage)
- proto_death_saves (0 HP handling)
- proto_combat_end (XP awards, loot)

**Part 4: Progression**
- proto_xp_award (immediate XP distribution)
- proto_level_up (level-up flow)
- proto_quest_completion (quest rewards)
- proto_loot_distribution (treasure division)
- proto_reputation (faction standing)

**Part 5: Utilities**
- proto_inventory (add/remove items)
- proto_spell_management (spell slots, known spells)
- proto_condition_tracking (poisoned, frightened, etc.)
- proto_encumbrance (carrying capacity)

**Source**: Can be ported from V1's `agent_parts/DND_ORCH_PART3-6_*.md` files
**Required changes**:
1. Wrap each protocol with `[PROTOCOL_START/END]` tags
2. Add Internal_Context_Retrieval calls for NPCs/locations/quests
3. Update to reference Kernel's Execution Loop

---

### Tools

#### TOOLS/assemble_protocol_library.py (3 KB)
**Purpose**: Assembles modular parts into indexed library
**Usage**:
```bash
python assemble_protocol_library.py [output_filename]
```
**Features**:
- Reads PART1-5 files
- Auto-generates `[PROTOCOL_INDEX]` from found protocols
- Automatic versioning:
  - 0-1 files changed → patch (2.0.0 → 2.0.1)
  - 2-3 files changed → minor (2.0.0 → 2.1.0)
  - 4-5 files changed → major (2.0.0 → 3.0.0)
- Tracks version in `version_v2.json`
- Outputs statistics (size, protocol count)
- Verification commands

**Output**: `../../PROTOCOL_LIBRARY_v{version}.md`

---

#### TOOLS/create_campaign_vault.py (4 KB)
**Purpose**: Converts campaign markdown to indexed vault
**Usage**:
```bash
python create_campaign_vault.py <input.md> [output.md]
```
**Features**:
- Auto-categorization (NPCs, locations, quests, encounters)
- Normalizes module IDs (e.g., "Zilvra Shadowveil" → "npc_zilvra_shadowveil")
- Wraps content with `[MODULE_START/END]` tags
- Generates `[MASTER_INDEX]`
- Flags uncategorized sections for manual review
- Outputs statistics (size, module count)

**Output**: `{campaign_name}_Data_Vault.md`

---

## What's Complete vs What's Needed

### ✅ Complete (Ready to Use)

| Component | File | Size | Status |
|-----------|------|------|--------|
| Architecture | V2_ARCHITECTURE_DESIGN.md | 15 KB | ✅ |
| Kernel | KERNEL/IMMUTABLE_KERNEL.md | 3 KB | ✅ |
| Session Mgmt | PART1_Session_Management.md | 6 KB | ✅ |
| Vault Example | EXAMPLE_Campaign_Data_Vault.md | 8 KB | ✅ |
| Assembly Tool | assemble_protocol_library.py | 3 KB | ✅ |
| Vault Tool | create_campaign_vault.py | 4 KB | ✅ |
| User Docs | README.md | 10 KB | ✅ |
| Migration Guide | MIGRATION_GUIDE_V1_TO_V2.md | 8 KB | ✅ |
| Summary | V2_SUMMARY.md | 5 KB | ✅ |

**Total**: ~60 KB of documentation and ~7 KB of tools

---

### ⏳ Needed for Production

| Component | Estimated Effort | Source |
|-----------|------------------|--------|
| PART2_Game_Loop.md | 2-3 hours | Port from V1 PART3 |
| PART3_Combat.md | 2 hours | Port from V1 PART4 |
| PART4_Progression.md | 2 hours | Port from V1 PART5 |
| PART5_Utilities.md | 1 hour | Port from V1 PART3 |
| Character_Schema_v2.md | 30 mins | Copy from V1 PART1 |
| Party_State_Schema_v2.md | 30 mins | Copy from V1 PART1 |
| Campaign_Module_Schema_v2.md | 1 hour | New (define vault module structure) |
| Full Act 2 Vault | 3-4 hours | Run tool + manual review |

**Total estimated**: 12-15 hours to complete V2.0.0

---

## Usage Workflows

### Workflow 1: Start Fresh V2 Session

```bash
# 1. Assemble Protocol Library
cd agent_parts_v2/TOOLS
python assemble_protocol_library.py

# 2. Create Campaign Vault
python create_campaign_vault.py "../../campaigns/Act_2_The_Dead_City.md"

# 3. Paste to AI (in order):
# - KERNEL/IMMUTABLE_KERNEL.md (system prompt)
# - PROTOCOL_LIBRARY_v2.0.0.md (user message)
# - Act_2_The_Dead_City_Data_Vault.md (user message)
# - "Initialize session and create party"
```

---

### Workflow 2: Migrate V1 Campaign

```bash
# 1. Save V1 party state
# (In V1 session): "End session and save party"
# Save output JSON

# 2. Assemble V2 components
cd agent_parts_v2/TOOLS
python assemble_protocol_library.py
python create_campaign_vault.py "../../campaigns/Act_2.md"

# 3. Resume in V2
# Paste: Kernel, Protocol Library, Campaign Vault
# Then: "Resume session: [paste V1 party JSON]"
```

---

### Workflow 3: Modify Protocols

```bash
# 1. Edit specific part file
# Example: PROTOCOL_LIBRARY/PART1_Session_Management.md

# 2. Reassemble library
python assemble_protocol_library.py
# Version auto-increments (e.g., 2.0.0 → 2.0.1)

# 3. Reload in session
# (Paste updated PROTOCOL_LIBRARY_v2.0.1.md)
```

---

### Workflow 4: Add New Campaign Content

```bash
# 1. Edit vault file
# Example: Act_2_Data_Vault.md
# Add new [MODULE_START: npc_new_character] section
# Update [MASTER_INDEX]

# 2. Reload vault in session
# (Paste updated vault)

# Or: For new session, just use updated vault
```

---

## Testing Checklist

Before considering V2 production-ready:

### Component Tests
- [ ] Kernel loads in system prompt
- [ ] Protocol Library assembles without errors
- [ ] Campaign Vault generator creates valid vault
- [ ] All modules in vault are retrievable

### Integration Tests
- [ ] Session initialization works (new party)
- [ ] Session resume works (V1 party import)
- [ ] NPC interaction retrieves correct module
- [ ] Location movement retrieves correct module
- [ ] Quest tracking retrieves correct module

### Reliability Tests
- [ ] Checkpoint triggers every 5 turns
- [ ] Checkpoint catches STOP violations
- [ ] Checkpoint catches XP tracking failures
- [ ] Checkpoint catches missing context retrieval
- [ ] Correction Protocol fixes violations

### Consistency Tests
- [ ] Same NPC dialogue consistent across 100 turns
- [ ] Quest details don't degrade over 100 turns
- [ ] Location descriptions don't degrade over 100 turns

### Stress Tests
- [ ] 200-turn session without context drift
- [ ] 500-turn session (approach context window limit)
- [ ] Multiple NPCs interacted with in same session
- [ ] Complex multi-step quest tracked accurately

---

## Roadmap to V2.0.0 Release

### Phase 1: Complete Core Components (Week 1)
- [ ] Write PART2_Game_Loop.md
- [ ] Write PART3_Combat.md
- [ ] Write PART4_Progression.md
- [ ] Write PART5_Utilities.md
- [ ] Port schemas from V1

### Phase 2: Create Full Example (Week 2)
- [ ] Generate complete Act 2 vault (45+ modules)
- [ ] Review and refine auto-generated content
- [ ] Manually add missing modules
- [ ] Verify all module IDs in index

### Phase 3: Integration Testing (Week 3)
- [ ] Run component tests
- [ ] Run full session test (new party)
- [ ] Run migration test (V1 → V2)
- [ ] Run stress test (200 turns)
- [ ] Document any issues found

### Phase 4: Refinement (Week 4)
- [ ] Fix issues from testing
- [ ] Refine documentation based on test findings
- [ ] Create video tutorial
- [ ] Create quick-start template

### Phase 5: Release
- [ ] Tag V2.0.0 in git
- [ ] Publish release notes
- [ ] Share with community
- [ ] Gather feedback

---

## Quick Reference: Key Files

**To understand V2**: Read `README.md` then `V2_SUMMARY.md`

**To use V2**: Follow quick start in `README.md`

**To migrate from V1**: Follow `MIGRATION_GUIDE_V1_TO_V2.md`

**To build V2**: Read `V2_ARCHITECTURE_DESIGN.md`

**To create a vault**: Use `create_campaign_vault.py` and see `EXAMPLE_Campaign_Data_Vault.md`

**To modify protocols**: Edit `PROTOCOL_LIBRARY/PART*.md` and run `assemble_protocol_library.py`

---

## Contact & Contributions

**Issues**: Document in GitHub issues with:
- File involved
- Expected behavior
- Actual behavior
- Steps to reproduce

**Contributions**: Submit PRs for:
- New protocols
- Campaign vaults
- Tool improvements
- Documentation clarifications

---

**Last Updated**: 2025-12-19
**Version**: 2.0.0-alpha
**Status**: Architecture complete, partial implementation, needs Protocol Library parts 2-5
