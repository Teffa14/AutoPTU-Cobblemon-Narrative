# Global NPC site interpretation to private inference contract — Pass 386

Status: PROPOSED IMPLEMENTATION CONTRACT
Canon effect: NONE
Date: 2026-09-09

## Purpose

Pass 384 created durable site interpretations. Pass 385 connected direct site observations to observer-only private knowledge. Pass 386 defines and implements the next boundary: an interpretation may enter an NPC's private `KnowledgeLedger` as `INFERENCE` only when that NPC already has explicit private knowledge of every observation supporting the interpretation.

## Owner

Schema: `OUROS_SITE_INTERPRETATION_KNOWLEDGE_V1`
Implementation: `tools/global_npc_site_interpretation_knowledge.py`

The bridge owns materialization provenance only. `OUROS_SITE_EVIDENCE_LEDGER_V1` continues to own site observations and interpretations. `KnowledgeLedgerStore` continues to own private claims.

## Admission contract

For interpretation `I` authored by actor `A` at semantic minute `T`:

1. `I` must exist in the site-evidence owner.
2. `A` must have a managed private knowledge ledger.
3. Every observation referenced by `I` must already exist and be temporally legal in site evidence.
4. `A` must possess a private claim whose subject identifies each source observation, whose value matches that observation, whose provenance root matches that observation and whose semantic minute is no later than `T`.
5. The bridge materializes exactly one deterministic private inference claim for `I`.

This permits inference from personally observed evidence and from evidence learned through an existing explicit report path, because `transmit_claim` preserves source subject/value/provenance. It does not permit inference directly from hidden world state.

## Private claim form

The generated claim uses:

- `SourceKind.INFERENCE`;
- the interpretation actor as `source_agent_id`;
- the site interpretation claim as value;
- interpretation confidence converted deterministically to 0–100;
- site-level inference subject identity;
- a conservative provenance root tied to supporting evidence rather than a fabricated independent root.

The bridge record separately preserves every source observation ID and every distinct source provenance root. This is required because the existing `Claim` model contains only one `parent_claim_id` and must not be misrepresented as a multi-parent evidence graph.

## Supersession

When interpretation `I2` supersedes `I1`, `I1` must already have a private materialization for the same actor/site before `I2` can materialize. `I2` uses the earlier private inference as `parent_claim_id` and preserves the earlier inference provenance root. The older claim remains unchanged.

This keeps intellectual history replayable and prevents repeated reinterpretations of the same evidence lineage from being counted as independent evidence merely because the wording or confidence changed.

## Invariants

`WORLD_INTERPRETATION != UNIVERSAL_KNOWLEDGE`

`OBSERVATION_KNOWN_BY_ACTOR + INTERPRETATION != DIRECT_OBSERVATION`

`INFERENCE_SUPERSESSION != MUTATED_OLD_CLAIM`

`MULTI_SOURCE_EVIDENCE != ONE_PARENT_CLAIM_GRAPH`

`EXPERT_AUTHORSHIP != CANON_TRUTH`

## Restore validation

Restore fails closed when materialization identity changes, source interpretation disappears, actor/site/time diverge, supporting observation IDs change, source provenance roots diverge, the actor no longer has an explicit private provenance path to a support observation, a parent inference is missing, the private claim differs from source interpretation, or the record lies after checkpoint semantic time.

## Authority boundary

The bridge changes information persistence only. It introduces no PTU Skill check, Feature, Item, species fact, excavation procedure or canon interpretation. `sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid and does not grant mechanics.

## Checkpoint ownership

This owner remains standalone in Pass 386. Site evidence, direct-observation materialization and interpretation materialization together describe persistent world/evidence state broader than the global-NPC V19 causal checkpoint. A later pass should define that world checkpoint deliberately rather than append these ledgers to V19 without an ownership decision.
