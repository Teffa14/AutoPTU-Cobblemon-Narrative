# Engine Readiness Snapshot — Pass 63

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live Java evidence

Newest inspected AutoPTU-Java commit:

`d2d232a4a5be9facbeaeea706081deb93b9c4b7c` — Port Chronicler profile match resolution (#225).

This is newer than the Pass-62 snapshot. It adds another parity-gated Chronicler slice and does not establish a new tactical family.

The current AutoPTU-Java README reports implemented slices including:

- targeting range, areas, footprints, target anchors and line of sight;
- Shift movement legality across existing Overland/Swim/Sky movement, terrain costs, blockers, Wallrunner, sprint and landing-fit boundaries;
- jump movement slices;
- Damage Base and type-effectiveness tables;
- calculation primitives including stages, accuracy stages, weather DB, crit probability, Burn, modifiers and rounding points;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow and action budget;
- deterministic initiative variants;
- legal action-space generation.

The same README still explicitly leaves unfinished:

- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic event/full BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Weather-specific interpretation

The Java README’s `weather DB` entry is a calculation primitive.

It does not establish:

- a battlefield Weather state controller;
- Weather lifecycle;
- weather-setting Moves;
- weather-removing Moves;
- weather-sensitive Ability hooks;
- weather-sensitive Item hooks;
- environmental zones;
- weather reactions;
- weather-aware tactical AI;
- synchronized Minecraft weather playback.

Therefore the permanent combined category `terrain/weather/hazards/zones/reactions` remains BLOCKING.

Similarly, Java Shift movement supporting terrain costs does not promote that combined environmental category. It proves a movement-legality slice only.

## Live Python evidence

Newest inspected AutoPTU commit:

`b77644e64596d40b5d712b261802bde19ae9d806` — Career: harden timeline numeric evidence (#160).

Recent adjacent commits reject malformed/coercible timeline values and malformed battle-quality hardware signals before they reach presentation/runtime surfaces.

These changes are robustness work. They do not add PTU tactical weather, forced movement, environmental hazards, AI policy or the Minecraft adapter.

The earlier Python boundary keeping rivalry continuity out of combat modifiers remains conceptually relevant: narrative state should not become a tactical modifier without an explicit mechanics contract.

Pass 63 applies that rule to forecasts, warnings, preparedness, observation confidence and institutional weather history.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No Pass-63 evidence justifies a category promotion.

## Weather-information non-inference gates

A forecast is not actual weather.

A weather observation is not a forecast.

A climate expectation is not actual weather.

A forecast warning is not route-closure authority unless canon explicitly grants that authority.

A forecast miss is not negligence, sabotage or incompetence.

A sensor outage is not proof of physical damage.

A missing observation is not clear weather.

Weather ending is not proof that a route, building, bridge or ferry is safe.

Weather visible in Minecraft is not automatically PTU battlefield Weather.

A narrative condition named rain, snow, fog, wind or heat does not automatically map to a PTU Weather state.

A weather calculation primitive does not prove the entire weather rules family.

A weather-associated Pokémon does not automatically have forecasting, rescue or occupational capability.

Type alone cannot create environmental competence.

Forecast confidence cannot modify Accuracy, Evasion, initiative, damage, Skills, Features, capture or AI behavior.

Institutional weather history cannot become a hidden combat buff.

## Encounter review — Ridgeline Evacuation Window

Narrative premise:

A revised forecast compresses the return window for a field team beyond an exposed ridge while wild Pokémon use the same approach.

Intended rich version may require:

- active battlefield weather;
- changing visibility or weather zones;
- validated gust/forced displacement;
- civilian or field-team withdrawal;
- route-clear/protection objectives;
- interception;
- objective-aware AI;
- synchronized Minecraft weather and movement playback.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL when exact statuses are involved
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Use forecast state to make the world decision before combat. Evacuate field staff and close the exposed section. If conflict remains, provide AutoPTU a static reviewed arena with no tactical Weather, gusts, escort rules or dynamic hazards. The battle result resolves the battle only. Travel/inspection state decides when the ridge can reopen.

## Encounter review — Weather Station Blackout

Narrative premise:

A remote observation node stops reporting while conditions deteriorate. The player needs to determine why without assuming the station was damaged or attacked.

Intended rich version may require:

- active rain/wind/lightning or another exact environment state;
- dynamic cover or safe zones;
- protected equipment objectives;
- retreat or territorial objectives;
- forced displacement and reactions;
- tactical AI that understands non-KO goals;
- persistent adapter playback and station state.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Keep the weather in overworld/world-state only. Remove noncombatants before tactical resolution. Investigate the node separately. If battle occurs, run a static sheltered encounter using individually verified mechanics. Maintenance/Communications resolves the observation-node repair afterward.

## Noncombat readiness

Pass-63 structures that can advance without new tactical engine families include:

- observation-node registry and operational state;
- forecast issue records;
- geographic scope and validity windows;
- qualitative confidence bands;
- forecast revision history;
- notice dissemination and acknowledgement;
- preparedness decision provenance;
- forecast verification against observations;
- microclimate claims with supporting/contradicting evidence;
- forecast-dispute investigations;
- route/event/facility/courier handoffs;
- station outage investigation when no tactical environment is simulated;
- preserving older forecasts and supersession history;
- post-weather inspection handoffs.

These need persistent world state and eventual UI/adapter surfaces, but they do not require PTU tactical Weather.

## Adapter implications

Minecraft/Cobblemon eventually needs a clean split between presentation and mechanics.

Safe future representations include:

- displaying a forecast board sourced from an issued forecast product;
- showing a station as offline when its operational state says so;
- changing a ferry departure board after Travel makes a decision;
- showing an event rain-plan overlay after Event Operations activates it;
- displaying temporary route barriers after the route owner closes access;
- showing weather visuals that match observed world state;
- exposing forecast revisions to players who have access to that information.

Unsafe shortcuts include:

- Minecraft rain independently enabling PTU rain bonuses;
- a visual thunderstorm applying damage or status without AutoPTU authority;
- Cobblemon AI changing behavior from forecast confidence;
- a sign or warning creating movement penalties;
- despawning NPCs or Pokémon as a substitute for owner-system evacuation state.

## PTU mapping requirement

Before overworld weather becomes tactical Weather, implementation must establish an explicit mapping contract.

That contract should identify:

- the PTU/Caelo source rule;
- source world-state conditions;
- lifecycle ownership;
- exact affected Moves;
- exact affected Abilities;
- exact affected Items;
- exact affected Trainer Features/perks;
- transcript events;
- AI implications;
- adapter rendering behavior;
- parity tests.

Until that contract exists, forecast and observed weather remain narrative/overworld state only.

## Pass-63 outcome

Weather can become much more operationally alive now without waiting for tactical-weather support.

Forecasts can affect planning, services, investigation, institutional memory and revisits while preserving uncertainty and provenance.

Mechanically rich weather encounters still require reduced static versions because the complete environmental family, forced movement, tactical AI and Minecraft/Cobblemon/Craftics playback remain blocking.

Capability classifications remain unchanged from Pass 62.