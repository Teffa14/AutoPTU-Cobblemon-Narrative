# Migration, stopover and temporal niche scan — Pass 235

Status: RESEARCH / PROVENANCE
Date: 2026-09-03
Scope: ecology programme pass 235

## Question

How should Ouros represent migration, seasonal range use and time-of-day niches without collapsing them into random encounter-table rotation or spawning new population truth?

## Existing-project constraints checked before this pass

This pass extends, rather than replaces:

- `design/ecology-development-program.md`;
- `design/ecological-pulse-event-contract.md`;
- `design/ecological-information-propagation-contract.md`;
- `design/wild-nesting-juvenile-parental-care-contract.md`;
- `design/cobblemon-native-spawn-projection-contract.md`;
- `design/ecology-observation-intervention-contract.md`.

The main distinction from ecological pulses is persistence of movement history. A pulse can make resident animals more visible without moving the population. Migration requires an origin, one or more transit/stopover areas, a destination or seasonal range, and tracked progress through that route.

## Public source findings

### 1. Pokémon franchise: moving distribution is an established pattern, but gameplay abstractions are not literal ecology by default

The core series has repeatedly used roaming wild Pokémon whose location changes across a region. Bulbapedia's sourced overview records official terminology including roaming, migrating and wandering Pokémon and notes region-scale movement rather than a single fixed encounter location.

Source:
- Bulbapedia, `Roaming Pokémon` (secondary index to game/manual terminology), retrieved 2026-09-03: https://bulbapedia.bulbagarden.net/wiki/Roaming_Pok%C3%A9mon

Design lesson:
- the franchise already tolerates individual wild Pokémon whose encounter location is a changing world fact;
- Ouros can use this as precedent for persistent moving individuals or cohorts;
- the legacy roaming mechanic must not be copied literally as random route teleportation unless a species/source explicitly supports that behavior.

### 2. Pokémon franchise: species can support long-distance movement and flock-level coordination

Swanna Pokédex material describes strong long-distance flight capability and coordinated flock behavior with a central leader. This is useful evidence that some Pokémon species can plausibly support group-scale movement over large geographic distances.

Source:
- Bulbapedia, `Swanna (Pokémon)` compiling main-series Pokédex entries, retrieved 2026-09-03: https://bulbapedia.bulbagarden.net/wiki/Swanna_(Pok%C3%A9mon)

Design lesson:
- migration eligibility should be species-specific and capability-backed;
- social organization can affect route choice, departure thresholds and cohesion;
- this source does not itself prove that every Swanna population is seasonally migratory.

Provenance grade for any Ouros inference from this source: `SPECIES_TRAIT_STRONG` at most until primary-source wording is independently pinned.

### 3. Pokémon Legends: Arceus: regional distribution changes can become an investigation loop

The official Daybreak page presents mass outbreaks across multiple places in Hisui, tied to rainstorms, as a phenomenon to investigate rather than merely a battle queue.

Source:
- The Pokémon Company, `Pokémon Legends: Arceus | Update`, retrieved 2026-09-03: https://legends.arceus.pokemon.com/en-au/update/

Design lesson:
- changing distribution is stronger when it creates field evidence and questions;
- weather-associated concentration can alter what the player sees without proving net population growth;
- this pattern belongs to pulse ecology unless actual individuals/cohorts move between areas.

### 4. PTU community travel design: travel works better when route events express the world rather than only interrupting movement

A Pokémon Tabletop community discussion about travel/exploration describes encounter buckets, environmental events, wild conflicts and optional route discoveries as ways to make travel consequential. Another community example frames living-world play as a persistent world where characters can affect changing conditions rather than advancing only through one campaign script.

Sources:
- Reddit r/PokemonTabletop, `First Time GM here, how do y'all GM Travel/Exploration`, 2024-12-02: https://www.reddit.com/r/PokemonTabletop/comments/1h4k1ui/
- Reddit r/PokemonTabletop, `Hexceawl travel tips or traveling tips?`, 2025-04-24: https://www.reddit.com/r/PokemonTabletop/comments/1k6z1wy/
- Reddit r/PokemonTabletop, `Kehalo Season 4 ~ Come Join!`, 2025-04-12: https://www.reddit.com/r/PokemonTabletop/comments/1jxrz43/

Design lesson:
- Ouros should not roll migration as a context-free random encounter;
- a migration crossing should change route use, observation opportunities, local resources and later world state;
- players should be able to alter their route, wait, observe, escort, protect, exploit or avoid the event.

These sources are community practice, not PTU rules authority.

### 5. Migration ecology: stopover sites are part of the route, not empty gaps between endpoints

USGS reviews emphasize that migrants depend on en-route habitats and that distribution, timing, habitat quality and migratory connectivity are essential to understanding population outcomes. Stopover areas can be especially important around geographic barriers.

Sources:
- Cohen et al., 2017, USGS, `How do en route events around the Gulf of Mexico influence landbird populations`: https://www.usgs.gov/publications/how-do-en-route-events-around-gulf-mexico-influence-landbird-populations
- Carlisle et al., 2009, USGS, `Landbird migration in the American West`: https://www.usgs.gov/publications/landbird-migration-american-west-recent-progress-and-future-research-directions

Design lesson:
- an Ouros migration route needs habitat nodes and corridors, not just origin/destination IDs;
- stopover quality should affect dwell time, condition and onward movement pressure;
- removing or degrading one stopover can create delayed consequences elsewhere.

### 6. Migration ecology: individuals can have repeatable timing but still respond to conditions

A 2022 meta-analysis found moderate repeatability in individual migration timing across studied birds, while also finding room for variation from conditions encountered during the journey and breeding outcomes.

Source:
- Wellbrock et al., 2022, Journal of Animal Ecology / PubMed: https://pubmed.ncbi.nlm.nih.gov/35385132/

Design lesson:
- Ouros should preserve an individual's or cohort's timing tendency instead of rolling every migration independently each year;
- weather, condition, resource state, life stage and prior outcomes can shift actual departure/arrival around that baseline;
- population-level phenology can change because individuals respond differently or because cohort composition changes.

### 7. Migration ecology: stopover departure depends on condition, resources and weather

Stopover research describes energy stores and refueling rate as important factors in departure probability, while predation, weather and other intrinsic/extrinsic factors also matter. Fuel-deposition studies show that food availability, predictability, moult and seasonal diet can reorganize migration behavior.

Sources:
- Schmaljohann et al., 2017, stopover departure review / PubMed: https://pubmed.ncbi.nlm.nih.gov/28332031/
- Schaub & Jenni, 2001, fuel deposition across migration route / PubMed: https://pubmed.ncbi.nlm.nih.gov/28308281/

Design lesson:
- `arrival_at_stopover` must not imply `depart_next_tick`;
- departure pressure can be computed from condition, resource access, threat/disturbance and time window;
- a route can fail because a stopover no longer supports replenishment, even if the physical corridor remains open.

### 8. Migration ecology: temporal niche matters at the scale of a day, not only a season

Research on nocturnal migrants shows departure decisions can have a specific time-of-day component. Artificial night lighting is also associated with high stopover density and can create an ecological trap rather than a beneficial habitat.

Sources:
- Eikenaar et al., 2020, diel departure decision / PubMed: https://pubmed.ncbi.nlm.nih.gov/32217064/
- Horton et al., 2023, artificial light and stopover density / PubMed: https://pubmed.ncbi.nlm.nih.gov/38049435/

Design lesson:
- a Pokémon population may occupy the same broad region but use different corridors/resources by day, dusk, night or dawn;
- attraction does not equal habitat quality;
- human light, sound or activity can increase apparent presence while worsening ecological outcomes.

### 9. Disturbance does not have a universal response

USGS work on songbird stopovers after hurricanes found that some migrants continued using heavily disturbed stopover habitat, showing that disturbance response should not be hard-coded as universal abandonment.

Source:
- Lain et al., 2017, USGS, `Songbirds are resilient to hurricane disturbed habitats during spring migration`: https://pubs.usgs.gov/publication/70191603

Design lesson:
- migration-route response must be species/population-specific;
- disturbance can lower resource quality without immediately eliminating use;
- persistence at a degraded stopover can itself create risk and downstream condition debt.

## PTU / Kairos cross-check

Project-supplied Kairos source index routes relevant questions to:

- world population/ecosystem guidance around pp. 437+;
- encounter creation around pp. 470+;
- movement/terrain around pp. 382+;
- terrain/weather around pp. 404+;
- Survivalist and Topographer as available utility-class concepts;
- Kairos living-world hunting selected by island/region, biome and requested level range.

Source:
- `sources/kairos/KAIROS_SOURCE_INDEX.md`.

Ouros interpretation:
- PTU/Kairos provides mechanical and living-world reference points but does not authorize a hidden tactical simulation for migration;
- route knowledge, navigation, tracking and field observation can inform what a Trainer learns or attempts;
- a migration system belongs to persistent Ouros ecology until explicit structured mechanics begin;
- Kairos's hunt workflow is evidence that biome/region choice matters in living-world play, but Ouros should go further by making availability emerge from persistent seasonal state.

No Kairos homebrew rule is imported by this pass.

## Proposed reusable structures

### Migration modes

Candidate ecology-level modes:

- `SEASONAL_RANGE_SHIFT`: recurring movement between seasonal ranges;
- `BREEDING_MIGRATION`: movement toward reproduction/nesting areas;
- `RESOURCE_TRACKING`: movement following food/water/resource availability;
- `WEATHER_ESCAPE`: directional displacement with a likely return window;
- `DISPERSAL`: one-way or weakly recurrent movement away from natal/current range;
- `ALTITUDINAL_SHIFT`: movement between elevation bands;
- `DIURNAL_COMMUTE`: repeated within-day movement between resting/feeding/social areas;
- `NOMADIC_WANDER`: non-fixed movement driven by resource patches rather than a stable annual route.

Do not map these automatically from real animal analogues. Each species/population needs Pokémon evidence or an explicitly labeled Ouros inference.

### Route model

A migration route should minimally contain:

```yaml
migration_route_id: null
population_or_cohort_id: null
mode: null
origin_range_id: null
destination_range_id: null
corridor_ids: []
stopover_site_ids: []
seasonal_window: null
diel_window: null
baseline_direction: null
route_fidelity: null
known_alternates: []
provenance: []
status: PROPOSED
```

### Stopover state

```yaml
stopover_site_id: null
resource_capacity: null
shelter_capacity: null
threat_pressure: null
human_disturbance: null
artificial_attraction: null
occupancy_pressure: null
recovery_rate: null
```

### Moving cohort state

```yaml
cohort_id: null
population_id: null
member_refs: []
estimated_count: null
current_route_segment: null
progress: null
condition_distribution: null
arrival_time: null
planned_departure_pressure: null
leader_or_route_memory_refs: []
observation_confidence: null
```

`estimated_count` does not authorize creation/destruction of individuals. The authoritative population ledger remains upstream.

## Critical invariant

Migration changes where existing ecological population truth is expressed.

It must not become:

```text
season changed -> delete old spawns -> create replacement population elsewhere
```

Preferred authority flow:

```text
persistent population/cohort state
-> migration trigger + route eligibility
-> movement through semantic route graph
-> stopover occupancy and resource effects
-> local Cobblemon availability/projection
-> player/NPC observation
-> optional Ouros-to-AutoPTU handoff
-> outcome returns to route/population state
```

## Relationship to ecological pulses

A migration can create a local pulse, but the two concepts remain separate.

Example:
- fifty tracked cohort members arrive at a stopover: migration + local concentration pulse;
- resident Pokémon become unusually visible after rain without moving between regions: pulse only.

This distinction prevents false population movement.

## Quest and encounter structures enabled

### Delayed arrival mystery

Expected cohort fails to arrive during its usual window. Evidence can point to:
- resource failure at an earlier stopover;
- corridor obstruction;
- changed weather timing;
- human disturbance;
- predation pressure;
- a legitimate shift to an alternate route.

The player investigates causes rather than being told the answer by omniscient quest state.

### Stopover debt

A cohort reaches Marea in poor condition because an upstream stopover was degraded. The local problem appears in Marea, but the causal site is elsewhere. This creates geographic consequence chains without teleporting narrative truth.

### Crossing management

A route temporarily intersects a human trail or transport corridor. Players can observe, redirect people, reduce disturbance, escort researchers or exploit the concentration. Outcomes affect trust, local resources and later route fidelity.

### Ecological trap

A human-altered site attracts a migrating species but provides poor survival/resource outcomes. Presence alone therefore cannot be interpreted as habitat success.

## Engine dependency note

Pure migration, stopover occupancy, temporal niche selection, observation and route-state consequences require no AutoPTU tactical family.

If a migration event becomes structured combat, exact dependencies must be declared. Rich variants may require:

- complete movement for escort, interception or forced displacement;
- full lifecycle for multi-phase objectives;
- stateful damage/status only if combat actually uses them;
- terrain/weather/hazards/zones/reactions for environmental crossing pressure;
- move/ability/item/Trainer Feature families when explicitly invoked;
- AI tactical policy for autonomous escort, protective, escape or route-seeking objectives;
- Minecraft/Cobblemon/Craftics adapter/playback for faithful world presentation and writeback.

Reduced variants should keep migration in Ouros world state, pause or abstract the transit during any simple supported AutoPTU battle, then resume from semantic results.

## Unresolved questions

- How large can a moving cohort be before individual identity must be partially aggregated?
- Which species/populations get stable route fidelity versus opportunistic movement?
- How much stopover resource use feeds back into resident populations?
- How are cohort splits/merges represented without duplicating population truth?
- How does weather alter departure timing without automatically becoming tactical weather?
- How are migration observations transmitted through NPC institutions without omniscience?
- Which real generated Ouros corridors and stopovers are valid after the global world substrate is frozen and indexed?

## Next design action

Define the persistent migration/stopover contract, then add a Marea fixture that remains species-agnostic until real worldgen biome and Cobblemon native-spawn compatibility are verified.
