# Reschedule delivery atomic recovery scan — Pass 362

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-08

Purpose

Inspect the full Ouros repository inventory and the current Pass 339–361 resource/checkpoint chain before changing persistence. The narrow question is whether a restored reschedule decision can be proven to depend on the same delivered RESCHEDULE_REQUEST that the live Pass 346 runtime required when the decision was originally recorded.

Repository boundary inspected before writing

The recursive repository tree, root guidance, canon governance, current focus, Kairos/PTU source index, world checkpoint code, resource V1–V5 codecs, appointment delivery helpers, Pass 346 reschedule runtime, Passes 347–352 downstream allocation contracts, Pass 359–361 research/proposals/readiness snapshots, current tests and CI path coverage were inspected first. No canon file is modified by this pass.

Existing Ouros facts relevant to this scan

Pass 345 records that an appointment notice was authored and ties it to one communication event. Communications separately owns transport state. Pass 346 permits the responder to decide a proposal only when the source RESCHEDULE_REQUEST has DeliveryStatus.DELIVERED. Pass 361 persists proposal, decision and successor-authorization lineage but does not yet put that lineage inside the same coherent world recovery boundary as the communication queue.

The durability risk is therefore a split-history restore: the resource ledger can claim a decision exists while the recovered information queue says the request is still queued, failed or otherwise not delivered. The live runtime would never have accepted that combination.

New public sources

1. AWS Prescriptive Guidance, Saga patterns.
https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/saga-patterns.html
Accessed 2026-09-08.

Reusable design lesson: a long workflow can span multiple state owners, but correctness depends on explicit continuation/compensation boundaries and durable knowledge of which step actually completed. Ouros does not adopt the Saga pattern wholesale. The transformed lesson is narrower: a later state transition should not be accepted after recovery unless the prerequisite event owned by another subsystem is also present in the recovered history.

2. Kehaloan Isles PTU Living Server public recruitment/discussion.
https://www.reddit.com/r/PokemonTabletop/comments/1dm8936
Accessed 2026-09-08.

Reusable design lesson: a PTU living world can support an overarching story while different groups play at different times and persistent characters continue to matter between sessions. For Ouros, small logistics and schedule consequences can therefore survive session boundaries and become shared-world evidence later. Kehaloan locations, characters, homebrew species and server rules are not imported.

3. Pokémon Fluvio public project description, updated 2026-07-10.
https://www.pokeharbor.com/2026/07/pokemon-fluvio/
Accessed 2026-09-08.

Reusable design lesson: a Pokémon fan adventure can center field research, local wildlife cataloging, community assistance and environmental mysteries alongside the gym circuit. Ouros can transform that structure into research obligations whose instruments, appointments and handoffs matter because they enable ecological observation rather than because every quest ends in combat. No Viridis-region geography, characters or story beats are imported.

4. Internal Kairos/PTU routing evidence.
`sources/kairos/KAIROS_SOURCE_INDEX.md`
Inspected 2026-09-08.

The project-supplied Kairos/PTU index points to campaign/session structure, encounter construction, recurring rivals/villains, boss encounters, movement, status, hazards, terrain/weather, items and living-world downtime. It also explicitly warns that Kairos homebrew is evidence, not automatic Ouros acceptance. This pass adds no PTU rule or Caelo fact.

5. AutoPTU-Java read-only evidence.
Head inspected: `e4e907349993a14c4c652f3dba58ff49db28ff79`, merge of PR #408.
https://github.com/Teffa14/AutoPTU-Java/pull/408
Inspected 2026-09-08.

The current Java evidence remains the audited Intimidate/Mirror Armor reflection slice. It does not change the logistics, interception, cargo or adapter gates used by the companion encounter.

6. AutoPTU Python read-only evidence.
Head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.
https://github.com/Teffa14/AutoPTU/commit/729bae2d424963ff9bb3f4159c9a7ac9152128a7
Inspected 2026-09-08.

The current head is presentation-only and provides no new battle-rule promotion.

Transformed Ouros structures

A reschedule decision should be recoverable only when the same checkpoint also recovers the appointment notice, its actual communication envelope and DELIVERED transport status. Resource history still owns proposal/decision/replacement facts. Communications still owns delivery. The world checkpoint is the place where those owners are cross-validated.

A later successor authorization must never be used as retroactive evidence that the request was delivered. If recovery sees the successor but the source request is queued or failed, the checkpoint is internally inconsistent and should fail closed.

This creates useful narrative states without deception. A requester can remember sending the change. A responder can lack it because delivery never happened. Another participant can already have moved according to the old arrangement. Only a genuinely delivered request can support the recorded responder decision.

Canon boundary

No public source above establishes an Ouros or Caelo world fact. The implementation is persistence architecture for an already existing NON-CANON global-NPC foundation. The companion location, field team and instrument remain proposed until separately promoted.

Encounter dependency note

The reduced encounter requires no AutoPTU battle implementation. The rich field-interception version depends on targeting/footprints/range/LoS, base movement legality, complete movement when interception/forced movement/carrying is used, action economy/initiative, full turn/round lifecycle for tactical deadlines, exact terrain/weather/hazard/reaction families used, AI legal-action infrastructure, AI tactical policy and Minecraft/Cobblemon/Craftics adapter/playback support. Full stateful damage pipeline, status lifecycle, move-specific behavior, abilities, items and Trainer Features/perks are required only if the authored encounter invokes those mechanics; each remains gated individually rather than inferred from representative coverage.
