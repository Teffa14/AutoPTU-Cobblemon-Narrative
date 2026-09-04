# Shared-resource multi-species ledger isolation scan — Pass 246

Status: RESEARCH / PROVENANCE. Not canon by itself.
Date: 2026-09-03

## Purpose

Close the next integration gap after Pass 245: prove that one ecological cause can affect multiple actor/population ledgers without silently changing abundance, identity, or unrelated history.

This pass deliberately does not approve a second Marea species. It reuses the already-PROPOSED Squawkabilly candidate from Pass 226 solely inside a non-canon implementation fixture. The finite forage patch is also fixture-only.

## Internal evidence checked first

- `canon/marea-interior-first-wild-population-v1.md`: Fletchling is the only canon-approved wild population in this slice; the first persistent actor is fixed.
- `design/interspecies-ecological-relations-layer.md`: shared-resource use and resource competition are distinct ecological relations; pressure is world state, not a combat modifier.
- `research/2026-09-03-marea-interspecies-predation-territory-scan-226.md`: Squawkabilly remains PROPOSED locally. Official species material supports a Fletchling/Squawkabilly territorial relationship, but local activation still requires an actual shared site/resource.
- `proposals/2026-09-03-marea-sendero-species-interaction-matrix-226.md`: the contested lower shelf was already proposed but explicitly gated on Squawkabilly approval and a concrete resource.
- `design/ecology-event-replay-contract.md`: deterministic replay may consume ecology-domain events but must not infer PTU outcomes or trust Minecraft UUID state.
- `design/ouros-source-authority-and-species-policy.md`: Caelo/Kairos are comparative sources; external content and rules never become Ouros canon automatically.

## New public research

### Resource distribution changes competition without requiring demographic loss

Sarah Richman et al., “Nonlinear effects of food aggregation on interference competition in mallards,” Behavioral Ecology and Sociobiology, 2010.
https://pmc.ncbi.nlm.nih.gov/articles/PMC2952768/

Reusable structure:
- the same total food can produce different access costs depending on how clumped it is;
- subordinate individuals can be excluded from high-quality patches while still achieving some intake elsewhere;
- spatial resource structure can therefore change individual behavior before population totals change.

Ouros use:
A finite patch can alter `resource_pressure`, avoidance, time spent at the patch, or displacement before any birth/death/emigration event occurs. A consumption event changes the resource ledger only; demographic writeback needs its own authority.

### Shared space can alternate between partitioning and crowding

Burger et al., “Effects of tide cycles on habitat selection and habitat partitioning by migrating shorebirds,” The Auk, 1977, USGS record.
https://www.usgs.gov/publications/effects-tide-cycles-habitat-selection-and-habitat-partitioning-migrating-shorebirds

Reusable structure:
- multiple species can use the same broad habitat but partition microhabitats and time;
- when usable space compresses, crowding and agonistic interactions increase;
- timing of resource access can be driven by environmental windows rather than fixed day/night behavior.

Ouros use:
The same lower-Sendero resource can support peaceful temporal partitioning in one window and contested access in another. The world event should change overlap/pressure rather than flip a permanent `HOSTILE` flag.

### Aggregation has context-dependent costs and benefits

Mouton & Martin, “Fitness consequences of interspecific nesting associations among cavity-nesting birds,” The American Naturalist, 2018, USGS record.
https://www.usgs.gov/publications/fitness-consequences-interspecific-nesting-associations-among-cavity-nesting-birds

Reusable structure:
Interspecific aggregation can simultaneously create resource competition and reduce another risk. The effect changes with resource abundance and predation pressure.

Ouros use:
A repeated mixed-species cluster should not be auto-labelled friendship, mutualism, or competition. Persist the observed shared-resource relation and separate pressure/evidence fields.

### Pokémon precedent: mixed assemblage does not imply one tactical team

Pokémon X/Y Horde Encounters, summarized by Bulbapedia:
https://bulbapedia.bulbagarden.net/wiki/Horde_Encounter

Reusable structure:
Mixed-species groups can exist in one encounter, and some known rival species can direct actions at each other instead of the player.

Ouros use:
Co-presence is not team membership. A shared-resource aggregation can contain actors with different goals. This is inspiration only; Ouros does not import Horde battle targeting/range rules.

### PTU community pattern: situation-first wild encounters

Public PokémonTabletop discussions:
https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5
https://www.reddit.com/r/PokemonTabletop/comments/jivcud
https://www.reddit.com/r/PokemonTabletop/comments/1vs58fn/have_you_used_sos_and_horde_battles_in_your/

Reusable structure:
GMs repeatedly describe stronger wild encounters when Pokémon are doing something in the world—territorial disputes, herd behavior, visible signs, reinforcement—rather than existing only as random battle entries. Large multi-actor PTU fights can also become expensive to run.

Ouros use:
Keep most shared-resource competition in overworld/ecology state. Escalate only the immediate participants if structured mechanics are actually required.

## Pass 246 design conclusion

The smallest safe integration test is:

1. canon Fletchling population and persistent actor;
2. fixture-only proposed Squawkabilly population;
3. fixture-only finite forage patch;
4. explicit resource-use observation that does not consume anything;
5. confirmed consumption transactions that decrement only the resource;
6. scoped individual/population pressure updates;
7. no population-count change because no demographic event occurred;
8. restart and deterministic replay.

The fixture is intentionally non-canon. It tests architecture while leaving the two required content decisions unresolved: whether Squawkabilly belongs in Marea and what resource actually exists at the lower shelf.

## Canon questions retained

- Is Squawkabilly approved as Marea's second wild species?
- Which plumage/form, if any, is locally present?
- What exact physical resource could Fletchling and Squawkabilly both use at lower Sendero?
- Is the resource renewable, seasonal, episodic, or a stable site?
- Which observations are strong enough to upgrade `SHARED_RESOURCE_USE` into `RESOURCE_COMPETITION`?
