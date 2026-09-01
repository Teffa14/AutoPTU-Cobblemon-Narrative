# Ouros Local Knowledge & Claim Propagation Layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01
Research basis: `research/2026-09-01-local-knowledge-rumor-revision-scan-174.md`

Purpose: define how observations, interpretations, rumors, professional hypotheses and corrections move through the persistent Ouros world without granting NPCs omniscience or collapsing belief into canonical truth.

This layer extends the existing investigation, communications, public-memory, relationship and institutional systems. It does not replace them.

## Core model

A local-information event should move through explicit stages:

`WORLD FACT`
`-> OBSERVATION`
`-> SOURCE INTERPRETATION`
`-> CLAIM PACKET`
`-> TRANSMISSION EDGE`
`-> RECIPIENT KNOWLEDGE STATE`
`-> ACTION / POSTING / NON-ACTION`
`-> CORROBORATION / CONTRADICTION`
`-> REVISION`
`-> HISTORICAL MEMORY`

The world fact may remain unknown to all actors.

## Claim packet

Minimum proposed fields:

- `claim_id`
- `subject_ids`
- `source_actor_id`
- `observation_event_ids`
- `source_location_id`
- `observed_at_world_time`
- `interpreted_at_world_time`
- `claim_type`
- `assertion_summary`
- `confidence_band`
- `firsthand_or_received`
- `source_channel_id`
- `evidence_refs`
- `contradiction_refs`
- `supersedes_claim_id`
- `status`

Suggested `claim_type` values:
- `DIRECT_OBSERVATION`
- `INTERPRETATION`
- `PROFESSIONAL_HYPOTHESIS`
- `CULTURAL_EXPLANATION`
- `WARNING`
- `ROUTE_REPORT`
- `SERVICE_REPORT`
- `BEHAVIOR_REPORT`
- `PUBLIC_RUMOR`
- `CORRECTION`

Suggested status values:
- `CURRENT`
- `DISPUTED`
- `PARTIALLY_CORROBORATED`
- `SUPERSEDED`
- `RETRACTED_BY_SOURCE`
- `ARCHIVED`

`SUPERSEDED` never means deleted.

## Observation vs interpretation

Example:

Observation: Mina sees loose stone on the lower crossing at 07:20.

Interpretation: Mina thinks the route is becoming unsafe.

These records must remain distinct. A later survey may show that the loose stone is old and stable while a different upper shelf is the actual problem. Mina's observation stays true even if her interpretation changes.

## Actor knowledge state

Each actor can hold a different state for the same claim:

- `UNHEARD`
- `HEARD_UNASSESSED`
- `CREDIBLE`
- `DOUBTED`
- `CONTRADICTED`
- `CORROBORATED`
- `SUPERSEDED`

The system should not try to simulate private psychology numerically. These values record explicit information posture used for content eligibility.

An actor may also have a reason code:
- firsthand observation;
- trusted professional source;
- institutional notice;
- repeated independent reports;
- contradiction by direct evidence;
- source correction;
- unresolved disagreement.

## Transmission edges

Claims do not teleport globally.

Eligible edges can come from existing world relationships:
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

Each edge may have:
- sender/receiver or channel audience;
- active hours/state;
- information categories normally carried;
- privacy constraints;
- delay;
- traceable delivery event.

No numeric rumor-spread probability is required for the first implementation. Deterministic eligible propagation is easier to audit.

## Corrections and revision

A correction should create a new packet linked to the older one.

Example:

`C-104: seasonal crossing unsafe after rain` — CURRENT

Later:

`C-118: lower crossing is stable; upper shelf has fresh slippage` — CORRECTION, supersedes `C-104`

Effects:
- actors who receive `C-118` update their posture;
- an old notice can be replaced;
- historical state still records that `C-104` influenced earlier behavior;
- actors who never receive `C-118` may still act on old information.

This allows believable asynchronous world state without fabricated misunderstandings.

## Rumor generation rule

Do not generate a rumor merely because a rumor slot is empty.

A public rumor requires at least one source packet plus a transmission event. The generated wording may summarize the claim, but the underlying state must identify what was actually observed and by whom.

Public rumor must never silently upgrade:
- `someone saw an agitated Pokémon` into `this species is aggressive`;
- `a route worker heard a cry` into `a Legendary appeared`;
- `two deliveries were smaller` into `someone is stealing shipments`;
- `an NPC missed a shift` into `the NPC disappeared`;
- `a patient count rose` into a named diagnosis.

## Cultural claims

Cultural explanations deserve their own record type because they can remain meaningful even when not mechanically or historically verified.

Store separately:
- tradition text/summary;
- community or source actor;
- observed practice;
- asserted causal explanation;
- current evidence status;
- whether the tradition itself is disputed.

A scientific correction about causality does not automatically invalidate the practice, memory or identity attached to it.

## Wild Pokémon behavior reports

Behavior reports should include:
- species/individual/collective identity actually observed;
- location;
- time;
- visible behavior;
- distance/context;
- nearby environmental events known to the observer;
- whether eggs, food, shelter, Trainer actions or route works were actually observed.

Do not infer territoriality, kinship, leadership, hostility or migration cause without evidence.

## Quest and dispatch integration

A claim can produce a request only when an actor or institution has both:
- the claim in an actionable posture;
- mandate/reason to ask for help.

Examples:
- Mara can post a route check from a credible warning.
- Nerea can request repeat observations from contradictory measurements.
- Taro can request source retrieval from conflicting historical accounts.
- Ivo can ask for delivery reconciliation from mismatched lot records.

The quest record should reference the claim IDs that caused it.

When those claims are superseded, the quest can:
- update objective text;
- change destination;
- become obsolete with explanation;
- split into a different investigation;
- complete because the original concern is resolved elsewhere.

## Relationship integration

Relationship state may affect whether an actor shares a claim, but it does not alter truth.

Allowed examples:
- a trusted player receives a sensitive-but-shareable warning earlier;
- a strained contact gives only the public version;
- a mentor introduces the player to another source.

Disallowed examples:
- high relationship score makes a false claim true;
- low relationship score makes evidence mechanically weaker;
- hidden affection automatically reveals private facts.

## Archive and public memory integration

Tideglass or another archive may store:
- original report;
- correction;
- later interpretation;
- public notice versions;
- action taken because of the report.

This makes misinformation and correction part of history without rewarding deliberate fabrication.

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
10. A message delivered to one actor does not imply settlement-wide awareness.

## Mechanically rich encounter contract

Candidate pattern: a route warning turns into an encounter with a protective wild group while survey markers must be inspected.

Full intended version may require:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement, especially interception/forced movement if retreat corridors are tactical;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle if status Moves are selected;
- terrain/weather/hazards/zones/reactions if unstable shelves or weather alter combat;
- exact move-specific behavior;
- exact abilities;
- exact items;
- exact Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Current conservative readiness:
- VERIFIED: targeting/footprints/range/LoS, base movement legality, core calculations, action economy/initiative, AI legal-action infrastructure for covered contracts.
- PARTIAL: complete movement, full lifecycle, damage pipeline, status lifecycle, move-specific behavior, abilities, items, Trainer Features/perks.
- BLOCKING as complete families: terrain/weather/hazards/zones/reactions, AI tactical policy, Minecraft/Cobblemon/Craftics adapter/playback.

Reduced version:
The route inspection occurs outside combat. An independently authored ordinary battle may occur only after its exact participants and mechanics pass current parity audit. No escort unit, moving civilian, unstable-terrain combat rule, weather modifier or reaction objective is included. The authoritative battle outcome can unlock access to continue observing, but it cannot determine the ecological explanation by itself.

## Data-driven validation targets

Future CI/startup validation should reject:
- claim source actor IDs that do not exist;
- source locations that do not exist;
- supersession loops;
- evidence references to missing observations;
- quest postings whose issuer never received the triggering claim;
- public notices exposing private claim categories;
- behavior claims that promote species-wide facts without explicit canon review.

## Promotion boundary

This architecture can enter implementation without canonizing any specific rumor, event or causal explanation. Individual claims, traditions, mysteries and outcomes remain proposals until reviewed.