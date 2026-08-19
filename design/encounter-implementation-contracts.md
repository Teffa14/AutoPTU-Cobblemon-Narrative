# Ouros Encounter Implementation Contracts

Status: proposed systems design. Not established canon.

## Purpose

Ouros already has mission grammar, dungeon state, challenge contracts, world-state systems and battle institutions. This document adds the missing implementation-facing layer beneath those systems.

A narrative concept may be approved as worldbuilding while its intended tactical implementation is still unavailable. The encounter contract records that gap explicitly instead of forcing one of two bad outcomes: deleting the concept or pretending an unfinished PTU mechanic already exists.

Every mechanically meaningful encounter should therefore describe:

- the narrative premise;
- the intended full tactical version;
- a reduced version when useful;
- the permanent engine capability families it requires;
- the current readiness of those families;
- the evidence needed before promotion from reduced to full;
- the authoritative mechanical sources that must be checked;
- the world-state outputs produced after authoritative resolution.

## 1. Permanent capability categories

Use these exact categories in encounter data:

1. targeting/footprints/range/LoS
2. base movement legality
3. complete movement including push/pull/knockback/interception/forced movement
4. core calculations
5. action economy/initiative
6. full turn/round lifecycle
7. full stateful damage pipeline
8. status lifecycle
9. terrain/weather/hazards/zones/reactions
10. move-specific behavior
11. abilities
12. items
13. Trainer Features/perks
14. AI legal-action infrastructure
15. AI tactical policy
16. Minecraft/Cobblemon/Craftics adapter/playback support

Do not create narrower substitute category names that hide one of these families.

## 2. Readiness states

```yaml
readiness_state:
  state: VERIFIED | PARTIAL | BLOCKING | UNKNOWN
  evidence_refs: []
  inspected_revision: null
  notes: null
```

Meaning:

VERIFIED: current tests/contracts establish the portion needed by this encounter family, not merely a representative helper.

PARTIAL: meaningful implementation and tests exist, but important general behavior required by the family remains unported or unverified.

BLOCKING: the required behavior is explicitly absent, deferred, or lacks an authoritative runtime path.

UNKNOWN: evidence has not been inspected recently enough to classify it.

A readiness result must be revision-aware. It is a snapshot, not permanent lore.

## 3. Three different questions

The authoring pipeline must not merge these questions:

1. Does PTU/Caelo define the mechanic?
2. Does AutoPTU/Python correctly implement or preserve that mechanic as the oracle?
3. Can AutoPTU-Java and the Minecraft/Cobblemon/Craftics layer execute and present it now?

A yes to question 1 or 2 does not answer question 3.

## 4. Encounter contract

```yaml
encounter_contract:
  encounter_id: null
  title: null
  status: proposed
  narrative_premise: null
  location_refs: []
  participant_refs: []
  world_state_inputs: []
  objective_profile: null
  full_version: null
  reduced_version: null
  capability_dependencies: []
  readiness_snapshot_ref: null
  ptu_caelo_source_refs: []
  python_oracle_refs: []
  java_evidence_refs: []
  adapter_evidence_refs: []
  authoritative_result_required: true
  world_state_writeback: []
  fail_forward_outputs: []
  promotion_gate: null
```

## 5. Capability dependency record

```yaml
capability_dependency:
  category: null
  required_for: full | reduced | both
  readiness: UNKNOWN
  exact_behavior_needed: null
  evidence_refs: []
  fallback_strategy: null
  blocking_if_absent: true
```

The `exact_behavior_needed` field matters because a category can be PARTIAL overall while the encounter depends on a slice that is already verified.

Example:

```yaml
category: status lifecycle
required_for: full
readiness: PARTIAL
exact_behavior_needed: "generic multi-status duration and save-check lifecycle across a multi-phase boss"
```

Burn support alone cannot satisfy that dependency.

## 6. Full and reduced versions

The full version expresses the intended final encounter once all required mechanics are validated.

The reduced version preserves the same narrative premise while removing only mechanics that are not ready.

A reduced version must not:
- fake the missing rule in Minecraft;
- replace a PTU mechanic with arbitrary scripted damage;
- grant a Pokémon an unsupported Move, Ability, Feature or capability;
- claim an objective was mechanically protected if it was actually outside the battle;
- award progression as though the full challenge was completed unless an approved policy says so.

A reduced version may:
- move a rescue target outside the tactical grid;
- represent dangerous weather visually while keeping the grid mechanically neutral;
- split a complex boss into multiple ordinary legal battles separated by world-state checkpoints;
- replace dynamic battlefield mutation with a reviewed static arena variant;
- make a tactical objective an overworld objective before or after a standard battle;
- choose a simpler approved opponent roster that preserves the story role.

## 7. Promotion gate

A reduced encounter may become full only when all blocking dependencies have current evidence.

```yaml
promotion_gate:
  required_states:
    - category: complete movement including push/pull/knockback/interception/forced movement
      minimum: VERIFIED
    - category: terrain/weather/hazards/zones/reactions
      minimum: VERIFIED
  required_tests: []
  required_adapter_events: []
  ptu_review_complete: false
  content_review_complete: false
```

Promotion requires the exact mechanic, not a similarly named representative mechanic.

## 8. Objective profiles

Narrative design may use these objective intents before they are mechanically executable:

- DEFEAT
- SURVIVE
- ESCAPE
- REACH_TILE
- HOLD_ZONE
- PROTECT
- PREVENT_ESCAPE
- BREAK_THROUGH
- DISABLE_OBJECT
- ACTIVATE_OBJECT
- CAPTURE
- WITHDRAW
- SURRENDER
- DELAY
- CLEAR_ROUTE

These names describe intent. They do not mean AutoPTU currently implements each objective.

Every non-DEFEAT profile requires a separate readiness review before it becomes authoritative battle logic.

## 9. Encounter archetype capability footprints

### Simple legal duel

Typical full dependencies:
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- full turn/round lifecycle
- full stateful damage pipeline
- move-specific behavior
- abilities
- AI legal-action infrastructure
- AI tactical policy for autonomous opponents
- adapter/playback for Minecraft execution

Current authoring note:
Even a "simple" production battle ultimately needs more than geometry and calculations if it is meant to execute end-to-end in Minecraft.

### Spatial duel

Adds:
- static terrain interpretation where required;
- LoS and footprint pressure;
- potentially complete movement if forced displacement matters.

### Escort / protect

Usually adds:
- objective-state support;
- AI policy aware of protected targets;
- reactions/interception if attacks can be body-blocked or redirected;
- adapter support for protected world entities.

Reduced form:
Keep protected actors outside the tactical grid and resolve a standard combat whose narrative consequence is whether the route becomes safe.

### Hazard arena

Adds:
- terrain/weather/hazards/zones/reactions;
- lifecycle timing;
- status/damage pipeline if hazards apply conditions or damage;
- adapter events capable of presenting the hazard state.

Reduced form:
Use the same visual location but make hazardous elements non-tactical until validated, or use a static legal blocker layout.

### Forced-movement arena

Adds:
- complete movement including forced movement/interception;
- collision/landing legality;
- reactions where applicable.

Reduced form:
Use ordinary movement around fixed geometry. Do not script knockback outside AutoPTU.

### Phase boss

Potentially adds:
- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific hooks;
- abilities;
- terrain/hazard transitions;
- semantic battle events;
- adapter playback.

Reduced form:
Use two or more separately approved ordinary encounters connected by a narrative checkpoint if that preserves the premise. Do not simulate an extra boss action by directly mutating HP.

### Reaction boss

Adds:
- terrain/weather/hazards/zones/reactions;
- ability/item/Feature hooks depending on source;
- precise lifecycle ordering.

Reduced form:
Remove reaction mechanics entirely and preserve the boss identity through legal roster, arena geometry and narrative behavior.

### Command/minion boss

Adds:
- AI policy for multiple allied units;
- possibly lifecycle/action-economy exceptions;
- move/ability hooks;
- target-selection logic.

Reduced form:
Run supporting groups as ordinary combatants under normal initiative, or resolve them in earlier separate battles.

### Item/object puzzle battle

Adds:
- item behavior if real battle items are involved;
- objective interaction with battlefield objects;
- adapter representation of interactables;
- potentially action-economy rules for object use.

Reduced form:
Resolve the object puzzle in the overworld, then enter a standard battle using the resulting world state.

### Feature-synergy encounter

Adds:
- Trainer Features/perks;
- their triggers and interrupts;
- lifecycle ordering;
- possibly reactions.

Reduced form:
Do not require the Feature interaction. Let legal Features work only when the engine already supports them authoritatively.

### Adaptive recurring rival

Adds:
- AI legal-action infrastructure;
- AI tactical policy;
- legal memory/scouting boundary;
- persistent public battle record.

Reduced form:
Use a curated, static approved policy/roster rather than claiming the rival learned tactically from prior fights.

## 10. Readiness snapshot from live Java evidence

Snapshot basis: AutoPTU-Java `main` inspected through commit `6570d95ac874bc26bc6bcc8ffe64d007bba37e34`, with representative parity slices from `046cc9f97ed8893e97674222f80789afcdf2cc7f` and `1757163fe793335e24a17769ee0fdfb78e87c754`.

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: BLOCKING
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: BLOCKING
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Why lifecycle remains PARTIAL:
The authoritative round controller now has an ordered lifecycle hook registry with seams for future status, terrain, delayed-hit, temporary-effect, ability and Trainer Feature work. The built-in registry currently proves a round-start move-frequency reset path, not the full population and ordering of those rule families.

Why abilities remain PARTIAL:
Canonical ability identity plus the parity-backed Mega Launcher/Errata effective-move hook proves the registry seam and one concrete behavior. It does not prove the complete Ability library, triggers, lifecycle effects or interactions.

Why items are now PARTIAL rather than BLOCKING:
Canonical held-item state, semantic rule-effect playback events and the parity-backed Pink Pearl damage hook prove an authoritative item path. The rest of the item registry and item behaviors remain unverified.

## 11. Example contract — Storm Signal Tower

Narrative premise:
A coastal signal tower is failing during a storm while aggressive wild Pokémon occupy the maintenance platform.

Full version:
The storm creates moving electrical danger zones; safe positions change between rounds; some legal actions may manipulate tower hardware; the party must secure the platform and stabilize the signal.

Full dependencies:
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- full turn/round lifecycle
- full stateful damage pipeline
- terrain/weather/hazards/zones/reactions
- move-specific behavior
- abilities
- AI legal-action infrastructure
- AI tactical policy
- adapter/playback

Current blockers:
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- adapter/playback
- full damage/move/ability families remain partial

Reduced version:
The storm remains visual and affects overworld access only. The maintenance platform is a static legal arena. Players resolve an ordinary encounter, then interact with the tower through an overworld repair step. No electrical zone applies tactical damage or status.

## 12. Example contract — Cliffside Stampede

Narrative premise:
Travelers are trapped at a narrow pass while frightened Pokémon rush through the area.

Full version:
The encounter uses push/knockback, interception, protected actors and escape lanes. Positioning prevents actors from being forced toward dangerous edges.

Blocked dependencies:
- complete movement including push/pull/knockback/interception/forced movement
- terrain/weather/hazards/zones/reactions if the cliff edge has mechanical fall consequences
- AI tactical policy
- adapter/playback

Reduced version:
Travelers wait in a safe overworld shelter outside the battle grid. A standard battle or calming/capture resolution clears the chokepoint. Cliff edges are represented only as legal static blockers, never as scripted knockback damage.

## 13. Example contract — Ancient Guardian Wake Cycle

Narrative premise:
An archaeological mechanism activates a guardian encounter in stages as different chambers power on.

Full version:
One continuous phase-based battle where arena state, legal Moves or guardian behavior changes at reviewed thresholds.

Potential dependencies:
- full lifecycle
- full stateful damage
- status lifecycle
- terrain/hazards/zones/reactions
- move-specific behavior
- abilities
- AI tactical policy
- adapter/playback

Reduced version:
Each chamber is a separate ordinary encounter with an explicit world-state checkpoint between them. The guardian does not gain hidden actions or arbitrary HP resets. The narrative still communicates progressive activation without pretending the engine supports continuous phase transitions.

## 14. World-state writeback

The encounter result must return to narrative systems through authoritative outputs.

Possible writeback:
- route_safe
- actor_rescued
- target_escaped
- faction_withdrew
- structure_secured
- device_activated
- guardian_dormant
- public_result_recorded
- ecological_disturbance_changed
- chronicle_event_created

Do not infer these solely from a cutscene. They should follow the reviewed battle/result contract or a separate authoritative overworld action.

## 15. Design workflow

For every new mechanically rich candidate:

1. Author the narrative premise without assuming a mechanic.
2. Describe the desired full tactical experience.
3. Map every required behavior to the permanent capability categories.
4. Inspect current engine evidence.
5. Mark VERIFIED, PARTIAL, BLOCKING or UNKNOWN.
6. Create a reduced version if the premise survives simplification.
7. Keep exact PTU/Caelo rules unresolved until source review.
8. Promote only after tests/contracts and adapter playback prove the needed behavior.
9. Preserve the old reduced version as a compatibility profile if useful.

## 16. Anti-false-completion rules

- Burn support does not prove status lifecycle.
- Weather damage-base arithmetic does not prove battlefield weather.
- Shift and Jump do not prove push/pull/knockback/interception.
- One authoritative Move test does not prove the move library.
- Mega Launcher parity does not prove the Ability family.
- Held-item state plus one Pink Pearl hook does not prove the Item family.
- A lifecycle registry seam does not prove all lifecycle-triggered rule families.
- A TrainerFeatureEvent type does not prove Trainer Features.
- Legal BattleChoice generation does not prove tactical AI.
- A headless semantic event does not prove Minecraft can animate or synchronize it.
- One boss fixture does not prove every boss archetype.

## 17. Source priority

Mechanical legality is resolved in this order for this project:

1. governing PTU/Caelo source material intended for Ouros;
2. Python AutoPTU oracle behavior where it encodes the chosen rules interpretation;
3. Java parity tests/contracts for current runtime readiness;
4. Minecraft/Cobblemon/Craftics adapter tests for world execution and playback.

External games, fangames, roleplay campaigns and other tabletop systems may inspire encounter structure but never establish PTU legality.