# The Box That Waited — Pass 307

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

Months after a relay-failure inquiry appears exhausted, a sealed evidence container is found during a records-room reorganization. The object itself is not new. What changes is the surviving handling documentation: the container can now be linked to an earlier collection event that investigators had treated as a documentation gap.

The old conclusion remains historically true: at that time, the investigator lacked continuity evidence. A new assessment may now support continuity without erasing the earlier uncertainty.

## Narrative loop

The player first encounters the case as background history. An earlier relay investigation contains an unresolved custody gap. The site may already have been repaired and the people involved may have moved on.

Later, a durable world event makes an old evidence container and a transfer receipt relevant again. The player can revisit the archive, interview people whose relationships have changed, and return to the original site where ordinary environmental details now carry a different interpretation.

The reopened inquiry can lead to several original outcomes without requiring one canonical culprit: the new receipt closes only the custody gap; the physical artifact still supports the original technical interpretation; re-examination weakens that interpretation; a separate compromise claim appears; or different NPCs continue to disagree because the new material has not reached all of them.

## Persistent-state requirements

The custody registry must survive restart in the same logical checkpoint as the investigator's private evidence ledger. A restored assessment cannot cite support evidence that disappeared from the ledger. A later checkpoint must preserve both the old assessment and any newer assessment rather than rewriting history.

The world should also preserve who actually learned about the reopened evidence. Discovery by one investigator does not update a faction or settlement automatically.

## Reduced implementation version

This version requires no AutoPTU combat.

The archive, storage room, relay and interview locations are ordinary world nodes. Travel uses verified base movement/world travel. Documents and physical observations create provenance-backed claims. Pass 306 evaluates custody. Pass 307 makes that custody state restart-safe inside the global checkpoint. Replanning and communication determine which NPCs react.

The narrative premise remains intact even if every active hazard is presentation-only.

## Full encounter version

The evidence container is recovered from an old service annex damaged by recurring weather. Entry may require traversing unstable maintenance access while another group tries to reach the same storage area first. A later confrontation can occur if interests collide over whether the evidence should be preserved, surrendered or destroyed.

Intended mechanical dependencies:

- targeting/footprints/range/LoS: required for spatial interaction or conflict; currently VERIFIED within audited contracts;
- base movement legality: required for ordinary access; VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement: required only if wind displacement, rescue interception or forced movement is mechanically active; PARTIAL;
- core calculations: VERIFIED within audited contracts;
- action economy/initiative: VERIFIED within audited contracts;
- full turn/round lifecycle: required for timed collapse/weather phases; PARTIAL;
- full stateful damage pipeline: required if environmental or combat damage is authoritative; PARTIAL;
- status lifecycle: required for persistent injury-like/status consequences authored as PTU conditions; PARTIAL;
- terrain/weather/hazards/zones/reactions: required for active unstable-floor, debris, storm or reaction-rescue mechanics; MIXED/PARTIAL/BLOCKING by subfamily;
- move-specific behavior: required only for authored Move interactions; PARTIAL;
- abilities: required only for authored Ability interactions; PARTIAL;
- items: required only for mechanically active PTU Items; PARTIAL;
- Trainer Features/perks: required only when a Feature changes legality, investigation or combat; PARTIAL;
- AI legal-action infrastructure: VERIFIED within audited contracts;
- AI tactical policy: required for general autonomous tactical opposition; BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback: required for authoritative end-to-end presentation; PARTIAL/BLOCKING.

## Reduced tactical fallback

Represent the annex as safe, blocked and accessible nodes. Weather changes visibility and dialogue only. Do not use wind knockback, timed collapse, dynamic hazard zones, reaction rescues or persistent statuses. If conflict occurs, keep it within verified movement/targeting seams and avoid mechanics whose owning capability family remains partial or blocking.

## Canon questions left open

No specific relay, archive, faction, settlement, culprit, Pokémon species or investigator is canonized here. Before binding this loop to a real Ouros location, validate which PTU/Caelo Skills, Features or Pokémon capabilities can legitimately discover, preserve, authenticate or re-examine the relevant evidence.
