# Marea managed development zone and conflict-pressure seeds — pass 223

Status: PROPOSED / NON-CANON
Date: 2026-09-03
Depends on: `design/ecosystem-conflict-pressure-and-strength-v1.md`

## Purpose

Exercise a world where frequent battles can change wild populations while authorities actively maintain some routes as suitable places for children and inexperienced Trainers to develop.

No seed below canonizes a specific route as Marea's starter zone, assigns new legal powers to an existing NPC, defines a species predator/prey relation, or creates a universal Level cap.

## Seed: The Route Is Getting Too Good at Fighting

A heavily used training corridor has accumulated a large number of legitimate Trainer-vs-wild battles over several ecological windows.

Survey and battle records suggest that the commonly encountered wild population now contains more individuals that are confident, experienced around Trainers, or otherwise harder to handle than historical observations predicted.

The first interpretation is not automatically “their Levels increased”. The field team separates:

- actual PTU mechanical evidence from witnessed battles;
- conflict exposure;
- approach/avoidance behavior;
- capture history;
- changes in age/stage composition;
- immigration of stronger individuals;
- survivor-selection effects.

If the upper risk tail exceeds development-zone policy, authorities can adjust patrols, access, habitat use, or individual management while leaving ordinary battle opportunities intact.

## Seed: The Strong One Wasn't Spawned

A dangerous wild individual appears near a beginner-heavy route.

The server must be able to explain its membership history. Possible explanations include migration, normal movement from another patch, maturation plus independently verified progression, prior survival history, release, or an authored persistent actor.

It is not created by a “rare high-level spawn roll”.

Its presence generates evidence and response:

```text
sighting -> corroboration -> risk assessment -> advisory/patrol -> intervention or natural departure -> population ledger update
```

If it moves elsewhere, it remains the same actor.

## Seed: Children’s Route, Adult Problem

A large or behaviorally dangerous adult moves into a route commonly used by young/new Trainers.

The conflict is institutional before it is tactical. Adults responsible for route safety need to decide whether to warn, supervise, close a segment, wait for natural movement, deter the animal, capture it, or relocate it.

This provides a reason that starter areas remain generally safe despite belonging to a real 1:1 ecosystem.

### Knowledge boundary

NPCs may disagree about the cause:

- one thinks heavy training traffic made the local population bolder;
- another thinks the adult immigrated from a quieter patch;
- another suspects food or another species displaced it.

The ledger retains the real history. Dialogue uses only available evidence.

## Seed: The Quiet Patch Is Not Safer

A familiar prey-sized population becomes less visible in one patch.

A naive interpretation is that the area is empty and therefore safe.

Later evidence can show increased avoidance, changed timing, displacement, or predator pressure. The underlying total may have changed a lot, a little, or not at all.

This makes absence an ecological signal rather than a spawn failure.

## Seed: Marks Without a Witness

Players find fresh disturbed ground, damaged vegetation, tracks, displaced feeding activity, and one abandoned use site after the server's off-screen ecological window.

No hidden battle replay exists.

NPCs can construct hypotheses from the traces. The evidence might fit territorial conflict, predation, human disturbance, or a larger Pokémon simply moving through.

If later observation resolves the cause, the earlier reports remain historically accurate as uncertain reports rather than being rewritten as omniscient knowledge.

## Seed: Capture Pressure Changed the Survivors

A popular species is captured repeatedly because it is easy for beginners to approach and battle.

The total declines according to the finite ledger. At the same time, the remaining population can become compositionally different if bold/visible individuals were disproportionately removed.

Possible later observations include longer approach distances, more nocturnal use, redistribution into quieter patches, or a lower/higher competence tail depending on which individuals were actually removed.

No universal direction is assumed.

## Seed: Remove the Predator, Change the Route

Authorities or Trainers repeatedly remove a predator from a managed corridor because of safety concerns.

That can solve the immediate human-safety issue while changing prey pressure and vegetation/resource use later.

The intervention therefore has an ecological afterlife. The project can revisit the same route seasons later and find a different problem produced by a once-successful policy.

This seed remains non-canon until a specific Marea predator/prey relation is source-backed and approved.

## Seed: The Outlier Comes Back

A dangerous actor is relocated rather than captured permanently.

The intervention records origin, destination, membership transfer, and monitoring evidence.

A later return is possible only if the world model actually routes that actor back. It is not a scripted clone.

This provides a long-form NPC arc: authorities can learn that relocation distance, habitat suitability, season, and the actor's established range matter.

## Seed: Experienced Does Not Mean Aggressive

A population with extensive battle exposure begins disengaging earlier from low-value confrontations.

Another species exposed to comparable pressure becomes more willing to display or defend resources.

Both are valid outputs because contest experience is species/context dependent. The system should not encode one universal “battle count -> aggression” curve.

## Long arc: Maintaining the Development Corridor

A future Marea development corridor can become a persistent civic/ecological system rather than a tutorial map.

Across months/seasons:

```text
new Trainers create high battle frequency
-> wild populations accumulate real encounter history
-> captures selectively alter membership
-> migration changes which cohorts are present
-> predators follow resources/prey
-> authorities monitor incidents and upper-tail risk
-> access/patrol/relocation policy changes
-> players see signs, altered paths, NPC reports, vegetation/traces, and different wild behavior
-> the corridor remains useful but never frozen
```

Veteran players can return and understand why the place has changed.

## Full encounter: Managed Development Corridor Incident

A dangerous individual is confirmed inside a high-use development segment while children/new Trainers are active nearby.

Narrative goals:

- verify identity and location without creating a duplicate;
- protect route users;
- understand whether the actor is passing through, displaced, territorial, feeding, or habituated;
- choose an intervention proportional to evidence;
- preserve ecological accounting;
- produce a persistent outcome visible later.

Possible full solutions include observation, temporary closure, controlled deterrence, managed capture, supervised battle, redirection, or relocation.

### Battle capability dependencies if the response becomes tactical

- targeting/footprints/range/LoS: needed for verified spatial threat/targeting.
- base movement legality: needed for ordinary movement.
- complete movement including push/pull/knockback/interception/forced movement: needed for containment, blocking, redirection, or forced displacement.
- core calculations: needed for authoritative combat arithmetic.
- action economy/initiative: needed once structured combat begins.
- full turn/round lifecycle: needed for complete encounter sequencing.
- full stateful damage pipeline: needed if damage is possible.
- status lifecycle: needed if calming/control/status tactics use PTU Status.
- terrain/weather/hazards/zones/reactions: needed only if the chosen site/intervention invokes them.
- move-specific behavior: needed for any specific Move interaction.
- abilities: needed for Ability-mediated behavior/mechanics.
- items: needed for Balls, medicine, bait, restraint, or other PTU Items.
- Trainer Features/perks: needed for relevant Features/Edges/Skills.
- AI legal-action infrastructure: needed to enumerate legal wild options.
- AI tactical policy: needed for competent autonomous tactical response.
- Minecraft/Cobblemon/Craftics adapter/playback support: needed to project the actor, route closure, movement, and authoritative results.

The world simulation cannot substitute for any missing tactical family.

## Reduced encounter: Signs, Patrol, Reroute

The same premise can run without a live rich battle.

1. The ecosystem window identifies a dangerous-risk observation from an existing member.
2. A trace/sighting is projected into the world.
3. NPC reports create a temporary advisory or route restriction.
4. The player investigates from safe distance using ordinary world movement and observation.
5. The actor either leaves through an authored/world-sim movement transition or remains, keeping the restriction active.
6. NPCs update their report based on evidence.
7. No hidden PTU battle, HP, Status, Move, or forced relocation is invented.

This reduced form already demonstrates the main narrative premise: safe beginner routes exist because people continuously manage a living ecosystem.

## Environmental playback examples

Results from conflict windows may become visible later as:

- a damaged but recovering patch of brush;
- a trail used less frequently by one population;
- warning signs or temporary barriers;
- an NPC patrol appearing at a different time;
- a feeding/roost site becoming quieter;
- old traces decaying while new ones appear elsewhere;
- changed species spacing or avoidance behavior;
- a relocated persistent actor later being reported in its destination ecosystem.

Environmental effects need duration/decay. They should not accumulate forever.

## Canon questions left open

- Which current Marea locations sit inside the first managed development zone.
- Whether Mara, Nerea, Teo, Lia, another institution, or a new role has authority for each intervention type.
- Minimum age/licensing/supervision norms for children/new Trainers.
- Which species provide the first test population.
- Which species can learn materially from repeated battle exposure.
- What amount of conflict history maps to an actual PTU progression event after source audit.
- Which dangerous-risk metrics authorities can reliably measure.
- Where relocated actors can legally/ecologically go.
