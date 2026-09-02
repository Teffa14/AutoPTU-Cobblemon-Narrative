# Engine Readiness Snapshot — Pass 210

Status: READ-ONLY ENGINE AUDIT
Date: 2026-09-02

## Evidence inspected

Narrative base at start of pass: `7b09df560172ed0e15f72994baf90484d62297c2`.

AutoPTU-Java current head inspected: `ee794c04014f87740703bc73d5929c15360e0840`.

The latest Java commit, “Freeze forced-movement prevention traces for area and delayed hits (#327),” adds regression coverage for forced-movement prevention on authoritative multi-target/area and delayed-hit execution. The inspected diff shows a delayed push move whose target keeps its original position when an `Insectoid Utility` Trainer Feature produces a `forced_movement_block` semantic event, while damage and action/frequency state still resolve.

This is meaningful evidence inside the complete-movement and Trainer-Feature families. It does not prove the whole push/pull/knockback/interception/forced-movement family complete, and it does not prove all Trainer Features complete.

AutoPTU current head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest change remains a presentation-only Career coordinate-sync fix after viewport resize. It changes no battle authority or parity classification.

Narrative pass 210 only writes research/design/proposal material. AutoPTU-Java and AutoPTU remain read-only.

## Permanent capability audit

| Capability family | State | Pass-210 consequence |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED within audited contracts | sufficient for reduced ordinary battles using supported actions |
| base movement legality | VERIFIED within audited contracts | sufficient for ordinary supported movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | newer prevention traces strengthen a bounded path; rich courier/interception objectives still depend on unverified remainder |
| core calculations | VERIFIED within audited contracts | usable on individually supported battle paths |
| action economy / initiative | VERIFIED within audited contracts | usable on individually supported battle paths |
| full turn / round lifecycle | PARTIAL | do not build narrative truth around unaudited multi-phase scripts |
| full stateful damage pipeline | PARTIAL | use individually audited paths only |
| status lifecycle | PARTIAL | avoid complex status-driven response objectives in reduced implementation |
| terrain / weather / hazards / zones / reactions | BLOCKING as complete family | route/weather may remain world presentation/state; no invented tactical effects |
| move-specific behavior | PARTIAL | every move required by a rich encounter must be individually supported |
| abilities | PARTIAL | every Ability effect remains engine-owned and individually auditable |
| items | PARTIAL | evidence packets remain semantic world objects unless an audited battle-object/item contract exists |
| Trainer Features / perks | PARTIAL | forced-movement prevention trace is useful evidence but cannot generalize to Orders, social Features or other interrupts |
| AI legal-action infrastructure | VERIFIED within audited contracts | usable where supported action space is available |
| AI tactical policy | BLOCKING for complete family | objective-aware courier interception, escort, surrender or evidence-seeking behavior remains blocked |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING for complete target support | notice/dialogue/world-state projection can proceed; rich battle-object reconciliation cannot be assumed |

## Pass-210 encounter boundary

The proposed `Keep the Record Moving` full encounter requires all permanent capability families because its rich form can involve objective movement, escort/interception, evidence custody, tactical environment, items, Trainer Features and objective-aware AI.

The reduced `Publish, Verify, Correct` form deliberately removes those dependencies. It can use:

- Ouros-authored claim, publication and response records;
- existing NPC/location schedules and navigation;
- authenticated evidence references;
- versioned corrections;
- ordinary audited battle handoff only when ecology independently produces a supported encounter.

Minecraft/Cobblemon can render a notice surface, actors and travel. It cannot decide whether a claim is true, whether a correction is accepted, whether an evidence packet is authentic or whether an institution has authority to act.

## Current verified/partial/blocking interpretation

Verified within the bounded audited contracts:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

Partial:

- complete movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

Blocking as complete families for the rich pass-210 encounter:

- terrain/weather/hazards/zones/reactions;
- AI tactical policy.

Partial/blocking for the complete end-to-end target:

- Minecraft/Cobblemon/Craftics adapter/playback support.

## Mechanical questions opened by pass 210

- Which PTU/Kairos Skills, Edges or Trainer Features govern persuasion, evidence interpretation, verification and institutional/social interaction under the production profile.
- Whether any verified Java contract can change an opponent/allied participant's tactical intent through a non-damage social action without narrative code bypassing battle authority.
- Whether BattleSpec currently supports semantic objective objects or evidence custody strongly enough for a courier/escort scenario.
- Whether an ordinary carried document should remain entirely outside battle state until object interactions are explicitly supported.
- Whether withdrawal/disengagement results expose enough authoritative state for a route-verification scene to resume correctly afterward.
- Which exact ordinary wild moves/Abilities are safe on the current player-vs-wild path if an encounter appears during verification.

No capability family is promoted because one representative mechanic or regression exists.