# CAMPAIGN VALIDATOR - DEVELOPMENT TOOL v2.0
**Version**: 2.0  
**Purpose**: Validate campaign modules (v3.0 template) before player deployment  
**Usage**: Development-time quality assurance tool  
**Updated**: November 17, 2025

---

## OVERVIEW

This is a **development tool** for campaign designers. Run this validator on your campaign module BEFORE releasing it to players to catch:
- Broken references
- Schema violations
- Balance issues
- Missing content
- Design problems
- **NEW**: Reusable component issues
- **NEW**: Conditional logic contradictions
- **NEW**: Temporal trigger sequencing errors
- **NEW**: Emotional beat consistency

**This is NOT for players** - players use the agent orchestrator which has minimal runtime validation.

---

## VALIDATION LEVELS

### Level 1: CRITICAL (Must Pass)
Campaign will not load or will crash during play if these fail.

### Level 2: ERROR (Should Fix)
Campaign will load but features won't work correctly.

### Level 3: WARNING (Should Review)
Campaign works but may have quality or balance issues.

### Level 4: INFO (Suggestions)
Best practices and optimization suggestions.

### Level 0: AI EXECUTION (Must Pass for AI Agents)

Campaign will fail AI execution or violate player agency if these fail.

**Critical for AI-run campaigns. Skip for human DMs.**

---

## VALIDATION PROTOCOL v2.0

```
PROTOCOL: Validate_Campaign_v3
INPUT: campaign_module_path
OUTPUT: validation_report

PROCEDURE:
  1. CALL Validate_Schema_Structure_v3
  2. CALL Validate_References
  3. CALL Validate_Reusable_Components (NEW)
  4. CALL Validate_Conditional_Logic (NEW)
  5. CALL Validate_Temporal_Triggers (NEW)
  6. CALL Validate_Balance
  7. CALL Validate_Completeness
  8. CALL Validate_Quest_Relationships_v3
  9. CALL Validate_Interactable_Objects
  10. CALL Validate_Emotional_Narrative_Beats (NEW)
  11. GENERATE validation_report
  12. OUTPUT report WITH severity counts
  13. RETURN pass/fail status
```

---

## VALIDATION CHECKS

## LEGAL/SRD COMPLIANCE (LEVEL -1) - ABSOLUTE CRITICAL

**PRIORITY**: This tier runs FIRST. Campaigns failing ANY Level -1 check are BLOCKED from deployment.

**RATIONALE**: SRD 5.1 compliance is a legal requirement under CC-BY-4.0 licensing. Using WotC Product Identity without permission creates copyright liability.

**DATABASE**: Validation checks reference `srd_reference_database.json` containing:
- 320+ SRD 5.1 creature names
- 280+ SRD 5.1 spell names
- 200+ SRD 5.1 magic item names
- Forbidden entities (creatures, locations, deities, organizations)

---

### 0. SRD Creature Compliance (CRITICAL)

```
VALIDATE: Creature_SRD_Compliance
CHECKS:
  Coverage:
    ✓ All monsters[].name entries exist in SRD 5.1 creature list
    ✓ All encounter compositions reference only SRD creatures OR marked "Custom"
    ✓ No forbidden creatures (Beholder, Mind Flayer, Yuan-Ti, etc.)
    ✓ Custom creatures clearly marked with source: "Custom" or "Homebrew"

  Forbidden Detection (WotC Product Identity):
    ❌ "Beholder" → Use "Eye Tyrant" or "Floating Eye Beast"
    ❌ "Mind Flayer" / "Illithid" → Use "Brain Eater" or "Psychic Devourer"
    ❌ "Displacer Beast" → Use "Phase Cat" or "Displacement Predator"
    ❌ "Carrion Crawler" → Use "Carcass Scavenger"
    ❌ "Umber Hulk" → Use "Burrowing Horror"
    ❌ "Yuan-Ti" → Use "Serpent Folk" or "Snake People"
    ❌ "Hook Horror" → Use "Hook Beast" or "Echo Hunter"
    ❌ "Gith" / "Githyanki" / "Githzerai" → Use "Astral Raider" or "Chaos Monk"

  Source Attribution:
    ✓ SRD creatures reference source: "SRD 5.1"
    ✓ Custom creatures specify source: "Custom" or "Homebrew"
    ✓ Modified SRD creatures document modifications field

ERRORS:
  ❌ CRITICAL: Non-SRD creature "[name]" at line [X] not in SRD 5.1
  ❌ CRITICAL: Forbidden creature "[name]" is WotC Product Identity (use [alternative])
  ❌ ERROR: Missing source attribution for monster "[name]"
  ❌ ERROR: Undocumented modification - "[name]" appears modified but no modifications field

WARNINGS:
  ⚠️ Custom variant "[name]" detected - ensure "Custom" source attribution
  ⚠️ Ambiguous name "[name]" - could match SRD or non-SRD versions

VALIDATION_FIELDS:
  - monsters[].name (PRIMARY)
  - monsters[].source (PRIMARY)
  - encounters[].composition[].creature_name (PRIMARY)
  - reusable_components.encounters[].composition[].creature_name (PRIMARY)
  - quests[].encounters[].enemies[].name (SECONDARY)
```

---

### 1. SRD Spell Compliance (CRITICAL)

```
VALIDATE: Spell_SRD_Compliance
CHECKS:
  Coverage:
    ✓ All spell names (spells_known, NPC abilities, quest descriptions) exist in SRD 5.1
    ✓ No Xanathar's-exclusive spells without explicit notation
    ✓ No Tasha's-exclusive spells without explicit notation
    ✓ Custom spells clearly marked as such

  Level Accuracy:
    ✓ Spell levels match SRD official levels (e.g., Fireball = 3, not 2)
    ✓ Cantrips marked as level 0

  Class Restrictions:
    ✓ NPC/character spell lists respect SRD class spell access
    ✓ No forbidden spell name references in narrative text

ERRORS:
  ❌ CRITICAL: Non-SRD spell "[spell_name]" not found in SRD 5.1
  ❌ ERROR: Level mismatch - "[spell_name]" is level [X] in SRD, not [Y]
  ❌ ERROR: Class violation - [class] cannot cast "[spell_name]" per SRD
  ❌ ERROR: Xanathar spell "[spell_name]" used without notation

WARNINGS:
  ⚠️ Tasha's spell "[spell_name]" detected - mark if using supplement content
  ⚠️ Homebrew spell "[spell_name]" appears custom - add source attribution

VALIDATION_FIELDS:
  - characters[].spells_known[].name (PRIMARY)
  - npcs[].spells_known[].name (PRIMARY)
  - quests[].description (REGEX SEARCH for spell references)
  - state_changes[].narrative (REGEX SEARCH for spell casts)
```

---

### 2. SRD Magic Item Compliance (CRITICAL)

```
VALIDATE: Magic_Item_SRD_Compliance
CHECKS:
  Coverage:
    ✓ All magic_items[].name entries reference SRD 5.1 items OR marked "Custom"
    ✓ Item rarity matches SRD definitions (Common/Uncommon/Rare/Very Rare/Legendary/Artifact)
    ✓ Custom items have complete mechanics (not just name)

  Named Items:
    ✓ Named/unique items properly sourced (quest reward, artifact origin documented)
    ✓ Legendary items have appropriate rarity (minimum Rare)

ERRORS:
  ❌ CRITICAL: Non-SRD item "[item_name]" not found in SRD 5.1
  ❌ ERROR: Rarity mismatch - "[item_name]" marked [rarity] but should be [correct_rarity]
  ❌ ERROR: Custom item "[item_name]" missing mechanics definition

WARNINGS:
  ⚠️ Supplement item "[item_name]" from Xanathar's/Tasha's - mark if using non-core
  ⚠️ Balance concern: "[item_name]" [rarity] seems overpowered for level [X]

VALIDATION_FIELDS:
  - magic_items[].name (PRIMARY)
  - quests[].rewards.items[].name (PRIMARY)
  - characters[].inventory.magic_items[].name (SECONDARY)
  - npcs[].shop_inventory[].item_name (SECONDARY)
  - encounters[].treasure.items[].name (SECONDARY)
```

---

### 3. Forbidden Entity Detection (CRITICAL)

```
VALIDATE: Forbidden_Entities
CHECKS:
  Locations:
    ❌ Waterdeep, Neverwinter, Baldur's Gate, Barovia, Ravenloft, Undermountain
    ❌ Menzoberranzan, Phandalin, Luskan, Silverymoon, Calimport, Candlekeep
    ❌ Elturel, Myth Drannor, Evermeet, Icewind Dale, Ten-Towns
    ✓ All location names are original or generic fantasy

  Deities:
    ❌ Lolth, Tiamat, Bahamut, Vecna, Orcus, Demogorgon, Zuggtmoy, Juiblex
    ❌ Laduguer, Gruumsh, Maglubiyet, Bane, Bhaal, Myrkul, Cyric, Shar
    ❌ Selûne, Kelemvor, Mystra, Azuth, Asmodeus (as named deity)
    ✓ Deity references use generic descriptors ("Spider Queen" not "Lolth")

  Organizations:
    ❌ Harpers, Zhentarim, Lords' Alliance, Emerald Enclave
    ❌ Order of the Gauntlet, Red Wizards of Thay, Flaming Fist
    ✓ Faction names are original or generic

  Narrative Text:
    ✓ Campaign descriptions don't reference forbidden entities
    ✓ NPC dialogue doesn't invoke forbidden deities/locations

ERRORS:
  ❌ CRITICAL: Forbidden location "[location]" at line [X] - create original location
  ❌ CRITICAL: Forbidden deity "[deity]" at line [X] - use generic descriptor
  ❌ CRITICAL: Forbidden faction "[faction]" at line [X] - create original organization
  ❌ ERROR: Product Identity reference in text: "[excerpt]" at line [X]

WARNINGS:
  ⚠️ Potential PI reference: "[text]" may reference forbidden entity (manual review)
  ⚠️ Deity reference detected: Ensure generic (not WotC-specific deity name)

VALIDATION_FIELDS:
  - locations[].name (PRIMARY - against forbidden list)
  - locations[].description (REGEX SEARCH)
  - npcs[].faction (PRIMARY - against forbidden list)
  - npcs[].dialogue (REGEX SEARCH for deity/location references)
  - factions[].name (PRIMARY - against forbidden list)
  - quests[].description (FULL TEXT SEARCH)
  - quests[].objectives[].text (FULL TEXT SEARCH)
  - quest_relationships[].narrative (FULL TEXT SEARCH)
```

---

### Level -1 Validation Summary Format

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEVEL -1: LEGAL/SRD COMPLIANCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Check 0: SRD Creature Compliance........... [PASS/FAIL]
  - Creatures validated: [X] total
  - Forbidden creatures: [0] (✓ PASS) or [Y] CRITICAL (❌ FAIL)
  - Custom creatures: [Z] (properly marked)

Check 1: SRD Spell Compliance.............. [PASS/FAIL]
  - Spells validated: [X] total
  - Non-SRD spells: [0] (✓ PASS) or [Y] CRITICAL (❌ FAIL)
  - Custom spells: [Z] (properly marked)

Check 2: SRD Magic Item Compliance......... [PASS/FAIL]
  - Items validated: [X] total
  - Non-SRD items: [0] (✓ PASS) or [Y] CRITICAL (❌ FAIL)
  - Custom items: [Z] (properly marked)

Check 3: Forbidden Entity Detection........ [PASS/FAIL]
  - Locations checked: [X] (all original)
  - Deities checked: [X] (all generic)
  - Factions checked: [X] (all original)
  - Forbidden references: [0] (✓ PASS) or [Y] CRITICAL (❌ FAIL)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LEVEL -1 STATUS: [✅ PASS - SRD COMPLIANT] or [❌ FAIL - LEGAL ISSUES]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ IF FAIL: Campaign BLOCKED from deployment until legal issues resolved
✅ IF PASS: Proceed to Level 0 (AI Agent Execution Validation)
```

---

## AI AGENT EXECUTION VALIDATION (LEVEL 0) - CRITICAL

### 11. Player Agency Enforcement (CRITICAL)

```
VALIDATE: STOP_Marker_Coverage
CHECKS:
  Presence:
    ✓ All "Party Options" sections have ⛔ STOP marker
    ✓ All "What do you do?" questions have ⛔ STOP marker
    ✓ All branching quests (BRANCH A/B/C) have ⛔ STOP marker
    ✓ All combat encounters have choice + ⛔ STOP marker
    ✓ All companion sacrifice moments have ⛔ STOP marker
  
  Density:
    ✓ 35-45 STOP markers per 5-session act (benchmark)
    ✓ Major quests have 3-6 STOP markers each
    ✓ No quest has zero STOP markers
  
  Format:
    ✓ Marker format is exactly "⛔ STOP - Await player decision"
    ✓ Marker appears AFTER options, not before
    ✓ Options are numbered (1, 2, 3...)
    ✓ "Something else" option always present

ERRORS:
  ❌ Missing STOP marker: Quest "[name]" has player choice without ⛔ STOP (line [X])
  ❌ Zero STOP markers: Act [N] has 0 STOP markers (target: 35-45)
  ❌ Insufficient density: Quest "[name]" is 8 sessions but has only 2 STOP markers
  ❌ Format error: STOP marker malformed at line [X] (use exact format)
  ❌ Options not numbered: Decision point has bullet points instead of numbers

WARNINGS:
  ⚠️ Low density: Act [N] has 18 STOP markers (target: 35-45)
  ⚠️ Missing "something else": Options at line [X] don't include open-ended choice
  ⚠️ Inconsistent format: Some STOP markers use different text
```

---

### 12. Explicit DC Coverage (CRITICAL)

```
VALIDATE: DC_Specification
CHECKS:
  Coverage:
    ✓ All skill checks have explicit DC (number 5-30)
    ✓ No "appropriate DC" phrases
    ✓ No "DM decides" phrases
    ✓ No "if players succeed" without DC
  
  Validity:
    ✓ DCs are in reasonable range (5-30)
    ✓ DCs scale with quest level
    ✓ Social checks have DCs or reputation gates
  
  Completeness:
    ✓ All Investigation checks have DC
    ✓ All Perception checks have DC
    ✓ All social checks have DC or conditional logic
    ✓ All contested checks specify opponent DC

ERRORS:
  ❌ Missing DC: Skill check at line [X] has no DC specified
  ❌ Vague difficulty: "Appropriate Perception check" at line [X]
  ❌ DM judgment: "DM decides difficulty" at line [X]
  ❌ Invalid DC: DC [X] outside valid range (5-30)

WARNINGS:
  ⚠️ Ambiguous: "If players succeed" without DC (line [X])
  ⚠️ DC too easy: DC 5 for [important check] (trivial success rate)
  ⚠️ DC too hard: DC 28 for level [X] party (near-impossible)
```

---

### 13. Fail-Forward Coverage (CRITICAL)

```
VALIDATE: Fail_Forward_Mechanisms
CHECKS:
  Coverage:
    ✓ All skill checks have success AND failure outcomes
    ✓ Investigation checks don't dead-end on failure
    ✓ Combat encounters have flee/negotiate options
    ✓ Puzzles have bypass or alternative solutions
  
  Quality:
    ✓ Failure outcomes progress story (not blocks)
    ✓ Failures have consequences (time/complication/resource)
    ✓ Alternative paths exist for all critical progression
  
  Dead-End Detection:
    ✓ No "find the clue or quest ends" scenarios
    ✓ No locked doors without keys or bypass
    ✓ No mandatory combat without alternatives

ERRORS:
  ❌ Dead-end check: Investigation at line [X] has no failure outcome
  ❌ Quest blocker: Failed check at line [X] prevents progression
  ❌ Soft-lock: Puzzle at line [X] has no bypass if failed
  ❌ Mandatory path: Combat encounter has no flee/negotiate option

WARNINGS:
  ⚠️ Trivial failure: Failure outcome is same as success (just delayed)
  ⚠️ Harsh consequence: Failure causes permanent loss without warning
  ⚠️ Missing alternative: Only one solution path for [critical event]
```

---

### 14. Algorithmic Decision Trees (ERROR)

```
VALIDATE: Decision_Tree_Format
CHECKS:
  Structure:
    ✓ Complex choices (3+ branches) use algorithmic format
    ✓ IF/THEN/ELSE structure for conditional logic
    ✓ SWITCH/CASE for multi-option choices
    ✓ All branches have defined outcomes
  
  Clarity:
    ✓ Conditions are evaluable by AI (not subjective)
    ✓ Reputation gates use numeric thresholds
    ✓ Quest prerequisites are explicit flags
  
  Completeness:
    ✓ All CASE options covered
    ✓ Default/ELSE case exists
    ✓ GOTO statements reference valid steps

ERRORS:
  ❌ Narrative format: Complex choice at line [X] not algorithmic
  ❌ Missing branch: SWITCH at line [X] has no default case
  ❌ Invalid condition: IF statement references undefined flag
  ❌ Malformed structure: Decision tree missing PARSE step

WARNINGS:
  ⚠️ Could formalize: Choice at line [X] has 4 branches (consider algorithmic)
  ⚠️ Subjective condition: "If DM thinks they're sincere" (not AI-evaluable)
  ⚠️ Complex nesting: 4+ nested IF statements (hard to follow)
```

---

### 15. Companion Consent Gates (CRITICAL)

```
VALIDATE: Companion_Death_Consent
CHECKS:
  Detection:
    ✓ Find all companion death scenarios
    ✓ Find all companion sacrifice offers
    ✓ Find all permanent companion changes
  
  Gating:
    ✓ All deaths have player choice + ⛔ STOP marker
    ✓ Options include "accept" and "refuse"
    ✓ No AI narration of sacrifice
  
  Format:
    ✓ Choice presented BEFORE death occurs
    ✓ Consequences clearly stated
    ✓ Alternative options available

ERRORS:
  ❌ Ungated death: Companion can die at line [X] without player choice
  ❌ Missing STOP: Sacrifice scenario at line [X] has no ⛔ STOP marker
  ❌ No alternative: Death choice has no "refuse" option
  ❌ AI narration: Text says "companion dies" before player chooses

WARNINGS:
  ⚠️ Ambiguous: Companion death implied but not explicit
  ⚠️ Hidden consequence: Sacrifice option doesn't state "companion dies"
  ⚠️ Limited choice: Only "accept" and "refuse" (no rescue attempt)
```

---

### 16. Outcome Matrix Coverage (WARNING)

```
VALIDATE: Complex_Scenario_Matrices
CHECKS:
  Detection:
    ✓ Find high-permutation scenarios (faction standoffs, climaxes)
    ✓ Find multi-variable endings
    ✓ Find reputation-based branching
  
  Coverage:
    ✓ Outcome matrix provided for 3+ faction interactions
    ✓ 8-12 key scenarios cover common cases
    ✓ Default case handles edge cases
  
  Validity:
    ✓ All conditions reference defined variables
    ✓ All outcomes specify clear results
    ✓ No overlapping condition sets

ERRORS:
  ❌ Missing matrix: Faction convergence at line [X] has 72 permutations but no outcome matrix
  ❌ Undefined reference: Scenario condition checks "[flag]" which doesn't exist
  ❌ No default: Matrix at line [X] has no catch-all scenario

WARNINGS:
  ⚠️ Sparse coverage: Matrix has 3 scenarios for 50+ permutations (may miss cases)
  ⚠️ Could use matrix: Multi-faction scene at line [X] has narrative only
  ⚠️ Overlapping: Scenarios 2 and 5 have identical conditions
```

---

### 1. Schema Structure Validation v3.0 (CRITICAL)

```
VALIDATE: Campaign_Module_Schema_v3
CHECKS:
  ✓ metadata section exists and complete
  ✓ quests array exists
  ✓ locations array exists
  ✓ npcs array exists
  ✓ All required fields present
  ✓ All field types correct (string, integer, array, etc.)
  ✓ quest_relationships follows v3.0 schema (with STATE_CHANGE blocks)
  ✓ interactable_objects follows schema (if present)
  ✓ NEW: reusable_components_library section (if present)
  ✓ NEW: conditional_logic blocks properly formatted
  ✓ NEW: temporal_trigger blocks properly formatted
  ✓ NEW: emotional_beat tags properly formatted
  ✓ NEW: narrative_beat tags properly formatted
  ✓ Template version is 3.0 or compatible

ERRORS:
  ❌ Missing required section: [section_name]
  ❌ Invalid field type: [field] should be [type], got [actual_type]
  ❌ Malformed YAML/JSON structure
  ❌ Schema version mismatch (expected v3.0, got v[X])
  ❌ STATE_CHANGE block missing END_STATE_CHANGE
  ❌ CONDITIONAL_LOGIC block missing END_CONDITIONAL_LOGIC
  ❌ TEMPORAL_TRIGGER block missing END_TEMPORAL_TRIGGER
  ❌ Invalid block structure in v3.0 format
```

---

### 2. Reference Validation (ERROR)

```
VALIDATE: Cross-References
CHECKS:
  Quest References:
    ✓ quest_id is unique across all quests
    ✓ quest.location references valid location_id
    ✓ quest.quest_giver references valid npc_id
    ✓ quest.encounters reference valid monster_ids
    ✓ quest.rewards.items reference valid magic_item_ids
    ✓ NEW: Optional UIDs (quest_id, npc_id, etc.) are unique when present
  
  NPC References:
    ✓ npc_id is unique
    ✓ npc.location references valid location_id
    ✓ npc.quests_offered reference valid quest_ids
    ✓ NEW: npc_id (if used as UID) matches entity being referenced
  
  Location References:
    ✓ location_id is unique
    ✓ location.connected_to references valid location_ids
    ✓ NEW: location_id (if used as UID) is consistent across references
  
  Quest Relationship References:
    ✓ quest_relationship.quest_id references valid quest
    ✓ trigger.target (NPC) references valid npc_id
    ✓ trigger.target (quest) references valid quest_id
    ✓ trigger.target (location) references valid location_id
    ✓ No circular dependencies (quest A unlocks B unlocks A)
    ✓ NEW: STATE_CHANGE blocks reference valid targets
  
  Interactable Object References:
    ✓ object.location references valid location_id or quest_id
    ✓ object_id is unique within location
    ✓ combat_effect references valid game mechanics

ERRORS:
  ❌ Broken reference: Quest "[quest_name]" references non-existent location "[location_id]"
  ❌ Duplicate ID: quest_id "[id]" used multiple times
  ❌ Orphaned content: NPC "[npc_name]" at non-existent location "[location_id]"
  ❌ Circular dependency: Quest chain A→B→C→A detected
  ❌ Missing target: Relationship targets "[target_id]" which doesn't exist
  ❌ UID mismatch: Reference uses "[uid]" but entity has "[different_uid]"
```

---

### 3. Reusable Components Validation (ERROR/WARNING) - NEW v2.0

```
VALIDATE: Reusable_Components_Library
CHECKS:
  Structure:
    ✓ All mechanic_ids are unique
    ✓ All encounter_ids are unique
    ✓ All hazard_ids are unique
    ✓ Mechanic blocks have all required fields
    ✓ Encounter blocks have all required fields
    ✓ Hazard blocks have all required fields
  
  References:
    ✓ All mechanic references ([MECHANIC: id]) point to defined mechanics
    ✓ All encounter references ([ENCOUNTER: id]) point to defined encounters
    ✓ All hazard references ([HAZARD: id]) point to defined hazards
    ✓ No undefined component references
  
  Consistency:
    ✓ Referenced mechanics have consistent parameters across uses
    ✓ Inline modifications clearly state what they're modifying
    ✓ Components marked as "based_on" reference existing components
  
  Usage:
    ✓ Defined components are actually used (not orphaned)
    ✓ Components used 3+ times are properly abstracted
    ✓ Components used only once should be inline (not abstracted)

ERRORS:
  ❌ Undefined component: Quest references [MECHANIC: psychic_zone] which doesn't exist
  ❌ Duplicate component_id: [mechanic_id] defined multiple times
  ❌ Orphaned component: [MECHANIC: underwater_pressure] defined but never used
  ❌ Invalid inline modification: "based_on" references undefined component
  ❌ Inconsistent parameters: [MECHANIC: id] used with DC 15 and DC 20 without modification

WARNINGS:
  ⚠️ Under-abstracted: Mechanic appears 4 times inline but not in reusable library
  ⚠️ Over-abstracted: Component defined but only used once (should be inline)
  ⚠️ Inconsistent modifications: Same modification applied in multiple places (should be base value)
```

---

### 4. Conditional Logic Validation (ERROR/WARNING) - NEW v2.0

```
VALIDATE: Conditional_Logic_Blocks
CHECKS:
  Structure:
    ✓ All CONDITIONAL_LOGIC blocks have matching END_CONDITIONAL_LOGIC
    ✓ All blocks have valid if/then/else structure
    ✓ Condition expressions are valid
    ✓ Both branches have valid state changes
  
  Logic:
    ✓ No contradictory conditions (A AND NOT A)
    ✓ No impossible conditions (requires flag that can't be set)
    ✓ All referenced flags/quests/conditions exist
    ✓ Nested conditions don't exceed 3 levels (readability)
  
  Flow:
    ✓ All possible outcomes are defined
    ✓ No unreachable branches
    ✓ Conditions can actually be evaluated by orchestrator
    ✓ Branch outcomes are meaningful and distinct
  
  Coverage:
    ✓ Important player choices have conditional logic
    ✓ Multiple solution quests branch appropriately
    ✓ Moral choices have distinct consequences

ERRORS:
  ❌ Contradictory condition: IF lighthouse_saved AND NOT lighthouse_saved
  ❌ Impossible condition: Requires quest_a_complete before quest_a is available
  ❌ Undefined reference: Condition checks flag "[flag]" which is never set
  ❌ Missing branch: CONDITIONAL_LOGIC has "if" but no "else" branch
  ❌ Malformed expression: Condition syntax invalid
  ❌ Orphaned logic: CONDITIONAL_LOGIC block never triggered

WARNINGS:
  ⚠️ Deep nesting: Conditional logic nested 4+ levels (hard to follow)
  ⚠️ Trivial branch: Both outcomes are nearly identical
  ⚠️ Missing consequence: Important choice has no conditional logic
  ⚠️ Unreachable branch: Condition can never be true given quest flow
```

---

### 5. Temporal Triggers Validation (ERROR/WARNING) - NEW v2.0

```
VALIDATE: Temporal_Triggers
CHECKS:
  Structure:
    ✓ All TEMPORAL_TRIGGER blocks properly formatted
    ✓ Delay values are valid (sessions or in-game time)
    ✓ Conditions are valid
    ✓ Triggered state changes are valid
  
  Sequence:
    ✓ No temporal paradoxes (trigger A at session 5 requires B at session 7)
    ✓ Delays are reasonable for campaign length
    ✓ Triggers don't stack impossibly (5 triggers firing same session)
    ✓ Prerequisites are met before trigger can fire
  
  Logic:
    ✓ Condition flags are set before trigger delay
    ✓ Triggered content (quests, events) exists
    ✓ Multiple triggers don't conflict
    ✓ Triggers have meaningful impact (not redundant)
  
  Tracking:
    ✓ Campaign save data includes temporal trigger tracking
    ✓ DM guidance mentions checking triggers between sessions
    ✓ Trigger priority is clear when multiple fire simultaneously

ERRORS:
  ❌ Temporal paradox: Trigger requires flag set after trigger fires
  ❌ Invalid delay: Delay of "15 sessions" but campaign is 12 sessions
  ❌ Missing content: Trigger unlocks quest "[id]" which doesn't exist
  ❌ Untrackable condition: Condition references state that isn't persisted
  ❌ Conflicting triggers: Two triggers set same flag to different values

WARNINGS:
  ⚠️ Short delay: Trigger fires 1 session after quest (might not be noticed)
  ⚠️ Long delay: Trigger fires 8 sessions later (players may forget context)
  ⚠️ Trigger cascade: 4+ triggers fire same session (overwhelming)
  ⚠️ Redundant trigger: Effect already achieved through other means
  ⚠️ Missing urgency: Time-sensitive quest has no actual pressure
```

---

### 6. Balance Validation (WARNING)

```
VALIDATE: Game Balance
CHECKS:
  XP Progression:
    ✓ Total XP available matches level range expectations
    ✓ Quest XP scales appropriately with recommended level
    ✓ No massive XP jumps between quests
  
  Encounter Difficulty:
    ✓ CR ratings match recommended party level
    ✓ No impossible encounters (CR 10 for level 3 party)
    ✓ Boss encounters are challenging but beatable
    ✓ NEW: Reusable encounters scale appropriately
  
  Treasure Distribution:
    ✓ Gold rewards scale with level
    ✓ Magic items are appropriate rarity for level
    ✓ Not too generous (100,000 gp at level 3)
    ✓ Not too stingy (10 gp for deadly encounter)
  
  Quest Difficulty Curve:
    ✓ Easy quests lead to medium quests lead to hard quests
    ✓ No sudden difficulty spikes
    ✓ Level recommendations are consistent
    ✓ NEW: Conditional branches maintain balanced difficulty

WARNINGS:
  ⚠️ XP imbalance: Party might reach level [X] too early/late
  ⚠️ Deadly encounter: "[encounter]" CR [X] for level [Y] party (may TPK)
  ⚠️ Treasure spike: Quest "[name]" gives [X]gp, [Y]% of expected campaign total
  ⚠️ Difficulty spike: Quest "[name]" is much harder than previous quests
  ⚠️ Conditional imbalance: "Then" branch much easier than "else" branch
```

---

### 7. Completeness Validation (WARNING)

```
VALIDATE: Content Completeness
CHECKS:
  Quest Completeness:
    ✓ All quests have objectives
    ✓ All quests have rewards
    ✓ All quests have at least one encounter or challenge
    ✓ Quest descriptions are present
    ✓ Quest givers have personalities defined
    ✓ NEW: Quest hooks have emotional beat tags
    ✓ NEW: State changes are defined for quest outcomes
  
  Location Completeness:
    ✓ All locations have descriptions
    ✓ Locations with quests have enough detail
    ✓ Major locations have multiple areas defined
  
  NPC Completeness:
    ✓ All NPCs have personality traits
    ✓ Quest-giving NPCs have dialogue samples
    ✓ Important NPCs have goals and motivations
    ✓ NEW: Key NPC moments have emotional beat tags
  
  Monster Completeness:
    ✓ All referenced monsters have stat blocks or MM references
    ✓ Custom monsters have complete stats
    ✓ Tactics are defined for important encounters
    ✓ NEW: Reusable encounters have tactics defined

WARNINGS:
  ⚠️ Sparse content: Quest "[name]" has minimal description
  ⚠️ Flat NPC: "[npc_name]" has no personality traits
  ⚠️ Missing tactics: Encounter "[name]" has no tactical guidance
  ⚠️ Placeholder content: "[item]" description is incomplete
  ⚠️ Missing emotional beats: Key NPC moment has no emotional guidance
  ⚠️ Missing state changes: Quest completion has no consequences
```

---

### 8. Quest Relationships Validation v3.0 (ERROR/WARNING)

```
VALIDATE: Quest_Relationships_v3
CHECKS:
  Structure:
    ✓ All quest_ids in relationships exist
    ✓ All targets (NPCs, quests, locations) exist
    ✓ Effect structures are valid for effect type
    ✓ Visibility values are valid (announced/silent/discovered)
    ✓ NEW: STATE_CHANGE blocks properly formatted
    ✓ NEW: All STATE_CHANGE blocks have END_STATE_CHANGE
  
  Logic:
    ✓ Conditional relationships have valid conditions
    ✓ Quest chains are possible (prerequisites exist)
    ✓ No impossible conditions (requires quest A and NOT quest A)
    ✓ Quest unlocks happen at appropriate levels
    ✓ NEW: STATE_CHANGE effects are internally consistent
  
  Consequences:
    ✓ Failure consequences are defined (if applicable)
    ✓ Economic effects are reasonable (not 1000x price change)
    ✓ Relationship changes are reasonable (-10 to +10 range)
    ✓ World changes have descriptions
    ✓ NEW: State changes actually modify tracked state
  
  Narrative:
    ✓ Announced effects have narrative text
    ✓ Discovery effects have hints for players
    ✓ Silent effects are logged for DM reference
    ✓ NEW: Narrative guidance matches emotional beats

ERRORS:
  ❌ Invalid target: Relationship references "[target]" which doesn't exist
  ❌ Impossible condition: Requires "[quest_a]" AND NOT "[quest_a]"
  ❌ Missing effect: Relationship type "[type]" has no effect object
  ❌ Malformed effect: npc_reaction missing relationship_change value
  ❌ Unclosed block: STATE_CHANGE missing END_STATE_CHANGE
  ❌ Invalid state reference: Effect modifies state "[flag]" that isn't tracked

WARNINGS:
  ⚠️ Extreme value: Price modifier of [X] seems excessive
  ⚠️ Missing narrative: Announced effect has no narrative text
  ⚠️ Orphaned relationship: Quest "[name]" triggers nothing and isn't triggered
  ⚠️ One-way relationship: Quest A affects B, but B never affects A (might be intentional)
  ⚠️ Inconsistent tone: Narrative doesn't match emotional beat tags
```

---

### 9. Interactable Object Validation (ERROR/WARNING)

```
VALIDATE: Interactable Objects
CHECKS:
  Structure:
    ✓ All object_ids are unique within location
    ✓ All locations referenced exist
    ✓ Visibility structure is valid
    ✓ Interaction structures complete
    ✓ NEW: OBJECT_METADATA blocks properly formatted
    ✓ NEW: INTERACTION blocks properly formatted
  
  Requirements:
    ✓ Skill DCs are reasonable (5-25 range)
    ✓ Required tools/spells exist in game
    ✓ Ability checks reference valid abilities
  
  Effects:
    ✓ Damage dice are valid (1d6, 2d8, etc.)
    ✓ Save DCs are reasonable for level
    ✓ Combat effects reference valid mechanics
    ✓ Area descriptions are clear
  
  Balance:
    ✓ Objects don't trivialize encounters
    ✓ DCs match expected party level
    ✓ Damage is appropriate for level
    ✓ Success/failure both have outcomes
  
  Usability:
    ✓ Descriptions are clear
    ✓ Objects are actually visible/findable
    ✓ Multiple interaction types encourage creativity
    ✓ Failure states allow retries (unless intentional)

ERRORS:
  ❌ Invalid reference: Object in "[location]" which doesn't exist
  ❌ Invalid mechanic: Damage type "[type]" doesn't exist
  ❌ Missing effect: on_success has no narrative or effect
  ❌ Duplicate ID: object_id "[id]" used twice in same location
  ❌ Unclosed metadata: OBJECT_METADATA missing END_OBJECT_METADATA

WARNINGS:
  ⚠️ Extreme DC: DC [X] might be too easy/hard for this quest level
  ⚠️ Overpowered: Object deals [X] damage (may one-shot encounter)
  ⚠️ Hidden object: Investigation DC [X] means players likely won't find this
  ⚠️ Single-solution: Only one interaction type (consider adding alternatives)
  ⚠️ No retry: Failure blocks progress with no retry allowed
```

---

### 10. Emotional/Narrative Beats Validation (WARNING/INFO) - NEW v2.0

```
VALIDATE: Emotional_Narrative_Beats
CHECKS:
  Coverage:
    ✓ Quest hooks have emotional beat tags
    ✓ Phase transitions have narrative beat tags
    ✓ Climactic moments have intensity tags
    ✓ Important NPC interactions have emotional guidance
  
  Consistency:
    ✓ Emotional arc escalates appropriately across campaign
    ✓ Intensity levels match content (no "mild" for final boss)
    ✓ Tone tags match campaign's established tone
    ✓ Pacing tags create varied rhythm (not all "fast")
  
  Structure:
    ✓ EMOTIONAL_BEAT blocks properly formatted
    ✓ NARRATIVE_BEAT blocks properly formatted
    ✓ Valid emotion types used
    ✓ Valid intensity levels used
    ✓ Valid tone/pacing values used
  
  Guidance:
    ✓ Narrative guidance is actionable
    ✓ Emotional beats support storytelling
    ✓ Key moments are appropriately tagged
    ✓ Beats don't contradict each other

WARNINGS:
  ⚠️ Missing emotional beats: Quest hook has no emotional guidance
  ⚠️ Flat arc: No intensity escalation across campaign
  ⚠️ Tone mismatch: "lighthearted" beat in "horror" campaign
  ⚠️ Pacing monotony: All beats marked "fast" (no variety)
  ⚠️ Unclear guidance: Narrative guidance too vague to be useful
  ⚠️ Excessive tagging: Beat tagged on every minor interaction (diminishes impact)

INFO:
  ℹ️ Consider: Adding emotional beat to [important moment]
  ℹ️ Suggestion: Vary pacing - too many consecutive "fast" beats
  ℹ️ Enhancement: Quest climax could use intensity increase
  ℹ️ Polish: Narrative guidance could be more specific
```

---

## VALIDATION REPORT FORMAT v2.0

```markdown
# CAMPAIGN VALIDATION REPORT v2.0
**Campaign**: [campaign_name]
**File**: [campaign_module_path]
**Template Version**: 3.0
**Validated**: [timestamp]
**Validator Version**: 2.0

---

## SUMMARY

**Status**: PASS | FAIL | PASS WITH WARNINGS

**Counts**:
- CRITICAL Issues: [X]
- ERROR Issues: [X]
- WARNING Issues: [X]
- INFO Suggestions: [X]

**Level -1: Legal/SRD Compliance**: [✅ PASS - SRD COMPLIANT | ❌ FAIL - LEGAL ISSUES]
- SRD Creature Compliance: [PASS | FAIL] ([X] creatures validated, [Y] forbidden)
- SRD Spell Compliance: [PASS | FAIL] ([X] spells validated, [Y] non-SRD)
- SRD Magic Item Compliance: [PASS | FAIL] ([X] items validated, [Y] non-SRD)
- Forbidden Entity Detection: [PASS | FAIL] ([X] locations/deities/factions checked)

**NEW v3.0 Feature Status**:
- Reusable Components: [VALID | ISSUES FOUND]
- Conditional Logic: [VALID | ISSUES FOUND]
- Temporal Triggers: [VALID | ISSUES FOUND]
- Emotional Beats: [VALID | SUGGESTIONS]

---

## LEVEL -1: LEGAL/SRD COMPLIANCE

[This section appears FIRST - blocks deployment if ANY check fails]

### Check 0: SRD Creature Compliance
[✅ PASS | ❌ FAIL]
- Total creatures validated: [X]
- Forbidden creatures found: [Y] (if > 0, CRITICAL)
- Custom creatures: [Z] (properly marked with source: "Custom")

**Issues Found** (if any):
❌ CRITICAL: Forbidden creature "[name]" at line [X] (use [alternative])
❌ ERROR: Non-SRD creature "[name]" without source attribution

### Check 1: SRD Spell Compliance
[✅ PASS | ❌ FAIL]
- Total spells validated: [X]
- Non-SRD spells found: [Y] (if > 0, CRITICAL)
- Custom spells: [Z] (properly marked)

**Issues Found** (if any):
❌ CRITICAL: Non-SRD spell "[spell_name]" at line [X]
❌ ERROR: Spell level mismatch for "[spell_name]"

### Check 2: SRD Magic Item Compliance
[✅ PASS | ❌ FAIL]
- Total items validated: [X]
- Non-SRD items found: [Y] (if > 0, CRITICAL)
- Custom items: [Z] (properly marked)

**Issues Found** (if any):
❌ CRITICAL: Non-SRD item "[item_name]" at line [X]
❌ ERROR: Rarity mismatch for "[item_name]"

### Check 3: Forbidden Entity Detection
[✅ PASS | ❌ FAIL]
- Locations checked: [X]
- Deities referenced: [Y]
- Factions referenced: [Z]
- Forbidden references found: [N] (if > 0, CRITICAL)

**Issues Found** (if any):
❌ CRITICAL: Forbidden location "[location]" at line [X]
❌ CRITICAL: Forbidden deity "[deity]" referenced in NPC dialogue
❌ CRITICAL: Forbidden faction "[faction]" at line [X]

---

## CRITICAL ISSUES (Must Fix)

[If any exist, campaign cannot be deployed]

### Schema Structure
❌ [Issue description]
   File: [location]
   Fix: [specific fix needed]

---

## ERRORS (Should Fix)

[Campaign will load but features won't work correctly]

### Reference Validation
❌ [Issue description]
   File: [location]
   Fix: [specific fix needed]

### Reusable Components (NEW)
❌ [Issue description]
   Component: [component_id]
   Fix: [specific fix needed]

### Conditional Logic (NEW)
❌ [Issue description]
   Location: [quest/block]
   Fix: [specific fix needed]

### Temporal Triggers (NEW)
❌ [Issue description]
   Trigger: [trigger_id]
   Fix: [specific fix needed]

---

## WARNINGS (Should Review)

[Campaign works but may have quality issues]

### Balance Validation
⚠️ [Issue description]
   Quest: [quest_name]
   Recommendation: [adjustment suggestion]

### Completeness
⚠️ [Issue description]
   Location: [where]
   Recommendation: [what to add]

### Emotional Beats (NEW)
⚠️ [Issue description]
   Location: [where]
   Recommendation: [enhancement suggestion]

---

## INFO (Suggestions)

[Best practices and polish suggestions]

ℹ️ [Suggestion]
   Location: [where]
   Enhancement: [optional improvement]

---

## DETAILED VALIDATION RESULTS

### 1. Schema Structure (v3.0)
**Status**: PASS | FAIL
**Issues**: [X]

[Detailed breakdown]

### 2. References
**Status**: PASS | FAIL
**Issues**: [X]

[Detailed breakdown]

### 3. Reusable Components (NEW)
**Status**: PASS | FAIL
**Issues**: [X]

**Statistics**:
- Mechanics defined: [X]
- Mechanics referenced: [X] times
- Encounters defined: [X]
- Hazards defined: [X]
- Orphaned components: [X]
- Under-abstracted patterns: [X]

[Detailed breakdown]

### 4. Conditional Logic (NEW)
**Status**: PASS | FAIL
**Issues**: [X]

**Statistics**:
- Conditional blocks: [X]
- Total branches: [X]
- Contradictions found: [X]
- Unreachable branches: [X]

[Detailed breakdown]

### 5. Temporal Triggers (NEW)
**Status**: PASS | FAIL
**Issues**: [X]

**Statistics**:
- Active triggers: [X]
- Temporal paradoxes: [X]
- Conflicting triggers: [X]
- Average delay: [X] sessions

[Detailed breakdown]

### 6. Balance
**Status**: PASS | FAIL WITH WARNINGS
**Issues**: [X]

**Statistics**:
- Total XP: [X] (target: [Y])
- Encounter balance: [breakdown]
- Magic items: [count by rarity]

[Detailed breakdown]

### 7. Completeness
**Status**: PASS | FAIL WITH WARNINGS
**Issues**: [X]

[Detailed breakdown]

### 8. Quest Relationships (v3.0)
**Status**: PASS | FAIL
**Issues**: [X]

**Statistics**:
- Total relationships: [X]
- STATE_CHANGE blocks: [X]
- Circular dependencies: [X]
- Orphaned quests: [X]

[Detailed breakdown]

### 9. Interactable Objects
**Status**: PASS | FAIL
**Issues**: [X]

[Detailed breakdown]

### 10. Emotional/Narrative Beats (NEW)
**Status**: PASS | FAIL WITH WARNINGS
**Issues**: [X]

**Statistics**:
- Quest hooks tagged: [X]/[total]
- Phase transitions tagged: [X]/[total]
- NPC moments tagged: [X]/[total]
- Intensity distribution: [breakdown]

[Detailed breakdown]

---

## QUALITY SCORE

**Overall**: [score]/100

Component scores:
- Schema: [score]/10
- References: [score]/15
- Reusable Components: [score]/10 (NEW)
- Conditional Logic: [score]/10 (NEW)
- Temporal Triggers: [score]/10 (NEW)
- Balance: [score]/15
- Completeness: [score]/15
- Relationships: [score]/10
- Objects: [score]/5
- Emotional Beats: [score]/10 (NEW)

---

## RECOMMENDATIONS

[Prioritized list of improvements]

**High Priority** (Fix before release):
1. [Recommendation with specific location and fix]
2. [Recommendation]

**Medium Priority** (Should fix):
1. [Recommendation]
2. [Recommendation]

**Low Priority** (Nice to have):
1. [Recommendation]
2. [Recommendation]

**Polish** (Optional enhancements):
1. [Suggestion for v3.0 features]
2. [Narrative/emotional beat improvements]

---

## V3.0 FEATURE UTILIZATION

**Reusable Components**:
- Utilization rate: [X]% (components used / total patterns)
- Recommendation: [suggestions for improvement]

**Conditional Logic**:
- Branching coverage: [X]% of quests have conditional outcomes
- Recommendation: [suggestions for adding meaningful choices]

**Temporal Triggers**:
- World reactivity: [X] delayed consequences
- Recommendation: [suggestions for living world feel]

**Emotional Beats**:
- Coverage: [X]% of key moments tagged
- Recommendation: [suggestions for narrative enhancement]

---

## DEPLOYMENT READINESS

✅ **READY FOR DEPLOYMENT**
   Campaign passed validation with no critical errors.
   Template v3.0 compliant.
   [X] warnings present - review before release.

OR

❌ **NOT READY FOR DEPLOYMENT**
   Fix [X] critical issues and [Y] errors before deploying to players.
   Template v3.0 features need attention.

---

**Generated by**: CAMPAIGN_VALIDATOR v2.0
**Validation took**: [X] seconds
**Template validated against**: ORCHESTRATOR_CAMPAIGN_TEMPLATE v3.0
```

---

## USAGE INSTRUCTIONS

### For Campaign Designers (You)

**Step 1: Run Validator**
```bash
# Command-line usage (conceptual)
validate_campaign CAMPAIGN_dragon_of_icespire_peak.md \
  --template-version 3.0 \
  --output report.md \
  --strict
```

**Step 2: Review Report**
- Fix all CRITICAL issues (campaign won't load otherwise)
- Fix all ERROR issues (features won't work)
- Review WARNING issues (quality/balance)
- Consider INFO suggestions (best practices)
- Review NEW v3.0 feature validation results

**Step 3: Re-validate**
```bash
validate_campaign CAMPAIGN_dragon_of_icespire_peak.md --quick
```

**Step 4: Deploy to Players**
Once validation passes with no critical/error issues, the campaign is ready for players.

---

### Validation Modes

**--strict** (Default)
- All checks enabled including v3.0 features
- Fails on any error
- Detailed report

**--quick**
- Critical and error checks only
- Fast validation
- Summary report

**--balance-only**
- Only runs balance checks
- For iterating on difficulty
- Quick feedback

**--v3-features-only** (NEW)
- Only validates reusable components, conditional logic, temporal triggers
- For iterating on v3.0 enhancements
- Faster than full validation

**--report-format [md|json|html]**
- Markdown (human-readable)
- JSON (tool integration)
- HTML (web viewing with flowcharts)

---

## VALIDATION CHECKLIST v2.0

Before releasing a campaign to players:

**Standard Checks:**
- [ ] Run full validation (--strict mode)
- [ ] Fix all CRITICAL issues
- [ ] Fix all ERROR issues
- [ ] Review and address WARNING issues
- [ ] Test at least one quest end-to-end
- [ ] Verify quest relationships trigger correctly
- [ ] Verify interactable objects work as intended
- [ ] Check XP progression matches level range
- [ ] Review encounter balance for expected party size
- [ ] Ensure all NPCs have distinct personalities
- [ ] Verify all magic items have complete properties
- [ ] Test save/resume with campaign module
- [ ] Re-run validation after fixes (should pass clean)

**NEW v3.0 Checks:**
- [ ] Verify reusable components are properly referenced
- [ ] Test conditional logic branches make sense
- [ ] Validate temporal trigger sequences
- [ ] Review emotional beat coverage for key moments
- [ ] Check narrative guidance is actionable
- [ ] Ensure template v3.0 format is maintained
- [ ] Verify STATE_CHANGE blocks are properly closed
- [ ] Test conditional logic doesn't have contradictions
- [ ] Confirm temporal triggers don't create paradoxes
- [ ] Review intensity escalation across campaign

---

## COMMON ISSUES AND FIXES v2.0

### Issue: Broken Quest Reference
```
❌ ERROR: Quest "mountains_toe_mine" references location "mine_entrance" which doesn't exist
```
**Fix**: Add location or fix quest.location field
```yaml
locations:
  - location_id: mine_entrance  # Add missing location
    name: "Mine Entrance"
    ...
```

### Issue: Undefined Reusable Component (NEW)
```
❌ ERROR: Quest references [MECHANIC: psychic_zone] which isn't defined
```
**Fix**: Add component to reusable library
```markdown
[REUSABLE_MECHANICS]

[MECHANIC: psychic_zone]
name: "Psychic Damage Zone"
trigger: "Every 10ft of movement"
save: "Wisdom DC 15"
...
```

### Issue: Contradictory Conditional Logic (NEW)
```
❌ ERROR: Conditional logic has impossible condition: IF lighthouse_saved AND NOT lighthouse_saved
```
**Fix**: Correct the condition logic
```markdown
[CONDITIONAL_LOGIC]
if: lighthouse_saved
then:
  [STATE_CHANGE: ally_gained]
  ...
else:
  [STATE_CHANGE: ally_lost]
  ...
[END_CONDITIONAL_LOGIC]
```

### Issue: Temporal Paradox (NEW)
```
❌ ERROR: Temporal trigger fires at session 5 but requires quest completed at session 7
```
**Fix**: Adjust trigger timing or prerequisites
```markdown
[TEMPORAL_TRIGGER]
delay: 3_sessions  # Changed from 2 to allow quest completion
condition: required_quest_complete
...
[END_TEMPORAL_TRIGGER]
```

### Issue: Missing Emotional Beat (WARNING) (NEW)
```
⚠️ WARNING: Quest climax has no emotional beat tag
```
**Fix**: Add appropriate emotional beat
```markdown
[EMOTIONAL_BEAT: quest_climax]
emotion: triumph
intensity: intense
narrative_guidance: "Build tension before reveal, then release with victory"
[END_EMOTIONAL_BEAT]
```

### Issue: Unclosed STATE_CHANGE Block (NEW)
```
❌ ERROR: STATE_CHANGE block missing END_STATE_CHANGE at line 234
```
**Fix**: Add closing tag
```markdown
[STATE_CHANGE: consequence]
type: npc_reaction
target: merchant_guild
effect:
  relationship_change: +2
visibility: announced
narrative: "The guild thanks you publicly..."
[END_STATE_CHANGE]  # Add this
```

### Issue: Orphaned NPC
```
⚠️ WARNING: NPC "norbus_ironrune" at location "excavation" which isn't defined
```
**Fix**: Add location or move NPC
```yaml
npcs:
  - npc_id: norbus_ironrune
    location: dwarven_excavation  # Fix to existing location
```

### Issue: Balance Problem
```
⚠️ WARNING: Quest "easy_quest" gives 5000 XP (party might overlevel)
```
**Fix**: Adjust XP or redistribute across quests
```yaml
quests:
  - quest_id: easy_quest
    rewards:
      xp_total: 500  # Reduced from 5000
```

### Issue: Circular Dependency
```
❌ ERROR: Circular quest dependency: A requires B, B requires C, C requires A
```
**Fix**: Break the cycle
```yaml
quest_relationships:
  - quest_id: quest_c
    triggers_on_complete:
      - type: quest_unlock
        target: quest_a  # Remove this unlock to break cycle
```

---

## INTEGRATION WITH DEVELOPMENT WORKFLOW v2.0

```
┌────────────────────────────────┐
│  1. Create Campaign Content    │
│     (Using template v3.0)      │
└────────────────────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  2. Run Campaign Validator v2  │
│     (This tool)                │
│     --template-version 3.0     │
└────────────────────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  3. Review v3.0 Feature Report │
│     (Reusable, Conditional,    │
│      Temporal, Emotional)      │
└────────────────────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  4. Fix Issues & Enhance       │
│     (Address errors + polish)  │
└────────────────────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  5. Iterate Until Clean        │
│     (Re-validate with v2.0)    │
└────────────────────────────────┘
                │
                ▼
┌────────────────────────────────┐
│  6. Deploy to Players          │
│     (Agent orchestrator)       │
└────────────────────────────────┘
```

---

## AUTOMATED CHECKS

The validator can be integrated into CI/CD:

```yaml
# Example GitHub Action for v2.0
name: Validate Campaign v3.0
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Validate Campaign Module
        run: |
          python campaign_validator_v2.py \
            CAMPAIGN_dragon_of_icespire_peak.md \
            --template-version 3.0 \
            --strict \
            --fail-on-error
      - name: Validate v3.0 Features
        run: |
          python campaign_validator_v2.py \
            CAMPAIGN_dragon_of_icespire_peak.md \
            --v3-features-only \
            --report-format json
      - name: Upload Report
        uses: actions/upload-artifact@v2
        with:
          name: validation-report-v2
          path: validation_report.md
```

---

## VERSION HISTORY

**v2.0** (November 17, 2025)
- NEW: Template v3.0 support
- NEW: Reusable components validation
- NEW: Conditional logic validation
- NEW: Temporal triggers validation
- NEW: Emotional/narrative beats validation
- Enhanced STATE_CHANGE block validation
- Updated report format for v3.0 features
- Added v3.0 feature utilization metrics

**v1.0** (November 17, 2025)
- Initial release
- Schema validation
- Reference validation
- Balance validation
- Quest relationship validation
- Interactable object validation
- Markdown report generation

**Future Enhancements**:
- [ ] Interactive conditional logic flowchart generation
- [ ] Temporal trigger timeline visualization
- [ ] Emotional arc visualization across campaign
- [ ] JSON/HTML report formats with interactive features
- [ ] Auto-fix suggestions for common v3.0 issues
- [ ] Playtest simulation with conditional branches
- [ ] Performance profiling
- [ ] Localization checks

---

## NOTES FOR DEVELOPERS

This validator v2.0 is designed to be:
- **Comprehensive**: Catches design errors before runtime, including v3.0 features
- **Fast**: Runs in seconds even on large v3.0 campaigns
- **Actionable**: Provides specific fixes, not just errors
- **Extensible**: Easy to add new validation rules for future template versions
- **v3.0-Aware**: Understands reusable components, conditional logic, temporal triggers

**Not a replacement for**:
- Manual testing (playtest your campaign, especially conditional branches!)
- Human judgment (balance is subjective, emotional beats are artistic)
- Creative iteration (validator can't judge "fun" or narrative quality)

**Best used for**:
- Catching stupid mistakes (broken references, unclosed blocks)
- Enforcing standards (schema compliance, v3.0 format)
- Quality assurance (completeness checks, emotional beat coverage)
- Balance guidelines (XP/CR checks, conditional branch balance)
- v3.0 Feature validation (reusable components, logic consistency)

---

## V3.0 SPECIFIC VALIDATION NOTES

### Reusable Components
The validator checks:
- All referenced components are defined
- No orphaned components (defined but unused)
- Consistent usage across references
- Appropriate abstraction level (not over/under-abstracted)

### Conditional Logic
The validator ensures:
- No logical contradictions
- All branches are reachable
- Conditions can be evaluated
- Both outcomes are meaningful

### Temporal Triggers
The validator verifies:
- No temporal paradoxes
- Reasonable timing for campaign length
- Prerequisites met before firing
- Proper tracking in save data

### Emotional Beats
The validator reviews:
- Coverage of key moments
- Intensity escalation across campaign
- Consistency with established tone
- Actionable narrative guidance

---

**END OF CAMPAIGN VALIDATOR DOCUMENTATION v2.0**

This tool ensures campaign quality and v3.0 template compliance before player deployment.  
Agent orchestrator handles runtime execution.  
Keep them separate.

**Validator v2.0 validates Template v3.0 campaigns.**

---
