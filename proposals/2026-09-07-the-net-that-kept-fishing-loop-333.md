# The Net That Kept Fishing — Pass 333

Status: PROPOSED / NON-CANON
Date: 2026-09-07
Region anchor: Marea Interior District
Primary existing location: Puerto Bruma

## Premise

After rough coastal conditions, a large section of old fishing net is found snagged near the working edge of Puerto Bruma's sheltered bay. The gear is no longer attended by any operator, yet fresh evidence suggests that wild Pokémon have recently interacted with it and at least one wildlife incident may be linked to it.

A faded identifier on part of the gear appears to match an old record.

That match creates a lead. It does not solve the incident.

The central question is not simply who owns the net. The player has to reconstruct what happened to a persistent object whose use, location, custody and effects may have changed several times.

## Canon-safe starting point

This proposal reuses established canon only:

- Puerto Bruma is a working bay town and transfer point between coastal traffic and inland producers;
- Puerto Bruma has a ferry landing and market;
- Marea Field Office coordinates wildlife incidents and practical assistance;
- Tideglass Archive preserves old local records;
- Mara Veyra, Dr. Nerea Sol and Taro Min already exist and have compatible responsibilities.

This proposal does not canonize:

- a Puerto Bruma commercial fishing fleet;
- a new fishing guild;
- a specific Pokémon population;
- a particular net owner;
- a crime;
- a final cause;
- local fishing regulations;
- any new PTU mechanic.

The gear may have arrived from outside the bay.

## Persistent features

Candidate feature IDs are design placeholders until canon promotion:

- `puerto_bruma.bay_working_edge`
- `puerto_bruma.ferry_approach`
- `puerto_bruma.derelict_gear_site_01`
- `puerto_bruma.temporary_recovery_staging`
- `tideglass.gear_record_collection`

The derelict gear itself must receive a persistent world-object ID independent of its current position.

Example:

`world_object.derelict_gear.net_01`

## Opening observation

A bay worker, ferry operator or Field Office observer reports an unattended net section where it should not normally remain.

The first report records only what was observed:

- feature/location;
- semantic time;
- visible extent;
- whether a mark is visible;
- whether wildlife interaction was directly observed;
- immediate navigation/access concern;
- observer identity.

It does not write ownership, origin, deliberate dumping, current hazard radius or ecological impact as fact.

## Existing NPC participation

### Mara Veyra

Mara can coordinate the immediate response and decide which local access restriction is justified by received evidence. Her job is to keep the bay functioning while avoiding unsupported accusations.

She can know:

- reports delivered to the Field Office;
- current feature access decisions;
- recovery attempts she authorized or was told about.

She does not automatically know:

- gear origin;
- who last used it;
- whether a mark is current;
- what Nerea observed before a report is delivered;
- what Taro found in archive records before he communicates it.

### Dr. Nerea Sol

Nerea can document current biological/habitat observations and distinguish observed effects from inferred origin.

A fresh wildlife interaction can support current hazard assessment while saying nothing definitive about who lost the gear.

### Taro Min

Taro can locate historical records associated with a visible identifier, old recovery notice or prior bay incident.

An archive match can establish that a code once referred to a registered object/operator record. It does not establish continuous ownership or current responsibility.

## Candidate supporting NPCs

These remain PROPOSED and should only be promoted if the setting needs them:

- a ferry or harbor worker who made the first report;
- an outside operator or family linked to an old gear mark;
- a trained recovery specialist;
- a resident who remembers an earlier storm or cleanup.

Each should own only the observations and records they actually received.

## Evidence chain

Useful evidence can include:

- original sighting report;
- current photographs/field notes represented as world evidence, not player omniscience;
- faded gear mark;
- an old registry or ownership record;
- a prior loss report;
- absence of a loss report where records are known to be incomplete;
- previous observed positions;
- snag points;
- current wildlife interaction evidence;
- ferry/navigation reports;
- weather or current observations already available through approved world systems;
- recovery-attempt records;
- custody after removal.

The player should be able to build a defensible history without necessarily obtaining a complete one.

## Plausible explanations

Keep several explanations viable until evidence narrows them:

- the gear was lost accidentally and drifted into the bay;
- it was reported lost elsewhere but the report never reached Puerto Bruma;
- an old owner record is correct but a later transfer is missing;
- the marked section became part of a larger debris mass assembled from multiple origins;
- a storm moved gear that had previously been snagged somewhere else;
- somebody recovered part of the gear earlier but not all of it;
- the mark belongs to the gear but says little about the final loss event;
- deliberate dumping occurred, but only if later evidence establishes it;
- multiple events contributed to the current state.

## Decision pressure

The loop should create two simultaneous obligations.

Immediate obligation:

Protect people, navigation and affected Pokémon at the current feature.

Longer obligation:

Reconstruct enough provenance to decide what should happen to the gear, records and any follow-up responsibility.

These obligations can resolve at different times.

## Full encounter version

A mechanically rich version can make the net and surrounding water part of a tactical rescue/containment encounter.

Possible authored elements:

- fixed and drifting net sections;
- an entangled or cornered Pokémon that should survive the encounter;
- moving water or wave-driven displacement;
- unstable footing near the working edge;
- ferry or worker exclusion zones;
- timed recovery windows;
- cutting/recovery equipment;
- wild Pokémon reacting defensively instead of fighting to defeat all opponents;
- protect/rescue objectives;
- a route that changes after gear shifts.

This version requires verified support in the exact capability families listed in the Pass 333 readiness snapshot. No adapter may improvise missing PTU rules.

## Reduced encounter version

The same narrative premise can run now without tactical net simulation.

Use the world layer for:

- discovery;
- access restriction;
- evidence collection;
- report delivery;
- archive lookup;
- current wildlife condition as authored semantic state;
- specialist recovery or staged removal between tactical scenes;
- custody and aftermath.

If combat is needed, keep the net outside the rules problem:

- use an ordinary static battle space;
- block unsafe cells rather than creating an unverified entanglement hazard;
- keep any trapped/noncombatant Pokémon outside BattleSpec unless the engine has verified support for the required objective behavior;
- let AutoPTU resolve only ordinary combat legality and outcome;
- return a narrow semantic result such as `IMMEDIATE_SITE_SAFE_FOR_RECOVERY_TEAM`.

The battle result cannot establish gear origin, ownership, liability, ecological effect or successful specialist disentanglement.

A fully noncombat version is also valid.

## World-state model

Candidate semantic states:

- `GEAR_REPORTED`
- `GEAR_LOCATION_OBSERVED`
- `GEAR_MARK_OBSERVED`
- `GEAR_RECORD_MATCH_FOUND`
- `LOSS_REPORT_FOUND`
- `LOSS_REPORT_NOT_FOUND_IN_SEARCHED_COLLECTION`
- `WILDLIFE_INTERACTION_OBSERVED`
- `NAVIGATION_CONCERN_REPORTED`
- `FEATURE_RESTRICTED`
- `RECOVERY_ASSESSMENT_REQUESTED`
- `RECOVERY_ATTEMPTED`
- `GEAR_STABILIZED`
- `GEAR_PARTIALLY_RECOVERED`
- `GEAR_RECOVERED`
- `GEAR_TRANSFERRED_TO_CUSTODY`
- `FEATURE_REOPENED`
- `FOLLOWUP_MONITORING_ACTIVE`

These are world semantics, not PTU statuses.

## Consequences and revisits

The quest should continue after the visible net disappears.

Possible later consequences:

- a second fragment appears elsewhere;
- a prior position report explains how the object moved;
- an old operator receives a correction or inquiry;
- Tideglass preserves a revised incident history;
- the ferry approach reopens while another feature remains monitored;
- habitat observations improve after removal;
- removal reveals that part of the gear had become incorporated into a local feature;
- a cleanup program gains a new reporting protocol;
- another group finds debris carrying a different mark, proving that the first event was not a complete explanation.

## Rivalry / faction potential

The conflict should come from legitimate priorities rather than cartoon antagonism.

Potential positions:

- operations staff want the navigation hazard handled quickly;
- researchers want enough documentation to preserve provenance;
- recovery specialists may judge immediate removal unsafe or damaging;
- an identified historical owner may dispute current responsibility while still cooperating with recovery;
- residents may care more about visible cleanup than evidentiary certainty.

None of these positions requires deception.

## Canon promotion gates

Before promotion, decide:

- whether Puerto Bruma has local fishing activity or the gear definitely arrived from elsewhere;
- exact feature within the bay;
- whether any species is specifically involved;
- what institution has authority over recovery/custody;
- whether a gear-mark registry exists locally or only through historical records;
- whether the incident joins the Thin Delivery Season arc or remains an independent recurring thread;
- final provenance, if the story ever needs one;
- whether combat occurs at all.

## Narrative value

This loop adds a persistent object whose history matters as much as its current location. It grows directly from Puerto Bruma's existing bay infrastructure, gives Mara/Nerea/Taro different evidence roles, supports revisits and institutional memory, and can run at current engine readiness without forcing entanglement, currents or rescue mechanics into Minecraft.