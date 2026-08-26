# Ouros Wildfire, Fire Regimes & Post-Fire Recovery — Research Scan 178

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-26
Pass: 178

## Why this pass exists

A full repository audit found substantial coverage for crisis response, climate, air quality, vegetation, remote sensing, water, soil, wildlife movement, public works and ecological monitoring, but no dedicated authority for fire as a recurring ecological process.

`crisis-rescue-recovery-layer.md` already owns the emergency lifecycle of a wildfire: signal, preparation, impact, response, stabilization, recovery and aftermath. Pass 178 therefore must not become a second crisis layer. Its scope is narrower and longer-term: fire history, fire regime, spatial burn effects, post-fire ecological succession, prescribed-fire projects, treatment objectives, monitoring and repeated-fire landscape history.

This pass is especially useful because the same event can be several different things at once:

- an active crisis for Emergency Services;
- a smoke event for Air Quality;
- a weather-sensitive disturbance for Meteorology/Climate;
- a vegetation disturbance for Flora;
- a sediment/runoff driver for Soil, Freshwater and Stormwater;
- a displacement event for Wildlife/Migration;
- a mapped change for Remote Sensing;
- a long-lived ecological episode for the new fire-ecology authority.

Those responsibilities should remain separate.

## Public-source findings

### 1. Fire is not ecologically uniform

The National Park Service describes fire ecology as the study of fire's relationship with ecosystems and emphasizes that different landscapes respond differently. Some ecosystems depend on recurring fire, while others experience fire rarely and recover slowly. Fire behavior and effects are influenced by vegetation, fuels, topography, weather and other local conditions.

Reusable Ouros lesson: do not store `burned=true` as the ecological conclusion. Preserve spatial variation, ecosystem context and uncertainty.

Sources:
- NPS, “Fire in Depth”: https://www.nps.gov/subjects/fire/fire-in-depth.htm
- NPS, Lassen Volcanic National Park, “Fire Ecology and Effects”: https://www.nps.gov/lavo/learn/nature/fire-ecology-and-effects.htm

### 2. Fire regimes are historical patterns, not one event

US Forest Service literature distinguishes the long-term fire regime from any single burn. Useful dimensions include frequency, size, seasonality, intensity/severity and spatial pattern. Fire-history interpretation can therefore change when a longer record becomes available.

Reusable Ouros lesson: a region can have a `FIRE_REGIME_ASSESSMENT` that is revised over decades without rewriting individual fire events.

Source:
- Jones & Tingley, “Pyrodiversity and biodiversity”: https://www.fs.usda.gov/rm/pubs_journals/2022/rmrs_2022_jones_g001.pdf

### 3. Prescribed fire requires objectives and follow-up

NPS monitoring programs collect information before, during and after prescribed burns or naturally ignited fires. Monitoring exists to determine whether objectives were met and whether undesired effects occurred. Results can change later management.

Reusable Ouros lesson: a prescribed burn should have a plan, objective set, authorized perimeter/window, actual burn footprint, observations, outcome assessment and later revision. “Burn completed” does not mean “objective achieved.”

Sources:
- NPS, “Studying Fire”: https://www.nps.gov/subjects/fire/studying-fire.htm
- NPS, “Fire Effects Monitoring”: https://www.nps.gov/articles/fire-effect-monitoring.htm
- NPS, Yosemite, “Fire Ecology and Monitoring”: https://www.nps.gov/yose/learn/nature/fireecology.htm

### 4. Burn severity is spatially heterogeneous

USGS post-fire research maps different levels of burn severity within the same fire perimeter and compares those patterns with surviving vegetation and recovery potential. Burn severity and recovery are not equivalent concepts.

Reusable Ouros lesson: keep `FIRE_FOOTPRINT`, `BURN_EFFECT_ZONE`, and later `RECOVERY_OBSERVATION` separate. A high-severity patch does not imply permanent loss; a low-severity patch does not imply no ecological consequence.

Sources:
- USGS, “Characterizing Post-Fire Burn Severity And Vegetation Recovery…” (2024): https://www.usgs.gov/centers/werc/science/characterizing-post-fire-burn-severity-and-vegetation-recovery-high-spatial
- USGS, “Remote sensing of forest fire severity and vegetation recovery”: https://www.usgs.gov/publications/remote-sensing-forest-fire-severity-and-vegetation-recovery

### 5. Recovery is multi-year and pathway-dependent

USGS work using multitemporal imagery shows that different vegetation types and burn-severity classes recover along different trajectories. Some patches resprout quickly while others remain structurally different years later.

Reusable Ouros lesson: avoid `time_since_fire -> recovered`. Recovery should be a set of observed changes owned by Flora/Soil/Water/Wildlife, linked to the fire history but not collapsed into one countdown.

Sources:
- USGS, “Time series of high-resolution images enhances efforts to monitor post-fire condition and recovery”: https://www.usgs.gov/publications/time-series-high-resolution-images-enhances-efforts-monitor-post-fire-condition-and
- USGS, “Detecting post-fire burn severity and vegetation recovery…”: https://www.usgs.gov/publications/detecting-post-fire-burn-severity-and-vegetation-recovery-using-multitemporal-remote

### 6. Fire can create a landscape mosaic rather than a single before/after state

Fire-ecology literature describes mixed-severity patterns and mosaics of patches with different burn histories and successional stages. The ecological meaning depends on spatial and temporal scale.

Reusable Ouros lesson: repeated burns should accumulate as overlapping historical footprints. A later fire can reburn part of an older footprint while leaving another portion untouched.

Source:
- USDA Forest Service, Jones & Tingley: https://www.fs.usda.gov/rm/pubs_journals/2022/rmrs_2022_jones_g001.pdf

### 7. Fire effects can be positive, negative or neutral depending on species and scale

Forest Service reviews of prescribed fire and wildlife emphasize that responses can vary by species, spatial scale and time horizon. Fire can create or maintain habitat for some species while reducing suitability for others.

Reusable Ouros lesson: never map `fire -> habitat damage` or `prescribed fire -> habitat benefit` globally. Wildlife, Flora and Conservation should own species/population-specific interpretation.

Source:
- USDA Forest Service, “Effects of prescribed fire on wildlife and wildlife habitat”: https://www.fs.usda.gov/rm/pubs_journals/2017/rmrs_2017_finch_d001.pdf

### 8. Remote sensing helps map fire, but does not replace field interpretation

NPS and USGS use imagery to map extent and severity while also relying on field monitoring. Different products and resolutions can change how recovery appears.

Reusable Ouros lesson: Pass 160 Remote Sensing can produce burn-related derived products, but Pass 178 must store provenance and field-validation links. Minecraft surface color is not burn severity truth.

Sources:
- NPS, “Wildland Fire Monitoring”: https://www.nps.gov/articles/wildland-fire-monitoring.htm
- USGS PHIRE high-resolution burn-severity project: https://www.usgs.gov/centers/western-geographic-science-center/science/characterizing-high-resolution-soil-burn-severity

## Pokémon narrative references

### Arboliva’s Forest

The official Pokémon Horizons episode summary describes a forest after a recent wildfire, visible burned terrain, injured wildlife and Arboliva remaining within the damaged landscape. The useful structure is not the specific characters or resolution. It is:

`recent fire -> changed habitat -> injured/displaced Pokémon -> misunderstood defensive behavior -> care/restoration questions that remain after the battle`

Ouros adaptation: a burned forest can remain socially and ecologically active. Wild Pokémon are not just encounter replacements in an empty tileset. Their presence may represent survival, displacement, site fidelity or use of newly altered habitat.

Source:
- Pokémon.com, “Arboliva’s Forest”: https://www.pokemon.com/us/animation/horizons/1/arbolivas-forest

### The Green Guardian

The official episode summary begins with a forest fire threatening Pokémon. Celebi’s intervention creates a second obstruction that later closes a road. This is a useful cascade pattern:

`fire -> emergency ecological response -> new physical obstruction -> route closure -> rescue/access problem`

Ouros adaptation: resolving the initial fire does not erase secondary states generated during response. The original crisis and later route/ecology problem can become separate jobs with shared provenance.

Source:
- Pokémon.com, “The Green Guardian”: https://www.pokemon.com/us/animation/seasons/9/episode-10-the-green-guardian

## PTU/community design references

A recent PTU community discussion about dual-type Gyms uses weather and seasonal themes as a battle-design concept. It is useful mainly as a warning for Pass 178: narrative wildfire or prescribed fire must not be implemented by silently turning on Sunny Weather, Fire Terrain, Burn, hazards or Type Ace mechanics simply because the scene is fire-themed.

Source:
- r/PokemonTabletop, dual-type Gym discussion, 2026-06-08: https://www.reddit.com/r/PokemonTabletop/comments/1tzz7ap/trying_to_theory_craft_fun_dual_type_gyms_for_a/

A separate PTU campaign discussion recommends open-ended regional hooks and expanding only the material players engage with. Fire history fits this approach well: old burn scars, fire-adapted habitat, closed lookout roads, historic crew stations and monitoring plots can exist as world texture without each becoming an active quest.

Source:
- r/PokemonTabletop, campaign GM discussion: https://www.reddit.com/r/PokemonTabletop/comments/1oz4e7w/first_time_dm_thinking_of_making_a_ptu_campaign/

## PTU/Caelo mechanical boundary

No public source found in this scan authorizes a generic PTU “wildfire simulator.” Fire-type Moves, Burned, Sunny Weather, Fire Ace, Weather mechanics, environmental damage and any smoke/fire zone rules must remain separate exact mechanics.

Rules guardrails for Ouros:

- a wildfire is not automatically Sunny Weather;
- smoke is not automatically Accuracy reduction or Blindness;
- burned vegetation is not automatically Rough Terrain;
- flame-front movement is not automatically forced movement;
- proximity to fire does not automatically apply Burned;
- Fire-type Pokémon do not automatically suppress, ignite or survive wildland fire;
- Water-type Moves do not have authored firefighting volume unless a validated rule or scenario contract explicitly defines it;
- Flash Fire, Flame Body, Heatproof or similar Abilities retain their exact PTU meaning and never become ecological immunity;
- prescribed fire never grants XP, Training, Loyalty or ecological bonuses by default.

The project’s Caelo corpus was not reliably recoverable in this run, and Super PTU Online Helper was not exposed as an invocable capability. No rule is inferred from either source.

## Design conclusions for Ouros

1. Crisis owns active emergency response. Fire Ecology owns long-term disturbance history and ecological monitoring.
2. Fire events persist as spatially heterogeneous historical objects.
3. Burn severity, vegetation mortality, soil effects, smoke, runoff, wildlife displacement and recovery are separate downstream observations.
4. Prescribed fire is a planned intervention with objectives and outcome review, not a guaranteed benefit.
5. Fire regime is a revisable historical interpretation built from multiple events and records.
6. Reburns must link to older fire footprints instead of overwriting them.
7. Years with no fire are meaningful parts of a fire history.
8. Public memory can simplify a fire into “the year the whole valley burned” while the scientific record preserves a patchier reality.
9. Fire-adapted Pokémon behavior must be authored per population/species context and never inferred from Type alone.
10. Minecraft renders a fire-state projection. It cannot author ecological truth through block destruction, spread ticks, particles or chunk state.
