# Ouros Myth, Archaeology & Sacred Sites Layer

Status: Proposed systems design. Not established canon.

## Purpose

Ouros already models Chronicle facts, public memory, evidence, settlements, factions, cases, dungeons, ecological state, material provenance and recurring events. This layer adds cultural deep time: myths, oral traditions, sacred places, archaeological sites, old objects, ritual practices, conflicting historical interpretations and extraordinary Pokémon phenomena.

The design goal is uncertainty with provenance. Players should be able to discover what people believe, what evidence exists, what institutions claim and what actually happened without the generator collapsing those layers into one omniscient lore answer.

## 1. Deep-history data layers

Do not store `the lore` as one text field.

```yaml
deep_history_subject:
  subject_id: null
  subject_type: null
  world_truth_fact_ids: []
  archaeological_observation_ids: []
  historical_claim_ids: []
  mythic_claim_ids: []
  ritual_practice_ids: []
  anomalous_phenomenon_ids: []
  public_memory_ids: []
  unresolved_questions: []
```

Candidate subject types:
- location;
- legendary_or_mythical_pokemon;
- historical_pokemon_entity;
- artifact;
- institution;
- migration;
- disaster;
- ancient settlement;
- sacred landscape;
- recurring phenomenon;
- old conflict;
- cultural relationship.

## 2. Mythic claims

A mythic claim records what a tradition says, not what the engine knows to be true.

```yaml
mythic_claim:
  mythic_claim_id: null
  subject_ids: []
  tradition_id: null
  holder_community_ids: []
  claim_summary: null
  motif_tags: []
  source_type: oral
  earliest_known_record_id: null
  current_version_id: null
  related_claim_ids: []
  contradicting_claim_ids: []
  geographic_scope_ids: []
  confidence_as_historical_fact: unknown
  sacred_status: null
  provenance: []
```

Rules:
- the claim can be true, false, mixed, metaphorical or unresolved;
- generated NPC dialogue may cite a claim only when that actor plausibly knows it;
- contradictions between myths are allowed;
- no myth is promoted to `world_truth` without authored evidence.

## 3. Tradition objects

A tradition is a living social system.

```yaml
tradition:
  tradition_id: null
  community_ids: []
  region_ids: []
  subject_ids: []
  foundational_claim_ids: []
  current_practices: []
  steward_ids: []
  sacred_location_ids: []
  protected_object_ids: []
  internal_variants: []
  reform_history: []
  external_relationships: []
  participation_rules: []
```

Traditions may split, merge, reform, secularize, revive or disappear.

The generator must not treat culture as static scenery.

## 4. Myth version lineage

Stories change as they move.

```yaml
myth_version:
  myth_version_id: null
  parent_version_ids: []
  tradition_id: null
  community_id: null
  region_id: null
  time_period: null
  claim_ids: []
  motif_tags: []
  adaptation_reasons: []
  surviving_record_ids: []
```

Possible adaptation reasons:
- migration;
- political reform;
- translation;
- disaster;
- religious schism;
- tourism;
- institutional standardization;
- children’s retelling;
- propaganda;
- new archaeological discovery;
- contact with another tradition.

This lets Ouros preserve shared motifs without pretending every region tells the same story word for word.

## 5. Archaeological site state

A ruin is a persistent location state machine with research context.

```yaml
archaeological_site:
  site_id: null
  location_id: null
  site_type: null
  estimated_period: null
  confidence: null
  known_structures: []
  sealed_areas: []
  exposed_areas: []
  stratigraphic_contexts: []
  inscription_ids: []
  artifact_ids: []
  biological_context_ids: []
  modern_damage_ids: []
  previous_excavation_ids: []
  current_steward_ids: []
  access_policy_ids: []
  active_hazards: []
  interpretation_ids: []
  unresolved_questions: []
```

The site may be partially known for years.

## 6. Archaeological observations

Store observations before interpretation.

```yaml
archaeological_observation:
  observation_id: null
  site_id: null
  observer_ids: []
  location_context: null
  object_ids: []
  structural_feature_ids: []
  inscription_ids: []
  material_description: null
  spatial_relationships: []
  condition_state: null
  documentation_refs: []
  timestamp: null
  disturbance_level: null
```

Examples:
- an inscription is physically above another layer;
- two materials occur together;
- a doorway was sealed from one side;
- a statue was moved in modern times;
- roots or water damaged one wall;
- a Pokémon nest currently occupies an old chamber.

Do not jump directly from these facts to `this proves the civilization worshipped X`.

## 7. Historical interpretations

```yaml
historical_claim:
  historical_claim_id: null
  author_ids: []
  institution_ids: []
  subject_ids: []
  proposition: null
  evidence_ids: []
  counterevidence_ids: []
  confidence: null
  publication_or_record_id: null
  current_status: active
```

Suggested states:
- PROPOSED
- ACTIVE
- REVISED
- CONTESTED
- WEAKENED
- DISPROVEN
- UNRESOLVED

Scholars, local historians and institutions can disagree without one side being secretly malicious.

## 8. Site context preservation

Excavation changes a site.

```yaml
site_intervention:
  intervention_id: null
  site_id: null
  actor_ids: []
  intervention_type: null
  target_context_ids: []
  documentation_before_ids: []
  removed_object_ids: []
  exposed_feature_ids: []
  damage_ids: []
  restoration_ids: []
  custody_outputs: []
  chronicle_event_id: null
```

Candidate intervention types:
- SURVEY
- DOCUMENT
- EXCAVATE
- STABILIZE
- REMOVE_OBJECT
- RESTORE
- RESEAL
- EMERGENCY_RECOVERY
- UNAUTHORIZED_DISTURBANCE

Whether an action is authorized depends on future Ouros canon, not this schema.

## 9. Protected old objects

A culturally significant object can also exist in the Material Culture layer.

```yaml
heritage_object_state:
  item_instance_id: null
  cultural_subject_ids: []
  associated_tradition_ids: []
  archaeological_context_id: null
  current_custodian_id: null
  stewardship_claim_ids: []
  display_state: null
  operational_function_unknown: true
  safe_to_move: unknown
  mechanics_review_required: true
```

The system should never assume `old object = loot`.

Possible states:
- left in context;
- documented in place;
- moved for stabilization;
- institution storage;
- community stewardship;
- public display;
- disputed custody;
- missing.

## 10. Sacred sites

Sacred status is social and cultural state.

```yaml
sacred_site:
  site_id: null
  tradition_ids: []
  community_ids: []
  sacred_subject_ids: []
  public_access_state: null
  stewardship_ids: []
  customary_practices: []
  restricted_actions: []
  pilgrimage_patterns: []
  seasonal_states: []
  ecological_dependencies: []
  modern_conflicts: []
```

A place may be sacred to one community and archaeological to another.

That overlap is a source of negotiation, not automatic antagonism.

## 11. Ritual practice

A ritual is what people do, not proof of metaphysics.

```yaml
ritual_practice:
  ritual_id: null
  tradition_id: null
  participant_roles: []
  location_ids: []
  time_conditions: []
  object_ids: []
  actions: []
  stated_purpose_claim_ids: []
  public_or_private: null
  current_status: active
  known_variants: []
```

Hard boundary:
No ritual grants a PTU modifier, invokes a Pokémon, changes weather, opens a portal or produces another mechanical effect unless that effect has an authored rule/implementation source.

A ritual may still matter socially even when no supernatural effect occurs.

## 12. Extraordinary phenomena

Record anomalous events before explaining them.

```yaml
anomalous_phenomenon:
  phenomenon_id: null
  location_ids: []
  timestamp_range: null
  observer_ids: []
  direct_observations: []
  environmental_changes: []
  pokemon_entity_ids: []
  instrument_or_record_ids: []
  associated_mythic_claim_ids: []
  associated_historical_claim_ids: []
  explanation_state: unknown
  mechanics_review_required: true
```

Possible explanation states:
- UNKNOWN
- NATURAL_CAUSE_SUPPORTED
- POKEMON_CAUSE_SUPPORTED
- HUMAN_CAUSE_SUPPORTED
- MULTIPLE_CAUSES
- UNRESOLVED

Do not label an event divine, cursed, psychic or legendary merely because residents do.

## 13. Legendary-scale entity policy

A legendary or mythical Pokémon should be modeled first as a persistent world entity with cultural, ecological and historical edges.

```yaml
legendary_context:
  pokemon_entity_id: null
  species_ref: null
  known_presence_state: unknown
  confirmed_event_ids: []
  associated_tradition_ids: []
  associated_location_ids: []
  ecological_relationships: []
  caretaker_or_steward_ids: []
  mythic_claim_ids: []
  historical_claim_ids: []
  public_knowledge_state: []
  sensitive_information_ids: []
  encounter_policy: authored_only
```

Generation rules:
1. Do not spawn a Legendary because a quest needs a climax.
2. Do not assume it can or should be captured.
3. Do not make cultural belief equivalent to ownership.
4. Do not invent motives from Pokédex flavor alone.
5. If a Legendary appears physically, require authored canon state and mechanics review.
6. A Legendary can influence story through signs, prior consequences, contested evidence or stewardship without appearing on-screen.

## 14. Sacred Pokémon stewardship

Some communities may care for or monitor special Pokémon without owning them.

```yaml
pokemon_stewardship:
  stewardship_id: null
  pokemon_entity_id: null
  steward_ids: []
  tradition_id: null
  habitat_ids: []
  responsibilities: []
  access_protocols: []
  known_behavior_refs: []
  current_concerns: []
  historical_events: []
```

Possible responsibilities:
- habitat maintenance;
- seasonal monitoring;
- visitor guidance;
- keeping people away during sensitive periods;
- maintaining old infrastructure;
- recording appearances;
- coordinating emergency response.

No stewardship record grants capture rights or command authority.

## 15. Cultural access gates

Some locations are difficult to access for social reasons, not because of level requirements.

```yaml
cultural_access_gate:
  gate_id: null
  location_id: null
  steward_ids: []
  reason_claim_ids: []
  access_routes: []
  temporary_exceptions: []
  emergency_override_ids: []
  alternate_physical_routes: []
```

Possible routes:
- invited by a steward;
- public festival day;
- research agreement;
- rescue emergency;
- community service relationship;
- open access with etiquette requirements;
- physically possible but socially contested trespass.

Exact legal consequences depend on future canon.

## 16. Translation and inscription state

Old text should not become perfect exposition automatically.

```yaml
inscription:
  inscription_id: null
  site_id: null
  physical_text_ref: null
  language_or_script_ref: null
  damage_state: null
  known_readings: []
  translation_hypotheses: []
  symbol_matches: []
  context_ids: []
  authentication_state: unknown
```

```yaml
translation_hypothesis:
  translation_id: null
  author_ids: []
  inscription_id: null
  reading: null
  confidence: null
  disputed_segments: []
  supporting_comparisons: []
```

Do not generate exact ancient languages by copying real scripts from cultures without deliberate art/lore review.

## 17. Myth-aware investigation

The existing Evidence Graph can use folklore without treating it as evidence of truth by default.

A myth can:
- point to a location;
- preserve a distorted historical relationship;
- encode a seasonal clue;
- reveal what a community fears or values;
- identify a symbol;
- explain why a site is avoided;
- conflict with physical evidence.

It cannot automatically:
- identify a culprit;
- prove a Pokémon caused an event;
- validate supernatural mechanics;
- reveal private world truth.

## 18. Myth-aware dungeon design

A ruin dungeon should separate four layers:

### Physical layer
Architecture, passages, damage, water, vegetation, collapse, machinery.

### Historical layer
Past uses supported by evidence.

### Cultural layer
Stories, rituals and modern stewardship.

### Current occupation layer
Wild Pokémon, researchers, visitors, factions, hazards and recent disturbance.

A strong dungeon can create friction between these layers.

Example abstract pattern:
An old ceremonial chamber is now a nesting site; opening a historical passage would disturb the current ecology; a community wants the chamber left alone; researchers suspect another entrance exists.

## 19. Ruin puzzle authenticity

Puzzles should have an in-world reason to exist.

Candidate reasons:
- functional control system;
- security mechanism;
- ritual sequence that modern explorers misunderstand;
- mnemonic teaching device;
- modern reconstruction puzzle;
- damage that requires spatial reasoning to bypass;
- translation problem;
- deliberately sealed hazardous system.

Avoid unexplained sliding-block puzzles inserted solely because the location is ancient.

## 20. Myth propagation and public memory

The Public Memory layer handles recent history. Deep-history myths can feed it when new discoveries occur.

Possible outputs:
- museum exhibit update;
- public controversy;
- festival reinterpretation;
- community apology;
- new preservation policy;
- faction legitimacy shift;
- tourism pressure;
- school curriculum change;
- renewed pilgrimage;
- backlash against an interpretation.

A new discovery changes present beliefs even when the ancient truth remains unresolved.

## 21. Archaeology and material provenance

Recovered objects should connect directly to the Material Culture layer.

Required provenance where feasible:
- site;
- context;
- finder;
- documenting actors;
- removal event;
- current custodian;
- conservation/restoration history;
- display history;
- linked claims.

Removing provenance can itself become a case or public-memory issue.

## 22. Research ethics without importing modern law

Ouros has not established universal archaeological law.

The generator therefore cannot assume:
- who legally owns antiquities;
- whether excavation permits exist everywhere;
- whether export is illegal;
- whether human-like burial customs exist in a given culture;
- whether a sacred site can be entered by outsiders;
- whether museums have superior claims over communities.

Instead, each region/institution/tradition must define its own authored norms, mandates and conflicts.

## 23. Quest generation hooks

Candidate causes:
- a newly exposed ruin after weather or construction;
- contradictory translation;
- damaged sacred site;
- missing heritage object;
- pilgrimage route blocked;
- archaeological team requests support;
- local community disputes an institution's interpretation;
- unusual Pokémon behavior near a protected site;
- old structure reactivates;
- tourist pressure damages habitat;
- artifact provenance points to another region;
- one myth version preserves a location absent from modern maps;
- public event revives an old controversy.

Each candidate still requires world-state support.

## 24. Minecraft / Cobblemon representation

Potential overworld state:
- ruins with persistent excavation stages;
- barriers, scaffolding and conservation covers;
- plaques with current public interpretations;
- community stewards or researchers;
- temporary closures;
- pilgrimage visitors;
- changing museum exhibits;
- tagged artifact containers;
- old pathways becoming accessible;
- protected nesting zones;
- visual traces of different construction phases;
- ritual/event decorations during specific windows.

Minecraft should show uncertainty through partial access and changing interpretation, not through random lore text spam.

## 25. PTU / Caelo mechanics boundary

Before any generated content uses mechanical resolution, validate against the supplied project sources and current AutoPTU implementation.

Potential checks include:
- actual Skills and ranks;
- legal Pokémon capabilities;
- special senses;
- Aura or dream-related capabilities where actually present;
- movement and terrain;
- Unown-related capabilities where applicable;
- environmental hazards;
- item behavior;
- capture rules;
- Legendary encounter legality;
- any Caelo-specific homebrew explicitly retained by Ouros.

This layer does not create new rituals, powers, supernatural rules, excavation DCs, translation bonuses or Legendary mechanics.

## 26. Implementation priority

Recommended order:
1. mythic claims separated from truth;
2. traditions and version lineage;
3. archaeological observation schema;
4. historical interpretations;
5. archaeological site state;
6. heritage-object provenance link;
7. sacred-site stewardship;
8. anomalous-phenomenon observations;
9. inscription/translation hypotheses;
10. Legendary context policy;
11. cultural access gates;
12. myth-aware quest generation.

This layer gives Ouros a past that can remain genuinely contested and discoverable instead of becoming a static lore encyclopedia.