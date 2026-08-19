# Ouros Media, Communications & Information Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already stores canonical facts, public memory, actor knowledge, rumors, evidence, crisis forecasts and institutional state. This layer defines how information moves between those systems.

The goal is to prevent impossible omniscience while still giving players a readable, useful world.

A fact can exist without being known.
A witness can know something without publishing it.
A publication can be wrong without changing world truth.
A correction can exist without erasing the earlier report.
A message can be sent without being delivered.

## 1. Information packet

The smallest durable unit is an information packet.

```yaml
information_packet:
  info_id: null
  source_fact_ids: []
  claim_ids: []
  created_by_actor_id: null
  created_by_institution_id: null
  created_at: null
  information_type: null
  confidence: null
  visibility: null
  sensitivity: null
  source_refs: []
  supersedes_info_id: null
  correction_of_info_id: null
```

Candidate information types:

- VERIFIED_NOTICE
- OFFICIAL_STATEMENT
- JOURNALISTIC_REPORT
- EYEWITNESS_ACCOUNT
- RESEARCH_REPORT
- WEATHER_REPORT
- ROUTE_REPORT
- SAFETY_ALERT
- EVENT_ANNOUNCEMENT
- PUBLIC_RECORD
- FACTION_MESSAGE
- ADVERTISEMENT
- PERSONAL_MESSAGE
- REQUEST
- RUMOR
- OPINION

An information packet stores claims. It does not become canonical truth merely because its publisher is trusted.

## 2. Publication record

A packet becomes public through a publication event.

```yaml
publication:
  publication_id: null
  info_id: null
  publisher_id: null
  channel_id: null
  published_at: null
  intended_audience_ids: []
  intended_region_ids: []
  presentation_summary: null
  editorial_tags: []
  source_disclosure: null
  correction_policy: null
  archived: true
```

The presentation summary is allowed to paraphrase. The underlying claims and provenance remain stable.

## 3. Communication channel

```yaml
communication_channel:
  channel_id: null
  channel_type: null
  operator_id: null
  infrastructure_ids: []
  coverage_regions: []
  audience_policy: null
  contact_requirement: null
  typical_latency: null
  reliability_band: null
  supports_private_delivery: false
  supports_broadcast: false
  supports_acknowledgement: false
  current_status: operational
```

Candidate channel types:

- PUBLIC_BULLETIN
- PRINT_NEWS
- RADIO
- TELEVISION
- DEVICE_NEWS
- DIRECT_CALL
- DIRECT_MESSAGE
- INSTITUTIONAL_DISPATCH
- COURIER
- PUBLIC_ADDRESS
- RESEARCH_NETWORK
- EMERGENCY_ALERT
- NPC_GOSSIP

The actual technology used in Ouros remains a canon decision. These are logical categories.

## 4. Communications infrastructure

Information reach can depend on physical state.

```yaml
communication_infrastructure:
  infrastructure_id: null
  infrastructure_type: null
  location_id: null
  operator_id: null
  status: operational
  dependency_ids: []
  coverage_effects: []
  repair_state: null
  security_state: null
  last_verified_at: null
```

Possible infrastructure types include relay, tower, repeater, local board, cable route, satellite-equivalent service, dispatch desk, server, postal hub or public terminal. The final technology level is not inferred automatically.

Infrastructure can depend on power, transport, staffing or route state. This lets existing crisis and travel systems create communication consequences without adding arbitrary drama.

## 5. Coverage state

Coverage should be explicit rather than universal.

```yaml
coverage_state:
  channel_id: null
  region_id: null
  state: available
  latency_modifier: null
  reliability_modifier: null
  reason_ids: []
  valid_from: null
  valid_until: null
```

Suggested states:

- AVAILABLE
- DEGRADED
- INTERMITTENT
- DELAYED
- LOCAL_ONLY
- BLOCKED
- UNKNOWN

A player outside coverage can still learn the same information later by entering another region, meeting an informed actor, reading an archived copy or receiving a delayed message.

## 6. Delivery receipt

Private communication needs delivery state.

```yaml
message_delivery:
  delivery_id: null
  info_id: null
  sender_id: null
  recipient_id: null
  channel_id: null
  sent_at: null
  delivered_at: null
  acknowledged_at: null
  delivery_state: queued
  failure_reason: null
  retries: 0
```

Suggested delivery states:

- QUEUED
- SENT
- DELAYED
- DELIVERED
- ACKNOWLEDGED
- FAILED
- EXPIRED

A failed delivery is useful world state. It should not silently become a completed conversation.

## 7. Contact graph

Direct messages require reachability.

```yaml
contact_edge:
  actor_a_id: null
  actor_b_id: null
  channel_types: []
  established_by_event_id: null
  active: true
  privacy: private
  institution_mediated: false
```

Possible reasons a message is valid:

- the actors exchanged contact details;
- they belong to the same institution;
- a public office provides a contact route;
- a mutual institution forwards the message;
- the recipient has an open public channel;
- an established quest/case provides a temporary dispatch route.

The generator must not give every NPC universal direct access to every PC.

## 8. Editorial transformation

A publication can summarize or frame claims without changing source truth.

```yaml
editorial_transform:
  transform_id: null
  input_info_ids: []
  output_info_id: null
  editor_actor_id: null
  editor_institution_id: null
  omitted_claim_ids: []
  emphasized_claim_ids: []
  uncertainty_preserved: true
  attribution_preserved: true
```

Hard rule: editorial framing may alter public interpretation but cannot mutate `world_truth`.

## 9. Corrections and version history

News should be append-only by default.

If an early report says a bridge is open and a later field report confirms collapse, the old story remains part of public-history state.

```yaml
information_revision:
  revision_id: null
  original_info_id: null
  replacement_info_id: null
  reason: correction
  issued_at: null
  issued_by: null
  affected_audiences: []
```

This supports realistic cases where some actors heard the correction and others did not.

## 10. Audience knowledge writeback

Receiving a packet does not guarantee belief.

Possible writeback:

```yaml
knowledge_update:
  actor_id: null
  received_info_id: null
  received_at: null
  knowledge_bucket: received_claims
  credibility_assessment: null
  retained_uncertainty: true
```

The actor's beliefs remain governed by the existing Actor Knowledge layer.

## 11. Public notices versus journalism

These should remain separate.

Public notice:

- communicates an institution's current position or instruction;
- may be authoritative about the institution's own schedule, closure or rule;
- may still contain incomplete factual assumptions about outside events.

Journalistic report:

- combines observations, interviews and records;
- may investigate contradictions;
- can correct previous reports;
- should preserve source attribution internally.

Rumor:

- can propagate without formal verification;
- must remain tagged as rumor/claim;
- may become a quest hook without becoming truth.

## 12. Emergency communication

Crisis communication should reuse existing crisis state.

```yaml
emergency_alert:
  alert_id: null
  crisis_id: null
  info_id: null
  severity_band: null
  affected_regions: []
  channel_ids: []
  issued_at: null
  expires_at: null
  superseded_by: null
```

Examples of valid alert content:

- route closure;
- shelter opening;
- transport suspension;
- evacuation advisory;
- weather warning;
- missing-person public request;
- service outage.

The alert itself does not create hazard mechanics.

If infrastructure fails, the crisis system can create alternative delivery paths such as local boards, runners, transport crews or physical sirens if those exist in canon.

## 13. Reporter and communicator roles

Ouros can support recurring media NPCs without turning them into omniscient exposition machines.

Possible roles:

- reporter;
- editor;
- field photographer;
- broadcaster;
- local bulletin keeper;
- researcher;
- public-information officer;
- dispatcher;
- courier;
- translator;
- archivist;
- technical operator.

Each role uses normal actor knowledge. A reporter must gather or receive information before publishing it.

## 14. Interview object

```yaml
interview:
  interview_id: null
  interviewer_id: null
  subject_ids: []
  related_event_ids: []
  asked_topic_ids: []
  response_claim_ids: []
  consent_scope: null
  recording_state: null
  publication_permission: null
```

The system must not fabricate a PC quote. Player-authored responses can be stored as claims with provenance.

Silence, refusal or “off record” can be valid outcomes if the UI supports them.

## 15. Local information ecology

Different places should have different information habits.

A small settlement may rely on:

- one public board;
- a transport office;
- word of mouth;
- a clinic notice desk.

A large city may support:

- competing newspapers;
- broadcasters;
- specialized research feeds;
- event channels;
- faction publications;
- public-data terminals.

This gives settlements cultural identity without requiring every region to use the same technology stack.

## 16. Information overload guardrail

The world can generate far more news than the player should read.

Use salience filtering.

A player-facing digest should prioritize:

- direct consequences of player actions;
- current region;
- active quests/cases;
- known factions;
- disrupted travel/services;
- crisis alerts;
- followed institutions/people;
- important corrections;
- major world events.

Low-salience updates can remain archived and searchable.

## 17. Multiplayer privacy

Not all packets are global.

Visibility levels can include:

- PUBLIC
- COMMUNITY
- INSTITUTION
- PARTY
- DIRECT
- CASE_RESTRICTED
- PRIVATE

The server must enforce visibility. Client UI must never receive hidden packets and simply hide them cosmetically.

## 18. Minecraft translation

Possible overworld manifestations:

- changing bulletin-board text;
- radio/TV terminal interaction;
- device inbox UI;
- public-address messages;
- newspaper stand or archive;
- reporter NPCs at major events;
- damaged relay structures;
- temporary emergency signage;
- courier NPCs;
- institutional dispatch desks.

Minecraft presents information. Server-owned world state decides what exists, who can access it and which version is current.

## 19. Battle integration boundary

Most communication content requires no battle mechanics.

When an information-focused quest enters combat, dependencies must be declared using the permanent capability categories.

Examples:

### Relay Tower Defense

Narrative premise: keep technicians safe long enough to restore regional communications.

FULL version dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING if enemies can shove defenders from work zones
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL for timed repair phases
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if exposed electrical zones or reactions matter
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for objective-aware targeting
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING

REDUCED version:

The technicians remain outside the tactical grid. Players fight a standard legal encounter in a static map. Victory unlocks an overworld repair interaction. No timed repair, escort, electrical hazard or forced-movement rule is simulated.

### Courier Breakthrough

Narrative premise: protect a courier carrying a physical copy of a critical report through a communications blackout.

FULL version depends on complete movement, interception/forced movement, objective-aware AI and adapter/playback support. Those families are currently BLOCKING.

REDUCED version uses a standard encounter at a chokepoint. The courier waits outside combat and continues only after the battle resolves.

### Broadcast Studio Evacuation

Narrative premise: clear a safe route from a damaged studio during a regional emergency.

FULL version may depend on hazards/zones/reactions, lifecycle and objective-aware AI.

REDUCED version separates exploration/evacuation checks from one static legal combat encounter.

## 20. PTU/Caelo guardrails

This layer does not create:

- new communication Moves;
- telepathy rules;
- radio ranges from Pokémon abilities;
- device bonuses;
- hacking Skill checks;
- interception actions;
- signal-jamming combat effects;
- communication-based initiative bonuses;
- free Trainer Features;
- automatic Fame or Reputation gains.

If a concept invokes Aura Pulse, telepathy, electrical capabilities, a Trainer Feature, a Skill check or another PTU mechanic, the exact effect must be validated from PTU/Caelo and supported by the current engine before implementation.

## 21. Integration with existing layers

Public Memory stores what communities remember.

World Agency stores what actors know and how factions act.

Case/Authority stores evidence, claims and responsibility.

Crisis stores hazards, forecasts and response state.

Travel stores route/service state.

Media/Communications stores how information about those systems travels.

The intended flow is:

```text
world fact
→ observation/evidence
→ information packet
→ publication or message
→ channel/coverage/delivery
→ actor receives claim
→ actor belief/public memory may change
```

No step may silently skip directly from world truth to universal knowledge.

## 22. Promotion gate

Before any specific media institution or device becomes canon, review:

1. technology level and regional fit;
2. ownership/operator;
3. coverage and infrastructure;
4. privacy/access rules;
5. relationship to public memory and faction influence;
6. Minecraft presentation feasibility;
7. any PTU/Caelo mechanical assumptions;
8. whether the concept relies on currently BLOCKING engine capability families.
