# Cobblemon Runtime Authority Boundary

Status: binding integration design rule for Ouros implementation work. This document does not create setting canon or new PTU mechanics.

## Purpose

Ouros should use as much of Cobblemon and Minecraft as is useful for presentation, persistence, overworld interaction and Pokémon-world embodiment without allowing Minecraft or Cobblemon battle-state code to become mechanically authoritative.

The governing architecture is:

- Minecraft/Cobblemon owns presentation and overworld embodiment.
- Ouros world-state systems own persistent narrative/world facts.
- AutoPTU owns tactical battle facts and resolution.
- Cobblemon battle-state authority is not part of the Ouros combat stack.

The integration should reuse Cobblemon aggressively where it is a view, asset source, entity implementation, animation surface, interaction surface or transport layer. It must bypass or adapt around Cobblemon code whenever that code attempts to choose combatants, construct authoritative battle state, resolve battle legality or decide battle outcomes.

## 1. Hard authority rule

No Minecraft/Cobblemon runtime object may become the source of truth for any tactical battle fact merely because it exists in the mod.

In particular, Ouros must not delegate these decisions to Cobblemon battle-state code:

- which Trainers or Pokémon are combatants;
- which Pokémon enter a battle roster;
- side/team membership;
- initial tactical positions when those positions have mechanical meaning;
- HP, injuries, statuses or combat stages used by the authoritative battle;
- initiative or action economy;
- legal Moves or legal targets;
- range, line of sight or footprint legality;
- damage, healing or status resolution;
- switching, withdrawal, defeat or victory state;
- capture legality or battle-result interpretation;
- weather, terrain, hazards or zones as tactical rules;
- AI tactical decisions;
- battle completion or result writeback.

If a Cobblemon class, component, API, event or subsystem is named or functions as `battle state`, `battle participant`, `battle actor`, `battle registry`, `battle side`, `battle controller`, `battle simulation` or equivalent, it is presumed non-authoritative until reviewed. Ouros may observe or bridge presentation-facing data from it only when doing so cannot mutate or override AutoPTU authority.

## 2. What Ouros should reuse from Cobblemon

Reuse is encouraged when the feature does not decide tactical truth. Candidate integration surfaces include, subject to actual API inspection and licensing:

- Pokémon models, textures, forms and species presentation;
- animations, poses, cries, particles and visual effects;
- Pokémon overworld entities;
- spawning/presence hooks when Ouros remains free to validate persistent identity and encounter eligibility;
- interaction hooks;
- storage/serialization utilities that do not overwrite Ouros-owned fields;
- player-facing Pokémon summaries and visual metadata;
- held-item visuals where useful;
- riding or movement presentation where mechanical eligibility remains governed by Ouros/PTU/Caelo rules;
- blocks, items, berries, apricorns, crops and decorative assets where their gameplay behavior does not invent PTU mechanics;
- NPC/Pokémon animation playback;
- sound and audiovisual battle playback;
- world particles and environmental presentation;
- entity tracking and client synchronization;
- Minecraft networking and packet transport;
- server/client lifecycle hooks;
- commands, menus, screens and interaction UI;
- world locations, block geometry and collision as input observations where an explicit adapter converts them into reviewed AutoPTU battlefield data;
- persistence hooks for identifiers that reference Ouros-owned records;
- compatibility hooks with other world-facing Cobblemon ecosystems when they remain downstream of Ouros authority.

The implementation goal is not to re-create Cobblemon features unnecessarily. The goal is to reuse everything safe around the authoritative combat core.

## 3. Presentation may mirror battle state; it may not originate it

During a battle, Minecraft/Cobblemon may display a projection of AutoPTU state.

Allowed direction:

`Ouros encounter/world state -> AutoPTU BattleSpec -> AutoPTU authoritative resolution/state -> adapter -> Minecraft/Cobblemon presentation`

Disallowed direction:

`Cobblemon battle state -> decide combatants/rules/outcomes -> write result into AutoPTU/Ouros`

A Minecraft entity can visually represent a combatant because AutoPTU says that persistent actor is in the battle. Its presence in the world must never be enough to enroll it automatically.

Likewise, despawning, chunk unloading, entity replacement, client latency or a Cobblemon-side battle callback must not remove, replace or defeat an AutoPTU combatant.

## 4. Combatant selection contract

Ouros constructs the combatant manifest before tactical resolution.

Every participant must originate from reviewed world state and an encounter/challenge contract. The manifest should carry stable references to the persistent Trainer/Pokémon records that AutoPTU will use.

Minecraft/Cobblemon may help locate or render those actors, but it cannot decide that a nearby entity joins the fight.

Wild encounters follow the same rule. A visible wild Pokémon does not become a tactical participant until Ouros selects that exact actor or an explicitly generated encounter actor according to the approved encounter pipeline.

Additional nearby Pokémon remain overworld actors unless Ouros explicitly adds them through a legal, reviewed transition.

## 5. Battle state contract

AutoPTU state is the only tactical source of truth once a battle instance is created.

Minecraft/Cobblemon receives a read/projection model containing only the data needed to present the current authoritative state and request player intent.

Player input should travel back as an intent/request. AutoPTU validates legality and produces the authoritative state transition. Minecraft then renders the returned semantic events/state.

The adapter must not silently repair, normalize or reinterpret an AutoPTU result using Cobblemon battle rules.

If Minecraft cannot represent an AutoPTU state yet, the correct behavior is reduced presentation, blocked promotion or explicit fallback. The correct behavior is never to let Cobblemon decide the missing rule.

## 6. Overworld-to-battle handoff

Minecraft remains highly valuable before battle creation. It can supply observations such as:

- exact persistent actor/entity references;
- world coordinates;
- facing or visual orientation;
- nearby block geometry;
- current visible weather;
- time of day;
- location/zone identity;
- interactable-object references;
- visible spectators or noncombatants;
- route closures and world barriers;
- animation context.

These are observations, not automatically tactical rules.

The Ouros adapter reviews/maps them into a BattleSpec only when the corresponding PTU/Caelo rule and AutoPTU capability exist. For example, visible rain can remain visual rain without becoming PTU Weather. A cliff can remain block geometry without automatically gaining fall/knockback mechanics.

## 7. Battle-to-overworld writeback

After AutoPTU resolves an authoritative transition or complete battle, the adapter may update Minecraft/Cobblemon presentation and Ouros persistent world state.

Examples include:

- play an animation for an accepted semantic battle event;
- reposition a visual entity to match an authoritative combatant position;
- show HP/status information that AutoPTU owns;
- render faint/withdrawal presentation after AutoPTU declares it;
- update encounter history;
- advance a challenge contract;
- change route/event/world state according to a reviewed result contract.

Minecraft animation timing cannot change the underlying result.

## 8. Cobblemon feature review classification

Every prospective Cobblemon integration should be classified before implementation:

`SAFE_REUSE`
Feature is presentation/overworld/infrastructure and does not own tactical truth.

`ADAPTER_REQUIRED`
Feature contains useful data or behavior, but Ouros must convert it into its own persistent or AutoPTU-owned representation before use.

`BATTLE_AUTHORITY_FORBIDDEN`
Feature chooses or mutates combatants, tactical state, legality or battle outcomes. Do not use it as authority.

`UNKNOWN_REVIEW_REQUIRED`
Implementation has not been inspected closely enough to classify.

This classification should be applied to concrete APIs/classes, not only broad Cobblemon feature names.

## 9. Encounter implementation requirement

Every mechanically meaningful encounter contract must preserve this boundary.

The `Minecraft/Cobblemon/Craftics adapter/playback support` capability category means the ability to project an AutoPTU-owned battle into Minecraft and collect player intent. It does not mean adopting Cobblemon's own battle simulation or battle-state ownership.

A reduced encounter must remain valid when all Cobblemon battle-state code is unavailable.

If an encounter only works because Cobblemon independently decides who is fighting or what happened, the encounter is not valid for Ouros.

## 10. Testing requirements

Integration tests should prove authority direction, not only audiovisual success.

Required classes of tests include:

- a nearby Pokémon does not join unless present in the Ouros/AutoPTU manifest;
- a missing/despawned Minecraft entity does not delete its AutoPTU combatant;
- a duplicate visual entity cannot create a duplicate tactical actor;
- client-supplied HP/status values cannot override AutoPTU values;
- Cobblemon-side battle callbacks cannot independently finish an Ouros battle;
- player intent rejected by AutoPTU is not executed because Cobblemon considers it legal;
- playback events are idempotent and cannot apply mechanics twice;
- reconnect/chunk reload reconstructs presentation from authoritative Ouros/AutoPTU state;
- overworld weather/geometry only gains tactical meaning through an explicit reviewed mapping;
- battle result writeback occurs from AutoPTU result data, not from visual/faint/despawn state.

## 11. Design consequence for future research passes

Future readiness snapshots must avoid wording that implies Cobblemon battle-state completion is a goal.

The desired Minecraft integration target is an authoritative AutoPTU adapter/playback layer that uses Cobblemon's safe world and presentation capabilities as deeply as possible.

When inspecting Cobblemon, future work should actively search for reusable non-battle-state APIs before proposing custom replacements. At the same time, any API that decides tactical truth must be isolated behind the authority boundary or excluded.

## 12. One-sentence invariant

Cobblemon shows and embodies the Pokémon world; Ouros chooses the actors and facts; AutoPTU decides the battle.