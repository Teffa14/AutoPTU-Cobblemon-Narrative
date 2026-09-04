# Resource scarcity, observation and world-event integration contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 247
Canon effect: NONE

## Purpose

Connect finite resource state to ecology-driven events and imperfect knowledge while preserving the authority boundaries established in Passes 238, 240, 241 and 246.

## State flow

```text
confirmed resource transaction
-> resource ledger mutation
-> explicit population/individual pressure mutation
-> event condition evaluation
-> event truth
-> observable symptoms
-> observation/evidence
-> holder claim
-> optional intervention or natural renewal
-> resource/pressure mutation
-> hysteretic event re-evaluation
-> persistent consequence
```

Every arrow is an explicit accepted event or evaluator. No downstream layer may write upstream truth by implication.

## Required separations

Resource quantity is hidden world state. An observer may see feeding concentration, damaged substrate, empty-looking patches, changed timing, searches or displacement, but receives the authoritative quantity only through an explicitly authorized measurement surface.

Event truth and knowledge remain independent. A claim cannot open an event. Event resolution cannot silently update a holder's belief.

Resource renewal is separate from resource observation and consumption. It requires a stable transaction ID, positive quantity and idempotency protection. Renewal does not create population members and does not reset individual history.

Population abundance changes only through the Pass 238 demographic ledger.

## Hysteresis

A scarcity event may open when resource availability is low and population pressure is high. Clearing requires a distinct recovery condition and repeated evaluations. The Pass 247 fixture uses two consecutive clear evaluations only as deterministic test data; the threshold values are not canon.

If recovery fails between clear evaluations, the clear streak must reset. A resolved event retains history instead of disappearing.

## Knowledge behavior

A symptom observation can support `RESOURCE_USE`, `BEHAVIOR_PATTERN` or `THREAT_OR_DISTURBANCE` evidence. `RESOURCE_SCARCITY` is an inference unless the observer has an authorized measurement that directly supports the hidden condition.

Relays preserve source roots. Multiple relays of one observation do not raise confidence.

A holder can still believe or suspect scarcity after the resource has recovered. A later fresh observation, measurement or communication event is required to revise that state.

## Reduced encounter version

The reduced Marea slice uses the canon Fletchling population and a fixture-only forage patch. Consumption reduces resource availability. A separate pressure event raises Fletchling resource pressure. Hidden world state opens a scarcity event. An observer sees concentrated foraging and forms a low-confidence claim. The patch later renews, pressure falls and hysteresis resolves the event. Population remains unchanged throughout.

This version does not require AutoPTU. It requires persistent Ouros state, event evaluation, Pass 240 evidence storage and adapter/persistence support for visible observations.

## Rich encounter version

A future full version may show individuals expanding search radius, contesting access, withdrawing to alternate patches, guarding a micro-site, or interacting with player attempts to protect/restore a resource.

Dependency classification:

- targeting/footprints/range/LoS: REQUIRED if structured targeting or defended areas are used; currently VERIFIED within audited contracts.
- base movement legality: REQUIRED for structured movement; VERIFIED within audited contracts.
- complete movement including push/pull/knockback/interception/forced movement: REQUIRED for authored interception, displacement or forced access changes; PARTIAL.
- core calculations: REQUIRED for adopted tactical checks/damage; VERIFIED within audited contracts.
- action economy/initiative: REQUIRED for structured turns; VERIFIED within audited contracts.
- full turn/round lifecycle: REQUIRED for timed access/escort/phase objectives; PARTIAL.
- full stateful damage pipeline: REQUIRED only if damaging attacks occur; PARTIAL.
- status lifecycle: REQUIRED only if statuses occur; PARTIAL.
- terrain/weather/hazards/zones/reactions: REQUIRED if resource access is represented by tactical zones, hazards, weather or reactions; MIXED/PARTIAL/BLOCKING outside verified slices.
- move-specific behavior: validate every Move selected; family PARTIAL.
- abilities: validate every Ability selected; family PARTIAL.
- items: validate every Item selected; family PARTIAL.
- Trainer Features/perks: validate every Feature selected; family PARTIAL.
- AI legal-action infrastructure: REQUIRED for tactical wildlife; VERIFIED within audited contracts.
- AI tactical policy: REQUIRED for forage/guard/yield/flee priorities; BLOCKING as a complete family.
- Minecraft/Cobblemon/Craftics adapter/playback: REQUIRED for end-to-end projection, observation capture and tactical playback; PARTIAL/BLOCKING.

## Invariants

1. Observation never decrements or renews a resource.
2. Resource consumption/renewal never changes population abundance by itself.
3. Pressure changes require explicit scoped events.
4. Event truth derives from persistent state, not claims, dialogue or quest flags.
5. Hidden resource quantities are not exposed through ordinary sightings.
6. Duplicate relays do not create corroboration.
7. Clearing uses declared hysteresis.
8. Event resolution does not erase stale or incorrect knowledge.
9. Restart preserves accepted resource, event and epistemic history.
10. Fixture replay success does not approve the resource identity, thresholds or new species.
