# Research scan — deceptive communication durability and long-memory world continuity — Pass 297

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05

This scan was performed after inspecting the current Ouros repository tree, current canon governance, global-NPC contracts through Pass 296, and the read-only AutoPTU-Java / AutoPTU heads. Nothing in this file is canon by itself.

## New external sources

### Microsoft Azure Architecture Center — Transactional Outbox
Source: https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos

Reusable lesson: when a durable state change and the event other systems must observe are committed separately, recovery can expose impossible combinations. A shared transaction/outbox boundary prevents one side from existing without the other. Ouros does not adopt Azure infrastructure; the useful abstraction is causal durability across state plus pending communication.

### Living Village prototype — NPC testimony and bounded knowledge
Source: https://ianlehrer.com/projects/livingvillage/

Reusable lesson: NPC dialogue becomes more credible when a character only knows events that actually reached them. Testimony and denial work better when knowledge provenance is preserved below the dialogue layer. Ouros keeps this as a design reference, not an implementation dependency.

### Pokémon Pokopia continuity coverage
Source: https://www.gamesradar.com/games/pokemon/after-30-years-pokemon-pokopia-finally-answers-an-important-question-for-the-hardcore-lore-freaks-whatever-happened-to-that-one-npc-builder-in-vermillion-city/

Reusable lesson: a small world fact can become valuable environmental storytelling when later locations or records reveal a consequence after a long interval. Ouros can use durable dispatch records, archives and changed locations to pay off old NPC actions without copying the Pokémon character, construction, location or reveal.

### Pokémon Tabletop United — current living-region campaign listing
Source: https://www.reddit.com/r/FoundryLFG/comments/1w7boia/onlinepokemontabletopunitedfoundryvttbiweekly25ses/

Reusable lesson: current PTU play still values exploration, research, recurring rivals, Pokémon care and rebuilt habitat tables alongside tactical combat. Persistent regional state therefore remains a useful target even when a narrative loop has a reduced non-combat implementation.

### The Reckless Rollers — current PTU actual play index
Source: https://podcastaddict.com/podcast/the-reckless-rollers/2836264

Reusable lesson: a long-running PTU campaign can sustain job structure, downtime and investigation episodes among battles. Ouros should preserve causal information state across long arcs instead of requiring every mystery or consequence to resolve in the scene where it began.

## Transformation into Ouros design

The new material supports a narrow principle: world history, communication history and later reconstruction should survive technical restart as coherent state. A false report that was pending before restart must remain the same false report afterward. A record discovered later may explain why an NPC acted, but it must not retroactively replace the NPC's earlier knowledge.

This supports future investigations where the player reconstructs sequence rather than merely identifies a single truth flag: what the speaker knew, what they asserted, who was selected, whether delivery completed, what the receiver believed, and what later archival evidence survives.

## Copyright and canon boundary

No protected dialogue, distinctive character, quest plot, region, faction or encounter is copied. External Pokémon/PTU material contributes only high-level design patterns. The Azure/Living Village references contribute architecture concepts only.

No combat rule, PTU Feature, Move, Ability, Item, hazard rule, movement permission or Caelo/Kairos rule is adopted here.
