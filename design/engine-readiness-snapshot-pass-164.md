# Engine Readiness Snapshot — Pass 164

Status: EVIDENCE SNAPSHOT. AutoPTU-Java and AutoPTU are read-only evidence for this narrative task.

## Authority correction

Final repository comparison surfaced Pass 71’s existing `design/seismic-faults-ground-failure-layer.md`. Pass 71 remains authoritative for seismic events, shaking footprints, aftershock sequences and ground failure. Pass 164 only extends monitoring-network history, automatic/reviewed detection, source-solution revisions, felt-report provenance and catalog vintages through `design/seismic-event-catalog-monitoring-revision-protocol.md`.

## Live heads inspected

AutoPTU-Java `main`: `4148255b038f85902feb781413f163c7b7cf3799` — `Add package-private move-special target result transport (#195)`.

This slice generalizes package-private per-target Move Special result transport so action-wide END_ACTION aggregation can consume result snapshots and applied damage without exposing mutable PTU bookkeeping to Minecraft/Cobblemon. It is evidence for move-specific execution/order and runtime ownership. It does not verify the complete Move catalog or promote another family.

AutoPTU Python `main`: `58f18824b32913d30d5c4e8ade91073729915a9b` — the inspected change is Career presentation/state work and does not alter tactical battle readiness.

The current Java README still states that Python AutoPTU is authoritative while the port is incomplete and lists core battle state, full damage resolution, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy and Craftics/Cobblemon adapter work as unfinished.

Project source search confirms `Earthquake` as a concrete Move concept and shows Groundshaper/Mold the Earth behavior in Python. Neither is evidence of an environmental-seismic runtime subsystem.

## Permanent capability map

| Capability category | Pass 164 status | Evidence boundary |
| --- | --- | --- |
| targeting/footprints/range/LoS | VERIFIED | Java README marks targeting, areas, footprints, anchors and LoS implemented. |
| base movement legality | VERIFIED | Shift/jump legality and movement-profile boundaries are implemented. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Forced movement remains explicitly unfinished. Narrow push/reaction paths do not complete the family. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy and documented calculation primitives are implemented. |
| action economy/initiative | VERIFIED | Typed turn flow, action budget and initiative/declaration ordering are implemented. |
| full turn/round lifecycle | PARTIAL | Several lifecycle/order slices exist; full battle state/transcript parity remains unfinished. |
| full stateful damage pipeline | PARTIAL | Authoritative damage/order pieces exist; full damage resolution remains unfinished. |
| status lifecycle | PARTIAL | Concrete prevention/application/expiry behavior exists; status controller remains unfinished. |
| terrain/weather/hazards/zones/reactions | BLOCKING | Representative field/reaction contracts exist; terrain, hazards and reactions remain unfinished as a family. |
| move-specific behavior | PARTIAL | PRE/POST/END_ACTION seams and representative mechanics exist; target-result transport improves plumbing, not catalog completeness. |
| abilities | PARTIAL | Representative Ability contracts exist; complete parity is not proven. |
| items | PARTIAL | Representative Item interactions exist; complete parity is not proven. |
| Trainer Features/perks | PARTIAL | Generic gates/effects/bookkeeping and representative Features exist; complete parity is not proven. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-choice/action-space infrastructure is documented. |
| AI tactical policy | BLOCKING | README explicitly lists AI scoring/policy unfinished. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | Adapter work remains deferred until a parity-safe vertical slice exists. |

One representative mechanic never promotes a whole category.

## Pass 164 encounter dependencies

### Monitoring Station Access Interruption — FULL

Verified foundation: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure.

Blocking:
- complete movement for technician traversal, withdrawal or interception;
- AI tactical policy for REACH_DEVICE, PROTECT_TECHNICIAN, WITHDRAW or CLEAR_ROUTE;
- Minecraft/Cobblemon/Craftics adapter/playback;
- terrain/weather/hazards/zones/reactions if unstable terrain, debris or an active physical hazard affects tactics.

Partial by exact use: lifecycle, damage, statuses, Move-specific behavior, Abilities, Items and Trainer Features.

REDUCED: technician remains outside the grid, Pass 71/other world authorities establish safe access, and AutoPTU resolves a static conventional encounter. Data retrieval and Metrology validation happen afterward.

### Archive Seismogram Recovery — FULL

Blocking: complete movement for a moving custodian/objective; AI tactical policy for PROTECT_CUSTODIAN/REACH_EXIT; adapter/playback. Environmental family becomes blocking if fire, collapse, debris or protected zones affect tactics. Items remain PARTIAL if the archive object receives tactical behavior.

REDUCED: Archives secures the record and removes custodians before battle. The static encounter cannot authenticate or interpret the record.

### Felt-Report Collection During Evacuation — FULL

Blocking: complete movement, AI tactical policy and adapter/playback for civilians/researchers. Environmental family is blocking only if the physical event remains tactically active.

REDUCED: testimony collection stops, civilians evacuate through world state, and only combatants enter a static arena. Missing reports remain missing.

### Catalog Reconciliation Review

No battle dependency. Automatic detections, station records, corrected timestamps, felt reports and Pass 71 event identities can produce merge/split/reclassification/revision or `UNRESOLVED`. A battle result cannot decide catalog truth.

## Pass 164 no-inference rules

Do not map an automatic detection directly to a confirmed Pass 71 seismic event.
Do not treat a catalog correction as a second physical earthquake.
Do not treat station silence as absence of shaking.
Do not infer magnitude from felt reports or damage.
Do not assign aftershock membership by timestamp alone.
Do not map the PTU Move `Earthquake` to environmental seismic state.
Do not map Groundshaper/Mold the Earth to tectonics or seismic sensing.
Do not map Whiscash behavior to deterministic prediction or causation.
Do not map Minecraft TNT, block damage, entity behavior or camera shake into the event catalog.
Do not invent falling-rock damage, knockback, Rough Terrain, Slowed, Tripped or Status effects from seismic flavor.

## PTU/Caelo open mechanics

Available project evidence confirms exact battle concepts such as `Earthquake` and Groundshaper-related behavior, but no complete reliable Caelo rules basis for regional earthquakes, environmental shaking, collapse, falling debris, liquefaction or ground-failure hazards was recovered.

Super PTU Online Helper was not exposed as an invocable capability. FULL dynamic-disaster battles must therefore remain blocked or use the REDUCED static handoff.