# Engine Readiness Snapshot — Pass 161

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `5f452c7e0fc938dd83bc323c5363971367ed686a`
Date: 2026-08-31

## Read-only engine heads inspected

AutoPTU-Java:

`4250bdda97ac354da5c291154ff17b43b342e337` — merged PR #299, `Compose Thrust through generic forced-movement ability modifiers`.

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

No file in either engine repository was modified by Pass 161.

AutoPTU-Java advanced from the Pass 160 head `e8bbd584cd55654b72d52117ee410d7e738f93b6`. AutoPTU did not advance.

## New Java evidence — PR #299

The merged PR describes a server-owned forced-movement Ability modifier path derived from the pinned Python oracle.

Its declared behavior includes:

- a declarative forced-movement Ability modifier resolver rather than adapter-owned per-Ability handling;
- composition after canonical Move Push/Pull resolution;
- Ability suppression handling;
- Python-oracle parity fixtures for the exact Thrust branch;
- creation of Push 1 for qualifying Physical Moves;
- addition of +1 to an existing Push;
- leaving Pull unchanged;
- rejection of Special cases and suppressed-Ability cases.

Changed files include a core Ability modifier resolution object, the runtime forced-movement Move application, runtime tests, oracle-parity tests and Python fixture export tooling.

This is meaningful live evidence for two permanent families:

- complete movement including push/pull/knockback/interception/forced movement;
- abilities.

The evidence remains representative rather than exhaustive.

Still unverified globally include:

- every Ability that can alter movement;
- exhaustive Push/Pull Move interactions;
- general Knockback semantics and every source;
- every Intercept variant and ordering interaction;
- arbitrary forced movement from non-Move/non-Ability sources;
- escort/rescue movement;
- object carrying;
- crowd routing;
- moving vehicles/platforms/scenery;
- height/fall semantics needed by rich rooftop encounters;
- generalized reaction windows;
- dynamic tactical objectives;
- tactical protect/deny/withdraw/evacuate policy;
- complete adapter/playback parity for forced-movement presentation.

Therefore no permanent capability category is promoted by Pass 161.

## Permanent capability map

VERIFIED:

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING:

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Why movement remains PARTIAL

Pass 160 already had positive server-owned evidence for generic Push/Pull Move resolution, stale target revalidation and shared partial-stop behavior.

PR #299 adds another important composition layer: the runtime can alter forced movement through a canonical Ability interaction while respecting suppression and a pinned Python oracle.

That still does not prove the whole permanent movement family. The category deliberately includes Push, Pull, Knockback, Interception and other forced-movement sources and ordering interactions. Escort, carrying, route control, moving geometry and generalized reactions also remain relevant to mechanically rich Narrative concepts.

The project rule remains conservative: representative mechanics strengthen evidence without promoting a family until the full contract is verified.

## Why Abilities remain PARTIAL

Thrust parity is good evidence for one Ability interaction family. It does not prove exhaustive Ability coverage, trigger ordering, suppression behavior across all abilities, status/terrain interactions, lifecycle integration or all adapter outputs.

Abilities therefore remain PARTIAL.

## AutoPTU evidence

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The commit explicitly describes viewport-resize coordinate synchronization as presentation-only and states that battle rules and outcomes do not change.

It creates no new evidence for any permanent mechanics category.

## Broadcast-specific PTU/Caelo boundary

The project source priority remains PTU Core Rulebook, Pokédex material, Caelo Player's Guide, Caelo rulebook/errata, character-creation material and Caelo Region Location & Encounter List.

Pass 161 found no internal authority establishing a universal broadcast subsystem.

UNKNOWN until exact source and implementation review:

- camera or microphone equipment mechanics;
- broadcasting or journalism Skill Checks with universal effects;
- remote Trainer command via television/radio/streaming;
- combat targeting or PTU line of sight from camera feeds;
- remote viewer effects on initiative, AP, accuracy, damage, movement or morale;
- Coordinator, Cheerleader or other Trainer Feature effects triggered merely by a broadcast audience;
- remote Contest judging;
- fame/reputation progression from viewer counts;
- signal-jamming/interception rules;
- Telepathy or Psychic communication functioning as region-scale broadcast without exact mechanics;
- Electric Pokémon automatically powering or amplifying communication infrastructure;
- Rotom-like Pokémon automatically controlling a device;
- archive recordings functioning as unquestionable evidence;
- sponsorship/ad revenue formulas;
- consent, licensing or media-rights mechanics.

## Encounter A — Studio Evacuation Access Corridor

Narrative premise: a hostile or wild-Pokémon incident blocks immediate studio access while a transmission is scheduled or underway.

Full version capability requirements:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED for static geometry
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL for contested withdrawal/protection
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL for staged evacuation and interruption timing
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if smoke, live equipment danger, moving zones or generalized reactions matter
- move-specific behavior — PARTIAL; individual audit required
- abilities — PARTIAL; individual audit required
- items — PARTIAL; individual audit required
- Trainer Features/perks — PARTIAL; individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw/route-control behavior
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for semantic studio/evacuation playback

Overall full status: BLOCKED.

Reduced status: READY at narrative-contract level if selected combat content is individually audited.

Reduced constraints:

- crew, guests and noncombatant Pokémon are already in a safe authored state before initiative;
- the broadcast transmission is marked INTERRUPTED before the battle begins;
- studio equipment and hazards remain outside BattleSpec;
- geometry is static;
- explicit combatants only;
- permitted output: `IMMEDIATE_STUDIO_ACCESS_ROUTE_CLEAR`.

Hard safeguards:

`IMMEDIATE_STUDIO_ACCESS_ROUTE_CLEAR != STUDIO_EVACUATED`

`BATTLE_WON != BROADCAST_RESUMED`

`VISIBLE_STUDIO_EQUIPMENT != PTU_HAZARD`

## Encounter B — Relay Rooftop Perimeter

Narrative premise: an immediate approach to a relay or rooftop broadcast position is contested.

Full version can require:

- complete movement for displacement near edges;
- lifecycle for staged access/withdrawal;
- terrain/weather/hazards/zones/reactions for wind, rain, edge danger, falling and generalized reactions;
- tactical policy for route control/protection;
- adapter/playback for semantic height and relay state.

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- use a safe bounded static platform;
- no fall/edge/weather mechanics;
- relay technical state stays outside BattleSpec;
- no repair or verification is implied;
- permitted output: `IMMEDIATE_RELAY_APPROACH_CLEAR`.

Hard safeguards:

`IMMEDIATE_RELAY_APPROACH_CLEAR != SIGNAL_RESTORED`

`BATTLE_WON != NETWORK_PATH_VERIFIED`

`MINECRAFT_HEIGHT != AUTOMATIC_PTU_FALL_RULE`

## Encounter C — Field Crew Withdrawal Corridor

Narrative premise: a field crew needs to leave an area while a separate tactical threat occupies an immediate corridor.

Full version requires escort/withdrawal semantics, possibly object carrying, complete movement, lifecycle and tactical policy.

Overall full status: BLOCKED.

Reduced status: READY.

Reduced constraints:

- crew and equipment are moved outside the tactical slice before initiative;
- their safe destination is authored by Ouros;
- no carrying/escort objective is simulated;
- battle occurs on static geometry;
- permitted output: `IMMEDIATE_FIELD_EXIT_CORRIDOR_CLEAR`.

Hard safeguards:

`IMMEDIATE_FIELD_EXIT_CORRIDOR_CLEAR != CREW_DEPARTURE_COMPLETED`

`CREW_DEPARTURE_COMPLETED != FOOTAGE_PRESERVED`

`BATTLE_FAILURE_WITHOUT_ESCORT_CONTRACT != CREW_HARM_CONFIRMED`

## Encounter D — Broadcast Battle Coverage

Narrative premise: a formal or otherwise valid AutoPTU battle is transmitted to an audience.

Baseline status: READY at narrative-contract level when the actual selected battle content is individually verified.

The baseline adds no tactical mechanic. Sequence:

1. Ouros determines the authoritative BattleSpec and event context.
2. AutoPTU resolves legal combatants, actions and results.
3. Broadcast continuity links a transmission to battle facts exposed through supported outputs.
4. Media produces attributed commentary/publication packets.
5. Communications Network and Media determine where transmission and receipt occurred.

This baseline does not require tactical AI to understand spectators, cameras or broadcasting.

A richer synchronized spectator version remains BLOCKED by Minecraft/Cobblemon/Craftics adapter/playback support and any unverified semantic camera/replay integration.

Hard safeguards:

`BROADCAST_BATTLE != SPECIAL_BATTLE_RULESET`

`CAMERA_FEED != TARGETING_LOS`

`COMMENTARY != BATTLE_EVENT`

`REPLAY != BATTLE_REWIND`

`SIGNAL_LOSS != BATTLE_INTERRUPTED`

`VIEWER_POLL != BATTLE_RESULT`

## AI boundary

AI legal-action infrastructure remains VERIFIED.

AI tactical policy remains BLOCKING for the full rich incident versions because those concepts require semantic reasoning such as:

- protect a studio exit rather than maximize damage;
- delay while another actor withdraws;
- avoid a noncombatant production area;
- contest relay access without treating the relay as an ordinary combat target;
- understand route-clearing completion;
- withdraw after an objective changes.

Legal-action enumeration does not prove these policies.

Broadcast commentary, stream chat or remote viewers may never substitute for AI policy.

## Adapter/playback boundary

Minecraft/Cobblemon/Craftics may display already-authoritative broadcast state through studios, screens, presenters, antennae, cameras, vehicles, crowds, overlays or archived replay interfaces.

It may not derive:

- combatants from visible entities;
- targeting or LoS from camera visibility;
- BattleSpec from broadcast rosters;
- hit/miss from animation;
- HP/status/damage from spectator UI;
- Move legality from commentator text;
- battle interruption from signal loss;
- signal restoration from redstone or block state;
- program receipt from loaded chunks;
- archive authenticity from a file existing client-side;
- audience belief, fame or reputation from crowd size;
- any PTU outcome from Cobblemon BattleState.

The permanent adapter/playback family remains BLOCKING.

## Canon unresolved questions

Pass 161 leaves these setting facts unresolved:

- which Ouros regions have radio, television, livestream-like systems or other authored broadcast technology;
- which institutions operate broadcast channels;
- which recurring programs are canon;
- whether formal battles, Contests, civic meetings, festivals or expeditions are routinely broadcast;
- where regional feed boundaries exist;
- what presenter/reporter careers already exist;
- whether local operators use emergency overrides and under what authored authority;
- how archives capture studio masters versus air feeds;
- what player-character consent rules govern interviews, quotation and broadcast appearances;
- whether sponsor/ad relationships exist and which system owns them;
- whether any exact PTU/Caelo capability interacts mechanically with broadcast equipment;
- how much synchronized spectator playback the Minecraft adapter will eventually support.

## Pass 161 conclusion

The new broadcast layer can progress immediately as persistent world state because most program, episode, schedule, transmission, feed and archive relationships are narrative/information continuity rather than battle mechanics.

Rich evacuation, rooftop, escort and semantic-objective versions remain blocked by their exact permanent capability families. A normal battle may still be covered by a broadcast today because the broadcast remains an observer of AutoPTU-authoritative facts rather than another rule engine.

No permanent engine category is promoted in Pass 161.