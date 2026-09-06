# Conflicting Testimony investigation loop — Pass 295

Status: PROPOSED NARRATIVE PATTERN
Canon: NO
Date: 2026-09-05

## Premise

Several NPCs describe the same world event differently. The disagreement has multiple possible causes: deliberate deception, an honestly repeated false report, incomplete recall, incorrect source attribution, or genuinely independent contradictory evidence.

The player cannot solve the situation by asking a single designated truth NPC. The useful information exists across testimony, records, travel history, relationships and physical/world evidence.

## Reusable structure

An actor directly observes or otherwise learns a fact.

That actor has a reason to mislead a specific audience: protect a person, preserve institutional reputation, conceal an unauthorized action, gain time, redirect suspicion, avoid punishment or influence access to a location/resource.

The deceptive statement becomes a new information event.

A second NPC receives it and may repeat it honestly. A third remembers the content later but misattributes the source. A durable record or independent witness preserves another branch of evidence.

The investigation becomes reconstruction of the chain rather than a binary dialogue check.

## Example shell

A route, facility, habitat boundary, shipment, competition venue or research site changed state during a narrow time window.

Witness A possessed evidence for state X.

Witness A told Witness B state Y.

Witness B later repeated Y without deceptive intent.

Witness C remembers hearing Y but attributes it to a different person.

A log, publication revision, travel record or direct environmental trace independently supports one side of the chronology.

All names, places, institutions, species and motives remain authoring slots. None are canonized here.

## Consequences

The player may expose a deliberate lie but still need to repair damage caused by honest downstream repetition.

An innocent NPC can appear suspicious because source confusion changed who another witness names.

A liar can tell a technically true sentence while falsely attributing its origin, making verification of source lineage important.

A later correction can reduce current misinformation without erasing the fact that earlier actions were reasonable from the information available at the time.

Relationships and institutional trust can change differently depending on whether the failure was malicious, negligent or accidental.

## Reduced playable version

The reduced form uses only world-agent systems:

observation/claim -> deceptive statement -> message/publication -> receiver ledger -> source attribution -> interviews/archive lookup -> replanning -> social or travel consequence

This version does not require AutoPTU.

## Mechanically rich version

The same investigation can culminate in a pursuit, contested retrieval, hazardous expedition or confrontation.

Dependency classification must be attached to the actual scene:

- targeting/footprints/range/LoS: required only if the structured scene uses spatial targeting;
- base movement legality: required for ordinary tactical movement;
- complete movement including push/pull/knockback/interception/forced movement: required if any of those behaviors are authored;
- core calculations: required for ordinary deterministic battle arithmetic;
- action economy/initiative: required for structured turn order;
- full turn/round lifecycle: required for round/turn-timed consequences;
- full stateful damage pipeline: required if damage resolution is part of the scene;
- status lifecycle: required for persistent/temporary statuses;
- terrain/weather/hazards/zones/reactions: required when these are mechanical rather than descriptive;
- move-specific behavior: required for authored special Move semantics;
- abilities: required for Ability-owned behavior;
- items: required for Item-owned behavior;
- Trainer Features/perks: required for Trainer Feature interrupts/modifiers;
- AI legal-action infrastructure: required when AutoPTU must enumerate legal tactical actions;
- AI tactical policy: required when NPCs must autonomously choose among tactical actions;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for full in-world presentation and acknowledgement.

## Fallback rule

If a rich confrontation depends on a partial or blocking capability, preserve the investigation premise and resolve the immediate consequence through a reduced world-state scene, travel change, negotiation, guarded access, timed arrival or authored non-combat outcome until the required engine family is verified.

The adapter must never invent missing PTU mechanics to make the scene appear complete.

## Long-arc use

The same structure can support a faction schism, reputation collapse, wrongful accusation, rival manipulation, institutional cover-up, research dispute or historical mystery. The durable value comes from preserving who knew what, who said what, who heard it and what each person later remembered.