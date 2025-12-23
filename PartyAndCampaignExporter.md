# PARTY EXPORTER - ENHANCED WITH CAMPAIGN PROGRESS
# Full-fidelity export of campaign state AND character sheets

1. OUT: "💾 GENERATING FULL-FIDELITY CAMPAIGN & PARTY EXPORT"
2. OUT: "⚠️ Copy ALL text between the START/END markers for complete portability."
3. OUT: ""

## SECTION 0: CAMPAIGN PROGRESS SUMMARY

OUT: "╔════════════════════════════════════════════════════════════════╗"
OUT: "║           CAMPAIGN STATE & NARRATIVE PROGRESS                  ║"
OUT: "╚════════════════════════════════════════════════════════════════╝"
OUT: ""

# 0A. CAMPAIGN METADATA
OUT: "=== 0A. CAMPAIGN OVERVIEW ==="
OUT: "Campaign Name: [campaign_state.campaign_name]"
OUT: "Module/Adventure: [campaign_state.module_name] (e.g., Lost Mine of Phandelver)"
OUT: "DM Style: [campaign_state.dm_style] (e.g., AI-Orchestrated, Human DM)"
OUT: "Session Number: [campaign_state.current_session] | Total Sessions: [campaign_state.total_sessions]"
OUT: "Campaign Start Date: [campaign_state.start_date_real]"
OUT: "Last Session Date: [campaign_state.last_session_date]"
OUT: "Current In-Game Date: [campaign_state.current_game_date] (If tracked)"
OUT: "Campaign Status: [campaign_state.status] (Active/On Hiatus/Completed)"
OUT: ""

# 0B. CURRENT SITUATION
OUT: "=== 0B. CURRENT PARTY STATUS ==="
OUT: "Party Location: [campaign_state.party.current_location]"
OUT: "Region/Area: [campaign_state.party.current_region]"
OUT: "Party State: [campaign_state.party.status] (Resting/Traveling/Exploring/In Combat/In Town)"
OUT: "Time of Day: [campaign_state.time_of_day] | Weather: [campaign_state.weather]"
OUT: "Last Rest: [campaign_state.party.last_rest_type] ([campaign_state.party.hours_since_rest] hours ago)"
OUT: "Active Scene/Context: [campaign_state.active_scene_description]"
OUT: ""

# 0C. QUEST LOG
OUT: "=== 0C. ACTIVE QUESTS ==="
IF campaign_state.quests.active.length > 0:
  FOR each quest IN campaign_state.quests WHERE quest.status == 'active':
    OUT: "📍 QUEST: [quest.name]"
    OUT: "   Type: [quest.type] | Priority: [quest.priority] | Quest Giver: [quest.giver]"
    OUT: "   Description: [quest.description]"
    OUT: "   Current Progress: [quest.progress_summary]"
    OUT: "   Objectives:"
    FOR each objective IN quest.objectives:
      OUT: "     [objective.completed ? '✅' : '❌'] [objective.description]"
    OUT: "   Rewards: [quest.rewards]"
    OUT: "   Notes: [quest.dm_notes]"
    OUT: ""
ELSE:
  OUT: "   (No active quests)"
  OUT: ""

OUT: "=== 0D. COMPLETED QUESTS ==="
OUT: "Total Completed: [campaign_state.quests.completed.length]"
IF campaign_state.quests.completed.length > 0:
  FOR each quest IN campaign_state.quests WHERE quest.status == 'completed':
    OUT: "✅ [quest.name] (Session [quest.completed_session]) - [quest.brief_outcome]"
ELSE:
  OUT: "   (No completed quests yet)"
OUT: ""

OUT: "=== 0E. FAILED/ABANDONED QUESTS ==="
IF campaign_state.quests.failed.length > 0:
  FOR each quest IN campaign_state.quests WHERE quest.status == 'failed':
    OUT: "❌ [quest.name] - Reason: [quest.failure_reason]"
ELSE:
  OUT: "   (None)"
OUT: ""

# 0F. STORY MILESTONES & CAMPAIGN HISTORY
OUT: "=== 0F. MAJOR STORY MILESTONES ==="
FOR each milestone IN campaign_state.story_milestones ORDER BY session DESC:
  OUT: "📜 Session [milestone.session_number]: [milestone.title]"
  OUT: "   [milestone.description]"
  OUT: "   Impact: [milestone.narrative_impact]"
  OUT: ""

# 0G. WORLD STATE & FACTIONS
OUT: "=== 0G. FACTION STANDINGS & RELATIONSHIPS ==="
IF campaign_state.factions.length > 0:
  FOR each faction IN campaign_state.factions:
    OUT: "🏛️  [faction.name]"
    OUT: "   Reputation: [faction.reputation_level] ([faction.reputation_score]/100)"
    OUT: "   Status: [faction.relationship_status] (Ally/Neutral/Hostile/Unknown)"
    OUT: "   Key Contact: [faction.primary_contact] (If known)"
    OUT: "   Recent Interaction: [faction.last_interaction]"
    OUT: ""
ELSE:
  OUT: "   (No faction relationships tracked yet)"
  OUT: ""

# 0H. KNOWN NPCs
OUT: "=== 0H. NOTABLE NPCs & RELATIONSHIPS ==="
OUT: "| NPC Name | Role/Occupation | Relationship | Location | Status | Last Seen |"
OUT: "|:---------|:---------------|:-------------|:---------|:-------|:----------|"
FOR each npc IN campaign_state.npcs WHERE npc.importance >= 'notable':
  OUT: "| [npc.name] | [npc.role] | [npc.relationship] | [npc.current_location] | [npc.status] | Session [npc.last_seen_session] |"
OUT: ""
OUT: "Key NPC Notes:"
FOR each npc IN campaign_state.npcs WHERE npc.importance == 'critical':
  OUT: "  • [npc.name]: [npc.character_notes]"
OUT: ""

# 0I. WORLD DISCOVERIES
OUT: "=== 0I. DISCOVERED LOCATIONS & MAP PROGRESS ==="
OUT: "Major Locations Discovered: [campaign_state.locations.discovered.length]"
FOR each location IN campaign_state.locations WHERE location.discovered == true:
  OUT: "  📍 [location.name] ([location.type])"
  OUT: "     Region: [location.region] | Status: [location.status]"
  OUT: "     Notes: [location.discovery_notes]"
OUT: ""

OUT: "Undiscovered/Rumored Locations:"
FOR each location IN campaign_state.locations WHERE location.rumored == true AND location.discovered == false:
  OUT: "  🗺️  [location.name] - Rumored to be in [location.rumored_region]"
OUT: ""

# 0J. PARTY RESOURCES & SHARED ASSETS
OUT: "=== 0J. PARTY-WIDE RESOURCES ==="
OUT: "Shared Gold Pool: [campaign_state.party.shared_gold] gp (If tracked separately from individuals)"
OUT: "Party Mounts: [list of mounts/vehicles]"
OUT: "Base of Operations: [campaign_state.party.base_location] (If established)"
OUT: "Shared Inventory/Storage:"
FOR each item IN campaign_state.party.shared_inventory:
  OUT: "  • [item.name] x[item.quantity] - [item.location]"
OUT: ""

OUT: "Transportation:"
OUT: "  • [campaign_state.party.transportation] (Cart, horses, airship, etc.)"
OUT: ""

# 0K. CAMPAIGN CALENDAR & TIME TRACKING
OUT: "=== 0K. TIME & CALENDAR ==="
OUT: "Days Elapsed (In-Game): [campaign_state.calendar.days_elapsed]"
OUT: "Current Season: [campaign_state.calendar.season]"
OUT: "Upcoming Events: [list of scheduled in-game events]"
OUT: "Travel Days Remaining: [campaign_state.party.travel_days_remaining] (If traveling)"
OUT: ""

# 0L. PLOT THREADS & MYSTERIES
OUT: "=== 0L. ACTIVE PLOT THREADS & MYSTERIES ==="
FOR each thread IN campaign_state.plot_threads WHERE thread.status == 'active':
  OUT: "🧵 [thread.name]"
  OUT: "   Clues Discovered: [thread.clues_found.length] / [thread.total_clues]"
  OUT: "   Current Theory/Understanding: [thread.party_understanding]"
  OUT: "   DM Notes: [thread.dm_secret_info] (Hidden from players in actual export)"
  OUT: ""

# 0M. CAMPAIGN NOTES & DM REMINDERS
OUT: "=== 0M. DM NOTES & SESSION PREP ==="
OUT: "Next Session Prep:"
OUT: "  • [campaign_state.dm_notes.next_session_focus]"
OUT: ""
OUT: "Pending Reveals:"
FOR each reveal IN campaign_state.dm_notes.pending_reveals:
  OUT: "  • [reveal.description] (Trigger: [reveal.trigger_condition])"
OUT: ""
OUT: "Unresolved Threads:"
FOR each thread IN campaign_state.dm_notes.unresolved_threads:
  OUT: "  • [thread]"
OUT: ""

OUT: "╔════════════════════════════════════════════════════════════════╗"
OUT: "║                    CHARACTER SHEETS                            ║"
OUT: "╚════════════════════════════════════════════════════════════════╝"
OUT: ""

## SECTION 1-N: INDIVIDUAL CHARACTER EXPORTS

SELECT: target_list (IF 'PARTY', FOR EACH character IN party_state.characters; ELSE, target = requested character)

FOR EACH character IN target_list:
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

## SECTION FINAL: EXPORT METADATA & RESTORATION

OUT: ""
OUT: "╔════════════════════════════════════════════════════════════════╗"
OUT: "║                  EXPORT METADATA                               ║"
OUT: "╚════════════════════════════════════════════════════════════════╝"
OUT: ""
OUT: "Export Generated: [CURRENT_TIMESTAMP]"
OUT: "Export Format Version: 2.0 (Enhanced with Campaign Progress)"
OUT: "Total Characters Exported: [target_list.length]"
OUT: "Campaign State Hash: [GENERATE_HASH] (For integrity verification)"
OUT: ""
OUT: "🔄 RESTORATION INSTRUCTIONS:"
OUT: "To restore this campaign state:"
OUT: "1. Copy ALL text between the START/END markers"
OUT: "2. Paste into a new AI DM session"
OUT: "3. Say: 'Load campaign from export'"
OUT: "4. The AI will reconstruct all campaign and character state"
OUT: ""
OUT: "⚠️  BACKUP RECOMMENDATION: Save this export as '[campaign_name]_Session_[session_number]_[date].txt'"
OUT: ""

CALL: Save_State_Protocol (File creation and computer link)
RETURN to game loop (Original decision point)