# Global NPC AI Readiness Snapshot — Pass 390

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 390 integrates the executable `PortableFindResourceBindingLedger` from Pass 389 into persistent-world evidence recovery.

`OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2` now preserves:

- site revision/observation/interpretation evidence;
- direct-observation private-knowledge bridge;
- private-inference bridge;
- portable-find → stable-world-resource binding;
- digest binding to external private knowledge;
- digest binding to the external stable resource-identity catalog.

Mutable `WorldResource` holder/location/state remains outside this checkpoint's authority.

New/updated implementation:
- updated `tools/persistent_world_evidence_checkpoint.py`;
- added `tests/test_global_npc_persistent_world_evidence_checkpoint_v2.py`;
- added `design/persistent-world-evidence-checkpoint-portable-find-v2-pass-390.md`.

Research/content:
- `research/2026-09-09-portable-find-checkpoint-recovery-scan-390.md`;
- `proposals/2026-09-09-the-catalog-that-survived-the-evacuation-pass-390.md`.

No canon file or engine repository was changed.

## Recovery behavior

V2 stores the complete portable-find binding snapshot and a SHA-256 of sorted declared `resource_id` identities.

The identity digest validates that the same external physical-resource identities are available at recovery time without freezing mutable resource fields.

A later holder/location/state change therefore remains legal when the stable `resource_id` is unchanged.

A different resource identity set fails closed.

Re-signed binding tampering still fails owner-level provenance validation.

Legacy `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1` remains readable and restores with an empty portable-find binding ledger rather than inferring old bindings from later state.

## Public research contribution

Collections Trust renumbering guidance reinforces that a persistent object number links the physical object to its associated information while storage and other descriptive fields remain separate.

NPS archaeological workflow material separates provenience, accession/catalog labeling, collections registration, later analysis and storage.

Collections Trust object-entry/inventory guidance further separates responsibility/custody, identity, current location and ownership/source.

Pokémon Altair / Sirius public descriptions provide a separate narrative pattern: familiar places and institutions can remain continuous after regional disruption even when geography, facilities and ecological conditions change. Ouros uses only this transformed continuity-through-disruption structure.

## New narrative candidate

`The Catalog That Survived the Evacuation` is PROPOSED / NON-CANON.

A portable find is documented and bound to a stable resource identity before an emergency relocation. Later records disagree about where the object should be because they describe different moments. The reduced investigation reconstructs identity and custody without tactical combat. The rich version can stage evacuation/recovery under pressure while retaining a non-KO objective.

## Read-only engine evidence

AutoPTU-Java inspected head: `36e6d7e34791cc7e950bdff31f80bb8a1abec1dd`, merge #420.

That merge wires the exact Impostor trigger through authoritative round-start execution, including effective-Ability resolution, nearest eligible opponent selection, battle-owned Python-compatible RNG, transformation-state mutation, once-per-round guards and a semantic Ability event. It strengthens evidence for this exact Ability/lifecycle seam only.

It does not verify the complete Abilities family or the entire turn/round lifecycle.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest change remains presentation-only viewport-coordinate synchronization.

Neither engine was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only.

Full turn/round lifecycle: PARTIAL. AutoPTU-Java #420 strengthens one authoritative round-start Ability path but does not complete the category.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Impostor #420 is representative evidence only for its tested seam.

Items: individually gated. A persistent archaeological resource is not automatically a PTU battle Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for protect-object, retrieve-object, evacuation-first, escort, rescue-first, objective-aware withdrawal and disengage-after-objective until exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, site/evidence projection, environmental objective state and authoritative non-KO completion playback.

## Reduced playable version

The Pass 390 proposal can run with semantic time, site evidence, private knowledge, V2 persistent-world evidence recovery, declared stable resource identities, existing custody/resource state, archive access, communication and world travel.

It needs no AutoPTU handoff.

## Rich version dependency gates

Ordinary placement can use verified targeting/base-movement scopes. Forced carrier movement, pull/push, knockback, interception and rescue repositioning require complete movement. Timed evacuation stages or delayed collapse require the full lifecycle. Damage-linked persistent objective effects require the stateful damage pipeline. Lasting conditions require status lifecycle. Fire/flood/debris/smoke/unstable terrain/reaction hazards require exact terrain/weather/hazards/zones/reactions support. Moves, Abilities, Items and Trainer Features remain individually gated.

The rich version remains blocked on objective-aware AI policy and authoritative adapter playback for non-KO success.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a router toward Researcher, Chronicler, Librarian, Paleontologist, Topographer, Skills/Edges/Features, Items/Gear, campaign structure and encounter construction. It is not a mechanics grant.

Pass 390 adds no excavation Skill checks, conservation bonuses, ownership rules, carrying mechanics, battle Item effects or Trainer Feature interrupts.

## Next implementation seams

The next recovery step should not add more evidence state to V2 casually.

Highest-value candidates are:

- an outer recovery manifest that binds global-NPC causal state and persistent-world evidence by semantic time/digest;
- a real resource-catalog recovery owner, after which the outer manifest can bind resource identity and resource/custody state coherently;
- explicit recovery reconciliation for in-flight AutoPTU sessions, without giving the world-agent checkpoint tactical authority.

## Canon unresolved

Still open:

- institution/location for any physical collection;
- emergency/disaster history;
- extraction and relocation authority;
- legal ownership versus custody;
- catalog/alias correction policy;
- exact PTU/Caelo Skills, Edges, Features or Items relevant to field documentation, conservation or authentication.

No answer is promoted by Pass 390.
