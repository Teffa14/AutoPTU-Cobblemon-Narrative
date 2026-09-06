# Durable evidence custody and reopened investigations — Pass 307

Status: RESEARCH / NON-CANON
Date: 2026-09-06

## Purpose

Research new public material that supports persistent investigations where physical evidence, custody history and later reinterpretation survive long gaps in play. This note preserves provenance separately from Ouros canon.

## Public sources reviewed

### NIST — Evidence Management Steering Committee / evidence lifecycle

NIST reported in December 2025 on evidence-handler practices across recognition, collection, intake, retention, preservation, integrity and final disposition. The useful abstraction for Ouros is that evidence has a lifecycle extending beyond the moment when it is first collected. Custody state therefore belongs in durable world state when a later investigation can depend on it.

Source: https://www.nist.gov/news-events/news/2025/12/new-report-reveals-evidence-handlers-common-practices-makes-recommendations

Transformation boundary: Ouros does not import U.S. legal admissibility rules, agency procedure or retention periods. It uses only the lifecycle principle and the need to preserve handling history.

### NIJ — retaining samples for future testing

NIJ training material explicitly discusses retaining portions of samples for possible later testing and documenting access while material remains at a laboratory. The reusable narrative pattern is that an apparently closed investigation may become investigable again because the underlying artifact and its handling record still exist.

Source: https://nij.ojp.gov/nij-hosted-online-training-courses/law-101-legal-guide-forensic-expert/report-writing-and-supporting-documentation/retaining-samples-future-testing

Transformation boundary: Ouros does not model laboratory law or biological evidence procedure. It adopts only the idea that evidence can persist beyond the first interpretation and support later re-examination.

### NIST — process mapping in forensic examination

NIST describes process maps as a way to expose decision points, workflow gaps and opportunities for root-cause analysis. The Ouros abstraction is to preserve investigation stages as causal history instead of storing only a final verdict. This supports revisiting exactly where an earlier conclusion depended on incomplete custody, weak evidence or an unverified assumption.

Source: https://www.nist.gov/forensic-science/process-mapping

Transformation boundary: no forensic discipline workflow is copied into mechanics.

### Pokémon FRLG.ips — revisiting a familiar place after a small change

The public fan-project page frames its core mystery around a familiar Kanto environment containing a small unexpected alteration, encouraging players to inspect a known route again. The useful structure for Ouros is environmental re-reading: a location already visited can become meaningful again after a change in context, evidence or world state.

Source: https://frlgips.com/

Transformation boundary: no map, event, rock placement, ending, dialogue or specific secret is imported. Ouros uses only the high-level revisitation pattern.

### PTUR / Midgarden living-world post — persistent activity between quests

A September 6, 2026 public Pokémon Tabletop community post describes Midgarden as a Westmarch-style living world with weekly downtime between quests. The reusable lesson is that persistent world state can advance and be revisited between discrete adventures rather than requiring every consequence to resolve in one session.

Source: https://www.reddit.com/r/PokemonTabletop/comments/1w8mdnx/ptur_midgarden/

Transformation boundary: PTUR homebrew rules, classes, moves, weather, abilities, traits and progression are not authoritative for Ouros and are not imported. This source is used only as living-world campaign-structure evidence.

### Pokémon World Tour: United — long-running PTU continuity

The public PTU actual-play feed reached episode 100 in April 2026 and posted a season/end-game update in July 2026. Its relevance is structural: a PTU campaign can sustain continuity over a very long span and revisit consequences after substantial elapsed play.

Source: https://podcasts.apple.com/au/podcast/pokemon-world-tour-united/id1154176782

Transformation boundary: no characters, dialogue, scenes or plots are imported.

## Reusable design lessons

1. Investigation artifacts should remain durable after their first interpretation.
2. Custody history and substantive interpretation must remain separate facts.
3. A later document can repair a documentation gap without deleting the historical fact that earlier investigators lacked it.
4. A reopened inquiry should create a new assessment rather than mutate the old assessment retroactively.
5. Familiar locations gain narrative value when later evidence changes how the player reads earlier environmental details.
6. Long-running living worlds benefit when unresolved evidence can remain dormant and become relevant again after downtime or unrelated adventures.

## Canon and mechanics boundary

No new place, NPC, institution, profession, species behavior, PTU rule or Caelo rule becomes canon through this research note.

The executable change in Pass 307 is persistence-only: `EvidenceCustodyRegistry` is added to the atomic global NPC checkpoint. It does not add evidence collection Skills, forensic checks, Pokémon senses, Trainer Features or battle mechanics.
