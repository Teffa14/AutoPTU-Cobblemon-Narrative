# Worker Associations, Collective Representation & Safety Voice Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

The Workplaces layer already models roles, shifts, training, staffing and institutional knowledge. Civic Governance can identify stakeholder groups. Agreements can store negotiated commitments. Institutional Review can issue bounded decisions.

This layer adds the missing worker-created institution model.

It supports:

- professional and craft associations;
- workplace committees;
- safety voice groups;
- shift councils;
- mutual-aid networks;
- cross-workplace professional societies;
- player-founded worker organizations;
- representation mandates;
- collective proposals and positions;
- coordinated workplace actions;
- institutional memory across careers.

It does not define Ouros labor law.

## 1. Hard separations

The generator must preserve these distinctions:

- employee != association member;
- association member != represented on every issue;
- represented != agreeing with the representative;
- workplace majority != unanimity;
- spokesperson != manager;
- association influence != legal authority;
- guild membership != PTU Trainer Class;
- craft reputation != mechanical crafting bonus;
- safety concern != confirmed hazard;
- reported hazard != mechanical hazard;
- work stoppage != crime;
- management disagreement != villainy;
- association position != canonical truth;
- negotiation != enforceable contract;
- mutual aid != ownership transfer;
- worker organization != faction hostility state.

## 2. Worker association

```yaml
worker_association:
  association_id: null
  public_name: null
  association_type: craft|profession|workplace|safety|mutual_aid|cross_workplace|informal
  founded_at: null
  dissolved_at: null
  workplace_ids: []
  profession_domains: []
  member_actor_ids: []
  former_member_actor_ids: []
  membership_rules_ref: null
  representation_scope_ids: []
  spokesperson_actor_ids: []
  meeting_location_ids: []
  archive_id: null
  mutual_aid_pool_id: null
  public_contact_routes: []
  status: active
  history_event_ids: []
```

An association can exist without statutory recognition.

## 3. Association types

Possible types are descriptive only.

Craft association:
Preserves tools, techniques, apprenticeships, shared workshops, quality discussions and professional history.

Professional society:
Connects people who perform similar work across multiple institutions.

Workplace committee:
Represents a specific workplace or defined group of workers.

Safety voice group:
Collects observations and concerns about workplace conditions.

Mutual-aid network:
Coordinates voluntary support such as emergency coverage, transport, temporary equipment sharing or care support.

Cross-workplace network:
Coordinates workers from several employers/institutions around a shared route, port, utility or profession.

Informal group:
A persistent but lightly structured network. It can later formalize, remain informal or dissolve.

## 4. Membership state

```yaml
association_membership:
  membership_id: null
  association_id: null
  actor_id: null
  joined_at: null
  left_at: null
  membership_basis: null
  role_ids: []
  voting_scope_ids: []
  representation_opt_in: null
  status: active
  source_event_ids: []
```

Membership must not be inferred from occupation alone.

A blacksmith can decline to join a smiths’ association.

A former employee can remain a professional-society member after leaving a workplace if the organization’s authored rules allow it.

## 5. Representation mandate

Representation must be scoped.

```yaml
representation_mandate:
  mandate_id: null
  association_id: null
  represented_actor_ids: []
  represented_group_ref: null
  issue_scope: []
  authorized_representative_ids: []
  granted_at: null
  expires_at: null
  source_procedure_id: null
  limitations: []
  status: active
```

Examples:

- safety conditions in one mine;
- schedule changes at one ferry terminal;
- professional standards for a regional craft;
- emergency staffing coordination;
- a single negotiation over a workshop closure.

A representative must not speak for private beliefs or unrelated political positions.

## 6. Member positions and dissent

```yaml
member_position_record:
  position_record_id: null
  association_id: null
  issue_id: null
  actor_id: null
  expressed_position: support|oppose|abstain|mixed|no_position
  stated_reasons: []
  privacy: association_only
  recorded_at: null
  source_event_ids: []
```

This prevents the association from becoming a hive mind.

Public summaries may report an adopted position without exposing individual votes unless canon and privacy rules permit it.

## 7. Association decision procedure

```yaml
association_decision:
  decision_id: null
  association_id: null
  issue_id: null
  procedure_ref: null
  eligible_participant_ids: []
  participation_ids: []
  proposal_ids: []
  adopted_position_id: null
  dissent_summary_id: null
  decided_at: null
  status: complete
```

Ouros does not assume elections, simple majority, consensus or any other procedure globally.

Each organization must define or inherit its own process.

## 8. Workplace observation and worker knowledge

Workers can generate high-value observations because they repeatedly occupy the same operational environment.

```yaml
worker_observation:
  observation_id: null
  observer_actor_ids: []
  workplace_id: null
  shift_id: null
  observed_at: null
  observation_type: equipment|route|pokemon_behavior|service|process|environment|near_miss|other
  raw_observation: null
  evidence_refs: []
  interpretation_claim_ids: []
  submitted_to_ids: []
  privacy: internal
```

Observation stays separate from interpretation.

Example:

Observed: three line crews independently report a vibration after midnight.

Not automatically true: the transformer is failing.

## 9. Safety concern

```yaml
safety_concern:
  concern_id: null
  workplace_id: null
  submitted_by_ids: []
  association_id: null
  observation_ids: []
  claimed_hazard: null
  affected_area_ids: []
  affected_role_ids: []
  requested_actions: []
  status: reported
  review_ids: []
  outcome_refs: []
```

Suggested states:

- REPORTED
- ACKNOWLEDGED
- UNDER_REVIEW
- MORE_EVIDENCE_NEEDED
- INTERIM_CONTROL
- SUPPORTED
- NOT_SUPPORTED
- PARTIALLY_SUPPORTED
- RESOLVED
- SUPERSEDED

A safety concern never creates PTU hazard mechanics by itself.

## 10. Safety voice groups

A safety voice group can coordinate:

- inspections;
- worker observations;
- near-miss reports;
- procedure review;
- training feedback;
- emergency-plan feedback;
- equipment concerns;
- route/access concerns;
- environmental observations;
- follow-up tracking.

Its authority must remain authored.

It may have advisory influence only.

## 11. Collective proposal

```yaml
collective_proposal:
  proposal_id: null
  association_id: null
  subject_refs: []
  requested_state: []
  supporting_observation_ids: []
  supporting_evidence_ids: []
  expected_tradeoffs: []
  affected_worker_group_ids: []
  affected_service_ids: []
  submitted_to_ids: []
  status: submitted
```

This can feed:

- Agreements;
- Civic Governance;
- Institutional Review;
- Workplaces;
- Infrastructure;
- Manufacturing;
- Crisis planning.

## 12. Collective position

```yaml
collective_position:
  position_id: null
  association_id: null
  issue_id: null
  adopted_at: null
  position_text: null
  supporting_decision_id: null
  support_count_or_band: null
  dissent_summary: null
  expires_at: null
  status: active
```

A collective position is what the organization adopted.

It is not proof that the claim behind it is correct.

## 13. Negotiation handoff

When an association enters structured negotiation, Agreements owns the negotiation session and accepted commitments.

This layer supplies:

- authorized representatives;
- adopted positions;
- membership scope;
- worker observations;
- requested outcomes.

Agreements supplies:

- proposal versions;
- acceptance;
- commitments;
- compliance;
- breach claims;
- amendment history.

## 14. Collective action event

Collective action is stored as observable behavior without a built-in moral or legal conclusion.

```yaml
collective_action_event:
  action_event_id: null
  association_id: null
  participant_actor_ids: []
  action_type: meeting|petition|delegation|refusal|pause|work_stoppage|work_to_rule|mutual_aid|public_statement|other
  target_issue_ids: []
  started_at: null
  ended_at: null
  stated_reason_ids: []
  operational_effect_ids: []
  public_information_ids: []
  legality_claim_ids: []
  status: complete
```

Do not infer legality, misconduct, sabotage or hostility.

## 15. Work refusal and stop-work boundary

A single worker can refuse an assignment.

A group can pause work together.

Possible observed causes include:

- safety concern;
- missing qualification;
- unavailable protective equipment;
- unclear instruction;
- schedule conflict;
- disputed procedure;
- missing materials;
- environmental change;
- equipment condition;
- unresolved agreement;
- personal reason;
- collective action.

The system must store the stated reason and evidence rather than choosing a hidden motive.

## 16. Service consequences

Collective action may affect service state through the Workplaces layer.

Examples:

- reduced ferry frequency;
- delayed manufacturing run;
- mine section closure;
- archive backlog;
- clinic staffing shortage;
- delayed repairs;
- market inspection backlog.

Consequences are operational facts.

They are not automatically evidence that the action was good, bad, justified or unjustified.

## 17. Mutual aid

```yaml
mutual_aid_commitment:
  aid_id: null
  association_id: null
  provider_actor_or_group_ids: []
  recipient_actor_or_group_ids: []
  aid_type: coverage|transport|equipment|food|temporary_workspace|care_support|information|other
  trigger_conditions: []
  resource_refs: []
  start_time: null
  expected_end_time: null
  status: planned
```

Finance, Supply Chains, Travel, Care or Workplaces retain authority over the actual resources/services.

Mutual aid does not create infinite stock.

## 18. Professional and craft associations

A professional association can maintain:

- technique archives;
- shared terminology;
- apprenticeships;
- training workshops;
- peer review;
- conferences;
- tool libraries;
- mutual aid;
- historical records;
- public directories;
- referrals.

None of those grant a PTU Feature, Skill Rank, recipe or crafting bonus by default.

## 19. Apprenticeship integration

Workplaces still owns workplace training.

Education owns formal learning programs.

Credentials owns recognized qualifications.

This layer can sponsor or coordinate an apprenticeship network, but it cannot convert participation into mechanical progression without PTU/Caelo authority.

## 20. Former workers and retirees

Associations may preserve institutional memory through former workers.

Possible roles:

- archive contributor;
- mentor;
- honorary member;
- retired craft expert;
- historical witness;
- emergency adviser.

A former worker does not regain expired facility access, command authority or current employment by being consulted.

## 21. Cross-workplace associations

Some organizations can span multiple workplaces.

Examples:

- ferry engineers from three ports;
- rural clinic staff network;
- regional survey technicians;
- blacksmiths across several towns;
- mine rescue volunteers;
- archivists’ society;
- market inspectors’ forum;
- railway maintenance mutual-aid group.

This can create interregional story arcs without requiring a political faction.

## 22. Player-founded associations

Players may create a worker/professional organization if canon permits.

The system should track:

- founding event;
- declared scope;
- membership;
- procedures;
- projects;
- assets;
- agreements;
- public statements;
- representation mandates;
- archive/history.

Founding an association does not grant legal authority.

## 23. Pokémon participation

Pokémon may participate in workplaces as persistent actors when already supported by the Workplaces/Pokémon Agency layers.

A human worker association does not automatically represent Pokémon.

Possible authored alternatives:

- individual Pokémon partner participation;
- handler-mediated observations;
- institutional stewardship representation;
- explicit player decisions for PC-owned Pokémon;
- species-specific communication when a validated PTU mechanic supports it.

Do not infer Pokémon consent from ownership.

## 24. Pokémon observations as workplace evidence

Repeated Pokémon behavior may be relevant workplace evidence.

Examples:

- a mine partner refuses one tunnel repeatedly;
- a ferry-associated Pokémon changes approach behavior;
- an institutional Pokémon stops using one machine;
- a utility Pokémon avoids one substation section.

Record the behavior.

Do not automatically diagnose fear, Injury, abuse, contamination or equipment failure.

## 25. Public communication

Media/Communications owns publication and delivery.

An association may issue:

- a statement;
- safety bulletin;
- meeting notice;
- position paper;
- correction;
- call for volunteers;
- public report.

Publication does not make the claim true.

## 26. Political neutrality boundary

This layer must not assume that every settlement uses the same labor institutions.

Possible regional outcomes include:

- no formal worker associations;
- craft guilds only;
- workplace committees;
- mutual-aid societies;
- professional societies;
- worker councils;
- employer-sponsored forums;
- independent associations;
- mixed systems.

Canon must choose where appropriate.

## 27. Labor-law boundary

Unresolved unless deliberately authored:

- statutory recognition;
- bargaining obligations;
- strike rights;
- lockouts;
- wages;
- overtime;
- employment contracts;
- dismissal rules;
- pensions;
- compensation systems;
- labor courts;
- mandatory safety committees;
- child labor rules;
- Pokémon labor rights.

Do not import a contemporary national legal system by default.

## 28. Narrative generation rules

Good worker-association hooks arise from actual world state:

- repeated observations;
- staffing shortages;
- procedure changes;
- new technology;
- route failures;
- environmental changes;
- safety incidents;
- apprenticeship gaps;
- succession;
- supply shortages;
- disputed schedules;
- public works;
- crisis response;
- institutional restructuring.

Do not generate “labor unrest” merely because the story has been quiet.

## 29. Conflict without villains

Useful conflicts include:

- workers want an immediate closure while management wants more evidence;
- two worker groups prioritize different risks;
- a safety committee and conservation team disagree about access;
- a craft association resists a process revision because old tools remain common;
- younger members want formal certification while older members favor apprenticeship;
- a mutual-aid network can cover one town but not all three;
- workers support a new facility but oppose its schedule;
- two associations both legitimately represent different affected groups.

## 30. Minecraft representation

Possible visible state:

- association hall or meeting room;
- notice board;
- workshop commons;
- shared tool library;
- safety map;
- archived shift reports;
- meeting schedule;
- public statement board;
- mutual-aid depot;
- training sessions;
- temporary closure signage;
- workers gathering before/after shifts.

Minecraft displays current state. It does not decide membership, representation or legitimacy.

## 31. Privacy

Private state may include:

- individual votes;
- membership status where sensitive;
- complaints;
- health/safety reports with identifying details;
- negotiation strategy;
- internal deliberation;
- private contact information.

Public state may include only what the association actually publishes.

## 32. Encounter dependency boundary

Most worker-association content should remain non-combat.

When a separate incident creates a battle, use FULL and REDUCED contracts.

A battle result can establish:

- who was present;
- legal actions taken in combat;
- damage/status/results supported by AutoPTU;
- whether a tactical route was cleared if the objective exists in the engine.

A battle result cannot establish:

- legitimacy of a collective action;
- truth of a safety claim;
- association membership;
- representative authority;
- contract enforceability;
- whether a worker should return to work;
- whether management acted correctly.

## 33. Encounter contract — Mine Ventilation Stop-Work

Narrative premise:
Several mine workers pause entry into one gallery after repeated observations of unusual air, Pokémon behavior and equipment readings. A separate wild-Pokémon disturbance occurs near the safe staging area while technical review is underway.

FULL version:

- workers evacuate/withdraw through protected routes;
- wild Pokémon attempt to leave rather than fight to KO;
- zones may represent validated hazards only if PTU rules exist;
- tactical AI understands `WITHDRAW`, `PROTECT`, `CLEAR_ROUTE`;
- Minecraft displays workers, instruments and changing access state.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if environmental mechanics are used
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

REDUCED version:
Resolve the stop-work, readings and worker evacuation in world state first. Freeze a safe dry staging arena. Only the actual combatants enter AutoPTU. No air-quality status is invented.

## 34. Encounter contract — Ferry Crew Mutual-Aid Transfer

Narrative premise:
A neighboring ferry crew arrives to provide emergency coverage after a storm. During equipment handoff, a separate Pokémon disturbance blocks access to the loading approach.

FULL version:

- technicians and equipment move through a protected lane;
- opponents/wild Pokémon may withdraw;
- route clearing has an explicit objective;
- tactical AI understands `CLEAR_ROUTE`, `PROTECT`, `WITHDRAW`;
- Minecraft replays handoff state correctly.

Dependencies:

- targeting/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING only if storm residue gets tactical mechanics
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

REDUCED version:
Complete the technician/equipment handoff outside battle. Freeze the approach after all noncombatants move to safety. AutoPTU resolves only the static confrontation.

## 35. Encounter contract — Workshop Association Archive Firebreak

Narrative premise:
A craft association’s archive and shared tool library are threatened during a broader incident. Members prioritize records, unique tools and evacuation differently.

FULL version:

- multiple protected-object objectives;
- noncombatant evacuation;
- interactables;
- possible hazard zones only when rules exist;
- objective-aware AI;
- Minecraft semantic playback.

Dependencies:

- targeting/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING for escorts/route denial
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL where invoked
- terrain/weather/hazards/zones/reactions: BLOCKING if fire/smoke receives tactical mechanics
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT_OBJECT`, `EVACUATE`, `REACH_EXIT`
- adapter/playback: BLOCKING

REDUCED version:
Resolve evacuation and custody priorities before battle. Move archive/tool assets outside the grid or mark them as noninteractive world-state objects. Run a static battle in an already-cleared workshop section.

## 36. Engine non-inference boundary

Do not infer from current Java progress:

- worker morale;
- crowd behavior;
- collective-action mechanics;
- escort AI;
- protected corridors;
- workplace hazards;
- mine-air effects;
- strike/stop-work effects;
- social Features;
- negotiation mechanics;
- guild crafting bonuses;
- worker initiative bonuses;
- Pokémon labor behavior.

## 37. Canon questions

Before promotion, decide only what the setting needs:

- Do worker-created associations exist in Ouros?
- Which regions use craft guilds, professional societies, safety committees or mutual-aid networks?
- Which organizations have formal authority, if any?
- Can players found associations?
- Can associations own/rent meeting halls or shared tools?
- Can they enter agreements as institutions?
- Who can represent an association in civic consultation?
- How are internal positions recorded?
- Are work stoppages recognized as a social institution or merely recorded events?
- How does Pokémon participation in work intersect with agency and representation?
- Which records are private?

## 38. Promotion checklist

Before a worker-association concept becomes canon:

1. Confirm the relevant workplace/profession exists.
2. Confirm the association exists or is player-founded through an explicit event.
3. Define scope without importing unsupported labor law.
4. Define membership/representation separately.
5. Preserve dissent and privacy.
6. Route negotiations through Agreements.
7. Route civic decisions through Governance.
8. Route sanctions/reviews through Institutional Review.
9. Validate any PTU mechanics against authoritative sources.
10. Add FULL/REDUCED encounter contracts when combat intersects the story.
11. Keep Pokémon agency explicit.
12. Preserve history when leadership, membership or procedures change.
