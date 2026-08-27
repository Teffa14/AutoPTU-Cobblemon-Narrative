# Ouros Fisheries, Aquatic Harvest, Landing & Stewardship Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

This extension fills the operational gap between the existing Maritime, Food, Conservation, Wild Collective, Science, Seasonality, Workplaces, Equipment, Storefront and Found Property systems.

It models persistent fishing/aquatic-harvest activity as world history without defining a second fishing rules engine.

PTU/Caelo/AutoPTU remain authoritative for fishing/capture mechanics when those mechanics matter. Ouros owns the surrounding world facts and handoffs. Minecraft/Cobblemon should provide as much interaction and presentation as safely reusable, while Cobblemon battle-state logic never decides participants or tactical outcomes.

## 1. Authority split

Ouros owns:
- fishing or aquatic-harvest activity identity;
- actor intent and chosen operating location;
- observed effort windows;
- landing-site state;
- ecological observations;
- release/return world-state records;
- provenance and downstream handoffs;
- closure/restriction references created by their actual owning institutions;
- explicit encounter composition.

Existing systems retain authority over:
- Maritime/Travel: vessels, sea lanes and journeys;
- Food: food/resource batches and preparation;
- Conservation: managed-use areas, restrictions and stewardship objectives;
- Science/Wildlife Monitoring: population claims, sampling and individual monitoring;
- Wild Collectives/Ecology: wild population/group state;
- Workplaces: employment, shifts and assignments;
- Shared Equipment/Material Culture: rods, tools and exact equipment instances;
- Found Property: recovered lost gear;
- Storefront/Finance: sale, price and commercial availability;
- Care: welfare/treatment state;
- Case/Authority: evidence or formal disputes.

AutoPTU owns all tactical battle facts.

## 2. Fishery or aquatic-use site

```yaml
fishery_site:
  fishery_site_id: null
  location_ids: []
  maritime_region_id: null
  agricultural_site_ref: null
  operator_or_steward_ids: []
  workplace_ids: []
  landing_site_ids: []
  target_practice_claim_ids: []
  ecological_context_ids: []
  seasonal_context_ids: []
  stewardship_area_ids: []
  current_access_state: UNKNOWN
  current_operational_state: UNKNOWN
  active_activity_ids: []
  observation_ids: []
  unresolved_questions: []
```

`fishery_site` is an operational coordination object. It does not establish ownership of water, fishing rights, quotas, legal authority or species availability.

Candidate operational states:
- OPERATING
- LIMITED
- PAUSED
- WEATHER_HELD
- ROUTE_HELD
- STEWARDSHIP_RESTRICTED
- EQUIPMENT_LIMITED
- CLOSED_BY_OWNER_SYSTEM
- UNKNOWN

## 3. Fishing activity record

```yaml
fishing_activity:
  activity_id: null
  fishery_site_id: null
  actor_ids: []
  vessel_or_position_ref: null
  equipment_instance_ids: []
  bait_or_lure_refs: []
  started_at: null
  ended_at: null
  intended_purpose: null
  intended_target_claims: []
  effort_observation_ids: []
  contact_event_ids: []
  release_event_ids: []
  landing_event_ids: []
  equipment_incident_ids: []
  weather_or_access_refs: []
  rules_resolution_refs: []
  status: PLANNED
```

Candidate purposes:
- FOOD_PRODUCTION
- RESEARCH
- CULTURAL_PRACTICE
- RECREATION
- TOURISM
- TRAINER_CAPTURE_ATTEMPT
- STEWARDSHIP_MONITORING
- OTHER_AUTHORED_PURPOSE

Purpose matters narratively but does not grant mechanical bonuses.

## 4. Effort observation, not hidden population math

```yaml
fishing_effort_observation:
  observation_id: null
  activity_id: null
  observer_ids: []
  time_window: null
  location_ref: null
  method_ref: null
  casts_or_attempts_observed: null
  duration_claim: null
  interruption_refs: []
  result_summary_claims: []
  provenance_ids: []
```

A low result after high effort may justify a research question. It does not directly set population abundance.

The system must preserve alternative explanations such as:
- reduced time on water;
- route changes;
- gear failure;
- weather;
- different target practice;
- deliberate release;
- incomplete observation;
- genuine ecological change.

Science/Ecology decides how much evidence is required for a population conclusion.

## 5. Contact event

```yaml
fishing_contact_event:
  contact_event_id: null
  activity_id: null
  contact_type: null
  pokemon_actor_ref: null
  item_or_material_ref: null
  exact_identity_state: UNKNOWN
  ptu_resolution_ref: null
  encounter_manifest_ref: null
  outcome_state: null
  observation_ids: []
```

Candidate contact types:
- NO_CONTACT
- ITEM_CONTACT
- POKEMON_HOOKED
- POKEMON_REELED
- POKEMON_ESCAPED
- RESEARCH_CONTACT
- OTHER_REVIEWED_CONTACT

The narrative layer cannot create a Pokémon because a contact type says `POKEMON_HOOKED`. The actor must originate from the approved ecology/encounter pipeline and, if tactical resolution occurs, from an explicit Ouros manifest.

## 6. Capture, release and landing stay separate

```yaml
release_event:
  release_event_id: null
  pokemon_actor_ref: null
  source_contact_event_id: null
  release_location_id: null
  release_actor_ids: []
  reason_claim_ids: []
  care_or_stewardship_refs: []
  completed_at: null
```

A release does not infer emotion, ownership, future cooperation or ecological benefit.

Capture is not owned by this extension. Any capture transition must use governing PTU/Caelo/AutoPTU and Pokémon Agency/ownership state.

## 7. Landing site

```yaml
landing_site:
  landing_site_id: null
  location_id: null
  harbor_id: null
  operator_ids: []
  workplace_ids: []
  storage_refs: []
  food_handoff_refs: []
  research_handoff_refs: []
  equipment_return_refs: []
  sanitation_or_quality_refs: []
  notice_ids: []
  current_capacity_state: UNKNOWN
  current_access_state: UNKNOWN
```

The landing site is where water activity becomes persistent downstream state.

Possible handoffs:
- Food batch creation from an approved physical resource;
- scientific sample/observation transfer;
- exact Pokémon actor release/care/capture state;
- equipment inspection/return;
- market/storefront intake;
- traceability record;
- stewardship review;
- case/evidence transfer.

## 8. Landing event

```yaml
landing_event:
  landing_event_id: null
  fishing_activity_id: null
  landing_site_id: null
  arrived_at: null
  actor_ids: []
  vessel_ref: null
  landed_batch_ids: []
  pokemon_state_handoffs: []
  research_record_ids: []
  equipment_return_ids: []
  discrepancy_ids: []
  public_claim_ids: []
```

A landing event records what arrived and what was handed off. It does not decide price, ownership, food quality or ecological sustainability.

## 9. Market/commercial names versus exact identity

```yaml
landing_identity_record:
  record_id: null
  exact_species_or_material_ref: null
  commercial_or_local_name: null
  exact_identity_confidence: null
  source_event_id: null
  identification_evidence_ids: []
  correction_event_ids: []
```

Local names can remain culturally useful even when biologically imprecise. Corrections preserve the earlier label historically.

## 10. Managed-use and stewardship integration

Pass 86 does not create harvest law.

Any restriction must point to a real policy/management source:

```yaml
fishery_access_constraint:
  constraint_id: null
  fishery_site_id: null
  source_policy_or_owner_system_ref: null
  affected_location_ids: []
  affected_activity_types: []
  starts_at: null
  ends_or_review_ref: null
  public_notice_ids: []
  observed_enforcement_state: null
```

Examples may include seasonal buffers, research-only periods or temporary closures only after canon establishes who can issue them.

Ecological concern alone cannot silently create a prohibition.

## 11. Non-target and unexpected contact

```yaml
unexpected_contact_observation:
  observation_id: null
  activity_id: null
  actor_or_species_ref: null
  context: null
  disposition: null
  science_handoff_ref: null
  conservation_handoff_ref: null
  care_handoff_ref: null
```

Unexpected contact can become a useful observation without automatically becoming loot, capture, combat or evidence of population change.

## 12. Equipment continuity

Fishing tools remain exact equipment/material instances where useful.

Potential events:
- line/rod lost;
- bait/lure consumed under governing mechanics;
- equipment damaged;
- tool left aboard a vessel;
- gear recovered later;
- shared kit returned for inspection;
- equipment superseded by another instance.

Found gear must use Found Property/Equipment custody rules. Nearby wild Pokémon never imply ownership of the object.

## 13. Production and food handoff

If canon establishes an aquatic food/resource product, Pass 86 may create a handoff into `food_batch`.

It may record:
- source location;
- activity/event provenance;
- producer/gatherer actors;
- time/season;
- landing location;
- storage handoff.

It may not invent:
- yields;
- quality tiers with mechanical effects;
- spoilage clocks;
- prices;
- nutrition;
- Digestion Buffs;
- species-specific products unsupported by canon/rules.

## 14. Reconciliation instead of instant scarcity conclusions

```yaml
landing_reconciliation:
  reconciliation_id: null
  expected_activity_refs: []
  observed_landing_refs: []
  route_or_weather_refs: []
  equipment_incident_refs: []
  release_refs: []
  missing_information: []
  resulting_claims: []
  science_review_ref: null
```

A settlement can notice that several boats returned light without instantly setting `fish_population=LOW`.

## 15. Cultural practice

Fishing may carry:
- occupational identity;
- seasonal traditions;
- teaching/mentorship;
- community meals;
- local vocabulary;
- visitor/tourism pressure;
- memorial history;
- intergenerational knowledge;
- disagreement over methods.

These belong to the appropriate social/cultural layers. They do not grant PTU bonuses.

## 16. Long-term site memory

A fishery/working waterfront should accumulate:
- route changes;
- equipment practices;
- observed species/contact history;
- market changes;
- research findings;
- closures/reopenings;
- habitat overlap;
- infrastructure repairs;
- changed landing routines.

Routine activity can compress into periodic summaries until a meaningful choice or anomaly appears.

## 17. Cobblemon integration profile

Current public Cobblemon provides Poké Rods, bobber interaction, bait, enchantment-sensitive fishing selection, item/Pokémon outcomes, audiovisual feedback and cast/reel statistics.

Desired reuse:
- rod/bobber models and held-item presentation;
- casting/reeling animation and audio;
- bubble/particle feedback;
- bait interaction UI where mapping is reviewed;
- interaction/network hooks;
- fishing statistics as observed activity telemetry;
- Pokémon overworld models/forms/poses/cries after an actor exists;
- docks, boats, barrels and other world assets.

Authority classification at design level:
- presentation assets/interactions: SAFE_REUSE candidate;
- cast/reel result hooks: ADAPTER_REQUIRED;
- Cobblemon spawn selection as a canonical Ouros ecology decision: ADAPTER_REQUIRED;
- Cobblemon spawn selection as automatic tactical participant creation: BATTLE_AUTHORITY_FORBIDDEN;
- Cobblemon battle controller/state after fishing: BATTLE_AUTHORITY_FORBIDDEN;
- exact API classes: UNKNOWN_REVIEW_REQUIRED until source inspection.

Required flow:

`Ouros fishery/ecology state -> reviewed fishing intent/rules path -> explicit encounter composition when needed -> AutoPTU BattleSpec/state/result -> adapter -> Cobblemon presentation`

Never:

`Poké Rod spawns nearby entity -> Cobblemon battle state enrolls it -> Ouros accepts tactical result`

## 18. Encounter contract — Working-Waterfront Withdrawal

Narrative premise:
A routine landing is interrupted by a local wild-Pokémon disturbance near the working edge. Crew and market workers need a safe withdrawal while the waterfront remains physically intact.

FULL version intends:
- narrow dock/shore geometry;
- explicit WITHDRAW/CLEAR_ROUTE objective;
- noncombatants moving out through world state or objective entities;
- Intercept where legal;
- Push/Pull/knockback if exact Moves require it;
- water/shore terrain only if authoritative;
- territorial/withdrawal AI rather than mandatory KO behavior;
- semantic playback distinguishing background waterfront actors from combatants.

Dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:
- Ouros pauses landing work first;
- all crew/customers/noncombatants leave tactical space;
- cargo, fishery batches and equipment remain outside the grid;
- only explicitly selected Trainers/Pokémon become combatants;
- static dock/shore blockers define the arena;
- no current, tide, wet-surface penalty or environmental damage exists tactically;
- AutoPTU resolves the battle;
- landing/work/stewardship state resumes afterward.

## 19. Encounter contract — Cove Release Window

Narrative premise:
A monitored or deliberately released wild Pokémon must be returned to a suitable location while another wild group uses the same cove.

FULL version intends:
- explicit protected/release objective;
- multiple access routes;
- territorial or withdrawal AI;
- water movement and environment only when verified;
- Intercept/reactions only through AutoPTU;
- exact actor identity from Ouros/monitoring state.

Same overall capability profile as Working-Waterfront Withdrawal, with particularly strong dependence on AI tactical policy, objective support, complete reaction/movement handling and adapter playback.

REDUCED version:
- the release target remains outside battle state;
- Ouros performs or pauses the release as a separate world action;
- any necessary battle uses explicit selected combatants in a static nearby arena;
- victory cannot count as release completion;
- Conservation/Science/Pokémon Agency decide the subsequent world state.

## 20. Noncombat mystery — Three Boats, Two Landing Records

Three departures are remembered, but only two landing records exist.

Investigation may compare:
- vessel journey history;
- fishing activity windows;
- weather/route state;
- landing-site records;
- equipment handoffs;
- market intake;
- witness claims.

Possible explanations include a combined landing, diversion to another site, incomplete paperwork, one trip returning without a formal landing event or unresolved evidence.

The design must not force theft, illegal fishing or fraud as the answer.

## 21. Anti-false-completion rules

- One empty landing does not prove ecological collapse.
- Several catches do not prove abundance.
- A market label does not establish species identity.
- A captured Pokémon is not automatically food/resource output.
- A hooked Pokémon is not automatically a combatant.
- A nearby Cobblemon entity is not automatically the hooked actor.
- A Cobblemon fishing spawn cannot choose tactical participants.
- Regeneration of a biological resource does not prove extraction is ethical or permitted.
- A stewardship recommendation does not become law without an owning authority.
- A battle victory does not authorize fishing, reopen a cove, complete a release or create a food batch.
- Lure/Luck of the Sea behavior in Cobblemon does not become PTU fishing arithmetic by default.

## 22. Canon questions

Before canon promotion, resolve:
- which Ouros settlements/regions have fishing or aquatic-harvest traditions;
- whether activity is subsistence, commercial, recreational, scientific, tourism-oriented or mixed;
- what resources besides Pokémon, if any, are harvested;
- how captured Pokémon relate to food culture, if at all;
- what welfare norms exist;
- which institutions can restrict access;
- whether quotas/licenses/landing requirements exist anywhere;
- what technologies and vessel scales exist;
- which market names/traditions are established;
- how much fishing activity should be materialized in Minecraft;
- which Cobblemon fishing APIs are safe to reuse directly.

Nothing in this extension answers those questions automatically.
