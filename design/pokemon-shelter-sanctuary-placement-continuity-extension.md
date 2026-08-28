# Pokémon Shelter, Sanctuary & Placement Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Pass: 94

## Purpose

Ouros already has authoritative narrative layers for Pokémon identity/agency, care, conservation, breeding/nurseries, custody and residence. This extension fills a narrower operational gap: the lifecycle of a shelter or sanctuary program from intake through temporary residence and eventual transition.

The extension must support Pokémon who are:

- found with incomplete history;
- temporarily surrendered or transferred into care;
- abandoned according to supported evidence;
- recovering before a later decision;
- awaiting reunification or rehoming;
- living in temporary foster/boarding;
- being prepared for reviewed release or relocation;
- transferred to a specialist institution;
- long-term sanctuary residents.

It must not create a second healing engine, ownership system, breeding service, Loyalty system or capture shop.

## 1. Authority boundaries

Existing systems keep their authority.

Care owns treatment plans, welfare observations, rehabilitation and medical privacy.

Pokémon Agency owns persistent Pokémon identity, custody, residence, association, transfer, rehoming and release events.

Conservation owns habitat suitability, relocation/release context, stewardship and post-release ecological monitoring.

Breeding/Nursery owns Eggs, hatching, juvenile-specific services, lineage and breeding legality.

Case/Custody owns disputed evidence or allegations where a formal case exists.

Homes/Residential systems own human household/residence facts.

AutoPTU owns battle mechanics.

This extension coordinates shelter-program workflow and records transitions between those systems.

## 2. Core separation

Keep these facts distinct:

```text
persistent Pokémon identity
  -> intake event and source claims
  -> current custody/residence
  -> care/readiness evidence
  -> shelter program state
  -> candidate transition(s)
  -> reviewed transition decision
  -> actual transfer/reunification/release/placement event
  -> follow-up history
```

No earlier line automatically proves the later line.

Examples:

- Intake does not prove abandonment.
- Shelter residence does not create institutional ownership.
- Medical discharge does not prove placement readiness.
- Placement readiness does not create a specific suitable household.
- A successful trial does not automatically settle ownership.
- Facility crowding does not authorize release.
- Release does not delete the Pokémon entity.

## 3. Shelter program

A shelter program is an operational program associated with one or more physical facilities.

```yaml
shelter_program:
  shelter_program_id: null
  institution_id: null
  facility_ids: []
  status: PROPOSED
  service_scope: []
  intake_scope: []
  transition_scope: []
  staffing_refs: []
  capacity_snapshot_refs: []
  referral_network_refs: []
  privacy_policy_ref: null
  public_information_ref: null
  incident_refs: []
  review_event_refs: []
  canon_status: proposed
```

Possible service descriptors are worldbuilding labels, not automatic powers:

- EMERGENCY_INTAKE
- TEMPORARY_RESIDENCE
- RECOVERY_RESIDENCE
- REUNIFICATION_SUPPORT
- FOSTER_COORDINATION
- REHOMING_COORDINATION
- RELEASE_PREPARATION
- SANCTUARY_RESIDENCE
- SPECIALIST_TRANSFER
- FOLLOW_UP

A program may provide only some of these.

## 4. Intake event

Intake records what arrived and what was known at that moment.

```yaml
shelter_intake_event:
  intake_event_id: null
  shelter_program_id: null
  pokemon_id: null
  timestamp: null
  arrival_location_id: null
  source_actor_id: null
  source_channel: found|voluntary_handoff|institutional_transfer|emergency_rescue|case_referral|unknown
  source_claim_refs: []
  direct_observation_refs: []
  identifier_refs: []
  belongings_or_item_refs: []
  prior_custody_claim_refs: []
  prior_residence_claim_refs: []
  care_case_ref: null
  immediate_safety_state_ref: null
  identity_confidence: CONFIRMED|PROVISIONAL|UNRESOLVED
  privacy_scope: restricted
```

The record should preserve uncertainty.

If someone says “this Pokémon was abandoned,” store the speaker and evidence. Do not upgrade the statement to canonical abandonment until the project’s evidence rules support it.

## 5. Placement case

A placement case coordinates decisions without duplicating ownership or care.

```yaml
placement_case:
  placement_case_id: null
  pokemon_id: null
  shelter_program_id: null
  intake_event_id: null
  opened_at: null
  case_state: INTAKE
  current_residence_ref: null
  current_custody_ref: null
  care_case_refs: []
  readiness_review_refs: []
  active_transition_tracks: []
  prospective_placement_refs: []
  release_review_ref: null
  reunification_ref: null
  specialist_transfer_ref: null
  follow_up_plan_ref: null
  closed_at: null
  closure_reason: null
  unresolved_questions: []
```

Suggested workflow states:

- INTAKE
- IDENTITY_REVIEW
- STABILIZING
- RESIDENT
- TRANSITION_REVIEW
- MATCHING
- TRIAL_PLACEMENT
- RETURNED_FROM_TRIAL
- TRANSFER_PENDING
- RELEASE_REVIEW
- LONG_TERM_SANCTUARY
- FOLLOW_UP
- CLOSED

These are operational states. They do not assign mechanical condition, Loyalty or emotion.

## 6. Transition tracks

Multiple outcomes can remain open while evidence develops.

```yaml
transition_track:
  track_id: null
  placement_case_id: null
  transition_kind: REUNIFICATION|FOSTER|REHOMING|SPECIALIST_TRANSFER|RELEASE|RELOCATION|LONG_TERM_SANCTUARY|CONTINUED_CARE
  state: PROPOSED|UNDER_REVIEW|READY|PAUSED|REJECTED|COMPLETED|WITHDRAWN
  eligibility_evidence_refs: []
  blocking_issue_refs: []
  decision_actor_refs: []
  decision_authority_refs: []
  resulting_agency_event_ref: null
```

No transition wins merely because it is the first available option.

## 7. Reunification

Reunification concerns a previous legitimate association or custodian.

```yaml
reunification_review:
  reunification_id: null
  pokemon_id: null
  claimant_actor_id: null
  claimed_association_ref: null
  identity_evidence_refs: []
  custody_or_registration_claim_refs: []
  conflicting_claim_refs: []
  observed_reintroduction_refs: []
  care_constraints: []
  decision_state: unresolved
  resulting_transfer_ref: null
```

A photograph, nickname, Poké Ball claim, registration record or recognized behavior can be evidence without independently settling the matter.

If canon later defines legal ownership or registration, the authoritative system must decide which evidence has force.

## 8. Foster and temporary placement

Temporary placement is first-class state.

```yaml
foster_placement:
  foster_id: null
  pokemon_id: null
  placement_case_id: null
  host_actor_or_institution_id: null
  start_event_id: null
  intended_scope: null
  custody_scope_ref: null
  residence_ref: null
  support_plan_refs: []
  observed_interaction_refs: []
  review_dates: []
  end_event_id: null
  outcome: ongoing|returned|extended|transitioned|unknown
```

Foster does not imply ownership. Return from foster is not automatically failure.

## 9. Prospective rehoming

Avoid a hidden compatibility score.

```yaml
prospective_placement:
  prospective_placement_id: null
  pokemon_id: null
  candidate_actor_or_institution_id: null
  authored_requirements: []
  residence_evidence_refs: []
  care_capacity_refs: []
  observed_meeting_refs: []
  practical_constraint_refs: []
  disclosure_packet_ref: null
  review_state: exploratory|reviewing|trial_ready|paused|declined|approved
```

Relevant evidence may include practical facts such as available space, schedule, transport, current residents, required care or known handling constraints when those facts are legitimate and privacy-safe.

Do not infer:

- “perfect bond”;
- permanent affection;
- compatibility from Type/species alone;
- obedience;
- battle effectiveness;
- future Loyalty;
- ownership simply because the player completed shelter quests.

## 10. Long-term sanctuary residence

A sanctuary can be a destination rather than a queue.

```yaml
sanctuary_residence:
  sanctuary_residence_id: null
  pokemon_id: null
  shelter_program_id: null
  residence_location_id: null
  start_event_id: null
  custody_ref: null
  care_support_refs: []
  habitat_or_enclosure_refs: []
  public_contact_policy_ref: null
  work_or_research_permissions: []
  review_refs: []
  end_event_id: null
```

Long-term sanctuary residence does not grant permission for breeding, research, public performance, labor, battle training or public handling.

Each additional activity needs its own governing system and authority.

## 11. Release and relocation handoff

Release uses existing Pokémon Agency and Conservation structures.

The shelter can prepare a transition packet:

```yaml
release_preparation:
  release_preparation_id: null
  pokemon_id: null
  care_readiness_refs: []
  conservation_review_refs: []
  candidate_location_refs: []
  known_collective_refs: []
  transport_requirements: []
  unresolved_risk_refs: []
  decision_state: unresolved
  authoritative_release_event_ref: null
  post_release_monitoring_plan_ref: null
```

The shelter does not decide that “wild is better” by default.

A release is not an overflow mechanism.

## 12. Capacity

Capacity needs more detail than a single occupancy number.

```yaml
shelter_capacity_snapshot:
  snapshot_id: null
  shelter_program_id: null
  timestamp: null
  operating_state: NORMAL|BUSY|STRAINED|PRIORITY_ONLY|OVERFLOW|PARTIAL_SERVICE|CLOSED|EVACUATED
  usable_zone_refs: []
  staffing_state_refs: []
  supply_state_refs: []
  care_dependency_refs: []
  intake_limit_claims: []
  referral_availability_refs: []
  active_case_count_band: null
  notes: null
```

A high case count can create:

- referrals;
- temporary overflow arrangements;
- staff/volunteer calls;
- supply requests;
- delayed nonurgent intake;
- reconfiguration of usable zones;
- transport needs;
- prioritization under an authored policy.

It must not silently trigger euthanasia, release, trade, transfer of player Pokémon or arbitrary placement.

## 13. Facility zones

Facilities can have distinct zones with distinct use.

Examples:

- intake/reception;
- quarantine or assessment area if canon/mechanics define it;
- quiet recovery space;
- exercise yard;
- aquatic area;
- public meeting room;
- staff-only records room;
- temporary foster handoff area;
- long-term sanctuary habitat;
- storage and supply area;
- emergency evacuation staging.

Zone labels do not create mechanical status, disease control or battle effects.

## 14. Identity reconciliation

Shelter intake is a good source of provenance mysteries.

Potential evidence:

- old registration claim;
- prior care record;
- collar/tag/device;
- distinctive markings;
- photograph;
- prior public appearance;
- known scar or physical observation;
- Poké Ball/capture record if mechanically accessible;
- testimony;
- previous sanctuary/facility record;
- wildlife-monitoring identity.

The system can end at `IDENTITY_UNRESOLVED`.

It must not generate missing records or alter a Pokémon's body/state to force an answer.

## 15. Shelter records and privacy

Shelter cases can contain sensitive material.

Keep separate visibility scopes for:

- public availability/status;
- medical/care history;
- alleged mistreatment;
- prior custodian identity;
- legal/case evidence;
- exact current residence for vulnerable individuals;
- prospective caretaker information;
- post-release location.

Public-facing information can use aggregate descriptions without exposing exact resident records.

## 16. Pokémon agency guardrails

Record behavior at the smallest defensible level.

Valid examples:

- entered a quiet room voluntarily;
- accepted food from caretaker A on three occasions;
- moved away when candidate B approached;
- followed candidate C during a supervised walk;
- returned to the facility after release;
- refused to enter a carrier during one handoff;
- slept in the same enclosure area for several nights.

Do not automatically write:

- afraid of all humans;
- trusts caretaker A;
- loves candidate C;
- wants to be adopted;
- never wants a Trainer again;
- has abandonment trauma;
- is cured of trauma;
- forgives a former owner.

Canonical character writing can establish private motives when intentionally authored. Procedural state should stay observational.

## 17. PTU Loyalty and Command boundary

PTU already supplies Loyalty and Command semantics.

Shelter history can create provenance for human review but cannot directly:

- assign Loyalty;
- increase or decrease Loyalty;
- set a Command DC;
- alter obedience;
- add a custom trauma modifier;
- replace an Ability;
- reduce movement;
- grant Intercept;
- create a permanent status;
- award a Feature or Edge.

Any such result must come from the governing PTU/Caelo rules and authoritative runtime.

## 18. Nursery boundary

A shelter resident can be juvenile without making the shelter a nursery.

A shelter does not automatically:

- breed Pokémon;
- incubate Eggs;
- determine parentage;
- manage inheritance;
- provide Hatcher/Breeder benefits;
- run a first-partner program.

If one institution genuinely runs both programs, use distinct service/program records and explicit handoffs.

## 19. Conservation boundary

A sanctuary is not automatically a protected wild habitat.

A release site is not automatically owned or managed by the shelter.

Post-release monitoring can connect to Conservation/Wildlife Monitoring, but lack of signal or sightings must remain uncertainty rather than proof of death, departure or failed release.

## 20. Player consent and anti-collectible rules

A shelter must never become an implicit free-Pokémon shop.

The procedural system may not:

- offer every resident to the player;
- expose full Moves/Ability/stats as a shopping catalogue unless legitimately known;
- award a resident because the player completed enough volunteer tasks;
- silently transfer a player Pokémon into shelter custody;
- permanently place or release a player Pokémon without explicit player action and authoritative mechanics;
- turn a disputed Pokémon into quest reward loot;
- force a permanent party slot decision to clear facility capacity.

Any player-facing acquisition or irreversible transfer requires explicit action plus the governing capture/transfer/registration rules.

## 21. Institutional network

Shelters should connect rather than solve every case locally.

Possible handoffs:

- Care facility for treatment;
- specialist rehabilitation site;
- nursery for Egg/juvenile services if authorized;
- conservation program for release review;
- wildlife monitoring for follow-up;
- transport service for transfer;
- case authority for disputed claims;
- residential/housing systems for prospective human household context;
- long-term sanctuary for residents unsuitable for another current transition.

This creates regional continuity without turning every shelter into a giant all-purpose institution.

## 22. Persistent callbacks

Useful callbacks include:

- a former resident returning with a legitimate caretaker;
- a released individual being re-sighted;
- a foster host later becoming staff or volunteer;
- an old intake identifier resolving months later;
- a transferred resident returning for specialist care;
- a facility changing procedure after a failed handoff;
- a long-term resident becoming familiar to local visitors;
- a former disputed claimant providing new evidence;
- a capacity crisis revealing a weakness in the regional referral network.

The same facility should accumulate these histories rather than reset between quests.

## 23. Minecraft/Cobblemon representation

Strong reuse candidates include:

- Pokémon entities, species forms and cosmetic state;
- poses, idle/walk/swim/fly animation and cries;
- buildings, pens, yards, gates and doors;
- beds/rest spaces and species-appropriate environmental props when canonized;
- signs, books, notice boards and displays;
- particles and sounds;
- UI for public shelter information and authorized staff workflows;
- networking and client synchronization;
- entity tracking and persistence hooks;
- world coordinates and residence anchors.

Adapter-required state includes stable mapping between the Ouros `pokemon_id` and current world entity representation, shelter residence, authorized visibility, case state and controlled spawn/despawn representation.

Battle-authority-forbidden behavior includes selecting combatants from nearby shelter entities, deriving tactical HP/status from Cobblemon state, letting a Minecraft gate/hazard apply PTU damage, or allowing Cobblemon battle controllers to resolve an encounter.

Binding flow:

`Ouros shelter/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

## 24. Encounter contract — Shelter Yard Withdrawal

Narrative premise:

An external disturbance reaches the edge of a shelter's outdoor yard while staff are moving residents into safer indoor or remote spaces. The story objective is to secure a route and prevent the shelter population from becoming accidental combatants.

Full version:

- staff withdraw through multiple routes;
- some selected defenders may use Intercept or forced movement;
- gates or temporary safe zones can matter tactically if authoritative support exists;
- autonomous opponents can prefer route pressure over KO;
- world state records whether evacuation staging remained usable.

Capability dependencies:

```yaml
targeting/footprints/range/LoS: VERIFIED
base movement legality: VERIFIED
complete movement including push/pull/knockback/interception/forced movement: PARTIAL
core calculations: VERIFIED
action economy/initiative: VERIFIED
full turn/round lifecycle: PARTIAL
full stateful damage pipeline: PARTIAL
status lifecycle: PARTIAL
terrain/weather/hazards/zones/reactions: BLOCKING
move-specific behavior: PARTIAL
abilities: PARTIAL
items: PARTIAL
Trainer Features/perks: PARTIAL
AI legal-action infrastructure: VERIFIED
AI tactical policy: BLOCKING
Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Reduced version:

Shelter staff and all resident Pokémon not explicitly selected as combatants complete the move to safety in world state before BattleSpec creation. Gates and facility objects are static, non-targetable scenery. Ouros selects the actual combatants. AutoPTU resolves a fixed legal arena. Afterward Shelter/Care systems decide whether residents can return to the yard.

## 25. Encounter contract — Transfer Handoff Interruption

Narrative premise:

A Pokémon is being transferred between two legitimate care institutions when a separate conflict blocks the route or handoff area. The custody chain must remain clear throughout the interruption.

Full version:

- WITHDRAW/CLEAR_ROUTE or PROTECT-like objective;
- moving transfer party;
- Intercept and reaction timing where appropriate;
- objective-aware AI;
- possible route weather/hazard only with authoritative support;
- adapter playback that keeps the placement subject distinct from tactical actors unless deliberately selected.

Capability profile:

- complete movement: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING if used;
- lifecycle/damage/status/move/ability/item/Feature families: PARTIAL as applicable;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version:

The placement subject and transport staff remain outside the tactical grid. Custody does not change during the interruption. Players resolve a static legal encounter or overworld access problem. The handoff resumes only after the relevant world system records a safe route.

## 26. Encounter contract — Release-Site Boundary Conflict

Narrative premise:

A reviewed release is ready, but another active wild group or human disturbance occupies the immediate access area. The question is whether the release can proceed safely and with correct ecological context.

Full version:

- release target remains a protected noncombatant unless explicitly selected under authoritative rules;
- CLEAR_ROUTE/WITHDRAW objectives;
- territorial or withdrawal-aware AI;
- possible terrain/zones;
- post-battle release requires a separate Conservation/Agency decision.

Dependencies:

- targeting and base movement: VERIFIED;
- complete movement: PARTIAL;
- normal combat calculations/action economy: VERIFIED foundations;
- lifecycle/damage/status/move/abilities/items/Features: PARTIAL;
- terrain/zones/reactions: BLOCKING if dynamic environment matters;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- adapter/playback: BLOCKING.

Reduced version:

The release does not begin until the access area is safe. The Pokémon awaiting release stays outside the battle grid. AutoPTU resolves a separate static encounter using explicit participants. Conservation then re-evaluates whether the original release window/site remains appropriate.

## 27. Noncombat scenario — Three Intake Names, Two Individuals

Three historical intake entries appear to describe three Pokémon. Differences in names, dates and markings initially support that reading.

Players can reconcile:

- photographs;
- old care records;
- tag/device history;
- staff testimony;
- transfer records;
- one later re-sighting.

A plausible resolution may establish that two records refer to one individual after a naming/identifier change. The scenario may also remain unresolved if evidence is incomplete.

No battle or hidden truth meter is required.

## 28. Long-form arc — A Shelter Learns Its Transitions

Stage 1: establish daily intake, residence and referral routines before crisis.

Stage 2: one ambiguous intake exposes a weakness in identity/custody records.

Stage 3: a placement or release pauses for a practical reason rather than dramatic betrayal.

Stage 4: the institution changes one visible procedure: intake photography, handoff records, quiet meeting space, foster review, referral agreement or public information.

Stage 5: a capacity spike tests the revised network. Some cases move, some remain, some are referred.

Stage 6: a former resident returns through a later sighting, visit, care referral or new legitimate association.

The arc changes how the institution works without creating an abstract `shelter_level`.

## 29. Promotion gate

Before shelter/placement content becomes canon or mechanically executable, reviewers must resolve as relevant:

- whether the institution/program exists in Ouros;
- its mandate and service scope;
- custody/ownership/registration law or practice;
- what counts as valid surrender, abandonment or reunification evidence;
- player acquisition/transfer flow;
- foster and long-term sanctuary policy;
- privacy/disclosure rules;
- PTU/Caelo Loyalty and Command interpretation;
- exact care/release mechanics;
- stable Pokémon identity in the Minecraft adapter;
- multiplayer authority for irreversible party/custody changes.

## Design outcome

A shelter should feel like a persistent institution with residents, staff, capacity, history and multiple legitimate outcomes.

The system remembers who arrived, what was known, what care occurred, which transitions were considered, what actually happened and whether the individual appears again later. It never turns care into automatic ownership or fills mechanical gaps with invented battle rules.
