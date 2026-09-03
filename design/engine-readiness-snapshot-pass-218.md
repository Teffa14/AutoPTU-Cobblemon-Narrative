# Engine readiness snapshot — pass 218

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-03

## Scope

This snapshot records dependencies exposed by pass 218 seasonal migration, corridor and stopover concepts. AutoPTU-Java and AutoPTU were inspected read-only. No capability family is promoted from one representative mechanic.

Narrative concept under review: `Seasonal Passage at the Narrow Shelf`, with reduced form `Watch, Yield, Record`.

## Live repository evidence

### AutoPTU-Java

Read-only head inspected:

`a4df700c4a9099448d5efbfccfd56214bc1f704c`

Head commit: `Freeze generic tile-entry trap contract (#329)`.

The current head remains the bounded authoritative tile-entry trap resolver already assessed in pass 217. It covers trap-layer/entry/block/event/status-consequence semantics with parity against the pinned Python oracle. It does not add group migration, participant insertion, complete interception, arbitrary zones, weather phases, autonomous passage tactics or broad environmental mutation.

The previous #328 Ability-event/forced-movement-prevention evidence also remains bounded. It does not complete movement or the Ability catalogue.

### AutoPTU

Read-only head inspected:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

The commit explicitly remains presentation-only and changes no battle rules/outcomes. It adds no migration-specific gameplay authority.

## Permanent capability-family status

`VERIFIED` means verified inside existing audited contracts, not global completeness for every possible rule.

| Permanent family | Pass-218 status | Seasonal-passage relevance |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED in audited contracts | Needed for route occupancy, observation distance and structured spatial interaction. World/battle geometry mapping still needs adapter integration. |
| base movement legality | VERIFIED in audited contracts | Supports ordinary approach, yielding, withdrawal and traversal. |
| complete movement incl. push/pull/knockback/interception/forced movement | PARTIAL | Needed only when blocking/interception/displacement becomes mechanical. Existing prevention semantics do not complete the family. |
| core calculations | VERIFIED in audited contracts | Can host already-audited calculations; migration itself creates no modifier. |
| action economy / initiative | VERIFIED in audited contracts | Applies once a passage scene becomes structured. |
| full turn/round lifecycle | PARTIAL | Needed for complete structured multi-actor encounters. |
| full stateful damage pipeline | PARTIAL | Needed only when real combat/injury occurs. |
| status lifecycle | PARTIAL | Needed when Status is used to control/capture. Tile-trap status consequences do not complete the lifecycle. |
| terrain/weather/hazards/zones/reactions | PARTIAL / BLOCKING outside bounded contracts | #329 covers a bounded tile-entry trap path. Passage/weather/zone/reaction semantics remain incomplete unless independently verified. |
| move-specific behavior | PARTIAL | Needed for Move-based escape, control, concealment, support or terrain effects. |
| abilities | PARTIAL | Bounded Ability semantics do not prove full catalogue coverage. |
| items | PARTIAL | Balls/tools require individual mechanical coverage. |
| Trainer Features/perks | PARTIAL | Observation/approach/capture/control changes require exact Feature/Edge coverage. |
| AI legal-action infrastructure | VERIFIED in audited contracts | Necessary before autonomous wild actors choose among legal actions. |
| AI tactical policy | BLOCKING as complete autonomous policy | Rich passage scenes need independent actors choosing tolerate, withdraw, warn, evade, protect, obstruct or engage according to species/context/capabilities. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING end-to-end | Needed for generic population projection, persistent identity, movement cues and semantic battle/world playback. |

## Migration is primarily world-runtime state

The passage system should not become a seventeenth battle family. It needs persistent world authority for passage identity, population reference, route segments, stopover use, authored seasonal/window state, observation provenance, access decisions and multiplayer/unload continuity.

Cobblemon owns ordinary natural spawning where its native spawn conditions/rules can express the approved availability. Ouros owns provenance-backed passage semantics, population/canon gates, persistent identity and consequences. AutoPTU becomes authoritative when PTU mechanics are invoked.

Pass 216 verified native temporal spawn support but did not prove a first-class arbitrary calendar-season condition for the deployed Cobblemon version. Pass 218 therefore leaves exact seasonal scheduling as an adapter/world-runtime verification item rather than inventing a parallel spawn scheduler.

## Full concept dependency trace

`Seasonal Passage at the Narrow Shelf` does not automatically require all permanent families. The observational core uses world/runtime state, ordinary movement, actor projection and provenance. Tactical families become dependencies only after the player or another actor invokes mechanics that use them.

A simple choice to yield the path needs base traversal and world-state consequences. A capture attempt adds Items/capture rules and potentially Features/Status/Move behavior. Physically cutting off an escape can add complete movement/interception. Weather matters only if an authored weather mechanic actually changes the encounter. A tile-entry trap is available only when the scene contains a trap matching the bounded #329 contract.

## Reduced-form readiness

`Watch, Yield, Record` can proceed with a narrow contract:

```text
provenance-backed passage episode
+ route/stopover identity
+ authoritative world time/window state
+ Cobblemon generic population projection where natively representable
+ Ouros persistent-identity/population gates
+ normal world traversal
+ observation timestamp/direction/count methodology
+ persistent access/consequence records
+ Minecraft/Cobblemon presentation
-> passage observation and later comparison
```

If a normal battle begins, participants must enter through existing authoritative BattleSpec paths. The reduced version does not fabricate group initiative, migration bonuses, forced movement, weather penalties, Status control, reactions, tactical swarm AI or mid-battle participant insertion.

## Specific blockers exposed by the rich version

Multi-actor autonomous passage intensifies two known blockers without creating new categories.

First, AI tactical policy must eventually reason from species/population behavior, current migration priority, individual state/capabilities, Trainer actions and legal options. It cannot simply assign one aggro state to the whole visible group.

Second, adding a previously non-participating wild responder into an already-running battle remains unverified/blocking. That depends on lifecycle, initiative, participant ownership, legal actions, tactical policy and adapter playback. A passage signal or alarm cannot silently insert another battler.

## PTU/Caelo/Kairos verification queue

Before mechanically rich passage encounters are approved, audit exact project-source authority for wild-interaction Skills/Edges/Features, perception/Stealth, capture action/range/modifiers, movement capabilities, trapping/restraint, interception/forced movement, Status effects used for capture/control, relevant Move/Ability/Item behavior, weather if invoked and Caelo/Kairos overrides.

Group movement must not be used as evidence for `Pack Mon`, shared initiative or a collective combat controller.

## Readiness conclusion

Pass 218 can advance immediately as persistent ecology, route policy and observation gameplay. The current engine evidence supports normal traversal and audited spatial/legal-action foundations while rich tactical interference remains constrained by complete movement, lifecycle, status/damage where invoked, per-Move/Ability/Item/Feature coverage, broader hazard/zone/reaction support, AI tactical policy and end-to-end adapter integration.

No live engine evidence in this run justifies promoting a permanent capability family beyond pass 217.