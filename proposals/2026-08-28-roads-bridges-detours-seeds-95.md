# Ouros Roads, Bridges & Detours Seeds — Pass 95

Status: NON-CANON proposals. These are reusable original situation seeds built from Pass 95 research. Names, institutions, road technologies and regional placements remain unassigned until canon review.

## Design intent

These seeds make route changes visible in familiar places. They favor evidence, access decisions, local consequences and recurring geography over disposable road encounters. A road problem can create investigation, logistics, social pressure, ecology, maintenance or tactical content without forcing combat.

## The Repair Finished, the Test Did Not

A crossing looks normal again. Scaffolding is gone and the visible repair crew has left, but the operational restriction remains because verification has not closed.

Useful tensions:
- residents assume the closure notice is stale;
- a courier has a time-sensitive delivery;
- a local business planned around the announced repair date;
- a maintenance record says work complete but not verified;
- an official map and physical barriers disagree temporarily.

Resolution depends on the verification/authority chain. Players cannot remove the restriction by proving that the structure looks repaired.

## One Span Open, One Crossing Closed

A multi-surface or multi-approach crossing retains limited access. Pedestrians or another authored access class may pass while heavier/general traffic remains diverted.

The narrative value comes from unequal effects. Some residents recover ordinary routines while freight, services or visitors still take the long route.

No universal vehicle or weight rule is implied. The exact allowed classes must be authored.

## The Detour Became the Busy Road

A temporary bypass remains active long enough to reshape daily life around it.

Possible consequences:
- a quiet settlement sees new customers and noise;
- a roadside service opens temporarily;
- a courier changes its ordinary circuit;
- children or residents learn a new crossing routine;
- wildlife observations shift;
- maintenance wear appears on infrastructure not built for the new use;
- the old main road reopens, but some people prefer the bypass.

The closing decision creates a second story: retire the detour, keep it as a secondary road, convert part to a path, or leave the question open for civic review.

## The Bridge That Passed Inspection but Stayed Closed

Maintenance evidence supports the physical asset, yet another dependency remains unresolved.

Possible causes:
- an approach road is still blocked;
- public safety barriers have not been removed by the responsible authority;
- a linked service window has not resumed;
- a worksite downstream is still active;
- a temporary environmental mitigation remains in force;
- the public notice system has not yet received the authoritative state change.

This seed teaches that technical verification and traveler access are different records.

## The Sign Says Open

A traveler reaches a route where the physical sign, map revision and current operational state disagree.

Potential evidence:
- timestamped notices;
- photographs;
- local testimony;
- maintenance completion record;
- network update;
- courier route log;
- barrier state;
- later correction.

There may be no misconduct. One information surface may simply be behind another.

## The Old Ford Returns

A permanent crossing becomes unavailable and a historically used crossing point appears in local memory as a possible alternative.

The old route is not automatically usable. It may now be:
- private or restricted space under local canon;
- habitat;
- physically changed;
- seasonally unsafe;
- remembered incorrectly;
- usable only by a subset of travelers;
- absent entirely despite the old map.

The hook connects oral history, cartography, survey and travel without inventing a traversal solution.

## The Wildlife Crossing Moved Before the Road Did

Repeated observations suggest that Pokémon are using a different crossing area than older monitoring records show. The active detour now overlaps that area.

Players can help gather evidence, adjust travel timing, speak to affected residents or support temporary monitoring.

A battle is optional. Species presence alone never establishes cause, migration, danger or policy.

## The Road Closed for the Right Reason, Explained Wrong

Officials correctly restrict a segment after an obstruction or repeated incident, but the first explanation is incomplete.

The investigation may reveal:
- two separate physical causes were conflated;
- the blockage was a consequence of another environmental event;
- a popular species was blamed because it was visible nearby;
- old road works altered drainage/access in a way nobody initially connected;
- the evidence remains insufficient for a single cause.

The closure can remain justified even after the story behind it changes.

## The Temporary Crossing Became Familiar

A temporary bridge, causeway, footpath or other authored bypass remains long enough to become part of local routine.

When the main connection returns, different groups may value the temporary alignment for different reasons: faster walking access, habitat observation, heritage from the crisis period, service access or simple habit.

Civic/Public Works decides any permanent future. Road Operations only preserves what exists and how it is being used.

## The Drawbridge Window Keeps Shifting

Conditional seed. Use only if the region canon supports a movable or scheduled crossing.

Road users complain that expected access windows keep changing. Maritime/service records, maintenance state and actual observed configuration do not initially line up.

Possible explanations include:
- service schedule changes;
- a mechanism under temporary operating restrictions;
- notice propagation lag;
- a one-off vessel movement;
- different actors referring to different windows;
- unresolved evidence.

Do not turn the bridge mechanism into tactical moving terrain unless AutoPTU supports the exact behavior.

## The Medicine Took the Long Way

A routine but time-sensitive delivery cannot use its expected corridor because of an access restriction. The courier must use a valid alternate connection, hand the package to a different service, or wait for an operating window.

The stakes come from logistics and relationships rather than a forced ambush. If no legal alternate route exists, the world should say so instead of spawning one.

The seed is structurally inspired by Pokémon stories where borrowed transport and road access affect urgent delivery, but all Ouros actors, locations and circumstances must be original.

## The Road Everyone Calls New Is the Old Alignment

A road described locally as “the new road” follows much of an older alignment that had been abandoned or repurposed.

Old photographs, property maps, drainage structures, habitat observations and resident memories reveal several generations of use. The hook can lead into heritage, public works, ecology or a disagreement about which segment a historical record actually describes.

## Mystery — Four Closure Notices, Two Actual Restrictions

Four public notices appear to document repeated closures over a month.

Investigation cross-checks:
- segment IDs;
- publication times;
- effective times;
- replacement/supersession links;
- barrier observations;
- maintenance records;
- map revisions;
- traveler logs.

Possible outcome: two notices were updates to the same continuous closure, one applied only to a different access class, and one was superseded before becoming effective. Other evidence patterns are valid. The system should not force a culprit.

## Mystery — Three Bridge Reports, One Crossing

Reports from residents describe “the bridge” differently: one says closed, another says open, another says work is still underway.

They may all be accurate if they refer to different surfaces, approaches, time windows or traveler classes.

The mystery rewards precise identity and timestamps rather than hidden deception.

## Encounter — Bridge Approach Withdrawal

Full premise:

A restricted crossing develops a territorial or hostile incident near one approach while workers or travelers still need to clear the immediate area. The ideal tactical objective values withdrawal and access control, potentially using Intercept and forced movement.

Full dependency profile:

```yaml
encounter: Bridge Approach Withdrawal
requirements:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Reduced version now:

Close the bridge fully before combat. Evacuate workers and ordinary travelers through world-state resolution. Keep equipment and noncombatants out of the grid. Use a static safe approach arena with no falling, moving bridge, water, wind, traffic or structural hazard rules. Ouros chooses the combatants explicitly. AutoPTU resolves only the battle. Securing the approach does not reopen the crossing.

## Encounter — Detour Wildlife Crossing

Full premise:

A temporary bypass intersects a recurring wildlife-use area. The ideal encounter supports withdrawal, route clearing, territorial behavior and non-KO objectives.

Key blockers:
- objective-aware AI tactical policy;
- dynamic terrain/zones/reactions if crossing space matters;
- complete exact movement interactions if Intercept/forced displacement matters;
- adapter/playback.

Reduced version now:

Close the bypass before battle and move ordinary traffic away. Select only the actors that actually enter the encounter. Use a static neighboring arena. Afterwards, Conservation/Wildlife interprets the ecological evidence and Road/Travel systems decide whether the bypass can resume.

## Encounter — Controlled Crossing Service Window

Conditional full premise:

A disturbance occurs while a movable/scheduled crossing is changing between transport uses.

Full version would require the exact supported moving-zone, reaction, route-control and playback behavior.

Reduced version:

Freeze the world crossing in one configuration before the BattleSpec. Pause ordinary road and linked service movement. Resolve a static fight away from the mechanism. After the result, the operating systems decide whether the next window proceeds.

## Long arc — A Road Learns Its Crossing

The same corridor remains relevant across many visits.

Opening phase: establish ordinary users, nearby places, local shortcuts, service traffic and baseline wildlife observations.

Restriction phase: a limited problem changes only part of access. People adapt differently depending on where they live and what movement they need.

Detour phase: a temporary route becomes part of daily life. Economic, social and ecological consequences appear away from the original blocker.

Work phase: assessment, procurement, repair or a civic project becomes visible in-world. Old rumors can coexist with better technical evidence.

Verification phase: the physical work appears complete while testing, public information or access authorization still changes in steps.

Reopening phase: the main connection returns, perhaps partially at first. The detour does not vanish from memory or geography.

Later callback: a former bypass, old bridge record, changed wildlife route, recurring worker, shop opened during the detour or outdated map makes the earlier event useful again.

The corridor accumulates state and memory without a progression bar or abstract infrastructure level.

## Canon review questions created by these seeds

The seeds deliberately leave open:
- which Ouros regions have roads or engineered bridges;
- what transport modes exist;
- who has authority to restrict or reopen a crossing;
- what access classes exist;
- whether movable crossings exist;
- what public-notice practices are normal;
- what engineering/inspection professions exist;
- whether any Pokémon have established road-work roles;
- what old alignments are culturally or ecologically significant.

No seed should silently answer these questions during generation.
