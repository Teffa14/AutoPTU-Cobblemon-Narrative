# Cobblemon Native Spawn Projection Contract

Status: PROPOSED DESIGN. Not established Ouros canon.
Date: 2026-09-03

## Purpose

Define how persistent Ouros ecology projects into visible wild Pokémon while preserving Minecraft/Cobblemon as the native overworld spawn substrate.

This contract is subordinate to `design/ecology-development-program.md` and complements `design/global-species-interaction-graph.md`.

## Authority boundary

The spawn pipeline is:

```text
Minecraft world facts
+ active Cobblemon spawn data
= native spawn envelope

native spawn envelope
+ Ouros persistent ecology state
= projected local likelihood/visibility

projected local likelihood/visibility
-> Cobblemon/Minecraft materialization
```

Minecraft/Cobblemon owns coarse habitat compatibility and spawn placement semantics.

Ouros owns persistent ecological causes that alter whether an otherwise native-plausible species is locally common, scarce, concealed, displaced, concentrated or temporarily absent.

Generic materialization never creates demographic truth.

## Native spawn envelope

A native spawn detail can expose, depending on the active Cobblemon schema:

```yaml
spawn_detail_id: null
species_id: null
biome_ids_or_tags: []
presets: []
context: null
bucket: null
base_weight: null
conditions: {}
anticonditions: {}
weight_multipliers: []
source_datapack: null
```

The adapter should index the installed data rather than reproduce it manually in narrative configuration.

If the active data says a species does not match the current Minecraft biome/context, ambient Ouros ecology does not make that generic spawn eligible.

An authored exception that expands habitat eligibility is a reviewed datapack/world-design change and must be represented as such.

## Ouros ecology overlay

Ouros should project state through a small overlay that never duplicates the full native spawn definition.

```yaml
ecosystem_id: null
species_id: null
population_pressure: 1.0
visibility_multiplier: 1.0
ecological_weight_multiplier: 1.0
allowed_native_detail_ids: []
suppressed_native_detail_ids: []
preferred_microhabitat_selectors: []
avoidance_zone_ids: []
concentration_zone_ids: []
active_time_pressure: []
reason_refs: []
valid_from: null
valid_until: null
```

`allowed_native_detail_ids` is optional and narrows among spawn details that are already legal.

`suppressed_native_detail_ids` provides reversible local suppression without editing species canon.

`preferred_microhabitat_selectors` should refer to Minecraft/Cobblemon-observable facts or adapter-defined authored zones. It must not introduce a parallel biome system.

## Effective selection rule

For each native spawn detail that is legal at the current Minecraft context:

```text
projected_weight
= native_detail.base_weight
* native_detail.native_condition_multipliers
* ecological_weight_multiplier
* visibility_multiplier
```

The exact arithmetic and clamp policy remain implementation details until validated against the pinned Cobblemon version.

The factors have different meanings and remain separately queryable.

`population_pressure` describes persistent ecological abundance/demographic pressure. It is an input to ecology policy and must not be reconstructed from recent visible spawn counts.

`ecological_weight_multiplier` describes local opportunity pressure such as migration arrival, resource concentration, territorial displacement or depleted abundance.

`visibility_multiplier` describes detectability and exposure such as refuge use, predator avoidance, disturbance sensitivity or human habituation.

## Habitat policy

Ouros uses the installed Minecraft biome and Cobblemon biome/tag taxonomy for spawn compatibility.

Species ecology profiles may retain source-oriented habitat descriptions for research and reasoning, but every implementation-facing habitat claim needs a normalization mapping to one or more native spawn selectors.

Example:

```yaml
species_ecology_habitat_claim:
  source_label: woodland edge
  normalized_spawn_selectors:
    biome_tags:
      - "#cobblemon:is_forest"
    microhabitat_requirements:
      - can_see_sky_or_edge_zone
  mapping_status: proposed
```

The source label is useful for ecology reasoning. The normalized selectors are what make it executable.

No narrative system should ask whether the player is in an invented Ouros biome enum when Minecraft already supplies the actual biome.

## Microhabitat policy

Microhabitat refines a native habitat rather than replacing it.

Use native facts first:

```text
biome/tag
block or block tag
nearby block
fluid
surface/grounded/submerged context
structure
sky access
light
Y range
time/weather/moon where supported
```

Use authored spatial zones only for ecological distinctions that cannot be expressed safely with native conditions, such as one protected nesting shelf or one disturbed road verge inside a larger biome.

Authored zones must still sit inside a valid Minecraft/Cobblemon habitat envelope unless a reviewed spawn-data change explicitly expands it.

## Multiple-detail reconciliation

A species may have multiple native spawn details.

The adapter should evaluate each detail independently because different rows may represent different biome groups, contexts, rarity buckets or environmental niches.

Ouros applies ecology to matching detail IDs rather than flattening the species into one universal spawn rate.

This allows one species to remain common in freshwater while becoming scarce on a neighboring bank, or to shift from open areas into cover without rewriting its whole species profile.

## Persistent individual boundary

Generic spawn projection applies to population-derived anonymous wild materialization.

Named, tagged, story-relevant or otherwise persistent individuals follow a separate reconciliation path.

Required invariant:

```text
canonical persistent individual
!= generic spawn row output
```

A persistent individual may be materialized through Minecraft/Cobblemon presentation, but it must be reserved/reconciled against generic population projection so a second equivalent individual is not generated accidentally.

## Ecology causes that may modify projection

The initial approved families for the overlay are:

- abundance/depletion;
- predation pressure;
- refuge/avoidance behaviour;
- territorial displacement;
- competition/resource scarcity;
- resource concentration;
- migration or dispersal;
- nesting/juvenile protection;
- human disturbance;
- habituation;
- disturbance/recovery succession;
- temporary world events grounded in persistent state.

Each applied modifier needs `reason_refs` so observations, debugging and NPC knowledge can distinguish causes.

## Example: predator pressure without population collapse

```yaml
species_id: wurmple
population_pressure: 0.92
visibility_multiplier: 0.35
ecological_weight_multiplier: 0.90
reason_refs:
  - local_predator_pressure:swellow
  - refuge_use:understory_cover
```

Narrative meaning: the population remains present, but visible encounters drop sharply because individuals use cover and avoid exposed activity.

The exact values are illustrative only.

## Example: local resource pulse

```yaml
species_id: null
population_pressure: 1.0
visibility_multiplier: 1.15
ecological_weight_multiplier: 1.8
preferred_microhabitat_selectors:
  - berry_patch_zone_04
reason_refs:
  - resource_pulse:ripe_fruit
```

The species ID and values must come from an approved local ecology fixture. This pattern shows that concentration can increase encounter likelihood without asserting rapid population growth.

## Adapter requirements

The Minecraft/Cobblemon/Craftics adapter eventually needs to provide:

- current Minecraft biome ID and biome-tag membership;
- active Cobblemon spawn details for the pinned mod/datapack set;
- resolved preset/condition semantics needed by the projector;
- legal native candidates at a position/context, or enough data to reproduce the legal filtering safely;
- a supported hook for dynamic filtering/weight modification;
- entity materialization identity callbacks;
- persistent-individual reservation/reconciliation;
- telemetry that records native detail, applied ecology modifiers and resulting materialization.

The narrative layer must not prescribe unsupported adapter hooks as if they already exist.

## Verification fixtures

Minimum deterministic fixtures for later implementation:

1. A species rejected by the native biome condition remains rejected even when Ouros multiplier is high.
2. A legal native spawn with multiplier `0` is suppressed locally without changing its base datapack definition.
3. Two legal spawn details for one species receive independent local modifiers.
4. Low visibility does not automatically reduce persistent population state.
5. Population depletion can reduce projected likelihood while visibility remains normal.
6. A persistent named individual does not cause a duplicate generic materialization.
7. Changing the Minecraft biome immediately changes the set of native legal details before ecology modifiers are applied.
8. Removing an ecological pressure restores native-relative likelihood according to the decay/recovery policy.

## Mechanical dependency classification

Primary dependency: `Minecraft/Cobblemon/Craftics adapter/playback support`.

Current status: PARTIAL/BLOCKING for complete semantic projection. Existing narrative evidence does not verify an end-to-end adapter that indexes the active spawn pool, reads native environmental eligibility, applies dynamic Ouros modifiers and reconciles persistent identities.

Ambient projection requires no AutoPTU tactical category.

Once a visible ecological event enters structured battle, encounter-specific dependencies must be declared separately across targeting/footprints/range/LoS; base movement legality; complete movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behaviour; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and adapter/playback support.

## Open questions

- pinned Cobblemon version and exact runtime spawn-rule extension point;
- dynamic runtime multiplier API versus generated/static datapack rules;
- biome-tag resolution/caching strategy;
- native rarity-bucket interaction when ecology drastically changes weights;
- safe clamp and decay rules for ecological multipliers;
- how local authored zones are represented and queried;
- how server restarts reconcile already materialized wild entities with the ecology ledger;
- whether anonymous materialized individuals can become persistent after meaningful player interaction and how population accounting changes when that happens.
