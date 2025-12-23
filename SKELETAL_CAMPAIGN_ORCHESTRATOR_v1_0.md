# SKELETAL CAMPAIGN ORCHESTRATOR v1.0

**Design Philosophy:** Minimal specification, maximum emergent gameplay. This orchestrator provides the *rules* and *feedback loops* of a campaign world, not the *narrative*. The DM agent must reason within constraints, not execute predetermined branches.

---

# ⚠️ CRITICAL DEPENDENCY: CONTEXT WEAVING

**This is not optional.** Skeletal campaigns REQUIRE hyperactive context weaving or they collapse into incoherence.

## Why Context Weaving is Load-Bearing

Comprehensive campaigns hide state in pre-written branches. Skeletal campaigns have no safety net.

If the DM agent loses track of:
- What reputation gate was triggered 3 sessions ago
- Which NPC's motivations shifted based on party choices
- What world state changed from a decision
- How faction interactions cascaded

...the game becomes broken. It devolves into reasoning about "what makes sense now" without actually knowing what *became true*.

**Solution:** Weaponized context weaving that surfaces state constantly.

---

# SECTION 0: FRAMEWORK PRINCIPLES

## Core Thesis

**Old Model (Comprehensive):** Campaign file specifies 80% of narrative content
- Result: DM agent pattern-matches, loses responsiveness, breaks when party deviates
- Problem: Feels less like playing D&D and more like reading flowcharts

**New Model (Skeletal):** Campaign file specifies 20% (rules + skeleton + feedback loops)
- Result: DM agent must reason, ask clarifying questions, discover consequences
- Benefit: More dynamic, responsive, player-driven gameplay emerges naturally

## Design Constraints

1. **No pre-written dialogue** - Only character motivations and personality templates
2. **No location descriptions** - Only mechanical function and what can be there
3. **No quest branches** - Only faction goals and consequence triggers
4. **No encounter stat blocks** - Only difficulty guidelines and enemy *types* (not specifics)
5. **No predetermined outcomes** - Only what changes the world based on choices

## What We KEEP Specified

1. **World Rules** - How the setting actually works (magic system, faction mechanics, economy)
2. **Feedback Loops** - Explicit reputation math, consequence triggers, state changes
3. **Character Templates** - Motivations, goals, constraints (but not dialogue)
4. **Encounter Types** - "This situation spawns X difficulty challenge" (not detailed encounters)
5. **Decision Points** - Explicit moments where DM MUST stop and ask player for input

---

# SECTION 1: CAMPAIGN SKELETON

## Campaign Name
[Fill in: One-sentence campaign premise]

### Story Spine (3-5 bullet points MAX)
- [What kicks off the adventure]
- [What major change happens midway]
- [What climax looms]

**That's it.** No filler, no detailed plot hooks.

### Theme & Tone (2-3 sentences)
[What emotional experience should this feel like?]

### Party Level Range
[Start → End]

---

# SECTION 2: WORLD RULES

## 2A. Faction Mechanics

### Faction Template
```yaml
faction_name: [Name]
faction_motivation: [One sentence: What do they WANT?]
faction_constraint: [One sentence: What stops them from just taking it?]

reputation_math:
  starting_value: 0
  scale: -10 to +10 (or appropriate range)
  
reputation_triggers:
  positive:
    - [Action that increases reputation]: +[amount]
    - [Action that increases reputation]: +[amount]
  
  negative:
    - [Action that decreases reputation]: -[amount]
    - [Action that decreases reputation]: -[amount]
  
  neutral:
    - [Action that doesn't change it]: +0

world_state_changes:
  at_reputation_5: [What becomes available?]
  at_reputation_-5: [What becomes hostile?]
  at_reputation_10: [What becomes true?]
  
# Add more factions below
```

### Faction Interaction Matrix
```
        | Faction A | Faction B | Faction C
--------|-----------|-----------|----------
Faction A|     -     |   [+1]    |   [-2]
Faction B|   [+1]    |     -     |   [+0]
Faction C|   [-2]    |   [+0]    |     -
```

*If party gains rep with A, what happens to B and C?*

## 2B. Economy & Resources

### Currency & Pricing
[What's the baseline economy? What does 1gp buy?]

### Supply & Scarcity
[What's abundant? What's rare? What's forbidden?]

### Consequence Chain
[If party spends X gold, what happens? Who notices? What changes?]

## 2C. Magic System Rules

### What Magic Can Do
[Explicit list of what's possible]

### What Magic Cannot Do
[Hard constraints]

### Consequence of Magic Use
[Who detects it? What's the fallout?]

## 2D. Social & Combat Rules

### NPC Reaction Triggers
[What makes NPCs trust/distrust/fear party?]

### Combat Difficulty Scaling
- **Easy:** [What does this feel like in narrative?]
- **Medium:** [What does this feel like?]
- **Hard:** [What does this feel like?]
- **Deadly:** [What does this feel like?]

### Resources That Matter
[HP, spells, gold, ammunition, provisions—which ones actually constrain player choices?]

---

# SECTION 3: CHARACTER TEMPLATES (NOT Stat Blocks)

## Major NPC Template

```yaml
npc_name: [Name]
role: [What are they? What do they do?]

motivation: [One sentence: What do they want?]
constraint: [One sentence: Why can't they just take it?]
personality_keywords: [3-5 words describing how they act]

goals_short_term: 
  - [What are they trying to do right now?]
  - [What's their next move if uninterrupted?]

goals_long_term:
  - [What are they working toward over months/years?]

relationship_with_party:
  current_standing: [+/-/0]
  triggers_trust: [What would make them trust party?]
  triggers_hostility: [What would make them enemies?]
  
dialogue_template:
  when_first_meeting: "[Describe tone, not words. E.g., 'Wary but professional']"
  when_angry: "[Tone description]"
  when_negotiating: "[Tone description]"

key_secret: [One secret that could change everything if revealed]
```

### Companion NPC Template
```yaml
companion_name: [Name]
why_join_party: [One sentence: Why would they travel with adventurers?]
why_leave_party: [One sentence: When would they abandon the group?]

core_conflict: [One sentence: Their internal struggle]
party_interaction: [How do they relate to PCs? Dynamic description, not rules]

combat_role: [What do they do in a fight?]
resource_state: [How much HP, spells, etc. do they have relative to PCs?]
```

---

# SECTION 4: ENCOUNTER FRAMEWORK (Not Stat Blocks)

## Encounter Trigger Template

```yaml
situation_name: [What is this encounter?]
trigger_condition: [When does this encounter activate?]
difficulty_rating: [Easy/Medium/Hard/Deadly]

enemy_composition:
  - [Type 1]: [Description of role, NOT stats. E.g., "Ranged attackers"]
  - [Type 2]: [Description of role]
  
environment:
  terrain: [What's the layout?]
  hazards: [What can hurt/help?]
  escape_routes: [How can this end without total death?]

resolution_outcomes:
  party_victory: [What happens if party wins? What changes?]
  party_defeat: [What happens if party loses? What changes?]
  party_negotiates: [Can this be avoided? What would it cost?]
  party_flees: [Can they run? What's the consequence?]
```

## Encounter Difficulty Guidelines

**Easy:** Party should win easily without resource expenditure  
**Medium:** Party uses some resources, gets scratched but fine  
**Hard:** Party uses significant resources, maybe 1 character drops  
**Deadly:** Party might lose, should flee/negotiate, not guaranteed victory  

---

# SECTION 5: DECISION POINT FRAMEWORK

## Structured Decision Points

Every time party makes a choice that affects world state:

```yaml
decision_point_name: [What's being decided?]
player_options:
  option_A: [Brief description of choice]
  option_B: [Brief description of choice]
  option_C: [Brief description of choice]
  option_D: "[Custom choice allowed]"

consequences_for_reputation:
  option_A:
    faction_X: [+/- amount]
    faction_Y: [+/- amount]
  
  option_B:
    faction_X: [+/- amount]
    faction_Y: [+/- amount]

consequences_for_world:
  option_A: "[What becomes true? What closes? What opens?]"
  option_B: "[What becomes true? What closes? What opens?]"

immediate_effect:
  option_A: "[What happens RIGHT NOW?]"
  option_B: "[What happens RIGHT NOW?]"

delayed_consequences:
  option_A: 
    - "[If X, then Y happens next session]"
    - "[If Z, then W happens later]"
  option_B:
    - "[...]"
```

---

# SECTION 6: WORLD STATE TRACKING

## Campaign Flag System

```yaml
story_flags:
  [flag_name]: false  # Boolean: has this happened yet?
  [flag_name]: false
  [flag_name]: false

time_sensitive_events:
  [event_name]: 
    trigger_date: [In-game day when this activates]
    consequence: "[What happens if party doesn't intervene?]"

active_threats:
  [threat_name]:
    current_danger_level: 1-10
    what_makes_it_worse: "[Party action X increases danger]"
    what_reduces_it: "[Party action Y decreases danger]"
```

## Reputation Score Summary

```yaml
factions:
  [faction_A]: 0
  [faction_B]: 0
  [faction_C]: 0

reputation_gates:
  faction_A_at_5: "[What becomes available?]"
  faction_A_at_-5: "[What becomes hostile?]"
  faction_B_at_3: "[What becomes available?]"
  # etc
```

---

# SECTION 7: SESSION PREP CHECKLIST

Before each session:

- [ ] Review all active reputation scores
- [ ] Check which story flags are true
- [ ] Identify next 2-3 decision points
- [ ] Read NPC motivations (not dialogue)
- [ ] Review faction interaction matrix—what's shifted?
- [ ] Identify what world changes should be visible this session
- [ ] Prepare 2-3 encounter difficulty levels (let player choice determine which)

---

# SECTION 8: DM REASONING FRAMEWORK

When party does something unexpected:

1. **Check faction motivations** - How would each faction react?
2. **Check reputation gates** - What becomes available/hostile?
3. **Check story flags** - Does this change anything?
4. **Apply reputation math** - What's the consequence?
5. **Update world state** - What becomes true now?
6. **Present outcome** - Tell player what they see/hear

**Never consult a pre-written branch.** Reason from first principles.

---

# SECTION 8.5: CONTEXT WEAVING FOR SKELETAL CAMPAIGNS

**MANDATE:** Every DM output must surface ONE active consequence of previous decisions. This is the skeleton's immune system.

## Hyperactive Context Weaving Protocol

### TIER 0 (Every Output - MANDATORY)
Surface the **single most relevant piece of state** that affects current decision:

**Examples:**
- "The duergar merchant's eyes narrow—you're at +2 reputation with his guild, which means he remembers your last deal."
- "Velryn would never negotiate with the surface elves. You know this about her because House Shadowveil has blood vendetta."
- "The revolutionary flag is visible in the town square—the rebellion won that vote last week, which is why the nobles withdrew their garrison."
- "The innkeeper glances nervously at your party. Last session, you sided with the duergar. Word spread. The gnome refugees won't come here anymore."

**What this does:**
- Grounds current scene in past decisions
- Reminds player their choices matter
- Prevents world from feeling inconsistent

### TIER 1 (Every 1-2 interactions)
Weave in the **active reputation scores** for factions about to interact:

**Examples:**
- "The Nobility contact arrives. [They're at -3 with you—hostile ground, but not actively attacking]"
- "The Guild representative seems calculating. [You're at +1 with them—marginally profitable, but not trusted enough to get discounts]"

**What this does:**
- Makes reputation scores feel real in narration
- Signals what's possible (trust gates, hostility thresholds)

### TIER 2 (Every 2-3 interactions)
Surface **what consequences cascaded** from last decision:

**Examples:**
- "Since you allied with the duergar, the gnome refugees organized an underground route that bypasses duergar territory. Three groups have already left."
- "Gralk seems more relaxed around camp. Your treatment of deep gnome prisoners bought you +1 with him. He noticed, and he's starting to believe you're different from other surface folk."
- "The military garrison is visibly depleted. Your tip to the nobles about rebel positions caused them to dispatch half their forces. The town feels less secure now."

**What this does:**
- Shows that decisions ripple outward
- Reveals unintended consequences
- Makes world feel alive and reactive

### TIER 3 (Every 3-4 interactions)
Remind of **world state changes**—what became true and stays true:

**Examples:**
- "The old mine entrance is still sealed from your side. The shadow you left behind still patrols it. That's not changing unless you go back."
- "The cult's influence in Thornhearth is weaker now. You killed two of their agents. The survivors are in hiding, but they're still recruiting in the outer settlements."
- "The Bridge District is under Revolutionary control now. You can't go through there if you're wanted by the Nobility."

**What this does:**
- Establishes permanent world changes
- Prevents retcon of past sessions
- Creates persistent tactical/political constraints

### TIER 4 (Every 4-5 interactions)
Surface **active threats**—what's escalating or de-escalating:

**Examples:**
- "The duergar hunting party hasn't returned in 3 days. Either your +5 reputation scared them off from retaliation, or they found something worse underground."
- "The revolutionary cell has been quiet. Too quiet. Either they're planning something, or the Nobility's campaign against them is working."
- "Plague deaths in the outer settlement are declining. The poultice your healer distributed is actually working. The population is starting to trust the Nobility again."

**What this does:**
- Signals emerging threats and opportunities
- Creates narrative tension
- Suggests what might happen next

---

## State Validation Protocol (Before Every Output)

Before narrating ANYTHING, the DM must validate:

```yaml
pre_output_validation:
  reputation_scores:
    - faction_A: [current value]
    - faction_B: [current value]
    - faction_C: [current value]
    "Question: Is this consistent with last session?"
  
  active_world_flags:
    - flag_1: [true/false]
    - flag_2: [true/false]
    "Question: Did a recent decision change any of these?"
  
  recent_decisions:
    - session_X: "[What did party choose?]"
    - session_Y: "[What did party choose?]"
    "Question: What consequences should be visible now?"
  
  escalating_threats:
    - threat_1: [danger level 1-10]
    - threat_2: [danger level 1-10]
    "Question: Should any threat level change based on party actions?"
  
  de_escalating_elements:
    - element_1: "[What became safer?]"
    - element_2: "[What became safer?]"
    "Question: Should party see evidence this worked?"

consistency_check:
  - Is this narration consistent with last weaved context?
  - Did I accidentally contradict something from 2 sessions ago?
  - Does this consequence follow from reputation math?
  - Would this NPC act this way given current reputation with faction?
```

If ANY validation fails: **HALT and rewind**. Surface the contradiction, ask player for clarification.

---

## Context Weaving in Different Scenarios

### In Combat
- Surface faction allegiance when enemies appear: "[These duergar are recognizing you—you're at -1 with them, so they're cautious but not hostile]"
- Weave threat escalation into enemy behavior: "[Their reinforcements are coming because last session you publicly defeated their captain]"

### In Negotiation
- Lead with reputation: "[The merchant remembers you from the caravan deal 3 sessions ago. +2 reputation means they expect profit, not betrayal]"
- Surface faction interaction: "[This NPC works for Faction A, which is at -3 with you but +2 with Faction B. They're walking a careful line]"

### In Exploration
- Weave world state into description: "[The settlement looks different. Since you sided with the rebels, the Nobility withdrew their banners. The revolution's symbol is up instead]"
- Surface consequences: "[The innkeeper won't serve your party anymore. Word got out about your massacre of neutral NPCs]"

### In Social Encounters
- Lead with relationship state: "[This NPC is at +4 reputation with you—they're willing to take risks for you now]"
- Show faction pressure: "[This NPC wants to help, but Faction B owns them. You'd need to do something to break that hold]"

---

## Integration with Skeletal Campaign Framework

For campaigns built on this framework, explicitly include:

```yaml
context_weaving_requirements:
  tier_0_mandatory: true
  
  tier_0_triggers:
    - Every DM output MUST surface ONE active consequence
    - Examples in world:
      - NPC whose rep just changed
      - World state that became true last decision
      - Faction interaction that cascaded
      - Threat level escalation/de-escalation
  
  state_validation_before_every_output: true
  
  consistency_check_mandatory: true
  
  what_to_track:
    - All reputation scores (with values)
    - All active story flags (with true/false)
    - All recent party decisions (last 3 sessions minimum)
    - All active threats (with danger levels)
    - All de-escalating elements (what's safer now?)
```

---

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

# SECTION 10: ORCHESTRATOR INTEGRATION

This skeletal structure integrates with the D&D 5E Orchestrator:

**Decision Point Protocol stays the same:**
- Present numbered options
- End with question
- ⛔ STOP, WAIT for input
- Execute only chosen action

**Ambient Context Weaving stays the same:**
- Surface reputation scores naturally
- Weave world state into narration
- Rotate what context gets highlighted

**What changes:**
- No consultation of pre-written branches
- No "running" predetermined encounters
- Reasoning happens in real-time from rules + world state
- Consequences emerge from reputation math + faction logic
- NPCs act from motivation + current circumstances, not scripts

---

# SECTION 10: ORCHESTRATOR INTEGRATION

This skeletal structure integrates with the D&D 5E Orchestrator:

**Decision Point Protocol stays the same:**
- Present numbered options
- End with question
- ⛔ STOP, WAIT for input
- Execute only chosen action

**Ambient Context Weaving becomes CRITICAL:**
- NOT optional for skeletal campaigns
- Surface reputation scores naturally
- Weave world state into narration
- Rotate what context gets highlighted (use TIER 0-4 framework)
- Validate all state before every output
- Surface consequences of recent decisions

**What changes:**
- No consultation of pre-written branches
- No "running" predetermined encounters
- Reasoning happens in real-time from rules + world state
- Consequences emerge from reputation math + faction logic
- NPCs act from motivation + current circumstances, not scripts
- **CRITICAL:** Context weaving prevents world from becoming incoherent

**The dependency chain:**
```
Skeletal Campaign Structure
    ↓
Requires reasoning from rules/feedback loops (no rails)
    ↓
Requires accurate state tracking (no narratives to hide inconsistency)
    ↓
Requires hyperactive context weaving (constantly surface state)
    ↓
Result: Game stays coherent while remaining emergent
```

Without context weaving, skeletal campaigns fail. This is load-bearing.

---

# SECTION 11: EXAMPLE CAMPAIGN SKELETON

## Campaign: The Shattered Court
**Premise:** Political intrigue in a crumbling empire where three factions vie for control.

### Story Spine
- Empire's central authority collapses
- Three factions emerge: Nobility, Guild, Revolutionary
- Party must choose sides or forge third path
- Final decision determines empire's future

### World Rules (Abbreviated)

**Faction: Nobility**
- Motivation: Preserve hierarchy
- Constraint: Losing military control
- Rep triggers: Help nobles stay in power (+2), work with commoners (-1)
- Rep gate at 5: Access to noble resources
- Rep gate at -5: Hunted as traitor

**Faction: Guild**
- Motivation: Control trade/wealth
- Constraint: No military power
- Rep triggers: Profit guild (+2), undercut their deals (-2)
- Rep gate at 5: Guild provides information network
- Rep gate at -5: Guild assassins deploy

**Faction: Revolutionary**
- Motivation: Overthrow all hierarchy
- Constraint: Outnumbered and hunted
- Rep triggers: Help revolution (+2), ally with nobles (-3)
- Rep gate at 5: Revolution shares rebel base location
- Rep gate at -5: Revolution executes party for betrayal

### Decision Point: First Faction Contact
```yaml
party_meets_representatives_from_all_three_factions

option_A: "Ally with Nobility"
  consequences:
    nobility: +3
    guild: -1
    revolutionary: -2
  world: "[Nobles give safe passage through their territories]"

option_B: "Ally with Guild"
  consequences:
    nobility: -1
    guild: +3
    revolutionary: -1
  world: "[Guild controls party's access to black market]"

option_C: "Remain neutral"
  consequences:
    nobility: +0
    guild: +0
    revolutionary: +0
  world: "[All three factions watch party carefully, less trustful]"
```

---

# SECTION 12: USAGE NOTES

- **For New Campaign Creation:** Fill in Sections 1-6. Sections 7-12 are templates
- **For Session Prep:** Use Section 7 checklist
- **During Play:** Reference Section 8 reasoning framework
- **When Party Surprises You:** Never hunt for a pre-written response. Use Section 8.
- **Session End:** Export using Section 9 format

---

# SECTION 13: MIGRATION NOTES

**Converting from Comprehensive Campaign File:**
1. Delete all pre-written dialogue
2. Delete all detailed location descriptions (keep mechanical function only)
3. Delete all quest branches
4. Delete all encounter stat blocks (keep difficulty + role descriptions)
5. Extract NPC motivation/constraint/goal into templates
6. Extract faction goals into reputation math
7. Identify decision points and consequence chains
8. Build feedback loops explicitly

**Result:** Campaign shrinks from 1,800 lines to 300-500 lines. Much more playable.

---

# FILE METADATA

```yaml
document_name: "Skeletal_Campaign_Orchestrator_v1_0.md"
version: 1.0
status: TEMPLATE_READY
purpose: "Framework for creating campaign files that enable AI reasoning instead of narrative execution"

design_principles:
  - Minimal specification (20% detail, 80% emergent)
  - Explicit feedback loops (reputation math, consequence chains)
  - Intentional gaps (force reasoning over pattern-matching)
  - Rule-based world (faction motivations, not predetermined outcomes)
  - Hyperactive context weaving (load-bearing dependency)

critical_dependencies:
  context_weaving: "MANDATORY - Without it, game loses coherence"
  reputation_tracking: "MANDATORY - Core to all decisions"
  world_state_validation: "MANDATORY - Before every DM output"
  consequence_surfacing: "MANDATORY - Tie every narration to past decisions"

integration:
  compatible_with: "CORE_DND5E_AGENT_ORCHESTRATOR_v6_8_0"
  required_protocols: "Player Agency, Decision Point Framework, Ambient Context Weaving (TIER 0-4)"
  
usage_ready: true

notes:
  - "This framework prioritizes coherence through aggressive state tracking"
  - "Skeletal design only works if context weaving is hyperactive"
  - "Validate all state before every output or world becomes incoherent"
  - "No safety net: every consequence must be traced and surfaced"
```

---

**END OF SKELETAL CAMPAIGN ORCHESTRATOR v1.0**

*Use this framework to build campaigns that emerge from player choice, not predetermined narrative.*
