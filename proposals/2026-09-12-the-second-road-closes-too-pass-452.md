# The Second Road Closes Too — Pass 452

Status: PROPOSED / NON-CANON
Date: 2026-09-12

No region, settlement, institution, named NPC, faction, species distribution, League structure or historical event is assigned by this proposal.

## Premise

A specialist and a requester already changed the date of a site obligation once. The replacement commitment is now the only executable schedule in its lineage.

Before that new start time, the specialist receives credible evidence that the route, access permission, required resource or underlying premise has changed again.

The earlier promise remains history. The replacement remains the active obligation. The new evidence attaches to that active generation and wakes the specialist to reconsider what can still be done.

Pass 452 stops there. It does not automatically request another renegotiation.

## Narrative use

The scene supports a world where plans can fail more than once without making continuity incoherent. A second complication can feel different from the first because the actors remember the history while the local environment keeps changing.

Useful blocker examples include a temporary crossing becoming unsafe, an inspection permit being suspended, required equipment being reassigned, a Pokémon nesting event making a work area inappropriate to enter, or new evidence showing that the original survey premise is obsolete.

A later observation can also restore viability. That restoration is evidence, not an invisible reschedule.

## Reduced implementation version

The reduced version requires no AutoPTU scene.

The specialist receives a source-backed blocker before the replacement start. Pass 452 records `AT_RISK` or `BLOCKED` on the active replacement and schedules ordinary replanning. A later notice may record `RESTORED` if the condition clears.

Travel, access and resolution remain narrative unless their dedicated owners already admit the required actions. The old commitment stays historical and cannot receive fresh viability evidence after it has been superseded.

This version preserves the premise even when the tactical stack is unavailable.

## Mechanically rich version

The same obligation can later lead to an alternate-ingress survey or protection scene. The site has two approaches: the expected path and a newly discovered secondary approach. Environmental evidence can reveal the second route. Local Pokémon or other actors may make one approach unsafe without being automatic enemies.

Possible objectives include reaching a survey point, observing a condition, protecting a worker during a short task, withdrawing safely when the site changes, or returning with enough evidence to justify another negotiation.

The encounter must be authored from world state at execution time. Pass 452 does not reserve the alternate route or freeze local actors when the blocker is recorded.

## Capability dependencies for the full version

Targeting/footprints/range/LoS is required if actors must acquire targets or interact through spatial constraints. Current posture: VERIFIED only within audited scopes.

Base movement legality is required for ordinary grid movement. Current posture: VERIFIED only within audited scopes.

Complete movement including push/pull/knockback/interception/forced movement is required only if the full encounter uses unstable ledges, forced displacement, intercepting protectors or similar effects. Current posture: PARTIAL. Remove those effects in the reduced tactical version.

Core calculations are required for structured attacks/checks that use the audited calculation paths. Current posture: VERIFIED only within audited scopes.

Action economy/initiative, full turn/round lifecycle, full stateful damage pipeline and status lifecycle are required for a complete structured battle. Current posture: PARTIAL for each family.

Terrain/weather/hazards/zones/reactions is required if the alternate route changes through weather, hazardous ground, reactive zones or trigger windows. Current posture: MIXED / PARTIAL / BLOCKING according to the exact behavior. The reduced version treats route state as pre-scene evidence rather than a live tactical transformation.

Move-specific behavior, abilities, items and Trainer Features/perks are individually gated. No named mechanic should be assumed from a representative implementation.

AI legal-action infrastructure must explicitly admit any specialized objective verb such as `INSPECT`, `OBSERVE`, `PROTECT`, `BRACE`, `WITHDRAW`, `RETRIEVE` or `EXTRACT` before autonomous actors can use it as a legal tactical action.

AI tactical policy remains BLOCKING for specialized objective policies that have not been individually admitted.

Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Safe degradation

If only basic verified movement and simple audited combat are available, keep the alternate route static for the duration of the structured scene. Resolve the discovery and viability change before AutoPTU. Avoid live weather phases, forced movement, reactions, delayed hazards, ability-created terrain and Trainer Feature interrupts.

The story remains the same: a replacement plan encounters new evidence, the world records that evidence against the correct generation, and the characters must decide what to do next.

## Unresolved questions

A later pass must decide how Pass 438 start assessment and Pass 439 disposition consume viability attached to a replacement rather than to the original ledger.

Only after those owners become generation-neutral should a second `REQUEST_RENEGOTIATION` chain be admitted end to end.

Accountability and social consequences still need to distinguish repeated bad luck, avoidable preparation failures, deliberate refusal and simple inability. Pass 452 assigns none of those interpretations.
