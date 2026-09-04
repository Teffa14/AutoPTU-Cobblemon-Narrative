# Coupled ecology ledger isolation contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 246
Canon effect: NONE

## Purpose

Define how one ecological event may touch several populations, individuals and resources without cross-ledger leakage.

## Scoped authority

Every accepted ecology-domain event names the smallest state scope it may mutate:

- resource event -> one named resource ledger;
- individual event -> one persistent actor record;
- population-pressure event -> one named population;
- demographic event -> one named population total plus any explicitly paired source/destination population;
- battle semantic result -> only the actor/battle identities explicitly returned by AutoPTU.

An event may never infer additional writes from species similarity, co-presence, Minecraft UUID proximity, or a shared encounter.

## Resource accounting

Resource observation and resource consumption are separate.

`RESOURCE_USE_OBSERVED` records evidence only.

`RESOURCE_CONSUMPTION_CONFIRMED` requires a stable transaction ID, resource ID, consumer population/actor scope, positive quantity, enough available resource and idempotency protection.

Confirmed consumption decrements the resource ledger. It does not change population abundance.

## Cross-population effects

One cause may legitimately create several pressure writes, but every write remains explicit.

Example:

resource patch becomes scarce
-> Fletchling population `resource_pressure +0.15`
-> Squawkabilly population `resource_pressure +0.12`
-> persistent Fletchling `avoidance_pressure +0.08`

Those are three separate accepted events. None is inferred from the other two.

## Atomicity boundary

A transaction that cannot be fully validated must produce no partial resource mutation.

Future coupled demographic/resource operations must declare their atomic group explicitly. Pass 246 does not authorize such combined operations.

## Canon boundary

The Pass 246 fixture contains a proposed-only Squawkabilly population and proposed-only forage patch. Replay proves software behavior only.

`FIXTURE_REPLAY_SUCCESS != CANON_APPROVAL`

The existing Fletchling population remains the sole canon wild population used by the slice.

## Full encounter version

If both species are later approved locally, the full premise is a compressed forage window at a bounded patch. Individuals approach, yield, displace, warn, reposition, possibly defend access, and may leave for alternative patches.

Potential structured escalation depends on targeting/footprints/range/LoS; base movement legality; complete movement including interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; the damage and status families if attacks occur; terrain/weather/hazards/zones/reactions if the patch/window has tactical effects; exact Move, Ability, Item and Trainer Feature behavior when selected; AI legal-action infrastructure; AI tactical policy for access/withdraw/redirect goals; and Minecraft/Cobblemon/Craftics adapter/playback.

## Reduced version

Run resource availability, consumption, observation and pressure entirely as Ouros world state. Visible Pokémon may idle, approach, withdraw or be projected separately. No tactical contest is simulated.

This reduced version needs no incomplete PTU capability family. Production still depends on adapter/persistence support to capture accepted events and rematerialize actors faithfully.

## Acceptance

Pass 246 integration succeeds when CI proves deterministic multi-population/resource replay; observation does not consume resources; confirmed consumption decrements the resource exactly once; overdraw fails without partial mutation; population totals remain unchanged without demographic events; Fletchling individual history does not leak into Squawkabilly population state; scoped pressure can change independently; and restart preserves accepted ecology state.
