# Site evidence ledger executable contract — Pass 384

Status: PROPOSED IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-09

## Scope

Pass 383 defined archaeological/context continuity. Pass 384 adds the smallest executable owner that can preserve site revisions, observations and interpretations without flattening them into one mutable clue state.

Schema: `OUROS_SITE_EVIDENCE_LEDGER_V1`.

The owner is `tools/global_npc_site_evidence.py`.

## Preserved boundaries

`SITE_REVISION != OBSERVATION`

`OBSERVATION != INTERPRETATION`

`CURRENT_SITE_STATE != HISTORICAL_OBSERVATION`

`REVISED_INTERPRETATION != MUTATED_OBSERVATION`

A later physical revision cannot rewrite what an actor observed under an earlier revision. A later interpretation can supersede a prior interpretation while the underlying observation remains unchanged.

## Revision chain

Each site has one linear physical-state revision chain. The first revision has no parent. Later revisions must point to an existing prior revision for the same site and cannot fork from an already-consumed parent.

This V1 intentionally models one authoritative physical-state history per site. Competing reports about what happened belong in observation/interpretation/provenance, not in parallel physical revision histories.

## Observation contract

An observation must point to one existing site revision, one explicit observer, one evidence ref and one provenance root. Its semantic minute cannot precede the revision it observed.

Observation kinds currently admitted are fixed feature, portable find, spatial relationship, material condition and access state. These are classifications of evidence records, not PTU mechanics.

## Interpretation contract

An interpretation consumes one or more explicit observation IDs from the same site. It cannot consume future observations. Confidence is bounded from 0.0 through 1.0.

Supersession is allowed only for the same actor at the same site and cannot point forward in semantic time. Superseding a claim does not modify its supporting observation records.

## Persistence

Snapshot order is deterministic. Restore reconstructs revision, observation and interpretation records through the same validation paths used by live recording.

World-time validation rejects any record whose semantic minute lies after the checkpoint time supplied by the caller.

This ledger is standalone in Pass 384. It is not yet included in `OUROS_NPC_WORLD_CHECKPOINT_V19`.

## Relationship to existing global NPC systems

Private memory continues to own what a named NPC currently remembers or believes. Communications continue to own transport. The site evidence ledger owns durable world evidence and its observation/interpretation history.

A later integration should materialize eligible observation or interpretation records into NPC knowledge by explicit provenance-preserving events rather than by shared institutional membership or direct database visibility.

## PTU/Caelo cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes Researcher, Paleontologist, Topographer and related utility-class material to the supplied PTU/Kairos sources. It also routes movement and encounter material. Those references establish where to verify a specific skill, Feature, item or tactical interaction. They do not create archaeological powers or automatic success rules in Ouros.

The ledger therefore records evidence facts and actor claims only. It does not invent skill checks, Feature bonuses, excavation actions or item behavior.

## Engine dependency map

Targeting/footprints/range/LoS remains VERIFIED within audited ordinary contracts and is needed only when a tactical scene makes evidence points targetable or visibility-sensitive.

Base movement legality remains VERIFIED within audited ordinary contracts.

Complete movement remains PARTIAL and is required for forced slides, drag/rescue, knockback, interception or moving hazards.

Core calculations remain VERIFIED within audited deterministic scopes.

Action economy/initiative remains VERIFIED for audited primitives. A tactical documentation or stabilization action still needs an explicitly admitted action contract.

Full turn/round lifecycle remains PARTIAL.

Full stateful damage pipeline remains PARTIAL.

Status lifecycle remains PARTIAL.

Terrain/weather/hazards/zones/reactions remains MIXED/PARTIAL/BLOCKING by exact mechanism.

Move-specific behavior remains INDIVIDUALLY GATED.

Abilities remain INDIVIDUALLY GATED. AutoPTU-Java merge #418 adds deterministic nearest-active-opponent parity for the pinned Impostor target-selection seam; it does not establish general Ability coverage.

Items remain INDIVIDUALLY GATED.

Trainer Features/perks remain INDIVIDUALLY GATED.

AI legal-action infrastructure remains VERIFIED for ordinary audited actions.

AI tactical policy remains BLOCKING for protect-evidence, rescue-first, escort, search, area-documentation, stabilization-first, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL/BLOCKING for persistent evidence identity, revision projection, interaction acknowledgement, non-KO objective state and authoritative end-to-end playback.

## Reduced implementation

A reduced ruin/investigation can now preserve a baseline site revision, later physical change, observations by different actors and explicit interpretations. It needs semantic time plus the existing world-agent travel/knowledge/communication systems when NPC participation is required. It does not require AutoPTU.

## Deferred work

Portable-find custody remains owned by the existing evidence-custody/resource families until a specific integration contract is justified. Spatial geometry remains an external ref in V1. No observation is automatically copied into private memory. V19 checkpoint integration remains future work.
