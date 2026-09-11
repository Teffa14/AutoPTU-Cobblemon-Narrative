# Global NPC AI readiness snapshot — Pass 426

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 426 starts from narrative `main` `d3f75123908ac175a9ea0145695bc99cf608e6e6`, after Pass 425.

The recursive repository tree was inventoried before writing. `CURRENT_FOCUS.md`, the complete canon inventory, Passes 422–425, world-action persistence, information delivery, private knowledge, Marea role canon, recent research/proposals and PTU/Kairos routing material were checked. Exact source-name searches were used to reject recently reused research anchors.

No canon file is changed.

Implemented seam

`tools/global_npc_assistance_response_dispatch.py` turns one durable assistance response world action into one explicit information envelope back to the original requester.

The helper requires exact request/response actor binding and chronology. Its source claim preserves the response action ID as provenance root while retaining the request/response relationship in the claim subject.

The requester receives no private claim merely because the response exists or the reply was queued. Ordinary terminal delivery remains the only path that can materialize requester knowledge.

The pass does not yet connect response delivery to requester replanning. It also does not create commitments, reservations, travel, relationship changes or PTU resolution.

Regression

`tests/test_global_npc_assistance_response_dispatch.py` verifies all four response kinds, exact sender/requester binding, source provenance, successful receiver lineage, queued/failed/waiting isolation, replay idempotency, chronology, unsupported-kind rejection and event-ID collision behavior.

Research added

`research/2026-09-11-assistance-response-return-path-scan-426.md` records transformed lessons from The Blood of Dawnwalker and Pokémon Mystère Exploration after duplicate-source searches rejected recent recurring anchors.

The shared design lesson is that a reply can arrive after the situation that caused it has changed. The response remains a durable historical fact, while the requester should re-evaluate only after actual receipt and against current world state.

Proposal added

`proposals/2026-09-11-the-answer-can-arrive-after-the-problem-changed-426.md` turns that lesson into a non-canon Ouros pattern. The reduced form requires no battle and preserves delayed/stale/useful-late replies through semantic time, communication, private knowledge, schedules, obligations and world-action persistence.

Read-only engine evidence

AutoPTU-Java `main`: `0415392b3391aed7329a062da159c882e0e2d43e`, merged PR #444, `Harden replacement initiative caller policy contract`.

PR #444 freezes the pinned Python `_apply_switch` caller policy set across ordinary Switch, TrainerSwitch, QuickSwitch, Round Trip, the Quick Switch trigger, Parting Shot and move-target replacement. It remains oracle-only. `INSERT_REPLACEMENT_INITIATIVE`, First Blood and Quick Switch runtime stages remain pending. Action economy/initiative therefore remains PARTIAL.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head remains explicitly presentation-only and does not alter tactical rules or outcomes.

Both engine repositories remain read-only.

Capability posture

Targeting/footprints/range/LoS — VERIFIED only in audited scopes.

Base movement legality — VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement — PARTIAL.

Core calculations — VERIFIED only in audited scopes.

Action economy/initiative — PARTIAL; PR #444 strengthens caller-policy evidence only.

Full turn/round lifecycle — PARTIAL.

Full stateful damage pipeline — PARTIAL.

Status lifecycle — PARTIAL.

Terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior — individually gated.

Abilities — PARTIAL and individually gated.

Items — individually gated.

Trainer Features/perks — individually gated.

AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized objective actions need explicit admission.

AI tactical policy — BLOCKING for specialized objective-aware rescue, escort, protection, extraction and withdrawal behavior.

Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

Reduced narrative availability

The new proposal can run entirely at world level. A request is sent, received and answered; the answer travels back; meanwhile the originating problem may change. No tactical capability is required to preserve that causality.

Mechanically rich variants retain the exact capability gates above. Forced displacement requires complete movement. Late entry or exact action timing requires action economy/initiative. Multi-round arrival windows require full turn/round lifecycle. Persistent damage/status consequences require their respective pipelines. Environmental phases or reactions require terrain/weather/hazards/zones/reactions. Specialized rescue/escort/extraction choices require explicit AI legal-action and tactical-policy support.

Open boundary

The next executable seam is response delivery-to-replanning for the original requester. It must require terminal successful delivery, preserve the response-action provenance root and wake no unrelated agent.

After that, ACCEPT needs a separate commitment/reservation owner before it consumes time or initiates travel. DEFER needs an explicit future condition/window. COUNTERPROPOSE needs an explicit payload for proposed scope, timing, location or alternative contributor.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` still needs inclusion in the coherent persistent-world checkpoint generation.

AutoPTU `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain separate unresolved paths.
