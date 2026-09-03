# Engine readiness snapshot — pass 216

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02

## Scope

This snapshot records the engine dependencies exposed by pass 216 temporal-ecology concepts. It does not modify AutoPTU-Java or AutoPTU and does not promote a capability family from one representative implementation.

Narrative concept under review: `Dusk Crossing Window` with reduced form `Observe, Return, Compare`.

## Live repository evidence

### AutoPTU-Java

Read-only head inspected for this pass:

`86aca6c86e5088bc58b8d5ffb688986693b741c7`

Head commit: `Emit forced-movement Ability prevention semantics (#328)`.

The current head adds a generic semantic `AbilityEvent`, preserves ability provenance and emits authoritative semantic events for verified forced-movement prevention cases. This is useful adapter/playback evidence because presentation can receive a resolved Ability consequence instead of reproducing the rule.

This evidence does not establish complete push/pull/knockback/interception/forced movement. It also does not prove the entire Ability catalogue. Complete movement and abilities therefore remain partial families.

### AutoPTU

Read-only head inspected for this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Head commit: `Career: keep battle coordinates synced after viewport resize (#237)`.

The commit explicitly describes itself as presentation-only and states that battle rules/outcomes do not change. It improves rendering synchronization but supplies no new gameplay authority for this pass.

## Capability-family status carried from audited project evidence

`VERIFIED` here means verified inside existing audited contracts, not globally complete for every possible mechanic. Any newly invoked rule still needs its own contract/source check.

| Permanent family | Pass-216 status | Temporal-ecology relevance |
| --- | --- | --- |
| targeting / footprints / range / LoS | VERIFIED in audited contracts | Needed if approach, observation or detection uses authoritative spatial relationships. Low-light semantics are not separately verified by this label. |
| base movement legality | VERIFIED in audited contracts | Supports normal approach/withdrawal/traversal. |
| complete movement incl. push/pull/knockback/interception/forced movement | PARTIAL | Needed only for rich containment/interception/forced-displacement variants. #328 adds prevention semantics for bounded cases, not family completion. |
| core calculations | VERIFIED in audited contracts | Can host already-verified calculations. It does not authorize invented time-of-day modifiers. |
| action economy / initiative | VERIFIED in audited contracts | Applies once a structured action/battle sequence begins. |
| full turn/round lifecycle | PARTIAL | Needed for complete structured encounter execution. |
| full stateful damage pipeline | PARTIAL | Needed only when combat damage is part of the encounter. |
| status lifecycle | PARTIAL | Needed for control/capture tactics that use Status Afflictions. |
| terrain/weather/hazards/zones/reactions | BLOCKING for concepts that need the complete family | Pass 216's reduced form deliberately avoids requiring this family. Dusk itself is not encoded as fake weather/terrain. |
| move-specific behavior | PARTIAL | Required when a Move changes detection, movement, capture/control or battle state. |
| abilities | PARTIAL | #328 improves a bounded Ability semantic path but does not prove catalogue completeness. |
| items | PARTIAL | Required for mechanically meaningful Balls/tools/items. |
| Trainer Features/perks | PARTIAL | Required for verified Features/Edges affecting observation, approach, restraint or capture. |
| AI legal-action infrastructure | VERIFIED in audited contracts | Required before wild tactical policy can choose an action. |
| AI tactical policy | BLOCKING as complete autonomous tactical policy | Species/context/intent architecture can proceed, but competent action choice across the full ruleset remains incomplete. |
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING end-to-end | Must project authoritative time/presence/semantic results without becoming battle or ecology authority. |

## New non-battle authority exposed by pass 216

Temporal ecology also exposes a world-runtime contract that is not one of the permanent battle families and must not be mistaken for a new battle category.

Ouros needs server-authoritative handling for:

- world time used by narrative/ecology state;
- persistence across unload/reload;
- multiplayer consistency;
- population activity opportunity;
- persistent-individual location/availability;
- human-traffic context;
- observation timestamp/effort/provenance.

Minecraft can supply/present clock and world-position observations, but client/local entity state cannot decide that a canonical Pokémon exists, moved, became capturable or left the ecosystem.

## Full concept dependency trace

`Dusk Crossing Window` in its richest intended form can touch all 16 permanent families if the Trainer turns observation into a tactical containment/capture encounter. The dependency is conditional rather than automatic.

Time-window observation alone needs no damage pipeline, Status lifecycle, forced movement or reaction system. Those families activate only when a selected tactic truly uses them.

This distinction is important for implementation planning: narrative/world-state work can ship before the tactical families are complete without reducing the premise.

## Reduced-form readiness

`Observe, Return, Compare` can proceed with a narrower contract:

```text
server-authoritative world time
+ site identity
+ authoritative population/individual state
+ observation provenance
+ normal world traversal
+ basic wild behavior intent/playback where already supported
-> observation record
-> later comparison
```

If a normal battle begins, battle authority transfers through the existing canonical blueprint/BattleSpec path. No missing PTU mechanic is recreated in the adapter.

The reduced form should explicitly reject:

- client-clock spawn authority;
- despawn = canonical departure;
- darkness = invented accuracy/LoS penalty;
- time-of-day = invented capture bonus;
- off-screen simulated combat;
- fake trapping/interception/status effects;
- AI decisions that require unavailable tactical policy.

## PTU/Caelo/Kairos questions for the next audit

Pass 216 does not assign mechanical effects to time of day. The next rules-source audit should locate exact authority, if any, for low-light visibility/perception, Stealth/detection, Survival/Intuition field observation, capture timing/range/modifiers, Features/Edges affecting approach and any relevant Caelo/Kairos overrides.

The first Fletchling canon already records supplied Caelo material as comparative provenance for territorial/diurnal behavior. That evidence can justify further research, but exact active hours and mechanical modifiers remain unresolved until explicitly approved.

## Readiness conclusion

Temporal ecology itself is not blocked by incomplete battle rules. A useful first implementation can be world-state and observation driven.

The rich tactical version remains constrained by complete movement, lifecycle, damage/status where invoked, Move/Ability/Item/Feature coverage, AI tactical policy and end-to-end adapter support. Terrain/weather/hazards/zones/reactions should only become a blocker when an authored scene actually needs those mechanics.