# Sendero multi-solution traversal seeds — pass 217

Status: PROPOSED / NON-CANON
Date: 2026-09-03

## Canon boundaries

This proposal reuses the established Sendero del Vidrio seasonal crossing and existing Marea responsibilities. It does not canonize a permanent bridge collapse, landslide, flood, new structure, new Pokémon population, new NPC or new cause for any previous incident.

The physical obstruction used below is an authored scenario candidate. Its exact cause, material and duration remain unset until canon review. Existing incident/access records should be reused if the final version is linked to a prior event rather than silently rewritten.

## Premise

A route obstacle should ask what the party can observe and accomplish, then preserve the difference between getting one person across and making the crossing usable again for everyone.

Sendero is suited to this because the seasonal crossing already matters to field observation and movement. Mara can care about safe access; Lia can care about route continuity; Nerea can care about evidence and ecological disturbance; Teo can care about whether a fixture or surface is actually stable. Their mandates produce consequences without requiring any of them to become an antagonist.

## Seed: The Crossing Has More Than One Answer

A temporary obstruction makes the normal cart-width line through the seasonal crossing unavailable. The authored scene exposes physical facts rather than a UI key requirement.

Possible player responses can include surveying the condition, using an alternate legal route, waiting for an authorized transition, documenting the blockage, reporting it, personally bypassing it with a verified Trainer/Pokémon capability, or attempting a mechanically authorized stabilization/clearance method.

No option is granted merely because it sounds plausible. If a player proposes climbing, lifting, flying, swimming, cutting, pushing, burning, freezing, tunnelling, teleporting or another special method, the game checks the actual actor, world preconditions and exact PTU/Caelo/Kairos authority before resolving it.

The important narrative consequence is retained even when the party has a clever bypass: who can use the route after them?

## Seed: A Shortcut Is Not a Reopening

A Trainer reaches the far side using a capability unavailable to ordinary travelers. That can be a complete success for the Trainer's immediate objective while the route remains restricted.

Lia still cannot treat the path as an open delivery line. Mara cannot remove a public restriction because one capable person crossed. A later NPC without the same movement option should encounter the same authoritative obstruction unless someone actually changes its state.

This creates a persistent distinction among:

- actor-specific access;
- group access;
- emergency access;
- public route reopening.

The exact categories can be normalized later if the route/access layer already has preferred terminology.

## Seed: Move the Debris, Lose the Clue

Before clearance, Nerea or Ema notices that the obstruction also preserves potentially useful traces: compressed material, displaced vegetation, footprints, nesting material, water marks, tool marks or another observation whose exact nature is authored later.

The player can document first, preserve part of the area, ask for a specialist review, choose a less destructive solution or clear immediately and accept that some evidence may become unrecoverable.

This does not turn every pile of debris into a mystery. `NO_USEFUL_EVIDENCE_FOUND` remains a valid outcome when the inspection is performed correctly.

The scene also supports wild-welfare consequences. A physical solution that removes shelter or blocks an escape line can change later behavior context only when the affected population/individual is authoritatively present and the behavioral model supports the consequence.

## Seed: Who Gets the Route Back?

Different Marea actors can agree that the obstacle should be addressed while disagreeing about the completion criterion.

Mara may require safe passage. Lia may need a width/load standard sufficient for deliveries. Teo may require a damaged fixture to be stabilized rather than merely avoided. Nerea may ask that measurements or traces be recorded before disturbance.

A player can therefore produce partial successes that remain meaningful: safe foot passage, documented evidence, temporary one-way access, completed stabilization or full public reopening. One success does not silently imply the others.

## Seed: The Pokémon Can Help, But How?

This seed exists to use Pokémon as world participants without inventing HM equivalents.

When a Trainer proposes Pokémon assistance, the resolver inspects the exact individual. Relevant evidence might include movement capabilities, size/weight, Skills, Moves, Abilities, Features/Edges or other verified PTU properties. Species appearance alone supplies no authority.

A Pokémon able to fly a Trainer over a gap may solve transport without moving the obstacle. A Pokémon with a legally applicable movement capability may take an alternate route. A Move capable of changing terrain or an object must have its exact behavior verified before the world mutates. Cooperative work can be valid when every contributing action and the combined result have an explicit contract.

The Trainer's own Athletics, Acrobatics, Survival or applicable Feature/Edge can matter independently when source-verified.

## Mechanically rich encounter: Seasonal Crossing Clearance Window

Working title only.

### Intended full version

The crossing is temporarily obstructed while several legitimate objectives compete for time and space. The party can inspect, preserve evidence, establish a safe lane, personally traverse, assist another actor, stabilize the obstruction or attempt full clearance.

The full version can support:

- authoritative obstacle geometry and site state;
- footprints/range/LoS for inspection and spatial interaction;
- base movement around reachable surfaces;
- verified jump/climb/swim/fly or other movement capabilities;
- Trainer Skill checks with exact source-backed modifiers;
- Pokémon Moves/Abilities/Items/Features whose environmental effect has an audited contract;
- cooperative actions where mechanically supported;
- push/pull/knockback/forced movement only if an actual entity/object interaction uses those semantics and the engine contract covers it;
- tile-entry hazards only where the specific hazard is authored and matches a verified engine contract;
- damage/status only when a real failure/consequence invokes those pipelines;
- semantic world-transition events for Minecraft/Cobblemon/Craftics playback;
- autonomous helpers only when AI legal-action and tactical-policy support is sufficient for their role.

The obstacle result is separate from battle results. Defeating a wild Pokémon does not clear the route. Crossing the route does not prove it structurally safe. Breaking a visible Minecraft block does not authorize a clearance outcome.

### Reduced version: Survey, Choose, Traverse

The reduced version preserves the premise without depending on unfinished environmental mechanics.

The server holds an authored obstacle state. The player can inspect it, record evidence, choose an already-authored detour, wait for an explicit world transition, report the condition, withdraw or use ordinary movement that is already legal in the world. If a simple actor-specific traversal capability is fully verified, it may be enabled independently without implying route restoration.

The reduced form deliberately avoids:

- arbitrary Strength-equivalent checks;
- unverified lifting/pushing object mechanics;
- fake difficult terrain;
- collapse or falling damage invented by Minecraft collision;
- unverified Field-Move/HM equivalents;
- automatic route reopening after one actor bypasses the obstacle;
- off-screen clearance by simulated AI;
- block destruction as rules authority.

A later implementation can enrich the same obstacle by registering additional verified solution methods. The narrative premise does not have to be rewritten when the engine gains capability.

## Engine capability dependencies

| Permanent capability family | Need in full version | Pass-217 boundary |
| --- | --- | --- |
| targeting / footprints / range / LoS | Required for spatial inspection and interaction | VERIFIED inside audited contracts; specific world-object targeting still needs adapter/world contract |
| base movement legality | Required | VERIFIED inside audited contracts |
| complete movement incl. push/pull/knockback/interception/forced movement | Conditional for displacement/containment methods | PARTIAL; do not use bounded forced-movement prevention as family completion |
| core calculations | Required for verified Skill/mechanical checks | VERIFIED inside audited contracts; each new Skill use still needs source validation |
| action economy / initiative | Conditional when clearance becomes structured/timed | VERIFIED inside audited contracts |
| full turn/round lifecycle | Conditional for fully structured scenes | PARTIAL |
| full stateful damage pipeline | Conditional for actual damage/falls/attacks | PARTIAL |
| status lifecycle | Conditional | PARTIAL |
| terrain/weather/hazards/zones/reactions | Conditional for dangerous terrain, tile traps, zones or reactions | PARTIAL/BLOCKING for the rich family; #329 verifies a bounded generic tile-entry trap path, not the family |
| move-specific behavior | Required for Move-based environmental solutions | PARTIAL |
| abilities | Required for Ability-based solutions | PARTIAL |
| items | Required for mechanically meaningful tools/items | PARTIAL |
| Trainer Features/perks | Required for Feature/Edge modifications/substitutions | PARTIAL |
| AI legal-action infrastructure | Required for autonomous mechanical helpers | VERIFIED inside audited contracts |
| AI tactical policy | Required only for autonomous prioritization in rich timed scenes | BLOCKING as a complete policy |
| Minecraft/Cobblemon/Craftics adapter/playback | Required for obstacle projection, authorized mutation and animation | PARTIAL/BLOCKING end-to-end |

## World-runtime contract

The obstacle also needs persistent world authority outside the 16 permanent battle families. This should remain a world/adapter concern rather than become a new battle category.

The runtime must preserve obstacle identity and state across unload/reload, ensure multiplayer players see the same authoritative transition, separate actor-specific traversal from public accessibility, associate destructive transitions with evidence consequences, and support rollback/reconciliation if presentation fails after authority has already resolved the change.

Where Minecraft/Cobblemon already provides native traversal or world capabilities that match the desired presentation, Ouros should reuse them. Native presentation still cannot manufacture a PTU mechanical success.

## PTU/Caelo/Kairos audit queue

Before full mechanical approval, locate and freeze exact project-source authority for Athletics and Acrobatics traversal checks; Survival/terrain interaction where relevant; Pokémon movement capabilities such as Overland/Sky/Swim/Jump and any special traversal capabilities; lifting/carrying/pushing environmental loads; Naturewalk/terrain Features; Feature/Edge substitutions or bonuses; environmental Move use outside combat; Ability-based traversal; cooperative checks; falling/collision consequences; and Caelo/Kairos overrides.

Do not infer those rules from the Ranger sources. Ranger is narrative/game-design provenance only.

## Longer-term arc potential

Once the obstacle contract exists, the same architecture can support washed-out paths, damaged stairs, cave gaps, locked maintenance routes, overgrown service paths, unstable ruins, temporary construction, wildlife-sensitive detours and dungeon loops without creating a separate quest scripting language for each one.

A route that changes after player intervention can also alter future deliveries, NPC schedules, fieldwork access and wildlife pressure. Those consequences should refer to the persistent obstacle transition rather than re-deciding history every time the chunk loads.

## Open canon questions

The pass does not decide what physically obstructs the seasonal crossing, whether the event is common or exceptional, who has final authority to reopen it, which public-access standards Marea uses, whether the first implementation permits Pokémon-assisted clearance, or which exact PTU/Caelo/Kairos mechanics qualify as world-interaction methods.