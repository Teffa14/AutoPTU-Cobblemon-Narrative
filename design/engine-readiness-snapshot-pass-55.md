# Engine Readiness Snapshot — Pass 55

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.

Date inspected: 2026-08-20

## Repositories inspected

`Teffa14/AutoPTU-Java` read-only head:

`752603a002a31c8d73078ef238f22d2b39ccb024`

`Teffa14/AutoPTU` read-only head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

The narrative repository remains the only writable destination.

## Java change since Pass 54

Pass 54 inspected Java at:

`98b5aca32262f902f2260ab73b6d22a8b6e468d5`

The current head is:

`752603a002a31c8d73078ef238f22d2b39ccb024`

Newest change:

`Run RNG post-damage hooks after base damage resolution`

Observed evidence:

- RNG-consuming post-damage hooks can be resolved after ordinary damage calculation consumes its RNG;
- selected Ability behavior is registered through the post-damage hook pipeline;
- signed post-damage adjustment remains upstream of HP/history mutation;
- live tests verify RNG ordering for selected behavior;
- Java continues to derive results inside core rather than from Minecraft presentation.

This strengthens evidence for:

- `full stateful damage pipeline`;
- `abilities`;
- authoritative RNG ordering.

It does not prove either family complete.

## Java README boundary

The current README continues to state that Python AutoPTU remains authoritative while the port is incomplete.

The repository still lists the following broad work as unfinished:

- core battle state expansion;
- full damage resolution;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full semantic battle transcript parity;
- AI tactical scoring/policy;
- Craftics/Cobblemon adapter.

The README does list calculation primitives that include weather DB. That is a calculation primitive, not a complete battlefield Weather subsystem.

## Python weather evidence

Available Python `battle_state.py` shows real weather-related runtime behavior, including selected handling for:

- sandstorm end/phase damage and immunities;
- hail/snow end/phase damage and immunities;
- selected Weather-linked Abilities;
- weather-immunity temporary effects;
- weather-related Move detection in Trainer Feature logic.

This is evidence that Python has selected weather behavior.

It does not prove:

- every Weather condition is complete;
- every weather Move is implemented;
- every Ability interacting with Weather is implemented;
- every Weather duration/transition rule is complete;
- Java parity exists for the family;
- Minecraft weather can be copied directly into battle state.

## Permanent capability map

### VERIFIED

Targeting / footprints / range / LoS.

Base movement legality.

Core calculations.

Action economy / initiative.

AI legal-action infrastructure.

### PARTIAL

Full turn / round lifecycle.

Full stateful damage pipeline.

Status lifecycle.

Move-specific behavior.

Abilities.

Items.

Trainer Features / perks.

### BLOCKING

Complete movement including push / pull / knockback / interception / forced movement.

Terrain / weather / hazards / zones / broad reactions.

AI tactical policy.

Minecraft / Cobblemon / Craftics adapter and playback.

## Pass 55 weather-specific interpretation

The permanent category `terrain/weather/hazards/zones/reactions` remains BLOCKING.

Reasons:

- Java README still explicitly lists terrain and hazards as unfinished;
- no current Java contract was found for authoritative battle Weather state lifecycle;
- no current Java evidence proves Rain/Sun/Sand/Hail/Snow initialization, duration, replacement and expiry as one complete subsystem;
- Python slices do not establish Java parity;
- weather DB calculation support does not equal active Weather state;
- selected Ability hook progress does not prove Weather-linked Ability coverage.

## World-weather to battle-weather handoff — BLOCKING

No verified project contract currently proves an end-to-end path where:

1. Minecraft/Cobblemon supplies an observed overworld weather context;
2. server authority validates that context;
3. AutoPTU-Java initializes the correct PTU battlefield Weather;
4. Weather lifecycle and mechanical effects resolve inside battle core;
5. semantic events are returned for playback.

Pass 55 therefore treats overworld weather and battle Weather as separate states.

## Forecasting/world-state systems — narrative-side feasible

The following Pass 55 systems do not require missing tactical Weather support:

- weather observations;
- station status;
- forecast issue/revision history;
- forecast delivery;
- microclimate hypotheses;
- route/service decisions based on forecasts;
- forecast verification;
- archived misses;
- public corrections;
- weather-driven quest generation where the tactical battle remains static.

These can progress in the narrative/world-state repository before battle Weather parity exists.

## Encounter readiness — Ridge Station Recovery

### REDUCED

Weather remains presentation and world-state context. Station repair occurs outside battle. If combat occurs, use a static legal encounter.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- AI legal-action infrastructure — VERIFIED;
- move/Ability/item/Feature families — their respective PARTIAL state only when selected content requires them.

### FULL

Dynamic Weather and exposed battlefield zones participate in the fight while players protect or restore station equipment.

Dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/forced movement/interception — BLOCKING when wind displacement or movement reactions exist;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if Weather causes/removes statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL when used;
- Trainer Features/perks — PARTIAL when used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## Encounter readiness — Ferry Before the Front

### REDUCED

Resolve route timing, departure and forecast pressure in world state. Any battle uses one static vessel/dock layout. Weather is presentation-only.

### FULL

Allow a timed departure objective, exposed zones, changing Weather and possible wind displacement.

Primary blockers:

- terrain/weather/hazards/zones/reactions — BLOCKING;
- complete movement/forced movement/interception — BLOCKING;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Lifecycle and selected rule families remain PARTIAL when used.

## Encounter readiness — Forecast Lab Intrusion

### REDUCED

Keep data custody, system access and exterior weather outside battle. Use a static indoor encounter if confrontation occurs.

### FULL

Facility power/doors and weather-linked systems change the tactical space while actors pursue a data objective.

Primary blockers:

- terrain/weather/hazards/zones/reactions — BLOCKING if environment changes tactical state;
- AI tactical policy — BLOCKING for objective-aware behavior;
- adapter/playback — BLOCKING;
- full lifecycle — PARTIAL for timed transitions.

## No-inference rules retained

One weather-related calculation primitive does not prove Weather.

One Sandstorm or Hail branch in Python does not prove complete Weather coverage.

One Ability interacting with Weather does not prove Abilities.

One weather Move does not prove move-specific behavior.

A Minecraft rain particle does not create battle Rain.

A visual thunderstorm does not create Lightning damage.

An overworld wind description does not permit forced movement.

## Unresolved implementation questions

- What Java object will own battlefield Weather state?
- What initializes that state at encounter creation?
- How are Weather duration, replacement and expiry represented?
- Which Weather conditions are authoritative for the selected PTU/Caelo ruleset?
- Which weather Moves are currently complete in Python?
- Which Weather-linked Abilities are currently complete in Python?
- How will Java represent Weather semantic events?
- How will overworld weather be validated before battle initialization?
- Can a battle deliberately override local overworld weather for authored indoor/special encounters?
- How will replay/transcript state encode Weather changes?

Until those questions have tested contracts, mechanically active weather-heavy encounters should use reduced versions.