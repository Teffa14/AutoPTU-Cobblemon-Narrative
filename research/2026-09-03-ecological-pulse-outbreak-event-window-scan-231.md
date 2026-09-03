# Ecological Pulse / Outbreak Event Window Scan — Pass 231

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-03

## Question

How can Ouros create temporary, visible ecological events that make the world feel alive without treating random spawn bursts as population truth or forcing every event into tactical combat?

This pass focuses on short-lived ecological pulses: temporary concentration, displacement, migration, weather-linked activity, disturbance response and route pressure.

## Existing Ouros constraints checked first

The active project focus remains Pokémon ecology and species behaviour under `CURRENT_FOCUS.md` and `design/ecology-development-program.md`.

The source policy in `design/ouros-source-authority-and-species-policy.md` remains binding:

- official Pokémon material can provide behaviour/distribution patterns;
- PTU is the mechanical baseline;
- Caelo/Kairos can inform living-world structures but do not silently become Ouros rules;
- Minecraft/Cobblemon can present visible world activity but cannot author PTU battle outcomes;
- generic spawning does not create persistent population truth.

This research therefore treats outbreak/event structures as design patterns, not literal rules imports.

## New public source scan

### Pokémon Legends: Arceus — Daybreak

Official source: https://legends.arceus.pokemon.com/en-au/update/

The Daybreak update explicitly frames massive mass outbreaks as a regional phenomenon to investigate. Multiple outbreak sites can appear across Hisui and the event is associated with rainstorms. The player does not receive every answer automatically; the activity is presented as a temporary field phenomenon requiring investigation.

Reusable structure:

```text
regional trigger
-> multiple local manifestations
-> limited observation window
-> field investigation
-> unusual species availability/concentration
-> event dissipates
```

Useful Ouros lesson: a temporary high-visibility event can be a regional ecological pulse rather than a permanent spawn-table change.

### Pokémon Sword / Shield — Wild Area

Official source: https://swordshield.pokemon.com/es-es/gameplay/wild-area/

The official Wild Area material states that species encountered depend on both local place and weather, and that weather varies spatially. This provides a strong official precedent for temporary environmental conditions changing visible species composition without changing the underlying geography.

Reusable structure:

```text
fixed habitat
+ temporary weather state
= changed visible activity / encounter composition
```

Useful Ouros lesson: weather-linked activity can modify exposure and local presence pressure while persistent population state remains separate.

### Pokémon Ranger: Guardian Signs / Tracks of Light

Official source: https://www.pokemon.com/it/videogiochi/pokemon-ranger-tracce-di-luce

The official Ranger material frames Rangers as protecting nature and helping people and Pokémon in difficulty. Missions use physical terrain and environmental obstacles, including strong currents, blocked passages and cooperative use of Pokémon capabilities.

Reusable structure:

```text
environmental condition
-> access or safety problem
-> field institution responds
-> Pokémon capability enables intervention
-> route/world state changes
```

Useful Ouros lesson: ecology-driven events do not need a villain or boss. A dangerous current, collapsed path, displaced population or stressed habitat can be the primary incident.

### Pokémon Mystery Dungeon: Rescue Team DX

Official source: https://mysterydungeon.pokemon.com/en-au/

The official game framing emphasizes dangerous changing environments, rescue missions and repeated expeditions into unstable dungeons. Pokémon.com strategy material for Rescue Team DX also treats terrain and weather as meaningful movement/strategy constraints rather than cosmetic scenery.

Supporting official strategy source: https://www.pokemon.com/it/approfondimenti/ecco-i-consigli-piu-efficaci-per-iniziare-la-tua-avventura-in-pokemon-mystery-dungeon-squadra-di-soccorso-dx

Reusable structure:

```text
environmental instability
-> temporary traversal constraint
-> rescue / observation objective
-> adaptation to terrain/weather
-> exit before conditions worsen
```

Useful Ouros lesson: ecological event pressure can create urgency through route viability and exposure rather than by increasing enemy HP.

## Combined pattern extracted for Ouros

The strongest reusable structure across the sources is:

```text
persistent ecological baseline
+ temporary driver
-> local activity/exposure change
-> visible manifestations across one or more sites
-> limited observation/intervention window
-> player/NPC response
-> event decays or transitions
-> persistent consequence recorded separately
```

Temporary drivers may include:

- weather pulse;
- seasonal movement;
- resource flush or collapse;
- breeding/nesting aggregation;
- disturbance displacement;
- predator pressure;
- route obstruction;
- fire/flood/storm aftermath;
- unusual but non-canonical anomaly event when separately approved.

## Authority rule

A pulse must not directly mutate population truth merely because more Pokémon entities are visible.

Required separation:

```text
persistent_population
activity_state
exposure_state
projection_multiplier
observation_state
```

Example:

```yaml
population_estimate: 84
activity_multiplier: 1.6
exposure_multiplier: 2.1
projection_multiplier: 1.8
```

A temporary visible concentration can therefore occur without inventing 100 new individuals.

## Event lifecycle candidate

```yaml
event_id: null
event_type: ecological_pulse
status: proposed
source_process: null
start_condition: null
active_window: null
decay_mode: null
affected_cells: []
affected_species: []
resource_pressure: []
weather_dependency: null
activity_delta: {}
exposure_delta: {}
projection_delta: {}
observation_channels: []
intervention_options: []
persistent_consequences: []
mechanical_handoff_policy: none_by_default
```

## Narrative uses

This structure supports:

- a dawn feeding aggregation that attracts observers and predators;
- a rain-linked movement pulse that temporarily makes normally hidden species visible;
- juveniles concentrating near a nursery zone, causing defensive adults to change route behaviour;
- drought pressure displacing wildlife toward farms and water infrastructure;
- a storm closing one migration corridor and concentrating multiple species along another;
- a resource bloom increasing prey activity and then predator presence;
- a temporary rescue corridor where the objective is guiding or protecting movement rather than defeating everything encountered.

## PTU / Caelo / Kairos cross-check

No new PTU rule is imported by this pass.

The concept remains compatible with the project PTU authority model because:

- off-screen activity/exposure changes are Ouros world-state calculations rather than hidden battles;
- direct skill checks, Trainer Features, movement capabilities, items or combat only become mechanical when the active rules profile explicitly calls for them;
- Caelo/Kairos may provide mission pacing or field-operation examples later, but those structures require provenance and do not activate campaign-specific rules automatically.

`SOURCE_HAS_RULE != OUROS_USES_RULE` remains unchanged.

## AutoPTU dependency audit

The core ecological pulse system requires no tactical category by itself.

World-state only version:

- targeting / footprints / range / LoS: not required;
- base movement legality: not required for off-screen state changes;
- complete movement: not required;
- core calculations: not required;
- action economy / initiative: not required;
- full turn/round lifecycle: not required;
- full stateful damage pipeline: not required;
- status lifecycle: not required;
- terrain/weather/hazards/zones/reactions: not required unless event becomes structured tactical mechanics;
- move-specific behavior: not required;
- abilities: not required;
- items: not required;
- Trainer Features/perks: not required;
- AI legal-action infrastructure: not required;
- AI tactical policy: not required;
- Minecraft/Cobblemon/Craftics adapter/playback: required for full visible projection, currently PARTIAL/BLOCKING end-to-end.

Rich direct encounter version can additionally depend on:

- targeting / footprints / range / LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement: PARTIAL;
- core calculations: VERIFIED;
- action economy / initiative: VERIFIED;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING outside verified slices;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING as complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

## Live engine evidence checked

AutoPTU-Java current head inspected during this pass:

`1d3ce8784cf5a327ef8dce44e6e73effd1956c3a` — `Add generic movement landing hook registry (#333)`.

This adds a bounded movement-landing hook registry and deterministic interaction with existing tile-trap contracts. It improves evidence around landing-trigger extensibility but does not complete forced movement, terrain/weather/hazard/reaction semantics, tactical AI or the full adapter.

AutoPTU current head remains:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

No capability family is promoted by this pass.

## Design recommendation

Ouros should model temporary ecological events as pulses over existing population/resource state rather than as ad-hoc spawn events.

The first implementation should support:

```text
baseline state
-> pulse driver
-> activity/exposure deltas
-> projected visible change
-> observations
-> player intervention
-> decay
-> persistent consequence
```

This can be implemented before rich tactical ecology is complete.

## Unresolved questions

- exact event duration representation: wall-clock, Minecraft time, ecology ticks or hybrid;
- whether multiple pulses can stack or must merge by driver family;
- how much a pulse can change native Cobblemon eligibility versus only weights/exposure;
- when weather is observation context versus authoritative tactical weather;
- how local institutions receive early warning without omniscient access;
- which pulse types can alter migration state versus merely local activity.
