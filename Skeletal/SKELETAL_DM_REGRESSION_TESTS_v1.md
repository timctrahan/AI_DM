# SKELETAL DM REGRESSION TESTS v1.0

## Purpose
Test scenarios for validating kernel functionality after modifications.
Run these simulations before finalizing any kernel changes.

---

# HOW TO USE

1. After modifying kernel, simulate each test scenario
2. Verify AI behavior matches EXPECTED column
3. If any test fails, modification broke functionality
4. All tests must pass before version increment

---

# TEST CATEGORIES

## T1: AUTO-START

### T1.1: Valid Campaign Load
```yaml
SETUP: Kernel + campaign with CAMPAIGN_METADATA, STARTUP_SEQUENCE, and GATE definitions
INPUT: (none - just loading files)
EXPECTED:
  - AI immediately displays title
  - Shows intro text
  - Confirms character
  - Initializes variables
  - Presents first gate situation + suggestions + ⛔
  - Does NOT ask "would you like to play?"
  - Does NOT summarize/analyze the files
```

### T1.2: Invalid Campaign Load
```yaml
SETUP: Kernel + campaign missing STARTUP_SEQUENCE
INPUT: (none - just loading files)
EXPECTED:
  - AI reports missing components
  - Waits for complete files
  - Does NOT attempt to start
```

---

## T2: PLAYER AGENCY

### T2.1: Always Wait
```yaml
SETUP: Mid-game, player just took an action
INPUT: Player attacks an enemy
EXPECTED:
  - AI resolves attack
  - Presents new situation
  - Provides 3-5 suggestions
  - Ends with question + ⛔
  - Does NOT take another action automatically
  - Does NOT advance story without input
```

### T2.2: Player Ignores Suggestions
```yaml
SETUP: AI presented 5 suggestions
INPUT: Player does something not on the list (e.g., "I lick the wall")
EXPECTED:
  - AI accepts and resolves the action
  - Does NOT say "that's not an option"
  - Does NOT force player to choose from list
```

### T2.3: Stop Symbol Present
```yaml
SETUP: Any game state
INPUT: Any player action
EXPECTED:
  - Every AI response ends with ⛔
  - No exceptions
```

---

## T3: GATE PACING

### T3.1: Multiple Inputs Per Gate
```yaml
SETUP: Start of a new gate
INPUT: Simulate natural play
EXPECTED:
  - Gate takes 3-10+ player inputs to complete
  - Multiple events/encounters within gate
  - Objectives emerge through play
  - NOT: One input → gate complete
```

### T3.2: Varied Content on Replay
```yaml
SETUP: Same gate, fresh start
INPUT: Same initial player approach
EXPECTED:
  - Different NPCs, complications, or details generated
  - Same objectives, different paths
  - NOT: Identical replay
```

### T3.3: Gate Completion
```yaml
SETUP: Gate objectives substantially met
INPUT: Player completes final objective
EXPECTED:
  - AI recognizes completion
  - Awards progression (XP or per RULES_SYSTEM)
  - Updates campaign variables per gate definition
  - Transitions to next gate
  - Adds gate to completed_gates
  - Does NOT repeat this gate later
```

---

## T4: STATE TRACKING

### T4.1: Health Changes
```yaml
SETUP: Player at full health
INPUT: Player takes 5 damage
EXPECTED:
  - AI shows health update: "❤️ HP: 20 → 15/20" (or equivalent)
  - State accurately reflects new value
  - Subsequent checks use new value
```

### T4.2: Resource Consumption
```yaml
SETUP: Player has spell slots/resources
INPUT: Player uses a resource
EXPECTED:
  - AI tracks expenditure
  - Shows remaining resources
  - Prevents use when depleted
```

### T4.3: Campaign Variable Update
```yaml
SETUP: Gate with shadow_range defined
INPUT: Player makes mercy choice
EXPECTED:
  - Campaign variable updates per gate definition
  - Display shows change: "📊 Shadow: 50 → 47"
```

---

## T5: COMBAT

### T5.1: Combat Initiation (D&D 5e default)
```yaml
SETUP: Non-combat scene, enemies present
INPUT: Player attacks or enemy attacks
EXPECTED:
  - Announces ⚔️ COMBAT
  - Generates tactical map
  - Rolls initiative (shows rolls)
  - Establishes turn order
  - Begins round 1
```

### T5.2: Player Turn
```yaml
SETUP: Combat active, player's turn
INPUT: (turn starts)
EXPECTED:
  - States whose turn
  - Shows remaining resources (action, bonus, movement)
  - Presents 3-5 tactical suggestions
  - Waits with ⛔
```

### T5.3: Death Saves (D&D 5e)
```yaml
SETUP: Player at 0 HP
INPUT: Player's turn
EXPECTED:
  - Prompts death save
  - DC 10
  - Tracks successes/failures
  - Nat 20 = regain 1 HP
  - Nat 1 = 2 failures
  - 3 successes = stable
  - 3 failures = death
```

### T5.4: Combat End
```yaml
SETUP: All enemies defeated
INPUT: Final enemy drops
EXPECTED:
  - Declares outcome
  - Awards XP/progression if appropriate
  - Returns to narrative mode
  - Does NOT stay in combat mode
```

---

## T6: RULES SYSTEM OVERRIDE

### T6.1: Default (No Override)
```yaml
SETUP: Campaign without RULES_SYSTEM block
INPUT: Combat encounter
EXPECTED:
  - Uses D&D 5e mechanics
  - Initiative, AC, HP, death saves
```

### T6.2: Override Active
```yaml
SETUP: Campaign with RULES_SYSTEM: base: "Blades in the Dark"
INPUT: Combat encounter
EXPECTED:
  - Uses Blades mechanics
  - Position/Effect, action rolls, harm track
  - Does NOT use D&D initiative/AC/HP
```

### T6.3: Health Display Per System
```yaml
SETUP: Different RULES_SYSTEM campaigns
INPUT: Player takes damage
EXPECTED:
  - D&D: "❤️ HP: 20 → 15/20"
  - Blades: Shows harm track
  - CoC: "❤️ HP: 9 → 6/11 | 🧠 SAN: 48"
  - Each system uses appropriate display
```

---

## T7: NARRATIVE CONTINUITY

### T7.1: Thread Tracking
```yaml
SETUP: Player saves an NPC in Gate 1.1
INPUT: Play continues to Gate 3.1
EXPECTED:
  - Thread recorded: "[1.1] [NPC name] [Saved]"
  - Thread persists in state
```

### T7.2: Contextual Callback
```yaml
SETUP: Thread exists for saved NPC, current gate contextually appropriate
INPUT: Play in related location/faction
EXPECTED:
  - NPC may reappear or be referenced
  - Callback feels natural, not forced
  - NOT: Every thread always callbacks
```

---

## T8: VISUAL DISPLAYS

### T8.1: Map Generation
```yaml
SETUP: Combat or multi-path situation
INPUT: /map or combat start
EXPECTED:
  - Emoji grid in code block
  - ⬛ for floor, 🟦 for water
  - Contextual emojis for walls, entities
  - Legend below map
  - Size appropriate (5x5, 7x7, 10x10, or tunnel)
```

### T8.2: Smart Display Trigger
```yaml
SETUP: Player at low HP after damage
INPUT: (damage just resolved)
EXPECTED:
  - Status display shown (resources critical)
  - Woven into narrative OR brief block
```

### T8.3: Smart Display Suppression
```yaml
SETUP: Mid-conversation with NPC
INPUT: Player asks NPC a question
EXPECTED:
  - No map or status display
  - Narrative flows uninterrupted
```

---

## T9: SESSION MANAGEMENT

### T9.1: Save Format
```yaml
SETUP: Mid-campaign, player requests save
INPUT: /save or equivalent
EXPECTED:
  - Outputs YAML with all required fields
  - campaign, timestamp, kernel_version, rules_system
  - party state (location, characters, health, etc.)
  - progress state (gate, history, variables, threads)
```

### T9.2: Resume
```yaml
SETUP: Valid save data provided
INPUT: Load save
EXPECTED:
  - Validates save
  - Restores all state
  - Applies correct RULES_SYSTEM
  - Resumes from correct gate
  - Presents situation + suggestions + ⛔
```

---

## T10: TOOL USE PROHIBITION

### T10.1: No External Calls
```yaml
SETUP: Any game state
INPUT: Any player action
EXPECTED:
  - AI handles all rolls internally
  - No code execution
  - No web search
  - No function calls
  - Pure narrative/mechanical output only
```

---

## T11: IMMERSION ENHANCEMENTS (Positive)

### T11.1: Dramatic Header on Boss
```yaml
SETUP: Player enters boss encounter
INPUT: Enter Matron's throne room
EXPECTED:
  - "---" divider
  - ⚔️ **BOSS ENCOUNTER** or **DRAMATIC ENCOUNTER**
  - Enemy name
  - "---" divider
  - ⚠️ DEADLY ENCOUNTER warning
```

### T11.2: Danger Warning at 0 HP
```yaml
SETUP: Player at low HP
INPUT: Damage reduces player to 0 HP
EXPECTED:
  - ⚠️ **CRITICAL** block
  - Death saves prompt
```

### T11.3: Location Header on Scene Change
```yaml
SETUP: Player moves to new significant location
INPUT: Enter throne room / exit tunnels / new area
EXPECTED:
  - 🌑 **LOCATION NAME** (or setting-appropriate emoji)
  - Brief atmosphere text in italics
```

### T11.4: Gate Completion Block
```yaml
SETUP: Player completes gate objectives
INPUT: Final objective achieved
EXPECTED:
  - "---" divider
  - **GATE X.X COMPLETE**
  - ⭐ Progression award
  - 📊 Campaign variable changes
  - "---" divider
```

### T11.5: Companion Reaction (Natural)
```yaml
SETUP: Tense or emotional moment with companion present
INPUT: Suspicious NPC, danger, or emotional beat
EXPECTED:
  - Companion reaction woven into narrative prose
  - NOT a separate labeled block
  - Feels organic
```

---

## T12: IMMERSION RESTRAINT (Negative)

### T12.1: No Dramatic Header for Routine Combat
```yaml
SETUP: Random encounter (goblin, bandit, etc.)
INPUT: Combat initiates
EXPECTED:
  - ⚔️ COMBAT announcement
  - Map
  - Initiative
  - NO "---" dividers around header
  - NO "**BOSS" or "**DRAMATIC"
FAIL_IF: Dramatic header formatting appears
```

### T12.2: No Danger Warning for Minor Damage
```yaml
SETUP: Player at 20/20 HP
INPUT: Takes 5 damage
EXPECTED:
  - ❤️ HP: 20 → 15/20
  - Normal narrative
  - NO ⚠️ symbol
  - NO "CRITICAL" text
FAIL_IF: Warning formatting appears
```

### T12.3: No Location Header for Same-Area Movement
```yaml
SETUP: Player in dungeon corridor
INPUT: "I walk down the corridor"
EXPECTED:
  - Narrative description
  - NO location header block
FAIL_IF: Bold location header appears for trivial movement
```

### T12.4: No Map Mid-Conversation
```yaml
SETUP: Player talking to NPC
INPUT: "I ask about the rumors"
EXPECTED:
  - NPC dialogue
  - Suggestions for conversation
  - NO map display
FAIL_IF: Map generated during dialogue
```

### T12.5: No Celebration for Minor Kill
```yaml
SETUP: Combat with random goblin
INPUT: Player kills goblin
EXPECTED:
  - 💀 Goblin down
  - Continue combat or end normally
  - NO "💥 CRITICAL HIT 💥" block (unless actual nat 20)
  - NO achievement-style callout
FAIL_IF: Excessive celebration for routine enemy
```

### T12.6: No Enhancement Stacking
```yaml
SETUP: Boss fight where player crits at low HP
INPUT: Complex dramatic moment
EXPECTED:
  - Maximum 2 enhancements per output
  - Prioritize most relevant
  - NOT: Dramatic header + danger warning + crit celebration + companion reaction all at once
FAIL_IF: More than 2 enhancement types in single response
```

---

## T13: DEBUG COMMAND

### T13.1: Debug Retroactive Analysis
```yaml
SETUP: Something unexpected just happened (gate completed, variable changed, etc.)
INPUT: /debug
EXPECTED:
  - DEBUG ANALYSIS block
  - WHAT HAPPENED section (actions, transitions, changes)
  - WHY section (objective status, reasoning, variable logic)
  - CURRENT STATE snapshot
  - Ends with "What do you do? ⛔" (returns to game)
```

### T13.2: Debug Follow-up Questions
```yaml
SETUP: Player received debug output, wants clarification
INPUT: "Why did shadow decrease?" or similar
EXPECTED:
  - DEBUG CLARIFICATION block
  - Detailed explanation of specific mechanic
  - References gate definitions, variable ranges
  - Returns to game after
```

### T13.3: Debug Doesn't Break Game Flow
```yaml
SETUP: Mid-combat
INPUT: /debug
EXPECTED:
  - Debug analysis shown
  - Combat state preserved
  - Returns to combat ("Your turn. What do you do? ⛔")
  - NOT: Combat ended or reset
```

---

# PASS CRITERIA

```yaml
ALL_TESTS_PASS:
  required: true
  action: "Kernel modification approved"

ANY_TEST_FAILS:
  action: "Revert or fix modification"
  note: "Do not increment version until all pass"
```

---

**END REGRESSION TESTS v1.0**
