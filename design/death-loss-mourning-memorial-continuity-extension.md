# Death, Loss, Mourning, and Memorial Continuity Extension

Status: PROPOSED ARCHITECTURE
Canon effect: NONE until individually approved
Pass: 154

## Purpose

Ouros needs durable continuity around death and loss without letting narrative systems create death from ambiguous evidence, tactical defeat, despawn, rumor, grief behavior, or memorialization.

This extension records life-status claims, uncertainty, confirmed death events when an authorized source exists, memorial relationships, grave/marker continuity, mourning participation, survivor consequences, personal-effect associations, and relocation of memorial sites.

It does not define PTU death mechanics, inheritance law, afterlife, resurrection, Ghost metaphysics, funerary religion, ownership succession, or universal grief behavior.

## Authority boundaries

### This extension owns

- persistent `loss_case` identity;
- attributed life-status assertions;
- evidence/provenance attached to those assertions;
- transition from unresolved status to confirmed status only when authorized;
- a canonical `death_confirmation_event` reference when such authority exists;
- memorial-subject relationships;
- memorial marker/site identity and continuity;
- memorial relocation history;
- remembrance and mourning participation records;
- personal-effect memory links;
- survivor-continuity references to other systems;
- disputed memorial identity;
- duplicate, missing, damaged, moved, replaced, or symbolic marker state;
- explicit unresolved and presumed states;
- public/private scope around loss-related records.

### Existing systems keep authority over

AutoPTU:
- tactical HP, damage, Injuries, status, KO/fainting, combat legality, battle participants, and any future verified lethal-combat result.

Care / Recovery / Welfare:
- observable medical state;
- diagnosis;
- treatment;
- stabilization;
- recovery;
- facility records;
- any future approved medical confirmation process.

World Agency:
- survivor goals;
- decisions;
- knowledge;
- attendance choices;
- avoidance;
- statements;
- changes of plan.

Social Bonds:
- relationship facts and observed relationship history.

Public Memory:
- public commemoration;
- monuments as civic/public-memory objects;
- public claims;
- reputation and historical framing.

Ritual / Tradition:
- repeated mourning practices;
- funerary or remembrance traditions;
- local variants;
- observance continuity;
- culturally attributed meanings.

Material Culture / Archives:
- physical object identity;
- construction;
- repair;
- custody;
- archive records;
- material provenance.

Case / Authority / Investigation:
- investigations into disappearance, death, vandalism, theft, identification, disputed records, or custody;
- evidence reasoning;
- institutional decisions.

Organizations / Civic Office:
- office succession;
- organizational replacement;
- mandate continuity.

Travel:
- journeys to memorial sites;
- route conditions;
- arrival/departure;
- transport.

Minecraft/Cobblemon/Craftics:
- rendering and playback after Ouros/AutoPTU authority has decided state.

## Hard invariants

These distinctions are permanent unless an explicit project-approved contract says otherwise:

`KO_OR_FAINTED != DEAD`

`ZERO_HP != DEATH_CONFIRMED`

`SEVERE_INJURY != DEATH_CONFIRMED`

`CARE_CASE_CLOSED != DEATH_CONFIRMED`

`MISSING != DEAD`

`UNREACHABLE != MISSING`

`DESPAWNED != LEFT_WORLD`

`BATTLE_LOST != KILLED`

`BATTLE_WON != OPPONENT_SURVIVED`

`NO_LONGER_SCHEDULED != DEAD`

`RUMORED_DEAD != DEAD`

`MEMORIALIZED != DEAD`

`GRAVE_MARKER_EXISTS != REMAINS_PRESENT`

`MARKER_DESTROYED != REMAINS_DISTURBED`

`GRAVE_RELOCATED != MEMORY_ERASED`

`PERSONAL_EFFECT_HELD != INHERITANCE_PROVEN`

`SURVIVING_POKEMON_PRESENT != OWNERSHIP_TRANSFERRED`

`MOURNING_BEHAVIOR != RELATIONSHIP_LABEL_PROVEN`

`GHOST_TYPE_PRESENT != DECEASED_SPIRIT_PRESENT`

`APPARITION_REPORTED != AFTERLIFE_CONFIRMED`

`SPIRIT_CLAIM != CANONICAL_METAPHYSICS`

`RESURRECTION_CLAIM != RESURRECTION_FACT`

## Core object: `loss_case`

A loss case tracks uncertainty around the continued life/presence of a specific actor or Pokémon.

```yaml
loss_case_id: loss:...
subject_ref: actor:...
opened_at: ...
origin_event_refs:
  - ...
current_status: UNRESOLVED
status_assertion_refs:
  - ...
search_or_case_refs:
  - ...
care_case_refs:
  - ...
death_confirmation_ref: null
public_visibility: PRIVATE
canon_status: PROPOSED
```

Recommended lifecycle values:

- `UNRESOLVED`
- `MISSING_REPORTED`
- `LOCATION_UNKNOWN`
- `PRESUMED_ALIVE_BY_SOURCE`
- `PRESUMED_DEAD_BY_SOURCE`
- `FOUND_ALIVE`
- `DEATH_CONFIRMED`
- `IDENTITY_DISPUTED`
- `CASE_CLOSED_UNRESOLVED`

`PRESUMED_DEAD_BY_SOURCE` always names the source. It is never canonical death by itself.

A loss case may close unresolved. Long-term uncertainty is a valid world state.

## `life_status_assertion`

Every claim about whether someone is alive, dead, missing, or seen recently needs provenance.

```yaml
assertion_id: lifeassert:...
subject_ref: actor:...
assertion_type: REPORTED_ALIVE
asserted_by_ref: actor_or_institution:...
asserted_at: ...
claimed_effective_time: ...
source_refs:
  - evidence:...
confidence: SOURCE_STATED
visibility: ...
status: ACTIVE
supersedes_assertion_refs:
  - ...
```

Candidate types:

- `REPORTED_ALIVE`
- `DIRECTLY_OBSERVED_ALIVE`
- `MISSING_REPORTED`
- `PRESUMED_ALIVE`
- `PRESUMED_DEAD`
- `DEATH_REPORTED`
- `DEATH_CONFIRMED_BY_AUTHORITY`
- `IDENTITY_UNCERTAIN`
- `REPORT_RETRACTED`
- `REPORT_CORRECTED`

A direct observation requires a canonical observation event, not an NPC statement claiming direct observation.

## `death_confirmation_event`

This object may exist only when an approved authority source produces the fact.

```yaml
death_confirmation_id: death:...
subject_ref: actor:...
effective_time: ...
confirmation_time: ...
authority_type: ...
authority_ref: ...
source_event_refs:
  - ...
identity_confidence: CONFIRMED
cause_claim_refs:
  - ...
public_visibility: ...
mechanical_source_refs:
  - ...
canon_status: CANON_APPROVED_FACT
```

Important separation:

- confirmation of death;
- time of death;
- cause of death;
- responsibility;
- intent;
- legal status;
- public knowledge.

One may be known while others remain disputed.

Example:

A body is authoritatively identified and death is confirmed. Cause remains UNKNOWN. Public rumor blames a faction. The Chronicle stores all three states separately.

## Cause-of-death claims

Use the existing claim/evidence architecture.

Candidate states:

- `UNKNOWN`
- `PROPOSED`
- `SUPPORTED`
- `CONTESTED`
- `CONFIRMED_BY_AUTHORITY`
- `REVISED`
- `DISPROVEN`

Narrative cannot transform a battle log into a cause statement beyond what the battle contract actually reports.

If a combatant becomes KO/fainted and a later authorized world event confirms death from unrelated circumstances, both events remain in history.

## Identity confirmation

Death confirmation and identity confirmation must be separable.

```yaml
identity_determination:
  determination_id: identitydet:...
  subject_claim_ref: ...
  candidate_actor_refs:
    - ...
  evidence_refs:
    - ...
  result: CONFIRMED | EXCLUDED | UNRESOLVED | DISPUTED
  authority_ref: ...
```

This supports:

- missing persons;
- damaged or old records;
- duplicate names;
- historical grave registers;
- relocated memorials;
- unidentified remains if canon ever uses them;
- mistaken memorial inscriptions.

No visual model match in Minecraft can establish identity by itself.

## Memorial subject relationship

A memorial can commemorate:

- one human;
- one Pokémon;
- several named individuals;
- an expedition;
- a disaster group;
- unknown or unnamed dead;
- a presumed-dead actor whose status remains unresolved;
- an event rather than a person.

```yaml
memorial_subject_link:
  link_id: memorialsubject:...
  memorial_ref: memorial:...
  subject_ref: actor_or_event:...
  relation: COMMEMORATES
  basis_refs:
    - ...
  status: ACTIVE
  certainty: ATTRIBUTED
```

A memorial subject link records what the memorial is intended to commemorate. It does not prove every underlying historical claim.

## Memorial object model

### `memorial_ref`

```yaml
memorial_ref: memorial:...
memorial_type: MARKER
location_ref: place:...
material_object_refs:
  - object:...
subject_link_refs:
  - memorialsubject:...
created_at: ...
commissioned_by_refs:
  - ...
maintainer_refs:
  - ...
access_policy_ref: ...
current_condition: INTACT
public_visibility: PUBLIC
```

Candidate memorial types:

- `GRAVE_MARKER`
- `BURIAL_SITE`
- `CENOTAPH_OR_SYMBOLIC_MARKER`
- `MEMORIAL_WALL`
- `PLAQUE`
- `TREE_OR_GARDEN`
- `STATUE`
- `SHRINE_LIKE_MEMORIAL`
- `ARCHIVE_ENTRY`
- `DIGITAL_OR_MEDIA_MEMORIAL`
- `NAMED_ROOM`
- `NAMED_ROUTE_FEATURE`
- `PERSONAL_MEMORIAL`
- `COLLECTIVE_MEMORIAL`

Names are descriptive until canon defines institutions and traditions.

## Remains and disposition boundary

Pass 154 does not define a general remains system or legal funerary process.

When future canon requires physical remains, use explicit references with narrow scope:

```yaml
remains_ref: remains:...
identity_status: ...
custody_ref: ...
location_ref: ...
disposition_status: ...
source_refs:
  - ...
```

No operation in this extension may infer:

- ownership of remains;
- next-of-kin;
- legal burial rights;
- cremation rules;
- religious obligation;
- inheritance;
- resurrection availability.

Those require separate canon decisions.

## `memorial_relocation_event`

Inspired by persistent memorial relocation patterns in Pokémon locations, without importing a specific setting.

```yaml
relocation_id: memorialmove:...
memorial_ref: memorial:...
from_location_ref: place:...
to_location_ref: place:...
requested_by_refs:
  - ...
approved_by_ref: ...
physical_move_event_refs:
  - ...
record_migration_refs:
  - ...
access_change_refs:
  - ...
objection_or_support_claim_refs:
  - ...
completion_status: COMPLETE
```

Relocation invariants:

`OLD_SITE_VACATED != HISTORICAL_ASSOCIATION_REMOVED`

`NEW_MARKER_INSTALLED != ALL_RECORDS_MIGRATED`

`RELOCATION_APPROVED != RELOCATION_COMPLETE`

`RELOCATION_COMPLETE != COMMUNITY_ACCEPTANCE_UNANIMOUS`

`MARKER_MOVED != REMAINS_MOVED`

The last distinction is mandatory unless the project explicitly models physical remains.

## Replacement and repair

Memorial material can change while commemorative identity persists.

```yaml
memorial_material_event:
  event_type: REPAIRED | REBUILT | REPLACED | VANDALIZED | WEATHER_DAMAGED | REMOVED | RECOVERED
  memorial_ref: ...
  material_object_refs_before: []
  material_object_refs_after: []
  cause_claim_refs: []
  performed_by_refs: []
  timestamp: ...
```

A rebuilt marker may be modern while the commemorative practice is old.

## Mourning participation

### `mourning_episode`

Records observable participation, not an emotion score.

```yaml
mourning_episode_id: mourning:...
subject_or_event_ref: ...
participant_ref: actor:...
time: ...
location_ref: ...
activity_refs:
  - ...
tradition_observance_ref: null
public_or_private: PRIVATE
statement_refs:
  - ...
world_fact_refs:
  - ...
```

Possible activities:

- visit;
- silence;
- flower placement;
- food/drink offering;
- marker cleaning;
- bell ringing;
- story sharing;
- archival donation;
- participation in a procession;
- absence from a usual event;
- private attendance;
- community service dedicated to the deceased;
- Pokémon care;
- maintenance work.

The system stores what happened. It does not calculate grief intensity.

## Survivor continuity

### `survivor_continuity_link`

Connects a confirmed loss to systems whose current state may need reevaluation.

```yaml
survivor_link_id: survivor:...
death_or_loss_ref: ...
affected_ref: actor_or_system_object:...
relationship_basis_ref: ...
reevaluation_type: ...
created_at: ...
resolved_by_refs:
  - ...
```

Candidate reevaluation types:

- `CARE_DEPENDENCY_REVIEW`
- `POKEMON_CUSTODY_REVIEW`
- `WORKPLACE_STAFFING_REVIEW`
- `EXPEDITION_ROSTER_REVIEW`
- `ORGANIZATION_ROLE_REVIEW`
- `CIVIC_OFFICE_SUCCESSION_REVIEW`
- `HOUSING_ACCESS_REVIEW`
- `ITEM_CUSTODY_REVIEW`
- `TRANSPORT_SERVICE_REVIEW`
- `MENTORSHIP_CONTINUITY_REVIEW`
- `PUBLIC_EVENT_PARTICIPATION_REVIEW`

A reevaluation request creates no outcome by itself.

Example:

A ferry operator dies. Transport Service receives a staffing/operation reevaluation. The ferry does not automatically close forever; another qualified operator may exist.

## Surviving Pokémon

A Trainer's death requires special caution.

For every surviving Pokémon linked to the Trainer, preserve separately:

- persistent Pokémon identity;
- current physical location;
- current mechanical health;
- custody;
- ownership claim if any;
- Poké Ball/item custody;
- actor relationships;
- current goals/behavior through World Agency;
- care requirements;
- public knowledge.

Forbidden automatic transitions:

`TRAINER_DEAD -> POKEMON_OWNED_BY_RELATIVE`

`TRAINER_DEAD -> POKEMON_OWNED_BY_PLAYER`

`TRAINER_DEAD -> POKEMON_RELEASED`

`TRAINER_DEAD -> POKEMON_WILD`

`TRAINER_DEAD -> POKEMON_INHERITS_ITEMS`

`TRAINER_DEAD -> POKEMON_GRIEVING_STATUS_EFFECT`

Any of those may become authored canon later through explicit rules/events.

## Personal effects and memory

A personal effect can retain a memory relationship while custody changes.

```yaml
personal_effect_memory_link:
  link_id: memoryitem:...
object_ref: object:...
associated_actor_ref: actor:...
association_basis: USED_BY | GIFTED_BY | CARRIED_BY | CREATED_BY | COMMEMORATIVE_OF
source_refs:
  - ...
public_visibility: ...
```

This link never establishes legal ownership.

It enables stories such as:

- returning a tool to a workshop;
- donating a map to an archive;
- placing a favorite food at a memorial;
- repairing an old field notebook;
- finding two objects attributed to the same person;
- discovering that a famous item was never actually theirs.

## Public memorialization while status is unresolved

Supported state:

`MEMORIALIZED_WHILE_STATUS_UNRESOLVED`

Use cases:

- a lost expedition;
- a missing ship;
- presumed-dead disaster victims;
- a historic figure whose death record is uncertain;
- conflicting survivor accounts.

The memorial records social response. If the subject later returns alive, the memorial becomes a historical object with a recontextualization event rather than disappearing.

Possible subsequent events:

- inscription corrected;
- purpose changed to commemorate the event;
- memorial retained as a record of the presumed loss;
- subject publicly responds;
- institution issues correction;
- no change because the memorial already commemorated all affected participants.

## Disputed memorials

Memorial identity and wording can be contested.

Store separately:

- physical marker text;
- current institutional description;
- community claims;
- family/group claims;
- historical evidence;
- vandalism/damage facts;
- proposed changes;
- approved changes;
- actual completed changes.

A dispute does not grant the generator permission to decide who deserves commemoration.

## Death record and public record separation

Suggested visibility levels:

- `PRIVATE_CASE`
- `LIMITED_INSTITUTIONAL`
- `FAMILY_OR_ASSOCIATE_SHARED`
- `PUBLIC_CONFIRMED`
- `PUBLIC_DISPUTED`
- `PUBLIC_PRESUMED`

A canon death can remain non-public.

A public death claim can remain canonically unconfirmed.

## Timeline handling

A loss may have several dates:

- last confirmed alive;
- disappearance noticed;
- missing report filed;
- presumed-dead statement issued;
- actual death effective time;
- death discovered;
- identity confirmed;
- public announcement;
- memorial created;
- funeral/observance held;
- marker installed;
- records corrected;
- memorial relocated.

Never compress these into one `death_date` when evidence distinguishes them.

## Chronicle integration

Example event chain:

```yaml
- event: LAST_CONFIRMED_ALIVE
  actor: actor:marin
  time: day:102

- event: MISSING_REPORTED
  loss_case: loss:marin
  time: day:104

- event: PUBLIC_PRESUMED_DEAD_STATEMENT
  source: guild:survey
  time: day:130

- event: MEMORIAL_CREATED
  memorial: memorial:ridge-team
  time: day:160

- event: FOUND_ALIVE
  actor: actor:marin
  time: day:197
```

No retroactive deletion occurs. The memorial and presumed-dead period remain historical facts.

## Minecraft/Cobblemon presentation boundary

Minecraft/Cobblemon/Craftics may present:

- grave markers;
- memorial gardens;
- flowers;
- bells;
- photographs or plaques where assets permit;
- NPC visits;
- relocated markers;
- restoration work;
- changed signage;
- crowds at observances;
- empty spaces after relocation;
- surviving Pokémon physically present after Ouros places them.

The adapter may not decide:

- death;
- identity;
- cause;
- responsibility;
- afterlife;
- spirit presence;
- grief state;
- inheritance;
- Pokémon ownership transfer;
- memorial truth;
- combatant roster;
- PTU HP/status;
- whether a ritual works.

Minecraft entity death/despawn events must not automatically become Ouros canonical death unless a dedicated authoritative bridge contract is approved.

## Tactical encounter contracts

### Memorial Relocation Access Corridor

Narrative premise:

A memorial relocation or emergency access operation needs a route cleared while records, visitors, caretakers, and memorial objects remain outside the tactical slice.

Intended rich version:

- multiple route-control goals;
- protect/withdraw behavior;
- potential forced movement;
- Intercept;
- hazards from damaged terrain;
- reactions;
- objective-aware opponents;
- dynamic arrival/withdrawal.

Required capability families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle as selected content requires;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Full version status: BLOCKED.

Reduced version:

- freeze memorial custody and relocation state before initiative;
- keep caretakers, records, remains if any, and memorial objects outside BattleSpec;
- use fixed geometry;
- use explicit combatants;
- allow only individually audited Moves/Abilities/Items/Features;
- AutoPTU may return `IMMEDIATE_MEMORIAL_ACCESS_ROUTE_CLEAR`;
- Ouros decides afterward whether the relocation operation continues.

Reduced version status: READY at narrative-contract level.

### Cemetery Visitor Withdrawal Perimeter

Narrative premise:

A dangerous event near a memorial site requires visitors to leave before or outside a tactical confrontation.

Rich version blockers:

- escort/withdraw semantics;
- reaction ordering;
- dynamic hazards if present;
- AI tactical policy for delay/block/escape/protect goals;
- adapter playback.

Reduced version:

Visitors are moved to a safe off-BattleSpec world state before initiative when plausibly possible. AutoPTU resolves only the combatants left in the perimeter. Result may be `IMMEDIATE_CEMETERY_PERIMETER_CLEAR`.

Battle victory cannot establish that every visitor survived any unmodeled preceding event.

### Memorial Archive Recovery Chokepoint

Narrative premise:

A disputed or damaged memorial register needs physical access after hostile actors occupy a fixed archive approach.

Rich version blockers:

- semantic object protection/carrying;
- tactical withdrawal/capture policy;
- reactions/zones if used;
- AI tactical policy;
- adapter playback.

Reduced version:

Archive records remain outside BattleSpec. AutoPTU may clear the immediate access route. Investigation/Archives then determines what records exist and what they prove.

`BATTLE_WON != DEATH_RECORD_AUTHENTICATED`

### Survivor Rescue From Memorial-Site Incident

Narrative premise:

A living person or Pokémon is endangered near a memorial location. The dramatic tension must not allow the narrative layer to infer death from battle failure.

Rich version blockers:

- escort/rescue semantics;
- dynamic hazards;
- complete movement;
- reactions;
- lifecycle;
- tactical AI policy;
- adapter playback.

Reduced version:

If a safe pre-battle extraction is possible, Ouros resolves that extraction before BattleSpec and fights only remaining combatants. If extraction cannot be resolved without missing mechanics, the scenario remains blocked rather than inventing rescue rules.

## Engine capability stance for Pass 154

Current conservative map:

VERIFIED:
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

The latest Java head improves server-owned Intercept sequencing but does not promote the complete movement family.

## Canon questions opened by this extension

- Does Ouros permit permanent death for Trainers, Pokémon, both, or only authored exceptional cases?
- Which PTU/Caelo death and Injury rules are approved for Ouros?
- What exact engine event can create `DEATH_CONFIRMED` from tactical state?
- Can medical institutions confirm death, and under what contract?
- How are missing actors handled institutionally across regions?
- Which communities use graves, memorial gardens, towers, plaques, cremation, symbolic markers, archives, or other practices?
- Which practices apply to humans, Pokémon, or both?
- Are any Ghost/spirit/afterlife claims canonically true, and which sources can establish them?
- What happens to a deceased Trainer's Pokémon under local law/custom and Pokémon agency?
- Who can hold or transfer Poké Balls and other personal effects?
- Which memorial records are public or private?
- Can memorial sites be relocated, and who has authority to approve it?
- Which historic losses remain unresolved or disputed?
- Which former companions, rivals, mentors, workers, public figures, or wild Pokémon should have authored memorial continuity?

## Implementation principle

Worldbuilding may proceed immediately with memorials, unresolved losses, survivor continuity, archival disputes, visits, relocation planning, maintenance, and reduced tactical contracts.

Canonical death remains gated behind an explicit authority source. Narrative must never manufacture that authority.