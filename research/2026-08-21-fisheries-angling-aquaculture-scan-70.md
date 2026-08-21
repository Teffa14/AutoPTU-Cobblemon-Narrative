# Fisheries, Angling & Aquaculture Research Scan — Pass 70

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-21

## Gap checked

Existing layers already cover freshwater hydrology, maritime travel, food/agriculture, conservation, wild collectives, interspecies ecology, biosecurity, workplaces and Pokémon agency. `FISHERY` appears as a possible site type and `FISHING_VESSEL` as a maritime asset, but no dedicated layer tracks fishing effort, catch/release, stock observations, seasonal access, hatchery releases, aquaculture or monitoring of stocked versus naturally recruited populations.

## Public Pokémon sources

Official Brilliant Diamond/Shining Pearl Trainer Guide:
https://diamondpearl.pokemon.com/en-au/trainersguide/fundamentals/

Fishing and Surf can expose different Pokémon even in the same general water body, and different rods can change what is encountered. Ouros should therefore keep encounter method separate from the underlying aquatic population.

Official fishing competition episode:
https://www.pokemon.com/us/animation/seasons/14/episode-37-a-fishing-connoisseur-in-a-fishy-competition

Reusable structure: fishing can support public competition, expertise, spectatorship, rivalry and event disruption without making every participant a battle combatant.

Official Whiscash episode:
https://www.pokemon.com/us/animation/seasons/7/episode-35-whiscash-and-ash

Reusable structure: a famous aquatic Pokémon can be a persistent individual with a long sighting history rather than a replaceable random spawn.

Official Brooklet Hill episode:
https://www.pokemon.com/us/animation/seasons/20/episode-33-big-sky-small-fry

Reusable structure: fishing can combine observation, welfare, skill demonstration and battle while keeping those outcomes separate.

Official Pokédex:
https://www.pokemon.com/us/pokedex/qwilfish
https://www.pokemon.com/us/pokedex/spinarak
https://www.pokemon.com/us/pokedex/veluza
https://www.pokemon.com/us/pokedex/arrokuda
https://www.pokemon.com/us/pokedex/wishiwashi

These sources support high-level ideas such as species-specific fishing knowledge, locally made gear, biological resources that do not necessarily imply capture, food-web relationships and aggregation/dispersal. None of that creates PTU bonuses or yields by itself.

## PTU community material

Fishing tournament discussion:
https://www.reddit.com/r/PokemonTabletop/comments/jh12kh

Reusable structure only: divide one lake into meaningful habitat zones, allow scouting and Pokémon assistance before combat, and use an objective other than defeating every opponent. Do not copy the exact scoring, team composition or encounter sequence.

Nonviolent encounter discussion:
https://www.reddit.com/r/PokemonTabletop/comments/1fta66r

Reusable structure: fishing works well as low-stakes travel content and can resolve without battle.

## Fangame material

Karpe Diem:
https://www.eeveeexpo.com/karpe-diem/

Reusable structure: a recurring fishing festival can combine local tradition, visitors, rivals, records, market activity and puzzles. Do not copy its characters, region or plot.

Pokémon Peaceful Fishing Wii:
https://eeveeexpo.com/threads/9175/

Holly Goes to the Lake:
https://eeveeexpo.com/holly-goes-to-the-fcking-lake/

Reusable structure: fishing can support a dedicated observation/collection loop outside battle. Ouros can keep an angling journal without treating every entry as a captured Pokémon.

## Fisheries and aquaculture research

NOAA area/time closure guide:
https://repository.library.noaa.gov/view/noaa/41981/noaa_41981_DS1.pdf

Reusable structure: closures can have different purposes such as spawning protection, rebuilding, habitat protection, bycatch reduction or conflict management. Ouros should record reason, scope and duration instead of a generic `FISHING_CLOSED` flag.

FAO hatchery monitoring guidance:
https://www.fao.org/docrep/015/i2428e/i2428e.pdf

Reusable structure: stocking is an intervention that requires later monitoring. Released individuals or cohorts should remain distinguishable from natural recruitment where evidence allows.

FAO stocking/aquaculture infrastructure guidance:
https://www.fao.org/4/ap976e/ap976e.pdf

Reusable structure: repeated stocking depends on hatchery capacity, trained staff, transport, release timing and follow-up monitoring. No real-world production ratios or legal rules are imported.

## Design conclusions

Fishing effort and stock state must remain separate. A poor catch can reflect abundance, distribution, season, gear, effort, schooling, water state or reporting.

Angling, capture, harvest, sampling and release are separate outcomes. A hooked Pokémon is not automatically captured or retained.

Minecraft loaded entities cannot be the source of truth for a fishery. Use coarse persistent stock/cohort state and project a controlled visible sample.

Hatchery output is not the same as wild recruitment. A release can succeed, fail, disperse or create unexpected effects.

Famous aquatic Pokémon should keep persistent identity across sightings.

Fishing can support profession, hobby, science, tourism, food culture, mentorship and conservation without mandatory combat progression.

## PTU/Caelo guardrail

The primary Caelo corpus was not reliably retrievable for an exact fishing-rule extraction in this run. This pass therefore does not assert rod mechanics, bait bonuses, fishing Skill DCs, net mechanics, hooked statuses, harvest yields, hatchery growth rates, stocking bonuses or Fishing-specific Trainer Features.

Existing project evidence confirms explicit capture and movement rules, but that does not prove a general fishing subsystem.

## Copyright boundary

Only high-level structures and factual public information were reused. No protected dialogue, distinctive fangame characters, detailed plots or exact encounter scripts were copied.
