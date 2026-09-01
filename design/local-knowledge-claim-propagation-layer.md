# Ouros Local Knowledge & Claim Propagation Layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01
Research basis: `research/2026-09-01-local-knowledge-rumor-revision-scan-174.md`

Purpose: define the missing pre-publication and actor-to-actor knowledge behavior between existing Ouros evidence/claim state and the existing Media, Communications & Information layer.

This file does not introduce a second information packet, publication, delivery, evidence or public-memory system.

Existing ownership remains:
- evidence, incidents, claims and hypotheses: existing investigation/case/world-agency layers;
- `information_packet`, publication, communication channels, coverage, delivery receipts and correction history: `design/media-communications-information-layer.md`;
- public historical persistence: existing public-memory layer;
- quest posting: existing mission/service-dispatch layers.

This layer owns only:
1. how an actor forms an interpretation from observations already available to that actor;
2. the actor's current posture toward an existing `claim_id`;
3. which existing social/institutional edge permits that actor to hand the claim into an information packet or direct interaction;
4. how receiving corroboration or contradiction changes that posture without mutating world truth.

## Core model

`WORLD FACT`
`-> OBSERVATION/EVIDENCE`
`-> EXISTING CLAIM_ID`
`-> ACTOR CLAIM POSTURE`
`-> EXISTING INFORMATION_PACKET OR DIRECT INTERACTION`
`-> EXISTING DELIVERY/PUBLICATION`
`-> RECIPIENT CLAIM POSTURE`
`-> ACTION / POSTING / NON-ACTION`
`-> CORROBORATION / CONTRADICTION`
`-> NEW OR REVISED CLAIM_ID`
`-> EXISTING REVISION/PUBLIC-MEMORY HISTORY`

The world fact may remain unknown to all actors.

## Actor claim posture

A lightweight record attaches an actor to an existing claim without copying the claim itself.

```yaml
actor_claim_posture:
  actor_id: null
  claim_id: null
  knowledge_state: HEARD_UNASSESSED
  basis_event_ids: []
  obtained_via_info_id: null
  obtained_via_actor_id: null
  assessed_at: null
  confidence_band: null
  reason_codes: []
  shareability: null
  superseded_by_claim_id: null
```

Suggested `knowledge_state` values:
- `UNHEARD`
- `HEARD_UNASSESSED`
- `CREDIBLE`
- `DOUBTED`
- `CONTRADICTED`
- `CORROBORATED`
- `SUPERSEDED`

Suggested reason codes:
- `FIRSTHAND_OBSERVATION`
- `TRUSTED_PROFESSIONAL_SOURCE`
- `INSTITUTIONAL_NOTICE`
- `REPEATED_INDEPENDENT_REPORTS`
- `DIRECT_EVIDENCE_CONTRADICTION`
- `SOURCE_CORRECTION`
- `UNRESOLVED_DISAGREEMENT`

This is information posture, not a numeric simulation of belief or private psychology.

## Observation vs interpretation

Observation and interpretation must remain separate existing records.

Example:
Mina sees loose stone on the lower crossing at 07:20.

A claim may interpret that observation as evidence that the route is becoming unsafe.

A later survey may show that the loose stone is old and stable while a different upper shelf is the actual problem. Mina's observation remains valid. The earlier interpretation can be superseded.

## Local transmission eligibility

Claims do not teleport globally.

An actor can pass a known claim into an existing `information_packet` or direct interaction only through a plausible edge already supported by the world graph.

Eligible edge classes can include:
- household/co-residence;
- workplace;
- institutional reporting chain;
- archive circulation;
- market/vendor relationship;
- ferry/service route;
- mentoring relationship;
- direct player conversation;
- publication/broadcast channel;
- dispatch board;
- recurring public event.

The actual transmission uses the existing communications layer. This file only answers whether the sender plausibly has the claim and a route to share it.

No numeric rumor-spread probability is required for the first implementation. Deterministic, auditable propagation is preferable.

## Corrections and revision

Corrections use existing new claims plus the existing information revision/history machinery.

Example:
- `C-104`: seasonal crossing unsafe after rain.
- `C-118`: lower crossing stable; upper shelf has fresh slippage; supersedes `C-104`.

Effects:
- actors who receive `C-118` can move their posture on `C-104` to `SUPERSEDED`;
- an old notice can be replaced through the existing publication system;
- earlier actions taken because of `C-104` stay in history;
- actors who never receive `C-118` may still act on old information.

A correction never rewrites `world_truth` merely by being published.

## Rumor creation rule

Do not generate a rumor because a rumor slot is empty.

A public rumor must originate from at least one existing claim known to an actor plus an actual transmission/publication event. The `NPC_GOSSIP` channel already exists in the communications design; this layer supplies the actor-knowledge eligibility behind it.

Generated wording must not silently upgrade:
- `someone saw an agitated Pokémon` into `this species is aggressive`;
- `a route worker heard a cry` into `a Legendary appeared`;
- `two deliveries were smaller` into `someone is stealing shipments`;
- `an NPC missed a shift` into `the NPC disappeared`;
- `a patient count rose` into a named diagnosis.

## Cultural explanations

Cultural explanations can be claims with provenance without becoming mechanics or canonical causality.

Keep separate:
- observed practice;
- remembered story or tradition;
- actor/community interpretation;
- evidence supporting or weakening a causal assertion;
- current canonical truth, when known.

A causal correction does not automatically invalidate the tradition's cultural meaning or historical importance.

## Wild Pokémon behavior reports

Behavior claims should preserve the evidence scope:
- actual species/individual/collective observed;
- location;
- time;
- visible behavior;
- observer position/distance/context;
- nearby environmental events known to the observer;
- whether eggs, food, shelter, Trainer actions or route works were actually observed.

Do not promote one observation into territoriality, kinship, leadership, hostility or migration cause without additional evidence/canon review.

## Quest and dispatch integration

An existing claim can cause a request only when the issuer:
- has an actionable actor-claim posture;
- has an authored reason or institutional mandate to request help.

Examples:
- Mara may post a route check from a credible warning.
- Nerea may request repeat observation after contradictory measurements.
- Taro may request source retrieval for conflicting historical accounts.
- Ivo may request delivery reconciliation for mismatched lot records.

The request should retain triggering `claim_id` references.

If the claim is superseded, existing dispatch/quest systems may update, retire or replace the request with an explicit world-state reason.

## Relationship integration

Relationship state may affect sharing access, never truth.

Allowed:
- a trusted player receives a sensitive-but-shareable warning earlier;
- a strained contact provides only the public information packet;
- a mentor introduces the player to another source.

Disallowed:
- relationship score makes a false claim true;
- low relationship makes evidence mechanically weaker;
- inferred affection automatically reveals private facts.

## Archive and public-memory integration

Tideglass or another archive can preserve existing records for:
- the original claim/report;
- later correction;
- publication versions;
- action taken because of each version.

The local-knowledge layer supplies which actors knew each version and when. The archive/public-memory layers own storage and history.

## Implementation-facing invariants

1. `WORLD_TRUTH != ACTOR_KNOWLEDGE`.
2. `OBSERVATION != INTERPRETATION`.
3. `PUBLIC_RUMOR != CANONICAL_FACT`.
4. `CORRECTION != HISTORY_DELETION`.
5. `CULTURAL_MEANING != VERIFIED_CAUSALITY`.
6. `WILD_BEHAVIOR_REPORT != SPECIES_TRAIT`.
7. `GLOBAL_SIMULATION_KNOWS != NPC_KNOWS`.
8. `QUEST_POSTED` requires an actor/institutional knowledge path.
9. Player-private data cannot enter NPC knowledge without an explicit observation or communication event.
10. `actor_claim_posture` references existing claim IDs; it never duplicates or replaces the authoritative claim object.

## Mechanically rich encounter contract

Candidate pattern: a route warning becomes an encounter with a protective wild group while survey markers must be inspected.

Full intended version may require:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement, especially interception/forced movement if retreat corridors are tactical;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if selected Moves use it;
- terrain/weather/hazards/zones/reactions if unstable shelves or weather alter combat;
- exact move-specific behavior;
- exact abilities;
- exact items;
- exact Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Current conservative readiness:
- VERIFIED for covered contracts: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative, AI legal-action infrastructure.
- PARTIAL: complete movement, full lifecycle, damage pipeline, status lifecycle, move-specific behavior, abilities, items, Trainer Features/perks.
- BLOCKING as complete families: terrain/weather/hazards/zones/reactions, AI tactical policy, Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:
Route inspection occurs outside combat. An independent ordinary battle may be compiled only after exact participants and mechanics pass current parity audit. No escort unit, moving civilian, unstable-terrain combat rule, weather modifier or reaction objective is included. Battle outcome can unlock continued observation but cannot establish ecological causality by itself.

## Data-driven validation targets

Future CI/startup validation should reject:
- actor postures referencing missing claim IDs;
- actor IDs that do not exist;
- impossible supersession loops;
- quest postings whose issuer never acquired the triggering claim;
- private claims exposed through a public packet without policy allowing it;
- behavior claims promoted to species-wide facts without explicit canon review.

## Promotion boundary

This architecture can be implemented without canonizing any specific rumor, mystery or causal explanation. Individual claims and events remain proposal/canon decisions.