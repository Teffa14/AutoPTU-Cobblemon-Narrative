# The Second Offer Had a Clock — Pass 447

Status: PROPOSED / NON-CANON
Canon effect: NONE
Location assignment: UNRESOLVED
Named NPC assignment: UNRESOLVED
Institution assignment: UNRESOLVED
Pokémon population assignment: UNRESOLVED

## Premise

A previously agreed assistance window became unworkable. The responder asked to reopen the terms, received permission to do so, and sent a second offer with a real deadline.

The requester receives the replacement terms while ordinary life continues around both actors. Another obligation may consume their attention. Access conditions may change again. Local Pokémon activity may make the proposed window more or less useful. The requester can accept, refuse, or simply fail to answer before the offer expires.

The central story fact is the difference among those outcomes. Silence after a deadline does not automatically mean refusal. Receipt does not mean agreement. Private acceptance does not mean the responder already knows there is a deal.

## Reduced version

This version can run without AutoPTU.

The scene uses:

- the old durable commitment;
- Pass 445 replacement terms;
- Pass 446 proposal transport and actual receipt;
- Pass 447 requester decision/expiry state;
- semantic time;
- private knowledge;
- later ordinary communication.

A possible sequence:

1. replacement terms arrive with a deadline;
2. the requester learns the exact new window and scope;
3. another local event or obligation competes for attention;
4. the requester accepts, rejects, or reaches the deadline without answering;
5. later actors can react to the documented outcome rather than guessing intention.

No battle, quest rollback or omniscient relationship adjustment is required.

## Mechanically rich version

If replacement terms are ultimately accepted and communicated back, the assistance can later resolve as a survey, escort, protection assignment, retrieval, containment task or extraction. The encounter must be generated from the world state at execution time rather than from conditions that existed when the second offer was authored.

Potential objective structures include:

- reach and inspect a safe observation point;
- escort a qualified worker through a newly reopened route;
- retrieve equipment before conditions close again;
- protect an inspection for a bounded interval;
- contain a local hazard long enough to complete a non-combat objective;
- withdraw safely when new evidence invalidates the plan.

These are design candidates only. None is mechanically admitted by this proposal.

## Engine dependency visibility

For any rich version:

- targeting/footprints/range/LoS — VERIFIED only in audited scopes;
- base movement legality — VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only in audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by requested behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated;
- AI legal-action infrastructure — `INSPECT`, `ESCORT`, `PROTECT`, `RETRIEVE`, `CONTAIN`, `EXTRACT` and similar verbs require explicit admission;
- AI tactical policy — BLOCKING for those specialized objective policies unless separately verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Narrative uses

This pattern can support future `SECONDARY`, `RELATIONSHIP`, `EXPLORATION`, `SETTLEMENT` or `FACTION` questlines after a concrete binding is canon-reviewed.

Useful consequences remain provenance-backed:

- explicit rejection can inform a later conversation about priorities;
- expiration can create a missed opportunity without assigning hostility;
- acceptance that has not yet travelled back can create temporary asymmetric expectations;
- a changed world can make the offer obsolete before either actor acts;
- a third party solving the underlying problem can remove the practical need while preserving the negotiation history.

## Canon boundary

No location, NPC, faction, species, institution or relationship consequence is established here. The proposal may later bind to an existing owner under the canonical correlation rule. It must not create a new isolated place or character merely to host this pattern.

## Research provenance

Structural inspiration is documented separately in `research/2026-09-12-replacement-offer-decision-and-expiry-scan-447.md`.

The primary new comparison is Stoneshard's separation among offered contracts, time limits, outcomes and later settlement situations, including background resolution by other mercenaries. Additional state-model comparisons come from Unofficial Voyage and UO Enigma. Only high-level structures are transformed; protected setting, characters, dialogue, objectives and plots are excluded.
