# Meteorology, Forecasting & Weather Research — Pass 55

Status: research/provenance only. Not Ouros canon. External sources are inspiration or factual references, not PTU rules authority.

Date: 2026-08-20

## Why this pass exists

The repository already separates calendar, season phase, climate expectation and observed weather in `design/seasonality-calendar-phenology-layer.md`. It also lets crises carry forecasts and verified field reports in `design/crisis-rescue-recovery-layer.md`.

A missing layer remains between those systems:

- who observes weather;
- how observations are aggregated;
- how a forecast is issued and revised;
- how uncertainty is preserved;
- how microclimates differ across nearby locations;
- how forecast information reaches actors;
- how weather affects travel, ecology and institutions before it becomes a crisis;
- and when an overworld weather state is allowed to become authoritative PTU battlefield Weather.

Pass 55 researches that gap.

## Source 1 — Castform as a weather-linked Pokémon

Source: The Pokémon Company International, Castform Pokédex.

URL: https://www.pokemon.com/us/pokedex/castform

Useful facts:

- Castform changes form in response to weather.
- The official entry describes that transformation as a reaction to weather rather than a voluntary choice.
- Forecast is the named Ability associated with that transformation.

Reusable design lesson:

A Pokémon can be a weather-sensitive biological instrument or research subject without becoming a universal forecast machine. Ouros should record what an individual Castform actually demonstrates rather than granting perfect meteorological knowledge from species identity alone.

Do not infer:

- exact forecast range;
- exact forecast confidence;
- ability to control weather;
- ability to sense every weather phenomenon;
- automatic PTU mechanical transformation outside authoritative rules.

## Source 2 — Hoenn Weather Institute

Source: Bulbapedia summary of the Weather Institute from Pokémon Ruby/Sapphire/Emerald and ORAS.

URL: https://bulbapedia.bulbagarden.net/wiki/Weather_Institute

Useful structural facts:

- Hoenn has a dedicated institution that observes regional weather.
- Its role is institutional rather than a single NPC giving omniscient predictions.
- Weather information can identify unusual regional patterns.
- The location also has archival research and backup records.
- Weather research is valuable enough to intersect with antagonistic institutional conflict.

Reusable design lesson:

Ouros can support regional meteorological institutions, field stations, archives and observational networks. Forecasts should be records with source, issue time, area, horizon and confidence rather than mutable global prose.

Copyright boundary:

Do not copy Hoenn's institute, staff, Castform origin story, villains, weather-control machine or story events. Use only the abstract pattern of a persistent weather-research institution.

## Source 3 — Route 119 weather as regional identity

Source: Bulbapedia, Hoenn Route 119.

URL: https://bulbapedia.bulbagarden.net/wiki/Hoenn_Route_119

Useful structural facts:

- Route 119's frequent rain is part of the route's identity.
- Weather is persistent enough to affect battles there.
- Visual lightning can exist without representing a distinct battle effect.

Reusable design lesson:

Presentation weather and mechanical weather require separate state. A thunderstorm-looking sky can remain presentation-only unless the governing battle rules authorize a mechanical effect.

This distinction is directly useful for Minecraft/Cobblemon.

## Source 4 — Community fangame regional weather implementation

Source: Eevee Expo, Pokémon Expedition project page.

URL: https://eeveeexpo.com/threads/9300/

Useful structural patterns:

- weather can be regional rather than rolled independently per map;
- adjacent locations can share a moving system;
- seasonal probabilities can influence local conditions;
- forecasts can expose current state plus multi-day outlooks;
- weather can interact with encounter ecology.

Reusable design lesson:

Represent a weather system as a moving world-state object with spatial coverage. Avoid map-border weather roulette where crossing one block line changes the entire sky with no causal transition.

Do not copy the project's calendar, regions, probabilities, interface or content.

## Source 5 — Pokémon Essentials weather implementation pattern

Source: Eevee Expo, Weather System plugin for Pokémon Essentials.

URL: https://eeveeexpo.com/resources/1411/

Useful implementation pattern:

- weather state can advance according to elapsed game time rather than every frame;
- outdoor maps can query a weather state after a defined update interval;
- weather logic can coexist with separate time systems.

Reusable design lesson:

Ouros does not need continuous high-cost meteorological simulation. A coarse authoritative update cadence can drive persistent conditions while visual interpolation remains client-side.

## Source 6 — Forecast participation and weather literacy

Source: American Meteorological Society, “Public Engagement on Weather and Climate with a Monsoon Fantasy Forecasting Game.”

URL: https://journals.ametsoc.org/view/journals/bams/104/1/BAMS-D-22-0003.1.xml

Useful design lesson:

Forecasting itself can be an activity. Players can compare observations, make bounded predictions and later score those predictions against actual outcomes without requiring combat.

For Ouros, this suggests:

- forecast challenges;
- field-station calibration;
- citizen observations;
- research competitions;
- institutional reputation based on transparent historical forecast performance.

This should remain a knowledge/research system, not an invented PTU Skill bonus.

## Source 7 — Dynamic weather and environmental coherence

Source: Southern Methodist University programming thesis, “Procedural Terrain Generation with Biome Ecosystem and Dynamic Weather” (2025).

URL: https://scholar.smu.edu/guildhall_programming_etds/9/

Useful design lesson:

Dynamic weather can be produced from a spatial/biome system while preserving designer control. For Ouros, authored regional climate profiles should constrain procedural weather rather than letting global RNG invent physically incoherent transitions.

## Source 8 — Environmental storytelling warning

Source: “The Art of the Environment in Interactive Walking Simulation Narratives: How GenAI Might Change the Game” (2026).

URL: https://www.mdpi.com/2076-0787/15/1/13

Useful warning:

Reactive environments become less believable when weather behaves like an obvious emotional mirror of the player. Ouros weather should follow climate, geography, anomalies and authored supernatural causes. It should not start raining because a player made a sad choice unless a verified in-world mechanism caused that weather.

## PTU / Caelo / AutoPTU boundary checked this pass

The existing Ouros seasonality layer already states:

`calendar -> season -> climate expectation -> observed weather -> overworld consequences -> optional validated battlefield weather`

Pass 55 preserves that chain.

The available Python AutoPTU `battle_state.py` provides live evidence that the oracle contains weather-sensitive behavior, including:

- explicit weather state queries;
- sandstorm damage handling and immunities;
- hail/snow damage handling and immunities;
- Ability interactions such as Sand Force, Sand Rush, Sand Veil, Sand Stream, Ice Body, Snow Cloak, Snow Warning and Overcoat;
- Trainer Feature logic that can detect weather-related moves;
- weather-immunity temporary effects.

This is evidence that Python has concrete weather-related slices. It is not evidence that every PTU Weather rule is complete or that Java has parity.

The same Python file also contains terrain-linked effects. Weather and terrain therefore must remain separate capability families even when a scenario uses both.

No new Caelo-specific numerical weather rule was introduced in this pass. The primary Caelo PDFs were not reliably retrievable through the current file-search surface, so this pass deliberately avoids asserting exact Caelo Weather durations, damage, immunities or Feature interactions that were not re-read here.

## Live Java evidence

AutoPTU-Java was inspected read-only.

Live head observed during Pass 55:

`752603a002a31c8d73078ef238f22d2b39ccb024`

Newest change:

`Run RNG post-damage hooks after base damage resolution`

Observed evidence:

- selected RNG-consuming post-damage Ability hooks now run after ordinary damage RNG;
- the hook result is applied before HP/history mutation;
- selected behavior is covered by live tests;
- this strengthens ordering evidence for `full stateful damage pipeline` and `abilities`.

It does not add a verified battlefield Weather subsystem.

## Research synthesis for Ouros

The strongest reusable architecture is:

observation network -> observation records -> weather-system estimate -> forecast issue -> forecast revisions -> actor delivery -> operational decisions -> actual observed outcome -> forecast verification -> institutional memory.

World weather should be spatial and causal rather than map-local decorative RNG.

Forecasts must remain fallible records. A correct forecast does not become world truth before the event occurs. A wrong forecast remains historical evidence that can affect later trust, planning and institutional procedures.

Weather can create content before crisis scale:

- transport schedule changes;
- farmers adjust work windows;
- field researchers change survey plans;
- wild collectives shift activity time;
- festivals prepare alternate venues;
- construction delays work;
- photographers chase unusual cloud conditions;
- ferry operators alter routes;
- power operators stage crews;
- players help repair a station or retrieve a failed sensor.

## New-source avoidance note

This pass intentionally avoided reusing earlier narrative sources as primary evidence where possible. Castform, Hoenn meteorology, a current Eevee Expo weather implementation and meteorological-game research were used because previous passes had not formalized a dedicated forecasting layer.

## Canon boundary

Nothing in this research creates:

- Ouros weather agencies;
- regional climates;
- weather-control technology;
- Castform ownership;
- forecast accuracy formulas;
- tactical Weather effects;
- Survival/Technology Education/Perception DCs;
- weather damage;
- Lightning mechanics;
- movement penalties;
- visibility penalties;
- wind displacement;
- Minecraft weather-to-battle conversion.

Those remain authored canon or mechanics decisions.