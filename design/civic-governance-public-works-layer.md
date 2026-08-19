# Ouros Civic Governance & Public Works Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models factions, settlement capabilities, crises, cases, media, public memory and infrastructure state. This layer adds the missing decision structure around collective choices: how a settlement or institution proposes a change, who is affected, which body has authored authority to decide, how objections and alternatives are preserved, how implementation is tracked, and how the result changes the world.

This document deliberately does not define Ouros as a democracy, monarchy, League state, corporate city, council federation or any other political model. Governance is data-driven and local until canon establishes more.

## 1. Civic body

A civic body is an institution with an authored mandate to make or coordinate specific collective decisions.

```yaml
civic_body:
  civic_body_id: null
  name_public: null
  settlement_ids: []
  geographic_scope_ids: []
  mandate_tags: []
  member_actor_ids: []
  represented_group_ids: []
  decision_procedures: []
  meeting_location_ids: []
  public_contact_routes: []
  record_archive_id: null
  faction_influence_edges: []
  legitimacy_state: unknown
  current_projects: []
  canon_reference_ids: []
```

Possible mandate tags may eventually include:
- public works;
- settlement services;
- route maintenance;
- emergency coordination;
- conservation coordination;
- market administration;
- festival/event logistics;
- research-site stewardship;
- local safety;
- land-use coordination;
- inter-settlement coordination.

A body receives none of these powers automatically. Canon must establish them.

## 2. Mandate is separate from influence

Formal decision authority, faction leverage, popularity and implementation capacity are different states.

```yaml
civic_influence_view:
  civic_body_id: null
  faction_id: null
  formal_role: none
  economic_leverage: low
  public_support: unknown
  information_access: low
  service_dependency: low
  direct_control: none
```

A transport guild may have strong practical leverage without having formal authority. A council may have formal authority but lack labor or materials. A popular Gym Leader may influence a debate without legally deciding it.

The generator must not convert high faction influence into secret ownership of the government unless canon explicitly says so.

## 3. Civic proposal

Every collective decision begins with a concrete proposal tied to world state.

```yaml
civic_proposal:
  proposal_id: null
  proposer_ids: []
  receiving_body_id: null
  title_public: null
  proposal_type: null
  affected_location_ids: []
  affected_service_ids: []
  affected_actor_group_ids: []
  stated_problem_ids: []
  intended_outputs: []
  required_resources: []
  dependencies: []
  expected_tradeoffs: []
  evidence_refs: []
  alternative_proposal_ids: []
  status: submitted
```

Suggested statuses:
- DRAFT
- SUBMITTED
- UNDER_REVIEW
- NEEDS_EVIDENCE
- OPEN_FOR_COMMENT
- REVISED
- APPROVED
- APPROVED_WITH_CONDITIONS
- DEFERRED
- REJECTED
- WITHDRAWN
- SUPERSEDED
- IMPLEMENTING
- COMPLETED
- FAILED_IMPLEMENTATION

A rejected proposal remains historical state and may become relevant later.

## 4. Problem statement and evidence

A proposal does not become correct because its sponsor says it is necessary.

```yaml
civic_problem_statement:
  statement_id: null
  proposal_id: null
  claim_ids: []
  supporting_evidence_ids: []
  disputed_evidence_ids: []
  affected_service_metrics: []
  uncertainty_notes: []
  public_visibility: public
```

This connects to the Evidence Graph and Media layer.

Examples:
- bridge traffic is increasing;
- a route is unsafe at night;
- a clinic is over capacity;
- a nesting area overlaps planned construction;
- a market lacks transport access;
- a communications relay is unreliable.

These remain claims until evidence supports them.

## 5. Stakeholders and constituencies

A civic decision should identify who is affected without simulating every resident.

```yaml
stakeholder_group:
  stakeholder_group_id: null
  proposal_id: null
  basis: null
  member_actor_ids: []
  represented_population_ref: null
  interests: []
  concerns: []
  dependencies: []
  preferred_outcomes: []
  known_information: []
  spokesperson_ids: []
```

Candidate bases:
- nearby residents;
- transport operators;
- market vendors;
- researchers;
- conservation workers;
- Gym staff;
- medical workers;
- farmers;
- artisans;
- club members;
- affected Pokémon stewardship group;
- neighboring settlement;
- event organizers;
- property or facility operator where canon supports ownership.

Do not infer unanimous opinion inside a group.

## 6. Public hearing / consultation state

A hearing is a structured social event, not an automatic persuasion check.

```yaml
public_consultation:
  consultation_id: null
  proposal_id: null
  host_body_id: null
  participant_ids: []
  testimony_records: []
  evidence_presented: []
  objections: []
  amendments_proposed: []
  unresolved_questions: []
  access_state: public
  outcome: pending
```

Possible outputs:
- new evidence request;
- site inspection;
- revised route;
- mitigation condition;
- phased implementation;
- deferral;
- approval;
- rejection;
- referral to another institution.

A Skill Check may affect clarity, credibility, speed or access when PTU/Caelo supports it, but one roll should not erase legitimate stakeholder interests.

## 7. Decision procedure

Decision procedures are explicit and local.

```yaml
civic_decision_procedure:
  procedure_id: null
  civic_body_id: null
  decision_type: null
  quorum_or_presence_rule: null
  eligible_decider_ids: []
  evidence_requirements: []
  consultation_requirements: []
  conflict_of_interest_rules: []
  decision_method: authored
  tie_or_deadlock_rule: authored
  appeal_or_review_route: null
```

The placeholder `authored` is intentional. The generator must not invent voting rules, elections, veto powers or legal appeals.

## 8. Conflict of interest

Important NPCs can hold multiple roles.

```yaml
conflict_of_interest_record:
  actor_id: null
  proposal_id: null
  role_edges: []
  disclosed: false
  review_required: false
  mitigation_state: none
```

Examples:
- a council member owns a transport business;
- a Gym Leader also runs a local school;
- a researcher helped produce the evidence supporting a conservation restriction;
- a merchant funds a proposed festival;
- a faction provides emergency services to the settlement.

A conflict does not automatically prove corruption. It creates a transparency or procedure question.

## 9. Public-works project

Approved changes become implementation objects rather than instant map edits.

```yaml
public_works_project:
  project_id: null
  proposal_id: null
  sponsor_body_ids: []
  implementation_actor_ids: []
  affected_location_ids: []
  dependency_ids: []
  resource_requirements: []
  material_instance_ids: []
  service_interruptions: []
  construction_or_restoration_phases: []
  inspection_events: []
  environmental_mitigation: []
  public_information_packets: []
  current_phase: planned
  visual_state_refs: []
  completion_outputs: []
  failure_outputs: []
```

Candidate projects:
- road repair;
- bridge repair or replacement;
- clinic expansion;
- market relocation;
- public shelter;
- relay tower;
- ferry dock;
- research outpost;
- irrigation repair;
- community venue;
- habitat crossing;
- trail reroute;
- waste/remediation work;
- restoration of damaged civic space.

Exact materials, construction times and prices are worldbuilding decisions, not PTU mechanics.

## 10. Project dependency graph

Projects should read the actual settlement graph.

Example:

```text
bridge repair
  -> needs route access
  -> needs construction crew
  -> needs material delivery
  -> temporarily disrupts river crossing
  -> affects market traffic
  -> may affect nesting site
  -> may create alternate-path demand
```

The generator should produce tasks only from true dependencies.

A project should not ask for an item, Pokémon capability or service that does not exist in current world state.

## 11. Competing projects

A settlement may have several worthwhile projects and insufficient capacity to execute all of them at once.

```yaml
civic_priority_window:
  window_id: null
  civic_body_id: null
  candidate_project_ids: []
  limiting_resources: []
  limiting_staff: []
  timing_constraints: []
  dependency_conflicts: []
  public_pressure_refs: []
  selected_project_ids: []
  deferred_project_ids: []
```

This creates meaningful choices without requiring a universal tax simulator.

Constraints may be:
- one construction crew;
- one specialist;
- seasonal access;
- limited material supply;
- route closure conflict;
- festival timing;
- ecological window;
- crisis recovery priority.

## 12. Compromise packages

Binary yes/no decisions should not be the default.

```yaml
civic_compromise:
  compromise_id: null
  proposal_ids: []
  retained_outputs: []
  removed_outputs: []
  added_conditions: []
  monitoring_requirements: []
  review_date_or_trigger: null
  stakeholder_support_changes: []
```

Examples:
- reroute the path around a habitat;
- build in phases;
- fund temporary transport before permanent construction;
- run a seasonal pilot;
- preserve an older structure while adding a new service nearby;
- require monitoring after completion.

## 13. Pilot projects and reversible decisions

Some proposals can be tested before permanent implementation.

```yaml
civic_pilot:
  pilot_id: null
  proposal_id: null
  scope_limit: null
  start_trigger: null
  end_trigger: null
  success_observations: []
  failure_observations: []
  monitoring_actor_ids: []
  automatic_outcome: none
```

The final decision still requires an authored procedure. Data from the pilot becomes evidence, not an automatic law machine.

## 14. Public legitimacy and trust

Institutional trust should not be one morality bar.

Potential dimensions:
- procedural_fairness;
- competence;
- transparency;
- responsiveness;
- reliability;
- local_identification.

These should usually be ordinal and actor/group-specific.

A body can be competent but secretive. A popular institution can still make a harmful decision. A disliked decision can still be procedurally fair.

## 15. Civic records and public memory

Every material decision can emit records.

```yaml
civic_record:
  record_id: null
  body_id: null
  proposal_id: null
  record_type: null
  public_summary_claim_ids: []
  full_record_access: restricted
  timestamp: null
  correction_ids: []
  superseded_by_id: null
```

Possible records:
- meeting notice;
- proposal summary;
- consultation transcript summary;
- decision notice;
- project update;
- completion report;
- audit/review;
- correction;
- historical archive entry.

This connects naturally to media and later historical disputes.

## 16. Institutional review without crime

A failed project may create review without creating a criminal case.

Possible findings:
- evidence was incomplete;
- project dependency was wrong;
- weather changed assumptions;
- contractor/faction capacity was insufficient;
- local knowledge was ignored;
- mitigation worked;
- the plan was reasonable but the world changed;
- responsibility remains disputed.

This keeps institutional drama broader than corruption plots.

## 17. Player participation modes

Players can influence civic state in different ways:
- submit a proposal;
- collect field evidence;
- inspect a site;
- deliver materials;
- mediate stakeholders;
- provide testimony;
- expose conflicting evidence;
- support a pilot;
- protect a work site;
- investigate a failure;
- document ecological effects;
- join implementation through a profession or club;
- choose not to participate.

Player involvement does not automatically grant formal office or control.

## 18. Multiplayer knowledge and participation

Different players may see different civic information.

One player may know a route is unsafe. Another may have access to an engineering report. A faction member may know material delivery is delayed. A researcher may know the affected species has moved.

The consultation system can merge submitted evidence without leaking private information automatically.

## 19. Minecraft representation

Preferred visible outputs:
- notice boards;
- meeting spaces;
- temporary survey markers;
- scaffolding;
- road closures;
- alternate paths;
- construction NPCs;
- relocated vendors;
- changed signage;
- completed public spaces;
- changed transport stops;
- restored facilities;
- inspection markers;
- mitigation structures;
- archived plaques or records.

The adapter should render authoritative project state. It must not decide the outcome of a civic process.

## 20. Boundary with existing systems

Use `case-authority-custody-layer.md` when the central problem is an incident, investigation, evidence custody or operational response.

Use this layer when the central problem is a collective choice about future public state.

Use `world-agency-layer.md` for faction action and influence.

Use `observation-settlement-time-layer.md` for settlement capability, infrastructure effects and clocks.

Use `media-communications-information-layer.md` for publication, delivery and public knowledge.

Use `crisis-rescue-recovery-layer.md` for emergency response and recovery phases.

A single arc may touch all of them, but each object keeps its own authority boundary.

## 21. Encounter implementation contracts

Civic content is often non-combat. When a public-works story creates a tactical encounter, the encounter must declare exact engine dependencies.

### Contract A — Riverside Survey Interruption

Narrative premise: a survey crew is checking a proposed crossing while territorial wild Pokémon react to the temporary equipment and foot traffic.

Full version:
- players protect survey markers while avoiding displacement of the wild group;
- some tiles become temporarily unsafe from unstable bank collapse;
- retreat and protection objectives matter more than KO.

Required capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- action economy/initiative;
- full turn/round lifecycle;
- terrain/weather/hazards/zones/reactions;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
- static battlefield with no moving hazard;
- survey markers remain outside the tactical rules;
- standard legal battle determines whether the area can be inspected safely;
- post-battle survey and ecological consequence resolve in overworld state.

Reduced dependency families:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- full stateful damage pipeline;
- status lifecycle where used by legal moves;
- move-specific behavior for selected moves;
- abilities/items only when present;
- AI legal-action infrastructure.

### Contract B — Depot Chokepoint

Narrative premise: construction materials cannot reach a public project because an active conflict or wild-group incident blocks the depot exit.

Full version:
- BREAK_THROUGH or PROTECT-style objective;
- interception and forced-movement interactions can matter around the exit;
- tactical AI understands the corridor objective.

Required capability families:
- targeting/footprints/range/LoS;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
- standard static battle at the depot entrance;
- materials remain a protected overworld asset outside the grid;
- success clears access rather than simulating an escort objective.

### Contract C — Pump House Shutdown

Narrative premise: a damaged public pump must be shut down while a Pokémon encounter is active around the facility.

Full version:
- players must reach and interact with a control point;
- periodic environmental zones or reactions may change safe routes;
- battle and infrastructure objective coexist.

Required capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities/items when involved;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:
- static legal battle first;
- shutdown interaction happens immediately before or after the battle in Minecraft;
- no custom hazard damage or interactable action is fabricated inside AutoPTU.

### Contract D — Public Hearing Security Incident

Narrative premise: a civic hearing is interrupted by a real safety incident, but the meeting itself remains a social event rather than a battle mechanic.

Full version:
- if combat occurs, the objective may include protecting exits or enabling evacuation;
- civilians are not automatically represented as tactical combatants;
- no speech check creates combat modifiers.

Required capability families for a complex version:
- targeting/footprints/range/LoS;
- complete movement including interception/forced movement if used;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions if the incident creates them;
- AI legal-action infrastructure;
- AI tactical policy;
- adapter/playback support.

Reduced version:
- civilians evacuate through scripted overworld state;
- AutoPTU receives only the legal static battle participants and battlefield;
- civic decision state is paused until the incident resolves.

## 22. Current engine dependency interpretation

At the live AutoPTU-Java evidence reviewed for Pass 20:
- targeting/footprints/range/LoS: VERIFIED;
- base movement legality: VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: BLOCKING;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING.

The new delayed-hit scheduling queue strengthens lifecycle state but does not by itself verify delayed move execution or the complete move family.

## 23. Implementation priorities

Recommended order:
1. civic body + mandate schema;
2. proposal state;
3. stakeholder groups;
4. consultation/testimony records;
5. decision procedure registry;
6. public-works project state;
7. project dependency graph;
8. civic priority windows;
9. compromise/pilot objects;
10. Minecraft visible-state mapping;
11. civic records + public-memory integration.

This creates civic depth without requiring a full constitutional simulation or inventing mechanics that belong to PTU, AutoPTU or future Ouros canon.
