# Temporal Continuity, Time Travel & Causal History Layer — Pass 54

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already has calendar time, historical records, public memory, anomalous spaces, archives and persistent entities. This layer adds an opt-in contract for genuinely temporal phenomena: observation of another time, physical crossing into another historical frame, bounded loops, possible futures and canon-approved causal intervention.

The default remains ordinary linear history. Nothing in this layer makes time travel common, available to players, or mechanically legal.

## Relationship to existing systems

This layer extends:

- `ouros-narrative-architecture.md` for Chronicle and persistent world state;
- `anomalous-spaces-dimensional-exploration-layer.md` for portal/space boundaries;
- `seasonality-calendar-phenology-layer.md` for ordinary time;
- `public-memory-event-legacy-layer.md` for remembered history;
- `archives-museums-collections-preservation-layer.md` for historical records;
- `science-research-discovery-layer.md` for hypotheses and evidence;
- `media-communications-information-layer.md` for information propagation;
- `digital-systems-cyberspace-data-layer.md` for versioned data and logs;
- `evolution-life-stage-transformation-layer.md` for one Pokémon changing through time;
- `encounter-implementation-contracts.md` for tactical dependency declarations.

Pass 50's rule remains active: strange clocks, altered duration, portals or non-Euclidean spaces do not prove time travel. This layer activates only when an authored/canon-reviewed phenomenon is explicitly temporal.

## Core separation

Never collapse these concepts:

```text
canonical event history
        ↓
historical state version
        ↓
temporal observation or claim
        ↓
actor knowledge
        ↓
physical temporal crossing, if real
        ↓
intervention attempt
        ↓
validated causal delta
        ↓
branch/version decision
        ↓
new world state
        ↓
records and public memory propagate later
```

Seeing a possible future does not make it inevitable.

Visiting the past does not automatically rewrite the present.

Remembering another temporal context does not make the actor omniscient.

## Canonical history policy

The Chronicle is append-only.

Never delete an old Chronicle event because later content changes what happens afterward.

If canon permits divergent history, store the source history and the divergence relation.

Recommended default:

- one PRIMARY timeline/context;
- historical versions are immutable records of what was authoritative at a given effective time;
- possible futures are projections/observations, not canonical future facts;
- alternate branches exist only through explicit canon action;
- branches do not merge automatically;
- a correction to historical knowledge does not erase the original record that people once believed.

## Temporal context

```yaml
temporal_context:
  temporal_context_id: null
  context_kind: PRIMARY | HISTORICAL_VIEW | POSSIBLE_FUTURE | DIVERGENT_BRANCH | LOOP_DOMAIN
  parent_context_id: null
  divergence_event_id: null
  canon_status: proposed
  effective_from: null
  effective_to: null
  world_state_version_ref: null
  source_provenance_refs: []
```

`HISTORICAL_VIEW` may describe the actual earlier state of the primary history without creating a branch.

`POSSIBLE_FUTURE` is not canonical until events actually produce it.

`DIVERGENT_BRANCH` requires human/canon approval.

## Historical state version

```yaml
historical_state_version:
  state_version_id: null
  temporal_context_id: null
  effective_at: null
  predecessor_version_id: null
  causal_event_ids: []
  entity_state_refs: []
  location_state_refs: []
  institution_state_refs: []
  ecology_state_refs: []
  unresolved_claim_refs: []
  immutable: true
```

This is a semantic state version, not a full Minecraft world backup.

Do not copy every block, NPC or inventory merely to represent a historical frame.

## Temporal anomaly

```yaml
temporal_anomaly:
  temporal_anomaly_id: null
  anchor_location_id: null
  observation_kind: TIME_OFFSET | VISION | WINDOW | CROSSING | LOOP | UNKNOWN
  observed_direction: PAST | FUTURE | CYCLIC | UNKNOWN
  stability: STABLE | INTERMITTENT | TRANSIENT | UNKNOWN
  evidence_refs: []
  causal_hypothesis_refs: []
  access_policy_ref: null
  mechanics_review_required: true
```

An anomaly can be verified as temporal while its cause remains unknown.

## Temporal observation

```yaml
temporal_observation:
  observation_id: null
  observer_ids: []
  source_temporal_context_id: null
  apparent_target_time: null
  observation_medium: DIRECT | VISION | RECORD | SENSOR | OTHER
  observed_claim_refs: []
  certainty: UNKNOWN | LOW | MEDIUM | HIGH | VERIFIED_WITHIN_CONTEXT
  current_timeline_validation: UNTESTED | CONTRADICTED | CONSISTENT | CONFIRMED
  provenance_refs: []
```

A future vision should normally start as `UNTESTED`.

Even a perfectly authentic future record can describe a possible future that current interventions later prevent.

## Temporal crossing

```yaml
temporal_crossing:
  crossing_id: null
  traveler_actor_ids: []
  pokemon_entity_ids: []
  item_instance_ids: []
  departure_context_id: null
  departure_time: null
  arrival_context_id: null
  arrival_time: null
  return_state: UNKNOWN | OPEN | CLOSED | RETURNED
  return_crossing_id: null
  witness_refs: []
  authorized_by_ref: null
  mechanics_resolution_ref: null
```

Persistent entities retain identity across the crossing unless canon explicitly creates a distinct branch copy.

## Temporal entity lineage

Temporal stories can create ambiguity when the same entity exists at different ages or in different branches.

```yaml
temporal_entity_lineage:
  persistent_entity_id: null
  temporal_context_id: null
  valid_time_range: null
  state_snapshot_ref: null
  branch_entity_id: null
  identity_relation: SAME_ENTITY | BRANCH_DERIVATION | UNKNOWN
  simultaneous_instantiation_policy: DENY | AUTHORED_ONLY | ALLOW
```

Default behavior:

- same timeline + same entity + two ages should not be simultaneously instantiated unless an authored temporal scenario explicitly handles it;
- branch versions are separate branch entities only after explicit divergence;
- Minecraft spawning two visually identical actors never proves they are temporal duplicates.

## Actor knowledge across time

```yaml
temporal_knowledge_record:
  actor_id: null
  claim_id: null
  learned_in_context_id: null
  learned_at: null
  source_ref: null
  applicable_context_ids: []
  validation_state: UNTESTED | STALE | CONTRADICTED | CONFIRMED
  privacy: PRIVATE | SHARED | PUBLIC
```

This prevents future knowledge from becoming global server knowledge.

Example:

A traveler sees that a bridge is destroyed in one possible future.

Valid state:

`actor knows: bridge destroyed in observed possible future`.

Invalid automatic state:

`bridge will definitely be destroyed`.

## Causal claims

```yaml
causal_claim:
  causal_claim_id: null
  proposed_cause_event_ids: []
  proposed_effect_event_ids: []
  temporal_context_id: null
  evidence_refs: []
  status: HYPOTHESIS | SUPPORTED | VERIFIED | DISPROVEN | UNKNOWN
  authored_rule_ref: null
```

Temporal sequence alone does not prove causation.

The system should remain able to discover that an event thought to cause a future state was merely correlated with it.

## Intervention record

```yaml
temporal_intervention:
  intervention_id: null
  actor_ids: []
  target_context_id: null
  target_event_or_state_refs: []
  intended_change: null
  attempted_at: null
  mechanics_resolution_ref: null
  resulting_delta_ref: null
  canon_review_state: REQUIRED
  branch_policy: UNRESOLVED | NO_BRANCH | CREATE_BRANCH | AUTHORED_OVERRIDE
```

Narrative generation may propose interventions. It cannot approve their causal consequences by itself.

## Validated causal delta

```yaml
temporal_state_delta:
  delta_id: null
  base_state_version_id: null
  changed_fact_refs: []
  created_entity_refs: []
  removed_from_active_state_refs: []
  preserved_history_refs: []
  downstream_dependency_refs: []
  feasibility_state: UNKNOWN | FAILED | VERIFIED
  canon_approval_ref: null
```

A delta never deletes provenance.

If a building no longer gets destroyed in a branch, the source branch still preserves the event where it was destroyed.

## Loop domain

A time loop must reset an explicit bounded domain.

```yaml
temporal_loop:
  loop_id: null
  temporal_context_id: null
  reset_anchor_time: null
  exit_condition_ref: null
  iteration: 0
  reset_scope_refs: []
  retained_state_refs: []
  retained_actor_knowledge_policy: null
  unique_reward_policy: IDEMPOTENT
  persistent_entity_policy: null
  max_safe_iterations: null
  mechanics_review_required: true
```

Never implement a loop as a full-server rollback.

Possible reset scope:

- one dungeon instance;
- one building;
- one local event;
- one authored quest pocket.

Normally excluded from reset:

- account ownership;
- unrelated world state;
- other players' private history;
- canonical external events;
- server moderation/audit logs.

## Loop anti-exploit policy

Every unique reward/object needs an idempotent claim key.

```yaml
loop_reward_claim:
  loop_id: null
  reward_identity_ref: null
  beneficiary_ref: null
  first_claim_iteration: null
  claim_state: CLAIMED
```

Repeated loops cannot create unlimited copies of:

- unique items;
- Pokémon individuals;
- rare research samples;
- currency rewards;
- institutional credentials;
- permanent progression.

If a loop intentionally produces duplicates, that requires authored canon plus explicit identity semantics.

## Memory and reset

Do not assume everyone forgets or remembers.

For each loop or branch event, define:

- which actors retain memory;
- whether records survive;
- whether cameras/logs survive;
- whether Pokémon retain observed behavior/history;
- whether items retain wear/provenance;
- whether public memory exists outside the reset domain.

PC private thoughts and emotions remain player-owned even when memory persists.

## Historical records from non-current timelines

An artifact carried from another temporal context should preserve provenance.

```yaml
temporal_record_provenance:
  record_or_item_id: null
  source_context_id: null
  source_time: null
  crossing_id: null
  current_context_id: null
  authenticity_state: null
  applicability_to_current_history: UNKNOWN | PARTIAL | NONE | VERIFIED
```

A future newspaper can be authentic to its source context while wrong about the current future.

## Public memory and retcons

If history branches, existing actors do not automatically gain rewritten memories.

Possible policies must be authored:

- travelers retain source-context memories;
- destination inhabitants only know their local history;
- selected supernatural actors remember both;
- records carried across contexts preserve their source history;
- public memory changes only when information propagates.

The generator may not invent a universal memory rewrite.

## Retired PC protection

Temporal content cannot use a retired PC as a free future/past NPC.

Without explicit player-authored canon, do not decide:

- that the PC died in another future;
- married or had children;
- joined a faction;
- became Champion;
- lost their Pokémon;
- regretted a decision;
- appears as an alternate villain;
- gives an item to their younger self.

Use records, anonymous institutional consequences or authored descendants only when established.

## Pokémon identity protection

A Pokémon crossing time remains the same `pokemon_entity_id` by default.

Do not infer:

- changed Loyalty;
- changed ownership;
- healing from time travel;
- de-aging;
- altered Moves/Abilities;
- evolution reversal;
- resurrection;
- duplicated capture eligibility.

If the Pokémon is observed at a historically earlier life stage, use the authoritative historical state version rather than modifying its current persistent state without an approved temporal transition.

## Evolution interaction

Pass 53 remains authoritative for Evolution architecture.

A current evolved Pokémon visiting an earlier time does not become unevolved merely because its younger self existed then.

A historical observation of that Pokémon before Evolution can use the old species/form from Evolution history.

Changing an earlier Evolution event is a causal intervention and requires explicit review of downstream species/form state, battle history, photos, records, relationships and ecology.

## Legendary and Mythical protection

Temporal anomalies must never automatically escalate to Celebi, Dialga or another Legendary/Mythical cause.

Allowed flow:

```text
anomaly
→ repeated temporal evidence
→ competing causal hypotheses
→ species/Legendary hypothesis if justified
→ human canon approval
→ direct appearance only if approved
```

A PTU campaign seed mentioning Celebi/Dialga is inspiration, not Ouros permission to use them.

## Ordinary prediction versus time travel

Keep separate:

- statistical forecast;
- tactical prediction;
- psychic vision;
- delayed attack;
- archived future simulation;
- direct temporal observation;
- physical time travel.

A tactical AI predicting an opponent's action is not a temporal mechanic.

## Minecraft representation

Minecraft may present:

- a historical instance of a location;
- changed architecture/vegetation;
- temporal particles/audio;
- a bounded loop instance;
- a portal/window;
- an NPC/Pokémon historical state;
- records from another context.

Minecraft must not independently decide:

- whether history changed;
- which memories survive;
- whether an item duplicates;
- whether HP/status rewinds;
- whether a battle turn repeats;
- whether a Legendary caused an anomaly;
- whether a future is inevitable.

## Temporal writeback protocol

Any mechanically meaningful temporal event should produce ordered outputs:

1. authoritative action/result reference;
2. source temporal context;
3. travelers/entities affected;
4. crossing or observation event;
5. knowledge changes;
6. proposed causal delta if intervention occurred;
7. canon/feasibility decision;
8. new state version or branch if approved;
9. downstream world-state invalidation/recalculation;
10. public-record propagation through ordinary communication systems.

## Encounter contract A — Clocktower Echo

Premise: a local five-minute interval repeats around a damaged clocktower while the surrounding town continues normally.

REDUCED version:

Treat each loop attempt as a separate static encounter instance. Reset only the authored local world-state objects between attempts. Explicitly retained clues remain in player knowledge. Battle rewards are idempotent. No battle turn rewinds in place.

FULL version:

The tactical encounter itself can rewind to a checkpoint while selected actor knowledge persists.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if positioning must rewind across forced effects;
- core calculations — VERIFIED primitives;
- action economy/initiative — VERIFIED baseline;
- full turn/round lifecycle — PARTIAL and required for checkpoint timing;
- full stateful damage pipeline — PARTIAL and required for exact restoration;
- status lifecycle — PARTIAL and required for reset semantics;
- terrain/weather/hazards/zones/reactions — BLOCKING if loop state includes dynamic zones/hazards;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED baseline;
- AI tactical policy — BLOCKING if opponents learn/adapt between iterations;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- dedicated authoritative battle rewind/snapshot contract — BLOCKING/unverified;
- authoritative RNG replay policy — BLOCKING/unverified for rewound turns.

## Encounter contract B — Warning From Tomorrow

Premise: players receive a provenance-valid record from a possible future showing a facility in crisis. They can investigate current causes before the predicted time.

REDUCED version:

The future record is a claim. Players investigate in ordinary overworld state. If a battle occurs, use a normal static encounter. Current actions may later make the forecast consistent, contradicted or irrelevant.

FULL version:

The system can maintain a simulated/alternate future state and compare causal interventions in real time.

Dependencies for battle content remain the normal encounter requirements. Additional temporal world-model dependency: versioned future-state projection and causal-delta validation — BLOCKING/unimplemented as an authoritative game contract.

This concept does not require literal physical time travel.

## Encounter contract C — Threshold Pursuit

Premise: an actor attempts to escape through a verified temporal crossing during a confrontation.

REDUCED version:

Resolve the crossing before or after the tactical battle. The combat grid contains only actors currently in one temporal context.

FULL version:

Actors can cross the temporal boundary during battle and continue in another temporal context.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED baseline;
- complete movement/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED baseline;
- lifecycle — PARTIAL;
- damage/status/moves/abilities/items/Features — respective PARTIAL families if used;
- terrain/weather/hazards/zones/reactions — BLOCKING for a live portal zone;
- AI legal actions — VERIFIED baseline;
- tactical AI — BLOCKING for escape/chase objectives;
- adapter/playback — BLOCKING;
- temporal combatant transfer contract — BLOCKING/unverified.

## Encounter contract D — Archive From Tomorrow

Premise: an archive acquires a document that appears to have a future date and describes several events that have not occurred.

This can remain entirely non-combat.

Required systems:

- archives/provenance;
- temporal observation/record provenance;
- actor knowledge;
- scientific/case investigation;
- future-claim validation over time;
- public-information policy.

No battle implementation is needed unless a separate conflict emerges.

## Engine boundary

AutoPTU-Java does not currently prove:

- temporal crossing;
- battle rewind;
- checkpoint restore;
- RNG rewind/replay policy;
- branch simulation;
- simultaneous time-context combatants;
- temporal clone identity;
- causal world-state rewriting.

The newest RNG-ready post-damage hooks are useful battle infrastructure only. They do not authorize temporal mechanics.

## Canon promotion gate

Before any temporal mechanic becomes canon, review:

- exact PTU/Caelo source support;
- whether the phenomenon is unique, rare or systematic;
- cause and access policy;
- temporal-context model;
- entity identity semantics;
- player/retired-PC agency;
- item/reward duplication policy;
- memory policy;
- causal branch policy;
- Minecraft feasibility;
- battle dependencies when relevant.

## Open questions

- Does Ouros ever permit physical time travel, or only visions/records/anomalies?
- If branches exist, are they explorable persistent worlds or historical bookkeeping only?
- Can a player return to the same past more than once?
- Can two versions of one persistent Pokémon coexist physically?
- What exact PTU/Caelo mechanics govern Celebi, Dialga, Future Sight and temporal powers?
- Does the project want deterministic loops, RNG-preserving loops or fresh-RNG retries?
- Can a time loop include a battle, or should battle remain outside the reset boundary initially?
- How should multiplayer parties behave when members occupy different temporal contexts?
- What world systems must be recomputed after a causal divergence?
- Which temporal phenomena, if any, can advance while players are offline?
