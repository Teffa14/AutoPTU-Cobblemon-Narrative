# Engine Readiness Snapshot — Pass 152

Status: ENGINE EVIDENCE SNAPSHOT. Read-only evidence and dependency classification only.

Date: 2026-08-30

## Live repositories inspected

### AutoPTU-Java — read only

Observed `main` head during Pass 152:

`c5b2a34ff23887770268bfe4108dfc86e9a796fb`

Commit:

`Compose Intercept position from server-owned Shift legality (#288)`

Recent evidence leading to this head includes server-owned Shift-destination resolution and server-owned Intercept-position composition. This is concrete evidence for a particular Intercept path using authoritative battle state and legal Shift destinations.

It does not verify the whole complete-movement family.

### AutoPTU — read only

Observed `main` head:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Commit:

`Career: keep battle coordinates synced after viewport resize (#237)`

The commit explicitly describes the change as presentation-only and states that battle rules and outcomes do not change.

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

No permanent capability category is promoted during Pass 152.

## Why no category changes

Pass 152 adds narrative reasoning architecture. It provides no evidence that tactical mechanics exist.

The current AutoPTU-Java Intercept work remains localized evidence. It does not establish:

- every Push source;
- every Pull source;
- every Knockback source;
- all collision and partial-stop interactions;
- every Intercept path;
- escort movement;
- object carrying;
- moving platforms;
- environmental forced movement;
- generalized reactions;
- reaction ordering;
- dynamic tactical zones;
- weather lifecycle;
- hazard lifecycle;
- objective-aware tactical AI;
- authoritative Minecraft/Cobblemon/Craftics playback.

## Narrative readiness

The Investigation Inference & Hypothesis Revision layer is READY as world-state architecture.

The following can be represented now without new battle mechanics:

- investigation questions;
- several simultaneous hypotheses;
- explicit assumptions;
- support and conflict inference edges;
- lead state and staleness;
- theory revision history;
- recontextualization of old evidence without deletion;
- narrow resolutions;
- accepted ambiguity;
- source-independence tracking through existing provenance;
- player-facing caseboards that expose only discovered material;
- battle results entering the investigation as narrow tactical facts rather than truth flags.

## Permanent investigation-to-battle boundary

AutoPTU may authoritatively resolve the tactical consequences inside its BattleSpec contract.

It must never directly author:

- `HYPOTHESIS_CONFIRMED`
- `WITNESS_TRUTHFUL`
- `CULPRIT_IDENTIFIED`
- `MOTIVE_PROVEN`
- `EVIDENCE_AUTHENTIC`
- `SCIENTIFIC_CAUSE_CONFIRMED`
- `ARCHAEOLOGICAL_INTERPRETATION_CONFIRMED`
- `INSTITUTIONAL_FINDING_ISSUED`
- `CASE_SOLVED`

Ouros can consume a battle fact and later use it as one input to an inference record.

## Evidence Room Withdrawal Corridor

Full-version intent:

Investigators have already documented evidence in a controlled room. Hostile combatants threaten immediate access or safe withdrawal. The tactical scene may involve contested routes and a protected semantic area.

Capability matrix:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | explicit targeting and spatial legality |
| base movement legality | VERIFIED | ordinary movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | blocking, displacement and contested withdrawal |
| core calculations | VERIFIED | ordinary PTU calculations |
| action economy/initiative | VERIFIED | sequencing |
| full turn/round lifecycle | PARTIAL | timed withdrawal/end semantics |
| full stateful damage pipeline | PARTIAL | authoritative combat damage state |
| status lifecycle | PARTIAL | status persistence and clearing |
| terrain/weather/hazards/zones/reactions | BLOCKING | protected/dynamic zone and reaction semantics if used |
| move-specific behavior | PARTIAL | exact selected move behavior |
| abilities | PARTIAL | exact selected ability behavior |
| items | PARTIAL | exact selected item behavior |
| Trainer Features/perks | PARTIAL | exact selected feature/interrupt behavior |
| AI legal-action infrastructure | VERIFIED | legal candidates |
| AI tactical policy | BLOCKING | evidence-aware denial, blocking and withdrawal choices |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative tactical projection |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- evidence and records remain outside BattleSpec;
- evidence custody is frozen before initiative;
- noncombatants are removed from tactical state;
- geometry is static;
- explicit combatants are fixed by Ouros;
- no evidence-aware AI objective is required;
- AutoPTU may return `IMMEDIATE_EVIDENCE_ROOM_EXIT_ROUTE_CLEAR` as a narrow reviewed fact;
- authenticity, custody, hypothesis state and later extraction remain world-state concerns.

## Witness Separation Perimeter

Full-version intent:

A witness or informant is present while several groups have distinct objectives such as protection, delay, capture, intimidation or withdrawal.

Capability matrix:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | combat spatial legality |
| base movement legality | VERIFIED | ordinary movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | escort-like movement, blocking and interception |
| core calculations | VERIFIED | ordinary calculations |
| action economy/initiative | VERIFIED | ordering |
| full turn/round lifecycle | PARTIAL | timed separation/withdrawal semantics |
| full stateful damage pipeline | PARTIAL | persistent battle damage |
| status lifecycle | PARTIAL | exact status timing |
| terrain/weather/hazards/zones/reactions | BLOCKING | reaction windows or dynamic perimeter if used |
| move-specific behavior | PARTIAL | selected move semantics |
| abilities | PARTIAL | selected ability semantics |
| items | PARTIAL | selected item semantics |
| Trainer Features/perks | PARTIAL | exact features and interrupts |
| AI legal-action infrastructure | VERIFIED | legal actions |
| AI tactical policy | BLOCKING | multi-objective protection/capture/withdrawal behavior |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | authoritative presentation/handoff |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- the witness is not a BattleSpec participant unless independently selected as a valid combatant;
- Ouros moves the witness to a defined safe/non-tactical state before initiative when the reduced scene requires it;
- the battle resolves explicit combatants in static geometry;
- AutoPTU may establish an immediate perimeter or approach result only;
- testimony content, credibility and hypothesis effects are handled after the battle through their owning systems.

## Reconstruction Site Chokepoint

Full-version intent:

Investigators reconstruct an earlier event while machinery, hazards, environmental state or access conditions change during a confrontation.

Capability matrix:

| Capability family | Status | Full-version use |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | static spatial checks; dynamic changes would need explicit support |
| base movement legality | VERIFIED | ordinary movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | displacement around the site |
| core calculations | VERIFIED | ordinary calculations |
| action economy/initiative | VERIFIED | sequencing |
| full turn/round lifecycle | PARTIAL | timed reconstruction/interruption state |
| full stateful damage pipeline | PARTIAL | combat state |
| status lifecycle | PARTIAL | exact status timing |
| terrain/weather/hazards/zones/reactions | BLOCKING | changing machinery, hazard areas, weather or reaction windows |
| move-specific behavior | PARTIAL | exact moves |
| abilities | PARTIAL | exact abilities |
| items | PARTIAL | exact items |
| Trainer Features/perks | PARTIAL | exact feature behavior |
| AI legal-action infrastructure | VERIFIED | legal candidates |
| AI tactical policy | BLOCKING | objective-aware disruption or protection |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | dynamic authoritative presentation |

Full version: BLOCKED.

Reduced version: READY.

Reduction contract:

- reconstruction pauses before BattleSpec;
- all observations, assumptions and site records are frozen;
- machinery/environmental state used by the battle is static;
- noncombatant analysts and equipment remain outside tactical authority;
- after combat, Ouros decides whether site conditions changed enough to require a new observation or reconstruction episode;
- battle victory never validates reconstruction correctness.

## False Lead Ambush

Intended current form:

An adversarial actor has learned which lead investigators are following and prepares a conventional ambush at the expected destination.

The narrative setup can be resolved entirely by World Agency, Communications, Rumor/Testimony or Covert Operation state before BattleSpec.

Capability matrix:

| Capability family | Status | Use in current reduced/static form |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED | normal combat |
| base movement legality | VERIFIED | normal movement |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | avoid requiring unsupported rich displacement behaviors |
| core calculations | VERIFIED | normal PTU calculations |
| action economy/initiative | VERIFIED | normal sequencing |
| full turn/round lifecycle | PARTIAL | stay within verified encounter contract limits |
| full stateful damage pipeline | PARTIAL | exact persistence remains capability-scoped |
| status lifecycle | PARTIAL | use only covered statuses |
| terrain/weather/hazards/zones/reactions | BLOCKING | omit dynamic terrain/weather/hazard/reaction gimmicks |
| move-specific behavior | PARTIAL | roster must use reviewed moves |
| abilities | PARTIAL | roster must use reviewed abilities |
| items | PARTIAL | roster must use reviewed items |
| Trainer Features/perks | PARTIAL | roster must use reviewed features |
| AI legal-action infrastructure | VERIFIED | legal action generation |
| AI tactical policy | BLOCKING | do not require sophisticated ambush policy after initiative |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING | full authoritative playback remains blocking |

Narrative reduced form: READY as an AutoPTU battle contract once selected combatants use individually reviewed mechanics and the adapter boundary is satisfied by the available execution path.

Important interpretation boundary:

The ambush does not determine whether the followed lead was true, false, stale or planted. That question remains in investigation provenance.

## PTU/Caelo UNKNOWN assumptions retained

The following remain UNKNOWN unless direct source evidence verifies them:

- universal investigation subsystem;
- generic clue threshold;
- universal deduction roll;
- automatic lie detection;
- generic forensic analysis procedure;
- universal evidence-authentication Skill Check;
- universal reconstruction mechanic;
- automatic motive detection;
- a Skill Check that reveals canonical causation;
- a Pokémon species entry granting unrestricted forensic authority;
- automatic witness credibility from Perception, Intuition, Guile, General Education, Technology Education or another Skill;
- automatic Trainer Feature authority over evidence or conclusions;
- automatic source-independence scoring;
- a universal caseboard exposed by PTU rules.

## Minecraft/Cobblemon/Craftics boundary

Minecraft/Cobblemon/Craftics may render discovered evidence, records, known witnesses, caseboard links, locations, objects, environmental traces and already-decided aftermath.

It does not decide:

- what is evidence;
- whether evidence is authentic;
- which hypothesis is correct;
- whether a witness lied;
- which actors become combatants;
- tactical legality;
- HP/status/positions;
- battle outcome;
- whether a case or mystery is solved.

Cobblemon/Minecraft BattleState remains non-authoritative for Ouros combat facts.

## Pass 152 conclusion

Pass 152 advances investigation continuity without requiring new tactical mechanics. Rich protection, escort-like withdrawal, dynamic reconstruction and reaction-heavy scenes remain gated by their exact capability families. Reduced variants preserve the same narrative premises using static geometry, explicit combatants and narrow battle outputs.