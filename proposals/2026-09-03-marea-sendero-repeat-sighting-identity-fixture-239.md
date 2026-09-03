# Marea / Sendero repeat-sighting identity fixture — Pass 239

Status: PROPOSED ECOLOGY / OBSERVATION BRIDGE
Date: 2026-09-03
Pass: 239

## Premise

Researchers on Sendero del Vidrio repeatedly see Fletchling near the lower shelf over several visits. One is the canon first persistent wild Fletchling. Other visible birds may be unresolved members of the same population.

The player-facing question is deliberately narrower than the hidden truth:

“Are we seeing the same individuals again, or different members of the local population?”

The fixture makes this question playable without exposing the population ledger or making every Minecraft entity permanent.

## Canon anchors

Use only established anchors:

- site: `ouros.marea.sendero_vidrio`;
- population: `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`;
- canon persistent member: `ouros.marea.encounter.sendero_lower_shelf.fletchling.0`;
- Redline remains Pia Min's external partner and cannot enter the wild population.

No additional species, actual abundance or named wild Fletchling is canonized by this proposal.

## Hidden Ouros state

Ouros knows which projected actor lease comes from:

- the canon persistent member;
- an unresolved pool slot;
- a transient/external source.

The player does not see lease IDs.

## Visible evidence loop

Visit 1:

- player sees one or more Fletchling;
- observation stores species, location/time context and any reliable visible traits;
- no identity claim is required.

Visit 2:

- a projected actor may be the same persistent member with a different Minecraft entity UUID;
- similarity creates `possible_repeat_individual`, not automatic confirmation;
- a missed sighting does not mean the individual left the population.

Visit 3+:

- repeated high-quality evidence can justify an observation confidence increase;
- if gameplay creates a durable individual history, Ouros may promote an unresolved member into persistent identity atomically;
- promotion preserves total abundance.

## Research interaction hooks

Player actions can improve evidence without granting raw truth:

- photograph from useful angles;
- record time and microhabitat;
- note distinctive natural marks/injuries when present;
- log nest/parent role;
- compare calls or behavior if the relevant species profile supports that evidence;
- return under different conditions.

Bad evidence can stay ambiguous.

## Consequences

Good fieldwork can unlock:

- stronger confidence that a recurring individual is present;
- a longitudinal observation record;
- targeted welfare/behavior follow-up;
- detection of disappearance as an investigation question rather than an automatic death/emigration event;
- later NPC knowledge propagation in Pass 240.

The reward is knowledge quality and continuity, not guaranteed capture or population manipulation.

## Reduced implementation version

The reduced version needs only:

- lease/source binding in Ouros;
- sighting records with confidence;
- ability to rematerialize the same persistent member under a new Minecraft UUID;
- unresolved pool actors that do not become permanent by default.

No battle is required.

## Intended richer version

A recurring individual can later be involved in an ecological encounter such as:

- defending a nest;
- reacting to a disturbance corridor;
- being displaced during a migration pulse;
- entering structured battle after player escalation.

Only the mechanics actually used should activate AutoPTU dependencies.

For example, a simple conventional battle can remain inside verified targeting/base movement/core/action-economy infrastructure plus the exact selected Move/Ability support. A timed nest-defense corridor with interception, forced movement and reaction zones additionally depends on complete movement, lifecycle, terrain/zones/reactions, tactical AI and adapter/playback.

## Failure cases protected by the fixture

- same canon member appears twice at once;
- new entity UUID is mistaken for new Pokémon;
- despawn is interpreted as emigration/death;
- repeated species sighting is automatically merged into one identity;
- unresolved member is promoted without consuming one unresolved pool slot;
- observation confidence writes back into population truth;
- Redline is mistaken for a wild population member.

## Canon status

PROPOSED.

This fixture exists to validate continuity and observation gameplay while preserving the established wild population canon.