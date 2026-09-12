# Replacement Offer Reply and World Continuity Research — Pass 448

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Research date: 2026-09-12

Scope

This pass looked for reusable structures that help Ouros keep negotiation, travel, local world change and NPC knowledge causally separate. No protected dialogue, named characters, plots, regions, factions or distinctive scene sequences are imported.

## New public anchors

### Citizen Sleeper

Source: https://citizensleeper.com/

The public description frames play cycle by cycle around contracts, factions, survival pressure, small victories and relationships. The reusable lesson for Ouros is concurrency: one social agreement can exist while other obligations and pressures continue to advance. A decision made by one actor therefore should not freeze the rest of the world or become shared knowledge automatically.

Ouros transformation:

- preserve the replacement offer and the requester's answer as separate durable facts;
- let schedules, access, ecology and other obligations continue while the reply travels;
- evaluate any eventual encounter from current world state rather than the state that existed when the offer was authored.

Excluded: setting, characters, corporations, terminology, plot, dialogue and contract content.

### Roadwarden

Source: https://moralanxietystudio.com/

The official description emphasizes exploring and changing a hostile world, travel, trust-building conversations, sidequests and investigation. The useful abstraction is that movement and relationships are processes with local state. A message about a future trip can be truthful when sent yet arrive after route conditions, trust or local circumstances have changed.

Ouros transformation:

- message delivery never reserves a route or guarantees access;
- trust may affect later interpretation, but transport itself cannot assign relationship change;
- a received acceptance authorizes only the next social/system step, not physical execution.

Excluded: setting, lore, locations, characters, quest text and plot structure.

### Pokémon tabletop travel/exploration discussions

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/1h4k1ui/
- https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9/

Public GM discussion describes route travel as a mixture of ordinary movement, wild Pokémon, trainers, side events, hidden locations and environmental incidents. Another GM describes Pokémon acting inside the environment through small local behaviors rather than standing as passive battle nodes.

Ouros transformation:

- the trip attached to a renegotiated obligation can acquire new local incidents after agreement;
- wild Pokémon activity may become evidence, access pressure or an optional scene without forcing combat;
- route content should be generated or selected from current ecology/world state, not precommitted by the social negotiation system;
- a mechanically rich incident can have a reduced non-combat or basic-mechanics version while preserving the same narrative premise.

Excluded: exact encounter tables, exact Pokémon scenes, map layouts, campaign-specific routes and GM-authored story content.

## Cross-check against Ouros/PTU/Caelo project assumptions

The recursive repository inventory and focused audit of `CURRENT_FOCUS.md`, canon surfaces, assistance contracts, information-network code, research/proposal history and Kairos/Caelo routing material preserve the same boundaries:

- NPC knowledge remains private until explicit receipt;
- world-agent state persists off-screen;
- communication does not become travel, access, resources or combat execution;
- AutoPTU handoff occurs only for structured mechanics;
- PTU/Kairos/Caelo references are comparison evidence and routing aids, not automatic canon or automatic capability admission.

No canon file is changed by this pass.

## Reusable design lessons

A social answer can be final for the speaker while still unknown to the other party. A route can change during that latency. An accepted future objective can later need a different tactical realization because ecology, weather, access or schedules changed. Those three facts should remain separate.

This supports longer arcs built from small obligations: repeated local commitments can establish reliability, friction or trust only after later systems consume explicit outcomes. The message transport layer itself must remain socially neutral.

## Mechanical dependency posture

The reduced Pass 448 story pattern requires no AutoPTU battle capability.

For later rich variants, dependency admission stays conservative:

- targeting/footprints/range/LoS: VERIFIED only in audited scopes;
- base movement legality: VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only in audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by behavior;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: specialized verbs require explicit admission;
- AI tactical policy: BLOCKING for specialized objectives unless separately verified;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

AutoPTU-Java evidence at `62f7f3671fd4176c49b359c8625e245905b19e2f` verifies an additional ordering guard for a specific Quick Switch ally-faint trigger. It does not justify a category-wide promotion. AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, with a presentation-only head.