# Engine Readiness Snapshot — Pass 141

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to the visual-record, photography and imaging-provenance concepts added in Pass 141. Both engine repositories remain read-only for this task.

One implemented representative mechanic never promotes an entire permanent capability family.

## Inspected heads

AutoPTU-Java:

`14662fb67778e71f2d55fc7a74c43dd9a8b06fa1`

Latest inspected commit:

`Freeze multi-target move execution contract (#169)`

The latest parity-backed contract freezes resource accounting for ordinary multi-target Move execution: declaration/action/frequency cost is paid once while each target still resolves individually. Recent preceding slices also bind TILE choices to authoritative affected targets and execute supported pre-damage reactions inside the authoritative Move pipeline.

These are meaningful tactical-core advances. They do not create photography, camera traps, image capture, visual identification, crowd evacuation, wildlife-observation AI or visual-record provenance.

AutoPTU Python:

`cd4668a1b0e7c995bc12f3768f7b04cfa0f1c896`

Latest inspected commit:

`Career: keep slim Vercel artifact on thin entrypoint (#78)`

This is Career/deployment packaging and does not alter the capability classification below.

Project AutoPTU evidence also contains Chronicler archive actions. That is narrow evidence for specific Trainer Feature behavior; it is not a generic camera or photography subsystem.

## Java repository boundary

The live AutoPTU-Java README still explicitly leaves unfinished:

- complete combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- complete status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent reaction, TILE-target and multi-target execution work does not override these repository-level blockers.

## Visual-record mechanics boundary

The following Pass 141 state belongs outside AutoPTU:

- camera/imaging-device identity;
- capture events;
- original and derivative image identity;
- crop/edit/redaction provenance;
- visual observations;
- visual-identification claims;
- camera-trap deployments;
- camera uptime/downtime and obstruction;
- camera clock provenance;
- image-sequence continuity;
- sensitive-location redaction;
- publication permission;
- visual archives;
- public photography attention loops;
- subject-disturbance context.

AutoPTU becomes authoritative only when an actual battle opens and combatants require legal tactical resolution.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Java has parity-backed range, area, footprint, tile-target expansion and LoS support.

This can support a static encounter near a camera site or archive.

It does not identify objects inside photographs and does not model camera field of view, focal length or imaging occlusion.

### base movement legality — VERIFIED

Ordinary Shift/Jump legality remains verified for the ported scope.

This can move combatants in a frozen arena.

It does not model photographers approaching wildlife, technicians carrying cameras, crowd flow or animals withdrawing through an ecological corridor.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

Java has narrow reaction-movement support and frozen Push/Pull instruction contracts, but the README still marks forced movement/reactions incomplete.

FULL Pass 141 encounters depend on this family when technicians, visitors, wildlife or fragile-object carriers must cross threatened space or be intercepted.

### core calculations — VERIFIED

Core stat/type/damage-table primitives remain verified for the ported scope.

Image sharpness, photographer experience, evidence quality, camera model or publication popularity cannot modify combat stats without exact PTU mechanics.

### action economy/initiative — VERIFIED

Action-budget and initiative infrastructure remain verified.

The new multi-target contract further protects action/frequency ownership for ordinary area Moves.

Taking a photograph, changing a lens, retrieving a memory card or reviewing an image is not automatically a combat action.

### full turn/round lifecycle — PARTIAL

Round flow, selected delayed effects, selected temporary effects and selected reaction paths have parity-backed coverage.

The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

Recent pre-damage reaction ordering and multi-target execution work strengthen the pipeline, but the README still marks full damage incomplete.

A dropped camera, broken tripod, flash, crowd surge or falling archive object cannot create custom damage from narrative description.

### status lifecycle — PARTIAL

Selected application, prevention, suppression, stacking and timing behavior exists.

Flash photography, stress, being photographed, poor image quality or public attention do not create Blinded, Confused, Flinched or other Status conditions by narrative declaration.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction support has concrete slices, but the combined permanent family remains incomplete.

Camera equipment, viewing platforms, archive shelves, crowd barriers, mud, darkness or bright light do not become tactical Terrain/Hazard/Zone automatically.

### move-specific behavior — PARTIAL

Target resolution and multi-target execution coverage continues to grow.

Any specific Move used during a Pass 141 battle still depends on parity for that Move and its side effects.

### abilities — PARTIAL

Selected Ability families have parity-backed behavior.

No Ability should be inferred to improve photography, species identification, imaging, camera operation or evidence review unless an exact rule says so.

### items — PARTIAL

Item coverage remains incomplete.

Cameras, lenses, memory cards, film, tripods, flashes, batteries and ordinary archival materials remain narrative objects unless mapped to validated PTU Items.

### Trainer Features/perks — PARTIAL

Generic Trainer Feature infrastructure and selected concrete effects exist. AutoPTU Python also contains Chronicler archive behavior.

This does not establish a generic Photographer Feature pipeline, photo-derived buffs or automatic Chronicler records for every image.

### AI legal-action infrastructure — VERIFIED

Battle-choice legality is verified for the ported scope.

This does not provide AI reasoning for observation, wildlife withdrawal, camera recovery, evidence preservation or visitor evacuation.

### AI tactical policy — BLOCKING

No complete policy exists for Pass 141 objectives such as:

- `RETRIEVE_DEVICE`;
- `PROTECT_TECHNICIAN`;
- `PROTECT_CUSTODIAN`;
- `EVACUATE`;
- `WITHDRAW`;
- `PROTECT_WILDLIFE`;
- `CLEAR_ROUTE`;
- `REACH_EXIT`;
- `PRESERVE_EVIDENCE`.

A legal-action list is not objective-aware photography or conservation behavior.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer authoritative visual-record state from:

- screenshots alone;
- a camera model in a player's hand;
- a camera-trap block;
- entities visible in rendered chunks;
- custom map art;
- frame/item displays;
- flash particles;
- a player standing near a rare Pokémon;
- a filename or caption;
- client-side timestamp or coordinates.

The adapter must not decide image authenticity, identity, species, capture time, publication permission, subject disturbance, scientific value or combat bonuses.

## Pass 141 encounter dependencies

### Camera Trap Retrieval at Redbank Crossing — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if exact supported effects are invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING only if an exact validated environmental hazard becomes tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Resolve the wildlife crossing window and technician route in world state. Retrieve or abandon the device before battle. Open a static arena with actual combatants only. Victory does not create an image or determine migration state.

### Rare Roost Photography Surge — FULL

Primary blockers:

- complete movement for visitor evacuation and wildlife withdrawal;
- AI tactical policy for `EVACUATE`, `WITHDRAW`, `PROTECT_ROUTE`, `PROTECT_WILDLIFE`;
- adapter/playback;
- environmental family only if an exact validated environmental mechanic becomes tactical.

REDUCED:

Close the viewing point and move visitors through world state. Resolve wildlife response outside battle. Open a static encounter only if a distinct confrontation remains.

### Archive Negative Recovery — FULL

Primary blockers:

- complete movement when custodians or fragile-object carriers move through threatened space;
- AI tactical policy for `PROTECT_CUSTODIAN`, `REACH_EXIT`, `CLEAR_ROUTE`;
- adapter/playback;
- environmental family only if fire, flood, collapse or another validated hazard becomes tactical.

REDUCED:

Archives moves staff and collection objects to safety before battle. Resolve any remaining confrontation in a static arena. Resume custody and image-integrity work afterward.

### The Identification Dispute

Non-combat by design.

Uses Visual Records, Taxonomy, Identity/Pokémon Agency, Archives and Science. It does not require AutoPTU to choose a winner, and `UNRESOLVED` is a valid result.

## Explicit non-inferences

Pass 141 does not authorize:

- Photography or Perception DCs;
- camera equipment bonuses;
- automatic Chronicler records;
- image-derived Accuracy, Evasion or crit bonuses;
- flash-induced Blinded/Flinch/Confusion;
- camera-trap spawn modifiers;
- camera field-of-view as battle LoS;
- screenshot pixels as authoritative battle state;
- same appearance as proof of actor identity;
- same species/marking as proof of Pokémon identity;
- image presence as proof of ownership, custody, parentage or causation;
- edited image as automatic fraud;
- no image as proof of absence;
- viral image as proof of truth;
- publication as permission to reveal exact sensitive locations;
- photo score systems copied from Pokémon Snap.

## New overworld blockers

Pass 141 adds implementation needs outside the tactical core:

- `VISUAL_RECORD_IDENTITY`;
- `CAPTURE_EVENT_PROVENANCE`;
- `ORIGINAL_DERIVATIVE_GRAPH`;
- `IMAGE_TRANSFORMATION_HISTORY`;
- `CAMERA_DEVICE_STATE`;
- `CAMERA_TRAP_DEPLOYMENT_STATE`;
- `VISUAL_OBSERVATION_LEDGER`;
- `VISUAL_IDENTIFICATION_CLAIMS`;
- `IMAGE_SEQUENCE_CONTINUITY`;
- `SENSITIVE_LOCATION_REDACTION`;
- `VISUAL_RECORD_TO_MEDIA_HANDOFF`;
- `VISUAL_RECORD_TO_ARCHIVE_HANDOFF`;
- `VISUAL_RECORD_TO_SCIENCE_HANDOFF`;
- `VISUAL_RECORD_TO_MINECRAFT_PRESENTATION`.

None belong inside AutoPTU-Java's battle rules core.

## Unresolved mechanical / canon questions

- Does the final PTU/Caelo ruleset contain explicit Photographer mechanics, or should this remain mostly narrative/Chronicler-adjacent?
- Which Chronicler records can legally be created from visual evidence, if any?
- What imaging Items exist in the project source material?
- Are flash, darkness or sensor mechanics defined anywhere in Caelo?
- Which Ouros institutions may deploy camera traps?
- What visual privacy rules exist for PCs, NPCs and partnered Pokémon?
- Which sensitive wildlife sites require location redaction?
- Does a player-created photo need permanent binary storage, metadata-only storage, or curated promotion into Chronicle?
- How should multiplayer resolve two players publishing different derivatives of the same source image?

The full Caelo source set and Super PTU Online Helper were not reliably invocable in this run. No missing rule was invented.