# The Confirmation That Reached the Wrong Person — Case 360

Status: PROPOSED / NON-CANON
Canon authority: NONE
Date: 2026-09-08

## Premise

A field team has an accepted request and a valid authorization to pick up a shared instrument. The provider authors a confirmation before the pickup window. A real communication event exists and is delivered, but the envelope was addressed to another legitimate participant in the same operation rather than the intended receiver.

The session ends before the mistake is discovered.

After restart, the world preserves both records: the appointment notice identifies the intended sender/receiver relationship, while Communications preserves the actual envelope that travelled. They disagree, so the recovery boundary refuses to silently collapse them into one history.

## Narrative value

The conflict does not require deception or irrational behavior.

The provider can truthfully remember sending the confirmation. The unintended recipient can truthfully remember receiving a message. The actual pickup actor can truthfully say no confirmation reached them. The resource can still be physically waiting at the handoff point.

A player investigating the missed pickup can reconstruct the causal chain from authored notice, communication provenance, delivery status, actor knowledge, travel evidence and any later handoff attempt.

Possible consequences remain policy-dependent rather than automatic. The player may discover a one-off clerical mistake, a failing contact process, repeated routing errors, an overloaded intermediary or a deliberate misdirection only if separate evidence supports those conclusions.

## Reduced implementation

This version requires no AutoPTU battle.

Required existing world systems:

- semantic time;
- resource request and acceptance history;
- handoff authorization;
- appointment notice history;
- information-envelope provenance and delivery state;
- per-agent knowledge/memory;
- travel and arrival evidence when available;
- failed handoff attempt history;
- coherent V9 checkpoint recovery.

Playable resolutions include waiting, contacting the provider, forwarding the correct information, rescheduling, choosing another authorized courier, releasing the resource, or documenting the routing failure for later institutional review.

## Mechanically rich version

The player discovers the mistake only after the intended receiver has already travelled toward the handoff location. A wild disturbance or environmental closure makes the last leg time-sensitive. The objective is to reach or redirect the receiver and preserve the resource opportunity before the authorization window closes.

The narrative premise does not change if the tactical layer is unavailable. The reduced version resolves the same problem using semantic travel and communications.

## Permanent capability dependencies for rich version

Targeting / footprints / range / LoS: required only if the intervention enters structured combat or spatial interception. Current project classification: VERIFIED within audited ordinary contracts, not universal.

Base movement legality: required for ordinary tactical repositioning. Current project classification: VERIFIED within audited scope.

Complete movement including push/pull/knockback/interception/forced movement: required if interception, forced separation from cargo, shoves, knockback or movement reactions matter. Current project classification: PARTIAL; treat those variants as gated.

Core calculations: required for ordinary deterministic battle arithmetic. Current project classification: VERIFIED within audited scope.

Action economy / initiative: required for structured turn actions. Current project classification: VERIFIED for audited primitives.

Full turn/round lifecycle: required for round deadlines, start/end triggers or once-per-round logic. Current project classification: PARTIAL.

Full stateful damage pipeline: required if damage consequences matter. Current project classification: PARTIAL.

Status lifecycle: required for persistent conditions and cleanup. Current project classification: PARTIAL.

Terrain/weather/hazards/zones/reactions: required only if the closure or wild disturbance uses those mechanics. Current project classification: MIXED / PARTIAL / BLOCKING by exact family.

Move-specific behavior: each selected Move must be individually verified. Current project classification: PARTIAL.

Abilities: each selected Ability must be individually verified. Current project classification: PARTIAL. Current Intimidate/Flower Veil parity is representative evidence, not family coverage.

Items: each battle-relevant Item must be individually verified. Current project classification: PARTIAL.

Trainer Features/perks: each interrupt or modifier must be individually verified. Current project classification: PARTIAL.

AI legal-action infrastructure: ordinary audited actions are available; cargo/pickup/interception-specific legal actions still require explicit contracts.

AI tactical policy: BLOCKING for delivery-first, intercept-to-inform, protect-courier, preserve-resource, rerouting and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for end-to-end cargo/objective semantics, structured interruption playback and acknowledgement.

## Reduced fallback for every blocked dependency

If complete movement is unavailable, interception becomes semantic arrival at a route node rather than a tactical intercept reaction.

If round lifecycle is unavailable, the deadline remains semantic-world time rather than a battle-round timer.

If hazards/weather are unavailable, the closure becomes an authored route availability change rather than a tactical zone effect.

If AI tactical policy is unavailable, the structured encounter uses ordinary legal combat goals or is resolved outside AutoPTU.

If Minecraft playback is unavailable, world state records the result and presentation remains non-authoritative.

## Canon questions left open

No specific Ouros institution, instrument, field team, penalty or communication technology is authorized by this proposal.

Before promotion, a local binding must identify the institution, its scheduling policy, the actors involved, the resource, the actual route/location and any consequences for a missed pickup.
