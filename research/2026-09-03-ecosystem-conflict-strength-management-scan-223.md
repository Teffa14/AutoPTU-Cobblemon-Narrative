# Ecosystem conflict, strength pressure, and managed development zones — research scan 223

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Canon authority: NONE. This file records source-backed patterns and design implications. It does not establish Ouros canon or PTU rules.

## Why this pass exists

Passes 221–222 established finite ecosystem populations and dynamic demography. A remaining gap is how frequent trainer battles, wild-vs-wild conflict, predation, survival, capture pressure, and institutional management can change the *composition and competence* of those populations without simulating thousands of invisible PTU battles.

The design target supplied for Ouros is a living ecosystem where consequences persist in population structure, behavior, NPC knowledge, habitat use, and physical traces. Starter/development areas may host many battles while authorities actively keep dangerous outliers and inappropriate risk away from children and inexperienced Trainers. Safety must therefore emerge from management, not from an invisible hard level cap.

## Existing Ouros boundaries checked before writing

This scan was prepared after inventorying the current repository tree and re-reading the relevant population, demographic, progression, and wild-behavior contracts.

Relevant established/proposed layers include:

- `design/ecosystem-population-authority-v1.md`: finite ecosystem membership; Cobblemon projection cannot create population.
- `design/ecosystem-demographic-cycle-v1.md`: births/hatches, deaths, capture, release, immigration/emigration, maturation, and migration change population through accounted transitions.
- `canon/npc-pokemon-dynamic-progression-v1.md`: persistent NPC/Pokémon progression exists and must not be replaced by an ecology-only shortcut.
- `design/wild-pokemon-behavior-tolerance-tactical-policy.md`: wild behavior derives from species/population behavior, individual capability, context, Trainer behavior, and legal mechanics rather than a universal aggression radius.
- passes 216–220: temporal ecology, movement/corridors, dependent sites, and provisioning already govern context; this pass must not duplicate their responsibilities.

## Internal PTU/Kairos routing evidence

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes future rule verification to:

- Pokémon leveling/evolution/training: pp. 347+
- injuries/death/rest: pp. 410–412
- world population/ecosystem guidance: pp. 437+
- rewards/XP: pp. 455–459
- encounter creation: pp. 470+

The index explicitly warns that page references are routing aids, not Ouros acceptance.

Therefore this pass does **not** assume that an off-screen wild victory grants PTU Experience, Levels, Features, Moves, Evolution, injuries, or any other mechanical benefit. Mapping ecosystem conflict history into an actual PTU stat/Level change remains UNCERTAIN until the supplied PTU/Caelo/Kairos source text is audited directly.

## Public research

### Contest experience can change later behavior without proving permanent physical power growth

Rillich/related contest literature and subsequent animal-behavior work support winner/loser effects: previous victories or losses can alter willingness to engage, escalation, assessment, and later contest outcomes. However, persistence varies strongly by species and context.

Useful sources:

- Oldham et al., “Winner–loser effects overrule aggressiveness during the early stages of contests between pigs”, Scientific Reports / PMC, 2020: https://pmc.ncbi.nlm.nih.gov/articles/PMC7414859/
- Hsu et al., “Prior contest experience exerts a long-term influence on subsequent winner and loser effects”, Behavioral Ecology and Sociobiology / PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC3262751/
- Lan et al., “Loser-effect duration evolves independently of fighting ability”, Proceedings of the Royal Society B / PMC, 2019: https://pmc.ncbi.nlm.nih.gov/articles/PMC6545094/
- Hotta et al., “The use of multiple sources of social information in contest behavior”, Frontiers in Ecology and Evolution, 2015: https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2015.00085/full

Reusable lesson: previous conflict can alter future behavior and perceived fighting ability, but “experienced” must not be treated as synonymous with “higher actual fighting ability”. Different species can retain, ignore, or express experience differently.

Ouros implication: the world simulation may maintain conflict exposure/history and behavioral adaptation separately from any PTU Level or combat-stat authority.

### Repeated conflict can also impose costs

Contest literature records injury, energetic expenditure, and context-dependent costs as possible consequences. Winning is not a monotonic free power-up.

Useful source:

- “Examination of prior contest experience and the retention of winner and loser effects”, Behavioral Ecology / PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC2821427/

Reusable lesson: high encounter pressure should be capable of producing avoidance, injury pressure, displacement, or reduced willingness to fight as well as greater competence. This helps prevent a positive-feedback loop where every crowded battle corridor inevitably evolves into an infinitely stronger population.

### Human-wildlife management can actively reshape where habituated animals spend time

The US National Park Service provides a contemporary real-world example of management aimed at reducing dangerous human-wildlife overlap. In 2026 Grand Canyon began a Conservation K-9 pilot to encourage habituated elk and bighorn sheep away from developed exclusion areas and toward more natural movement/habitat patterns. The project combines movement monitoring, exclusion zones, emergency-call records, attractant reduction, landscaping changes, and controlled hazing by trained staff.

Source:

- NPS, “Meet Blue: Grand Canyon’s New Conservation K-9”, updated 2026-05-29: https://www.nps.gov/articles/000/conservation-k9-blue.htm

Glacier National Park has also used trained wildlife shepherding to move bighorn sheep, mountain goats, and deer out of high-use human spaces; one management goal was reducing predator attraction into populated areas.

Source:

- NPS, “Wildlife Shepherding in Glacier National Park”: https://home.nps.gov/articles/barkrangergracie.htm

Reusable lesson: a protected development corridor can stay biologically connected to a larger ecosystem while staff actively manipulate overlap, attractants, access, and animal movement. It need not be ecologically sterile.

### Relocation is a real intervention with ecological cost, not a teleport cleanup button

USGS work on relocated Yellowstone grizzly bears found that return, survival, distance moved, age, and sex affected outcomes; relocation was not consequence-free.

Source:

- Blanchard & Knight, “Biological consequences of relocating grizzly bears in the Yellowstone ecosystem”, Journal of Wildlife Management / USGS, 1995: https://www.usgs.gov/publications/biological-consequences-relocating-grizzly-bears-yellowstone-ecosystem

Reusable lesson: if Ouros authorities relocate a dangerous Pokémon, that individual remains a population member somewhere. The intervention must create an accounted transfer and can create future return, survival, territory, or social consequences. Relocation cannot delete an inconvenient actor.

### Habituation changes risk without making wildlife tame

Grand Canyon NPS describes repeated human exposure reducing avoidance, while animals can still become dangerous when startled or approached too closely.

Source:

- NPS, “Wildlife Habituation”: https://home.nps.gov/grca/learn/nature/wildlife-habituation.htm

Reusable lesson: development corridors with frequent Trainer contact can produce context-specific tolerance or altered behavior. Frequent battle/contact does not imply friendship, domestication, or universal aggression.

### Pokémon precedent: dangerous strong wild individuals can coexist with normal regional populations

The official Pokémon Legends: Arceus site describes Alpha Pokémon as larger, strong/tough wild opponents that may chase and attack the player when noticed.

Source:

- The Pokémon Company, Pokémon Legends: Arceus official gameplay page: https://legends.arceus.pokemon.com/en-gb/gameplay/

Reusable high-level structure only: a regional population can contain conspicuously dangerous strength outliers. Ouros should not copy Alpha presentation, mechanics, visuals, or spawning. The useful design pattern is merely “outlier individual requiring different risk handling”.

## Design synthesis

### Three independent state families

The ecosystem simulation should never collapse these into one number:

1. **Demographic state** — how many members exist, stages, recruitment, death, capture, immigration/emigration, predation losses.
2. **Combat/behavioral state** — distribution of battle exposure, learned tolerance/avoidance/escalation tendencies, and eventually source-authorized PTU strength/progression.
3. **Institutional safety state** — what risk level authorities are willing to permit in a managed human-development corridor, what evidence they have, and which interventions they choose.

A population can therefore be abundant but weak, sparse but dangerous, battle-experienced but avoidant, or demographically healthy while generating one dangerous outlier.

### Off-screen conflict is statistical world simulation, not hidden AutoPTU

Wild-vs-wild events that occur while no player is present should be resolved through ecosystem windows, not by instantiating tactical battles.

The simulation may estimate:

- contact opportunity;
- predator/prey pressure;
- territorial/resource overlap;
- season/reproductive pressure;
- trainer-battle exposure recorded from actual player battles;
- injury/mortality/displacement pressure only through explicitly authored ecological functions;
- learned behavioral response;
- change in an aggregate combat-competence distribution.

It must not invent:

- specific Moves used;
- HP values after an unseen fight;
- exact Status conditions;
- initiative order;
- tile-by-tile movement;
- Trainer Features;
- Item consumption;
- PTU Experience/Levels unless an audited rule explicitly authorizes that progression path.

### Strength should be a distribution, not one ecosystem level

A useful population profile needs at least a center and an upper tail. A single average hides exactly the dangerous outliers that authorities care about.

Candidate representation:

```text
population_combat_profile:
  exposure_index
  competence_band_distribution
  behavioral_confidence_distribution
  dangerous_outlier_count_or_probability
  last_materialized_ptu_strength_evidence
  source_authority_for_ptu_mapping
```

`competence_band_distribution` is intentionally world-simulation state until PTU mapping is verified.

### Battle-heavy starter zones can remain starter zones through active management

A managed development area can legitimately accumulate large quantities of Trainer-vs-wild battle exposure. That should influence surviving populations where species behavior supports learning or selection pressure.

Safety comes from feedback:

```text
battle/contact pressure rises
-> monitor strength/risk distribution
-> detect dangerous upper-tail change or unsuitable predator arrival
-> authority intervention
-> relocation / managed capture / deterrence / habitat steering / access change / patrol response
-> ecosystem membership and behavior update
-> monitor again
```

There is no invisible `max_level = starter_zone_cap` rule.

A strong individual can enter or emerge in a starter zone. The system should create a real incident and institutional response rather than despawn or downscale it.

### Capture can create selection pressure

Actual player captures already remove real members from the ledger. Repeated selective capture can also change composition:

- bold/easily approached animals may be removed disproportionately;
- visually conspicuous or powerful individuals may be targeted disproportionately;
- cautious individuals may remain;
- predator removal may increase prey abundance;
- prey removal can constrain predator populations later.

These are candidate ecological effects and require species/context-specific functions. They are not universal rules.

### Predation affects both demographics and the visible world

Predation should resolve as demographic/resource pressure at ecosystem-window scale unless a player witnesses the encounter.

A confirmed aggregate predation loss can reduce prey membership and feed predator resource sufficiency without creating a hidden PTU combat transcript.

Its world manifestation can include aged evidence categories such as remains, tracks, disturbed ground, abandoned feeding sites, changed movement corridors, or altered activity timing. Exact cause remains uncertain to characters unless evidence justifies it.

### NPC inference must remain epistemic

NPCs receive observations, reports, historical comparisons, patrol records, traces, and direct sightings. They do not read the server ledger.

A ranger may say that “something strong is pushing the smaller Pokémon out of this patch” based on observations. Server truth can later show predation, repeated contests, human disturbance, or migration instead.

This preserves mystery while keeping canon deterministic underneath.

## Proposed data structures for pass 223

Names are candidates, not canon:

- `ECOSYSTEM_CONFLICT_PRESSURE_WINDOW`
- `POPULATION_COMBAT_PROFILE`
- `OFFSCREEN_CONFLICT_LEDGER`
- `MANAGED_DEVELOPMENT_ZONE_POLICY`
- `AUTHORITY_WILDLIFE_INTERVENTION`
- `ECOLOGICAL_TRACE_EVENT`

## Battle-engine boundary

The aggregate simulation belongs to Ouros world authority and does not prove any AutoPTU capability.

A live intervention can activate PTU only when a real, present confrontation requires it. At that point missing battle families remain real dependencies; the ecosystem simulator cannot approximate them inside the Minecraft adapter.

## Canon questions intentionally open

- Which Marea corridor, if any, is canonically intended as the first children/new-Trainer development route.
- Which institution has legal authority to relocate, capture, close access, or order deterrence.
- Whether authorities may retain relocated Pokémon, transfer them to another ecosystem, release them, or involve licensed Trainers.
- Exact PTU/Caelo/Kairos authority for Experience/Level gain from wild-vs-wild or repeated wild encounters.
- Whether battle exposure should ever directly alter Level, or only create an input into a later source-backed progression process.
- Species-specific learning/contest-memory profiles.
- Predation lethality and off-screen mortality calibration.
- How often simulation windows run relative to Ouros seasons and server uptime.
