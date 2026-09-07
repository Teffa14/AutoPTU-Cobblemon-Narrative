# Reclaimed extraction landscape contract — Pass 319

Status: DESIGN CONTRACT / PROPOSED INFRASTRUCTURE / NON-CANON CONTENT

Date: 2026-09-06

## Purpose

This contract defines how Ouros may represent a former quarry, mine, borrow pit, spoil field, or similar extraction landscape without turning narrative observations into hidden-world omniscience and without implementing missing PTU rules in Minecraft/Cobblemon adapters.

## Authority layers

The system must keep these layers separate:

1. Physical world feature state.
2. Observation made about that feature.
3. Source/provenance of the observation.
4. Actor knowledge derived from observations actually received.
5. Interpretation or hypothesis.
6. Institutional decision.
7. Consequence applied to a specific world feature.
8. Minecraft/Cobblemon presentation of authoritative state.

A visible crack does not automatically mean a slope is mechanically unstable. A sealed opening does not prove an underground route cannot exist. A Pokémon using a reclaimed bench does not prove the entire site is safe. A remediation record does not certify features outside its scope.

## Feature identity

Persistent extraction landscapes should use stable feature identities rather than one global `QUARRY_STATE`.

Examples:
- haul road segment;
- upper highwall sector;
- reclaimed bench;
- spoil slope;
- drainage cut;
- culvert;
- monitoring station;
- sealed service opening;
- wetland/seep;
- public trail;
- retaining work.

Each feature can change independently through authored world events and consequence-repair adapters.

## Historical phase provenance

Evidence should retain the historical phase it is believed to belong to when known:
- EXTRACTION;
- SHUTDOWN;
- EMERGENCY_STABILIZATION;
- RECLAMATION;
- ECOLOGICAL_SUCCESSION;
- COMMUNITY_REUSE;
- RECENT_DISTURBANCE;
- UNKNOWN.

These are provenance descriptors, not PTU conditions. Unknown phase must remain valid when the evidence cannot establish chronology.

## Observation record minimum

A future typed observation runtime should preserve at least:
- observation id;
- feature id;
- observer id;
- semantic time;
- location/viewpoint;
- channel/source, such as visual inspection, map, instrument, testimony, Pokémon behavior, water sample, or maintenance record;
- raw authored observation or source-backed result;
- confidence/uncertainty if the source defines it;
- referenced historical phase if known;
- provenance root;
- interpretation claim id separately when an actor draws a conclusion.

The runtime must not infer responsibility, cause, safety, toxicity, age, or species identity merely because an observation exists.

## Safety and access decisions

Access decisions must target explicit features or route edges. `RESTRICT upper_spoil_path` must not close the entire location unless authored scope explicitly includes every relevant feature.

Reclamation or repair likewise applies to explicit consequences. Stabilizing a highwall does not automatically restore reputation, reopen a drainage gallery, change a wetland, remove an old notice, or alter unrelated NPC beliefs.

This contract should reuse the existing decision dependency, decision review, selective consequence repair, and checkpoint lineage rather than invent a parallel remediation authority system.

## Ecology boundary

Secondary habitat can arise in a disturbed landscape. That ecological use is world evidence, not proof that an industrial feature is desirable or safe.

Species observations require source-backed behavior before they are interpreted. Official franchise flavor may justify a candidate species for narrative ecology, but PTU mechanics, traversal capability, immunity, Move behavior, Ability behavior, and encounter legality must be verified separately.

## Reduced implementation contract

Until richer terrain/hazard support is verified, use:
- normal authoritative route graph;
- feature-scoped OPEN/CLOSED/RESTRICTED world state;
- static or between-scene observation changes;
- deterministic rockfall/drainage events outside tactical timing;
- authored evidence records with provenance;
- feature-scoped decisions and consequences;
- ordinary verified movement on open edges;
- no invented status, environmental damage, forced movement, reaction, fall, current, or terrain-cost rule.

The narrative premise must remain solvable through cross-checking evidence and making feature-level decisions.

## Full implementation dependency boundary

Dynamic loose ground, slides, knockback near drops, falling displacement, rescue/interception, or water current require complete movement including push/pull/knockback/interception/forced movement.

Timed collapse, delayed debris, round-phased drainage, weather escalation, or scheduled machinery effects require full turn/round lifecycle. AutoPTU-Java's current generic round-start seam is representative evidence only and does not authorize the whole family.

Rockfall, fall, crushing, impact, drowning, chemical, or environmental damage require the full stateful damage pipeline.

Persistent mechanical conditions require status lifecycle.

Scree fields, unstable ledges, dynamic water, hazard zones, weather-driven changes, and rescue reactions require the exact terrain/weather/hazards/zones/reactions subfamilies.

Every authored Move, Ability, Item, and Trainer Feature/perk must be individually verified against current PTU/engine contracts.

Autonomous NPC/Pokémon tactical behavior in a changing hazard field requires AI legal-action infrastructure for legality and AI tactical policy for selection; current generalized tactical policy remains blocking.

Minecraft/Cobblemon/Craftics may display block changes, water, particles, entities, sounds, barriers, and pathing consequences only as playback of authoritative state. Adapter logic must not independently decide collapse success, forced movement, damage, statuses, legality, or PTU outcomes.

## Canon and source boundary

This contract creates no quarry, mine, geology, pollution event, organization, settlement, Pokémon population, or reclamation program in canon.

Current repository inspection exposes `sources/kairos` and did not locate an adopted `sources/caelo` quarry/reclamation overlay. Numeric PTU/Caelo behavior remains unverified until a project-authoritative source is identified and cited.

Research provenance belongs in `research/`; authored candidates belong in `proposals/`; only approved material may later cross into canon through the repository's existing canon process.
