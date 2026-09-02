# Community Tradition & Oral History Continuity Layer

Status: DESIGN / PROPOSED ARCHITECTURE. NOT CANON.
Date: 2026-09-01
Pass: 197
Research basis: `research/2026-09-01-community-tradition-oral-history-practice-scan-197.md`

## Purpose

Represent recurring local practices, oral accounts, inherited explanations, practice variants and material continuity without turning cultural repetition into universal belief or historical certainty.

This layer exists so Marea can slowly acquire lived culture through repeated behavior and remembered versions rather than receiving a single static lore dump.

It does not establish a religion, festival calendar, spiritual office, sacred place, official holiday, region-wide custom or supernatural truth.

## Existing-system boundaries

Reuse existing project systems rather than duplicating them.

- public memory owns community-level publication, commemoration and later public interpretation;
- mourning/private memory owns loss, private memorials and post-loss practice;
- archive/provenance owns document/object custody and evidentiary lineage;
- language/translation owns source expression, transcription and semantic interpretation;
- correspondence owns message identity and delivery;
- temporary visitor continuity owns outsider presence and access;
- public exhibition owns scheduled judged events and Contest/battle boundaries;
- education owns what was taught and corrected;
- supervised practice owns competency evidence and operational scope;
- ecology owns wildlife observations and population hypotheses;
- Minecraft/Cobblemon projects visible state but does not author cultural truth;
- PTU owns Skills, Features, Capabilities and mechanically consequential checks.

This layer owns only continuity of repeated practice and attributed accounts about it.

## Core record: community_practice

```yaml
community_practice:
  practice_id: null
  working_name: null
  name_provenance_ref: null
  place_scope_refs: []
  participant_scope_refs: []
  first_evidence_at: null
  last_observed_at: null
  recurrence_state: UNKNOWN | OCCASIONAL | REPEATED_OBSERVED | CLAIMED_RECURRING
  recurrence_claim_refs: []
  current_practice_version_ref: null
  origin_claim_refs: []
  meaning_claim_refs: []
  material_trace_refs: []
  public_scope: PRIVATE | HOUSEHOLD | GROUP | LOCAL_PUBLIC | UNKNOWN
  status: OBSERVED | REPORTED | RECONSTRUCTED | DORMANT | DISPUTED
  provenance_refs: []
```

The record says that a practice is observed/reported and how broadly evidence supports it. It does not declare that everyone in a settlement follows it.

## Practice instance

Each occurrence is preserved separately.

```yaml
practice_instance:
  instance_id: null
  practice_id: null
  occurred_at: null
  location_refs: []
  host_or_coordinator_refs: []
  participant_refs: []
  observer_refs: []
  actions_observed: []
  objects_used_refs: []
  route_refs: []
  interruptions: []
  deviations_from_version: []
  account_refs: []
  evidence_refs: []
  completed_state: COMPLETE | PARTIAL | CANCELLED | UNCERTAIN
```

A cancelled instance can still be historically meaningful if people prepared, traveled, posted notices or changed schedules.

## Practice version

```yaml
practice_version:
  version_id: null
  practice_id: null
  effective_or_observed_from: null
  supersedes_version_id: null
  procedure_summary: null
  wording_refs: []
  route_or_location_refs: []
  material_refs: []
  known_participant_scope: []
  change_basis_refs: []
  source_confidence: null
```

The current form is not assumed to be the original form.

If an old account describes another route or object arrangement, preserve both versions.

## Oral account

```yaml
oral_account:
  account_id: null
  teller_ref: null
  heard_by_refs: []
  recorded_by_ref: null
  told_at: null
  setting_ref: null
  firsthand_state: FIRSTHAND | INHERITED | MIXED | UNKNOWN
  subject_refs: []
  summarized_claim_refs: []
  wording_source_ref: null
  confidence_notes: null
  linked_account_refs: []
  contradiction_refs: []
  privacy_scope: PRIVATE | LIMITED | PUBLIC | UNKNOWN
  recording_provenance_refs: []
```

Narrative stores a summarized account or authored source reference. It must not fabricate long verbatim speeches for historical figures that were never authored.

## Meaning and origin claims

Meaning is attributed.

```yaml
practice_claim:
  claim_id: null
  practice_id: null
  claimant_ref: null
  claim_kind: ORIGIN | PURPOSE | MEANING | AGE | PARTICIPANT_SCOPE | SUPERNATURAL | HISTORICAL
  claim_text_ref: null
  made_at: null
  evidence_refs: []
  contradiction_refs: []
  confidence: null
  review_state: UNREVIEWED | SUPPORTED | PARTIAL | DISPUTED | SUPERSEDED | UNRESOLVED
```

`SUPPORTED` means evidence supports the attributed claim under the project's evidence workflow. It does not make a supernatural proposition true unless the relevant authoritative setting/mechanics layer establishes it.

## Practice variants

Different groups can perform related versions without requiring one to be erroneous.

```yaml
practice_variant:
  variant_id: null
  practice_id: null
  scope_refs: []
  version_refs: []
  distinguishing_features: []
  account_refs: []
  relation_state: RELATED | POSSIBLY_RELATED | DISPUTED_RELATION
```

Examples of legitimate variation:

- a household uses different wording;
- Puerto Bruma and Loma Clara use different timing;
- workers emphasize a practical purpose while visitors emphasize celebration;
- one version uses an object no longer available;
- a safety revision changes the route without erasing cultural continuity.

## Participation record

Participation is observable conduct, not belief.

```yaml
practice_participation:
  participation_id: null
  instance_id: null
  actor_ref: null
  role: HOST | PARTICIPANT | OBSERVER | WORKER | GUEST | UNKNOWN
  actions_observed: []
  stated_reason_claim_ref: null
  consent_or_invitation_ref: null
  knowledge_event_refs: []
```

Hard rule:

`PARTICIPATION != BELIEF`

A resident may participate for friendship, work, food, family, habit, hospitality, curiosity or duty.

## Recurrence

A single event cannot establish a recurring custom unless an attributed source says it is recurring, and that source remains a claim until corroborated.

Useful states:

- `OCCASIONAL`: observed more than once but no stable interval established;
- `REPEATED_OBSERVED`: multiple instances support recurrence;
- `CLAIMED_RECURRING`: an actor/source explicitly says it recurs, but observed history may be incomplete.

Do not infer annual, seasonal or religious recurrence from one date.

## Skipped and changed instances

A missing expected occurrence can have explicit reasons:

- weather;
- transport;
- ecological conditions;
- mourning;
- work pressure;
- unavailable host;
- safety issue;
- no reason known.

`ONE_SKIPPED_INSTANCE != PRACTICE_EXTINCT`

A later revival can legitimately reference the previous version while changing it.

## Material traces

Objects can support continuity without deciding meaning.

Examples:

- route markers;
- stored tables or cloths;
- old notices;
- tokens;
- recipe cards;
- repaired tools;
- photographs;
- archive copies;
- worn paths;
- recurring decorations when canonized.

Each object remains under normal provenance/custody systems.

`MATERIAL_TRACE != ORIGINAL_MEANING_PROVEN`

A reused object can acquire another role while retaining history.

## Public versus private practice

A household practice can remain private even if Tideglass knows it exists.

A local-public event can contain private stories that are not published.

A visitor observing an event does not gain unrestricted access to its archival or personal background.

Promotion to public memory requires the public-memory workflow, not this layer.

## Oral-history disagreement

When two accounts disagree:

1. preserve both account identities;
2. identify overlapping claims;
3. identify genuinely conflicting claims;
4. check source access and timing;
5. link later evidence without rewriting the old accounts;
6. allow partial resolution;
7. keep unresolved spans open.

`DIFFERENT_TELLING != DECEPTION`

If later evidence establishes one detail, do not automatically invalidate the rest of the older account.

## Relationship with language/translation

The oral-history layer records that a teller communicated an account and what claims were captured.

If the original speech required translation or transcription, the language layer owns that transformation.

A translation revision can change how an account is rendered without deleting the historical fact that an earlier rendering circulated.

## Visitor interpretation boundary

Outsiders can supply useful contrast.

A visitor may call something:

- a shrine;
- monument;
- festival;
- superstition;
- lucky route;
- memorial;
- ceremony.

Store the term as their interpretation until local/canon evidence establishes the category.

`VISITOR_LABEL != LOCAL_CANON`

A repeated traveler can later correct their own interpretation.

## Supernatural boundary

This layer records claims and observable practice only.

It cannot prove efficacy.

Hard boundaries:

`RITUAL_PERFORMED != SUPERNATURAL_EFFECT_OCCURRED`

`GHOST_TYPE_PRESENT != SPIRIT_IDENTIFIED`

`POKEMON_ARRIVED_DURING_PRACTICE != BLESSING_PROVEN`

`DREAM_REPORTED != PROPHECY_CONFIRMED`

`OLD_STORY != LEGENDARY_ENCOUNTER_CONTRACT`

If Caelo/PTU later establishes a mechanically governed supernatural interaction, that mechanic remains authoritative and should emit a narrow fact back to Narrative.

## PTU Skill boundary

Project PTU content includes General Education, Occult Education, Pokémon Education and other Skills. Occult Education participates in concrete prerequisites/effects.

Therefore:

- local residence does not grant a Skill Rank;
- age does not grant a Skill Rank;
- attendance does not grant a Skill Rank;
- telling a story does not prove high Occult Education;
- an archive job does not grant General Education;
- Narrative cannot invent a folklore roll that bypasses PTU;
- a successful governed knowledge check may establish recall/recognition only within the exact procedure;
- mechanical success does not transform an attributed supernatural or historical claim into objective truth unless the governing mechanic explicitly says it does.

## NPC agency

Practices can occur without the player.

If the required residents are present and schedules permit, the world may record an instance while the player is elsewhere.

Later evidence might include:

- moved furniture;
- a dated Tideglass note;
- leftovers or cleaned-up materials;
- a route sign restored to normal;
- a resident remembering who attended;
- a visitor referencing the event;
- an updated practice version after a problem.

The player should not be required to personally trigger every recurrence.

## Long-term evolution

A practice can evolve through small deltas:

- new host;
- changed route;
- safer procedure;
- different wording;
- participation by a new household;
- temporary pause;
- disagreement over origin;
- correction to public description;
- a visitor becoming a repeat participant;
- an ecological observation changing timing;
- material objects being repaired or replaced.

No global culture score is required.

## Minecraft/Cobblemon projection boundary

Minecraft may project:

- participants;
- temporary gathering positions;
- tables, signs or route markers;
- wearable/held visual objects when canonized;
- food or supply presentation;
- Pokémon observers/participants;
- lights, decorations or particles as presentation where culturally approved.

Projection cannot author meaning.

Hard rules:

`NPC_SPAWNED_AT_EVENT != PARTICIPATION_RECORDED`

`ENTITY_UNLOAD != PRACTICE_ENDED`

`ITEM_PICKUP != CULTURAL_OWNERSHIP_TRANSFER`

`DECORATION_PLACED != TRADITION_CANONIZED`

`PARTICLE_EFFECT != SUPERNATURAL_EFFECT`

`WILD_SPAWN_NEAR_EVENT != ECOLOGICAL_CAUSE_PROVEN`

`CLIENT_LOCALIZATION != IN_WORLD_WORDING`

## Quest grammar

Low-mechanics stories can include:

- compare two oral accounts;
- locate the source of an old wording variation;
- identify which version of a route practice a notice describes;
- preserve a household account without publishing it;
- correct an outsider's label without deciding the deeper history;
- prepare material for a recurring event without creating a festival authority;
- record why one expected instance was skipped;
- return an old object to its normal storage after use;
- document a new safety change;
- discover that a practical habit and a celebratory explanation refer to the same repeated action;
- leave a disputed origin unresolved while still supporting the current practice.

## First implementation slice — Two Tellings at Tideglass

Premise:

Tideglass holds two separately sourced accounts of an older Marea work practice or storm-season habit. Most details agree. One origin claim and one step differ.

State exercised:

- two `oral_account` records;
- one `community_practice` working identity;
- overlapping and conflicting `practice_claim` records;
- one provenance link per account;
- one partial corroborating record;
- unresolved final origin.

Actors:

- Pia prepares comparison material within her existing archive responsibilities;
- Taro reviews provenance and preserves both tellings;
- no new institutional role is created.

Possible resolution:

A mundane record confirms that one sequence detail existed by a certain date but does not prove who invented it or why.

Persistent consequence:

Tideglass now holds a reviewed comparison. Future education, visitor dialogue or public-memory material can cite the disagreement rather than flatten it.

Requirements:

- no battle;
- no Skill check required;
- no supernatural content;
- no new named historical character required;
- no festival canon;
- no religion canon.

Current disposition: IMPLEMENTABLE AS NARRATIVE/WORLD STATE.

## Mechanically rich encounter — Community Route Walk at Glass Bend

Premise:

A repeated practical/community walk uses a known part of Sendero del Vidrio. Different participants may describe its significance differently. Local wild activity creates an immediate safety problem during one instance.

The practice itself is not a battle objective and wild Pokémon do not validate its story.

### Intended full version

Potential tactical content:

- a group of world-state participants;
- one or more wild combatants;
- narrow route geometry;
- protection/withdrawal objective;
- Interception;
- Push/Pull/Knockback or other forced movement when selected content uses it;
- terrain/weather/hazards only when authored and mechanically verified;
- exact Moves, Abilities, Items and Trainer Features;
- objective-aware wild and allied AI;
- faithful Minecraft/Cobblemon/Craftics projection and playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content uses statuses;
- terrain/weather/hazards/zones/reactions when route conditions are tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current disposition: FULL VERSION BLOCKED.

### Reduced version

1. Practice identity, participants, route meaning, material objects and oral-history state remain Narrative-owned.
2. Noncombatants are moved to a safe authored world-state position before BattleSpec.
3. The practice never becomes a battle buff/debuff.
4. Select stable geometry and audited combatants/content.
5. Omit tactical weather, hazards, reactions and forced-movement objectives unless separately verified.
6. If an immediate wild actor still blocks passage, run a conventional audited battle.
7. Consume only narrow handoffs such as `IMMEDIATE_ROUTE_THREAT_WITHDREW` or `IMMEDIATE_PASSAGE_CLEAR`.

Battle cannot establish:

- origin of the practice;
- historical age;
- belief;
- community-wide adoption;
- festival status;
- supernatural efficacy;
- participant relationship changes;
- future recurrence;
- whether an oral account is true.

Current disposition: REDUCIBLE WITH AUDITED CONTENT.

## Strong invariants

`REPEATED_PRACTICE != REGION_WIDE_CUSTOM`

`PARTICIPATION != BELIEF`

`PUBLIC_STORY != HISTORICAL_FACT`

`OLD_VERSION != FALSE`

`DIFFERENT_TELLING != DECEPTION`

`MATERIAL_TRACE != ORIGINAL_MEANING_PROVEN`

`VISITOR_INTERPRETATION != LOCAL_CANON`

`ARCHIVED_ACCOUNT != ENDORSED_ACCOUNT`

`FESTIVAL_ATTENDANCE != INSTITUTIONAL_MEMBERSHIP`

`POKEMON_BEHAVIOR_DURING_PRACTICE != SUPERNATURAL_VALIDATION`

`MINECRAFT_DECORATION != CANONICAL_RITUAL_OBJECT`

`ONE_SKIPPED_INSTANCE != PRACTICE_EXTINCT`

`SUCCESSFUL_KNOWLEDGE_CHECK != SUPERNATURAL_TRUTH`

## Canon promotion gate

Before an actual Marea recurring practice is promoted, resolve only the facts that slice needs:

- who is observed participating;
- whether it is private, group-level or locally public;
- which past instances have evidence;
- what current procedure is observed;
- which origin/meaning statements are attributed rather than established;
- which existing actor can legitimately host or record it;
- whether public display requires consent or publication authority.

Do not globally resolve:

- Marea religion;
- Caelo religion;
- sacred geography;
- official holidays;
- compulsory customs;
- priesthood/clergy;
- supernatural efficacy;
- region-wide beliefs;
- universal cultural etiquette;
- cultural ownership law.

The layer is intentionally useful while all those questions remain open.