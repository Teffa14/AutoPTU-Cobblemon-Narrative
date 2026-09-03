# Marea Ecology Evidence Loop Fixture — Pass 230

Status: PROPOSED IMPLEMENTATION FIXTURE. Does not change canon.
Date: 2026-09-03

## Purpose

Provide a migratable Marea example for `design/ecology-observation-intervention-contract.md` without finalizing biome compatibility before the global Ouros world is generated and frozen.

This fixture uses existing Marea institutions and route concepts only as observers/actors. It does not add a new canon species, biome or permanent coordinate.

## Spatial status

Existing Marea anchors in `canon/marea-interior-map-resident-network-v2.md` remain legacy canonical coordinates until the global worldgen migration gate is resolved.

The ecological fixture therefore binds to semantic sites:

```yaml
site_refs:
  - marea.sendero_lower_shelf
  - marea.loma_clara_cultivation_edge
  - marea.estacion_mirador_observation_network
coordinate_binding: migrate_after_global_world_lock
minecraft_biome_binding: unresolved
```

No biome, Cobblemon tag or native spawn compatibility is inferred from the site names.

## Scenario family — Thin Foraging Pressure

This is a system fixture, not a fixed quest plot.

The world contains an ecological process in which a locally approved resource becomes temporarily scarce or shifts spatially. One or more approved local wild populations respond by changing exposed activity and resource use.

The player-facing symptom can be a producer, route observer or field worker reporting unusual signs.

The authoritative cause is intentionally hidden from the observer layer.

## Truth-state example

Illustrative only:

```yaml
process_id: marea.fixture.resource_shift.01
process_type: resource_depletion
state: active
affected_resources:
  - local_resource_node_unassigned
affected_species: []
pressure_vectors:
  - reduced_local_foraging_opportunity
  - increased_edge_use
cause_refs:
  - fixture_only
```

Species remain empty until the Marea roster is approved against the frozen Minecraft/Cobblemon habitat envelope.

## Observable manifestations

Possible manifestations:

```yaml
- channel: resource_damage
  raw_shape: concentrated feeding damage near an edge zone

- channel: track_or_trace
  raw_shape: repeated fresh traces along a route not previously used heavily

- channel: visual_absence
  raw_shape: fewer observations at a formerly reliable resource site

- channel: human_report
  raw_shape: producer or route worker reports a recent pattern change

- channel: instrument_reading
  raw_shape: Mirador records a correlated environmental change when instrumentation supports it
```

No single manifestation establishes the cause.

## Existing NPC/institution surfaces

These existing canon actors can participate without becoming omniscient:

### Alba Ríos

Can observe changes on her own holding and report local production/resource evidence.

Cannot automatically know:
- the regional population trend;
- the causal species;
- whether another holding has the same pattern.

### Brin Havel

Can compare cooperative intake/dispatch records and identify whether a resource shortage is broader than one producer.

Cannot convert inventory records directly into wildlife causality.

### Dr. Nerea Sol / Estación Mirador

Can compare repeated field observations and environmental measurements.

Can generate hypotheses with higher evidence quality where her actual observations support them.

Cannot receive hidden ecology-service truth.

### Mara Veyra

Can coordinate route reports and interventions after evidence reaches the Field Office.

Her institutional role may aggregate reports but does not grant direct observation of remote cells.

## Investigation loop

A possible system-driven sequence:

```text
1. first local report enters observation history
2. player inspects affected site
3. evidence packet records traces/resource condition
4. second observation at another site supports or contradicts the initial explanation
5. player/NPC institution opens competing hypotheses
6. intervention is selected
7. ecology ledger applies pressure changes
8. later visit or report verifies effect
```

The sequence can shorten if evidence is already strong or lengthen when signals conflict.

## Example hypotheses

These are generic hypothesis shapes, not canonical answers:

```text
H1: approved wild population shifted foraging because its primary resource declined
H2: local human activity displaced animals into the observed edge
H3: a second species created competitive pressure
H4: the visible damage is unrelated to the reported wildlife change
```

The system should permit H4. Not every coincident signal shares one cause.

## Intervention examples

### Low-mechanical intervention

```yaml
method: protect_or_close_route
mechanical_handoff: none
world_effect:
  disturbance_delta: reduced_after_initial_transition
verification:
  compare route use and resource damage after delay
```

### Resource restoration

```yaml
method: restore_resource
mechanical_handoff: none unless action invokes a mechanical item/feature contract
world_effect:
  resource_state_delta: positive
verification:
  monitor whether exposed foraging redistributes
```

### Observation only

```yaml
method: observe_only
mechanical_handoff: none
world_effect:
  none
verification:
  accumulate more temporal evidence
```

### Escalated defensive encounter

Occurs only if a visible actor's behavior escalates into structured mechanics.

Reduced version dependencies:
- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- core calculations: VERIFIED;
- action economy / initiative: VERIFIED;
- AI legal-action infrastructure: VERIFIED;
- exact move/ability/status subset: must be individually verified before use;
- AI tactical policy: BLOCKING as complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

Full version may additionally consume:
- complete movement: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside bounded slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL.

Do not require the full version for the ecological premise to function.

## Success conditions

The fixture is successful when:

- the player can receive a meaningful ecological problem without an omniscient explanation;
- at least two evidence channels can support or contradict a hypothesis;
- intervention changes persistent ecology state rather than merely setting a quest flag;
- later observations can verify the change;
- no species or biome becomes canon through this fixture;
- no hidden tactical battle is simulated;
- any direct battle is resolved by AutoPTU and returns semantic consequences only.

## Worldgen migration requirement

After the global planet is frozen:

```text
semantic Marea site
-> final coordinate polygon
-> actual Minecraft biome/tags
-> resource-node geometry
-> approved species/native spawn envelope
-> concrete manifestation placement
```

Only then can this fixture become a fully executable local ecology scenario.

## Next implementation questions

- define the evidence confidence representation;
- define passive versus active observation checks;
- bind existing Marea institutions to observation-sharing permissions;
- define the first approved resource node after world lock;
- select approved species only after native habitat validation;
- create delayed verification scheduler/state transitions;
- identify which visible warning/avoidance behaviors can be projected through the actual Cobblemon adapter.
