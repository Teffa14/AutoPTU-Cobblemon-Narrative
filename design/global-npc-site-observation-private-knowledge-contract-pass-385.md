# Global NPC site observation to private knowledge contract — Pass 385

Status: PROPOSED IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-09

## Purpose

Pass 384 created `OUROS_SITE_EVIDENCE_LEDGER_V1`, which owns durable physical site revisions, observations and interpretations. Existing global-NPC memory owns private claims. Pass 385 connects those owners through the smallest admissible bridge for direct observation.

Schema: `OUROS_SITE_OBSERVATION_KNOWLEDGE_V1`.

Owner: `tools/global_npc_site_observation_knowledge.py`.

## Preserved authority boundaries

`WORLD_OBSERVATION != UNIVERSAL_PRIVATE_KNOWLEDGE`

`DIRECT_OBSERVER != INSTITUTIONAL_PEER`

`OBSERVATION_CONTENT != INTERPRETATION`

`CURRENT_SITE_STATE != PRIVATE_HISTORICAL_CLAIM`

A site observation may materialize only into the private ledger of the actor recorded as its observer. Faction membership, employment, proximity, later site access or database visibility do not create knowledge.

## Materialization rule

For one source observation, the bridge derives deterministic IDs for the materialization record, private claim and observation subject.

The private claim copies only the source observation content and provenance root. It is recorded as `DIRECT_OBSERVATION`, with the observer as source agent and the same semantic minute as the world observation.

The claim's confidence is 100 because the proposition being stored is the actor's own direct observation record. This does not make any interpretation of that observation certain and does not promote the observation into global narrative truth beyond the source world-evidence record itself.

## No automatic interpretation materialization

Pass 385 does not copy `SiteInterpretationRecord` entries into private memory. Interpretations already name an actor, but inference materialization needs a separate contract because it must preserve supporting observation lineage and should not be conflated with direct sensory evidence.

## No automatic sharing

After materialization, the claim remains private. Another NPC can receive it only through an already-authorized communication/report/archive path or by making an independent observation.

The bridge therefore cannot be used to bypass recipient resolution, information transport, publication receipt or archive-access rules.

## Replay and validation

The bridge stores only relationship records. It does not duplicate either source owner.

Restore requires the current `SiteEvidenceLedger` and `KnowledgeLedgerStore`. Every materialization must still point to an existing observation, the same observer, site, revision, evidence ref and semantic minute. The corresponding private claim must exist and must exactly preserve source kind, source agent, content, time and provenance root.

A checkpoint time earlier than the observation rejects the materialization as future evidence.

A later physical revision of the site does not rewrite the private claim because the claim describes what the actor observed under the earlier revision.

## PTU/Caelo boundary

This contract records information provenance only. It does not define how difficult an observation was to make.

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes utility classes, Skills/Edges/Features, movement, terrain and encounter construction to supplied PTU/Kairos sources. Any authored observation gated by a particular skill, Feature, item, Move, Ability, terrain state or tactical action must verify that exact rule separately.

## Engine dependency map

Targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts. Relevant only if a tactical scene requires a clue or observer to be visibility-sensitive.

Base movement legality: VERIFIED within audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required only for rich scenes involving collapse displacement, dragging, rescue, forced slides or interception.

Core calculations: VERIFIED within audited deterministic scopes.

Action economy/initiative: VERIFIED for audited primitives. A dedicated observe/document/stabilize action still requires explicit legal-action admission.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. AutoPTU-Java merge #419 proves only seeded Impostor random ability-choice and RNG-stream parity for the pinned oracle scenario.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for documentation-first, protect-evidence, escort, search, rescue-first, stabilization-first, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for stable site/evidence identity, observation acknowledgement, physical revision projection, non-KO objectives and authoritative end-to-end playback.

## Reduced implementation

A reduced investigation can run without AutoPTU. A named NPC travels to a persistent site, records an observation under one site revision and immediately gains the matching private claim. The site may later change. Another NPC does not know the first observation until an explicit information path carries it.

## Deferred work

Interpretation-to-private-inference materialization remains separate.

Archive lookup remains external evidence until a specific claim-materialization path is invoked.

Portable-find possession/custody remains owned by existing resource/evidence-custody systems.

Checkpoint placement remains unresolved. The site ledger and this bridge may belong in a broader persistent-world checkpoint rather than the global-NPC V19 owner.
