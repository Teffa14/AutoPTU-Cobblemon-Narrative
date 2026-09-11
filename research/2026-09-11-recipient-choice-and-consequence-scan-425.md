# Recipient choice and consequence research — Pass 425

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Retrieval date: 2026-09-11

## Repository inspection basis

The recursive Narrative repository tree at `ff2872878a067b072307860905a26a79e34b12a7` was inventoried before writing. The Pass 422 world-action owner, Pass 423 request dispatch, Pass 424 request-delivery/replanning bridge, their regressions, current global NPC focus, relevant Marea canon and recent research/proposal titles were checked before selecting this slice.

No canon file is changed by this pass.

## Public source A — PTU campaign log #13

Source: `campaign log #13`, r/PokemonTabletop.
URL: https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5
Accessed: 2026-09-11.

High-level reusable observation:

The published PTU session summary describes exploration through a haunted location where room-to-room progress mixes battles, a riddle, blocked access, searching, capture opportunities and environmental interaction. The useful structural lesson is that an assignment can contain several kinds of work, so answering a request for help should not imply that the helper has agreed to a single combat-shaped solution.

Ouros transformation:

An NPC who receives a request can accept the overall need while proposing a different contribution: inspect records, repair equipment, hold a route, escort someone, retrieve evidence or join a later field phase. A counterproposal can therefore preserve the requester's goal while changing who does what and when.

Protected/distinctive material deliberately not imported:

No mansion, room sequence, riddle, captured Pokémon, hooded figure, battle setup, dialogue or session plot is copied into Ouros.

## Public source B — Wildermyth event eligibility and character-state choice

Source: Wildermyth Wiki, `Event` and `Event Types`.
URLs:
- https://wildermyth.com/wiki/Event
- https://wildermyth.com/wiki/Event_Types
Accessed: 2026-09-11.

High-level reusable observation:

Wildermyth chooses story events only when the participating characters satisfy targeting criteria such as personality, hooks or relationships, and events may then present choices with persistent character consequences. The reusable structure is that a choice belongs to the actor/context that qualifies for it; another character cannot make the decision merely by causing the event to appear.

Ouros transformation:

Delivery of an assistance request creates eligibility for the recipient to consider a response. The response is authored by that recipient's planner from its own knowledge, relationships, obligations, risk, travel and schedule state. The requester supplies a cause, not a remote command.

Protected/distinctive material deliberately not imported:

No Wildermyth characters, relationships, event text, transformations, campaign beats, combat bonuses or event implementations are copied.

## Public source C — Citizen Sleeper competing clocks and finite attention

Sources:
- Citizen Sleeper official site: https://citizensleeper.com/
- Citizen Sleeper overview describing Dice, Clocks and Drives: https://player.gg/explore/games/152271-citizen-sleeper
- Neoseeker overview of branching clocks: https://www.neoseeker.com/citizen-sleeper/Do_My_Dialogue_Choices_Matter
Accessed: 2026-09-11.

High-level reusable observation:

Citizen Sleeper presents multiple progressing opportunities and pressures under finite per-cycle capacity. Some branches compete with clocks that continue independently, so choosing one line can close or delay another.

Ouros transformation:

ACCEPT, DEFER, REJECT and COUNTERPROPOSE are useful only if they preserve schedule cost and competing obligations. Acceptance should later create an explicit commitment rather than free time. Deferral should retain a future condition or window. Rejection should leave a durable answer. Counterproposal should create a new communicative branch rather than silently edit the requester's plan.

Protected/distinctive material deliberately not imported:

No station, characters, factions, dice system, named clocks, drives, economy, quests, endings or dialogue are copied.

## Combined design lesson

An assistance request produces a causal opportunity, followed by a response owned by the recipient.

The response should be durable before any downstream effect occurs. Four semantic choices are sufficient for the first executable seam:

- `ACCEPT_ASSISTANCE_REQUEST`
- `DEFER_ASSISTANCE_REQUEST`
- `REJECT_ASSISTANCE_REQUEST`
- `COUNTERPROPOSE_ASSISTANCE_REQUEST`

Each response remains a world action selected by the responder. It does not itself create travel, commitment, inventory transfer, relationship change or a reply in the requester's knowledge.

This supports NPC arcs where two people care about the same problem but disagree about timing or method without either actor being treated as irrational or omniscient.

## PTU/Caelo cross-check posture

This slice creates no PTU rule. A narrative response grants no Move, Ability, Item, Trainer Feature, reaction, movement exception or tactical objective.

The PTU/Caelo/Kairos index remains a source locator. Any later tactical encounter must admit the exact engine capability families it uses.

## Live engine evidence checked read-only

AutoPTU-Java `main`: `fec801a6ed420d9f5181a06a24158b92610ac7c8`, merge PR #443, `Freeze replacement initiative switch handoff policy`.

PR #443 is explicitly oracle-only. It freezes the pinned Python switch-to-replacement-initiative handoff policy and traces real switch call sites, including `allow_replacement_turn` and `allow_immediate`. It does not wire the switch handoff into Java production runtime, First Blood or Quick Switch. This strengthens evidence for a narrow initiative/switch policy seam while leaving action economy/initiative PARTIAL.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head remains presentation-only and states that viewport-coordinate synchronization does not change battle rules or outcomes.

Neither engine repository was modified.

## Capability posture for a mechanically rich assistance encounter

Targeting/footprints/range/LoS — VERIFIED only in audited scopes.
Base movement legality — VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
Core calculations — VERIFIED only in audited scopes.
Action economy/initiative — PARTIAL; PR #443 is oracle-only evidence for one replacement switch-handoff policy seam.
Full turn/round lifecycle — PARTIAL.
Full stateful damage pipeline — PARTIAL.
Status lifecycle — PARTIAL.
Terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior — individually gated.
Abilities — PARTIAL and individually gated.
Items — individually gated.
Trainer Features/perks — individually gated.
AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract actions require explicit admission.
AI tactical policy — BLOCKING for specialized objective-aware rescue/escort/protection/withdrawal behavior.
Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

## Unresolved questions

A recorded ACCEPT response still needs a separate owner to create a real commitment or reservation. The response record must never be treated as proof that travel or field work already happened.

DEFER needs an explicit future condition/window before it can wake again without polling.

COUNTERPROPOSE and any answer that should affect the requester need reply dispatch through ordinary communication with their own provenance.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` remains outside the coherent persistent-world checkpoint generation unless a later pass changes that contract.

AutoPTU `UNKNOWN`, `EXPLICITLY_ABANDONED`, persistent Injury and persistent Status remain separate unresolved paths.
