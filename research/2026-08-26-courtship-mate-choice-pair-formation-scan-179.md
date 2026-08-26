# Pass 179 Research — Courtship, Mate Choice & Pair Formation

Status: RESEARCH / PROVENANCE ONLY
Canon status: NON-CANON until separately approved
Date: 2026-08-26

## Why this scan exists

The repository already has an authoritative Breeding/Egg/Nursery layer for mechanical breeding resolution, Egg provenance and institutional care, plus a Wild Nesting / Parental Care / Juvenile Dispersal layer for reproductive sites, Eggs/young, caregiver observations, dependency and natal dispersal.

The Wild Nesting layer explicitly says not to fabricate courtship, mating, conception or parentage when they were not observed or mechanically established. That leaves a useful missing interval before nesting: courtship displays, candidate comparison, reciprocal approach/withdrawal, temporary associations, pair formation, pair continuity and pair dissolution.

This scan treats those subjects as behavioral evidence. It does not create PTU breeding eligibility, Infatuation, Attract effects, parentage, Eggs, gender assumptions or permanent pair bonds.

## Existing Ouros boundaries checked before writing

### Breeding, Eggs, Nursery & Lineage

`design/breeding-eggs-nursery-lineage-layer.md` remains authoritative for PTU/Caelo breeding resolution, Egg mechanical state, Egg custody, hatch timing, inheritance and mechanically established lineage.

Pass 179 cannot decide that a courtship observation produced an Egg or that two observed Pokémon are mechanically compatible.

### Wild Nesting, Parental Care & Juvenile Dispersal

`design/wild-nesting-parental-care-juvenile-dispersal-layer.md` owns reproductive-site identity, nesting episodes, Eggs/young observations, caregiver behavior, dependency and dispersal.

Pass 179 may hand off a later nesting episode, but cannot infer that nesting occurred merely because courtship was observed.

### Pokémon Agency / Wild Collectives

Persistent individual identity, partnership, custody, release and agency stay with Pokémon Agency. Group structure stays with Wild Collectives.

A pair-like association must never become ownership, trainer partnership or collective membership automatically.

### Soundscapes / Olfactory Landscapes / Lightscapes / Social Learning

Signals may be acoustic, olfactory, visual or learned. Those evidence systems remain authoritative for recordings, scent observations, light displays and transmission claims. Pass 179 only interprets them inside a courtship or pair-formation context when evidence supports that interpretation.

### Spatial Ecology / Territory

Courtship sites, display courts and pair-use areas may overlap with home ranges or territories, but a display site is not automatically a territory and territorial defense is not automatically courtship.

## Pokémon source patterns

### Volbeat and Illumise — signal coordination without automatic mechanical attraction

The official Pokédex says Volbeat communicates by flashing its rear light and is attracted to the sweet aroma of Illumise. Illumise is described as using scent to guide Volbeat into many night-sky patterns, some of which are studied by scholars.

Sources:
- Pokémon official Pokédex — Volbeat: https://www.pokemon.com/us/pokedex/volbeat
- Pokémon official Pokédex — Illumise: https://www.pokemon.com/us/pokedex/illumise

Reusable design lessons:

1. Courtship-like or affiliative behavior can use multiple signal channels at once: light, scent, movement and spatial coordination.
2. A repeated display can become a local cultural or scientific event without revealing the private reproductive outcome of every participant.
3. The same display can be studied as communication, performance ecology, mate-choice behavior or social coordination depending on the evidence.
4. Species lore about attraction must not be converted into PTU `Infatuation`, `Attract`, lure rolls or AI obedience unless those mechanics are explicitly invoked and implemented.

### “Love at First Flight” — recurring festival around a Pokémon display

The anime episode commonly known as “Love at First Flight” centers on a recurring lakeside festival where Volbeat and Illumise perform coordinated aerial light displays. The useful structure is not its human romance plot. The reusable pattern is:

`seasonal species behavior / trained display -> public festival -> rehearsal -> disruption -> recovery -> performance`

Source:
- Bulbapedia episode summary: https://bulbapedia.bulbagarden.net/wiki/AG042

Reusable design lesson:

Ouros can have communities whose calendars, tourism, public memory or local identity are built around a recurring Pokémon display. The public event must remain separate from wild reproductive truth. A performance staged by Trainers also cannot be treated as evidence of wild pair formation.

## Animal-behavior research

### A display can serve more than one function

A USGS study of Western Sandpipers compared explanations for breeding displays as mate attraction versus territory defense. Display intensity differed with mate and site fidelity, showing why the same visible behavior should not receive a single universal interpretation.

Source:
- U.S. Geological Survey, “Do male breeding displays function to attract mates or defend territories? The explanatory role of mate and site fidelity.”
  https://www.usgs.gov/publications/do-male-breeding-displays-function-attract-mates-or-defend-territories-explanatory

Reusable design lesson:

Ouros should store the observation first and the function as an assessment. A display may support `COURTSHIP_POSSIBLE`, `PAIR_MAINTENANCE_POSSIBLE`, `TERRITORIAL_POSSIBLE`, multiple simultaneous hypotheses or `UNRESOLVED`.

### Courtship behavior can vary substantially among individuals

Smithsonian research on golden-collared manakins found individual variability in elaborate courtship displays performed at display courts. Males could perform with or without a potential mate present.

Source:
- Smithsonian Research Online, “High-speed video analysis reveals individual variability in the courtship displays of male golden-collared manakins.”
  https://repository.si.edu/items/ede06c52-2fad-4b2b-a930-347af9b09a91

Reusable design lesson:

A species-grounded display template should not become a fixed animation script for every individual. Persistent Pokémon can accumulate their own display histories, preferred sites and revisions over time.

### Mate choice is a decision process, not a deterministic ranking

Smithsonian Tropical Research Institute work on mate-choice rules argues that real choice need not reduce cleanly to a single fixed preference value. Other work on túngara frogs shows that choice can remain open to interruption and competing signals during the approach process.

Sources:
- Kirkpatrick, Rand & Ryan, “Mate Choice Rules in Animals.” Smithsonian repository: https://repository.si.edu/items/94d9556e-13e4-4196-98a5-b9bcdaa85273
- Baugh & Ryan, “Mate choice in response to dynamic presentation of male advertisement signals in Tungara frogs.” https://repository.si.edu/items/b9d29b51-0141-48f3-aa78-e7f52cc09620

Reusable design lessons:

- Do not build a hidden `mate_score` that deterministically selects the “best” candidate.
- Approach, attention, interruption, withdrawal and later re-approach can all be meaningful events without producing a pair.
- A chosen association at one time does not prove a stable lifetime preference.

### Ecological context can change courtship decisions

Smithsonian research on fiddler crabs shows that perceived predation risk can alter mate-search and preference behavior. More broadly, courtship structures and signals can help with orientation or safety as well as signaling.

Sources:
- Christy research overview: https://stri.si.edu/scientist/john-christy
- “The strength of a female mate preference increases with predation risk.” https://repository.si.edu/items/c15befb0-acf5-4872-9adb-749f4953a5cc

Reusable design lesson:

Courtship should respond to habitat, disturbance, crowding, predators, weather, signal masking or altered landmarks through authored ecology. The system should not treat a canceled display as rejection by default.

## PTU / tabletop cross-check

PTU 1.05 contains explicit battle mechanics named `Attract` and `Infatuation`. Public Core references describe Attract as a Social Move that can cause Infatuation under its own mechanical restrictions, and Infatuation as a volatile battle affliction with a Save Check and targeting consequences.

Sources:
- PTU 1.05 Core public mirror, Infatuation section: https://anyflip.com/tcye/paot/basic/201-250
- PTU move reference, Attract: https://pturpg.wikidot.com/normal

The read-only AutoPTU repository also contains an `Infatuated` status path and references to Attract-related material. AutoPTU-Java remains an incomplete port and its README still lists the full status controller, remaining move/ability registries and other large subsystems as unfinished.

Critical rule:

`COURTSHIP BEHAVIOR != PTU INFATUATION`

`PAIR FORMATION != ATTRACT SUCCESS`

`ILLUMISE SCENT != AUTOMATIC ATTRACT MOVE`

`DISPLAY PREFERENCE != CHARM CHECK RESULT`

The narrative layer may only record mechanical Infatuation if the authoritative rules engine actually produced it in a battle or rules transaction.

## PTU campaign/community pattern

A public PTU campaign log demonstrates the value of giving wild Pokémon distinct recurring personalities, group behaviors and attachments to places rather than treating all wild encounters as anonymous combatants. Another public discussion about daycare/breeding notes that groups often avoid overbuilding breeding mechanics because of tabletop overhead.

Sources:
- r/PokemonTabletop campaign log #21: https://www.reddit.com/r/PokemonTabletop/comments/tvggwm
- r/PokemonTabletop, “Is there a system for pokémon daycare?”: https://www.reddit.com/r/PokemonTabletop/comments/isn800

Reusable design lesson:

Courtship ecology should enrich the world through observed behavior, recurring individuals and seasonal callbacks. It should not become a mandatory reproductive minigame or a breeding optimization layer.

## High-value Ouros structures extracted

- persistent display sites that can outlive individual participants;
- display repertoires that vary by individual and season;
- reciprocal and one-sided approach events;
- interruptions caused by habitat, weather, crowds or competing signals;
- temporary pair-like associations that may dissolve without drama;
- multi-year mate/site fidelity assessments with uncertainty;
- public festivals built around observable displays while private reproductive outcomes remain unknown;
- scientific disagreement over whether a display is courtship, territory defense, pair maintenance or another function;
- courtship sites that become conservation, tourism or development conflicts;
- pair continuity that changes after migration, injury, evolution, relocation, release or landscape change without rewriting identity.

## Guardrails for Ouros

Never infer any of the following automatically:

- display -> mating;
- mating -> Egg;
- pair association -> genetic parentage;
- proximity -> pair bond;
- repeated association -> permanent monogamy;
- same nest -> pair bond;
- same species lore -> same individual preference;
- rejection/withdrawal -> hostility;
- courtship failure -> Loyalty loss;
- species gender ratio -> identity of a specific individual;
- beauty/cuteness -> preference;
- PTU Cute Contest Stat -> mate choice;
- Attract/Infatuation -> reproductive relationship;
- two Pokémon rendered together in Minecraft -> pair formation.

## Caelo status

Repository search did not recover a primary Caelo rules or setting source that defines courtship, mate choice, pair bonds or wild reproductive-behavior checks. No Caelo-specific mechanical rule is asserted here.

Super PTU Online Helper was not available as an invocable capability in this runtime. No output is attributed to it.

## Recommended Ouros direction

Create a behavioral layer between ordinary social observations and Wild Nesting. It should preserve event evidence, individual identity, uncertainty and long-term pair history while refusing to resolve breeding mechanics. The strongest narrative value is not “who breeds with whom”; it is how recurring displays, sites, associations, interruptions and changes become recognizable parts of regional life over years.