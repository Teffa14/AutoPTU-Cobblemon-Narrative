# Allocation notice obligation restart provenance scan — Pass 369

Status: RESEARCH / PROVENANCE. NOT CANON.
Date: 2026-09-08
Canon effect: NONE

## Repository review first

The recursive repository tree, current Pass 350/351/352 contracts, Pass 367 V8 standalone checkpoint, Pass 368 V13 coherent world checkpoint, regression suite, CI paths and PTU/Caelo source-priority evidence were inspected before writing.

The gap selected for this pass is persistence of Pass 350 notice ownership. V13 can recover that a scarce-resource decision was applied, while the Pass 350 obligation to inform each displaced reservation holder is not yet durable. Recomputing that obligation after restart from current reservations or later messages would lose provenance and could silently assign responsibility that did not actually exist at save time.

Internal source-name searches were used before selecting external narrative material. Previously processed recent sources were not reused as primary evidence. `Miragea's Traveler` returned no prior research match and was selected as a new fan-game reference.

## Operational source — University of Pennsylvania shared-equipment reservations

Source: Abramson Family Cancer Research Institute, University of Pennsylvania, “Equipment Reservations and USE Guidelines”.
URL: https://www.med.upenn.edu/afcri/equipment-reservations-and-use-guidelines.html

The public policy treats a reservation as an accountable operational object. Users are expected to release time they cannot use; missed use can forfeit the slot; repeated cancellations/no-shows can affect future access. The useful Ouros abstraction is that a booking change has an affected holder and institutional consequences. When an institution displaces a valid booking, preserving who was affected is preferable to treating the later free calendar slot as the whole history.

No Penn policy, penalty, organization or terminology becomes Ouros canon.

## Operational source — Cheqroom reservation lifecycle

Source: Cheqroom Help Center, “How To: Create and Manage Reservations”.
URL: https://help.cheqroom.com/en/articles/9515148-how-to-create-and-manage-reservations

The public documentation distinguishes reservation lifecycle states such as draft, booked, converted, overdue, closed and cancelled, and separately exposes notifications. The reusable design lesson is separation of resource state from communication state. A booking can change state while notification remains another operation.

Ouros transformation: persist `application`, `notice obligation`, `message binding`, `delivery` and `knowledge` as different facts. Current calendar state cannot substitute for those facts after restart.

No vendor workflow or software implementation is imported.

## New fan-game source — Pokémon Miragea's Traveler

Source: PokéHarbor public project page for `Pokémon Miragea's Traveler` (released May 10, 2025).
URL: https://www.pokeharbor.com/2025/06/pokemon-mirageas-traveler/

The public project description frames the player as a rookie member of a trainer organization whose remit includes helping people, protecting Pokémon and preserving nature. The reusable high-level structure is professional/adventuring work where small service obligations can coexist with exploration and larger mysteries.

Ouros transformation: a scientific or ranger-style team can receive institutional duties that matter because another person is depending on them, not because every task is a main-plot battle. A missed notification about scarce equipment can therefore become a credible field problem, relationship consequence or side quest.

Not imported: the Trainer Union, named characters, missing-person plot, poachers, ranks, setting, dialogue, quests, bespoke mechanics or Pokémon placements.

## PTU / Caelo cross-check

The project source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List. This pass adds no move, ability, item, Trainer Feature, combat rule or Caelo location fact.

The notice ledger models world administration and information provenance. If a later encounter uses PTU combat, every required battle capability remains independently gated by current engine evidence.

## Reusable Ouros structures

A displaced booking should create a durable responsibility record tied to the exact application and exact holder. Shift changes can produce believable coordination failures when the duty exists but no message has yet been authored. Later calendar cleanup must not erase that earlier responsibility. Multiple displaced holders require separate obligations because one delivered message does not prove all affected parties were informed. The world can expose these differences through logs, staff recollection, travel plans and private knowledge without forcing any NPC to lie.

## Canon disposition

All material in this note is research/provenance only. The accompanying scenario is PROPOSED / NON-CANON. No canon file is changed.
