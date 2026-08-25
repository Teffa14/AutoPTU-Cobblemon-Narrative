# Engine Readiness Snapshot — Pass 163

Status: EVIDENCE SNAPSHOT. AutoPTU-Java and AutoPTU are read-only evidence for this narrative task.

## Live heads inspected

AutoPTU-Java `main`: `10fd20bfd513898a6f8f157a9b469db993444974` — `Finalize move-special END_ACTION per declaration (#194)`.

The current Java README still states that the Python engine remains authoritative while the port is incomplete and lists full combat state, full damage, status controller, terrain, hazards, forced movement, reactions, remaining hook registries, full transcript parity, AI scoring/policy and Craftics/Cobblemon adapter work as unfinished.

The latest slice finalizes Move Special END_ACTION once per declaration after ordered per-target results, preserving last-target result semantics and total applied damage. This is real evidence for move-specific execution/order. It does not verify all Moves or promote another family.

AutoPTU Python remains the source oracle for unported behavior. No rangeland, grazing or pastoral-movement runtime subsystem was found or inferred.

## Permanent capability map

| Capability category | Pass 163 status | Evidence boundary |
| --- | --- | --- |
| targeting/footprints/range/LoS | VERIFIED | Java README marks targeting, areas, footprints, anchors and LoS implemented. |
| base movement legality | VERIFIED | Shift/jump legality and movement-profile rules are implemented for the documented boundary. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | README still explicitly lists forced movement as unfinished; narrow reaction/push contracts do not complete the family. |
| core calculations | VERIFIED | Damage Base/type tables, stages, accuracy and documented calculation primitives are implemented. |
| action economy/initiative | VERIFIED | Typed turn flow, action budget and initiative/declaration ordering are implemented. |
| full turn/round lifecycle | PARTIAL | Several lifecycle/order slices exist, but full battle state/transcript parity remains unfinished. |
| full stateful damage pipeline | PARTIAL | Significant authoritative ordering exists, but README still lists full damage resolution as unfinished. |
| status lifecycle | PARTIAL | Concrete status prevention/application/expiry slices exist; status controller remains unfinished. |
| terrain/weather/hazards/zones/reactions | BLOCKING | Representative field/reaction contracts exist, but README still lists terrain, hazards and reactions as unfinished. |
| move-specific behavior | PARTIAL | PRE/POST/END_ACTION Move Special seams and representative mechanics exist; complete Move catalog is not proven. |
| abilities | PARTIAL | Several Ability contracts exist; complete registry/catalog parity is not proven. |
| items | PARTIAL | Representative item interactions exist; complete catalog is not proven. |
| Trainer Features/perks | PARTIAL | Generic gates/effects/bookkeeping exist; complete Feature catalog and interrupts are not proven. |
| AI legal-action infrastructure | VERIFIED | README documents deterministic action-space/legal-choice infrastructure. |
| AI tactical policy | BLOCKING | README explicitly lists AI scoring/policy as unfinished. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | README says the adapter is deferred until a parity-safe vertical slice exists. |

One implemented representative mechanic never promotes a whole category.

## Pass 163 encounter dependencies

### Seasonal Crossing at Cedar Range — FULL

Verified foundation: targeting when combat occurs, base movement legality, core calculations, action economy/initiative and AI legal-action infrastructure.

Blocking requirements: complete movement for crossing/withdrawal/interception; AI tactical policy for CROSS, WITHDRAW, CLEAR_ROUTE and protection objectives; adapter/playback for persistent managed/wild actors and road state. Terrain/weather/hazards/zones/reactions is also blocking if road barriers, weather or ground conditions have tactical effects.

Partial-by-exact-use: lifecycle, stateful damage, statuses, Move-specific behavior, Abilities, Items and Trainer Features. Any specific mechanic must be checked separately.

REDUCED: resolve traffic, managed group, wild movement and civilians in world state first; then run a static conventional battle on a cleared verge. Narrative premise remains an interrupted crossing.

### Waterpoint Rotation Conflict — FULL

Blocking: complete movement, AI tactical policy, adapter/playback. The environmental family is additionally blocking if water, mud, protected lanes or dynamic access changes affect tactics.

REDUCED: close/redirect the source outside battle and run a static encounter away from infrastructure. No custom Water Terrain, mud penalty or forced movement is invented.

### Fence-Line Repair During Seasonal Movement — FULL

Blocking: complete movement for route crossing and withdrawal, tactical AI for PROTECT_TECHNICIAN/CLEAR_ROUTE/WITHDRAW, adapter/playback for workers/fence/group state. Environment remains blocking if the fence or ground becomes a tactical zone/hazard.

REDUCED: pause repair and reroute noncombatants before the battle snapshot.

### Forage Condition Review

No battle engine dependency by default. A combat transcript, if some independent confrontation occurs, cannot determine forage condition, grazing pressure, permission or ecological causation.

## Rangeland-specific no-inference rules

Do not map herd membership to Pack Mon, shared turns or tactical coordination.
Do not map Gogoat/Skiddo lore to PTU Mountable, carrying or willingness.
Do not map pasture blocks to Rough Terrain or any field effect.
Do not map trampling to Slowed/Tripped or forced movement.
Do not map fences/gates to interception or movement denial without an exact battle rule.
Do not map waterpoints to Water Terrain.
Do not map drought or forage shortage to Fatigue, Injury, HP loss or Combat Stages.
Do not map rest/recovery periods for land to healing.
Do not map dung or concentrated use to Poisoned/toxic hazards.
Do not map managed group count from loaded Minecraft entities to population truth.
Do not map managed seasonal movement to the Wildlife Migration authority.

## PTU/Caelo open mechanics

The project sources available in this run did not provide a complete, reliable Caelo rules basis for pastoral movement, grazing, animal handling, Mountable, workload or forage. Super PTU Online Helper was not exposed as an invocable capability. Exact mechanics must remain unresolved until primary project evidence is recovered.