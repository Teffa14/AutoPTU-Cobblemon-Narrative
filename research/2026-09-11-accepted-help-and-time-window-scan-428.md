# Accepted help and finite time-window research — Pass 428

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Retrieval date: 2026-09-11

Repository basis

The recursive Narrative tree at `f20fe3f9215a9e648809ccb7d6559406b8506d90` was inventoried before writing. `CURRENT_FOCUS.md`, the global goal/need/schedule contract, `ScheduledCommitment`, the world-event coordinator, the Pass 422–427 assistance chain, coherent world checkpoint surfaces, recent research/proposals and the PTU/Kairos boundary were checked. Exact source-title searches found no prior use of `I Was a Teenage Exocolonist` or `Pathologic 2` as research anchors. No canon file is changed.

Public source A — I Was a Teenage Exocolonist

Source: official Exocolonist site, https://www.exocolonist.com/

The official description frames a life across ten years where chosen activities, skills and jobs consume the finite span in which other events also occur. The useful abstraction for Ouros is opportunity cost: agreeing to one activity is meaningful because the actor has a limited calendar rather than unlimited parallel availability.

Ouros transformation: an ACCEPT assistance response should be able to create an explicit future commitment window owned by the responder. That window competes with the responder's goals, needs and other commitments through the existing agenda model. Acceptance therefore acquires temporal weight without becoming teleportation or automatic completion.

No characters, colony premise, card system, romance content, jobs, locations, endings, dialogue or event text are imported.

Public source B — Pathologic 2 community time-window observations

Sources: public r/pathologic discussions about time-limited objectives and time progression, including https://www.reddit.com/r/pathologic/comments/eoa4pq and https://www.reddit.com/r/pathologic/comments/exaja5 .

Community reports consistently describe objectives whose useful windows differ and a world clock that continues through ordinary activity while pausing in selected interfaces/conversations. The reusable structure is not the game's plague premise. It is that a commitment window can expire independently of whether the actor actually reached or completed the intended work.

Ouros transformation: a responder-owned commitment may become UPCOMING, DUE, GRACE or MISSED using Ouros semantic time. A missed assistance commitment should use the existing follow-up behavior rather than retroactively moving the NPC, claiming that the work happened off-screen or rewriting the acceptance.

No characters, disease setting, quest content, map, dialogue, survival systems or day structure are imported.

Supporting PTU community observation

A 2024 r/PokemonTabletop exploration discussion describes travel between settlements as multi-session exploration populated with small environmental situations and active wild-Pokémon behavior rather than empty transit. Source: https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9 .

Ouros transformation: accepting help does not collapse travel and field execution into the commitment itself. If the eventual assignment needs a route, wildlife interaction or structured encounter, those remain separate world/travel/AutoPTU steps. The commitment only gives the responder a bounded obligation window.

Combined design lesson

A useful acceptance chain is:

request -> recipient receipt -> recipient-owned ACCEPT -> response delivery -> explicit responder commitment window -> ordinary agenda competition -> later travel/world action/AutoPTU only when separately selected.

The commitment should carry provenance back to the ACCEPT action. It should not infer a location, route, resource reservation, relationship change or completed objective.

PTU/Caelo and engine boundary

This research introduces no PTU rule. A scheduled world commitment grants no Move, Ability, Item, Trainer Feature, movement exception, reaction or tactical permission.

Current live evidence checked read-only:

AutoPTU-Java `main` is `0415392b3391aed7329a062da159c882e0e2d43e`, merged PR #444, `Harden replacement initiative caller policy contract`. The evidence strengthens one replacement-initiative caller-policy seam only. Action economy/initiative remains PARTIAL as a family.

AutoPTU Python `main` is `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains explicitly presentation-only and does not change battle rules or outcomes.

Capability posture for a later mechanically rich assistance scene

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
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract actions still need explicit admission.
AI tactical policy: BLOCKING for specialized objective-first policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

Open questions

The accepted-help commitment ledger added by Pass 428 is not yet part of the coherent persistent-world checkpoint chain. Route reservation, location choice and resource allocation remain separate owners. DEFER still needs a durable future condition/window contract. COUNTERPROPOSE still needs structured proposal content. AutoPTU `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain separate concerns.
