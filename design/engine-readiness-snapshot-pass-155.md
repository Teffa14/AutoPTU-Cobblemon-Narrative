# Engine Readiness Snapshot — Pass 155

Status: LIVE EVIDENCE SNAPSHOT
Narrative head before pass: `edf6ffd83cb48ae41089f83d5808dd62f216fdcb`
Date: 2026-08-30

## Read-only engine heads inspected

AutoPTU-Java:

`ba5d97576b4fe469b2e4064737b1520e8b67a384` — `Resolve Intercept attack line from authoritative battle state (#290)`

AutoPTU:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`

No files in either engine repository were modified by Pass 155.

## Live Java evidence added since Pass 154

The current Java head advances the server-owned Intercept geometry boundary one step further.

The commit:

- introduces `GridLineResolution` as a canonical integer grid-line primitive that delegates to the same Bresenham cells already used for targeting line of sight;
- freezes grid-line endpoint and tie-breaking behavior against the pinned Python `BattleState._line_cells` oracle;
- derives the Intercept attack line from authoritative battle-state positions instead of accepting an externally planned attack-line input;
- migrates spatial-sequence and PRE-target Intercept tests to server-owned attack-line geometry;
- expands the parity workflow so the grid line, Intercept geometry, Shift destination resolution and affected Intercept boundaries are tested together.

This is meaningful evidence for server-owned targeting/line geometry and a bounded Intercept sequence.

It remains localized evidence. It does not prove the complete movement family or generalized reaction semantics.

## Conservative interpretation

Do not extrapolate the latest Intercept evidence to:

- every Push source;
- Pull;
- general Knockback;
- every Intercept form, eligibility interaction or ordering interaction;
- arbitrary forced movement;
- environmental displacement;
- escort/rescue movement;
- object carrying or contested cargo transfer;
- moving platforms or vehicles;
- generalized reaction windows or ordering;
- dynamic hazards or zones;
- semantic objective ownership;
- tactical flee, protect, seize, delay or capture policy.

The AutoPTU head remains presentation-only evidence. Its latest commit states that battle rules and outcomes do not change.

## Permanent capability map

### VERIFIED

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted by Pass 155.

## Pass 155 encounter matrix

### Warehouse Handoff Perimeter — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when doors, loading lanes or reaction windows are tactical
- move-specific behavior — PARTIAL, individual audit required
- abilities — PARTIAL, individual audit required
- items — PARTIAL, individual audit required
- Trainer Features/perks — PARTIAL, individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Overall: BLOCKED for the intended rich form.

Reduced form: READY at narrative-contract level if only individually audited battle content is used.

Reduced constraints:

- cargo and records remain outside BattleSpec;
- custody is frozen before initiative;
- noncombatants remain outside BattleSpec;
- explicit combatant roster;
- static geometry;
- no carry, steal, escort, semantic protect or dynamic door objective;
- permitted result: `IMMEDIATE_WAREHOUSE_HANDOFF_APPROACH_CLEAR` only.

Ouros decides whether custody changes or the handoff occurs after the battle.

### Transit Yard Withdrawal Corridor — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected combat content requires
- status lifecycle — PARTIAL as selected combat content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if active lanes, vehicle hazards or reaction windows matter
- move-specific behavior — PARTIAL, individual audit required
- abilities — PARTIAL, individual audit required
- items — PARTIAL, individual audit required
- Trainer Features/perks — PARTIAL, individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for withdrawal/delay decisions
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for moving vehicles/platforms and authoritative tactical playback

Overall: BLOCKED for intended moving-yard form.

Reduced form: READY.

Reduced constraints:

- vehicles are stationary during the tactical slice;
- cargo and uninvolved workers remain outside BattleSpec;
- static yard geometry;
- explicit combatants only;
- no moving-platform semantics;
- permitted result: `IMMEDIATE_TRANSIT_YARD_EXIT_ROUTE_CLEAR`.

A clear exit route does not itself establish that a particular carrier escaped.

### Holding-Site Recovery Perimeter — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL, with escort/rescue semantics still unverified
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if holding areas, hazard zones or reaction windows are tactical
- move-specific behavior — PARTIAL, individual audit required
- abilities — PARTIAL, individual audit required
- items — PARTIAL, individual audit required
- Trainer Features/perks — PARTIAL, individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for delay, protect, flee, capture or rescue-aware choices
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Overall: BLOCKED for true tactical rescue/protection play.

Reduced form: CONDITIONAL READY.

Use the reduced form only when Ouros can establish, from already verified world facts, that living subjects are moved to a safe non-tactical state before initiative. If the rescue itself requires contested tactical simulation, the encounter remains blocked.

Permitted result after safe extraction: `IMMEDIATE_HOLDING_SITE_PERIMETER_CLEAR`.

Hard safeguards:

`BATTLE_WON != POKEMON_OWNERSHIP_TRANSFERRED`

`TACTICAL_FAILURE_WITHOUT_RESCUE_CONTRACT != HARM_CONFIRMED`

### Market Exit Chokepoint — full version

Required families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL as selected content requires
- status lifecycle — PARTIAL as selected content requires
- terrain/weather/hazards/zones/reactions — BLOCKING if crowd lanes, doors or reaction windows matter
- move-specific behavior — PARTIAL, individual audit required
- abilities — PARTIAL, individual audit required
- items — PARTIAL, individual audit required
- Trainer Features/perks — PARTIAL, individual audit required
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for flee/delay/carry decisions
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Object carrying is an additional unverified semantic dependency if goods must move with combatants.

Overall: BLOCKED for intended rich form.

Reduced form: READY.

Reduced constraints:

- sellers, buyers, bystanders and goods that are not explicit combatants remain outside BattleSpec;
- static geometry;
- explicit combatant roster;
- no semantic carrying or market-custody objective;
- permitted result: `IMMEDIATE_MARKET_EXIT_APPROACH_CLEAR`.

The tactical outcome cannot establish ownership, sale completion, knowledge of origin, guilt or wider network closure.

## Clandestine-trade authority boundary

Pass 155 gives Narrative continuity authority over proposed or canon-backed records such as:

- source and destination claims;
- observed chain nodes;
- handoffs linked to existing custody events;
- provenance-obscuring events;
- actor-relative knowledge slices;
- market offers;
- interdiction events;
- network disruption and reconfiguration events;
- unresolved provenance gaps;
- route hypotheses that remain explicitly hypotheses until supported.

It does not give Narrative authority to manufacture:

- criminal law;
- contraband classes;
- customs rules;
- protected-species lists;
- search/seizure mandates;
- arrest powers;
- guilt;
- organization membership;
- ownership;
- forged-document outcomes;
- black-market prices;
- automatic Pokémon placement after recovery.

AutoPTU remains authoritative only for tactical facts covered by BattleSpec and verified mechanics.

Minecraft/Cobblemon/Craftics remains presentation/playback only. It cannot decide illicit status, concealed content, search success, guilt, route knowledge, combatant roster, PTU HP/status, custody transfer or network closure.

## PTU/Caelo unresolved mechanics and setting assumptions

Keep UNKNOWN until project-approved source evidence and current implementation contracts verify them:

- universal contraband or prohibited-item categories;
- regional criminal-law definitions;
- universal customs or border-control regime;
- generic search, seizure, arrest or detention procedure;
- universal concealment or smuggling checks;
- bribery mechanics;
- fencing mechanics;
- black-market price modifiers;
- generic document forgery mechanics;
- automatic detection of forged or false records;
- poaching mechanics;
- universal wildlife-trade permits;
- capture-legality rules beyond exact PTU/Caelo and authored setting authority;
- generic cargo-search Skill checks;
- any Move, Ability, Skill or Trainer Feature that reveals provenance, ownership, guilt or hidden contents without an exact rule;
- automatic guilt or faction reputation from possession;
- automatic organization membership from participation in a handoff;
- automatic ownership transfer when a Pokémon is recovered;
- escort/rescue objective mechanics;
- object-carrying and contested cargo-transfer mechanics;
- tactical withdrawal policy;
- moving-vehicle tactical geometry.

## Canon questions opened by Pass 155

Future canon review must decide, separately and explicitly:

- which Ouros regions or institutions regulate which materials, Pokémon, specimens or activities;
- whether any wildlife capture or trade restrictions exist beyond ordinary PTU capture authority;
- which institutions, if any, may inspect, hold, recover or seize disputed subjects;
- what evidence is required for ownership or custody claims;
- what happens to a recovered Pokémon while claims are unresolved;
- whether specific ports, warehouses, markets or routes have established clandestine histories;
- whether any faction derives revenue from clandestine trade;
- whether black-market venues are stable places, temporary social networks or both;
- what kinds of provenance records ordinary merchants expect;
- what penalties or adjudication processes exist, if any;
- which recurring NPCs or organizations belong in the first canon-approved chain.

Until those decisions are approved, Pass 155 remains a systems grammar and NON-CANON seed library rather than established regional history.