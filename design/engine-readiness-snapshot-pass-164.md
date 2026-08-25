# Engine Readiness Snapshot — Pass 164

Status: EVIDENCE SNAPSHOT. AutoPTU-Java and AutoPTU are read-only evidence for this narrative task.

## Live heads inspected

AutoPTU-Java `main`: `4148255b038f85902feb781413f163c7b7cf3799` — `Add package-private move-special target result transport (#195)`.

This slice generalizes package-private per-target Move Special result transport so action-wide END_ACTION aggregation can consume result snapshots and applied damage without exposing mutable PTU bookkeeping to Minecraft/Cobblemon. It is useful evidence for move-specific execution/order and runtime ownership. It does not verify the complete Move catalog or promote another capability family.

AutoPTU Python `main`: `58f18824b32913d30d5c4e8ade91073729915a9b` — current inspected change is Career presentation/state work and does not change tactical battle readiness.

The current Java README continues to state that Python AutoPTU remains authoritative while the port is incomplete. It still lists core battle state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy and Craftics/Cobblemon adapter work as unfinished.

Project file search confirms an `Earthquake` Move concept exists in available source material. That is a battle mechanic, not an environmental-seismic subsystem. Available Python evidence also contains Groundshaper/Mold the Earth behavior. Neither may be generalized into regional earthquakes, fault motion, liquefaction, collapse or environmental shaking.

No generic seismicity, earthquake-hazard or ground-failure runtime subsystem was found or inferred.

## Permanent capability map

| Capability category | Pass 164 status | Evidence boundary |
| --- | --- | --- |
| targeting/footprints/range/LoS | VERIFIED | Java README marks targeting, areas, footprints, anchors and LoS implemented. |
| base movement legality | VERIFIED | Shift/jump legality and movement-profile rules are implemented for the documented boundary. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | README still explicitly lists forced movement unfinished. Narrow reaction/push examples do not complete the family. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy and documented calculation primitives are implemented. |
| action economy/initiative | VERIFIED | Typed turn flow, action budget and initiative/declaration ordering are implemented. |
| full turn/round lifecycle | PARTIAL | Several lifecycle/order slices exist; full battle state/transcript parity remains unfinished. |
| full stateful damage pipeline | PARTIAL | Authoritative damage/order pieces exist; README still lists full damage resolution unfinished. |
| status lifecycle | PARTIAL | Concrete status prevention/application/expiry behavior exists; status controller remains unfinished. |
| terrain/weather/hazards/zones/reactions | BLOCKING | Representative field/reaction contracts exist, but terrain, hazards and reactions remain explicitly unfinished as a family. |
| move-specific behavior | PARTIAL | PRE/POST/END_ACTION seams and representative mechanics exist; current target-result transport improves internal plumbing, not catalog completeness. |
| abilities | PARTIAL | Representative Ability contracts exist; complete registry/catalog parity is not proven. |
| items | PARTIAL | Representative Item interactions exist; complete catalog is not proven. |
| Trainer Features/perks | PARTIAL | Generic gates/effects/bookkeeping and representative Features exist; complete catalog/interrupt parity is not proven. |
| AI legal-action infrastructure | VERIFIED | README documents deterministic legal-choice/action-space infrastructure. |
| AI tactical policy | BLOCKING | README explicitly lists AI scoring/policy unfinished. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | README says adapter work waits for a parity-safe vertical slice. |

One implemented representative mechanic never promotes a whole category.

## Pass 164 encounter dependencies

### Transit Hub Aftershock Evacuation — FULL

Verified foundation: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure.

Blocking:
- complete movement for civilians/responders moving through threatened space, interception or any forced displacement;
- terrain/weather/hazards/zones/reactions if unsafe areas, debris or aftershock effects change tactics;
- AI tactical policy for EVACUATE, WITHDRAW, CLEAR_ROUTE and protection objectives;
- Minecraft/Cobblemon/Craftics adapter/playback for persistent civilians, route state and semantic objectives.

Partial by exact use:
- full lifecycle if the scene contains timed/repeated phase changes;
- stateful damage if environmental damage exists;
- status lifecycle, move-specific behavior, abilities, items and Trainer Features whenever a specific mechanic is invoked.

REDUCED: Crisis resolves the aftershock, civilians leave, damaged geometry is excluded and AutoPTU receives one stable static arena. No debris damage, earthquake Move, dynamic ground failure or forced movement is invented.

### Seismic Station Recovery — FULL

Verified foundation: ordinary targeting, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure.

Blocking: complete movement for technician/objective traversal; AI tactical policy for REACH_DEVICE, PROTECT_TECHNICIAN, WITHDRAW or CLEAR_ROUTE; adapter/playback. The environmental family is additionally blocking if unstable ground, slope state or repeated shaking affects tactics.

REDUCED: technician remains outside the combat snapshot; world state establishes safe access and AutoPTU runs a conventional static encounter. Metrology validates the station afterward.

### Liquefaction Street Closure — FULL

Blocking: complete movement, terrain/weather/hazards/zones/reactions, AI tactical policy and adapter/playback. Stateful damage is PARTIAL if ground failure itself can damage actors.

REDUCED: ground-failure observation and street closure occur in world state. Battle happens on adjacent stable geometry. No liquefaction tile, Slowed, Tripped, sinking, knockback or environmental damage is invented.

### Magnitude vs Damage Review

No battle dependency by default. Geology/seismic observations, Metrology, Timekeeping and Architecture can reconcile evidence and remain `UNRESOLVED`. A battle transcript cannot determine event magnitude, source fault or structural cause.

## Seismicity-specific no-inference rules

Do not map the PTU Move `Earthquake` to an environmental seismic event.
Do not map a regional earthquake to the Move’s damage, targeting, frequency or special behavior.
Do not map Groundshaper/Mold the Earth to tectonics, fault movement or earthquake prediction.
Do not map Ground typing to seismic sensing or immunity.
Do not map visible Minecraft cracks/block destruction to fault rupture or event magnitude.
Do not map camera shake to local intensity.
Do not map wet ground or sand to liquefaction.
Do not map earthquake context to Rough Terrain, Slowed, Tripped, Stuck, Accuracy penalties or forced movement without exact rules.
Do not map aftershock timing to initiative or reaction windows.
Do not map Whiscash behavior to causation or prediction without authored evidence.
Do not map structural damage directly to event size; Architecture owns structural condition.
Do not map landslide/rockfall state into the seismic protocol; Slope Instability owns it.

## PTU/Caelo open mechanics

The project source search in this run confirms the existence of the `Earthquake` Move and Groundshaper-related behavior, but did not recover a complete reliable Caelo rules basis for regional earthquakes, environmental shaking, liquefaction, collapse, falling debris or ground-failure hazards.

Super PTU Online Helper was not exposed as an invocable capability.

Any future FULL seismic battle must wait for exact mechanics or remain in the reduced static form.