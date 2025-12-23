# FORCE SAVE PROTOCOL

Delta-based saves - only what changed from campaign defaults.

---

## ON LOAD - EXECUTE IMMEDIATELY

```yaml
DO_NOT:
  - Ask if user wants to save
  - Summarize game first
  - Wait for instructions
  - Output save in chat
  - Include base stats (ability scores, features, starting gear)
  - Include empty attunements
  - Include unused spell slot levels
  - Include factions at 0
  - Include NPCs not yet met
  - Include death saves unless dying

DO:
  - Immediately generate slim save
  - Only include DELTAS from campaign defaults
  - Create as .md file
  - Save to /mnt/user-data/outputs/SAVE_[Campaign]_S[#].md
  - Present file to user
  - Flag uncertain values with ⚠️

OUTPUT:
  method: create_file
  location: /mnt/user-data/outputs/
  filename: SAVE_[CampaignName]_S[Number].md
  then: present_files
```

---

## SAVE PHILOSOPHY

```yaml
PRINCIPLE: Campaign file has base. Save file has changes.

SKIP (in campaign file):
  - Ability scores, AC, speed
  - Class/racial features
  - Starting equipment
  - Faction definitions
  - World mechanics

INCLUDE (deltas only):
  - HP if not full
  - Resources spent
  - Items added/removed
  - Level/XP if changed
  - Active conditions
  - Attunements if any
  - Non-zero faction rep
  - NPCs encountered
  - True flags
  - Current situation
```

---

## SAVE STRUCTURE

Describe the save file structure - AI generates appropriate formatting:

```yaml
HEADER:
  - Campaign name, session number, act, current gate, date

PARTY_STATUS:
  - Per character: HP, spent resources, inventory changes, gold
  - Skip unchanged characters or write "full"
  - Party gold pool if communal

LOCATION:
  - Where, time of day
  - Environment only if relevant (hazards, weather)

COMBAT (if active):
  - Round, current turn
  - Initiative order with HP
  - Enemy status
  - Notes (concentration, terrain)

TRACKERS:
  - Campaign-specific (corruption, tokens, etc.)
  - Include last change reason

FACTIONS:
  - Non-zero only
  - Score and standing

NPCS_MET:
  - One line each: name, disposition, status, key fact

FLAGS:
  - True flags only, comma-separated

GATES:
  - Current gate and progress
  - Completed gates list

RECENT:
  - Last 3 actions
  - NOW: 2-3 sentences on immediate situation
  - PENDING: decision awaiting input

SESSION_LOG:
  - Key events (brief)
  - Key choices
  - Combats and outcomes
  - XP gained, gold net

FOOTER:
  - Resume instructions: Kernel → Campaign → Resume → Paste
```

---

## SIZE TARGET

```yaml
GOAL: 2-5 KB

BLOAT_CHECK:
  - Over 8 KB = too much base data
  - Listing ability scores = wrong
  - Listing class features = wrong
  - Listing empty slots = wrong
  - Listing 0-rep factions = wrong
  - Writing paragraphs = wrong
```

---

## EXAMPLES

```yaml
BLOATED:
  "Caramon: STR 18, DEX 12... [20 lines] HP 49/49, all resources full"
  
CORRECT:
  "Caramon (NPC): full"

BLOATED:
  "Slots: 1st 4/4, 2nd 3/3, 3rd 2/2, 4th 0/0, 5th 0/0..."
  
CORRECT:
  "Slots: full" or "Slots: 1st:2/4, 3rd:1/2"

BLOATED:
  "Knights of Solamnia: 0 (Unknown) - not yet encountered"
  
CORRECT:
  [omit entirely - only non-zero factions]
```

---

## AFTER SAVE

```yaml
OUTPUT:
  "💾 Save created: [filename]"
  "Resume: Kernel → Campaign → Resume → Upload/paste"

THEN:
  ASK: "Continue playing or end session?"
  ⛏ WAIT
```

---

## UNCERTAINTY

Flag uncertain values, don't skip them:
```
HP: ⚠️ ~35/49 (uncertain)
```

---

**END FORCE SAVE PROTOCOL**
