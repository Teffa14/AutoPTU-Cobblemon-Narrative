# Memorial, Absence & Succession Continuity Extension

Status: proposed systems design. Not established canon.

## Purpose

This extension gives Ouros a safe way to represent absence, confirmed loss, remembrance and continuity after an actor is no longer present.

It does not decide whether death exists as a normal campaign consequence. It does not infer death from defeat, fainting, disappearance or retirement. It does not create inheritance law, ownership transfer, spiritual mechanics or emotional states.

Its job is narrower:

- preserve what is known about an absence;
- distinguish confirmed facts from public belief;
- maintain memorial places and practices over time;
- route unresolved role, object, residence and Pokémon questions to the systems that own them;
- create return visits and world changes without fabricating posthumous canon.

## Ownership boundaries

Public Memory owns community interpretation, commemoration history and contested narratives.

Archives/Collections owns records, documents, preserved collections and provenance.

Material Culture owns physical object instances and provenance.

Residential Life owns occupancy and former-home continuity.

Workplace/Institution systems own role staffing and service continuity.

Case/Authority owns formal missing-person, identity, custody or evidence procedures where those procedures exist.

Care/Recovery owns health and recovery state before any confirmed-loss fact.

Myth/Anomalous systems own spiritual claims, apparitions and supernatural interpretation.

This extension owns the continuity bridge between absence facts and those systems.

## Absence state

```yaml
absence_record:
  absence_id: null
  actor_id: null
  first_noted_at: null
  last_verified_presence_at: null
  last_verified_location_id: null
  current_state: UNKNOWN
  source_fact_ids: []
  public_claim_ids: []
  private_claim_ids: []
  active_case_ref: null
  expected_return_window: null
  return_event_id: null
  closure_fact_id: null
```

Candidate states:

- TEMPORARILY_AWAY
- TRAVELING
- RELOCATED
- RETIRED
- UNREACHABLE
- MISSING
- PRESUMED_DEAD_BY_ACTORS
- PUBLICLY_REPORTED_DEAD
- CANONICALLY_CONFIRMED_DEAD
- RETURNED
- UNKNOWN

The state name must reflect the strongest validated world fact available to the server, not the most dramatic public theory.

`PRESUMED_DEAD_BY_ACTORS` and `PUBLICLY_REPORTED_DEAD` remain claim-bearing states. They do not authorize posthumous canon generation.

## Confirmed-loss gate

```yaml
confirmed_loss_ref:
  actor_id: null
  fact_id: null
  confirmation_scope: null
  confirmed_at: null
  source_authority: canonical_world_state
  public_visibility: restricted
```

A narrative generator may only write the actor as deceased when a valid canonical fact reference exists.

Battle defeat, 0 HP, fainting, Injury, missing roster state, absent NPC spawn, old age, disappearance, rumor, memorial marker or another actor's statement are insufficient by themselves.

For retired PCs, the existing retired-character boundary remains stronger than this extension. The system cannot decide that a retired PC later died.

## Memorial site

```yaml
memorial_site:
  site_id: null
  location_id: null
  site_type: null
  steward_ids: []
  commemorated_subject_ids: []
  marker_ids: []
  access_state: OPEN
  upkeep_state: STABLE
  public_access_policy_ref: null
  ecological_overlap_refs: []
  cultural_practice_refs: []
  incident_history: []
  revision_history: []
```

Possible site types are descriptive only until canon approves local traditions:

- CEMETERY
- MEMORIAL_GARDEN
- SHRINE_LIKE_SITE
- MONUMENT
- BELL_TOWER
- WALL_OR_PLAQUE
- ROUTE_MARKER
- PRESERVED_ROOM
- ARCHIVAL_MEMORIAL
- PRIVATE_MARKER
- OTHER

A region should not receive a generic cemetery merely because this system exists.

## Memorial marker

```yaml
memorial_marker:
  marker_id: null
  site_id: null
  subject_ids: []
  inscription_claim_ids: []
  verified_identity_fields: []
  unresolved_identity_fields: []
  commissioning_actor_ids: []
  installed_at: null
  revision_ids: []
  physical_condition_ref: null
  provenance_ref: null
```

The inscription is a public statement. It is not automatically canonical truth.

If new evidence changes a name, date, attribution or description, create a revision event rather than replacing history silently.

## Marker revision

```yaml
marker_revision:
  revision_id: null
  marker_id: null
  requested_by_ids: []
  reason_claim_ids: []
  evidence_refs: []
  approved_by_ref: null
  prior_text_ref: null
  new_text_ref: null
  completed_at: null
```

Approval rules are canon/institution dependent. This extension does not invent who has authority to alter memorials.

## Remembrance participation

```yaml
remembrance_event:
  event_id: null
  participant_ids: []
  subject_ids: []
  site_id: null
  timestamp: null
  observable_actions: []
  public_visibility: private
  object_refs: []
  statement_claim_ids: []
  emotional_labels: []
```

`emotional_labels` should remain empty unless explicitly authored or canonically established.

Safe observable actions include:

- VISITED
- CLEANED_MARKER
- LEFT_APPROVED_OFFERING
- RANG_BELL
- READ_NAME
- SPOKE_PUBLICLY
- REQUESTED_PRIVACY
- DECLINED_PUBLIC_CEREMONY
- REQUESTED_CORRECTION
- MAINTAINED_PATH
- ATTENDED_ANNIVERSARY

The system may remember that an actor returned every year. It may not infer that grief became stronger, weaker or resolved.

## Memorial object custody packet

Objects connected to a deceased or absent actor are not automatically rewards or inheritances.

```yaml
memorial_object_handoff:
  handoff_id: null
  object_ids: []
  prior_holder_ref: null
  current_custodian_ref: null
  claimed_owner_refs: []
  requested_destination_refs: []
  governing_rule_ref: null
  status: UNRESOLVED
```

Possible statuses:

- UNRESOLVED
- TEMPORARY_CUSTODY
- ARCHIVAL_HOLD
- RETURN_REQUESTED
- TRANSFER_AUTHORIZED
- TRANSFER_COMPLETED
- DISPUTED

No transfer occurs without an established rule or explicit canon decision.

## Pokémon continuity packet

A Pokémon associated with an absent or deceased Trainer requires special non-inference protection.

```yaml
pokemon_continuity_packet:
  pokemon_id: null
  associated_actor_id: null
  observed_relationship_refs: []
  current_custody_ref: null
  current_location_ref: null
  current_routine_refs: []
  ownership_status_ref: null
  care_plan_ref: null
  unresolved_questions: []
```

The extension must not infer:

- new ownership;
- automatic release;
- automatic inheritance;
- Loyalty change;
- willingness to battle for another Trainer;
- grief behavior;
- species-wide mourning behavior;
- spiritual connection to the deceased.

Observed routine changes can persist if the world actually records them.

## Role continuity handoff

```yaml
role_continuity_handoff:
  role_id: null
  prior_actor_id: null
  absence_ref: null
  service_impact_ref: null
  temporary_coverage_refs: []
  succession_rule_ref: null
  candidate_refs: []
  decision_ref: null
```

This object surfaces the operational question. Workplace, faction, civic or institutional systems decide what happens next.

The generator cannot infer hereditary succession, promotion, election, appointment or ownership merely because a role is vacant.

## Memorial stewardship

Memorial spaces can produce ordinary world-state work:

- path repair;
- vegetation management;
- accessibility work;
- marker cleaning;
- record correction;
- visitor guidance;
- temporary closure after weather or construction;
- protection during nearby public works;
- ecological coexistence management;
- replacement of damaged signage;
- coordination with archives when identity records conflict.

These hooks keep memorial sites alive without turning every visit into a supernatural encounter.

## Access state

```yaml
memorial_access_state:
  site_id: null
  state: OPEN
  reason_refs: []
  affected_paths: []
  temporary_access_refs: []
  review_at: null
```

Candidate states:

- OPEN
- LIMITED
- CLOSED_FOR_WORKS
- CLOSED_FOR_SAFETY
- PRIVATE_EVENT
- RESTORING
- UNKNOWN

Closure state belongs to real world conditions. It should not be generated solely to force a quest.

## Absence callback grammar

A durable absence arc can use:

1. routine establishes expected presence;
2. actor becomes absent for a validated reason or unresolved reason;
3. other systems register real consequences without deciding the cause;
4. claims and public interpretations emerge independently;
5. records, travel, case, communication or direct return narrow the state;
6. memorialization occurs only if death is canonically confirmed or an approved non-death commemoration exists;
7. role/object/residence/Pokémon questions receive explicit handoffs;
8. later visits preserve what changed.

## Memorial callback grammar

A memorial site can evolve through:

1. ordinary visit and baseline condition;
2. a marker, route or record becomes incomplete/damaged/contested;
3. investigation identifies what is physically wrong and what is historically uncertain;
4. stewardship repairs the site without pretending to resolve disputed history;
5. a record or inscription revision may occur through an authorized path;
6. later visits show the updated site and retain the old revision history.

## Minecraft representation

Safe visible state includes:

- marker condition;
- flowers or approved offerings;
- path access;
- maintenance barriers;
- steward NPC presence;
- visitor cohorts;
- revised inscription text;
- temporary closure signs;
- seasonal vegetation;
- a remembered object displayed under approved custody;
- a bell or ceremonial prop whose interaction is narrative only unless mechanics say otherwise.

The client must not display hidden confirmation facts to actors who should only know a rumor or public report.

## Encounter contract — Marker-Ridge Evacuation

Narrative premise: severe weather or nearby slope failure threatens access to a memorial ridge while visitors and stewards are present.

Full intended version may require:

- active civilian evacuation;
- changing safe routes;
- unstable terrain zones;
- weather effects;
- falling debris hazards;
- forced movement near edges;
- protection/withdrawal objectives;
- objective-aware AI;
- synchronized Minecraft playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic slope/weather effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Resolve visitor evacuation and route closure as world state before combat. Freeze one stable area outside fragile markers. If a battle occurs, include only legal combatants and verified mechanics. The tactical result cannot decide whether the site is historically significant, who owns memorial objects or whether a damaged marker may be moved.

## Encounter contract — Boundary-Nest Disturbance

Narrative premise: wild Pokémon begin using vegetation along the edge of a memorial site. Some visitors interpret damage as deliberate desecration, while field evidence suggests ordinary habitat pressure.

Full intended version may require:

- protected fragile zones;
- moving visitor groups;
- non-KO retreat/containment goals;
- interception;
- forced displacement;
- terrain-sensitive routing;
- objective-aware AI;
- persistent site playback.

Permanent dependency state is the same map above, with complete movement, environmental systems, tactical AI and adapter/playback BLOCKING where used.

Reduced version:

Close the affected section to visitors. Record marker/vegetation condition before combat. Use a static ordinary encounter only if conflict actually occurs away from fragile objects. Resolve habitat cause, responsibility and stewardship through observation/ecology state rather than the battle winner.

## Noncombat-ready scenes

The following can exist before missing tactical families are implemented:

- reconstructing an incomplete memorial identity from records;
- comparing an inscription against archival provenance;
- tracking marker revisions;
- recording anniversary visits;
- maintaining a path or sign through Facility Maintenance;
- returning an object to approved custody;
- observing a surviving Pokémon's routine without assigning emotion;
- handing a vacant role to Workplace/Institution systems;
- distinguishing public death reports from canonical confirmation;
- documenting that an actor returned after being missing.

## PTU/Caelo guardrails

PTU campaign tone does not require permanent death as a default consequence. Ouros therefore treats death as explicit canon state.

This extension cannot create:

- death from HP loss or fainting;
- Injury-to-death conversion;
- resurrection;
- spirit communication;
- Ghost-type identity with a deceased actor;
- supernatural memorial effects;
- mourning modifiers;
- Loyalty changes;
- automatic ownership transfer;
- automatic inheritance;
- automatic role succession;
- legal presumptions;
- burial or funeral practices not already approved for the relevant culture.

Any Move, Ability, item, Feature, occult class, Channeler-like effect, afterlife claim or supernatural interaction requires governing PTU/Caelo validation plus current AutoPTU implementation evidence.

## Integration flow

```text
presence history
→ absence record
→ claims/public report/case state
→ canonical resolution if available
→ optional memorial/commemoration
→ object/Pokémon/role/residence handoffs
→ stewardship and return visits
→ Public Memory / Archives / institutional history
```

No arrow may jump from rumor, memorial marker or battle defeat directly to canonical death.

## Promotion gate

Before any Ouros-specific cemetery, memorial custom, funeral practice, inheritance rule, caretaker role, religious interpretation, grave object, succession convention or Pokémon mourning practice becomes canon, review:

- regional culture fit;
- approved geography;
- institutional ownership/authority;
- privacy expectations;
- PTU/Caelo assumptions;
- player-authorship boundaries;
- Minecraft representation;
- overlap with Public Memory, Archives, Residential, Staffing, Care and Myth systems.
