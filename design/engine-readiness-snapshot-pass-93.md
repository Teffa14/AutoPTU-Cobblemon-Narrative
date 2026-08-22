# Engine Readiness Snapshot — Pass 93

Status: Implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Evidence inspected

AutoPTU-Java live head inspected:
`1b4a38e871190844ae296a0fbb5966ea6f3da8bf`

Latest relevant Java change:
`Freeze delayed target-selection semantics (#127)`

Observed behavior in that slice:

- delayed combatant hits prefer the live defender position when that defender still resolves;
- affected tiles are recomputed at maturity;
- combatants are selected by footprint overlap;
- line of sight is rechecked;
- an explicit target id retains priority where appropriate;
- stored target position remains fallback when the defender is missing;
- parity assertions freeze the contract against the Python oracle.

Source:
https://github.com/Teffa14/AutoPTU-Java/commit/1b4a38e871190844ae296a0fbb5966ea6f3da8bf

Java README remains explicit that the port is incomplete. It still lists core battle-state expansion, full damage, status controller, terrain/hazards/forced movement/reactions, complete hook registries, full transcript parity, tactical AI and Minecraft/Cobblemon adapter work as unfinished.

Source:
https://github.com/Teffa14/AutoPTU-Java/blob/main/README.md

AutoPTU Python live head inspected:
`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its latest visible work remains Career-oriented and does not justify changing the tactical capability map.

## Permanent capability categories

### VERIFIED

#### targeting / footprints / range / LoS

Static geometry, range, footprints and geometric line of sight remain verified at the established project level.

Pass 93 non-inference:
A rock shelf, tidepool edge, exposed boulder or sea cave entrance is not automatically a supported blocker or cover object until projected into the battle snapshot using supported geometry.

The new delayed-hit target-selection contract strengthens evidence that live target geometry and LoS can be recomputed for that specific verified path. It does not establish dynamic tide geometry.

#### base movement legality

Basic movement legality remains verified at the established project level.

Pass 93 non-inference:
Base movement does not prove slipping, wave displacement, climbing wet rock, changing water depth, retreat from an incoming tide or movement through moving water.

#### core calculations

Established calculation primitives remain verified.

#### action economy / initiative

Established action economy and initiative remain verified.

#### AI legal-action infrastructure

Deterministic legal-choice generation remains verified.

This does not prove tactical understanding of tide windows, withdrawal routes, visitor protection or pool reconnection.

### PARTIAL

#### full turn / round lifecycle

Lifecycle ownership includes strong representative evidence for round progression, field progression, initiative rollover and delayed-hit maturity.

Still partial because representative slices do not prove every START/END trigger, duration, reaction, delayed Move, status, Ability, Feature and transcript interaction.

Pass 93 implication:
A tide changing every N rounds would depend on a world/environment contract that does not yet exist. Lifecycle alone cannot author that change.

#### full stateful damage pipeline

Delayed combatant hits can re-enter authoritative accuracy, target, damage, hook, HP and history paths for verified slices.

Still partial because full damage remains listed as unfinished.

#### status lifecycle

Representative status application, phase and cleanup behavior exists.

Still partial because the complete controller is unfinished.

Intertidal prose cannot create Slowed, Tripped, Poisoned, Burned or other statuses.

#### move-specific behavior

Delayed-hit behavior has increasingly strong representative contracts.

Still partial because the full Move library is not ported.

#### abilities

Representative Ability hooks exist with parity fixtures.

Still partial because the complete registry is not ported.

Species flavor such as Wimpod scattering or Binacle feeding does not prove a corresponding live Ability implementation.

#### items

Representative held-item behavior exists.

Still partial because coverage remains incomplete.

#### Trainer Features / perks

Representative Feature infrastructure and specific Features exist.

Still partial because the catalog and broad interrupt/reaction families remain incomplete.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

Still blocking.

Pass 93 implications:

- waves cannot push combatants through verified forced movement;
- an advancing tide cannot move actors;
- wildlife cannot rely on a verified tactical withdrawal corridor;
- civilians cannot be intercepted or escorted through complete movement rules;
- pool reconnection cannot displace actors through current/flow mechanics.

#### terrain / weather / hazards / zones / reactions

Still blocking as a complete family.

Canonical field-state progress exists, but it does not establish intertidal terrain or tide mechanics.

Pass 93 does not infer:

- wet rock = Rough or Slow Terrain;
- shallow pool = Water Terrain;
- rising tide = zone effect;
- breaking wave = knockback;
- barnacles = damage hazard;
- sea spray = Accuracy penalty;
- isolated pool = environmental damage;
- extreme low tide = capture bonus;
- extreme high tide = Weather.

#### AI tactical policy

Still blocking.

No current evidence proves reliable AI for:

- WITHDRAW;
- REACH_EXIT;
- PROTECT_POOL;
- AVOID_VISITORS;
- CROSS_BEFORE_TIDE;
- HOLD_SAFE_CORRIDOR;
- DISENGAGE_WITHOUT_KO;
- PROTECT_RESEARCHER.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still blocking.

No verified adapter contract currently turns:

- tide state;
- intertidal exposure revisions;
- tidepool isolation;
- temporary low-tide routes;
- visitor-pressure state;
- ecological occupancy history

into authoritative battle state and semantic playback without duplicating PTU rules.

## Pass 93 intertidal-specific blockers

`OVERWORLD_INTERTIDAL_SYSTEM_STATE`
Persistent intertidal segment identity and links to coast/maritime/ecology.

`OVERWORLD_TIDE_STATE_AUTHORITY`
Server-owned tide phase/level input independent of client moon graphics and loaded water blocks.

`OVERWORLD_INTERTIDAL_EXPOSURE_REVISIONS`
Versioned exposed/submerged footprint per tide context.

`OVERWORLD_TIDEPOOL_IDENTITY`
Persistent pool identity across repeated fill/isolation/reconnection cycles.

`OVERWORLD_POOL_ISOLATION_HISTORY`
Time-bounded pool connection state without inventing oxygen/salinity mechanics.

`OVERWORLD_INTERTIDAL_OBSERVATION_PROVENANCE`
Observation records that preserve tide, zone, time, method and source.

`OVERWORLD_LOW_TIDE_ACCESS_WINDOWS`
Temporary route eligibility handed off to Travel instead of inferred from visible blocks.

`OVERWORLD_VISITOR_PRESSURE_AND_DISTURBANCE`
Observed visitor use separated from demonstrated ecological effect.

`INTERTIDAL_TO_TRAVEL_HANDOFF`
Temporary shore routes become Travel connections only for their valid window.

`INTERTIDAL_TO_CONSERVATION_HANDOFF`
Stewardship/access measures preserve reason, scope and duration.

`INTERTIDAL_TO_COBBLEMON_PROJECTION`
Coarse tide-linked presence opportunities without loaded-entity truth or rare-spawn exploits.

`INTERTIDAL_TO_BATTLE_SNAPSHOT`
Freeze only supported geometry and mechanics at encounter start.

## Encounter readiness

### Low-Tide Shelf Survey

Reduced version: feasible as overworld tide/access resolution plus a static arena and normal battle if needed.

Full version blockers:

- complete movement if incoming water changes routes or displaces actors;
- full lifecycle only if a verified external tide event can enter combat state;
- terrain/weather/hazards/zones/reactions for dynamic exposure or wave zones;
- tactical AI for WITHDRAW/REACH_EXIT/PROTECT_POOL;
- adapter/playback;
- intertidal-to-battle snapshot.

### Pool Reconnection

Reduced version: feasible as an overworld investigation/interaction followed by an optional fixed adjacent-platform battle.

Full version blockers:

- interactable objective authority;
- complete movement for any flow/displacement behavior;
- dynamic environment/zone state;
- tactical AI for withdrawal/protection;
- adapter/playback.

Reconnection itself must not be simulated as a Minecraft-side PTU mechanic.

### Visitor Surge at Moonpool Point

Reduced version: feasible as visitor routing and stewardship outside battle plus a cleared static arena if confrontation occurs.

Full version blockers:

- crowd/civilian projection;
- complete movement/interception for protected corridors;
- tactical AI for wildlife withdrawal;
- environment mechanics only when exact effects are verified;
- adapter/playback.

## Current category summary

VERIFIED:
- targeting / footprints / range / LoS;
- base movement legality;
- core calculations;
- action economy / initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn / round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features / perks.

BLOCKING:
- complete movement including push / pull / knockback / interception / forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter and playback.

## Canon/mechanical questions left open

- What service owns tide calculation for Ouros, and how does it consume world calendar/astronomy?
- Which regions have rocky intertidal systems worth persistent modeling?
- Which species have authored intertidal behavior in each region?
- Does the PTU/Caelo corpus define any exact slippery-rock, wave, shallow-water, climbing or exposure rules that should be inherited?
- How should temporary low-tide connections appear in multiplayer maps without creating desync?
- How much of the shoreline physically changes in Minecraft each tide versus using authored access gates?
- Can Cobblemon expose spawn conditions without letting players force rare tide-linked spawns through block manipulation or relogging?
- Will AutoPTU ever support a tide-changing encounter, or should intertidal battles permanently use a frozen snapshot policy?

The full primary Caelo corpus was not recovered reliably during this run, so no Caelo-specific tide, shoreline or exposure rule is asserted here.