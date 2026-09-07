# Global NPC AI readiness snapshot — Pass 324

Status: LIVE EVIDENCE SNAPSHOT
Date: 2026-09-07

## Narrative destination

Pass 324 adds intertidal/tidal-window research, the proposed `The Staircase the Sea Borrowed` loop, and a reusable intertidal observation contract. All new world content remains NON-CANON unless separately promoted through `canon/`.

The slice advances the current global NPC/world-agent focus by adding a reusable temporal-access domain where route state, observation validity and public information can change at different times without hidden-state leakage.

## Repository source boundary

The recursive narrative repository inventory was inspected before authoring. No dedicated prior tide/intertidal/tidepool workstream was found. Existing recent environmental work already covered hydraulic works, floodplains, snowpack and several environmental-observation channels, so Pass 324 avoids duplicating those domains.

Current source inventory exposes `sources/kairos/KAIROS_SOURCE_INDEX.md`. It routes movement/terrain to pp. 382+, hazards to p. 401, terrain/weather to pp. 404+, Fishing to p. 368 and broader world/encounter guidance later in the supplied compilation. The index explicitly states that it is a routing aid and that Kairos is comparative evidence rather than automatic Ouros law.

No adopted `sources/caelo` directory was visible during the inspected recursive tree. Caelo-specific coastal mechanics therefore remain UNVERIFIED.

## Read-only engine evidence

### AutoPTU-Java

Observed main head: `73cdc14df32fd14825cbbf16c6b603b73bc46486`
Commit: `Freeze round-start Trainer Feature dispatch contract (#389)`
Observed commit date: 2026-09-07 UTC.

PR #389 is merged. It freezes a Python-compatible round-start Trainer Feature dispatcher boundary. Focused evidence includes:
- trigger `round_start`;
- payload containing the current round;
- no actor or target arguments in that dispatch contract;
- ordering `round_start semantic event -> Trainer Feature dispatch -> Air Lock` in the pinned oracle fixture;
- a typed Java contract;
- an oracle differential test;
- a dedicated parity workflow.

The PR body explicitly states that concrete Trainer Feature effect parity is not established yet. The Java commit therefore strengthens one round-start dispatch seam and one Trainer Feature invocation contract. It does not prove complete Trainer Feature coverage, the complete turn/round lifecycle, arbitrary environmental scheduling, dynamic water, reactions, movement, damage, statuses or end-to-end adapter playback.

The workflow pins Python oracle `16d228efa63aabecb67fa788959a359aac7f8f03` for this specific parity fixture. That fixture pin remains distinct from current AutoPTU Python main.

### AutoPTU Python

Observed main head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
Commit: `Career: keep battle coordinates synced after viewport resize (#237)`
Observed commit date: 2026-08-29 UTC.

The commit explicitly describes itself as presentation-only and states that no battle rules or outcomes change. It adds no new coastal, tide, water, movement or hazard evidence.

Both engine repositories remain read-only for this workstream.

## Permanent capability categories

### Targeting / footprints / range / LoS — VERIFIED within audited ordinary contracts

The ordinary audited contract remains verified. Pass 324 does not extend that verification to underwater vision, water-surface distortion, spray/fog concealment, wave occlusion, changing water cover or other coastal visibility behavior.

Reduced version: supported on ordinary exposed authored spaces.

Rich version: specialized water/visibility behavior requires dedicated evidence.

### Base movement legality — VERIFIED within audited ordinary contracts

Ordinary movement remains available on authored open route surfaces. Pass 324 does not infer Swim, wading costs, slippery footing, wet-rock climbing, gap jumping, aquatic traversal or species-specific movement privileges.

Reduced version: block unsupported route edges when submerged or otherwise unavailable.

### Complete movement including push/pull/knockback/interception/forced movement — PARTIAL

Currents, wave displacement, rescue pulls, interception, forced movement near water or knockback into/out of water depend on this family.

Reduced version: no forced movement.

### Core calculations — VERIFIED within audited deterministic contracts

No tide equation, buoyancy model, drowning meter, current-force calculation, pressure formula or environmental risk score is introduced.

### Action economy / initiative — VERIFIED within audited ordinary contracts

Ordinary action ordering remains usable. Custom rescue actions, environmental interrupts, braces, water-control interactions or tide-specific action costs require exact contracts.

### Full turn / round lifecycle — PARTIAL

PR #389 strengthens the round-start seam by freezing Trainer Feature dispatch ordering relative to the semantic round-start event and an Air Lock check in the pinned Python oracle.

The family remains PARTIAL. This does not prove end-of-round handling, every phase, arbitrary delayed events, repeated environmental pulses, reaction windows or general scheduled terrain/weather changes.

A reduced tidal site changes authored phase between structured encounters or through explicit world events. Within-battle waterline changes remain dependency-gated.

### Full stateful damage pipeline — PARTIAL

Pass 324 authors no environmental damage. Any future fall, collision, crushing-water, submersion or other environmental damage must use the authoritative pipeline rather than adapter-side shortcuts.

### Status lifecycle — PARTIAL

`TIDE_HIGH`, `LOWER_ROUTE_SUBMERGED`, `WINDOWED_ACCESS` and similar Pass 324 values are world-state descriptors, not PTU statuses.

Any persistent mechanical condition requires independent rules and lifecycle evidence.

### Terrain / weather / hazards / zones / reactions — MIXED / PARTIAL / BLOCKING by subfamily

The reduced version needs no dynamic water terrain. A rich version involving changing water coverage, currents, waves, slippery sectors, rescue windows, environmental reaction zones or tide-dependent safe geometry depends on exact verified subfamilies.

Representative support elsewhere does not establish intertidal behavior.

### Move-specific behavior — PARTIAL

Every Move used for water manipulation, terrain change, movement, concealment, weather, rescue or environmental damage must be verified individually.

### Abilities — PARTIAL

Official species material can inform ecological candidates, but franchise flavor and main-series Ability text are not AutoPTU implementation contracts. Every Ability remains individually gated.

### Items — PARTIAL

Ropes, markers, survey tools, flotation devices, boots or rescue equipment may exist as narrative objects. Mechanical effects require verified item contracts.

### Trainer Features / perks — PARTIAL

PR #389 verifies a specific round-start Trainer Feature dispatcher invocation/order contract. Its own scope explicitly does not establish concrete Trainer Feature effect parity.

Therefore the category remains PARTIAL. Survivalist, Topographer, Climatologist, Researcher or any coastal/navigation/rescue privilege must be checked individually against project-authoritative rules and implementation.

### AI legal-action infrastructure — VERIFIED within audited contracts

Existing infrastructure may enumerate already supported legal actions. It cannot create swimming, rescue, current resistance, water-terrain manipulation or specialist coastal actions that the rules engine does not support.

### AI tactical policy — BLOCKING for general autonomous dynamic-coast reasoning

Current evidence does not establish general autonomous tactical reasoning for changing water coverage, evacuation, refuge selection, rescue prioritization, current avoidance, window timing or unsupported environmental actions.

World-agent NPCs may still reason outside battle from explicit route/tide/evidence state. Structured tactical ownership remains with AutoPTU.

### Minecraft / Cobblemon / Craftics adapter/playback — PARTIAL / BLOCKING end-to-end

PR #389 improves one Java round-start dispatch contract but does not prove tidal geometry playback, dynamic water, forced movement, hazards, damage, status, rescue or complete encounter synchronization.

Minecraft may display authoritative waterline state, exposed geometry, route markers and semantic events. It must never decide tide truth, route legality, PTU movement, damage, statuses, hidden world state or NPC knowledge.

## Pass 324 implementation decision

`The Staircase the Sea Borrowed` is safe to advance in reduced form now.

Its core gameplay uses:
- persistent feature identity;
- authored tide phases;
- feature-scoped route state;
- semantic time;
- timestamped observations;
- explicit NPC receipt;
- potentially truthful but temporally incompatible reports;
- publication revision;
- route replanning;
- durable consequences;
- revisits under another phase.

None of those require dynamic water mechanics inside AutoPTU.

## Rich-version dependency summary

Depending on final authoring, a rich version requires:
- underwater/spray/occluded visibility: additional targeting/LoS evidence;
- wading, swimming, wet-rock climbing or aquatic traversal: source-backed movement contracts;
- currents, wave push/pull, rescue/interception and forced displacement: complete movement;
- timed waterline changes or repeating environmental events: full turn/round lifecycle;
- fall, impact, submersion or environmental damage: full stateful damage pipeline;
- persistent mechanical conditions: status lifecycle;
- changing water terrain, currents, wave sectors, safe zones and rescue reactions: terrain/weather/hazards/zones/reactions;
- each environmental Move: move-specific behavior;
- each aquatic/environmental Ability: abilities;
- mechanical coastal gear: items;
- specialist navigation/research/rescue privileges: Trainer Features/perks;
- autonomous tactical coastal behavior: AI tactical policy;
- authoritative audiovisual/state playback: Minecraft/Cobblemon/Craftics adapter/playback.

## Unresolved PTU / Caelo questions

Before rich implementation, locate and verify the project-authoritative definitions for Swim or aquatic movement, wading if present, water terrain, currents, underwater visibility/targeting, slippery surfaces, climbing/jumping near water, falls, environmental damage, drowning/submersion if present, rescue/interception, Fishing, relevant Skills, relevant Trainer Features, relevant Moves, relevant Abilities and relevant items.

The visible narrative source registry does not currently expose an adopted Caelo directory, so Caelo-specific coastal overlays remain UNVERIFIED.

## Open canon questions

Region; coast type; settlement; route identity; tidal regime; route authority; service/landing purpose; economic dependency; ecological significance; resident Pokémon; whether Wiglett or another coastal species fits local ecology; historical route construction; public-access policy; source and timing of the conflicting reports; long-term maintenance; and whether a rich tactical version is desirable all remain unresolved.