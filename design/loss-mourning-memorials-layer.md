# Ouros Loss, Mourning & Memorials Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already tracks public memory, family continuity, care/recovery, cases, missing actors, archives, sacred sites, housing, institutions and legacy. This layer adds a safe model for confirmed death, unresolved absence, memorialization, burial/resting places, remembrance practices and the long-term world changes caused by loss.

The system must preserve a strict truth boundary. A battle state, rumor, grave marker, Ghost-type sighting or missing-person report cannot independently establish death.

## 1. Mortality state

```yaml
mortality_state:
  subject_id: null
  state: ALIVE_CONFIRMED
  source_fact_ids: []
  effective_at: null
  confirmed_by_ids: []
  confidence: authoritative
  visibility: restricted
  supersedes_state_id: null
```

Allowed high-level states:
- ALIVE_CONFIRMED
- ACTIVE_STATUS_UNKNOWN
- MISSING
- INCAPACITATED
- RETIRED_FROM_ACTIVE_STORY
- DECEASED_CONFIRMED

Do not store `presumed dead` as mortality truth. Store it as a claim in the information/public-memory layers.

Hard rules:
- Fainted does not mean dead.
- An Injury does not mean dead.
- 0 HP does not mean dead unless the governing PTU/Caelo rule explicitly says so for the resolved state.
- A missing actor remains missing until evidence changes the state.
- A retired PC remains retired unless player-approved canon establishes later events.
- A grave, memorial or obituary can be wrong, symbolic or contested.

## 2. Mortality authority boundary

Death-specific state may be created only by one of these routes:

```yaml
mortality_confirmation:
  confirmation_id: null
  subject_id: null
  route: null
  authoritative_source_refs: []
  mechanics_result_ref: null
  canon_editor_ref: null
  timestamp: null
```

Candidate routes:
- AUTHORED_CANON
- AUTHORITATIVE_MECHANICAL_RESOLUTION
- HUMAN_CANON_REVIEW

Procedural narrative generation cannot create a DECEASED_CONFIRMED state by itself.

Until exact PTU/Caelo death rules are extracted and Java parity exists for any relevant mechanical path, generated combat should not promote a Fainted combatant to deceased.

## 3. Loss event

```yaml
loss_event:
  loss_event_id: null
  event_type: null
  subject_ids: []
  affected_actor_ids: []
  source_event_ids: []
  location_id: null
  timestamp: null
  public_visibility: null
  confirmed_fact_ids: []
  unresolved_questions: []
  downstream_state_ids: []
```

Candidate event types:
- CONFIRMED_DEATH
- DISAPPEARANCE
- LONG_TERM_SEPARATION
- RETIREMENT
- INSTITUTIONAL_CLOSURE
- HABITAT_LOSS
- DESTRUCTION_OF_SIGNIFICANT_PLACE

This broader model allows the world to represent absence without treating every loss as death.

## 4. Mourning and reaction boundary

Mourning is not a universal meter.

The system may record observable actions:

```yaml
remembrance_action:
  action_id: null
  actor_id: null
  subject_ids: []
  action_type: null
  location_id: null
  timestamp: null
  public_visibility: null
  object_ids: []
  source_event_ids: []
```

Candidate action types:
- VISIT
- LEAVE_OFFERING
- MAINTAIN_SITE
- ATTEND_CEREMONY
- CREATE_TRIBUTE
- SHARE_STORY
- REQUEST_PRIVACY
- DECLINE_PARTICIPATION
- ARCHIVE_RECORD
- DONATE_OBJECT
- NAME_PROJECT
- OBSERVE_SILENCE

These actions do not authorize emotional inference.

The generator must not infer grief, guilt, relief, anger, forgiveness, revenge, closure, depression, acceptance or spiritual belief unless authored for that NPC or explicitly supplied by a player for their PC.

## 5. Memorial subject

```yaml
memorial_subject:
  memorial_subject_id: null
  subject_ids: []
  source_loss_event_ids: []
  canonical_fact_ids: []
  public_claim_ids: []
  disputed_claim_ids: []
  privacy_constraints: []
  authorized_by_ids: []
```

A memorial can represent:
- one person;
- one Pokémon;
- a group;
- an institution;
- an expedition;
- a disaster;
- a lost settlement;
- an ecological loss;
- an unresolved disappearance.

A memorial to a missing person must not silently convert the person to deceased.

## 6. Memorial site

```yaml
memorial_site:
  site_id: null
  location_id: null
  subject_ids: []
  site_form: null
  steward_ids: []
  access_policy_ids: []
  marker_ids: []
  offering_area_ids: []
  archival_record_ids: []
  ecological_state_ids: []
  maintenance_state: null
  public_interpretation_ids: []
  ritual_practice_ids: []
  disturbance_history: []
  relocation_history: []
```

Possible forms:
- cemetery;
- memorial garden;
- tower;
- grove;
- wall/plaque;
- roadside marker;
- museum room;
- preserved route section;
- shrine-like site only when canon authors that cultural form;
- informal player-built tribute.

No one form is assumed to be universal across Ouros.

## 7. Burial/resting-place state

If Ouros canon eventually defines burial, cremation, preservation or other practices, record them separately from memorial meaning.

```yaml
resting_place_record:
  record_id: null
  subject_id: null
  location_id: null
  disposition_type: unresolved
  custodian_ids: []
  access_policy_ids: []
  provenance_refs: []
  public_marker_id: null
  privacy_state: null
```

Do not invent bodily remains, ashes or disposition for a deceased actor unless canon explicitly establishes them.

This separation also allows a memorial to exist somewhere other than the physical resting place.

## 8. Memorial record versus historical truth

A marker can contain claims.

```yaml
memorial_marker:
  marker_id: null
  site_id: null
  subject_ids: []
  inscription_record_id: null
  public_claim_ids: []
  omitted_fact_ids: []
  disputed_claim_ids: []
  installed_at: null
  revised_at: null
  steward_ids: []
```

A marker may:
- contain an error;
- use an outdated name/title;
- omit participants;
- reflect one community's interpretation;
- have a later correction;
- remain unchanged even after historians revise the record.

The Public Memory and Archives layers own propagation and correction. This layer owns the memorial object's state.

## 9. Ghost-type ecology boundary

Ghost-type Pokémon remain Pokémon entities.

```yaml
ghost_site_presence:
  site_id: null
  pokemon_population_ids: []
  collective_ids: []
  observation_ids: []
  habitat_factors: []
  folklore_claim_ids: []
  supernatural_event_ids: []
```

Rules:
- a Ghost-type population at a cemetery does not prove that those Pokémon are the buried dead;
- a spirit claim does not create a Ghost Pokémon identity;
- a Ghost Pokémon familiar with a deceased actor does not prove reincarnation;
- unusual behavior becomes an observation first;
- confirmed supernatural identity requires authored canon or validated governing mechanics.

This protects the ecology layer from metaphysical fanon.

## 10. Supernatural event separation

```yaml
postmortem_claim:
  claim_id: null
  claimed_subject_id: null
  phenomenon_event_ids: []
  claimant_ids: []
  evidence_ids: []
  interpretation: null
  status: UNRESOLVED
```

Possible states:
- UNRESOLVED
- CONTESTED
- SUPPORTED_BY_AUTHORED_EVENT
- DISPROVEN
- CANON_CONFIRMED

Dreams, Aura impressions, psychic residue, Ghost behavior and folklore can contribute evidence/claims but cannot by themselves overwrite mortality or identity state unless the governing system explicitly provides that result.

## 11. Survivor Pokémon state

A Pokémon whose Trainer or companion dies remains its own actor.

```yaml
survivor_pokemon_context:
  pokemon_entity_id: null
  source_loss_event_ids: []
  current_custodian_id: null
  current_residence_id: null
  ownership_claim_ids: []
  observed_routine_changes: []
  relationship_fact_ids: []
  future_decision_state: unresolved
```

Do not infer:
- that the Pokémon wants a new Trainer;
- that it wants release;
- that it wants to remain with a family;
- that it is permanently traumatized;
- that it inherits the previous Trainer's goals;
- that ownership transfers automatically.

Any ownership, guardianship, transfer, release or new partnership requires the appropriate canon/rules path.

## 12. Estate and custody boundary

This layer does not define inheritance law.

Potential affected assets can include:
- Pokémon custody;
- Eggs;
- homes;
- workshop equipment;
- research notes;
- club property;
- trophies;
- museum loans;
- vehicles;
- personal items.

The Family, Homes, Material Culture, Archives, Case/Custody and Civic layers decide their own state once Ouros canon defines relevant institutions.

Until then, use `ownership_unresolved` rather than assuming next of kin receives everything.

## 13. Memorial stewardship

```yaml
memorial_stewardship:
  site_id: null
  steward_ids: []
  responsibilities: []
  maintenance_schedule: null
  funding_source_ids: []
  access_principles: []
  ecological_constraints: []
  cultural_constraints: []
  unresolved_issues: []
```

Possible stewardship conflicts:
- preservation versus habitat growth;
- visitor access versus privacy;
- road expansion versus relocation;
- tourism versus quiet use;
- historical correction versus traditional inscription;
- family wishes versus public institution policy;
- archaeology beneath a modern memorial;
- Ghost Pokémon population versus site maintenance.

Do not manufacture a villain. Each position can have coherent reasons.

## 14. Memorial lifecycle

```yaml
memorial_lifecycle:
  site_id: null
  state: PROPOSED
  source_event_ids: []
  consultation_ids: []
  construction_or_design_ids: []
  dedication_event_id: null
  maintenance_history: []
  revisions: []
  relocation_events: []
  closure_or_repurposing_state: null
```

Suggested states:
- PROPOSED
- CONSULTING
- PREPARING
- DEDICATED
- ACTIVE
- WEATHERED
- UNDER_REPAIR
- CONTESTED
- RELOCATING
- ARCHIVED

A memorial can outlive the institution that created it.

## 15. Recurring remembrance events

Use the Public Event system rather than inventing a separate event engine.

A remembrance event may have:
- quiet visitation windows;
- archive access;
- storytelling;
- maintenance work;
- performance or ceremony when regionally authored;
- community meals;
- museum exhibits;
- route closures;
- temporary transport demand;
- research/public-history activities.

Avoid mandatory combat incidents merely to make the event "gameplay."

## 16. Missing-versus-memorialized cases

A community may build a memorial for people/Pokémon whose fate is unresolved.

```yaml
missing_memorial_context:
  case_id: null
  memorial_site_ids: []
  missing_subject_ids: []
  death_claim_ids: []
  unresolved_search_state: null
```

Rules:
- memorialization does not close the case;
- new evidence can reopen public debate without disrespecting prior remembrance;
- a returned missing actor should trigger record correction, not a continuity error;
- the memorial may remain historically meaningful after the person's return.

## 17. Place after loss

A location may change because an actor is absent.

Possible world-state effects:
- empty workstation;
- closed shop hours;
- unused bedroom;
- club role vacancy;
- changed patrol route;
- caretaker vacancy;
- unmaintained trail;
- memorial object;
- archived equipment;
- successor appointment;
- unresolved obligations.

The Workplace, Homes, Clubs and Institution layers should consume these outputs.

The system should preserve absence rather than instantly spawning a replacement NPC.

## 18. Player-created memorials

Minecraft allows players to build meaningful places. These require consent and anti-griefing rules.

```yaml
player_memorial:
  memorial_id: null
  creator_ids: []
  approved_subject_ids: []
  claimed_meaning: null
  location_id: null
  edit_policy: null
  public_visibility: null
  moderation_state: null
```

Hard boundaries:
- one player cannot create canonical death for another PC by building a grave;
- memorializing another active player's PC requires explicit consent if the marker implies death or intimate biography;
- edits/destruction must respect multiplayer permissions;
- player memorial text remains player-authored claim unless canon-approved.

## 19. Tone and procedural frequency

Death-heavy content should be sparse and intentional.

The procedural generator should prefer:
- maintenance;
- historical uncertainty;
- missing-person continuity;
- remembrance;
- stewardship;
- archive corrections;
- ecological coexistence;
- inheritance/custody questions;
- quiet callbacks.

It should not repeatedly kill NPCs to manufacture emotional stakes.

Suggested generator guard:

```yaml
loss_content_policy:
  procedural_confirmed_death: false
  procedural_pc_death: false
  procedural_major_npc_death: false
  authored_loss_callbacks_allowed: true
  missing_cases_allowed: true
  memorial_maintenance_allowed: true
  supernatural_identity_inference: false
```

Values remain design defaults until human canon review.

## 20. PTU / Caelo boundary

This layer does not define death mechanics.

Before any mortality outcome is generated from combat, extract and validate the exact governing rules for:
- Fainted;
- HP thresholds;
- Injuries;
- lethal damage/death if present;
- healing/recovery;
- emergency intervention;
- capture and ownership;
- Trainer death if supported;
- Pokémon death if supported;
- Ghost/Aura/Spirit-related Features;
- any Caelo living-world house rules.

Narrative code may receive `DECEASED_CONFIRMED` as an authoritative output. It may not derive it from lower-level battle state.

## 21. Engine capability dependencies

Most memorial content is world-state content and can advance without tactical support.

Mechanically rich memorial-site encounters can depend on the permanent capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

No memorial-specific battle rules are introduced here.

## 22. Encounter contract A — Memorial Garden Night Disturbance

Narrative premise: repeated nighttime disturbances are damaging a memorial garden. Witnesses blame spirits, but the cause is unresolved and may involve ordinary Pokémon behavior, visitors, weather or a specific authored supernatural event.

FULL version:
- investigate overworld observations before battle;
- if battle occurs, Ghost or other Pokémon use a site with fragile zones and noncombat objectives;
- players may need to drive away, protect, withdraw or reach an exit rather than defeat all opponents;
- any supernatural identity remains separate from species identity.

Dependencies:
- targeting/footprints/range/LoS
- base movement legality
- complete movement/interception if protection or escape objectives are tactical
- core calculations
- action economy/initiative
- full lifecycle
- full damage pipeline
- status lifecycle
- terrain/hazards/zones if fragile beds or fog are mechanical
- move-specific behavior
- abilities
- items
- Trainer Features/perks if used
- AI legal-action infrastructure
- AI tactical policy
- Minecraft adapter/playback

REDUCED version: investigation and fragile memorial areas remain overworld state. If combat is necessary, AutoPTU receives a cleared static arena and a standard legal battle. Site damage is updated only from explicit world actions, not inferred from battle AoE.

## 23. Encounter contract B — Cemetery Perimeter Evacuation

Narrative premise: a hazard or wild collective enters a memorial site's public path while visitors are present.

FULL version could require evacuation/protection, moving civilians, interception and hazardous terrain.

REDUCED version: visitors leave through overworld logic before combat. AutoPTU resolves a static encounter after the path is cleared. This preserves the premise without inventing escort/interception rules.

## 24. Encounter contract C — Old Tower Night Watch

Narrative premise: an old memorial tower has unusual lights/noises and increased Ghost-type activity. The job is to document what is happening, not to prove a haunting.

FULL version may eventually use low-visibility zones, changing terrain, interaction objectives and objective-aware AI.

REDUCED version: observations, switches/doors and light state remain outside the grid. Any tactical battle uses a fixed map and legal combat state. Post-battle conclusions remain evidence/claims, not metaphysical truth.

## 25. Minecraft representation

Potential persistent representation:
- graves/markers as protected block structures;
- offerings as provenance-tracked display objects rather than free loot;
- caretaker NPC schedules;
- archive books or plaques;
- memorial gardens with ecological state;
- weathering/repair variants;
- visitor schedules;
- annual event decoration;
- lighting states;
- private/family sections with access controls;
- old homes/workplaces showing absence;
- player-created tribute zones with permissions.

Avoid thousands of persistent dropped items or NPC mourners.

## 26. Implementation priority

Recommended order:
1. mortality truth boundary;
2. loss event;
3. memorial subject/site;
4. remembrance action with no emotion inference;
5. missing-versus-deceased separation;
6. survivor Pokémon context;
7. memorial stewardship/lifecycle;
8. marker/public-record separation;
9. Ghost ecology/postmortem-claim separation;
10. player memorial consent rules;
11. cross-layer outputs to Family/Homes/Workplaces/Archives/Public Memory;
12. only then evaluate mechanically authoritative mortality integration.

This layer lets Ouros acknowledge loss as part of a persistent world without turning death into procedural shock content, collapsing Ghost Pokémon into souls, or taking authorship away from players.