# DRAGON OF ICESPIRE PEAK - ENHANCEMENT EXAMPLES
**Purpose**: Concrete examples of Quest Relationships and Interactable Objects  
**Campaign**: Dragon of Icespire Peak  
**Version**: Enhancement Preview

---

## QUEST RELATIONSHIPS EXAMPLES

These would be added to CAMPAIGN_dragon_of_icespire_peak.md in a new section.

---

### Mountain's Toe Gold Mine Quest

```yaml
quest_relationships:
  - quest_id: mountains_toe_mine
    
    triggers_on_complete:
      # Norbus sees opportunity for partnership
      - type: npc_reaction
        target: norbus_ironrune
        condition: dwarven_excavation_complete
        effect:
          relationship_change: +2
          dialogue_unlock: partnership_offer
          quest_offer: joint_mining_venture
        visibility: announced
        narrative: >
          Two days after you clear the Mountain's Toe Mine, Norbus Ironrune 
          finds you at the Stonehill Inn. "Heard about your work at the mine," 
          he says with a grin. "That wererat problem you solved? That was Zeleen's 
          pack - they've been raiding claims for months. You and I should talk 
          business. With your muscle and my mining knowledge, we could open a 
          proper operation. What do you say to a partnership?"
      
      # Halia becomes jealous/competitive
      - type: npc_reaction
        target: halia_thornton
        effect:
          relationship_change: -1
          internal_state: competitive
          price_modifier_mining_supplies: 1.15
        visibility: discovered
        narrative: >
          [Players discover this through Halia's colder demeanor. When buying 
          mining-related supplies, she quotes higher prices. "Supply and demand," 
          she says curtly. Other NPCs mention she's upset about competition.]
      
      # Gold availability increases
      - type: world_change
        target: phandalin_region
        effect:
          flag: gold_rush_starting
          value: true
          description: "More prospectors arriving in Phandalin"
        visibility: discovered
        narrative: >
          [Over the next few sessions, players notice more dwarven prospectors 
          in town. Quest board has mining-related jobs. Elmar mentions 
          Phandalin is becoming a mining hub again.]
      
      # Unlocks advanced mining quest
      - type: quest_unlock
        target: quest_board
        condition: party_level_5_or_higher
        effect:
          quest_id: deep_veins
          announcement: >
            Norbus approaches with a map. "Found something deep in the 
            mountains - a vein of mithral. But it's in dangerous territory. 
            Interested in a real payday?"
        visibility: announced
    
    triggers_on_fail:
      # Zeleen escapes and continues raiding
      - type: world_change
        target: phandalin_region
        effect:
          flag: wererat_raids_active
          value: true
          description: "Wererat pack continues attacking claims"
        visibility: silent
        narrative: >
          [Manifests as increased random encounters with wererats. Prospectors 
          complain about raids. Some mining quests become more dangerous.]
      
      # Halia offers alternative deal (at cost)
      - type: npc_reaction
        target: halia_thornton
        effect:
          relationship_change: 0
          dialogue_unlock: alternative_mining_proposal
          quest_offer: halias_terms
        visibility: announced
        narrative: >
          "I heard you couldn't handle the wererat problem," Halia says with 
          a thin smile. "Perhaps you'd be interested in a different 
          arrangement. I have contacts who can... persuade Zeleen to leave. 
          For a price, of course."
```

---

### Butterskull Ranch Quest

```yaml
quest_relationships:
  - quest_id: butterskull_ranch
    
    triggers_on_complete:
      # Ranch becomes safe haven
      - type: location_change
        target: butterskull_ranch
        effect:
          status: safe_rest_location
          services_available: [free_lodging, safe_storage, horse_rental]
        visibility: announced
        narrative: >
          "You're heroes, all of you," Mayleen says, tears in her eyes. 
          "This ranch is your home anytime you need it. Free room and board, 
          and our horses are yours if you need them."
      
      # Big Al becomes staunch ally
      - type: npc_reaction
        target: big_al_kalazorn
        effect:
          relationship_change: +3
          emotional_state: deeply_grateful
          quest_offer: al_personal_favor
        visibility: announced
        narrative: >
          Big Al clasps your shoulder with his massive hand. "You saved my 
          family. I owe you a debt I can never repay. But if you ever need 
          the law to look the other way, or muscle for a dangerous job, 
          you call on me. No questions asked."
      
      # Orc threat reduced
      - type: world_change
        target: phandalin_region
        effect:
          flag: orc_aggression_level
          value: reduced
          description: "Orc raids decrease after warband defeated"
        visibility: silent
        narrative: >
          [Fewer random orc encounters. NPCs mention roads are safer. 
          Travelers more common on paths.]
    
    triggers_on_fail:
      # Family killed or captured
      - type: world_change
        target: phandalin_region
        effect:
          flag: kalazorn_family_status
          value: lost
          description: "Alfonse Jr. and family are gone"
        visibility: announced
        narrative: >
          When you return to Phandalin without the family, Big Al's face 
          goes white. He says nothing, just turns and walks away. The town 
          feels emptier, sadder. You've failed people who counted on you.
      
      # Big Al becomes broken
      - type: npc_reaction
        target: big_al_kalazorn
        effect:
          relationship_change: -4
          emotional_state: grieving_hostile
          location_change: leaves_phandalin
        visibility: announced
        narrative: >
          Big Al leaves Phandalin. Some say he went hunting orcs alone. 
          Others say he's drinking himself to death in Neverwinter. Either 
          way, Phandalin has lost its sheriff, and it's your fault.
      
      # Orc aggression increases
      - type: world_change
        target: phandalin_region
        effect:
          flag: orc_aggression_level
          value: increased
          description: "Emboldened orcs raid more frequently"
        visibility: silent
        narrative: >
          [More random orc encounters. Orcs attack Phandalin directly in 
          later sessions. NPCs live in fear. Roads become dangerous.]
      
      # Ranch becomes orc outpost
      - type: location_change
        target: butterskull_ranch
        effect:
          status: hostile_location
          occupants: orc_warband_expanded
        visibility: discovered
        narrative: >
          Travelers report the ranch is now an orc stronghold. Smoke rises 
          from the burning buildings. It's too late to save it now.
```

---

### Loggers' Camp Quest

```yaml
quest_relationships:
  - quest_id: loggers_camp
    
    triggers_on_complete:
      # Timber supply restored
      - type: price_change
        target: barthen_provisions
        effect:
          merchant: barthen_provisions
          category: wooden_items
          modifier: 0.75
        visibility: discovered
        narrative: >
          "Lumber's flowing again!" Elmar says cheerfully. "I can finally 
          get proper prices from my suppliers. Passing the savings to you, 
          of course."
      
      # Construction boom in Phandalin
      - type: world_change
        target: phandalin
        effect:
          flag: construction_active
          value: true
          description: "New buildings being constructed"
        visibility: discovered
        narrative: >
          When you return to Phandalin, you notice scaffolding on several 
          buildings. New construction has begun - a proper inn annex, 
          expanded smithy, and townmaster's hall improvements. The town 
          is growing.
      
      # Tibor becomes confident
      - type: npc_reaction
        target: tibor_wester
        effect:
          relationship_change: +2
          personality_shift: less_cowardly
          dialogue_unlock: tibor_brave_moment
        visibility: discovered
        narrative: >
          [In future encounters, Tibor stands a bit straighter. He even 
          volunteers for the town watch. "You showed me courage can be 
          learned," he says.]
      
      # Affects Falcon's Lodge quest
      - type: quest_unlock
        target: quest_board
        condition: party_level_5_or_higher
        effect:
          quest_id: rebuild_lodge
          announcement: >
            Tibor approaches with a proposal. "With lumber flowing, we 
            could rebuild Falcon's Lodge as a proper waystation. But we'd 
            need to clear it of those... things... first."
        visibility: announced
    
    affects_quests:
      # Makes Dragon's Lair slightly easier
      - quest_id: dragons_lair
        relationship: modifies
        modification:
          lumber_available: true
          benefit: >
            Party can request construction of siege equipment (ballista) 
            from Phandalin craftsmen for assault on Icespire Hold. 
            Costs 250 gp, takes 3 days to build.
```

---

## INTERACTABLE OBJECTS EXAMPLES

These would be added to quest location descriptions in the campaign module.

---

### Loggers' Camp - Tactical Combat Objects

```yaml
interactable_objects:
  
  # The signature tactical object
  - object_id: half_cut_tree
    location: loggers_camp_clearing
    name: "Precariously Leaning Tree"
    description: >
      A massive pine tree, half-cut by the loggers before they fled, 
      leans at a dangerous angle over the main clearing. The trunk is 
      a good two feet across, and saw marks show where the loggers 
      started their work before the ankhegs attacked. The tree creaks 
      ominously in the wind.
    visible: true
    
    interactions:
      - action: topple
        requirements:
          skill_check:
            skill: athletics
            dc: 14
            note: "Two characters can attempt together, each rolls DC 11"
        
        on_success:
          narrative: >
            You throw your weight against the massive trunk. Wood fibers 
            snap with sharp cracks as the tree slowly tips past its 
            balance point. Then gravity takes over. With a thunderous 
            CRASH that echoes through the forest, the pine slams into 
            the ground, sending up a cloud of pine needles, dirt, and 
            startled birds!
          
          combat_effect:
            area_damage:
              area: "10-foot-wide, 30-foot-long line from tree base"
              dice: "3d6"
              type: bludgeoning
              save:
                ability: dexterity
                dc: 13
              note: "Half damage on successful save"
            
            creates_terrain:
              type: difficult_terrain
              area: "30-foot line where tree fell"
              cover_type: half_cover
              note: >
                Creatures behind the fallen tree get half cover. 
                Climbing over requires 10 feet of movement.
            
            special_effect:
              condition: "If ankheg is in the line when tree falls"
              effect: >
                Ankheg is pinned under tree (restrained condition). 
                Can escape with STR DC 16 check as action, or allies 
                can lift tree with combined STR 28.
        
        on_failure:
          narrative: >
            The tree shudders and groans, showering you with loose bark, 
            but remains stubbornly upright. You need more force - maybe 
            help from allies, or a different approach like chopping more 
            of the base.
          penalty: none
          retry_allowed: true
      
      - action: climb
        requirements:
          skill_check:
            skill: athletics
            dc: 10
        
        on_success:
          narrative: >
            You scramble up the slanted trunk, using the rough bark for 
            handholds. From this elevated position, you have a commanding 
            view of the battlefield below.
          
          combat_effect:
            tactical_advantage:
              benefit: "Advantage on ranged attacks against ground targets"
              cover: "Half cover from ground-based attacks"
              height: "15 feet above ground"
              note: >
                Ankheg acid spray can still reach you. If tree is toppled 
                while you're on it, DC 12 DEX save or fall prone and take 
                1d6 damage.
        
        on_failure:
          narrative: >
            Your foot slips on loose bark and you slide back down, 
            scraping your hands.
          penalty:
            damage: "1d4 bludgeoning if failed by 5 or more"
          retry_allowed: true
  
  # Secondary tactical object
  - object_id: stacked_logs
    location: loggers_camp_clearing
    name: "Stack of Cut Logs"
    description: >
      A large pile of cut logs sits at the edge of the clearing, neatly 
      stacked but unstable. Each log is about six feet long and quite heavy.
    visible: true
    
    interactions:
      - action: topple_toward_enemies
        requirements:
          skill_check:
            skill: athletics
            dc: 12
        
        on_success:
          narrative: >
            You kick the support log out from under the stack. With a 
            rumbling crash, dozens of logs roll across the clearing toward 
            your enemies!
          
          combat_effect:
            area_damage:
              area: "15-foot cone"
              dice: "2d6"
              type: bludgeoning
              save:
                ability: dexterity
                dc: 12
            
            creates_terrain:
              type: difficult_terrain
              area: "15-foot cone scattered with logs"
              duration: "Until cleared"
        
        on_failure:
          narrative: >
            The logs shift but don't fall. You've made them more unstable 
            though - one more try should do it.
          penalty: none
          retry_allowed: true
  
  # Puzzle/utility object
  - object_id: logging_equipment
    location: loggers_camp_shed
    name: "Logger's Tools"
    description: >
      Inside the shed: axes, two-person saws, wedges, rope, and other 
      logging equipment. Professional quality.
    visible: true
    
    interactions:
      - action: take
        requirements: none
        
        on_success:
          narrative: >
            You collect useful tools from the shed. These could come in 
            handy.
          
          combat_effect: none
          
          world_state_change:
            items_acquired:
              - "Logging Axe (1d8 slashing, versatile 1d10, two-handed)"
              - "50 feet of sturdy rope"
              - "Iron wedges (useful for various tasks)"
            
            note: >
              These tools can be used later. The wedges can jam doors, 
              the rope enables climbing/binding, the axe is a weapon 
              or tool for chopping.
        
        on_failure: n/a
        retry_allowed: n/a
```

---

### Mountain's Toe Gold Mine - Trap & Tactical Objects

```yaml
interactable_objects:
  
  - object_id: mine_portcullis
    location: mountains_toe_main_chamber
    name: "Rusty Iron Portcullis"
    description: >
      A heavy iron portcullis guards the entrance to the deeper mine 
      shafts. It's currently raised, held by a corroded winch mechanism. 
      The rope looks frayed, and rust flakes off the iron bars.
    visible: true
    
    interactions:
      - action: drop_portcullis
        requirements:
          option_1:
            ability_check:
              ability: strength
              dc: 10
              note: "Turn the rusty winch"
          option_2:
            method: cut_rope
            note: "Automatic success with slashing weapon/damage"
        
        on_success:
          narrative: >
            [If winch] You wrench the rusted mechanism, and with a 
            shrieking groan of metal on stone, the portcullis drops!
            
            [If cut rope] Your blade parts the frayed rope, and the 
            portcullis falls with a tremendous CLANG!
          
          combat_effect:
            area_damage:
              area: "10-foot-wide gate opening"
              targets: "All creatures in area"
              dice: "3d10"
              type: bludgeoning
              save:
                ability: dexterity
                dc: 14
              additional: >
                On failed save, creature is also restrained (pinned 
                under portcullis)
            
            creates_barrier:
              type: impassable
              note: >
                Blocks passage completely. STR DC 20 to lift (allows 
                one Medium creature to squeeze through). Multiple 
                creatures can combine STR checks.
        
        on_failure:
          narrative: >
            [Only if using winch] The mechanism is rusted solid and 
            won't budge. You'll need to cut the rope instead.
          penalty: "Wasted action"
          retry_allowed: true
      
      - action: jam_mechanism
        requirements:
          tool_required: "Iron spike, piton, or similar wedge"
        
        on_success:
          narrative: >
            You wedge the spike into the winch's gear mechanism. The 
            portcullis is now locked in place - it won't drop unless 
            someone removes this spike.
          
          combat_effect:
            tactical_note: >
              Prevents Zeleen from dropping portcullis on party. She 
              knows this trap and will try to lure party under it if 
              it's still functional.
        
        on_failure: n/a
        retry_allowed: n/a
  
  - object_id: mine_cart
    location: mountains_toe_tunnels
    name: "Loaded Ore Cart"
    description: >
      A wooden mine cart filled with ore sits on rusty rails that slope 
      downward into the darkness. It looks like it could roll easily if 
      given a push.
    visible: true
    
    interactions:
      - action: push_down_slope
        requirements:
          skill_check:
            skill: athletics
            dc: 8
            note: "Easy - just need to overcome inertia"
        
        on_success:
          narrative: >
            You heave against the cart. It resists for a moment, then 
            wheels screech as it picks up speed, rumbling down the tracks 
            into the darkness with increasing velocity!
          
          combat_effect:
            area_damage:
              area: "5-foot-wide, 60-foot-long line (following tracks)"
              dice: "4d6"
              type: bludgeoning
              save:
                ability: dexterity
                dc: 14
              note: >
                Creatures can attempt to dodge aside. Those in narrow 
                tunnels have disadvantage on save.
            
            tactical_effect: >
              Cart smashes through weak supports at end of track, 
              potentially causing partial tunnel collapse (blocks 
              passage, creates cover, may damage enemies beyond).
        
        on_failure:
          narrative: >
            The cart barely budges - the wheels are more stuck than 
            you thought. You need to put your back into it.
          penalty: none
          retry_allowed: true
      
      - action: loot_ore
        requirements: none
        
        on_success:
          narrative: >
            You examine the ore in the cart. Looks like decent quality 
            gold ore - worth selling in Phandalin.
          
          world_state_change:
            items_acquired: "Gold ore (5 lbs, worth 25 gp to Halia)"
            note: >
              Can sell to Halia at Miner's Exchange. She'll offer fair 
              price if relationship is good, lowball if hostile.
```

---

### Umbrage Hill - Environmental Objects

```yaml
interactable_objects:
  
  - object_id: adabras_garden
    location: umbrage_hill
    name: "Adabra's Herb Garden"
    description: >
      A well-tended garden filled with medicinal herbs and healing plants. 
      Adabra has been cultivating these for years.
    visible: true
    
    interactions:
      - action: harvest_herbs
        requirements:
          option_1:
            skill_check:
              skill: nature
              dc: 12
              note: "Know which herbs are useful"
          option_2:
            skill_check:
              skill: medicine
              dc: 12
              note: "Know which herbs heal"
          option_3:
            condition: adabra_permits
              note: "She'll show you which to pick"
        
        on_success:
          narrative: >
            [If skill check] You identify several useful herbs - comfrey 
            for wounds, feverfew for illness, and valerian for calming.
            
            [If Adabra helps] "These here are good for healing," she says, 
            showing you which plants to harvest. "Take what you need, dears."
          
          world_state_change:
            items_acquired: "Healing Herbs (3 doses)"
            uses: >
              Can be used during short rest. One dose adds +2 to hit die 
              healing. Takes 10 minutes to prepare as poultice.
            
            adabra_reaction: >
              If taken with permission: +1 relationship. If taken without 
              asking: -1 relationship, she notices.
        
        on_failure:
          narrative: >
            You pick some plants, but you're not sure if these are the 
            right ones. Adabra gently corrects you. "Not those, dear - 
            those will give you a stomach ache!"
          penalty: none
          retry_allowed: true
  
  - object_id: cottage_roof
    location: umbrage_hill
    name: "Cottage Rooftop"
    description: >
      Adabra's cottage has a relatively low, accessible roof. A barrel 
      sits near the wall that could serve as a step up.
    visible: true
    
    interactions:
      - action: climb_roof
        requirements:
          skill_check:
            skill: athletics
            dc: 8
            note: "Easy climb with barrel assist"
        
        on_success:
          narrative: >
            You clamber onto the cottage roof. From up here, you have 
            a much better vantage point - and the manticore will have 
            to work harder to reach you.
          
          combat_effect:
            tactical_advantage:
              benefit: >
                High ground advantage on ranged attacks. Manticore must 
                fly or climb to reach you. You get three-quarters cover 
                from ground-based attacks.
              
              drawback: >
                If manticore stays airborne, it can attack without penalty. 
                Roof may not support multiple people (DM judgment).
        
        on_failure:
          narrative: >
            You slip on the thatch and slide back down. Try again?
          penalty: none
          retry_allowed: true
```

---

## HOW THESE ENHANCE THE CAMPAIGN

### Before Enhancements

**Quest Completion**:
```
Party completes Mountain's Toe Mine
→ Get XP, gold, thank you from Halia
→ Quest over, world unchanged
→ Next quest
```

**Environment Interaction**:
```
Player: "I want to push over that tree!"
DM: [Improvises] "Uh, sure, roll Athletics... DC 15?"
DM: [Improvises damage] "It deals... 2d6?"
DM: [Forgets about it next round]
```

### After Enhancements

**Quest Completion**:
```
Party completes Mountain's Toe Mine
→ Get XP, gold
→ QUEST CASCADE TRIGGERS:
   - Norbus offers partnership (if excavation done)
   - Halia becomes competitive (prices up)
   - Gold rush begins (more prospectors)
   - Deep Veins quest unlocks (at level 5)
→ World has changed
→ Next quest is different because of past choices
```

**Environment Interaction**:
```
Player: "I want to push over that tree!"
DM: CALL Object_Interaction protocol
→ Find half_cut_tree object
→ Require Athletics DC 14
→ On success: 3d6 damage in line, creates cover, can pin ankheg
→ Narrate dramatically
→ Update combat map
→ Consistent, balanced, memorable
```

---

## CONCLUSION

These enhancements transform Dragon of Icespire Peak from:
- ❌ Series of disconnected quests
- ❌ Static world
- ❌ Limited player creativity

Into:
- ✅ Living, reactive world
- ✅ Interconnected quest web
- ✅ Tactical environmental gameplay
- ✅ Meaningful consequences
- ✅ Memorable moments

All while maintaining:
- ✅ Consistent mechanics
- ✅ Predictable outcomes
- ✅ Easy validation
- ✅ Clear state tracking

---

**Next Step**: Implement these examples into the actual campaign module.

---
