# Research Scan — Infrastructure, Service Interruption, Repair & Restoration — Pass 156

Status: PROVENANCE / NON-CANON RESEARCH. This file records external inspiration and design extraction. It does not establish Ouros canon.
Date: 2026-08-30

## Research question

How can Ouros make power plants, pumps, bridges, cable routes, stations, waterworks, workshops and other infrastructure feel persistent before and after an incident without turning every facility into a combat dungeon or inventing a utility-engine subsystem that PTU/Caelo and AutoPTU do not currently prove?

The target gap is continuity between ordinary operation, degradation, interruption, assessment, isolation, temporary service, repair, restoration and eventual repurposing. Existing Ouros layers already own travel, ports, workplaces, civic authority, hazards, disasters, material objects, case evidence and battle facts. This pass must not absorb those authorities.

## Existing-repository gap check

The recursive repository tree was inspected before writing and returned without truncation. Focused repository searches for infrastructure, utility, outage, restoration and maintenance did not identify a dedicated continuity layer with this scope.

Adjacent systems remain authoritative for their own domains:

- transport systems own journeys, schedules and vehicle/service movement;
- workplace systems own staffing and job participation;
- civic and institutional systems own mandates, offices and approvals;
- material culture owns physical object identity, custody and provenance;
- disaster/emergency concepts own emergency events and response episodes when authored;
- terrain/environment systems own environmental state when established;
- case/investigation systems own evidence and causal hypotheses;
- AutoPTU owns only tactical facts covered by BattleSpec and verified rules.

The missing layer is longitudinal service and asset continuity.

## Pokémon source patterns

### Kalos Power Plant and Lumiose City

Pokémon X/Y links a facility-level problem to a city-level service consequence. Team Flare diverts electricity from the Kalos Power Plant and Lumiose experiences a blackout; clearing the takeover is followed by restoration of city power and renewed access to Prism Tower.

Reusable structure:

1. a service asset exists for an ordinary regional function;
2. an incident affects that function;
3. the consequence propagates beyond the encounter location;
4. restoring access to the asset and restoring the service can be represented as separate world facts, even when the source game compresses them together.

Ouros adaptation: a battle inside or near an asset may produce an access or security fact. It must never silently produce `SERVICE_RESTORED` unless a separate authored world-state transition supports that result.

Source: Bulbapedia, Kalos Power Plant / Lumiose Gym / Pokémon X and Y. Public reference consulted 2026-08-30.

### Kalos Power Plant backup generation in animation

A separate animated continuity depicts a damaged plant whose backup generator continues to provide power. This is useful because it separates asset damage from total service loss.

Reusable structure:

`PRIMARY_ASSET_DAMAGED != SERVICE_ZERO`

A fallback source can keep a limited service alive while repair remains necessary.

Ouros adaptation: backup power, bypass pumps, temporary bridges or substitute routes are authored state, not generic automatic responses.

Source: Bulbapedia, Kalos Power Plant anime coverage.

### Valley Windworks

Valley Windworks presents an operating wind-generation site with visible turbines, a processing building, workers/owners and a surrounding ecology. The location remains a functioning place rather than existing only to host a villain encounter.

Reusable structure:

Infrastructure can have normal routines, staff knowledge, environmental relationships and public consequences before an adventure occurs. That normal state gives later disruption meaning.

Ouros adaptation: establish baseline service, users, inspection routines and local ecological relationships before introducing failure.

Source: Bulbapedia, Valley Windworks.

### New Mauville

New Mauville is a decommissioned power facility/project that persists physically after its original intended function ends, with Electric-type Pokémon inhabiting the site in some continuities.

Reusable structure:

`FORMER_DESIGN_PURPOSE != CURRENT_OPERATIONAL_STATE`

A map, sign, old work order or historical plan can accurately describe what a facility used to be without proving current operation.

Ouros adaptation: preserve decommission and repurposing events instead of deleting the old asset identity.

Source: Bulbapedia, New Mauville.

## Infrastructure restoration source patterns

### Department of Energy emergency response

The U.S. Department of Energy describes energy emergency response in terms of damaged systems, coordination, stabilization and reestablishment. It also distinguishes assessment and safety work from the act of restoring service.

Reusable high-level sequence:

DISRUPTION -> ASSESSMENT -> ISOLATION/STABILIZATION -> REPAIR OR SUBSTITUTE -> REESTABLISHMENT -> LATER NORMALIZATION

Ouros adaptation: use this as process grammar only. Do not import U.S. law, agencies, codes, contractor requirements or regulatory authority.

Source: U.S. Department of Energy, Office of Cybersecurity, Energy Security, and Emergency Response, Emergency Response.

### Qualified repair and inspection guidance

DOE public guidance also emphasizes that structural, electrical or gas-related safety issues can require assessment before service restoration. This supports a narrative distinction between physical repair completion and authorization/safety to return an asset to service.

Reusable structure:

`REPAIR_PERFORMED != SAFE_TO_REENERGIZE`

`SAFE_TO_REENERGIZE != SERVICE_ACTUALLY_RESTORED`

Ouros adaptation: any inspection or authorization must come from an institution already established in canon. The research does not create an Ouros code regime.

Source: U.S. Department of Energy, Hiring Qualified Contractors.

## PTU community and campaign-design cross-check

The public Pokémon Tabletop site’s Tales of Visiwa retrospective remains useful as a campaign-scale reference because it describes a long-running PTU region with exploration restrictions, dangerous wilds and persistent places that matter outside individual combats. It demonstrates that PTU campaigns can support region-level institutions and location continuity without every world fact needing a dedicated combat mechanic.

This source is community/campaign evidence only. It is not mechanical authority.

Source: Pokémon Tabletop RPG, “Tales of Visiwa: A Retrospective.”

Additional public PTU campaign listings and community discussions were reviewed for urban, institutional and long-running campaign structures. They reinforce that tables routinely author regional infrastructure as setting material, but they do not establish universal PTU rules for utilities, repair, engineering, outages or reconstruction.

## Design extraction for Ouros

### Separate the physical asset from the service it provides

A pump can exist while not pumping. A bridge can physically stand while closed. A generator can operate while only part of a district receives power. A repaired cable may await inspection. A station may remain decommissioned even though its building is intact.

Therefore use at least two state axes:

- asset condition;
- service state.

Do not collapse either into the other.

### Preserve dependencies explicitly

A service interruption can propagate to dependent locations without inventing causality. The dependency must already be authored.

Example:

`substation-17 -> clinic-cold-storage`

If the substation is interrupted and no alternate source exists, the dependent service can be reevaluated. The system must not assume every nearby building shares that dependency.

### Temporary service deserves persistent history

A generator, detour, temporary footbridge, rented pump, alternate radio mast or manual process can keep a community functioning. Temporary solutions create excellent later hooks because they accumulate cost, wear, social expectations and route changes without requiring catastrophe.

`TEMPORARY_SERVICE != PERMANENT_REPAIR`

### Restoration can be partial

A district can regain critical service before full capacity. A bridge may reopen to pedestrians before freight. A station may operate one platform. A pump may hold water below an emergency threshold without restoring normal drainage.

Avoid a single global `fixed=true` flag.

### Old infrastructure is environmental storytelling

Retired conduits, patched walls, old route signs, incompatible replacement parts and maintenance annotations can show historical change. These artifacts support hypotheses. They do not automatically prove why a project was abandoned or who caused an incident.

### Repair should create characters and institutions

Useful recurring archetypes include:

- a veteran inspector who remembers obsolete layouts;
- a junior engineer with accurate current drawings but little historical context;
- a dispatcher who sees service reports but not field conditions;
- a caretaker whose job survived the asset’s original purpose;
- a contractor or craft specialist who knows one subsystem deeply;
- residents or businesses who maintain local workarounds;
- a field technician who can identify symptoms but not institutional causes.

No archetype receives automatic technical authority beyond authored qualifications.

## Reusable quest structures

### The service is back, but only partly

Players hear that “the power is back.” Investigation reveals that emergency generation restored a clinic and transit control while residential blocks remain disconnected. No testimony has to be false; different speakers mean different restoration scopes.

### The repair changed the route

A temporary bypass becomes socially important. When permanent repair is finally ready, some businesses and residents prefer the new route. The conflict is civic and logistical rather than tactical.

### The abandoned line still appears on maps

Old maps, current maintenance records and physical traces disagree because the line was decommissioned in stages. The mystery is chronology and scope, not sabotage by default.

### A battle clears access, nothing more

Hostile actors or wild Pokémon prevent technicians from reaching a safe staging area. AutoPTU can resolve the tactical confrontation. Ouros then decides whether assessment, isolation, repair and restoration occur based on separate facts.

### The temporary fix becomes the long-term problem

A bypass installed during an emergency remains in service months later. Its limitations now affect another system. The players can investigate why permanent work stalled without the answer being predetermined as corruption or incompetence.

## Environmental-storytelling seeds

- a row of newer poles ends abruptly at an older substation;
- replacement panels carry two generations of labeling conventions;
- a closed bridge still has maintained lighting because another service crosses it;
- an abandoned pump house contains fresh inspection tags on one surviving subsystem;
- a former power project has become habitat without losing its recorded engineering history;
- a station concourse is active while an old platform remains sealed;
- a district’s shops share visible temporary generators after a service event;
- maintenance paint shows that the same wall has been opened repeatedly over decades.

## Hard provenance safeguards

`FACILITY_DAMAGED != SERVICE_INTERRUPTED`

`SERVICE_INTERRUPTED != CAUSE_KNOWN`

`OUTAGE_REPORTED != OUTAGE_SCOPE_PROVEN`

`ACCESS_CLEARED != REPAIR_COMPLETE`

`REPAIR_COMPLETE != SERVICE_RESTORED`

`SERVICE_RESTORED != ORIGINAL_CONFIGURATION`

`TEMPORARY_BYPASS != PERMANENT_REPAIR`

`MAP_MARKS_ACTIVE != CURRENTLY_ACTIVE`

`DECOMMISSIONED != OWNERLESS`

`POWER_OFF != SAFE_TO_ENTER`

`WORK_ORDER_EXISTS != WORK_STARTED`

`BATTLE_WON != EQUIPMENT_FIXED`

`POKEMON_MOVE_USED_NEAR_ASSET != TECHNICAL_REPAIR_COMPLETED`

## PTU/Caelo assumptions that remain UNKNOWN

This scan found no project-approved basis for silently creating any of the following:

- a universal Engineering or Repair subsystem;
- generic infrastructure hit points;
- universal structural-collapse rules;
- electrical-network simulation;
- water-network simulation;
- universal power-generation values for Pokémon;
- generic Move/Ability/Feature effects on civic infrastructure;
- repair DCs, costs or durations;
- universal safety inspection rules;
- building/electrical/plumbing codes;
- utility ownership or regulatory law;
- generic contractor licensing;
- automatic service restoration after combat;
- automatic infrastructure damage from ordinary overworld Minecraft physics;
- universal service-priority rules.

Any exact PTU/Caelo Skill, Move, Ability, Item or Trainer Feature proposed for technical work must be source-checked individually before canon approval and, when tactical, against current AutoPTU contracts.

## Candidate scope for Pass 156 design

The design layer should own only persistent continuity records for:

- infrastructure asset identity and functional role;
- authored service dependencies;
- service interruption episodes;
- condition assessments;
- work orders and repair episodes;
- isolation/stabilization facts;
- temporary bypass/substitute service;
- restoration events and restoration scope;
- decommissioning and repurposing history.

It must leave tactical battle facts to AutoPTU and presentation to Minecraft/Cobblemon/Craftics.