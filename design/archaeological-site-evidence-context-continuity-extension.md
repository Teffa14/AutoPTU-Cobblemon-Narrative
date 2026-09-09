# Archaeological site evidence and context continuity extension

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE
Date: 2026-09-09

## Purpose

Define a reusable Ouros narrative/world-state model for ruins, excavations, historical structures, fossil/research sites and other persistent places where evidence depends on context.

This extension does not create an Ouros civilization, ruin, institution, archaeology law, species distribution or historical event. Those remain canon/content decisions.

## Core principle

A field site contains evidence with history. The game must not flatten every clue into a collectible item or replace prior observations when later interpretation changes.

`OBSERVATION != INTERPRETATION`

`PORTABLE_FIND != FIXED_FEATURE`

`POSSESSION != CONTEXT`

`CURRENT_SITE_STATE != HISTORICAL_SITE_STATE`

## Minimal evidence model

A reusable site implementation should support these independent records.

### Site

Persistent identity for the place or bounded field area.

Required fields:
- site_id;
- stable world location/ref;
- current access state;
- current physical-state revision;
- provenance refs for changes that matter.

### Portable find

An object that can leave the location without erasing its identity.

Suggested fields:
- find_id;
- item/object identity;
- discovery semantic minute;
- discoverer/observer;
- original site_id;
- original context ref;
- current custody/location;
- preservation/documentation state.

A portable find can survive while its original context is lost.

### Fixed feature

Evidence whose meaning depends on remaining at the site: wall alignment, cut channel, sealed opening, foundation, wear pattern, stair, pit, built surface or other nonportable feature.

Suggested fields:
- feature_id;
- site_id;
- geometry/location ref;
- first observed minute;
- observer;
- physical-state revision;
- accessibility/visibility state.

### Context record

A record of where and how evidence was encountered.

Suggested fields:
- context_id;
- site_id;
- evidence refs;
- spatial relationship refs;
- layer/relative-order note when known;
- environmental note;
- observation method/source;
- semantic minute;
- observer;
- confidence;
- provenance root.

This record remains historical even when the physical site later changes.

### Interpretation

A claim made by an actor or institution about evidence.

Suggested fields:
- interpretation_id;
- actor/source;
- evidence/context refs;
- claim content;
- semantic minute;
- confidence;
- supersedes/refines refs when applicable.

A later interpretation does not mutate the source observation.

## State changes

The field site may change through explicit world events such as exposure, collapse, stabilization, repair, excavation, backfilling, flooding, erosion, construction, deliberate disturbance, Pokémon activity, authorized removal or unauthorized removal.

Each change should preserve:
- previous revision identity;
- new revision identity;
- semantic minute;
- causal source if known;
- actor/institution if known;
- evidence affected;
- whether visibility/access/context changed.

Unknown cause remains unknown.

## Knowledge boundary

NPCs know only records they personally observed, received through communication, accessed through an archive/institution or learned through another explicit evidence path.

Faction membership does not imply shared archaeological knowledge.

A researcher who visited before a collapse and a ranger who arrives afterward may possess different but compatible truths.

## Quest structures

The system supports reusable quest loops without requiring new combat mechanics.

Field documentation: visit several evidence points, record them, return findings.

Revisit: earlier notes gain meaning after another discovery.

Custody chain: locate an object that moved while reconstructing where it came from.

Site-change investigation: compare historical observation with current state to determine what changed.

Preservation choice: extract, document, stabilize or leave evidence depending on time, authority and risk.

Competing interpretation: gather enough independent evidence to distinguish sincere disagreement from bad inference or deception.

## Dungeon and puzzle application

A ruin can use spatial reasoning without requiring a scripted lock-and-key dungeon.

Examples:
- two wall alignments imply different construction phases;
- a sealed doorway is meaningful because a later floor crosses it;
- a drainage feature explains why one chamber remained usable;
- an object found away from its expected context suggests later movement rather than automatically proving theft;
- repeated site maps reveal that a passage changed between visits.

The puzzle answer should arise from evidence relationships. It should not depend on copying a protected source's exact riddle, map or sequence.

## Reduced implementation

The reduced form uses only persistent world state and ordinary global-NPC infrastructure.

Required capabilities:
- persistent site and evidence IDs;
- semantic time;
- world travel;
- private knowledge and provenance;
- communication;
- access/permission state where applicable;
- deterministic observation/interpretation records.

No AutoPTU handoff is required.

## Rich implementation and permanent engine dependency map

Targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts. Required only if tactical inspection, protection or combat uses targeting/visibility.

Base movement legality: VERIFIED within audited ordinary contracts. Can support ordinary tactical traversal where no special movement is needed.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for collapsing floors that displace actors, forced slides, interception, drag/rescue or similar mechanics.

Core calculations: VERIFIED within audited deterministic contracts.

Action economy/initiative: VERIFIED for audited primitives. Required when documentation, interaction or protection becomes a tactical action competing with ordinary combat actions.

Full turn/round lifecycle: PARTIAL. Required for phase-based excavation pressure, countdowns or multi-round environmental changes.

Full stateful damage pipeline: PARTIAL. Required for authoritative injury/damage from tactical threats.

Status lifecycle: PARTIAL. Required for persistent/complex conditions such as trapped, blinded, poisoned or other status-dependent site play.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism. Unstable floors, falling debris, flood phases, dust zones, reaction-triggered cave-ins and similar effects require exact verified contracts.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. Current Transform/Impostor and Intimidate parity evidence proves only those specific seams and does not admit unrelated archaeological interactions.

Items: INDIVIDUALLY GATED. A required tool must be checked against authoritative item behavior rather than inferred from narrative text.

Trainer Features/perks: INDIVIDUALLY GATED. Researcher/Paleontologist/Topographer relevance in Kairos/PTU routing does not prove a specific Feature implementation.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for protect-evidence, rescue-first, escort, search, area-documentation, objective-aware withdrawal, disengage-after-objective and other narrative-objective policies unless specifically implemented/tested.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for persistent evidence identity, site revision projection, interaction acknowledgement, non-KO objectives and authoritative end-to-end playback.

## Adapter boundary

Minecraft may display the site, blocks, objects, particles, animations and local entities.

Ouros owns:
- stable evidence identity;
- historical revisions;
- provenance;
- observation records;
- knowledge;
- interpretation history;
- canon meaning.

AutoPTU owns structured tactical truth whenever the explicit handoff occurs.

Minecraft block state alone cannot silently rewrite historical evidence.

## Canon promotion checklist

Before an authored archaeological site becomes canon, resolve:
- exact location in approved Ouros/Caelo geography;
- historical culture/event authority;
- responsible institution/owner if any;
- public/restricted/private access;
- species and habitat from approved source authority;
- which evidence is portable and which is fixed;
- what is genuinely known at campaign start;
- what remains uncertain;
- PTU Features/Items/skills used and their authority;
- battle handoff and reduced implementation;
- aftermath and site-state persistence.
