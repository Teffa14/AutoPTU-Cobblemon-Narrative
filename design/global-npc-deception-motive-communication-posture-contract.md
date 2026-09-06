# Global NPC deception motive / communication-posture contract — Pass 300

Status: IMPLEMENTED, NON-CANON SYSTEM CONTRACT
Date: 2026-09-06

## Purpose

Pass 295–299 established deception authorship, delivery, persistence, discovery and source-attribution exposure. This pass adds the missing world-agent decision seam: an NPC can evaluate whether to disclose the basis value, remain silent, or select a deceptive communication option.

This is a deterministic gameplay policy. It is not a psychological model and does not claim universal human lying behavior.

## Invariants

1. The decision consumes only evidence already present in the speaker's private `KnowledgeLedger`.
2. The opportunity must identify a concrete target and a concrete basis claim.
3. Deception is available only when proposed content or source attribution actually differs from the basis claim.
4. Truth, silence and deception remain distinct postures. Silence is not automatically classified as deception.
5. Relationship state is directional. High trust/affinity can increase honesty pressure; rivalry/fear can increase strategic deception pressure. These are bounded world-policy modifiers, not mind reading.
6. Explicit harm, exposure risk and duty conflict can make deception less attractive.
7. Goal pressure, utility gain and secrecy value can make deception more attractive.
8. A policy decision never authors or delivers a lie by itself. If `DECEPTIVE` wins, downstream code must still call the existing deception authoring and delivery contracts.
9. No choice here changes PTU legality or AutoPTU tactical policy.
10. All scores are inspectable implementation policy and may be replaced later without changing historical communication provenance.

## Executable API

`tools/global_npc_deception_policy.py`

Primary types:

- `DeceptionPolicyProfile`
- `CommunicationOpportunity`
- `CommunicationPolicyDecision`
- `CommunicationPosture`
- `DeceptionMotive`

Primary function:

`choose_communication_posture(...)`

The resolver scores three alternatives from explicit authored/runtime inputs. Ties resolve deterministically in favor of truth, then silence, then deception.

## Separation from existing layers

This module does not create `DeceptiveStatement`, expand audiences, schedule envelopes, modify relationships or infer discovery. It ends at an inspectable posture decision.

The intended chain is:

private evidence -> motive/opportunity -> communication posture -> optional deceptive statement -> audience -> delivery -> receiver evidence -> possible later exposure -> social consequence.

## Canon boundary

No NPC personality, faction ethic, legal duty, punishment, cultural norm or institutional truthfulness rule is canonized by this contract. Profiles and opportunities are data inputs that authored content or later simulation systems must supply.
