# Resource scarcity, imperfect knowledge and world-event integration scan — Pass 247

Status: RESEARCH / PROVENANCE. Not canon by itself.
Date: 2026-09-03

## Scope

Pass 247 connects the finite-resource ledger from Pass 246 to the observation/knowledge contract from Pass 240 and the ecology-driven event contract from Pass 241. It does not approve Squawkabilly, a physical forage species, a numeric carrying capacity, or a new Marea location.

## Internal evidence inspected first

The repository tree, active focus and ecology development program were reviewed before writing. The relevant existing contracts were `design/coupled-ecology-ledger-isolation-contract.md`, `design/observation-evidence-npc-knowledge-contract.md`, and `design/ecology-driven-world-event-consequence-contract.md`, together with the Pass 246 trace/reducer and the existing Marea Fletchling canon. Existing research already covered food aggregation, shorebird habitat partitioning, interspecific nesting associations and Horde encounters, so those sources were not reprocessed here.

## New public research

### Food limitation can change behavior before abundance changes

U.S. Geological Survey, Tinker, Bentall & Estes, “Food limitation leads to behavioral diversification and dietary specialization in sea otters” (2008):
https://www.usgs.gov/publications/food-limitation-leads-behavioral-diversification-and-dietary-specialization-sea-otters

Reusable structure: low food availability can increase between-individual variation in foraging choices and behavior. A population-level resource shortage therefore need not produce one uniform species response.

Ouros use: `resource_pressure` can alter candidate behavior and individual history while population abundance stays unchanged. The event layer must not translate scarcity directly into mortality or emigration.

### Resource pulses can reorganize interaction webs

USGS record, LaMontagne et al., “Mast seeding patterns are asynchronous at a continental scale” (2020):
https://pubs.usgs.gov/publication/70210435

PubMed, Hahus et al., “Periodical cicadas disrupt trophic dynamics through community-level shifts in avian foraging” (2023):
https://pubmed.ncbi.nlm.nih.gov/37856588/

Reusable structure: short resource pulses can cause large behavioral and food-web responses, and consumers can switch foraging targets quickly. Resource recovery can therefore close one pressure window while leaving other ecological effects behind.

Ouros use: resource renewal is an explicit world-state transaction followed by event re-evaluation. It does not reset every pressure, claim or history record to baseline.

### Scarcity can drive movement or diet switching without proving demographic loss

U.S. National Park Service, Northern Hawk Owl species account:
https://www.nps.gov/articles/northern-hawk-owl.htm

U.S. National Park Service, Kit Fox — White Sands National Park:
https://www.nps.gov/whsa/learn/nature/kit-fox.htm

Reusable structure: animals may search more broadly, relocate temporarily or switch foods when prey is scarce. These are behavioral responses. A sighting elsewhere does not by itself prove permanent emigration from the original population.

Ouros use: future scarcity events can increase search radius, alternate-resource intent or local avoidance before any Pass 238 demographic event is authorized.

### Pokémon spin-off pattern: environmental obstacles can structure a mission

Poképédia, Eastern Sea / Pokémon Ranger: Guardian Signs:
https://www.pokepedia.fr/Mer_orientale

The area combines environmental hazards, route constraints and Pokémon-assisted traversal rather than treating every obstacle as a battle.

Reusable structure: an environmental problem can create observation, traversal and intervention beats before structured combat.

Ouros use: a scarcity investigation can remain an overworld ecology problem. If a later authored version uses hazards or Pokémon capabilities to manipulate terrain, those exact PTU/engine capability families must be verified rather than inferred from the Ranger precedent.

### Tabletop community precedent: habitat/tracking can precede roleplay

Pokémon Tabletop forum, “Habitat roller” (2011):
https://www.tapatalk.com/groups/pokemon_tabletop/habitat-roller-t2516.html

Reusable structure: habitat choice and tracking can determine what becomes discoverable before the encounter is roleplayed.

Ouros use: retain the separation between investigation and encounter. Do not import the rarity tables, percentages or tracking procedure as Ouros rules; Pass 240 remains the epistemic authority contract and PTU checks are adopted only through the active rules profile.

## Integration conclusion

The smallest safe next trace uses only the canon Fletchling population plus a fixture-only finite resource. Confirmed consumption reduces the resource and an explicit pressure write raises Fletchling resource pressure. The hidden world state opens a scarcity event. A field observer sees concentrated foraging but does not receive the hidden resource quantity. The observer may form a low-confidence scarcity claim. Repeating the same source does not corroborate it. A separate resource-renewal transaction restores availability, an explicit pressure write lowers pressure, and two clear evaluations resolve the event. The observer's old claim can remain suspected after world truth has changed.

This proves state/knowledge separation in both directions: knowing about scarcity does not create scarcity, and resolving scarcity does not synchronize every NPC belief.

## Canon boundary

The resource node, event thresholds, observer identity and numeric quantities in Pass 247 are fixture-only. The canon Fletchling population is reused as an approved input. No second species is required, so Pass 247 does not advance Squawkabilly from PROPOSED.

## Open questions

Which physical resource exists at lower Sendero remains unresolved. Its renewal model may be seasonal, weather-driven, reproductive, human-maintained or episodic; no option is canonized here. The project also still needs a rules/data policy for how resource pressure changes projection weights and individual foraging radius without turning pressure directly into population change.
