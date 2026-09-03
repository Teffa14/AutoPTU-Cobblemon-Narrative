# Observation, evidence and NPC knowledge contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Pass: 240
Canon effect: NONE unless an input record references existing approved canon

## Purpose

Provide a persistent epistemic layer between Ouros ecological truth and what a player or NPC can legitimately know.

The contract must support field research, repeated sightings, testimony, rumor, stale information and contradictory evidence without exposing hidden population state or allowing Minecraft presentation to create facts.

## Authority boundary

Authoritative ecological truth remains in Ouros persistent world state.

AutoPTU owns structured tactical results after explicit handoff.

Minecraft/Cobblemon supplies observable presentation events only. Entity existence, entity UUID, despawn, unload, vanilla damage and animation state do not become ecological facts by themselves.

Knowledge records are representations of evidence and belief. They do not mutate population truth.

## Pipeline

```text
world truth
-> observable projection/event
-> observation capture
-> evidence record
-> claim/inference
-> knowledge-holder state
-> optional corroboration/contradiction/revision
```

Never permit:

```text
observation -> population mutation
rumor -> canon truth
Minecraft UUID -> persistent identity proof
no sighting -> population absence
newer report -> automatic overwrite
```

## ObservationRecord

Required fields:

```text
observation_id
observer_id
observed_at
location_ref
modality
observable_payload
evidence_quality
source_event_ref nullable
subject_resolution
subject_ref nullable
projection_correlation_ref nullable
```

`projection_correlation_ref` is internal-only and temporary. It may help reconcile an observation with a lease from Pass 239 but is never evidence shown to a player/NPC.

`observable_payload` may contain only presentation-accessible facts such as visible count, apparent species/form, direction, behavior, vocalization, trace type, visible condition, location and time.

## Evidence modalities

`DIRECT_VISUAL`
`DIRECT_AURAL`
`TRACK`
`REMAINS_OR_TRACE`
`INSTRUMENT`
`FIRSTHAND_TESTIMONY`
`SECONDHAND_REPORT`
`AUTHORIZED_RECORD`
`AUTOPTU_SEMANTIC_RESULT`

Each modality may define different false-positive, false-negative, freshness and interpretation profiles. Those profiles are world/rules data, not hidden tactical simulation.

## Claims

A claim is an interpretation of one or more evidence records.

Required fields:

```text
claim_id
holder_id
claim_type
claim_payload
evidence_refs
source_chain
created_at
last_supported_at
state
confidence_band
freshness_band
conflict_refs
```

Recommended claim types:

`PRESENCE`
`OBSERVED_MINIMUM_COUNT`
`IDENTITY_MATCH`
`BEHAVIOR_PATTERN`
`ROUTE_USE`
`HABITAT_USE`
`RESOURCE_USE`
`NESTING_OR_CARE`
`CONDITION`
`THREAT_OR_DISTURBANCE`
`RECENT_BATTLE_OUTCOME`

A `PRESENCE` claim cannot imply abundance. An `OBSERVED_MINIMUM_COUNT` is a lower bound for that observation window only.

## Claim state

`OBSERVED`: direct evidence supports the narrow claim.
`SUPPORTED`: multiple independent or high-quality sources support it.
`SUSPECTED`: plausible but insufficiently supported.
`DISPUTED`: material evidence conflicts.
`STALE`: once-supported information is too old for the configured question.
`RETRACTED`: holder has explicit evidence that the prior interpretation should no longer be used.

State is epistemic. `SUPPORTED` does not mean the claim is secretly guaranteed true.

## Confidence and freshness

Use coarse bands rather than fake precision by default:

Confidence: `LOW`, `MEDIUM`, `HIGH`.
Freshness: `CURRENT`, `AGING`, `STALE`.

Confidence changes because of evidence quality, independence, corroboration, contradictions and observer competence when an adopted rules profile exposes that information.

Freshness changes with time relative to claim type. A terrain landmark may remain useful longer than a report about a migrating cohort.

## Source chains and rumor

A copied report must append a relay node instead of replacing provenance.

```text
original observer -> first recipient -> relay -> current holder
```

Relaying alone must never increase confidence. Independent corroboration may.

The system must distinguish two NPCs repeating the same original rumor from two independent observations. Shared provenance therefore prevents false corroboration.

## Contradictions

Conflicting claims coexist.

Example:

```text
A: DIRECT_AURAL -> species likely present near creek at dusk
B: DIRECT_VISUAL -> no matching actor observed during one later survey
```

B does not automatically falsify A because detection is imperfect and observation windows differ.

A stronger contradiction can set both claims or their inference to `DISPUTED` until new evidence resolves the question.

## Subject resolution and Pass 239

Allowed resolution states:

`KNOWN_PERSISTENT`
`PROBABLE_MATCH`
`UNRESOLVED_LOCAL_MEMBER`
`UNKNOWN_EXTERNAL`

A direct projection lease may let the world service internally know which persistent member produced an observation. The observer receives only evidence they could perceive.

Persistent identity recognition requires observable evidence such as repeated distinctive markings, documented behavior, tagging/authorized identification or other rules-supported cues. Never expose a Minecraft UUID, lease ID or hidden persistent ID as diegetic proof.

Promotion of an unresolved population member to a persistent individual remains governed by Pass 239 and must conserve population total.

## NPC knowledge

Each NPC/organization owns its own knowledge view. There is no global synchronized rumor table masquerading as cognition.

Knowledge-holder stance:

`KNOWS_FROM_EVIDENCE`
`BELIEVES`
`SUSPECTS`
`HEARD`
`DISPUTES`
`UNKNOWN`

Organizations may have shared records, but access must be explicit. An NPC can know an institutional report without personally observing the event.

NPC dialogue and quest availability should query the holder's knowledge view, not hidden world truth.

## PTU/Caelo/Kairos seam

PTU Perception, Survival and Education skills can affect acquisition or interpretation when the active Ouros rules profile calls for a check. This contract does not invent replacement checks or fixed DCs.

Caelo/Kairos procedures may propose research services, archives, factions or downtime interactions, but campaign-specific rules activate only through explicit Ouros adoption.

## AutoPTU handoff

Ambient research requires no battle engine.

If observation crosses into structured conflict:

1. Ouros freezes/records the relevant projection/evidence context.
2. Explicit combatants enter AutoPTU.
3. AutoPTU resolves authoritative tactical events.
4. Only semantic outcomes returned from AutoPTU can become `AUTOPTU_SEMANTIC_RESULT` evidence.
5. Ecology and knowledge are then updated through declared world-state consequences.

A KO can support `RECENT_BATTLE_OUTCOME: KO`. It cannot support `DEATH` without an explicit authoritative semantic outcome defined by the rules profile.

## Capability dependency map

Reduced field-research version:

- targeting/footprints/range/LoS: not required unless a structured tactical check begins;
- base movement legality: not required for evidence storage;
- complete movement: not required;
- core calculations: not required beyond any adopted skill-check resolver;
- action economy/initiative: not required;
- full turn/round lifecycle: not required;
- full stateful damage pipeline: not required;
- status lifecycle: not required;
- terrain/weather/hazards/zones/reactions: ecology context may reference weather/terrain, but no tactical family is required merely to record it;
- move-specific behavior: not required;
- abilities: not required;
- items: only if an adopted observation tool mechanically changes a check;
- Trainer Features/perks: only if an adopted Feature changes observation/interpretation;
- AI legal-action infrastructure: not required;
- AI tactical policy: not required;
- Minecraft/Cobblemon/Craftics adapter/playback: required for automatic capture of visible overworld observations; PARTIAL/BLOCKING end-to-end until proven.

Rich pursuit/field encounter version may additionally require:

- targeting/footprints/range/LoS for visibility and legal targeting;
- base movement legality;
- complete movement for interception, forced movement or pursuit boundaries;
- action economy/initiative and full turn/round lifecycle for timed rounds;
- terrain/weather/hazards/zones/reactions for fog, storms, dangerous ground or reactionary zones;
- move-specific behavior, abilities, items and Trainer Features only when the encounter explicitly uses them;
- AI legal-action infrastructure plus AI tactical policy for wildlife that chooses hide/flee/regroup/guard objectives;
- adapter/playback to present the authoritative result.

## Invariants

1. Evidence records never directly alter abundance.
2. No sighting cannot prove absence by itself.
3. One sighting cannot reveal total population size.
4. Relayed reports preserve source ancestry.
5. Duplicate relays of one source are not independent corroboration.
6. Contradictions are retained.
7. Staleness never rewrites historical evidence.
8. NPC knowledge updates only through evidence, communication or authorized records available to that NPC.
9. Minecraft UUIDs are not diegetic identity.
10. AutoPTU semantic outcomes are the only tactical results eligible to enter the evidence layer as authoritative battle evidence.

## Status

This contract is PROPOSED. It defines implementation behavior but creates no new canon NPC, species, population value, PTU rule adoption or Marea geography.