# Engine readiness snapshot — Pass 242

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-03
Purpose: classify the exact engine capabilities consumed by the proposed ecological encounter handoff contract.

## Read-only repositories inspected

### AutoPTU-Java

Live `main` inspected at:

`c5ca00d22cc234d0ec8dc0429e60f8ee42381dec`

Commit: `Freeze terrain-trap semantic event payload (#337)`.

New evidence since Pass 241:

- tile-entry trap semantic event keys are frozen against the pinned Python oracle;
- trap block/trigger payload shape is asserted in Java tests;
- the Python tile-entry contract is exported as a CI artifact;
- forced-movement/landing work from the previous slice remains underneath this contract.

Interpretation: semantic event interoperability for this specific terrain-trap slice improved materially. This does not establish complete terrain/hazard/reaction support, complete movement, full status lifecycle or a general world-to-battle handoff.

### AutoPTU

Live `main` inspected at:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Latest commit remains presentation-only viewport coordinate synchronization and explicitly changes no battle rules or outcomes.

No Python change promotes any permanent capability family for Pass 242.

## Permanent capability categories

### targeting / footprints / range / LoS

State: VERIFIED within audited contracts.

Required for a normal structured engagement that needs spatial target legality. Not required when the ecological interaction remains overworld-only.

### base movement legality

State: VERIFIED within audited contracts.

Required when a BattleSpec contains ordinary tactical movement.

### complete movement including push/pull/knockback/interception/forced movement

State: PARTIAL.

The forced-movement landing path has direct evidence. That evidence does not prove complete interception, push/pull/knockback and all forced-movement interactions. The rich Sendero pursuit version remains gated if it requires interception or forced displacement.

### core calculations

State: VERIFIED within audited contracts.

Required for PTU arithmetic consumed by the selected tactical profile.

### action economy / initiative

State: VERIFIED within audited contracts.

Required for ordinary structured combat. Overworld warning, hiding or unopposed flight does not consume it.

### full turn / round lifecycle

State: PARTIAL.

Required for timed escape objectives, delayed encounter transitions, round-bound reinforcements or other lifecycle-sensitive handoff variants.

### full stateful damage pipeline

State: PARTIAL.

Required when the encounter permits authoritative damaging combat. Pass 242 must not infer ecological death from tactical damage or KO.

### status lifecycle

State: PARTIAL.

Required only when the authored encounter permits status mechanics. No blanket support is assumed.

### terrain / weather / hazards / zones / reactions

State: MIXED / PARTIAL / BLOCKING outside verified slices.

The new Java commit freezes one terrain-trap semantic payload against Python. That is strong evidence for that slice only. Visible world rain, cliffs or route geometry remain presentation-only unless a reviewed tactical mapping exists.

### move-specific behavior

State: PARTIAL.

Every Move entering a BattleSpec must be validated individually. The canonical level-5 Fletchling blueprint contains Tackle and Growl; this snapshot does not newly certify either Move beyond existing engine evidence.

### abilities

State: PARTIAL.

The canonical first Fletchling uses Big Pecks. Its tactical effect must be validated against current engine contracts before the fixture relies on it.

### items

State: PARTIAL.

World-service equipment can remain outside AutoPTU when it does not pretend to resolve a PTU Item mechanic. Tactical Items require direct implementation evidence.

### Trainer Features / perks

State: PARTIAL.

Any Trainer Feature or Edge that changes the engagement, escape, capture or tactical result requires exact evidence. Pass 242 does not assume blanket Feature coverage.

### AI legal-action infrastructure

State: VERIFIED within audited contracts.

Required for an AI-controlled wild combatant to choose among legal actions.

### AI tactical policy

State: BLOCKING as a complete family.

The rich ecological pursuit premise needs policy that can prioritize escape, guarding, separation or another ecological objective over damage optimization. Legal-action infrastructure alone does not prove that behavior.

### Minecraft / Cobblemon / Craftics adapter and playback

State: PARTIAL / BLOCKING end-to-end.

Pass 242 exposes the exact missing seams:

- convert an Ouros interaction decision into one immutable combatant manifest;
- map reviewed world facts into BattleSpec input without importing Cobblemon battle authority;
- suspend or correlate projection leases while a persistent actor is in AutoPTU;
- project semantic AutoPTU events without applying mechanics twice;
- receive the final semantic result envelope;
- re-evaluate ecological/world state from that envelope;
- rematerialize or relocate persistent actors after battle even when their original Minecraft entity no longer exists.

No live evidence proves this complete pipeline today.

## Handoff readiness verdict

The encounter-intent evaluator and deterministic handoff fixture are READY FOR OUROS WORLD-SERVICE IMPLEMENTATION.

A reduced integration can already make the critical decision:

`STAY_OVERWORLD`
`OPEN_AUTOPTU`
`USE_REDUCED_VERSION`
`BLOCK_UNSUPPORTED`

The full Minecraft-visible BattleSpec/open/playback/writeback path remains gated by adapter work and by whatever exact tactical families a selected encounter consumes.

## Reduced Sendero fixture readiness

Ready as a deterministic contract:

- observation remains overworld;
- warning remains overworld;
- unopposed flight remains overworld;
- explicit structured engagement freezes the known Fletchling plus player combatant;
- nearby actors stay outside the manifest;
- unmapped rain remains visual;
- unsupported interception chase falls back to overworld escape;
- AutoPTU KO returns as a narrow tactical fact rather than ecological death;
- event resolution occurs only after Ouros re-evaluation.

## Rich-version blockers

The pursuit/escape version remains blocked by some combination of:

- complete movement if interception/forced displacement matters;
- full lifecycle if an escape timer or round threshold matters;
- exact Move/Ability support;
- AI tactical policy for objective-aware fleeing;
- tactical terrain/hazard/reaction support if the route itself becomes mechanical;
- end-to-end Minecraft/Cobblemon/Craftics adapter/playback/writeback.

## No category promotion

The new Java semantic trap payload contract improves confidence in one terrain-trap seam only. No permanent capability family is promoted by Pass 242.
