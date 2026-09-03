# Cobblemon Native Spawn/Habitat Contract Research — Pass 227

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-09-03

## Question

How should Ouros ecology use habitat information without replacing Cobblemon/Minecraft spawning semantics?

## Current Cobblemon evidence

Cobblemon world spawn data already carries the environmental eligibility and relative selection inputs needed for a native projection layer.

The documented spawn detail surface includes:

- `presets`: reusable bundled spawn conditions and contexts;
- `context`: grounded, submerged, surface, and other spawn-placement semantics;
- `bucket`: rarity pool;
- `weight`: relative selection weight inside the applicable pool;
- `condition`: positive requirements;
- `anticondition`: exclusions;
- `biomes`: biome IDs or biome tags inside conditions;
- `weightMultiplier`: conditional multiplication of a spawn detail's weight.

Cobblemon biome conditions accept concrete biome IDs and biome tags. The documented examples use tags such as `#cobblemon:is_jungle`, `#cobblemon:is_hills`, `#cobblemon:is_plains`, `#cobblemon:is_river`, and broad world tags.

Spawn detail presets can bundle block, structure, biome and context requirements. This means a useful ecological microhabitat does not need to become a new Minecraft biome. It can often project through existing biome compatibility plus native block/context/preset conditions.

Cobblemon also documents `spawn_rules`, including weight and filter components. These rules can inspect spawn identity and local context and can modify weight or deny a spawn. The context includes biome membership and coordinates as well as environmental values such as light and moon phase.

## Source references

- Cobblemon Wiki, `Spawn Pool World`: https://wiki.cobblemon.com/index.php/Spawn_Pool_World
- Cobblemon Wiki, `Spawn Detail Presets`: https://wiki.cobblemon.com/index.php/Spawn_Detail_Presets
- Cobblemon Wiki, `Spawn Rules`: https://wiki.cobblemon.com/index.php/Spawn_Rules
- Cobblemon Wiki, `Tutorials/Creating Custom Spawns`: https://wiki.cobblemon.com/index.php/Tutorials/Creating_Custom_Spawns

These are implementation references, not Ouros canon sources.

## Design consequence

Minecraft/Cobblemon habitat compatibility should remain the projection substrate.

Ouros should not maintain a second independently-authored table that says a species may spawn in a biome which its installed Cobblemon spawn details reject. The ecology layer should first resolve against the active installed spawn data and Minecraft biome/tag state.

The useful separation is:

```text
Cobblemon/Minecraft native spawn envelope
    biome/tag eligibility
    context / preset / blocks / structure
    base bucket and weight
    time/light/weather/etc conditions

Ouros persistent ecology state
    local abundance pressure
    refuge/avoidance visibility
    trophic pressure
    territorial displacement
    temporary concentration
    migration/season pressure
    human-disturbance response

projection result
    native detail remains eligible or becomes temporarily suppressed
    native weight receives an ecology multiplier
    native location/time subset can be narrowed where supported
```

Ouros may narrow or weight an already plausible native spawn. Broadening native eligibility should require an explicit reviewed world-design/datapack decision, because that changes the underlying Cobblemon habitat definition rather than merely expressing current ecology.

## Important distinction: habitat versus microhabitat

A Minecraft biome or Cobblemon biome tag is the coarse environmental envelope.

An Ouros ecological microhabitat is a local niche inside that envelope. Examples include a reed margin, exposed tidal rock, shaded understory, nesting ledge, berry patch, carrion site, disturbed roadside edge, or temporary refuge.

Where possible, microhabitats should map onto native Minecraft/Cobblemon facts such as:

- nearby/base blocks;
- fluid and surface context;
- sky visibility;
- Y range;
- structures;
- light;
- biome/tag membership;
- coordinates or authored zones when the adapter supports them.

Do not create a bespoke `OUROS_FOREST`, `OUROS_COAST`, or similar parallel biome ontology merely to drive spawning.

## Rate semantics

Cobblemon `weight` is a relative spawn selection input, not a direct ecological population count.

Therefore Ouros must keep at least these concepts separate:

- `population_state`: persistent abundance/demography truth;
- `native_spawn_weight`: weight supplied by the matching Cobblemon spawn detail;
- `ecology_weight_multiplier`: temporary/local projection factor derived from ecology;
- `visibility_multiplier`: behavioural observability independent from abundance;
- `effective_spawn_weight`: projection result, not population truth.

Suggested relationship:

```text
effective_spawn_weight
= native_spawn_weight
* ecology_weight_multiplier
* visibility_multiplier
```

This is a projection heuristic only. Exact runtime integration depends on the adapter and active Cobblemon version.

A prey species hiding because predators are active can have stable population state but a low visibility multiplier. A depleted population can have low abundance pressure even when remaining individuals are not hiding. These states must not collapse into one number.

## Installed-data requirement

The actual server/modpack spawn datapack is the runtime authority for which biome IDs/tags, presets and spawn details exist. Documentation examples cannot substitute for reading the installed data.

Future implementation should ingest or index the active Cobblemon `spawn_pool_world`, relevant biome tags, spawn-detail presets and any Ouros/addon spawn rules. This allows ecology fixtures to validate against the exact world configuration instead of a generic wiki snapshot.

## Proposed invariant

For a generic wild spawn candidate:

1. Minecraft provides the actual world position and biome/block/environment facts.
2. Cobblemon determines which native spawn details are environmentally legal.
3. Ouros evaluates persistent ecology state only for those legal candidates.
4. Ouros may suppress or modify relative likelihood according to ecology.
5. Cobblemon/Minecraft materializes the visible overworld entity.
6. Materialization does not create or overwrite hidden population truth.

Persistent named individuals follow the separate persistent-individual reconciliation path and must not be cloned by generic spawn projection.

## Engine dependency classification

This work is primarily `Minecraft/Cobblemon/Craftics adapter/playback support`.

Current narrative readiness remains PARTIAL/BLOCKING for semantic end-to-end spawn projection because the narrative repository does not yet demonstrate a verified adapter contract that reads active spawn details, applies ecology multipliers and reconciles resulting entities with persistent ecology state.

No AutoPTU tactical capability family is required to calculate ambient generic spawn eligibility or weighting.

If a visible ecological situation becomes combat, the encounter must separately declare its AutoPTU dependencies using the permanent capability categories.

## Open implementation questions

- Which exact Cobblemon version and spawn schema will Ouros pin?
- Will the adapter alter spawn selection at runtime through spawn rules/hooks, generate datapack rules from ecology state, or use another supported extension point?
- How are dynamic per-zone ecology multipliers supplied without regenerating static datapacks continuously?
- How are biome tags expanded and cached for the installed world/modpack?
- How are multiple legal spawn details for one species combined when they overlap at the same location?
- Which native conditions are safe for Ouros to narrow dynamically?
- What minimum multiplier should count as effective temporary suppression rather than disabling a spawn detail?
- How does the persistent-individual system reserve ecological capacity so generic rows cannot create duplicates?
