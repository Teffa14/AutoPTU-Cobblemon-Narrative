# Ouros Ecology Development Program

Status: OUROS PROJECT DIRECTIVE
Date: 2026-09-03

## Active focus

From Pass 227 onward, and until this program is explicitly declared complete, every new Ouros lore, research, species, encounter-ecology and related world-state pass must primarily advance Pokémon ecology and species behaviour.

Unrelated lore systems remain valid but are not the primary pass target while this directive is active. A pass may touch NPCs, settlements, quests, weather, exploration or battles only when the main purpose is to improve, expose, validate or implement ecology.

## Objective

Build a persistent Pokémon ecology system that can explain:

- which species live in a place and why;
- habitat and microhabitat use;
- food and resource use;
- predator/prey relationships;
- competition, displacement and territoriality;
- social groups and interspecies information;
- nesting, juveniles and parental behaviour;
- time, season, weather and migration;
- human disturbance and habituation;
- individual variation from the species baseline;
- how Moves, Abilities, capabilities, Trainer Skills, Edges and Features alter legal behaviour;
- what becomes visible through Cobblemon;
- what players and NPCs can actually observe;
- when ambient behaviour crosses into an AutoPTU encounter;
- what ecological consequences persist after player intervention.

The target is a living ecological model, not a larger random encounter table.

## Source programme

Use multiple source layers while preserving provenance and authority.

1. Official Pokémon material for explicit species identity, habitat and behaviour. This includes main-series Pokédex/game evidence plus useful behaviour and distribution patterns from games such as Pokémon Legends, New Pokémon Snap, Pokémon GO and Pokémon UNITE. Gameplay abstractions must not automatically become literal biology.
2. PTU as the mechanical baseline. Use Caelo and Kairos as living-world and rules references, subject to `design/ouros-source-authority-and-species-policy.md`. `SOURCE_HAS_RULE != OUROS_USES_RULE`.
3. Real behavioural and community ecology to enrich gaps: predation, competition, territoriality, foraging, alarm signalling, social structure, parental care, dispersal, migration, disturbance, urban tolerance, succession and related fields. Biological analogues propose mechanisms; they do not create Pokémon canon automatically.
4. Cobblemon/Minecraft for native overworld projection wherever possible: spawning conditions, time, biome, weather/light context, persistence, navigation, animation and presentation.
5. AutoPTU for authoritative structured mechanics only. The ecology layer must not simulate hidden tactical battles to create world truth.

Kairos remains a high-value living-world reference and its local source index is `sources/kairos/KAIROS_SOURCE_INDEX.md`.

## Mandatory system areas

The program is not complete until the project has explicit design, provenance and implementation paths for all of these areas:

- species ecology profiles;
- habitat and microhabitat model;
- resource network;
- directed species interaction graph;
- individual wild behaviour policy;
- social ecology and temporary/persistent groups;
- nesting, reproduction and life stage;
- population and demography;
- temporal ecology and migration;
- human disturbance and habituation;
- disturbance, succession and recovery;
- Cobblemon spawn projection and persistent-individual reconciliation;
- observation, field research and NPC knowledge;
- ecology-driven quests/events;
- AutoPTU handoff for ecological encounters;
- deterministic validation/regression fixtures.

## Core behaviour rule

Species behaviour is a prior, not a script.

```text
species baseline
+ form
+ individual capabilities and Moves/Abilities
+ level/size/life stage/current condition
+ feeding/nesting/parental context
+ resources and threats
+ nearby Pokémon
+ distance/cover/exits
+ recent disturbance and alarm history
+ human-population tolerance
+ Trainer behaviour and verified capabilities
= candidate behavioural intent
```

Possible intent includes forage, rest, observe, tolerate, approach, investigate, follow, avoid, freeze, hide, warn, guard, displace, flee, pursue, defend, engage, disengage, care for juveniles and relocate.

These are behavioural states, not PTU Status Afflictions.

## Authority flow

```text
persistent ecology state
-> local availability and behaviour pressure
-> native Cobblemon/Minecraft projection
-> visible interaction
-> Ouros decides whether structured mechanics begin
-> AutoPTU resolves legal tactical state/outcomes
-> semantic result returns to persistent ecology state
```

Generic Cobblemon spawning does not create population truth. A canonical persistent individual must never be duplicated by a generic spawn row. Minecraft visual contact, velocity or vanilla damage cannot replace AutoPTU adjudication.

## Pass requirements

Every pass while this directive is active should, where relevant:

1. inspect current repo state and existing ecology work;
2. answer one bounded ecology question;
3. add new source-backed research;
4. compare official Pokémon evidence with PTU/Caelo/Kairos where applicable;
5. enrich with real ecology when useful;
6. make a concrete Ouros design/data change;
7. ground it in Marea/Sendero or another existing ecosystem rather than creating unrelated regions;
8. map it to Cobblemon/Minecraft;
9. audit AutoPTU dependencies if structured mechanics can occur;
10. record unresolved ecology questions and the next highest-value gap.

Do not create a pass whose only result is a generic lore essay.

## Initial pass sequence

- 227: species ecology profile schema and source normalization.
- 228: Marea/Sendero microhabitat and resource map.
- 229: first local roster plus trophic/resource network.
- 230: individual wild behaviour policy.
- 231: predator/prey pursuit, avoidance and non-consumptive pressure.
- 232: territoriality, competition and scarcity.
- 233: social groups, alarm signalling and interspecies information.
- 234: nesting, juveniles and parental behaviour.
- 235: migration, seasonality and temporal niches.
- 236: human disturbance and habituation gradients.
- 237: disturbance, succession and recovery.
- 238: population/demography model.
- 239: persistent individual vs generic Cobblemon spawn reconciliation.
- 240: observation/research/NPC knowledge pipeline.
- 241: ecology-driven world events and player consequences.
- 242: AutoPTU ecological encounter handoff matrix.
- 243+: implementation fixtures, integration tests and gap closure until completion.

The sequence may split or repeat when evidence requires it.

## Completion gates

Ecology remains the active workstream until all of these are satisfied or explicitly waived:

- all mandatory system areas have ownership/data contracts;
- the source-research pipeline is repeatable;
- at least one Marea ecosystem works end-to-end with multiple species and resources;
- ecology reliably affects visible Cobblemon presence/behaviour;
- persistent individuals cannot be cloned by generic spawning;
- representative ecological encounters hand off to/from AutoPTU correctly;
- population, observation and player-caused ecological state persist across server/world lifecycle;
- regression fixtures protect the core invariants.

## Definition of done

A player must be able to enter a habitat and have the presence, absence, hiding, feeding, nesting, competition, hunting, fleeing, tolerance and movement of Pokémon explained from persistent ecological state plus species and individual behaviour. Those explanations must survive observation, player intervention, Cobblemon projection and AutoPTU encounters without authority violations.

Until then, ecology is the default Ouros pass workstream.
