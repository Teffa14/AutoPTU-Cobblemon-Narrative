# The Species That Was There Yesterday — Pass 332

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

A regional survey program detects environmental DNA from a Pokémon species that has not been directly observed in the surveyed waterway for years. The first result comes from a downstream collection point near a route or managed wetland. A follow-up team searches the exact bank and sees nothing.

The result is not automatically false, and the field team is not automatically looking in the wrong place.

The investigation asks a narrower question: what claim does each sample actually support, and how far can the institution responsibly extend that claim before more evidence arrives?

## Narrative purpose

This loop gives Ouros a research mystery where strong evidence exists before direct sighting. It supports Researcher, Chronicler, field-service and institutional characters without turning any laboratory result into world omniscience.

The same structure can support rare-species surveys, invasive-species alerts, migration questions, upstream habitat disputes, restoration monitoring or disputed historical records.

No species, settlement, laboratory, waterway or institution is canonized by this proposal.

## Persistent features

Candidate persistent feature roles:

- downstream sample station;
- upstream tributary junction;
- sediment deposition pocket;
- temporary wetland or side channel;
- field access point;
- sample-processing facility or archive;
- public notice board or publication channel;
- one or more later direct-observation sites.

Each feature retains its own observations and history. One result may be relevant to several features without collapsing them into one shared ecological state.

## Initial evidence

The first arc state can contain all of the following without contradiction:

- one properly identified downstream water sample reports a positive species-level signal;
- direct visual survey at that collection feature is negative;
- older local records contain no recent confirmed sighting;
- a second team notes conditions capable of moving biological material through the system;
- the public-facing summary compresses the result into wording that some readers interpret as “the species has returned.”

None of those statements establishes exact source location, count, breeding status, health, intent or current occupancy of the collection point.

## NPC and faction roles

### Field collector

Knows the collection feature, time, container identity, environmental conditions and handling steps personally performed.

Does not automatically know the laboratory result before delivery.

### Laboratory analyst

Knows the assay, controls, result and sample identity received.

Does not automatically know current field conditions or whether the source organism remains in the watershed.

### Survey coordinator

Receives reports and must decide whether to schedule repeats, broaden sampling, issue a limited notice or delay a stronger public claim.

### Local observer

May have repeated visual knowledge of one feature and legitimately report no sightings there.

### Archive or records custodian

Can provide older survey versions, past sample locations and historical claims without converting archive access into personal memory.

### Infrastructure or land manager

May need to decide whether a planned intervention should proceed, pause or receive additional monitoring.

Shared institution membership does not give any actor the others' evidence automatically.

## Investigation progression

### Stage A — verify the sample lineage

Confirm which feature, time, collector and container produced the reported result. Check whether the public map or notice points to the sample location, the inferred source area or a simplified administrative area.

### Stage B — broaden evidence without forcing a sighting

Possible actions include repeat water samples, sediment samples, upstream/downstream comparisons, archive review, local interviews and ordinary field observation.

The system should preserve each result independently instead of reducing the arc to a single hidden “species present” boolean visible to every NPC.

### Stage C — reconcile apparently conflicting observations

Examples:

- water positive, sediment negative;
- water negative, sediment positive;
- downstream positive, upstream negative;
- several negatives after one positive;
- direct sighting outside the area implied by the first public map;
- an older specimen/sample record that changes interpretation of what “return” means.

The player should be able to conclude that multiple datasets are compatible even when the public narrative originally made them look contradictory.

### Stage D — feature-scoped decision

The survey coordinator or land manager can choose a bounded response, such as:

- repeat sampling before changing access;
- protect one temporary side channel;
- delay work on one feature while leaving another open;
- publish a correction that narrows the claim;
- expand monitoring upstream;
- archive the detection as unresolved after a defined review window.

The decision should record the evidence set that justified it.

### Stage E — revisitation

A later visit can reveal a direct sighting, another positive, a run of negatives, a changed flow path, a seasonal return or evidence that the original signal came from transported material.

The later result may strengthen or weaken an interpretation without rewriting what earlier actors actually knew.

## Open explanations

The authored scenario can eventually choose one or combine several:

- a low-density Pokémon population was genuinely present but difficult to observe;
- a transient individual passed through before the field team arrived;
- biological material moved downstream from another feature;
- older material was resuspended from sediment;
- environmental conditions reduced later detection probability;
- a sample or analysis problem produced a spurious result;
- the public summary overstated a correctly reported laboratory finding;
- multiple subpopulations or seasonal routes produced an incomplete first map.

Sabotage is optional and should never be the default explanation.

## Reduced implementation

The reduced version can run with current world systems and ordinary audited combat primitives.

Use authored semantic events for:

- sample collection;
- sample custody transfer;
- laboratory result availability;
- explicit report delivery;
- public notice publication and later revision;
- repeat sampling;
- direct observation;
- feature-scoped access or monitoring decisions.

Represent sample/result facts as world evidence, not PTU statuses.

If combat occurs, keep it ordinary and incidental. A localized confrontation may delay access to a sample feature, but victory cannot prove the ecological source of the DNA or establish population size.

## Intended full version and engine dependencies

A richer field encounter may use a moving shoreline or stream edge, thick vegetation, rain, equipment protection, rescue/interception, a territorial wild Pokémon, timed sampling or an objective where harming the observed subject is counterproductive.

Permanent capability dependencies:

- targeting / footprints / range / LoS: special concealment, dense vegetation, spray, sensor-assisted acquisition;
- base movement legality: ordinary traversal only is safe today; specialized swimming/climbing/wading needs separate evidence;
- complete movement: rescue, interception, push/pull, forced displacement, current-driven movement;
- core calculations: ordinary verified deterministic combat math only;
- action economy / initiative: ordinary verified primitives only;
- full turn / round lifecycle: timed sampling windows, recurring rainfall/flow changes, delayed environmental events;
- full stateful damage pipeline: falls, current impact, debris or environmental damage;
- status lifecycle: any persistent exposure, entanglement or similar condition;
- terrain / weather / hazards / zones / reactions: water-edge hazards, rain, unstable banks, protected observation zones, reactive environmental effects;
- move-specific behavior: individually verify any Move used for sensing, terrain alteration, displacement, rescue or concealment;
- abilities: individually verify any Ability claimed to detect, hide, navigate or alter the environment;
- items: individually verify field gear if it participates in battle rules;
- Trainer Features / perks: individually verify Researcher or other Feature effects before tactical use;
- AI legal-action infrastructure: ordinary audited legal-action generation is usable;
- AI tactical policy: richer protect-subject, protect-equipment, retreat, rescue, observation or non-defeat objectives require policy support;
- Minecraft / Cobblemon / Craftics adapter/playback: may present authoritative state but may not infer occupancy from entity spawning or perform alternate scientific/tactical resolution.

## Canon boundary

This proposal does not select a species, region, settlement, institution, laboratory technology, ecological cause, final interpretation or PTU mechanic.

Any future canon binding should grow from approved Ouros geography and institutions, preserve sample provenance and keep ecological inference separate from Minecraft entity presence.
