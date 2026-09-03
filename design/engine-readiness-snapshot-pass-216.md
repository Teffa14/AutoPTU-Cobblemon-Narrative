# Engine readiness snapshot — pass 216

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Implementation correction: 2026-09-03 — native Cobblemon temporal spawning verified

## Scope

This snapshot records the engine dependencies exposed by pass 216 temporal-ecology concepts. It does not modify AutoPTU-Java or AutoPTU and does not promote a battle capability family from one representative implementation.

Narrative concept under review: `Dusk Crossing Window` with reduced form `Observe, Return, Compare`.

The pass originally treated part of temporal spawn availability as a new Ouros world-runtime need. Current Cobblemon documentation confirms that ordinary natural spawn timing/filtering/weighting already exists natively. This snapshot corrects that boundary.

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

### Cobblemon native spawn capability

Current public Cobblemon documentation verifies the following platform capabilities:

- `spawn_pool_world` controls natural Pokémon spawning and supports time-range conditions combined with biome/block/moon/other conditions;
- Spawn Rules can filter or reweight spawn details against current world context;
- Pokémon behaviour time ranges support named periods such as `day`, `night`, `dawn` and `dusk` for supported behaviour properties;
- the Cobblemon config includes `savePokemonToWorld`, allowing Pokémon persistence across chunk/world reload when enabled.

Sources:
- https://wiki.cobblemon.com/index.php/Spawn_Pool_World
- https://wiki.cobblemon.com/index.php/Spawn_Rules
- https://wiki.cobblemon.com/index.php/Pok%C3%A9mon/Behaviour
- https://wiki.cobblemon.com/index.php/Config

This verifies platform support, not the project's complete Ouros integration contract. In particular, persistent canonical identity, duplicate prevention and reconciliation with generic natural spawning remain project work.

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
| Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL end-to-end | Native Cobblemon temporal spawn support is VERIFIED as a platform capability. Ouros population/canon gating, persistent-identity reconciliation and semantic playback remain incomplete end-to-end. |

## Corrected non-battle authority split

Pass 216 does not require Ouros to invent a second temporal spawn engine.

### Minecraft/Cobblemon owns

- server world time used by natural spawning;
- ordinary spawn eligibility by time and other native conditions;
- ordinary spawn weighting/filtering through Cobblemon spawn data/Spawn Rules;
- physical world entity projection and supported persistence behaviour.

### Ouros owns

- whether an authored population exists in canon/world state;
- provenance and approval for regional ecology rules;
- persistent individual identity/history;
- duplicate prevention where a known individual overlaps generic species spawning;
- narrative observation records and methodology;
- disturbance/social context not represented by a simple native spawn condition;
- behavior/tolerance intent once a Pokémon is actually present.

### AutoPTU owns

- PTU legality;
- Skills/Features/Edges when mechanically invoked;
- capture/battle calculations;
- movement/control/status/damage mechanics;
- structured tactical resolution.

The Minecraft/Cobblemon layer may supply time, light, weather, biome and spawn context without becoming battle-state authority.

## Integration work still exposed by pass 216

Even with native spawn support, several project-specific contracts remain unresolved:

- map canon-approved population profiles to Cobblemon datapack spawn conditions without silently changing lore;
- keep source/provenance links from an authored population rule to the corresponding datapack entry;
- prevent a persistent canonical individual from being duplicated by generic natural spawning;
- reconcile Cobblemon save/despawn/unload behavior with Ouros persistent-individual availability;
- preserve multiplayer consistency for observations and persistent identities;
- distinguish `no entity spawned/visible` from ecological absence;
- decide how dynamic Ouros events should temporarily alter a native spawn rule, if such alteration is needed, without implementing a competing scheduler.

These are adapter/world-state integration tasks, not missing PTU battle rules.

## Full concept dependency trace

`Dusk Crossing Window` in its richest intended form can touch all 16 permanent families if the Trainer turns observation into a tactical containment/capture encounter. The dependency is conditional rather than automatic.

Time-window observation alone needs no damage pipeline, Status lifecycle, forced movement or reaction system. Generic temporal spawn eligibility also does not require a new Ouros scheduler because Cobblemon supplies that platform feature.

This distinction is important for implementation planning: ecology/spawn configuration and narrative observation work can ship before the tactical families are complete without reducing the premise.

## Reduced-form readiness

`Observe, Return, Compare` can proceed with a narrower contract:

```text
Minecraft server world time/context
+ native Cobblemon spawn conditions for generic populations
+ Ouros site/population/canon state
+ Ouros persistent-individual identity where applicable
+ observation provenance
+ normal world traversal
+ basic wild behavior intent/playback where supported
-> observation record
-> later comparison
```

If a normal battle begins, battle authority transfers through the existing canonical blueprint/BattleSpec path. No missing PTU mechanic is recreated in the adapter.

The reduced form should explicitly reject:

- a duplicate Ouros day/night spawn scheduler;
- client-clock spawn authority;
- generic spawn condition = permission to clone a persistent individual;
- despawn/failure-to-spawn = canonical departure or ecological absence;
- darkness = invented accuracy/LoS penalty;
- time-of-day = invented capture bonus;
- off-screen simulated combat;
- fake trapping/interception/status effects;
- AI decisions that require unavailable tactical policy.

## PTU/Caelo/Kairos questions for the next audit

Pass 216 does not assign mechanical effects to time of day. The next rules-source audit should locate exact authority, if any, for low-light visibility/perception, Stealth/detection, Survival/Intuition field observation, capture timing/range/modifiers, Features/Edges affecting approach and any relevant Caelo/Kairos overrides.

The first Fletchling canon already records supplied Caelo material as comparative provenance for territorial/diurnal behavior. That evidence can justify further research, but exact active hours and mechanical modifiers remain unresolved until explicitly approved.

## Readiness conclusion

Temporal ecology itself is less blocked than the original pass-216 snapshot implied. Cobblemon already supplies the ordinary temporal spawn machinery. The next implementation work should integrate with that machinery, not duplicate it.

A useful first implementation can therefore combine Cobblemon-native temporal spawning for generic populations with Ouros population provenance, persistent identity and observation state.

The rich tactical version remains constrained by complete movement, lifecycle, damage/status where invoked, Move/Ability/Item/Feature coverage, AI tactical policy and end-to-end adapter support. Terrain/weather/hazards/zones/reactions should only become a blocker when an authored scene actually needs those mechanics.