# Act 1: The Frozen Token (Levels 5-7)

```yaml
SETTING: "Frozen glacier region - render per source material geography"
DRAGON: "Adult White Dragon"
TOKEN: "Shard of Winter's Heart"

GATE_1.1_CONCLAVE_CHALLENGE:
  trigger: "Campaign opening"
  what_happens: |
    The wizard governing body summons the protagonist. The great Tower awaits a master.
    Trial declared: five Tokens of Dominion from five dragon lords.
    The rival dark-robed mage has already departed.
  objectives:
    - Receive trial terms
    - Learn of rival
    - Gather supplies and information
  completion: "Party sets out toward frozen glacier region"

  rendering_note: "Render governing body members per source material (three leaders, one per order)"

GATE_1.2_FROZEN_WASTES:
  trigger: "Party enters frozen glacier region"
  what_happens: |
    Survival challenges, primitive ice tribes, dragon-soldier patrols.
    The rival's trail is visible - ahead but struggling.
  objectives:
    - Survive environment
    - Find passage to dragon's domain
    - Discover dragon's weakness
  completion: "Party locates dragon's lair"

  rendering_note: "Render ice folk tribes and dragon-soldier types per source material"

GATE_1.3_WHITE_DRAGONS_LAIR:
  trigger: "Party enters lair"
  what_happens: |
    Ice caves, frozen hazards, moral choices (prisoners?).
    Token in deepest chamber with dragon.
  objectives:
    - Navigate lair
    - Handle moral choices (corruption implications)
    - Confront dragon
  completion: "First Token obtained"

ACT_1_COMPLETION:
  milestone_xp: "Reach level 7"
  loot: "2,000-4,000 currency, 2-3 uncommon items, cold-themed weapons"

  currency_note: "Render using source material's steel piece economy"
```
