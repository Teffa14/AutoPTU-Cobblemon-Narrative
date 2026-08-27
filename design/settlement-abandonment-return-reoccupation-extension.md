# Ouros Settlement Abandonment, Return & Reoccupation Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

Pass: 84

## Purpose

Ouros already models settlements, households, crises, maintenance, public works, ecology, public memory and local content. This extension preserves settlement-scale continuity when normal occupancy declines or stops and when people later return, partially return, reuse the place or choose a different future for it.

The core design goal is to keep one place alive in world state across change.

A settlement that loses most residents should not become a blank ruin object. A settlement that receives new residents should not instantly revert to its old snapshot. Human absence also does not imply ecological emptiness.

## 1. Boundary with existing systems

This extension coordinates state. It does not take authority away from adjacent systems.

Use `observation-settlement-time-layer.md` for settlement capability bands and resident/service causality.

Use `crisis-rescue-recovery-layer.md` for active emergency phases, evacuation, shelters, immediate response and recovery projects.

Use `residential-life-household-relocation-layer.md` for decisions by individual households, temporary displacement and move events.

Use `facility-maintenance-repair-inspection-extension.md` for technical condition, work orders, inspection and facility reopening.

Use `civic-governance-public-works-layer.md` for collective land-use, infrastructure and public decisions.

Use `conservation-protected-areas-stewardship-layer.md` for ecological management or access policy.

Use `public-memory-event-legacy-layer.md` for public interpretation of decline, evacuation, rebuilding or return.

Use `travel-transport-expedition-layer.md` for route and transport availability.

Use `local-sidequest-ecology-location-reuse-extension.md` for foregrounding optional local content.

Use this extension when the central question is: who or what currently occupies and uses the settlement, which parts are active, and how does that state change across abandonment and return?

## 2. Settlement continuity record

```yaml
settlement_occupancy_continuity:
  settlement_id: null
  current_phase: NORMAL_OCCUPANCY
  public_status_labels: []
  active_zone_ids: []
  inactive_zone_ids: []
  inaccessible_zone_ids: []
  permanent_household_refs: []
  temporary_occupant_refs: []
  caretaker_refs: []
  institutional_presence_refs: []
  wild_use_refs: []
  service_state_refs: []
  physical_condition_refs: []
  route_refs: []
  stewardship_refs: []
  historical_phase_ids: []
  current_return_program_ids: []
  unresolved_questions: []
  canon_refs: []
```

`settlement_id` remains stable unless canon explicitly establishes that the place ceased to exist as a geographic identity.

## 3. Occupancy phases

Candidate phases are descriptive world-state categories, not legal classifications.

```text
NORMAL_OCCUPANCY
DECLINING_OCCUPANCY
PARTIAL_OCCUPANCY
EVACUATING
EVACUATED
LOW_OCCUPANCY
NO_KNOWN_PERMANENT_HOUSEHOLDS
TEMPORARY_OPERATIONAL_USE
SURVEY_AND_STABILIZATION
PROVISIONAL_RETURN
PARTIAL_REOCCUPATION
STABLE_NEW_USE
```

A settlement does not need to move through these in order.

Examples:

- gradual economic decline may move NORMAL -> DECLINING -> LOW_OCCUPANCY;
- a crisis may move NORMAL -> EVACUATING -> EVACUATED;
- a field team may create TEMPORARY_OPERATIONAL_USE before any household returns;
- a former residential settlement can eventually reach STABLE_NEW_USE as a research, conservation or mixed-use place.

## 4. Public label versus occupancy truth

```yaml
settlement_status_claim:
  claim_id: null
  settlement_id: null
  label: abandoned
  claimant_or_source_id: null
  issued_at: null
  scope: public
  evidence_refs: []
  still_current: unknown
```

Common labels such as `abandoned`, `closed`, `evacuated`, `ruined`, `ghost town` or `rebuilt` are claims/summaries.

They do not automatically establish:

- zero residents;
- zero visitors;
- zero services;
- zero wild Pokémon;
- zero institutional activity;
- physical destruction;
- legal access;
- ownership;
- safety;
- permission to salvage;
- permission to reoccupy.

Minecraft signage may display a public label. The sign does not become authoritative settlement truth.

## 5. Occupancy categories

```yaml
settlement_occupancy_group:
  occupancy_group_id: null
  settlement_id: null
  group_type: null
  actor_refs: []
  household_refs: []
  pokemon_refs: []
  zone_refs: []
  start_event_id: null
  expected_end: null
  authority_or_invitation_ref: null
  known_purpose: null
  public_visibility: unknown
```

Possible authored `group_type` values:

- PERMANENT_HOUSEHOLDS
- CARETAKERS
- COMMUTING_STAFF
- TEMPORARY_WORK_CREW
- RESEARCH_FIELD_TEAM
- CRISIS_RESPONSE_TEAM
- TEMPORARY_LODGERS
- RETURNING_HOUSEHOLDS
- NEW_HOUSEHOLDS
- VISITORS
- OTHER_AUTHORED_USE

Wild Pokémon use belongs to ecology/agency records and is referenced separately. It should not be represented as human-style occupancy.

## 6. Remnant resident rule

A settlement can remain meaningful with one household or one caretaker.

```yaml
remnant_presence:
  settlement_id: null
  actor_or_household_refs: []
  current_residence_refs: []
  service_role_refs: []
  local_knowledge_refs: []
  dependency_refs: []
  isolation_or_access_constraints: []
  voluntary_status_claims: []
```

Do not treat remnant residents as exposition machines or mandatory stewards. They retain ordinary actor agency and privacy.

## 7. Zone-level state

Whole-settlement flags are too coarse for return play.

```yaml
settlement_zone_state:
  zone_id: null
  settlement_id: null
  occupancy_state: EMPTY_OR_UNKNOWN
  access_state: UNKNOWN
  physical_condition_ref: null
  active_service_refs: []
  household_refs: []
  institutional_use_refs: []
  wild_use_refs: []
  active_project_refs: []
  notice_refs: []
  last_survey_event_id: null
```

One street may be occupied while another remains closed. A clinic can operate while nearby residences remain empty. A route can reopen before the destination has normal services.

## 8. Settlement-use history

```yaml
settlement_use_phase:
  phase_id: null
  settlement_id: null
  phase_type: null
  began_at: null
  ended_at: null
  trigger_event_refs: []
  occupancy_summary_refs: []
  active_institution_refs: []
  service_summary_refs: []
  ecology_summary_refs: []
  physical_change_refs: []
  public_memory_refs: []
```

Previous phases stay queryable.

This supports statements such as:

- the old school served as a field clinic during displacement;
- a former market became a roost while the district was empty;
- an institution operated from a temporary site for three seasons;
- the first returning households used only the eastern road;
- a building reopened under a different function.

## 9. Decline without crisis

```yaml
settlement_decline_state:
  settlement_id: null
  observed_population_change_refs: []
  service_loss_refs: []
  route_change_refs: []
  institution_change_refs: []
  housing_vacancy_refs: []
  economic_or_social_claim_refs: []
  confirmed_causes: []
  unresolved_causes: []
  current_phase: DECLINING_OCCUPANCY
```

Do not invent a single cause because the settlement is quiet.

Possible actual causes must originate from existing world state, for example:

- service closure;
- route bypass;
- institution relocation;
- repeated infrastructure failure;
- changing employment;
- ecological pressure;
- household decisions;
- long-term crisis aftermath;
- deliberate policy or redevelopment where canon establishes it.

## 10. Evacuation handoff

Crisis owns the evacuation itself. This extension receives the resulting occupancy change.

```yaml
evacuation_occupancy_handoff:
  crisis_id: null
  settlement_id: null
  evacuation_event_ids: []
  households_departed: []
  actors_remaining: []
  institutions_relocated: []
  services_continuing_in_place: []
  services_continuing_elsewhere: []
  closed_zone_refs: []
  uncertain_occupancy_refs: []
  effective_at: null
```

If people are unaccounted for, preserve uncertainty. `Evacuated` should not silently assert that every actor left.

## 11. Temporary operational use

An empty or low-occupancy settlement can acquire a temporary function.

```yaml
temporary_settlement_use:
  use_id: null
  settlement_id: null
  operator_refs: []
  purpose: null
  active_zone_refs: []
  start_event_id: null
  end_condition_refs: []
  installed_asset_refs: []
  maintenance_refs: []
  access_policy_refs: []
  household_status_unchanged: true
  ownership_status_unchanged: true
  closure_or_handoff_event_id: null
```

Possible purposes:

- field base;
- survey camp;
- recovery staging;
- temporary service location;
- storage/staging;
- conservation monitoring;
- event or expedition support.

Operational use never proves ownership or permanent settlement rights.

## 12. Institutional displacement and continuity

Public Memory already owns institution identity. This extension adds the location handoff.

```yaml
displaced_institution_operation:
  institution_id: null
  former_home_location_id: null
  current_operating_location_ids: []
  continuity_state: LIMITED
  displacement_event_id: null
  service_state_refs: []
  staff_relocation_refs: []
  archived_asset_refs: []
  return_proposal_refs: []
  temporary_site_history_refs: []
```

Candidate continuity states:

- SUSPENDED
- LIMITED
- OPERATING_TEMPORARILY
- OPERATING_LONG_TERM_ELSEWHERE
- RETURN_PREPARATION
- PARTIALLY_RETURNED
- RETURNED
- RELOCATED_PERMANENTLY

A temporary site can become historically important in its own right.

## 13. Return readiness packet

No universal settlement-level readiness score.

```yaml
settlement_return_readiness:
  readiness_id: null
  settlement_id: null
  reviewed_zone_ids: []
  access_findings: []
  housing_findings: []
  service_findings: []
  maintenance_findings: []
  care_access_findings: []
  transport_findings: []
  communications_findings: []
  environmental_findings: []
  stewardship_findings: []
  unresolved_hazards: []
  unknowns: []
  reviewed_by_refs: []
  reviewed_at: null
  outcome: FURTHER_REVIEW
```

Possible outcomes:

- NOT_READY
- LIMITED_ACCESS_ONLY
- PROVISIONAL_RETURN_POSSIBLE
- ZONE_SPECIFIC_RETURN_POSSIBLE
- BROADER_RETURN_POSSIBLE
- FURTHER_REVIEW

This packet coordinates evidence. It does not create technical, medical or civic authority.

## 14. Household return remains individual

```yaml
household_return_candidate:
  household_id: null
  settlement_id: null
  former_residence_ref: null
  candidate_residence_refs: []
  return_interest_claim_refs: []
  constraint_refs: []
  dependency_refs: []
  selected_option_ref: null
  relocation_case_ref: null
```

Rules:

- a settlement reopening does not force former residents to return;
- a former resident may choose another home;
- a new household can move in without replacing a specific former household;
- helping rebuild does not create residence;
- returning to visit does not create occupancy;
- a household can return before every service is restored if its own constraints allow it.

Residential/Relocation owns the actual move event.

## 15. New-arrival rule

Reoccupation can include new residents.

The generator should not search the world for NPCs solely to turn them into service unlocks.

A plausible new arrival requires:

- an actor with an independent motive;
- a plausible information path to the opportunity;
- a residence option;
- relevant household constraints;
- a relocation decision owned by the actor/Residential state;
- a work/service transition only when existing Staffing/Storefront/Institution state supports it.

## 16. Ecological succession during low human use

```yaml
abandonment_ecology_overlap:
  overlap_id: null
  settlement_id: null
  zone_ids: []
  observation_event_ids: []
  individual_pokemon_refs: []
  collective_refs: []
  habitat_state_refs: []
  recurring_use_claims: []
  human_absence_dependency_claims: []
  disturbance_change_refs: []
  stewardship_review_refs: []
```

Rules:

- one sighting does not prove established habitat use;
- species identity does not prove territorial claim;
- repeated use may justify more observation;
- human return does not automatically displace wild Pokémon;
- wild use does not automatically create a protected-area designation;
- capture/battle legality remains governed elsewhere.

## 17. Return creates a new ecology interaction

Human return can change:

- noise;
- lighting;
- traffic;
- waste;
- water use;
- vegetation management;
- route pressure;
- food availability;
- building access;
- nesting/resting opportunities.

These effects should be recorded only when supported by concrete world-state relationships. They are not generic environmental penalties.

## 18. Stable new use

A settlement does not have to be restored to its historical purpose.

```yaml
settlement_new_use_state:
  settlement_id: null
  former_use_refs: []
  current_use_refs: []
  permanent_household_refs: []
  active_institution_refs: []
  stewardship_refs: []
  retained_ruin_zone_refs: []
  converted_zone_refs: []
  public_memory_refs: []
  adopted_at: null
```

Possible outcomes may include:

- mixed residential/research use;
- smaller settlement footprint;
- active center with retained ruin district;
- service node without large resident population;
- memorial/heritage use with caretakers;
- conservation/research use;
- full residential return;
- long-term low occupancy.

No outcome is inherently the successful one.

## 19. Reopening is not restoration completion

A route, building or service can reopen before every project completes.

Use explicit handoffs:

```yaml
settlement_reopening_event:
  event_id: null
  settlement_id: null
  zone_refs: []
  service_refs: []
  reopening_scope: LIMITED
  evidence_refs: []
  remaining_restrictions: []
  followup_project_refs: []
  notice_update_refs: []
```

Minecraft can render OPEN/LIMITED/CLOSED differences. The visual state does not decide readiness.

## 20. Settlement return chronicle

Meaningful transitions should write history:

- last known normal occupancy phase;
- evacuation or decline milestones;
- service relocations;
- remnant presence;
- temporary operational uses;
- major surveys;
- first provisional return;
- first reopened service;
- new ecological observations;
- contested return decisions;
- stable new-use adoption.

Do not chronicle every routine arrival or repair.

## 21. Local content generation

```yaml
return_hook_candidate:
  settlement_id: null
  source_state_refs: []
  unresolved_constraint_refs: []
  relevant_actor_refs: []
  candidate_activity_types: []
  location_reuse_priority: high
  mechanics_review_required: false
  completion_handoff_owner: null
```

Good sources:

- contradictory occupancy records;
- a service reopening before household return;
- ecology observed in a former public space;
- a temporary institution that may or may not move back;
- a caretaker request;
- an access survey;
- a former resident visit;
- a building whose new use conflicts with its historical one;
- a return plan dependent on one unresolved infrastructure fact.

Reject filler whose only purpose is `raise settlement restoration percentage`.

## 22. Minecraft/Cobblemon representation

The persistent place should change visibly without replacing safe Cobblemon/Minecraft systems.

Preferred SAFE_REUSE or ADAPTER_REQUIRED surfaces include:

- existing block palettes and structure variants;
- vegetation and environmental props;
- doors, barriers and signs;
- lighting state;
- containers and furniture presentation;
- Pokémon overworld entities;
- models, forms, poses, animations and cries;
- pathing/schedule presentation;
- particles and ambient sound;
- entity tracking and client synchronization;
- UI for zone status, notices or surveys;
- persistence hooks for stable Ouros IDs;
- block geometry/collision as observed input to an explicit battlefield adapter.

The adapter renders Ouros-owned occupancy/use state. Cobblemon does not decide that a location is inhabited, safe, reopened or ecologically claimed.

## 23. Binding battle authority boundary

Required direction:

`Ouros settlement/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden authority:

- nearby Cobblemon entities choosing themselves as combatants;
- Cobblemon BattleState deciding participants;
- world despawn removing an AutoPTU participant;
- visible ruined terrain creating PTU hazard effects without mapping;
- Minecraft AI deciding tactical withdrawal or territorial objectives;
- a faint/despawn animation deciding the encounter result.

## 24. Encounter contract — Return Survey at Old Main Street

Narrative premise:

A survey team is checking a partially reopened settlement when a Pokémon confrontation makes the current route unsafe. The survey itself remains necessary regardless of battle outcome.

Intended full version:

- surveyors withdraw toward more than one safe exit;
- changing access or unstable sections can affect route choice;
- Intercept/forced movement may matter in protecting withdrawal lanes;
- wild opponents may prioritize territory/escape rather than KO;
- environment state may matter tactically when actual PTU rules support it;
- adapter playback must preserve selected combatants versus noncombatant surveyors.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when roster requires it;
- terrain/weather/hazards/zones/reactions — BLOCKING if unstable structures/route hazards become tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

The survey team exits through Ouros world state before battle creation. Unsafe building sections are excluded from the reviewed arena. Ouros explicitly chooses combatants. AutoPTU resolves an ordinary static encounter. Afterward, survey findings remain independent: victory may allow inspection to resume, but it cannot certify structures, reopen houses or establish ecological cause.

## 25. Encounter contract — Reclaimed Courtyard Conflict

Narrative premise:

During the low-occupancy period, recurring wild Pokémon began using a former civic courtyard. Returning residents need to decide how normal use and current ecology can coexist after an encounter interrupts the first reopening attempt.

Intended full version:

- territorial/withdrawal routes matter;
- returning residents remain protected noncombatants;
- dynamic zones may represent areas intentionally left undisturbed only when tactical zone support exists;
- Intercept and forced movement may matter;
- AI should understand escape/territorial priorities;
- battle playback must not transform every visible wild Pokémon into a participant.

Dependencies:

The same permanent categories apply. Complete movement is PARTIAL; environment/reactions, tactical AI and adapter/playback remain BLOCKING.

Reduced version:

Residents leave before combat. The observed wildlife-use record remains world state. Ouros selects only the active opponents. AutoPTU resolves a static legal battle. After the encounter, Conservation/Science/Residential/Public Space decide observation, stewardship, access or redesign actions. Winning does not erase habitat use or grant humans automatic authority over the courtyard.

## 26. Noncombat contract — Occupancy Map Reconciliation

Narrative premise:

A reopening map says seven buildings are occupied, while current household and service records only explain five.

This can run without tactical combat.

Evidence may include:

- residence occupancy history;
- temporary work-team lodging;
- commuting service staff;
- outdated notice boards;
- caretaker records;
- direct observation;
- courier deliveries;
- utility/service use only where those records plausibly exist;
- actor testimony;
- former-address history.

Possible results include duplicate records, temporary occupancy, outdated maps, unknown current use or insufficient evidence. Do not force trespass, crime or unauthorized occupancy as the answer.

## 27. Current engine note for Pass 84

Live AutoPTU-Java evidence has advanced beyond Pass 83:

- `c6bff5893c680dd7aef2995317f7fb6a88fd849d` commits successful Intercept movement authoritatively after geometry/check resolution and keeps reaction movement separate from the ordinary Shift bucket.
- `1649cdba59117221d6eb18080a49765cc8521c3b` composes the melee Intercept follow-up with authoritative Push 1 forced movement and frozen Python ordering.

These are substantial slices for interception/forced movement.

They do not establish the full `complete movement` family because broad reaction timing/conflicts, all knockback/forced-movement sources, full Move/Ability/Item/Feature integration, tactical AI and Minecraft playback remain incomplete.

The permanent category therefore remains PARTIAL in this design.

## 28. Canon questions intentionally left open

- Which Ouros settlements have experienced major decline, evacuation or abandonment?
- What caused each case?
- Which residents stayed and why?
- Which institutions relocated and which remained?
- Who has authority to declare a zone safe, open or closed?
- What records of former occupancy exist?
- What happens to empty residences under local customs or law?
- Which places acquired meaningful wild Pokémon use during low human occupancy?
- What technologies/services are needed before return in each region?
- Do any settlements choose permanent new uses rather than residential recovery?
- What privacy rules apply to return/occupancy information?

No answer is established by this extension.

## 29. Implementation priority

Recommended order:

1. settlement continuity record;
2. zone-level occupancy/use state;
3. crisis evacuation handoff;
4. temporary operational use;
5. institutional displacement location history;
6. return-readiness packet;
7. Residential return candidate links;
8. ecology overlap links;
9. reopening event and notice projection;
10. Chronicle/public-memory callbacks;
11. Minecraft materialization of occupancy/use variants;
12. mechanically rich encounters only after required AutoPTU/adapter evidence exists.
