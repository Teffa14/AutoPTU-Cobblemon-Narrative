# Ouros Case, Authority & Custody Layer

Status: Proposed systems design. Not established canon.

## Purpose

The existing Ouros architecture already models missions, investigations, evidence, factions, settlements, public memory, clocks, persistent Pokémon and world actors. This layer formalizes the missing operational structure around incidents: who reports them, who is involved, which institution can respond, how evidence changes hands, how a moving target persists across the world, and how a case can resolve without requiring a defeat-all battle.

The design must remain flexible because Ouros has not yet established a universal legal system. `Authority` in this document means world-authored mandate or responsibility, not real-world law.

## 1. Case Object

A case is a persistent container for an unresolved incident or connected set of incidents.

```yaml
case:
  case_id: null
  status: OPEN
  incident_ids: []
  title_public: null
  title_internal: null
  origin_location_id: null
  current_location_ids: []
  lead_institution_id: null
  assisting_institution_ids: []
  assigned_actor_ids: []
  participant_ids: []
  affected_entity_ids: []
  evidence_ids: []
  claim_ids: []
  hypothesis_ids: []
  person_or_pokemon_of_interest_ids: []
  unresolved_questions: []
  response_state: null
  custody_records: []
  transfer_history: []
  linked_case_ids: []
  public_visibility: low
  mechanics_review_required: false
```

Suggested case states:
- INTAKE
- OPEN
- ACTIVE
- STALLED
- TRANSFER_PENDING
- TRANSFERRED
- RESOLVED
- CLOSED_INCOMPLETE
- REOPENED

A case may be resolved while some historical questions remain unknown.

## 2. Incident Intake

Cases originate from events rather than from arbitrary procedural prompts.

```yaml
incident_report:
  incident_id: null
  report_source_type: null
  reporter_id: null
  observed_event_ids: []
  location_id: null
  timestamp: null
  reported_claims: []
  immediate_risks: []
  affected_entities: []
  missing_entities: []
  damaged_or_missing_assets: []
  credibility_state: unreviewed
  intake_institution_id: null
```

Possible report sources:
- direct player discovery;
- NPC report;
- Pokémon behavior interpreted as a possible alert;
- settlement service report;
- faction report;
- research observation;
- public event incident;
- patrol/response actor;
- infrastructure alarm where supported;
- Chronicle callback.

The report contains claims. It does not become truth merely because an NPC filed it.

## 3. Mandate and Jurisdiction

Ouros needs explicit responsibility boundaries before it can generate institutional conflict fairly.

```yaml
institution_mandate:
  institution_id: null
  geographic_scope_ids: []
  incident_categories: []
  services_provided: []
  authority_tags: []
  restricted_actions: []
  escalation_targets: []
  handoff_partners: []
  emergency_scope: []
  canon_reference_ids: []
```

Candidate mandate categories may eventually include:
- settlement safety;
- route safety;
- ecological protection;
- research-site security;
- tournament/League administration;
- rescue and disaster response;
- transport security;
- heritage/ruins stewardship;
- cross-regional major investigations.

No institution receives any of these powers automatically. They must be established in Ouros canon.

### Jurisdiction rule

Before generating an official assignment, ask:
1. Which location owns the current problem state?
2. Which institutions have an authored mandate here?
3. Which incident type is being alleged?
4. Is this an emergency, an investigation, a service request or a faction conflict?
5. Has responsibility already been transferred?

If no institution has a valid mandate, the content may instead emerge as community self-help, a private request, faction action or unresolved regional problem.

## 4. Participation Roles

A player's relation to a case must be explicit.

```yaml
case_participant:
  case_id: null
  actor_id: null
  role: null
  invited_by_id: null
  access_level: null
  permitted_evidence_ids: []
  assigned_tasks: []
  conflicts_of_interest: []
```

Candidate roles:
- reporting_party;
- witness;
- affected_party;
- field_investigator;
- analyst;
- liaison;
- capability_specialist;
- rescue_responder;
- tactical_responder;
- logistics_support;
- local_guide;
- expert_consultant;
- voluntary_helper;
- person_of_interest.

These are narrative permissions and responsibilities. They do not create Trainer Classes or mechanical bonuses.

## 5. Capability-Assisted Evidence

Pokémon and Trainer capabilities can change which clues are accessible.

```yaml
clue_access_route:
  clue_id: null
  route_type: capability
  required_capability_refs: []
  required_skill_refs: []
  required_item_refs: []
  required_world_state: []
  observable_result_ids: []
  alternative_route_ids: []
  mechanics_review_required: true
```

Hard rules:
- verify the actual character or Pokémon state before presenting a capability route;
- the capability reveals an observation supported by the fiction, not the case's hidden truth;
- critical revelations need alternate access routes;
- do not invent capabilities from a species stereotype when the governed PTU data does not grant them;
- results generated from scent, special senses, Aura, tracking, terrain access or similar powers require the corresponding PTU/Caelo rule reference.

This directly extends the Evidence Graph in `world-agency-layer.md`.

## 6. Evidence Custody

Evidence needs identity and history.

```yaml
evidence_custody:
  evidence_id: null
  source_event_id: null
  discovered_by_ids: []
  discovery_location_id: null
  discovery_timestamp: null
  acquisition_method: null
  initial_state: null
  current_custodian_id: null
  current_storage_location_id: null
  custody_events: []
  access_log: []
  integrity_state: intact
  authenticity_state: unknown
```

Custody event types can include:
- DISCOVERED
- DOCUMENTED
- COLLECTED
- LEFT_IN_PLACE
- TRANSFERRED
- EXAMINED
- RETURNED
- LOST
- STOLEN
- DAMAGED
- DESTROYED
- SEALED
- RELEASED

### Evidence integrity rule

Changing custody does not change the canonical event that produced the object. It changes confidence, accessibility, admissibility within fictional institutions, and future investigative options.

The system should preserve raw provenance even when an in-world item disappears.

## 7. Hypotheses and Case Theories

World truth, evidence and investigator theory remain separate.

```yaml
case_hypothesis:
  hypothesis_id: null
  case_id: null
  author_ids: []
  claim_ids: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  unresolved_dependencies: []
  confidence: null
  status: ACTIVE
```

Suggested hypothesis states:
- PROPOSED
- ACTIVE
- WEAKENED
- CONTRADICTED
- SUPPORTED
- RETRACTED
- UNRESOLVED

A supported hypothesis is still not automatically canonical truth unless the underlying facts establish it.

## 8. Accusation and Attribution

Accusing an NPC, faction or player-character-adjacent entity can create public consequences even when the accusation is wrong.

```yaml
attribution_event:
  case_id: null
  attributed_actor_ids: []
  made_by_ids: []
  evidence_cited: []
  venue: private
  confidence_declared: null
  public_record_created: false
  later_status: unresolved
```

This connects to the Public Memory layer.

Possible later statuses:
- CONFIRMED
- RETRACTED
- DISPUTED
- DISPROVEN
- UNRESOLVED

Do not rewrite relationship or reputation state globally simply because a player selected an accusation dialogue option. Apply consequences through witnesses, institutions and affected actors.

## 9. Response State

A case can require immediate operational work before anyone knows the cause.

```yaml
case_response:
  case_id: null
  active_intentions: []
  protected_entities: []
  hazard_ids: []
  target_ids: []
  secured_location_ids: []
  evacuation_state: null
  pursuit_state_id: null
  handoff_required: false
```

Candidate intentions:
- OBSERVE
- WARN
- SEARCH
- RESCUE
- ESCORT
- EVACUATE
- SECURE
- PROTECT
- RECOVER
- CONTAIN
- NEGOTIATE
- PURSUE
- INTERCEPT
- INTERRUPT
- TRANSFER

These describe narrative intent. Any action that enters PTU combat or Minecraft interaction requires implementation validation.

## 10. Pursuit State

A moving target should persist as world state.

```yaml
pursuit_state:
  pursuit_id: null
  case_id: null
  target_ids: []
  last_confirmed_location_id: null
  last_confirmed_event_id: null
  probable_route_ids: []
  known_resources: []
  known_allies: []
  actor_observations: []
  misinformation_ids: []
  current_behavior: unknown
  visibility: partial
```

Possible behaviors:
- stationary/hiding;
- traveling;
- seeking shelter;
- contacting allies;
- attempting to cross jurisdiction;
- abandoning property;
- taking a hostage only if canon/authored content explicitly supports it;
- attempting surrender;
- continuing another objective.

World Pulse may move a target only when the target has a plausible route, resources and motive. Do not teleport fugitives to create drama.

## 11. Custody and Resolution Outcomes

Not every threat resolution is imprisonment or capture.

```yaml
case_resolution:
  case_id: null
  resolution_type: null
  resolved_fact_ids: []
  unresolved_fact_ids: []
  target_outcomes: []
  asset_outcomes: []
  evidence_outcomes: []
  transfer_outputs: []
  public_outputs: []
  chronicle_event_ids: []
  followup_case_ids: []
```

Candidate resolution types:
- recovered;
- rescued;
- returned;
- voluntarily surrendered;
- transferred_to_institution;
- released;
- relocated;
- escaped;
- threat_contained;
- misunderstanding_resolved;
- no_responsible_actor_found;
- unresolved_but_inactive;
- referred_to_another_case.

Which outcomes are legally/socially valid depends on future Ouros canon.

## 12. Institutional Handoff

Cases can change ownership without losing history.

```yaml
case_transfer:
  case_id: null
  from_institution_id: null
  to_institution_id: null
  reason: null
  timestamp: null
  evidence_transferred: []
  information_withheld: []
  outstanding_actions: []
  acknowledged_by_ids: []
```

Potential reasons:
- geography changed;
- incident scope escalated;
- specialist expertise required;
- conflict of interest;
- emergency phase ended;
- local capacity exceeded;
- linked case discovered;
- institution lost mandate or access.

A handoff can create social friction, but disagreement should be rooted in actual motives or institutional design.

## 13. Jurisdiction Conflict

Overlap can become playable content.

```yaml
mandate_conflict:
  conflict_id: null
  case_id: null
  institution_ids: []
  disputed_scope: null
  shared_goals: []
  conflicting_goals: []
  procedural_blockers: []
  compromise_options: []
```

Useful conflicts:
- conservation vs transport access;
- local settlement control vs regional expertise;
- research secrecy vs public safety;
- event organizer continuity vs emergency evacuation;
- Gym civic role vs specialist investigation;
- private property claim vs ecological protection.

Avoid manufacturing conflict through incompetence alone. Each side should usually have a coherent reason for its position.

## 14. Emergency-to-Investigation Transition

One incident can change activity type over time.

Example state sequence:

```text
hazard discovered
-> rescue / containment
-> scene stabilized
-> evidence documented
-> cause investigation
-> responsibility dispute
-> repair / prevention
-> public aftermath
```

This connects existing activity lanes without forcing all stages into one quest.

Players who only participate in the rescue still create Chronicle facts used by later investigators.

## 15. Accountability and Institutional Memory

Organizations should record operational failures as well as victories.

```yaml
institution_review:
  review_id: null
  institution_id: null
  source_case_ids: []
  trigger_event_ids: []
  findings_claim_ids: []
  disputed_findings: []
  policy_change_candidates: []
  personnel_effects: []
  public_visibility: null
```

Possible outputs:
- changed training;
- changed access policy;
- new equipment request;
- leadership dispute;
- public apology;
- cover-up attempt if specifically authored;
- no change despite criticism;
- improved coordination with another institution.

This gives institutions long-term character without requiring them to be heroic or corrupt by default.

## 16. Low-Governance Areas

Not every region should have formal authority nearby.

A location may instead depend on:
- local custom;
- settlement council;
- community volunteers;
- a profession guild;
- a powerful faction;
- a Gym or institution with informal legitimacy;
- no reliable responder at all.

The generator must not spawn a universal officer or agency simply because `incident=true`.

## 17. Multiplayer Case Separation

Different players can hold different case access and knowledge.

One character may interview an NPC while another follows a physical trail and another analyzes records in town.

The case state should merge confirmed shared discoveries without leaking private evidence automatically.

Suggested fields:

```yaml
case_view:
  case_id: null
  viewer_id: null
  visible_evidence_ids: []
  visible_claim_ids: []
  private_notes: []
  institution_shared_notes: []
  public_case_notes: []
```

## 18. PTU / Caelo Boundary

This layer defines narrative orchestration only.

Before any capability-assisted clue, pursuit action, contested interaction, capture, restraint, hazardous scene or battle becomes executable, validate against the project's governing sources and AutoPTU state.

Required validation can include:
- actual Skill ranks;
- legal Pokémon capabilities;
- special senses;
- movement and traversal;
- opposed Skill Checks;
- Trainer Features;
- Moves and action economy;
- inventory ownership;
- capture rules;
- environmental hazards;
- encounter objectives;
- any Caelo-specific rules explicitly retained by Ouros.

This document does not define warrant systems, arrest powers, criminal codes, ownership law, sentencing, detention, search powers or real-world legal procedure.

## 19. Minecraft / AutoPTU Mapping

Potential overworld-facing state:
- case board entry;
- restricted or secured location marker;
- investigator/responding NPC presence;
- evidence object state;
- NPC availability for interview;
- target last-known-location marker based on player knowledge;
- route checkpoint only when canon supports it;
- transfer courier/NPC;
- rescue perimeter;
- changed dialogue after public accusation;
- case archive record.

Potential tactical encounter requests:
- protect evidence;
- protect/escort target;
- escape;
- intercept;
- contain;
- force retreat;
- rescue;
- recover item;
- surrender/negotiation transition.

AutoPTU must own legality and results.

## 20. Implementation Priority

Recommended order:
1. case and incident schema;
2. participation roles;
3. evidence custody history;
4. capability-assisted clue gates;
5. hypotheses separated from truth;
6. case views / knowledge separation;
7. institution mandate registry;
8. transfer/handoff state;
9. pursuit state;
10. response and non-elimination objectives;
11. institutional review/history.

This layer gives existing mysteries, factions and world events a durable operational backbone without forcing Ouros to decide its final legal/political system prematurely.
