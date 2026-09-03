# Ecological Encounter Observation Loop Scan — Pass 230

Status: RESEARCH / PROVENANCE. Does not change Ouros canon.
Date: 2026-09-03

## Scope

This pass researches reusable structures for ecology-driven play while the global Ouros worldgen substrate remains unresolved.

The objective is not to add unrelated story content. It is to identify patterns that help Ouros expose persistent ecology to players through observation, investigation, intervention and consequences without turning every wild contact into a tactical battle.

This pass follows:
- `CURRENT_FOCUS.md`
- `design/ecology-development-program.md`
- `design/ouros-source-authority-and-species-policy.md`
- `design/global-world-generation-spec.md`
- `design/global-species-interaction-graph.md`
- `design/engine-readiness-snapshot-pass-226.md`

## Sources reviewed

### PTU baseline

1. Pokémon Tabletop United Survival skill reference
   - https://pturpg.wikidot.com/skills
   - PTU explicitly treats wilderness scouting as a way to learn common Pokémon, local plants/resources, rare signs, geology/geography and tracks.
   - This supports an observation-first ecology loop instead of omniscient encounter tables.

2. Pokémon Tabletop United 1.05 encounter guidance
   - public mirror excerpt indexed at https://anyflip.com/gqibw/ifqm/basic/451-500
   - The wild encounter guidance recommends a small number of species and coherent pack/group composition rather than arbitrary mixed rosters.
   - This is useful as a preparation heuristic only; Ouros should derive composition from ecology state rather than cloning a static encounter template.

### PTU campaign play evidence

3. Pokémon Tabletop campaign log #24
   - https://www.reddit.com/r/PokemonTabletop/comments/wudfhz
   - A player damages a tree, an unknown Pokémon reacts because eggs are nearby, the party discovers the parental/nesting cause, and the situation is resolved through restorative action rather than battle.
   - Reusable structure: player action changes local ecological pressure -> defensive behavior appears -> evidence reveals the hidden cause -> restorative intervention can resolve escalation.

4. Pokémon Tabletop campaign log #22
   - https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t
   - Local Pokémon behavior, human offerings and a diseased tree combine into a drought problem. The party gathers information, diagnoses the mechanism and acts on the environmental cause.
   - Reusable structure: visible social/ecological symptoms can be downstream effects of one environmental mechanism. The meaningful objective is diagnosis, not defeating the visible Pokémon.

5. Pokémon Tabletop campaign log #21
   - https://www.reddit.com/r/PokemonTabletop/comments/tvggwm
   - A forest traversal presents multiple wild groups with distinct local behavior and territorial/social identity rather than one undifferentiated encounter pool.
   - Reusable structure: a route can contain several small ecological/social niches with different tolerance, resources and threat responses.

6. Tales of Visiwa retrospective
   - https://pokemontabletop.com/tales-of-visiwa-a-retrospective/
   - The campaign treats dangerous wilderness, exploration certification, forgotten sites and multiple competing organizations as parts of one region-level adventure structure.
   - Reusable structure for Ouros: ecological access, field institutions and geographic risk can create progression without making every wilderness gate a combat gate.

### Official Pokémon ecological presentation

7. New Pokémon Snap official site — exploration / habitats
   - https://newpokemonsnap.pokemon.com/en-au/
   - The game is explicitly framed as an ecological survey of Pokémon in natural habitats.

8. New Pokémon Snap official exploration material
   - https://newpokemonsnap.pokemon.com/nl-be/explore/
   - Different environments expose different habitats; repeated investigation can reveal different behavior; plants and environmental objects are also research targets.
   - Reusable structure: repeated observation of the same place should reveal additional state, not simply repeat the same spawn list.

9. New Pokémon Snap official free update material
   - https://newpokemonsnap.pokemon.com/pt-pt/free-update/
   - A river sustains a broad portion of an island and attracts multiple Pokémon; arid areas use underground and cliff refuges; routes have day/night variants.
   - Reusable structure: resource nodes and refuge geometry explain concentration and detectability.

10. Pokémon Legends: Arceus official Cyndaquil profile
   - https://legends.arceus.pokemon.com/en-au/pokemon/cyndaquil/
   - Species behavior explicitly distinguishes timidity, surprise response and defensive escalation.
   - Reusable structure: species baseline defines a prior response, while context determines whether behavior escalates.

11. Pokémon Legends: Arceus official Hisuian Zoroark profile
   - https://legends.arceus.pokemon.com/en-au/pokemon/zoroark/
   - The same species profile can combine broad hostility with strong protective behavior toward close/family-associated individuals.
   - Reusable structure: aggression is relational/contextual rather than one scalar disposition.

### Pokémon spin-off / fan-game structural references

12. Pokémon Mystery Dungeon natural-disaster structure
   - https://mysterydungeonwiki.com/wiki/Pkmn%3ANatural_Disasters
   - Environmental disruptions can create routes, rescue needs, habitat danger and institutional responses.
   - Ouros should use the structural lesson, not import Mystery Dungeon cosmology or mechanics.

13. Pokémon Gaia overview
   - https://pokehackdb.com/hacks/pokemon-gaia
   - The fan game combines ruins, climbing, underwater access, day/night and environmental exploration with a region-scale mystery.
   - Reusable lesson: traversal capabilities can expose ecological/historical layers without every gate being a battle.

14. Pokémon Unbound location index
   - https://www.pokemonunboundpokedex.com/wiki/locations/
   - The region uses strongly differentiated environments and local mission surfaces tied to those places.
   - Reusable lesson: ecological identity is clearer when routes and settlements have persistent environmental roles rather than being generic connectors.

## Source-authority notes

- PTU is used for mechanical baseline and play-pattern evidence.
- Public campaign logs are examples of what produced meaningful play, not Ouros canon.
- Official Pokémon sources may support species/habitat/behavior claims where explicit.
- Fan games and spin-offs contribute structural design lessons only.
- No distinctive external plot, character or dialogue is imported.

## Reusable pattern 1 — Evidence before explanation

A strong ecological encounter should usually expose one or more observable signals before presenting the underlying cause.

Possible evidence channels:

```text
species presence / absence
alarm calls
unusual hiding or congregation
feeding traces
tracks
nests / eggs / juveniles
resource damage
plant condition
water level / turbidity
shed material
carcasses / scavenging signs
territorial marks
human reports
repeated route observations
weather-correlated behavior
```

The evidence packet should not automatically contain the authoritative cause.

Ouros world state may know the cause while observers know only signals they can plausibly access.

## Reusable pattern 2 — Symptom species need not be the cause

The Pokémon that attracts player attention can be downstream of a different pressure.

Example abstract chain:

```text
resource degradation
-> prey changes activity
-> predator shifts range
-> territorial overlap increases
-> humans report aggressive Pokémon
```

A quest that starts as an “aggressive Pokémon problem” can therefore resolve through habitat/resource intervention if evidence supports it.

This prevents the world from reducing ecological problems to removing whichever wild actor is most visible.

## Reusable pattern 3 — Nesting creates asymmetric tolerance

Campaign log #24 and official protective-behavior examples support treating nesting/juvenile context as a major behavior modifier.

A species may tolerate ordinary travel but strongly react when:
- a Trainer approaches a nest;
- a tree/rock/refuge is damaged;
- an escape corridor is blocked;
- a juvenile emits alarm behavior;
- food needed for juveniles is removed.

The encounter should expose warning behavior before battle when species/context allow it.

## Reusable pattern 4 — Repeated observation changes knowledge

New Pokémon Snap provides a useful presentation model: the same route can reveal different behaviors after repeated research and under different conditions.

Ouros adaptation:

```text
same spatial cell
+ different time/weather/season/ecology state
+ different observer competence/history
= different evidence available
```

This should not mean a magic global “research level” changes animal behavior by itself. The underlying ecology changes independently; player knowledge improves through accumulated observations.

## Reusable pattern 5 — Resource nodes organize multi-species scenes

A river, fruiting patch, nesting ledge, carrion site, sap source, crop edge or shelter can create a coherent multi-species encounter.

Instead of selecting species first and inventing a reason afterward:

```text
resource node
-> species that use it
-> temporal activity
-> competition / predation / tolerance relationships
-> visible scene
```

This is compatible with the existing Ouros interaction graph and microhabitat model.

## Reusable pattern 6 — Human behavior is ecological pressure

Campaign #22 shows how offerings and local custom can change animal behavior and resource distribution.

Ouros should treat recurring human practices as pressures that can affect:
- habituation;
- concentration near settlements;
- feeding expectations;
- conflict frequency;
- waste/scavenging opportunities;
- nesting-site disturbance;
- crop predation;
- local tolerance.

A settlement therefore participates in ecology instead of being an empty safe zone adjacent to “the wild”.

## Reusable pattern 7 — Noncombat resolution must remain first-class

Ecological tension can resolve through:
- withdrawal;
- restoring damaged cover;
- removing a disturbance source;
- changing a route;
- protecting a nest temporarily;
- redirecting food/waste;
- repairing water/resource access;
- waiting for a temporal window;
- using verified Trainer capabilities to avoid alarming or constrain an actor safely.

Battle remains valid when behavior escalates, but it should not be the only successful verb.

## Proposed ecology-driven content grammar

The research supports a general loop:

```text
persistent ecological state
-> observable anomaly
-> evidence collection
-> competing hypotheses
-> chosen intervention
-> immediate behavioral response
-> optional AutoPTU handoff if structured mechanics begin
-> persistent ecological consequence
-> later observation verifies or falsifies the intervention
```

The key design property is delayed verification. The player should sometimes need to return later or compare observations before knowing whether an intervention worked.

## Mechanical dependency implications

Most of the loop can exist outside structured tactical combat.

World-state only:
- evidence generation;
- resource condition;
- population/exposure/activity pressure;
- observation history;
- NPC knowledge propagation;
- quest hypothesis state;
- delayed ecological consequences.

Visible overworld behavior may require:
- Minecraft/Cobblemon/Craftics adapter/playback support;
- overworld perception/behavior policy;
- entity identity reconciliation.

If an encounter escalates into battle, exact dependencies must be declared per encounter.

A simple defensive battle can use verified targeting, base movement, calculations, action economy and legal-action infrastructure while avoiding unsupported rich mechanics.

A full nesting-defense encounter using forced displacement, reactive terrain, weather, delayed hazards, complex Ability triggers or Trainer interrupts additionally depends on those specific partial/blocking families.

## Engine evidence checked

AutoPTU-Java `main` head checked: `61321c3ab798993be25e10f287e7a375e5db3b63`.

Recent work verifies bounded tile-trap ownership/runtime slices but does not complete the overall terrain/hazard/reaction category.

Current audited capability interpretation remains:

VERIFIED within audited contracts:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

MIXED / PARTIAL / BLOCKING outside verified slices:
- terrain / weather / hazards / zones / reactions.

BLOCKING as complete family:
- AI tactical policy.

PARTIAL / BLOCKING end-to-end:
- Minecraft / Cobblemon / Craftics adapter/playback support.

No capability family is promoted by this research pass.

## Ouros conclusions

1. Ecology-driven quests should begin from observable state, not omniscient quest text.
2. The visible Pokémon may be a symptom rather than the cause.
3. Resource nodes are the preferred organizer for coherent multi-species scenes.
4. Nesting/juvenile context must materially change tolerance and escalation.
5. Human routines belong inside the ecological pressure model.
6. Repeated observation should improve knowledge and expose temporal behavior.
7. Noncombat ecological interventions must produce persistent, testable consequences.
8. Tactical combat is an optional escalation layer, not the hidden simulator of ecological truth.

## Open questions

- exact observation/evidence packet schema;
- how Survival and other Trainer Skills/Edges/Features alter evidence quality without granting omniscience;
- how long ecological interventions take to produce measurable consequences;
- how false hypotheses are represented without frustrating players;
- how NPC institutions aggregate observations from multiple actors;
- how persistent world events create temporary resource pulses or disturbance without bypassing the population model;
- which visible behaviors can be projected safely through current Cobblemon/Minecraft APIs before the richer adapter exists.
