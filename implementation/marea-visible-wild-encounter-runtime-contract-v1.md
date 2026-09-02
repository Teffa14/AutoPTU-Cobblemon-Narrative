# Marea Visible Wild Encounter Runtime Contract v1

Status: IMPLEMENTATION CONTRACT / PROPOSED, NON-CANON SPECIES CONTENT
Date: 2026-09-02

## Goal

Make the first wild-Pokemon loop physically playable in Minecraft while keeping PTU encounter and battle authority outside Cobblemon presentation.

This contract extends the existing Marea runtime slice. It does not canonize a Sendero species table.

## Player-visible acceptance path

The first implementation must support this exact journey:

1. player leaves Puerto Bruma through the canonical south trailhead;
2. server identifies the player inside a bounded Sendero encounter region;
3. encounter authority asks the active Marea population profile for live candidates;
4. one or more candidates receive stable encounter actor IDs;
5. Minecraft/Cobblemon projects those actors visibly with authored presentation behavior;
6. the player may observe, avoid or approach them;
7. interaction/escalation requests an authoritative encounter handoff;
8. if battle is legal, BattleSpec is assembled from the already-provisioned actor rather than rerolling species/level;
9. AutoPTU-Java resolves combat under its verified contracts;
10. semantic outcome returns to Ouros world authority;
11. world state decides whether the wild projection remains, withdraws, is captured, is unavailable, or later reappears;
12. Minecraft reconciles presentation from that result.

## Authority boundaries

### Narrative / Ouros world authority owns

- population profile identity and version;
- habitat/region membership;
- encounter actor identity;
- live/available encounter state;
- ecology provenance;
- player-observation history when persisted;
- whether an encounter is eligible to be projected;
- post-battle world interpretation.

### PTU rules profile / encounter authority owns

- rule-governed tracking checks;
- any search frequency/cost restriction selected by the active profile;
- legal encounter level source;
- PTU Skills/Capabilities used before combat;
- capture legality and capture calculations;
- battle participant/stat/loadout construction where required.

### AutoPTU-Java owns during BattleSpec

- tactical legality;
- action economy;
- Initiative;
- targeting/range/LoS;
- movement legality supported by current contracts;
- accuracy/critical/damage calculations;
- stateful battle effects actually implemented and verified;
- battle semantic events.

### Minecraft/Cobblemon owns presentation only

- model/animation;
- bounded non-tactical locomotion;
- facing;
- warning/curiosity/flee visual state;
- particles/sounds/environmental tell;
- interaction hitbox;
- loading/unloading entity actors;
- transition/playback UI.

Minecraft entity state never creates a new encounter roll, changes level, establishes capture ownership, applies PTU damage, decides Fainted/Death, or completes a quest by itself.

## Required data object

Proposed runtime shape:

```text
WildPopulationProfile
  profile_id
  location_scope[]
  version
  active_context_predicates[]
  entries[]
  provenance_refs[]

WildPopulationEntry
  entry_id
  species_or_form_ref
  legal_level_source
  relative_frequency
  temporal_windows[]
  environmental_predicates[]
  presentation_behavior_profile
  ecology_tags[]
  encounter_flags[]

EncounterActor
  encounter_actor_id
  population_profile_id
  population_entry_id
  resolved_species_form
  resolved_level
  build_seed_or_sheet_ref
  current_world_state
  current_region_id
  created_at_world_time
  expires_or_refresh_policy
```

Exact field names may change in implementation. The authority separation may not.

## Presentation behavior profiles

Initial renderer-safe profiles:

### IDLE

Stays near a provisioned anchor, periodically changes facing or plays species-compatible ambient animation.

### WANDER

Moves inside an authored encounter-region polygon/radius. It must never path outside the region solely because vanilla mob AI selected a destination.

### AVOIDANT

Uses distance and line-of-sight only for presentation escape intent. If PTU adjudication is required for an actual chase/trap/interaction, the world runtime escalates to rules authority rather than resolving it from Minecraft speed values.

### TERRITORIAL_WARNING

Faces/approaches the player or performs a warning tell inside a presentation radius. Crossing the escalation boundary requests encounter adjudication. The presentation profile cannot unilaterally start tactical damage.

### HIDDEN_TELL

No visible Pokemon entity is required before discovery. Grass movement, sound, dust, water disturbance or another authored tell represents the live encounter actor. Revealing/interacting preserves the same encounter actor ID.

## Encounter regions for first slice

Use existing canonical anchors. New precise polygons/radii are implementation data and may be tuned without moving canon anchors.

Suggested first scopes:

- Sendero south trailhead / lower shelf transition;
- lower shelf;
- seasonal crossing approach;
- upper junction / Mirador branch transition.

Do not globally spawn wild Pokemon around every online player.

Each region should have:

- maximum projected actor count;
- minimum spawn separation;
- player-distance projection window;
- despawn/unload reconciliation policy;
- optional sub-biome tags;
- debug visualization available only to admin/dev tooling.

Those numeric tuning values are implementation parameters, not PTU rules.

## Ambient spawn lifecycle

### Provision

The server chooses an entry using the authoritative population profile and resolves the actor once.

### Project

Cobblemon receives an immutable binding token and presentation descriptor.

### Observe

Looking at or approaching an actor may create an observation event, but does not create capture/combat state.

### Engage

Player interaction or rules-authorized aggression sends `EncounterEngagementRequest(encounter_actor_id, player_id, intent)`.

### Handoff

If combat follows, BattleSpec uses the same actor identity and resolved species/level/build reference.

### Resolve

Allowed broad world results include:

- `WILD_ACTOR_REMAINS_AVAILABLE`
- `WILD_ACTOR_WITHDREW`
- `WILD_ACTOR_CAPTURED`
- `WILD_ACTOR_TEMPORARILY_UNAVAILABLE`
- `WILD_ACTOR_DEFEATED_BATTLE_STATE_REQUIRES_RULE_PROFILE_INTERPRETATION`

Do not derive permanent death from entity removal or Fainted unless the active rules profile and authoritative engine explicitly resolve it.

### Reconcile

Minecraft removes/updates/reprojects only after receiving the world result.

## Tracking path

The visible system must not make deliberate tracking obsolete.

Proposed request:

```text
TrackWildPokemonRequest
  trainer_id
  requested_species_or_form
  location_scope
  rules_profile_id
```

Rules authority resolves whether the selected PTU/Caelo/Kairos/Ouros profile requires Survival, Perception, Bait, an Extended Action, time cost, frequency limit, or another rule.

On success, the runtime may:

- reveal an already-provisioned matching actor;
- provision a matching actor from a legal local entry;
- return evidence/trail information instead of an immediate visible Pokemon if the active profile requires it.

The minimap, entity radar or Cobblemon spawn query must not substitute for this adjudication.

## Social/noncombat interaction gate

Before creating BattleSpec, the runtime must permit PTU-governed alternatives where appropriate.

Core PTU supports uses of Intimidate, Charm and Guile against wild Pokemon. Therefore an encounter actor can expose possible intents such as calm, scare away, distract, observe, bait, withdraw or engage when supported by rules/content.

The Minecraft UI may present an interaction option. It cannot decide the check or outcome.

## Sendero population authoring checklist

A future approved `ouros.marea.sendero_vidrio.population.v1` must be supported by:

- Marea environmental facts;
- Pokédex habitat/capability data;
- desired early-game difficulty band;
- time/condition rationale if used;
- encounter behavior notes;
- capture/boss/special flags if applicable;
- rules-profile compatibility;
- no reliance on unsupported engine mechanics for ordinary ambient fights.

At minimum, the first table should include ecological variety across ordinary-visible, avoidant/hidden and territorial/context-reactive behaviors. Species remain UNRESOLVED in this document.

## First safe battle profile

The first Minecraft-visible wild battle should intentionally avoid rich objective mechanics.

Use:

- stable simple geometry;
- ordinary one-side-vs-one-side or otherwise currently audited participant structure;
- no required weather phase;
- no terrain zones with mechanical effects;
- no reaction-heavy objective;
- no escort object in BattleSpec;
- no encounter-critical push/pull/knockback requirement;
- only Moves/Abilities/Items/Features whose current Java parity is verified for the selected combatants.

This preserves the narrative premise while the engine port remains incomplete.

## Capability dependency classification

### Required for first reduced visible-wild battle

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED within audited contracts;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- full turn/round lifecycle: PARTIAL, therefore constrain the selected battle content to currently audited lifecycle paths;
- full stateful damage pipeline: PARTIAL, therefore constrain content;
- status lifecycle: PARTIAL, therefore do not author a first encounter that depends on complex status persistence;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL.

### Not required for the reduced first slice unless selected content invokes them

- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- terrain/weather/hazards/zones/reactions: BLOCKING as a complete family;
- AI tactical policy: BLOCKING for ecology-aware/objective-aware tactics;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING for the complete target architecture, though the existing RPG mod already has world/runtime surfaces that can host the first projection work.

## Rich version later

A mature Sendero encounter may allow territorial groups, weather-sensitive populations, pursuit/escape objectives, protective positioning, terrain hazards, pack behavior or conditional reinforcements.

That version depends on the exact families it invokes. Never promote complete movement because forced-movement prevention works for one tested path, and never treat presentation aggro as tactical AI.

## Java live-evidence note for 2026-09-02

AutoPTU-Java head inspected at `716687c6f8431807b91f33567cc8c9c7fd010756`.

The latest commit wires forced-movement semantic events into authoritative move results and asserts a concrete prevention event ordering for a tested Trainer Feature path. This is valuable event/playback evidence for that path. It does not close the full complete-movement category.

## Required implementation tests

A production implementation should fail CI if:

1. a projected wild entity lacks an authoritative `encounter_actor_id`;
2. contact rerolls species or level;
3. two projections bind to the same live actor unintentionally;
4. entity unload marks the actor captured/dead/defeated;
5. capture completion occurs without authoritative capture result;
6. BattleSpec species/level differ from the engaged actor;
7. a population entry references a missing Pokédex/species record;
8. a profile references a missing canonical location;
9. a behavior profile can directly modify PTU HP/status;
10. a tracking UI can reveal/provision a requested species without rules authority when the active profile requires a check.

## Definition of done

This slice is done only when a human can join the server, physically walk onto Sendero, see/react to at least one authoritative wild actor, engage that same actor into an AutoPTU battle, finish the battle, and observe correct world reconciliation without admin commands fabricating the result.
