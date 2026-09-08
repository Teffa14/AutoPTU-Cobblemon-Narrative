# Atomic failed-attempt world recovery scan — Pass 358

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-08

Repository-first check

The recursive repository tree at `741dba9833da7f2f58c88d9fb797e9f9f24c0bfe` was inspected before writing. Pass 357 already owns failed handoff-attempt persistence in `OUROS_NPC_RESOURCE_CHECKPOINT_V3`; Pass 356 owns the global world-resource checkpoint at V7. This pass therefore targets atomic integration rather than another attempt model. Searches found no prior use of Pokémon Lodestone or The RED Questbook material below.

Source 1 — Pokémon Lodestone side missions

Public source: https://pokemon-lodestone.fandom.com/wiki/Side_Missions

Useful structure: the documented Serengi Bingo side mission remains in the quest log after failure and can be challenged again later. The reusable lesson is that failure can be a durable intermediate state instead of deletion of the obligation.

Ouros transformation: a failed pickup can remain historical evidence while the parent authorization or broader objective continues, subject to its own expiry/refusal rules. The later retry is a new event. No Lodestone characters, locations, rewards, Pokémon lists, dialogue or quest plot are imported.

Source 2 — The RED Questbook, journal state and tracking

Public source: https://hlky.github.io/cyberpunk-quest-authoring/journal/quest-state.html

Useful structure: quest journal state is save-backed, and robust flows treat action completion, objective success, cleanup, authored facts and quest termination as separate transitions. Reload testing at interruption boundaries is explicitly important.

Ouros transformation: world restore must recover the failed attempt as recorded state without rerunning the pickup, firing replans again, moving custody or silently completing another transition. The checkpoint is evidence recovery, not quest execution.

Source 3 — Pokémon Keishou quest taxonomy

Public source: https://pokemon-keishou.fandom.com/wiki/Main_Quest_Guides

Useful structure: the public quest guide separates main quests, supplemental quests that provide tools/progression needed by main quests, and optional quests. This supports a campaign structure where logistical obligations can matter without every one becoming a main-story beat.

Ouros transformation: a resource pickup, missed rendezvous or later retry can persist as a supporting obligation attached to a larger expedition, investigation or institution. Failure can create delay, substitution or another route instead of forcing a global story failure. No Keishou characters, locations, quest names or plot are imported.

PTU/Caelo boundary

No external source above is rules authority. PTU Core, project-held Caelo material, errata/extras, Pokédex data and the project's existing AutoPTU contracts remain authoritative for mechanics. This pass adds no Move, Ability, Item, Trainer Feature or regional fact.

Reusable Ouros lessons

1. Persist failed attempts as facts, not as erased branches.
2. Keep retry eligibility separate from the historical fact of failure.
3. Save/load must not replay side effects.
4. Supporting logistics can remain meaningful without becoming mandatory main-plot content.
5. Old saves that never stored an event stay historically incomplete instead of receiving inferred history.

Canon result

No canon promotion. All material remains research or proposal-level until separately reviewed.
