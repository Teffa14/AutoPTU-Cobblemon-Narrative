# Global NPC AI readiness snapshot — Pass 429

Status: ACTIVE IMPLEMENTATION SNAPSHOT

Pass 429 starts from Narrative `main` `e50c04ed3855bab9239cf0d1f947e89bfd7930ed`, after Pass 428.

The recursive repository tree was inventoried before writing. Root files and the canon, design, implementation, proposals, research, sources, tests and tools surfaces were checked, with targeted reads of the current focus, coherent world checkpoint, world-action intent ledger, assistance commitment owner, agenda profile and relevant checkpoint regression coverage. No canon file is changed.

## Concrete change

`tools/global_npc_assistance_world_checkpoint.py` adds `OUROS_ASSISTANCE_WORLD_CHECKPOINT_V1`.

The wrapper binds the existing global world checkpoint, world-action intent ledger and assistance commitment ledger into one digested semantic generation. It validates action time, agent identity, request/response binding, commitment provenance and exact responder-agenda membership.

Restore reconstructs the assistance commitment into the responder agenda from the durable commitment ledger and rejects conflicting caller-supplied schedule state. It does not reconstruct authority from messages.

`tests/test_global_npc_assistance_world_checkpoint.py` covers coherent round-trip, missing agenda state, future action rejection, digest mutation, generation-time mismatch and authored-region/tactical-special-case exclusion.

## Research added

`research/2026-09-11-persistent-promises-evidence-revision-scan-429.md` adds new transformed material from Heaven's Vault design coverage and a public PTU campaign listing. The reusable pattern is continuity across absence: prior evidence and prior promises remain historical facts while later information can change interpretation or plans.

`proposals/2026-09-11-the-promise-survives-the-restart-429.md` is PROPOSED / NON-CANON. It describes an accepted assistance window surviving player departure, sleep, unload or restart without implying that the promised work already occurred.

## Live engine evidence

AutoPTU-Java read-only head checked for this pass: `0415392b3391aed7329a062da159c882e0e2d43e`, merged through PR #444. Current evidence strengthens replacement-initiative caller policy and switch handoff tracing. It does not verify the complete action-economy/initiative family, full round lifecycle, reactions or interrupts.

AutoPTU Python read-only head checked for this pass: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its current head states that the viewport-coordinate change is presentation only and does not change battle rules or outcomes.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary actions.

AI tactical policy: BLOCKING for specialized rescue, escort, protection, retrieval, extraction and objective-aware withdrawal policies unless separately verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

## Remaining boundaries

The outer assistance checkpoint is a logical atomic generation, not a claim of crash-safe database/disk commit.

Other agenda sources are still owned by their established systems. A future broader checkpoint pass can absorb more agenda families without making this assistance wrapper authoritative over unrelated goals or needs.

DEFER still needs a durable future condition/window model. COUNTERPROPOSE still needs structured proposal payloads for time, place, scope or alternative. Route reservation and resource allocation remain separate. `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain outside this chain.
