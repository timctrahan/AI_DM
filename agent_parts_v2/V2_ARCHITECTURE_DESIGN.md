# D&D 5E Orchestrator V2 Architecture Design

## Executive Summary

This document defines the V2 architecture for the D&D 5E AI Orchestrator, designed to eliminate context drift and ensure mechanical integrity across long play sessions.

## Core Problem Statement

**Current V1 Issues**:
1. **Context Decay**: AI forgets campaign details, NPC personalities, quest objectives as conversation grows
2. **Protocol Drift**: AI may forget to follow its own protocols (STOP and WAIT, XP tracking, etc.)
3. **No Forced Memory Access**: AI relies on vague memory instead of re-reading authoritative sources
4. **User Friction**: Players must manually paste campaign data when AI loses context

**Root Cause**: The AI treats all text equally - core operating rules sit alongside campaign flavor text, and both degrade over time in the conversation history.

## V2 Solution: Three-Layered Defense System

### Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 1: IMMUTABLE KERNEL (System Prompt)              │
│  - Player Agency Law                                     │
│  - Execution Loop Definition                            │
│  - Internal_Context_Retrieval Protocol                  │
│  - Checkpoint Protocol                                  │
│  Size: <1000 tokens | Priority: MAXIMUM                 │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  LAYER 2: PROTOCOL LIBRARY (User Message)               │
│  - All gameplay protocols (Combat, Exploration, etc.)   │
│  - Indexed by protocol_id                               │
│  - Retrieved on-demand by Kernel                        │
│  Size: ~40KB | Priority: HIGH                           │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│  LAYER 3: CAMPAIGN DATA VAULT (User Message)            │
│  - All campaign content (NPCs, locations, quests)       │
│  - Indexed by module_id                                 │
│  - Retrieved on-demand by protocols                     │
│  Size: Variable (10-50KB per act) | Priority: MEDIUM    │
└─────────────────────────────────────────────────────────┘
```

## Layer 1: The Immutable Kernel

**Location**: System Prompt (highest priority context)

**Purpose**: The "BIOS" that bootstraps all other logic. This cannot be forgotten because it IS the AI's operating instructions.

**Contents** (~5KB machine-readable YAML):

### 1. Immutable Laws
```yaml
PLAYER_AGENCY_LAW:
  ALWAYS: present_options, end_with_question, STOP, WAIT_for_input
  NEVER: decide_for_player, move_without_consent, assume_intent

MECHANICAL_INTEGRITY_LAW:
  ALL_XP: award_immediately, use_mandatory_format
  ALL_GOLD: track_every_transaction, no_negatives
  ALL_STATE: validate_before_after
```

### 2. The Execution Loop (Mandatory Process)
```yaml
EXECUTION_LOOP:
  # This loop runs for EVERY player input
  1. AWAIT_INPUT: from player
  2. PARSE_INPUT: extract action_type and target_entity
  3. MANDATORY_CONTEXT_RETRIEVAL:
     a. IDENTIFY: Does this action involve an indexed entity?
        - NPC name? → RETRIEVE: npc_[name]
        - Location? → RETRIEVE: loc_[location_id]
        - Quest? → RETRIEVE: quest_[quest_id]
        - Protocol? → RETRIEVE: protocol_[protocol_name]
     b. EXECUTE: Internal_Context_Retrieval_Protocol
     c. LOAD: Fresh data from index into working_memory
  4. EXECUTE_ACTION: Using ONLY the freshly loaded context
  5. UPDATE_STATE: Track all changes (HP, gold, XP, flags)
  6. NARRATE_OUTCOME: Generate player-facing description
  7. PRESENT_OPTIONS: With mechanics clearly stated
  8. STOP_AND_WAIT: ⛔ Mandatory wait for input
  9. LOOP: Return to step 1

# CRITICAL: Steps 3-8 are INSEPARABLE. Cannot execute without context retrieval.
```

### 3. Internal_Context_Retrieval Protocol
```yaml
PROTOCOL: Internal_Context_Retrieval

INPUT: module_id (e.g., "npc_zilvra_shadowveil")

PROCEDURE:
  1. CHECK_WORKING_MEMORY:
     - Is module_id in last_5_accessed_modules?
     - If YES: Use cached version (fast path)
     - If NO: Proceed to step 2

  2. SEARCH_CONVERSATION_HISTORY:
     - Look for: "[MODULE_START: {module_id}]"
     - Extract all text until: "[MODULE_END: {module_id}]"
     - If NOT FOUND: Escalate to CRITICAL_ERROR (see Layer 3 failure mode)

  3. FOCUS_ATTENTION:
     - Treat extracted text as SOLE source of truth
     - Ignore any vague memories from earlier in conversation
     - This is the HIGH-FIDELITY authoritative data

  4. UPDATE_WORKING_MEMORY:
     - Add module_id to working_memory_cache
     - Push out oldest entry if cache > 5 modules
     - Log: "Retrieved: {module_id}" (for checkpoint audit)

  5. RETURN: extracted_module_data

FAILURE_MODE:
  IF module_id not found in conversation:
    OUTPUT: "⛔ CRITICAL ERROR: Module '{module_id}' not found in Data Vault."
    OUTPUT: "Please verify Campaign Data Vault is loaded."
    HALT_EXECUTION
```

### 4. Checkpoint Validation Protocol
```yaml
PROTOCOL: Checkpoint_Validation

TRIGGER: Every 5 player inputs (in main game loop)

PROCEDURE:
  1. VERIFY_LAST_5_TURNS:
     - Player Agency: Did I STOP and WAIT every turn?
     - Gold Tracking: Are all transactions logged?
     - XP Awards: Are all combat XP distributed?
     - Context Retrieval: Do logs show retrieval for all indexed entities?

  2. CHECK_RETRIEVAL_LOGS:
     FOR EACH of last_5_turns:
       IF turn involved NPC/Location/Quest:
         VERIFY: "Retrieved: {module_id}" log exists
         IF MISSING:
           FAIL: context_retrieval_honored = false

  3. IF ANY VERIFICATION FAILS:
     OUTPUT: "⚠️ SYSTEM INTEGRITY FAULT"
     OUTPUT: "I failed protocol: {failed_check_name}"
     OUTPUT: "Correcting now..."
     CALL: Correction_Protocol
     REPROCESS: Last turn with proper protocol adherence

  4. IF ALL PASS:
     SILENT: Continue (no need to announce success)
```

## Layer 2: Protocol Library

**Location**: First user message (loaded once per session)

**Purpose**: Contains ALL gameplay logic protocols, but in indexed, retrievable chunks

**Format**:
```markdown
# PROTOCOL LIBRARY v2.0

[PROTOCOL_INDEX]
- session_management:
  - proto_session_init
  - proto_character_creation
  - proto_session_resume
- game_loop:
  - proto_exploration
  - proto_movement
  - proto_investigation
  - proto_npc_interaction
  - proto_shopping
  - proto_rest_short
  - proto_rest_long
- combat:
  - proto_combat_init
  - proto_combat_round
  - proto_attack_action
  - proto_death_saves
  - proto_combat_end
- progression:
  - proto_xp_award
  - proto_level_up
  - proto_quest_completion

---

[PROTOCOL_START: proto_exploration]
## PROTOCOL: Exploration_Protocol

**TRIGGER**: Not in combat
**GUARD**: not_in_combat AND party_conscious

**PROCEDURE**:
```yaml
... (full protocol content)
```
[PROTOCOL_END: proto_exploration]

---

[PROTOCOL_START: proto_npc_interaction]
## PROTOCOL: NPC_Interaction_Protocol

**TRIGGER**: Player chooses to interact with NPC
**GUARD**: npc_exists AND npc_available

**PROCEDURE**:
```yaml
1. MANDATORY_CONTEXT_CHECK:
   - CALL: Internal_Context_Retrieval WITH npc_id
   - LOAD: npc.personality, npc.goals, npc.relationship_to_party

2. GENERATE_DIALOGUE:
   - Use ONLY freshly loaded NPC data
   - Match personality traits from module
   - Reference current quest/reputation flags

... (rest of protocol)
```
[PROTOCOL_END: proto_npc_interaction]

---
... (continues for all ~40 protocols)
```

**Key Insight**: The Kernel knows HOW to load protocols. The Protocol Library is WHAT to load. The Kernel can't forget how to load because it IS the system prompt.

## Layer 3: Campaign Data Vault

**Location**: Second user message (loaded once per act/session)

**Purpose**: Contains all campaign-specific content (NPCs, locations, quests, loot)

**Format**:
```markdown
# CAMPAIGN DATA VAULT: Act 2 - The Dead City

[MASTER_INDEX]
- overview: _act2_overview
- main_quests:
  - quest_mq1_mapping_the_dead
  - quest_mq2_three_fragments
  - quest_mq3_hunters_in_dark
  - quest_mq4_outer_sanctum
- side_quests:
  - quest_sq1_architects_map
  - quest_sq2_volunteers_plea
  - quest_sq3_bone_market
  ... (all 7 side quests)
- locations:
  - loc_main_street
  - loc_artisan_quarter
  - loc_temple_district
  - loc_noble_estates
  - loc_vault_antechamber
  - loc_vault_outer_sanctum
- npcs:
  - npc_zilvra_shadowveil
  - npc_xalaphex_aberrant_devourer
  - npc_durin_warden_ghost
  - npc_thalgrim_ghost
  - npc_velryn_act2
  ... (all NPCs)
- companions:
  - companion_velryn_act2
- encounters:
  - enc_undead_patrol
  - enc_helmed_horrors
  - enc_drow_ambush
  ... (all encounters)

---

[MODULE_START: _act2_overview]
### ACT 2: THE DEAD CITY - OVERVIEW

**Tone**: moral_corruption, choosing_lesser_evils, oppressive_isolation

**Core Themes**:
- Every choice has a cost
- Desperation drives normally good people to evil acts
- The past's sins haunt the present

**Victory Conditions**:
1. Obtain all three key fragments
2. Gain access to Vault Outer Sanctum
3. Survive the moral corruption of the Dead City

**Defeat Conditions**:
1. TPK (total party kill)
2. Velryn captured and not rescued within 3 in-game days
3. Party succumbs to madness (all members reach 5+ exhaustion)

... (full overview content)
[MODULE_END: _act2_overview]

---

[MODULE_START: npc_zilvra_shadowveil]
### Zilvra Shadowveil (Drow Priestess - Antagonist)

**Role**: Velryn's former mentor, now hunting him for betrayal

**Personality**:
- Dutiful, not cruel
- Believes in Lolth's justice
- Sees Velryn's escape as personal failure
- Will show mercy if party proves worthy

**Goals**:
- Capture Velryn alive
- Retrieve House Shadowveil secrets he stole
- Restore her honor

**Relationship to Party**: Neutral → Hostile (if party protects Velryn)

**Key Dialogue Samples**:
> "Velryn Duskmere. I taught you everything. And you repay me with betrayal."
> "The Spider Queen demands your blood, but I offer mercy: surrender him, and you may leave."
> "You do not understand the burden of duty. I hope you never have to."

**Combat Stats**: CR 8 Drow Priestess of Lolth (MM p.128)
... (full stats if needed)

**Quest Flags**:
- zilvra_met: false
- zilvra_negotiated: false
- velryn_surrendered: false
- zilvra_hostile: false

[MODULE_END: npc_zilvra_shadowveil]

---

[MODULE_START: quest_mq2_three_fragments]
### MAIN QUEST 2: The Three Key Fragments

**Objective**: Obtain three mystical fragments to unlock the Vault Outer Sanctum

**Fragments Required**:
1. **Soulforge Shard** (from Artisan Quarter forge)
2. **Warden's Sigil** (from Temple District)
3. **Mourner's Tear** (from Noble Estates crypts)

**Structure**: These can be obtained in any order

**Fragment 1: Soulforge Shard**
- Location: Artisan Quarter - Ancient Forge
- Guardian: Ghost of Thalgrim (dwarf smith, CR 4 Ghost)
- Pacification: DC 15 Persuasion ("Your work saved thousands")
- Combat Alternative: Fight the Ghost (Deadly encounter)
- Secondary Challenge: Deactivate Helmed Horrors (DC 16 Arcana or fight CR 4 each)

... (full quest content)
[MODULE_END: quest_mq2_three_fragments]

---
... (continues for all indexed content)
```

## How This Solves Context Drift

### Problem 1: AI Forgets NPC Personality
**V1 Behavior**: "You meet Zilvra. She attacks!" (Generic hostile NPC)

**V2 Behavior**:
1. Player: "I want to talk to Zilvra"
2. Kernel's Execution Loop: Parse input → Target is "Zilvra"
3. Kernel: MANDATORY step - CALL Internal_Context_Retrieval("npc_zilvra_shadowveil")
4. Kernel: Search conversation for [MODULE_START: npc_zilvra_shadowveil]
5. Kernel: Load fresh data - personality, goals, dialogue samples
6. Kernel: Generate response using ONLY this fresh data
7. Output: "Zilvra steps forward, not with hatred, but weary duty. 'Velryn Duskmere. I taught you everything...'"

**Result**: High-fidelity NPC behavior even 1000 turns into a campaign

### Problem 2: AI Forgets to STOP
**V1 Behavior**: AI might generate "The party enters the temple and searches for clues..." (acting without input)

**V2 Behavior**:
1. Kernel's Execution Loop: Step 8 is MANDATORY "STOP_AND_WAIT"
2. Checkpoint (every 5 turns): Verify "Did I STOP every turn?"
3. If NO: "⚠️ SYSTEM INTEGRITY FAULT - I proceeded without input - Correcting..."
4. Rollback and re-present options

**Result**: Player agency cannot be violated because it's enforced by the unchangeable system prompt

### Problem 3: AI Forgets Quest Details
**V1 Behavior**: "You need to find... uh... something important in the temple" (vague)

**V2 Behavior**:
1. Player: "What quests do I have?"
2. Kernel: Parse → Action is "view_quests"
3. Kernel: CALL Internal_Context_Retrieval for each active quest
4. Kernel: Load fresh quest objectives, structure, flags
5. Output: "Active Quests: Main Quest 2 - The Three Key Fragments (Need: Soulforge Shard [obtained], Warden's Sigil [in progress], Mourner's Tear [not started])"

**Result**: Perfect quest tracking with zero degradation

## Session Initialization Flow

### User Setup (Once per session):

```
User Message 1:
"Initialize a new session. Loading orchestrator and campaign data."

[Paste entire Protocol Library - 40KB]

User Message 2:
[Paste entire Campaign Data Vault for current act - 20KB]

User Message 3:
[Paste Party State JSON or "New party"]
```

### AI Response:
```
✓ Kernel loaded (from system prompt)
✓ Protocol Library indexed (40 protocols found)
✓ Campaign Data Vault indexed (Act 2: The Dead City - 45 modules found)
✓ Party state: [Loaded existing party OR Starting character creation]

⚠️ CORE RULES ACTIVE:
- I ALWAYS present options and ⛔ STOP
- I NEVER act without your input
- I retrieve fresh data for every entity
- Checkpoint validates every 5 turns

Ready to begin. Retrieving Act 2 overview...

[AI calls Internal_Context_Retrieval("_act2_overview") and begins]
```

## Benefits Over V1

| Issue | V1 Behavior | V2 Solution |
|-------|-------------|-------------|
| NPC inconsistency | Forgets personality after 50 turns | Retrieves fresh data every interaction |
| Quest vagueness | "Find the thing" | Loads exact objectives from vault |
| Protocol drift | Might skip STOP | Kernel enforces it (can't forget system prompt) |
| User friction | "Paste campaign module now" | Silent retrieval from loaded vault |
| Hallucination risk | Fills gaps with guesses | Errors if module not found (honest failure) |
| Long sessions | Degrades after 2 hours | Maintains fidelity for 10+ hour sessions |

## File Structure for V2

```
agent_parts_v2/
├── KERNEL/
│   └── IMMUTABLE_KERNEL.md           # <1KB - System prompt content
├── PROTOCOL_LIBRARY/
│   ├── PART1_Session_Management.md    # Session init, character creation, resume
│   ├── PART2_Game_Loop.md             # Exploration, movement, investigation
│   ├── PART3_Combat.md                # Combat rounds, attacks, death saves
│   ├── PART4_Progression.md           # XP, leveling, quests, loot
│   └── PART5_Utilities.md             # Shopping, resting, inventory
├── SCHEMAS/
│   ├── Character_Schema_v2.md
│   ├── Party_State_Schema_v2.md
│   └── Campaign_Module_Schema_v2.md
├── assemble_protocol_library.py       # Generates indexed Protocol Library
└── V2_ARCHITECTURE_DESIGN.md          # This document
```

**Separate Repository** (Campaign Data Vaults):
```
campaigns/
├── Descent_into_Khar-Morkai/
│   ├── Act_1_Data_Vault.md
│   ├── Act_2_Data_Vault.md
│   └── Act_3_Data_Vault.md
└── create_campaign_vault.py           # Tool to convert campaign markdown to indexed vault
```

## Migration Path from V1 to V2

1. **Extract Kernel** from Part 1 - Take only execution constraints, core laws, checkpoint
2. **Reformat Protocols** with [PROTOCOL_START/END] tags
3. **Create Campaign Vault Generator** - Script to convert existing campaign markdown
4. **Test** with single act
5. **Full rollout** once validated

## Next Steps

1. Implement `IMMUTABLE_KERNEL.md`
2. Refactor Part 1-6 into indexed Protocol Library
3. Create `assemble_protocol_library.py`
4. Create `create_campaign_vault.py` tool
5. Test with Act 2 (has existing rich campaign data)
6. Document user-facing session initialization flow
