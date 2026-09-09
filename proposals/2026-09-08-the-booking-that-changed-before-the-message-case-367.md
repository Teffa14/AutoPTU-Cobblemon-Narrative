# The Booking That Changed Before the Message — Pass 367

Status: PROPOSED / NON-CANON
Date: 2026-09-08

## Premise

Two field teams need the same survey instrument. A real conflict is admitted and an authorized scheduler selects the deadline-sensitive survey. The allocation decision is then applied to the operational planning view, displacing the competing booking, but no notice has yet reached the displaced team when the world is saved.

After restart, the scheduler and booking system can correctly reflect the applied decision while a technician from the displaced team continues preparing for the old booking from information that was valid when they last checked.

Nobody must lie. Nobody needs global amnesia. The disagreement comes from different causal owners and different knowledge histories.

## Reduced version

The reduced version runs entirely in world-state systems. The player can discover the mismatch through the reservation history, conflict admission, authority evidence, allocation decision, application record, communication state and individual knowledge. Possible responses include carrying the update to the displaced team, arranging another resource, changing the observation route, or documenting why the earlier plan changed.

No AutoPTU handoff is required.

## Mechanically rich version

The displaced team may already be travelling toward the instrument or an obsolete observation site. The player can try to reach them before a time-sensitive field window closes. A wild encounter or environmental obstruction can complicate the route while the narrative objective remains to communicate, reroute, protect the instrument or withdraw safely.

A basic implementation can omit tactical interception and resolve travel semantically. The premise remains unchanged.

## Capability dependencies

Targeting/footprints/range/LoS: VERIFIED within previously audited ordinary contracts if a local encounter occurs.

Base movement legality: VERIFIED within previously audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Any literal tactical interception, carrier displacement or forced separation depends on this family.

Core calculations: VERIFIED within previously audited deterministic scope.

Action economy/initiative: VERIFIED for audited primitives. Pickup, drop, guard, handoff and objective interactions remain individually gated.

Full turn/round lifecycle: PARTIAL. A round-counted deadline depends on this family.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Weather-gated observation or hazard zones require explicit verified support.

Move-specific behavior: individually gated / PARTIAL.

Abilities: individually gated / PARTIAL.

Items: individually gated / PARTIAL.

Trainer Features/perks: individually gated / PARTIAL.

AI legal-action infrastructure: VERIFIED for ordinary audited action-generation scope; cargo and bespoke objective actions require dedicated contracts.

AI tactical policy: BLOCKING for intercept-to-inform, protect-carrier, preserve-resource, reroute and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for cargo identity, timed objective acknowledgement and authoritative end-to-end playback.

## Canon boundary

This scenario does not establish the existence of a named institution, survey programme, instrument, policy or location in Ouros. Those bindings require later canon approval. The proposal introduces no PTU rule or Caelo fact.
