# Sendero temporal ecology seeds — pass 216

Status: PROPOSED / NON-CANON
Date: 2026-09-02
Implementation correction: 2026-09-03 — use native Cobblemon temporal spawning

## Canon boundaries

This proposal reuses only established Marea sites and residents. It does not add a second wild population, alter the first Fletchling blueprint, assign exact activity hours, establish weather mechanics or create a new explanation for Thin Delivery Season.

Canon-approved anchors used here:

- Sendero del Vidrio lower shelf `(2056, 77, 2120)`;
- seasonal crossing `(2072, 79, 2154)`;
- Estación Mirador and its field-transect function;
- Mara Veyra as coordinator for route checks and wildlife incidents;
- Dr. Nerea Sol as owner of longitudinal ecological/weather observation work;
- Lia Morn as owner of arrival/departure and unloading-window records;
- the first persistent wild Fletchling slot `ouros.marea.encounter.sendero_lower_shelf.fletchling.0`.

The canonical Fletchling remains level 5 with its frozen PTU 1.05 mechanical identity. Its Sky 5 matters only when authoritative movement/encounter state makes flight relevant. Time does not rewrite its Moves, Ability, HP, stats or ownership state.

## Corrected implementation boundary

Cobblemon already supports natural spawn conditions by time and other world context through `spawn_pool_world`, with Spawn Rules available for additional filtering/weighting. Therefore Sendero should not receive a parallel Ouros day/night spawn scheduler.

Use this split:

```text
Cobblemon spawn data + server world context
-> generic species availability and relative natural spawn opportunity

Ouros population/canon state
-> whether an authored population is valid in the region
-> provenance for why regional spawn conditions exist

Ouros persistent individual state
-> where a known individual actually is and whether it can be projected
-> prevents duplication by generic spawning

Ouros behavior policy
-> what a present Pokémon does in response to context and Trainer actions

AutoPTU
-> PTU legality, calculations and structured encounter resolution
```

For future generic Sendero populations, approved day/night/weather/light conditions should normally be represented in Cobblemon datapack configuration rather than reimplemented in Ouros code.

For the existing persistent Fletchling, a matching generic spawn window must never clone the individual. Persistent identity stays stronger than generic natural spawning.

## Narrative premise

Sendero should feel like one place used by different actors at different times, not a static encounter room whose contents reset whenever a player enters.

The player can learn that timing changes what is observable. Cobblemon may produce ordinary temporal variation at the world layer, while Ouros preserves the evidence, population meaning and identity consequences. No UI should simply announce a universal “night spawn bonus.”

## Seed: Same Shelf, Different Hour

Nerea has two legitimate observations from the lower shelf that appear inconsistent. One visit records ordinary human transit and no direct wild sighting. Another records wild activity during a quieter interval.

The player can visit during one window, return during another, compare traces, or ask Lia/Mara whether routine traffic differed. A single absence remains weak evidence. Repeated observations with recorded effort can establish a local pattern later.

If the observation concerns a future generic population, its approved temporal availability can map to native Cobblemon spawn conditions. If it concerns the persistent Fletchling, its authoritative individual state decides whether that known bird can be present. The quest cannot force-spawn or duplicate it to satisfy a script.

Possible outcomes remain narrow:

- evidence supports a tentative activity window;
- evidence shows the earlier observations used different methods;
- human traffic appears correlated with presence but causation remains open;
- insufficient evidence remains the correct conclusion.

None of those outcomes changes species canon by itself.

## Seed: The Rush-Hour Gap

Lia's dock and route records reveal a recurring pulse of people moving between Puerto Bruma and Sendero. Nerea wants to know whether the apparent wildlife gap during that period reflects actual temporal avoidance, poorer observation quality, simple coincidence or a sampling bias created by researchers themselves.

The player can accompany an observation before the pulse, remain through it, and inspect afterward.

If later canon approves a population-specific response to those hours, the ordinary availability/weight change should be expressed through Cobblemon spawn data where possible. Ouros keeps the provenance and world consequence instead of duplicating the spawn algorithm.

This creates a useful worldbuilding consequence: regular human schedules can become ecological facts without becoming hostile environmental effects. Wildlife may habituate to routine traffic, avoid it, exploit its aftermath, or respond differently by species/population. Every such pattern requires evidence.

## Seed: Quiet Does Not Mean Safe

A Trainer deliberately chooses a low-traffic period to approach a wild Pokémon.

The reduced background disturbance can make a close approach easier to read, but it can also make the Trainer unusually salient. The behavior policy still runs in the established order:

```text
species/population prior
+ temporal/site context
+ persistent individual state
+ actual mechanical capabilities
+ observed Trainer approach
+ verified Skill/Feature/Edge/Move/Item effects
-> legal behavior options
-> tactical selection
```

Cobblemon deciding that the species is eligible to spawn at that hour does not decide the individual's tolerance or tactical intent.

This seed directly supports several Trainer strategies already contemplated by the project: waiting, changing approach vector, maintaining distance, avoiding escape-route blockage, using verified concealment or calming tools, or disengaging before pressure escalates.

## Seed: Stay for the Changeover

Nerea asks for a continuous observation spanning a transition between two activity windows rather than two disconnected visits.

The player is rewarded for noticing changes instead of defeating something. Valid observations may include a persistent individual leaving, a call becoming audible, fresh traces appearing, ordinary human traffic declining, a different generic population becoming naturally eligible through Cobblemon, or no change at all.

No second species is authored by this proposal. Until another Sendero population is canon-approved, cross-species evidence can remain indirect: unidentified trace, sound, displaced material or an unresolved observation record. Species identity cannot be inferred merely because the narrative wants a reveal.

## Seed: A Schedule Becomes Bad Science

After several successful observations, an institutional routine develops around the presumed “best” hour. That convenience risks creating a sampling blind spot.

Nerea can challenge the routine and ask for observations outside the familiar window. Mara may prefer daylight route checks for operational reasons. Both positions can be valid under their mandates.

The player can help preserve methodology metadata so later records distinguish ecological absence from lack of observation effort.

Native spawn conditions do not remove this problem. A datapack condition describes implementation truth for an approved population; researchers inside the fiction may still have incomplete knowledge of that pattern.

## Mechanically rich encounter: Dusk Crossing Window

Working title only. Exact dusk/night behavior remains unresolved until species and rules provenance are approved.

### Intended full version

A field observation near the seasonal crossing overlaps a transition in routine human traffic and a possible wild-presence window. Generic natural wildlife availability is supplied by Cobblemon's native spawn system; known persistent individuals remain gated by Ouros identity/state. The player's objective is to obtain useful observation data while preserving freedom to withdraw, approach, redirect movement or begin a legitimate capture/battle interaction if they choose.

The rich version can support:

- server-authoritative Minecraft time/weather/light context consumed by Cobblemon;
- native Cobblemon spawn eligibility/weight for generic populations;
- Ouros population/canon gates and persistent-individual identity;
- actual visibility and LoS rather than cosmetic darkness deciding PTU rules;
- footprint/range-aware approach;
- legal base movement and escape routes;
- a wild actor evaluating whether the Trainer is observing, pursuing or containing it;
- Trainer Skills/Edges/Features individually verified for perception, Stealth, handling or interaction;
- legal Items/Moves/Abilities used for concealment, restraint, hindrance, capture preparation or Status application;
- interception/forced movement only when those exact mechanics are verified;
- capability-aware wild tactical choice among tolerate, alert, warn, withdraw, evade, guard, obstruct, engage or disengage;
- semantic adapter events that tell Minecraft what happened without asking Minecraft to recalculate PTU.

Battle outcome and observation outcome remain separate facts. Winning a battle does not prove an activity pattern. A successful observation does not grant capture or ownership.

### Reduced version: Observe, Return, Compare

This version preserves the premise using substantially simpler capabilities.

Minecraft/Cobblemon supplies server world time and ordinary natural spawning. Ouros records site, player presence, observation effort, population/canon context and any persistent identity state. The player can traverse Sendero normally, wait or return later, record direct evidence/traces, and change approach or leave.

If the persistent Fletchling is present, Minecraft may render its already-authorized world actor and behavior cues supported by the world behavior layer. If an actual battle begins, the existing frozen blueprint enters the normal BattleSpec path.

The reduced version does not:

- create an Ouros day/night spawn scheduler;
- fabricate darkness penalties;
- invent Stealth/Perception bonuses;
- invent trapping or movement reduction;
- force a persistent individual because a generic clock condition matched;
- simulate unimplemented tactical AI off-screen;
- infer ecological absence from a failed spawn/despawn;
- let Minecraft own PTU legality.

## Engine capability dependencies

The intended full `Dusk Crossing Window` touches the permanent capability families as follows.

| Capability family | Need in full version | Current boundary for this concept |
| --- | --- | --- |
| targeting / footprints / range / LoS | Required for detection, approach and spatial interaction | VERIFIED only inside audited engine contracts; darkness/visibility semantics themselves remain unverified here |
| base movement legality | Required | VERIFIED inside audited contracts |
| complete movement incl. push/pull/knockback/interception/forced movement | Required only if containment/interception/forced displacement is used | PARTIAL; do not generalize from prevention subcases |
| core calculations | Required when an authorized Skill/capture/battle calculation occurs | VERIFIED inside audited contracts, but each new modifier still needs source validation |
| action economy / initiative | Required once structured battle/action timing begins | VERIFIED inside audited contracts |
| full turn/round lifecycle | Required for complete structured encounters | PARTIAL |
| full stateful damage pipeline | Required if combat damage occurs | PARTIAL |
| status lifecycle | Required if the Trainer uses Status to control/capture | PARTIAL |
| terrain/weather/hazards/zones/reactions | Optional unless the authored encounter actually uses these | BLOCKING for rich effects that depend on them; time-of-day must not be smuggled into this family as a fake rule |
| move-specific behavior | Required for any Move-based concealment/control/capture setup | PARTIAL |
| abilities | Required when an Ability changes behavior/mechanics | PARTIAL |
| items | Required for Balls or other mechanically meaningful equipment | PARTIAL |
| Trainer Features/perks | Required for Feature/Edge tactical modifiers | PARTIAL |
| AI legal-action infrastructure | Required | VERIFIED inside audited contracts |
| AI tactical policy | Required for competent autonomous wild decisions | BLOCKING as a complete family; behavior-intent design can proceed independently |
| Minecraft/Cobblemon/Craftics adapter/playback | Required for native spawn configuration, world actor projection and semantic playback | PARTIAL end-to-end; native temporal spawn capability itself is VERIFIED in Cobblemon documentation, but Ouros integration/persistent-identity reconciliation is not yet end-to-end verified |

## PTU/Caelo/Kairos boundary

The first Fletchling canon cites supplied PTU 1.05 material for its blueprint and Caelo material as comparative living-world evidence for territorial/diurnal behavior. This proposal does not convert “diurnal” into exact spawn hours or a combat modifier.

Before mechanics are approved, the project still needs exact source checks for:

- perception/visibility and low-light rules, if any;
- Stealth and detection;
- Survival/Intuition or other observation/field uses;
- Features/Edges that alter approach or wild interaction;
- capture action/range/modifiers;
- effects that genuinely trap, restrain or reduce movement;
- Status interactions relevant to capture/control;
- any Caelo/Kairos overrides.

Every verified rule should be recorded separately. Temporal ecology should not create a generic bonus layer that bypasses PTU.

## Longer-term arc potential

Once multiple populations are canon-approved, the same model supports meaningful regional changes without authored quest replacement. A new ferry schedule can alter human-pressure windows. A temporary closure can make a route attractive at a different hour. A predator or competitor can alter overlap between populations. Repeated player traffic can create a measurable disturbance record. Seasonal migration can make a crossing important for a short period.

Where those changes can be represented as ordinary spawn eligibility/weight, Cobblemon datapacks should carry them. Ouros should own the provenance, canon approval, population consequence and persistent-individual exceptions.

## Open canon/implementation questions

Exact Sendero activity windows remain unapproved. The next species remains unapproved. The project must decide how the first persistent Fletchling maps onto Cobblemon world persistence without allowing generic duplicate spawns. It also needs a clear reconciliation rule between Cobblemon natural despawn/save behavior and Ouros canonical individual availability.

The server's Minecraft world clock should be the primary temporal input. Ouros should consume that authoritative world context rather than maintain a competing clock unless a future explicit simulation requirement cannot be represented by Minecraft/Cobblemon.