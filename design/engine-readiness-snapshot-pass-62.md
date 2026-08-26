# Engine Readiness Snapshot — Pass 62

Status: implementation-facing evidence snapshot for narrative design. Not Ouros canon.
Date inspected: 2026-08-26

## Repositories inspected

- `Teffa14/AutoPTU-Java` — read-only
- `Teffa14/AutoPTU` — read-only source-oracle/runtime context
- `Teffa14/AutoPTU-Cobblemon-Narrative` — writable narrative destination

## Live evidence

Newest inspected AutoPTU-Java commit:

`55bdeb0cb9146054d4d80a0999bcd793275fe140` — Freeze canonical Chronicler profile metadata (#223).

Recent Java work also includes `149254ca0f54c6b8a35a25a57a7c872e50ce042e`, which ports one Focused Training Accuracy bonus resolver from authoritative runtime state.

These commits strengthen exact Trainer Feature/Accuracy slices. They do not establish the complete Trainer Features/perks family or any new environmental, movement, AI-policy or adapter capability.

The current Java README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- move/ability/item/perk/Trainer Feature hook registries;
- semantic transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Newest inspected Python AutoPTU commit:

`659950df573cd629e37a62d55780268dc5745972` — Career: harden battle quality hardware signals (#159).

The immediately preceding Python work rejects malformed battle hardware/quality signals. This is runtime robustness, not a new PTU combat family.

The earlier `57ee50adfaf1739e1f5d167ce530f1b1a072fe76` remains relevant narrative-boundary evidence: rivalry history is deliberately kept out of combat modifiers. Pass 62 applies the same boundary to memorial, absence and mourning state.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No Pass-62 evidence justifies a category promotion.

## Memorial and absence non-inference gates

Battle defeat is not death.

Fainting is not death.

An Injury is not automatically death.

An NPC missing from Minecraft spawn state is not death.

Retirement is not death.

Disappearance is not death.

A public death report is not canonical confirmation unless the world-state fact is separately validated.

A memorial marker proves that a memorial exists. It does not automatically prove every proposition on the inscription.

A surviving Pokémon's routine does not prove grief, ownership transfer, willingness to join another Trainer or supernatural connection.

Ghost-type Pokémon near a cemetery do not prove spirit identity.

A memorial practice does not create morale, Loyalty, Skill, Accuracy, Evasion, initiative, Feature or other combat modifiers.

A vacant role does not establish a successor.

Objects associated with an absent/deceased actor do not become loot or rewards through narrative convenience.

For retired PCs, the pre-existing retired-character authorship boundary remains authoritative. Automated generation cannot decide later death.

## PTU tone evidence

PTU campaign guidance explicitly treats permanent death as avoidable rather than a required consequence of defeat and advises groups to define campaign assumptions with the GM.

For Ouros implementation this means:

- death must be explicit world/canon state;
- tactical battle output cannot silently create it;
- loss can remain meaningful through injury, reputation, route state, institutional consequence, relationships, recovery, retreat or other validated systems without killing characters;
- any future death rules require a separate rules/canon decision rather than narrative inference.

## Encounter review — Marker-Ridge Evacuation

Narrative premise: weather or slope instability threatens access to a memorial ridge while visitors and stewards are present. Wild Pokémon may be displaced toward the safe approach.

Intended version may require:

- active civilian evacuation;
- changing safe routes;
- unstable terrain zones;
- weather effects;
- falling-debris hazards;
- forced movement near edges;
- protection/withdrawal objectives;
- objective-aware AI;
- synchronized Minecraft playback.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when displacement matters
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING for dynamic slope/weather effects
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Resolve visitor evacuation and route closure in world state before combat. Freeze one stable area outside fragile markers. Run only legal combatants and individually verified mechanics. The tactical result can determine the battle outcome only; it cannot authorize marker relocation, object transfer, memorial revision or historical interpretation.

## Encounter review — Boundary-Nest Disturbance

Narrative premise: wild Pokémon use vegetation along a memorial boundary. Some visitors attribute existing marker damage to them, while field evidence is incomplete.

Intended version may require:

- moving civilians;
- protected fragile zones;
- retreat/containment objectives;
- interception;
- forced movement;
- terrain-sensitive routing;
- objective-aware AI;
- persistent site playback.

Dependency state:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING when used
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain / weather / hazards / zones / reactions — BLOCKING when protected/dynamic terrain matters
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft / Cobblemon / Craftics adapter/playback — BLOCKING

Reduced version:

Close the affected boundary to visitors. Capture physical-condition observations before conflict. If battle occurs, move it to a static safe area away from fragile markers. Determine earlier damage and habitat cause from observations, maintenance records and ecology state rather than battle outcome.

## Noncombat readiness

The following Pass-62 structures can advance without additional tactical engine support:

- absence records with explicit state separation;
- canonical confirmed-loss references;
- memorial-site access and upkeep state;
- marker inscription provenance;
- marker revision history;
- remembrance participation events based on observable actions;
- unresolved object-custody handoffs;
- Pokémon continuity packets without ownership/emotion inference;
- role-continuity handoffs into staffing/governance systems;
- comparing public death reports with canonical facts;
- preserving a memorial created during a missing-person period after the actor returns;
- archival identity correction scenes.

These require world-state persistence and eventual Minecraft/UI representation, but not missing PTU tactical families.

## Adapter implications

Minecraft/Cobblemon should eventually render only knowledge the viewer is allowed to see.

Examples:

- a public marker can display its current inscription;
- a revision-history UI may show old text if the archive is accessible;
- an NPC may say someone is presumed dead while server canon remains unresolved;
- a returned actor can reappear without automatically deleting prior memorial objects;
- a Pokémon routine can be represented spatially without exposing hidden emotional labels;
- barriers and signage can show memorial access restrictions.

The adapter must not derive canonical death from entity absence or turn narrative memorial state into PTU modifiers.

## Pass-62 outcome

Memorial, absence and succession continuity can advance now as noncombat world-state design.

Mechanically rich memorial-site emergencies still need reduced static encounter versions until complete movement, terrain/weather/hazards/zones/reactions, tactical AI and Minecraft/Cobblemon/Craftics playback are verified.

Capability classifications remain unchanged from Pass 61.
