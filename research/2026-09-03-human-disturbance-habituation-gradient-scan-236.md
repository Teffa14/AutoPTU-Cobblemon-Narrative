# Human disturbance and habituation gradient scan — Pass 236

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Primary ecology question: How should Ouros represent repeated human exposure without collapsing every wild Pokémon into either permanently fearful or permanently tame?

## Existing Ouros context checked

This pass follows `CURRENT_FOCUS.md` and `design/ecology-development-program.md`. It preserves the authority boundary in `design/ouros-source-authority-and-species-policy.md` and does not modify the canon-approved first Sendero Fletchling population in `canon/marea-interior-first-wild-population-v1.md`.

Pass 235 already owns migration/temporal niches. Pass 236 therefore focuses specifically on human disturbance, habituation, sensitization and altered resource use.

## Public sources

### Official Pokémon-derived behavioral evidence

1. Pidove — Bulbapedia synthesis of official Pokédex/anime material
   https://bulbapedia.bulbagarden.net/wiki/Pidove
   Retrieved 2026-09-03.
   Useful high-level pattern: some Pokémon can show low fear of people and use parks/plazas while still retaining grassland/rural habitat use. Human proximity is therefore a species/context prior, not an automatic domestication state.

2. Trubbish — Bulbapedia synthesis of official Pokédex material
   https://bulbapedia.bulbagarden.net/wiki/Trubbish
   Retrieved 2026-09-03.
   Useful high-level pattern: human waste can become an ecological resource and attract a species toward litter/unsanitary sites. Human activity can therefore increase local suitability for some species while reducing it for others.

3. Grimer — Bulbapedia synthesis of official Pokédex material
   https://bulbapedia.bulbagarden.net/wiki/Grimer
   Retrieved 2026-09-03.
   Useful high-level pattern: pollution/industrial waste can support some Pokémon. Anthropogenic pressure must not be modeled as one scalar that is universally negative.

These sources support candidate mechanisms only. They do not authorize Pidove, Trubbish or Grimer for Marea.

### Real behavioral ecology

4. Kc et al. 2024, flight initiation distance and bird tolerance in urban/rural habitats
   https://pubmed.ncbi.nlm.nih.gov/39386984/
   Reported higher tolerance in urban conspecifics, with variation by dietary guild, season, time, body size, flock size and human density. Reusable lesson: tolerance should be species-, context- and population-sensitive.

5. Uchida et al. / tropical comparative study, Nature Communications 2023
   https://doi.org/10.1038/s41467-023-37936-5
   Across 842 bird species, tolerance varied with human footprint and species traits. Reusable lesson: a local disturbance gradient should modify behavior probabilistically rather than overwrite species baseline.

6. Petelle et al. 2021, yellow-bellied marmot long-term disturbance responses
   https://academic.oup.com/beheco/article/32/4/668/6209789
   Repeated approaches produced lower average flight-initiation distance, but individual responses differed; some individuals sensitized instead. Highly disturbed colonies also showed lower body-mass gain. Reusable lesson: behavioral habituation and fitness cost must be tracked separately.

7. Communications Biology 2024 urban bird tolerance / COVID mobility study
   https://www.nature.com/articles/s42003-024-06387-z
   Reusable lesson: response to human presence can operate at multiple time scales and may not immediately reverse when short-term activity changes.

## PTU / Kairos / Caelo cross-check

The project-supplied Kairos index routes ecosystem guidance to the Running the Game material around pp. 437+ and encounter construction around pp. 470+. Kairos is evidence that a living-world server can maintain world and hunting state outside active encounters; it is not authority for a new Ouros behavioral rule.

PTU skills such as Survival, Stealth, Intuition and Pokémon Education can support observation/adjudication where the active Ouros rules profile validates them, but this pass does not create new Skill DCs or mechanical effects.

The supplied Caelo evidence already used by the Marea foundation treats ordinary Pokémon as having local territorial/diurnal behavior. This supports contextual wild behavior but does not establish a universal habituation rule.

## Reusable structures extracted

### Disturbance is multidimensional

Track at least these pressures separately:
- human foot traffic;
- vehicles/machinery;
- noise;
- artificial light;
- waste/food subsidy;
- deliberate feeding;
- pursuit/harassment;
- capture pressure;
- battle history;
- construction/habitat modification.

A single `human_disturbance = high` field cannot represent the ecological result.

### Tolerance and welfare are separate

A Pokémon may become easier to approach while simultaneously:
- feeding less efficiently;
- shifting to nocturnal activity;
- abandoning a nest or resting site;
- losing body condition;
- increasing vigilance;
- becoming dependent on anthropogenic food;
- becoming more vulnerable to capture or conflict.

Therefore:

`LOW_ESCAPE_RESPONSE != LOW_ECOLOGICAL_COST`

### Individual learning matters

Repeated harmless exposure can reduce escape response for one individual while another remains cautious or sensitizes. Species baseline remains a prior, and individual exposure history modifies it.

### Human activity can create both refuge and trap

Some Pokémon may exploit waste, structures, artificial water, warmth, lighting or predator-free human spaces. The same environment can be beneficial in one axis and harmful in another. Ouros should be able to express an anthropogenic resource subsidy without declaring the site ecologically healthy.

## Ouros candidate model

For each persistent population or individual, retain separate values for:
- `human_tolerance_baseline`;
- `harmless_exposure_memory`;
- `harmful_exposure_memory`;
- `resource_subsidy_affinity`;
- `vigilance_pressure`;
- `avoidance_pressure`;
- `activity_shift_pressure`;
- `welfare_cost`;
- `capture_conflict_pressure`.

Candidate visible intents include tolerate, observe, retreat, reroute, hide, forage-near-human, exploit-waste, wait-until-dark, warn, defend or relocate.

These are ecology behaviors, not PTU Status Afflictions.

## Marea/Sendero application

The existing Fletchling population remains canon-approved and unchanged. Pass 236 may use it as the first deterministic regression species because its population identity already exists, but no new biological claim about all Fletchling becomes canon from this fixture alone.

Sendero del Vidrio is suitable for a gradient test because the same persistent population can encounter low-traffic shelves, route traffic, observation activity and repeated player presence without inventing a new region.

## Implementation lesson

The first implementation should not require tactical combat. A world-state service can accumulate exposure and calculate a behavioral modifier. Minecraft/Cobblemon can alter projection distance, visible activity window or presentation behavior. If pursuit, attack, capture or structured defense begins, Ouros must explicitly hand off the selected combatants to AutoPTU.

## Open questions

- What decay curve should harmless and harmful exposure memories use?
- Does tolerance learn per human actor, per activity class or toward humans generally?
- How much of individual learning can influence a population baseline across generations?
- Which official species should be candidate urban exploiters after Marea's worldgen/spawn envelope is verified?
- How should deliberate feeding affect resource dependence and disease/conflict risk?
- Which Minecraft signals are reliable enough to classify noise, traffic and artificial light without making Minecraft authoritative over ecological truth?
