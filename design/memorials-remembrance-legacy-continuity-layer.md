# Memorials, Remembrance & Legacy Continuity Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs a durable way to remember people, Pokémon, places, institutions, disasters, retirements and unresolved absences without turning every memory into a sacred site, every loss into a death, or every commemorative object into a quest item.

This layer owns memorial identity, revision history, commemoration state and non-property legacy continuity. It does not own the underlying truth of an incident, private grief, religion, inheritance law, Pokémon ownership or PTU death mechanics.

## Core separation

Keep these states distinct:

```text
underlying event / actor state
        ↓
reports and evidence
        ↓
acknowledged status
        ↓
memorialization decision
        ↓
memorial site / object / publication
        ↓
revisions, maintenance and relocation
        ↓
commemoration events
        ↓
public interpretations
        ↓
legacy handoffs
```

No arrow proves the next state automatically.

A memorial can be wrong about an event. A public belief can be wrong about a memorial. A missing subject can later return. A retired living subject can be commemorated. A memorial can disappear physically while its Chronicle identity survives.

## 1. Acknowledged loss or absence state

Do not reduce every commemorative trigger to death.

```yaml
loss_or_absence_event:
  loss_event_id: null
  subject_refs: []
  event_kind: death|missing|destruction|retirement|disbandment|closure|disaster|extirpation|relocation|unknown
  event_time: null
  location_ref: null
  authoritative_state_ref: null
  evidence_refs: []
  acknowledgement_state: unconfirmed|reported|corroborated|institutionally_acknowledged|canon_confirmed|disputed
  acknowledged_by_refs: []
  uncertainty_notes: null
  chronicle_refs: []
```

`death` is allowed only when an authored/canon fact or authoritative evidence supports it.

Never infer death from:

- Fainted;
- zero or low HP;
- Injury count;
- a lost battle;
- disappearance from loaded chunks;
- missing tracking data;
- release;
- retirement;
- storage;
- absence from a migration count;
- a memorial inscription by itself.

## 2. Memorial subject

A memorial subject can be broader than a deceased individual.

```yaml
memorial_subject:
  memorial_subject_id: null
  subject_kind: actor|pokemon|group|event|place|institution|route|structure|population|object|other
  subject_ref: null
  commemorative_scope: null
  living_or_active_state_at_creation: living|active|deceased|missing|retired|closed|destroyed|unknown|not_applicable
  privacy_constraints: []
  consent_or_authorization_refs: []
```

Examples:

- a retired ferry captain;
- a living service Pokémon ending a long institutional role;
- a missing expedition;
- a locally extirpated Pokémon population;
- a rebuilt district after a flood;
- a bridge crew that completed a rescue;
- a closed rail line;
- a deceased Pokémon when that status is explicitly established.

Commemoration does not imply death.

## 3. Memorial identity

A memorial must have identity independent of its current blocks.

```yaml
memorial:
  memorial_id: null
  title_current: null
  subject_refs: []
  memorial_kind: marker|garden|hall|wall|bridge_name|route|archive|digital|collection|ceremony|other
  created_event_id: null
  current_site_ref: null
  current_object_refs: []
  current_custodian_ref: null
  current_status: proposed|active|relocated|partially_removed|inactive|archived|destroyed|unknown
  revision_refs: []
  commemoration_refs: []
  public_memory_refs: []
  provenance_refs: []
```

Minecraft blocks are a projection of `current_site_ref` and the current memorial revision. They are not the authority for the memorial's existence or history.

## 4. Memorial revision

A memorial can change without being replaced as a historical object.

```yaml
memorial_revision:
  revision_id: null
  memorial_id: null
  effective_from: null
  effective_to: null
  change_kind: inscription|translation|relocation|rebuild|accessibility|name|design|custodian|scope|digital_rebuild|partial_removal|other
  prior_revision_ref: null
  physical_change_refs: []
  text_artifact_refs: []
  reason_recorded: null
  authority_ref: null
  dispute_refs: []
  provenance_refs: []
```

Examples:

- a plaque gains a corrected spelling;
- a route marker moves because the river changed course;
- an inaccessible staircase is replaced by an accessible approach;
- a memorial hall is repurposed and the memorial moves to a smaller garden;
- a missing person's marker changes wording after new evidence;
- a public inscription adds names found in an archive decades later.

Do not silently rewrite old versions.

## 5. Site, object and publication are separate

A memorial can have several physical and digital components.

```yaml
memorial_site:
  site_id: null
  memorial_id: null
  location_id: null
  land_use_ref: null
  access_policy_ref: null
  sacred_site_ref: null
  physical_structure_refs: []
  active_from: null
  active_to: null
```

```yaml
memorial_object:
  memorial_object_id: null
  memorial_id: null
  item_instance_ref: null
  role: marker|bell|book|photograph|banner|replica|relic|inscription|other
  custody_ref: null
  museum_collection_ref: null
  current_location_ref: null
```

```yaml
digital_memorial:
  digital_memorial_id: null
  memorial_id: null
  digital_system_ref: null
  publication_revision_refs: []
  privacy_scope: null
  moderation_scope: null
  archival_copy_refs: []
```

A digital page can remain active after a physical site moves. A museum may borrow a memorial object without becoming owner of the memorial itself.

## 6. Inscription and factual truth

An inscription is a versioned text artifact.

It may be:

- accurate;
- incomplete;
- based on the best evidence available at the time;
- translated from an earlier inscription;
- politically or institutionally contested;
- later corrected;
- culturally important even when some factual details are wrong.

Do not convert inscription text directly into Chronicle truth.

Use Archives, Cases, Public Memory, Identity/Record Linkage, Languages and the relevant event-owning layer to evaluate underlying facts.

## 7. Missing-subject memorials

Ouros should support memorials for unresolved absence.

```yaml
missing_subject_memorial_state:
  memorial_id: null
  missing_case_ref: null
  wording_scope: missing|unaccounted_for|lost_expedition|outcome_unknown|other
  death_asserted: false
  last_review_time: null
  review_trigger_refs: []
```

If a subject later returns:

- preserve the old memorial revision;
- create a new public-memory event;
- update the current wording/status;
- do not treat earlier mourners or caretakers as foolish;
- do not erase years of legitimate uncertainty.

This can produce powerful long-term continuity without retconning.

## 8. Pokémon-specific protections

For Pokémon subjects:

- preserve `pokemon_entity_id` for a living persistent Pokémon;
- memorialization never changes capture/ball state;
- memorialization never transfers custody or ownership;
- a former Trainer association remains historical, not command authority;
- a released Pokémon can be commemorated while remaining wild/independent;
- a retired institutional Pokémon can receive a living-service memorial;
- a missing Pokémon marker cannot declare death without evidence;
- a Pokémon visiting a memorial is an observation, not proof of grief or supernatural perception;
- Ghost-type presence does not prove the subject's spirit is present;
- a memorial to a Pokémon does not create a Ghost-type spawn or Legendary event.

Mechanical Loyalty, Command and party state remain authoritative elsewhere.

## 9. Commemoration events

Recurring remembrance belongs at the intersection of this layer and Festivals/Observances.

```yaml
commemoration_event:
  commemoration_id: null
  memorial_id: null
  event_time: null
  event_kind: anniversary|maintenance_day|service_recognition|quiet_visit|public_ceremony|route_walk|archive_release|other
  organizer_refs: []
  participant_refs: []
  attendance_observation_refs: []
  activity_refs: []
  public_event_ref: null
  observance_ref: null
  outcome_notes: null
```

Attendance does not prove:

- grief;
- belief;
- friendship;
- kinship;
- political support;
- religious affiliation;
- agreement with the inscription;
- forgiveness;
- private emotional state.

PC inner state remains player-authored.

## 10. Maintenance and ordinary years

A memorial should be able to exist for decades without generating constant quests.

Possible maintenance states:

- routine cleaning completed;
- vegetation trimmed;
- digital archive backed up;
- sign repaired;
- accessibility inspection completed;
- no ceremony this year;
- custodian changed;
- inscription unchanged;
- minor weathering observed;
- site quiet and functional.

`nothing dramatic happened` is a valid Chronicle outcome.

## 11. Relocation and adaptive reuse

Memorial relocation should integrate with Architecture, Land Tenure, Public Space and Accessibility.

Possible reasons:

- building redevelopment;
- river migration;
- road or rail project;
- accessibility improvement;
- erosion or wildfire;
- changed land-use agreement;
- museum loan;
- relocation by the commemorating community;
- digital migration to a new platform.

Relocation does not erase the old location's historical role.

## 12. Legacy handoff without inventing inheritance law

Ouros can preserve continuity of responsibility without defining universal inheritance.

```yaml
legacy_handoff:
  handoff_id: null
  source_actor_or_institution_ref: null
  receiving_actor_or_institution_ref: null
  responsibility_kind: caretaker|project|archive|route_knowledge|annual_event|research_series|maintenance_role|other
  scope: []
  proposed_at: null
  accepted_at: null
  authority_refs: []
  property_transfer_refs: []
  pokemon_transfer_refs: []
  status: proposed|accepted|declined|partial|ended|disputed
```

A legacy handoff can transfer responsibility for maintaining a garden or archive without transferring land, money, a Pokémon or legal ownership.

If property, funds or custody are involved, route them to Land Tenure, Finance/Currency, Material Culture, Markets, Agreements, Pokémon Agency or other authoritative layers.

Do not invent wills, probate, heirs, next-of-kin rules, estate taxes or succession law.

## 13. Caretakers and stewardship

Memorial caretaking can be individual, institutional, rotating or informal.

Caretakers may:

- maintain access;
- preserve records;
- report damage;
- organize permitted events;
- coordinate repairs;
- manage public information;
- request conservation work;
- hand responsibility to another actor.

Caretaking does not automatically grant:

- ownership of the land;
- ownership of memorial objects;
- authority over remembered persons' families;
- Hex Maniac Features;
- sacred authority;
- law-enforcement power;
- control over wild Pokémon present at the site.

## 14. Relationship to Sacred Sites

A memorial may also be a Sacred Site only when an authored cultural tradition says so.

Possible combinations:

- civic memorial, not sacred;
- family marker, not sacred;
- sacred shrine with memorial function;
- historic battlefield marker with no religious practice;
- ecological memorial to a locally lost population;
- digital remembrance archive;
- living-service garden for a retired Pokémon.

Sacred status, memorial status and supernatural truth are separate records.

## 15. Relationship to Public Memory

Public Memory owns how groups narrate and reinterpret the past.

This layer owns:

- the persistent memorial identity;
- its sites and objects;
- its inscription/publication revisions;
- maintenance and relocation;
- recurring commemoration records;
- legacy handoffs connected to its stewardship.

Public controversy about a monument can change its interpretation or future revision without rewriting the physical object's past.

## 16. Relationship to Museums and Archives

Museums can accession or borrow memorial objects while the memorial's identity remains outside the collection system.

Archives can preserve:

- original dedication documents;
- earlier inscription versions;
- photographs of prior locations;
- maintenance ledgers;
- names omitted for privacy;
- records that later challenge the memorial narrative.

A museum label or archival finding does not edit the memorial automatically. A decision/revision event is required.

## 17. Relationship to Identity and Languages

A memorial may preserve an alias, historical spelling, title or translated name.

When new record-linkage evidence shows that two names refer to one actor:

- do not rewrite the original inscription silently;
- attach the identity resolution;
- decide whether the current memorial revision changes;
- preserve earlier forms in Archives.

Translations must point to the source inscription revision they translate.

## 18. Relationship to ecology and conservation

A memorial site may become habitat or conflict with later ecological needs.

Examples:

- a memorial grove becomes a nesting area;
- a riverside marker is threatened by channel migration;
- an old rail memorial becomes part of a wildlife corridor;
- a remembrance garden requires a new accessible path;
- a locally extirpated population later recolonizes the place commemorating its loss.

Ecological change should be solved by the relevant ecology layer, not by symbolic status.

## 19. Event generation gates

Generate a memorial-related story when at least one meaningful state changes:

- new evidence alters an acknowledged status;
- a site becomes inaccessible;
- an inscription is challenged by archival evidence;
- a memorial needs relocation;
- a custodian retires or disappears;
- a living commemorated subject returns;
- a missing subject is found;
- a memorial object is damaged or transferred;
- an observance conflicts with a new ecological or infrastructure state;
- a digital memorial loses platform support;
- a legacy responsibility needs an explicit handoff.

Do not generate a quest simply because an anniversary occurred.

## 20. Minecraft projection

Minecraft may present:

- plaques and signs;
- benches, gardens and walls;
- bells or non-mechanical symbolic objects;
- route markers;
- archive terminals;
- old foundations from previous memorial locations;
- temporary public-event decoration;
- accessibility changes;
- wear and restoration phases.

The server-side memorial graph remains authoritative.

A player breaking a sign block does not delete the memorial record. A chunk reset does not restore an old inscription. A recreated structure must project the current revision.

## 21. Mechanical guardrails

Never infer these mechanics from memorial narrative:

- healing;
- Temporary HP;
- AP restoration;
- Combat Stage changes;
- Status removal/application;
- Ghost-type encounter generation;
- Legendary appearances;
- Loyalty or Command changes;
- Friendship;
- capture modifiers;
- morale;
- grief penalties;
- fear;
- occult perception;
- weather or terrain;
- resurrection;
- death from Fainted/Injury state.

Any such mechanic requires exact PTU/Caelo authority and verified engine support.

## 22. Encounter design contracts

### Memorial Procession Route Interruption

Narrative premise: a recurring civic remembrance walk encounters a separate route obstruction or external threat. The objective is to protect people and preserve access, not to make the memorial itself a combat mechanic.

FULL version dependencies:

- complete movement including interception/forced movement for moving civilians, route control and withdrawal;
- AI tactical policy for `EVACUATE`, `PROTECT_ROUTE`, `WITHDRAW`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback for procession state and semantic objectives;
- terrain/weather/hazards/zones/reactions only if a verified environmental hazard is actually part of the incident.

REDUCED version:

- stop the procession in world state;
- evacuate civilians from the battle area;
- freeze one cleared street segment;
- run a conventional static AutoPTU encounter;
- resume, reroute or cancel the commemoration afterward based on world state.

A battle result never determines what participants believe or feel.

### Archive Recovery at Old Memorial Hall

Narrative premise: records from an older memorial revision must be recovered during a separate access or safety incident.

FULL version dependencies when the building is actively unstable:

- complete movement for extraction and moving actors;
- terrain/weather/hazards/zones/reactions for any actual collapse/fire/smoke/blocked-zone mechanics;
- AI tactical policy for `RECOVER_RECORD`, `WITHDRAW`, `PROTECT_ARCHIVIST`;
- Minecraft/Cobblemon/Craftics playback.

REDUCED version:

- stabilize or cordon the unsafe areas in world state;
- move records/civilians outside the grid;
- freeze a safe room/corridor as a conventional battle map;
- resolve custody and archival interpretation afterward.

Winning cannot make an inscription historically accurate.

### Caretaker Succession at Lantern Hill

Narrative premise: a long-term caretaker leaves the role and several actors propose different stewardship arrangements.

FULL version:

Primarily non-combat. If an independent external threat interrupts the meeting, dynamic evacuation/protection requires complete movement, AI tactical policy and Minecraft playback.

REDUCED version:

- resolve proposals and acceptance through Agreements, Credentials, Land Tenure and Institutional Review where applicable;
- record a `legacy_handoff` only after explicit acceptance/authority;
- use no battle unless a genuinely separate confrontation occurs.

Winning a battle cannot award stewardship.

## 23. Engine capability mapping

For this layer's rich encounters, use the permanent engine categories exactly:

- targeting/footprints/range/LoS — useful for any static combat that occurs;
- base movement legality — sufficient for reduced static encounters;
- complete movement including push/pull/knockback/interception/forced movement — required for moving processions, escorts, dynamic evacuation or tactical withdrawal;
- core calculations — ordinary battle resolution;
- action economy/initiative — ordinary battle resolution;
- full turn/round lifecycle — required as encounters rely on more complex temporal effects;
- full stateful damage pipeline — required for full parity combat;
- status lifecycle — required only when exact status mechanics are invoked;
- terrain/weather/hazards/zones/reactions — required only when the memorial incident contains verified tactical environmental effects;
- move-specific behavior — required according to Moves used;
- abilities — required according to participants;
- items — required for actual PTU Items, not symbolic memorial objects;
- Trainer Features/perks — required only for Features actually used;
- AI legal-action infrastructure — supports legal static choices;
- AI tactical policy — required for non-KO objectives such as evacuation/protection/withdrawal;
- Minecraft/Cobblemon/Craftics adapter/playback — required for semantic world objectives and authoritative projection.

## 24. Current implementation posture

At the live Java evidence inspected for Pass 129:

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
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING.

Java now contains a parity-tested contract that can recognize `Push`/`Pull` instruction intent from Move metadata. That freezes an instruction; it does not execute forced movement. Do not promote the complete-movement category until authoritative spatial execution, collision/landing interactions and relevant parity are present.

## 25. Canon decisions still required

Before any memorial practice becomes canon, Ouros needs authored decisions on:

- which regions have formal memorial institutions;
- whether burial/cremation or any other funerary practice exists at all and in what original form;
- which sites predate the players;
- which memorials are civic, familial, ecological, institutional or sacred;
- what records can establish a death versus missing status;
- whether and how PC death can occur under the campaign's PTU/Caelo rules;
- who can authorize inscription changes or relocation;
- privacy for names and correspondence;
- what non-property legacy roles can be handed off;
- whether any inheritance/estate law exists;
- how living or missing Pokémon are commemorated;
- which supernatural claims around memorials are actually true.

Until those decisions exist, generated content should remain proposed and conservative.