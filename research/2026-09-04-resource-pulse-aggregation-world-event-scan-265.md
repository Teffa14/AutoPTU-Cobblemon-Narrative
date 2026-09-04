# Resource-pulse, phenology and temporary aggregation scan — Pass 265

Date: 2026-09-04
Status: RESEARCH / PROVENANCE ONLY. No new canon is established by this note.

## Gap selected

The current ecology program already covers population authority, projection, disturbance, individual response, site-use identity, provisional identity, retention, semantic horizons and aftermath ingress/reconciliation. Migration/dispersal also has prior dedicated work. A repository-wide search found no dedicated contract for short-lived resource pulses, phenological resource waves or temporary feeding aggregations. This pass therefore addresses a distinct gap: how a temporary increase in resource availability can alter encounter visibility and spatial concentration without being mistaken for demographic growth.

## Public sources

### Yang et al. 2008 — resource pulses

Source: Louie H. Yang, John L. Bastow, Kenneth O. Spence and Amber N. Wright, “What can we learn from resource pulses?”, Ecology 89 (2008), DOI 10.1890/07-0175.1.

Reusable lesson: resource pulses are episodes of unusually high resource availability that are large in magnitude, short in duration and meaningful at the spatial/temporal scale of the consumer. They can change consumer behavior, life-history outcomes and community interactions. The review explicitly distinguishes individual behavioral responses from numerical population responses.

Ouros transformation: a pulse can immediately alter where already-existing Pokémon forage or become observable. A demographic response, if one later exists, must be represented by a separate authoritative demographic process. The presence of a pulse never authorizes an instantaneous population increase.

### Yang et al. 2010 — response depends on resource and consumer traits

Source: Louie H. Yang et al., “A meta-analysis of resource pulse–consumer interactions”, Ecological Monographs 80 (2010), DOI 10.1890/08-1996.1.

Reusable lesson: consumer response varies with pulse characteristics and consumer characteristics. A universal multiplier is not ecologically justified.

Ouros transformation: species/context response belongs in explicit response policy. “Food appeared, therefore every nearby Pokémon converges” is invalid. Species, individual history, access, disturbance and context can all change the result.

### Armstrong et al. 2016 — resource waves

Source: Jonathan B. Armstrong et al., “Resource waves: phenological diversity enhances foraging opportunities for mobile consumers”, Ecology 97 (2016), DOI 10.1890/15-0554.1; USGS publication 70173781.

Reusable lesson: ephemeral food resources can become available at different places/times and mobile consumers can track the resulting resource wave. Phenological diversity can matter independently of raw abundance.

Ouros transformation: one world event may change its spatial eligibility over time. Moving the resource event from one site window to another does not assert that any Pokémon teleported, migrated, was forced to move, or even chose to follow it. Actual actor movement remains a separate simulation/tactical claim.

### Pokémon Legends: Arceus — mass-outbreak investigation loop

Source: official Pokémon Legends: Arceus Daybreak update page, The Pokémon Company. It presents mysterious mass outbreaks across Hisui as phenomena the player investigates, including outbreaks at multiple locations.

Reusable structure only: changing ecological-looking phenomena can create an investigation loop based on repeated field visits, comparison between sites and uncertainty about cause.

Ouros transformation: use a temporary resource-driven activity window as a world event that the player can observe across onset, peak, spatial shift and decline. Do not import Hisui, outbreak rules, characters, dialogue or plots. Do not assume an Ouros resource pulse is equivalent to a canonical Pokémon mass outbreak.

## PTU / project mechanical boundary

PTU remains the selected mechanical baseline under project policy. Survival/Perception can support field observation and ecological information where the adopted rules allow it, but a successful check does not reveal private source IDs or convert visible concentration into exact population size.

Kairos remains reference material unless explicitly adopted. The current repository evidence does not provide a local Caelo source pack suitable for a new mechanical claim in this pass; Caelo-specific rules therefore remain unresolved rather than inferred.

## Design conclusions

CANON-ALIGNED: population authority and presentation/projection remain separate; observation does not create population; Minecraft/Cobblemon presentation cannot adjudicate PTU state.

PROPOSED: `RESOURCE_PULSE_EVENT_V1` as an ecological world-event record whose direct outputs are resource availability, projection/activity eligibility and public observational evidence. It may have onset, peak, decline and spatial-wave stages.

PROPOSED: a resource wave can change which site has elevated resource availability while keeping all source identities and demographic totals unchanged.

UNCERTAIN: which resource classes exist in Marea/Sendero, which species respond, response magnitude, pulse duration, recurrence, causal weather relationships and whether any pulse later generates a real demographic effect.

FIXTURE-ONLY: every resource/site/stage value used by the Pass 265 executable trace.

## Anti-overreach rules

Higher visible activity must never be serialized as population growth without a separate demographic event.

A resource event cannot spawn a new persistent actor, alias two sources, set HP/status/Move/Ability/Item/Feature state, or select tactical actions.

A moving resource wave cannot be used as evidence that actors moved between sites. If the full encounter physically moves actors, that behavior must use verified movement and AI capabilities rather than adapter-side shortcuts.

Restart, chunk unload, day/night change and non-detection do not end a pulse. Closure must follow the semantic-horizon contract from Pass 261 or a future explicit authoritative end condition.
