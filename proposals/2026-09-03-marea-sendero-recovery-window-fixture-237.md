# Marea / Sendero recovery-window fixture

Status: PROPOSED CONTENT FIXTURE
Date: 2026-09-03
Pass: 237

## Scope

This fixture grounds the disturbance/succession/recovery contract in the already-approved Sendero del Vidrio lower shelf and its canon Fletchling population. The disturbance itself is not canon. The fixture exists so implementation and later content review can exercise the state transitions without authorizing a new species or rewriting Marea geography.

Machine-consumable state sequence:

`implementation/marea-sendero-disturbance-recovery-fixture-v1.json`

## Premise

A strong runoff/debris event has recently altered a bounded portion of the lower shelf. Cover is reduced, one ordinary passage is partially obstructed and exposed substrate creates a temporary ecological opportunity. The known Fletchling population still exists; the fixture does not invent deaths, captures, migration or replacement members.

The player arrives after the immediate event rather than during a scripted disaster cutscene. The question is what the habitat is becoming.

## Exploration loop

The first visit establishes acute evidence: damaged cover, changed access, reduced normal visibility and traces that surviving actors are using remaining refuge differently.

A later visit can reveal early succession. Some resources remain below reference condition while a temporary resource pulse appears. This is intentionally ambiguous: increased visible activity by one beneficiary would not prove that the whole site is healthier.

A third observation window tests whether recovery is progressing. Route connectivity and cover may improve, but the site cannot be declared recovered until the configured functional targets and observation window are met.

A repeat runoff event during incomplete recovery produces a different problem from the first impact because the site starts from its current recovering state. Loss of remaining legacies can push the trajectory toward transient or persistent reorganization.

## Player interventions

Possible interventions remain world-state actions unless a concrete tactical conflict starts:

- document environmental evidence for Marea staff;
- avoid trampling or repeated traffic through fragile recovering ground;
- redirect ordinary movement around a vulnerable refuge;
- clear an authored obstruction when the world interaction layer permits it;
- protect a temporary resource point from unnecessary disturbance;
- identify whether the original disturbance source is still active;
- revisit after time has passed to distinguish recovery from temporary appearance changes.

The content should support a valid outcome where the player decides not to force the area back toward the old visual state because a stable reorganization is ecologically coherent.

## Evidence and uncertainty

Ordinary NPCs and players can know only what has been observed or institutionally recorded. Useful evidence includes route usability, repeated use of refuge, return latency, cover recovery, resource use and whether the same damage recurs.

No NPC automatically receives hidden values such as `recovery_momentum` or `reorganization_pressure`.

## Canon-preservation rules

The approved Fletchling population remains `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`.

This fixture does not establish:

- a canonical storm date;
- canonical Fletchling mortality;
- new species in Marea;
- a permanent new route geometry;
- an automatic regional disaster questline;
- Shaymin, Suicune or another restoration specialist as present in Marea;
- a PTU mechanical weather effect.

Any future species that benefits from early succession must pass the normal regional species gate before it can become local population truth.

## Reduced encounter version

The entire fixture can run without combat. Ouros updates site state, Minecraft shows authored evidence, and observation/intervention produces semantic world results.

If a simple conflict occurs, Ouros selects explicit combatants and freezes the recovery process for the duration of a normal bounded AutoPTU encounter. Only verified mechanics and individually validated Moves/Abilities are allowed. The result returns as a semantic disturbance/intervention outcome.

## Intended rich encounter version

A later restoration-defense sequence could involve a refuge that must remain accessible while actors retreat through changing terrain, with time pressure and environmental zones.

Required capability families:

- targeting/footprints/range/LoS: VERIFIED within audited contracts;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: PARTIAL;
- core calculations: VERIFIED;
- action economy/initiative: VERIFIED;
- full turn/round lifecycle for timed objectives: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions for runoff, debris or changing safe areas: MIXED/PARTIAL/BLOCKING;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy for flee/guard/retreat priorities: BLOCKING as a complete family;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING end-to-end.

Until those exact dependencies are verified, the rich sequence must reduce to static terrain plus semantic ecological consequences.

## Acceptance

The fixture succeeds when repeated evaluation can visibly distinguish impact, early succession, incomplete recovery and repeat disturbance while preserving the same population identity and without using generic spawn/despawn as ecological truth.