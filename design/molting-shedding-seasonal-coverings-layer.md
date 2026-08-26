# Molting, Shedding & Seasonal Coverings Layer

Status: PROPOSED systems design. Not established Ouros canon.

## Purpose

This layer records reversible or cyclical replacement of body coverings and closely related visible structures when that change matters to Chronicle, research, welfare, tracking, material provenance or public knowledge.

It does not decide PTU Forms, Evolution, Abilities, Status cures or stats.

## Authority boundary

This layer owns:

- molt/shedding episodes;
- observed coat, plumage, skin, scale or authored seasonal-covering states;
- episode timing and uncertainty;
- shed-material provenance before handoff;
- site-use observations specifically associated with the episode;
- population-level molt phenology summaries derived from evidence.

Other authorities remain authoritative for:

- Evolution/Form mechanics: Evolution/Life Stage;
- daily activity/rest: Diel Activity;
- broad seasonal timing and phenology: Seasonality;
- diagnosis/welfare: Care;
- samples and scientific interpretation: Science/Research Ethics;
- traces found in the field: Field Signs;
- photographs: Visual Records;
- physical collected objects: Material Culture/Museums;
- species classification: Taxonomy;
- PTU Ability execution: AutoPTU.

## Core separation

```text
persistent pokemon_entity_id
        ↓
authored biological covering profile
        ↓
observed episode or state
        ↓
observation / photo / shed material
        ↓
episode assessment
        ↓
phenology comparison or site-use inference
        ↓
possible handoff to Care / Science / Field Signs / Material Culture
```

A Form change is a separate authoritative transition.

## Persistent records

### Covering profile

```yaml
covering_profile:
  profile_id: null
  species_or_population_ref: null
  pokemon_entity_id: null
  covering_kind: null
  authored_cycle_kind: unknown
  expected_window_ref: null
  source_refs: []
  confidence: proposed
```

Possible `covering_kind` values are descriptive only: fur, feathers, skin, scales, foliage-like ornament, shell-associated covering, other_authored.

Do not create a profile because an animal analogue suggests one should exist.

### Molt/shedding episode

```yaml
covering_episode:
  episode_id: null
  pokemon_entity_id: null
  population_ref: null
  covering_profile_ref: null
  episode_kind: null
  earliest_start: null
  latest_start: null
  earliest_end: null
  latest_end: null
  stage: unknown
  location_refs: []
  observation_refs: []
  shed_material_refs: []
  welfare_handoff_ref: null
  authoritative_form_event_ref: null
  provenance_refs: []
```

Suggested stage vocabulary:

`PRE_CHANGE`, `ACTIVE_PARTIAL`, `ACTIVE_ADVANCED`, `APPARENTLY_COMPLETE`, `INTERRUPTED_OR_UNKNOWN`, `UNRESOLVED`.

These stages are observational. They do not change battle state.

### Covering observation

```yaml
covering_observation:
  observation_id: null
  observer_id: null
  pokemon_entity_id: null
  population_ref: null
  observed_at: null
  location_id: null
  method: direct_visual
  covering_description: null
  apparent_stage: unknown
  effort_ref: null
  image_ref: null
  confidence: null
  notes: null
```

A photograph can support the observation while Visual Records remains owner of image provenance.

### Shed material occurrence

```yaml
shed_material_occurrence:
  occurrence_id: null
  found_at: null
  location_id: null
  material_kind: null
  suspected_source_taxon_ref: null
  suspected_pokemon_entity_id: null
  identity_confidence: unresolved
  field_sign_ref: null
  collection_authorization_ref: null
  material_instance_ref: null
  sample_ref: null
  provenance_refs: []
```

If collected, the physical material hands off to Material Culture or scientific sample systems. If left in place, it can remain a Field Sign observation.

## Individual identity

Molt never creates a new Pokémon identity.

The same `pokemon_entity_id` persists before, during and after the episode.

A new coat, plumage, skin or visible ornament cannot be used to create a duplicate entity when the individual is otherwise known.

## Form-change handoff

Some Pokémon have authoritative seasonal Forms.

When the rules/canon says the Form changed:

1. Evolution/Form authority performs or records the Form transition.
2. This layer may record associated observable covering changes.
3. Any battle Ability or mechanical consequence is re-queried from authoritative mechanics.

The narrative layer never selects the Form from temperature, Minecraft biome, date or appearance alone.

## PTU `Shed Skin` boundary

Biological shedding and the Ability named `Shed Skin` are different systems.

A world-state molt:

- does not cure Poisoned, Burned, Paralysis or any other Status;
- does not trigger an Ability use;
- does not consume or reset Ability frequency;
- does not grant immunity;
- does not alter battle timing.

If AutoPTU executes `Shed Skin`, that result remains a battle-mechanics event. Narrative may later describe it only if the authoritative transcript exposes a suitable event.

## Seasonal Ability boundary

A species may have PTU mechanics whose text refers to seasons. That is not implemented here.

Season state should be supplied from the authoritative world calendar only when the PTU engine explicitly requests it through a future adapter contract. The adapter must not translate a visible coat into a mechanical season or Ability.

## Population phenology

A population summary can track timing without pretending every individual changes together.

```yaml
molt_phenology_revision:
  revision_id: null
  population_ref: null
  season_or_year_ref: null
  observation_window: null
  sample_size_or_effort_ref: null
  early_stage_band: null
  peak_stage_band: null
  completion_band: null
  comparability_notes: null
  uncertainty_notes: null
  source_refs: []
```

A later revision does not rewrite prior observations.

## Site use

A molt site may be important because individuals spend more time resting, hauled out, sheltered or otherwise observable there.

Do not infer:

- nest;
- territory;
- ownership;
- sacred status;
- breeding site;
- permanent habitat;
- capture availability.

Any access restriction must come from Conservation, Land Tenure, public-safety or another existing authority.

## Welfare handoff

A rough, patchy or incomplete appearance may be normal or concerning.

This layer records appearance. Care decides whether there is a welfare concern.

The narrative generator may create a welfare question such as “is this normal molt or something else?” but must not diagnose from appearance alone.

## Material provenance

Shed fur, feathers, skins or analogous authored material may become scientifically or culturally meaningful.

Collection requires an explicit authorization path where relevant. A discovered piece does not create ownership or research consent.

Potential handoffs:

- Field Signs for in-situ evidence;
- Science for sampling;
- Museums for accessioned historical material;
- Material Culture for a persistent object;
- Textiles only when canon explicitly allows ethical/material use.

## Minecraft projection

Minecraft/Cobblemon may show:

- model/texture variation supplied by authoritative state;
- particles or decorative traces;
- temporary site dressing;
- visual markers of an observation.

Minecraft may not decide:

- biological stage;
- completion;
- species identity from dropped items;
- welfare;
- Form;
- seasonal PTU mechanics;
- population size;
- sample provenance.

Chunk unload/despawn has no biological meaning.

## Offline advancement

Routine episodes may advance offline only when their transition policy is authored and no player-controlled irreversible decision is involved.

For important persistent individuals, uncertain episodes should remain interval-based rather than inventing exact start/end times while unobserved.

## Encounter design contracts

### Molt-Site Access Disturbance

Narrative premise: a seasonal concentration site becomes temporarily disturbed while researchers or visitors are present.

FULL version:

- wildlife can withdraw through dynamic routes;
- civilians/researchers can evacuate;
- protected lanes matter;
- objectives include `WITHDRAW`, `EVACUATE`, `PROTECT_ROUTE`, `CLEAR_ROUTE`;
- environmental conditions may influence tactical space only when exact mechanics are validated.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if tactical environment is used;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

Suspend the survey, evacuate civilians, resolve wildlife withdrawal in world state and freeze a static legal arena. AutoPTU receives only actual combatants. The episode remains ecologically unresolved until follow-up observations occur.

### Shed-Skin Identity Survey

Narrative premise: several shed skins appear along a watercourse and may belong to one persistent Pokémon or several individuals.

Preferred implementation: non-combat investigation using Field Signs, Taxonomy, Visual Records, Science and possibly Telemetry. No battle-engine dependency is required.

If a separate confrontation occurs, use a static battle and do not let the result answer the identity question.

### Seasonal Crossing During Active Coat Change

Narrative premise: a road/rail crossing coincides with a short seasonal period when a local population changes site use.

FULL version depends on complete movement, tactical AI and adapter/playback for dynamic crossing/withdrawal. Environment is BLOCKING only if weather or road conditions have tactical effects.

REDUCED version stops traffic in world state, completes the crossing outside the grid, then resolves any independent conflict in a static arena.

## Generator guardrails

Never infer:

- `Shed Skin` Ability from a visible shed;
- Status cure from biological molt;
- Evolution readiness from shed frequency;
- age from coat alone unless an authored validated method exists;
- illness from messy plumage;
- population decline from lower molt-site counts without effort/detectability review;
- capture eligibility from reduced mobility or aggregation;
- Form from season-like appearance;
- mechanical season from Minecraft biome;
- rare loot from shed material.

## Canon questions left open

- Which Ouros species/populations have authored molt/shedding cycles?
- Which are mechanical Forms and which are only biological appearance?
- Are any recurrent molt sites known at campaign start?
- Which institutions monitor them?
- Can any shed materials be collected, studied, traded or exhibited?
- What privacy/protection rules apply to sensitive sites?
- Does Caelo alter PTU `Shed Skin`, `Seasonal`, Form rules or season definitions?

Until answered, all examples remain PROPOSED.