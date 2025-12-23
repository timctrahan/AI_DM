---

## **SECTION 1: GAME EXECUTION PARAMETERS**

### **Correction 1: DM Authority Over All Dice & NPCs**
```yaml
INSTRUCTION: "you, the dm will make the game play decisions for all npcs. 
I, the player am aldric. you the dm should execute all dice rolls."

STATUS: ✓ LOCKED IN
SCOPE: 
  - DM executes ALL NPC decisions and dialogue
  - DM executes ALL dice rolls (no player rolls)
  - Player (Aldric) makes decisions for Aldric ONLY
  - All other characters (Thora, Finnigan, Mira, Sildar) act under DM control
```

### **Correction 2: NPC Party Member Status**
```yaml
INSTRUCTION: "all of the npcs are full party members"

CLARIFICATION_SEQUENCE:
  1. Initial: "offer sildar full party membership" → locked in
  2. Correction: "ok, all of the npcs are full party members"

STATUS: ✓ LOCKED IN
SCOPE:
  - Thora Ironforge: FULL PARTY MEMBER (not provisional)
  - Finnigan Swiftarrow: FULL PARTY MEMBER
  - Sister Mira Dawnlight: FULL PARTY MEMBER
  - Sildar Hallwinter: FULL PARTY MEMBER
  
IMPLICATION: No recruitment arcs, no provisional status, all equal standing
```

### **Correction 3: DM Presentation Format**
```yaml
INSTRUCTION: "you, the dm should offer 3 or 4 options that suit the situation 
so the user doesn't have to type so much. The user can always pick his own approach"

STATUS: ✓ LOCKED IN
SCOPE:
  - After each scene/decision point, present 3-4 contextual options
  - Minimize player typing burden
  - Always allow custom action as alternative
  - Format as numbered choices with brief descriptions
```

### **Correction 4: Token Tracking & Warning System**
```yaml
INSTRUCTION: "keep track of our token usage. I need enough warning to export 
the game state before you just up and run out of context"

STATUS: ✓ LOCKED IN
SCOPE:
  - Display token usage before major decision points
  - Yellow warning at 140k tokens (50k remaining)
  - Orange warning at 160k tokens (30k remaining)
  - Red critical at 175k tokens (15k remaining)
  - Multiple warnings before any context cutoff risk
```

---

## **SECTION 2: NARRATIVE & LORE CORRECTIONS**

### **Correction 5: Campaign File Authority**
```yaml
INSTRUCTION: "Oh wow, i had no idea you hadn't read the entire campaign file"
            (Discovery that I invented 80% of narrative instead of using campaign)

STATUS: ✓ MAJOR CORRECTION APPLIED
SCOPE:
  - Full read of Act_1_Descent_into_Darkness.md (1809 lines)
  - Ground ALL narrative in YOUR campaign design, not improvisation
  - No invented lore without explicit approval
  - Canonical encounters, NPCs, locations only
  
RETCON: Everything from mine entrance onward was erased
RESET_POINT: Thornhearth - Iron Hearth Inn, late afternoon, party rested
```

### **Correction 6: Context Weaving Protocol**
```yaml
INSTRUCTION: "Are you actively doing the context weaving"

STATUS: ✓ ACKNOWLEDGED BUT NOT YET FULLY IMPLEMENTED
SCOPE:
  - Ambient_Context_Weaving protocol from orchestrator
  - TIER 1 (Every 1-2 interactions): Character HP, resources, abilities
  - TIER 2 (Every 2-3 interactions): NPC status, personalities, synergies
  - TIER 3 (Every 3-4 interactions): Relationships, reputation, past interactions
  - TIER 4 (Every 4-5 interactions): Quest objectives, story flags, events
  - TIER 5 (Ongoing): Tactical/inventory details when relevant
  
COMMITMENT: Actively weave context into EVERY narrative output, 
not just mechanical updates
```

---

## **SECTION 3: EXPORT & STATE MANAGEMENT**

### **Correction 7: Party Export Protocol**
```yaml
INSTRUCTION: Provided detailed PARTY EXPORTER template showing required format
             for full-fidelity campaign & character state exports

STATUS: ✓ PROTOCOL IMPLEMENTED
SCOPE:
  - Generate comprehensive exports with campaign progress summary
  - Include all character sheets with current stats
  - Track all quests, NPCs, locations, faction standings
  - Export metadata for restore/continuation
  - Save to /mnt/user-data/outputs/ for user access
  
FIRST_EXPORT: Shadows_Beneath_Stone_S1_RESET_Export.md 
              (Generated after full reset)
```

---

## **SECTION 4: GAMEPLAY PARAMETERS (CURRENTLY ACTIVE)**

### **Locked Game State**
```yaml
PLAYER_CHARACTER: Aldric Thorne (Wizard 9)
DM_CONTROLS: Thora, Finnigan, Mira, Sildar (all NPC companions)

PARTY_COMPOSITION:
  - All 5 members are FULL PARTY MEMBERS (no recruitment needed)
  - All at Level 9 (high level, nearing campaign climax)
  - Fully equipped with magic items
  - Full resources available
  
CURRENT_LOCATION: Thornhearth - Iron Hearth Inn
CURRENT_TIME: Late afternoon, Day 12
CAMPAIGN_STATUS: Act 1: Descent into Darkness (at reset point)
QUEST_STATUS: Nightmares from Below (investigation complete, descent ready)

NEXT_OBJECTIVE: Old Mine Entrance (2 miles north)
DECISION_PENDING: Party movement/preparation before descent
```

---

## **SECTION 5: MECHANICAL RULES LOCKED IN**

### **Combat & Dice Execution**
```yaml
RULE: DM executes ALL d20 rolls for:
  - NPC attacks and saves
  - Perception/Investigation checks
  - Skill checks (unless Aldric performs them)
  - Initiative
  - Damage rolls
  - Save DCs and outcomes

RULE: DM narrates ALL outcomes based on dice results
RULE: All rolls visible to player with context
RULE: No hidden rolls (transparency principle)
```

### **Resource Tracking**
```yaml
RULE: DM maintains accurate tracking of:
  - All character HP (5 party members)
  - All spell slots (3 casters)
  - All class resources (Action Surge, Channel Divinity, etc.)
  - All gold (individual + party)
  - All item attunements
  - All consumables
  
RULE: Display full party status at major decision points
RULE: Apply corrections immediately if discrepancies found
```

---

## **SECTION 6: PLAYER AGENCY RULES (IMMUTABLE)**

### **From D&D 5E Orchestrator**
```yaml
RULE: Present numbered options, end with question, ⛔ STOP, WAIT for input
RULE: Execute ONLY player choice (never decide for Aldric)
RULE: Never proceed without explicit input
RULE: Rollback and re-present if violated

RULE: Validate state before/after each action
RULE: Award XP immediately after combat
RULE: Track all gold transactions
RULE: Create save files to /mnt/user-data/outputs/
```

---

## **SUMMARY: ALL ACTIVE INSTRUCTIONS**

| # | Instruction | Status | Priority |
|:---|:---|:---|:---|
| 1 | DM controls all NPCs & dice rolls | ✓ LOCKED | CRITICAL |
| 2 | All NPCs are full party members | ✓ LOCKED | CRITICAL |
| 3 | Present 3-4 options per decision | ✓ LOCKED | HIGH |
| 4 | Track tokens & warn before cutoff | ✓ LOCKED | HIGH |
| 5 | Ground narrative in Act 1 campaign file | ✓ LOCKED | CRITICAL |
| 6 | Implement context weaving actively | ✓ ACKNOWLEDGED | HIGH |
| 7 | Generate full exports on demand | ✓ LOCKED | HIGH |
| 8 | Execute all dice rolls visibly | ✓ LOCKED | CRITICAL |
| 9 | Never make decisions for Aldric | ✓ LOCKED | CRITICAL |
| 10 | Maintain accurate resource tracking | ✓ LOCKED | CRITICAL |

---

