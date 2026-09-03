# Marea / Sendero species interaction matrix — Pass 226

Status: PROPOSED. This file does not canonize candidate species by itself.
Date: 2026-09-03

Depends on:
- `design/global-species-interaction-graph.md`
- `design/wild-pokemon-behavior-tolerance-tactical-policy.md`
- `canon/marea-interior-first-wild-population-v1.md`
- `canon/marea-interior-map-resident-network-v2.md`
- `research/2026-09-03-marea-interspecies-predation-territory-scan-226.md`

## Goal

Start the first inspectable ecological community around Marea instead of treating wild Pokémon as independent spawn-table entries.

The matrix answers four different questions separately:

1. **Trophic:** who can consume whom?
2. **Threat response:** who treats whom as risk and what responses are plausible?
3. **Competition:** which species can lose access to the same limiting resource?
4. **Territory/displacement:** who can contest or exclude whom from a bounded space/resource?

None of these automatically means battle.

## Local ecosystem cells

The map already canonizes Puerto Bruma, Sendero del Vidrio, Loma Clara and Estación Mirador. The ecology system should subdivide them into ecological cells without inventing new named settlements.

### `marea.puerto_bruma_populated_edge`

CANON location basis: Puerto Bruma and the south trailhead.

Useful ecological traits:
- human traffic;
- structures and possible roost surfaces;
- market/dock food opportunities only when a specific resource node is authored;
- high habituation/tolerance can exist but is individual/contextual.

### `marea.sendero_lower_shelf`

CANON location basis: lower shelf and the already established persistent Fletchling.

Useful ecological traits:
- route corridor;
- escape routes and vertical movement matter;
- disturbance changes with route traffic;
- resource nodes remain to be authored rather than assumed.

### `marea.sendero_vegetated_band`

Status: PROPOSED MICROHABITAT, not yet canon.

Purpose:
- candidate cell for vegetation/tree-dependent species and interactions;
- must not be treated as forest until the physical map actually establishes compatible cover/vegetation.

### `marea.loma_clara_cultivation_edge`

CANON location basis: Loma Clara mixed-crop production exists through Alba Ríos and the producer lane.

Ecological use:
- crop/plant resources can be authored explicitly;
- wild use of cultivated resources should create stewardship/conflict consequences rather than making farms generic spawn zones.

## Species roster state

| Species | Local status | Why it is in this file |
| --- | --- | --- |
| Fletchling | **CANON PRESENT** | first persistent wild individual already established at lower Sendero |
| Squawkabilly | **PROPOSED** | official direct territorial relation with Fletchling; compatible with populated environments |
| Wurmple | **PROPOSED** | official Swellow prey; active anti-predator defense; tree-sap feeder |
| Swellow | **PROPOSED** | official Wurmple predator; aerial prey-search behaviour |
| Taillow | **PROPOSED CONDITIONAL** | official Wurmple predator in forests; only usable if compatible microhabitat is authored |
| Scatterbug | **PROPOSED LATER** | plant-resource feeder with explicit chemical defense; useful future resource-web species, not needed to activate first predator web |

No candidate row changes Marea canon until approved separately.

## Interaction matrix

Legend:
- `EXPLICIT` = source names the relationship directly.
- `DERIVED` = Ouros can infer a candidate from approved facts but must preserve provenance.
- `INACTIVE` = the relationship exists as a template but lacks a required local actor/resource/context.

| ID | Actor | Target | Type | Trigger/resource | Provenance | Local state | Typical world consequence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ME-001 | Fletchling | Squawkabilly | `TERRITORIAL_AGAINST` | bounded contested site/resource | EXPLICIT species relation | INACTIVE until Squawkabilly + resource exist | warning, contest, spatial separation, possible escalation |
| ME-002 | Squawkabilly | Fletchling | `TERRITORIAL_AGAINST` | bounded contested site/resource | EXPLICIT species relation | INACTIVE until Squawkabilly + resource exist | group pressure, warning, exclusion, possible escalation |
| ME-003 | yellow Squawkabilly | Fletchling | `DISPLACES` | populated-space occupancy | EXPLICIT generic bird displacement + local Fletchling target | INACTIVE; form-specific candidate | Fletchling shifts roost/activity/visibility before combat is considered |
| ME-004 | Swellow | Wurmple | `PREDATES_ON` | prey detection + actual overlap | EXPLICIT | INACTIVE until both populations are approved | consumptive pressure plus prey risk/cover response |
| ME-005 | Taillow | Wurmple | `PREDATES_ON` | forest-compatible overlap | EXPLICIT | INACTIVE; habitat gate unresolved | consumptive pressure plus prey risk/cover response |
| ME-006 | Wurmple | Swellow | `AVOIDS` | recent/present predation cue | DERIVED from explicit predator relationship | INACTIVE until both present | hide/withdraw/defend candidates; lower visibility in exposed space |
| ME-007 | Wurmple | Taillow | `AVOIDS` | recent/present predation cue | DERIVED from explicit predator relationship | INACTIVE until both present | hide/withdraw/defend candidates; altered foraging window |
| ME-008 | Swellow | Taillow | `COMPETES_WITH` | Wurmple prey scarcity or shared feeding patch | DERIVED conditional | INACTIVE until co-occurrence + limiting resource | reduced feeding access / temporal or spatial partitioning; not automatic combat |
| ME-009 | Taillow | Swellow | `COMPETES_WITH` | Wurmple prey scarcity or shared feeding patch | DERIVED conditional | INACTIVE until co-occurrence + limiting resource | reduced feeding access / temporal or spatial partitioning; not automatic combat |
| ME-010 | Wurmple | tree-sap node | `FORAGES_RESOURCE` | suitable tree/sap | EXPLICIT species trait | INACTIVE until Wurmple + resource node exist | concentration around feeding sites; exposure trade-off |
| ME-011 | Scatterbug | plant-resource node | `FORAGES_RESOURCE` | suitable local vegetation | EXPLICIT species trait | INACTIVE until approved | plant-use pressure; possible crop/edge conflict later |

## Important: interaction is not response

The graph stores durable ecological relationships. The encounter stores the actual response.

Example:

```yaml
relationship:
  actor: swellow
  target: wurmple
  type: PREDATES_ON

encounter_context:
  wurmple_cover_distance: 2
  wurmple_condition: healthy
  swellow_detected: true
  escape_routes:
    - tree_cover
    - low_brush
  recent_alarm: false

candidate_wurmple_responses:
  - hide
  - withdraw
  - evade
  - defensive_display
  - defend_if_contacted
```

Do not convert this into `Wurmple always flees Swellow`. Official Wurmple material specifically gives it an active anti-predator defense.

## Runtime evaluation

```text
1. locate ecosystem cell
2. load actually present persistent + generic populations
3. load active resource nodes
4. select interaction edges whose context requirements are satisfied
5. evaluate current individuals, not abstract species only
6. apply disturbance / human traffic / time / weather / cover
7. create behavioral options and ecological pressure
8. Ouros resolves non-combat world intent/state
9. if structured mechanics begin:
      -> create explicit BattleSpec / encounter handoff
      -> AutoPTU owns legal actions and resolution
10. project resulting world state back through Minecraft/Cobblemon presentation
```

## First playable ecological loop

### `The contested lower shelf`

This should only be enabled if Squawkabilly is approved locally and a concrete contested resource is authored.

State A:
- the persistent Fletchling uses the lower-Sendero area normally;
- Squawkabilly activity is absent or low.

State B:
- Squawkabilly begins using the same bounded resource/space;
- warnings and spatial displacement can become observable;
- Fletchling does not automatically attack or flee.

State C:
- sustained territorial pressure changes where/when one or both species are visible;
- observers can notice the change without knowing the hidden pressure values;
- only a direct encounter with escalation needs tactical mechanics.

This gives the first Fletchling persistent ecological context without cloning it or turning it into a scripted aggressor.

### Reduced version

If reliable behavior animation or dynamic spawn projection is not ready:

- preserve the same ecology ledger;
- vary spawn eligibility/observation records in bounded cells;
- show direct encounters only when both actual actors are loaded;
- use simple movement/idle/warning presentation;
- enter a normal AutoPTU battle only after explicit escalation.

## First trophic loop

Enable only after Wurmple and Swellow are approved for an authored compatible cell.

```text
tree/sap resource
    -> Wurmple foraging concentration
    -> Swellow search opportunity
    -> predation pressure
    -> Wurmple refuge/visibility shift
    -> lower exposed prey availability
    -> lower immediate Swellow hunting success
```

This is already more useful than `spawn Wurmple + spawn Swellow`, because changes in one population or resource propagate through the same ecosystem.

If Taillow is later approved, it can add competitor pressure on the same prey resource. Scarcity can then cause partitioning without requiring a fight.

## Population and spawn consequences

Do not collapse these values:

```yaml
actual_population_estimate: null
exposed_fraction: null
activity_multiplier: null
spawn_projection_multiplier: null
predation_pressure: null
resource_pressure: null
territorial_pressure: null
```

A player seeing fewer Wurmple can mean:
- fewer Wurmple actually exist;
- the same number are using cover;
- their active window shifted;
- their feeding site moved;
- the player is observing the wrong microhabitat.

That ambiguity is useful worldbuilding and must remain available to Nerea/Mara/Tideglass observation systems.

## Individual capability rule

Species ecology only proposes intent.

For every visible interaction, compare:

1. species relationship;
2. actual individual Pokémon capabilities;
3. condition/injury/status;
4. movement modes and reachable cover/exits;
5. actual Moves/Abilities relevant under verified mechanics;
6. Trainer presence/actions and Features/Edges when applicable;
7. current environment.

An underpowered, injured or cornered predator can withdraw. A prey Pokémon can defend. A territorial species can tolerate another individual when the resource is abundant or no contested site is active.

## Canon approvals required before activation

1. Approve or reject Squawkabilly as a Marea population.
2. If approved, identify at least one actual local contested resource/site with Fletchling.
3. Approve/reject Wurmple and Swellow in a compatible Marea ecological cell.
4. Decide whether Sendero gains a wooded/forest-compatible microhabitat; only then evaluate Taillow's explicit forest Wurmple relationship locally.
5. Keep Scatterbug deferred unless plant-resource ecology is being implemented in the same area.

## Mechanical readiness

The persistent matrix itself is world-state data and can be implemented before complete AutoPTU tactical AI.

VERIFIED/usable for reduced combat where already audited:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL/BLOCKING when rich interactions require them:
- full movement interactions;
- lifecycle/damage/status families;
- move/ability/item/Trainer Feature breadth;
- terrain/hazard/reaction breadth;
- complete AI tactical policy;
- semantic Minecraft/Cobblemon/Craftics world projection/playback.

Do not simulate an aerial chase, grapple escape, group reinforcement or environmental trap tactically unless the exact required contracts are verified.
