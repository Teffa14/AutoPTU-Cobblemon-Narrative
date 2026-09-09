# Global NPC AI readiness snapshot — Pass 385

Status: EVIDENCE SNAPSHOT
Date: 2026-09-09
Canon effect: NONE

Narrative baseline inspected before writing: `e4b56136acc9fae9986caa13dd2dd2b2cd4550cd` (Pass 384).

Read-only AutoPTU-Java head inspected: `01a7787048ba92068f8c1340d80c9e9cb89c371d` (merge #419, seeded Impostor random ability-choice and RNG-stream parity against Python).

Read-only AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (presentation-only viewport synchronization).

No engine repository was modified.

## Repository and canon inspection

The recursive repository tree, `CURRENT_FOCUS.md`, `canon/README.md`, Pass 383/384 archaeology files, the site-evidence owner and tests, private knowledge owner, global-NPC CI and Kairos/PTU source routing were inspected before writing.

Pass 384 left one explicit seam: world observations must reach private NPC knowledge only through provenance-preserving materialization rather than direct shared visibility. Pass 385 closes the direct-observer subset with `OUROS_SITE_OBSERVATION_KNOWLEDGE_V1`.

No file under `canon/` changes in this pass.

## New executable bridge

`tools/global_npc_site_observation_knowledge.py` now materializes one durable site observation into the existing private `KnowledgeLedger` of the actor named as its observer.

The bridge derives deterministic IDs, preserves observation content, semantic minute, observer identity and provenance root, and records the private claim as `DIRECT_OBSERVATION`.

The bridge validates against both owners on restore. A materialization to another actor, a missing private claim, changed claim content/provenance, a missing source observation or evidence from after checkpoint time fails closed.

A later physical site revision does not rewrite the observer's earlier private claim.

Interpretations, institutional peers and later visitors are deliberately excluded from automatic materialization.

## Capability classification

1. targeting/footprints/range/LoS — VERIFIED within audited ordinary contracts.
2. base movement legality — VERIFIED within audited ordinary contracts.
3. complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
4. core calculations — VERIFIED within audited deterministic contracts.
5. action economy/initiative — VERIFIED for audited primitives; dedicated narrative observe/document actions still require explicit admission.
6. full turn/round lifecycle — PARTIAL.
7. full stateful damage pipeline — PARTIAL.
8. status lifecycle — PARTIAL.
9. terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanism.
10. move-specific behavior — INDIVIDUALLY GATED.
11. abilities — INDIVIDUALLY GATED. Java merge #419 proves seeded Impostor random ability-choice and subsequent RNG-stream parity for the pinned scenario only. It does not prove the whole Ability family.
12. items — INDIVIDUALLY GATED.
13. Trainer Features/perks — INDIVIDUALLY GATED.
14. AI legal-action infrastructure — VERIFIED for ordinary audited actions.
15. AI tactical policy — BLOCKING for documentation-first, protect-evidence, rescue-first, escort, search, stabilization-first, objective-aware withdrawal and disengage-after-objective.
16. Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for persistent evidence identity, site-revision projection, observation acknowledgement, non-KO objective state and authoritative end-to-end playback.

No category is promoted globally from one representative mechanic.

## Reduced versus rich narrative implementation

The Pass 385 case `The Mark That Vanished Before the Second Team Arrived` can run in reduced form without AutoPTU. It requires persistent site revisions/observations, semantic time, the new direct-observer knowledge bridge, world travel and explicit communication/archive access for later information spread.

The rich form can add visibility pressure, unstable access, rescue, escort, documentation or withdrawal goals. Forced movement depends on complete movement. Timed environmental phases depend on full lifecycle plus exact terrain/hazard support. Dedicated observation/documentation tactical behavior remains blocked by legal-action/policy seams until explicitly admitted.

## PTU/Caelo authority boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes utility classes including Researcher, Paleontologist and Topographer, Skills/Edges/Features, movement/terrain and encounter construction to supplied Kairos/PTU material. It remains a router rather than a rules grant.

Pass 385 therefore introduces no new skill check, Feature bonus, excavation procedure, item rule, species distribution or tactical permission.

## Research provenance

New primary anchors in this pass are CIDOC CRM/CRMsci/CRMba, a public PTU campaign log on Giant in the Playground, and Pokémon Frozen Spirit. Their reusable structures were transformed into Ouros-specific provenance and environmental-storytelling patterns. No protected characters, dialogue, locations, plots, artwork or distinctive mechanics were imported.

## Next seams

Interpretation-to-private-inference materialization should be a separate owner that preserves supporting observation IDs rather than pretending inference is direct observation.

The site-evidence ledger and direct-observer bridge still need an explicit checkpoint ownership decision. They may fit better under a broader persistent-world checkpoint than under global-NPC V19.

Portable-find custody should continue through existing resource/evidence-custody owners rather than creating a parallel inventory path.

Minecraft/Cobblemon projection needs stable evidence IDs and revision acknowledgements before physical block-state changes can be treated as durable world evidence.
