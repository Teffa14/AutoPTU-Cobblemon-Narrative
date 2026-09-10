# The Room That Opened After the Team Left — Pass 393

Status: PROPOSED / NON-CANON.
Date: 2026-09-09

## Premise

A field team surveys a damaged research outpost after a local disruption.

They document the accessible rooms, report one sealed service corridor and leave because a shared field resource is reassigned to a higher-priority task elsewhere.

Later, physical conditions change and the sealed corridor becomes accessible. A second team enters and finds evidence that appears to contradict the first survey.

The contradiction is only apparent. The first team recorded the site they could actually access at that time. The second team sees a later physical revision and has access to a different resource state.

No liar, saboteur or supernatural explanation is required.

## Investigation structure

The site is divided into small evidence-bearing spaces instead of one combat gauntlet.

An entry room can establish the first team's presence and departure time.

A storage room can show that a field resource was present earlier but is currently assigned elsewhere.

A damaged operations room can contain an observation whose meaning changes only after later evidence is found.

The previously sealed corridor can expose another layer of the outpost without proving why it was sealed or what happened there.

A later-access room can contain enough information to explain one earlier decision while opening a larger unresolved question.

The player reconstructs sequence, access and knowledge rather than merely collecting a single master document.

## NPC and faction pressure

A field researcher may defend the original survey because they know exactly what was visible when they were there.

A logistics coordinator may appear responsible for the failed follow-up because the required resource was reassigned, even though the reassignment was authorized.

A second investigator may initially distrust the first report because the current building layout no longer matches it.

An institutional rival may exploit the discrepancy publicly without having enough evidence to prove misconduct.

Relationship consequences should follow observed accusations, cooperation, corrections and evidence-sharing events. Faction membership alone cannot synchronize private knowledge.

## Reduced playable version

The reduced version requires no AutoPTU battle.

It uses:

- semantic time;
- persistent site revisions and observations;
- private knowledge and inference lineage;
- explicit information delivery;
- current `WorldResource` state and resource-catalog recovery;
- travel/replanning;
- `OUROS_NPC_WORLD_CHECKPOINT_V19`;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2`;
- `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1`;
- `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V2` to select one coherent generation.

The player can solve the immediate contradiction by reconstructing which rooms were accessible, which evidence existed, who knew what and which resources were available at each point.

The larger mystery can remain unresolved.

## Rich encounter version

A mechanically rich version can place the second survey during unstable access conditions. The party may need to document evidence, keep an exit route usable, recover a portable resource or escort a specialist before conditions worsen.

The objective is safe evidence acquisition and exit. Defeating every opponent is optional unless an exact battle contract later requires it.

## Permanent capability dependencies

Targeting/footprints/range/LoS: needed if combatants, interactable consoles or evidence zones use tactical range/visibility. Use only verified audited scopes.

Base movement legality: needed for ordinary tactical navigation. VERIFIED only within audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: needed for collapsing passages, forced slides, dragging, rescue reposition or interception. PARTIAL.

Core calculations: needed for ordinary audited combat calculations if combat occurs. VERIFIED only within audited scopes.

Action economy/initiative: required if inspecting, securing, transferring or operating site objects consumes tactical actions. Existing primitives are VERIFIED only in audited scopes; objective interactions need their own contract.

Full turn/round lifecycle: required for timed closure, delayed collapse, phased evacuation or end-of-round access changes. PARTIAL.

Full stateful damage pipeline: required if damage changes persistent objective or resource state. PARTIAL.

Status lifecycle: required if lasting status effects alter access, carrying or timing. PARTIAL.

Terrain/weather/hazards/zones/reactions: required for unstable floor, flooding, smoke/dust visibility, electrical zones, triggered collapse or reaction hazards. MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated. Current Impostor evidence verifies only its tested seam.

Items: individually gated. Narrative field resources do not become PTU Items automatically.

Trainer Features/perks: individually gated, especially interrupts or objective interactions.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for investigation-first, protect-evidence, retrieve-resource, escort-specialist, split-team search, objective-aware withdrawal and disengage-after-objective until those exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for stable site/evidence identity, room-state projection, resource acknowledgement, objective state and authoritative non-KO completion playback.

## Full premise without rule duplication

If rich tactical dependencies remain incomplete, the same story stages the hazardous access transition outside AutoPTU. The player still chooses what to inspect, whom to trust, whether to wait for a resource, whether to share partial evidence and when to leave.

No adapter-side knockback, hazard, status, reaction or objective AI is invented to preserve spectacle.

## Canon questions deliberately left open

This proposal does not establish:

- the outpost's location;
- its owning institution;
- the cause of the disruption;
- the reason the service corridor was sealed;
- the nature or importance of the deeper evidence;
- any specific Pokémon species;
- legal access or extraction authority;
- a PTU Skill, Edge, Feature or Item effect;
- a regional conspiracy or villain.

All remain review decisions before canon promotion.
