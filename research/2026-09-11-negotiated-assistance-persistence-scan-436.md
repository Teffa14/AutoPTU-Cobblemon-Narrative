# Negotiated Assistance Persistence Scan — Pass 436

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

## Repository inspection

The full recursive repository tree at `179bed59bf544fc600413b882b4fcbac592e3e55` was inventoried before writing. Current focus, canon governance, canon foundations, design contracts, proposals, research, source routing, tools, tests and workflow surfaces were checked before selecting the slice. Passes 422–435 were traced specifically so this work would extend the assistance chain rather than repeat response delivery, replanning, acceptance, deferral, counterproposal delivery, requester consent or commitment materialization.

Repository search also rejected recently repeated anchors including Roadwarden, Wildermyth and Pokémon Burning Scales. The sources below had no repository matches before this pass.

## Source: Shadows of Doubt

Developer page: https://colepowered.com/games/shadows-of-doubt/
Steam description: https://store.steampowered.com/app/986130/Shadows_of_Doubt/
Accessed: 2026-09-11

High-level reusable structure: the world continues independently, with individual citizens maintaining jobs, homes and routines while cases are investigated through evidence. The important abstraction for Ouros is temporal separation between what an actor agreed to do and the state encountered when the actor later arrives. A durable appointment must preserve the agreement without freezing the surrounding simulation.

Transformation for Ouros: negotiated assistance can survive off-screen simulation and restart, while current access, route state, witnesses, hazards and the original problem remain free to change. The agreement provides causal history and scheduling pressure, not a frozen encounter instance.

Excluded material: setting, crimes, characters, gadgets, dialogue, city structure and distinctive case content.

## Source: Star Traders: Frontiers mission structure

Public mission reference: https://startraders.fandom.com/wiki/Missions
Accessed: 2026-09-11

High-level reusable structure: missions carry explicit deadlines, and lateness can alter consequences rather than automatically erasing the historical mission. Some optional event chains begin only when world conditions are right and may span long periods.

Transformation for Ouros: a proposal window, acceptance time and scheduled work window should remain separate durable facts. A checkpoint must not refresh an expiry or rewrite the accepted appointment. Later policy can decide what missed, late or impossible work means, but persistence must retain the original terms first.

Excluded material: factions, eras, contacts, economy, mission text, reward values and setting-specific story beats.

## Source: Pokémon Unbound mission system

Public mission index: https://unboundwiki.com/missions/
Public walkthrough index: https://unboundwiki.com/walkthrough/
Accessed: 2026-09-11

High-level reusable structure: a large optional mission layer coexists with the main journey, with missions tied to locations, prerequisites and later world progression. The reusable lesson is modularity: side work can remain legible as its own stateful thread while the broader adventure continues.

Transformation for Ouros: assistance incidents should be capable of remaining small, composable quest threads. A negotiated survey, delivery, inspection or repair can persist through travel and unrelated story progression without becoming the main arc or requiring a battle.

Excluded material: Borrius, named missions, characters, rewards, maps, dialogue, plot, dungeon layouts and specific progression gates.

## PTU / Caelo cross-check

The project source inventory and Kairos routing material continue to treat PTU references as rule-location evidence rather than automatic Ouros canon. This pass introduces no PTU rule reinterpretation. The new checkpoint contract stores narrative causality only. Any later encounter that uses movement, damage, statuses, terrain, reactions, moves, abilities, items or Trainer Features must still route those mechanics through verified AutoPTU authority.

## Read-only engine evidence

AutoPTU-Java main was inspected read-only at `d2b3c593d235f1c841ca936df91c42c4a881f000`, merged by PR #447 on 2026-09-11. The change adds a parity-safe switch-trigger planner registry and a concrete Quick Switch trigger decision plan with AP requirements, replacement candidates, optional interrupt phase, switch policy and dedupe effects. This is useful evidence for a narrow Trainer Feature / switch-trigger seam. It does not prove the entire action-economy, initiative, reaction, interrupt or Trainer Feature families.

AutoPTU Python main remains read-only at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head explicitly describes a presentation-only battle viewport synchronization change with no rules or outcomes changed.

No engine repository was modified.

## Capability posture retained

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL. PR #447 adds narrow Quick Switch trigger-planning evidence but does not close the family.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING depending on the exact behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated. Quick Switch now has stronger live evidence, but one Feature contract cannot promote the family.

AI legal-action infrastructure: verified only for audited ordinary actions; specialized inspect, brace, escort, protect, retrieve, carry and extract verbs still require explicit admission.

AI tactical policy: BLOCKING for specialized objective policies.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and in-flight recovery.

## Design lesson selected for Ouros

The durable object should preserve the terms that actors actually agreed to. It should not preserve an obsolete copy of the surrounding world. This permits an assistance thread to remain causal without making NPC commitments omnipotent or making save/restart reset opportunity windows.
