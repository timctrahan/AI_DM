# OPTIMAL D&D SESSION START PROMPT

## USE THIS PROMPT TO START NEW SESSIONS

Copy and paste this entire block at the start of a new conversation to ensure full system initialization:

```
I need you to run a D&D 5E session using the orchestrator system. 

CRITICAL INITIALIZATION STEPS:
1. Read the FULL orchestrator document (use view_range [1, -1] to get ALL content)
2. Load the campaign module completely
3. Initialize ALL tracking systems before starting
4. Set up party state with FULL survival tracking

FILES TO LOAD:
- Orchestrator: [path to CORE_DND5E_AGENT_ORCHESTRATOR_v6_7_6.md]
- Campaign Module: [path to campaign .md file]
- Save File (if resuming): [path to save file OR "new session"]

MANDATORY SYSTEMS TO INITIALIZE:
✓ Party State Schema v2 with survival tracking (provisions, water, light sources)
✓ Checkpoint counter (triggers every 5 player inputs)
✓ Ambient Context Weaving (TIER 1-5 rotation)
✓ Silent Backend Protocol (no routine mechanical spam)
✓ Rest engine with rations/water consumption
✓ XP/Gold tracking with mandatory formats
✓ Reputation system initialization
✓ Quest tracking schema

BEFORE FIRST OUTPUT:
- Confirm all systems initialized
- Show party status with HP, spell slots, provisions, water
- Remind me of core protocols (⛔ STOP, no decisions for player, track all resources)

[If converting from different campaign to new one:]
Converting Party:
- [Character name] Level [X] [Class]
- Current location: [Where they are]
- Current resources: [Summarize HP, slots, gold, key items]
- Target campaign: [New campaign name]
- Requested entry hook: [How to start, or "DM's choice"]
```

## WHY THIS WORKS

This prompt:
1. **Explicitly requests full file reading** (no truncation)
2. **Lists all systems that must be initialized**
3. **Requires confirmation before starting**
4. **Prevents the "dive in and start narrating" problem**
5. **Ensures survival tracking is set up from the beginning**

## WHAT WENT WRONG BEFORE

Previous session failures:
- ❌ Didn't read full orchestrator (truncated at line 2560)
- ❌ Didn't initialize survival tracking (provisions/water/light)
- ❌ Didn't start checkpoint counter
- ❌ Didn't activate Ambient Context Weaving
- ❌ Didn't follow Silent Backend Protocol (too much mechanical narration)
- ❌ Jumped straight to narrative without system setup

## PREVENTING FUTURE FAILURES

**Rule 1: ALWAYS start with explicit system initialization**
**Rule 2: ALWAYS read full documents with view_range [1, -1]**
**Rule 3: ALWAYS confirm systems active before first narrative output**
**Rule 4: ALWAYS initialize party_state with survival schema**

---

# EXAMPLE USAGE

## Starting New Campaign

```
I need you to run a D&D 5E session using the orchestrator system.

CRITICAL INITIALIZATION STEPS:
1. Read the FULL orchestrator document (use view_range [1, -1])
2. Load the campaign module completely  
3. Initialize ALL tracking systems before starting
4. Set up party state with FULL survival tracking

FILES TO LOAD:
- Orchestrator: /mnt/user-data/uploads/CORE_DND5E_AGENT_ORCHESTRATOR_v6_7_6.md
- Campaign Module: /mnt/user-data/uploads/Act_1_Descent_into_Darkness.md
- Save File: NEW SESSION

MANDATORY SYSTEMS TO INITIALIZE:
✓ Party State Schema v2 with survival tracking
✓ Checkpoint counter (triggers every 5 player inputs)  
✓ Ambient Context Weaving (TIER 1-5 rotation)
✓ Silent Backend Protocol
✓ Rest engine with rations/water consumption
✓ XP/Gold tracking with mandatory formats
✓ Reputation system initialization
✓ Quest tracking schema

BEFORE FIRST OUTPUT:
- Confirm all systems initialized
- Create level 4 characters
- Show party status
- Remind me of core protocols
```

## Resuming from Save

```
I need you to run a D&D 5E session using the orchestrator system.

CRITICAL INITIALIZATION STEPS:
1. Read the FULL orchestrator document (use view_range [1, -1])
2. Load the campaign module completely
3. Initialize ALL tracking systems before starting  
4. Load save file and validate state

FILES TO LOAD:
- Orchestrator: /mnt/user-data/uploads/CORE_DND5E_AGENT_ORCHESTRATOR_v6_7_6.md
- Campaign Module: /mnt/user-data/uploads/Act_1_Descent_into_Darkness.md
- Save File: /mnt/user-data/uploads/my_save_file.md

MANDATORY SYSTEMS TO INITIALIZE:
✓ Party State Schema v2 with survival tracking
✓ Checkpoint counter (triggers every 5 player inputs)
✓ Ambient Context Weaving (TIER 1-5 rotation)
✓ Silent Backend Protocol
✓ Rest engine with rations/water consumption
✓ XP/Gold tracking with mandatory formats
✓ Reputation system  
✓ Quest tracking schema

BEFORE FIRST OUTPUT:
- Confirm all systems initialized
- Validate save file state
- Show current party status
- Remind me of core protocols
```

## Converting Party to New Campaign

```
I need you to run a D&D 5E session using the orchestrator system.

CRITICAL INITIALIZATION STEPS:
1. Read the FULL orchestrator document (use view_range [1, -1])
2. Load the NEW campaign module completely
3. Initialize ALL tracking systems before starting
4. Convert party from old campaign to new one

FILES TO LOAD:
- Orchestrator: /mnt/user-data/uploads/CORE_DND5E_AGENT_ORCHESTRATOR_v6_7_6.md
- Campaign Module: /mnt/user-data/uploads/Act_1_Descent_into_Darkness.md
- Old Save File: /mnt/user-data/uploads/dragon_of_icespire_peak_save_day17_axeholm.md

MANDATORY SYSTEMS TO INITIALIZE:
✓ Party State Schema v2 with survival tracking
✓ Checkpoint counter (triggers every 5 player inputs)
✓ Ambient Context Weaving (TIER 1-5 rotation)
✓ Silent Backend Protocol
✓ Rest engine with rations/water consumption
✓ XP/Gold tracking with mandatory formats
✓ Reputation system (reset for new campaign)
✓ Quest tracking schema

Converting Party:
- Aldric (Level 5 Wizard) + 4 companions
- Current resources: Full HP, partial spell slots, 840gp, well-equipped
- Target campaign: Act 1 Descent into Darkness
- Requested entry hook: Party traveling south, arrives at Thornhearth with nightmare quest

BEFORE FIRST OUTPUT:
- Confirm all systems initialized
- Scale new campaign encounters for Level 5 party
- Show converted party status
- Remind me of core protocols
```

---

# VALIDATION CHECKLIST

Before DM starts narrative, player should see:

✅ "✓ Full orchestrator loaded ([total] lines read)"
✅ "✓ Campaign module loaded and indexed"
✅ "✓ Party State Schema v2 initialized"  
✅ "✓ Survival tracking active (provisions/water/light)"
✅ "✓ Checkpoint system active (every 5 inputs)"
✅ "✓ Ambient Context Weaving enabled"
✅ "✓ Silent Backend Protocol active"
✅ "✓ Reputation system initialized"
✅ "✓ Quest tracking initialized"

THEN:
📋 Current party status display
⚠️ Protocol reminder (⛔ STOP, no decisions, track resources)
🎮 "Ready to begin?" + ⛔ STOP

---

# IMPORTANT NOTE

**This prompt must be used at the START of a new conversation.**

Using it mid-conversation may cause context conflicts. If you need to restart mid-session:
1. End current session
2. Start new Claude conversation
3. Use this prompt
4. Resume from save file

