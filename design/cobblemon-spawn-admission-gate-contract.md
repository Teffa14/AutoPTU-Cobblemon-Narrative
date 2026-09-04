# Cobblemon spawn admission gate contract — Pass 250, corrected by Pass 251

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE until separately approved

## Purpose

Pass 249 defined how Ouros should treat direct entities, indirect signs, no-presentation results and uncorrelated Pokemon entities. Pass 250 bound that policy to Cobblemon spawn-control primitives. Pass 251 narrows the event claim against the tagged Cobblemon 1.7.3 source so the adapter does not pretend that one event covers every PokemonEntity lifecycle path.

## Verified Cobblemon 1.7.3 primitives

At upstream tag `1.7.3`:

- `CobblemonEvents.ENTITY_SPAWN` is a `CancelableObservable<SpawnEvent<*>>`.
- `CobblemonEvents.POKEMON_ENTITY_SPAWN` is the PokemonEntity-filtered projection of that same event.
- `SpawnEvent` explicitly documents that it fires for an entity spawned using `BestSpawner` and that cancellation prevents that spawn.
- `SingleEntitySpawnAction.run()` creates the entity, posts `ENTITY_SPAWN`, and only on success calls `world.addFreshEntity(e)`.
- `PokemonSpawnAction` is a `SingleEntitySpawnAction<PokemonEntity>` used by the spawning system.
- Spawn Rules support `filter` and `location` components that can block natural spawn candidates earlier in the spawning process.
- Cobblemon also exposes separate `POKEMON_SENT_PRE` / `POKEMON_SENT_POST` events for party send-out lifecycle.

These are adapter affordances, not Ouros canon.

## Critical scope correction

`POKEMON_ENTITY_SPAWN` must not be described as a universal stream for every PokemonEntity entering the world.

The verified 1.7.3 contract is narrower: it observes PokemonEntity instances flowing through Cobblemon's `BestSpawner` spawn action path.

Therefore:

- Gate B can safely reason about candidates that actually traverse this verified spawner path.
- Owned party send-outs, entity loads/restores, commands, integrations or other presentation paths must not be assumed to traverse Gate B unless separately verified.
- A listener must never cancel or classify an unrelated lifecycle path merely because the object is a PokemonEntity.
- Absence from `POKEMON_ENTITY_SPAWN` is not evidence that an entity is wild, owned, restored or authoritative.

This correction supersedes the Pass 250 wording that treated the stream as entity-wide.

## Two-gate model for verified BestSpawner natural projection

### Gate A — early natural-spawn policy

Within an Ouros-managed ecological scope, use Cobblemon Spawn Rules or an equivalent version-supported configuration to deny generic natural direct presentation that would bypass Ouros source reservation.

Gate A reduces uncontrolled BestSpawner candidates. It does not reserve a population member, create identity or authorize a direct actor.

### Gate B — cancellable BestSpawner backstop

Subscribe to the supported cancellable Pokemon spawn surface for candidates that flow through `BestSpawner`.

Within an Ouros-managed ecological scope the verified classes are:

- `OUROS_MANAGED_DIRECT`
- `UNCONTROLLED_BESTSPAWNER_WILD`
- `UNKNOWN_BESTSPAWNER_CANDIDATE`

`EXEMPT_OWNED_OR_SYSTEM_PRESENTATION` is removed from this event classifier. Those paths require their own lifecycle-specific verification and remain outside wild ecological authority.

## OUROS_MANAGED_DIRECT

Admission requires all of the following before a BestSpawner Pokemon entity becomes trusted presentation:

1. projection envelope permits direct presentation;
2. an already-counted Ouros source is selected;
3. a Pass 239 projection lease is active;
4. a one-use adapter admission token exists for that lease;
5. species/form requested by materialization agrees with the leased source profile;
6. scope/location agrees with the request within adapter tolerance;
7. token has not already admitted another entity.

On successful admission:

- consume the one-use admission token;
- correlate the resulting Minecraft UUID to the active lease;
- keep persistent actor identity in Ouros state;
- expose only sanitized observation data externally;
- do not change population total.

If any required field fails, cancel the BestSpawner event when it is still inside the verified cancellable path. Never repair a mismatch by inventing a population member.

## UNCONTROLLED_BESTSPAWNER_WILD

A generic BestSpawner Pokemon candidate inside an Ouros-managed ecological scope without an Ouros admission token has no authoritative source.

Required result:

- `presentation_admitted = false`
- `ecology_write_authorized = false`
- `population_delta = 0`
- `persistent_actor_created = false`
- `autoptu_eligible = false`

Cancellation is presentation control only. It cannot become death, capture, emigration or evidence that the persistent population does not exist.

## UNKNOWN_BESTSPAWNER_CANDIDATE

If a candidate traverses the verified BestSpawner event but its provenance cannot be reconciled, fail closed for wild ecological authority. Inside a managed scope, cancellation is the safe default for the verified 1.7.3 event path unless a separately documented integration requires another treatment.

Unknown provenance must never be upgraded to a persistent wild actor automatically.

## Non-BestSpawner PokemonEntity paths

Owned send-out, recall, load/restore, command and third-party integration paths are separate adapter concerns.

Current policy:

- do not create wild membership from physical presence;
- do not use Gate B as proof that these paths were observed;
- preserve valid owned/system gameplay through lifecycle-specific hooks;
- use separate correlation/reconciliation contracts where persistent Ouros actors are restored;
- quarantine ecological authority when provenance is unresolved;
- add a dedicated regression for each path before declaring it controlled.

Cobblemon 1.7.3 exposes `POKEMON_SENT_PRE` and `POKEMON_SENT_POST`; those events are evidence that party send-out has an explicit lifecycle surface and should not be conflated with BestSpawner natural spawning.

## Admission token

Minimum token shape:

```text
token_id
lease_id
source_id
species_id
form_id
scope_id
issued_at
expires_at
consumed
request_correlation_id
```

Properties:

- one token admits at most one BestSpawner Pokemon entity;
- token creation does not create population;
- token consumption does not create population;
- expired or reused token fails admission;
- entity UUID is written only after successful admission;
- restart invalidates unresolved runtime tokens unless a later persistence contract explicitly says otherwise.

## Ordering contract

For Ouros-managed direct projection:

```text
projection envelope eligible
-> select already-counted source
-> reserve lease
-> issue one-use admission token
-> request versioned Cobblemon materialization
-> verified BestSpawner Pokemon spawn callback
-> validate/consume token
-> event succeeds
-> entity is added to world
-> correlate Minecraft UUID
```

Forbidden order:

```text
uncontrolled entity appears
-> search for a similar population member
-> reserve or invent source retroactively
```

Presentation cannot author ecology.

## Cancellation ordering evidence

Cobblemon 1.7.3 `SingleEntitySpawnAction.run()` posts `ENTITY_SPAWN` before `world.addFreshEntity(e)` and only executes the add-to-world block when the event succeeds. This is strong source-level evidence that cancellation on this path occurs before world insertion.

It does not prove that every command, restore, send-out or third-party entity creation path uses the same ordering.

## Spawn Rules relationship

Spawn Rules are an early filtering layer. They may reduce generic spawn generation inside managed habitats or for managed species.

They must not encode hidden persistent counts, lease IDs or individual identities. A Spawn Rule passing a candidate does not authorize direct projection; Gate B remains the backstop for the verified BestSpawner path.

## Indirect evidence

Suppressing a direct entity must not suppress ecological evidence. Pass 249 `INDIRECT_SIGN` remains independent.

A cancelled generic BestSpawner candidate does not automatically become a new evidence root. Signs must originate from Ouros-approved sign generation or a valid admitted actor.

## AutoPTU boundary

Spawn admission never opens AutoPTU.

Only a valid admitted direct actor can later be considered by the Pass 242 encounter-intent evaluator. A cancelled or unresolved candidate cannot enter a combatant manifest.

## Executable invariants

- managed direct admission requires a prior active lease;
- managed direct admission requires a live unused token;
- one token admits no more than one entity;
- UUID correlation follows successful admission;
- generic BestSpawner candidates cannot mutate population state;
- non-BestSpawner physical presence cannot become wild membership by inference;
- cancellation cannot become mortality/emigration/capture truth;
- spawn-rule pass does not substitute for lease/token admission;
- cancelled candidates cannot open AutoPTU;
- restart clears unresolved runtime tokens without deleting persistent population state;
- a Cobblemon upgrade must re-verify event type, event scope and cancellation ordering.

## Capability dependencies

Reduced ecology projection path:

- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING until the Ouros runtime dependency is pinned and the 1.7.3-compatible contract is implemented/tested there;
- AutoPTU tactical capability families: NOT REQUIRED.

Rich pursuit/interception after a valid admitted actor additionally depends on the exact tactical families used, including complete movement for interception/forced movement interactions, lifecycle, tactical AI and adapter/playback. Terrain, reactions, damage, statuses, Moves, Abilities, Items and Trainer Features are dependencies only when the encounter actually uses them.

## Version status

Upstream Cobblemon 1.7.3 is a verified compatibility target for this contract, not proof of the Ouros runtime's current dependency pin.

The project still needs to locate or establish the actual Cobblemon/loader/Minecraft version used by the writable integration project. Until then, adapter implementation remains BLOCKING even though the upstream 1.7.3 seam is source-verified.
