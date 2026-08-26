# Rumor, Testimony & Local-Knowledge Extension

Status: proposed systems design. Not established canon.

## Purpose

This extension makes informal information playable without duplicating Media/Communications, Public Memory, Observation or Case/Authority.

It answers four implementation questions:

1. Who actually said the claim?
2. How did it reach the current actor?
3. What changed during retelling?
4. What evidence, if any, has tested it?

The design treats rumors as durable claim objects with provenance rather than disposable quest text.

## Ownership boundaries

Media/Communications owns channels, packets, publication and delivery.

Observation owns direct field observations and knowledge records.

Public Memory owns community-scale remembered narratives.

Case/Authority owns evidentiary status where formal cases exist.

This extension owns informal claim continuity and local testimony before or outside those formal systems.

## Informal claim

```yaml
informal_claim:
  claim_id: null
  subject_ids: []
  proposition: null
  originating_actor_id: null
  originating_event_id: null
  origin_time: null
  origin_location_id: null
  source_mode: first_person
  confidence_at_origin: uncertain
  belief_state_at_origin: believed
  sensitivity: ordinary
  current_resolution: unresolved
  evidence_support_ids: []
  evidence_conflict_ids: []
  canonical_fact_links: []
```

Candidate source modes:

- FIRST_PERSON
- SECOND_HAND
- LOCAL_TRADITION
- PROFESSIONAL_HEARSAY
- PUBLIC_CHATTER
- DELIBERATE_PLANT
- UNKNOWN_ORIGIN

Candidate belief states:

- BELIEVED
- SUSPECTED
- DOUBTED
- REPEATED_WITHOUT_COMMITMENT
- KNOWN_FALSE_BY_SOURCE
- UNKNOWN

A claim marked KNOWN_FALSE_BY_SOURCE can still spread. That flag does not reveal itself to actors who lack evidence of the source’s intent.

## Transmission event

```yaml
claim_transmission:
  transmission_id: null
  claim_id: null
  from_actor_id: null
  to_actor_ids: []
  location_id: null
  timestamp: null
  channel_ref: null
  directness: direct
  attribution_preserved: true
  uncertainty_preserved: true
  wording_changed: false
  emphasis_tags: []
  omitted_elements: []
  added_inference_claim_ids: []
```

A retelling must never mutate the original claim. It creates a transmission record and, where meaning changes materially, a new linked claim.

## Claim lineage

```yaml
claim_lineage:
  root_claim_id: null
  descendant_claim_ids: []
  mutation_events: []
  merge_events: []
  split_events: []
```

This supports cases where one modest observation becomes several rumors, or where two unrelated stories are combined by the community.

## Distortion metadata

Possible tags:

- MEMORY_COMPRESSION
- SECOND_HAND
- AMBIGUOUS_VISIBILITY
- MISTAKEN_IDENTITY
- METAPHOR_LITERALIZED
- PROTECTIVE_OMISSION
- STATUS_PRESSURE
- FEAR_FRAMING
- FACTION_FRAMING
- DELIBERATE_BAIT
- OUTDATED
- EVENT_MERGE

These tags describe provenance. They never produce dice modifiers.

## Local knowledge scope

```yaml
local_knowledge:
  knowledge_id: null
  holder_id: null
  subject_scope: null
  location_ids: []
  time_scope: null
  basis_event_ids: []
  basis_observation_ids: []
  repeated_exposure_count_band: null
  known_patterns: []
  known_exceptions: []
  confidence: null
  last_confirmed_at: null
```

Examples:

- a ferry worker knows the normal third-departure crowd;
- a shopkeeper knows which delivery usually arrives before opening;
- a resident recognizes the ordinary sound of a building at night;
- a guide knows which trail nickname older residents still use;
- a ranger-like worker knows that a certain seasonal closure is normal.

Local knowledge is not universal expertise. It must be grounded in repeated access or explicit learned history.

## Testimony packet

When informal claims enter a formal investigation, create an explicit handoff rather than rewriting them as evidence.

```yaml
testimony_packet:
  testimony_id: null
  claimant_id: null
  related_claim_ids: []
  interview_event_id: null
  first_hand_claim_ids: []
  second_hand_claim_ids: []
  uncertainty_notes: []
  contradiction_ids: []
  consent_scope: null
  formal_case_ref: null
```

Case/Authority then decides formal relevance. This extension does not invent evidentiary law.

## Corroboration graph

```yaml
corroboration_graph:
  subject_id: null
  claim_ids: []
  observation_ids: []
  record_ids: []
  object_or_trace_ids: []
  supporting_edges: []
  conflicting_edges: []
  unresolved_edges: []
```

The graph should surface intersections without calculating “truth score.”

A useful player-facing result can say:

- two independent witnesses describe the same time window;
- a maintenance log conflicts with both;
- a direct observation supports the location but not the claimed cause.

The server still owns world truth.

## Rumor family

```yaml
rumor_family:
  family_id: null
  shared_subject_ids: []
  root_claim_ids: []
  active_claim_ids: []
  communities: []
  current_salience: local
  known_contradictions: []
  formal_response_ids: []
  resolution_state: unresolved
```

Rumor families help the generator recognize that several apparently separate hooks are about the same place, actor or phenomenon.

They must not become a generic “rumor meter.” Salience comes from real transmissions, events and consequences.

## Resolution states

Suggested states:

- UNRESOLVED
- PARTIALLY_CONFIRMED
- CONFIRMED_NARROWLY
- DISPROVEN_NARROWLY
- REINTERPRETED
- OUTDATED
- FORMALLY_DISPUTED
- CLOSED_WITHOUT_CERTAINTY

A resolution applies only to the proposition tested. If a witness accurately saw a glowing shape, discovering its identity does not prove unrelated claims about motive, rarity or supernatural meaning.

## Deliberate planting

```yaml
planted_claim:
  claim_id: null
  planter_actor_id: null
  intended_audience_ids: []
  intended_effect: null
  known_truth_state: null
  dissemination_plan_refs: []
  discovered_by_ids: []
  discovery_event_id: null
```

Narrative generator rules:

- do not invent persuasion success;
- do not assume everyone repeats the claim;
- do not reveal planter intent to actors without evidence;
- do not turn a planted story into canonical history merely because it spreads.

## Local rumor surfaces in Minecraft

Possible presentations:

- changing ambient NPC conversation snippets;
- bulletin-board annotations clearly marked as informal;
- tavern/café/common-room chatter where such venues exist;
- transport-line talk;
- worker break-area talk;
- repeated comments from residents with distinct provenance;
- a notebook or field-journal UI showing claim lineage;
- visible correction or retraction after later evidence.

The client should not receive hidden source-intent metadata it is not allowed to know.

## Generator hooks

Generate an informal-information scene only when at least one concrete state source exists:

- an unresolved observation;
- an unexplained service change;
- conflicting witness accounts;
- a repeated local anomaly;
- a public event with incomplete visibility;
- a historic claim with new evidence;
- a player action that had limited witnesses;
- a faction or institution with an actual reason to frame information.

Do not generate rumors purely to make a quiet area feel busy.

## Noncombat scene grammar

A compact investigation can use:

claim → provenance check → second source → direct observation/record → contradiction → narrower question → resolution or retained uncertainty.

The final step may legitimately be “we still do not know.”

## Long-arc grammar

For larger mysteries:

1. several low-confidence claims appear independently;
2. repeated subjects or timestamps connect them;
3. one claim is disproven but reveals a useful place/person;
4. a trusted account is shown to be incomplete;
5. a formal institution responds to only part of the issue;
6. later direct evidence changes the community interpretation;
7. Public Memory records both the earlier story and the correction.

## Encounter contract — Quarry Echo Search

Narrative premise: several workers report a recurring sound near an inactive extraction face. Investigation establishes a real Pokémon presence, but the cause of the sound remains uncertain until the site is checked.

Full intended version may use unstable zones, route changes, falling-debris hazards, forced displacement, objective-aware withdrawal and environmental playback.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if displacement matters
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when instability is tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Resolve site evacuation and unstable-area closure in world state before battle. Freeze one safe static combat area. Run only legal combatants and verified mechanical slices. The battle result can establish that the Pokémon were present; it cannot automatically prove what caused earlier sounds.

## Encounter contract — Market-Lane Misidentification

Narrative premise: repeated stories blame one Pokémon for damaged goods, but observation reveals more than one actor used the lane during the relevant period.

Full intended version may involve moving civilians, narrow-lane interception, destructible stalls, escape objectives and objective-aware AI.

Reduced version:

Clear civilians and merchandise from the tactical area first. Use a static ordinary encounter only if conflict actually occurs. Resolve responsibility through observations, timestamps and claims after combat rather than through a fabricated combat score.

## PTU/Caelo guardrails

This extension cannot create social Skill modifiers, deception DCs, perception DCs, initiative effects, accuracy changes, hidden tactical preparation bonuses, supernatural truth detection, Pokémon communication capabilities, Feature effects or reputation bonuses.

Any mechanically resolved interrogation, tracking, perception, Feature use, Move, Ability or item effect must be checked against governing PTU/Caelo material and current AutoPTU support.

## Integration flow

```text
world fact
→ observation/event
→ first claim
→ transmission/retelling
→ actor knowledge
→ corroboration or contradiction
→ optional field report/testimony packet
→ publication/case/public memory
```

No arrow may jump directly from widespread belief to canonical truth.

## Promotion gate

Before any specific rumor tradition, information venue, elder role, gossip custom or informal investigation practice becomes canon, review its location, institution/culture fit, privacy implications, PTU/Caelo assumptions, Minecraft representation and overlap with existing approved lore.