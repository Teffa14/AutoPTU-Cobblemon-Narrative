# Proposal — Reactive World-Event NPC Loop

Status: PROPOSED / NOT CANON
Date: 2026-09-05

## Premise

A world event should change the lives of NPCs who actually learn about it or are directly affected, while everyone else continues from the state they genuinely have.

The loop is global and location-neutral.

## Example structure

A route used by several travelers becomes unavailable.

One courier receives a reliable message and wakes immediately. Their existing delivery goal remains valid, but the new claim makes `REPLAN_ROUTE` eligible and more urgent.

A rival traveling elsewhere has not received the information and continues toward the old route until another event reaches them.

A faction officer receives two separate updates in the same semantic minute: the closure and a social obligation. Both causes enter one replan batch. The agent makes one agenda decision using all current state instead of executing two contradictory scripts.

A sleeping or off-screen named NPC is still eligible for semantic replanning if the relevant channel and world rules permit the information to reach them. A loaded Minecraft entity is not required.

## Mystery / quest use

This creates investigation structures where the player can reason about timing:

- who knew about an incident before a deadline;
- which NPC changed travel plans and why;
- why another character continued with stale information;
- whether several apparent reactions came from one common source;
- whether a message arrived before or after a decision;
- whether an NPC ignored information or simply never received it.

The player can alter later events by delivering evidence, warning someone, delaying communication or opening an alternative route without the narrative system rewriting earlier knowledge retroactively.

## Full version

The full version may combine:
- Pass 279 agenda and commitments;
- Pass 280 relationships/faction duties;
- Pass 281 world travel;
- Pass 282 memory/beliefs;
- Pass 283 information transport;
- Pass 284 selective wake-up/replanning;
- local Minecraft projection where a visible interaction is needed;
- AutoPTU only if a selected world intent becomes structured conflict.

## Reduced version

A fully useful reduced loop needs no tactical engine. It can use messages, off-screen travel state, schedule changes, investigation, missed meetings and route replanning entirely at Ouros world level.

## Mechanical dependency visibility

World-only information delivery and agenda reevaluation require none of the tactical capability families.

If the consequence becomes a structured encounter:
- pursuit, interception or forced displacement depends on complete movement;
- tactical weather, hazards, zones or reactions depend on that capability family;
- delayed combat effects depend on lifecycle plus the relevant move/ability/item/feature contracts;
- autonomous tactical choice depends on AI tactical policy;
- visible local reproduction depends on Minecraft/Cobblemon/Craftics adapter/playback support.

A world-agent `ReplanTrigger` never counts as a PTU Reaction or Interrupt.

## Canon boundaries

This proposal creates no canon route, city, faction, communication technology, closure, courier or rival. Concrete bindings must be authored separately and promoted explicitly.
