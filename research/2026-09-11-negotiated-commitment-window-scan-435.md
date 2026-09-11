# Negotiated Commitment Window Scan — Pass 435

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-11

## Repository inspection and duplicate control

The full recursive repository tree at `321e99f08da866b19ba0da33247ebb4c58207f54` was inventoried before writing. Current focus, canon inventory, Passes 422–434, world-action persistence, ordinary assistance commitments, counterproposal terms, requester decisions, world scheduling, Kairos routing material and recent research files were checked before selecting the slice.

Repository search found no prior named use of Battle Brothers contract negotiation and no prior `Mimikyu Quest` / Dressa reference. The distinctive PTU Oranguru / festival / drought / diseased-tree campaign-log material also returned no repository match. Frequently reused anchors such as Roadwarden, Pentiment, Citizen Sleeper, Six Ages, Heaven's Vault, Pyre, Unsighted, Pokémon Unbound, Pokémon Gaia and Pokémon Desolation were not reused as primary sources.

## Public source 1 — Battle Brothers contract negotiation

Source:
https://www.moddb.com/games/battle-brothers/news/how-contracts-will-work-part-1

The public developer article describes contracts as offers that can be negotiated before acceptance. Different payment structures can be proposed, and accepted work remains a later obligation rather than an immediate completion event. Time limits and mutually contradictory contracts also exist in the broader contract structure.

Reusable abstraction for Ouros:

A changed offer needs an explicit agreement, and agreement should produce a bounded obligation rather than execute the work. Terms agreed during negotiation should constrain the later commitment instead of being silently rewritten by the scheduler.

Excluded:

No mercenary economy, payment math, factions, contract plots, reputation system or prose is imported.

## Public source 2 — PTU campaign log #22

Source:
https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t/campaign_log_22/

The public session recap describes a town festival, Pokémon behavior, environmental symptoms, information gathered through interaction and a drought problem traced to a diseased tree. The group obtained information about a cure and resolved the local problem without the reported scene being structured solely around defeating opponents.

Reusable abstraction for Ouros:

A scheduled specialist visit can retain a narrow negotiated scope such as observation, diagnosis or treatment advice. Arrival at a problem site does not imply permission or necessity to escalate into combat. Environmental evidence can alter what the later appointment actually needs while the original promise remains historically intact.

Excluded:

No named characters, exact festival, exact disease, species lineup, dialogue or cure sequence is imported.

## Public source 3 — PokeXGames Mimikyu Quest

Source:
https://wiki.pokexgames.com/index.php/Mimikyu_Quest

The public quest documentation uses an NPC with temporal availability and a delayed follow-up: after the requested study material is delivered, a later reward step waits on elapsed time and the NPC's presence schedule.

Reusable abstraction for Ouros:

World time and actor availability can matter after agreement. A promise can exist before the actor is physically present at the relevant place. The scheduler should preserve the agreed window while travel/presence remain separate state owners.

Excluded:

No reward, NPC identity, Mimikyu-specific story, item drop loop, geography or MMO timer is imported.

## Combined design lesson

These sources support a three-part separation:

1. negotiate and explicitly accept concrete terms;
2. create a durable time-bounded obligation owned by the actor who promised the work;
3. later determine travel, access, resources and scene resolution from current world state.

This is useful for Ouros because it permits believable appointments, inspections, escort windows, training sessions, repair work and research visits without turning communication into teleportation or turning narrative scope into tactical legality.

## PTU / Caelo / Kairos cross-check

The repository source inventory was rechecked. `sources/en/` contains the project's PTU textual material, including GM/encounter guidance, while `sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid and explicitly does not make referenced rules Ouros canon. The recursive inventory did not expose a standalone `sources/caelo/` directory; therefore this pass does not infer a Caelo-specific rule that is not present in the inspected source surface.

The new commitment bridge is world-simulation scheduling. It does not need PTU tactical rules to exist. If a later appointment becomes a structured encounter, the exact involved mechanics must be admitted individually.

## Live engine evidence checked

AutoPTU-Java `main` was checked at `536e495e91e28d65637e4f2af2ebd06bcf262940` (PR #446, Quick Switch entry contract). The evidence freezes and tests a specific Quick Switch/replacement-entry path. It does not verify the complete action economy/initiative family, complete lifecycle, generic reactions or Trainer Feature interrupt coverage.

AutoPTU Python `main` remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is presentation-only and explicitly does not change battle rules or outcomes.

Neither engine repository was modified.

## Capability classification for the mechanically rich extension

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL. Quick Switch evidence remains a narrow verified path, not family completion.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior: individually gated.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated. PR #446 adds evidence for Quick Switch entry semantics only.

AI legal-action infrastructure: VERIFIED only for audited ordinary actions. Specialized inspect, brace, rescue, escort, protect, retrieve, carry and extract still require explicit admission.

AI tactical policy: BLOCKING for specialized objective behavior without dedicated evidence.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and in-flight recovery.

## Reduced implementation lesson

The reduced version needs only semantic time, durable proposal/decision history, an ordinary scheduled commitment and later world-state checks. A specialist can keep an appointment, inspect a condition, write a report or discover that the problem changed. No knockback, reaction, status, weather phase or special move needs to be emulated.

## Open questions

The new negotiated commitment linkage and the counterproposal ledger still need coherent checkpoint integration.

`location_ref`, `scope_ref` and `alternative_ref` are preserved as negotiated metadata but are not yet normalized machine-authoritative contracts.

Travel reservation, resource allocation, access permission and specialized action admission remain downstream owners.

A policy is still needed for what happens when an accepted appointment becomes impossible before its window because of route closure, new evidence, injury or another hard obligation.
