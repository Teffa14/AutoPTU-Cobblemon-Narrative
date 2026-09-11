# Selective request replanning research — Pass 424

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Retrieval date: 2026-09-11

## Repository inspection basis

The recursive Narrative repository tree at `c0395d4563aa7dfc317523e3666461599a467738` was inventoried before writing. Pass 423's assistance-request dispatch contract, implementation and regression were read in full. The existing Pass 421 delivery-to-replanning bridge and regression were read as the closest implemented analogue. Canon search was cross-checked against `canon/marea-interior-map-resident-network-v2.md`; recent research/proposal titles were searched before choosing this slice so it does not reintroduce the request-routing work from Passes 421–423.

No canon file is changed by this pass.

## Public source A — Pokémon Rejuvenation help-request structure

Source: Rejuvenation Wiki, `Chase Team AA`.
URL: https://rejuvenation.wiki.gg/wiki/Chase_Team_AA
Accessed: 2026-09-11.

High-level reusable observation:

The published quest guide describes a later request that becomes available after a set of local Help Center requests has been completed. The useful pattern is not the named faction, reward, battle or plot. It is the separation between a request hub, prior local work and a later consequence that becomes eligible because earlier work happened.

Ouros transformation:

A service request can be a durable world event without becoming an assignment in the recipient's agenda. Delivery can make a response eligible. Whether the recipient acts still belongs to that recipient's state, knowledge, schedule, travel cost and priorities.

Protected/distinctive material deliberately not imported:

No Rejuvenation characters, factions, rewards, map locations, dialogue, battle teams, plot sequence or quest names are copied into Ouros.

## Public source B — 80 Days and a world with its own agenda

Source: Just Adventure interview with Frogwares co-founder Waël Amr about `80 Days`.
URL: https://www.justadventure.com/2005/12/20/frogwares-wael-amr-interview/
Accessed: 2026-09-11.

High-level reusable observation:

The interview describes time, energy and money as interacting constraints and explicitly frames the world as having its own agenda that the player must fit into. Places may be available only at certain times; spending time on one activity changes what remains possible elsewhere.

Ouros transformation:

Receiving a request should create a new decision point inside an NPC's existing agenda. It must not create free time, erase earlier obligations or teleport the actor. A late request can be valid and still lose to another commitment. An accepted request can require a later travel or scheduling decision.

Protected/distinctive material deliberately not imported:

No characters, cities, vehicles, puzzles, dialogue, plot, monetary model or deadline structure is copied.

## Combined design lesson

A request has at least four separate states useful to Ouros narrative causality:

1. the requester decides to ask;
2. the request travels;
3. the named recipient actually receives it;
4. that recipient gets an opportunity to reconsider its own agenda.

Pass 423 implemented stages 1–2. Existing information infrastructure owns stage 3. Pass 424 binds stage 3 to stage 4 without inventing acceptance.

This supports stories where two equally legitimate NPC plans diverge because one actor heard the request and another did not, or because the recipient hears it too late to make the same choice it would have made earlier.

## PTU/Caelo cross-check posture

This slice does not introduce a new PTU rule. Narrative roles, job descriptions and receipt of a request grant no Move, Ability, Item, Trainer Feature, movement permission, reaction or combat action.

If a resulting response later reaches structured tactical play, the encounter must still enter through explicit AutoPTU ownership and use the permanent capability families below. The Kairos/PTU source index remains a locator for source rules, not implementation proof.

## Live engine evidence checked read-only

AutoPTU-Java `main`: `8098f8299a24e365649a25573ddcd664da996c71`, merge PR #442, `Port replacement initiative insertion mutation`.

That is concrete evidence for a replacement-initiative insertion seam. It does not prove the complete action-economy/initiative family, full round lifecycle, reactions or interrupts.

AutoPTU Python `main`: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its current head states that the viewport-coordinate synchronization change is presentation-only and does not change battle rules or outcomes.

Neither engine repository was modified.

## Capability posture for a mechanically rich assistance encounter

Targeting/footprints/range/LoS — VERIFIED only in audited scopes.
Base movement legality — VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement — PARTIAL.
Core calculations — VERIFIED only in audited scopes.
Action economy/initiative — PARTIAL; PR #442 strengthens one replacement insertion path only.
Full turn/round lifecycle — PARTIAL.
Full stateful damage pipeline — PARTIAL.
Status lifecycle — PARTIAL.
Terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior — individually gated.
Abilities — PARTIAL and individually gated.
Items — individually gated.
Trainer Features/perks — individually gated.
AI legal-action infrastructure — VERIFIED only for audited ordinary actions; specialized rescue/escort/protect/retrieve/carry/interact/brace/extract actions require explicit admission.
AI tactical policy — BLOCKING for specialized objective-aware rescue/escort/protection/withdrawal policies.
Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and in-flight recovery.

## Unresolved questions

The recipient's later ACCEPT / DEFER / REJECT / COUNTERPROPOSE response still lacks its own durable owner in this seam.

`OUROS_WORLD_ACTION_INTENT_LEDGER_V1` remains outside the coherent persistent-world checkpoint generation unless a later pass changes that contract.

`UNKNOWN` and `EXPLICITLY_ABANDONED` AutoPTU recovery outcomes remain separate from normal completion.

Persistent Injury and persistent Status projection remain outside this slice until their producing paths are sufficiently verified.
