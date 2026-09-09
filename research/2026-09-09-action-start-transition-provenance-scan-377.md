# Action-start transition provenance scan — Pass 377

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-09
Canon effect: NONE

## Repository deduplication

Before selecting sources, the current repository tree and research corpus were searched for the candidate names and themes used here. `Valoryn`, `PTU Campaign - Perspectives` and `Pokémon Prisme` had no prior matches in the narrative repository at the start of this pass. Previously processed sources including Pokémon Nova, Pokémon Stalactite, Pokémon World Tour, Pokémon Rollout!, Pokémon Bushido, Pokémon Rejuvenation, Pokémon Odyssey and other recent research anchors were not reused as primary inspiration.

## Source 1 — Atlassian Jira workflow documentation

Public sources:
- https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-statuses-priorities-and-resolutions/
- https://www.atlassian.com/software/jira/guides/workflows/overview

Reusable structure:
Jira explicitly distinguishes work that is ready to begin from work that is actively being worked on, and models transitions as the one-way bridges between workflow states. The reusable lesson is not software-project management itself. The useful abstraction is that assignment/selection and actual execution are separate historical facts.

Ouros transformation:
A world-agent plan may be selected without any action starting. The first verifiable transition should have its own provenance. Travel begins when semantic edge travel actually starts. Structured resolution begins only when a concrete AutoPTU binding is accepted. Later completion remains separate.

Nothing about Atlassian products, terminology or business process becomes Ouros canon.

## Source 2 — Pokémon Tabletop United: Valoryn Region Campaign

Public source:
- https://www.warwicktabletop.co.uk/events/809/

The public campaign listing describes a PTU setting where exploration, scholarship, factional governance, regulated travel, old secrets and large threats coexist. The opening begins at a much smaller local scale rather than immediately operating at the largest geopolitical layer.

Reusable structure:
A large setting can preserve strong macro-level pressure while individual sessions still turn on small transitions: leaving a settlement, receiving permission, beginning an expedition, crossing a regulated route or deciding to investigate a local disturbance.

Ouros transformation:
Institutional or faction-scale consequences should often become playable through concrete field starts instead of omniscient state changes. An expedition being authorized, selected and actually departing can produce three different facts and three different investigation hooks.

Do not import Valoryn, the Guild Concord, its Titans, seals, factions, characters, settlements, events or plot.

## Source 3 — PTU Campaign: Perspectives

Public source:
- https://www.reddit.com/r/PokemonTabletop/comments/1pap4qc/ptu_campaign_perspectives_13/

The public recruitment post uses environmental detail in a damaged cavern to communicate prior disruption, unstable conditions and surviving ecology before the larger context is fully explained.

Reusable structure:
Environmental evidence can reveal that an action began even when the actor is absent. Disturbed equipment, opened barriers, fresh tracks, abandoned survey markers or a partially crossed route can function as evidence of execution rather than merely intention.

Ouros transformation:
A mystery can ask whether a team only planned to leave, actually departed, or departed and was interrupted. The environment should expose action-start evidence without automatically explaining cause, success or outcome.

Do not reuse the post's descriptive prose, exact cavern setup, characters, unexplained figure, crystal imagery or plot.

## Source 4 — Pokémon Prisme

Public source:
- https://pokemonprisme.com/

The public project page advertises broad regional travel and a separate side-quest journal alongside the main progression.

Reusable structure:
A persistent world benefits when side obligations and regional travel have durable state independent from the main plot.

Ouros transformation:
Action-start provenance allows a side expedition, courier run, survey trip or repair job to leave a durable historical trace even if the player continues elsewhere. Later consequences can query whether the job was selected, started or completed instead of treating the quest journal as a binary active/done flag.

Do not import Prisme's regions, progression, quest content, characters or implementation.

## Resulting design lessons

The next durable causal chain should remain queryable as:

`TRIGGER_CONSUMED -> PLAN_SELECTED -> ACTION_STARTED -> ACTION_COMPLETED/FAILED`

For structured mechanics:

`PLAN_SELECTED -> REQUEST_AUTOPTU -> AUTOPTU_BINDING_ACCEPTED -> AUTOPTU_RESULT_INGRESSED`

Useful environmental-storytelling evidence can point to `ACTION_STARTED` while leaving success, failure and cause unresolved.

A selected expedition that never leaves camp and an expedition that leaves camp but never reaches its destination must remain distinguishable after restart.

## PTU / Caelo boundary

Internal project material remains authoritative for rules and setting: PTU Core, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and the Caelo Region Location & Encounter List when available.

This pass adds no species placement, Move rule, Ability, Item, Trainer Feature, regional geography or Caelo fact. Public research informs structure only.

## Read-only engine evidence

AutoPTU-Java head inspected: `948f42cfcfd34000087cb0667b4926c9aa2c8df4`, merge #414. The live head wires admitted round-start Ability dispatch into the authoritative lifecycle after the relevant Trainer Feature dispatch seam. This remains evidence for that specific lifecycle integration and does not prove the entire Ability, reaction or turn/round lifecycle categories.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change is explicitly presentation-only and does not alter battle rules or outcomes.

Neither engine repository was modified.
