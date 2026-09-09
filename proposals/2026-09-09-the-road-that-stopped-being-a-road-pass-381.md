# The Road That Stopped Being a Road — Pass 381

Status: PROPOSED / NON-CANON
Canon effect: NONE

## Premise

A persistent field actor selects a legitimate destination and begins traveling. After departure, the next route edge becomes unavailable under the world facts visible to that actor. The semantic travel runtime can now preserve a replayable `REPLAN_REQUIRED` interruption without claiming failure or cancellation.

The useful mystery begins after that fact. The route may have become unusable because of an environmental change, damaged infrastructure, a new permission restriction, lost knowledge, an emergency closure, a Pokémon-related disturbance or deliberate interference. These remain hypotheses until another authoritative owner provides evidence.

## What can be true together

The dispatching institution can prove the actor left.

The actor can prove the original plan was valid when travel began.

Pass 381 can prove that the route later required replanning.

A destination contact can correctly say the actor never arrived by the expected route.

None of those facts proves that the mission failed, was canceled or was abandoned.

## Reduced version

No AutoPTU encounter is required.

A named NPC begins semantic travel. One route edge changes state after departure. `OUROS_NPC_ACTION_INTERRUPTION_PROVENANCE_V1` records the replayable interruption. The existing replanning layer can then decide among another route, waiting, contacting someone, seeking permission, gathering information or changing priorities.

This version works even while the physical map and exact Caelo location remain unresolved.

## Full version

A player-facing version can turn the interrupted edge into an investigation or assistance site. Possible goals include establishing why passage changed, finding a safe alternate path, escorting delayed travelers, recovering equipment, reopening communication, documenting ecological change or getting vulnerable actors out before conditions worsen.

Combat remains optional pressure. Defeating every Pokémon is not required by the narrative premise.

## Environmental storytelling

The route should show evidence of transition rather than a generic invisible blocker. Examples can include changed water level, damaged markers, displaced cargo, fresh detours, abandoned work, tracks that stop or split, newly posted restrictions, temporary shelters or evidence that local Pokémon behavior changed.

Which evidence is legal depends on approved geography, institution, technology and species ecology. These examples are placeholders only.

## Engine capability dependencies for the full version

Targeting/footprints/range/LoS: VERIFIED within audited ordinary scopes if ordinary tactical targeting is used.

Base movement legality: VERIFIED within audited ordinary scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. The premise does not require these mechanics.

Core calculations: VERIFIED within audited deterministic scopes.

Action economy/initiative: VERIFIED for audited primitives only.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING. A dynamic flood, collapse, weather phase, hazard trigger or reactive zone requires exact evidence for that family. The reduced version instead changes semantic route availability without simulating the tactical cause.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. Current Intimidate rollover parity does not establish blanket Ability support.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for escort, search, route-clearing, protect-equipment/noncombatant, rescue-first, objective-aware withdrawal and disengage-after-objective unless those exact policies gain live evidence.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for persistent route/closure/objective/equipment identity, non-KO objective acknowledgement and authoritative end-to-end result playback.

## Canon questions before promotion

Approved route and geography.

The actor and institution that use it.

The authority capable of closing or restricting passage.

Species and habitat evidence for any Pokémon-related explanation.

Communication coverage and travel technology in the chosen place.

Whether an existing canon route/site already serves this function.

What owner records the underlying route-state change so the interruption cause can eventually be proven rather than inferred.

Until those questions are resolved, all names, locations and causes remain placeholders.
