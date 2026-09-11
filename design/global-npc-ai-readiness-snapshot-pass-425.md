# Global NPC AI readiness snapshot — Pass 425

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 425 starts from narrative `main` `ff2872878a067b072307860905a26a79e34b12a7`, after Pass 424.

The recursive repository tree was inventoried before writing. Current focus, canon inventory, Marea resident/role canon, Pass 422 world-action persistence, Pass 423 request dispatch, Pass 424 delivery/replanning, relevant communication/replanning owners, regressions and recent research/proposals were checked before selecting this seam.

No canon file is changed.

Implemented seam

`tools/global_npc_assistance_response.py` records the delivered recipient's own response as a durable ordinary world action using the existing `WorldActionIntentLedger`.

The response is admitted only after a terminal delivered request, intact request provenance, receiver claim materialization and an exact `replan:information:<event_id>` trigger belonging to the recipient.

Supported responses are ACCEPT, DEFER, REJECT and COUNTERPROPOSE in assistance-specific intent kinds. The original request remains unchanged.

Agency posture

The requester still cannot accept on the recipient's behalf.

An ACCEPT record does not create free time, travel or a commitment. A DEFER record does not schedule its own wake. A REJECT record does not automatically alter trust. A COUNTERPROPOSE record does not alter the requester's agenda until a reply actually reaches that actor.

Research added

`research/2026-09-11-recipient-choice-and-consequence-scan-425.md` records transformed lessons from a public PTU campaign log, Wildermyth event eligibility/choice structure and Citizen Sleeper's competing progress/time pressures.

`proposals/2026-09-11-every-answer-leaves-a-schedule-behind-425.md` turns those lessons into a non-canon Ouros pattern where requests can lead to accepted, deferred, rejected or counterproposed help without erasing the recipient's existing life.

Read-only engine evidence

AutoPTU-Java `main`: `fec801a6ed420d9f5181a06a24158b92610ac7c8`, merged PR #443, `Freeze replacement initiative switch handoff policy`.

PR #443 is explicitly oracle-only. It freezes and traces the Python switch-to-replacement-initiative handoff policy, including `allow_replacement_turn` and `allow_immediate`. It does not wire that handoff into Java production runtime, First Blood or Quick Switch. Action economy/initiative therefore remains PARTIAL.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head remains explicitly presentation-only and does not change tactical rules or outcomes.

Both engine repositories remain read-only.

Capability posture

Targeting/footprints/range/LoS — VERIFIED only in audited scopes.
Base movement legality — VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
Core calculations — VERIFIED only in audited scopes.
Action economy/initiative — PARTIAL; PR #443 adds narrow oracle evidence only.
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

The proposed story pattern needs no tactical battle. Private delivery, semantic time, schedules, obligations, relationships, travel constraints, selective replanning and durable world-action intents are enough to preserve the response and its consequences.

Regression target

`tests/test_global_npc_assistance_response.py`

The regression covers all four responses, terminal-delivery gating, responder identity, exact causal trigger, reply target, AutoPTU-handoff rejection, provenance tampering, replay idempotency, conflicting reuse and snapshot durability.

Open boundary

The next useful seam is reply dispatch from the recipient's durable response back to the original requester. That reply must preserve the response action as provenance and must not change requester knowledge before delivery.

ACCEPT also needs a separate commitment/reservation owner before accepted help consumes time or initiates travel. DEFER needs a future condition/window. COUNTERPROPOSE needs an explicit proposal payload.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` still needs inclusion in the coherent persistent-world checkpoint generation.

AutoPTU `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain separate unresolved paths.
