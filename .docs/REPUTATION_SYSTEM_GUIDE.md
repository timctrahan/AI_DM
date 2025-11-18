# REPUTATION SYSTEM GUIDE
**For Campaign Designers**  
**Version**: 1.0  
**Created**: November 17, 2025

---

## OVERVIEW

The Reputation System replaces static alignment with dynamic relationship tracking. Characters build (or destroy) relationships with NPCs, factions, and regions based on their actions, creating a living world that remembers and reacts.

---

## THREE REPUTATION TYPES

### 1. NPC Relationships (Individual)
**Scale**: -10 (Hated) to +10 (Beloved)  
**Purpose**: Track how individual NPCs feel about the character  
**Effects**: Dialogue options, quest availability, prices, assistance

### 2. Faction Standing (Organizational)
**Scale**: -10 (Enemy) to +10 (Leader)  
**Purpose**: Track standing with groups/organizations  
**Effects**: Ranks, resources, missions, organizational support

### 3. Regional Fame/Infamy (Public)
**Scale**: 0-100 for both Fame and Infamy  
**Purpose**: Track public reputation in regions  
**Effects**: Recognition, prices, guard reactions, random encounters

---

## NPC REPUTATION SYSTEM

### Reputation Scale

```
-10 to -8: HATED
  - NPC refuses to interact
  - May attack on sight
  - Reports to authorities
  - Spreads negative rumors

-7 to -5: HOSTILE
  - Actively works against character
  - Refuses service
  - Demands exorbitant prices (2x-3x)
  - Warns others about character

-4 to -2: DISLIKED
  - Cold, unhelpful
  - Higher prices (1.2x-1.5x)
  - Won't go out of their way
  - Remembers past slights

-1 to +1: NEUTRAL
  - Standard interactions
  - Normal prices
  - No special treatment
  - Fresh start possible

+2 to +4: LIKED
  - Friendly, helpful
  - Small discounts (0.9x)
  - Offers information freely
  - Gives benefit of doubt

+5 to +7: FRIENDLY
  - Goes out of their way to help
  - Good discounts (0.75x)
  - Offers side quests
  - Warns of dangers

+8 to +10: BELOVED
  - Considers character close friend
  - Major discounts (0.5x)
  - Shares secrets
  - Takes risks to help
  - Offers unique rewards
```

### How to Change NPC Reputation

**In Quest Relationships**:
```yaml
quest_relationships:
  - quest_id: butterskull_ranch
    triggers_on_complete:
      - type: npc_reaction
        target: big_al_kalazorn
        effect:
          relationship_change: +3
          dialogue_unlock: "grateful_response"
        visibility: announced
```

**In Campaign Events**:
- Completing quests for NPC: +1 to +3
- Saving NPC's life: +3 to +5
- Protecting NPC's family: +3 to +5
- Keeping promises: +1
- Giving gifts: +1 to +2
- Defending NPC's honor: +2

**Negative Changes**:
- Failing quests: -1 to -2
- Breaking promises: -2
- Lying (when caught): -1 to -3
- Stealing from NPC: -3 to -5
- Threatening NPC: -2 to -4
- Harming NPC's loved ones: -5 to -8
- Killing NPC's allies: -4 to -7

### Campaign Integration Example

```yaml
# In quest definition
quest: rescue_alfonse_family
  on_success:
    npc_reputation_changes:
      - npc: big_al_kalazorn
        change: +3
        reason: "Saved my family from orcs"
      
      - npc: alfonse_jr
        change: +5
        reason: "Risked life to rescue me"
  
  on_failure:
    npc_reputation_changes:
      - npc: big_al_kalazorn
        change: -5
        reason: "Failed to save my family"
```

---

## FACTION STANDING SYSTEM

### Faction Scale

```
-10 to -8: ENEMY
  - Faction actively hunts character
  - Assassins/bounty hunters sent
  - Barred from faction locations
  - Allied factions may turn hostile

-7 to -5: OPPOSED
  - Faction works against character
  - No services available
  - Intelligence gathered on character
  - Warns allied factions

-4 to -2: UNFRIENDLY
  - Faction distrusts character
  - Limited services at high cost
  - No promotions possible
  - Closely watched

-1 to +1: NEUTRAL
  - No affiliation
  - Standard services (if public)
  - Recruitment possible
  - Fresh slate

+2 to +4: AFFILIATED
  - Member or ally
  - Basic services available
  - Minor missions offered
  - Access to faction resources

+5 to +7: TRUSTED
  - Valued member
  - Important missions
  - Faction support in conflicts
  - Discount on services

+8 to +10: LEADERSHIP
  - High rank in faction
  - Major decision-making power
  - Faction resources at disposal
  - Can call on faction aid
```

### Faction Ranks Example

```yaml
faction: harpers
  ranks:
    - name: "Watcher"
      reputation_required: 2
      benefits:
        - "Access to Harper safehouses"
        - "Basic intelligence sharing"
    
    - name: "Harpshadow"
      reputation_required: 5
      benefits:
        - "Can requisition equipment"
        - "Backup from local Harpers"
    
    - name: "Brightcandle"
      reputation_required: 8
      benefits:
        - "Command Harper agents"
        - "Access to faction treasury"
        - "Vote on Harper policies"
```

### How to Change Faction Standing

**Positive Changes**:
- Completing faction missions: +1 to +3
- Major victories for faction: +2 to +4
- Protecting faction members: +2
- Recruiting new members: +1
- Donating resources: +1 to +2

**Negative Changes**:
- Failing faction missions: -1 to -3
- Betraying faction secrets: -5 to -8
- Attacking faction members: -4 to -7
- Working for rival factions: -1 to -3
- Refusing critical missions: -2

---

## REGIONAL FAME/INFAMY SYSTEM

### Fame (Positive Reputation)

```
0-10: UNKNOWN
  - Nobody knows who you are
  - Normal prices
  - No special treatment

11-25: RECOGNIZED
  - Some people have heard of you
  - Occasional free drinks
  - Guards may nod in recognition

26-50: FAMOUS
  - Well known in region
  - 10% discount on goods/services
  - People ask for autographs
  - Guards let minor issues slide

51-75: RENOWNED
  - Celebrated hero
  - 20% discount
  - Free lodging at inns
  - Guards provide escort
  - Quest givers seek you out

76-100: LEGENDARY
  - Living legend
  - 30% discount
  - Statues erected in your honor
  - Guards protect you
  - Parade when you arrive
  - Regional rulers grant audience
```

### Infamy (Negative Reputation)

```
0-10: CLEAN RECORD
  - No criminal record
  - Normal guard interactions

11-25: SUSPICIOUS
  - Guards watch you closely
  - Shopkeepers count their inventory
  - 10% markup on prices

26-50: WANTED
  - Bounty on your head
  - Guards attempt arrest
  - 25% markup on prices
  - Some services refused

51-75: NOTORIOUS
  - Large bounty
  - Bounty hunters actively hunt you
  - 50% markup (black market)
  - Most services refused
  - Barred from establishments

76-100: INFAMOUS
  - Massive bounty
  - Kill-on-sight orders
  - Can't enter towns freely
  - Black market only (2x-3x prices)
  - Faction armies may mobilize
```

### Fame/Infamy Can Coexist

A character can be famous AND infamous:
- Fame 60, Infamy 40: "Famous outlaw"
- Fame 30, Infamy 70: "Villainous but impressive"
- Fame 80, Infamy 10: "Hero with minor scandal"

### How to Change Regional Fame/Infamy

**Increase Fame**:
- Save town from danger: +10 to +20
- Defeat major threat: +15 to +30
- Complete multiple quests: +5 to +10
- Public acts of heroism: +5 to +15
- Donations to community: +3 to +5

**Increase Infamy**:
- Murder innocents: +20 to +40
- Major theft: +10 to +20
- Betray community: +15 to +25
- Work for villains: +5 to +15
- Commit war crimes: +30 to +50

**Reduce Infamy**:
- Pay fines: -5 to -10
- Complete penance quests: -10 to -20
- Jail time: -15 to -30
- Heroic redemption act: -20 to -40

---

## ALIGNMENT TENDENCY (Behavioral Tracking)

**NOT A RESTRICTION** - This is purely for roleplay flavor and NPC reactions.

### What It Tracks

```yaml
alignment_tendency:
  recent_actions:
    - action: "Spared defeated enemy who begged for mercy"
      context: "Could have killed for gear, chose mercy"
      timestamp: "2025-11-17"
    
    - action: "Kept promise to help farmer despite better pay elsewhere"
      context: "Honor over profit"
      timestamp: "2025-11-18"
  
  behavior_summary: >
    Character tends toward mercy and keeping oaths. Values honor and 
    compassion but isn't naive. Pragmatic when necessary.
```

### How AI Uses This

The AI DM references behavioral patterns when:
- NPCs describe the character to others
- Determining how NPCs react to character
- Creating rumors about the party
- Offering quests that match character values
- Generating dialogue that reflects character's reputation

**Example**:
```
NPC: "I've heard you're someone who keeps their word. I need someone 
I can trust with this delicate matter..."

vs.

NPC: "Word is you get results, but you're not too worried about the 
collateral. Perfect for what I need..."
```

---

## INTEGRATION WITH QUEST RELATIONSHIPS

The reputation system works seamlessly with quest relationships:

```yaml
quest_relationships:
  - quest_id: mountains_toe_mine
    triggers_on_complete:
      # This automatically calls Track_Reputation_Change
      - type: npc_reaction
        target: norbus_ironrune
        effect:
          relationship_change: +2
          dialogue_unlock: "partnership_offer"
      
      # You can also manually track in quest completion
      reputation_changes:
        npcs:
          - id: norbus_ironrune
            change: +2
            reason: "Cleared wererat infestation"
        
        factions:
          - id: miners_guild
            change: +1
            reason: "Secured valuable mine"
        
        regions:
          - id: phandalin
            fame_change: 5
            deed: "Defeated wererat pack leader Zeleen"
```

---

## BEST PRACTICES FOR CAMPAIGN DESIGNERS

### 1. Start Characters at Neutral (0)

Don't pre-load relationships. Let players earn them through play.

### 2. Make Reputation Changes Visible

```
Bad: [Reputation changed silently]
Good: "Big Al clasps your shoulder. 'You saved my family. I won't forget this.'"
```

### 3. Consequences Should Be Meaningful

```
+2 reputation: "Barthen gives you a friendly wave"
+5 reputation: "Barthen offers you his family heirloom as thanks"
+8 reputation: "Barthen risks his life to warn you of the assassins"
```

### 4. Negative Reputation Should Have Impact

```
-2 reputation: "Halia's smile doesn't reach her eyes"
-5 reputation: "Halia refuses to do business with you"
-8 reputation: "Halia hires thugs to teach you a lesson"
```

### 5. Regional Fame Creates Emergent Stories

```
Fame 60 in Phandalin:
- Free drinks at tavern
- Town guard escorts party
- Townmaster seeks counsel
- Vendors give discounts
- BUT: Enemies know where you are
```

### 6. Track Major Deeds

```yaml
regional_fame:
  - region_id: phandalin
    fame: 75
    known_for:
      - "Defeated the dragon Cryovain"
      - "Saved Butterskull Ranch from orcs"
      - "Cleared Mountain's Toe Mine of wererats"
      - "Restored prosperity to the region"
```

NPCs can reference these specific deeds in dialogue!

---

## EXAMPLE: Full Reputation Journey

### Session 1: First Contact
```
Harbin Wester: 0 (neutral, first meeting)
→ Party accepts quest
```

### Session 3: Quest Complete
```
Harbin Wester: +2 (liked)
→ "Excellent work! You're more capable than I expected."
→ Offers better quests
```

### Session 7: Major Achievement
```
Harbin Wester: +5 (friendly)
→ "I consider you friends of Phandalin now."
→ Free lodging at town hall
→ Introduces party to regional leaders
```

### Session 12: Hero Status
```
Harbin Wester: +8 (beloved)
→ "You're the best thing to happen to this town in years!"
→ Names street after party
→ Offers to adopt party members into family (half-joking)
→ Will risk political career to help party
```

---

## TROUBLESHOOTING

### "My players min-max reputation"

That's fine! Social engineering is a valid strategy. Make it interesting:
- High reputation with one faction may lower it with rivals
- Being beloved by everyone is suspicious
- Villains target popular heroes
- Fame brings unwanted attention

### "Reputation changes too fast"

Adjust the magnitude:
- Small actions: ±1
- Standard quests: ±2
- Major events: ±3
- Life-changing: ±5
- Legendary: ±8

### "Players want to reset reputation"

Redemption should be hard but possible:
- Penance quests
- Public apology
- Major sacrifice
- Time and good deeds
- Never instant

### "How do I track this?"

The orchestrator tracks it automatically:
- Character schema has reputation fields
- Protocols update automatically
- Save/resume preserves all reputation
- You just define when reputation changes

---

## SUMMARY

**Reputation System Benefits**:
- ✅ Dynamic world that remembers player actions
- ✅ Meaningful consequences without "alignment police"
- ✅ Natural quest chains based on relationships
- ✅ Emergent storytelling opportunities
- ✅ Players feel their choices matter
- ✅ NPCs feel alive and reactive
- ✅ No arbitrary restrictions on player behavior

**vs. Static Alignment**:
- ❌ Arbitrary 9-box grid
- ❌ "That's not lawful good!"
- ❌ Paladin falls for one lie
- ❌ No nuance or context
- ❌ Punitive rather than reactive

**Use reputation to create living worlds, not to restrict players.**

---

## QUICK REFERENCE CARD

```
NPC REPUTATION:
-10 = Hated      | -1 to +1 = Neutral    | +8 = Beloved
Effect: Dialogue, quests, prices, assistance

FACTION STANDING:
-10 = Enemy      | -1 to +1 = Neutral    | +8 = Leader
Effect: Rank, resources, missions, support

REGIONAL FAME/INFAMY:
0-25 = Unknown   | 26-50 = Famous        | 76-100 = Legendary
0-25 = Clean     | 26-50 = Wanted        | 76-100 = Infamous
Effect: Prices, guards, recognition, bounties

BEHAVIORAL TRACKING:
Recent actions tracked, patterns observed, used for NPC reactions
NOT enforced, purely for roleplay flavor
```

---

**END OF REPUTATION SYSTEM GUIDE**

Use reputation to make your campaign world feel alive!

---
