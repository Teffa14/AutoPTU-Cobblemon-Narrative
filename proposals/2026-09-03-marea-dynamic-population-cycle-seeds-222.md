# Marea dynamic population cycle seeds — pass 222

Status: PROPOSED / NON-CANON
Date: 2026-09-03

## Scope

These seeds exercise the dynamic demographic cycle introduced in pass 222 without assigning a new canonical species, population total, reproduction rate, mortality rate, lifespan or ecosystem boundary.

They extend pass 221's finite population. The population is no longer conceptually frozen between explicit captures/migration events: it can change through source-backed demographic windows while preserving strict accounting.

## Seed: The Population Did Not Respawn

A commonly encountered species becomes visibly rarer after sustained legal capture pressure.

The important behavior is what does not happen: Cobblemon does not quietly replenish the missing animals because the native spawn entry remains eligible.

Characters can notice fewer detections, a changed stage structure, altered movement or greater difficulty finding the species. Nerea can compare survey effort against earlier records before concluding that abundance actually fell.

Recovery, if it happens, must come through confirmed recruitment, release/introduction or immigration. It is not a presentation-system correction.

## Seed: A Good Breeding Season Is Not Instant Recovery

Field evidence indicates a successful reproductive window and a larger juvenile cohort.

The population count can rise through confirmed births/hatches while the number of breeding-capable adults remains nearly unchanged. Juveniles need time to mature and can face different survival pressure.

This prevents a common simulation shortcut in which one breeding event immediately restores the entire adult population.

Player-facing evidence can include dependent sites, juvenile sightings, altered parental behavior and later maturation observations. Exact counts remain server ground truth unless a specific survey justifies an estimate.

## Seed: They Grew Up, They Did Not Level Up

A known cohort first observed as juveniles is encountered later at another biological stage.

Nothing in that maturation event grants PTU Levels or Evolution by itself.

If one persistent Pokémon from that cohort also gained Levels through actual training/combat/progression, the two histories coexist:

```text
biological history: juvenile -> later stage
PTU history: Level changes from authoritative progression only
```

The seed exists primarily to teach the engine/worldbuilding boundary and prevent future content from using Level as an age field.

## Seed: Same Ecosystem, Different Biome

A population that had been observed mostly in one Minecraft biome band shifts toward another habitat patch inside the same authored ecosystem because seasonal resources or disturbance change.

The server records internal redistribution. It does not emit immigration/emigration events.

Characters may incorrectly describe the first patch as a population crash and the second as a population boom. Repeated identity/track/resource observations can reveal that much of the change was movement.

This seed reinforces the 1:1 ecosystem scale rule: a large ecosystem can contain several terrain/biome expressions while maintaining one coherent demographic population.

## Seed: The Seasonal Departure

An authored migratory population begins its departure window.

Only the eligible subset moves. Resident members may remain. The transfer is atomic through origin -> transit -> destination semantics, so one Pokémon cannot count as resident in both ecosystems.

The player can observe departure pulses, stopover use and changed local abundance without receiving omniscient knowledge of the transfer count.

If a persistent individual participates, its exact identity moves with the transfer. Generic spawning at the destination cannot create a duplicate.

## Seed: Capture Pressure Changes Composition First

A population can retain a superficially similar total while its composition becomes unhealthy.

Examples, only when the species/source supports the required structure:

- repeated capture of easily approached adults leaves many juveniles but fewer breeders;
- selective capture near one habitat patch redistributes the remaining members;
- immigration temporarily masks poor local recruitment;
- a successful juvenile pulse masks a decline in mature members.

The story question becomes “what kind of population remains?” rather than only “how many Pokémon are there?”

## Seed: Recovery Came From Somewhere Else

Characters celebrate an apparent recovery after sightings increase again.

Longitudinal evidence later shows that local recruitment was still weak and that immigration supplied much of the increase.

This is not a twist that changes server truth retroactively. The server always records birth/recruitment and immigration separately. The uncertainty exists only in character knowledge.

This gives Nerea and Ema a reason to distinguish local reproductive success from simple abundance.

## Seed: Resource Boom, Delayed Response

A source-backed dietary resource becomes unusually abundant for a season.

Immediate effects can include changed foraging distribution, residence time and competition. Demographic effects are delayed.

The system does not execute:

```text
more food -> spawn more Pokemon
```

Instead, resource sufficiency can improve a later recruitment or survival window if the species demographic profile permits it.

This makes ecosystem management legible over time and keeps provisioning/bait separate from real population support.

## Seed: A Bad Year Can Matter

A breeding/recruitment window fails because required conditions are not met.

No invisible compensation occurs. The population enters the next cycle with the age/stage structure produced by that failure.

One poor season need not create a crisis. Repeated poor seasons can become a genuine demographic problem, especially if capture, emigration or mortality continue.

This creates long arcs from ordinary ecology rather than requiring a villain or supernatural cause.

## Full encounter/system scenario: Marea Population Year

A future implementation can expose one population through a complete authored annual/seasonal sequence:

```text
baseline ledger
-> seasonal resource update
-> breeding/recruitment window
-> juvenile/dependent-site observations
-> survival window
-> maturation
-> local habitat redistribution
-> capture/release events during player play
-> migration departure or resident split when applicable
-> stopover/transit
-> migration arrival/return
-> next-cycle ledger
```

The exact sequence and intervals are species-specific. This scenario is a test harness shape, not a universal Pokémon life cycle.

### Required world-runtime authority

- finite ecosystem ledger;
- stage/cohort accounting;
- persistent-member accounting;
- source-backed demographic profile;
- source-backed diet/resource links;
- deterministic/persisted demographic windows;
- capture/release writeback;
- intra-ecosystem redistribution;
- atomic cross-ecosystem transfer;
- Cobblemon projection reservations against current membership.

### Battle capability dependencies

Most demographic processing itself does not need AutoPTU combat.

When player actions invoke battle mechanics, activate only the exact permanent capability families required:

- targeting/footprints/range/LoS for spatial targeting/observation;
- base movement legality for ordinary traversal;
- complete movement for interception, forced movement, blocking or displacement;
- core calculations for verified arithmetic/checks;
- action economy/initiative for structured actions;
- full turn/round lifecycle for complete battle sequences;
- full stateful damage pipeline when damage matters;
- status lifecycle when Status affects capture/survival/outcome;
- terrain/weather/hazards/zones/reactions only when an actual mechanic invokes them;
- move-specific behavior for Moves used to capture/control/traverse/interact;
- abilities for Ability effects;
- items for Balls, Berries, medicine, bait or other mechanically meaningful Items;
- Trainer Features/perks for Skills/Edges/Features;
- AI legal-action infrastructure for legal wild options;
- AI tactical policy for competent autonomous decisions;
- Minecraft/Cobblemon/Craftics adapter/playback for physical representation and result playback.

The demographic layer never supplies a missing battle rule.

## Reduced system scenario: Cohort Refresh Without Combat

A first implementation can demonstrate the cycle without rich combat:

1. Author one population ledger and stage cohorts.
2. Project only members that exist in those cohorts.
3. Run one persisted recruitment window.
4. Run one maturation window.
5. Redistribute part of the population between habitat patches.
6. Run one atomic seasonal departure/arrival transfer if applicable.
7. Verify total conservation for all non-birth/death/capture/release/immigration/emigration operations.
8. Expose only character-facing observations, not canonical totals.

This reduced version proves that the world can change demographically without fake respawns, fake battles or per-tick simulation.

## Long-term balance target

A population should be able to find a dynamic equilibrium when habitat and vital rates support it, but equilibrium is not guaranteed.

The system must permit:

- healthy growth;
- stable fluctuation;
- seasonal redistribution;
- partial migration;
- age/stage imbalance;
- pressure-induced decline;
- genuine recovery;
- source/sink dependence;
- local extinction.

The intended player experience is a living ecosystem whose consequences persist, not a spawn table that repairs itself after every visit.

## Canon questions intentionally left open

- first Marea species to receive a complete demographic profile;
- source-backed life stages for that species;
- reproduction/hatching mechanics and timing;
- lifespan/background survival model;
- migration fraction and route if any;
- carrying/resource pressure functions;
- capture policy and legal/social consequences;
- whether Sendero and its neighboring habitat patches belong to one finalized ecosystem envelope;
- how biological age should be represented for persistent Pokémon;
- which demographic facts institutions can estimate accurately in-world.