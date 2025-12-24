# Act 2: The Poisoned Token (Levels 7-9)

```yaml
SETTING: "Eastern swamplands - render per source material geography"
DRAGON: "Adult Black Dragon"
TOKEN: "The Venom Chalice"

GATE_2.1_INTO_THE_SWAMPS:
  trigger: "Party travels to swamp region"
  what_happens: |
    Disease, decay, predators. Lizardfolk encounters.
    Rival appears - temporary alliance or ambush?
  objectives:
    - Navigate swamps
    - Handle disease and environment
    - Deal with rival encounter
  completion: "Party locates dragon's territory"

  rendering_note: "Render lizardfolk tribes per source material cultures"

GATE_2.2_THE_DROWNED_CITY:
  trigger: "Party enters dragon's domain"
  what_happens: |
    Sunken city, cunning dragon using traps and minions.
    Prisoners being tortured (rescue opportunity).
  objectives:
    - Infiltrate drowned city
    - Gather intelligence
    - Locate Token
  completion: "Dragon's lair penetrated"

GATE_2.3_MIRES_GAME:
  trigger: "Party reaches dragon"
  what_happens: |
    Dragon enjoys games. Offers deal - morally compromising task.
    CORRUPTION MOMENT: Accept dark bargain or fight.
  objectives:
    - Navigate manipulation
    - Obtain Token through chosen method
    - Survive betrayal
  completion: "Second Token obtained"

ACT_2_COMPLETION:
  milestone_xp: "Reach level 9"
  loot: "4,000-6,000 currency, 2-3 uncommon + 1 rare, poison-resistant gear"

  currency_note: "Render using source material's steel piece economy"
```
