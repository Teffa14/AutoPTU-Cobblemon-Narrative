# Cobblemon spawn-control seam scan — Pass 250

Status: RESEARCH / PROVENANCE
Canon effect: NONE
Date: 2026-09-04

## Question

Which publicly verified Cobblemon primitives can support the Pass 249 requirement that uncontrolled native Pokemon entities never become Ouros population truth?

## Existing Ouros constraints inspected

This pass preserves the active ecology directive, the source-authority policy, Pass 239 persistent-source leasing, Pass 248 projection envelopes and Pass 249 projection arbitration.

The required authority order remains:

persistent ecology -> projection eligibility -> source reservation -> Minecraft/Cobblemon presentation

Cobblemon entity creation, despawn, animation, vanilla damage or local UUID state cannot author population membership or PTU outcomes.

## New public evidence

### Cobblemon event surface

Current Cobblemon `CobblemonEvents.kt` exposes `ENTITY_SPAWN` as a `CancelableObservable<SpawnEvent<*>>`. `POKEMON_ENTITY_SPAWN` is a filtered view of that event for `PokemonEntity`.

Source:
- Cobblemon source, `common/src/main/kotlin/com/cobblemon/mod/common/api/events/CobblemonEvents.kt`
- https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/api/events/CobblemonEvents.kt

Historical Cobblemon changelog evidence also records a fix making `SpawnEvent` respect `Cancelable#cancel`. This matters because a contract should not assume cancellation semantics merely from a type name.

Source:
- Cobblemon changelog
- https://gitlab.com/cable-mc/cobblemon/-/blob/df8f078d13702ab9a000438910b822ceffbb2248/CHANGELOG.md

### Spawn Rules filter layer

Cobblemon Spawn Rules are data-driven and include a `filter` component capable of blocking or allowing spawns according to a spawn selector and context selector.

Source:
- Cobblemon Wiki, Spawn Rules
- https://wiki.cobblemon.com/index.php/Spawn_Rules

This is useful as an early denial layer for ecology-managed natural spawning. It does not by itself create an Ouros lease or prove persistent identity.

### Spawn pool data remains presentation input

Cobblemon spawn-pool files define species, rarity, levels and environmental conditions for natural spawning. They are useful inputs for habitat compatibility and presentation policy, but in Ouros they cannot be interpreted as population counts.

Source:
- Cobblemon Wiki, Spawn Pool World
- https://wiki.cobblemon.com/index.php/Spawn_Pool_World

### Important event-classification risk

Public sidemod evidence shows that `POKEMON_ENTITY_SPAWN` also fires for Pokemon entities sent into the world by trainers, not only natural wild spawns. Therefore Ouros must never subscribe to this event and cancel every Pokemon entity indiscriminately.

Source:
- Cobblemon Max IVs sidemod documentation
- https://github.com/pell707/Cobblemon_Max_IVs

This is not an authority source for Cobblemon internals, but it is useful integration evidence and agrees with the broad entity-level event design in current Cobblemon source.

## Reusable design lessons

1. Use an early data-driven denial layer for natural spawns inside an Ouros-managed ecological scope when feasible.
2. Use the cancellable entity-spawn event as a runtime backstop, not as the sole population system.
3. Never blanket-cancel every `PokemonEntity`; classify controlled materializations, owned/sent Pokemon and unmanaged natural candidates separately.
4. An Ouros-controlled materialization requires a reservation/token before the entity is admitted.
5. A spawn event with no valid reservation must fail closed for ecological authority. If technical cancellation is unavailable in a future Cobblemon version, quarantine semantics remain required until the adapter can remove or isolate it safely.
6. Event cancellation prevents presentation leakage; it does not itself alter abundance.
7. Spawn-rule eligibility and projection-envelope eligibility are separate concepts. Cobblemon can say an entity could spawn physically while Ouros still says no persistent source is available.

## Narrative payoff

This seam supports ecology without making the world feel empty. Ouros can suppress uncontrolled direct Pokemon actors while still presenting indirect evidence, then intentionally materialize already-counted individuals when the projection envelope and lease system permit it.

The player-facing loop remains:

ecological pressure -> sign or no presentation -> later direct sighting of an already-existing Pokemon -> optional structured interaction

## PTU/Caelo/Kairos cross-check

No PTU rule is changed here. PTU remains relevant only once an interaction requires structured adjudication. Caelo and Kairos remain living-world references; neither supplies authority for the Cobblemon adapter.

## Confidence

VERIFIED PUBLIC PRIMITIVE:
- `ENTITY_SPAWN` is cancellable in current Cobblemon source.
- `POKEMON_ENTITY_SPAWN` derives from it for Pokemon entities.
- Spawn Rules support filter components.

PARTIAL / ADAPTER-SPECIFIC:
- exact identification of every natural-spawn cause versus player-owned/sent-out/entity restoration path;
- exact tagging mechanism for an Ouros reservation on the entity/Pokemon object;
- ordering guarantees between the Ouros materialization request, event callback and UUID correlation;
- loader-specific integration details.

UNVERIFIED:
- that one hook alone covers every possible third-party entity creation path;
- that cancellation semantics and event names remain identical across every future Cobblemon release.

## Next implementation target

Create an adapter-facing admission fixture with three paths:

- managed direct projection with pre-existing Ouros lease -> admit and correlate;
- uncontrolled natural Pokemon spawn inside managed scope -> cancel/backstop with zero ecology write;
- player-owned or otherwise explicitly exempt presentation -> pass through without becoming wild population truth.
