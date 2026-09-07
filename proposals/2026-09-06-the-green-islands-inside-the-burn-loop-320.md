# The Green Islands Inside the Burn — Ouros exploration / recovery loop

Status: PROPOSED / NON-CANON

Pass: 320

## Premise

A route corridor crosses a landscape that burned during a previous fire season. Administrative maps show one large historical fire perimeter, but new field reports disagree sharply about current conditions. One patrol describes broad blackened ground and obstructed travel. Another reports living canopy, fresh feeding signs, and usable shelter inside the same mapped perimeter.

The contradiction is real only at the scale of the reports. The landscape itself is a mosaic.

The player is asked to help establish which features are safe to reopen, which patches should remain monitored or protected, and why some areas recovered differently from others.

No location, institution, species, fire cause, or final resolution in this proposal is canon.

## Core exploration structure

The site has at least four distinguishable field zones.

### Perimeter overlook

A high or otherwise broad observation point shows the historical disturbance footprint and the large-scale pattern. It can support evidence such as:
- old perimeter markers;
- route closure notices;
- visible canopy discontinuity;
- surviving green patches;
- later infrastructure cuts or service tracks.

This location gives scale but weak local detail.

### Burned route segment

A former travel edge has visible disturbance evidence and may still be blocked or restricted. Useful observations can include:
- fallen material;
- repaired or unrepaired markers;
- erosion/sediment changes;
- new low vegetation;
- recent tracks or service use;
- evidence that one side of the route burned differently from the other.

The route state is authored feature state. Visual blackening alone does not decide mechanical safety.

### Green island / refuge patch

A patch inside the historical perimeter retained more cover or recovered faster. It can contain:
- surviving vegetation structure;
- shade or shelter unavailable nearby;
- water or damp ground if later canon supports it;
- Pokémon use documented through sourced species-appropriate evidence;
- monitoring markers placed after the fire.

This patch is valuable without being declared globally safe, pristine, or permanently protected.

### Boundary / transition strip

A narrow transition between high-impact and low-impact patches creates the strongest comparative evidence. The player can compare:
- vegetation age/structure;
- surface condition;
- route damage;
- signs of animal use;
- prior treatment or infrastructure;
- reports collected at different dates.

The design goal is to make the difference between patches observable before the explanation is known.

## Investigation loop

1. Receive two or more reports that appear inconsistent.
2. Inspect the scale and provenance of each report.
3. Visit at least two physically different patches inside the same historical perimeter.
4. Record observations without converting them immediately into causal conclusions.
5. Compare historical records, route state, weather/event records, prior land treatment, and testimony when available.
6. Form one or more hypotheses for why severity/recovery differed.
7. Conduct a controlled follow-up observation or revisit after a meaningful interval.
8. Support a feature-level access, monitoring, or protection decision.
9. Return later and observe consequences rather than replacing the site with a completed-quest state.

## Possible explanations

The final explanation remains unset. Viable authored branches include:
- topography or moisture created a surviving patch;
- an older route/service break interrupted fuel continuity;
- previous maintenance or vegetation management changed local conditions;
- local weather made one sector burn differently;
- the first report sampled a severe patch and overgeneralized;
- the second report sampled a refuge and overgeneralized;
- later regrowth changed conditions between reports;
- a Pokémon species influenced only a small local ignition or vegetation pattern, if official ecology and PTU mechanics later support that species;
- two or more causes acted together.

Sabotage is not required.

## NPC and faction roles

Potential reusable roles:
- route custodian with authority over reopening;
- field ecologist or recovery monitor;
- local resident with pre-fire knowledge;
- logistics operator affected by closure;
- emergency-response trainer or ranger analogue;
- researcher maintaining long-term comparison plots;
- caretaker who knows current Pokémon use but not the broader fire history.

Each actor must possess only information explicitly received or observed. Shared employment or faction membership never grants automatic knowledge.

## Consequence branches

Possible outcomes should be feature-scoped.

A route can reopen while a refuge remains restricted.

A monitoring area can remain closed even after the main corridor reopens.

A service detour can be removed while another emergency path stays active.

A later survey can revise the severity interpretation without deleting the historical report that used older evidence.

A management decision can be reviewed if new evidence arrives, using the existing decision-dependency, review, and selective-consequence-repair model rather than a global world reset.

## Reduced implementation

This version preserves the full narrative premise without requiring dynamic fire simulation.

Allowed representation:
- static or between-scene patch states;
- ordinary route graph edges;
- feature states such as `OPEN`, `RESTRICTED`, `CLOSED`, `MONITORING`, `REFUGE_OBSERVED`, `RECOVERY_UNRESOLVED`;
- provenance-backed observations;
- semantic-time revisits;
- explicit NPC receipt and belief updates;
- feature-level decisions and consequences;
- authored environmental presentation that never creates mechanics by itself.

Excluded from the reduced version:
- spreading flame;
- dynamic smoke LoS penalties;
- weather-driven fire propagation;
- tactical Fire Hazard generation;
- Burn application;
- environmental damage;
- forced evacuation movement;
- rescue/interception reactions;
- automatic Water-vs-fire suppression;
- species-triggered ignition mechanics;
- generalized autonomous hazard tactics.

## Full encounter version

A later engine-ready version may include a short active flare-up, controlled response scene, or threatened edge near an already burned landscape. This is optional and must not replace the slower investigation/recovery loop.

Possible mechanics, only when individually verified:
- smoke or obscured zones;
- changing hazard sectors;
- timed environmental transitions;
- safe/unsafe movement corridors;
- rescue/interception;
- knockback or forced movement near dangerous terrain only when the source effect actually causes it;
- environmental damage through the stateful damage pipeline;
- Burn through the verified status lifecycle;
- weather interactions;
- Move-specific suppression or terrain changes;
- Ability, Item, or Trainer Feature interactions;
- tactical AI choosing legal evacuation, protection, or suppression actions.

## Permanent capability dependencies

Targeting / footprints / range / LoS:
- ordinary audited geometry is usable;
- smoke-dependent visibility remains an additional unverified subfamily.

Base movement legality:
- sufficient for the reduced route graph;
- specialized traversal through debris, steep slopes, or temporary barriers requires exact rule verification.

Complete movement including push/pull/knockback/interception/forced movement:
- not required reduced;
- required full for rescue/interception or any authored forced displacement.

Core calculations:
- usable for existing deterministic PTU arithmetic;
- does not authorize fire-spread, smoke, heat, fuel, or ecological recovery formulas.

Action economy / initiative:
- usable once a valid tactical response action exists.

Full turn / round lifecycle:
- not required reduced;
- required full for timed flare-ups, spreading/changing zones, delayed collapse, or phase-linked environmental transitions.

Full stateful damage pipeline:
- not required reduced;
- required full for fire, smoke, impact, collapse, or other environmental battle damage.

Status lifecycle:
- not required reduced;
- required full for Burn or any persistent condition.

Terrain / weather / hazards / zones / reactions:
- reduced uses authored static world states only;
- full dynamic fire/smoke/weather/rescue behavior depends directly on these exact subfamilies.

Move-specific behavior:
- required for every Move used to suppress, ignite, clear, create weather, alter terrain, rescue, or fight.

Abilities:
- required for any actual Ability interaction with fire, heat, weather, smoke, terrain, or rescue.

Items:
- required for rules-level firefighting, protective, surveying, or rescue equipment.

Trainer Features / perks:
- required for specialized intervention, hazard mitigation, weather, rescue, or tactical interrupts.

AI legal-action infrastructure:
- usable once the underlying action contracts are verified.

AI tactical policy:
- blocking for generalized autonomous fire-response, rescue prioritization, dynamic hazard navigation, and coordinated evacuation tactics.

Minecraft / Cobblemon / Craftics adapter and playback:
- can present charred blocks, regrowth, smoke, closures, signs, NPCs, and route changes;
- cannot decide PTU damage, Burn, LoS penalties, hazard timing, species behavior, route authority, or causal world truth.

## PTU / Caelo boundary

The Narrative repository currently exposes Kairos source indexes but no adopted Caelo directory or fire-specific Ouros rules overlay.

The Kairos index points to PTU movement/terrain, status, hazards, terrain/weather, and encounter-creation sections. Those page references are research routing aids only.

Before full implementation, verify every Fire Hazard, Burn, weather, terrain, movement, reaction, Move, Ability, Item, Trainer Feature, and species-specific interaction against the active Ouros rules profile and current AutoPTU tests.

## Canon questions left open

- region and exact site;
- vegetation community;
- historical fire date and cause;
- whether the event was wildfire, prescribed fire, mixed-origin, or another disturbance;
- local fire-management institution;
- settlement exposure;
- route importance;
- existing monitoring program;
- official Pokémon species present;
- refuge significance;
- final explanation for the burn mosaic;
- which access/protection decision becomes canon after play.
