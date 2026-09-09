# The Crossing With No Result — Pass 378

Status: PROPOSED / NON-CANON
Date: 2026-09-09
Canon effect: NONE

## Premise

A field crew selects a routine crossing toward a survey destination and actually leaves its staging point. Partway along the route, the crew reaches a narrow passage where frightened or territorial Pokémon make ordinary world-level travel insufficient. The world-agent layer requests structured resolution and a concrete AutoPTU binding is accepted.

The world is saved before any AutoPTU result is ingressed.

After recovery, two facts are durable:

- the expedition genuinely started;
- structured-resolution ownership was genuinely accepted.

The world does not yet know whether the crew crossed, withdrew, was injured, calmed the Pokémon, found another route or remains engaged.

That missing terminal state is the hook rather than a reason to fabricate an outcome.

## Why it fits Ouros

Persistent NPCs can create consequences while the player is elsewhere. A later player investigation can begin from partial but reliable provenance instead of an omniscient quest marker.

The scenario also makes the AutoPTU boundary visible in fiction. World agents can decide and travel, but once a situation requires structured PTU mechanics the world layer hands authority away and waits for an explicit result before changing world facts.

No location, organization, route, species or historical event is approved by this proposal.

## Reduced implementation

The reduced version never enters AutoPTU.

A named field crew:

1. selects the survey destination;
2. begins semantic travel;
3. reaches a route state that cannot continue safely;
4. emits an explicit assistance/reroute communication;
5. remains at the last world-agent state until help, new information or a legal alternate route produces replanning.

Playable objectives can include locating the crew, carrying a message, bringing equipment, identifying an alternate route or coordinating a return.

Required world-agent support:

- semantic time and named-agent persistence;
- ordinary audited world-route planning/start;
- Communications and private knowledge;
- event-triggered replanning;
- plan-selection provenance;
- action-start provenance and V17 recovery.

No tactical battle capability is required.

## Intended full implementation

The full version permits the route interruption to become an explicit `REQUEST_AUTOPTU` handoff. Success conditions should be objective-based where possible: make the crossing safe, open a withdrawal path, protect vulnerable field equipment, calm or redirect the threat, or disengage once the route objective is satisfied.

A total KO sweep is not inherently the narrative objective.

### Engine capability dependencies

Targeting/footprints/range/LoS: VERIFIED within ordinary audited scope for simple spatial engagement. Complex visibility geometry remains subject to exact encounter layout.

Base movement legality: VERIFIED within audited ordinary scope.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any narrow-passage design that relies on forced displacement, interception or carrier movement is gated on those exact mechanics.

Core calculations: VERIFIED within audited deterministic scope.

Action economy/initiative: VERIFIED for audited primitives. Java merge #415 adds direct oracle-backed evidence for authoritative round rollover/initiative cursor state, but does not establish every lifecycle interaction.

Full turn/round lifecycle: PARTIAL. The encounter must not assume all round-start/end families are complete.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. Flooding, collapsing ground, reactive choke points or weather phases require explicit verified contracts before use as tactical rules.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for protect-equipment, route-clearing, escort, calming/redirecting, objective-aware withdrawal and disengage-after-objective unless those policies are separately demonstrated.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for persistent route/objective identity, non-KO acknowledgement and authoritative end-to-end playback/result return.

## Reduced tactical fallback

If a battle presentation is desired before richer objective policy exists, the route interruption can use only currently verified ordinary targeting, movement, calculation and action primitives with a simple legal stop condition owned by the narrative adapter. Do not simulate unsupported pushes, reactive terrain, staged weather, delayed statuses or Trainer Feature interrupts merely for spectacle.

The world premise remains unchanged: the crew left, reached a structured interruption, and the later world state waits for an authoritative result.

## Canon questions

Before promotion, decide from approved Ouros/Caelo material:

- which established route or geography can support a meaningful choke point;
- which institution or recurring NPC crew has reason to make the trip;
- which species are locally valid;
- what communication infrastructure exists along the route;
- what field equipment or survey purpose is already established;
- whether the interruption is routine ecology, exceptional behavior or evidence of a larger event.

Until those questions are answered, all proper nouns and local facts remain placeholders.