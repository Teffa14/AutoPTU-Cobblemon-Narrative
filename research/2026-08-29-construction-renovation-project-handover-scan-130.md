# Ouros Narrative Research — Construction, Renovation, Project Handover — Pass 130

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-29

## Research objective

Identify reusable narrative structures for physical construction, renovation, redevelopment and handover without inventing Ouros building law, engineering rules, labor law, procurement rules, ownership, permitting, inspection authority or PTU mechanics.

This pass was selected only after inspecting the complete recursive repository tree at narrative head `537b597e88f406e4ad907bceca2ba12ef707e334` and checking neighboring systems.

The repository already owns:

- collective decisions and public-works sponsorship in Civic Governance;
- faults, maintenance work orders, repairs and verification after a facility exists in Facility Maintenance;
- post-damage use restrictions and reentry decisions in Building Safety;
- procurement and supplier fulfillment in Procurement;
- material identity and provenance in Material Culture;
- workforce identity and workplace state in Workplaces;
- route/service effects in Travel and transport layers;
- ecology, conservation, land, archaeology/history, utilities and hazards in their own owner systems.

The uncovered continuity gap is the execution layer between an authored project decision/scope and a completed physical handover: work packages, construction-phase state, discovered conditions, scope revisions, temporary works, partial completion, inspection/verification, commissioning where applicable, residual work, record handoff and transition into normal facility/service ownership.

## Source hygiene

The sources below are used only for high-level structures, chronology patterns, evidence boundaries and world-state design lessons.

No protected dialogue, distinctive character arc, exact plot, proprietary procedure, construction standard, legal doctrine, threshold, contract clause or engineering calculation is copied into Ouros.

Real-world sources are not authority for Ouros institutions. Their terminology is retained here only for provenance; the design layer uses neutral authored states.

## Pokémon source 1 — Unova Route 4 across Black/White and Black 2/White 2

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Unova_Route_4
- https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Black_2_and_White_2/Part_5

Observed high-level structure:

In Black and White, Route 4 is visibly under construction, with incomplete paved sections and multiple work sites. Two years later the corridor has changed substantially. Black 2 presents extensive development, while White 2 presents development that stopped after ancient ruins were discovered.

Reusable design lessons:

1. Construction itself can be a persistent world phase rather than a transition hidden between scenes.
2. A corridor can remain traversable while neighboring work continues.
3. The same initial project can branch because a later discovery changes what work may continue.
4. A discovery does not automatically tell the construction system what the discovery means. Archaeology/history, conservation, utilities or another owner system must interpret it.
5. `WORK_PAUSED_FOR_DISCOVERY` can be a valid long-lived state without implying cancellation.
6. A future visit should show accumulated changes rather than regenerating the original worksite.

Ouros transformation:

A project can preserve versioned scope and phase history. When an unexpected feature is found, the project records location, discovery time, affected work package and pause boundary, then hands the evidence to the correct owner. Work outside that boundary may continue if authoritative state permits it.

Do not infer from the Pokémon source that Ouros has the same construction technology, archaeology rules, road standards or approval process.

## Pokémon source 2 — Cold Storage replaced by Pokémon World Tournament

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Cold_Storage
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_World_Tournament
- https://bulbapedia.bulbagarden.net/wiki/Driftveil_City

Observed high-level structure:

A working logistics/warehouse district south of Driftveil later contains a major tournament facility where Cold Storage previously stood. The redevelopment changes the site's function and contributes to broader changes in the city.

Reusable design lessons:

1. Redevelopment should preserve site lineage even when a former structure is demolished.
2. `OLD_USE_ENDED`, `DEMOLITION_COMPLETE`, `NEW_CONSTRUCTION_COMPLETE`, `FACILITY_HANDED_OVER` and `NEW_SERVICE_OPERATIONAL` are different facts.
3. A new destination can change nearby businesses, traffic, lodging, routes and public identity after construction is finished.
4. Physical redevelopment can become a long-term historical reference for later quests.
5. A former use may survive in archives, maps, foundations, utility alignments, memories or place names even when the structure no longer exists.

Ouros transformation:

Keep stable land/location identity and explicit structure lineage. A redevelopment project creates successor structures and use relationships rather than deleting the former world record.

## Pokémon source 3 — PWT construction-site appearance in Pokémon Adventures

Source:

- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_World_Tournament

Observed high-level structure:

The manga depicts the future PWT location while construction is still underway before the completed facility becomes the familiar destination.

Reusable design lesson:

A named future facility may exist narratively before it exists operationally. Characters can encounter its worksite, surrounding routes and discoveries during construction without the finished service being available.

Ouros transformation:

Separate `project identity`, `worksite present`, `structure physically present`, `handover`, and `service launch`.

## Pokémon source 4 — Development can alter a city's supporting systems

Sources:

- https://bulbapedia.bulbagarden.net/wiki/Driftveil_City
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_World_Tournament

Observed high-level structure:

The PWT is linked with Driftveil's later development, tourism and changed built environment.

Reusable design lesson:

A completed project should emit handoffs to other world systems. Construction completion alone should not directly simulate every downstream effect.

Example Ouros handoffs:

- Hospitality decides whether lodging capacity changes;
- Road/Transit systems decide service effects;
- Commercial systems decide vendor activity;
- Events decide programming;
- Public Memory stores changed identity;
- Workplace systems create actual jobs only when institutions establish them.

## Real-world source 1 — GSA completion versus closeout

Sources:

- https://www.gsa.gov/real-estate/reimbursable-services-program/frequently-asked-questions/process
- https://www.gsa.gov/real-estate/reimbursable-services-program/frequently-asked-questions/customer-letters

Research date context: pages available 2026-08-29; GSA page reports updates in August 2026.

Observed high-level structure:

The public process distinguishes a point when work is sufficiently complete for intended use from later administrative/financial closeout. Remaining punch-list work may still exist at the earlier milestone.

Reusable design lessons:

1. Physical usability and total project closure are separate.
2. Residual work can remain after a bounded scope begins use.
3. Completion can be scoped to one work package or area rather than the whole program.
4. Final records may arrive after occupants/services begin using the result.

Ouros transformation:

Use neutral states such as `USE_READY_FOR_SCOPE`, `RESIDUAL_WORK_OPEN`, `HANDOVER_IN_PROGRESS`, and `PROJECT_RECORD_CLOSED` rather than importing legal terms or contract rules.

## Real-world source 2 — U.S. Department of Energy commissioning

Source:

- https://www.energy.gov/cmei/femp/commissioning-federal-buildings

Observed high-level structure:

Commissioning is described as a quality-assurance process that can include design review, functional testing, documentation and operator training to verify systems perform as intended.

Reusable design lessons:

1. Installation does not prove operational performance.
2. A system can be physically present while verification remains open.
3. Documentation and operator handoff can be separate deliverables.
4. Verification can produce defects or adjustments without implying total project failure.

Ouros transformation:

Where a canonized technology and competent institution exist, a project may create `verification_requirement` and `commissioning_record` objects. These records never invent engineering tests; exact checks must be authored from the relevant technology/facility system.

## Real-world source 3 — FHWA partial/final acceptance pattern

Sources:

- https://highways.fhwa.dot.gov/sites/fhwa.dot.gov/files/docs/federal-lands/specs/archives/14311/fp-03met.pdf
- https://www.fhwa.dot.gov/construction/cpmi04gg.cfm

Observed high-level structure:

Public highway material separates inspection/acceptance of completed portions from final acceptance of the whole project and records incomplete/corrective work when an inspection finds remaining issues.

Reusable design lessons:

1. A project area can transfer in pieces.
2. Inspection is an evidence-producing event; it does not rewrite what was physically completed earlier.
3. A failed or partial inspection should create bounded corrective work rather than resetting all progress.
4. Responsibility for a completed portion can change at a handover milestone while other work remains active elsewhere.

Ouros transformation:

Support phase- and scope-specific handover. Never infer legal responsibility from the real-world source; Ouros canon defines who owns, operates, maintains or accepts each asset.

## Cross-source synthesis

The strongest reusable pattern is a chain of independent truths:

`PROJECT_AUTHORIZED`
→ `EXECUTION_SCOPE_ACTIVE`
→ `WORK_PACKAGE_STARTED`
→ `PHYSICAL_PROGRESS_RECORDED`
→ `DISCOVERY_OR_CHANGE_RECORDED`
→ `WORK_PACKAGE_COMPLETED`
→ `VERIFICATION_PERFORMED`
→ `USE_READY_FOR_SCOPE`
→ `OPERATOR_HANDOVER`
→ `SERVICE_OWNER_ACTIVATES`
→ `RESIDUAL_WORK_CLOSED`
→ `PROJECT_RECORD_CLOSED`

Not every project uses every step. The chain is a state vocabulary, not a universal procedure.

## Important non-equivalences

- approved project != work started;
- work started != access closed everywhere;
- materials delivered != installed;
- installed != verified;
- work package complete != entire project complete;
- structure complete != safe/authorized for every use;
- use-ready != service operational;
- service operational != residual work closed;
- demolition complete != site history erased;
- discovery made != discovery interpreted;
- drawing revised != field work changed;
- Minecraft blocks placed != authoritative construction progress;
- battle victory != project acceptance.

## Discovery-driven narrative patterns

Unexpected discoveries are especially useful because they create cross-system stories without requiring villainy.

Candidate discovery owners:

- archaeology/history for ruins, artifacts or earlier structures;
- utilities for undocumented service lines;
- land/boundary system for geometry conflicts;
- conservation/ecology for habitat or active nesting;
- pollution/waste for unknown material or contamination evidence;
- water/drainage for unexpected flow/path;
- building safety for unsafe existing structures;
- case/evidence for suspicious or contested objects.

Construction stores the pause and scope consequence. The specialist owner stores interpretation.

## Persistent environmental storytelling opportunities

A long project can leave:

- temporary paths that become permanent shortcuts;
- old access gates after the work entrance moves;
- phased pavement or masonry showing different construction periods;
- a former wall preserved inside a new building;
- signage referring to an earlier project stage;
- temporary shops or worker food stalls that survive completion;
- unused foundations from a cancelled scope;
- a relocated tree, shrine, habitat feature or public object when canon supports that decision;
- old project photographs and survey marks;
- different local names for the pre-project and post-project place.

These are worldbuilding candidates, not automatic canon.

## PTU / Caelo cross-check

Internal source scan reviewed:

- `research/2026-08-18-source-scan.md`
- `design/engine-readiness-snapshot-pass-129.md`

The PTU/Caelo evidence supports central plots, character arcs, sandbox jobs, wild encounters and authored location mechanics when a governing source defines them. It does not provide a generic construction simulator.

Keep UNKNOWN unless exact governing rules are found:

- construction Skill DCs;
- universal demolition actions;
- structural HP for ordinary buildings;
- falling-object damage;
- scaffold/fall hazards;
- moving machinery zones;
- lifting/carrying construction loads beyond exact capability rules;
- concrete/soil/material strength calculations;
- species-based engineering competence;
- Type-based immunity to worksite hazards;
- universal Move-based excavation, welding, cutting, lifting or repair productivity;
- Trainer Feature authority to inspect or accept work;
- automatic service commissioning from a successful Skill Check.

A Pokémon may have an authored workplace role only through existing Agency/Work state and exact supported capabilities. Species flavor alone cannot qualify it for construction work.

## Engine evidence checked live

AutoPTU-Java head during this pass:

`80f08b5d66f3451f70743ac0d4717f3a3dd21a0b` — `Derive intercept Justified bonus from server state (#275)`.

This is unchanged from Pass 129. It remains specific evidence for a bounded Intercept route and does not establish the whole complete-movement family.

AutoPTU head during this pass:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

This is unchanged from Pass 129 and explicitly presentation-only.

## Design direction for Pass 130

Add a construction/renovation execution-and-handover continuity extension that:

- consumes an already-authorized project or private/institutional project basis;
- preserves scope versions and work packages;
- records physical progress without simulating engineering;
- allows partial works and partial handover;
- handles discovered-condition pauses and owner-system referrals;
- separates verification, use-readiness, handover and service launch;
- preserves predecessor/successor site identity during redevelopment;
- exposes exact tactical dependencies for worksite encounters;
- supplies reduced static variants that can run before moving hazards, objective AI or environmental reactions exist.

All proposed Ouros examples remain NON-CANON until explicitly promoted.