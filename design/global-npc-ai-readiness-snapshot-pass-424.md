# Global NPC AI readiness snapshot — Pass 424

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 424 starts from narrative `main` `c0395d4563aa7dfc317523e3666461599a467738`, after Pass 423.

The recursive repository tree was inventoried before writing. Pass 423 request dispatch files, the Pass 421 observation-delivery replanning bridge, relevant private-knowledge/communication/replanning owners, current Marea canon references and recent research/proposals were checked before selecting this seam.

No canon file is changed.

Implemented seam

`tools/global_npc_assistance_request_replanning.py` connects a Pass 423 assistance-request envelope to the existing world-event coordinator.

The bridge requires exact world-action, envelope and source-claim binding. A terminal successful delivery can wake only the target named by the original `REQUEST_ASSISTANCE` action. Pending, failed or waiting-for-ACK messages create no recipient decision.

The implementation preserves the original world `action_id` as provenance through request authoring, transmission, receiver knowledge and replanning.

Agency posture

Receipt creates an opportunity to reconsider. It is not acceptance.

The target's decision remains local to that NPC. The requester cannot create the target's commitment, travel, reservation or schedule mutation.

An unrelated NPC does not acquire the claim simply because it shares a location, institution or compatible agenda.

Research added

`research/2026-09-11-selective-request-replanning-scan-424.md` records transformed design lessons from Pokémon Rejuvenation's request-hub structure and an 80 Days developer interview about time/resource constraints and a world with its own agenda.

`proposals/2026-09-11-the-request-opens-a-window-not-a-command-424.md` turns those lessons into a non-canon Ouros pattern for requests that arrive inside persistent NPC schedules.

Read-only engine evidence

AutoPTU-Java `main`: `8098f8299a24e365649a25573ddcd664da996c71`, merged PR #442, `Port replacement initiative insertion mutation`.

This provides concrete evidence for replacement initiative insertion. Action economy/initiative remains PARTIAL because the evidence does not cover the complete initiative/action/reaction family or full round lifecycle.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The current head is explicitly presentation-only and does not change tactical rules or outcomes.

Both engine repositories remain read-only.

Capability posture

Targeting/footprints/range/LoS — VERIFIED only in audited scopes.
Base movement legality — VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
Core calculations — VERIFIED only in audited scopes.
Action economy/initiative — PARTIAL.
Full turn/round lifecycle — PARTIAL.
Full stateful damage pipeline — PARTIAL.
Status lifecycle — PARTIAL.
Terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior — individually gated.
Abilities — PARTIAL and individually gated.
Items — individually gated.
Trainer Features/perks — individually gated.
AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized objective actions require explicit admission.
AI tactical policy — BLOCKING for specialized rescue/escort/protection/extraction/withdrawal policy.
Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING for authoritative specialized objectives, specialized non-KO completion and in-flight recovery.

Reduced narrative availability

The proposal can run without tactical battle support. Semantic time, private knowledge, communications, schedules, obligations, permissions, travel constraints, world-action intents and selective replanning are sufficient to tell the core story.

Regression target

`tests/test_global_npc_assistance_request_replanning.py`

The new regression covers successful selective wake, peer isolation, queued request, unavailable channel, local ACK acceptance/rejection, delivery-budget deferral and provenance tampering.

Open boundary

The next useful executable seam is the recipient's durable response. ACCEPT, DEFER, REJECT and COUNTERPROPOSE must be represented as that actor's own decision. A reply that affects the requester should then travel back through the explicit communication network.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` also still needs inclusion in the coherent persistent-world checkpoint generation.

AutoPTU `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain separate unresolved paths.
