# Global NPC AI readiness snapshot — Pass 423

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 423 starts from narrative main `c39cd4676c4102503a811f23b2ae5c6af954c57e` after Pass 422. The recursive repository tree was inventoried before writing. `CURRENT_FOCUS.md`, the complete canon inventory, canon governance, the Marea resident network, Pass 418–422 consequence/observation/delivery/replanning/action-intent chain, information delivery, private knowledge, recent research/proposals and `sources/kairos/KAIROS_SOURCE_INDEX.md` were reviewed. Canon files remain unchanged.

Implemented seam

`tools/global_npc_assistance_request_dispatch.py` converts one admitted `PLANNED` `REQUEST_ASSISTANCE` world-action intent into one explicit request claim and one ordinary information envelope addressed to the exact action target.

The source claim preserves the action ID as provenance root. Scheduling does not mutate the target. Failed, queued and waiting-for-ack states do not create receiver knowledge. Successful delivery uses the existing information queue and preserves causal lineage into the receiver's report claim.

The dispatch owner does not accept the request on the target's behalf, create a commitment, edit a schedule, reserve travel, call AutoPTU or infer any Trainer/Pokémon mechanic.

Exact replay remains idempotent, including after terminal delivery. Conflicting event reuse fails closed before a conflicting source request claim is authored.

Regression

`tests/test_global_npc_assistance_request_dispatch.py` covers admission, source provenance, pre-delivery isolation, successful delivery lineage, unavailable-channel failure, local acknowledgement waiting/rejection, terminal replay, event collision, target requirements, chronology and unknown action identity.

Research and proposal

Research: `research/2026-09-11-routed-assistance-and-field-time-scan-423.md`

Proposal: `proposals/2026-09-11-the-request-has-a-route-of-its-own-423.md`

Both remain outside canon.

New public sources

`PTU Night Rangers: Hollow Underdeep`, StartPlaying Games. Reusable structure: field liaisons reconnect separated communities through bounded travel and delivery work; communication and custody can be adventure objectives without requiring combat.

`Pentiment` design interview with Josh Sawyer, MMORPG.com. Reusable structure: opportunities exceed available time, so receipt of information must compete with existing commitments rather than granting unlimited action capacity.

`Roadwarden` design analysis by Jay McGavren. Reusable structure: longer routes consume meaningful time and records help preserve orientation; response latency and travel cost can be explicit rather than hidden by quest scripting.

No characters, plots, settings, dialogue, maps, distinctive missions or protected prose were imported.

PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a router into the supplied PTU/Kairos material rather than an Ouros mechanics grant. Its living-world evidence supports persistent off-session activity as a structural reference. Combat, movement, statuses, hazards, weather, encounter construction, Items and Trainer capabilities still require their actual source rules and implementation evidence.

Live AutoPTU-Java evidence

Inspected main: `8098f8299a24e365649a25573ddcd664da996c71`, merge PR #442, `Port replacement initiative insertion mutation`, committed September 11, 2026 UTC.

This is stronger than Pass 422's baseline. Java now contains the server-authoritative replacement initiative insertion mutation corresponding to the previously frozen Python oracle. The implementation handles missing/duplicate candidates, authoritative detailed order, natural insertion, cursor preservation and explicitly allowed immediate replacement turns, with oracle-parity tests included in the switch-entry parity workflow.

This evidence strengthens one bounded replacement-initiative path. It does not establish complete action economy/initiative, all switching semantics, full round lifecycle, reaction timing, interruption policy or other unrelated initiative mutations. The permanent action economy/initiative category therefore remains PARTIAL.

Live AutoPTU evidence

Inspected main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains the August 29, 2026 viewport-resize coordinate synchronization change and explicitly states that it is presentation-only and does not change battle rules or outcomes.

Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited paths.

Action economy/initiative: PARTIAL. PR #442 strengthens replacement initiative insertion only.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary actions. Specialized rescue, escort, protect, retrieve, carry, interact, brace and extract actions still require explicit admission.

AI tactical policy: BLOCKING for specialized rescue-first, escort-first, protect-carrier, objective-aware withdrawal and disengage-after-objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for authoritative tactical objective state, specialized non-KO completion and in-flight recovery.

Narrative encounter reduction

`The Request Has a Route of Its Own` has a zero-battle reduced implementation. A requester records a durable assistance intent, sends one explicit message and waits for real delivery. The target then owns any response.

The full version may embed request generation inside rescue, escort, retrieval, protection, extraction or hazard pressure. Those variants inherit the exact relevant capability families above. Forced displacement needs complete movement; timed windows need full turn/round lifecycle; persistent damage/status outcomes need their full pipelines; reactive terrain/weather needs the terrain/weather/hazards/zones/reactions family; specialized objective choice needs AI legal-action and tactical-policy support.

Unresolved seams

A delivered assistance request is not yet directly wired from this Pass 423 dispatch helper into the selective delivery-to-replanning coordinator. Existing infrastructure can perform that later step, but the end-to-end request-specific contract still needs a regression proving that only the explicit recipient wakes.

Receiver acceptance, deferral, rejection and counterproposal do not yet have a dedicated durable response owner. They must remain receiver-owned decisions.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` is still outside the coherent persistent-world checkpoint generation. A restart must not reconstruct missing intent authority from a request message alone.

Engine authority `UNKNOWN` and `EXPLICITLY_ABANDONED` still require separate durable policies. Persistent Injury and Status consequences remain deferred until their producing AutoPTU paths are sufficiently verified.
