# Mourning, memorial and legacy stewardship layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01
Research basis: `research/2026-09-01-mourning-memorial-legacy-stewardship-scan-180.md`

## Purpose

Define how Ouros can represent verified permanent loss, private remembrance, public memorials, legacy objects, custodial handoffs and long-term reinterpretation without confusing battle state, grief, public history, institutional succession or supernatural claims.

This layer does not create a second public-memory, archive, relationship, care, inheritance, succession, quest, calendar or communications system. It supplies a continuity contract that those existing systems can reference.

## Existing ownership remains

- battle HP, Fainted, Injuries, statuses and legal combat results: AutoPTU/PTU authority;
- care, treatment and recovery: care/recovery layer;
- actor knowledge and claims: local-knowledge/claim layer;
- publications and corrections: communications layer;
- historical/public interpretation: public-memory layer;
- object provenance and collections: archive/custody layers;
- role vacancy, acting cover and succession: institutional-role layer;
- site condition and physical markers: site aftermath layer;
- Minecraft/Cobblemon entities, blocks, sounds and particles: presentation only.

This layer owns the relationship among a verified loss event, remembrance practices, memorial records and legacy references.

## Permanent authority separations

`FAINTED != DECEASED`

`HP_ZERO != DECEASED`

`ENTITY_DESPAWNED != DECEASED`

`MISSING != DECEASED`

`MEMORIALIZED != HISTORICALLY_CORRECT_IN_EVERY_DETAIL`

`PUBLIC_MEMORIAL != PRIVATE_GRIEF_STATE`

`LEGACY_OBJECT != AUTOMATIC_PROPERTY_TRANSFER`

`COMPANION_POKEMON != INHERITABLE_ITEM`

`GHOST_TYPE_PRESENT != SPECIFIC_DECEASED_SPIRIT_PRESENT`

`REMEMBRANCE_ACT_COMPLETED != GRIEF_RESOLVED`

## Entry gate: verified loss event

No death-dependent state may open from battle presentation or inference alone.

Suggested reference object:

```yaml
verified_loss_event:
  loss_event_id: null
  subject_id: null
  subject_type: TRAINER | POKEMON | OTHER_ACTOR
  loss_type: DEATH | PERMANENT_DEPARTURE | PRESUMED_LOST | OTHER_AUTHORED
  authority_source_refs: []
  effective_at: null
  verification_status: VERIFIED | DISPUTED | PRESUMED | REVOKED
  privacy_scope: null
  supersedes_loss_event_id: null
```

Only `VERIFIED` death should enable consequences that require confirmed death. `PRESUMED_LOST` may support missing-person procedures or provisional remembrance but must not silently become death.

The exact authority that can set `DEATH` is deliberately undefined until PTU/Caelo/Ouros policy is canonized.

## Memorial subject

A memorial subject is a person, Pokémon, group, incident or service period that a community or individual chooses to remember.

```yaml
memorial_subject:
  memorial_subject_id: null
  subject_refs: []
  basis_event_refs: []
  public_status: NONE | PROPOSED | APPROVED | RETIRED
  private_remembrance_refs: []
  approved_memorial_record_ids: []
  disputed_claim_ids: []
```

A memorial subject need not be deceased. Retirement, closure of a service, a historic rescue or decommissioned institution can also be commemorated. This keeps memorial gameplay from becoming synonymous with death content.

## Private remembrance

Private remembrance records only authored acts and access decisions.

Possible fields:

```yaml
remembrance_act:
  remembrance_act_id: null
  actor_id: null
  memorial_subject_id: null
  act_type: VISIT | LEAVE_OBJECT | WRITE_NOTE | REVIEW_RECORD | MAINTAIN_MARKER | WALK_ROUTE | OTHER
  location_id: null
  object_refs: []
  occurred_at: null
  visibility_scope: PRIVATE
  authored_meaning_ref: null
```

Do not infer:

- grief intensity;
- forgiveness;
- guilt;
- closure;
- loyalty change;
- romantic/familial relationship;
- supernatural contact.

Those require authored relationship/emotion state elsewhere.

## Public memorial record

A public memorial should be versioned because later evidence can change wording or interpretation.

```yaml
memorial_record:
  memorial_record_id: null
  memorial_subject_id: null
  site_id: null
  custodian_actor_or_institution_id: null
  status: DRAFT | APPROVED | INSTALLED | REVISED | REMOVED | RELOCATED
  text_version_id: null
  source_record_refs: []
  claim_refs: []
  object_refs: []
  approved_at: null
  supersedes_record_id: null
```

The memorial text is a publication. It should participate in communications/public-memory correction logic.

## Memorial text provenance

Suggested version object:

```yaml
commemorative_text_version:
  text_version_id: null
  transcription_source_refs: []
  factual_claim_ids: []
  interpretive_claim_ids: []
  omitted_private_fields: []
  author_actor_ids: []
  reviewer_actor_ids: []
  approval_authority_ref: null
  published_at: null
```

A later correction can append context without erasing the historical existence of an earlier inscription.

## Legacy objects

A legacy object is an existing canonical object whose social meaning changes after retirement, transfer, death or institutional transition.

```yaml
legacy_object_ref:
  object_id: null
  prior_custody_ref: null
  current_custody_ref: null
  provenance_refs: []
  mechanical_item_ref: null
  memorial_subject_id: null
  disposition: RETURNED | ARCHIVED | DISPLAYED | RETAINED_IN_USE | TRANSFER_PENDING | DECOMMISSIONED | OTHER
  public_visibility: null
```

Important:

- a mechanical held item remains under item rules;
- a sentimental object does not become mechanically special because it matters socially;
- archive display does not erase ownership/custody history;
- a keepsake may remain private and never enter public collections.

## Companion Pokémon continuity

If a companion loses its Trainer, the next state must be authored separately from property transfer.

Suggested reference:

```yaml
companion_continuity:
  pokemon_id: null
  former_trainer_id: null
  trigger_event_ref: null
  immediate_care_ref: null
  custody_status: UNRESOLVED
  preferred_social_refs: []
  institutional_refs: []
  legal_ownership_refs: []
  capture_status_ref: null
  next_review_at: null
```

Potential authored outcomes require Caelo/PTU validation and may include continued independent residence, family/social-group care, institutional boarding, another willing caretaker, or another canon-specific arrangement.

No outcome follows automatically from a will, family relationship or player proximity unless canon explicitly defines that rule.

## Institutional loss and vacancy

Verified permanent loss can notify the institutional-role layer that a holder is unavailable.

Allowed handoff:

`VERIFIED_LOSS_EVENT`
`-> ROLE_HOLDER_UNAVAILABLE_SIGNAL`
`-> INSTITUTIONAL ROLE LAYER`
`-> ACTING COVER / VACANCY / SUCCESSION PROCESS`

Disallowed:

`MEMORIAL_CREATED -> SUCCESSOR_APPOINTED`

`PLAYER_COMPLETES_FUNERAL_QUEST -> PLAYER_GAINS_OFFICE`

`NPC_ENTITY_DESPAWNS -> ROLE_VACANT`

## Memorial sites

A memorial site is a canonical location or subsite with a custodial relationship.

Possible dimensions:

- public access;
- restricted/private areas;
- maintenance state;
- visitor capacity;
- archive linkage;
- quiet-hour/service schedule;
- relocation status;
- physical marker set;
- environmental/ecological observations;
- active event schedule.

Site aftermath owns material condition. Calendar owns recurring access/events. Memorial layer only references the meaning/custody of markers and practices.

## Relocation and redevelopment

Memorial relocation is a provenance-sensitive site transition.

Required references should include:

- old site;
- new site;
- object/remains/record inventory if canon has them;
- authorization;
- chain of custody;
- visitor-facing notice;
- archived prior layout;
- unresolved discrepancies.

A new building or changed district must not silently erase a memorial's records.

## Absence and presumed loss

Ouros should support unresolved disappearance without forcing binary death.

Possible states:

- missing report open;
- contact lost;
- search active;
- search suspended;
- presumed lost under policy;
- returned alive;
- death later verified;
- record disputed.

A community may hold a vigil or provisional remembrance while the official status remains unresolved. That social act cannot promote the missing actor to deceased.

## Public memory integration

Memorials are unusually influential publications because they are physically persistent and often treated as authoritative by visitors.

Therefore:

- factual statements require source refs;
- interpretive statements should remain tagged as interpretation;
- disputed claims may be exposed in archive annotations;
- corrections should be versioned;
- later political or factional attempts to rewrite a memorial should create a governance/public-memory conflict rather than directly editing world truth.

## Supernatural interpretation boundary

If Ghost-types, unusual sounds, apparitions or anomalous behavior occur near a memorial:

1. record the observable phenomenon;
2. identify canonical Pokémon/entities when server evidence permits;
3. create actor claims separately;
4. do not identify a specific deceased subject without explicit world authority;
5. do not grant mechanical spirit communication without a verified PTU/Caelo capability/Feature;
6. do not use Cobblemon spawn species as metaphysical proof.

## Quest grammar

Useful non-mechanical objective verbs:

- LOCATE_RECORD
- VERIFY_NAME
- TRACE_CUSTODY
- RETURN_KEEPAKE
- PREPARE_ARCHIVE_COPY
- COMPARE_INSCRIPTIONS
- VISIT_SITE
- CLEAN_MARKER
- DELIVER_NOTICE
- RECORD_RECOLLECTION
- CHECK_ACCESS
- ASSIST_RELOCATION
- CATALOG_LEGACY_OBJECT
- FIND_NEXT_OF_KIN_OR_AUTHORIZED_CONTACT
- SUPPORT_COMPANION_CARE
- REVIEW_MEMORIAL_TEXT
- CORRECT_PUBLIC_RECORD

Avoid objective verbs such as:

- ACCEPT_DEATH
- FIND_CLOSURE
- FORGIVE
- MOVE_ON
- SPEAK_TO_THE_DEAD

unless a specific authored story and verified supernatural mechanic support them.

## Marea integration seam

Current canon supports several possible custodial intersections without establishing any memorial practice:

- Taro/Pia can preserve or circulate historical records;
- Mara can hold incident/service records without owning private grief;
- Lia/Mina can know transport and arrival histories;
- Teo can maintain ordinary physical markers or fixtures;
- Jo can use approved public history for teaching;
- Nerea/Ema can distinguish observation from interpretation;
- Sela/Jace can preserve competitive records and retired equipment;
- Oren can hold private care information that must not automatically enter memorial text.

None of these roles proves that Marea has a cemetery, funeral office, shrine or religious authority.

## Mechanically rich encounter pattern: Last Light on the Upper Path

Status: DESIGN EXAMPLE / NON-CANON

Narrative premise:

A resident or institution needs to reach an older route marker carrying a legacy record or permitted remembrance token. The journey matters because of continuity with a past field team or service period, not because the player must defeat an enemy to prove respect.

### Intended full version

Possible sequence:

1. memorial/legacy purpose is established before tactical danger;
2. route access is partially restricted by current world conditions;
3. player escorts one or more non-combat actors along a bounded corridor;
4. wild Pokémon or another authored threat can create combat without being framed as evil or sacrilegious;
5. movement safety and line-of-retreat matter;
6. the legacy object must remain in authorized custody;
7. after the incident, the remembrance act can proceed only if the world route is still operationally safe;
8. battle victory never proves a supernatural claim or completes mourning.

Potential capability dependencies if selected content uses them:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement for corridor control, escorts or displacement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected Moves/statuses;
- terrain/weather/hazards/zones/reactions for unstable route cells, weather phases, protected corridors or reaction movement;
- move-specific behavior for every chosen Move;
- abilities for every chosen Ability;
- items for every relevant Item;
- Trainer Features/perks for every selected interrupt/modifier;
- AI legal-action infrastructure;
- AI tactical policy if opponents/allies must choose positioning tactically;
- Minecraft/Cobblemon/Craftics adapter/playback support for faithful visible execution.

### Reduced version

Preserve the premise while removing unsupported tactical dependencies:

- the memorial purpose, custody and route restriction remain world state outside BattleSpec;
- no civilian or legacy object becomes a combatant;
- player performs authored observation/access tasks at safe checkpoints;
- if combat occurs, it happens separately on a stable clearing;
- matchup is selected only after exact Moves, Abilities, Items and Trainer Features are audited;
- no forced movement, hazards, weather phases, escort reactions or tactical-objective AI are required;
- battle result may emit only a narrow event such as `IMMEDIATE_ROUTE_THREAT_WITHDREW`;
- memorial access, object custody, historical meaning and route reopening remain non-battle decisions.

## Current engine-readiness boundary

Read-only AutoPTU-Java head checked in this pass: `6afb2d95c1de0fcc5b8e6a6c72b361370b3eeb80`.

The newest slice binds forced-movement content through a canonical registry seam and adds registry-backed ownership tests. This is useful composition evidence inside forced displacement. It does not demonstrate the complete movement family.

Conservative classification:

VERIFIED for currently covered contracts:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING when a concept requires the complete family:

- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

AutoPTU visible head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; recent work is Career/presentation and does not promote tactical categories.

## Validation targets

Future validation should reject:

- memorial records referencing missing subjects/sites;
- death-dependent memorial state sourced only from Fainted/HP/entity despawn;
- legacy object transfer without custody provenance;
- companion Pokémon reassignment without explicit authority;
- memorial text that exposes private care records without authorized publication;
- a Ghost-type spawn mapped directly to a deceased identity;
- succession changes authored by memorial completion;
- relocation without old/new site provenance;
- circular memorial text supersession;
- public memorial installation with no approving authority once such authority is canonized.

## Canon boundary

This architecture can be implemented without canonizing any death, funeral rite, cemetery, afterlife model, religion, memorial date or legacy-transfer custom in Ouros. All such content requires explicit later approval and Caelo/source cross-check.