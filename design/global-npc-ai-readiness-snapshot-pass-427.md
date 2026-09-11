# Global NPC AI readiness snapshot — Pass 427

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT
Date: 2026-09-11

Repository baseline

Pass 427 starts from narrative `main` `95dfae83fcd6c6846b10f8392701d65af9674818`, after Pass 426.

Repository inspection

The recursive repository tree was inventoried before writing. `CURRENT_FOCUS.md`, canon governance, the Marea resident network, Pass 422–426 assistance-request/response chain, knowledge delivery and world-event replanning owners, recent research/proposals and the PTU/Kairos routing boundary were checked. No canon file is modified by this pass.

Implemented slice

`tools/global_npc_assistance_response_replanning.py` validates the complete request/response/envelope/source-claim binding and allows only a genuinely delivered assistance response to materialize private knowledge and wake the original requester through `GlobalNpcWorldEventCoordinator`.

Supported durable responses remain ACCEPT, DEFER, REJECT and COUNTERPROPOSE. Delivery gives the requester new information. It does not create a commitment, reservation, route, relationship change or AutoPTU handoff.

Regression coverage

`tests/test_global_npc_assistance_response_replanning.py` covers all four response kinds, requester-only wake-up, third-party isolation, queued delivery, unavailable channel, zero delivery budget, local ACK acceptance/rejection and tampered response provenance.

Research and proposal

New research anchors are Pokemon Reclamation for actor-owned handoff continuity and Signs of the Sojourner for communication/travel consequences that continue after successful or failed interaction. The resulting proposal, `The Answer Belongs to the Person Who Receives It`, keeps request, response, receipt and subsequent requester decision as separate durable facts.

Live engine evidence

AutoPTU-Java was inspected read-only at `0415392b3391aed7329a062da159c882e0e2d43e`, merge PR #444. The current replacement-initiative caller-policy evidence strengthens only that specific initiative seam. Action economy/initiative remains PARTIAL as a family.

AutoPTU remains read-only. No engine repository is modified by this pass.

Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract actions need explicit admission.
AI tactical policy: BLOCKING for specialized objective-first policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

Next seams

An ACCEPT response still needs a separate commitment/reservation owner before consuming time or starting travel. DEFER needs an explicit future condition or time window. COUNTERPROPOSE needs a structured proposal payload. The world-action intent ledger still needs coherent checkpoint integration. UNKNOWN and EXPLICITLY_ABANDONED AutoPTU recovery remain separate concerns, as do persistent Injury and Status projection.