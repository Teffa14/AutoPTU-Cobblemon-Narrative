# Proposal — global NPC travel living-world loop

Status: PROPOSED / NOT CANON
Date: 2026-09-05
Depends on: global NPC agenda, social/faction state, global travel contract

## Premise

Recurring NPCs should occupy the world continuously enough that distance matters.

A rival who wants to meet the player, a mentor with a job in another settlement, a courier carrying information, a researcher answering an ecological event and a friend attending a tournament all use the same travel architecture. Their destination comes from goals, relationships, duties or commitments. Their journey comes from the global route planner.

## Full intended loop

1. An existing agenda source creates a destination-bearing purpose.
2. The NPC evaluates a known/permitted world route.
3. If a commitment has a start time, travel duration reserves a departure window.
4. The NPC can continue ordinary activity until departure if time allows.
5. Off-screen semantic travel advances along graph edges without requiring a loaded Minecraft entity.
6. A route disruption can change the ETA or block the journey.
7. Knowledge or permission differences can make two NPCs choose different paths through the same world.
8. Player proximity can promote an abstract leg into local Minecraft projection.
9. A meaningful interruption can become a world event, conversation or explicit AutoPTU handoff.
10. Arrival, delay or failure becomes input to schedules, relationships, factions and later memory rather than being erased.

## Example story structures

A recurring rival schedules a match in another city. The rival must leave early enough to get there. A closure creates a detour; the player may arrive first and hear that the rival is delayed. The rivalry persists without pretending the rival was always waiting behind the next door.

A trusted contact agrees to bring evidence to an investigator. One contact knows a restricted institutional route and arrives quickly; another must use a public connection. The difference comes from explicit knowledge/permission rather than NPC importance.

A mentor starts a long off-screen trip. When the player enters the same travel corridor during the appropriate semantic window, the world can locally project the mentor there. Meeting them on the road becomes a consequence of persistent state rather than a scripted spawn.

A faction duty and a personal commitment overlap. Travel time makes the conflict visible before either event begins. The NPC may leave early, choose one obligation, report likely lateness, or fail one commitment. Later social consequences can consume the actual outcome.

## Reduced implementation version

The reduced version uses only semantic graph travel:

- route selection;
- departure reservation;
- ETA;
- off-screen edge progression;
- replan/block state;
- arrival or lateness;
- ordinary agenda/social consequences.

It requires no AutoPTU battle resolution and no fine Minecraft navigation.

This version preserves the complete narrative premise: NPCs have their own lives, distances and schedules.

## Mechanically rich version

When a trip expands into a locally resolved encounter, the exact dependency families must be declared.

A visible ordinary walk may require Minecraft/Cobblemon/Craftics adapter support but not AutoPTU.

A PTU-resolved chase or obstruction can require targeting/LoS, base movement, action economy, lifecycle and tactical AI. Knockback, interception, forced movement, reactions, weather, statuses, special Moves, Abilities, Items or Trainer Features are included only when the encounter explicitly uses them and the corresponding engine family is verified enough for that encounter.

The route graph itself never supplies those mechanics.

## Long-term arc value

Global travel makes recurring cast arcs spatially coherent. NPCs can pursue careers, friendships, rivalries and faction obligations across the region while remaining physically constrained by where they actually were.

Later memory and communication passes can exploit these travel facts. An NPC can remember being delayed, tell another actor about a closure, learn a shortcut, promise to leave earlier next time or become unreliable because of repeated choices. Those consequences should be derived from persistent events, not from scripted dialogue.

## Canon boundary

No example actor, city, route, institution, closure or tournament in this proposal is canon-approved. This file defines reusable narrative structure only.
