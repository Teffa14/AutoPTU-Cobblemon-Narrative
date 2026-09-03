# Seasonal migration, stopover and corridor scan — pass 218

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-03

## Scope and repository fit

The repository was inspected before writing, including the full current tree and the recent temporal-ecology, alarm-network and multi-solution traversal passes. Pass 216 already covers diel/activity windows and was corrected so ordinary time-conditioned species spawning reuses native Cobblemon spawn conditions rather than a parallel Ouros scheduler. Pass 217 covers physical route obstruction and multi-solution traversal. This pass fills a different gap: population-scale directional movement between sites over a seasonal or event window, temporary stopover use, bottlenecks, imperfect counts and conflicts between wildlife passage and human route use.

Nothing in this note canonizes a migrating species in Marea, exact migration dates, a new population, breeding behavior or a new cause for existing incidents.

## Public research reviewed

### Pokémon mass outbreaks — concentration is an observation, not an explanation

Official Pokémon Scarlet/Violet material defines a mass outbreak as many Pokémon of the same species appearing in one location and uses bounded event windows and locations. This provides a useful Pokémon-world precedent for temporary local concentration.

Reusable Ouros lesson: seeing many members of one species at a site is a world fact that still needs interpretation. A concentration can be migration, feeding, breeding, sheltering, displacement, a temporary resource pulse, or another cause. Ouros should not label it migration from headcount alone.

Sources:
- Pokémon.com, “Break the Ice in Pokémon Scarlet and Pokémon Violet Mass Outbreaks” (2025): https://www.pokemon.com/uk/pokemon-news/break-the-ice-in-pokemon-scarlet-and-pokemon-violet-mass-outbreaks
- Pokémon.com, “A Series of Mass Outbreaks Featuring Grass-, Ice-, Ground-, and Fire-Type Pokémon” (2025): https://www.pokemon.com/uk/news/a-series-of-mass-outbreaks-featuring-grass-ice-ground-and-fire-type-pokemon

The event-specific spawn bonuses and shiny rates are videogame mechanics and are not imported into Ouros.

### Seasonal routes can differ by direction and season

A 2026 GPS-tracking study of Greater Sand Plovers found different spring and autumn strategies, with spring and autumn using different broad pathways and stopover patterns. The same tracked population did not reduce to one fixed reversible route, and the Beibu Gulf could function as both a stopover bottleneck and a nonbreeding endpoint for different movements.

Reusable Ouros lesson: a migration profile needs direction, season/window and stopover role. “This population migrates through Sendero” is too coarse if northbound and return movement can differ.

Source:
- Xu et al., Ecology and Evolution (2026), “Seasonal Differences in Migration Routes and Stopover Use of Greater Sand Plovers Between Mongolia and the Beibu Gulf Revealed by GPS Tracking”: https://onlinelibrary.wiley.com/doi/10.1002/ece3.73914

### Stopovers are functional sites, not decorative waypoints

Research on mule deer migration shows that animals can retain fidelity to broad routes while changing movement rate, duration and stopover use around human development. In heavily developed contexts, stopovers can shift or be used for less time even when the larger migration continues.

Reusable Ouros lesson: a population can keep using a regional corridor while changing how long it remains at a particular Marea site. A stopover should record its function and evidence independently from the route itself.

Source:
- Wyckoff et al., Ecosphere (2018), “Evaluating the influence of energy and residential development on the migratory behavior of mule deer”: https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecs2.2113

### Disturbance can reduce corridor use non-linearly

A 2020 mule deer study using 15 years of movement data found declining migratory use as surface disturbance increased and identified a sharp decline beyond a study-specific disturbance level. The authors explicitly caution that thresholds can differ among regions, species and habitat types.

Reusable Ouros lesson: do not create a universal disturbance number. Ouros can accumulate evidence that a population tolerates, accelerates through, detours around or abandons a route segment, but the behavior profile must be population/site specific.

Source:
- Sawyer et al., Journal of Wildlife Management (2020), “Migratory Disturbance Thresholds with Mule Deer and Energy Development”: https://wildlife.onlinelibrary.wiley.com/doi/10.1002/jwmg.21847

### Human presence can make stopover quality species-specific

A shorebird stopover study measured different flight-initiation distances among species under pedestrian disturbance and used that evidence to reason about buffer zones. The important design point is the variance: different species reacted at different distances.

Reusable Ouros lesson: the existing Ouros tolerance architecture remains the correct layer. A passage event does not grant a universal “migration tolerance.” Population/species behavior, individual state, human-density context and actual Trainer behavior still determine response.

Source:
- Koch et al., Journal of Wildlife Management (2014), “Assessing anthropogenic disturbances to develop buffer zones for shorebirds using a stopover site”: https://wildlife.onlinelibrary.wiley.com/doi/10.1002/jwmg.631

### Severe disturbance can alter route and stopover choice

Tracking of Greater Spotted Eagles during the war in Ukraine found route deviations and fewer stopovers relative to prior years, with delayed arrival and increased likely energetic costs.

Reusable Ouros lesson: a major world event can alter movement without requiring the population to disappear. This supports long-term consequences from closures, construction, disasters or conflict while preserving uncertainty about whether the old route will resume later.

Source:
- British Trust for Ornithology, “Active European warzone impacts raptor migration”: https://www.bto.org/our-work/science/publications/papers/active-european-warzone-impacts-raptor-migration

### PTU community experience — make routes carry authored behavior

Public PTU GM discussion repeatedly warns that random route encounters can consume table time without advancing exploration. A 2024 exploration discussion instead describes wild Pokémon as active parts of maps, with territorial or ecological behavior and small local stories rather than entities waiting only to become battles. A separate route discussion recommends pre-authoring meaningful features/events when travel itself matters.

Reusable Ouros lesson: a migration corridor should create authored observations, conflicts, choices and consequences. It should not become a larger random encounter table.

Sources:
- r/PokemonTabletop, “Question for Exploration” (2024): https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9
- r/PokemonTabletop, “The wild/routes” (2024): https://www.reddit.com/r/PokemonTabletop/comments/1hlmhnx
- r/PokemonTabletop, “Are there any decent resources that can help me speed up the process of putting pokemon into Routes and encounter areas?” (2022): https://www.reddit.com/r/PokemonTabletop/comments/xckvjh

These discussions are community design evidence, not PTU rules authority.

## Proposed data structures

### `MIGRATION_PASSAGE_RECORD`

Proposed, not canon-approved.

```yaml
migration_passage_record:
  passage_id: null
  population_ref: null
  provenance_refs: []
  confidence: OBSERVED | SOURCE_BACKED | PROVISIONAL
  expected_window_ref: null
  observed_window_start: null
  observed_window_end: null
  direction: null
  route_segment_refs: []
  stopover_refs: []
  current_state: EXPECTED | ACTIVE | SHIFTED | COMPLETED | UNCERTAIN
  disturbance_refs: []
  human_use_conflict_refs: []
  count_estimate_refs: []
  interpretation_refs: []
```

This record expresses an authored/population-level movement hypothesis or observed episode. It does not spawn entities by itself.

### `STOPOVER_USE_RECORD`

```yaml
stopover_use_record:
  site_ref: null
  population_ref: null
  passage_ref: null
  observed_use: REST | FORAGE | WATER | SHELTER | STAGING | UNKNOWN
  evidence_refs: []
  first_observed_at: null
  last_observed_at: null
  human_activity_context: null
  disturbance_refs: []
  confidence: null
```

A stopover role can change between passage windows. A place used to rest in one season does not automatically retain that role forever.

### `PASSAGE_OBSERVATION`

```yaml
passage_observation:
  observation_id: null
  observer_ref: null
  site_ref: null
  timestamp: null
  population_ref: null
  direction_observed: null
  count_method: null
  raw_count: null
  duplicate_detection_risk: null
  observation_effort: null
  evidence_refs: []
  interpretation_refs: []
```

The raw count is evidence, not population size. Re-crossing, circling, repeated detections, incomplete visibility and multiple route branches can all separate a checkpoint count from abundance.

## Evidence rules

A local concentration does not prove migration.

Repeated directional passage can support a migration hypothesis, especially when it recurs across sites or windows, but exact origin/destination remain separate claims.

One familiar persistent individual moving with a larger group does not prove that its entire species or home population is migratory. Its authoritative identity/location state must permit participation.

A collective passage does not grant `Pack Mon`, permanent pack identity, shared initiative or combat coordination. Those are separate mechanical/social claims.

Failure to observe passage in one window is `ABSENCE_WITH_EFFORT`, not proof that migration ceased.

## Cobblemon/Ouros authority boundary

Pass 216's correction remains binding. Where ordinary seasonal availability can be represented using native Cobblemon conditions/rules available to the deployed version, Cobblemon should own generic spawn eligibility/weight. Ouros stores why a population is expected, passage provenance, route/stopover semantics, persistent identities and consequences.

This pass does not assume that the deployed Cobblemon version exposes a first-class calendar-season primitive. Exact season/calendar mapping must be verified before implementation. If the desired window cannot be expressed natively, use an approved server/world-state gate rather than silently duplicating the entire Cobblemon spawning system.

Persistent canonical individuals remain identity-owned by Ouros and must never be duplicated because a generic population spawn becomes eligible.

## PTU/Caelo/Kairos boundary

Migration is primarily world/ecology state. It does not create a PTU bonus, Status, movement capability or battle behavior by itself.

Before any mechanically rich passage encounter is approved, project-source authority still needs exact checks for movement capabilities, Athletics/Acrobatics/Survival where Trainers physically traverse or assist, Stealth/detection, capture, Features/Edges affecting wild interaction, interception/forced movement, hazards, weather and relevant Caelo/Kairos overrides.

The existing rule remains: species behavior -> population/context -> individual state/capabilities -> observed Trainer behavior -> verified mechanics -> legal options -> tactical choice. A migrating individual can have different priorities, but it cannot perform an action it does not mechanically possess.

## Research outcome

Seasonal movement can become a long-lived regional system rather than a scripted spectacle. A route can matter for delivery, research, safety and wildlife at the same time. Players can learn a passage, notice that it shifted, protect a stopover, challenge a bad count, or deliberately yield space without requiring every encounter to become combat. The key design unit is a provenance-backed movement episode connecting population, route segments, stopovers and observations.