# Global NPC Audience / Recipient Resolution Contract

Status: PROPOSED IMPLEMENTATION CONTRACT
Date: 2026-09-05
Scope: global persistent/recurring NPC world-agent AI

## Purpose

Pass 283 can transport information once a sender, receiver and channel are known. Pass 284 can wake the affected receiver after delivery. This contract owns the missing decision immediately before transport: which explicit recipients a sender chooses to contact.

Audience resolution is global world-agent policy. It is not dialogue generation, faction hive-mind state, Minecraft proximity truth or AutoPTU tactical policy.

## Core flow

```text
sender knows claim
+ candidate contacts the sender can actually consider
+ directional relationships
+ explicit institutional duties
+ proximity/contactability
+ topic/role relevance
+ communication budget
= explicit ranked recipient set
-> Pass 283 schedules one envelope per selected receiver
-> delivery updates only that receiver's private ledger
-> Pass 284 wakes only affected agents
```

## Invariants

1. Shared faction membership alone never broadcasts a claim.
2. A candidate without a reachable channel cannot be selected when reachability is required.
3. Audience size is bounded by policy; large fanout requires an explicit broadcast/publication subsystem.
4. Selection is deterministic for identical state. Equal scores break by stable agent ID.
5. Directional relationship state may affect likelihood of contact but never changes truth or recipient knowledge by itself.
6. Institutional routing requires an explicit obligation tag on an eligible recipient in a shared organization. Membership alone is insufficient.
7. Topic and role relevance are world-simulation inputs. They do not create permissions or secret knowledge.
8. Selecting a recipient does not deliver information. Pass 283 remains transport authority.
9. Selecting a recipient does not mutate trust, affinity, faction standing or belief state.
10. No region or settlement may fork the semantics of recipient selection.

## Initial scoring inputs

The executable foundation uses bounded contributions from:
- sender -> receiver trust, affinity, respect and fear;
- explicit receiver institutional obligation for the communication;
- semantic proximity/contact opportunity;
- topic relevance;
- explicit role relevance.

These weights are Ouros simulation policy, not PTU/Caelo/Kairos rules.

The score answers only whether this sender has a reason to contact this receiver now. It does not answer whether the receiver believes the message.

`RECIPIENT_SELECTION != BELIEF_UPDATE`

## Faction boundary

Organizations may define explicit reporting roles. Example: a field member who observes a hazard may have a reason to contact an on-duty recipient with `RECEIVE_HAZARD_REPORT`.

The organization still does not gain the observation globally. Other members remain ignorant until a separate legal information path reaches them.

`MEMBERSHIP != AUDIENCE`

## Budget and backpressure seam

`max_recipients` is an initial per-decision fanout cap. Candidates below the cap remain uncontacted, even when they were otherwise eligible.

This is intentionally compatible with future backpressure work. A public bulletin, broadcast, news service or emergency alert must have its own explicit audience-expansion contract rather than setting an arbitrarily huge individual fanout.

## Minecraft/Cobblemon boundary

Local contactability may come from an accepted adapter observation, but this planner does not inspect Minecraft entities directly. A local conversation channel can still require the Pass 283 acknowledgement gate before delivery.

## AutoPTU boundary

This system requires no tactical capability family for ordinary communication. It never chooses Moves, targets, squares, initiative, reactions, damage, statuses or forced movement.

If information later causes a structured encounter, that encounter inherits the exact AutoPTU capability dependencies of its intended mechanics. Audience resolution itself remains world-layer policy.

## Canon status

The contract and implementation are proposed reusable infrastructure. Fixture agents, factions, channels, scores and obligation tags are synthetic validation data and do not create Ouros canon.
