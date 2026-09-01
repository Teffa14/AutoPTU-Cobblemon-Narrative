# Marea Mourning, Private Memory & Post-Loss Seeds — Pass 191

Status: PROPOSED / NON-CANON
Date: 2026-09-01

These candidates use only the current Marea resident/institution network as anchors. They do not establish a cemetery, funeral rite, religion, inheritance law, death-record office or spirit doctrine.

No current canon resident is killed by this file.

## 1. The Notice Before the Notice

A historical death record being prepared for a Tideglass public display contains a detail that was preserved in a private source but never previously published.

Taro must decide whether the source supports public disclosure. Pia can locate circulation history and earlier editions. The player can help compare copies and provenance.

Playable decision:

Publish only the already public facts, seek additional authorization, or postpone the display update.

Persistent outputs:

- publication version;
- withheld claim record;
- provenance links;
- correction path if later authorization arrives.

No combat dependency.

## 2. A Packet for Someone Who Is Gone

Pia receives a legitimate packet addressed to a person whose death is already a validated historical fact.

The task is not to invent an heir. The player can trace the sender, determine whether the packet should be returned, preserved unopened, or routed to an institution with documented authority.

Connects correspondence continuity with post-loss privacy.

No combat dependency.

## 3. The Tool on the Wrong Shelf

Teo finds an old tool in ordinary repair stock carrying a provenance mark that links it to a deceased former worker in an archival record.

The object may have been legitimately transferred years ago. Its presence does not prove theft, abandonment or inheritance.

The player compares repair marks, intake notes and Tideglass records.

Possible closure:

The tool stays in service with corrected provenance, moves to archive custody, or remains unresolved pending stronger evidence.

No combat dependency.

## 4. One Name, Two Dates

A private memorial object brought to Tideglass for documentation carries a date that conflicts with an older public record.

Taro treats both as claims. Nerea can explain why one copied field observation cannot settle historical chronology. Pia can locate an earlier edition.

The quest can end with uncertainty preserved.

No combat dependency.

## 5. Covering the Shift

A resident needs to attend a private farewell outside their ordinary schedule.

The story focuses on Marea functioning without making the player responsible for grief itself. Another resident can cover the work, a service can run at reduced capacity, or a nonessential activity can be postponed.

Candidate existing roles:

- Lia covering dock coordination through a documented handoff;
- Ema postponing a noncritical observation block;
- Jace taking routine yard maintenance while Sela is absent.

No named death is established. The reason remains background unless later canonized.

No combat dependency.

## 6. The Companion That Waits at the Door

A future non-canon NPC death leaves a persistent companion Pokémon continuing an old routine at a workplace entrance.

The design focus is observation and care, not instant adoption.

Oren can assess welfare within verified mechanics. Mara can coordinate practical assistance. The player's actions can help establish temporary care without deciding final ownership.

Hard boundary:

`pokemon_follows_player != ownership_transferred`

Mechanical dependencies are care-state dependent, not battle-dependent by default.

## 7. Flowers With No Public Label

A small recurring arrangement appears at a non-canon private marker. No public plaque identifies the subject.

Different residents may know different amounts about it. The player is not entitled to the private story merely by discovering the site.

The interaction can remain observational unless an authorized actor chooses to share information.

This seed tests privacy-respecting discovery.

No combat dependency.

## 8. The Marker Moved for Repairs

A future resting-site marker must be temporarily moved because nearby infrastructure needs repair.

Teo can handle the physical fixture. Tideglass preserves location history. The actual authorization to move the marker must come from whatever future canon establishes as valid.

The player can document before/after state and prevent the old location from becoming false history.

No battle dependency.

## 9. Returned From the Field

Mara receives personal effects recovered after a future field death that has already been confirmed by authoritative state.

The items enter temporary custody. They do not become Field Office property and they do not become player loot.

The quest is about inventory reconciliation, packaging, provenance and routing.

Battle is explicitly outside the premise; the death occurred earlier and must already be authoritative.

## 10. The Public Story Is Smaller

Tideglass has a detailed private deposit about a deceased local figure but only a short, deliberately limited public notice.

A visitor assumes the archive is hiding a scandal. The player can investigate the publication policy and learn that privacy can explain an omission without proving corruption.

Potential outputs:

- corrected visitor interpretation;
- unchanged private record;
- optional public note describing why some holdings are restricted without revealing them.

No combat dependency.

## 11. Night Visit at the Upper Marker

Mechanically rich encounter candidate.

A future resident visits a private marker placed near, but not inside, an established route segment. Wild activity makes the ordinary return unsafe.

The memorial is not haunted by default and does not generate the wild Pokémon.

### Full version

If the encounter uses narrow route geometry, escort-like withdrawal, interception, displacement, visibility limits or terrain hazards, it depends on:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected content uses statuses;
- terrain/weather/hazards/zones/reactions when route conditions are tactical;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Full version disposition: BLOCKED by incomplete families.

### Reduced version

The visitor reaches a safe holding position through RPG world state. The marker stays outside BattleSpec. If one wild actor still blocks the route, run an isolated standard battle on stable audited terrain.

Allowed handoff:

`IMMEDIATE_ROUTE_THREAT_WITHDREW`

Afterward Narrative decides whether the visit ends or continues.

Forbidden battle conclusions:

- spirit appeased;
- grief resolved;
- memorial protected forever;
- death cause proven;
- supernatural claim confirmed.

## 12. What We Keep, What We Share

Longer-term arc candidate.

Over several seasons, Marea encounters different kinds of historical loss without a single central tragedy:

- a returned letter;
- a corrected archive date;
- a private object temporarily deposited;
- a repaired marker;
- a companion Pokémon care question;
- a public notice that intentionally discloses less than the archive knows;
- a later commemoration built only from information that was actually authorized for public use.

The arc makes privacy, provenance and continuity visible through small physical changes.

It does not require a universal grief meter, a town cemetery, a religion, a supernatural explanation or a sequence of deaths.

## Recommended first implementation slice

`A Packet for Someone Who Is Gone` is the safest first slice.

Why:

- it uses already established Tideglass/courier responsibilities;
- it requires no new map location;
- it exercises correspondence, privacy, archive provenance and post-loss continuity;
- it needs no battle mechanics;
- it can use a historical non-resident death fact rather than altering current Marea residents;
- it proves that a dead addressee does not automatically create an heir, new owner or public record.

## Canon promotion requirements

Do not promote any seed that establishes an actual Marea death, resting site, ritual or inheritance outcome until reviewed against:

- Caelo material;
- PTU rules where mechanical death is involved;
- player authorship constraints;
- current institutional canon;
- privacy/custody architecture;
- actual implementation support.