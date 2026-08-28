# Engine Readiness Snapshot — Pass 95

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or setting canon.

Date: 2026-08-28

## Scope

Pass 95 adds road, bridge and detour continuity to Narrative. This snapshot classifies the tactical capabilities required by its mechanically rich encounter concepts against current live AutoPTU evidence.

Read-only engine evidence inspected:

- AutoPTU-Java current head during this pass: `39b81222af080dd5b2db9b3efdfe742b746d5f5d`
- AutoPTU current head at final live recheck before this snapshot: `1f3367f2bfd8c09280e8eff3238be13a7de91fbf`
- AutoPTU-Java README current `main`
- Pass 94 readiness snapshot
- AutoPTU-Java #255 commit contract

Narrative baseline before Pass 95 work: `2d73b89d7cb16d7b98159dae540f67951a8e985b`.

## AutoPTU-Java delta since Pass 94

The latest Java slice is #255, `Freeze intercept orchestration control flow`.

The parity contract freezes ordering in the Python `_attempt_intercept` oracle across meaningful checkpoints including candidate ordering, Intercept check, temporary-resource consumption, success branch, interceptor position commit, melee forced movement and target-anchor commit.

This is useful live evidence for one specific Intercept orchestration path.

It does not prove complete coverage for:

- every Intercept trigger/source;
- competing reactions;
- broad knockback;
- every push/pull/forced-movement source;
- terrain-triggered movement;
- environmental forced displacement;
- generalized reaction ordering;
- objective-aware tactical movement;
- end-to-end semantic battle transcript parity;
- Minecraft playback.

The Java README still lists core battle state, full damage, status controller, terrain, hazards, forced movement/reactions, hook registries, full BattleTranscript parity, AI scoring/policy and the Craftics/Cobblemon adapter among the broad unfinished families.

No permanent category is promoted by #255 alone.

## AutoPTU Python delta

The live Python head moved during Pass 95 to `1f3367f2bfd8c09280e8eff3238be13a7de91fbf`, `perf(career): defer auth chunk until after page load`.

The inspected diff delays loading the Career web authentication module until after page load/timeout and adds route-splitting tests around that behavior.

This is Career startup/performance work. It supplies no new evidence for tactical movement, damage, reactions, terrain, status, AI or adapter capability.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Representative contracts and current README evidence support the targeting family sufficiently for Narrative readiness classification. This does not imply every Move-specific targeting exception is complete.

`base movement legality`

Shift/Jump legality, movement modes, terrain-cost handling already covered by the engine project remain verified at the base-legality family level. Dynamic road/bridge effects are outside this classification.

`core calculations`

Damage-base/type/stage/accuracy/stat primitives remain verified at the established readiness level.

`action economy/initiative`

Typed action budget and deterministic initiative/ordering remain verified at the established family level.

`AI legal-action infrastructure`

The deterministic legal `BattleChoice` space remains verified as infrastructure. This is not tactical policy.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. The project now has a substantial chain covering base movement, Push/Pull slices, collision/partial-stop work, Intercept candidate discovery, eligibility/checks, geometry, position commits, melee forced-movement interaction, resource mutation and orchestration-order parity. Broad family completion still lacks general end-to-end coverage of all forced movement and reactions.

`full turn/round lifecycle`

PARTIAL. Typed phases/action budgets exist, but broad battle lifecycle/state parity remains unfinished.

`full stateful damage pipeline`

PARTIAL. Calculation primitives exist; full authoritative stateful damage behavior remains listed as incomplete.

`status lifecycle`

PARTIAL. Some status and temporary-effect behavior exists, including slices relevant to Intercept state, but the complete controller/lifecycle is not ported.

`move-specific behavior`

PARTIAL. Representative behavior is insufficient to mark the whole Move family complete.

`abilities`

PARTIAL. Representative Ability interactions are insufficient for registry-wide readiness.

`items`

PARTIAL. Representative Item interactions are insufficient for registry-wide readiness.

`Trainer Features/perks`

PARTIAL. Intercept-related Feature/perk slices do not imply full hook coverage.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for rich road encounters. The README still identifies terrain, hazards and reactions among unfinished broad engine families. A road surface, drop, unstable edge, moving bridge component, traffic lane, wind, rain, collapse area or work zone therefore has no tactical effect unless an exact rule and engine contract later verify it.

`AI tactical policy`

BLOCKING. Legal choices can be enumerated, but objective-aware policy for withdrawal, route clearing, territorial behavior, protection or avoidance is not complete.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. The authoritative adapter remains future work. Minecraft/Cobblemon may present road geometry and state but may not resolve PTU legality or outcomes.

## Pass 95 encounter readiness

### Bridge Approach Withdrawal

Intended full behavior wants:
- several withdrawal routes;
- Intercept/forced movement;
- route protection/denial;
- possible static or dynamic infrastructure zones;
- non-KO tactical policy;
- authoritative playback.

Current profile: REDUCED.

Safe reduced form:
- crossing closed before combat;
- workers, travelers and ordinary traffic removed first;
- static safe approach arena;
- no fall, water, traffic, moving mechanism or structural hazard mechanics;
- combatants selected explicitly by Ouros;
- AutoPTU resolves combat only;
- Road/Maintenance systems decide later operational state.

### Detour Wildlife Crossing

Intended full behavior wants:
- CLEAR_ROUTE/WITHDRAW-like objectives;
- territorial or escape-oriented AI;
- possible route zones;
- complete movement interactions;
- adapter/playback.

Current profile: REDUCED.

Safe reduced form:
- temporary bypass closed before battle;
- unrelated wildlife/travelers remain outside the grid;
- static nearby arena;
- no road traffic or ecological state resolved tactically;
- Conservation/Wildlife interprets post-encounter evidence;
- Road/Travel chooses later access state.

### Controlled Crossing Service Window

Intended full behavior is conditional on canon establishing a movable/scheduled crossing. It could require moving configuration, route-control objectives, reactions, environmental zones and synchronized playback.

Current profile: REDUCED / CONDITIONAL CANON.

Safe reduced form:
- freeze crossing configuration before BattleSpec;
- pause road and linked transport flow;
- clear noncombatants;
- static arena away from machinery;
- no mid-battle bridge movement;
- operational systems resume or cancel later windows after battle resolution.

## PTU/Caelo rule boundary for roads

PTU 1.05 supports `Overland` movement on dry land and tactical Shift positioning. This gives no permission to create an overworld road physics or vehicle system.

Pass 95 therefore leaves unresolved:

- vehicle movement statistics;
- bridge capacity/load rules;
- traffic collisions;
- braking;
- road-speed modifiers;
- structural HP/damage;
- tactical falling from bridge edges;
- wet/slick road penalties;
- dynamic traffic hazards;
- engineering/repair checks;
- universal mount/riding rules;
- road-work Pokémon capabilities.

The existing project source inventory confirms Caelo can author location-specific environmental mechanical identity. No road-specific universal Caelo rule has been extracted into current Narrative evidence. A future exact source extraction may add a local effect, but Narrative must not pre-author one.

## Minecraft/Cobblemon authority consequences

The binding `cobblemon-runtime-authority-boundary.md` applies directly.

Minecraft/Cobblemon can safely contribute presentation candidates such as road/bridge blocks, barriers, signs, lights, weather visuals, particles, sounds, Pokémon entities/models/poses/cries, map UI, coordinates, entity tracking and network synchronization, subject to concrete API review.

Useful data becomes `ADAPTER_REQUIRED` when it affects authoritative world or tactical interpretation. Examples include mapping block geometry into reviewed AutoPTU cells, projecting road closure state into physical barriers and maintaining stable segment identifiers.

Minecraft/Cobblemon must never decide:
- who becomes a combatant because they are nearby;
- tactical HP/status/position;
- whether a collision causes PTU damage;
- whether a moving block pushes a combatant;
- whether rain changes Accuracy;
- whether a bridge edge causes a fall;
- whether a route obstruction creates a battle hazard;
- whether a redstone gate means the authoritative road is open;
- battle result or reopening state.

Authority direction remains:

`Ouros world/road state -> explicit encounter composition -> AutoPTU authoritative battle -> adapter -> Minecraft/Cobblemon presentation`

## Readiness conclusion

Pass 95 requires no promotion to ship its noncombat continuity, detours, histories, investigations and reduced encounters.

The road/crossing world-state layer can advance now because access, restrictions, detours, notices, repair references and verification are persistent narrative facts rather than combat mechanics.

Rich tactical versions stay blocked primarily on the same three broad gaps as Pass 94: terrain/weather/hazards/zones/reactions, AI tactical policy and Minecraft/Cobblemon/Craftics adapter/playback. Complete movement remains PARTIAL despite genuine Intercept progress.
