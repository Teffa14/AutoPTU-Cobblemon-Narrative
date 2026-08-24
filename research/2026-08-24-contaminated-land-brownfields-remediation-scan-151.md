# Research Scan 151 — Contaminated Land, Brownfields, Legacy Industry & Remediation

Status: research/provenance only. Not established Ouros canon.
Date: 2026-08-24

## Why this scan exists

The repository already has Soil, Toxicology, Groundwater, Air Quality, Waste/Sanitation, Manufacturing, Architecture, Land Tenure, Public Health, Conservation and Supply Chains. Those layers can establish contamination signals, toxic exposure, waste sources, buildings, ownership/use relations and redevelopment.

What is still missing is a persistent owner for the contaminated site itself across decades: suspected contamination, investigation zones, conceptual source/pathway/receptor hypotheses, land-use restrictions, cleanup phases, residual contamination, verification, long-term monitoring and later reuse.

This pass researches that missing layer. It does not define real-world environmental law, cleanup thresholds, PTU Poisoned, custom hazard damage, contaminant chemistry or Minecraft block effects.

## Existing Ouros boundaries inspected

`design/soil-health-erosion-land-restoration-layer.md` already stores `contamination_ref_ids` and `CONTAMINATION_SIGNAL`, but treats contamination as a linked claim rather than owning the contamination history.

`design/toxicology-poison-exposure-layer.md` owns hazardous agents, source events, exposure opportunities, route-specific exposure, samples, toxicology assessment and decontamination of subjects/objects. It explicitly expects source-owning world systems to establish the environmental source.

Related authorities remain unchanged:

- Groundwater owns aquifers, wells, recharge, plume observations and groundwater-flow claims.
- Freshwater owns surface-water state.
- Air Quality owns atmospheric plumes and deposition.
- Waste/Sanitation owns waste streams and disposal operations.
- Manufacturing owns production history and deviations.
- Architecture owns structures and adaptive reuse.
- Land Tenure owns access/use relations and boundaries.
- Conservation owns ecological management and restoration goals.
- Cases owns allegations, wrongdoing and evidence.
- AutoPTU owns battle Status, hazards and tactical consequences.

## Official Pokémon material

### Grimer

Source: official Pokédex.
https://www.pokemon.com/uk/pokedex/grimer

Grimer is explicitly associated with polluted places. Alolan Grimer is also described as widely used at garbage disposal facilities because it consumes trash.

Reusable structure:

polluted or waste-processing environment -> Pokémon presence adapted to or associated with that environment -> later institutional use of a related population/form.

Ouros lesson: Pokémon presence can be a response to contaminated/waste conditions, a management relationship or both. It must never be treated as proof that the Pokémon caused the contamination. Alolan Grimer also demonstrates that an organism can be institutionally useful around waste without granting a generic purification mechanic.

### Muk

Source: official Pokédex.
https://www.pokemon.com/us/pokedex/muk

Muk is described with highly toxic bodily material and poison-bearing footprints.

Ouros lesson: species-authored toxic material can create a legitimate source hypothesis in a specific incident, but the site layer still needs observations and provenance. A Muk seen on an old industrial parcel cannot retroactively explain contamination that predates its arrival.

### Sparks Fly for Magnemite

Source: official animation page.
https://www.pokemon.com/us/animation/seasons/1/episode-29-sparks-fly-for-magnemite

The episode uses Gringy City as an industrial town where a power-station crisis, pollution, Grimer/Muk and Magnemite intersect.

Reusable structure:

industrial district with accumulated environmental history -> infrastructure failure -> Pokémon presence inside the affected facility -> immediate operational crisis layered over an older environmental problem.

Ouros lesson: the blackout/crisis and the contaminated-city history should remain separate records. Resolving an immediate encounter does not clean the site.

### Big Brother to the Rescue!

Source: official animation page.
https://www.pokemon.com/us/animation/seasons/25/episode-17-big-brother-to-the-rescue

Dirty water displaces one group of Pokémon. Investigation identifies a local pollution source associated with a Grimer nest, and changing that nesting arrangement helps resolve the conflict.

Reusable structure:

visible ecological conflict -> investigate environmental driver -> identify a local source relationship -> alter site use/habitat -> observe recovery.

Ouros lesson: environmental conflict can be resolved by changing physical relationships at a site rather than defeating the Pokémon involved. Even then, long-term recovery should require later observation rather than an immediate `clean=true` writeback.

## Public PTU material

### Campaign Seeds: The Road to Tomorrow — The Last Caravan

Source: official Pokémon Tabletop RPG blog.
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

The campaign seed uses environmental degradation, abandoned infrastructure, scavenging, reconstruction and rediscovery as persistent regional conditions. It also warns against turning survival/resource tracking into repetitive bookkeeping.

Reusable structure:

legacy environmental damage -> abandoned or degraded sites -> recovery choices -> infrastructure and community consequences that persist for generations.

Ouros lesson: a contaminated industrial site should produce decisions about reuse, access, investigation and long-term stewardship, not a repeated contamination meter that must be maintained every session.

### Tales of Visiwa retrospective

Source: official Pokémon Tabletop RPG blog.
https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

The retrospective includes a player-created Weezing engineered in that campaign to consume pollution as part of a chemistry-focused character arc.

Ouros lesson: PTU campaigns can support player-authored scientific or environmental projects, but this is campaign-specific narrative material rather than a universal PTU rule. Ouros must not infer that Weezing purifies contaminated sites, assign rates, or convert a Pokémon into cleanup infrastructure without exact authored/canon and mechanical support.

### GM Advice: Your First PTU Session

Source: official Pokémon Tabletop RPG blog.
https://pokemontabletop.com/gm-advice-your-first-ptu-session/

The article encourages environmental interaction during encounters, including objects and hazards present in an abandoned urban building.

Ouros lesson: contaminated-site scenes can contain meaningful physical evidence and interactables, but any object that becomes a tactical hazard still requires exact engine support. Narrative barrels, drums, dust or puddles cannot invent damage/status mechanics.

## Fan-game / ROM-hack adjacent material

### Pokémon Reborn — Blacksteam Factory and Mosswater Industrial

Sources:
https://pokemon-reborn.fandom.com/wiki/Blacksteam_Factory
https://pokemon-reborn.fandom.com/wiki/Mosswater_Industrial

These locations combine industrial facilities, pollution of a larger water body, exploration, puzzles and antagonist activity. Blacksteam Factory is later replaced by a shelter after city restoration.

Reusable structures:

- industrial pollution can connect a local dungeon to a regional environmental consequence;
- the same parcel can change function later rather than remain a permanent hostile dungeon;
- factory puzzles can use machinery and spatial logic while the surrounding city remembers the old use;
- post-crisis redevelopment can be narratively as important as the infiltration itself.

Ouros adaptation: avoid copying Reborn's factions, lake, fields, puzzles or plot. Reuse only the longitudinal structure: contaminated industrial parcel -> investigation/closure -> cleanup/redevelopment -> new public function with preserved site history.

A useful anti-pattern also appears here. Reborn mechanically defines special battle Fields for factories. Ouros must not create a `Brownfield Field` or `Factory Field` merely because a battle occurs at a contaminated property.

## Brownfield / contaminated-site research

### EPA Brownfields 101 (2026)

Source:
https://semspub.epa.gov/work/04/11185251.pdf

Useful architecture:

- suspected or known contamination is assessed before cleanup design;
- reuse planning can occur alongside site assessment;
- a site's future use affects what cleanup and controls are appropriate;
- community understanding and technical assistance are separate from the physical cleanup.

Ouros adaptation: planned reuse should be a versioned proposal, not proof that the site is ready. `reuse_plan_approved` must not imply `cleanup_complete` or `access_unrestricted`.

### EPA Cleaning Up Brownfield Sites

Source:
https://19january2021snapshot.epa.gov/sites/static/files/2019-10/documents/cleaning_up_brownfield_sites.pdf

Useful cleanup patterns include excavation/removal, capping, tank removal, in-situ treatment and stabilization. Different approaches may leave different residual states and long-term controls.

Ouros adaptation: cleanup actions should be typed, have provenance and produce verification requirements. A capped site may be safe for one use while remaining unsuitable for another; the underlying contamination history remains part of Chronicle.

### EPA Brownfields Road Map / Conceptual Site Model

Source:
https://semspub.epa.gov/work/HQ/160503.pdf

The contaminated-site workflow emphasizes uncertainty, source areas, spatial variation, fate/migration, potential receptors and data gaps.

Ouros adaptation: use a coarse `SITE_CONCEPTUAL_MODEL` that records hypotheses and evidence rather than pretending to simulate contaminant transport at block resolution.

The same roadmap also notes that cleanup itself has environmental effects. This matters for Ouros because excavation, truck traffic, dewatering, vegetation removal or temporary access roads can create new Soil, Air Quality, Noise, Traffic, Wildlife or Public Space consequences even when the remediation objective is legitimate.

### EPA Reuse and Redevelopment Planning

Source:
https://semspub.epa.gov/src/document/HQ/100002010.pdf

Useful design lesson: contaminated-site reuse can include commercial, industrial, recreational or ecological futures, and stewardship can remain necessary after redevelopment.

Ouros adaptation: a former factory can become housing, a park, a workshop district, a research site, habitat, memorial, shelter or mixed-use parcel while still carrying historical restrictions, monitoring wells or an archive of cleanup decisions.

## Core design lessons extracted

1. `CONTAMINATED_SITE` is a persistent place/history object, not a one-time Toxicology incident.
2. Suspected contamination, confirmed contamination and exposure are separate states.
3. A visible Pokémon associated with pollution does not establish the source.
4. Site investigation needs spatial scopes and data gaps; one clean sample never clears the entire property.
5. A cleanup action is not equivalent to verification or closure.
6. Residual contamination may remain with caps, barriers, restricted excavation or monitoring.
7. Reuse is a new site phase, not deletion of the contaminated-site history.
8. Cleanup can itself create temporary ecological, traffic, noise, dust, soil or access consequences.
9. Old infrastructure such as tanks, drains, sumps, fill areas or buried foundations can remain relevant decades after operations cease.
10. Responsibility for contamination must remain separate from the technical finding unless Cases/Institutional Review establishes it.
11. Ecology can colonize abandoned industrial land. Habitat value does not automatically mean the site is safe for unrestricted human access, and contamination does not automatically mean the site is ecologically empty.
12. Minecraft blocks are a presentation of the current revision, not the authority for contamination or cleanup state.
13. A battle can secure access or stop an immediate threat. It cannot determine plume extent, cleanup success, exposure or redevelopment eligibility.
14. Long-term monitoring can make a site narratively valuable years after the dramatic cleanup phase ends.

## PTU / Caelo mechanical guardrails

This scan found no authoritative project rule for a generic contaminated-land combat subsystem.

Do not infer:

- Poison Type = contamination immunity;
- Steel Type = contamination immunity;
- Grimer/Muk/Trubbish/Garbodor presence = contamination source;
- industrial parcel = Factory Terrain;
- stained soil = Rough Terrain;
- sludge = Poisoned or Badly Poisoned;
- dust = Accuracy penalty;
- buried waste = custom hazard zone;
- cleanup PPE = automatic PTU protection;
- decontamination = Status cure;
- contaminated groundwater = Water-type damage modifier;
- removing visible waste = site closure;
- KO/capture of a Pokémon = remediation.

Exact Moves, Abilities, Items, Statuses and environmental protections must remain governed by PTU/Caelo and AutoPTU.

## Source novelty / duplication check

The branch inventory through Pass 150 was inspected before writing. No dedicated brownfield, contaminated-land, legacy-industrial-site or remediation layer was present.

Soil already references contamination but does not own site cleanup history. Toxicology owns exposure. Groundwater/Air/Freshwater own their media. Manufacturing/Waste own operational sources. Architecture/Land Tenure own structures and access. This pass therefore fills a coordination gap rather than replacing those layers.

## Candidate handoffs

Manufacturing/Waste/Material Culture -> historical source/process/container facts.
Soil/Groundwater/Freshwater/Air Quality -> medium-specific observations and migration evidence.
Contaminated Land -> site conceptual model, investigation areas, remediation history, controls, verification and reuse state.
Toxicology/Care/Health Surveillance -> subject exposure and health consequences.
Architecture/Land Tenure/Markets/Public Space -> redevelopment and permitted use.
Conservation/Flora/Wildlife -> habitat response and ecological reuse.
Cases/Institutional Review -> responsibility, allegations and enforcement decisions.
Battle -> only a bounded confrontation after site state and tactical rules have been validated.