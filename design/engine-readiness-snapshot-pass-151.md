# Engine Readiness Snapshot — Pass 151

Status: ENGINE EVIDENCE SNAPSHOT. Read-only evidence and dependency classification only.

Date: 2026-08-30

## Live repositories inspected

### AutoPTU-Java — read only

Observed `main` head:

`c5b2a34ff23887770268bfe4108dfc86e9a796fb`

Commit:

`Compose Intercept position from server-owned Shift legality (#288)`

This is unchanged from Pass 150.

The current evidence confirms a concrete Intercept path where the server-owned runtime composes an Intercept destination from authoritative battle state and legal Shift destinations. It improves confidence that Minecraft/Cobblemon must not choose tactical Intercept positions.

It does not verify the broader complete-movement family.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

This remains presentation-only. The commit explicitly states that battle rules and outcomes do not change.

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

No permanent category changes during Pass 151.

## Why Pass 151 does not promote any category

The new narrative architecture concerns cover, access, exposure, operation objectives and extraction. Those are not proof that battle systems exist.

The current Intercept work remains representative evidence only. It does not establish:

- all Push sources;
- all Pull sources;
- all Knockback sources;
- every Intercept path;
- every collision and partial-stop case;
- escort movement;
- moving platforms;
- environmental forced movement;
- generalized reactions;
- reaction ordering;
- dynamic tactical zones;
- objective-aware AI;
- authoritative Minecraft/Cobblemon/Craftics battle playback.

## Narrative readiness

The covert-operation continuity layer itself is READY as world-state architecture.

The following operations can be modeled now without adding tactical mechanics:

- recording an operation identity;
- storing several independent objectives;
- recording preparation that actually occurred;
- storing observer-scoped cover claims;
- storing scoped access provenance;
- recording route knowledge and staleness;
- recording an exposure event;
- passing alert information through Communications;
- recording extraction plans and blockers;
- recording evidence and fallout through existing owners;
- keeping noncombatants outside BattleSpec;
- using an ordinary static battle as one bounded operation slice.

## Record Room Exit Corridor

Full-version intent:

The party has already completed an information objective and must leave while hostile actors pursue different goals such as delay, capture, protection or route denial.

Capability matrix:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | explicit spatial and targeting legality |
| base movement legality | VERIFIED | ordinary legal movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | contested withdrawal, blocking and displacement |
| core calculations | VERIFIED | ordinary PTU calculations |
| action economy/initiative | VERIFIED | sequencing |
| full turn/round lifecycle | PARTIAL | timed exit and encounter-end semantics |
| full stateful damage pipeline | PARTIAL | authoritative damage persistence |
| status lifecycle | PARTIAL | status consequences during withdrawal |
| terrain/weather/hazards/zones/reactions | BLOCKING | dynamic doors, route zones or generalized reactions if used |
| move-specific behavior | PARTIAL | exact move semantics |
| abilities | PARTIAL | exact ability semantics |
| items | PARTIAL | exact battle-item semantics |
| Trainer Features/perks | PARTIAL | exact feature/interrupt semantics |
| AI legal-action infrastructure | VERIFIED | legal candidate actions |
| AI tactical policy | BLOCKING | objective-aware delay, blocking and withdrawal behavior |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative tactical presentation/handoff |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- Ouros determines operation/exposure state before battle;
- explicit combatants are fixed before initiative;
- records, staff and semantic evidence stay outside BattleSpec;
- geometry is static;
- no dynamic alarm reinforcement or extraction AI is simulated;
- AutoPTU may return `IMMEDIATE_EXIT_ROUTE_CLEAR` as a reviewed narrow fact;
- extraction is resolved afterward by Travel and operation state.

## Loading Bay Observation Window

Full-version intent:

The party needs to preserve an observation window while a working loading area, moving cargo and several actor groups create changing lines and objectives.

Relevant capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including forced movement/interception — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic work zones, doors or reactions
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for multiple simultaneous objectives
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version: BLOCKED.

Reduced version: READY.

The loading operation pauses before BattleSpec. Cargo and workers are removed from tactical state. AutoPTU resolves explicit combatants in fixed geometry. A result such as `OBSERVATION_WINDOW_CREATED` may be returned. Observation/world-state systems then determine what is actually observable.

## Compromised Cover Perimeter

Full-version intent:

Some actors suspect the player's cover while other observers do not. The party wants to leave without turning every observer into a combat participant.

This encounter is especially sensitive to authority boundaries.

Observer-relative suspicion is narrative state. It is not AI battle knowledge and it must not be flattened into `all hostiles aggro` by Minecraft or Cobblemon.

Relevant capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — PARTIAL if used
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if reaction/zone logic is used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for suspicion-aware objectives and selective withdrawal
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full version: BLOCKED.

Reduced version: READY.

Ouros decides before BattleSpec exactly which actors become combatants. Noncombatant observers remain outside tactical state. AutoPTU resolves those explicit participants only. Communications and exposure state determine later information spread.

## Mobile Site Boarding Chokepoint

Full-version intent:

A mobile laboratory, convoy, ship, train or other moving site creates a narrow boarding/exit conflict while the platform itself may move.

Relevant capability families:

- targeting/footprints/range/LoS — VERIFIED for static geometry only
- base movement legality — VERIFIED for current ordinary movement legality
- complete movement including forced movement/interception — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if platform/environment states change
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for boarding/withdrawal priorities
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for moving-platform authoritative playback

Full version: BLOCKED.

Reduced version: READY.

The mobile site is stationary for the tactical slice. World state determines its presence and access before battle. AutoPTU may clear an immediate approach or exit. Vehicle/Travel systems determine subsequent movement.

## Operation concepts that require no battle

The following are READY when their owning world-state evidence exists:

- observing a meeting from a valid location;
- entering a public floor;
- receiving a legitimate introduction;
- discovering that an old credential was revoked;
- learning that a facility belongs to another organizational branch;
- comparing route knowledge against renovation state;
- recording that an alias was recognized by one observer;
- receiving a delayed alert through Communications;
- abandoning object removal to preserve provenance;
- finding an already evacuated headquarters;
- completing a quiet operation with no combat.

These should not acquire artificial battles merely because AutoPTU exists.

## PTU / Caelo assumptions kept UNKNOWN

Pass 151 does not invent:

- universal Stealth checks;
- universal infiltration checks;
- universal disguise rules;
- universal suspicion meters;
- universal alarm mechanics;
- universal silent takedowns;
- generic hacking;
- generic electronic security;
- generic lockpicking;
- generic credential forgery;
- generic impersonation authority;
- generic patrol AI;
- generic escort/extraction mechanics;
- generic reinforcement timing;
- generic non-KO capture of hostile Trainers;
- generic witness-memory mechanics;
- generic faction Heat;
- automatic criminal status;
- automatic law-enforcement authority;
- automatic faction reputation consequences;
- automatic Pokémon utility powers from species flavor;
- cross-BattleSpec HP/status/initiative persistence.

An exact PTU/Caelo rule can be used only after source and implementation validation.

## Minecraft/Cobblemon/Craftics boundary

The adapter may present already-decided state:

- doors that world state says are open or closed;
- badges or uniforms attached to item/actor state;
- public and restricted areas;
- a fixed set of NPCs currently present;
- alert lights or sounds after an alert event exists;
- changed facility appearance after fallout;
- an NPC recognizing an alias when Ouros actor knowledge supports it;
- a post-battle exit animation after world state confirms extraction.

It must not decide:

- that cover succeeded or failed;
- that an NPC believed a claim;
- that a credential grants authority;
- that every NPC learned an alert;
- which entities are AutoPTU combatants;
- tactical HP/status/position;
- Intercept destination;
- whether a Pokémon bypassed an obstacle;
- whether an objective was acquired;
- whether evidence proves identity or motive;
- whether extraction succeeded;
- whether an organization was exposed or defeated.

Cobblemon BattleState remains outside Ouros tactical authority.

## Readiness conclusion

Pass 151 changes no permanent capability status.

Covert-operation continuity is READY as world-state orchestration. Rich tactical infiltration/extraction scenes remain blocked where they depend on complete movement, lifecycle, generalized reactions/zones, objective-aware AI or authoritative adapter playback.

Reduced versions remain READY by fixing world-state conditions before BattleSpec, excluding semantic noncombatants and evidence from tactical state, using static geometry and allowing AutoPTU to return only narrow immediate spatial facts.