# Salvage, Recovery and Found-Property Continuity Layer

Status: DESIGN PROPOSAL. NOT CANON.
Date: 2026-09-01
Research basis: `research/2026-09-01-salvage-recovery-found-property-scan-187.md`

## Goal

Represent displaced, damaged, lost, found or recovered material as persistent world objects with provenance, safety, custody, condition and unresolved claim state.

This layer begins at discovery and ends when the object is handed into an existing downstream system such as archive intake, storage, repair, ordinary return, disposal or an explicitly approved future claim process.

It does not define Caelo property law, maritime law, insurance, criminal evidence rules or PTU battle-item ownership.

## Existing systems this layer reuses

Do not duplicate:

- portable evidence and provenance ledgers;
- courier and chain-of-custody handoffs;
- provisioning stock and reserve ledgers;
- after-sale repair/warranty flows;
- workshop/material-condition inspection;
- information claims and actor knowledge;
- preparedness and emergency access;
- restoration/public works;
- ecological observation;
- questline graph and world-fact authority.

A recovery case should reference those systems by IDs when responsibility passes to them.

## Core entities

### Recovery object

```yaml
recovery_object:
  recovery_object_id: null
  persistent_world_object_ref: null
  provisional_type: null
  descriptive_name: null
  material_tags: []
  marks_observed: []
  condition_observations: []
  current_location_ref: null
  discovery_event_ref: null
  current_custodian_ref: null
  custody_chain_ref: null
  hazard_state: UNKNOWN
  movement_clearance_state: NOT_ASSESSED
  use_clearance_state: NOT_ASSESSED
  claim_state: UNRESOLVED
  provenance_claim_refs: []
  condition_assessment_refs: []
  archive_hold_ref: null
  repair_case_ref: null
  stock_lot_ref: null
  disposition_state: OPEN
```

### Recovery case

```yaml
recovery_case:
  recovery_case_id: null
  opened_at: null
  opened_by_ref: null
  trigger_observation_refs: []
  location_refs: []
  object_refs: []
  hazard_assessment_refs: []
  custody_refs: []
  claimant_refs: []
  source_record_refs: []
  unresolved_questions: []
  downstream_case_refs: []
  status: VERIFYING
```

### Provenance claim

A provenance claim is attributed evidence, not world truth.

```yaml
provenance_claim:
  claim_id: null
  object_ref: null
  claim_type: ORIGIN | PRIOR_CUSTODY | PRIOR_OWNER | ROUTE | EVENT_ASSOCIATION | FUNCTION
  asserted_value_ref: null
  source_ref: null
  evidence_refs: []
  confidence: null
  status: OPEN | CORROBORATED | CONTRADICTED | SUPERSEDED | UNRESOLVED
```

### Condition assessment

```yaml
condition_assessment:
  assessment_id: null
  object_ref: null
  assessor_ref: null
  assessor_scope: null
  observed_at: null
  physical_condition: null
  safe_to_move: UNKNOWN
  safe_to_use: UNKNOWN
  requires_specialist: false
  calibration_required: false
  contamination_or_hazard_notes: []
  repair_route_ref: null
  limitations: []
```

## Recovery lifecycle

Recommended case states:

`REPORTED -> VERIFYING -> HAZARD_ASSESSMENT -> DOCUMENTING -> RECOVERY_AUTHORIZED -> RECOVERED -> IN_CUSTODY -> ASSESSING -> ROUTED -> CLOSED_WITH_RESOLUTION | CLOSED_UNRESOLVED`

Optional branches:

- `LEFT_IN_PLACE` when movement would be unsafe or destroy needed context;
- `AREA_RESTRICTED` when the site itself requires temporary control;
- `SPECIALIST_REQUIRED` when current residents cannot legitimately assess the object;
- `CLAIM_PENDING` when physical custody is stable but disposition is not;
- `ARCHIVE_HOLD` when historical or documentary relevance dominates;
- `REPAIR_HANDOFF` when the downstream repair system takes over;
- `STOCK_HANDOFF` only after acceptance into an authoritative stock ledger;
- `DISPOSAL_PENDING` only when a legitimate process exists.

## Authority separation

The following conclusions require separate authority:

### Discovery authority

Can write:

- object observed at location;
- visible marks;
- visible damage;
- immediate surrounding conditions.

Cannot write:

- ownership;
- abandonment;
- cause of displacement;
- safe-to-use status unless qualified to assess it.

### Safety / condition authority

Can write within scope:

- handling hazard;
- movement restrictions;
- ordinary repair condition;
- need for specialist inspection.

Cannot automatically write:

- title or claim resolution;
- historical provenance;
- PTU Item legality.

### Custody authority

Can record who physically controls the object and authorized handoffs.

Custody does not imply title.

### Historical / records authority

Can correlate labels, manifests, prior surveys, archive references and dated records.

Matching records can corroborate provenance without deciding every legal consequence.

### Battle authority

AutoPTU may resolve combat facts only.

A BattleResult may unblock access to the immediate recovery area if the world contract explicitly allows that consequence. It cannot decide ownership, condition, calibration, archival value, abandonment, compensation or future disposition.

## Identification model

Objects may carry multiple marks with different meanings:

- maker mark;
- repair mark;
- storehouse lot;
- transport manifest number;
- institution asset ID;
- owner label;
- old owner label;
- survey tag;
- temporary work tag;
- decorative mark;
- unknown mark.

The system must store the observed mark before assigning meaning.

A single object can legitimately have conflicting identifiers from different periods.

## Physical context preservation

Before movement, a recovery observation may record:

- position or bounded location;
- orientation when relevant;
- nearby debris or infrastructure;
- waterline, sediment or weather exposure;
- packaging state;
- whether contents are exposed;
- nearby wildlife interaction;
- photographs or equivalent world evidence if the adapter supports them;
- observer and timestamp.

Context recording is especially important for historical objects and incident investigation.

## Hazard states

Suggested non-mechanical world states:

- `UNKNOWN`
- `OBSERVATION_ONLY`
- `SAFE_FOR_ORDINARY_HANDLING`
- `REQUIRES_PROTECTIVE_HANDLING`
- `REQUIRES_SPECIALIST`
- `DO_NOT_MOVE`
- `CLEARED_FOR_TRANSFER`

These are narrative/world-service states. They do not create PTU damage, statuses or resistances.

If a hazard becomes tactical, the exact terrain/weather/hazards/zones/reactions capability family must be audited before putting it inside BattleSpec.

## Claim states

Until Caelo authority is located, use neutral workflow labels rather than legal conclusions:

- `UNRESOLVED`
- `IDENTIFIER_FOUND`
- `POTENTIAL_PRIOR_CUSTODIAN_FOUND`
- `CLAIM_ASSERTED`
- `MULTIPLE_CLAIMS`
- `RECORDS_CORROBORATED`
- `RETURN_ROUTE_APPROVED`
- `DISPOSITION_PENDING`
- `CLOSED_UNRESOLVED`

Do not create `ABANDONED`, `OWNERLESS`, `FORFEITED`, `SALVAGE_RIGHT_GRANTED` or equivalent legal statuses without canon/source approval.

## Minecraft / Cobblemon adapter rules

The server-side Ouros object record remains authoritative.

Minecraft item representations are projections or interaction handles.

Required safeguards:

- ordinary item pickup does not silently transfer narrative ownership;
- a protected recovery object cannot become ordinary player inventory without an explicit custody transition;
- chunk unload does not change object state;
- entity despawn does not mean destruction;
- duplicate item entities cannot produce duplicate authoritative objects;
- a visual crate can represent a recovery object without exposing its contents as Minecraft loot;
- Cobblemon interacting with, carrying or standing near an object creates observations only unless a specific authoritative behavior contract says more;
- battle-state logic never determines custody or claim state.

## PTU item boundary

Moves, Abilities, Items and Trainer Features can affect battle possessions only according to their verified mechanics.

Narrative ownership remains outside that conclusion.

Examples:

- Thief may produce a battle-state Held Item change when implemented correctly. The narrative layer does not infer title transfer.
- Frisk may reveal information permitted by its actual rule. It does not prove historical provenance.
- Pickup or comparable content cannot manufacture institutional stock without an adapter contract that explicitly maps a generated mechanical item into world inventory.

## Downstream handoff contracts

### To Tideglass / archive

Allowed when:

- item has documentary or historical relevance;
- custody transfer is explicit;
- archive accepts it under an existing or future intake workflow.

### To repair workflow

Allowed when:

- condition assessment supports repair;
- custody for repair is recorded;
- downstream repair case owns later queue/parts/warranty state.

### To provisioning / stock

Allowed only after:

- object identity is sufficient;
- condition is acceptable;
- receiving institution accepts it;
- authoritative stock ledger records the intake.

Physical presence on a shelf is insufficient.

### To disposal

Requires a canon-approved authority/process. Until then, Narrative can mark `DISPOSAL_PENDING` but must not invent legal authority.

## Persistent consequences

Recovery should create later world texture:

- a returned crate can disappear from the recovery shelf and reappear in Brin's ordinary circulation;
- an instrument can remain tagged as recovered even after repair;
- a disputed object can occupy storage for weeks;
- a historical label can trigger an archive research thread;
- cleanup can visibly progress while one held object remains untouched;
- a false initial provenance claim can remain in history after correction;
- a storm can create several unrelated recoveries instead of one conspiracy.

## Questline integration

Likely canonical family tags for future authored content:

- `ITEM`
- `EQUIPMENT`
- `SETTLEMENT`
- `EXPLORATION`
- `REGION`
- `SECONDARY`
- `FACTION`
- `CHARACTER` when a resident's own history is central.

Do not create a new `SALVAGE` questline family. The canon taxonomy already supports these arcs compositionally.

## Implementation priority

First safe slice:

1. one persistent recovery object;
2. one discovery record;
3. one condition assessment;
4. one custody handoff;
5. one records check;
6. one downstream handoff or unresolved closure;
7. no battle requirement.

This tests the architecture with ordinary world-state surfaces before adding tactical pressure.