# Engine Readiness Snapshot — Pass 125

Status: implementation-evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU were inspected read-only.

## Live heads inspected

AutoPTU-Java `main`: `554b97e44fca9736f98704f8db3b1a661c63e93f`

Newest Java slice: `Port Flower Veil combat-stage prevention (#157)`.

The slice adds an authoritative pre-mutation Combat Stage prevention boundary and ports Flower Veil / Flower Veil [Errata] behavior against a pinned Python oracle. The implementation evaluates active Ability holders, Grass-type targets and battle geometry/range before allowing an external negative Combat Stage mutation.

This strengthens evidence for:

- canonical Combat Stage mutation boundaries;
- Ability-specific prevention hooks;
- geometry-aware Ability behavior;
- ordered effect/event handling around a stage mutation.

It does not prove:

- the Ability catalog is complete;
- all Combat Stage prevention mechanics are ported;
- full status lifecycle;
- full move behavior;
- tactical group coordination;
- learned behavior;
- social learning;
- teaching;
- persistent wild-group knowledge;
- Minecraft behavior projection.

AutoPTU `main`: `cd2d31ab9438713629ad3fc65939e8cc622b5a1f`

Newest Python change verifies the deployable Career browser artifact and source provenance. It does not promote a battle capability family.

The latest Java Flower Veil parity workflow currently pins Python oracle commit `16d228efa63aabecb67fa788959a359aac7f8f03` for that contract. This does not replace the separate inspection of Python `main` above.

## Current Java README evidence

The live Java README explicitly marks the following broad areas incomplete:

- broader canonical combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/Perk/Trainer Feature hook registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative rule slices must not be promoted to family-complete coverage.

## Permanent capability map

VERIFIED:

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL:

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING:

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 125.

## Why social learning remains overworld state

Nothing inspected in Java or Python establishes an authoritative battle subsystem for:

- individual behavioral innovation;
- socially acquired behavior;
- learned vocal repertoires;
- transmission between demonstrator and observer;
- teaching hypotheses;
- population-level tradition adoption;
- tradition revision over years;
- loss of experienced individuals as knowledge loss;
- local behavioral variants;
- observation effort for tradition research;
- behavior transmission during unloaded chunks;
- cultural/behavioral projection into Cobblemon groups.

Those belong to world persistence, observation and research state.

AutoPTU should receive only actual combatants plus the frozen tactical state required for a confrontation.

## Important non-mechanical boundary

A behavior can be learned and narratively important while having zero battle effect.

Examples:

- a Chatot group sharing a local phrase;
- a wild collective using one safe crossing;
- urban Pokémon learning a container-opening sequence;
- a group preserving a foraging technique;
- experienced individuals influencing naïve route use.

None establishes:

- a Move;
- an Ability;
- a Feature;
- Pack Mon;
- Receiver;
- a Skill rank;
- action economy;
- coordinated target selection;
- ally status;
- Loyalty;
- command authority;
- AI tactical policy.

The latest Flower Veil implementation is a useful example of the opposite case: a specific effect becomes mechanical only because a precise Ability rule is implemented and parity-tested. Narrative learned behavior does not receive the same authority by analogy.

## Encounter dependency map — Orchard Technique Survey

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving resource objectives, active interception and withdrawal
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if an environmental object or route is given a tactical field effect
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for ACCESS_RESOURCE / WITHDRAW / PROTECT_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Observation, resource access, adoption and any social-transmission hypothesis remain overworld state. If conflict remains after noncombatants clear the site, AutoPTU receives a static orchard edge and only actual combatants. Battle outcome cannot prove or disprove a tradition.

## Encounter dependency map — Chatot Chorus Shift

FULL version if tactical disturbance is included:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including interception/forced movement: BLOCKING for group dispersal and protected retreat paths
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if a validated tactical environment effect is active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for DISPERSE / REACH_ROOST / AVOID_CONFLICT
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Repertoire observation, recordings, route/contact hypotheses and dispersal happen in world state. Any unrelated combat starts after the chorus has moved out of the tactical perimeter. No Sonic, Chatter, language or morale rule is invented.

## Encounter dependency map — The Last Demonstrator

FULL version:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving search/reunion/pursuit objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when route hazards are represented tactically
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for REACH_GROUP / WITHDRAW / FOLLOW_SAFE_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Tracking, route reconstruction and reunion resolve in overworld state. A separate threat may produce a normal static battle. Finding the experienced Pokémon does not grant ownership, partnership, command authority or proof that it taught the local technique.

## New overworld blockers introduced by Pass 125

- `BEHAVIOR_OBSERVATION_LEDGER`
- `LOCAL_BEHAVIOR_PATTERN_REGISTRY`
- `BEHAVIOR_INNOVATION_EVENT`
- `SOCIAL_TRANSMISSION_OBSERVATION`
- `BEHAVIORAL_TRADITION_ASSESSMENT`
- `TRADITION_ADOPTION_SNAPSHOT`
- `TRADITION_REVISION_HISTORY`
- `TRADITION_KEY_INDIVIDUAL_LINK`
- `TEACHING_HYPOTHESIS_STATE`
- `TRADITION_DISRUPTION_CASE`
- `BEHAVIOR_INTERVENTION_PROVENANCE`
- `TRADITION_TO_WILD_COLLECTIVE_HANDOFF`
- `TRADITION_TO_SOUNDscape_HANDOFF`
- `TRADITION_TO_LANGUAGE_HANDOFF`
- `TRADITION_TO_MIGRATION_HANDOFF`
- `TRADITION_TO_URBAN_WILDLIFE_HANDOFF`
- `TRADITION_TO_POKEMON_AGENCY_HANDOFF`
- `TRADITION_TO_RESEARCH_ETHICS_HANDOFF`
- `TRADITION_TO_CONSERVATION_HANDOFF`
- `TRADITION_TO_COBBLEMON_PROJECTION`
- `TRADITION_TO_MINECRAFT_PRESENTATION`
- `TRADITION_TO_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 125

Do not infer:

- repeated behavior -> social learning;
- group behavior -> culture;
- co-location -> imitation;
- demonstration -> teaching;
- social organization -> Pack Mon;
- local behavior -> species-wide behavior;
- behavioral tradition -> PTU mechanic;
- shared vocalization -> language;
- Chatot speech mimicry -> translation authority;
- Passimian group organization -> shared initiative or tactical bonuses;
- experienced Pokémon -> leader;
- older Pokémon -> parent or teacher;
- observer later performing a behavior -> proven copying without alternatives considered;
- one innovator -> established tradition;
- one missing season -> tradition loss;
- one absent individual -> knowledge loss;
- behavioral change -> Evolution;
- behavioral difference -> regional form;
- environmental similarity -> common social origin;
- released former partner -> renewed Trainer authority;
- wild group learning from a released partner -> Trainer ownership of the group;
- Minecraft path repetition -> learned route;
- loaded subgroup -> population adoption rate;
- despawn -> loss of behavior;
- battle victory -> tradition restoration;
- battle withdrawal -> learned migration change.

## PTU/Caelo validation state

Repository code search did not expose a generic AutoPTU/AutoPTU-Java subsystem named or clearly equivalent to social learning, behavioral tradition, teaching or population knowledge transfer.

Official Pokémon behavior is inspiration/species grounding, not PTU rules authority.

PTU public GM guidance supports characterizing Pokémon outside combat and non-violent wild interaction, but it does not establish a generic tradition mechanic.

The complete primary Caelo Player’s Guide/rulebook/errata corpus was not reliably exposed through the available runtime. Super PTU Online Helper was not available as an invocable capability.

No result is invented for either source.

## Current conclusion

Pass 125 can advance safely without new battle mechanics.

The persistent value is in observing behavior across individuals and years, recording possible transmission, preserving repertoire revisions, linking persistent Pokémon to local knowledge and allowing traditions to change or disappear only when evidence supports it.

Mechanically rich versions that require group retreat, following, moving objectives or deliberate route protection remain blocked primarily by complete movement, AI tactical policy and Minecraft/Cobblemon/Craftics playback.

The reduced versions preserve the same narrative premise by resolving learning, transmission and population movement in world state and using AutoPTU only for conventional static combat when a real confrontation exists.