# V5 session boundary and moving leads — Scan 413

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-10
Narrative baseline inspected before writing: `0aed0c4e41f206be48444738283a7c629c76fe1c`.

The recursive repository tree was inventoried before writing. `CURRENT_FOCUS.md`, the complete current `canon/` inventory, relevant Pass 411–412 session/recovery code and tests, recent recovery research/proposals, and the Kairos/PTU routing material were checked. Repository-wide source-name searches were used to avoid repeating prior anchors. The Alexandrian/Three Clue Rule, Pokémon Ashen Frost and Pokémon Svalbard were rejected because the current corpus already contains them. Searches for `Lethalmon` and `Cryptochrome` returned no prior research entry before this pass.

## Internal technical finding

Pass 412 makes the AutoPTU session checkpoint an exact V5 manifest owner, while Pass 411's `reconcile_autoptu_session_checkpoint_with_agents()` can still be invoked independently on a valid session snapshot plus an independently supplied agent set.

Reusable systems lesson: generation selection must happen before session or agent content is allowed to influence post-restore state. Pass 413 therefore composes the two existing contracts into one exact V5 boundary. Agents come from the global checkpoint selected by the same manifest that selected the session ledger.

## Source 1 — Lethalmon

Sources:
- https://lethalmon-fangame.com/
- https://lethalmon-fangame.com/pitch/

Public project material describes a roguelike Pokémon fangame built around repeated hostile expeditions followed by return to a central hub. Different destinations host different species and environmental contexts, while each sortie has an explicit return-and-prepare rhythm.

Reusable Ouros structures:

- a field excursion can be a bounded decision unit instead of an obligation to clear an entire area;
- returning with sufficient information or resources can be a valid successful outcome;
- repeated departures from one service hub can expose different world conditions while preserving persistent relationships and obligations at home;
- expedition pressure can come from deciding whether to continue or return, without requiring every sortie to culminate in a boss battle.

No planet, ship, convict premise, economy, Gym structure, species roster, biome, dialogue, item or plot from Lethalmon is imported.

## Source 2 — Pokémon Knowledge by Cryptochrome

Source:
- https://eeveeexpo.com/threads/9690/

The public release thread began on 2026-08-16. Its stated story structure lets the player choose the order in which several directions are pursued after one initiating incident. The thread also describes an open branching-path structure, extensive inspectable environmental descriptions and relatively little mandatory Trainer combat in the current release.

Reusable Ouros structures:

- one incident may create several legitimate leads whose pursuit order is chosen rather than scripted;
- different routes can carry information rather than serving only as geographic connectors;
- a lead can culminate in a decision rather than an automatic battle;
- environmental inspection can sustain investigation even when combat density is low.

No robbery, casino, thieves, family/police setup, Shadow Pokémon, Delta Species, Mega Evolution, puzzle, map, character, dialogue or specific choice from Pokémon Knowledge is imported.

## Combined design lesson

The useful synthesis is a moving-leads loop. Several leads exist at once, semantic time continues while one is pursued, and the player or persistent NPCs may return to a coordination point with incomplete but useful evidence. A lead left alone may later be observed under different conditions or handled by another actor. The system does not invent what happened during an unobserved interval; it records only authoritative world transitions and attributed observations.

This structure uses existing Ouros strengths: persistent named agents, off-screen travel, schedules, obligations, private knowledge, explicit communication, provenance and site revisions. It does not require AutoPTU for its reduced form.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was checked as a router only. Campaign/session and encounter material may support later adjudication research, while movement, hazards, terrain/weather, Items and Trainer Features still require their exact source contracts.

This scan grants no Skill DC, Move behavior, Ability effect, Item effect, Trainer Feature, forced movement, reaction, hazard, terrain rule, weather phase or objective-completion mechanic.

## Live engine evidence

AutoPTU-Java head inspected: `b0563ab0c0998648a93d3e4daf52fb7734c81fd0`, merge PR #435, `Synchronize replacement tactical position during switch`, dated 2026-09-10.

The change updates `CombatantSwitchExecutor` so the replacement combatant's server-owned runtime tactical position is moved to the validated switch destination before post-entry temporary effects/hooks. Its oracle parity regression also verifies that invalid presence validation does not mutate that runtime position.

This strengthens one switching/base-position synchronization seam. It does not establish complete movement, push/pull, knockback, interception, forced movement, full action economy, full initiative semantics, full turn/round lifecycle, full damage/status pipelines, hazards/zones/reactions, all Abilities or Trainer Features.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only viewport coordinate synchronization and explicitly changes no battle rules or outcomes.

Neither engine repository was modified.

## Derived narrative direction

The proposal `The Leads Do Not Wait` applies the combined structure to an Ouros field incident without establishing a culprit or even requiring wrongdoing. More than one attributed lead can exist simultaneously. Player choice, NPC assignments, travel time and communication determine which evidence actually becomes known before conditions change.

The reduced implementation uses existing persistent-world systems only. A richer version may add tactical retrieval, escort, extraction or withdrawal after those capabilities are individually verified.
