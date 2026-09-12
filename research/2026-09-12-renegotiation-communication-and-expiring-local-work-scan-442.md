# Renegotiation Communication and Expiring Local Work Scan — Pass 442

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

Repository cross-check

The complete recursive Narrative tree at `25fedb8a5e1b288c3d9d555be58e7c998ce34993` was inventoried before writing. Root files plus canon, design, implementation, proposals, research, sources, tests, tools and workflow surfaces were checked. The assistance chain through Pass 441, existing information-event dispatch patterns, generic schedule/MISSED behavior, Kairos/PTU routing and live read-only engine heads were inspected. Exact repository search found no prior `Stardew Valley` research anchor and no prior use of the PTU thread `Need some help for some side adventures. PTU` (`szuk12`). No canon file is changed.

Public source A — Stardew Valley Help Wanted quests

Sources:
- https://wiki.stardewvalley.net/Quests
- https://stardewvalleywiki.com/Quests

High-level reusable structure: the game distinguishes persistent story quests from short local requests. Help Wanted requests have a limited completion window, while ordinary world life continues. The public wiki also documents that a daytime festival can make ordinary access unavailable during the request window.

Ouros transformation: small assistance promises can have real windows without becoming main-story locks. If circumstances invalidate the accepted plan, the responder can ask to reopen terms. The request to renegotiate must travel as information; it does not silently extend the old commitment or fabricate a replacement appointment.

Excluded protected material: villagers, town layout, authored quest text, rewards, item tables, festival content and game-specific progression.

Public source B — PTU community side-adventure discussion

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/szuk12/

The public PTU post describes a campaign whose main regional conflict continues while the GM seeks smaller side adventures that fit the same setting and tone.

Ouros transformation: local obligations can branch around a larger arc without every complication escalating into the campaign's central antagonist plot. A failed appointment, request for new terms, delayed survey or alternate form of help can remain a compact local story while the wider region continues independently.

Excluded material: the homebrew region, player characters, cult premise, collateral incident and any proposed comments or distinctive scenario material.

Reusable pattern

ACCEPTED LOCAL OBLIGATION -> ADVERSE START -> RESPONDER CHOICE -> EXPLICIT RENEGOTIATION MESSAGE -> REQUESTER KNOWLEDGE -> LATER NEW TERMS OR REFUSAL.

The communication step is mandatory. A responder's private decision does not modify requester knowledge and does not amend the agreement.

Reduced Ouros use

A specialist reaches the accepted appointment window while normal access remains closed. They choose `REQUEST_RENEGOTIATION`. A field-radio message says which commitment is being reopened and carries the original accepted window/location/scope references for context. Until that envelope is delivered, the requester can reasonably continue believing the original arrangement stands unchanged.

After delivery, a later system may author a new proposal, refusal, alternative or abandonment. Pass 442 stops before that policy.

Mechanically rich extension

If later replacement terms produce a hazardous survey, escort, retrieval, protection or extraction encounter, the narrative premise remains independent from tactical implementation. The exact encounter must declare every capability family it uses.

PTU / Caelo / Kairos cross-check

The source inventory continues to expose Kairos/PTU routing material as a rules-location aid, not automatic Ouros adoption. No relevant adopted Caelo override was identified for this world-level communication seam. Negotiated social obligations and information delivery therefore remain Ouros world-simulation responsibilities until a later intent explicitly requires AutoPTU.

Live engine evidence

AutoPTU-Java head inspected read-only: `f859888213385e313df923678b62374ac6919b22`, merge of PR #449, `Freeze Quick Switch side-effect order`. The change pins ordering for one Quick Switch path: AP consumption, switch application, temporary sent-out marker, then Trainer Feature event. This strengthens parity evidence for that specific Trainer Feature/reactive-switching behavior only. It does not verify complete action economy, full reactions/interrupts, Trainer Features as a family, or unrelated objective mechanics.

AutoPTU Python head inspected read-only: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is presentation-only coordinate synchronization after viewport resize and explicitly changes no battle rules or outcomes.

Conservative capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated; Quick Switch now has stronger evidence for one pinned side-effect order only.

AI legal-action infrastructure: verified only for audited ordinary actions; specialized INSPECT, ESCORT, PROTECT, RETRIEVE, CARRY, BRACE, EXTRACT or equivalent objectives require explicit admission.

AI tactical policy: BLOCKING for specialized objective behavior until verified policy exists.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

Open questions

A delivered renegotiation request still needs a later responder/requester proposal cycle. The new message does not decide who must make the next offer, whether the old commitment remains due until replaced, whether an alternative is acceptable, or what accountability applies if no new terms are reached before the window closes. Those policies remain separate from communication and from tactical resolution.
