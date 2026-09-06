# The Order Signed on Yesterday's Report

Status: PROPOSED / NON-CANON
Date: 2026-09-06
Pass: 310

## Premise

A local authority issued a consequential route restriction after receiving an investigator's custody assessment that reported a documentation gap in a recovered relay sample. The order was reasonable enough to issue under the information available then. Later, the investigator finds a missing transfer record and issues a superseding assessment supporting continuity.

The correction reaches some people but not the official who signed the restriction. The repaired report therefore exists while the old order remains active.

The mystery is no longer only 'what does the evidence say?' It becomes 'which decisions were made from which version, who has learned that the basis changed, and what must be reviewed rather than silently erased?'

No place, institution, NPC, title or incident in this proposal is canon-approved.

## World-state structure

The old custody assessment remains historical evidence of what the investigator concluded at that time.

The signing actor receives the old assessment claim and makes an authored decision such as a route restriction, inspection hold, service suspension or access denial. Pass 310 records the exact assessment claim as that decision's basis.

A later assessment supersedes the first. Pass 309 can propagate it to explicit recipients. If the signing actor never receives it, the order remains `SUPERSEDED_NOT_RECEIVED` from a review perspective. The world knows a better conclusion exists; that actor does not.

Once the correction actually reaches the signer, Pass 310 can classify the old order as `REVIEW_ELIGIBLE`. Nothing is reversed automatically. An authorized review may uphold, narrow, replace or cancel the restriction for reasons that must be recorded separately.

## Quest hooks

A traveler discovers that a route remains closed even though a technician says the sample problem was resolved. The apparent contradiction is genuine because different actors possess different versions.

A merchant who lost business wants the restriction removed immediately. A cautious official insists that corrected custody does not prove the structure itself is safe. Both positions can be internally coherent.

A rival benefits from the stale order and has incentive to delay delivery of the correction. That possibility should use the existing deception/communication systems only when evidence supports it; the quest must also work when the delay is ordinary backlog or reachability failure.

An investigator can trace the decision backward: active order -> signing actor -> basis claim -> old assessment -> later superseding assessment -> actual receipt history.

## Reduced implementation version

The entire loop can run without tactical combat.

Locations are ordinary world nodes. Travel uses verified base movement/world-route infrastructure. The restriction is authored world state. Evidence and decision basis live in private ledgers and Pass 310's dependency registry. The revision travels through the ordinary information queue. Review is an explicit later world event.

Any dangerous route remains blocked as a binary traversal gate. Weather, structural instability and Pokémon activity can be presented narratively without mechanically resolving knockback, dynamic zones, statuses or delayed collapse.

## Full encounter version

The restricted route crosses an exposed relay service span. A correction arriving late causes multiple groups to converge while a maintenance crew is already present. The scene can include unstable footing, wind displacement, falling debris, emergency interception, a stranded Pokémon or worker, and optional confrontation over whether the route should reopen before inspection finishes.

Exact battle/encounter dependencies:

- targeting/footprints/range/LoS for spatial attacks or rescue targeting;
- base movement legality for ordinary traversal;
- complete movement including push/pull/knockback/interception/forced movement for wind, falls, catches or forced displacement;
- core calculations for ordinary deterministic combat arithmetic;
- action economy/initiative if the scene enters tactical resolution;
- full turn/round lifecycle for timed collapse or phased emergency events;
- full stateful damage pipeline for environmental or combat injury;
- status lifecycle for persistent conditions;
- terrain/weather/hazards/zones/reactions for wind, debris, unstable surfaces and reactive rescue;
- move-specific behavior only for authored Moves used in the encounter;
- abilities only for authored Ability interactions;
- items only for authored equipment interactions;
- Trainer Features/perks only for authored Trainer interventions;
- AI legal-action infrastructure for legal tactical option generation;
- AI tactical policy for autonomous tactical choice by non-player combatants/rescuers;
- Minecraft/Cobblemon/Craftics adapter/playback support for authoritative results to appear reliably in the playable scene.

## Capability-aware fallback

The narrative premise survives without the rich tactical layer. Replace the exposed service span with safe, blocked and inspectable nodes. Wind stays audiovisual. Debris is a static gate. Rescue becomes deterministic travel plus authored checks only after those checks are validated against the active rules profile. Optional confrontation can hand off to AutoPTU only within capabilities verified at implementation time.

## Consequence design

A correction can reopen one decision without restoring all social trust. The signer may have acted responsibly on the old information. The investigator may still be criticized for communication delay. A technician may be cleared on custody continuity while remaining responsible for an unrelated maintenance failure. A merchant can suffer real loss even when nobody acted maliciously.

This lets Ouros preserve consequences while avoiding retroactive omniscience or one-click moral resets.

## Canon and mechanics questions

Which Ouros institutions, if any, have authority to impose route restrictions or inspection holds remains undecided.

Which PTU/Caelo/Kairos Skills, Trainer Features or Pokémon capabilities can legitimately inspect structural safety, authenticate records or accelerate rescue must be validated before use.

Whether decision review, compensation, institutional appeals or reputation repair become reusable global systems remains open. Pass 310 records dependency and review eligibility only.
