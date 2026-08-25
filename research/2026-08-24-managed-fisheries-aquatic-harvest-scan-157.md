# Research Scan — Fisheries Stock Assessment, Effort & Release Monitoring — Pass 157

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Extension research for Pass 70.
Date: 2026-08-24

## Existing authority found during final repository audit

Pass 70 already established `design/fisheries-angling-aquaculture-layer.md` and its companion research/proposals. It is the Fisheries authority for fishing effort, angling events, catch observations, stock assessments, management measures, non-target interactions, aquaculture, stocking/release and festival fishing.

Pass 157 therefore does not create a second Fisheries authority.

This scan deepens four narrower questions that Pass 70 identified but did not model in detail:

- how fishery-dependent catch/effort differs from independent survey evidence;
- how stock-assessment revisions should preserve data limitations and method changes;
- how release/non-target outcomes should be recorded without assuming zero impact or injury;
- how seasonal/area management measures should retain their exact scope and rationale.

The companion design file for this pass is an extension protocol, not a replacement for Pass 70.

## Fresh public source scan

### 1. Pokémon — recurring fishing events can accumulate civic history

The official Pokémon episode `Hook, Line and Stinker` uses an annual Seaking catching competition as a recurring local event with rivalry, spectators and a recognizable place in community life.

Source:
- Pokémon.com, `Hook, Line and Stinker`: https://www.pokemon.com/us/animation/seasons/4/episode-11-hook-line-and-stinker

Pass 70 already researched another fishing competition, so the new lesson here is longitudinal rather than mechanical: one event can have editions, records, old champions, rule revisions and public memory without changing the underlying fishery authority.

Reusable Ouros structure:

`recurring aquatic event -> edition-specific participation/rules -> catch/release records -> public result -> later edition comparison`

Do not copy the competition, characters or plot.

### 2. PTU actual-play/community — a fishing contest can sit inside a broader public event

A public PTU one-shot pitch set in White Harbor combines a spring festival, vendors, a bug-catching competition, fishing activity and a separate security threat. The useful pattern is that angling can be one activity inside a larger settlement event rather than a standalone minigame.

Source:
- Reddit r/lfg, White Harbor PTU one-shot: https://www.reddit.com/r/lfg/comments/v2suxf

Reusable Ouros structure:

`festival edition -> temporary fishing activity -> market/audience context -> ordinary participation -> independent incident if one actually occurs`

The battle should be separable from catch records and fishery management.

### 3. PTU community — fishing procedures are frequently homebrewed, so provenance matters

An old Pokémon Tabletop forum discussion proposes custom d100 fishing encounter bands and even a homebrew Fisherman class. It is useful evidence that GMs often want location-specific fishing structure, but those mechanics are community homebrew rather than authoritative PTU 1.05 rules.

Source:
- Pokémon Tabletop forum, `Fishing`: https://www.tapatalk.com/groups/pokemon_tabletop/fishing-t1262.html

Design lesson:

Never promote a public fishing table, custom class or encounter percentage into Ouros mechanics merely because it appears in a PTU community thread.

### 4. PTU 1.05 — fishing already has an explicit rules procedure

The public PTU 1.05 Core contains a Fishing section with rod categories, bait/lure use, periodic rolls and an Athletics check to reel in a hooked Pokémon. Fishing Rods also exist as two-handed equipment.

Sources:
- PTU 1.05 Core, Fishing section around page 217: https://anyflip.com/tcye/paot/basic/201-250
- PTU 1.05 Core, Fishing Rod equipment around page 293: https://anyflip.com/qloz/xgfq/basic/251-300

Project check:
- AutoPTU Python remains the designated rules oracle while Java is incomplete.
- Current repository search did not expose a dedicated end-to-end AutoPTU fishing runtime path that can be assumed for Minecraft.
- A PTR2e Old Rod JSON appears in imported Foundry material, but PTR2e imported content is not evidence of the target PTU runtime contract.

Design consequence:

Pass 157 records world-state fisheries evidence. It does not recreate the Core Fishing checks, generate catch tables or treat Minecraft fishing as their implementation.

### 5. NOAA — fishery-dependent and fishery-independent data are different evidence streams

NOAA Fisheries distinguishes fishery-dependent data such as effort, landings/discards and biological samples from fishery-independent surveys designed to estimate abundance and ecosystem/biological conditions separately from ordinary fishing activity.

Sources:
- NOAA Fisheries, `Understanding Population Assessments`: https://www.fisheries.noaa.gov/insight/understanding-population-assessments
- NOAA Fisheries, `Fish Stock Assessment 101 Part 1`: https://www.fisheries.noaa.gov/feature-story/fish-stock-assessment-101-series-part-1-data-required-assessing-us-fish-stocks

Reusable Ouros structure:

`activity/effort records + independent surveys + biological/ecological observations -> assessment revision -> management interpretation`

A harbor ledger and a research survey may disagree without either being fraudulent or useless.

### 6. NOAA — catch per unit effort needs standardization and context

A 2024 NOAA summary on catch-per-unit-effort modeling emphasizes that CPUE can contribute to stock assessments but is sensitive to fishery definition, gear, spatial behavior, environmental covariates, reporting and other choices.

Source:
- NOAA Fisheries, `Catch per Unit Effort Modelling for Stock Assessment: A Summary of Good Practices`: https://www.fisheries.noaa.gov/resource/peer-reviewed-research/catch-unit-effort-modelling-stock-assessment-summary-good-practices

Ouros lesson:

`same catch != same evidence` when effort, location, gear or conditions differ.

A stable catch rate can also be misleading when a population aggregates strongly or fishing activity increasingly concentrates on the remaining high-density locations.

### 7. NOAA — data-limited assessments should remain data-limited

NOAA describes multiple stock-assessment model families chosen according to available evidence. Data-limited and index-based approaches provide narrower conclusions than richer age/length structured models.

Source:
- NOAA Fisheries, `Stock Assessment Model Descriptions`: https://www.fisheries.noaa.gov/insight/stock-assessment-model-descriptions

Reusable Ouros lesson:

Institutions should be allowed to publish:

- `DATA_LIMITED`;
- `LOW_CONFIDENCE`;
- `NO_CURRENT_ASSESSMENT`;
- `TREND_ONLY`;
- `ASSESSMENT_REJECTED_OR_UNSUITABLE`.

The simulation must not invent an exact hidden stock number merely because an NPC asks for one.

### 8. NOAA — assessment status can change when evidence is reviewed

NOAA's FY2025 stock-assessment report explains that assessments differ in data inputs and methods and may fail scientific review, in which case results are not used for management.

Source:
- NOAA Fisheries, `Fish Stock Assessment Report`: https://www.fisheries.noaa.gov/national/population-assessments/fish-stock-assessment-report

Reusable Ouros structure:

`draft assessment -> review -> accepted for current decision use | rejected/returned -> later revision`

A rejected assessment remains part of institutional history. It does not vanish from Chronicle.

### 9. NOAA — annual harvest rate and population size are separate dimensions

NOAA's 2026 stock-status updates distinguish whether annual fishing pressure is too high from whether a population is already too small.

Source:
- NOAA Fisheries, 2026 quarterly fishery stock status updates: https://www.fisheries.noaa.gov/national/population-assessments/fishery-stock-status-updates

Ouros lesson:

Avoid a single `fishery_health` score. Preserve at least:

- abundance/trend assessment;
- recruitment observations;
- activity/effort pressure;
- habitat/ecosystem context;
- uncertainty;
- management response.

### 10. NOAA — non-target interactions need their own evidence

Fishery observers collect information on target catch, catch composition, discards, protected-species interactions and gear configuration.

Source:
- NOAA Fisheries, `Using Observer Data`: https://www.fisheries.noaa.gov/national/fisheries-observers/using-observer-data

Reusable Ouros structure:

`activity -> target interaction + non-target interaction(s) -> disposition -> later observation/assessment`

A non-target Pokémon is not automatically a nuisance, pest or hostile combatant.

### 11. NOAA — release is not proof of zero effect

NOAA's catch-and-release guidance was updated August 4, 2026. It states that releasing an animal does not itself guarantee survival and that handling, gear, exposure and depth can affect outcomes. NOAA separately maintains release-mortality research because effects can be delayed.

Sources:
- NOAA Fisheries, `Catch and Release Fishing Best Practices`: https://www.fisheries.noaa.gov/national/resources-fishing/catch-and-release-fishing-best-practices
- NOAA Fisheries, `Fish Discard and Release Mortality Science`: https://www.fisheries.noaa.gov/national/bycatch/fish-discard-and-release-mortality-science

Ouros adaptation:

Record `RELEASED` separately from:

- `KNOWN_UNHARMED`;
- `INJURED`;
- `LATER_REOBSERVED`;
- `OUTCOME_UNKNOWN`.

Do not invent any of those later states merely because an interaction occurred.

### 12. NOAA — management controls can be narrow in time, space and method

A February 26, 2026 NOAA bulletin describes a seasonal closure of a spawning aggregation area with specific temporal and gear scope.

Source:
- NOAA Fisheries, 2026 spawning-aggregation closure bulletin: https://www.fisheries.noaa.gov/bulletin/reminder-seasonal-closure-mutton-snapper-spawning-aggregation-area-federal-waters-st-1

Reusable Ouros lesson:

A management measure should preserve:

- objective/rationale;
- geographic scope;
- temporal scope;
- activity/method scope;
- subject scope;
- issuing authority;
- evidence version;
- review date/end condition.

Do not import U.S. law, dates, species or gear rules.

## New design synthesis beyond Pass 70

Pass 70 correctly established that fishing effort, catch and stock state are different. Pass 157 adds a more explicit evidence hierarchy:

`raw activity/effort -> standardized index if appropriate -> independent survey -> biological/ecosystem evidence -> assessment version -> review state -> management decision`

It also adds a disposition distinction:

`interaction -> release/landing/capture referral/unknown -> later evidence`

and a management-scope distinction:

`ecological observation -> assessment -> authored institutional decision -> scoped measure`.

A spawning observation does not automatically create a closure. A closure does not prove spawning.

## Strong narrative structures

### Stable catches, rising effort

The harbor celebrates stable landings while crews work longer or farther away. The mystery is methodological/ecological before it is criminal.

### Independent survey and harbor ledger disagree

Both sources can be legitimate because they observe different portions of the system with different sampling behavior.

### A traditional closure no longer matches the biological window

Migration or phenology shifts, leaving an old management calendar increasingly mismatched with the event it was intended to protect.

### A released persistent Pokémon returns years later

The Chronicle can connect the same `pokemon_entity_id` across a release and later sightings without creating custody, ownership or guaranteed survival at the original event.

### Emergency harvest creates institutional inertia

A temporary crisis measure becomes socially expected. Ending it later can produce conflict even after the ecological/emergency reason disappears.

## Mechanics boundary

Pass 157 does not change Pass 70's PTU/Caelo guardrails.

Do not infer:

- stock abundance from PTU fishing success;
- fishing success from Minecraft bobber events;
- capture eligibility from a fishery rule;
- capture ownership from a landing record;
- population removal from KO/despawn;
- release survival from a battle result;
- Schooling/Pack Mon from narrative aggregation;
- Swim from fishing or handling proficiency;
- currents, drowning, lines, hooks, nets or restraint without exact validated mechanics.

## Source status

Research/provenance only. Pass 70 remains the existing Fisheries/Aquaculture authority.

The complete primary Caelo corpus was not reliably available through accessible project sources in this run. Super PTU Online Helper was not exposed as an invocable capability. No output from either has been invented.