# AutoPTU World Observation Owner Contract — Pass 419

Status: ACTIVE IMPLEMENTATION CONTRACT

## Purpose

Pass 418 can commit an explicitly mapped `WorldConsequenceTransaction` after an admitted AutoPTU result. Pass 419 adds one deliberately small world owner that can consume only `FIELD_OBSERVATION` consequences.

This seam proves that a tactical result can create one persistent world observation without asking the world layer to reinterpret battle state.

## Authority boundary

The owner consumes only fields already projected into the committed transaction.

It does not read or reconstruct:

- HP or Injuries;
- Status Afflictions;
- initiative or turn order;
- positions, range or line of sight;
- Moves, Abilities, Items or Trainer Features;
- weather, terrain, hazards, zones or reactions;
- a tactical transcript;
- hidden engine state.

`WORLD_OBSERVATION_OWNER != BATTLE_INTERPRETER`

## Accepted consequence

The only accepted consequence kind is:

`FIELD_OBSERVATION`

Accepted projected fields:

- `objective_ref` — required;
- `outcome` — required;
- `evidence_ref` — optional.

Every accepted record also preserves the transaction identity, durable AutoPTU session identity, authoritative result reference and provenance reference already frozen upstream.

## Replay rule

A repeated transaction with identical content is idempotent.

A repeated transaction identity with different content fails closed.

The owner does not generate a replacement transaction ID and does not derive one from its payload.

## No implicit quest completion

An observation can say that an objective outcome was `PARTIAL`, `COMPLETE` or another admitted semantic value. This record does not itself complete a quest, change a relationship, alter ecology or schedule an obligation.

Those are separate owners with separate admission contracts.

## Reduced implementation value

This owner is intentionally useful before richer persistent consequences exist. A battle or structured field objective can leave a durable sourced observation while all unsupported tactical detail remains inside AutoPTU.

## Current capability posture

No new tactical capability family becomes verified through this pass.

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by mechanism.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary scopes.
AI tactical policy: BLOCKING for specialized objective policies unless explicitly implemented.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives and in-flight battle recovery.

## Next boundary

A later owner may convert a committed observation into a world-agent knowledge event or a specific obligation, but it must cite the observation transaction and preserve provenance. It must not re-open the original tactical payload.
