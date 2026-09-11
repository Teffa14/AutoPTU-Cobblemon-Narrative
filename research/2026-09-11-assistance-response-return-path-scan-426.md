# Assistance response return-path research — Pass 426

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Retrieval date: 2026-09-11

Repository basis

The recursive narrative tree at `d3f75123908ac175a9ea0145695bc99cf608e6e6` was inventoried before writing. Current focus, the complete canon inventory, Passes 422–425, the information queue, private knowledge ledger, world-action persistence, Marea role canon, recent research/proposals and the Kairos/PTU source-routing material were checked. No canon file is changed.

Repository-wide source-name searches rejected recently processed anchors including Pokémon Nova, Pokémon Synthesis, Pokémon Living World, Outer Wilds, Pokémon Starwish, Pokémon Unchosen, Wildermyth, Citizen Sleeper, Pentiment and Roadwarden.

Public source A — The Blood of Dawnwalker

Source: PC Gamer interview/article on quest failure and world continuity, published 2026.
URL: https://www.pcgamer.com/games/rpg/the-blood-of-dawnwalker-lets-you-complete-areas-in-any-order-kill-any-npcs-you-like-and-still-complete-the-game-after-failing-every-quest-were-giving-even-more-freedom-to-players/
Accessed: 2026-09-11.

Reusable structure:

The developers describe a world in which failed or ignored quests do not invalidate the whole campaign. Objectives can close, alter or be approached in another order while the broader world remains playable. Time is tied to meaningful actions and outcomes can remove later opportunities.

Ouros transformation:

A response to an assistance request must be allowed to arrive after the original situation has changed. REJECT or DEFER should not break a quest graph. ACCEPT can arrive too late to solve the original problem yet still matter as historical evidence, relationship context or support for a later phase. The requester should learn the response only through explicit delivery, then replan against the world state that exists when the reply arrives.

Not imported: characters, vampire premise, setting, family plot, named factions, quests, dialogue or proprietary quest logic.

Public source B — Pokémon Mystère Exploration

Source: official Pokémon Mystère Exploration project site.
URL: https://www.pmexploration.net/
Accessed: 2026-09-11.

The public description presents multiplayer Mystery Dungeon-inspired exploration with changing dungeon structures, traps, hidden shops, positioning and terrain-aware combat.

Reusable structure:

A party can share an expedition while still depending on spatial conditions, route changes and environmental constraints. Information about a route or hazard is useful only when it reaches the people who need it, and a changed environment can make an earlier plan obsolete.

Ouros transformation:

A returned assistance response can be narratively important even when nobody physically joins the original encounter. A responder may send timing, availability, a refusal, a warning or a counterproposal. When the message reaches the requester, that actor evaluates it against current route condition and current obligations. Minecraft may present the changed environment, but communication state remains authoritative in the world system.

Not imported: dungeon layouts, Pokémon roles, traps, blessings, shops, combat controls or project-specific progression.

Combined design lesson

The return path is a separate causal phase. A durable response does not alter the requester until it travels. Delivery can occur after the originating objective has changed, failed, succeeded by another route or moved into a new phase. The historical chain should remain inspectable:

request decision -> request delivery -> recipient replan -> durable response -> response message -> requester receipt -> requester replan.

This supports delayed answers, stale answers and useful-but-late answers without creating omniscient shared state.

PTU/Caelo boundary

This pass creates no PTU rule and grants no Move, Ability, Item, Feature, movement exception or reaction. If a later response causes a structured encounter, exact capabilities must be admitted individually through AutoPTU.

Live engine evidence checked read-only

AutoPTU-Java `main`: `0415392b3391aed7329a062da159c882e0e2d43e`, merged PR #444, `Harden replacement initiative caller policy contract`.

PR #444 freezes the pinned Python `_apply_switch` caller policy set for ordinary Switch, TrainerSwitch, QuickSwitch, Round Trip, Quick Switch trigger, Parting Shot and move-target replacement paths. It remains oracle-only. `INSERT_REPLACEMENT_INITIATIVE`, First Blood and Quick Switch runtime stages remain pending. Action economy/initiative therefore remains PARTIAL.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The current head remains presentation-only and states that viewport-coordinate synchronization does not alter battle rules or outcomes.

Capability posture for mechanically rich variants

Targeting/footprints/range/LoS — VERIFIED only in audited scopes.
Base movement legality — VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
Core calculations — VERIFIED only in audited scopes.
Action economy/initiative — PARTIAL; PR #444 is caller-policy oracle evidence, not complete runtime coverage.
Full turn/round lifecycle — PARTIAL.
Full stateful damage pipeline — PARTIAL.
Status lifecycle — PARTIAL.
Terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior — individually gated.
Abilities — PARTIAL and individually gated.
Items — individually gated.
Trainer Features/perks — individually gated.
AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract actions require admission.
AI tactical policy — BLOCKING for specialized objective-aware rescue, escort, protection, extraction and withdrawal policies.
Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

Unresolved questions

A delivered response still needs a response-specific delivery-to-replanning bridge before the requester can act on it. ACCEPT still needs a separate commitment/reservation owner. DEFER needs an explicit future condition or window. COUNTERPROPOSE still needs an explicit proposal payload. `OUROS_WORLD_ACTION_INTENT_LEDGER_V1` remains outside the coherent persistent-world checkpoint generation. AutoPTU UNKNOWN, EXPLICITLY_ABANDONED, persistent Injury and persistent Status remain separate paths.
