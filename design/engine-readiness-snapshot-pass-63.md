# Engine Readiness Snapshot — Pass 63

Status: implementation evidence snapshot for narrative planning. Not a substitute for tests, PTU/Caelo source text or engine acceptance gates.

Date: 2026-08-20

## Repositories inspected

Read-only:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

Writable destination:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

## AutoPTU-Java live evidence

Current inspected Java head:

`44f7d67afe7573593e996ebc39c99cd188c88f1d`

Latest inspected commit:

`Port initiative additional bonus family (#96)`

Canonical URL:
https://github.com/Teffa14/AutoPTU-Java/commit/44f7d67afe7573593e996ebc39c99cd188c88f1d

This follows:

`a5d6221ab13a9f249656da2e0a55fe866791e156` — `Port initiative weather and terrain speed abilities (#95)`.

New bounded evidence since Pass 62 includes:

- initiative-time Slush Rush parity;
- initiative-time Surge Surfer parity;
- initiative-time Chlorophyll [Errata] parity;
- weather, terrain, grounded state and HP passed as semantic inputs to that resolver;
- Early Bird [Errata] initiative contribution;
- Agility Training initiative contribution;
- Rider doubling for that Agility Training slice;
- Hardened Initiative contribution;
- Python-oracle fixtures, Java tests and CI wiring for both slices.

These commits strengthen the already-VERIFIED action economy / initiative category and add specific evidence inside the PARTIAL Abilities / Trainer Features families.

They do not prove runtime battlefield terrain/weather, broad reaction handling or full Feature/Ability catalogs.

## Why commit #95 does not promote terrain/weather

`InitiativeSpeedAbilityResolution` accepts authoritative semantic inputs such as weather name, terrain name and grounded state in order to calculate selected initiative-time Ability effects.

That proves a bounded consumer of those inputs.

It does not prove:

- creating Weather in battle;
- changing Weather;
- Weather duration;
- battlefield terrain creation/removal;
- weather damage;
- terrain entry/exit behavior;
- zones;
- hazards;
- broad reactions;
- adapter synchronization from Minecraft weather;
- complete Ability interactions with Weather/Terrain.

Therefore `terrain / weather / hazards / zones / reactions` remains BLOCKING.

## Java README boundary

The current README continues to state that Python AutoPTU remains authoritative while the Java port is incomplete.

It still lists unfinished broad work including:

- core combatant/grid battle state expansion;
- full damage resolution pipeline;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/item/perk/Trainer Feature hook registries;
- full semantic BattleSpec -> BattleTranscript parity;
- tactical AI scoring/policy;
- Craftics/Cobblemon adapter.

README:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

## Python AutoPTU live evidence

Current inspected Python main head:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Latest visible main work remains Career-focused (`Career: make roster recovery deterministic`).

The Java parity slices use pinned Python oracle revisions for their exact fixtures. That does not change the broader rule that a representative ported mechanic cannot stand in for an entire capability family.

Available project-file evidence includes a specific Python implementation path for Minior / Shields Down. That is species/Ability evidence only; it does not create an astronomy subsystem and does not prove Java parity for Minior.

## Permanent capability map

| Permanent capability family | Pass 63 state | Evidence interpretation |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Dedicated geometry, targeting, footprint, anchor and LoS coverage exists. |
| base movement legality | VERIFIED | Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers and fit predicates exist. |
| complete movement incl. push/pull/knockback/interception/forced movement | BLOCKING | Forced movement/interception and broad movement reactions remain unfinished. |
| core calculations | VERIFIED | PTU tables, combat stages, accuracy primitives, crit probability and selected modifiers exist. |
| action economy / initiative | VERIFIED | Typed turn flow, deterministic ordering, round rebuilds and multiple parity-tested initiative slices are evidenced. |
| full turn / round lifecycle | PARTIAL | Timing infrastructure is substantial, but complete status/Ability/Feature/reaction/delayed-effect coverage is not proven. |
| full stateful damage pipeline | PARTIAL | Multiple damage/post-damage slices exist while the README still lists full damage as unfinished. |
| status lifecycle | PARTIAL | Multiple status contracts/timing slices exist; complete controller coverage does not. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Initiative-time consumers of weather/terrain do not prove runtime battlefield terrain/weather/hazards/zones/reactions. |
| move-specific behavior | PARTIAL | Selected Move contracts exist; complete PTU Move behavior does not. |
| abilities | PARTIAL | Multiple Ability hooks and new initiative-time Ability slices exist; full registry remains incomplete. |
| items | PARTIAL | Selected item behavior exists; complete catalog behavior remains incomplete. |
| Trainer Features / perks | PARTIAL | Ordered/lifecycle infrastructure plus selected Features and initiative contributions exist; complete catalog remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal-action generation/filtering exists. |
| AI tactical policy | BLOCKING | Goal-aware scoring/policy remains future work. |
| Minecraft / Cobblemon / Craftics adapter & playback | BLOCKING | Java remains a rules core and does not yet own Minecraft projection/playback. |

## Pass 63-specific overworld blockers

Astronomy is primarily world-state and observation infrastructure.

`OVERWORLD_CELESTIAL_EVENT_CALENDAR = BLOCKING`

The server needs persistent authored/derived celestial events connected to the single world calendar, with event IDs, prediction windows and historical editions.

`OVERWORLD_SKY_VISIBILITY_MODEL = BLOCKING`

Local observing conditions need a server-owned model linking weather, haze/smoke, artificial light, lunar brightness, horizon state and observation quality without turning those labels into PTU bonuses.

`OVERWORLD_OBSERVATORY_INSTRUMENT_STATE = BLOCKING`

Telescope/camera/instrument condition, calibration, coverage and downtime need persistent records independent from celestial-event truth.

`OVERWORLD_FALL_SITE_AND_FRAGMENT_PROVENANCE = BLOCKING`

Candidate fall areas and recovered fragments need recovery location/time, material instance identity, custody and analysis history.

`OVERWORLD_CELESTIAL_POKEMON_OBSERVATION = BLOCKING`

The server needs observations that can associate individual/species behavior with sky events while keeping correlation separate from causal claims and avoiding automatic spawn manipulation.

`OVERWORLD_CELESTIAL_TO_BATTLE_PROJECTION = BLOCKING`

A revisioned adapter contract is needed before sky/world state can initialize any battlefield Weather, Gravity, visibility or other PTU effect. Only mechanics actually supported by Java may cross this boundary.

`OVERWORLD_SKY_TO_MINECRAFT_PLAYBACK = BLOCKING`

The server needs safe presentation hooks for observatory state and celestial visuals. Client/Minecraft visuals cannot become authoritative event or battle state.

## Encounter dependency review

### Observatory Ridge Disturbance

Full version requires:

- targeting / footprints / range / LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING if wild Pokémon withdraw through route lanes;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for darkness/weather/ridge effects as mechanics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal/avoid-observatory goals;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- observatory/sky-state writeback — BLOCKING outside battle core.

Reduced version:

Keep instruments, public visitors, access state and sensitive habitat in overworld state. Freeze one static ridge arena if battle starts. Do not convert visibility or celestial state into tactical modifiers.

### Fresh Fall Recovery

Full version may require moving search actors, protected zones, environmental hazards, interactable fragments and objective-aware AI.

Key permanent blockers:

- complete movement/interception/forced movement — BLOCKING if actors flee or compete over locations;
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic environmental pressure;
- AI tactical policy — BLOCKING for protect/recover/withdraw goals;
- Minecraft playback — BLOCKING.

Reduced version:

Resolve search pattern, recovery timestamps, fragment provenance and custody outside battle. Start a conventional static encounter only if an actual confrontation occurs. A battle result never assigns fragment ownership automatically.

### Dark-Sky Access Dispute

This concept should normally remain a social/governance/tourism scenario.

A future full tactical version with protected corridors or reach/withdraw objectives would depend on:

- complete movement/interception/forced movement — BLOCKING;
- broad zones/reactions — BLOCKING;
- tactical AI — BLOCKING;
- Minecraft playback — BLOCKING.

Reduced version:

Resolve access policy, crowd movement and negotiation in world state. Use battle only if the story produces a separate legal confrontation.

## PTU / Caelo caution

Pass 63 creates no astronomy mechanic.

Do not infer or invent:

- lunar stat modifiers;
- Moon-phase accuracy/damage changes;
- Gravity changes;
- meteor impact damage;
- falling-object attacks;
- magnetic fields or zones;
- cosmic radiation;
- telescope bonuses;
- star-navigation bonuses;
- Minior shower encounter rates;
- Clefairy full-moon spawn rates;
- Moon Stone creation;
- special capture modifiers;
- Jirachi wish mechanics;
- Deoxys arrival mechanics;
- Weather generation from celestial events.

The project-supplied full Caelo corpus was not reliably retrievable during this run. No new exact Caelo celestial, lunar, Gravity, Weather or observation rule is asserted.

## Snapshot conclusion

Pass 63 does not justify a permanent capability promotion.

Java head `44f7d67afe7573593e996ebc39c99cd188c88f1d` strengthens the already-VERIFIED initiative family and adds bounded Ability/Feature evidence. The weather/terrain initiative resolver in `a5d6221ab13a9f249656da2e0a55fe866791e156` consumes semantic weather/terrain inputs but does not implement the battlefield family, which remains BLOCKING.

Astronomy worldbuilding can advance safely as calendar, visibility, observation, institutional and provenance state. Any concept that turns a sky condition into a tactical PTU effect remains blocked until exact rules and Java contracts exist.