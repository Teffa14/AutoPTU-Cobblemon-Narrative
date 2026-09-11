# AutoPTU World Observation Explicit Delivery Contract — Pass 420

Status: ACTIVE IMPLEMENTATION CONTRACT

## Purpose

Pass 419 can materialize an admitted AutoPTU world consequence as one persistent `WorldObservationRecord`. Pass 420 connects that record to the existing private information network without turning institutional membership into omniscient knowledge.

The seam is deliberately narrow: one explicit custodian receives the record, then one explicit recipient may receive a report through one explicit communication channel.

`OBSERVATION_EXISTS != EVERYONE_KNOWS`

## Authority boundary

The delivery seam consumes only a committed `WorldObservationRecord`.

It never re-opens the AutoPTU result payload and never reads tactical state such as HP, initiative, positions, status, weather, terrain, Moves, Abilities, Items or Trainer Features.

The sender-side source claim is an `INSTITUTIONAL_RECORD`, not a `DIRECT_OBSERVATION`. Its subject and value come from the committed observation's `objective_ref` and `outcome`. Its provenance root is the observation transaction identity, which remains the pointer to the upstream admitted result provenance.

## Explicit identities

A delivery requires all of the following:

- one `custodian_id`;
- one `recipient_id`;
- one `channel_id`;
- one source claim identity;
- one delivery event identity;
- one message identity;
- one receiver claim identity;
- one semantic creation minute.

No faction, organization or role automatically expands that audience.

## Existing communication semantics

The seam delegates actual transmission to `InformationEventQueue`.

Channel latency, availability, local acknowledgement, terminal delivery state, restart persistence and report confidence remain owned by the existing global NPC information system.

Before the event is due, the recipient does not know the claim merely because the custodian has it. A failed channel does not create recipient knowledge. A different member of the same institution receives nothing unless separately targeted.

## Provenance

The custodian's source claim uses the world-observation transaction ID as its provenance root. The ordinary `transmit_claim()` path preserves that root when the recipient receives a `REPORT` claim.

The returned scheduling record also preserves the observation's upstream `provenance_ref`. This keeps both the local delivery chain and the original admitted-result provenance addressable without copying tactical detail into the world-agent layer.

## Replay

Re-scheduling the same observation delivery with the exact same event envelope is idempotent before or after terminal delivery.

Reusing the event identity with a different recipient or other envelope content fails closed. Reusing a source claim identity for a different observation also fails through the existing claim collision guard.

## Reduced implementation value

This seam enables stale-information stories immediately. A field result can exist, be recorded at one desk and still fail to affect another team until a concrete message reaches them.

No battle is required for that reduced version.

## Capability posture

No tactical capability family is promoted by this pass.

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary scopes.
AI tactical policy: BLOCKING for specialized rescue, warning-aware withdrawal and objective policies unless explicitly implemented.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives and in-flight battle recovery.

## Next boundary

The existing delivery-to-replanning coordinator can eventually consume the successful recipient delivery and wake only that named actor. A future integration pass should prove that the AutoPTU-derived observation can flow through delivery into selective replanning without bypassing the communication queue or broadening the audience.