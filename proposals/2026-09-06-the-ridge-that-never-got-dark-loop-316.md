# The Ridge That Never Got Dark — Pass 316

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

A ridge overlooking a managed habitat has long been used for nocturnal observations. After a nearby service corridor receives brighter overnight lighting, observers report that a recurring visual pattern has disappeared.

Secondary evidence says the local Pokémon may still be present. Tracks continue across the lower path. Feeding traces remain fresh. A worker occasionally sees silhouettes beyond the illuminated zone. The problem is therefore not `the Pokémon vanished`; it is `the expected nocturnal signal can no longer be established from the old observation routine`.

No location, species, institution or incident in this proposal is canon until explicitly adopted.

## Core mystery

The quest separates four questions:

1. Are the relevant Pokémon still present?
2. Is the expected visual signal still being produced?
3. Can observers detect that signal under the changed lightscape?
4. Has the animals' behavior, route or timing changed because of the new conditions?

Those questions can have different answers.

## Spatial structure

The investigation uses at least three viewpoints.

The traditional ridge station has a clear geometric view but strong glare from the new work lights. A shielded lower station blocks direct glare but sees a narrower slice of habitat. A remote dark-side station is farther from the service corridor and exposes another route or activity area.

The same habitat should look different from each position. Environmental evidence, not an NPC exposition dump, teaches the player why one viewpoint can be misleading.

## Candidate explanations

Canon review can select one or combine compatible causes:

- the signal continues but glare makes it difficult to detect from the old ridge;
- the population remains present but shifted its signaling window later into the night;
- some individuals avoid the illuminated corridor and use a darker route;
- some individuals are attracted toward the infrastructure while others avoid the immediate area;
- the visual pattern genuinely declined because the local population or social behavior changed;
- the historical baseline was weaker than observers remember;
- a new obstruction, haze, vegetation change or observer relocation creates a detection problem unrelated to animal behavior;
- lighting and another disturbance act concurrently.

Sabotage is unnecessary. An operator can have a legitimate safety reason for the lights and still create an ecological conflict.

## Quest progression

The player first verifies the old ridge report and records exactly what is seen. They then compare evidence from the shielded and dark-side stations at equivalent observation windows.

If the operator cooperates, the party can negotiate a limited test: shield one fixture, dim a section or turn a non-critical bank off during a defined observation period. A reappearing pattern supports a visibility/masking explanation. It does not prove that illumination has no behavioral effect. Conversely, movement returning to a dark corridor after the test may support a behavioral response without proving long-term population harm.

The player can then recommend an operational response: shielding, directional lighting, a dark interval, relocating an observation point, changing a route schedule, continuing monitoring, or escalating because stronger ecological evidence exists.

## Stakeholder roles

A field observer knows the historical pattern but may overvalue a familiar viewpoint. A maintenance or safety operator understands why the lighting exists and can explain which fixtures are critical. A worker has repeated local observations but no ecological model. A researcher can improve experimental discipline without knowing hidden world state. A route user benefits from safe illumination and can reasonably resist a blanket blackout.

Conflict comes from partial evidence and competing costs rather than assigned moral alignment.

## Environmental storytelling

The old ridge has field marks showing where observations were made before the lighting change. New poles or fixtures produce visible glare from that exact position. The lower shielded point feels darker but has poorer geometry. Tracks cross both lit and dark ground. A maintenance board establishes lighting schedules. Old observation records allow time-window comparison.

If the chosen species eventually has source-backed visual signaling, the player can compare signal geometry or timing. Until species canon is approved, the proposal should use generic authored `visual event observed/not observed` language.

## Full encounter version

The rich version places part of the investigation along an elevated service route where light and shadow change tactical geometry. A scheduled light-bank change can alter illuminated zones during a structured encounter. A frightened or displaced Pokémon may choose a darker route. A rescue or containment problem can overlap with moving equipment, uneven ground or a local electrical hazard.

This version must not assume that existing LoS automatically models darkness. Dynamic illumination is an additional zone/visibility contract.

Possible authored interactions include a verified light-producing Move changing local presentation, an Ability with exact verified semantics, an infrastructure light failure that changes route visibility, or a hazard telegraphed through visible electrical/arcing state. Each requires its specific capability family.

## Reduced implementation version

The reduced version requires no tactical light simulation.

World/narrative scene state uses authored descriptors such as `LIGHTS_ON`, `LIGHTS_REDUCED`, `LIGHTS_OFF`, `SIGNAL_DETECTED`, `SIGNAL_NOT_DETECTED` and `SECONDARY_PRESENCE_EVIDENCE`. These are scenario facts, not PTU statuses.

Lighting changes between scenes. Observation points have authored visibility outcomes backed by world state. There are no numerical darkness penalties, light radii, glare modifiers or night-vision rules. No Move creates an environmental effect unless separately verified. The route is represented with static open/blocked edges rather than dynamic shadow-dependent movement.

The complete mystery still works through revisitation, comparative observation, stakeholder negotiation and provenance-backed conclusions.

## Capability dependencies for the full version

Targeting/footprints/range/LoS: ordinary spatial targeting remains VERIFIED within audited contracts. Dynamic darkness, glare and illumination-dependent visibility are not included in that verification and must not be inferred from it.

Base movement legality: VERIFIED within audited contracts; sufficient for reduced navigation and ordinary tactical movement.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required only if panic movement, rescue interception, moving machinery or forced repositioning is authored.

Core calculations: VERIFIED within audited contracts. No illumination formula is introduced.

Action economy/initiative: VERIFIED within audited contracts for structured scenes.

Full turn/round lifecycle: PARTIAL. Required if light banks change at exact phase boundaries or delayed infrastructure events resolve during combat. AutoPTU-Java PR #385 adds declarative round-window history state but does not complete lifecycle timing.

Full stateful damage pipeline: PARTIAL. Required only for real electrical/environmental injury or ordinary combat damage consequences.

Status lifecycle: PARTIAL. The proposal invents no `blinded`, `dazzled`, `night-adapted` or similar persistent status.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily. Dynamic light/shadow fields, electrical hazards, moving safe areas or reaction rescues depend here.

Move-specific behavior: PARTIAL. Flash or any light-producing Move must use verified PTU/engine semantics before affecting exploration or encounter state.

Abilities: PARTIAL. Illuminate or another relevant Ability cannot gain ecological/tactical effects from flavor alone.

Items: PARTIAL. Narrative lamps/meters can remain world equipment; PTU Item mechanics require explicit validation.

Trainer Features/perks: PARTIAL. Any Feature modifying observation, visibility, interruption or night operation requires direct source validation.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING for general autonomy. Choosing shadow routes, exploiting illumination, rescue priorities or infrastructure controls cannot be assumed.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end. Rendering bright/dark blocks or client light does not make the client authoritative for tactical visibility or ecological state.

## PTU/Caelo questions before full implementation

Direct source validation is required before mapping this scenario to Perception/Survival, visibility penalties, light-producing Moves, Illuminate or other Abilities, Trainer Features, Items or species sensory capabilities.

No Caelo artificial-light or nocturnal-visibility overlay was located in the repository material inspected for Pass 316. Those mechanics remain `UNVERIFIED`.

## Canon questions before adoption

A canon pass must choose the geography and determine whether this belongs in an existing managed-development corridor or another region. It must select the affected species only after source-backed ecology is available. The responsible infrastructure, lighting purpose, historical observation baseline and stakeholder jurisdiction also need approval.

The scenario should remain valid if the final outcome is a modest operational mitigation rather than a villain reveal or battle.