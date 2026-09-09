# The Catalog That Survived the Evacuation

Status: PROPOSED / NON-CANON.
Date: 2026-09-09

## Premise

A field team documents a portable find and registers the physical object under a stable resource identity. Before normal processing finishes, a local emergency forces the receiving facility to evacuate part of its collection.

Months later, the old field register still points to the original receiving location. A current inventory places the same resource elsewhere. A third record says the original room was damaged badly enough that some staff assumed its contents were lost.

All three records can be historically accurate.

The mystery is not solved by asking which document is false. The useful questions are when each record was true, who had custody at each transition, and whether the stable object identity remained connected to its original discovery context through the disruption.

## What the scenario can establish

With the Pass 390 recovery seam, the world can durably establish that:

- one `PORTABLE_FIND` observation occurred at a specific site revision and semantic minute;
- the observation was explicitly bound to one stable `WorldResource` identity;
- the evidence checkpoint survived restart with that binding intact;
- later holder, location and operational-state changes do not erase the discovery relation.

It cannot automatically establish:

- legal ownership;
- who authorized removal or emergency relocation;
- whether every transfer was legitimate;
- whether a damaged room destroyed other objects;
- whether an apparently missing document was lost, delayed, withheld or never created;
- whether the resource has scientific, sacred, commercial or battle-Item significance.

## Reduced playable version

No AutoPTU handoff is required.

The investigation can run with:

- semantic time;
- site-evidence history;
- `PortableFindResourceBindingLedger`;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2`;
- an externally supplied declared-resource identity catalog;
- ordinary resource/custody records;
- archive/publication/private-knowledge access;
- world travel and communication.

The player reconstructs the object's path by reconciling time-scoped records. The immediate objective can succeed once the discovery identity, current resource identity and custody path are sufficiently reconciled, even if legal ownership or the emergency's full cause remain unresolved.

## Rich encounter version

The same premise can support a playable evacuation or recovery scene during the disruptive event.

Possible objectives:

- recover a documented object before access closes;
- escort a curator or field researcher carrying provenance records;
- preserve evidence labels while moving material to a safe staging point;
- choose which records or objects to evacuate under time pressure;
- withdraw after the evidence objective is complete rather than clearing every hostile Pokémon.

A battle, if present, is pressure around the objective. KO is not the narrative victory condition.

## Exact engine dependencies

Targeting/footprints/range/LoS: usable only inside verified audited scopes for ordinary tactical geometry.

Base movement legality: usable inside verified audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for forced carrier displacement, rescue repositioning, pulls, knockback or interception.

Core calculations: verified only within audited scopes.

Action economy/initiative: verified for audited primitives only.

Full turn/round lifecycle: PARTIAL. Required for timed evacuation windows, phase changes or delayed collapse timing.

Full stateful damage pipeline: PARTIAL. Required if damage persistently alters a carrier, protected object or objective state.

Status lifecycle: PARTIAL. Required for lasting conditions that affect evacuation or carrying.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Fire, flood, debris, unstable floors, smoke/visibility and triggered collapse must be individually verified.

Move-specific behavior: individually gated.

Abilities: individually gated. AutoPTU-Java merge #420 strengthens only the exact authoritative Impostor round-start seam.

Items: individually gated. The archaeological resource is not a PTU battle Item unless source authority separately establishes that fact.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: verified only in ordinary audited scopes.

AI tactical policy: BLOCKING for protect-object, retrieve-object, evacuation-first, escort, rescue-first, objective-aware withdrawal and disengage-after-objective until exact policy coverage exists.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, environmental objective state and authoritative non-KO completion playback.

## Canon questions deliberately left open

- Which Ouros location or institution, if any, owns this event?
- What caused the evacuation?
- Was the object formally accessioned, temporarily deposited or merely in field custody?
- Who had authority to move it?
- Who legally owns it?
- Which NPCs had access to the old and current records?
- Does the find have any wider cultural, ecological or mechanical significance?

No answer is canon in this proposal.
