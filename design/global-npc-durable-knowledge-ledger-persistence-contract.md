# Global NPC durable knowledge-ledger persistence contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Pass: 291
Scope: all persistent/recurring Ouros NPC world agents
Parent: `design/global-npc-memory-belief-communication-contract.md`

## Purpose

Preserve each named NPC's private claim history across process restart without changing provenance, confidence, source identity or belief outcome.

The invariant is:

`RESTART != FORGETTING`

Server restart, process migration or save/load cannot make an NPC lose a fact, gain a fact, merge knowledge with another agent or reinterpret a report as direct observation.

## Snapshot boundary

`KnowledgeLedger.snapshot()` emits schema `OUROS_NPC_KNOWLEDGE_LEDGER_V1`.

The snapshot preserves agent identity, every claim ID, subject and asserted value, source kind and source actor, semantic minute, confidence, provenance root, parent claim and message ID.

Claims are serialized in stable claim-ID order so equal state produces equal snapshot output.

`KnowledgeLedger.restore()` rejects unknown schemas and rebuilds claims through the same claim validation used for live state.

## Multi-agent store

`KnowledgeLedgerStore` persists several ledgers without combining them.

The store schema is `OUROS_NPC_KNOWLEDGE_LEDGER_STORE_V1`.

Ledgers serialize in stable agent-ID order. Duplicate agent IDs with conflicting state are rejected. A store restore therefore cannot turn separate actors into a shared faction or region knowledge pool.

## Epistemic continuity

Belief assessment remains derived after restore.

The snapshot does not store a preferred belief as authoritative state. It stores the evidence ledger. `evaluate_belief()` recomputes the result from the restored claims.

`PERSISTED_EVIDENCE -> RECOMPUTED_BELIEF`

## Compatibility with communication

A report received before restart retains its `message_id`, `parent_claim_id` and `provenance_root`.

After restore, later retellings still derive from the original root. Restart cannot turn one source into several independent sources.

## Deliberate exclusions

Pass 291 does not implement forgetting or confidence decay, deliberate deception, source confusion, production database transactions, cross-component atomic checkpointing, automatic schema migration or persistence of Minecraft projection state.

A production save must eventually commit ledgers, information queues, replan queues, publication cursors and coordinator guards atomically or through a recoverable journal. This pass supplies the missing ledger snapshot seam required for that larger checkpoint.

## AutoPTU boundary

Knowledge persistence is world-agent infrastructure and requires no tactical capability family.

If restored knowledge later causes a structured encounter, the encounter inherits only the mechanics it uses. No persisted claim can manufacture movement legality, reactions, status behavior, Move behavior, Ability behavior, Item behavior, Trainer Feature behavior or tactical policy.

## Canon boundary

The fixture uses synthetic actors and a synthetic route subject. It promotes no location, faction, NPC, technology or event into Ouros canon.
