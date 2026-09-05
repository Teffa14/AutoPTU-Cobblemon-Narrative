# Research Scan 288 — Public Publication, Broadcast Receipt and Interest Filtering

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: NONE

## Existing Ouros material checked

This pass inspected the current global NPC information, audience and communication runtime contracts plus the older `broadcast-programming-live-transmission-continuity-extension.md`. Pass 161 already established the critical semantic distinction between a program, episode, transmission, audience receipt and audience belief. Pass 288 therefore does not redesign broadcast continuity; it adds an executable receiver-expansion seam for the global NPC architecture.

The project authority policy remains binding: `SOURCE_HAS_RULE != OUROS_USES_RULE`.

## New external sources

### Cañas, Zhang, Kemme, Kienzle & Jacobsen — Publish/subscribe network designs for multiplayer games, Middleware 2014

Source: https://doi.org/10.1145/2663165.2663337

Reusable lesson: massive multiplayer systems benefit from explicit publish/subscribe and interest-management structures rather than sending every message to every participant. Different filtering designs have meaningful traffic/coordination trade-offs.

Ouros transformation: a public artifact is expanded only toward explicit eligible persistent actors, in bounded deterministic batches. The publication layer does not equate public visibility with universal receipt.

Not adopted: their networking architecture, benchmark values, middleware implementation or client/server assumptions.

### Han, Lim, Lee & Hyun — A scalable interest management scheme for distributed virtual environments, 2008

Source: https://doi.org/10.1002/cav.218

Reusable lesson: fine-grained relevance filtering reduces unnecessary dissemination in crowded virtual environments; location alone can be supplemented with interest grouping and scoped interaction.

Ouros transformation: public reception can require service access, scope and explicit topic state before a receipt event is scheduled. Production indexing remains future work.

Not adopted: multicast topology, exact grouping algorithm, viewing-direction model or performance claims.

### Pokémon Gold/Silver/Crystal and HeartGold/SoulSilver — Pokégear radio structure

Reference summary: https://bulbapedia.bulbagarden.net/wiki/PokeGear

Reusable high-level structure: radio access is gated; stations differ by region and additional access can be required when moving between Johto and Kanto. Radio carries distinct programs rather than one universal world feed.

Ouros transformation: media service access and distribution scope are explicit world facts. A public publication can exist without reaching every NPC, and regional/service differences can produce divergent knowledge states.

Not adopted: Pokégear hardware, Goldenrod/Lavender infrastructure, station names, radio frequencies, quest gates, music effects, characters or any assumption that Ouros regions use equivalent technology.

## Design conclusions

1. Public availability must remain separate from individual receipt.
2. Large fanout needs a dedicated expansion seam rather than abusing private-contact selection.
3. Audience filtering should consume explicit access/scope/interest state and remain deterministic.
4. Expansion should be budgeted and resumable so a large audience cannot force unbounded work in one simulation cycle.
5. Final delivery should reuse the existing information queue and knowledge ledger so latency, failure, provenance and belief semantics do not fork.
6. Corrections/retractions should append new evidence with lineage rather than rewriting historical receipts.

## PTU / Caelo / Kairos cross-check

No battle or Trainer rule is required for this layer. Nothing found in public media/game references overrides PTU/Caelo/Kairos mechanics or creates a new Ouros rules-profile overlay.

Public communication reach, service access, retention and fanout are MMO/world-simulation policy owned by Ouros and must remain versioned/tested as such.

## Copyright boundary

Only abstract structures and design lessons were extracted. No protected dialogue, prose, named fan characters, quest scripts or distinctive plots were copied into Ouros content.
