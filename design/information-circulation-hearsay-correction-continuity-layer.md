# Ouros Information Circulation, Hearsay & Correction Continuity Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Pass: 200
Date: 2026-09-02

## Purpose

This layer models how claims travel through a persistent community.

It does not decide truth from repetition. It records origin, version, audience, transmission, correction and later use so Ouros can support investigation, misunderstandings, public notices and local impressions without omniscient NPCs or a global reputation score.

Core chain:

`observation/source -> claim version -> transmission -> received version -> later repetition or action -> correction/qualification -> uneven update`

Existing provenance systems remain owners of documents, observations and testimony. Pass 200 owns the circulation seam between them.

## Authority boundaries

Narrative owns world-facing information history:
- who made or published a claim;
- what version existed at a given time;
- attributed source references;
- who actually received a version when known;
- transmission lineage;
- corrections, withdrawals and qualifications;
- public/private audience scope;
- later authored callbacks and consequences.

PTU/Caelo/AutoPTU own mechanically governed:
- Skill ranks;
- social/perception checks;
- Features/Edges that change information access or interaction;
- supernatural information mechanics;
- battle facts and results.

Minecraft/Cobblemon/Craftics may project speech, boards, books, notices, subtitles, particles and NPC actors. Presentation never creates canonical knowledge merely because a client rendered it.

## 1. Information claim

```yaml
information_claim:
  claim_id: null
  subject_refs: []
  proposition_key: null
  statement_summary: null
  speaker_or_publisher_id: null
  source_refs: []
  origin_time: null
  location_id: null
  epistemic_state: REPORTED
  scope_limits: []
  confidence: null
  canon_truth_ref: null
  current_version_id: null
```

Suggested epistemic states:
- REPORTED
- OBSERVED
- INFERRED
- HYPOTHESIZED
- CORROBORATED
- CONTRADICTED
- CORRECTED
- WITHDRAWN
- UNRESOLVED

These states describe provenance. They do not replace PTU Skills or automatically determine truth.

## 2. Claim version

```yaml
claim_version:
  claim_version_id: null
  claim_id: null
  version_number: null
  wording_summary: null
  qualifiers: []
  omitted_scope: []
  issued_by_id: null
  issued_at: null
  revision_of: null
  superseded_by: null
  source_refs: []
```

A later version must preserve earlier versions.

## 3. Transmission event

```yaml
information_transmission:
  transmission_id: null
  claim_version_id: null
  transmitter_id: null
  recipient_actor_ids: []
  audience_scope_ref: null
  channel: CONVERSATION
  location_id: null
  occurred_at: null
  parent_transmission_id: null
  transformation_tags: []
  confidence_presented: null
```

Suggested channels:
- CONVERSATION
- DIRECT_MESSAGE
- COURIER
- PUBLIC_NOTICE
- ARCHIVE_COPY
- CLASS_HANDOUT
- MARKET_BOARD
- FERRY_ADVISORY
- BATTLE_YARD_BOARD
- FIELD_REPORT
- PUBLICATION

Suggested transformation tags:
- DIRECT_REPEAT
- PARAPHRASED
- SHORTENED
- QUALIFIED
- AMPLIFIED
- GENERALIZED
- CONTRADICTED
- UNCERTAINTY_ADDED
- UNCERTAINTY_DROPPED

A transformation tag records what happened to the content. It does not infer intent.

## 4. Source lineage

```yaml
claim_lineage:
  lineage_id: null
  terminal_claim_or_version_id: null
  root_source_refs: []
  transmission_refs: []
  independent_source_groups: []
  unresolved_origin: false
```

This prevents false corroboration.

Three separate speakers can still have one root source.

`MANY_REPEATERS != MANY_INDEPENDENT_SOURCES`

## 5. Reception state

```yaml
information_reception:
  reception_id: null
  recipient_id: null
  claim_version_id: null
  transmission_id: null
  received_at: null
  understood_scope: null
  retained_qualifiers: []
  later_update_refs: []
```

Use explicit reception only where it matters. Do not simulate every sentence heard by every resident.

Compression is allowed for low-stakes public information when the audience can be represented as a bounded group and the exact individual history is irrelevant.

## 6. Public information surface

```yaml
public_information_surface:
  surface_id: null
  location_id: null
  channel_type: null
  current_publication_ref: null
  physical_projection_refs: []
  intended_audience_scope: null
  update_responsibility_ref: null
  last_authoritative_update_at: null
```

Examples:
- ferry board;
- Battle Yard schedule;
- market notice;
- field advisory;
- school handout display;
- archive reading-room notice.

A physical projection can lag behind the authoritative publication.

`NOTICE_VISIBLE != NOTICE_CURRENT`

## 7. Correction and qualification

```yaml
information_correction:
  correction_id: null
  target_claim_version_ids: []
  correcting_actor_or_institution_id: null
  corrected_proposition_summary: null
  evidence_refs: []
  issued_at: null
  publication_ref: null
  reach_scope: null
  followup_transmission_refs: []
```

A correction has two histories:
- issuance;
- reception.

`CORRECTION_ISSUED != EVERY_RECIPIENT_UPDATED`

The system should never retroactively rewrite what an NPC plausibly believed before receiving the correction.

## 8. Contradiction without forced resolution

Two claims may conflict while both remain unresolved.

```yaml
claim_conflict:
  conflict_id: null
  claim_version_refs: []
  conflict_dimension: null
  evidence_refs: []
  resolution_state: OPEN
  resolved_by_ref: null
```

Useful dimensions include:
- time;
- quantity;
- location;
- identity;
- cause;
- interpretation;
- forecast;
- responsibility.

Conflict does not imply deception.

## 9. Distributed impressions

Do not implement a universal `reputation_score`.

```yaml
actor_impression_record:
  impression_id: null
  holder_id: null
  subject_actor_or_faction_id: null
  basis_event_refs: []
  basis_claim_refs: []
  authored_impression_tags: []
  confidence: null
  last_updated_at: null
```

Examples of tags may be authored terms such as RELIABLE_ON_ROUTE_REPORTS or HAS_UNRESOLVED_COMPLAINT. They must point to concrete basis records.

No tag directly grants Charm, Guile, Command, Intuition, Perception, access, discounts or relationship changes unless a separate authored/mechanical rule does so.

## 10. Knowledge boundary

Canonical hard boundaries:

`REPEATED_CLAIM != FACT`

`PUBLICLY_STATED != UNIVERSALLY_KNOWN`

`PUBLICLY_HEARD != REMEMBERED_BY_EVERYONE`

`CORRECTION_ISSUED != CORRECTION_RECEIVED`

`RUMOR != MALICIOUS_LIE`

`DIFFERENT_VERSION != DELIBERATE_DECEPTION`

`SOURCE_CONFIDENCE != TRUTH`

`MANY_SOURCES != INDEPENDENT_CORROBORATION`

`PLAYER_HEARD != PARTY_OR_NPC_KNOWLEDGE`

`NPC_PROXIMITY != NPC_KNOWLEDGE`

`MINECRAFT_CHAT_VISIBLE != CANONICAL_RECEPTION`

`FAVORABLE_TALK != RELATIONSHIP_GAIN`

`HOSTILE_TALK != GLOBAL_REPUTATION_LOSS`

`BATTLE_OUTCOME != BROAD_CLAIM_VERIFIED`

## 11. Thin Delivery Season integration

This layer strengthens the existing open mystery without resolving it.

Examples:
- Ivo reports a smaller lot.
- a vendor repeats that report as evidence of regional scarcity.
- another resident hears only the shortened version.
- Lia later verifies that a specific scheduled shipment arrived on time.
- that correction narrows one route-delay claim but does not explain the overall season.

The system can trace the claim history while the causal question remains open.

## 12. Mirador integration

Mirador observations already have provenance and revision history.

Pass 200 adds circulation around them.

Example:
- Ema records one direct sighting;
- Nerea publishes a qualified note;
- a market speaker says there are “many” of that species on the route;
- two residents repeat the market version;
- Tideglass later links both repetitions to the same upstream source.

The population layer remains owner of ecological interpretation.

## 13. Tideglass integration

Tideglass can preserve:
- original deposition;
- copies;
- later correction slips;
- edition links;
- attributed oral testimony;
- circulation history when relevant.

Taro's role supports preserving contradiction rather than flattening it.

## 14. Visitor integration

A visitor may become an information source about places beyond currently canonized geography.

Narrative may store:
- visitor identity;
- exact attributed claim;
- time of visit;
- later repeaters;
- later corrections.

The claim does not canonize an external settlement, event or regional condition until separately approved.

## 15. Public boards and stale projections

A current schedule or advisory should live in authoritative Narrative state.

Minecraft signs/books/screens are projections.

If the authoritative schedule changes while an old sign remains physically loaded:
- the old sign remains evidence that an outdated version was visible;
- it does not revert the schedule;
- NPCs who saw only the old version can still act in good faith;
- replacing the sign is a maintenance/publication task, not a truth rewrite.

## 16. Off-screen circulation

Important information can circulate without the player present when there is a plausible path.

Compression requirements:
- named source or publication exists;
- recipient/audience relationship is plausible;
- channel exists;
- time is sufficient;
- high-impact transformations remain inspectable;
- the system does not spread a claim merely to force a plot beat.

Do not run full social-network diffusion simulation for every line of dialogue.

## 17. PTU Skills and social mechanics

AutoPTU source material confirms real Skill categories including Guile, Perception, Charm and Intuition.

Narrative can present evidence and preserve what was said. Any mechanically meaningful attempt to:
- detect deception;
- read intent;
- persuade;
- intimidate;
- notice a hidden detail;
- conceal information;
- leverage a Feature or Edge

must defer to an authoritative PTU/Caelo/AutoPTU path when mechanics are required.

A narrative `confidence` field is provenance metadata. It is never a replacement Skill roll.

## 18. Battle-aware encounter pattern

### Full concept: Field Check after the Glass Bend Warning

A circulating warning claims that wild Pokémon have “taken over” the seasonal crossing. Mara or Mirador commissions a bounded field check because the claim is operationally relevant, not because it is accepted as truth.

On site, the team finds evidence supporting only a narrower immediate fact: a specific wild actor or small encounter currently obstructs passage.

If the full encounter uses protected withdrawal, corridor control, Interception, displacement, environmental constraints or objective-aware wild behavior, dependencies are:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where selected content requires it;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

The rich form remains blocked while required families remain partial/blocking.

### Reduced concept

Keep claim lineage, field-check purpose, noncombatants, ecology evidence and route advisory outside BattleSpec.

Narrative first moves observers/noncombatants to a safe semantic state. If one immediate actor still prevents passage, create one ordinary audited battle on stable geometry with verified content.

Allowed narrow handoffs:
- `IMMEDIATE_ROUTE_THREAT_CONFIRMED_AT_TIMESTAMP`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR_AT_TIMESTAMP`

The battle cannot establish:
- rumor origin;
- speaker intent;
- population-scale presence;
- permanent route safety;
- ecological cause;
- future recurrence;
- that every prior warning was false or true;
- who received the correction;
- relationship/reputation changes.

## 19. Generation rules

1. Attribute consequential claims.
2. Preserve source lineage when claims repeat.
3. Keep independent corroboration distinct from social repetition.
4. Preserve old versions instead of silently rewriting history.
5. Model correction reach only where it matters.
6. Keep actor knowledge bounded by plausible reception.
7. Let honest witnesses be mistaken about interpretation.
8. Do not infer malicious intent from a wrong statement.
9. Avoid global reputation numbers.
10. Avoid omniscient town gossip.
11. Use boards/publications as versioned channels.
12. Keep battle facts narrow and timestamped.
13. Never use client chat/proximity as world authority.
14. Defer mechanically significant social/perception actions to PTU/Caelo/AutoPTU.
15. Prefer consequences from uneven information over scripted exposition.

## 20. Canon status

CANON-APPROVED inputs:
- Marea geography and residents;
- Mirador provenance/revision principle;
- Tideglass contradictory-testimony role;
- Thin Delivery Season competing hypotheses;
- per-NPC knowledge and relationship history;
- Minecraft presentation cannot author world truth.

PROPOSED:
- all schemas and state names in this layer;
- claim-lineage and reception tracking;
- correction-reach model;
- distributed impression records;
- Marea pass-200 seeds.

UNCERTAIN:
- Caelo social/information rules;
- formal reputation mechanics;
- publication authority;
- privacy/defamation standards;
- emergency-notice powers;
- supernatural truth/intent-reading boundaries beyond verified mechanics.
