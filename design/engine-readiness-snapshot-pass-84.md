# Engine Readiness Snapshot — Pass 84

Status: implementation-evidence snapshot for narrative dependency planning. This document does not modify AutoPTU-Java or AutoPTU.

Inspected: 2026-08-21.

## Live revisions

AutoPTU-Java `main` inspected at:

`fb91a65dc3bd92f49c7020ec856406df78bfc70a`

Latest visible commit:

`Own delayed-hit queue and RNG in BattleRuntimeState`

Pass 83 head:

`a5a77bd23cbe9841d896b901522de83e7d4280a8`

The current head is three commits ahead of the earlier delayed-hit baseline `3c82018e8f9f123500688d59cc94eba565593231`.

AutoPTU Python remains the project-designated oracle while Java parity is incomplete. No Python change inspected in this pass justifies changing the permanent category map.

## New Java evidence relevant to Pass 84

The current Java head moves two important mutable resources under `BattleRuntimeState` ownership:

- the delayed-hit queue;
- the Python-compatible battle RNG stream used by delayed-hit lifecycle execution.

The runtime now exposes a read-only delayed-hit snapshot while scheduling/execution boundaries remain inside the core package. Mature combatant-target delayed hits can re-enter the normal authoritative target/attack path without Minecraft owning their queue or RNG.

This is useful authority work for future mountain encounters because a renderer or adapter must not invent delayed results or rolls.

It does not implement mountain systems.

## What the new evidence does not prove

Do not infer:

- complete delayed-hit coverage, including all tile/area semantics;
- full `BattleSpec -> BattleTranscript` parity;
- complete turn/round lifecycle;
- falling or cliff-edge rules;
- climbing movement;
- altitude bands;
- wind displacement;
- avalanche or rockfall hazards;
- dynamic snow;
- high-altitude Weather;
- visibility changes by elevation;
- objective-aware evacuation/withdrawal AI;
- interactable mountain infrastructure;
- Minecraft/Cobblemon playback.

## Java README boundary

The current AutoPTU-Java README still lists unfinished work for:

- core combatant/grid battle state expansion;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic event emission and full transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

This remains the anti-overclaim boundary.

# Permanent capability categories

## VERIFIED

### targeting/footprints/range/LoS

VERIFIED for implemented static geometric targeting.

Pass 84 guardrail:

Geometric LoS does not prove visibility through fog/cloud, altitude-relative sight, glare, ridge masking beyond represented blockers, falling line-of-fire or multi-level targeting.

A reduced mountain encounter may use a single frozen 2D/static geometry snapshot.

### base movement legality

VERIFIED for implemented Shift/Jump and Overland/Swim/Sky surface.

Pass 84 guardrail:

This does not prove climbing, scrambling, rope movement, ledge hanging, slope failure, altitude transitions, vertical multi-level maps, passenger transport, mountaineering endurance or falling.

### core calculations

VERIFIED for ported primitives.

Pass 84 guardrail:

There is no generic `high altitude`, `steep slope`, `summit`, `thin air`, `cold ridge`, `mountain shelter` or `treeline` bonus/penalty.

### action economy/initiative

VERIFIED for the implemented surface.

The latest runtime-owned delayed-hit/RNG work preserves the rule that battle timing and randomness remain core-owned.

Pass 84 guardrail:

Expedition legs, ascent time, shelter windows, route closures and weather forecast windows are overworld clocks unless an exact tactical mechanic says otherwise.

### AI legal-action infrastructure

VERIFIED for supported legal choices.

It does not establish policy goals such as:

- REACH_PASS_EXIT;
- WITHDRAW_DOWNSLOPE;
- PROTECT_SURVEY_MARKER;
- EVACUATE_SHELTER;
- AVOID_CLIFF_EDGE;
- SEEK_COVER_FROM_WIND;
- HOLD_RELAY_PLATFORM;
- ESCORT_NONCOMBATANT;
- RETREAT_TO_STAGING_SITE.

## PARTIAL

### full turn/round lifecycle

PARTIAL.

Java has authoritative initiative/phase infrastructure, selected cleanup and hook surfaces, delayed-hit state and execution slices, and now runtime-owned delayed-hit queue/RNG authority.

It still does not prove every phase effect, duration, delayed form, switch/send-out flow, reaction or transcript event.

### full stateful damage pipeline

PARTIAL.

Covered move/delayed paths increasingly derive and mutate state inside the battle core.

The README still declares full damage resolution unfinished.

Pass 84 guardrail:

A collision with a cliff, boulder, shelter wall or snowbank cannot create damage unless an authoritative mechanic produces it.

### status lifecycle

PARTIAL.

Selected statuses have application/phase/expiry evidence. Full coverage is incomplete.

Pass 84 guardrail:

Altitude, cold, wind, exertion, fear, snow glare, thin air or exposure cannot generate Slowed, Tripped, Frozen, Confused, Blinded, Injured or other battle Status by narrative description.

### move-specific behavior

PARTIAL.

Representative Move contracts and delayed-hit paths exist. Full library behavior is not proven.

Pass 84 guardrail:

A Move that visually pushes air, breaks rock, creates snow, climbs, flies or teleports cannot be assigned mountain traversal/hazard behavior without exact implementation evidence.

### abilities

PARTIAL.

Representative Ability hooks have parity evidence. The family remains incomplete.

Pass 84 guardrail:

Species flavor such as mountain residence, snow travel or herd leadership never grants unimplemented battle behavior.

### items

PARTIAL.

Representative held-item state/effects exist. Complete item coverage does not.

Pass 84 guardrail:

Ropes, crampons, climbing gear, radios, route markers, oxygen equipment, shelters and survey instruments remain world-state assets unless validated as PTU Items with mechanics.

### Trainer Features/perks

PARTIAL.

Representative Features and hook infrastructure exist. The complete catalog is not ported.

Pass 84 guardrail:

The Python oracle contains a concrete Wilderness Guide branch for `mountain`/`cave`. That proves only the exact feature behavior when legally present and activated. It does not make every mountain actor hazard-immune and does not prove Java parity for the complete feature.

## BLOCKING

### complete movement including push/pull/knockback/interception/forced movement

BLOCKING as a family.

Pass 84 FULL encounters need this for:

- cliff-edge displacement;
- intercepting actors on narrow passes;
- forced retreat routes;
- moving through chokepoints with conflicting flows;
- escort/evacuation movement;
- any future wind/avalanche displacement;
- multi-level positional interactions if designed.

### terrain/weather/hazards/zones/reactions

BLOCKING as a family.

Pass 84 FULL concepts may eventually need:

- exposed/sheltered wind zones;
- changing cloud/fog visibility;
- snow or ice terrain effects;
- falling-rock zones;
- avalanche paths;
- summit Weather;
- cliff/ledge hazards;
- interactable shelter/relay zones;
- environmental reactions.

None may be fabricated by the adapter.

### AI tactical policy

BLOCKING.

Legal choices exist, but there is no verified mountain-aware scoring for withdrawal, sheltering, protected survey points, evacuation, route objectives, avoiding cliffs or preserving infrastructure.

### Minecraft/Cobblemon/Craftics adapter/playback

BLOCKING.

There is no verified end-to-end contract that turns server-owned mountain state into a battle snapshot and then replays semantic outcomes in Minecraft without duplicating PTU rules.

# Pass 84 encounter dependency summary

## Treeline Survey Dispute

VERIFIED:

- targeting/footprints/range/LoS for static geometry;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- lifecycle;
- stateful damage if combat occurs;
- statuses/moves/abilities/items/Features used by actual combatants.

BLOCKING for FULL version:

- complete movement/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- tactical AI;
- adapter/playback.

Reduced version is viable as overworld survey plus static standard battle.

## Pass Shelter Evacuation

FULL version additionally requires protected/exit objectives and noncombatant/escort policy, both currently unsupported at the required level.

Reduced version resolves evacuation before combat.

## Summit Relay Failure

FULL version needs interactable objective state, environmental projection and tactical objective policy.

Reduced version keeps relay/weather/repair outside the grid and uses a static battle only when needed.

# Overworld blockers introduced by Pass 84

These do not belong inside AutoPTU-Java:

- `MOUNTAIN_SYSTEM_STATE`;
- `VERTICAL_ECOLOGICAL_ZONE_GRAPH`;
- `SLOPE_ASPECT_SECTOR_STATE`;
- `TREELINE_REVISION_HISTORY`;
- `MOUNTAIN_PASS_ENVIRONMENT_CONTEXT`;
- `STAGING_SITE_STATE`;
- `MOUNTAIN_OBSERVATION_PROVENANCE`;
- `MOUNTAIN_TO_TRAVEL_PROJECTION`;
- `MOUNTAIN_TO_CRYOSPHERE_PROJECTION`;
- `MOUNTAIN_TO_FLORA_PROJECTION`;
- `MOUNTAIN_TO_COBBLEMON_PROJECTION`;
- `MOUNTAIN_TO_BATTLE_SNAPSHOT`.

# Live evidence citations retained for project review

AutoPTU-Java current head inspected:

`fb91a65dc3bd92f49c7020ec856406df78bfc70a`

Current README continues to state that Python remains authoritative while the port is incomplete and that full damage, status/terrain/hazard/forced-movement/reaction coverage, registries, AI policy and Minecraft adapter are unfinished.

# Unresolved rules questions

Before a FULL mountain encounter enters production, extract exact PTU/Caelo authority for:

- climbing/scrambling;
- falling;
- Jump versus vertical traversal;
- Wallrunner;
- Naturewalk (Mountain), if applicable;
- Wilderness Guide;
- Mountable/Sky passenger behavior;
- high-altitude or exposure rules, if any;
- environmental wind/snow/rock hazards;
- visibility under cloud/fog;
- any rule that changes movement or Accuracy by mountain terrain.

Primary Caelo source material was not reliably recoverable in this runtime. No new Caelo-specific rule is asserted in Pass 84.