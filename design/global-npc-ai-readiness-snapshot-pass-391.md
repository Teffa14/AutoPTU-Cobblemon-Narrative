# Global NPC AI Readiness Snapshot — Pass 391

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 391 adds `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1`.

The manifest binds one valid `OUROS_NPC_WORLD_CHECKPOINT_V19` and one valid `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2` by exact SHA-256 and one shared semantic minute.

Implementation:
- `tools/persistent_world_recovery_manifest.py`;
- `tests/test_persistent_world_recovery_manifest.py`;
- `design/persistent-world-recovery-manifest-contract-pass-391.md`.

Research/content:
- `research/2026-09-09-coherent-recovery-and-distributed-expedition-scan-391.md`;
- `proposals/2026-09-09-the-survey-that-survived-the-collapse-pass-391.md`.

No canon file or engine repository was changed.

## Recovery boundary

The manifest owns pair selection only.

It does not duplicate either checkpoint payload and does not replace either owner's restore-time semantic validation.

A pair is buildable only when both candidate owner checkpoints are internally digest-valid, use the current V19/V2 schemas and carry the same semantic minute.

Reconciliation rejects:

- a corrupt manifest;
- a corrupt owner checkpoint;
- a different valid checkpoint generation at the same minute;
- a valid checkpoint from a different semantic minute;
- a legacy/unknown owner schema.

The complete mutable `WorldResource` catalog remains outside the manifest because the repository still lacks a dedicated authoritative recovery owner for that full state.

In-flight AutoPTU session reconciliation also remains outside this slice.

## Public research contribution

Apache Flink provides a useful abstract model for consistent distributed checkpoints: independently stateful operators participate in one coherent checkpoint boundary rather than restoring arbitrary generations together.

An event-sourcing recovery reference reinforces point-in-time reconstruction and the rule that current/later state must not contaminate recovery of an older moment.

A previously unused PTU campaign-log episode demonstrates a contained exploration site combining navigation, optional combat, environmental interaction, blocked access and a puzzle instead of uniform battle-room cadence.

Pokémon Xenoverse was a new fan-game anchor in this repository. Only its high-level structure of linking a personal search to a broader regional mystery was reused.

## New narrative candidate

`The Survey That Survived the Collapse` is PROPOSED / NON-CANON.

A survey site physically changes while different named actors are travelling, observing and reporting. The investigation reconstructs which revision each actor saw and which evidence they actually possessed. The reduced version needs no AutoPTU handoff. The rich version can stage collapse/evacuation pressure around non-KO objectives.

## Read-only engine evidence

AutoPTU-Java inspected head: `36e6d7e34791cc7e950bdff31f80bb8a1abec1dd`, merge #420.

That merge wires the exact Impostor trigger through authoritative round-start execution with effective-Ability resolution, nearest eligible opponent selection, battle-owned Python-compatible RNG, transformation-state mutation, once-per-round guards and a semantic Ability event.

This strengthens only that exact Ability/round-start seam. It does not verify the complete Abilities family or full turn/round lifecycle.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest change remains presentation-only viewport-coordinate synchronization.

Neither engine was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only.

Full turn/round lifecycle: PARTIAL. AutoPTU-Java #420 strengthens one authoritative round-start Ability path only.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Impostor #420 is representative evidence for its tested seam only.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for escort, rescue-first, documentation-first, protect-evidence, route-clearing, objective-aware withdrawal and disengage-after-objective until exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for persistent site/evidence projection, route-state acknowledgement, environmental objectives and authoritative non-KO completion playback.

## Reduced playable version

The new proposal can run with semantic time, site evidence, private knowledge, communication, world travel, V19 global-NPC recovery, V2 persistent-world-evidence recovery and the new manifest.

No tactical battle resolution is required.

## Rich-version dependency gates

Ordinary placement can use verified targeting/base-movement scopes. Forced movement, rescue repositioning, knockback, pull and interception require complete movement. Timed collapse/evacuation phases require full turn/round lifecycle. Persistent damage-linked objective consequences require the stateful damage pipeline. Lasting conditions require status lifecycle. Debris, unstable floors, dust visibility, flood, triggered collapse and reaction hazards require exact terrain/weather/hazards/zones/reactions support.

Moves, Abilities, Items and Trainer Features remain individually gated. Objective-aware tactical AI and authoritative adapter playback remain blocking for the full non-KO encounter.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a router toward campaign structure, encounter creation, recurring rivals, bosses, movement, hazards, terrain/weather and utility classes such as Researcher, Chronicler, Librarian, Paleontologist and Topographer.

Pass 391 adds no excavation check, collapse rule, Skill bonus, Item effect, Trainer Feature interrupt or battle mechanic from that index.

## Next implementation seams

Highest-value next recovery work:

- inspect whether the existing resource subsystem can support an authoritative mutable world-resource catalog checkpoint without duplicating custody ownership;
- if yes, add that owner and only then extend the outer manifest;
- define explicit in-flight AutoPTU reconciliation by session/battle identity and authoritative result;
- keep Minecraft/Cobblemon acknowledgement downstream of narrative and tactical authority.

## Canon unresolved

Still open:

- concrete site and institution;
- physical-change cause;
- lower-layer meaning;
- relevant species;
- access/preservation authority;
- exact PTU/Caelo Skills, Edges, Features and Items;
- whether the incident joins a larger regional story arc.

No answer is promoted by Pass 391.
