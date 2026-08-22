# Ouros Field Signs, Tracking & Spoor Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models wildlife populations, persistent Pokémon, routes, photography, science, conservation, cases, biosecurity, diel activity and public information.

This layer defines indirect evidence left behind after an actor has moved on.

The system must support tracking and ecological interpretation without turning the overworld into an omniscient minimap.

Core separation:

```text
physical sign
    -> observation
    -> classification
    -> maker hypothesis
    -> behavioral / route hypothesis
    -> corroboration
    -> downstream decision
```

No later interpretation silently rewrites the original sign.

## 1. Field sign

```yaml
field_sign:
  sign_id: null
  sign_type: null
  created_time_claim: null
  world_location_ref: null
  substrate_ref: null
  physical_extent_ref: null
  current_visibility_state: null
  preservation_state: null
  linked_event_ref: null
  linked_actor_ref: null
  provenance_refs: []
  world_truth_refs: []
```

Candidate sign types:

- footprint;
- trackway;
- scratch or rub mark;
- shed fur, feather or scale;
- scent trace;
- scat-like biological trace;
- feeding remains;
- gnawed vegetation;
- disturbed soil;
- bed/rest site;
- nesting material;
- burrow or tunnel entrance;
- drag mark;
- broken vegetation;
- residue;
- trail wear;
- other authored field sign.

`sign_type` does not establish species, individual, cause or age.

## 2. Sign observation

```yaml
sign_observation:
  observation_id: null
  sign_id: null
  observer_ids: []
  observed_at: null
  method_refs: []
  environment_refs: []
  substrate_condition_ref: null
  dimensions_or_measurements: []
  photo_refs: []
  sample_refs: []
  visibility_band: null
  confidence_band: null
  notes: []
```

Observers can record the same sign differently.

A later expert review may improve the classification without changing what the first observer actually saw.

## 3. Classification

```yaml
sign_classification:
  classification_id: null
  sign_id: null
  classifier_id: null
  classification_kind: species|group|sign_type|behavior|age_band|other
  candidate_refs: []
  confidence_band: null
  evidence_refs: []
  conflicting_classification_refs: []
  created_at: null
  superseded_by: null
```

Useful status values:

- UNCLASSIFIED;
- PROVISIONAL;
- SUPPORTED;
- REVIEWED;
- REJECTED;
- SUPERSEDED.

A species-level classification does not automatically identify an individual.

## 4. Trackway

A trackway links multiple spatial signs without requiring every footprint to remain rendered.

```yaml
trackway:
  trackway_id: null
  sign_ids: []
  first_observed_at: null
  latest_observed_at: null
  start_area_ref: null
  end_area_ref: null
  route_geometry_ref: null
  route_certainty_band: null
  maker_hypothesis_refs: []
  behavior_hypothesis_refs: []
  interruption_refs: []
  degradation_refs: []
  status: active
```

Suggested statuses:

- ACTIVE_VISIBLE;
- PARTIAL;
- LOST;
- DEGRADED;
- BURIED;
- WASHED_OUT;
- HISTORICAL_RECORD_ONLY.

A lost trackway can remain valid historical evidence.

## 5. Scent trace

Scent remains a specialized evidence channel.

```yaml
scent_trace:
  scent_trace_id: null
  source_sign_ref: null
  suspected_source_ref: null
  reference_sample_ref: null
  first_detected_at: null
  last_detected_at: null
  route_claim_ref: null
  environment_refs: []
  detection_actor_id: null
  capability_validation_ref: null
  interpretation_state: null
```

Rules:

- no actor can use scent mechanically without verified PTU/Caelo authority for that actor;
- a scent trail is not a coordinate feed;
- the presence of a scent does not prove the subject is still nearby;
- overlapping scents may create uncertainty;
- weather, water, crowds and time may matter only through authored or verified mechanics/state, never improvised DC math.

## 6. Maker hypothesis

```yaml
maker_hypothesis:
  hypothesis_id: null
  sign_or_trackway_ref: null
  candidate_species_refs: []
  candidate_pokemon_ids: []
  candidate_group_refs: []
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  confidence_band: null
  status: open
```

The system must allow:

- correct route, wrong species;
- correct species, wrong individual;
- multiple individuals using the same trail;
- old sign confused with fresh sign;
- human/Pokémon/tool-created marks being misclassified.

## 7. Biological trace sample

```yaml
biological_trace_sample:
  sample_id: null
  source_sign_id: null
  collection_event_ref: null
  collected_at: null
  collector_ids: []
  sample_kind: hair|feather|scale|residue|other
  custody_refs: []
  storage_ref: null
  analysis_refs: []
  contamination_notes: []
  sensitive_location: false
```

Samples connect to Science, Cases and Health Surveillance.

Do not infer genetics, identity, disease or ownership without a validated analysis process.

## 8. Sign degradation

```yaml
sign_degradation_revision:
  revision_id: null
  sign_id: null
  observed_at: null
  visibility_before: null
  visibility_after: null
  suspected_driver_refs: []
  measured_change_refs: []
  evidence_refs: []
```

Candidate drivers:

- rain;
- snow;
- snowmelt;
- wind;
- tide;
- flood;
- dust;
- traffic;
- crowds;
- wildlife reuse;
- construction;
- fire;
- vegetation growth;
- ordinary aging.

The generator may not erase the original event because the sign degraded.

## 9. Tracking survey

```yaml
tracking_survey:
  survey_id: null
  purpose_ref: null
  surveyor_ids: []
  area_refs: []
  time_window: null
  methods: []
  target_claim_refs: []
  substrate_suitability_refs: []
  weather_since_window_refs: []
  effort_refs: []
  sign_observation_ids: []
  nondetection_records: []
  route_hypothesis_refs: []
  result_status: draft
```

A nondetection is evidence about the survey, not automatic absence.

## 10. Corroboration graph

```yaml
sign_corroboration_link:
  link_id: null
  source_evidence_ref: null
  corroborating_ref: null
  relationship: supports|contradicts|independent|duplicate_source|uncertain
  created_at: null
  reviewer_id: null
```

Useful corroboration sources:

- camera-trap image;
- direct sighting;
- acoustic record;
- sample analysis;
- another trackway;
- known Pokémon identity record;
- transport/service record;
- weather history;
- field-sign archive;
- public report;
- battle transcript if the subject later enters battle.

## 11. Known trail use

Repeated sign can support a coarse route-use model.

```yaml
known_trail_use:
  trail_use_id: null
  population_or_actor_ref: null
  route_feature_ref: null
  observation_window: null
  evidence_refs: []
  use_band: occasional|repeated|seasonal|unknown
  last_reviewed_at: null
  uncertainty_notes: []
```

This is not pathfinding AI.

It can inform Conservation, Road Ecology, Wild Collectives, Diel Activity and Travel.

## 12. Persistent Pokémon identity

A sign can propose, but not create, an individual identity.

Strong identity support may come from:

- a validated tag or marker;
- repeated distinctive physical traits;
- verified sample analysis;
- direct observation connected to the sign;
- known custody/route history;
- multiple independent records.

Never merge two Pokémon entities because two footprints look similar.

## 13. Cases and missing-person/Pokémon work

Cases may use:

- last confirmed direct sighting;
- last confirmed field sign;
- last supported trackway;
- scent reference sample;
- route hypotheses;
- contradictions;
- degradation state;
- search coverage.

A `last sign` does not prove current location, safety, intent or movement direction after the sign was made.

## 14. Conservation and science

Field signs can support:

- occupancy;
- habitat use;
- migration timing;
- den/roost use;
- predation/scavenging hypotheses;
- biosecurity arrival pathways;
- post-release monitoring;
- rare-species surveys;
- individual re-identification.

Do not convert every sign into a quest marker. Most records should remain compressed research/world state.

## 15. Player knowledge and privacy

Different players may know different trails.

```yaml
tracking_knowledge:
  holder_id: null
  sign_or_trackway_ref: null
  knowledge_state: unknown|reported|observed|classified|verified|stale
  source_refs: []
  private_notes: []
```

Sensitive den, nesting or endangered-population locations can be redacted through Conservation/Science access policy.

## 16. Minecraft projection

Minecraft may show selected signs through:

- temporary footprint decals/particles;
- disturbed blocks or vegetation variants;
- scratch/rub marks;
- feathers/hair-like decorative entities;
- track markers in survey mode;
- inspectable evidence objects;
- NPC/Pokémon behavior near a sign;
- map annotations.

The server-side sign record remains authoritative.

Chunk unload/reload must not recreate expired evidence as fresh.

Block breakage by a player does not delete Chronicle history.

## 17. Anti-exploit policy

Players must not be able to create rare Pokémon detections by placing fake footprints or decorative signs unless a deliberate deception system records them as player-created evidence.

Sign spawning should be derived from persistent world events/population state, not used as the population source of truth.

Rare sign should not automatically increase spawn odds.

Repeatedly forcing chunk reload must not refresh trace age.

## 18. PTU/Caelo mechanics boundary

Public PTU discovery material shows `Tracker` and Perception interactions with scent/signs. Exact project PTU/Caelo wording must be verified before implementation.

This layer does not create:

- tracking DCs;
- scent radius;
- automatic direction arrows;
- opposed Stealth checks;
- surprise bonuses;
- Accuracy changes;
- capture bonuses;
- initiative bonuses;
- movement penalties;
- Trailblazer-like mechanics;
- automatic Odor Sleuth behavior.

## 19. Encounter implementation contracts

### Encounter A — Last Tracks at Cedar Ford

Narrative premise:

A missing service Pokémon was last seen before a storm. Fresh-looking tracks appear near a ford, but the route divides and some sign may predate the storm.

FULL version:

- overworld tracking survey with degradable track segments;
- target Pokémon may continue moving while players search;
- multiple route hypotheses;
- possible withdrawal/rescue objective if battle starts;
- environmental water state reflected only through verified battle mechanics;
- AI understands escape/protect goals.

Dependencies:

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when exact content is used:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement including interception/forced movement if an active escape/rescue is in-grid;
- terrain/weather/hazards/zones/reactions if the ford matters tactically;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback;
- overworld tracking/scent contract.

REDUCED version:

Resolve tracking entirely in overworld world state. Once players locate the relevant site, freeze the ford geometry. If a battle occurs, use a conventional static encounter. Resolve recovery/identification after battle without inventing pursuit mechanics.

### Encounter B — The False Trail

Narrative premise:

A conservation team believes a rare population crossed a road. A second sign suggests the trail may belong to a common species or to an older passage.

FULL version:

- multi-method evidence collection;
- road-crossing state;
- camera or sample corroboration;
- optional noncombat observation of the subject;
- if disturbed, wildlife can withdraw dynamically.

Primary blockers:

- overworld sign observation/identity;
- AI tactical policy for withdrawal;
- complete movement if withdrawal becomes tactical;
- Minecraft projection.

REDUCED version:

Keep the investigation noncombat. Record observations, run a later camera/sample check and allow `INCONCLUSIVE` as a valid outcome. A battle happens only if an independent encounter genuinely occurs.

### Encounter C — Scent Lost at the Market

Narrative premise:

A verified Tracker follows a known scent toward a busy market, where the trail becomes ambiguous among crowds, deliveries and multiple exits.

FULL version:

- verified PTU Tracker implementation;
- overworld scent-state degradation/ambiguity;
- crowd/access graph;
- target continues acting independently;
- investigation can transition into a pursuit only if supported.

Primary blockers:

- exact PTU/Caelo Tracker contract;
- overworld scent-state system;
- AI tactical policy for pursuit/withdrawal;
- complete movement/interception for a true chase;
- Minecraft playback.

REDUCED version:

Use Tracker only if its exact validated mechanic is available in the runtime executing the skill check; otherwise treat scent as an authored clue with no mechanical roll. The trail ends at the market. Players continue through witnesses, cameras, deliveries or other evidence. No battle chase is implied.

## 20. Canon guardrails

No specific tracking guild, ranger institution, rare species route, missing Pokémon, famous tracker, law-enforcement procedure or regional field-sign tradition becomes canon through this layer.

No species receives Tracker, scent ability or trail behavior solely because its real-world analogue would have it.

No field sign becomes proof of emotional state, intent, guilt, ownership or aggression.

No biological sample authorizes cloning, breeding, capture, disease diagnosis or identity without an explicit validated system.

## Open questions

- Which exact Tracker/Perception text does the project's PTU/Caelo corpus use?
- Does Caelo alter Tracker, Odor Sleuth or relevant Skill checks?
- Which Pokémon Capabilities are exposed by AutoPTU outside battle?
- How should sign age advance while nobody is online?
- Which substrates should preserve sign at coarse world-state level?
- How much physical evidence should Minecraft render versus leave inspectable through UI?
- Can players deliberately create false evidence, and if so how is provenance preserved?
- What evidence threshold is enough to merge a sign with a persistent Pokémon identity?
- How should trackways cross unloaded chunks without simulating every step?
- Should scent ever be represented spatially, or remain an abstract route clue until mechanics are verified?