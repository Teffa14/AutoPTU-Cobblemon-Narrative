# Global NPC AI Readiness Snapshot — Pass 393

Status: READINESS EVIDENCE. Not canon.
Date: 2026-09-09

## Slice completed

Pass 393 upgrades persistent-world generation selection to `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2`.

Implementation:
- updated `tools/persistent_world_recovery_manifest.py`;
- updated `tests/test_persistent_world_recovery_manifest.py`;
- `design/persistent-world-recovery-manifest-v2-contract-pass-393.md`.

Research/content:
- `research/2026-09-09-coherent-resource-recovery-dungeon-investigation-scan-393.md`;
- `proposals/2026-09-09-the-room-that-opened-after-the-team-left-pass-393.md`.

No canon file or engine repository was changed.

## Recovery boundary

V2 binds one exact generation of:

- `OUROS_NPC_WORLD_CHECKPOINT_V19`;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2`;
- `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1`.

All three must have valid owner digests and the same semantic minute. The manifest stores their exact SHA-256 identities and signs its own payload.

The manifest remains a generation selector. It does not copy domain state or replace any owner's restore-time validation.

Legacy V1 manifests remain readable as two-owner manifests and do not fabricate a missing resource checkpoint.

## Public research contribution

Apache Flink's public operations documentation reinforces the technical distinction between independent state and a consistent checkpoint used for recovery.

A public PTU campaign log contributed a dungeon/exploration pattern based on functionally different rooms, environmental cues, puzzle access, blocked routes and optional combat rather than a uniform battle sequence.

Pokémon Empyrean was new to the repository by name. Its public material contributed the high-level pattern of personal investigation nested inside ordinary regional progression and research-site access that changes as story/knowledge state advances.

No protected plot, characters, layouts, dialogue or custom mechanics were imported.

## New narrative candidate

`The Room That Opened After the Team Left` is PROPOSED / NON-CANON.

Two survey teams see different versions of the same damaged research outpost. The first leaves while one corridor is inaccessible and a needed field resource is reassigned. The second arrives after the physical site changes and finds evidence that appears to contradict the first survey.

The reduced version is an evidence, knowledge, resource, travel and recovery investigation requiring no AutoPTU battle.

The rich version can stage evidence acquisition and evacuation under unstable access conditions while keeping safe documentation and exit as the objective rather than a KO sweep.

## Read-only engine evidence

AutoPTU-Java inspected head remains `36e6d7e34791cc7e950bdff31f80bb8a1abec1dd`, merge #420.

That head strengthens the tested Impostor path through authoritative round-start execution with effective-Ability resolution, nearest eligible opponent selection, battle-owned compatible RNG, transformation mutation, once-per-round guard and Ability event. It does not verify the complete Abilities family or complete lifecycle.

AutoPTU Python inspected head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is presentation-only viewport-coordinate synchronization.

Neither engine was modified.

## Permanent capability classification

Targeting/footprints/range/LoS: VERIFIED within audited scopes only.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only. New investigation/objective interactions are not implied.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Impostor #420 remains evidence for its tested seam only.

Items: individually gated. `WorldResource` remains distinct from a PTU Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for investigation-first, protect-evidence, retrieve-resource, escort-specialist, split-team search, objective-aware withdrawal and disengage-after-objective until exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for persistent evidence/site identity, room-state projection, resource acknowledgement, objective state and authoritative non-KO completion playback.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as an authority router only. Pass 393 introduces no new Skill check, Edge, Trainer Feature, Item effect, puzzle bonus, hazard rule, forced movement effect or tactical interrupt.

Any later mechanically defined investigation action or environmental hazard must be checked against the actual supplied PTU/Caelo/Kairos source material and current AutoPTU implementation.

## Next implementation seams

Highest-value work after this pass:

- run the global regression suite and confirm V2 does not break legacy V1 recovery;
- define cross-owner reconciliation between restored current resource holder/reservation state and historical request/reservation/handoff ledgers without fabricating missing history;
- define in-flight AutoPTU battle/session recovery by stable battle/session identity and authoritative tactical state/result;
- keep Minecraft/Cobblemon acknowledgement downstream of world and battle authority.

## Canon unresolved

Still open:

- research outpost location and institution;
- reason for restricted/deeper access;
- cause of the physical change;
- field-resource identity and assignment authority;
- species present;
- legal access/extraction rules;
- relevant PTU/Caelo Skills, Edges, Features or Items;
- whether the investigation participates in a larger regional arc.

No answer is promoted by Pass 393.
