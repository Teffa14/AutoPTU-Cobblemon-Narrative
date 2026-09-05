# Proposal: selective warning network loop — Pass 285

Status: PROPOSED / NOT CANON
Date: 2026-09-05

## Premise

A meaningful world event occurs. Several NPCs could potentially be told, but the first witness has limited time and does not treat every acquaintance, coworker or faction member as an automatic audience.

The witness chooses explicit recipients from relationship, duty, relevance and reachability. Those people receive the information later through Pass 283, update private beliefs through Pass 282 and selectively replan through Pass 284.

## Full narrative version

A player can encounter the same event from several social directions:

- a close friend receives a personal warning first;
- a duty officer receives an institutional report because their role explicitly owns that subject;
- another member of the same organization remains unaware;
- a rival is reachable but omitted because the sender has no sufficient reason to contact them;
- one intended recipient is unavailable and never receives the message;
- a later independent witness contacts a different audience, creating a second provenance root.

The resulting story question is not only what happened. It can also be who was warned, who was excluded, whether that choice was reasonable and what consequences followed before the information spread further.

## Reduced executable version

No combat is required.

1. Record one semantic observation.
2. Resolve a bounded audience.
3. Schedule one Pass 283 envelope per selected receiver.
4. Deliver only when each channel becomes due/available.
5. Wake only recipients whose private state actually changed.
6. Let their existing global agenda choose the consequence: report, travel, warn someone else, wait, investigate or continue ordinary work.

This version can run entirely in Ouros world-agent simulation.

## Optional mechanically rich escalation

A recipient may later decide to investigate a dangerous location, escort someone, flee, pursue or confront another actor. At that point an explicit encounter contract must declare the mechanics it uses.

Possible dependencies:
- targeting/footprints/range/LoS if structured targeting is needed;
- base movement legality for ordinary PTU movement;
- complete movement if interception, push/pull, knockback or forced movement matters;
- action economy/initiative and full turn/round lifecycle for structured encounter sequencing;
- full stateful damage pipeline if damage occurs;
- status lifecycle for persistent conditions;
- terrain/weather/hazards/zones/reactions for mechanically active environment or reactions;
- move-specific behavior, Abilities, Items and Trainer Features only when explicitly present;
- AI legal-action infrastructure for legal tactical choices;
- AI tactical policy if autonomous tactical selection is required;
- Minecraft/Cobblemon/Craftics adapter/playback for end-to-end visible realization.

Audience selection itself depends on none of those tactical families.

## Worldbuilding use

This loop can support rumor mysteries, evacuation warnings, tournament news, commercial opportunities, scientific observations, faction mobilization, missing-person searches, road closures and social consequences without hard-coding any region.

Fixture names and organizations used by tests remain synthetic.
