# Global NPC AI readiness snapshot — Pass 323

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Narrative destination

Pass 323 adds winter mountain-route research, the proposed `The Pass That Looked Used` loop, and a reusable layered-snowpack/winter-route observation contract. All new world content remains NON-CANON unless separately approved through the repository's canon process.

The slice advances the current global NPC/world-agent direction by giving agents a new reusable evidence domain: route reports can be feature-scoped, time-bounded, stale after later events, and received by different actors without leaking hidden world state.

## Repository source boundary

Current narrative source inventory exposes `sources/kairos` only. No adopted `sources/caelo` directory was observed during Pass 323.

`sources/kairos/KAIROS_SOURCE_INDEX.md` routes movement/terrain to pp. 382+, status to pp. 397+, hazards to p. 401, and terrain/weather to pp. 404+ of the supplied Kairos compilation. The source manifest explicitly classifies Kairos as comparative evidence rather than Ouros law, and the index explicitly says it does not replace the source PDF.

Therefore Pass 323 does not promote any winter mechanic from Kairos and does not invent missing PTU/Caelo rules.

## Read-only engine evidence

### AutoPTU-Java

Observed main head: `2bb5ceaf21ab08d09a4048fec0f8498d24189142`
Commit: `Add Python-compatible round-start semantic event (#388)`
Observed commit date: 2026-09-07 UTC.

Live evidence includes a typed `round_start` battle event, preservation of authoritative initiative-entry snapshots, registration of the new semantic event kind, emission before round-start effects, language-neutral fixture export, differential testing against the pinned Python oracle, parity gating, and tests preserving ordered/stacked statuses inside the event payload.

The parity workflow in that commit pins Python oracle `16d228efa63aabecb67fa788959a359aac7f8f03` for its specific round-start fixture. The current AutoPTU main branch is newer than that pinned fixture commit, so the fixture pin and current Python head must not be silently treated as identical evidence.

This materially verifies a specific round-start semantic-event seam and ordering contract. It does not prove the complete turn/round lifecycle, arbitrary delayed environmental events, every status transition, reaction windows, dynamic terrain/weather scheduling, complete movement, or end-to-end Minecraft/Cobblemon/Craftics playback.

### AutoPTU Python

Observed main head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
Commit: `Career: keep battle coordinates synced after viewport resize (#237)`
Observed commit date: 2026-08-29 UTC.

The commit explicitly states that the change is presentation-only and changes no battle rules or outcomes. It provides no new evidence for winter mechanics or the capability families below.

Both engine repositories remain read-only for this workstream.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited ordinary contracts

Current evidence supports the ordinary audited targeting, footprint, range, and LoS contract. Pass 323 does not extend that verification to snowfall, whiteout, snow walls, drifting concealment, elevation-specific obscuration, glare, or other winter visibility changes.

Reduced version: supported without new targeting behavior.

Rich version: any visibility-changing snow/weather effect requires dedicated evidence.

### Base movement legality — VERIFIED within audited ordinary contracts

Ordinary movement legality remains available within the verified scope. No deep-snow cost, ice-footing rule, climbing privilege, sliding behavior, snowshoe-equivalent item effect, or species-specific winter traversal is inferred.

Reduced version: use ordinary open route edges or block unsupported spaces.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

A rich version involving moving snow/debris, forced slides, rescue pulls, interception, knockback near ledges, or environmental displacement depends on this family.

Reduced version: no forced movement.

### Core calculations — VERIFIED within audited deterministic contracts

No avalanche probability, stability score, snow-load equation, temperature model, exposure meter, or custom risk arithmetic is introduced.

### Action economy / initiative — VERIFIED within audited ordinary contracts

Ordinary action ordering remains available. This does not establish custom rescue actions, environmental interrupts, or snow-specific action costs.

### Full turn / round lifecycle — PARTIAL

PR #388 strengthens a specific seam by emitting a Python-compatible authoritative `round_start` event before round-start effects and checking parity/order through focused tests.

The family remains PARTIAL. The evidence does not prove all phases, end-of-round processing, arbitrary delayed events, reaction windows, dynamic environmental schedules, or every state transition.

A reduced winter route changes authored state between scenes. Timed snowfall, moving debris, delayed collapse, repeated hazard pulses, or refuge windows remain dependency-gated.

### Full stateful damage pipeline — PARTIAL

Pass 323 authors no environmental damage. Falls, collisions, crushing, cold, moving debris, or any other future winter damage must use verified authoritative damage handling rather than adapter-side shortcuts.

### Status lifecycle — PARTIAL

Pass 323 introduces no new PTU status. `OPEN`, `RESTRICTED`, `MONITORING`, `ROAD_CLEARED`, or `TRACKS_OBSERVED` are route/evidence descriptors, not combat conditions.

Any persistent cold, burial, restraint, visibility, movement, or other mechanical condition requires independent rule and lifecycle evidence.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

The reduced version needs no dynamic snow terrain or hazard zone. A rich version involving snow/ice terrain, active snowfall, moving hazard sectors, refuges, changing boundaries, weather phases, or rescue reactions depends on exact verified subfamilies.

Representative support for a terrain/hazard event elsewhere does not prove winter behavior.

### Move-specific behavior — PARTIAL

Every Move affecting ice, snow, wind, weather, terrain, visibility, movement, protection, rescue, or environmental damage must be checked individually. No representative Move closes the family.

### Abilities — PARTIAL

Official franchise material describes Avalugg and exposes videogame Ability text such as Ice Body, but franchise flavor is not an AutoPTU implementation contract. Ice Body and every other Ability remain individually gated.

### Items — PARTIAL

Pass 323 may use maintenance or rescue equipment as narrative objects. No item bonus, movement privilege, sensor function, protection, or rescue mechanic is inferred.

### Trainer Features / perks — PARTIAL

Kairos source indexing identifies utility classes including Survivalist, Topographer and Climatologist, but the index is not rule authority and Kairos is not automatically adopted. No Ouros Feature privilege, Skill modifier, inspection authority, prediction ability, or rescue interrupt is granted by this pass.

### AI legal-action infrastructure — VERIFIED within audited contracts

Existing infrastructure can enumerate supported legal actions. It cannot make unsupported winter movement, rescue, hazard manipulation, or specialist actions legal.

### AI tactical policy — BLOCKING for general autonomous winter-hazard reasoning

Current evidence does not establish general autonomous reasoning for changing snow zones, refuge selection, route-risk tradeoffs, rescue prioritization, evacuation, dynamic weather, or unsupported environmental actions.

World-agent NPCs may reason from explicit route/evidence state outside battle. Once a structured tactical scene begins, the existing AutoPTU ownership boundary still applies.

### Minecraft / Cobblemon / Craftics adapter/playback — PARTIAL / BLOCKING end-to-end

PR #388 strengthens the Java semantic-event side for a round-start event, but it does not prove complete playback for winter terrain, changing weather, forced movement, hazards, damage, statuses, or rescue.

Minecraft may display snow, tracks, barriers, debris, route markers, refuge geometry, and authoritative events after receiving state. Presentation must never decide route truth, PTU legality, damage, status, hidden ecological state, or NPC knowledge.

## Pass 323 implementation decision

`The Pass That Looked Used` is safe to advance in reduced form now because its core play is world investigation: persistent route features, timestamped observations, provenance, explicit NPC receipt, conflicting but potentially truthful reports, feature-scoped access decisions, semantic-time changes, and durable consequences.

The rich version is optional. It is blocked wherever its exact winter mechanic depends on partial or absent engine families. No missing PTU behavior should be recreated in the Minecraft/Cobblemon/Craftics adapter.

## New encounter dependency summary

Reduced version requires only already supported world-state/NPC systems plus ordinary verified route/movement contracts.

Rich-version additions require, depending on authored content:
- snowfall/whiteout visibility: additional targeting/LoS evidence;
- deep snow, ice, climbing or sliding: source-backed movement/terrain contracts;
- forced slide, push/pull, rescue/interception: complete movement;
- timed snowfall, delayed debris or changing refuge windows: full turn/round lifecycle;
- impact/fall/cold/debris damage: full stateful damage pipeline;
- any persistent mechanical condition: status lifecycle;
- snow/ice/weather/hazard/refuge zones and environmental reactions: terrain/weather/hazards/zones/reactions;
- each snow/weather/ice Move: move-specific behavior;
- each winter-related Ability: abilities;
- mechanical equipment: items;
- specialist inspection/navigation/rescue privileges: Trainer Features/perks;
- autonomous tactical winter behavior: AI tactical policy;
- authoritative visual playback: Minecraft/Cobblemon/Craftics adapter/playback.

## Unresolved PTU / Caelo questions

Before rich implementation, locate and verify the project-authoritative definitions for snow/ice terrain, difficult terrain if applicable, weather, visibility, climbing/jumping/falls, cold/environmental damage, rescue/interception, relevant Skills, relevant Trainer Features, relevant Moves, relevant Abilities, and relevant items.

No adopted Caelo source directory was visible in the narrative repository during this pass, so Caelo-specific winter overlays remain UNVERIFIED.

## Open canon questions

Region; mountain range; pass identity; nearby communities; climate; crossing type; route authority; economic/logistical importance; shelter and maintenance history; prior closures/incidents; resident Pokémon; whether Avalugg/Bergmite fit local ecology; seasonal water consequences; exact source and timing of the conflicting reports; whether uncertainty remains durable; and whether a future rich tactical version is desirable all remain unresolved.