# Borrowed Teeth, Permanent Roots — Pass 325

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Narrative purpose

Create a recurring Ouros arc about an old ecological-management intervention that became part of ordinary life. The conflict is designed to produce field investigation, institutional disagreement, local jobs, reputation changes, optional battles and later review without assigning automatic villainy to any faction or species.

Nothing in this file establishes region, species, institution or history as canon.

## Core premise

Generations ago, a productive district experienced repeated losses from a Pokémon population that damaged stored food, crops, infrastructure or another protected resource. A public or cooperative management program deliberately introduced a different Pokémon population to reduce that pressure.

The original target problem later changed. Land use shifted, storage improved, habitat moved, work schedules changed or another disturbance altered where both populations spend time. Descendants of the introduced Pokémon now occupy service routes, field margins and work yards as an ordinary part of local life.

A present-day incident reactivates the old charter. One office cites it as authority for broad control. Another group argues that the historical objective was much narrower. Residents remember the introduced population as normal neighbors. Workers report real current damage in one feature. A habitat team reports useful ecological interactions somewhere else.

All can be correct about their own evidence.

## Stable world features

The proposal requires persistent feature identity rather than a disposable quest map:

- a productive/storage district where the historical problem mattered;
- a service corridor used by workers and Pokémon;
- a habitat edge or restored patch where current interactions differ;
- an archive, cooperative office or maintenance station holding pieces of the old authorization;
- a monitoring site with recent observations;
- at least one alternate route or refuge that makes displacement consequences visible later.

Exact geography remains unresolved until canon placement.

## Stakeholder roles

### Management officer

Goal: act on a currently documented public obligation.
Knowledge: current complaints, current mandate summary, some historical records.
Risk: treating inherited language as broader authority than the original program granted.

### Cooperative or logistics representative

Goal: protect goods, schedules and worker safety.
Knowledge: recent losses and operational constraints.
Risk: extrapolating from a real problem in one feature to the whole population.

### Habitat researcher or field monitor

Goal: preserve current ecological function and obtain enough evidence before irreversible action.
Knowledge: recent observations and habitat use.
Risk: underweighting operational damage outside the monitored site.

### Long-term resident or retired worker

Goal: protect community continuity and remembered local practice.
Knowledge: oral history and old routines.
Risk: memory can be sincere but incomplete, compressed or attached to the wrong period.

### Current workers

Goal: complete work without repeated disruption.
Knowledge: direct recent encounters.
Risk: they may see only the time window when their shift overlaps with the population.

### Pokémon populations

They are world actors and ecological participants, not moral proxies for the historical institution. Current individuals do not inherit guilt for why their ancestors were introduced.

## Arc structure

### Beat 1 — A current problem invokes an old answer

A recent loss, access problem or repeated encounter causes an official or cooperative notice to cite the historical management charter. A broad action is proposed quickly because the document appears to settle the issue.

The first player task is not to approve or reject the policy. It is to establish what the current incident actually occurred at, when, and which population was observed.

### Beat 2 — Field evidence fails to match the inherited summary

The service corridor shows recent use, but another monitored site shows different behavior. Evidence may establish presence without establishing cause. A current individual may be using a route created long after the original program.

Players can collect observations, interview workers, compare shifts and identify which claims refer to which feature.

### Beat 3 — The charter has a narrower provenance

Archive material, meeting minutes, maintenance records or an old map show that the original authorization targeted a particular resource, season or zone. Later summaries may have dropped those qualifiers without deliberate deception.

This activates the existing Ouros provenance and memory systems: receiving the summary never implies receiving the underlying record.

### Beat 4 — Every available intervention moves pressure somewhere

A local exclusion can protect one feature while increasing activity on another route. Leaving the situation unchanged can preserve habitat interactions while continuing documented losses. A targeted change can require monitoring and staffing. A broad removal can affect relationships that developed after the original introduction.

The player decision therefore selects an objective and accepts visible follow-up obligations.

### Beat 5 — Consequences return later

The arc must schedule at least one revisit. Later state can include:

- reduced loss at the protected feature;
- displacement toward another area;
- changed work schedules;
- new monitoring records;
- a revised public notice;
- increased or reduced trust in one institution;
- a newly eligible job or research task;
- altered availability of a service route;
- evidence that the initial diagnosis was incomplete.

A later review can revise the decision without erasing who authorized the first one or what happened under it.

## Investigation evidence model

Every material claim should preserve:

- claim ID;
- feature ID;
- observation time;
- observer or record source;
- observed population/species identity confidence;
- behavior actually observed;
- inferred impact, if any;
- authorization or publication from which an NPC learned the claim;
- later correction/update lineage.

Examples of safe observation descriptors:

- `POPULATION_PRESENT_OBSERVED`
- `FEEDING_DAMAGE_OBSERVED`
- `ROUTE_USE_OBSERVED`
- `NEST_SITE_OBSERVED`
- `HISTORICAL_CHARTER_RECEIVED`
- `CHARTER_SCOPE_QUALIFIER_FOUND`
- `IMPACT_CAUSE_UNRESOLVED`
- `INTERVENTION_EFFECT_REVIEW_DUE`

These are world/provenance states, not PTU statuses.

## Optional battle encounter

A battle is possible if a field intervention, work crew or player action causes a territorial confrontation. Combat is not mandatory for proving the narrative premise.

### Reduced implementation

Use an authored static tactical space with ordinary legal terrain, ordinary movement, verified targeting/range/LoS, core calculations and ordinary action economy. No custom population-control rule exists inside battle. No actor receives a free ecological action because of species flavor.

The objective can be ordinary defeat, withdrawal through an already-supported route, or completion of an external world task before/after combat. World consequences are applied from explicit semantic results after AutoPTU resolution.

### Intended rich version

A richer encounter may include refuge zones, noncombatants crossing the map, interception/rescue, territorial displacement, environmental barriers, changing work machinery, species-specific Moves/Abilities and an objective where forcing every combatant to zero HP is unnecessary.

That version is dependency-gated. It may not be simulated adapter-side while the engine families remain incomplete.

## Full-version dependency classification

Targeting / footprints / range / LoS: ordinary version can use currently verified audited contracts. Any concealment from vegetation, machinery or species-specific sensing requires additional exact evidence.

Base movement legality: ordinary authored walking spaces can use currently verified audited contracts. Burrowing, climbing, swimming, squeezing through habitat structures or species-specific traversal require source-backed contracts.

Complete movement: PARTIAL dependency for push/pull/knockback, forced displacement, interception, rescue and moving noncombatants.

Core calculations: ordinary deterministic combat calculations are currently verified within audited scope. No population or ecological effectiveness formula is added.

Action economy / initiative: ordinary actions are usable. Custom rescue, deterrence, gate-closing or handling actions require explicit contracts.

Full turn / round lifecycle: PARTIAL dependency for timed machinery, repeating environmental events, delayed arrivals or phase-driven objectives.

Full stateful damage pipeline: PARTIAL dependency for environmental or machinery damage.

Status lifecycle: PARTIAL dependency for any persistent mechanical condition. World labels such as `INTERVENTION_ACTIVE` are not statuses.

Terrain / weather / hazards / zones / reactions: MIXED / PARTIAL / BLOCKING for refuge zones, dynamic barriers, hazard areas, environmental reactions or specialized terrain.

Move-specific behavior: PARTIAL; verify each authored Move individually.

Abilities: PARTIAL; verify each authored Ability individually. Franchise descriptions never substitute for implementation evidence.

Items: PARTIAL; equipment used mechanically requires exact item support.

Trainer Features / perks: PARTIAL; specialist ecology, handling, research or command privileges require exact PTU/Caelo and engine verification.

AI legal-action infrastructure: currently verified within audited supported actions. It cannot invent ecological-control actions.

AI tactical policy: BLOCKING for general autonomous objective reasoning, rescue/interception and dynamic environmental tactics.

Minecraft / Cobblemon / Craftics adapter/playback: PARTIAL / BLOCKING end-to-end for rich objective state, dynamic hazards and specialized movement. Presentation cannot own rules.

## World-agent AI use

This proposal intentionally exercises the global NPC focus.

Different actors may hold:
- the original charter;
- a later summary;
- a complaint report;
- a field observation;
- a corrected species identification;
- a meeting decision;
- a revised public notice.

Receiving one item never grants the others. Institutional membership never creates shared omniscience. A review meeting should consume explicit received evidence and produce a new decision event with named recipients/publication scope.

Off-screen NPC work can include monitoring, archive lookup, route inspection, complaint filing, procurement, scheduling, public communication and review preparation.

## Canon questions intentionally left open

Region; district; historical date; original target problem; introduced species; target species; whether either remains classified as invasive or pest-like locally; responsible institution; current land ownership; productive resource; habitat significance; current economic damage; cultural attachment; charter wording; review authority; available interventions; final policy; and whether any battle version is desirable all remain unresolved.

No species should be selected solely because a franchise Pokédex entry superficially resembles the premise.