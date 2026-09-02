# Memorial, Death, Remains & Belongings Continuity Layer

Status: PROPOSED SYSTEMS DESIGN
Date: 2026-09-02
Canon effect: NONE

## Purpose

Ouros needs to remember confirmed deaths, memorial practices, surviving belongings and posthumous provenance without letting Narrative invent death, inheritance law, afterlife truth or mechanics.

This layer extends existing Public Memory, Material Provenance, Archive, Residence, Care, Identity and Myth systems. It does not replace them.

## Core boundary

`FAINTED != DEAD`
`MINECRAFT_ENTITY_DEATH != CANONICAL_DEATH`
`MEMORIAL_EXISTS != DEATH_DETAILS_PROVEN`
`BELONGED_TO_DECEASED != CURRENT_OWNER_PROVEN`
`SURVIVING_COMPANION != INHERITED_ASSET`
`GHOST_TYPE_PRESENT != SPIRIT_IDENTITY_PROVEN`
`REMEMBRANCE_RITUAL != SUPERNATURAL_EFFECT`
`PUBLIC_OBITUARY != PRIVATE_FACT_COMPLETE`

## 1. Confirmed death record

A death record may exist only when its source authority is explicit.

```yaml
death_record:
  death_id: null
  subject_actor_id: null
  subject_kind: human_or_pokemon
  confirmation_state: null
  confirmation_source_refs: []
  occurred_at: null
  confirmed_at: null
  location_id: null
  cause_claim_ids: []
  authoritative_mechanical_ref: null
  public_knowledge_state: null
  remains_record_id: null
  memorial_ids: []
  unresolved_questions: []
```

Suggested confirmation states:
- UNCONFIRMED_REPORT
- PRESUMED_BY_AUTHORED_CANON
- CONFIRMED_CANON
- CONFIRMED_MECHANICAL_HANDOFF
- DISPUTED
- ERRONEOUS_REPORT

Only `CONFIRMED_CANON` or an explicitly validated `CONFIRMED_MECHANICAL_HANDOFF` may create final persistent death state.

## 2. Combat death handoff

If AutoPTU eventually exposes authoritative PTU/Caelo death resolution, Narrative receives a narrow event such as:

```yaml
battle_death_handoff:
  battle_id: null
  actor_id: null
  result: CONFIRMED_DEAD
  rule_source_ref: null
  engine_contract_ref: null
  timestamp: null
```

Narrative must not reconstruct death by looking at HP, Injuries, Fainted flags or animation state itself.

Until end-to-end death adjudication is verified, authored battles used by Narrative should avoid requiring a permanent death output unless a human canon decision explicitly supplies it.

## 3. Remains state

```yaml
remains_record:
  remains_id: null
  subject_actor_id: null
  current_location_id: null
  custody_state: null
  custodian_actor_or_institution_id: null
  identification_state: null
  documentation_refs: []
  movement_history: []
  disposition_claim_ids: []
  final_disposition_state: unresolved
```

This schema intentionally does not define burial, cremation, biological handling, legal authority or religious requirements. Those depend on future Caelo/Ouros canon.

## 4. Memorial object

```yaml
memorial_record:
  memorial_id: null
  subject_actor_ids: []
  source_death_ids: []
  location_id: null
  form: null
  created_at: null
  steward_ids: []
  inscription_or_public_claim_refs: []
  recurring_practice_ids: []
  physical_state: null
  relocation_history: []
  access_state: null
  provenance_refs: []
```

Possible forms may include marker, plaque, register entry, dedicated object, maintained planting, room display, named workbench, route marker or ceremony. These are candidate forms, not mandatory regional tradition.

## 5. Posthumous belongings

Use existing material-instance provenance wherever possible.

```yaml
posthumous_belonging_ref:
  item_instance_id: null
  former_holder_actor_id: null
  former_relationship_type: owned_or_custodied_or_used
  death_id: null
  discovered_at: null
  current_custodian_id: null
  disposition_state: null
  authority_ref: null
  claimant_ids: []
  public_display_state: null
  unresolved_questions: []
```

Suggested disposition states:
- INVENTORIED
- HELD_FOR_REVIEW
- RETURNED_TO_PRIOR_OWNER
- TRANSFERRED_BY_AUTHORED_AUTHORITY
- DONATED_BY_AUTHORED_AUTHORITY
- DISPLAYED_WITH_PERMISSION
- UNCLAIMED
- DISPUTED
- LOST

The layer never decides inheritance.

## 6. Surviving Pokémon companion continuity

A persistent Pokémon that survives a human partner's death keeps its own actor identity and history.

```yaml
surviving_companion_state:
  pokemon_actor_id: null
  deceased_partner_actor_id: null
  relationship_evidence_refs: []
  current_care_actor_or_institution_id: null
  current_custody_state: null
  ownership_claim_ids: []
  battle_eligibility_state: separately_governed
  future_partnership_state: unresolved
  welfare_refs: []
```

No automatic transfer to:
- family;
- employer;
- institution;
- player;
- memorial steward;
- finder.

Capture/ownership legality remains governed elsewhere.

## 7. Bereavement and behavior

Narrative may preserve observable behavior and authored statements:
- repeated visits;
- avoidance;
- changed routine;
- care request;
- stored objects;
- unfinished correspondence;
- public remembrance;
- withdrawal from a voluntary event.

It must not infer private emotional labels or mechanical penalties without evidence.

`OBSERVED_BEHAVIOR != DIAGNOSED_GRIEF_STATE`

## 8. Memorial practices

A remembrance practice should use the existing community-tradition architecture when recurrent.

A practice can record:
- participants;
- time window;
- object or place;
- observable acts;
- stated purpose claims;
- variants;
- changes over time.

Participation does not prove belief. Absence does not prove disrespect.

## 9. Ghost and anomalous phenomena boundary

Any Ghost-type encounter near a memorial is first recorded using ecology/encounter state.

Any unusual observation uses the anomalous-phenomenon architecture.

Claims such as “this Ghost is the deceased” require explicit authored world truth or separately governed supernatural mechanics. Species, location and timing do not prove identity continuity.

## 10. Memorial site change

Memorials can be moved, restored, damaged or placed temporarily in storage.

```yaml
memorial_transition:
  transition_id: null
  memorial_id: null
  from_state: null
  to_state: null
  reason_claim_ids: []
  authorizing_refs: []
  documentation_before_refs: []
  documentation_after_refs: []
  temporary_storage_ref: null
```

A relocation changes physical placement. It does not erase historical association with the prior site.

## 11. Residence crossover

After a confirmed death, an assigned room or quarters may enter a transition state. Pass 204 residence records remain authoritative for the address history.

Narrative may record:
- room remains assigned pending review;
- personal items remain present;
- access is limited by authored local procedure;
- items are inventoried with provenance;
- future reassignment occurs later.

It may not assume eviction, estate succession, next-of-kin rights or property seizure.

## 12. Archive crossover

Tideglass can preserve:
- obituary or memorial notice as publication state;
- oral history deposit;
- memorial inscription copy;
- inventory record;
- correspondence deposited by authorized actors;
- conflicting testimony.

Archive possession of a copy does not create ownership of the original object.

## 13. Public-memory crossover

A death can produce public memory while private facts remain restricted or unresolved.

Public claims may include occupation, known service, public achievements and date of remembrance. Cause of death, medical details, ownership disputes and private relationships remain separately governed.

## 14. Quest generation rules

Allowed triggers require existing state:
- a confirmed death has left a documented object without resolved custody;
- a memorial object needs repair or temporary relocation;
- an archive notices an inscription discrepancy;
- a surviving companion requires a care arrangement;
- two public records disagree about a memorial date;
- a route repair intersects an existing memorial marker;
- a Ghost-type sighting is being publicly misreported as proof of a specific spirit identity.

Forbidden triggers:
- kill an NPC because the world needs drama;
- create a corpse as a random investigation hook;
- make a memorial site dangerous by default;
- turn every Ghost encounter into dead-person lore;
- loot burial sites.

## 15. Battle interface

A memorial-related confrontation can occur only when current ecology, route or actor state supports it.

The battle engine owns tactical truth. Narrative owns memorial identity, provenance, access and aftermath meaning.

Possible narrow outputs:
- `IMMEDIATE_SITE_APPROACH_CLEAR`
- `IMMEDIATE_WITHDRAWAL_ROUTE_CLEAR`
- `IMMEDIATE_WILD_ACTOR_WITHDREW`

Battle output cannot determine:
- whether a spirit exists;
- whether a Ghost is a deceased person/Pokémon;
- ownership of remains or belongings;
- memorial authority;
- inheritance;
- grief resolution;
- public interpretation;
- future access policy.

## 16. Implementation persistence

Minecraft/Cobblemon may render memorial props, flowers, markers, Ghost-type actors, NPC visitors and item containers. All persistent identity must come from Narrative IDs.

Breaking or moving a block cannot erase a memorial record. Entity death cannot create a death record. Respawn cannot revive a canonically dead actor.

## 17. Privacy and sensitivity

The generator should treat death-related state as low-frequency and high-specificity.

Prefer:
- established historical figures;
- already-authored deaths;
- community remembrance;
- stewardship;
- object provenance;
- survivor continuity.

Avoid procedural churn around recent deaths unless a human-authored arc establishes that subject.

## 18. First implementation target

`The Label on the Old Field Case`.

Tideglass holds a field case used by a former worker whose death is already established only inside the local historical record created for this slice. The case itself is not loot and its present owner is unresolved. Pia notices two labels from different dates. Taro can document the provenance difference. The slice ends with a corrected catalog record and custody retained unchanged.

Implementation value:
- tests death fact versus object provenance;
- needs no battle;
- needs no afterlife claim;
- needs no inheritance decision;
- needs no new institution;
- keeps custody stable while knowledge improves.

Because no deceased Marea resident is currently canonized, the first production implementation should use either an explicitly approved historical non-resident/non-current worker or defer actor creation until human canon review. This design file itself does not create that person.