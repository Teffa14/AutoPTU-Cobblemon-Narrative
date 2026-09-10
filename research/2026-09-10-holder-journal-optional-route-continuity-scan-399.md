# Pass 399 Research — Holder History, Optional Routes and Persistent Consequences

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-10

Repository inspection before writing covered the current root tree, canon surface, implementation surface, current focus, recent recovery/resource contracts, current holder journal/checkpoint, reservation/custody call sites, post-restore validation, the PTU/Caelo/Kairos router, recent proposals and source-name searches. The research corpus is already extensive, so recurring anchors were excluded. Pokémon Rollout!, The Reckless Rollers, Pokémon World Tour: United, Pokémon Monomyth, Pokémon Prisme and the recent resource/courier sources were not reprocessed.

Specific repository searches returned no prior match for Pokémon Mystère Exploration / PME, Pokémon Elysium, or Reddit thread `1oz4e7w` before this note was added.

## Source 1 — PTU GM discussion: serious tone with episodic/open exploration

Public source:
https://www.reddit.com/r/PokemonTabletop/comments/1oz4e7w/first_time_dm_thinking_of_making_a_ptu_campaign/

Retrieved: 2026-09-10.

The thread asks how to reconcile a serious PTU campaign with a more episodic structure. One response proposes an open-ended exploration model in which the GM places several lightly specified hooks in the world, watches which ones the players engage with, and expands those rather than pre-writing every branch.

Reusable structure:

A serious persistent story can grow from optional local hooks. Ignored hooks do not need to disappear. They can remain in the world, be handled by NPCs, fail, change ownership, or acquire later significance because time continued.

Ouros transformation:

An optional field survey can exist as a real obligation with its own time window, resource requirements and NPC awareness. If the player ignores it, a named NPC team may attempt it using the same global planning/resource systems. Later consequences depend on what actually happened, not on a hidden assumption that the player was destined to accept the quest.

No campaign setting, character, encounter, dialogue or plot from the thread is imported.

## Source 2 — Pokémon Mystère Exploration / PME

Official public source:
https://pmexploration.net/

Retrieved: 2026-09-10.

The project describes mystery dungeons with changing layouts, traps and hidden shops, together with an expedition loop where failure can still leave a form of persistent preparation/progression for later attempts.

Reusable structures:

- revisiting an exploration space can present a materially different traversal problem;
- failed or incomplete expeditions can still change later preparation;
- terrain and route knowledge can be part of the challenge rather than decorative background.

Ouros transformation:

A side route can change between survey attempts because of ordinary world processes or an authored event. The earlier survey remains historically meaningful as a baseline even if the current topology differs. The reduced implementation represents the change between scenes/revisions. A richer implementation may represent dynamic hazards during an encounter, but only when the relevant AutoPTU capability families are verified.

No PME map, dungeon, trap, shop, blessing, progression currency, character or proprietary encounter is copied.

## Source 3 — Pokémon Elysium

Public references:
https://www.reddit.com/r/PokemonROMhacks/comments/168t2g5
https://romhaven.com/games/pokemon-elysium/

Retrieved: 2026-09-10.

The developer's public release description identifies Elysium as a long story/lore-focused hack with optional side quests inside a larger chapter structure. Current public listings retain that same broad description.

Reusable structure:

Optional work can coexist with a strong long-form narrative. Side content does not have to be disposable filler if it creates information, relationships, resources or consequences that remain relevant later.

Ouros transformation:

A small survey request can create a baseline observation, a holder/custody history for shared equipment, knowledge held by specific NPCs and a site revision. Those facts may later intersect a larger regional problem without retroactively making the original request mandatory.

No Elysium region, character, faction, championship, side quest, dialogue, creature, item or plot event is imported.

## Systems research result

Pass 398 established a four-owner recovery generation that includes the holder-transition checkpoint. Inspection of the current implementation found that the post-restore reconciler still ignored that owner.

It also found an important coverage limit. Ordinary checkout, return and the holder-aware handoff wrapper produce `ResourceHolderTransition` records. However, `tools/global_npc_resource_handoff_rescheduling.py::execute_current_authorized_handoff()` can still call `execute_authorized_handoff()` directly. Therefore the holder journal cannot yet be treated as complete for every possible resource.

Pass 399 uses an explicit audited-completeness set. Journal evidence can prove a current-holder match or contradiction only for resource ids whose relevant mutation paths have been audited complete. Other cases remain `INDETERMINATE`.

The holder checkpoint was also hardened so a transition later than the checkpoint's semantic cut is invalid even if a payload is re-digested.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked strictly as a routing aid. Relevant source families remain campaign/session structure, Skills/Edges/Features, Researcher/Chronicler/Climatologist/Topographer-style utility classes, movement, hazards, terrain/weather, encounter construction and Items/Gear.

This pass grants none of those mechanics to Ouros. It does not invent a survey Skill DC, Topographer bonus, weather modifier, carrying rule, Item effect, Trainer Feature interrupt or dungeon hazard rule. Any such mechanic still requires verification against the underlying supplied source and the engine contract.

## Live engine evidence refreshed

Read-only AutoPTU-Java main observed on 2026-09-10:
`d809490e15ef77afeaf3fd6ed32ac6d70638f166` — merge PR #424, `Freeze switch entry state prefix`.

The new contract freezes a narrow successful-switch pre-entry state prefix. It adds release/joined-round temporary-effect planning before later send-out Feature or Ability hooks. Its own source states that field presence and active-affiliation mutation remain outside the class until a first-class off-field placement store exists. This is stronger evidence for that exact switch-entry seam, not for complete switching, the whole turn/round lifecycle, Abilities, Trainer Features or movement.

Read-only AutoPTU Python main remains:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — the newest commit is presentation-only viewport coordinate synchronization and changes no battle rule or outcome.

## Resulting Ouros candidate

See `proposals/2026-09-10-the-survey-trail-nobody-took-pass-399.md`.

The core design is an optional survey hook that remains causally real if ignored. Another expedition can act on it, a route can later change, and an old baseline can become important. Holder history, site evidence and NPC knowledge answer different parts of the later investigation. The campaign does not retroactively force the original side quest into the player's past.