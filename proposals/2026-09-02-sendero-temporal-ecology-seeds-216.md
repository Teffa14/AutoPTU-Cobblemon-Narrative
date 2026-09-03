# Sendero temporal ecology seeds — pass 216

Status: PROPOSED / NON-CANON
Date: 2026-09-02

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

## Narrative premise

Sendero should feel like one place used by different actors at different times, not a static encounter room whose contents reset whenever a player enters.

The player can learn that timing changes what is observable. This knowledge comes from repeated world evidence: direct sightings, traces, sounds, route traffic and comparison of records. No UI should simply announce a universal “night spawn bonus.”

## Seed: Same Shelf, Different Hour

Nerea has two legitimate observations from the lower shelf that appear inconsistent. One visit records ordinary human transit and no direct wild sighting. Another records wild activity during a quieter interval.

The player can visit during one window, return during another, compare traces, or ask Lia/Mara whether routine traffic differed. A single absence remains weak evidence. Repeated observations with recorded effort can establish a local pattern later.

The persistent Fletchling may appear only if its authoritative world state places it there. The quest cannot force-spawn or duplicate the individual to satisfy a script.

Possible outcomes remain narrow:

- evidence supports a tentative activity window;
- evidence shows the earlier observations used different methods;
- human traffic appears correlated with presence but causation remains open;
- insufficient evidence remains the correct conclusion.

None of those outcomes changes species canon by itself.

## Seed: The Rush-Hour Gap

Lia's dock and route records reveal a recurring pulse of people moving between Puerto Bruma and Sendero. Nerea wants to know whether the apparent wildlife gap during that period reflects actual temporal avoidance, poorer observation quality, simple coincidence or a sampling bias created by researchers themselves.

The player can accompany an observation before the pulse, remain through it, and inspect afterward.

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

The encounter therefore cannot encode `night = calmer` or `empty trail = lower alarm` as a global rule.

This seed directly supports several Trainer strategies already contemplated by the project: waiting, changing approach vector, maintaining distance, avoiding escape-route blockage, using verified concealment or calming tools, or disengaging before pressure escalates.

## Seed: Stay for the Changeover

Nerea asks for a continuous observation spanning a transition between two activity windows rather than two disconnected visits.

The player is rewarded for noticing changes instead of defeating something. Valid observations may include a persistent individual leaving, a call becoming audible, fresh traces appearing, ordinary human traffic declining, or no change at all.

No second species is authored by this proposal. Until another Sendero population is canon-approved, cross-species evidence can remain indirect: unidentified trace, sound, displaced material or an unresolved observation record. Species identity cannot be inferred merely because the narrative wants a reveal.

## Seed: A Schedule Becomes Bad Science

After several successful observations, an institutional routine develops around the presumed “best” hour. That convenience risks creating a sampling blind spot.

Nerea can challenge the routine and ask for observations outside the familiar window. Mara may prefer daylight route checks for operational reasons. Both positions can be valid under their mandates.

The player can help preserve methodology metadata so later records distinguish ecological absence from lack of observation effort.

This seed creates character and institutional tension without requiring a villain or hidden conspiracy.

## Mechanically rich encounter: Dusk Crossing Window

Working title only. Exact dusk/night behavior remains unresolved until species and rules provenance are approved.

### Intended full version

A field observation near the seasonal crossing overlaps a transition in routine human traffic and a possible wild-presence window. The player's objective is to obtain useful observation data while preserving freedom to withdraw, approach, redirect movement or begin a legitimate capture/battle interaction if they choose.

The rich version can support:

- authoritative world time and local activity-window state;
- actual visibility and LoS rather than cosmetic darkness deciding rules;
- footprint/range-aware approach;
- legal base movement and escape routes;
- a wild actor evaluating whether the Trainer is observing, pursuing or containing it;
- Trainer Skills/Edges/Features that have been individually verified for perception, Stealth, handling or interaction;
- legal Items/Moves/Abilities used for concealment, restraint, hindrance, capture preparation or Status application;
- interception/forced movement only when those exact mechanics are verified;
- capability-aware wild tactical choice among tolerate, alert, warn, withdraw, evade, guard, obstruct, engage or disengage;
- semantic adapter events that tell Minecraft what happened without asking Minecraft to recalculate PTU.

Battle outcome and observation outcome remain separate facts. Winning a battle does not prove an activity pattern. A successful observation does not grant capture or ownership.

### Reduced version: Observe, Return, Compare

This version preserves the premise using substantially simpler verified/world-state capabilities.

The server records world time, site, player presence, observation effort and any authoritative wild presence. The player can traverse Sendero normally, wait or return later, record direct evidence/traces, and change approach or leave.

If the persistent Fletchling is present, Minecraft may render its already-authorized world actor and simple behavior cues supported by the world behavior layer. If an actual battle begins, the existing frozen blueprint enters the normal BattleSpec path.

The reduced version does not:

- fabricate darkness penalties;
- invent Stealth/Perception bonuses;
- invent trapping or movement reduction;
- force a wild spawn because a clock condition matched;
- simulate unimplemented tactical AI off-screen;
- infer ecological absence from entity despawn;
- let Minecraft own time-sensitive PTU legality.

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
| Minecraft/Cobblemon/Craftics adapter/playback | Required for world clock cues, actor projection and semantic playback | PARTIAL/BLOCKING end-to-end |

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

Those consequences should emerge from persistent records and authored population logic. They should never be generated solely by the client clock.

## Open canon questions

Exact Sendero activity windows remain unapproved. The next species remains unapproved. The project must decide whether the first Fletchling individual gets a persistent daily location schedule or uses a population-level opportunity model plus individual state. It also needs a server-authoritative policy for time passage during multiplayer/unload/reload before temporal ecology can become gameplay truth.