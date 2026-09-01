# Marea Salvage and Recovery Seeds — Pass 187

Status: PROPOSED. NOT CANON.
Date: 2026-09-01

These seeds apply `design/salvage-recovery-found-property-continuity-layer.md` to the canon Marea district. They introduce no new law, government agency, insurance system, Legendary event, Pokémon encounter table or confirmed historical disaster.

Existing Marea residents and institutions should own the work wherever their canon roles already fit.

## 1. Tide-Thrown Crate

Premise:

After rough conditions, a closed crate is found above the usual working edge near Ferry Landing. It has a faded handling mark and a newer handwritten mark that do not immediately identify the same destination.

Participants:

- Lia Orren can compare ferry freight-window records;
- Mina Orren can judge whether approach/removal around landing infrastructure is safe within her ordinary repair scope;
- Brin Hale can compare cooperative/storehouse container marks if asked;
- Tideglass can check older identifiers only if the player or resident brings a documented observation.

Useful outcomes:

- the crate is matched to a recent delivery and routed back through custody;
- the mark identifies a container family but not the specific current custodian;
- the crate remains safely stored with claim unresolved.

No outcome requires theft, sabotage or a villain.

Recommended first implementation candidate because it needs no BattleSpec.

## 2. Mirador Instrument Below the Deck

Premise:

A weather or observation instrument component is found downslope from Estación Mirador after heavy weather. Its shape and wear make a Mirador connection plausible.

Key design point:

Physical identification, functional inspection and scientific readiness are separate decisions.

Nerea or Ema may recognize the instrument record. Teo may be able to assess ordinary physical damage if within scope. Even after repair, Mirador can require calibration or comparison before accepting readings.

Possible closure:

The object returns to Mirador but remains marked `NOT_CLEARED_FOR_DATA_COLLECTION` until its downstream verification is complete.

## 3. Two Marks on One Parcel

Premise:

A recovered parcel carries an older stamped identifier beneath a newer transport label.

The first mark points toward one institution; the later mark points toward another.

Gameplay:

The player can document both marks, compare dates and determine whether the older identifier records maker, prior custodian, reusable container pool or an earlier route.

The story is successful even if no original private owner is established.

## 4. Brin's Returnable Crates on the Wrong Shore

Premise:

Several recognizable reusable containers appear away from their normal circulation point.

Brin can establish that the cooperative uses that container type. That does not automatically prove every container is currently cooperative property or explain how it moved.

This seed connects recovery with the provisioning layer after intake is accepted.

Persistent consequence:

Recovered containers can later re-enter normal dispatch circulation rather than remaining permanent quest props.

## 5. Old Survey Tag in New Debris

Premise:

A tag associated with historical survey work is discovered among recent storm-thrown material.

Risk:

Residents may assume the tag proves the whole debris field is old or that a historic site has been uncovered.

Tideglass can instead establish the tag's documented era and known uses. Mirador can record the present find context. Neither conclusion alone proves when the surrounding material arrived.

This seed trains provenance discipline without requiring a hidden treasure reveal.

## 6. Cleanup With One Hold

Premise:

Most debris around a public working area can be cleared. One object has identifiers or context important enough that it should remain documented and separately held.

Gameplay purpose:

Teach that cleanup and investigation can progress at different speeds.

World consequence:

The area visibly becomes cleaner while one tagged item remains in a controlled location awaiting review.

## 7. The Tool That Works Too Soon

Premise:

A recovered tool powers on or appears physically functional after drying/repair.

Teo, Mina or another qualified resident can still refuse ordinary deployment until the relevant inspection is complete.

The lesson is practical rather than bureaucratic: apparent function is one observation, not complete readiness.

## 8. Pokémon With a Found Object

Premise:

A wild or companion Pokémon is observed carrying, moving or repeatedly visiting a human-made object.

The system records:

- Pokémon identity if known;
- observed interaction;
- object description;
- location and time.

It does not infer:

- that the Pokémon owns the object in a legal sense;
- that it stole the object;
- that it is delivering the object;
- that it understands the object's human significance.

Any capture or battle remains a separate PTU question and should not be used as a shortcut to acquire the object.

## 9. Interrupted Ferry Delivery

Premise:

A routine shipment arrives with one container missing from the acceptance count. Later, a matching container is found nearby but outside the normal handoff point.

The recovery case can corroborate identity and restore custody, while the delivery ledger separately records whether the original shipment was accepted, delayed or short.

This connects Ferry Landing, courier/custody and provisioning systems without merging them.

## 10. Historical Object, Ordinary Material

Premise:

A physically mundane object has a mark that suggests an older period of district work.

It may have little resale or mechanical value while still having documentary value.

Tideglass can preserve provenance and testimony without turning every old object into a relic, magical artifact or museum centerpiece.

## 11. Claim Asserted, Cause Unknown

Premise:

A resident can credibly establish that an object was in their custody before it disappeared. Nobody can yet prove whether weather, handling error or another mundane cause displaced it.

The object may still be returned through an approved handoff while the incident cause remains unresolved.

This prevents the quest system from requiring a culprit before ordinary recovery can finish.

## 12. What the Tide Gives Back

Longer-term arc concept.

Questline types:

- REGION
- SETTLEMENT
- ITEM
- EQUIPMENT
- EXPLORATION
- SECONDARY

Structure:

Across several unrelated weather, transport and maintenance events, Marea accumulates a small history of recovered objects. Some return to normal circulation. Some require repair. Some become archive records. Some remain unresolved.

The arc's value comes from continuity:

- residents remember earlier recovery procedures;
- storage shelves physically change;
- corrected labels persist;
- an object can reappear months later in normal use;
- old records can make later identification faster without making Tideglass omniscient;
- repeated recovery events can reveal weak procedures without implying conspiracy.

No single grand cause is required.

## Mechanically rich encounter: Recovery Line at Ferry Shore

### Narrative premise

A displaced container or equipment case lies beyond the normal working edge near Ferry Landing. Workers need to document and secure the area. Wild Pokémon activity makes the approach temporarily unsafe. The object itself must remain outside battle authority.

### Intended full version

The full version may include:

- workers and a recovery corridor;
- a persistent cargo object;
- shoreline or landing geometry;
- objective-aware wild movement;
- protection/interception around retreat lanes;
- displacement if selected Moves or Features support it;
- environmental pressure if weather, debris or unstable footing is tactical;
- post-battle return to recovery/custody work.

Permanent engine dependency categories required by the intended version:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when any such behavior is present;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected content;
- terrain/weather/hazards/zones/reactions if shoreline pressure enters BattleSpec;
- move-specific behavior for every selected Move;
- abilities for every selected Ability;
- items when any battle Item is allowed;
- Trainer Features/perks when Trainers participate mechanically;
- AI legal-action infrastructure;
- AI tactical policy for objective-aware positioning;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current classification: BLOCKED for the intended rich form because multiple complete families remain unverified or partial.

### Reduced version

Preserve the narrative premise while narrowing battle authority.

1. Discovery, documentation, cargo position, workers, hazard assessment and custody remain world-state objects.
2. Residents first move to a safe position through ordinary RPG/world orchestration rather than BattleSpec escort units.
3. The recovery object cannot be targeted, looted, pushed or destroyed by tactical simulation.
4. If a wild actor still prevents safe approach, compile an ordinary audited encounter on stable nearby terrain.
5. Select roster content only after exact Move/Ability/Item/Feature parity review.
6. AutoPTU may return a narrow consequence such as `IMMEDIATE_RECOVERY_AREA_CLEAR` or `IMMEDIATE_WILD_THREAT_WITHDREW`.
7. Narrative then resumes hazard assessment, physical retrieval, custody and claim handling.

The battle cannot decide:

- who owns the recovered object;
- whether it was abandoned;
- whether it is safe to use;
- whether it is historically important;
- whether a shipment should be accepted;
- whether compensation is owed;
- why the object was displaced;
- whether future shoreline access is safe.

This reduced version can advance worldbuilding without asking the Minecraft adapter to reproduce unsupported PTU rule families.

## Canon boundaries

This proposal does not canonize:

- a specific storm or wreck;
- a permanent debris problem at Ferry Landing;
- salvage rights;
- maritime jurisdiction;
- insurance;
- abandonment doctrine;
- criminal evidence procedure;
- a new Marea authority;
- any specific cargo commodity;
- any Pokémon species associated with recovery events;
- any historical wreck or disaster.

All seeds remain candidates until explicitly promoted through the repository's canon process.