# Food Safety, Kitchen Operations & Traceability Layer

Status: PROPOSED SYSTEMS DESIGN. Not Ouros canon.
Date: 2026-08-23

## Purpose

This layer tracks safety-relevant food handling, preparation, service, holds, withdrawals and traceability without replacing the existing Food, Supply Chain, Outbreak, Toxicology, Care, Manufacturing or Institutional Review layers.

It is intentionally not a pathogen simulator, nutrition simulator or universal restaurant-inspection system.

## Ownership boundary

Existing authorities remain primary:

- Food, Agriculture & Hospitality owns ingredients, recipes, culinary traditions, venues and meal/service events.
- Supply Chains owns procurement, inventory, storage nodes and freight.
- Drinking Water owns potable-water service state.
- Manufacturing owns industrial production runs and quality release for manufactured products.
- Outbreak/Health Surveillance owns illness clusters and case definitions.
- Toxicology owns hazardous agents and subject-specific exposure.
- Care owns diagnosis and treatment.
- Cases owns allegations/evidence.
- Institutional Review owns formal findings/remedies when a real mandate exists.
- Material Culture owns persistent physical item identity where needed.

This layer owns the operational food-safety graph between received food and served portions.

## Core separation

Never collapse these states:

1. physical ingredient or prepared-food identity;
2. culinary suitability;
3. safety-relevant handling history;
4. observed deviation;
5. suspected hazard;
6. confirmed hazardous agent;
7. subject-specific exposure;
8. symptom/diagnosis;
9. mechanical PTU Status;
10. formal institutional finding.

A dish can taste bad and be safe.

A dish can look normal and still be under investigation.

A deviation can occur without harm.

An illness can occur without the venue being the source.

## Primary objects

### FOOD_SAFETY_CASE

Persistent operational investigation object.

```yaml
food_safety_case:
  case_id: null
  opened_at: null
  venue_or_site_refs: []
  trigger_refs: []
  implicated_food_refs: []
  preparation_batch_refs: []
  service_event_refs: []
  handling_observation_refs: []
  hypothesis_refs: []
  hold_refs: []
  withdrawal_or_recall_refs: []
  outbreak_investigation_ref: null
  toxicology_case_refs: []
  formal_review_ref: null
  status: SIGNAL_ONLY
  closed_at: null
  resolution_summary_ref: null
```

Suggested status vocabulary:

- SIGNAL_ONLY
- OPERATIONAL_REVIEW
- TRACEBACK_ACTIVE
- TRACEFORWARD_ACTIVE
- SOURCE_UNRESOLVED
- SOURCE_PARTIALLY_RESOLVED
- CONTROL_ACTION_ACTIVE
- CLOSED
- REOPENED

`FOOD_SAFETY_CASE` is not a criminal case and does not establish diagnosis.

### PREPARATION_BATCH

A new food batch created by transformation/preparation.

```yaml
preparation_batch:
  preparation_batch_id: null
  venue_id: null
  recipe_record_ref: null
  mechanical_food_ref: null
  parent_food_batch_refs: []
  potable_water_event_refs: []
  preparation_started_at: null
  preparation_completed_at: null
  process_step_refs: []
  equipment_refs: []
  staff_participant_refs: []
  pokemon_participant_refs: []
  quantity_state: null
  hold_state: RELEASED_FOR_SERVICE
  disposition: null
```

The parent links preserve ingredient provenance.

Changing a recipe name does not change the physical batch.

A batch may combine several parent lots. A single ingredient lot may feed many preparation batches.

### PREPARATION_STEP_EVENT

```yaml
preparation_step_event:
  step_event_id: null
  preparation_batch_id: null
  step_type: RECEIVE|WASH|CUT|MIX|COOK|COOL|HOLD|REHEAT|PORTION|PACKAGE|SERVE_PREP|OTHER
  started_at: null
  ended_at: null
  equipment_refs: []
  observation_refs: []
  source_record_refs: []
  recorded_by: null
```

These events document what happened.

They do not carry universal safe numeric thresholds.

### FOOD_HANDLING_OBSERVATION

```yaml
food_handling_observation:
  observation_id: null
  observed_at: null
  observer_ref: null
  venue_or_site_ref: null
  food_or_batch_ref: null
  preparation_step_ref: null
  observed_condition: null
  method_ref: null
  instrument_ref: null
  evidence_refs: []
  quality: UNREVIEWED
```

Examples:

- storage unit was not operating;
- container seal was broken;
- raw and prepared items were observed sharing a work surface;
- potable-water service was unavailable;
- a label did not match receiving records;
- no abnormal condition was observed.

Do not store `unsafe` here unless an authorized assessment actually reached that conclusion.

### SAFETY_HYPOTHESIS

```yaml
safety_hypothesis:
  hypothesis_id: null
  case_id: null
  claim: null
  candidate_source_refs: []
  candidate_handling_event_refs: []
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  status: OPEN|SUPPORTED|WEAKENED|REJECTED|UNRESOLVED
  reviewed_at: null
```

Possible hypotheses include:

- ingredient arrived compromised;
- cross-contact occurred during preparation;
- storage/holding failure occurred;
- potable-water interruption affected preparation;
- labeling/provenance error without a safety hazard;
- unrelated illnesses were grouped together;
- source is outside the venue;
- mixed causes;
- unknown.

No hypothesis creates exposure or illness state.

### SERVICE_PORTION

A coarse link from preparation batch to consumption/service.

```yaml
service_portion:
  portion_id: null
  preparation_batch_id: null
  meal_or_service_event_id: null
  served_at: null
  recipient_ref: null
  recipient_visibility: PRIVATE
  consumed_state: UNKNOWN
  returned_or_discarded: false
```

For routine service, individual portions can be aggregated when no later investigation needs person-level linkage.

Privacy is mandatory. Public analytics should use aggregate counts, not diner identities.

### FOOD_HOLD

```yaml
food_hold:
  hold_id: null
  scope_refs: []
  reason_refs: []
  placed_at: null
  placed_by: null
  authority_basis_ref: null
  state: ACTIVE
  disposition: PENDING
  lifted_at: null
```

Possible dispositions:

- RELEASED
- DISCARDED
- RETURNED_TO_SUPPLIER
- TRANSFORMED_UNDER_AUTHORIZED_PLAN
- RETAINED_FOR_SAMPLE
- UNKNOWN

A hold is a precautionary state, not proof of hazard.

### WITHDRAWAL_OR_RECALL_EVENT

```yaml
withdrawal_or_recall_event:
  event_id: null
  initiating_institution_ref: null
  event_type: VOLUNTARY_WITHDRAWAL|SUPPLIER_NOTICE|INSTITUTIONAL_RECALL|INTERNAL_STOP_USE
  affected_food_refs: []
  affected_batch_refs: []
  issued_at: null
  reason_refs: []
  distribution_scope_refs: []
  notification_refs: []
  response_refs: []
  closed_at: null
```

The term `recall` should only be used if Ouros canon defines an institution/process that supports it. Otherwise prefer withdrawal, stop-use or supplier notice.

### TRACEABILITY_LINK

```yaml
traceability_link:
  link_id: null
  source_ref: null
  destination_ref: null
  event_type: RECEIVED|SPLIT|COMBINED|TRANSFORMED|TRANSFERRED|SERVED|DISCARDED|RETURNED
  event_time: null
  location_ref: null
  record_refs: []
```

This graph supports both traceback and traceforward.

It must never become a guilt graph.

## Safety state versus food quality

Separate:

- taste;
- freshness claim;
- cultural quality;
- presentation;
- mechanical Food Buff definition;
- safety hold;
- contamination evidence.

A stale-tasting bread may be safe.

A prize-winning dish may still have a traceability problem.

A mechanically valid PTU food can still be physically unavailable or under a narrative hold.

## Kitchen equipment

Equipment state comes from Technology/Workplaces/Material Culture as appropriate.

Food Safety may reference:

- cold storage;
- hot holding equipment;
- cooking equipment;
- washing/sanitation infrastructure;
- potable-water connection;
- preparation surfaces;
- containers;
- thermometers or other instruments;
- ventilation when relevant.

A machine fault creates an operational observation. It does not automatically make every food unsafe.

## Pokémon participation

Pokémon may participate in kitchens only through explicit individual state and capability validation.

Examples may include:

- carrying sealed ingredient containers;
- retrieving produce;
- assisting with service;
- providing an authored heat/cold capability if the exact individual and rules support it;
- detecting a specific condition if a validated capability actually exists.

Forbidden shortcuts:

- Fire-type = safe cooking temperature;
- Ice-type = refrigeration;
- Water-type = potable water;
- Poison-type = poison detector;
- Psychic-type = perfect inspection;
- Rotom = equipment repair;
- Alcremie = safe cream;
- Fidough/Dachsbun = safe baking;
- Sniffing behavior = Tracker capability.

## Routine compression

Do not generate content for every wash, cut, meal, cleaning cycle or storage check.

Compress normal operations into a summary state when:

- inputs are traceable;
- equipment is operating;
- no material deviation exists;
- no complaint/health signal intersects the service;
- no player decision is required.

Expand when:

- a source lot is disputed;
- a critical piece of equipment fails;
- potable water changes;
- a recall/withdrawal arrives;
- a health cluster intersects a venue;
- a festival creates temporary service pressure;
- records disagree;
- a player is pursuing a professional culinary goal;
- a Pokémon participant changes role or withdraws;
- the venue must choose between service continuity and precautionary hold.

## Outbreak handoff

Food Safety does not classify people or Pokémon as outbreak cases.

When a cluster exists:

1. Outbreak/Health Surveillance opens/owns the health investigation.
2. Food Safety provides service/traceability records and environmental observations.
3. Toxicology or other lab/science layers own agent-specific evidence where applicable.
4. Care owns individual diagnosis/treatment.
5. Cases may open only when allegations/evidence require a separate legal/institutional process.

A restaurant can be epidemiologically associated with cases while the precise food source remains unknown.

## Traceback and traceforward

Traceback asks where implicated food came from.

Traceforward asks where an implicated lot/batch went.

Both use the same persistent links.

Example:

```text
orchard batch A17
  -> distributor receiving event
  -> café receipt
  -> sauce batch S04
  -> lunch service L22
  -> 18 served portions
```

If sauce batch S04 also used ingredient B09, the graph records both parents.

No parent link implies blame.

## Withdrawal, discard and destruction

Narrative generation may propose a hold or voluntary stop-use when an institution/person with the correct authority chooses it.

Physical destruction requires an actual disposition event.

Do not silently delete inventory because a warning exists.

A retained sample should remain a persistent material object with custody/provenance.

## Inspection versus investigation

Routine inspection, venue self-check, outbreak environmental assessment and formal adjudication are separate event types.

A venue may:

- pass inspection and later experience an incident;
- fail an internal check without causing illness;
- close voluntarily without a formal sanction;
- reopen after operational corrections while a larger outbreak investigation remains unresolved.

## Minecraft projection

Minecraft/Cobblemon may display:

- kitchen equipment;
- sealed/held storage areas;
- labels/signage;
- discarded or quarantined containers;
- staff movement;
- a temporarily closed counter;
- cleanup activity.

Minecraft must not infer:

- whether food is safe;
- microbial growth;
- exact food temperature;
- contamination identity;
- traceability parentage;
- consumer exposure;
- PTU Status;
- legal authority to close/reopen;
- disposition of a batch.

## Battle boundary

A kitchen or restaurant can be an encounter location, but food safety state remains outside battle unless an exact validated PTU mechanic is invoked.

Narrative smoke, broken refrigeration, spilled ingredients, bad smell or suspect food do not create hazards, Accuracy penalties, Poisoned, Burned, Slowed, Rough Terrain or forced movement.

## Encounter contract A — Kitchen Shutdown During Service

Narrative premise:

A service interruption and equipment alarm occur while a busy venue is operating. Staff need to stop service, secure food and clear the work area while an independent Pokémon conflict may still need resolution.

FULL dependency:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING for live evacuation/route control;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL if combat occurs;
- status lifecycle — PARTIAL if an exact Move/Status is invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if kitchen hazards gain tactical effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for EVACUATE/CLEAR_ROUTE/PROTECT_STAFF;
- adapter/playback — BLOCKING.

REDUCED:

Stop service in world state. Move staff/diners out. Place affected food on hold. Freeze a clear static arena. Run only the remaining combatants through AutoPTU. Resume equipment/safety investigation afterward.

## Encounter contract B — Festival Stall Traceback

Narrative premise:

Several health reports intersect a festival. The party helps reconstruct which lots and stalls overlapped while the public event continues or winds down.

FULL dependency:

Most of the scenario is non-combat. If crowd movement or a confrontation occurs, complete movement, AI tactical policy and adapter/playback become blocking. Any actual PTU status or Move used during a fight remains under the relevant partial families.

REDUCED:

Resolve stall closure, crowd routing and interviews outside battle. Use AutoPTU only for a separate static confrontation if one occurs. The battle result never identifies the source lot.

## Encounter contract C — Supplier Withdrawal at a Remote Lodge

Narrative premise:

A supplier sends a stop-use notice after a storm has already disrupted the route to a remote lodge. The lodge must identify affected stock, preserve safe alternatives and decide how to feed guests until resupply.

FULL dependency:

The scenario is primarily Supply Chain + Food Safety + Travel. Combat dependencies exist only if an independent route/wildlife confrontation occurs.

REDUCED:

Inventory and food decisions happen in world state. Any battle is a separate conventional static encounter. No hunger, starvation or food-buff penalty is created because the menu is reduced.

## New overworld requirements

Pass 136 adds requirements outside AutoPTU-Java:

- preparation-batch identity;
- parent ingredient-lot links;
- preparation-step history;
- food-handling observation ledger;
- service-portion aggregation/privacy;
- food hold/disposition state;
- withdrawal/stop-use state;
- traceability graph;
- Food Safety -> Outbreak handoff;
- Food Safety -> Toxicology handoff;
- Food Safety -> Supply Chain handoff;
- Food Safety -> Water Service handoff;
- Food Safety -> Institutional Review handoff;
- food-service world state -> Minecraft projection;
- explicit gate before any food-related battle mechanic is requested.

## Explicit non-inferences

Forbidden:

- abnormal smell -> unsafe food;
- spoiled-looking food -> Poisoned;
- illness after meal -> restaurant caused it;
- shared venue -> shared source;
- equipment fault -> every batch unsafe;
- hold -> contamination confirmed;
- withdrawal -> wrongdoing;
- safe appearance -> safe food;
- cooked -> permanently safe;
- water outage -> contaminated dish;
- traceability gap -> theft/fraud;
- restaurant reputation -> safety state;
- Chef class -> food-safety authority;
- Medicine Education -> inspection authority;
- Pokémon species -> universal kitchen capability;
- battle victory -> venue safe/reopened.

## Canon questions left open

- Which Ouros institutions, if any, inspect food venues?
- Who may order versus voluntarily initiate a hold or closure?
- What recordkeeping technology exists in each region?
- Which foods require lot-level traceability versus coarse provenance?
- Are there authored concepts equivalent to allergens, foodborne pathogens or chemical residues?
- How much serving-level data is retained, and for how long?
- What privacy rules protect diner and employee information?
- Which emergency shelters/schools/clinics operate kitchens?
- Which Pokémon participate in food service and under what individual capability evidence?
- Which exact PTU/Caelo Chef, Food Buff, Digestion Buff, poison, item and Medicine rules are enabled by this project?
