# Global NPC AI readiness snapshot — Pass 387

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative baseline inspected before writing: `6da348ecbdb77b4980ed6495f0e09dde2bea7bc7` (Pass 386).

Read-only AutoPTU-Java head inspected: `01a7787048ba92068f8c1340d80c9e9cb89c371d` (merge #419, seeded Impostor random Ability choice plus subsequent RNG-stream parity against pinned Python behavior).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Repository and canon inspection

The recursive repository tree was inspected before writing. Current focus, canon governance, the Pass 383–386 archaeology/evidence chain, global-NPC world checkpoint family, private KnowledgeLedger persistence, global-NPC CI and Kairos/PTU source routing were reviewed. Existing research was searched before source selection. Harris Matrix and Pokémon Clockwork had no prior repository hits and were used only for transformed structural lessons.

No file under `canon/` changes in this pass.

## Executable seam closed

Pass 387 adds `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V1`.

The checkpoint owns the three site-evidence snapshots introduced in Passes 384–386 and binds them to the exact external `KnowledgeLedgerStore` state via deterministic SHA-256. It does not copy private NPC claims into a second authority.

Restore validates the checkpoint digest, the private-store digest, world-time legality and all existing cross-owner provenance contracts. A caller cannot make tampered world evidence valid merely by recomputing the outer digest.

This resolves the ownership question left by Pass 386 without appending archaeology-specific state to global-NPC action checkpoint V19.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; new narrative objective actions remain separately gated.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Java merge #419 proves seeded Impostor random Ability selection and following RNG value for its pinned scenario only.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions; documentation/stabilization/protection objectives need explicit admission.
15. AI tactical policy — BLOCKING for documentation-first, protect-evidence, rescue-first, escort, search, stabilization-first, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent evidence identity, physical site-revision projection, non-KO objective state, evidence interaction and authoritative end-to-end playback.

No family is promoted from one representative mechanic.

## Reduced and rich narrative use

`The Wall That Was Recorded Twice` can run in reduced form with semantic time, persistent site revisions, direct-observation/private-inference bridges, communication and the new recovery checkpoint. It requires no AutoPTU scene.

Its rich form may add unstable access, documentation windows, escort, rescue, equipment protection or objective-aware withdrawal. Those additions remain gated by the exact capability families above.

## PTU/Caelo boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a source router. It points to Researcher, Paleontologist, Topographer, Skills/Edges/Features, movement/terrain, campaign structure and encounter creation in the supplied source material, but provides no automatic mechanical grant.

Pass 387 adds no Skill DC, Feature bonus, Item action, species placement, excavation mechanic or tactical permission.

## Research provenance

New public anchors are Harris Matrix documentation, CIfA stratigraphic relationship guidance and Pokémon Clockwork's public past/present exploration feature. Ouros transforms only the high-level structures: persistent sequences, cross-record validation and geographically stable places observed under different temporal states. No protected prose, characters, regions, plots, maps, quests or distinct mechanics are imported.

## Next seams

An outer recovery manifest can later bind global-NPC V19 and persistent-world-evidence V1 by digest so crash recovery selects a coherent pair without merging ownership.

Portable finds should still connect to existing custody/resource owners instead of gaining a parallel archaeology inventory.

If site evidence expands beyond archaeology, rename or generalize content types only when a second concrete use case proves the abstraction; do not generalize preemptively.
