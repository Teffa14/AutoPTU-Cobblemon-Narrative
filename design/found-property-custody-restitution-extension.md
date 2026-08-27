# Found Property, Custody & Restitution Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already tracks meaningful physical items, evidence custody, shipments, residences, public events, transit services, circulation records and persistent actor schedules. This extension handles the ordinary object that becomes separated from its holder outside an intended shipment and before it becomes a formal investigation.

Its job is to answer a narrow set of questions:

- What exact object was reported missing or found?
- When and where was it last known or recovered?
- Who currently has custody?
- Is there a plausible match between a found object and a loss report?
- Who has asserted a claim?
- What evidence supports or weakens that claim?
- Has the object actually been returned?
- Which existing system receives the handoff when the situation becomes a shipment problem, evidence issue, institutional collection matter or unresolved dispute?

The extension does not define universal property law. It does not decide that possession equals ownership. It does not turn Minecraft pickup state into narrative authority.

## 1. Authority boundaries

### Material Culture

`material-culture-economy-crafting-layer.md` owns persistent `item_instance` identity, provenance, current owner/custodian references, repair history and significance.

This extension references those records. It should not create a duplicate object identity when a persistent instance already exists.

### Courier

`courier-parcel-last-mile-logistics-extension.md` owns an object while it is inside an intended shipment lifecycle.

If a shipped parcel goes missing and is later found, the found-property record attaches a recovery event to that shipment. It does not replace delivery state or invent a parallel route.

### Case / Authority

`case-authority-custody-layer.md` owns formal incidents, evidence custody and institutional mandates.

If evidence suggests theft, tampering, fraud, violence, prohibited access or another authored case category, this extension stops adjudicating and creates a handoff candidate. A missing item alone is not proof of theft.

### Libraries / Archives / Collections

A circulating copy or institutional collection object remains governed by its circulation/accession layer. Found-property state can record where it was found and who recovered it, but cannot silently discharge a loan, change accession status or transfer ownership.

### Residential / Transit / Events / Storefront / Workplace

These systems own the routines and locations that can explain why an object was left behind, who had access and when a claimant may return. Found-property state references those facts.

## 2. Found property record

```yaml
found_property_record:
  found_property_id: null
  item_instance_id: null
  mechanical_item_ref: null
  current_state: FOUND_UNATTRIBUTED
  loss_report_ids: []
  find_event_id: null
  current_custodian_ref: null
  current_holding_location_id: null
  claimant_ids: []
  claim_assertion_ids: []
  possible_match_ids: []
  restitution_event_id: null
  linked_shipment_id: null
  linked_case_id: null
  source_refs: []
```

Suggested states:

- REPORTED_MISSING
- FOUND_UNATTRIBUTED
- FOUND_POSSIBLE_MATCH
- HELD_FOR_CLAIM
- CLAIM_PENDING
- CLAIM_DISPUTED
- RETURN_AUTHORIZED
- RETURN_IN_PROGRESS
- RETURNED
- REFERRED_TO_COURIER
- REFERRED_TO_CASE
- REFERRED_TO_COLLECTION
- UNCLAIMED_PENDING_REVIEW
- CLOSED_NO_RETURN

`CLOSED_NO_RETURN` means the found-property workflow ended without restitution. It does not specify disposal or new ownership.

## 3. Loss report

A loss report is a claim that an expected possession is missing.

```yaml
property_loss_report:
  loss_report_id: null
  reporter_id: null
  reported_holder_id: null
  item_instance_id: null
  mechanical_item_ref: null
  public_description: null
  private_verification_descriptors: []
  last_known_location_id: null
  last_known_time: null
  discovery_of_loss_time: null
  related_event_ids: []
  related_route_ids: []
  related_residence_ids: []
  related_service_ids: []
  report_state: OPEN
  source_refs: []
```

Suggested report states:

- OPEN
- POSSIBLE_MATCH
- MATCH_REJECTED
- WITHDRAWN
- OUTDATED
- RETURNED
- REFERRED
- CLOSED_UNKNOWN

Hard rules:

- a report can be mistaken or outdated;
- the reporter and reported holder may be different people;
- a report does not prove the object existed exactly as described;
- a report does not prove theft;
- public description and private verification detail should be separated when privacy matters.

## 4. Find event

```yaml
find_event:
  find_event_id: null
  item_instance_id: null
  finder_id: null
  finder_party_ids: []
  location_id: null
  found_at: null
  initial_condition_observation: null
  container_or_context_ref: null
  immediate_handoff_ref: null
  source_event_ids: []
  observation_refs: []
```

A find event establishes only that the object was observed/recovered at a place and time by specific actors.

It does not establish:

- who previously owned it;
- who dropped it;
- how long it was there;
- why it was there;
- whether it was stolen;
- whether the finder may keep it.

## 5. Temporary custody

```yaml
found_property_holding:
  holding_id: null
  found_property_id: null
  custodian_ref: null
  holding_location_id: null
  received_at: null
  received_from_ref: null
  observed_condition: null
  access_event_ids: []
  transfer_event_ids: []
  current: true
```

Custody should be explicit because the finder may hand the object to:

- the apparent holder directly;
- an approved staff member;
- a service desk;
- an institution with a canon mandate;
- a route/event/workplace operator responsible for the location;
- a courier only when an actual delivery/restitution shipment is created.

No generic “police lost-and-found” is assumed.

## 6. Possible matches

A matching process compares observations rather than generating certainty from a quest marker.

```yaml
property_match_candidate:
  match_id: null
  found_property_id: null
  loss_report_id: null
  supporting_evidence_refs: []
  contradicting_evidence_refs: []
  unresolved_questions: []
  match_state: POSSIBLE
  reviewed_by_ids: []
  updated_at: null
```

Suggested states:

- POSSIBLE
- PLAUSIBLE
- CONTRADICTED
- REJECTED
- VERIFIED_FOR_RETURN
- ESCALATION_REQUIRED

These states describe the workflow. They are not probabilities or a hidden truth score.

## 7. Claim assertions

```yaml
property_claim_assertion:
  claim_assertion_id: null
  found_property_id: null
  claimant_id: null
  asserted_relationship: null
  submitted_at: null
  public_claim_text_ref: null
  private_detail_refs: []
  evidence_refs: []
  contradiction_refs: []
  verification_state: UNREVIEWED
  requested_recipient_ref: null
```

Possible asserted relationships:

- PREVIOUS_HOLDER
- CURRENT_OWNER_CLAIM
- AUTHORIZED_PROXY
- INSTITUTIONAL_CUSTODIAN
- BORROWER
- MAKER_OR_REPAIRER
- SHIPMENT_RECIPIENT
- COLLECTION_CUSTODIAN
- OTHER_AUTHORED_RELATION

The label records what the claimant says. It does not grant that relationship.

## 8. Claim evidence

Evidence should remain concrete and attributable.

Strong claim evidence may include:

- a nonpublic identifying mark;
- contents known before recovery;
- a matching repair record;
- a commission or maker record;
- a prior photograph of the exact instance;
- a circulation or shipment identifier;
- a witness to a prior handoff;
- an item-instance provenance event;
- a timeline that puts the object with the claimant before the loss.

Weaker context may include:

- the claimant regularly visits the find location;
- the object resembles one the claimant usually carries;
- a friend says it probably belongs to them;
- a public description matches;
- the claimant arrives quickly.

Hard rule: no single evidence type is universally sufficient unless Ouros canon or a governing institutional rule says so.

## 9. Restitution event

```yaml
property_restitution_event:
  restitution_event_id: null
  found_property_id: null
  from_custodian_ref: null
  recipient_ref: null
  recipient_role: null
  location_id: null
  transferred_at: null
  authorization_basis_refs: []
  observed_condition: null
  acknowledgement_ref: null
  linked_courier_transfer_id: null
  linked_case_handoff_id: null
```

A restitution event records a physical handoff. It can update Material Culture's current custodian and, where the relevant authority explicitly establishes it, holder/owner state.

The handoff itself does not create a universal legal conclusion.

## 10. Unclaimed property

The extension can record that an item remains unclaimed. It must not invent what happens next.

```yaml
unclaimed_property_review:
  found_property_id: null
  review_at: null
  custodian_ref: null
  holding_duration_ref: null
  active_claim_ids: []
  governing_policy_ref: null
  disposition_state: PENDING_POLICY
```

Possible disposition states are deliberately conservative:

- PENDING_POLICY
- CONTINUE_HOLDING
- TRANSFERRED_TO_AUTHORIZED_SYSTEM
- CLOSED_WITH_CANON_DISPOSITION

Do not generate sale, finder ownership, destruction, donation or forfeiture unless a setting-specific policy is canon-approved.

## 11. Distinguishing lost, misplaced, abandoned and stolen

Narrative generation should avoid collapsing different possibilities into one label.

Candidate descriptive states:

- MISPLACED_SELF_REPORTED
- LEFT_BEHIND_OBSERVED
- DROPPED_OBSERVED
- FOUND_WITHOUT_LOSS_EVENT
- HOLDER_UNKNOWN
- ABANDONMENT_CLAIMED_BY_ACTOR
- THEFT_ALLEGED
- THEFT_EVIDENCE_PRESENT

Only observable facts and claims should be stored. “Abandoned” and “stolen” can carry authority implications, so the system should not promote them from intuition.

## 12. Privacy and actor knowledge

A found item can contain information without making that information public.

Examples:

- a closed notebook does not grant the finder its full contents;
- a labeled case may reveal a name while hiding contents;
- a photograph can be visible without identifying every person shown;
- an address label may be outdated after relocation;
- a medical or research object may require a specialized handoff without exposing its contents.

Actor knowledge should update only from what was actually observed, read or communicated.

## 13. Multi-object recovery

A recovered pile should not become one ownership bundle automatically.

```yaml
recovery_batch:
  recovery_batch_id: null
  find_event_ids: []
  item_instance_ids: []
  location_id: null
  recovered_at: null
  batch_context_ref: null
```

Each significant object keeps its own match and claim state. This matters after:

- event teardown;
- transit disruptions;
- building evacuation;
- storm cleanup;
- household moves;
- warehouse or workshop incidents.

## 14. Recurring holding points

A location can develop persistent lost-property routines without needing every item to be an NPC-scale quest.

Suggested aggregate state:

```yaml
found_property_service_state:
  service_node_id: null
  location_id: null
  operator_ids: []
  accepted_categories: []
  current_backlog_band: LOW
  named_found_property_ids: []
  current_constraints: []
  last_review_at: null
```

Backlog bands can remain qualitative:

- NONE
- LOW
- MODERATE
- HIGH

Only narratively significant items need individual persistence. Ordinary umbrellas or gloves can remain aggregate scenery unless one becomes important.

## 15. Integration examples

### Transit hub

A passenger cohort leaves behind a bag. Transit state supplies the departure/time evidence. Found-property state tracks recovery and claim. If the object must be sent onward, Courier starts only after an actual shipment is created.

### Public event

Teardown finds several objects after visitors leave. Event Operations supplies attendance/time/location context. Each named object has independent claim state.

### Residential relocation

An object appears at an old address after the resident moved. Residential history explains the stale location. It does not prove the former resident still owns the object.

### Workshop

A repair mark can support a claim because Material Culture remembers repair provenance. The repairer can identify workmanship without becoming the owner.

### Library

A personal insert found inside a returned book may create a found-property record. The book's circulation remains under the Library layer; the insert follows its own item/claim state.

### Memorial or absence context

Belongings connected to an absent person require a handoff to the memorial/absence/succession system. Found-property logic cannot infer inheritance or next owner.

## 16. Noncombat encounter — Three Claimants, One Camera Case

Premise:

A distinctive camera case is found after a crowded public day. Three actors independently claim it. Each knows some correct details, but only one timeline fits the exact repair mark, prior photograph and last observed handoff.

Play loop:

- document the find context;
- separate public description from private verification details;
- inspect existing provenance/repair evidence;
- compare witness timelines;
- identify shared-source testimony so apparent corroboration is not overcounted;
- authorize or decline a return;
- preserve unresolved questions if evidence remains insufficient.

No battle is required. The encounter can run with persistent narrative state now.

## 17. Tactical encounter — Trail Satchel Recovery

Premise:

A personally significant satchel was reported missing along a route. A later route inspection locates the exact object in an area currently occupied by hostile or defensive Pokémon.

### Intended full version

The full encounter may use:

- an exact recoverable object outside ordinary loot generation;
- search/withdrawal or area-access objective;
- route terrain and weather where mechanically mapped;
- changing safe approach lanes;
- forced movement/interception near the recovery area;
- AI that may defend territory, withdraw or block access instead of maximizing KOs;
- synchronized playback so object recovery occurs only after a valid world-state handoff.

Capability dependency:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

### Reduced version

Freeze the satchel as narrative world state outside tactical targeting. Close the unsafe search area while combat is active. Run a reviewed static battle using only verified/basic-supported mechanics. After the authoritative battle result makes the area safe, perform the recovery as a separate world interaction.

The battle result can establish that the route threat was resolved during that encounter. It cannot prove who owns the satchel or whether the contents match a claimant's statement.

## 18. Tactical encounter — Event Teardown Recovery Sweep

Premise:

After a temporary public event closes, teardown staff discover a cluster of lost objects near a section that wild Pokémon have begun using again.

### Intended full version

Potential mechanics:

- several protected search/recovery zones;
- workers withdrawing while Pokémon re-enter the site;
- fragile scenery or temporary barriers;
- dynamic route access;
- interception/forced movement;
- environmental hazards if supported;
- AI with territorial/retreat objectives;
- adapter playback preserving which items were recovered before/after the disturbance.

Capability dependency:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when active
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

### Reduced version

Teardown workers leave the contested section before combat. Named objects stay represented in persistent world state rather than as targetable battle entities. Run a static encounter to clear/improve access. Afterwards, conduct the recovery sweep and create individual find events for significant objects.

The outcome never grants ownership to the battler who wins.

## 19. Minecraft / Cobblemon representation

Safe future representations include:

- showing a named lost object as a single persistent prop only when its exact item instance matters;
- rendering an aggregate lost-property shelf for ordinary items;
- syncing a named object's visible location to current custody state;
- letting an NPC dialogue expose only the claim details that actor actually knows;
- hiding/restoring the prop after an authoritative restitution event;
- preserving the record across chunk unloads and restarts;
- spawning a future callback when the verified recipient is encountered again.

Unsafe shortcuts include:

- giving ownership to whoever breaks/picks up the Minecraft prop;
- using despawn as evidence that an object was returned;
- recreating a supposedly unique object after chunk load;
- exposing private verification details to every claimant;
- using item NBT alone as canon provenance if narrative state disagrees;
- making victory automatically complete the return;
- making a dropped Minecraft item enter combat as an `items` mechanic without PTU support.

## 20. Canon questions

Before this extension can become setting-specific, Ouros needs decisions on:

- which places accept found property;
- whether transit/event/workplace operators have explicit lost-property responsibilities;
- what identification practices exist;
- which claim evidence is culturally/institutionally persuasive;
- whether different regions use different customs;
- how privacy is handled;
- whether rewards to finders are normal, optional or absent;
- how proxies are authorized;
- how unclaimed property is handled;
- which item categories require special custody or case escalation.

Until those decisions exist, generation should remain descriptive and conservative.

## Design conclusion

Found property is a continuity system, not a loot system. Its value comes from exact object identity, a traceable recovery, incomplete claims, temporary custody and a later handoff that changes a relationship or routine. It can create memorable stories at settlement scale while staying mechanically lightweight and respecting the authority boundaries already established elsewhere in Ouros.