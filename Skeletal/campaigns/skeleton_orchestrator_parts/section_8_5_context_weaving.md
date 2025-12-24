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
