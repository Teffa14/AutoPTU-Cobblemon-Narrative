# Pass 176 Research — Pokémon Spatial Ecology, Home Ranges, Site Fidelity & Territoriality

Status: RESEARCH / PROVENANCE ONLY
Canon status: NON-CANON until separately approved
Date: 2026-08-26

## Why this scan exists

The repository already has strong authorities for migration, telemetry, nesting, urban wildlife, wayfinding, land tenure and persistent Pokémon identity. The missing question is smaller and local: how does an individual, pair or collective repeatedly use space when it is not performing a long-distance migration?

This scan focuses on:

- home ranges and core-use areas;
- repeated use and site fidelity;
- excursions outside ordinary use areas;
- range overlap;
- territorial displays and defended subareas;
- changes in local space use after infrastructure, resource or social changes;
- uncertainty caused by incomplete observation.

It does not define land ownership, migration corridors, nesting state, population abundance, Minecraft spawn logic or PTU battle mechanics.

## Existing Ouros boundaries checked before writing

### Wildlife Migration, Stopovers & Corridors

`design/wildlife-migration-stopovers-corridors-layer.md` already owns repeated seasonal or condition-linked movement across multiple locations, corridor revisions, stopovers, migration episodes and partial migration.

Pass 176 must not turn ordinary local use into a migration episode.

### Wildlife Telemetry

`design/wildlife-telemetry-tagging-movement-monitoring-protocol.md` owns devices, deployments, receiver stations, detections, fixes and derived movement segments. It explicitly hands ecological interpretation elsewhere.

Pass 176 may consume validated fixes, but cannot alter raw detections or pretend a straight line between fixes was the animal's true path.

### Urban Wildlife

`design/urban-wildlife-synanthropy-coexistence-layer.md` owns repeated use of human-built environments, attractants, habituation, food conditioning, urban roosts/nests and conflict/coexistence interventions.

Pass 176 may describe the spatial footprint of an urban individual or group, but Urban Wildlife remains authoritative for the human-built relationship and attractants.

### Wild Nesting / Juvenile Dispersal

Nesting owns reproductive sites, dependency and natal dispersal. A defended nest-area observation can inform a spatial assessment, but Pass 176 must not infer parentage, brood state or abandonment.

### Land Tenure

Human property, passage, occupancy and use permissions remain separate. A Pokémon territory is never a deed, cadastral parcel or legal boundary.

### Pokémon Agency

Persistent individuals retain their `pokemon_entity_id`. A range shift, excursion, release, transfer or change of collective does not create a new individual.

## Ecology research

### Home range is a repeated-use area, not a hard boundary

USGS's historical review of home-range studies emphasizes that home ranges are dynamic and lack boundaries in the ordinary cadastral sense. Range size can vary with habitat, season and resources.

Source: U.S. Geological Survey, "Home range and travels."
https://www.usgs.gov/publications/home-range-and-travels

Reusable design lesson:

Ouros should store a spatial-use assessment with method, period and uncertainty, not a polygon that acts like an invisible fence. A Pokémon can legitimately appear outside its assessed home range without the data becoming contradictory.

### Core-use area is not the same thing as the whole home range

A USGS-published study of black-bellied fruit bats separated broader home range from smaller core-use areas associated with day roosts or food resources. It also found different overlap patterns and extended fidelity to particular roost sites.

Source: U.S. Geological Survey, "Home range, territoriality, and flight time budgets in the black-bellied fruit bat."
https://www.usgs.gov/publications/home-range-territoriality-and-flight-time-budgets-black-bellied-fruit-bat-melonycteris

Reusable design lesson:

Ouros can distinguish a broad routine-use footprint from places receiving disproportionate repeated use. That creates more interesting consequences than a single `territory_radius`.

### Overlap does not establish social relationship or territoriality

A USGS study of northern flying squirrels found extensive home-range overlap while finding little evidence that the overlap itself represented attraction. It also suggested that territorial behavior may occur only in portions of a larger range, such as around den trees during specific periods.

Source: U.S. Geological Survey, "Spatial organization of northern flying squirrels, Glaucomys sabrinus: Territoriality in females?"
https://www.usgs.gov/publications/spatial-organization-northern-flying-squirrels-glaucomys-sabrinus-territoriality

Reusable design lesson:

`range overlap` must never become `friends`, `same collective`, `rivals` or `fight expected`. Several Pokémon can use the same orchard edge for unrelated reasons.

### Territories can contain overlap among accepted occupants and still allow excursions

A USGS study of cooperatively breeding Micronesian Kingfishers separated home range, territory and prospecting movement. Birds shared substantial space with members of their own territory while making occasional extraterritorial movements.

Source: U.S. Geological Survey, "Territoriality, prospecting, and dispersal in cooperatively breeding Micronesian Kingfishers."
https://www.usgs.gov/publications/territoriality-prospecting-and-dispersal-cooperatively-breeding-micronesian

Reusable design lesson:

A defended area does not imply solitary use or total exclusivity. A rare excursion should be recorded as an event before anyone concludes that the stable range has shifted.

### Site fidelity can persist across years without identical daily use

USGS research on gulls found high winter-site fidelity across years while the duration of local persistence within a winter varied substantially.

Source: U.S. Geological Survey, "Fidelity and persistence of Ring-billed and Herring gulls to wintering sites."
https://www.usgs.gov/publications/fidelity-and-persistence-ring-billed-larus-delawarensis-and-herring-larus-argentatus

Reusable design lesson:

Ouros should separate `returned to the same site this season` from `remained there continuously`. Site fidelity can survive temporary absences and variable residence periods.

## Pokémon source patterns

### Rhyhorn — large claimed area does not mean precise spatial cognition

The official Pokédex states that Rhyhorn claims a large area as territory but may forget where that area is while running. It also links repeated movement to habitat expansion.

Source: Pokémon official Pokédex — Rhyhorn.
https://www.pokemon.com/uk/pokedex/rhyhorn

Reusable structure:

A species can have strong territorial behavior without producing a perfectly surveyed boundary. Behavioral claim, actual use and environmental footprint can diverge.

Do not import the stated radius as a universal Ouros distance or PTU mechanic.

### Fletchinder — defended area can be species- and context-specific

The official Pokédex describes a territory with a stated scale and aggressive response toward bird Pokémon entering it.

Source: Pokémon official Pokédex — Fletchinder.
https://www.pokemon.com/us/pokedex/fletchinder

Reusable structure:

An authored population may defend against a subset of intruders while tolerating other species or situations. Territoriality should therefore be an observed relationship, not `hostile_to_everyone=true`.

Do not import the radius as a generic range rule.

### Trumbeak — territory can be signaled acoustically

The official Pokédex describes Trumbeak using many cries to declare territory.

Source: Pokémon official Pokédex — Trumbeak.
https://www.pokemon.com/us/pokedex/trumbeak

Reusable structure:

Territorial evidence can hand off to Soundscapes/Passive Acoustic Monitoring without making a vocalization an invisible combat zone. Repeated calls can support a boundary hypothesis only when the spatial evidence supports it.

### Aggron — territorial relationship can include environmental stewardship

The official Pokédex describes Aggron claiming a mountain, patrolling it, and restoring damaged ground after landslides or fire.

Source: Pokémon official Pokédex — Aggron.
https://www.pokemon.com/us/pokedex/aggron

Reusable structure:

Territoriality can generate constructive environmental behavior rather than merely combat. An Aggron-like authored individual could be a recurring landscape actor whose patrols, restoration and conflict responses all accumulate history.

Do not convert this lore into automatic restoration rates, Groundshaper effects or immunity to hazards.

### Hisuian Growlithe — territory may be jointly guarded

The official Legends: Arceus site describes Hisuian Growlithe watching over territory in pairs and being wary of humans.

Source: Pokémon Legends: Arceus official site — Hisuian Growlithe.
https://legends.arceus.pokemon.com/en-au/pokemon/growlithe/

Reusable structure:

A territorial unit can be a pair or collective rather than one individual. Pair occupancy still does not establish ownership, breeding status or Pack Mon mechanics.

## PTU campaign/community pattern

A public PTU campaign log describes a forest containing Pokémon with distinct local personalities and attachments, including a Lombre portrayed as highly protective of a particular pond. The useful lesson is not that Lombre universally defend ponds; it is that local spatial attachment can make an otherwise ordinary wild encounter memorable and legible.

Source: r/PokemonTabletop, campaign log #21, 2022.
https://www.reddit.com/r/PokemonTabletop/comments/tvggwm

Reusable structure:

Give some recurring wild Pokémon a stable place relationship that can be recognized later. The same pond can produce negotiation, observation, conflict, absence, reunion or environmental change across years.

## High-value Ouros design conclusions

1. Home range, territory, core-use area and site fidelity must be separate concepts.
2. A territory is a behavioral/ecological assessment, never a legal property boundary.
3. Overlapping range polygons do not establish friendship, collective membership, rivalry or combat.
4. Territorial defense may be selective by resource, location, time, life stage, species or individual.
5. Core-use areas can move while the broader range remains recognizable.
6. An excursion should not create a range revision until repeated evidence or persistent landscape change supports it.
7. Site fidelity can be seasonal and can coexist with long absences.
8. Observation effort matters. A range derived from three sightings is not equivalent to one derived from years of telemetry and field observations.
9. Range assessments are scientific products, not omniscient world-state boundaries.
10. Persistent individuals let local spatial ecology become character history.

## Mechanics / PTU boundary

No generic PTU rule was found that should be interpreted as a universal home-range or territoriality system.

The project corpus contains terms such as Tracker and several capability/Feature concepts used elsewhere, while repository searches for Pack Mon also return PTR2e/Foundry material. Those sources must not be conflated with PTU/Caelo authority.

Forbidden shortcuts:

- territory -> Pack Mon;
- territorial display -> Intimidate effect;
- scent marking -> Tracker lock-on;
- patrol -> free Shift;
- range boundary -> battle zone;
- core-use area -> defensive bonus;
- intruder -> hostile AI;
- shared range -> ally/faction;
- known home range -> capture modifier;
- site fidelity -> Loyalty;
- range shift -> Evolution/Form change;
- Minecraft loaded-area presence -> residency truth.

Any exact Move, Ability, Item, Capability, Skill or Trainer Feature used tactically must still be verified against the project PTU/Caelo sources and current AutoPTU runtime.

## Caelo / helper status

A reliable complete Caelo corpus defining generic home ranges, territoriality or spatial ecology was not recovered during this scan. Super PTU Online Helper was not exposed as an invocable capability. No output is attributed to it.

## Candidate authority recommendation

Pass 176 should create one PROPOSED spatial-ecology layer owning only derived local space-use state:

observation evidence -> spatial-use assessment -> core-use assessment -> site-fidelity comparison -> overlap assessment -> territorial-behavior evidence -> range revision.

Migration, Telemetry, Nesting, Urban Wildlife, Pokémon Agency, Land Tenure, Soundscapes and other existing layers remain authoritative over their own states.