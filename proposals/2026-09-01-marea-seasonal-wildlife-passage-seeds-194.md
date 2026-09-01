# Marea Seasonal Wildlife Passage Seeds — Pass 194

Status: PROPOSED / NON-CANON
Date: 2026-09-01

These candidates reuse canonical Marea Interior places, residents, and institutions. They do not establish new species distributions, seasonal rules, protected-area law, capture restrictions, or the cause of the Thin Delivery Season.

## 1. Tracks Before Sightings

Questline types: POKEMON / EXPLORATION / CLASS
Primary anchors: Ema Rey, Dr. Nerea Sol, Estación Mirador transect trailhead.

Ema records repeated indirect signs along one transect but no direct sighting. The player can help repeat the same method rather than immediately searching the whole district.

Useful state:
- first indirect observation;
- method and timestamp;
- second observation under different conditions;
- whether the signal strengthens, weakens, or remains ambiguous.

The story closes successfully even if the correct result is `insufficient evidence`.

## 2. The Crossing Is Busy Today

Questline types: POKEMON / EXPLORATION / SETTLEMENT
Primary anchors: Sendero del Vidrio seasonal crossing, Mara Veyra.

A temporary wild-Pokémon concentration is observed at the crossing. The road is physically intact. Mara adjusts a field visit rather than immediately declaring an emergency.

This tests the separation between ecological use, practical avoidance, and formal closure.

Species remains UNRESOLVED until a later canon/source decision.

## 3. Two Counts, Two Methods

Questline types: POKEMON / CLASS / CHARACTER
Primary anchors: Nerea Sol, Ema Rey.

Two observers report very different counts from the same general area. One walked a fixed transect; another watched a water source for a shorter period. Neither record is discarded.

The player can help determine whether the numbers are genuinely contradictory or methodologically incomparable.

No generic Researcher bonus is invented.

## 4. Quiet After the Crowd

Questline types: POKEMON / EXPLORATION
Primary anchors: Estación Mirador, Sendero del Vidrio.

After several days of unusually frequent observations, a repeat survey finds no target individuals. The absence is logged as a negative observation rather than proof that the population has left the district.

A later revisit can narrow the end bound of the ecological window.

## 5. Jo Moves the Lesson

Questline types: POKEMON / SETTLEMENT / CLASS
Primary anchors: Jo Venn, Loma Clara field school.

Jo planned an outdoor field-school session near a familiar route segment. New wildlife observations make another location or time more appropriate. The educational content stays the same while the logistics change.

This connects the ecology layer to the existing education layer without granting Jo wildlife-management authority.

## 6. Alba's Early Cart

Questline types: SETTLEMENT / POKEMON / SECONDARY
Primary anchors: Alba Ríos, Sendero del Vidrio.

Alba temporarily shifts one ordinary cart movement earlier because recent observations suggest the crossing is quieter then. The decision is practical and local.

If a delivery subsequently arrives on time, that does not prove the wildlife concentration caused earlier delivery irregularity.

## 7. Old Notes, Similar Week

Questline types: POKEMON / REGION / ITEM
Primary anchors: Tideglass Archive, Taro Min, Pia Min, Mirador records.

A current observation resembles an older archived note. The dates and location are suggestive but not identical. Taro preserves the comparison as a possible historical pattern rather than declaring a recurring migration.

This can later become `historical_pattern` only after sufficient evidence or explicit canon review.

## 8. Ferry-Side Visitors

Questline types: POKEMON / SETTLEMENT / EXPLORATION
Primary anchors: Lia Morn, Mina Cors, ferry landing.

Lia and Mina independently notice the same wild species near coastal operations during a short window. Their observations corroborate presence near the landing but do not establish where the Pokémon came from or where they go next.

No external ferry destination is canonized.

## 9. The Individual That Stayed

Questline types: POKEMON / CHARACTER
Primary anchors: a future explicitly authored wild individual, Mirador observation records.

Most observations associated with a temporary concentration end, but one recognizable individual continues appearing afterward. If later canon promotes that Pokémon to a persistent identity, its personal history begins with dated observations rather than an arbitrary spawn conversion.

Until promotion, it remains an uncertain individual-identification candidate.

## 10. Weather Beside the Pattern

Questline types: POKEMON / REGION / CLASS
Primary anchors: Nerea Sol, Estación Mirador.

The same period contains a weather change and an ecological concentration. Nerea records both and refuses to label one the cause of the other without supporting evidence.

This is a direct tutorial for `CORRELATION != CAUSATION` using a lived world event rather than exposition.

## 11. The Route Nobody Closed

Questline types: SETTLEMENT / POKEMON / EXPLORATION
Primary anchors: Mara Veyra, Sendero del Vidrio.

Residents begin informally favoring another time of day because the seasonal crossing has been busy with wild activity. No authorized closure exists.

The player can discover that a route described as “best avoided for now” remains legally/physically accessible under current canon.

This avoids converting every social adaptation into a hard quest gate.

## 12. Mirador Window Board

Questline types: POKEMON / SETTLEMENT / SERVER_EVENT
Primary anchors: Estación Mirador.

Mirador maintains a small public-facing board summarizing current dated observations with explicit uncertainty. The board can change while the player is away.

Example presentation:
- increased sightings reported at seasonal crossing;
- observations cover two mornings;
- cause unknown;
- next scheduled check pending.

The board projects existing records. It never reads raw spawn counts directly.

## 13. Long arc — When the Route Belongs to Others

Questline types: POKEMON / REGION / EXPLORATION / SETTLEMENT / SERVER_EVENT

Across several in-world periods, Marea residents learn that the same physical landscape does not have the same practical use every day.

Possible episodes:
- an initial concentration is noticed;
- Mirador records incompatible observations;
- ordinary work timing changes;
- an old Tideglass record suggests a possible precedent;
- the concentration declines;
- one future period does not repeat it when expected;
- another later observation either strengthens or weakens the recurrence hypothesis.

The arc produces longitudinal ecological memory without requiring a single hidden mastermind, legendary cause, or permanent crisis.

It should remain compatible with a future canon decision that the first event was unusual rather than seasonal.

## Rich encounter — Passage at the Seasonal Crossing

Status: PROPOSED / FULL VERSION BLOCKED BY ENGINE READINESS

Premise:
A temporary ecological window is active at the canonical seasonal crossing. Ema or another authorized observer is completing a field observation. A specific wild individual creates an immediate safe-passage problem while the larger group continues its own movement.

The narrative goal is safe withdrawal and preservation of the observation context, not defeating the population.

### Full intended version

Potential tactical elements:
- route geometry and footprints matter;
- an unsafe edge or narrow passage constrains movement;
- interception may be needed to protect withdrawal;
- a Move may Push, Pull, Knockback, or otherwise force movement;
- terrain/hazard zones may matter;
- statuses, Abilities, Items, and Trainer Features work exactly according to authoritative content;
- wild AI values legal withdrawal, corridor continuation, spacing, and threat response rather than behaving as a generic KO-seeking opponent;
- Minecraft/Cobblemon faithfully plays back the authoritative encounter and returns to the persistent ecological scene afterward.

Permanent capability dependencies:
- targeting/footprints/range/LoS — required;
- base movement legality — required;
- complete movement including push/pull/knockback/interception/forced movement — required for the rich corridor version;
- core calculations — required;
- action economy/initiative — required;
- full turn/round lifecycle — required;
- full stateful damage pipeline — required;
- status lifecycle — required if selected content applies statuses;
- terrain/weather/hazards/zones/reactions — required if route conditions are tactical;
- move-specific behavior — required;
- abilities — required for roster Abilities;
- items — required when used;
- Trainer Features/perks — required when participating Trainers use them;
- AI legal-action infrastructure — required;
- AI tactical policy — required for objective-aware wild behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — required for faithful end-to-end world execution.

### Reduced implementation

Keep outside BattleSpec:
- the ecological window;
- the larger population;
- observers and other noncombatants;
- route-use advice;
- observation records;
- movement of the larger group;
- any hypothesis about cause or recurrence.

Narrative first moves noncombatants to a safe state. If one specific immediate actor still blocks withdrawal or passage, compile an ordinary audited battle on stable geometry with only supported mechanics.

Allowed battle handoffs:
- `IMMEDIATE_CROSSING_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`
- `IMMEDIATE_FIELD_TEAM_CAN_WITHDRAW`

Narrative then records what was actually observed and decides whether the field session continues.

Battle outcome cannot decide:
- that the ecological window ended;
- total population size;
- migration status;
- why the Pokémon were present;
- whether weather caused the event;
- whether the Thin Delivery Season shares a cause;
- capture permissions;
- permanent route safety;
- institutional ecological conclusions.

## Recommended first implementation slice

Implement `Two Counts, Two Methods` before the rich encounter.

Reasons:
- uses canonical Nerea/Ema responsibilities;
- tests longitudinal observation provenance;
- requires no new species canon if records use an unresolved target placeholder during authoring;
- requires no battle engine capability;
- demonstrates that contradictory-looking evidence can coexist without one record being silently deleted;
- creates reusable infrastructure for later seasonal events, species arcs, route investigations, and Thin Delivery hypotheses.
