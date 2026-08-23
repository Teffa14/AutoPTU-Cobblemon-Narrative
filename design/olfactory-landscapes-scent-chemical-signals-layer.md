# Ouros Olfactory Landscapes, Scent & Chemical Signals Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already models soundscapes, lightscapes, air quality, tracking, flora, decomposition, waste, Pokémon agency and urban wildlife. This layer adds persistent olfactory information without turning every smell into PTU mechanics or every scent trace into perfect tracking.

Core separation:

```text
physical source
→ odor emission event
→ olfactory field / local extent
→ possible persistence or degradation
→ actor detection
→ actor interpretation
→ recording / comparison
→ downstream ecological or social decision
→ any verified PTU mechanical effect
```

A smell can be real while its source remains unknown.

A source can be known while its effect on behavior remains uncertain.

A Pokémon can have strong scent-related Pokédex lore without receiving an overworld mechanical power.

## 1. Olfactory source

```yaml
olfactory_source:
  source_id: null
  source_type: null
  actor_id: null
  object_id: null
  habitat_ref: null
  infrastructure_ref: null
  location_ref: null
  persistent: false
  authored_profile_refs: []
  operating_state_ref: null
  provenance_refs: []
```

Candidate source types:

- POKEMON
- HUMAN
- PLANT_OR_FUNGUS
- FOOD
- WASTE
- DECOMPOSITION
- WATER
- SOIL
- SMOKE_OR_AEROSOL
- INDUSTRIAL_PROCESS
- HOUSEHOLD_OR_WORKPLACE
- PERFUME_OR_PRODUCT
- UNKNOWN

The source type never defines mechanical range, damage, status or behavioral response.

## 2. Odor emission event

```yaml
odor_event:
  odor_event_id: null
  source_id: null
  emitted_at: null
  ended_at: null
  origin_location_ref: null
  event_class: null
  profile_tags: []
  intensity_band_observed_or_authored: null
  persistence_class: null
  environment_refs: []
  mechanics_event_ref: null
  provenance_refs: []
```

Candidate event classes:

- BODY_ODOR
- SCENT_MARK
- DEFENSIVE_SPRAY
- FLOWERING
- FOOD_PREPARATION
- DECAY
- WASTE_RELEASE
- SMOKE
- CHEMICAL_PROCESS
- CLEANING
- PERFUME
- UNKNOWN

`intensity_band` is descriptive world state unless a verified rule consumes it.

## 3. Olfactory field

The olfactory field is a coarse spatial record, not a fluid simulation.

```yaml
olfactory_field:
  field_id: null
  odor_event_ids: []
  valid_from: null
  valid_until: null
  extent_geometry_ref: null
  vertical_context_ref: null
  indoor_outdoor_context: null
  ventilation_ref: null
  weather_ref: null
  water_flow_ref: null
  masking_source_refs: []
  confidence_band: null
  revision: 1
```

The server may store a small number of semantic areas such as:

- source immediate zone;
- detectable corridor;
- downwind area;
- room/building section;
- trail segment;
- water-connected reach;
- uncertain edge.

Do not calculate a universal meter radius from flavor text.

## 4. Smellscape

A smellscape describes what is commonly detectable in one place and context.

```yaml
smellscape_state:
  smellscape_id: null
  location_ref: null
  time_window_ref: null
  season_ref: null
  expected_profile_refs: []
  active_field_refs: []
  masking_state_refs: []
  baseline_ref: null
  disturbance_refs: []
  last_updated_at: null
```

Examples:

- bakery district before dawn;
- wet forest after rain;
- harbor fish market;
- flowering orchard;
- compost facility;
- geothermal spring area;
- workshop using oils or solvents;
- old library with stable material odors;
- nesting site with recurring biological scent;
- storm-burned forest weeks after fire.

A recognizable smellscape can give a location identity without being pleasant, healthy, dangerous or mechanically relevant.

## 5. Olfactory baseline

```yaml
olfactory_baseline:
  baseline_id: null
  location_ref: null
  context_tags: []
  expected_profile_refs: []
  observation_refs: []
  sensor_or_observer_refs: []
  confidence_band: null
  valid_from: null
  valid_until: null
```

A first observation cannot be called anomalous without a prior reference, authored expectation or explicit comparison site.

## 6. Olfactory observation

```yaml
olfactory_observation:
  observation_id: null
  observer_id: null
  observed_at: null
  observer_location_ref: null
  field_or_source_ref: null
  perceived_profile_tags: []
  perceived_intensity_band: null
  perceived_direction_band: null
  comparison_sample_ref: null
  observer_capability_ref: null
  confidence_band: null
  interpretation_claim_refs: []
  provenance_refs: []
```

Possible observations include:

- known odor, unknown source;
- source-like smell, low confidence;
- two overlapping scents;
- expected smell absent;
- familiar profile shifted;
- scent only one observer detects;
- scent masked by smoke, cleaning product, flowers or crowd activity.

Detection is not identification.

Identification is not individual identity.

## 7. Scent mark

Field Signs owns the physical trace; this layer owns its olfactory behavior.

```yaml
scent_mark_profile:
  scent_mark_profile_id: null
  field_sign_ref: null
  suspected_maker_refs: []
  first_observed_at: null
  latest_observed_at: null
  refresh_observation_refs: []
  degradation_state: null
  environment_refs: []
  interpretation_refs: []
```

A scent mark can persist after its maker leaves.

A refreshed mark does not prove permanent territory.

Several individuals may use the same marking location.

## 8. Olfactory profile

```yaml
olfactory_profile:
  profile_id: null
  subject_type: SPECIES|INDIVIDUAL|POPULATION|PRODUCT|LOCATION|PROCESS|UNKNOWN
  subject_ref: null
  profile_tags: []
  context_tags: []
  supporting_observation_refs: []
  contradicting_observation_refs: []
  authored_fact_refs: []
  confidence_band: null
  version: 1
```

Profiles are learned records, not universal chemistry.

Example: researchers may document that one Spritzee individual produces a different fragrance after a diet change. The system updates the profile version without creating a new Pokémon identity.

## 9. Olfactory anomaly

```yaml
olfactory_anomaly:
  anomaly_id: null
  smellscape_ref: null
  first_detected_at: null
  anomaly_type: NEW_ODOR|MISSING_ODOR|SHIFTED_PROFILE|UNEXPECTED_INTENSITY|MASKING|OTHER
  observation_refs: []
  baseline_refs: []
  candidate_source_refs: []
  hypothesis_refs: []
  confidence_band: null
  status: OPEN
```

A missing expected smell can be information without implying danger.

A new odor can come from a new source, changed process, changed wind, changed vegetation, moved wildlife, cleanup activity or observer error.

## 10. Masking and overlap

```yaml
olfactory_masking_state:
  masking_id: null
  affected_field_refs: []
  masking_source_refs: []
  observed_at: null
  observer_refs: []
  effect_band: null
  evidence_refs: []
```

Masking does not delete the underlying source.

A strong bakery odor may make a faint scent trail harder to distinguish without physically removing it.

Do not convert masking into an Accuracy, Perception or Tracker modifier unless PTU/Caelo provides a verified rule.

## 11. Pokémon-specific scent behavior

Ouros may store authored observations such as:

- an individual Spritzee changes fragrance after a diet change;
- Slurpuff assists a pastry workshop through smell discrimination;
- Stunky creates a defensive odor event and nearby wild Pokémon alter their route;
- Skiploom scent observations contribute to a geographic-origin hypothesis;
- a species repeatedly marks one crossing site.

These remain behavioral/ecological facts unless a rule text creates a mechanic.

Do not infer:

- Move knowledge;
- Ability activation;
- Tracker capability;
- scent range;
- command authority;
- territory ownership;
- Friendship/Loyalty;
- guaranteed attraction or repulsion;
- status effects.

## 12. Integration with Tracking

Tracking asks: what indirect evidence did this actor leave?

Olfactory Landscapes asks: what odor information exists here now, from all sources, and what can an observer detect?

Handoff:

```text
olfactory observation
→ possible source comparison
→ scent trace / track hypothesis
→ tracking investigation
```

The smellscape must never become an omniscient arrow toward the target.

## 13. Integration with Sound, Light and Air Quality

All four sensory/environmental layers remain independent.

A smoke plume may:

- alter Air Quality;
- change visual visibility;
- change the Soundscape indirectly through closures;
- create a dominant odor that masks weaker scents.

No layer silently writes another layer’s mechanical state.

## 14. Integration with ecology

Candidate handoffs:

- Flora → flowering odor events;
- Decomposition → decay odor events;
- Waste → waste-source events;
- Urban Wildlife → attractant or avoidance observations;
- Migration → changed smellscape during mass movement;
- Fisheries/Markets/Food → recurring commercial odors;
- Wildfire/Air Quality → smoke odor context;
- Water systems → odor observations around treatment, stagnation or contamination claims;
- Social Learning → learned responses to odor cues only when supported by observation.

An ecological response must be observed or authored. An odor field does not directly manipulate Cobblemon spawn rates.

## 15. Human and institutional uses

Possible noncombat uses:

- food quality screening;
- perfume/cosmetic craft history;
- environmental complaint investigation;
- leak/process anomaly detection;
- wildlife survey support;
- search-and-rescue evidence;
- archive/material conservation observations;
- market and festival place identity;
- occupational knowledge from workers who notice a changed smell before instruments report a fault.

None automatically creates a Skill rank or success.

## 16. Accessibility and privacy

Critical information cannot depend only on smell.

Any mandatory puzzle or safety cue must have another accessible channel such as visual signage, text, instrument reading, NPC report or route state.

Private biological or medical inference must not be generated from odor observations. Do not infer health conditions, pregnancy, fear, stress, identity or protected personal information from scent.

## 17. Minecraft projection

Minecraft may present smell indirectly through:

- semantic HUD text when appropriate;
- NPC/player observations;
- particles used only as presentation;
- source blocks/objects;
- environmental storytelling;
- optional subtitles/log entries for detected odor events;
- sensor or research UI.

Minecraft block/particle state is never authoritative for:

- source identity;
- actual odor extent;
- individual recognition;
- toxicity;
- status effect;
- tracking certainty;
- wildlife response.

## 18. Battle boundary

A narrative odor event remains outside AutoPTU unless it maps to a verified battle rule.

Examples that require exact rule validation before tactical use:

- Stench;
- Sweet Scent;
- Odor Sleuth;
- Aroma Veil;
- Sweet Veil;
- Poison Gas;
- any Move/Ability/Feature that explicitly uses scent or aroma;
- any environmental gas/odor hazard.

Even if one such mechanic is implemented, that does not validate the entire olfactory family.

## 19. Hard non-inferences

Do not infer:

- smell → Poisoned;
- bad smell → Flinch;
- fragrance → Charm bonus;
- pleasant smell → healing;
- scent mark → territory ownership;
- scent mark → individual identity;
- scent detection → exact coordinates;
- Tracker enum/data presence → working Java Tracker subsystem;
- Spritzee/Aromatisse flavor → combat aroma effect;
- Stunky presence → current Stench Ability activation;
- Slurpuff lore → guaranteed identification;
- Skiploom scent → exact birthplace;
- smoke odor → Air Quality hazard automatically;
- food smell → encounter attraction formula;
- decay smell → disease;
- cleaning smell → safe environment;
- lack of smell → absence of source;
- Minecraft particles → semantic olfactory truth.

## 20. Open canon questions

- Which regions have distinctive smellscapes authored from the start?
- Which species/populations use chemical communication in Ouros canon?
- Do any institutions use Pokémon formally for scent-sensitive work?
- How are perfume, food, agriculture and material-culture traditions represented without mechanical inflation?
- How much olfactory state advances while chunks are unloaded?
- Which odor information is stored as coarse context versus persistent event history?
- What PTU/Caelo rules govern Tracker, scent-based Perception and aroma-related Moves/Abilities?
- Should a future adapter expose a semantic sensory context distinct from visual LoS?
