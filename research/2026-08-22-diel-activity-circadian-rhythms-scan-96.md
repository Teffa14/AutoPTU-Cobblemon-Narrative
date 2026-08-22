# Research Scan — Diel Activity, Circadian Rhythms and Daily Ecological Windows

Status: RESEARCH / PROVENANCE. Not canon. Not a PTU rules source.
Pass: 96
Date: 2026-08-22

## Why this pass exists

The existing repository already models seasonality, light/darkness, schedules, soundscapes, travel windows, public-space timing, wildlife collectives and persistent ecological observations. It does not yet give daily biological activity its own persistent authority.

This matters because `night` is a lighting/calendar fact, while `active at night` is a biological observation or hypothesis. A species, local population or individual can change its activity window without the sun setting at a different time.

The design target for Pass 96 is therefore a separate diel-activity layer that can represent:

- dawn and dusk activity peaks;
- nocturnal, diurnal, crepuscular and cathemeral patterns;
- rest/roost/refuge periods;
- feeding, migration, social and display windows;
- shifts caused by weather, temperature, human activity or ecological pressure;
- uncertainty and sampling bias;
- repeated observations across days, seasons and locations;
- persistent individual exceptions without rewriting species lore.

## Internal repository review

Before selecting this topic, the branch tree and the existing `design/`, `research/` and `proposals/` layers were inspected. Searches for `circadian`, `diel`, `crepuscular`, `diurnal`, `nocturnal`, `activity window`, `roost` and related terms returned no dedicated layer.

Closest existing responsibilities:

- `seasonality-calendar-phenology-layer.md` owns calendar and seasonal cycles;
- `light-darkness-night-ecology-layer.md` owns physical illumination and night visibility;
- `soundscapes-acoustic-ecology-layer.md` owns acoustic observations;
- `photography-visual-evidence-layer.md` owns timestamped visual evidence;
- `wild-collective-agency-layer.md` owns persistent wild groups;
- `world-agency-layer.md` and travel layers own schedules and actor actions;
- ecological habitat layers own place-specific physical state.

Pass 96 should consume those layers without replacing them.

## Pokémon official sources

### Pokémon Legends: Arceus — time of day changes discovery

Official gameplay guidance states that certain Pokémon behaviors, and sometimes entire species, may only be witnessed under the right conditions such as a particular time of day or weather. It also explicitly says different Pokémon are active during day and night and encourages revisiting the same area at different times.

Reusable structure:

- a location can remain physically unchanged while its observable biological community changes by time;
- repeated visits at different hours are legitimate exploration content;
- time-of-day discovery belongs in observation/world state before it becomes any battle rule.

Source:
https://legends.arceus.pokemon.com/en-gb/gameplay/

### Johto — recurring nighttime population and Trainer changes

The official Johto visitor guide notes that some Pokémon and Trainers only appear after dark and recommends revisiting open-air routes at night even after daytime exploration.

Reusable structure:

- a route can have multiple legitimate daily states;
- time-based recurrence creates reasons to revisit without procedural map regeneration;
- NPC schedule and wild activity can share a clock while remaining separate systems.

Source:
https://www.pokemon.com/us/strategy/a-visitors-guide-to-johto

### Hoothoot — internal clock as species behavior

The official Pokédex describes Hoothoot as possessing an extremely precise internal clock and moving its head in a fixed rhythm.

Reusable structure:

- some species can provide evidence about timing through observed behavior;
- species lore can justify a research hook without granting a generic time-sensing mechanic to all individuals;
- Hoothoot behavior is not proof that it knows absolute world time under every anomalous condition.

Source:
https://www.pokemon.com/us/pokedex/hoothoot

### Dreepy — evening-specific group behavior

The official Pokédex states that groups of Dreepy fly quickly over the ocean in the evening and interact with Pokémon in the water.

Reusable structure:

- a behavior can have a narrow daily window;
- activity can be group-specific and location-specific;
- an observed evening aggregation should not become a permanent collective location.

Source:
https://www.pokemon.com/us/pokedex/dreepy

### Oddish — day refuge and nighttime movement

An official Pokémon feature reproduces the Pokédex behavior that Oddish remains buried during the day and wanders at night while sowing seeds.

Reusable structure:

- rest/refuge state can be as important as active state;
- a species may alter both visibility and ecological function across the daily cycle;
- absence during daylight is not evidence of local population loss.

Source:
https://oddish.pokemon.com/en-au/

### Doduo — alternating sleep/watch behavior

The official Pokédex describes its two heads as alternating sleep and watch periods rather than sleeping simultaneously.

Reusable structure:

- rest state need not mean complete inactivity;
- individual biology can complicate binary awake/asleep assumptions;
- narrative rest should not be translated into PTU Sleep unless an actual mechanic applies.

Source:
https://www.pokemon.com/us/pokedex/doduo

## Ecological research sources

### Time can function as ecological niche space

Kronfeld-Schor and Dayan review diel temporal partitioning as an ecological dimension that can reduce overlap between competitors or predators and prey, while noting that activity patterns are constrained and not infinitely flexible.

Reusable structure:

- two populations can share the same physical habitat while using it at different hours;
- changes in overlap can create new encounter conditions without spatial migration;
- time partitioning should be evidence-backed rather than generated as arbitrary variety.

Source:
https://www.annualreviews.org/content/journals/10.1146/annurev.ecolsys.34.011802.132435

### Cathemerality prevents false day/night binaries

A 2024 Biological Reviews synthesis argues that activity across both day and night is widespread enough to treat cathemerality alongside nocturnal, diurnal and crepuscular patterns.

Reusable structure:

- Ouros should not force every species into one of two activity bins;
- activity windows can be broad, multi-peaked or flexible;
- local observations can differ from broad species expectations.

Source:
https://onlinelibrary.wiley.com/doi/full/10.1111/brv.13024

### Activity patterns are plastic and location-sensitive

A 2025 USGS-linked global study using millions of observations found frequent disagreement between simple literature classifications and measured local activity patterns. Activity timing can shift under anthropogenic change.

Reusable structure:

- authored species baselines should remain hypotheses/defaults, not immutable spawn law;
- local population histories can diverge after urbanization, tourism, heat, lighting or disturbance;
- an observed change should preserve both previous and current activity profiles.

Source:
https://pubs.usgs.gov/publication/70266263

### Sampling effort matters

USGS methodology guidance on diel activity emphasizes spatial variation, repeated observations and the risk of misleading conclusions when sampling effort differs across sites.

Reusable structure:

- five nighttime camera detections and zero daytime detections do not prove strict nocturnality if daytime effort was weak;
- activity estimates should retain sampling provenance;
- confidence can rise with repeated independent methods.

Source:
https://www.usgs.gov/publications/a-how-guide-estimating-animal-diel-activity-using-hierarchical-models

### Human disturbance can shift timing

USGS research on brown bears shows diel patterns can respond to human encroachment and temperature. A 2026 meta-analysis similarly examines how human disturbance alters predator-prey temporal overlap.

Reusable structure:

- roads, tourism, lighting and settlement activity can change when Pokémon use a place without immediately changing whether they use it at all;
- apparent population decline can instead be a detectability/time-window shift;
- ecological consequences should be generated from observed timing changes rather than assumed fear or hatred.

Sources:
https://www.usgs.gov/publications/diel-niche-brown-bears-constraints-adaptive-capacity-human-modified-landscapes
https://www.nature.com/articles/s41467-026-69113-9

## PTU / AutoPTU evidence and guardrails

The available Python battle-state evidence confirms exact combat mechanics for Sleep blockers such as Insomnia and Vital Spirit. It also shows that PTU-like Ability terms can have precise battle meanings.

Important non-inference:

- narrative sleep/rest/roost state is not the PTU Sleep status;
- Insomnia does not mean a Pokémon never rests in world ecology;
- Early Bird does not mean a Pokémon is naturally active at dawn;
- Vital Spirit does not define a diel niche;
- Illuminate does not grant a generic ecological light-attraction system;
- a nighttime encounter does not automatically grant tactical bonuses.

Available evidence:
`battle_state.py` shows Insomnia/Vital Spirit blocking Sleep in concrete status application paths.

The full primary Caelo corpus was not reliably recoverable during this run. No Caelo-specific rule for dawn/dusk, sleep ecology or time-of-day combat modifiers is asserted here.

## Design conclusions for Ouros

1. Daily biological timing deserves its own persistent state.
2. The smallest useful unit is usually population/location, not species globally.
3. Species lore can seed a prior expectation, but observations should be able to revise the local profile.
4. `resting`, `inactive`, `hidden`, `absent` and `undetected` must remain distinct.
5. Diel state should alter discovery opportunities before it alters battle mechanics.
6. Time-based wild presence must not become a direct rare-spawn exploit.
7. A shift from day to night activity can be a consequence of heat, light, roads, tourism or predators without requiring physical relocation.
8. The same population may show different profiles by season.
9. Camera, acoustic and direct-observation records should all feed one activity estimate with provenance.
10. Player absence should not permanently miss central content; repeated windows and archive evidence should support recovery.

## Candidate handoffs

Pass 96 should connect to:

- Calendar/Seasonality for local sunrise, sunset and seasonal day length;
- Light for actual illumination and artificial light;
- Meteorology/Urban Heat for temperature and weather context;
- Soundscape and Photography for observations;
- Wild Collectives/Interspecies Ecology for group and interaction timing;
- Tourism/Road Ecology/Public Space for disturbance schedules;
- Travel for time-window route opportunities;
- Conservation for quiet-hour or seasonal-time management;
- Cobblemon projection for bounded presence/activity changes;
- AutoPTU only after a battle snapshot is opened.

## Copyright and transformation note

No protected story prose, dialogue, distinctive characters or plots are copied into Ouros. Pokémon and ecological sources are used only for high-level structural patterns, species facts and design constraints. All worldbuilding candidates produced from this research are original and remain NON-CANON until reviewed.