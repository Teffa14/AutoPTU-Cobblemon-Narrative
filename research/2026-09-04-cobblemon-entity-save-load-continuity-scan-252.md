# Cobblemon entity save/load continuity scan — Pass 252

Status: RESEARCH / PROVENANCE
Canon effect: NONE
Date: 2026-09-04

## Question

How can an Ouros-managed wild Pokemon survive Minecraft chunk unload or server restart as the same persistent actor without treating a restored `PokemonEntity` as a new ecological spawn?

## Existing project boundary

Pass 239 already separates persistent Ouros identity from temporary Minecraft entity UUIDs. Pass 250 introduced admission tokens for direct BestSpawner projection. Pass 251 source-verified that `POKEMON_ENTITY_SPAWN` is a BestSpawner seam, not a universal PokemonEntity lifecycle hook. Restore/load therefore needs its own reconciliation path.

## New upstream evidence

Cobblemon tag `1.7.3` exists at upstream commit `e6fda613` (2026-01-31). The project still does not claim that this is the final Ouros runtime dependency pin.

In the 1.7.3 `PokemonEntity` source:

- `PokemonEntity.saveWithoutId(...)` posts `CobblemonEvents.POKEMON_ENTITY_SAVE` with the entity and the mutable NBT compound before the save returns through the superclass.
- `PokemonEntity.load(...)` posts `CobblemonEvents.POKEMON_ENTITY_LOAD` with the entity and NBT compound after Cobblemon restores its own entity state.
- `POKEMON_ENTITY_LOAD` is cancellable; cancellation calls `discard()` on the entity.
- `PokemonEntity.spawnCause` explicitly documents that it is wiped by chunk unload. It is therefore unsuitable as durable Ouros identity or restore authority.

Sources:

- Cobblemon 1.7.3 tag: https://gitlab.com/cable-mc/cobblemon/-/tags/1.7.3
- Cobblemon 1.7.3 PokemonEntity source: https://gitlab.com/cable-mc/cobblemon/-/raw/1.7.3/common/src/main/kotlin/com/cobblemon/mod/common/entity/pokemon/PokemonEntity.kt
- Cobblemon event registry: https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/api/events/CobblemonEvents.kt

These are implementation evidence, not Ouros canon.

## Ecological identity pattern

The USGS Bird Banding Laboratory treats repeated encounters of a marked bird as observations of the same individual. Individual identification supports reconstruction of movement, behaviour, territory fidelity, survival and repeated encounters without claiming the animal is a new population member each time it is seen.

Sources:

- https://www.usgs.gov/labs/bird-banding-laboratory
- https://www.usgs.gov/labs/bird-banding-laboratory/science/why-do-we-band-birds
- https://www.usgs.gov/labs/bird-banding-laboratory/science/banding-and-encounter-data-requests

Reusable Ouros lesson: a world presentation is an encounter with an existing actor. Reappearance after absence can extend history while abundance remains unchanged.

## PTU / campaign pattern

PTU's Survival skill explicitly supports scouting and tracking from signs in an environment. A public PTU campaign log also demonstrates a useful structure where recurring wild-Pokemon behaviour acts as evidence for a larger environmental problem rather than every sighting being an isolated random battle.

Sources:

- PTU 1.05 Survival material: https://anyflip.com/deia/psdg/basic
- Public campaign log #22: https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t

Reusable Ouros lesson: continuity of an individual can matter narratively through tracks, remembered behaviour and later resighting even when the player cannot see an internal persistent ID.

## Proposed architecture

A saved Minecraft entity may carry a minimal namespaced Ouros projection receipt. The receipt is correlation evidence only. Suggested fields are receipt schema version, persistent actor ID, lease ID, managed scope ID, projection epoch and a non-secret integrity/correlation value if the runtime design requires it.

On load, Ouros must resolve that receipt against its authoritative ledger before the entity may regain managed-wild presentation authority.

Valid receipt plus matching live/suspended lease -> reconcile presentation to the existing actor.

Missing receipt -> no wild-authority inference. For a physical PokemonEntity inside a managed scope, quarantine/discard unless another explicit lifecycle contract owns it.

Stale or conflicting receipt -> cancel/discard presentation and schedule ledger reconciliation. Never mint a new actor to make the entity fit.

Two loaded entities claiming one actor/lease -> fail closed for the duplicate. One persistent actor may have at most one authoritative direct projection.

## Explicit non-claims

This pass does not prove that arbitrary Ouros NBT keys survive every loader, server implementation or third-party serialization path in the eventual runtime.

This pass does not claim that chunk unload itself is observable through a Cobblemon-specific event.

This pass does not make Minecraft UUID durable identity.

This pass does not promote a research tag, band, marking or other visible identifier to Marea canon.

This pass does not make restored physical presence an AutoPTU combatant. AutoPTU eligibility still requires the Pass 242 handoff and frozen combatant manifest.

## Narrative opportunity

PROPOSED: repeated sightings can make individual wild Pokemon into emergent local characters. The player may recognize a habitual route, warning posture, preferred perch or other evidence. Recognition should use observation history and confidence rather than exposing internal actor IDs. A physical band/tag is only appropriate if separately approved in canon.
