# Engine readiness snapshot — Pass 147

Status: implementation-facing evidence snapshot for narrative design. AutoPTU-Java and AutoPTU are read-only in this task.

## Live evidence inspected

AutoPTU-Java head inspected: `d829224655f057d19a7470a0bc5cfa1f0bdefeda` — `Freeze Sway pre-damage reaction contract (#175)`.

Recent sequence after Pass 146:
- `7ab7243f186e710a4c8294b045517f1483fcb5f1` — Perception Errata pre-damage reaction;
- `5bb41ed8d137e3067258d38e9dd04b2cf0840750` — Parry pre-damage reaction;
- `d829224655f057d19a7470a0bc5cfa1f0bdefeda` — Sway pre-damage reaction contract.

The Sway contract verifies a narrow but sophisticated reaction path including melee/non-status gating, standard-action spend, once-use state, recursive redirect protection, redirecting the attacker into its own move resolution, selecting a neighboring push destination under bounds/blocker/occupancy checks, emitting a push event and cancelling the original hit. The commit freezes this behavior against the Python oracle; it does not establish generic forced movement/reaction completeness.

AutoPTU-Java README still explicitly lists as unfinished:
- core combatant/grid battle state;
- full damage pipeline and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python head inspected from current commits: `7605265f2548a3967b2de3eb00cc0db33b0e9303`. Recent work is Career persistence recovery for malformed Pokémon containers and related save-state resilience; it does not justify a tactical capability promotion.

Additional PTU-runtime evidence relevant to Pass 147:
- `reports/trainer_runtime_coverage.md` lists 950 Trainer entries and 729 missing runtime mappings at the inspected Python head;
- `Paleontologist` is explicitly present but marked `missing_runtime_mapping`.

Therefore narrative fossil/paleontology rules must not assume that the Paleontologist mechanical concept executes in AutoPTU today.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Java README marks range, areas, footprints, target anchors and LoS complete. Recent multi-target and reaction slices continue deriving geometry from authoritative state.

`base movement legality`

Java README marks Shift and Jump legality complete for the listed Overland/Swim/Sky, terrain-cost, blocker, Wallrunner, sprint and landing-fit boundaries.

`core calculations`

Damage Base/type tables, stages, accuracy primitives, weather DB primitive, crit probability, Burn, modifiers, rounding and combat-stat resolution are ported primitives. This does not imply the full damage pipeline is complete.

`action economy/initiative`

Typed turn flow/action budget, initiative ordering, Trick Room/League ordering and declaration ordering remain verified. Recent reaction slices consume actions only under their exact contracts.

`AI legal-action infrastructure`

Legal action-space enumeration exists for Shift, direct targets, SELF/FIELD, tile AoE, footprints, LoS and action-budget filtering. This remains legality infrastructure rather than tactical policy.

### PARTIAL

`full turn/round lifecycle`

Many round-start, delayed-hit, temporary-state and reaction-order contracts exist, but full lifecycle parity is not declared complete.

`full stateful damage pipeline`

Core calculations and multiple Move-resolution paths exist, but Java README still lists full damage resolution as unfinished.

`status lifecycle`

Application/removal/prevention contracts exist for representative cases. Full status controller remains incomplete.

`move-specific behavior`

Delayed hits, area/multi-target execution and representative interaction paths exist. The Move catalog is not complete.

`abilities`

A growing set of Ability prevention/reaction hooks has parity evidence. Full Ability registry/catalog is incomplete.

`items`

Some item-related boundaries exist in accumulated evidence. Complete item hooks are not declared complete.

`Trainer Features/perks`

Generic transaction infrastructure and representative effects exist, but many mappings remain missing. `Paleontologist` specifically remains `missing_runtime_mapping` in Python coverage evidence.

### BLOCKING AS COMPLETE FAMILIES

`complete movement including push/pull/knockback/interception/forced movement`

Sway now freezes a specific one-tile neighboring push-selection/event contract after a reaction. Earlier slices include reaction movement and Push/Pull instruction parsing. The README still lists forced movement unfinished. Do not generalize Sway into generic Push/Pull/knockback/interception/collision support.

`terrain/weather/hazards/zones/reactions`

Several reaction paths are increasingly well-specified, but the README still lists reactions, terrain and hazards as unfinished. The family remains blocking for generic dynamic-environment or arbitrary-reaction encounter design.

`AI tactical policy`

Legal choices exist. Scoring/policy remains explicitly unfinished.

`Minecraft/Cobblemon/Craftics adapter/playback support`

The adapter is not complete and remains intentionally downstream of a parity-safe Java core.

## Pass 147 encounter dependencies

### Roadcut Fossil Rescue — FULL

Required:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING for workers/wildlife crossing or being redirected through threatened space;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT_TECHNICIAN`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING only if unstable rock, collapse, traffic lanes or falling debris become tactical mechanics.

Reduced version works sooner because road closure, worker/wildlife movement, documentation and stabilization occur in world state. If combat remains, AutoPTU receives a static legal arena away from the fossil face.

### Trackway Protection at Low Water — FULL

Required:
- base movement legality — VERIFIED;
- complete movement — BLOCKING for `CROSS`, interception or protected-route objectives;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING;
- environment family — BLOCKING only if water-level changes, slippery surfaces or fragile-ground exclusions are mechanically active.

Reduced version resolves rerouting and trackway documentation outside battle and uses AutoPTU only for a separate static confrontation.

### Preparation Lab Emergency — FULL

Required:
- targeting/LoS — VERIFIED if combat occurs;
- base movement — VERIFIED;
- complete movement — BLOCKING if staff/equipment evacuation is tactical;
- AI tactical policy — BLOCKING for `EVACUATE`, `PROTECT_STAFF`, `CLEAR_ROUTE`;
- adapter/playback — BLOCKING;
- environment family — BLOCKING if dust, debris, electrical/equipment failures or unstable supports gain tactical behavior.

Reduced version powers equipment down and secures the specimen first. Staff leave through world state. AutoPTU gets an adjacent static arena.

### Restoration Authorization Review

No battle dependency by default.

Primary blockers are world-state/canon/rules authority:
- restoration legality and procedure;
- PTU/Caelo Fossil rules;
- Pokémon Agency handoff;
- Research Ethics authorization;
- custody and specimen state.

## Why Sway does not promote complete movement/reactions

The live Sway contract is meaningful evidence. It proves that the port can freeze a specific reaction containing redirect logic and a constrained push destination/event under the Python oracle.

It still does not prove:
- generic Push execution for arbitrary Moves/Features;
- Pull;
- knockback distance chains;
- collision resolution;
- interception;
- movement through hazards/zones;
- simultaneous forced movement;
- objective-aware movement;
- generic reaction discovery/dispatch for the full catalog;
- AI policy capable of choosing ecological or rescue objectives.

Pass 147 therefore keeps both `complete movement` and `terrain/weather/hazards/zones/reactions` blocking as full families.

## Paleontology implementation blockers outside battle core

`FOSSIL_LOCALITY_STATE`
Persistent locality identity and exposure revisions.

`STRATIGRAPHIC_CONTEXT_STATE`
Measured sections, layer identity, relative/absolute dating claims and correlations.

`FOSSIL_OCCURRENCE_LEDGER`
In-situ body/trace fossil observations before extraction.

`SPECIMEN_IDENTITY_AND_PREPARATION_HISTORY`
Persistent specimen through field jacket, preparation, imaging, fragments and collection handoff.

`TAPHONOMY_EVIDENCE_GRAPH`
Observations, alternative hypotheses and confidence.

`FOSSIL_ASSEMBLAGE_SAMPLING_STATE`
Assemblage summaries with preservation/sampling bias rather than direct ancient population counts.

`PALEOENVIRONMENT_INTERPRETATION_STATE`
Ancient-environment claims connected to evidence and revisions.

`FOSSIL_TO_MUSEUM_HANDOFF`
Accession/conservation while preserving field provenance.

`FOSSIL_TO_LIVING_POKEMON_HANDOFF`
Only if restoration is canon/rules-authorized.

`PALEONTOLOGY_TO_MINECRAFT_PROJECTION`
No fossil respawns, context loss or block-authoritative rules.

## PTU/Caelo unresolved

Project evidence confirms the Paleontologist concept exists in source data but currently lacks runtime mapping. This pass did not recover a reliable Caelo-specific source defining fossil discovery, excavation, restoration, restored Pokémon generation or Paleontologist modifications.

Super PTU Online Helper was not exposed as an invocable capability.

Do not add until verified:
- fossil-search DCs;
- Pokémon Education/Survival thresholds;
- quarry drop rates;
- Paleontologist mechanical benefits;
- restoration timing/cost/success;
- restored Pokémon species/Nature/Ability/Level/Moves;
- custody/ownership produced by restoration;
- excavation damage or tool bonuses;
- prehistoric battle traits inferred from fossil morphology.