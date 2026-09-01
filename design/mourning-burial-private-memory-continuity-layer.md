# Mourning, Burial & Private Memory Continuity Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Date: 2026-09-01
Research basis: `research/2026-09-01-mourning-burial-private-memory-scan-191.md`

## Purpose

Ouros already has public memory, commemoration, archives, care, custody, correspondence and persistent aftermath. This layer covers a narrower and previously missing interval: what happens after a death is authoritatively established and before, during and after any private farewell, funerary practice or later public commemoration.

Its job is to preserve consent, uncertainty, custody and continuity while preventing Minecraft presentation state or narrative convenience from authoring death.

## 1. Death fact must be authoritative

```yaml
death_fact:
  death_id: null
  subject_id: null
  subject_kind: HUMAN|POKEMON|OTHER
  authority_source: null
  occurred_at: null
  location_id: null
  confirmation_state: UNCONFIRMED|CONFIRMED
  cause_claim_ids: []
  public_visibility: PRIVATE
  player_authorship_ref: null
```

Rules:

- Narrative may consume a confirmed death fact.
- Narrative may not create one from a Minecraft entity death event.
- Fainted state is not death.
- Missing or overdue state is not death.
- A rumor is not death.
- A grave marker is not proof unless linked to validated state.
- Retired PCs require explicit human/player authorization before any future death fact is created.

## 2. Notification state

```yaml
loss_notification:
  notification_id: null
  death_id: null
  intended_recipient_ids: []
  sender_or_authority_id: null
  channel_id: null
  issued_at: null
  delivery_state: PENDING|DELIVERED|FAILED|RETURNED
  acknowledged_by: []
  privacy_scope: PRIVATE
```

A death can be confirmed while some relevant actors still do not know.

This enables:

- a companion institution waiting before publication;
- someone away on field work receiving the news later;
- a returned letter whose recipient has already died;
- a public rumor preceding official confirmation;
- a correction if an earlier report was wrong.

## 3. Mourning context

```yaml
mourning_context:
  mourning_id: null
  death_id: null
  actor_id: null
  relationship_evidence_ids: []
  observable_practice_ids: []
  privacy_scope: null
  start_at: null
  last_observed_at: null
  authored_emotion_tags: []
  player_consent_ref: null
```

The system records only authored or observable facts.

It may record:

- repeated visits;
- a kept object;
- a changed schedule;
- participation in a ceremony;
- a stated memory;
- a request for privacy;
- explicit dialogue about grief.

It must not infer internal emotional labels merely because two actors were close.

## 4. Farewell / funerary event

```yaml
farewell_event:
  farewell_id: null
  death_ids: []
  host_ids: []
  invited_ids: []
  location_id: null
  event_form: null
  practice_version_ref: null
  public_access: PRIVATE|INVITED|PUBLIC
  remains_handling_ref: null
  effect_custody_refs: []
  companion_care_refs: []
  completed_at: null
```

`event_form` remains null or locally authored until Caelo/canon establishes actual practice.

Candidate forms may later include burial, memorial gathering, archive deposit, private farewell or other regional practices, but this layer does not choose among them.

## 5. Remains / physical disposition boundary

Where a setting uses physical remains, model custody separately.

```yaml
remains_custody:
  remains_id: null
  death_id: null
  current_custodian_id: null
  current_location_id: null
  custody_basis_ref: null
  transfer_history: []
  disposition_state: UNRESOLVED|TEMPORARY_CUSTODY|FINALIZED
  final_disposition_ref: null
```

No Minecraft container, item or entity is the authority for this record.

If the setting does not preserve physical remains in a given case, this object need not exist.

## 6. Personal effects

```yaml
post_loss_effect:
  effect_record_id: null
  object_instance_id: null
  prior_holder_id: null
  found_at: null
  current_custodian_id: null
  ownership_claim_ids: []
  disposition_authority_id: null
  disposition_state: HELD|RETURNED|TRANSFERRED|ARCHIVED|UNRESOLVED
  provenance_refs: []
```

Rules:

- pickup is not ownership;
- custody is not inheritance;
- an item can remain disputed after a farewell;
- archived objects remain distinct from ordinary stock;
- mechanical PTU Items retain their authoritative mechanics separately.

## 7. Companion Pokémon continuity

```yaml
surviving_companion_case:
  case_id: null
  pokemon_id: null
  deceased_actor_id: null
  current_caretaker_id: null
  current_custody_basis_ref: null
  ownership_claim_ids: []
  observed_preference_evidence_ids: []
  care_requirements_ref: null
  transfer_state: UNRESOLVED|TEMPORARY|FINALIZED
```

Important boundaries:

- a deceased Trainer's Pokémon does not automatically enter the player's roster;
- a surviving Pokémon does not become wild merely because its Trainer died;
- a caretaker is not automatically the owner;
- observed preference is evidence, not a universal legal transfer rule;
- battle participation cannot decide custody by itself.

## 8. Memorial object

```yaml
private_memorial:
  memorial_id: null
  death_ids: []
  creator_ids: []
  location_id: null
  object_instance_ids: []
  visibility: PRIVATE|INVITED|PUBLIC
  claims_displayed: []
  consent_refs: []
  maintenance_owner_id: null
  superseded_by_public_commemoration_id: null
```

A private memorial can coexist with the existing public-memory `commemoration` object.

The distinction is intentional:

- private memorial: personal or household practice;
- public commemoration: community-level interpretation and record.

One does not automatically promote into the other.

## 9. Grave / resting-site record

```yaml
resting_site:
  site_id: null
  death_ids: []
  physical_anchor: null
  access_policy_ref: null
  caretaker_id: null
  marker_ids: []
  relocation_history: []
  public_listing_state: PRIVATE|LIMITED|PUBLIC
  cultural_practice_ref: null
```

A site can move through redevelopment while continuity survives through a relocation record.

A marker can be damaged, replaced or corrected without changing the underlying death fact.

## 10. Privacy and publication

Death information is not automatically public.

Possible fields:

```yaml
post_loss_publication:
  publication_id: null
  death_id: null
  issuer_id: null
  authorized_claim_ids: []
  withheld_claim_ids: []
  publication_channel_id: null
  issued_at: null
  correction_of: null
```

The public-memory layer may consume only published/observable claims, not private mourning state.

## 11. Supernatural claim boundary

```yaml
supernatural_claim:
  claim_id: null
  subject_death_id: null
  claimant_id: null
  phenomenon_observation_ids: []
  interpretation: null
  confidence: null
  canonical_truth_ref: null
```

Rules:

- Ghost-type presence does not prove a deceased person's spirit is present;
- a dream does not prove contact;
- a ritual does not prove efficacy;
- a grave disturbance does not prove haunting;
- a mechanically legal Ghost encounter stays a Pokémon encounter unless stronger evidence exists.

## 12. World-state consequences

Validated loss can produce persistent but non-universal consequences:

- schedule coverage gaps;
- equipment awaiting disposition;
- a companion Pokémon care case;
- an archive deposit;
- a temporary closure or gathering;
- correspondence that arrives after death;
- role succession questions;
- private memorial maintenance;
- public notice decisions;
- disputed factual claims around cause or history.

Do not generate every consequence for every death.

## 13. NPC agency after loss

Surviving NPCs continue living and working.

The world may independently:

- cover a missed shift;
- redistribute routine duties;
- preserve a workspace for a period;
- move personal effects into temporary custody;
- postpone an event;
- continue an institution's work;
- make a memorial decision without player involvement if authority and authored motives support it.

The player need not become executor of every loss.

## 14. Quest grammar

Low-mechanics quest forms:

1. confirm what may be shared before a public notice is issued;
2. return a personal object into correct custody;
3. locate a missing document needed to identify an item's provenance;
4. escort a surviving companion Pokémon to an approved caretaker without implying ownership transfer;
5. update an archive index after a public notice;
6. distinguish a rumor of death from confirmed state;
7. repair or relocate a memorial marker while preserving record history;
8. deliver a message whose intended recipient has died;
9. reconcile two incompatible dates or names on a marker and source record;
10. help an institution cover routine work while a resident attends a private farewell.

## 15. Player-authorship boundary

For player characters and player-authored companion Pokémon:

Narrative may remember validated past actions and explicit current state.

Narrative must not invent:

- death;
- cause of death;
- funeral wishes;
- heirs;
- burial site;
- spiritual beliefs;
- posthumous messages;
- surviving spouse or descendants;
- disposition of Pokémon or possessions.

Those require explicit player input or human canon approval.

## 16. Minecraft/Cobblemon projection rules

Minecraft can project:

- flowers;
- markers;
- benches;
- sealed containers;
- visitors;
- candles/lamps where culturally approved;
- archive displays;
- closed rooms;
- temporary gathering spaces;
- companion Pokémon actors.

Projection events never author death or ownership.

Hard rules:

`minecraft_entity.removed != canonical_death`

`minecraft_entity.killed != canonical_death` unless an authoritative battle/world rule emits a validated death fact

`item_pickup != custody_transfer`

`grave_block_broken != death_fact_deleted`

`ghost_spawn != spirit_identified`

`pokemon_follows_player != ownership_transferred`

## 17. Battle integration boundary

Most post-loss content should remain outside BattleSpec.

When violence or wild pressure occurs near a memorial/resting site, the tactical engine resolves only the combat facts it owns.

The battle handoff may say:

- `IMMEDIATE_WILD_THREAT_WITHDREW`;
- `IMMEDIATE_AREA_CLEAR`;
- `COMBATANT_DEATH_CONFIRMED` only if the engine actually has and emits an authoritative PTU death result.

It may not say:

- grief resolved;
- spirit appeased;
- ownership transferred;
- burial authorized;
- memorial desecration forgiven;
- public narrative accepted;
- companion custody settled.

## 18. Mechanically rich encounter pattern

### Night Visit at the Upper Marker

Premise:

A resident visits a private marker after hours. Wild activity makes the return route unsafe. The memorial itself is not the cause of the encounter.

Full version may involve narrow terrain, protection of a withdrawal corridor, visibility, displacement and reactive wild behavior.

Permanent capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement if corridor protection or displacement matters;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected content;
- terrain/weather/hazards/zones/reactions if darkness, fog, ledges, hazards or reaction windows become tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy for autonomous retreat/protection behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Full form: dependency-gated.

### Reduced form

The visitor and memorial remain world-state actors outside BattleSpec. The RPG layer first moves the visitor to a safe holding position. If a wild Pokémon still blocks the ordinary route, AutoPTU receives a standard audited battle on stable terrain.

Allowed handoff:

`IMMEDIATE_ROUTE_THREAT_WITHDREW`

Narrative then decides whether the visit continues, ends, is postponed or changes future access procedures.

No battle result can identify a spirit, resolve grief or alter the memorial record.

## 19. Implementation priority

P0:

- validated death fact boundary;
- notification state;
- personal-effects custody;
- surviving companion case;
- private memorial versus public commemoration distinction;
- Minecraft projection guardrails.

P1:

- resting-site records;
- relocation history;
- privacy/publication linkage;
- correspondence-after-death integration;
- institutional continuity after a resident's death.

P2:

- region-specific funerary practices only after Caelo/canon review;
- long-term memorial culture;
- supernatural investigations only when separately supported.

## 20. Required unresolved decisions

Before canon or implementation adds an actual Marea funeral or cemetery, human review must determine:

- Caelo funerary practice;
- authority for death confirmation;
- privacy expectations;
- treatment of human remains if applicable;
- Pokémon companion custody rules;
- inheritance/property rules;
- Ghost/spirit cultural doctrine;
- whether any regional institution maintains burial records;
- which practices are civic, religious, household or personal.

This layer intentionally works before those decisions by preserving the state needed to make them safely later.