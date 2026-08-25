# Community Science and Participatory Monitoring Protocol

Status: PROPOSED SYSTEM / NON-CANON
Pass: 166
Date: 2026-08-25

## Scope

This protocol owns the provenance and quality workflow for observations contributed by people outside a dedicated scientific staff role, including structured volunteers, students, clubs, visitors, local naturalists, Trainers responding to an institutional call, and other public participants.

It does not own ecological truth, taxonomy, research ethics, photography, actor identity, battle rules, capture authority, migration, population estimates, or scientific publication.

## Authority boundary

Authoritative chain:

`program definition -> participation event/effort -> submission -> evidence/source linkage -> validation/review -> quality state -> aggregate product -> handoff to domain science`

Existing systems remain authoritative for their content:

- Research Ethics decides participant/subject protection, site authorization, secondary use, and sensitive information.
- Visual Records owns photographs and image provenance.
- Taxonomy owns identification/classification determinations.
- Identity owns contributor identity and aliases.
- Metrology and Timekeeping own instrument/time correction.
- Telemetry and Remote Sensing own their instrument products.
- Domain layers own biological, ecological, hydrological, health, geological, or institutional interpretation.
- Science/publication systems decide research conclusions and publication state.

## Core records

### `COMMUNITY_MONITORING_PROGRAM`

Persistent identity for an organized public-observation program.

Suggested fields:

- `program_id`
- `name`
- `sponsoring_institution_ids`
- `purpose`
- `domain_authority`
- `start_date`
- `end_date_or_open`
- `status`
- `accepted_methods`
- `training_material_revision_ids`
- `review_policy_revision_id`
- `privacy_policy_revision_id`
- `sensitive_location_policy_id`
- `public_output_policy`

The program never grants a Trainer Class, Skill rank, credential, field-access right, or capture permission merely through participation.

### `PARTICIPATION_CAMPAIGN`

A bounded count, BioBlitz, school term, migration weekend, annual survey window, or other coordinated episode within a program.

Suggested fields:

- `campaign_id`
- `program_id`
- `time_window`
- `target_geography`
- `target_taxa_or_phenomena`
- `method_revision_id`
- `planned_effort`
- `actual_effort_summary`
- `weather_or_access_context_refs`
- `known_coverage_gaps`
- `status`

### `OBSERVATION_EFFORT_RECORD`

Captures what the observer attempted to observe rather than only what was found.

Suggested fields:

- `effort_id`
- `program_id`
- `contributor_id_or_private_ref`
- `method`
- `start_time_raw`
- `end_time_raw`
- `corrected_time_ref`
- `route_or_station_ref`
- `distance_or_area_if_known`
- `search_duration`
- `observer_count`
- `complete_reporting_claim`
- `target_scope`
- `equipment_refs`
- `access_constraints`
- `notes`

A complete effort with no detections is still an observation record. A casual absence of reports is not.

### `OBSERVATION_SUBMISSION`

Immutable submitted claim plus attached evidence references.

Suggested fields:

- `submission_id`
- `program_id`
- `effort_id_optional`
- `submitted_by`
- `submitted_at`
- `observed_at_raw`
- `location_authoritative`
- `public_location_revision_id`
- `claimed_subject_or_taxon`
- `count_or_quantity_claim`
- `behavior_claim`
- `evidence_refs`
- `source_submission_refs`
- `free_text_notes`
- `submission_revision_parent_optional`

The original submission remains preserved even after correction.

### `SOURCE_DEPENDENCY_LINK`

Records when several submissions rely on the same underlying photograph, audio clip, observer group, copied note, broadcast, or social post.

Suggested relationships:

- `INDEPENDENT_AS_KNOWN`
- `SAME_FIELD_PARTY`
- `SHARED_MEDIA_SOURCE`
- `REPOST_OR_DERIVATIVE`
- `DERIVED_FROM_PUBLIC_REPORT`
- `DEPENDENCY_UNRESOLVED`

Source dependency affects aggregation confidence but never erases the social history of the duplicate reports.

### `VALIDATION_REVIEW`

A review event performed under a named policy revision.

Possible outcomes:

- `NOT_REVIEWED`
- `AUTO_CHECK_PASSED`
- `PENDING_DOCUMENTATION`
- `EXPERT_REVIEW_PENDING`
- `VALID_FOR_SCOPE`
- `VALID_BUT_COARSE`
- `DUPLICATE_SOURCE`
- `IDENTIFICATION_REVISED`
- `INSUFFICIENT_FOR_PRODUCT`
- `REJECTED_FOR_SPECIFIED_REASON`
- `UNRESOLVED`

Review is not discipline. No negative reputation, wrongdoing, sanction, or dishonesty inference follows automatically.

### `QUALITY_ASSESSMENT`

A scoped assessment of how the record may be used.

Possible dimensions:

- spatial precision
- temporal precision
- method completeness
- effort known/unknown
- identification confidence
- count confidence
- independence/source dependence
- evidence availability
- privacy restrictions
- suitability for presence-only products
- suitability for occupancy/non-detection products
- suitability for abundance/index products

A record can be strong for one use and weak for another.

### `COVERAGE_REVISION`

Describes where and when the program had meaningful observation opportunity.

Coverage can be partitioned by:

- geography
- time of day
- season
- habitat
- accessibility
- transport availability
- observer expertise
- taxonomic focus
- weather
- event attendance
- method

Coverage must never be inferred from loaded Minecraft chunks or visible entities.

### `SENSITIVE_LOCATION_PRESENTATION`

Stores the difference between authoritative and publishable location.

Possible public treatments:

- exact
- rounded/coarse
- obscured region
- delayed publication
- private to program staff
- restricted to named projects

The underlying observation may remain scientifically valid while public coordinates are withheld.

### `AGGREGATE_PRODUCT`

A derived map, checklist summary, seasonal dashboard, count report, hotspot layer, phenology chart, or other program product.

Suggested fields:

- `product_id`
- `program_id`
- `input_submission_query`
- `method_revision`
- `quality_filters`
- `coverage_revision_ids`
- `source_dependency_handling`
- `privacy_transform`
- `generated_at`
- `supersedes_product_id_optional`
- `limitations`

An aggregate product never becomes raw world truth.

### `CORRECTION_EVENT`

Preserves later changes to identification, time, location, count, duplicate status, or review state.

A correction creates a new interpretive revision while the original submission remains in history.

## Important distinctions

### Submission versus observation truth

A submission proves that an actor reported something. It does not by itself prove the reported organism, count, identity, behavior, cause, or location.

### Many submissions versus many independent detections

A viral photograph can produce hundreds of reports while containing one underlying observation. Group walks can generate several valid uploads of the same individual. Aggregation must account for source dependency.

### Presence versus abundance

A high number of reports can reflect high observer effort, a popular trail, an event, a famous Pokémon, better transit, better cameras, or an easier-to-identify species. Domain science decides whether an abundance inference is justified.

### No report versus non-detection

No public report means only no qualifying report was received. A structured effort that explicitly reports a complete checklist can support a scoped `NOT_DETECTED` record.

### Contributor expertise versus authority

A contributor can become historically accurate, locally knowledgeable, or highly trusted without acquiring a mechanical Skill, institutional credential, or universal authority.

### Validation versus taxonomy

Review may flag or route an identification. Taxonomy remains the authority for formal species/form determinations and revisions.

### Public map versus exact coordinates

Public products can intentionally obscure a sensitive site. Minecraft map markers and client waypoints must never recover or override restricted coordinates.

## Bias and coverage model

Every aggregate should be able to preserve known observation biases such as:

- access-road concentration
- urban concentration
- weekend/event concentration
- daylight-only effort
- photography-friendly species
- charismatic/rare-species reporting
- expert specialization
- school-route repetition
- seasonal tourism
- language/interface barriers
- weather-related cancellations
- transit outages
- accessibility exclusions
- viral-interest spikes

The default interpretation is not that these biases invalidate the data. They define what questions the data can answer safely.

## Pokémon-specific protections

- A participant sighting does not change capture eligibility.
- A rare sighting does not create a spawn.
- A public location does not create a waypoint to a persistent Pokémon.
- Repeated reports of the same persistent Pokémon do not create clones or population abundance.
- A photo does not override `pokemon_entity_id` linkage rules.
- A nickname does not prove individual identity.
- A participant feeding or baiting Pokémon must be recorded as disturbance/method context where relevant; it does not become a neutral observation automatically.
- A participant cannot convert a nest, Egg, juvenile, rehabilitation release, or telemetry target into public property through documentation.

## PTU mechanical boundary

Community participation grants no automatic:

- Researcher class
- Pokémon Education rank
- General Education rank
- Perception rank
- Chronicler Feature
- Trainer Feature/perk
- XP
- Tutor Points
- item reward
- capture bonus
- identification bonus
- initiative/Accuracy bonus

If a character independently possesses a PTU mechanic that affects observation or research, the authoritative PTU implementation may be referenced only when that exact mechanic is verified. This protocol never synthesizes one from narrative participation.

## Minecraft/Cobblemon boundary

Allowed projection examples:

- public notice boards
- scheduled count events
- coarse observation maps
- observer NPCs
- field notebooks
- marked survey stations
- non-authoritative UI showing submissions/review state

Forbidden authority shortcuts:

- loaded entity count -> abundance
- minimap marker -> scientific observation
- entity despawn -> absence
- server log -> participant observation unless explicitly ingested as another method
- block placement -> official survey station
- client screenshot -> validated record without provenance
- public map -> exact sensitive coordinate
- player nearby -> observation effort automatically occurred

## Encounter contracts

### BioBlitz Trail Closure — FULL

Narrative premise: a scheduled public biodiversity count overlaps with a route closure and unexpected wildlife movement. The objective is to keep participants safe, preserve the survey’s provenance, and avoid turning the animals into combat objectives.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED for an ordinary battle portion.
- base movement legality: VERIFIED.
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING when participants or wildlife must CROSS/WITHDRAW through contested space.
- core calculations: VERIFIED.
- action economy/initiative: VERIFIED.
- full turn/round lifecycle: PARTIAL.
- full stateful damage pipeline: PARTIAL.
- status lifecycle: PARTIAL when exact statuses are invoked.
- terrain/weather/hazards/zones/reactions: BLOCKING if the closure, terrain, weather, or protected corridor has tactical effects.
- move-specific behavior: PARTIAL for exact Moves beyond verified contracts.
- abilities: PARTIAL.
- items: PARTIAL if tactical equipment is introduced.
- Trainer Features/perks: PARTIAL if exact Features are invoked.
- AI legal-action infrastructure: VERIFIED.
- AI tactical policy: BLOCKING for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_PARTICIPANT`, or non-hostile wildlife goals.
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

REDUCED: suspend the count in world state, remove participants and moving wildlife from the grid, preserve submitted records up to the interruption, and run only an independent static battle if one remains.

### Rare Sighting Crowd Surge — FULL

Narrative premise: a validated but sensitive observation spreads publicly and attracts a crowd near a wildlife site.

FULL requires complete movement, tactical AI, and adapter/playback for crowd routing and wildlife withdrawal. Environmental family is required only if real tactical terrain/weather/hazard effects exist.

REDUCED: Community Science changes public location precision, Public Space reroutes visitors, wildlife movement resolves outside battle, and any independent confrontation occurs in a static arena. Battle victory never validates the sighting or grants capture access.

### Community Sensor Retrieval — FULL

Narrative premise: volunteers need to recover a simple program device or data logger after a storm while keeping the record chain intact.

FULL requires complete movement for technician traversal, AI tactical policy for `REACH_DEVICE`, `PROTECT_TECHNICIAN`, `WITHDRAW`, and adapter/playback. Environmental family is BLOCKING if storm debris, water, unstable ground, or protected zones matter tactically.

REDUCED: world state handles device custody, technician movement, and diagnosis. A static battle nearby may occur separately. Retrieval and validation happen after combat.

### Observation Review Night

Primarily non-combat. Possible outcomes include `VALID_FOR_SCOPE`, `DUPLICATE_SOURCE`, `IDENTIFICATION_REVISED`, `INSUFFICIENT_FOR_PRODUCT`, and `UNRESOLVED`. No battle result can settle scientific review.

## Longitudinal behavior

A community program should be able to improve over years through better training material, broader access, new survey stations, translation, accessibility, reviewer capacity, and correction of old records.

Success can mean fewer adventure hooks. A mature network may recognize a normal seasonal pattern, catch a duplicate rumor early, or flag a coverage gap before anyone assumes ecological collapse.

## Canon status

This protocol is PROPOSED and NON-CANON. It introduces no named Ouros institution, technology platform, volunteer organization, research credential, or preexisting monitoring program until approved.