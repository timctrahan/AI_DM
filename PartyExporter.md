1. OUT: "💾 GENERATING FULL-FIDELITY CHARACTER SHEET EXPORT"
2. OUT: "⚠️ Copy ALL text between the START/END markers for portability."

3. SELECT: target_list (IF 'PARTY', FOR EACH character IN party_state.characters; ELSE, target = requested character)

4. FOR EACH character IN target_list:
     OUT: ""
     OUT: "--- START OF CHARACTER EXPORT: [character.identity.name] ---"
     OUT: ""

     # A. IDENTITY & PROGRESSION
     OUT: "=== A. IDENTITY & PROGRESSION ==="
     OUT: "Name: [name] | Player: [PC/NPC] | Campaign ID: [campaign_id]"
     OUT: "Race: [race] | Class: [class] [level] | Subclass: [subclass/archetype] (If known)"
     OUT: "Background: [background] | Alignment: [alignment]"
     OUT: "Experience: [xp_current] / [xp_next_level] | Proficiency Bonus: +[proficiency_bonus]"
     OUT: "Movement Speed: [speed] ft | Darkvision: [range] ft (If any)"
     OUT: "Languages: [list of known languages]"
     OUT: ""

     # B. ABILITY SCORES & SAVES
     OUT: "=== B. ABILITY SCORES & SAVES ==="
     OUT: "| STAT | Score | Modifier | Save Proficient | Save Total |"
     OUT: "|:---|:---:|:---:|:---:|:---:|"
     FOR each ability IN abilities:
       OUT: "| [ability.name] | [score] | [modifier] | [save_proficient ? 'Yes' : 'No'] | [save_proficient ? (modifier+PB) : modifier] (+[Ring of Protection bonus IF exists]) |"
     OUT: "Passive Perception: [10 + WIS modifier + (skills.perception.proficient ? PB : 0)]"
     OUT: ""

     # C. COMBAT STATS & RESOURCES
     OUT: "=== C. COMBAT & DEFENSE ==="
     OUT: "Armor Class (AC): [armor_class] | Initiative: [initiative_bonus] | Reaction Available: [reaction_available ? 'Yes' : 'No']"
     OUT: "Hit Points: [hp_current] / [hp_max] | Temporary HP: [temp_hp]"
     OUT: "Hit Dice: [hit_dice_remaining] / [hit_dice_total] ([hit_dice_type])"
     OUT: "Death Saves: [death_saves.successes] Successes, [death_saves.failures] Failures"
     OUT: "Active Conditions: [conditions.active]"
     OUT: ""

     # D. SKILLS & PROFICIENCIES
     OUT: "=== D. SKILLS & PROFICIENCIES ==="
     OUT: "| Skill | Modifier | Proficient | Expertise |"
     OUT: "|:---|:---:|:---:|:---:|"
     FOR each skill IN proficiencies.skills:
       OUT: "| [skill.name] | [skill.modifier] | [skill.proficient ? 'Yes' : 'No'] | [skill.expertise ? 'Yes' : 'No'] |"
     OUT: "Armor Proficiencies: [proficiencies.armor] | Weapon Proficiencies: [proficiencies.weapons]"
     OUT: "Tool Proficiencies: [proficiencies.tools]"
     OUT: ""

     # E. CLASS FEATURES & RACIAL TRAITS
     OUT: "=== E. FEATURES & ABILITIES ==="
     OUT: "Fighting Style: [class.fighting_style] (If any)"
     OUT: "Racial Traits: [list of racial traits (e.g., Dwarven Resilience)]"
     FOR each resource IN resources.class_resources:
       OUT: "• [resource.name]: [current] / [max] (Reset: [reset_on])"
     OUT: "Other Features: [list of all other class features (e.g., Improved Critical, Sculpt Spells, Blessed Healer)]"
     OUT: ""

     # F. SPELLCASTING (If applicable)
     IF character.spells EXISTS:
       OUT: "=== F. SPELLCASTING ==="
       OUT: "Casting Ability: [spells.spellcasting_ability] | Spell Attack: +[spells.spell_attack_bonus]"
       OUT: "Spell Save DC: [spells.spell_save_dc] | Ritual Caster: [ritual_caster ? 'Yes' : 'No']"
       OUT: "Cantrips Known: [list cantrips]"
       OUT: "Spell Slots: [list slots (L1:C/M, L2:C/M, ...)]"
       OUT: "Prepared/Known Spells:"
       FOR each spell IN spells.spells_known:
         OUT: " - [spell.name] (L[spell.level]) [Prepared: [prepared] / Known: [known]]"
       OUT: "Spellbook Status: [list all spells in spellbook NOT prepared/known]"
       OUT: ""

     # G. INVENTORY & WEALTH
     OUT: "=== G. INVENTORY & WEALTH ==="
     OUT: "Gold (Liquid): [inventory.gold] gp"
     OUT: "Carrying Capacity: [carrying_weight] / [STR * 15] lbs"
     OUT: "Attuned Magic Items (3/3):"
     FOR each item IN inventory.magic_items WHERE item.attuned == true:
       OUT: "• [item.name] ( [item.type] ) - [brief description/effect ]"
     OUT: "Weapons & Armor (Equipped):"
     FOR each item IN inventory.equipment WHERE item.type IN [weapon, armor]:
       OUT: "• [item.name] (AC/Damage: [stats] ) - [equipped ? 'EQUIPPED' : 'BACKPACK']"
     OUT: "Consumables & Scrolls:"
     FOR each item IN inventory.magic_items WHERE item.type IN [potion, scroll, gem]:
       OUT: "• [item.name] x[item.count] ( [stored location] )"
     OUT: "Other Important Items: [list of all remaining non-consumable, non-equipped items]"

     OUT: ""
     OUT: "--- END OF CHARACTER EXPORT: [character.identity.name] ---"
     OUT: ""

5. CALL: Save_State_Protocol (File creation and computer link)
6. RETURN to game loop (Original decision point).