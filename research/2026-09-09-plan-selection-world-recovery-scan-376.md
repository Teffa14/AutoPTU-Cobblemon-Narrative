# Pass 376 research — plan-selection world recovery

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-09
Canon impact: NONE

## Repository boundary inspected

Narrative baseline before this pass: `58fbf3b624ff19b55e2d567c3f103d88166aea76`.

The recursive repository tree, current focus, canon governance, Pass 374 V15 checkpoint, Pass 375 standalone plan-selection owner, related tests and current research corpus were inspected before writing. Searches were used to reject previously processed candidates. Pokémon Aragonite and the Not Presently Deceased Reflection Cave PTU one-shot were excluded because existing research already covers them.

Read-only engine evidence checked:

- AutoPTU-Java `948f42cfcfd34000087cb0667b4926c9aa2c8df4` — merge #414, round-start Ability dispatch wired into the authoritative lifecycle after round-start Trainer Feature dispatch.
- AutoPTU Python `729bae2d424963ff9bb3f4159c9a7ac9152128a7` — presentation-only viewport synchronization.

No engine repository was modified.

## New public sources

### New Zealand Search and Rescue — Incident Action Plan guidance

Source: https://www.nzsar.govt.nz/nzs-sar/planning/creating-an-incident-action-plan

Public guidance says an Incident Action Plan should include objectives and strategies plus supporting records such as a chronological communications log, decision record, taskings, debriefs and resource tracking. The plan is reviewed and updated as objectives are achieved.

Reusable Ouros structure:

A field organization can preserve what it intended to do, why that course was selected, and which taskings followed without treating the final world state as sufficient evidence of the earlier decision.

Transformation boundary:

No real-world SAR procedure, authority, form, terminology or safety rule becomes Ouros canon. Only the high-level separation between decision record, tasking, execution and debrief is reused.

### Pokémon Shinju Adventures

Public listing: https://www.astartgaming.com/2024/07/pokemon-shinju-adventures-RPGXP.html

The public description presents a foreign-exchange student in a biodiverse region with freedom to explore, train, pursue the Gym challenge and build relationships with other exchange students.

Reusable Ouros structure:

A recurring institutional identity can coexist with open exploration. A character can have scheduled obligations and still choose among research, travel, training, relationships and optional exploration when a replanning window opens.

Transformation boundary:

No Shinju region, characters, exchange-student cast, shiny rate, quest text, maps or plot are imported.

### Pokémon Svalbard

Public listing: https://www.astartgaming.com/2026/06/pokemon-svalbard-rpgxp-fangame.html

The public description uses an Arctic-region journey where a newly certified trainer leaves an ordinary starting context after a friend goes missing and travels through a hazardous northern environment.

Reusable Ouros structure:

A selected ordinary plan can be interrupted by a new personal emergency before execution begins. Harsh geography can make the distinction between choosing a route and physically committing to it consequential.

Transformation boundary:

No Svalbard geography, missing-person plot, characters, locations or progression structure are imported.

## Design synthesis

The sources reinforce a useful causal sequence for persistent Ouros NPCs:

`INFORMATION AVAILABLE -> OPTIONS COMPETE -> PLAN SELECTED -> TASK/ACTION STARTED -> OBSERVABLE CONSEQUENCE -> REVIEW`

Pass 375 made the middle decision replayable. Pass 376 places that decision in coherent world recovery. The next owner still needs to represent action start explicitly.

This matters narratively because a recovered world may correctly remember that an NPC chose an expedition, rescue, survey, meeting or route while also correctly showing that the NPC never departed. The gap can come from a new interruption, missing equipment, closed access, a later order or simple elapsed time rather than from deception or save/load amnesia.

## PTU / Caelo cross-check

Internal project authority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List when available.

This pass introduces no species placement, move, Ability, item, Trainer Feature, encounter table, regional landmark or PTU combat rule. Any later field encounter must bind those details only after internal source validation.

Research remains provenance. The companion proposal remains non-canon until explicitly promoted through `canon/`.
