# Research scan — durable NPC knowledge across restart

Status: RESEARCH / PROVENANCE
Date: 2026-09-05
Pass: 291
Canon effect: none

## Gap inspected

Passes 282–290 gave named NPCs private claims, communication, revision-aware public receipts and selective replanning. Queue and scheduler layers already had snapshot seams, but `KnowledgeLedger` did not. A restart could therefore preserve a pending message while losing the receiver's earlier evidence, creating a causal discontinuity.

Pass 291 closes only the ledger snapshot gap. Cross-component atomic commit remains future work.

## Public sources reviewed

### MemoryRepository for AI NPC

The 2024 IEEE Access paper describes separate short- and long-term NPC memory and treats forgetting/summarization as deliberate memory mechanisms rather than accidental process loss.

Reusable lesson: operational restart must not be confused with authored forgetting; memory transformation should be explicit and versioned.

Source: `https://doi.org/10.1109/ACCESS.2024.3393485`

### Quilltale

The public project separates validated world state from generated narration and records per-NPC episodic history rather than relying on model context alone.

Reusable lesson: durable structured state should own facts and memory; prose/rendering should consume that state instead of becoming the source of truth.

Source: `https://github.com/Aeesh/quilltale`

### SQLite transactional / atomic-commit documentation

SQLite documents ACID transactions and crash recovery where a transaction appears fully committed or not committed.

Reusable lesson: the eventual Ouros production persistence layer should treat a checkpoint as a transaction boundary rather than independently writing several causally linked files.

Sources: `https://www.sqlite.org/transactional.html`, `https://www.sqlite.org/atomiccommit.html`

Pass 291 does not claim to implement SQLite or production atomic commit. The sources inform the next persistence boundary.

### Akka event-sourced entities

Akka documentation describes reconstructing state after restart from durable events, with snapshots used to reduce replay cost.

Reusable lesson: restored state should derive from durable evidence/history; snapshots are a recovery representation, not a reason to erase prior causal history.

Sources: `https://doc.akka.io/sdk/event-sourced-entities.html`, `https://doc.akka.io/concepts/state-model.html`

### PTU community material

A 2025 PTU first-session discussion describes an investigation flow using tracking, skill checks, witnesses and a final confrontation after Pokémon are stolen. The useful structure is that different witnesses and discoveries provide staged information before combat.

Reusable lesson: witness knowledge is adventure state and should survive session/server boundaries; investigation can remain useful without forcing every clue into a battle.

Source: `https://www.reddit.com/r/PokemonTabletop/comments/1iz38d4/tips_and_ideas_for_a_first_session_ptu/`

A PTU campaign recruitment post describes undercover infiltration and heist-style play mixed with Pokémon battles.

Reusable lesson: long-running identity/information state can carry an arc across many scenes; secrecy and evidence need persistence independent from tactical encounters.

Source: `https://www.reddit.com/r/PokemonTabletop/comments/z24ni1/ptu_dm_lfm_pokemon_undercover/`

## Transformation into Ouros

No source character, plot, place, dialogue or bespoke mechanic was copied.

The transformed Ouros principle is: a named NPC's evidence history survives restart exactly. Forgetting, distortion, deception and belief revision must be later authored simulation events, never side effects of persistence failure.

## Internal cross-check

The existing memory contract already states that contradiction is retained and future forgetting must reduce active influence without erasing provenance. Pass 291 follows that rule by persisting the evidence ledger and recomputing belief after restore.

The global world-agent contract continues to require non-omniscient NPCs, deterministic replay, explicit communication and no region-specific core behavior.

## Open research

Future passes should research recoverable multi-component transaction boundaries, memory consolidation without destructive provenance loss, deliberate forgetting policies by memory type, source-monitoring error and deceptive testimony, and save migration/schema evolution.
