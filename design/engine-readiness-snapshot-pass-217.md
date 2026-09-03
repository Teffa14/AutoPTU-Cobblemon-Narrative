# Engine readiness snapshot — pass 217

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-03

## Scope

This snapshot records engine dependencies exposed by the pass-217 multi-solution environmental-obstacle concepts. AutoPTU-Java and AutoPTU were inspected read-only. No capability family is promoted from a representative mechanic.

Narrative concept under review: `Seasonal Crossing Clearance Window`, with reduced form `Survey, Choose, Traverse`.

## Live repository evidence

### AutoPTU-Java

Read-only head inspected for this pass:

`a4df700c4a9099448d5efbfccfd56214bc1f704c`

Head commit: `Freeze generic tile-entry trap contract (#329)`.

The new head adds an authoritative `TileEntryTrapResolution` path and parity coverage against a pinned Python oracle. The commit covers bounded tile-entry trap semantics including trap layers, actor entry context, blocking behavior, event descriptions and status-consequence payload/order. Its source comment explicitly places resolution in the authoritative engine and leaves adapters to render the result.

This is meaningful evidence for one hazard subfamily. It does not establish arbitrary environmental hazards, dynamic terrain mutation, weather, zones, reactions, falling/collapse rules, moving world objects, push/pull completeness or every status consequence. `terrain/weather/hazards/zones/reactions` therefore improves from the prior snapshot only in evidence depth; it remains incomplete and blocking for concepts outside the frozen tile-entry contract.

The prior #328 evidence for semantic Ability-based forced-movement prevention also remains bounded and does not complete the Ability catalogue or complete movement.

### AutoPTU

Read-only head inspected for this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

This remains presentation-only and states that battle rules/outcomes do not change. It adds no new authority for environmental obstacle resolution.

## Permanent capability-family status

`VERIFIED` below means verified inside the project's existing audited contracts, not universal completeness for every rule or new environmental use.

| Permanent family | Pass-217 status | Relevance to multi-solution traversal |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED in audited contracts | Useful for actor-to-space targeting and inspection. World-object targeting still needs an adapter/world contract. |
| base movement legality | VERIFIED in audited contracts | Supports ordinary legal traversal and detours. |
| complete movement incl. push/pull/knockback/interception/forced movement | PARTIAL | Required only when a solution truly displaces actors/objects or invokes interception. Existing prevention semantics do not complete the family. |
| core calculations | VERIFIED in audited contracts | Can host source-verified Skill/calculation paths; does not authorize invented obstacle DCs. |
| action economy / initiative | VERIFIED in audited contracts | Applies if clearance/escape becomes structured. |
| full turn/round lifecycle | PARTIAL | Needed for a complete structured clearance encounter. |
| full stateful damage pipeline | PARTIAL | Needed for real fall/collapse/attack damage. |
| status lifecycle | PARTIAL | #329 verifies bounded status consequences from tile traps, not the entire lifecycle. |
| terrain/weather/hazards/zones/reactions | PARTIAL / BLOCKING outside bounded contracts | #329 verifies a generic tile-entry trap path. Other hazard/terrain/zone/reaction behavior remains unverified or incomplete. |
| move-specific behavior | PARTIAL | Environmental Move solutions require exact per-Move contracts. |
| abilities | PARTIAL | Prior forced-movement-prevention semantics are bounded evidence only. |
| items | PARTIAL | Tools/items need individual mechanical coverage. |
| Trainer Features/perks | PARTIAL | Traversal modifiers/substitutions require exact Feature/Edge coverage. |
| AI legal-action infrastructure | VERIFIED in audited contracts | Can constrain autonomous actors to legal options when integrated. |
| AI tactical policy | BLOCKING as a complete autonomous policy | Needed only when autonomous helpers must prioritize among competing objectives. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING end-to-end | Must project obstacle state and authorized transitions without becoming PTU authority. |

## New evidence from #329

Pass 217 should record #329 narrowly because environmental exploration is precisely where over-generalization would be tempting.

The verified statement is: AutoPTU-Java now contains a parity-gated authoritative resolver for a generic class of tile-local traps triggered by entry, with bounded block/status/event semantics.

The following statements are not verified by #329:

- every Minecraft block can become an AutoPTU hazard;
- every hazardous terrain type is implemented;
- entering/leaving arbitrary zones is covered;
- reactions or attacks of opportunity tied to environmental triggers are complete;
- a collapsing bridge or falling rock has a full damage/lifecycle contract;
- pushing a boulder uses the same resolver;
- Minecraft collision may determine trap legality;
- the whole status lifecycle is complete.

## Obstacle authority outside battle

Pass 217 exposes a world-runtime contract rather than a seventeenth battle family.

The narrative/world layer needs authoritative persistent records for obstacle identity/state, access effects, actor-specific bypass, public-route status, evidence that may be destroyed by clearance, and the transition that actually changed the environment.

Minecraft/Cobblemon/Craftics can implement physical geometry, collision, animation, native traversal affordances and block/entity presentation where appropriate. For mechanically meaningful PTU actions, the adapter sends the request/context to authority and applies the returned result. It must not convert a block break, jump animation, entity push or redstone signal into PTU success on its own.

## Full concept dependency trace

`Seasonal Crossing Clearance Window` can touch most permanent families when the player attempts a mechanically rich solution, but each dependency is conditional.

A simple detour needs world-state authority and base movement. A Trainer climbing personally may need an exact Skill/capability calculation. Moving an object may require a different rules contract. A tile trap invokes the bounded hazard path only if the authored scene actually contains such a trap. A Move-based solution activates move-specific behavior. Autonomous Pokémon assistance can activate AI legal actions/policy.

No single obstacle should be authored to require all families merely to justify complexity.

## Reduced-form readiness

`Survey, Choose, Traverse` can ship earlier with a narrow contract:

```text
authoritative obstacle record
+ authoritative route/access state
+ physical observation/provenance
+ authored alternate route or wait/report choice
+ verified ordinary base traversal
+ persistent world-state transition when one occurs
+ Minecraft/Cobblemon presentation
-> outcome and consequences
```

The reduced form rejects arbitrary environmental DCs, unverified object-force mechanics, fake difficult terrain, collision-authored damage, improvised HM equivalents, automatic public reopening and off-screen simulated clearance.

## PTU/Caelo/Kairos verification queue

Before richer variants are approved, audit exact project sources for Athletics/Acrobatics traversal; Survival and terrain uses; Pokémon Overland/Sky/Swim/Jump and special movement capabilities; Power/lifting/carrying/pushing if present; Naturewalk or terrain-oriented traits; Features/Edges that modify or substitute traversal checks; environmental Move/Ability use; cooperative checks; falling/collision consequences; and any Caelo/Kairos overrides.

Public PTU references demonstrate that Trainer physical skills and terrain Features exist, but project-source provenance must decide exact mechanics.

## Readiness conclusion

Pass 217 can proceed narratively and in reduced world-state form without waiting for the entire battle engine. The new Java tile-entry trap contract is a concrete improvement for bounded hazard scenes. Rich environmental clearance remains constrained by exact traversal rules, object interaction, complete movement where invoked, Move/Ability/Item/Feature coverage, hazard coverage beyond #329, autonomous tactical policy and end-to-end adapter/world mutation support.