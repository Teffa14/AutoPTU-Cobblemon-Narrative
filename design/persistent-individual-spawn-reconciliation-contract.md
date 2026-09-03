# Persistent individual / Cobblemon spawn reconciliation contract

Status: PROPOSED DESIGN CONTRACT
Date: 2026-09-03
Pass: 239

## Purpose

Define how Ouros projects canonical wild Pokémon into Minecraft/Cobblemon without allowing entity creation, despawn, unload, UUID churn or generic spawn logic to clone or delete population members.

This contract consumes Pass 238 population/demography state and prepares Pass 240 observation/research state.

## Authority

Ouros owns:

- population membership;
- persistent individual identity;
- unresolved member pool slots;
- lease ownership;
- identity promotion;
- canonical ecological condition;
- semantic removal/return outcomes.

Minecraft/Cobblemon owns:

- entity UUID;
- current rendered position;
- animation/presentation;
- chunk-local presence;
- realtime visible movement requests;
- native spawn attempt surface.

AutoPTU owns structured battle mechanics after explicit handoff.

## Core invariant

```text
canonical member or already-counted unresolved slot
-> at most one active presentation lease
-> at most one active Minecraft/Cobblemon actor
```

A presentation actor never creates a new population member.

## Canonical source classes

```text
PERSISTENT_MEMBER
UNRESOLVED_POOL_SLOT
TRANSIENT_COHORT_MEMBER
EXTERNAL_ASSOCIATED_INDIVIDUAL
```

Examples:

- the first canon Sendero Fletchling uses `PERSISTENT_MEMBER`;
- an ordinary unnamed member from the same population can use `UNRESOLVED_POOL_SLOT`;
- a Pass 235 migrant can use `TRANSIENT_COHORT_MEMBER` without joining the resident population;
- Redline remains `EXTERNAL_ASSOCIATED_INDIVIDUAL` and cannot consume a wild population slot.

## Presentation lease record

Minimum proposed record:

```text
lease_id
lease_class
canonical_source_id
population_id_or_null
member_id_or_null
unresolved_slot_token_or_null
cohort_id_or_null
species_id
form_id
lease_state
minecraft_dimension_or_null
minecraft_entity_uuid_or_null
materialized_at_tick_or_null
last_seen_tick_or_null
suspension_reason_or_null
battle_id_or_null
revision
```

## Lease states

```text
AVAILABLE
RESERVED
MATERIALIZED
ENGAGED
SUSPENDED
RELEASE_PENDING
RELEASED
INVALIDATED_WITH_AUDIT
```

State meaning:

- `RESERVED`: source slot is locked before entity creation;
- `MATERIALIZED`: one visible actor is correlated;
- `ENGAGED`: source is locked to a structured interaction/battle;
- `SUSPENDED`: canonical source remains active but has no trusted visible actor;
- `RELEASED`: projection lock is free;
- `INVALIDATED_WITH_AUDIT`: adapter correlation became unsafe and requires reconciliation.

## Reservation-before-spawn rule

Ouros must reserve first and materialize second.

```text
eligible source slot
-> atomic lease reservation
-> adapter spawn request
-> successful entity UUID correlation
-> MATERIALIZED
```

If materialization fails, the lease returns to `RELEASED`/available state without changing population truth.

A generic entity observed before a valid lease exists is not automatically canonized.

## Unresolved pool slot tokens

An unresolved pool lease represents one already-counted member.

Token requirements:

- unique within `population_id`;
- non-reusable while an active lease exists;
- persisted independently of entity UUID;
- safe to release and later reuse only after prior lease closure;
- never counted in addition to `unresolved_member_pool_count`.

```text
active_unresolved_leases <= unresolved_member_pool_count
```

## Persistent member uniqueness

For every `member_id`:

```text
active_lease_count(member_id) <= 1
```

If Minecraft exposes a second entity claiming the same member correlation, Ouros must reject/quarantine the duplicate presentation and retain the original canonical member.

## Identity promotion

An unresolved member can become persistent when individual history becomes narratively or ecologically meaningful.

Atomic transaction:

```text
require active unresolved source slot
require unresolved_member_pool_count >= 1
create new persistent member_id
unresolved_member_pool_count -= 1
known_persistent_member_ids += member_id
rebind active lease source to member_id
population_total unchanged
```

Promotion reasons must be typed, for example:

```text
REPEATED_RESEARCH_IDENTIFICATION
STRUCTURED_ENCOUNTER
CAPTURE_ATTEMPT
DISTINCTIVE_INJURY_OR_MARK
NEST_PARENT_ROLE
MIGRATION_ROLE
AUTHORED_STORY_ROLE
```

Promotion is not a demographic event because abundance does not change.

## Despawn and unload

These events cannot change population membership:

```text
MINECRAFT_DESPAWN
CHUNK_UNLOAD
DIMENSION_UNLOAD
SERVER_RESTART
ENTITY_DISCARDED
ENTITY_UUID_LOST
```

They can only change projection state.

Default safe behavior:

```text
MATERIALIZED -> SUSPENDED/RELEASED
minecraft_entity_uuid -> null
canonical source persists
```

## Restart reconciliation

On server/world restart:

1. load canonical population/member state;
2. load lease ledger;
3. inspect surviving entity correlations when available;
4. accept only one valid entity per active lease/source;
5. invalidate stale UUIDs;
6. never infer death/emigration from missing entities;
7. allow rematerialization from canonical state when ecology permits.

## Battle handoff lock

Before structured battle:

```text
MATERIALIZED -> ENGAGED
```

While `ENGAGED`:

- no second lease may be issued for the source;
- generic spawn logic must not project the same source slot;
- battle snapshot uses canonical/Ouros-authored state, not mutable Cobblemon payload as PTU truth.

Post-battle semantic outcomes:

```text
KO_ONLY -> return to ecology, no abundance delta
RETREAT -> return/reposition through ecology semantics, no automatic abundance delta
CAPTURE_CONFIRMED -> close lease + CAPTURE_REMOVAL demographic event
AUTHORIZED_RELOCATION -> close/rebind with paired demographic events
DEATH_CONFIRMED_BY_OUROS_POLICY -> ecological mortality event only if the active rules/profile allows that semantic result
```

## Generic spawn intake

Native Cobblemon spawn attempts may be used as a placement opportunity, but not as source creation.

Preferred integration:

```text
spawn opportunity
-> Ouros asks which canonical source is eligible here/now
-> reserve lease
-> materialize approved species/form/presentation
```

If interception is not technically possible in the current adapter, generic actors must remain explicitly non-authoritative until matched through a safe reconciliation seam. They cannot enter structured combat as canon merely because they exist.

## Actor eligibility

Projection selection may consume:

```text
population membership
+ activity/exposure state
+ time/weather context
+ microhabitat eligibility
+ disturbance/habituation state
+ current lease locks
+ individual role/nesting/migration state
+ adapter capacity
```

Selection affects visibility only.

## Failure handling

### Duplicate actor

If one canonical source maps to multiple live entities:

```text
keep canonical source
select at most one trusted lease correlation
quarantine/discard duplicate presentation
emit reconciliation audit event
population delta = 0
```

### Lost actor

If lease says materialized but entity no longer exists:

```text
invalidate UUID correlation
suspend/release lease
population delta = 0
```

### Reused/stale UUID

UUID is correlation data only. A mismatch in species/source revision invalidates the correlation; it never overwrites canonical identity.

## Observation boundary

Pass 240 consumes sightings, not lease internals.

The observation layer may classify evidence as:

```text
KNOWN_INDIVIDUAL_CONFIRMED
KNOWN_INDIVIDUAL_PROBABLE
UNRESOLVED_INDIVIDUAL
SPECIES_PRESENCE_ONLY
```

Player/NPC knowledge must not receive `unresolved_slot_token`, internal lease ID or raw population totals unless another system explicitly authorizes that knowledge.

## Marea first-slice binding

Canon member:

`ouros.marea.encounter.sendero_lower_shelf.fletchling.0`

must always satisfy:

```text
active_lease_count <= 1
```

Redline remains external and cannot be reconciled into `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`.

## Reduced implementation

The reduced version can run with:

- canonical population/member storage;
- lease ledger;
- adapter spawn/despawn correlation;
- create-only battle blueprint publication;
- idempotent release/rebind.

No rich PTU movement/terrain/AI mechanics are required.

## Rich encounter dependencies

If a leased ecological actor enters a mechanically rich encounter, classify only the mechanics actually used:

- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

## Acceptance gates

Pass 239 is ready for implementation when a deterministic fixture proves:

1. one canonical persistent member cannot own two active leases;
2. unresolved leases do not alter abundance;
3. lease release/despawn/unload do not alter abundance;
4. identity promotion conserves abundance;
5. ENGAGED actors cannot respawn concurrently;
6. KO-only result does not remove a member;
7. capture removal requires semantic confirmation and a demographic event;
8. stale UUID repair preserves canonical state;
9. server restart can reconstruct safe lease state;
10. external associated individuals cannot consume resident wild slots.

## Canon status

PROPOSED.

This contract does not change species availability, actual abundance, battle rules, capture rules or the canon identity of the first Sendero Fletchling.