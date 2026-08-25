# Research Scan — Managed Fisheries, Aquatic Harvest & Stock Stewardship — Pass 157

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-24

## Why this gap is worth filling

The repository already has strong authorities for freshwater systems, lake limnology, estuaries, open-ocean ecology, migration, conservation, markets, food, supply chains and Pokémon agency. The Lake Limnology layer explicitly reserves a future `Lake -> Fisheries` handoff and says Fisheries should own harvest/access policy rather than lake physics or ecology.

No dedicated Fisheries authority existed in the inspected repository tree at the start of this pass.

The useful design problem is therefore not "add a fishing minigame." It is to preserve the history of an aquatic resource-management system without confusing:

- catches with population abundance;
- a fishing contest with long-term harvest policy;
- a released animal with a zero-impact interaction;
- a management closure with ecological truth;
- a Poké Ball capture with a fishery landing;
- Minecraft fishing loot or loaded Cobblemon with authoritative stock state.

## Public source scan

### 1. Pokémon — fishing as a recurring social event, not only a capture button

The official Pokémon episode `Hook, Line and Stinker` uses an annual Seaking catching competition as a recurring local event with rivalry, spectators and a recognizable place in community life.

Source:
- Pokémon.com, `Hook, Line and Stinker`: https://www.pokemon.com/us/animation/seasons/4/episode-11-hook-line-and-stinker

Reusable Ouros structure:

`recurring aquatic event -> participants with different experience -> public rules -> observation/catch activity -> rivalry or social complication -> event record -> later editions`

Do not copy the Seaking contest, competitors or plot. The reusable lesson is that an aquatic-use tradition can have edition history, rule revisions and public memory independently from regional resource management.

### 2. Pokémon — fishing technique, equipment and event rules can be distinct

`A Fishing Connoisseur in a Fishy Competition!` distinguishes beginner technique, rod choice, event-specific rules and the eventual handling of hooked Water-type Pokémon. The episode also makes clear that an organized event can impose rules beyond the basic act of fishing.

Source:
- Bulbapedia summary of `A Fishing Connoisseur in a Fishy Competition!`: https://bulbapedia.bulbagarden.net/wiki/A_Fishing_Connoisseur_in_a_Fishy_Competition%21

Reusable Ouros structure:

`general activity -> local/event rule set -> equipment choice -> encounter -> handling decision -> event outcome`

Guardrail: event rules are not universal PTU rules.

### 3. PTU 1.05 — fishing already has explicit mechanics

The public PTU 1.05 Core text contains a dedicated Fishing section. It distinguishes Old, Good and Super Rods, bait/lures, periodic d20 checks, an Athletics check to reel in a hooked Pokémon, and then a possible Hand Net or Poké Ball interaction. Fishing Rods also exist as two-handed equipment.

Sources:
- Public PTU 1.05 Core, Fishing section around page 217: https://anyflip.com/tcye/paot/basic/201-250
- Public PTU 1.05 Core, Fishing Rod gear around page 293: https://anyflip.com/qloz/xgfq/basic/251-300

Project cross-check:
- `Teffa14/AutoPTU` remains the project-designated Python rules oracle while Java is incomplete.
- Repository search on the current Python head did not expose a dedicated fishing runtime subsystem or an authored Fisheries management system.
- A PTR2e `old-rod.json` exists inside imported Foundry material, but that is not evidence of PTU runtime support and must not be treated as the authority for this project.

Design consequence:

If Ouros later executes the exact PTU Fishing procedure, that implementation must be validated against the project's pinned PTU/Caelo material and authoritative runtime. This narrative layer does not recreate those checks, rod limits, capture logic or encounter tables.

### 4. PTU community — avoid treating homebrew fishing tables as core rules

An old Pokémon Tabletop forum thread proposes custom d100 encounter bands and even a homebrew Fisherman class. This is useful evidence that GMs often want fishing to produce location-specific encounter structure, but the mechanics are community homebrew rather than PTU authority.

Source:
- Pokémon Tabletop forum, `Fishing`: https://www.tapatalk.com/groups/pokemon_tabletop/fishing-t1262.html

Reusable Ouros lesson:

Location-specific aquatic encounter ecology should live in authored population/habitat state. Do not copy encounter percentages or homebrew class features into Ouros.

### 5. PTU actual-play/community — fishing can sit inside a wider public event

A public PTU one-shot pitch set in White Harbor combines a spring festival, vendors, bug catching, fishing competition and combat security concerns. The useful pattern is layering a recreational aquatic event into a larger public-space/event system instead of creating a standalone minigame disconnected from the settlement.

Source:
- Reddit r/lfg, PTU White Harbor one-shot: https://www.reddit.com/r/lfg/comments/v2suxf

Reusable Ouros structure:

`festival edition -> temporary aquatic activity -> vendors/audience -> ordinary participation -> optional independent incident`

The battle should be separable from the fishing activity rather than making every catch a combat encounter.

### 6. PTU campaign anecdote — extraction can be replaced by ecological problem-solving

A public PTU GM described players who responded to a food-web crisis by organizing fishing to feed a displaced predatory group while a poisoned forest recovered. The useful structure is not the exact solution; it is that an apparent combat problem can become a temporary resource-management problem with a follow-up obligation.

Source:
- Reddit r/AskReddit PTU GM account: https://www.reddit.com/r/AskReddit/comments/hhl1c5

Reusable Ouros lesson:

A temporary aquatic harvest intervention can create later consequences: pressure on another stock, monitoring requirements, altered local expectations or a need to stop the emergency measure once the original habitat recovers.

### 7. NOAA Fisheries — landings and stock abundance are different evidence streams

NOAA distinguishes fishery-dependent data from fishery-independent surveys. Fishery-dependent records can include effort, landings/discards, species and biological observations. Independent surveys measure abundance and biology using standardized methods outside ordinary fishing activity.

Sources:
- NOAA Fisheries, `Understanding Population Assessments`: https://www.fisheries.noaa.gov/insight/understanding-population-assessments
- NOAA Fisheries, `Fish Stock Assessment 101 Part 1`: https://www.fisheries.noaa.gov/feature-story/fish-stock-assessment-101-series-part-1-data-required-assessing-us-fish-stocks

Reusable Ouros structure:

`activity records + independent surveys + biological/ecological observations -> assessment revision -> management decision`

Never use `catch_count` alone as `population_count`.

### 8. NOAA Fisheries — catch per unit effort is useful but interpretation-sensitive

NOAA's 2024 CPUE good-practices summary emphasizes that catch-per-unit-effort can contribute to stock assessments but requires standardization and interpretation. Gear, spatial choices, environmental conditions, targeting and other covariates can change the index.

Source:
- NOAA Fisheries, `Catch per Unit Effort Modelling for Stock Assessment: A Summary of Good Practices`: https://www.fisheries.noaa.gov/resource/peer-reviewed-research/catch-unit-effort-modelling-stock-assessment-summary-good-practices

Reusable Ouros consequence:

Two boats landing the same number can provide different information if one fished twice as long, used different gear or worked a different habitat. A stable catch can also conceal changing effort or concentration of a schooling population.

### 9. NOAA Fisheries — stock assessments can be data-limited

NOAA uses multiple model classes depending on available evidence. Data-limited approaches provide narrower advice and do not support all the conclusions available from richer assessments.

Source:
- NOAA Fisheries, `Stock Assessment Model Descriptions`: https://www.fisheries.noaa.gov/insight/stock-assessment-model-descriptions

Reusable Ouros lesson:

An institution should be allowed to publish `LOW_CONFIDENCE`, `DATA_LIMITED` or `NO_CURRENT_ASSESSMENT` instead of forcing the simulation to know the real stock size.

### 10. NOAA Fisheries — management status is not one scalar

NOAA distinguishes population size from annual harvest rate. In its terminology, a stock can be too small and the current catch rate can be too high; these are separate determinations based on assessments and reference points.

Source:
- NOAA Fisheries, 2026 fishery stock status updates: https://www.fisheries.noaa.gov/national/population-assessments/fishery-stock-status-updates

Reusable Ouros lesson:

Avoid `fishery_health = 72`. Maintain assessment, effort/harvest pressure, habitat state, recruitment observations and management response as separate dimensions.

### 11. NOAA Fisheries — bycatch/non-target interactions need their own records

Observer programs collect information not only about target catch but also catch composition, discards, protected-species interactions and gear configuration.

Source:
- NOAA Fisheries, `Using Observer Data`: https://www.fisheries.noaa.gov/national/fisheries-observers/using-observer-data

Reusable Ouros structure:

`harvest activity -> target interaction + non-target interaction(s) -> disposition/release -> follow-up evidence`

A non-target Pokémon is not automatically a pest or hostile actor.

### 12. NOAA Fisheries — release is an event, not proof of no consequence

NOAA's updated catch-and-release guidance, last updated August 4, 2026, states that releasing an animal does not itself guarantee survival. Handling, gear, air exposure, depth and other factors can affect outcomes. NOAA separately maintains discard/release mortality science because effects can be delayed.

Sources:
- NOAA Fisheries, `Catch and Release Fishing Best Practices`: https://www.fisheries.noaa.gov/national/resources-fishing/catch-and-release-fishing-best-practices
- NOAA Fisheries, `Fish Discard and Release Mortality Science`: https://www.fisheries.noaa.gov/national/bycatch/fish-discard-and-release-mortality-science

Ouros adaptation:

Record `RELEASED` separately from `KNOWN_UNHARMED`. Do not invent injury, mortality or PTU damage either. Later observation can update the evidence.

### 13. NOAA Fisheries — closures can be narrow in time, space and purpose

A February 26, 2026 NOAA bulletin describes a seasonal closure for a mutton snapper spawning aggregation area from March 1 through June 30, with particular gear restrictions. The useful design lesson is scope: a management measure can be tied to one area, season, activity or method rather than shutting down an entire regional fishery.

Source:
- NOAA Fisheries, 2026 spawning aggregation closure bulletin: https://www.fisheries.noaa.gov/bulletin/reminder-seasonal-closure-mutton-snapper-spawning-aggregation-area-federal-waters-st-1

Reusable Ouros structure:

`observed recurring concentration -> vulnerability/uncertainty assessment -> scoped seasonal/area control -> compliance/monitoring -> later review`

Do not import U.S. law, dates, species or gear rules into Ouros.

## Design synthesis for Ouros

The most reusable high-level model is:

`aquatic population / management unit -> observations -> activity/effort records -> stock assessment revision -> management objective -> scoped control -> harvest/interaction records -> landing/release handoff -> monitoring -> later assessment`

The world should preserve disagreement and uncertainty. A harbor ledger, survey transect, camera network, migration record and fisher observations may all describe the same population from different vantage points.

## Strong narrative structures

### Catch is not abundance

A long-running harbor can have stable landings while effort grows, gear changes or a school concentrates closer to shore. The mystery is methodological and ecological rather than automatically criminal.

### One population, several jurisdictions

A migratory aquatic population can pass through an inland river, estuary and coastal zone. Different institutions may each have valid local data while disagreeing about whether they are managing one stock, several units or an unresolved mixture.

### A closure can outlive its original timing

A traditional closed week may have been calibrated to a spawning run decades earlier. Migration/phenology shifts can make the old schedule increasingly mismatched, creating a research and governance problem without requiring an antagonist.

### Release has a history

A non-target individual can be hooked, released and later re-observed. If it has a persistent Pokémon identity, the Chronicle can connect those observations without converting the release into custody, capture or guaranteed harm.

### Emergency harvest can create a second problem

A temporary harvest measure used during a crisis can become socially expected or economically important. Ending it later can be harder than starting it, even when the original emergency has passed.

## Mechanics boundary

PTU 1.05 has explicit Fishing rules. This pass does not rewrite them.

Fisheries management is world-state logic. It must not infer:

- stock abundance from PTU fishing success;
- fishing success from Minecraft bobber events;
- capture eligibility from fishery access;
- capture ownership from a landing record;
- population removal from KO/despawn;
- release survival from successful battle escape;
- Water-type identity as eligibility for a fishery;
- Schooling/Pack Mon/Swarm behavior from a narrative aggregation;
- Swim capability as fishing, boating or handling proficiency;
- dynamic currents, drowning, nets, restraint or line tension without exact validated mechanics.

## Source status

Research/provenance only. None of the examples above establish Ouros canon.

The complete primary Caelo corpus was not reliably available through the task's accessible project sources during this pass. Super PTU Online Helper was not exposed as an invocable capability. No output from either source has been invented.