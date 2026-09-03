# Nesting, parental care and disturbance scan — pass 219

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-03

## Scope

The repository was inspected before writing, including the full recursive file tree and recent layers for wild tolerance, Trainer approach, alarm propagation, temporal ecology, traversal obstacles and seasonal passage. Searches for dedicated nesting, breeding, egg, juvenile and parental-care layers returned no established system. This pass fills that gap without assigning a breeding population, nest, egg, juvenile or new species to Marea canon.

The goal is to make reproductive-site context meaningful while preserving the existing behavior model: species/population evidence, local context, individual state and capabilities, observed Trainer behavior, verified PTU effects, legal actions, tactical selection, AutoPTU resolution and Minecraft/Cobblemon playback.

## Public material reviewed

### PTU community encounter practice

A public r/PokemonTabletop discussion about storytelling encounters includes a GM example where a pair of Talonflame occupied a building, defended a nest and egg, and the problem was resolved by relocating the animals rather than treating the scene as a mandatory battle. The same discussion contains examples of Fletchling defending a berry tree and groups whose ecological behavior gave players reasons to observe or help instead of capture.

Reusable Ouros lesson: reproductive or home-site context can change the objective of an encounter. A defensive Pokémon should not automatically be authored as generally aggressive, and resolution can involve space, relocation, withdrawal, observation or institutional response.

Source:
- r/PokemonTabletop, “Pokemon Encounters (A Storytelling)” (2023): https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5/

### Pokémon nesting behavior varies by species and habitat

Published Pokédex material summarized by Bulbapedia describes very different nesting relationships. Trapinch constructs a sloped sand pit that is simultaneously nest, hunting structure and physical hazard. Gible uses horizontal holes in cave walls, with geothermal warmth forming part of the habitat relationship. Nincada builds underground nests around tree roots and can remain below ground for long periods.

Reusable Ouros lesson: `nest` cannot mean one generic circular protected zone. Species can construct, occupy or depend on sites for different functions. Geometry, substrate, temperature, concealment, feeding strategy and movement capabilities can matter before any combat mechanic exists.

Sources:
- Trapinch: https://bulbapedia.bulbagarden.net/wiki/Trapinch_(Pok%C3%A9mon)
- Gible: https://bulbapedia.bulbagarden.net/wiki/Gible_(Pok%C3%A9mon)
- Nincada: https://bulbapedia.bulbagarden.net/wiki/Nincada
- Trapinch underground labyrinth: https://bulbapedia.bulbagarden.net/wiki/Trapinch_underground_labyrinth

The anime-exclusive Trapinch labyrinth also provides a useful high-level structure: an apparently dangerous environmental formation can be part of a species' normal life cycle and a research site rather than a malicious dungeon trap. Ouros should preserve that ambiguity until evidence establishes cause and function.

### Human disturbance changes parental behavior

A 2026 study covering 83 nests across 30 migratory bird species found that human presence, vehicle traffic and noise affected parental return and visitation, with response also depending on nesting stage and habitat openness. The result is useful because it rejects a universal disturbance threshold.

Reusable Ouros lesson: an adult being absent from a nest after disturbance does not prove abandonment. Trainer presence can itself change what the observer sees. Observation records therefore need effort, disturbance context and stage uncertainty.

Source:
- Saini et al., Ornithological Applications, “Human and vehicle disturbance reduces nest attendance in migratory birds during pipeline construction activities” (2026): https://doi.org/10.1093/ornithapp/duag057

### Static and moving humans can produce different responses

Weston, Ehmke and Maguire compared static and mobile human disturbance around incubating hooded plovers. Return behavior differed strongly between treatments.

Reusable Ouros lesson: `human nearby` is too coarse. Stopping beside an occupied site, passing through, approaching directly, lingering, operating machinery or withdrawing can be different behavioral inputs.

Source:
- Weston et al., Journal of Wildlife Management, “Nest return times in response to static versus mobile human disturbance” (2011): https://doi.org/10.1002/jwmg.7

### Defense depends on perceived threat

Research on Northern Bobwhite nest defense found that parental decisions were related to the threat posed by an approaching predator rather than a fixed always-defend rule. Research on urban Masked Lapwings likewise found different responses to different human stimuli, showing that animals can discriminate between activities rather than reacting only to distance.

Reusable Ouros lesson: parental defense belongs inside the existing capability-aware behavioral policy. The system should evaluate what the approaching Trainer is doing, what routes remain, the actual capabilities of the adult and the current dependent-site context.

Sources:
- Ellison & Ribic, Ornithology, “Fight or Flight: Parental Decisions about Predators at Nests of Northern Bobwhites” (2013): https://academic.oup.com/auk/article/130/4/637/5148963
- Weston et al., Animals, “Swooping in the Suburbs; Parental Defence of an Abundant Aggressive Urban Bird against Humans” (2013): https://www.mdpi.com/2076-2615/3/3/754

### Buffers are contextual management decisions

Canadian federal guidance for occupied migratory-bird nests recommends adapting, rescheduling or relocating disruptive activity and explicitly states that suitable buffer distances vary by species tolerance, previous exposure, disturbance level and landscape context. A recent Least Tern study similarly reports stronger responses to direct pedestrian approaches than passing vehicles, with colony size and presence of eggs or chicks affecting disturbance response.

Reusable Ouros lesson: Marea institutions can create temporary access buffers, but a buffer should be a stewardship decision backed by observations rather than a magical aggro radius. It may be revised as evidence changes.

Sources:
- Environment and Climate Change Canada, “Guidelines to avoid harm to migratory birds”: https://www.canada.ca/en/environment-climate-change/services/avoiding-harm-migratory-birds/reduce-risk-migratory-birds.html
- Ornithological Applications, “Breeding Sternula antillarum disturbance distances and duration of escape behaviors” (2025): https://academic.oup.com/condor/article/127/3/duaf026/8112800

## Proposed data structures

### `DEPENDENT_SITE_RECORD`

Proposed, not canon-approved.

```yaml
dependent_site_record:
  site_record_id: null
  location_ref: null
  occupant_population_ref: null
  occupant_individual_refs: []
  species_identification: CONFIRMED | PROVISIONAL | UNKNOWN
  evidence_refs: []
  site_function: NEST | ROOST | DEN | NURSERY | EGG_SITE | UNKNOWN
  dependent_stage: EGG | HATCHLING | JUVENILE | UNKNOWN | NONE_OBSERVED
  activity_status: SUSPECTED_ACTIVE | CONFIRMED_ACTIVE | INACTIVE | UNKNOWN
  disturbance_refs: []
  access_decision_refs: []
  first_observed_at: null
  last_verified_at: null
  notes: []
```

A site can be recorded before the species or reproductive stage is known. `NONE_OBSERVED` means no dependent was observed during that effort; it does not prove absence.

### `DEPENDENT_SITE_OBSERVATION`

Proposed, not canon-approved.

```yaml
dependent_site_observation:
  observation_id: null
  site_record_ref: null
  timestamp: null
  observer_ref: null
  approach_mode: PASSING | DIRECT | STATIC | WORK_ACTIVITY | REMOTE | UNKNOWN
  minimum_observed_distance: null
  line_of_sight_context: null
  adult_presence: PRESENT | ABSENT_DURING_EFFORT | UNKNOWN
  dependent_evidence: null
  warning_or_defense_evidence: []
  withdrawal_or_return_evidence: []
  human_traffic_context: null
  observation_effort: null
  interpretation_refs: []
```

This structure separates facts from interpretations such as `abandoned`, `defending young` or `habituated`.

### `TEMPORARY_WILDLIFE_BUFFER`

Proposed institutional/world-state record.

```yaml
temporary_wildlife_buffer:
  buffer_id: null
  site_record_ref: null
  authority_ref: null
  geometry_ref: null
  start_condition: null
  review_condition: null
  allowed_activity_classes: []
  restricted_activity_classes: []
  evidence_refs: []
  status: PROPOSED | ACTIVE | EXPIRED | REVISED
```

The buffer is an access/stewardship decision. It does not directly modify PTU accuracy, movement, capture chance or aggression.

## Behavioral integration

Dependent-site context is another input to the established wild-behavior policy, not a replacement policy.

```text
species/population prior
+ dependent-site context and evidence
+ human-pressure / temporal / local context
+ persistent individual state and capabilities
+ observed Trainer actions and approach
+ verified Skills / Features / Edges / Moves / Items
-> legal behavior options
-> tactical intent and action selection
-> AutoPTU resolution when mechanics are structured
-> Minecraft/Cobblemon/Craftics playback
```

Possible intent changes can include heightened alert, warning, withdrawal, return-route preservation, obstruction, distraction, guarding or engagement, but none is guaranteed merely because a nest exists.

## Canon and rules boundary

CANON-APPROVED constraints preserved:

- Existing Marea and Sendero geography, institutions and population records remain unchanged.
- The persistent Sendero Fletchling keeps its frozen mechanical identity and receives no parental role from this pass.
- Existing wild-behavior, alarm, temporal-spawn and persistent-identity boundaries remain in force.
- Cobblemon continues to own generic natural spawn eligibility/weight where its native conditions apply; Ouros does not create a parallel spawn scheduler.
- AutoPTU remains the authority for PTU legality and tactical resolution.

PROPOSED:

- the three records above;
- reproductive/dependent-site context as a behavior input;
- evidence-backed temporary wildlife buffers;
- encounter seeds developed in the paired proposal file.

UNCERTAIN:

- whether Sendero or another current Marea site should receive the first canon dependent site;
- which species should establish it;
- exact breeding season or reproductive schedule;
- exact PTU/Caelo/Kairos mechanics for identifying eggs/young, Pokémon Education, Survival/Intuition observation, calming, handling, capture, restraint or protection actions.

The repository search did not locate a current project-side rule extraction that is sufficient to authorize those exact mechanics, so this pass deliberately assigns no DC, bonus, action cost or Feature effect.

## Guardrails

A nest or egg does not become loot because the player discovered it.

An unattended egg or juvenile does not prove abandonment. One observation can be distorted by the observer's own presence.

A defensive adult does not establish species-wide aggression.

A temporary buffer does not create an invisible combat zone or PTU penalty.

A generic Cobblemon spawn cannot create the canonical parent of a specific dependent record unless Ouros explicitly binds that entity identity.

A Move animation or Minecraft pathing event cannot decide that a dependent was harmed, rescued, captured or displaced when the consequence requires PTU/world authority.

## Research outcome

Nesting and dependent care give Ouros a way to turn ordinary routes and structures into temporary ecological problems without fabricating villains or mandatory battles. The strongest design consequence is epistemic: Trainers can disturb the evidence they are trying to understand. That makes approach, waiting, retreat, route management and repeated observation meaningful actions before combat begins.