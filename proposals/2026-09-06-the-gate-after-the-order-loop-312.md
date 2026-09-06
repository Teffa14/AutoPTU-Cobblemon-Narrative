# The Gate After the Order — Pass 312

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

A route was closed after an authority relied on an evidence-custody assessment that later proved incomplete. The authority reviews the old decision and rescinds it.

The player returns expecting the world to snap back to normal. It does not.

The physical gate can be reopened because that consequence depended directly on the rescinded order. A warning notice is still posted because nobody has issued a public revision. A delayed shipment is still delayed. A worker's damaged reputation remains a separate social history. A merchant still expects compensation for losses. None of those facts are silently repaired by changing the route decision.

Then an inspection finds an unrelated structural problem on a bridge beyond the gate.

The authority now faces a second question: reopen immediately because the original reason disappeared, or retain the closure under a new independent safety basis.

## Narrative value

The loop turns correction into a world-state investigation rather than a dialogue flag.

The player can discover:
- which consequence came from which decision;
- which people received the correction;
- which effects have already been changed;
- which effects need separate action;
- whether a continuing restriction still relies on the invalidated report or has a legitimate new basis.

This supports institutional conflict without requiring corruption. Two NPCs can disagree because they are responsible for different consequences or because they know different facts.

## Cast archetypes

The reviewing authority owns the historical order and can rescind, amend or maintain it.

The route custodian controls the gate but cannot erase public notices or compensate merchants without separate authority.

The inspector owns the new structural finding and can provide an independent basis for continued closure.

The affected worker wants the correction acknowledged publicly because reopening the gate alone does not repair reputation.

The merchant wants practical restitution and may care less about the documentary distinction than about lost deliveries.

These are reusable roles, not canon NPCs.

## Reduced implementation

The route exists as authored world nodes with a gate consequence state.

Required sequence:
1. old custody assessment exists;
2. route-restriction decision depends on it;
3. the gate closure is registered as one downstream consequence;
4. a later assessment supersedes the old one;
5. the decision actor receives the correction;
6. the actor records a `RESCIND` or `AMEND` review;
7. the gate consequence receives a targeted `CEASE` or `AMEND` repair;
8. other consequences remain unchanged until separately handled.

If the bridge inspection supplies an independently authored hazard basis, a rescinded review may retain the gate consequence with an explicit independent basis reference.

No combat is required.

## Full encounter version

The inspection route crosses a storm-exposed service bridge and a maintenance corridor below it. The player may need to reach an isolated worker or Pokémon before the inspection can finish.

Intended mechanical elements:
- unstable footing and blocked lines;
- wind-driven forced movement;
- debris zones;
- timed structural deterioration;
- rescue/interception opportunities;
- environmental damage;
- optional hostile or panicked Pokémon whose behavior follows species rules rather than scripted aggression.

### Capability dependencies

Targeting/footprints/range/LoS: required for spatial rescue, obstruction and any tactical confrontation.

Base movement legality: required for ordinary navigation across valid bridge and corridor cells.

Complete movement including push/pull/knockback/interception/forced movement: required for wind displacement, falling-object movement and rescue interception.

Core calculations: required for ordinary deterministic tactical arithmetic.

Action economy/initiative: required if the inspection becomes a structured encounter.

Full turn/round lifecycle: required for timed deterioration and phase-linked environmental events.

Full stateful damage pipeline: required for environmental damage and downstream faint/injury interactions.

Status lifecycle: required only if the authored full version uses persistent shock, trapped, slowed or similar states.

Terrain/weather/hazards/zones/reactions: required for storm wind, unstable surfaces, debris areas and rescue reactions.

Move-specific behavior: required only for authored Pokémon Moves used in the encounter.

Abilities: required only when an Ability changes movement, weather, terrain or rescue outcomes.

Items: required only for mechanically authoritative equipment use.

Trainer Features/perks: required only for authored PTU Feature interventions.

AI legal-action infrastructure: required for autonomous tactical actors to choose only legal actions.

AI tactical policy: required for general autonomous rescue, retreat, pursuit or combat choices.

Minecraft/Cobblemon/Craftics adapter/playback support: required for reliable world projection and authoritative battle-result playback.

## Engine-safe fallback

The same story can run before the full tactical stack is ready.

The bridge uses fixed SAFE, BLOCKED and INSPECTION nodes. Weather is presentation plus authored availability gates. No forced movement occurs. Debris is a blocked node rather than a dynamic zone. Rescue is resolved through deterministic travel and world-agent state. No delayed collapse, reaction interception, persistent status or environmental damage is required.

The investigation premise remains unchanged: the original order can be wrong while a later independent hazard can still justify the same physical closure.

## Consequence branches

If the gate is reopened and no independent hazard exists, traffic resumes but social/public/economic consequences remain open threads.

If the gate stays closed under a new structural basis, the affected worker can still be cleared of the original suspicion even though the route remains unavailable.

If the authority fails to communicate the new basis, outsiders may interpret continued closure as refusal to honor the correction.

If the public notice remains stale after the operational state changes, a later publication-revision quest can emerge naturally.

## Canon boundary

No named location, institution, NPC, bridge, route, species, historical event or legal procedure in this proposal is canon-approved. The proposal demonstrates a reusable world loop for later binding to approved Ouros content.
