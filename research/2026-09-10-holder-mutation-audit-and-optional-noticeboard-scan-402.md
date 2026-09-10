# Holder mutation audit and optional noticeboard scan — Pass 402

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Accessed: 2026-09-10

## Repository inspection and duplicate control

The recursive repository tree was inventoried at narrative head `25bb6b5a70ba07aa96931bd5b8a5cc0b18fc9147` before writing. Current focus, canon governance, the playable foundation, Passes 396–401, holder mutation/search call sites, recovery/reconciliation seams and the Kairos source index were checked first.

Source-name searches rejected heavily reused material including The Reckless Rollers, Pokémon Adventures in the Millennium, Putuland, Super Pokémon Online, Pokémon Realidea System and the prior PMD references. Pokémon Opalo had no repository hit by name. The specific Pokémon World Tour: United episode used below also had no repository hit by episode title.

## Implementation provenance — Python AST

Source: Python documentation, `ast — Abstract Syntax Trees`.
URL: https://docs.python.org/3.12/library/ast.html

The standard `ast` module can parse Python source into syntax-tree nodes and recursively walk descendant nodes. Pass 402 uses that capability only to enforce a repository-local architectural rule: production tool modules may not call known low-level holder-mutating primitives outside the holder-transition boundary.

This is implementation provenance, not worldbuilding or PTU authority.

## Pokémon fan-game source — Pokémon Opalo optional missions

Source: community-maintained Pokémon Opalo game guide, secondary missions.
URL: https://pokemon-opalo.fandom.com/es/wiki/Gu%C3%ADa_del_juego/Misiones_secundarias

Publicly documented optional content includes groups of independent jobs activated from notices, objectives distributed across different locations and at least one investigation where what the player reports changes which interested party rewards the outcome.

Reusable structure for Ouros:

- one public board can expose several independent field obligations;
- each obligation can be accepted, ignored or completed separately;
- evidence found during an apparently simple errand can create a disclosure decision;
- different institutions or actors can legitimately care about the same result for different reasons;
- optional work can become a source of later provenance without being mandatory campaign content.

Do not copy Opalo's regions, criminals, organizations, item rewards, exact puzzle, dialogue, characters or quest plots.

## PTU actual-play source — Pokémon World Tour: United, ReUnited 002

Source: public episode listing for `ReUnited 002 - Let The Egg Games Begin! Mystery At The Spring Hatching Festival`.
URL: https://www.podchaser.com/podcasts/pokemon-world-tour-united-217976/episodes/reunited-002-let-the-egg-games-205170923

The public episode description starts with characters performing ordinary work during a festival before a missing egg turns routine duty into an investigation.

Reusable structure for Ouros:

- ordinary employment or assigned duty can be the entry point to mystery;
- an incident can emerge inside an already-active social event rather than through a special quest giver;
- the same location can hold work obligations, witnesses, distractions and evidence at once;
- investigation can grow from a mundane responsibility without replacing the character's prior obligations.

Do not copy the festival, missing egg, characters, setting, scenes or solution.

## PTU/Caelo/Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing document only. It points toward Skills/Edges/Features, utility classes, movement, status, hazards, terrain/weather, Items/Gear, campaign/session structure, encounter creation, rivals and boss design. None of those page references grants a mechanic to this pass.

A public noticeboard, field report, evidence record, custody log or disclosure choice is narrative/world-agent content unless a concrete PTU check, Feature, Item effect, environmental rule or battle interaction is explicitly invoked.

## Live engine evidence

AutoPTU-Java read-only head inspected: `cf1e19c2ffb07ebd044d1d36348e88a67d5e413e`, merge #426, `Freeze authoritative switch transaction order`.

The change freezes an ordered switch transaction plan against the pinned Python source: deactivate outgoing, remove outgoing presence, activate replacement, place replacement, add joined-round marker, add released-from-ball marker, then dispatch combatant-entry hooks. This strengthens that exact switching seam. It does not establish full switching, complete movement, full action economy, full lifecycle, Abilities as a family or Trainer Features as a family.

AutoPTU Python read-only head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only and adds no tactical authority.

## Pass 402 synthesis

The technical lesson and narrative lesson meet at the same boundary: histories become trustworthy only when the system can show that all admitted state-changing paths pass through the history owner.

For worldbuilding, this supports optional jobs where several actors may handle the same physical resources or observations across time. Missing history remains uncertainty. A verified architectural boundary may strengthen later reconciliation, but it still cannot fabricate events from before an authoritative baseline existed.
