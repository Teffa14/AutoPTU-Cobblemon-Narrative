# Fisheries Stock Assessment, Effort & Release Monitoring Protocol — Pass 157

Status: PROPOSED SYSTEMS EXTENSION. Not canon.

Authority note: `design/fisheries-angling-aquaculture-layer.md` from Pass 70 remains the Fisheries authority. This protocol extends its `FISHING_EFFORT_RECORD`, `CATCH_OBSERVATION`, `STOCK_ASSESSMENT`, `MANAGEMENT_MEASURE` and `BYCATCH_OR_NON_TARGET_EVENT` concepts. It does not create a second fishery layer.

## Purpose

Pass 70 established the correct high-level separation between population state, fishing effort, catch, capture, release, harvest, aquaculture and management. This protocol deepens the evidence lifecycle needed when Ouros wants to compare years, institutions or methods without turning catch records into population truth.

Use this evidence chain:

`raw activity record -> effort context -> standardized index when justified -> independent survey -> biological/ecosystem evidence -> assessment revision -> review state -> management interpretation`

Management remains downstream of evidence:

`assessment/other evidence -> institutional decision -> scoped measure -> monitoring -> later review`

## 1. Evidence source class

Every Fisheries observation used in an assessment should state how it entered the system.

```yaml
fishery_evidence_source:
  source_id: null
  source_class: null
  institution_or_actor_refs: []
  method_ref: null
  sampling_scope_ref: null
  coverage_ref: null
  effort_ref: null
  quality_flags: []
  source_refs: []
```

Candidate source classes:

- FISHERY_DEPENDENT_LANDING
- FISHER_LOG
- RECREATIONAL_ACTIVITY_SURVEY
- ONBOARD_OR_SITE_OBSERVER
- FISHERY_INDEPENDENT_SURVEY
- CAMERA_OR_IMAGING_SURVEY
- ACOUSTIC_OR_REMOTE_SURVEY
- BIOLOGICAL_SAMPLE
- MIGRATION_OBSERVATION
- COMMUNITY_LONGITUDINAL_OBSERVATION
- ARCHIVAL_RECORD
- UNKNOWN

Source class describes provenance, not automatic reliability rank.

## 2. Effort normalization

Pass 70's `FISHING_EFFORT_RECORD` should remain the raw effort authority. A derived catch/effort index is a separate versioned interpretation.

```yaml
catch_effort_index_revision:
  index_revision_id: null
  fishery_id: null
  period_ref: null
  source_effort_record_refs: []
  source_catch_observation_refs: []
  effort_definition_ref: null
  standardization_method_ref: null
  spatial_scope_ref: null
  environmental_covariate_refs: []
  gear_or_method_refs: []
  index_band: null
  uncertainty: null
  caveat_refs: []
  supersedes_revision_id: null
```

Do not derive this from Minecraft casts or loaded entities.

Important confounders:

- gear/method revision;
- different fishing locations;
- schooling/aggregation;
- route/access changes;
- weather/water state;
- experience/technology;
- reporting coverage;
- changed target preference;
- seasonal timing.

## 3. Independent survey extension

Pass 70 allows stock observations. Add a specific object when an institution conducts a standardized survey outside ordinary fishing activity.

```yaml
fishery_independent_survey:
  survey_id: null
  fishery_id: null
  method_ref: null
  design_revision_ref: null
  period_ref: null
  station_or_transect_refs: []
  effort_ref: null
  observation_refs: []
  environmental_context_refs: []
  coverage_assessment: null
  limitations: []
  source_refs: []
```

Possible coverage states:

- REPRESENTATIVE_FOR_DEFINED_SCOPE
- PARTIAL
- WEATHER_LIMITED
- ACCESS_LIMITED
- METHOD_LIMITED
- INTERRUPTED
- UNKNOWN

`NO_DETECTION` in one survey remains distinct from population absence.

## 4. Assessment revision

Extend Pass 70's `STOCK_ASSESSMENT` into a revision history rather than overwriting the current object.

```yaml
stock_assessment_revision:
  assessment_revision_id: null
  stock_assessment_id: null
  fishery_id: null
  assessment_date: null
  method_family: null
  input_evidence_refs: []
  abundance_assessment_band: unknown
  trend_assessment: unknown
  recruitment_assessment: unknown
  harvest_pressure_assessment: unknown
  major_data_gaps: []
  uncertainty: null
  alternative_interpretation_refs: []
  review_state: DRAFT
  reviewer_refs: []
  supersedes_revision_id: null
```

Suggested method families:

- DATA_LIMITED
- INDEX_BASED
- MULTI_INDEX
- DEMOGRAPHIC_STRUCTURED
- EXPERT_SYNTHESIS
- UNKNOWN

Suggested review states:

- DRAFT
- UNDER_REVIEW
- ACCEPTED_FOR_CURRENT_USE
- RETURNED_FOR_REVISION
- REJECTED_FOR_CURRENT_USE
- SUPERSEDED

A rejected or superseded assessment remains part of Chronicle.

## 5. Assessment dimensions stay separate

Do not create `fishery_health`.

Track separately when evidence permits:

- abundance/trend;
- recruitment;
- harvest/activity pressure;
- distribution/migration changes;
- habitat/ecosystem context;
- non-target interactions;
- uncertainty/data gaps.

A stock can have a concerning abundance assessment while current effort is low, or stable abundance while fishing pressure is rising.

## 6. Non-target interaction extension

Pass 70's `BYCATCH_OR_NON_TARGET_EVENT` remains authoritative for the event. Add disposition as a separate record.

```yaml
fishery_interaction_disposition:
  disposition_id: null
  non_target_event_id: null
  state: null
  occurred_at: null
  location_ref: null
  handling_observation_refs: []
  care_or_agency_handoff_refs: []
  later_observation_refs: []
  outcome_confidence: null
```

Candidate states:

- RELEASED_AT_SITE
- AUTHORIZED_RELOCATION_HANDOFF
- CARE_TRANSFER
- CAPTURE_PROCESS_REFERRED_TO_POKEMON_AGENCY
- LOST_CONTACT
- UNKNOWN

`RELEASED_AT_SITE` does not mean `KNOWN_UNHARMED`.

Do not invent harm either. Later Care, Pokémon Agency, Visual Records or field observations may add evidence.

## 7. Scoped management-measure extension

Pass 70's `MANAGEMENT_MEASURE` should retain scope explicitly.

```yaml
management_measure_scope_revision:
  scope_revision_id: null
  management_measure_id: null
  spatial_scope_ref: null
  temporal_scope_ref: null
  activity_scope_ref: null
  method_scope_ref: null
  subject_scope_refs: []
  rationale_claim_ref: null
  evidence_version_refs: []
  authority_ref: null
  effective_from: null
  effective_until_or_review_ref: null
  supersedes_revision_id: null
```

This allows a measure to be:

- seasonal but not year-round;
- one bay rather than the entire region;
- catch-and-release only for one activity;
- method-specific;
- research-only;
- temporary after an incident.

Do not import real-world legal structures or quota formulas.

## 8. Spawning/migration timing handoff

Migration, Wild Nesting, Lake/Estuary/Open Ocean and related ecology layers own biological observations.

Fisheries can reference them when considering a management measure.

Use:

`observed recurring pattern -> assessment/interpretation -> institutional decision -> management measure`.

Do not use:

`calendar says spring -> closure automatically exists`.

A measure can later become mismatched with the phenomenon it was designed around. That creates a review problem, not a retcon.

## 9. Persistent Pokémon after fishery interactions

If an interaction involves a known Pokémon:

- preserve its `pokemon_entity_id`;
- keep pre-interaction wild/custody state;
- record the contact/disposition;
- link later re-observations without inventing survival certainty between them;
- use Pokémon Agency for any capture/partnership/custody change.

A fishery record never grants ownership.

## 10. Market and landing evidence

Market or Supply Chain state can help reconcile where a landed resource went, but cannot be read backwards as stock abundance.

Examples:

- market inventory may be old storage;
- supply may come from another fishery;
- landing point may have moved;
- product labels may refer to a historical management unit;
- a market can continue selling after local activity stops.

## 11. Minecraft/Cobblemon boundary

Never use:

- loaded aquatic Pokémon count;
- spawn rate near a player;
- Minecraft fishing loot;
- bobber success;
- despawn/chunk unload;
- chest contents;
- client-side fishing animations;

as stock-assessment inputs unless an explicitly authored server-side observation adapter creates a provenance record for a defined scientific/management purpose.

Even then, the observation is evidence, not population truth.

## 12. PTU Fishing boundary

PTU 1.05 contains explicit Fishing rules. This protocol does not reproduce them.

A player-facing fishing attempt that materially depends on those rules must use the validated PTU/Caelo/AutoPTU path when one exists. Fisheries management can continue in world state without simulating every cast.

## 13. Encounter implementation pattern

FULL versions of fisheries encounters may require:

- dynamic crossing/withdrawal;
- non-hostile wildlife objectives;
- moving boats/equipment;
- current/water/debris hazards;
- protected tactical zones;
- exact item/Move/Ability/Feature interactions.

These must declare the permanent capability categories individually.

REDUCED versions should:

- stop/redirect activity first in world state;
- move civilians, staff and non-target wildlife out when possible;
- freeze water/boat/gear state;
- run only the remaining static confrontation;
- return afterward to Fisheries/Migration/Conservation/Pokémon Agency for the actual disposition or management result.

## 14. Explicit non-inferences

This protocol does not authorize:

- Pokémon-as-food canon;
- stock abundance from catch count;
- stock abundance from catch/effort without an authored assessment method;
- capture/KO/despawn as population removal;
- fishery access as capture permission;
- landing as Pokémon ownership;
- release as proof of survival or injury;
- Water typing as fishery eligibility;
- Swim as fishing proficiency;
- Schooling as stock truth;
- nets/lines/hooks as Stuck/Restrained;
- current as forced movement;
- deep water as drowning;
- seasonal closure as proof of spawning;
- spawning observation as automatic closure;
- market availability as local abundance.

## 15. Immediate value

Without adding new combat mechanics, Ouros can now preserve:

- catch and effort histories that remain interpretable after methods change;
- independent survey history;
- assessment revisions and review outcomes;
- data-limited uncertainty;
- non-target release disposition;
- scoped management measures;
- cross-year comparisons;
- disagreements among valid evidence sources;
- long-term institutional improvement.

Pass 70 remains the authority. Pass 157 adds evidence discipline.