# Portable Find Context/Custody Bridge — Pass 388

Status: DESIGN / PROPOSED CONTRACT. Not canon.

## Intent

Connect `ObservationKind.PORTABLE_FIND` to the existing world-resource and custody systems without creating a duplicate archaeology inventory.

This contract preserves three different authorities:

- `SiteEvidenceLedger` owns discovery context and historical observation.
- `WorldResource` owns current resource state, current location and current holder.
- `ResourceHandoffLedger` owns authorized custody-transfer history.

A future ownership/title system, if approved, must remain separate from custody.

## Required invariant

`DISCOVERY_CONTEXT != CURRENT_RESOURCE_STATE != CUSTODY_HISTORY`

A find moving after discovery must never rewrite its original site observation.

## Bridge record

Proposed record: `PortableFindResourceBinding`.

Minimum fields:
- `binding_id`
- `observation_id`
- `resource_id`
- `bound_at_semantic_minute`
- `bound_by_actor_id`
- `authority_ref`

Validation requirements:
- the observation exists;
- its kind is exactly `PORTABLE_FIND`;
- the resource exists;
- binding time is not earlier than observation time;
- one observation cannot bind to two resources;
- one resource cannot claim two discovery observations unless a later explicit assemblage abstraction is designed;
- binding does not move the resource;
- binding does not change holder, location, reservation, state or quantity;
- binding does not authorize a handoff;
- binding does not prove legal ownership.

## Recovery sequence

A portable-find recovery should be represented by explicit stages.

1. Actor observes the object in a site revision.
2. `SiteEvidenceLedger` records the `PORTABLE_FIND` observation.
3. The observation may materialize into that observer's private knowledge through the existing observation bridge.
4. A stable `WorldResource` identity is created or admitted by the world-resource owner.
5. `PortableFindResourceBinding` links the resource identity to the historical observation.
6. If the object is physically removed or passed to another actor, the ordinary resource/custody owners record that change.
7. If removal changes the physical site, a new site revision records the site change separately.
8. Any later interpretation remains based on observations and private evidence, not on current possession alone.

## What the bridge must not infer

A valid binding cannot infer:
- that the observer picked up the find;
- that the holder observed the find in situ;
- that current holder owns the find;
- that a repository accepted the find;
- that removal was lawful or authorized;
- that the object is authentic;
- that the object's interpretation is correct;
- that a PTU Item effect exists;
- that an objective succeeded.

## Handoff integration

When custody changes, use `ResourceHandoffAuthorization` and `ResourceCustodyTransfer` unchanged.

The bridge only supplies the stable `resource_id` that lets custody history point back to the discovery observation.

This preserves:

`CUSTODY_TRANSFER != OWNERSHIP_TRANSFER`

`CUSTODY_TRANSFER != KNOWLEDGE_TRANSFER`

`CUSTODY_TRANSFER != SITE_REVISION`

A receiver can physically possess the object and still lack its discovery context unless that information is separately communicated or accessed.

## Loss and mismatch as gameplay

A later mismatch between resource state and context record is valid world state, not automatic corruption.

Examples:
- the site record exists but the resource is missing;
- the resource is held by a different actor than expected;
- the item reaches a repository but its context report is delayed;
- a handoff condition record conflicts with a later inspection;
- an actor possesses the object but received an incomplete provenance report.

Each mismatch can become an investigation seed without deciding theft, fraud, negligence or error in advance.

## Checkpoint ownership

Do not append portable-find custody directly into `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1`.

The evidence checkpoint should preserve the binding itself because it is the cross-system identity relation, but `WorldResource` and `ResourceHandoffLedger` remain owned by their existing resource checkpoint chain.

A later outer recovery manifest may bind by digest:
- global-NPC checkpoint state;
- persistent-world-evidence checkpoint state;
- resource/custody checkpoint state.

It should validate that every bound `resource_id` exists in the selected resource recovery state without merging those owners.

## Reduced encounter contract

A complete reduced scene requires only:
- semantic time;
- site revision and observation;
- direct-observer knowledge materialization;
- world resource identity;
- portable-find binding;
- ordinary custody handoff if removal occurs;
- communication/reporting if another actor must understand provenance.

No AutoPTU handoff is required.

## Rich encounter dependency matrix

A tactical recovery variant must classify dependencies exactly.

Targeting/footprints/range/LoS: required for tactical interaction geometry only.

Base movement legality: required for ordinary tactical movement.

Complete movement: PARTIAL dependency for drag/rescue, forced movement, push/pull, knockback or interception.

Core calculations: VERIFIED only for audited calculations actually used.

Action economy/initiative: VERIFIED only for audited primitives used by the encounter.

Full turn/round lifecycle: PARTIAL dependency for multi-round timed recovery, delayed collapse or phase changes.

Full stateful damage pipeline: PARTIAL dependency if damage changes actors or objectives over time.

Status lifecycle: PARTIAL dependency if persistent PTU statuses matter.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING for unstable floors, flooding, debris, dust/visibility, reaction hazards or delayed zones.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated; a `WorldResource` find must not be treated as a PTU battle Item merely because it is portable.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: usable only within verified legal-action scopes.

AI tactical policy: BLOCKING for protect-find, retrieve-object, escort, rescue-first, objective-aware withdrawal and disengage-after-objective behavior unless directly verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for stable find identity, pickup/handoff acknowledgement, site-state revision and non-KO objective playback.

## Canon boundary

This design introduces no artifact, relic, institution, ownership law, excavation authority, species, location or historical interpretation into canon.
