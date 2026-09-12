# Renegotiation Checkpoint and Sandbox Triage Research — Pass 450

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Research date: 2026-09-12
Narrative baseline inspected before writing: `08c68b47b6291b2439dce9702ea9a7ffe935bc6e`

## Repository cross-check

The complete recursive Narrative tree was inventoried before writing. `CURRENT_FOCUS.md`, the full canon path inventory, assistance Passes 422–449, world and assistance checkpoint owners, private knowledge, information delivery, agendas, replacement-commitment code/tests, prior proposals/research and PTU/Kairos routing material were checked before selecting the slice. No canon file is changed.

Recent primary anchors including Citizen Sleeper, Roadwarden, Stoneshard, Archmage Rises, Pokémon Mystery Dungeon, Wartales, 80 Days, A Highland Song, Dead Rising, Long Live the Queen, Suzerain and The Life and Suffering of Sir Brante were not reused.

Repository search found no prior source-level use of `BOOK OF HOURS` / Hush House and no prior exact quest-page use of `A Song of Ice and Ire`.

## Public source 1 — A Song of Ice and Ire

Source:
- Pokémon Tabletop Wiki, `A Song of Ice and Ire`: https://pokemontabletop.com/wiki/index.php/Quest%3AA_Song_of_Ice_and_Ire

Observed high-level structure:
- the adventure advertises light time-management pressure and environmental hazards;
- players must triage side-quest priorities while a larger problem continues;
- the scenario is presented as a small sandbox;
- side objectives can provide resources or enable further exploration instead of existing only as disconnected rewards.

Transformation for Ouros:
- after a replacement appointment is restored, current access/resources can still change before execution;
- optional local work can make the eventual obligation safer or easier without rewriting the agreement that scheduled it;
- preparation objectives should be allowed to alter available routes, evidence or supplies while remaining distinct from the historical promise;
- time pressure should consume semantic world state rather than silently delete unchosen tasks.

Excluded:
- the named mountain/resort, supernatural blizzard plot, specific side quests, NPCs, encounter roster, dialogue and sequence of events.

## Public source 2 — BOOK OF HOURS

Source:
- Steam store description, Weather Factory: https://store.steampowered.com/app/1028310/BOOK_OF_HOURS/

Observed high-level structure:
- progression can be entirely combat-free;
- the player restores a damaged place and uncovers history embedded in that place;
- cataloguing and investigation accumulate durable context rather than resetting each visit;
- visitors arrive seeking assistance while the institution and its stored history continue to exist independently of those visits.

Transformation for Ouros:
- an institution or work site can remember an old appointment and a replacement appointment as two historical records even though only the latter controls current execution;
- environmental storytelling can expose the chain through schedules, logs, notices, repair marks or other evidence without requiring an exposition NPC;
- investigation of why a plan changed can be meaningful gameplay without requiring battle;
- restart persistence should preserve the world's documentary/history layer rather than flattening it to the latest mutable quest flag.

Excluded:
- Hush House, occult cosmology, named histories, books, characters, lore, dialogue, crafting recipes and endings.

## PTU/Caelo cross-check

The current Ouros source policy still treats PTU/Kairos/Caelo material as reference evidence that must be reviewed rule by rule. Neither source above grants a new mechanic or canon fact.

The useful PTU-side lesson is structural: environmental pressure, resource triage and optional enabling objectives can coexist with a main objective. If an Ouros version later uses actual PTU weather, forced movement, statuses, reactions, abilities, items or Trainer Feature interrupts, those exact families still require engine admission.

## Live engine evidence

AutoPTU-Java `main` was inspected at `1ff22f2bb1495527ca6aea08d40ce87f38f4a9d5`, merge of PR #452, `Dispatch guarded switch triggers from authoritative runtime`.

This strengthens one server-authoritative switch-trigger path and Feature-specific guard/dispatch seam. It does not establish complete reactions, complete action economy, full Trainer Feature coverage, complete movement, weather/hazard systems or specialized non-KO objectives.

AutoPTU Python `main` remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is presentation-only and explicitly does not alter battle rules or outcomes.

## Capability posture

- targeting/footprints/range/LoS — VERIFIED only inside audited scopes;
- base movement legality — VERIFIED only inside audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only inside audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by requested behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated; PR #452 supports only a narrow switch-trigger seam;
- AI legal-action infrastructure — specialized verbs such as `INSPECT`, `ESCORT`, `PROTECT`, `BRACE`, `RETRIEVE` or `EXTRACT` need explicit admission;
- AI tactical policy — BLOCKING for specialized nonstandard objectives unless separately verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Reusable design lesson

History, current schedule and current world conditions are three separate layers. A restart must preserve all three. The old agreement explains how the present arose, the replacement controls future execution, and the live environment determines what the actors actually face when the appointment arrives.