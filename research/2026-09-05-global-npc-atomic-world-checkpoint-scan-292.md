# Research scan — atomic global NPC checkpoint — Pass 292

Status: RESEARCH / PROVENANCE, NOT CANON
Date: 2026-09-05

Pass 291 already closed the standalone knowledge-ledger restart gap. Current inspection found the next failure mode: ledgers, information queue, replan queue, mutable agent knowledge and coordinator idempotency guard can each be valid yet belong to different causal moments after a partial save.

Internal authority was rechecked in `design/ouros-source-authority-and-species-policy.md`: PTU remains deep mechanical authority; Caelo/Kairos are living-world references; source rules do not activate automatically. `sources/kairos/KAIROS_SOURCE_INDEX.md` confirms persistent living-world activity across quests/downtime but does not define Ouros persistence semantics.

New public sources reviewed:

SQLite Atomic Commit — https://www.sqlite.org/atomiccommit.html
Reusable structure: interrupted multi-part state changes require a recovery boundary that exposes a coherent pre-commit or post-commit state rather than arbitrary partial state. Ouros uses this only as architecture inspiration for one logical checkpoint. SQLite storage/journal algorithms are not imported.

Transactional Outbox — https://microservices.io/patterns/data/transactional-outbox.html
Reusable structure: state change and the durable intent/event caused by it belong to the same transaction boundary, while consumers need idempotency. Ouros transforms this into packaging delivery status, receiver knowledge, wake-up scheduling and materialization guards together. No broker, table schema or polling topology is adopted.

Pokémon Legends: Arceus Tasks/Requests — https://bulbapedia.bulbagarden.net/wiki/Task_(Legends:_Arceus) and https://bulbapedia.bulbagarden.net/wiki/Jubilife_Village
Reusable structure: optional requests have prerequisites, independent tracking and can contribute to persistent world development/unlocks. Ouros transforms this into a continuity requirement: a technical restart cannot silently cancel an NPC obligation, warning or investigation state. No Hisui character, quest, reward or location is imported.

PTU campaign log #22 — https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t/campaign_log_22/
Reusable structure: observation/information gathering identifies an environmental problem and enables a non-combat intervention with settlement-scale consequence. Ouros reuses only evidence → diagnosis → action → persistent consequence. The original town, festival, Pokémon cast, environmental cause and scene sequence are not copied.

The Pass 292 transformation is narrow: technical restart must not become diegetic amnesia; causally coupled world-agent state should restore from one validated logical unit; idempotency state belongs beside the events it protects; invalid/corrupt checkpoint data fails before a partial runtime is exposed; world-only consequences remain available when tactical families are incomplete.

Physical crash-safe commit remains deferred to a storage adapter. Full AutoPTU battle serialization remains outside this repository's authority. The checkpoint keeps only the existing binding reference.

Canon status: research conclusions are RESEARCH; checkpoint contract is PROPOSED EXECUTABLE INFRASTRUCTURE; the Interrupted Dispatch loop is PROPOSED / NON-CANON. No lore or PTU/Caelo/Kairos rule changed.
