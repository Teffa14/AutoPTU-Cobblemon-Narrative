# Portable-find numbering and persistent identity scan — Pass 389

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-09

## Repository inspection and deduplication

The recursive `main` tree at `48bbbced0367d6814d7490d644ae65dfb63c57c7` was inspected before this scan. The pass also checked `CURRENT_FOCUS.md`, every file currently under `canon/`, the Pass 384-388 archaeology/evidence work, `tools/global_npc_site_evidence.py`, `tools/global_npc_resources.py`, `tools/global_npc_world_resource_checkpoint.py`, `tools/persistent_world_evidence_checkpoint.py`, the corresponding tests, and `sources/kairos/KAIROS_SOURCE_INDEX.md`.

The research corpus was searched before selecting sources. Pokémon Ranger: Guardian Signs, Pokémon Mineral, Pokémon Aragonite, Gaia, Stalactite and other recent archaeology/exploration anchors were rejected because they already appear in prior research. The exact Collections Trust numbering guidance, the A14 Archaeology Data Service record used below, and the PTU campaign pitch `Pokémon Heroes: Champions of Jugdral` did not have prior matching corpus entries by title/source query.

## Internal seam found

Pass 388 correctly separated discovery context from current resource state and custody history. The concrete implementation gap was the stable cross-system identity relation.

A second limitation became visible while inspecting recovery code: `WorldResource` provides the operational resource identity/state used by planning, but `OUROS_NPC_WORLD_CHECKPOINT_V10` currently persists reservation/request/handoff/attempt/appointment/reschedule history rather than a canonical catalog of every `WorldResource` definition. Pass 389 therefore must not pretend that V10 can independently prove the existence of a bound object.

The executable bridge should validate against an explicit declared `WorldResource` mapping supplied by the selected world/resource state. A later outer recovery owner can make that selection coherent by digest.

## Public source 1 — Collections Trust: numbering

Source:
https://collectionstrust.org.uk/resource/numbering/

Retrieved: 2026-09-09.

Collections Trust distinguishes entry numbers from object/accession numbers and explicitly recommends preserving external numbering systems as additional identifiers rather than overwriting them. Its archaeology guidance also describes museum accession numbers being used alongside an excavator's site code and notes that small-find numbers may need separate handling.

Reusable Ouros structure:

- one physical object can legitimately accumulate identifiers from different stages or institutions;
- an early field identifier can remain useful after a later repository/accession identifier is assigned;
- a number mismatch is evidence that needs reconciliation, not automatic proof that there are two objects;
- an identity bridge should point from historical field evidence to a stable world object without rewriting either system's local identifier history.

Do not import UK museum accreditation rules, legal ownership assumptions, exact numbering formats, or institutional policy into Ouros canon.

## Public source 2 — Archaeology Data Service A14 digital archive

Source:
https://archaeologydataservice.ac.uk/archives/collections/view/1003796/fullrecord.cfm?id=383973

Retrieved: 2026-09-09.

The public A14 record exposes a context record separately from an associated find record. The page presents a context number and then a small-find/object entry with its own identifying number and material/function metadata.

Reusable Ouros structure:

A field object should remain linkable to the context in which it was documented even after the physical object is handled by a different subsystem. Context identity and object identity should be cross-referenced instead of flattened into one mutable record.

Do not copy project identifiers, archaeological interpretations, site geography, object descriptions, or real-world dataset content into Ouros fiction.

## Public source 3 — PTU campaign pitch: Pokémon Heroes: Champions of Jugdral

Source:
https://www.reddit.com/r/lfg/comments/qekmoi

Retrieved: 2026-09-09.

This public Pokémon Tabletop United campaign pitch uses separated custody of important objects as part of the world's political stability, then makes uncertainty around a missing object consequential before the players have a complete account.

Reusable Ouros structure:

The state and identity of a portable object can matter to several factions or institutions at once. A discrepancy in custody or records can therefore create investigation, negotiation and rivalry without requiring that the object itself grant a battle power.

Do not import Jugdral, its hero, nations, relic set, war premise, elemental blessings, factions, characters, or plot. The only retained abstraction is that institutional consequences can depend on traceable object identity and custody.

## PTU/Caelo/Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a router, not rules authority. It points to Researcher, Chronicler, Paleontologist, Topographer, Skills/Edges/Features, encounter construction and Items/Gear as relevant source families. No source inspected in this pass authorizes an Ouros-specific accession Skill check, archaeological Item effect, ownership rule, extraction permission, or conservation Feature.

Current canon already supplies an archive institution (`Tideglass Archive`) and persistent NPC evidence rules, but this research does not assign the proposed numbering workflow to Tideglass automatically. Any local binding must be promoted separately through canon review.

## Reusable design lessons

1. Preserve field identity after later cataloging.
2. Treat multiple identifiers as aliases with provenance, not as automatic duplicates.
3. Bind the historical observation to a stable world-resource identity.
4. Let operational holder/location/state change without rewriting the discovery record.
5. Keep authority-to-bind separate from legal title, authenticity and custody authorization.
6. Recovery must fail when the selected evidence history points to a resource identity absent from the selected declared-resource state.
7. A later identifier reconciliation can be a story event while the physical object remains unchanged.

## New Ouros candidate direction

A portable find receives one field identifier when documented and a different catalog/accession identifier later. Old notes reference only the first code; newer records reference the second. Some actors conclude that one object disappeared and another appeared. A validated identity bridge can establish that both codes may refer to the same persistent physical resource, while still leaving open whether every disputed record actually belongs to that object.

This becomes `proposals/2026-09-09-the-find-with-two-numbers-pass-389.md`.

## Engine dependency posture

The reduced investigation requires no AutoPTU handoff. It can use semantic time, site evidence, the Pass 389 binding ledger, world-resource state, custody history, archive/report access and private knowledge.

A richer recovery/transport scene may require tactical geometry and base movement. Forced repositioning, carrying under pressure, push/pull, knockback or interception depend on complete movement. Multi-round timed protection, delayed hazards or phased environmental change depend on the full turn/round lifecycle. Damage-driven objective degradation depends on the full stateful damage pipeline. Persistent status consequences depend on status lifecycle. Flooding, unstable floors, debris zones, visibility effects and reactive hazards depend on the exact terrain/weather/hazards/zones/reactions mechanisms used. Moves, Abilities, Items and Trainer Features remain individually gated. Objective-aware protect/retrieve/escort/withdraw behavior depends on AI tactical policy, and authoritative non-KO pickup/handoff/playback remains an adapter requirement.

## Canon boundary

No object, numbering policy, museum procedure, ownership law, excavation authority, new institution, species, historical claim or PTU mechanical permission is established by this note.
