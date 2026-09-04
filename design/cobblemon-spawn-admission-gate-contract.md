# Cobblemon spawn admission gate contract — Pass 250

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE until separately approved

## Purpose

Pass 249 defined how Ouros should treat direct entities, indirect signs, no-presentation results and uncorrelated Pokemon entities. This contract binds that policy to publicly verified Cobblemon spawn-control primitives without moving ecological or PTU authority into the adapter.

## Verified Cobblemon primitives

Current public Cobblemon source exposes:

- `CobblemonEvents.ENTITY_SPAWN` as `CancelableObservable<SpawnEvent<*>>`;
- `CobblemonEvents.POKEMON_ENTITY_SPAWN` as the PokemonEntity-filtered stream;
- Spawn Rules `filter` components capable of blocking natural spawn candidates.

Historical changelog evidence explicitly records that SpawnEvent cancellation was fixed to respect `Cancelable#cancel`.

These primitives are adapter affordances, not Ouros canon.

## Double-gate model

### Gate A — natural spawn policy

Within an Ouros-managed ecological scope, use Cobblemon Spawn Rules or equivalent supported configuration to deny natural direct Pokemon presentation that would bypass Ouros source reservation.

Gate A reduces uncontrolled candidates early. It does not reserve a population member, create identity or authorize a direct actor.

### Gate B — entity admission backstop

Subscribe to the supported cancellable Pokemon entity-spawn surface.

For every Pokemon entity candidate entering an Ouros-managed scope, resolve an admission class before accepting ecological authority.

Allowed admission classes:

- `OUROS_MANAGED_DIRECT`
- `EXEMPT_OWNED_OR_SYSTEM_PRESENTATION`
- `UNCONTROLLED_NATURAL`
- `UNKNOWN_OR_UNCLASSIFIED`

The event must fail closed for ecological authority when the class is unknown.

## OUROS_MANAGED_DIRECT

Admission requires all of the following before the Pokemon entity becomes trusted presentation:

1. projection envelope permits direct presentation;
2. an already-counted Ouros source is selected;
3. a Pass 239 projection lease is active;
4. a one-use adapter admission token exists for that lease;
5. species/form requested by the materialization agrees with the leased source profile;
6. scope/location agrees with the request within adapter tolerance;
7. token has not already admitted another entity.

On successful admission:

- consume the one-use admission token;
- correlate returned Minecraft UUID to the active lease;
- keep persistent actor identity in Ouros state;
- expose only sanitized observation data externally;
- do not change population total.

If any required field fails, cancel or quarantine the entity according to the supported adapter mechanism. Never repair the mismatch by inventing a population member.

## EXEMPT_OWNED_OR_SYSTEM_PRESENTATION

The Pokemon entity spawn surface can include non-wild presentations such as Pokemon sent out by an owner. A blanket cancellation policy would break valid gameplay.

An exempt entity may pass through when the adapter can verify that it belongs to a presentation path outside wild population projection.

Pass-through does not imply wild ecological membership. The entity cannot be inserted into a wild population ledger merely because it is physically present in a habitat.

Where classification cannot be proven from supported metadata, treat the candidate as `UNKNOWN_OR_UNCLASSIFIED` rather than guessing.

## UNCONTROLLED_NATURAL

A natural Pokemon entity appearing inside an Ouros-managed ecological scope without an admission token has no authoritative source.

Preferred action when supported by the current adapter version: cancel at the cancellable spawn event.

Required semantic result:

- `presentation_admitted = false`
- `ecology_write_authorized = false`
- `population_delta = 0`
- `persistent_actor_created = false`
- `autoptu_eligible = false`

Cancellation is a presentation-control action only. It cannot be recorded as death, capture, emigration or failure of the population to exist.

## UNKNOWN_OR_UNCLASSIFIED

Unknown entity provenance must never be upgraded to a persistent wild actor automatically.

If cancellation is safe for the current integration path, cancel. Otherwise preserve the Pass 249 quarantine rule until a loader/version-specific isolation mechanism is verified.

This branch exists because `POKEMON_ENTITY_SPAWN` is entity-wide; it is not documented as a natural-spawn-only stream.

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

- one token admits at most one Pokemon entity;
- token creation does not create population;
- token consumption does not create population;
- expired or reused token fails admission;
- entity UUID is written only after successful admission;
- restart invalidates unresolved runtime tokens unless a future persistence contract explicitly says otherwise.

## Ordering contract

For Ouros-managed direct projection:

```text
projection envelope eligible
-> select already-counted source
-> reserve lease
-> issue one-use admission token
-> request Cobblemon entity materialization
-> Pokemon entity spawn callback
-> validate/consume token
-> admit entity
-> correlate Minecraft UUID
```

Forbidden order:

```text
Cobblemon entity appears
-> search for something in the population that resembles it
-> create or reserve source retroactively
```

That reverse lookup would allow presentation to author ecology.

## Spawn Rules relationship

Spawn Rules are an early filtering layer. They may reduce natural spawn generation inside managed habitats or for managed species.

They must not encode hidden persistent counts, lease IDs or individual identities.

A Spawn Rule passing a candidate does not authorize direct projection. Gate B remains authoritative for admission.

## Indirect evidence

Suppressing a direct entity must not suppress all evidence of ecological presence. Pass 249 `INDIRECT_SIGN` remains available independently when the projection policy chooses it.

The adapter must not convert a cancelled uncontrolled entity into a new evidence root. Evidence must originate from an Ouros-approved sign-generation event or a valid admitted actor.

## AutoPTU boundary

Spawn admission never opens AutoPTU.

Only a valid admitted direct actor can later be considered by the Pass 242 encounter-intent evaluator.

An uncontrolled, cancelled or quarantined entity cannot enter a combatant manifest.

## Executable invariants

- managed direct admission requires a prior active lease;
- managed direct admission requires a live unused token;
- one token admits no more than one entity;
- UUID correlation occurs after admission, never before;
- uncontrolled natural entities cannot mutate population state;
- owned/system pass-through cannot become wild population membership;
- a blanket `cancel every PokemonEntity` policy is invalid;
- cancellation cannot become mortality/emigration/capture truth;
- spawn-rule pass does not substitute for lease/token admission;
- cancelled uncontrolled entities cannot open AutoPTU;
- restart clears unresolved runtime tokens without deleting persistent population state.

## Capability dependencies

Reduced ecology projection path:

- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING until implemented against a pinned Cobblemon version;
- all AutoPTU tactical capability families: NOT REQUIRED.

Rich pursuit/interception after a valid admitted actor:

- targeting/footprints/range/LoS when tactical range/visibility matters;
- base movement legality;
- complete movement for interception/forced movement interactions;
- core calculations when PTU arithmetic is used;
- action economy/initiative;
- full turn/round lifecycle;
- damage/status only when those outcomes are authored;
- terrain/weather/hazards/zones/reactions only when used;
- exact Moves, Abilities, Items and Trainer Features used;
- AI legal-action infrastructure;
- AI tactical policy for autonomous tactical behavior;
- Minecraft/Cobblemon/Craftics adapter/playback end-to-end.

## Version risk

The runtime implementation must pin the Cobblemon version/API surface it compiles against. Event names, spawn causes, fields and cancellation behavior must be regression-tested on upgrade.

Public evidence proves useful primitives exist in current Cobblemon source. It does not prove every third-party spawn path or future release traverses the same path.
