# The Night Shift After the Revision

Status: PROPOSED / NON-CANON
Date: 2026-09-06
Pass: 313

## Premise

A regional service complex changed access policy after an evidence-based restriction was reviewed. The day shift applied the revised order and reopened one operational corridor. Several hours later the night shift arrives with incomplete information, a different duty roster and one genuinely independent safety concern affecting another corridor.

The adventure asks a simple question with layered consequences: what state did the world actually reach, and who knows that state?

The important historical chain is durable:

old custody assessment → restriction decision → physical access consequence → corrected assessment → explicit review → selective repair.

The reopened corridor must remain reopened across unload/restart because that change already happened. The historical closure must also remain inspectable because later arguments, liabilities and NPC beliefs can depend on it.

## Core cast candidates

Shift supervisor: responsible for keeping operations moving. Receives operational bulletins but not every investigative document.

Archive runner: carries the revision packet and can prove when different departments received it.

Safety inspector: discovered a separate structural problem that justifies keeping one side route closed even after the original restriction was rescinded.

Contract crew lead: lost work under the original closure and wants clarity on whether compensation or schedule priority follows from the correction.

Resident Pokémon caretaker: knows how local Pokémon react to machinery changes and can provide behavior observations if the setting later validates an appropriate PTU/Caelo skill or communication route.

All roles are candidates only. No named NPC becomes canon through this proposal.

## Exploration loop

The player arrives after shift change and finds contradictory visible state: one gate is open, one remains closed, an old notice is still posted, and the night roster contains a stale instruction copied before the revision.

Investigation can proceed through the gate log, shift handoff records, the physical notice board, the archive packet, the safety inspection and direct conversations. No single clue is mandatory. Different evidence establishes different facts.

The player can establish that reopening one corridor was a legitimate repair of the reviewed decision while the second closure has an independent basis. That distinction prevents a false binary where either every closure was wrong or every closure remains justified.

## Persistent consequences

If the reopened corridor was already repaired to `CEASED`, restart cannot restore the old closed state.

If the second corridor is retained under a new structural basis, removing the old evidentiary basis cannot automatically open it.

The stale notice may remain until a separate publication correction occurs.

The contract crew's lost work remains historical even if future access is restored.

Trust damage, payment claims and schedule repair require their own systems and events.

## Reduced implementation version

The reduced version needs no AutoPTU combat.

Represent the complex as authored safe/open/closed nodes. Use the world-agent knowledge ledgers, custody lineage, decision dependency, review registry and consequence repair registry. Persist them through `OUROS_NPC_WORLD_CHECKPOINT_V5`. The night shift receives only the information explicitly delivered to its members.

Hazards are authored facts rather than tactical zones. Rescue, if needed, resolves as deterministic travel/state transitions outside battle.

This version preserves the narrative premise: operational history and personal knowledge can diverge without the world reverting.

## Full mechanically rich version

A later full version can place the service complex on a weather-exposed elevated structure with moving service platforms, unstable decking and a Pokémon-assisted emergency response.

Exact capability dependencies:

targeting/footprints/range/LoS — required if rescue or confrontation needs spatial target legality.

base movement legality — required for ordinary traversal of the tactical site.

complete movement including push/pull/knockback/interception/forced movement — required for wind displacement, forced repositioning, interception or rescue movement.

core calculations — required for deterministic tactical arithmetic.

action economy/initiative — required for structured turns and contested timing.

full turn/round lifecycle — required for timed platform movement, deterioration pulses or phase changes.

full stateful damage pipeline — required for environmental harm that can affect HP/injury state.

status lifecycle — required if shock, trapped, slowed or other persistent conditions are authored.

terrain/weather/hazards/zones/reactions — required for exposed surfaces, weather pressure, live hazard zones and rescue reactions.

move-specific behavior — required only for explicitly authored Moves.

abilities — required only when Pokémon Abilities alter the scene.

items — required only when equipment or held items have mechanical effects.

Trainer Features/perks — required only when a Trainer Feature changes legality, timing or outcome.

AI legal-action infrastructure — required for any autonomous tactical actor to choose only legal options.

AI tactical policy — required for general autonomous rescue/combat choices.

Minecraft/Cobblemon/Craftics adapter/playback support — required for authoritative visible execution in the final game environment.

## Full-version fallback

Keep weather and structural danger in presentation, but convert mechanical terrain into fixed `SAFE`, `BLOCKED` and `INSPECTION` nodes. Remove wind knockback, timed collapse, reaction rescue and persistent statuses. Use deterministic authored transitions for the service lift.

This preserves the same investigation, personnel conflict and consequence history while avoiding mechanics not yet verified end-to-end.

## Canon questions

Which institution owns the service complex?

Which region eventually binds this encounter?

Which Pokémon species, if any, are resident or employed there?

Which PTU Skills or Trainer Features can legitimately inspect structural conditions, authenticate documents or interpret Pokémon behavior?

None of these are approved by this proposal.
