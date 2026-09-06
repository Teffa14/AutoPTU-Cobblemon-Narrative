# Olfactory observation and trace contract — Pass 317

Status: DESIGN CONTRACT / PROPOSED IMPLEMENTATION BOUNDARY
Date: 2026-09-06

## Purpose

This contract defines how Ouros may represent scent/chemical evidence without turning the world simulator, Minecraft client or generic Perception into omniscient tracking.

It does not add PTU rules. Exact Tracker, Odor Sleuth, Perception, Survival, Feature, Ability, Item and environmental semantics must come from project-authoritative sources.

## Required separation

An olfactory evidence implementation must preserve separate facts for:

1. source existence or authored source event;
2. trace production/deposition;
3. trace persistence or transfer;
4. environmental context affecting observation;
5. detector identity and verified sensory capability;
6. raw detection result;
7. tracking result, when PTU-authorized;
8. source/identity attribution;
9. interpretation claim and confidence;
10. communication of that conclusion to other actors.

A later interpretation must never overwrite the earlier raw observation.

## Provenance requirements

Every durable detection should identify the observer/detector, semantic time, observation location, source record or unknown-source token, sensory method, and any authored context that materially affects interpretation.

A conclusion such as `recent crossing by species X` must point back to the detections and corroborating evidence that support it. The system must be able to preserve a valid detection when the later causal interpretation is revised.

## Knowledge boundary

The world layer may know that an authored source deposited a trace. That hidden fact must not appear in an NPC ledger merely because the trace exists.

NPC knowledge requires observation, communication or another explicit provenance path. A Tracker-capable partner may produce an observation claim for its handler or other actors according to the communication contract; unrelated NPCs do not learn it automatically.

## PTU boundary

Public PTU 1.05 material establishes a Tracker Capability tied to smell and Perception-based pursuit and indicates that Odor Sleuth can grant Tracker. Before implementation, the project must resolve exact authority from its PTU/Caelo source tree.

The following are prohibited without direct validation:

- universal scent tracking through ordinary Perception;
- invented scent ranges or areas;
- numeric weather/terrain modifiers;
- automatic individual identification;
- scent-based targeting through walls;
- new persistent `scented`, `masked`, `nauseated` or similar statuses;
- new effects for Odor Sleuth, Abilities, Items or Trainer Features;
- inferred Caelo modifications reconstructed from memory.

## Environmental model boundary

A reduced world implementation may store authored trace observations and state transitions between scenes. It does not need a physical plume solver.

A full dynamic implementation would require a dedicated environmental contract for transport, decay, barriers, ventilation, weather and interaction with zones. That model must remain world/environment authority and must hand tactical effects to AutoPTU rather than calculating battle outcomes in the adapter.

## Cross-channel evidence

Olfactory conclusions should be able to coexist with and contradict visual, acoustic and physical-trace evidence. The evidence layer should support queries such as:

- scent detected, no fresh footprints;
- visual sighting, scent not detected;
- old trace present, recent feeding evidence elsewhere;
- two detectors disagree because their capabilities differ;
- trace identity revised after a contamination source is discovered.

Contradiction is evidence for investigation, not an automatic data error.

## Minecraft/Cobblemon/Craftics boundary

Client particles, sound, block state and lighting are presentation unless an explicit server-authoritative adapter maps them from Ouros state.

A rendered scent trail must be a view of an authoritative trace/observation record. Player proximity to a particle cannot itself create a PTU tracking success. Cobblemon species data may inform presentation and entity identity but cannot replace Ouros provenance or AutoPTU legality.

## Capability dependencies

Targeting/footprints/range/LoS: current ordinary spatial contract is VERIFIED. Olfactory targeting or detection geometry remains outside scope.

Base movement legality: VERIFIED for ordinary movement.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL; unrelated to basic trace observation unless a rich encounter adds rescue/forced motion.

Core calculations: VERIFIED; no new chemical/scent calculation is authorized here.

Action economy/initiative: VERIFIED for structured tactical actions.

Full turn/round lifecycle: PARTIAL; required for within-round environmental evolution or delayed trace/ventilation changes.

Full stateful damage pipeline: PARTIAL; not required by base olfactory evidence.

Status lifecycle: PARTIAL; no new scent condition is authorized.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING. Required for dynamic scent fields, environmental masking and reactive hazard behavior.

Move-specific behavior: PARTIAL; Tracker-granting or scent-related Moves require exact verification.

Abilities: PARTIAL; no flavor-derived olfactory effects.

Items: PARTIAL; PTU mechanical items require validation, while ordinary world sample containers may remain non-combat props.

Trainer Features/perks: PARTIAL; direct source validation required.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING for autonomous general scent reasoning or tactical exploitation.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

## Engine evidence inspected

AutoPTU-Java head: `704722ffecbef9e003abe1870829843f29f029c7` / PR #385. It adds declarative server-core state for selected round-indexed histories and parity tests against the pinned Python oracle. That supports a narrow lifecycle/history seam only.

AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The current head remains presentation-only for the purposes of this audit.

No capability family is promoted by Pass 317.

## Reduced implementation contract

A first implementation may use immutable observation records with authored values such as `TRACE_PRESENT`, `TRACE_NOT_DETECTED`, `TRACE_CONTAMINATED`, `SOURCE_UNRESOLVED` and `TRACKING_ATTEMPT_RECORDED`.

Those are narrative/world evidence descriptors, not PTU status conditions. They should integrate with existing provenance and NPC knowledge infrastructure and survive world persistence if adopted into executable state.

## Acceptance criteria for a later executable slice

A future implementation should prove at minimum that:

- two NPCs can hold different scent-related knowledge without hidden-state leakage;
- a valid detection can survive a later attribution revision;
- a transferred/contaminated trace can be distinguished from the hypothesized source movement;
- a non-Tracker actor cannot invoke Tracker-only semantics;
- restart preserves observation provenance if the system becomes persistent;
- the adapter cannot manufacture detection by client presentation alone;
- exact PTU/Caelo authority is cited beside any numeric or mechanically consequential rule.