# Marea Sendero escalation handoff fixture — Pass 242

Status: PROPOSED / NON-CANON
Date: 2026-09-03

## Premise

Use the already approved lower-shelf Fletchling vertical-slice actor to test that the same ecological situation can remain overworld behavior, de-escalate, or enter AutoPTU depending on the actual mechanical question.

No new species, NPC, population count, route or PTU rule is introduced.

## Sequence

The player encounters the persistent Fletchling near the lower shelf while the bird is feeding. The actor notices the player and changes behavior.

The first branch remains ambient. The Fletchling warns, shifts position and watches. If the player observes, waits or backs away, Ouros records only the relevant observation/disturbance consequences. No BattleSpec exists.

A second branch has the Fletchling leave through an open route. If the player does not contest the departure, Minecraft may project the flight and Ouros records avoidance. This is not emigration and does not require AutoPTU.

The structured branch begins only if the interaction now asks a tactical question. A direct attack, an explicitly contested PTU action, or an authored objective requiring targets/range/initiative can cause Ouros to freeze the manifest and create a BattleSpec.

## Manifest rule

The canonical first Fletchling is the only wild combatant in the reduced fixture. Other visible wild projections remain noncombatants unless a later contract explicitly adds them.

The player-side participant must come from the normal authoritative party/profile pipeline. Minecraft proximity does not enroll a Trainer, party member or wild Pokémon.

## Reduced encounter

The reduced version permits only ordinary battle mechanics whose exact profiles are validated before execution.

World rain, route vegetation and nearby ledges may remain visual if their tactical mappings are not verified.

The encounter ends with narrow AutoPTU facts. Ouros then decides whether the Fletchling remains nearby, avoids the area temporarily, is eligible for later observation, or participates in another world event.

A KO cannot become death. Withdrawal cannot become emigration. A visual Poké Ball success cannot become capture without the verified capture result path.

## Rich version

A later richer version can test a player trying to prevent the Fletchling from reaching an exit while the wild actor prioritizes escape.

That version requires exact evidence for:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement if interception or forced displacement is used;
- action economy/initiative;
- full turn/round lifecycle if escape timing is round-bound;
- move-specific behavior for every selected Move;
- Ability behavior for Big Pecks where relevant;
- AI legal-action infrastructure;
- AI tactical policy capable of prioritizing escape over damage;
- Minecraft/Cobblemon/Craftics playback and writeback.

Because complete movement and objective-aware AI remain incomplete as families, this rich chase must not be treated as production-ready.

## Fallback preserving the premise

If tactical pursuit is unsupported, the Fletchling exits through the overworld route under Ouros behavior authority. The player can later follow tracks, revisit the site or receive a changed observation opportunity. The ecological premise survives without fabricating interception rules.

## Expected player-facing lesson

Wild Pokémon are not random combat tokens. The player can watch, pressure, avoid, pursue or deliberately escalate. Structured combat appears when the interaction actually needs PTU mechanics, while ordinary ecological behavior remains continuous in the Minecraft world.

## Canon boundary

CANON-APPROVED inputs reused:

- Sendero del Vidrio lower shelf;
- `ouros.marea.wild.sendero_lower_shelf.fletchling.v1`;
- `ouros.marea.encounter.sendero_lower_shelf.fletchling.0`;
- `ouros.vertical_slice.ptu_1_05.fletchling_v1`.

PROPOSED:

- the branch structure;
- encounter-intent evaluation;
- reduced escape fallback;
- result-routing behavior.

UNCERTAIN:

- exact capture authority path;
- exact thresholds for hostile engagement;
- whether pursuit becomes a single BattleSpec or linked encounter in the first production adapter;
- which final-state fields can safely persist back from AutoPTU at current parity.
