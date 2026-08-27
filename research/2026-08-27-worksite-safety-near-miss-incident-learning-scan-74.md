# Worksite Safety, Near-Miss & Incident Learning Scan — Pass 74

Status: research/provenance only. Not Ouros canon.

## Why this scan

The repository already models workplaces, staffing, facility condition, maintenance work orders, crisis response, credentials, public notices, equipment custody and case investigations. What is still missing is the preventive layer between ordinary work and a crisis: observations of unsafe conditions, close calls that caused no injury, temporary work restrictions, investigation without automatic blame, corrective actions, shift-to-shift learning and explicit return-to-work verification.

This scan looks for reusable structures rather than setting facts. It does not establish an Ouros regulator, safety law, inspectorate, reporting deadline, worker right, employer duty, liability rule or compensation system.

## Internal overlap review

Relevant existing files inspected before writing:

- `design/workplaces-professions-staffing-layer.md`: owns workplaces, roles, shifts, work assignments, backlog, training and operational handoffs.
- `design/facility-maintenance-repair-inspection-extension.md`: owns physical condition, faults, technical assessment, work orders, mitigations, repair verification and reopening of facilities.
- `design/crisis-rescue-recovery-layer.md`: owns emergencies once a hazard becomes an active crisis affecting people, routes, services or settlements.
- `design/credentials-authorizations-recognition-extension.md`: owns qualifications, authorization scopes and credential validity.
- `design/shared-equipment-lending-issued-assets-extension.md`: owns equipment custody and return state.
- `design/case-authority-custody-layer.md`: owns formal cases/evidence when wrongdoing, authority or formal investigation becomes relevant.
- `design/engine-readiness-snapshot-pass-73.md`: provides the permanent capability categories used by this scan.

The research and proposals directories were enumerated through Pass 73. No prior scan specifically owns near-miss reporting, stop-work state, corrective-action learning or safety handoff continuity.

## Source A — Oreburgh Mine and Roark

Source:
https://bulbapedia.bulbagarden.net/wiki/Roark
https://bulbapedia.bulbagarden.net/wiki/Oreburgh_Mine
https://bulbapedia.bulbagarden.net/wiki/Oreburgh_City

Observed high-level pattern:

- Roark has an explicit safety-supervision role in addition to being a Gym Leader.
- The mine is represented as a working institution rather than a disposable dungeon.
- Ventilation, automation and organized work practices are visible parts of how the mine operates.
- Mine operations are described as taking care around wild Pokémon habitat.
- Workers use Pokémon as part of ordinary work.

Reusable lesson for Ouros:

A dangerous workplace can remain a functioning everyday location because safety is represented through roles, physical controls, routines and tradeoffs. A mine does not need to become a catastrophe every time the player visits. The interesting narrative hook can be a deviation from a known safe baseline.

Transformation rule:

Do not import Oreburgh, Roark, coal economics, specific mining technology, species assignments or Sinnoh institutions. Do not infer that a Pokémon species is qualified for labor from its Pokédex concept or type. Ouros requires authored occupational relationships plus PTU/Caelo-supported capabilities for any mechanically relevant work.

## Source B — Bothersome Bidoof, Pokémon Legends: Arceus

Source:
https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30

Observed high-level pattern:

A recurring nuisance in Jubilife Village is reinterpreted once another institutional actor recognizes that the Bidoof's ordinary behavior can be useful for construction. The resolution includes supervision and a durable change in the relationship between settlement and Pokémon rather than simple removal.

Reusable lesson for Ouros:

A safety/operations problem can resolve through redesigning the work arrangement instead of defeating or expelling the Pokémon involved. Supervision, changed access, changed task assignment and a new routine can all be persistent consequences.

Transformation rule:

Do not copy the quest, characters or Bidoof solution. The Ouros extension only takes the structure `observed problem -> reassessment -> controlled integration or changed procedure -> persistent new baseline`.

## Source C — Oreburgh incident escalation in animation

Source:
https://bulbapedia.bulbagarden.net/wiki/DP017

Observed high-level pattern:

A technical/research incident releases dangerous Pokémon into an inhabited area. The response includes alerting responsible actors, evacuation, containment and explicit concern for people and equipment rather than treating the event only as a battle.

Reusable lesson for Ouros:

The boundary between a near miss, local incident and full crisis should be explicit. Once people require evacuation and the normal workplace can no longer safely operate, control passes to Crisis/Rescue. The safety layer can retain the incident history and later corrective actions without owning emergency response itself.

Transformation rule:

Do not reuse the Fossil revival plot, characters, species or sequence of events.

## Source D — Pokémon.com: temporary containment is not resolution

Source:
https://www.pokemon.com/us/animation/seasons/10/episode-23-faced-with-steelix-determination

Observed high-level pattern:

A community initially improves a physical barrier against a rampaging Steelix, but the story treats stronger walls as a temporary measure because the underlying cause remains unresolved.

Reusable lesson for Ouros:

A mitigation can reduce immediate exposure while the causal problem remains open. A barrier, closure, changed route or extra supervision must never silently mark an incident resolved.

Transformation rule:

Only the `temporary control vs underlying cause` structure is reused.

## Source E — OSHA hazard identification and near-miss investigation

Sources:
https://www.osha.gov/safety-management/hazard-Identification
https://obis.osha.gov/dcsp/products/topics/incidentinvestigation/
https://www.osha.gov/safety-management/education-training

Observed operational pattern:

- recurring inspections and worker observations can identify hazards before injury occurs;
- close calls/near misses are useful evidence even when no one was hurt;
- investigation should collect facts and underlying contributing conditions;
- corrective action should be tracked to completion;
- investigation can focus on prevention rather than blame;
- training and communication are part of maintaining controls.

Reusable lesson for Ouros:

This is useful as an information architecture: observation, near miss, evidence, contributing-factor claims, interim control, corrective action, verification and learning. It supports mysteries and persistent workplace change without needing a casualty every time.

Critical boundary:

OSHA is a real-world United States legal/regulatory system. Ouros does not inherit OSHA statutes, duties, reporting windows, rights, penalties, terminology as law, or institutional structures. Only generic operational concepts are used.

## Source F — PTU system boundary

Source:
Pokémon Tabletop United 1.05 core, project-available PTU/Caelo material, plus the repository's existing source hierarchy.

Useful structural point:

PTU provides character skills, capabilities, Pokémon movement and combat mechanics that may support authored work scenes. It does not make an occupational title equivalent to a Trainer Class, nor does it automatically create a complete worksite-safety simulation.

Pass 74 therefore keeps occupational safety as world state. If an encounter uses falling debris, unstable floors, moving workers, knockback near an edge, reactions, active weather, dangerous zones or objective-aware opponents, those behaviors must be backed by the exact engine capability families instead of being improvised in Minecraft.

## Synthesis for Ouros

The strongest reusable loop is:

`ordinary work baseline -> observation or near miss -> immediate safe-state decision -> evidence capture -> contributing-factor review -> temporary controls -> corrective action -> verification -> return-to-work decision -> learned change visible on later visits`

Important separations:

- observation does not prove cause;
- near miss does not prove negligence;
- incident does not prove wrongdoing;
- corrective action does not imply punishment;
- temporary restriction does not mean permanent closure;
- repair completion does not alone authorize work to resume;
- a physical danger in the overworld is not automatically a PTU tactical Hazard;
- a Pokémon helping with work does not automatically possess a mechanical Skill, Feature or legal authority.

## Original design opportunities

1. Safety can generate low-intensity continuity hooks: a changed walkway, a new briefing ritual, a tagged-out machine, a relocated workbench, a revised shift handoff.
2. Near misses create mysteries without requiring villains. Several individually plausible reports can reveal a recurring condition only when compared across shifts.
3. Workers can disagree honestly because they observed different windows of the same process.
4. A site can improve visibly over months without a hidden `safety_score`.
5. Players can contribute observations, escort an assessment team, retrieve records, test a safe alternate route or help communicate a restriction without automatically becoming inspectors or managers.
6. A repeated Pokémon presence near a workplace can trigger ecological redesign rather than combat if evidence supports coexistence.

## Canon protection

This scan establishes no Ouros employer, union, regulator, inspector, safety committee, permit system, stop-work law, PPE standard, disciplinary process, compensation rule or universal reporting procedure.

Any later canon adoption must answer those setting questions explicitly.
