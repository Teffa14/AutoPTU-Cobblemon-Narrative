# Ouros Fire-Regime Monitoring & Treatment Effectiveness — Research Scan 178

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-26
Pass: 178

## Audit correction and scope

The final repository comparison found `design/wildfire-fire-ecology-landscape-recovery-layer.md` from Pass 64. That layer already owns wildfire event state, cause hypotheses, active fronts, smoke, burn-severity mosaics, refugia, fire-regime profiles, planned fire, ecological displacement, recovery and post-fire watershed coupling.

Pass 178 therefore does not create another fire-ecology authority. The duplicate draft layer created earlier in this run was removed. The useful new material is narrowed to monitoring provenance, treatment-effectiveness review, repeated-fire chronology, method revisions and comparability across long-term fire records.

## New public-source findings

### Monitoring before and after fire supports adaptive management

NPS fire-effects programs collect observations before, during and after prescribed burns and wildland fires. Monitoring exists to evaluate objectives, identify undesired effects and revise later management.

Ouros use: Pass 64 keeps the fire/treatment state. Pass 178 adds versioned monitoring series and explicit outcome review.

Sources:
- NPS, “Studying Fire”: https://www.nps.gov/subjects/fire/studying-fire.htm
- NPS, “Fire Effects Monitoring”: https://www.nps.gov/articles/fire-effect-monitoring.htm
- NPS, Yosemite, “Fire Ecology and Monitoring”: https://www.nps.gov/yose/learn/nature/fireecology.htm

### Fire history is a pattern assembled from many events

US Forest Service literature treats fire regime as a long-term pattern involving frequency, size, seasonality, severity and spatial structure rather than one event.

Ouros use: a Pass 64 `fire_regime_profile` can accumulate successive evidence reviews without rewriting the individual `fire_event` records behind it.

Source:
- Jones & Tingley, “Pyrodiversity and biodiversity”: https://www.fs.usda.gov/rm/pubs_journals/2022/rmrs_2022_jones_g001.pdf

### Severity and recovery must remain separate

USGS field and remote-sensing programs measure spatially different burn effects and then follow vegetation recovery through later years. Different vegetation types and severity classes can follow different trajectories.

Ouros use: Pass 178 should never turn a severity map into `recovered=false/true`. It links monitoring observations back to Pass 64 while Flora, Soil, Water and Wildlife retain domain authority.

Sources:
- USGS, “Characterizing Post-Fire Burn Severity And Vegetation Recovery…”: https://www.usgs.gov/centers/werc/science/characterizing-post-fire-burn-severity-and-vegetation-recovery-high-spatial
- USGS, “Time series of high-resolution images enhances efforts to monitor post-fire condition and recovery”: https://www.usgs.gov/publications/time-series-high-resolution-images-enhances-efforts-monitor-post-fire-condition-and
- USGS, “Detecting post-fire burn severity and vegetation recovery…”: https://www.usgs.gov/publications/detecting-post-fire-burn-severity-and-vegetation-recovery-using-multitemporal-remote

### Remote products and field observations have different provenance

NPS and USGS use both field monitoring and remote sensing. Product resolution, processing method and field-validation coverage affect what comparisons are justified.

Ouros use: Pass 160 owns imagery/products. Pass 178 only records how those products participate in a fire-monitoring series and whether two revisions are comparable.

Sources:
- NPS, “Wildland Fire Monitoring”: https://www.nps.gov/articles/wildland-fire-monitoring.htm
- USGS PHIRE burn-severity project: https://www.usgs.gov/centers/western-geographic-science-center/science/characterizing-high-resolution-soil-burn-severity

### Prescribed fire outcomes can be mixed

Forest Service reviews emphasize that wildlife responses to prescribed fire can vary by species, spatial scale and time horizon. NPS monitoring likewise treats objectives as things to evaluate, not guaranteed consequences of completing the burn.

Ouros use: a Pass 64 planned-fire project can be operationally completed while a Pass 178 assessment later reports `PARTIALLY_SUPPORTED`, `MIXED_OUTCOME`, `INSUFFICIENT_EVIDENCE` or another scoped result.

Source:
- USDA Forest Service, “Effects of prescribed fire on wildlife and wildlife habitat”: https://www.fs.usda.gov/rm/pubs_journals/2017/rmrs_2017_finch_d001.pdf

## Pokémon narrative references

Pokémon Horizons’ “Arboliva’s Forest” depicts a forest after a recent wildfire, injured Pokémon and defensive behavior inside the burned landscape. The reusable pattern is recent disturbance -> surviving/displaced wildlife -> misunderstanding -> care/recovery questions that continue after conflict.

Source:
- Pokémon.com, “Arboliva’s Forest”: https://www.pokemon.com/us/animation/horizons/1/arbolivas-forest

“The Green Guardian” begins with a forest fire and then shows a secondary route/access problem produced during the response. The reusable structure is fire -> ecological response -> new obstruction -> route closure -> later rescue/access work.

Source:
- Pokémon.com, “The Green Guardian”: https://www.pokemon.com/us/animation/seasons/9/episode-10-the-green-guardian

These examples enrich Pass 64. They do not create new PTU rules or a new wildfire authority.

## PTU/community references and mechanical boundary

A 2026 PTU community discussion uses weather/fire themes as battle design. It is useful mainly as a warning: a fire-themed narrative scene must not silently activate Sunny Weather, Burned, Fire Terrain, Fire Ace effects or other mechanics simply because the fiction contains wildfire.

Source:
- r/PokemonTabletop, dual-type Gym discussion: https://www.reddit.com/r/PokemonTabletop/comments/1tzz7ap/trying_to_theory_craft_fun_dual_type_gyms_for_a/

Another PTU GM discussion supports regional hooks that become detailed when players engage with them. Fire-history plots, old lookout sites, monitoring stations and quiet years can therefore exist as world texture without forcing a quest every season.

Source:
- r/PokemonTabletop, campaign GM discussion: https://www.reddit.com/r/PokemonTabletop/comments/1oz4e7w/first_time_dm_thinking_of_making_a_ptu_campaign/

No public source found in this run authorizes a generic PTU wildfire simulator. Keep exact mechanics separate:

- wildfire is not automatically Sunny Weather;
- smoke is not automatically an Accuracy penalty or Status;
- charred ground is not automatically Rough Terrain;
- flame movement is not automatically forced movement;
- nearby fire is not automatically Burned;
- Fire-type does not mean ecological fire immunity;
- Water-type Moves do not have authored firefighting volume by default;
- Flash Fire, Flame Body, Heatproof and similar Abilities retain their exact PTU contracts;
- prescribed fire never grants XP, Loyalty, stats or spawn bonuses.

The project’s complete Caelo corpus was not reliably available in this run. Super PTU Online Helper was not exposed as an invocable capability. No output from either source was invented.

## Final design lesson

Pass 64 remains authoritative. Pass 178 adds the narrower question: how do institutions know whether the landscape changed in the way they expected, how comparable are their records across years, and what does a new fire mean when it overlaps older fire history?
