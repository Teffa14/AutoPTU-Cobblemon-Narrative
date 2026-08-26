# Ouros Facility Maintenance & Repair Seeds — Pass 58

Status: PROPOSED / NON-CANON.

These are original Ouros candidates derived from the high-level patterns documented in `research/2026-08-26-facility-maintenance-repair-lifecycle-scan-58.md`. Names, institutions, facilities, technologies, procedures and locations are placeholders until canon review.

## Design intent

Use maintenance to make existing places remember use, damage, repairs and changing service conditions. The goal is not to generate chores. Materialize maintenance play when a meaningful choice, investigation, dependency, temporary relocation, access change, ecological concern, recurring fault or tactical incident exists.

Every seed below assumes:
- physical condition and operational availability are separate;
- observations do not automatically prove causes;
- temporary mitigation does not equal repair;
- repair does not automatically equal full reopening;
- property rights, inspection powers, building codes, labor rules and prices remain undefined unless canon supplies them;
- Pokémon work capability cannot be inferred from typing/species stereotype;
- Minecraft displays authoritative facility state rather than calculating structural outcomes.

## Seed 1 — The Door That Keeps Sticking

A frequently used public room develops the same small access problem for the third time. Each prior adjustment restored normal use briefly, but the work history shows that nobody confirmed the underlying cause.

Player-facing structure:

1. compare current observation with prior work orders;
2. interview the people who use or maintain the room;
3. inspect whether the symptom changes by time, weather, load, neighboring work or another explicit world-state variable;
4. choose whether another temporary adjustment is sufficient or whether the fault should be escalated for assessment;
5. preserve the conclusion and uncertainty for the next revisit.

Possible outcomes:
- TEMPORARILY_MITIGATED;
- MONITORED;
- REPAIR_PLANNED;
- ESCALATED;
- RESOLVED only if evidence supports it.

The actual cause remains authored. The generator should offer evidence-led hypotheses rather than invent structural explanations.

Narrative value:

A very small recurring fault can teach the player that Ouros remembers previous interventions. A quick fix may still be reasonable if the cost of interruption is high and evidence does not yet justify larger work.

## Seed 2 — Temporary Counter Across the Courtyard

A service room closes for repair, but the institution can continue a narrower version of the service from a temporary desk in an adjacent safe area.

State changes:
- original facility area becomes CLOSED or UNDER_WORK;
- service becomes LIMITED rather than disappearing;
- customer/patient/visitor flow moves to a temporary location;
- staffing coverage may change;
- signage and props change in Minecraft;
- normal service returns only after verification.

Story hooks:
- users discover the temporary desk is easier to access;
- the move exposes a staffing bottleneck that was hidden by the old layout;
- one service can operate temporarily while another cannot;
- an alternate queue or entrance affects neighboring activity.

This seed can later hand a question to civic/accessibility design: should any successful temporary change become permanent? Maintenance state alone does not decide that.

## Seed 3 — The Repair That Exposes an Older Repair

During authorized work, a crew discovers evidence of an older patch beneath the current surface. Records are incomplete, and different people remember the earlier problem differently.

Important separation:
- physical evidence;
- prior work record;
- oral recollection;
- current hypothesis;
- canonical truth.

The old repair is not evidence of corruption, negligence or wrongdoing by default.

Playable sequence:
1. document the newly visible patch;
2. locate older material/work records if they exist;
3. compare provenance and dates;
4. determine whether the discovery changes current scope;
5. preserve unresolved questions for archive/public-works review if appropriate.

This can connect facility history to archives, materials, public memory or a case without forcing any of those systems to conclude guilt.

## Seed 4 — Three Closures, One Dependency

Three unrelated facilities enter LIMITED service within a short period. Nothing indicates that all three buildings are physically damaged.

Potential shared dependencies must come from actual world state, such as:
- one utility/service interruption;
- one specialist unavailable;
- one transport link affecting necessary supplies;
- one shared temporary access restriction;
- one environmental condition affecting operations;
- one institution coordinating several sites.

Investigation structure:

`compare service changes -> separate physical faults from operational limits -> map dependencies -> identify shared edge -> choose mitigation priorities`

The generator must not select a shared cause unless the dependency graph supports it.

This is a strong noncombat mystery because the visible symptom is closure, while the real system-level question may be staffing, transport, utilities or scheduling.

## Seed 5 — Reopening Day Is Not Completion

A facility passes enough verification to reopen, but one secondary area or service remains unavailable.

Possible visible state:
- main entrance open;
- one corridor/room still restricted;
- temporary sign remains;
- some staff return while others stay relocated;
- one recurring service resumes later;
- users react differently to the partial reopening.

The point is to avoid a binary repaired/unrepaired world. Reopening can be a state transition with follow-up work rather than the end of the story.

## Seed 6 — The Spare Route During Works

Maintenance blocks the normal entrance or path to a facility. An existing alternate path becomes the temporary access route.

During the work period, players and NPC cohorts learn that the alternate route has different consequences: it may be longer, safer, more accessible, worse in weather, closer to another service or disruptive to a habitat. Those effects must come from authored route/world state.

When the original access reopens, a new question can emerge: should the temporary route remain recognized?

Maintenance does not answer that question. If keeping it requires a collective future choice, hand off to civic governance/public works.

## Seed 7 — Deferred Until the Right Window

A known repair is deliberately deferred because the current world state makes immediate work less suitable.

Possible authored reasons:
- seasonal access;
- ecological timing;
- one necessary specialist unavailable;
- material delivery delayed;
- another higher-priority recovery job uses the same crew;
- service interruption would conflict with a major event;
- monitoring indicates temporary mitigation is currently acceptable.

Required state:
- the fault remains OPEN or ACCEPTED_DEFERRED;
- mitigation is explicit;
- a review trigger is recorded;
- escalation conditions are recorded where known;
- no hidden random-failure timer is invented.

The later revisit should compare what actually changed rather than assume the delay was good or bad.

## Seed 8 — The Work Order Nobody Closed

The physical work appears finished, but the operational record still shows the job as VERIFYING because one documented requirement has not been completed.

This can create a low-stakes procedural mystery:
- was verification performed but never recorded?
- is one inspection/assessment genuinely outstanding?
- did the scope change?
- is a service waiting on a separate dependency?

The story should resolve the information gap before treating the facility as fully restored.

This seed is useful for teaching the difference between visible construction state and authoritative service state.

## Seed 9 — The Room Everyone Learned to Avoid

A room stayed closed long enough that staff, residents or visitors built new routines around its absence. After repair, reopening does not instantly restore the old pattern.

Possible persistent consequences:
- a temporary desk became a familiar meeting point;
- staff developed a different shift handoff;
- visitors continue using the alternate entrance;
- a nearby service absorbed part of the old demand;
- a wild Pokémon presence changed around the quieter area, if ecological evidence supports it.

The facility can be mechanically/operationally restored while social routines remain changed. This links maintenance to settlement memory without inventing relationship labels.

## Recurring arc — A Work Crew Learns the Building

Status: PROPOSED / NON-CANON.

Premise:

One existing multi-use facility accumulates several small maintenance episodes over a long campaign. The same maintenance institution or role group may recur, but individual workers only become persistent NPCs when they matter narratively.

Phase 1 — Baseline
- establish the facility’s normal services and access;
- record who operates it and who maintains it if canon supports those roles;
- create no fault simply because the system exists.

Phase 2 — First meaningful fault
- a traceable observation limits one part of the facility;
- temporary mitigation keeps another service operating;
- players may assist with evidence, access, supply or a legal tactical encounter.

Phase 3 — Revisit
- history shows whether the repair held;
- crew/staff knowledge improves because prior records exist, not through invented buffs;
- a new problem may share or differ from the old dependency.

Phase 4 — Competing pressures
- another settlement/service need competes for the same staff, materials or timing window;
- players see maintenance as part of a real world rather than an isolated quest queue.

Phase 5 — Major decision threshold
- repeated faults or changed community needs may eventually make routine repair insufficient;
- if replacement, expansion, relocation or redesign becomes a collective future decision, emit a civic proposal instead of silently rebuilding.

Long-term persistence:
- facility history;
- known recurring fault patterns;
- temporary access routes used previously;
- work-order records;
- visible repairs/modifications;
- staff or community routines that changed;
- any unresolved deferred items.

## Mystery — Four Work Orders, Three Stories

A facility has four historical work orders describing what appears to be one recurring problem. Three were written by different teams or at different times and use inconsistent language.

Goal:

Reconstruct what was actually observed each time before deciding whether the fault truly recurred.

Evidence may include:
- timestamps;
- photographed/recorded observations;
- material provenance;
- service interruption records;
- staff recollections;
- weather/utility/route state from those dates;
- previous verification outcomes.

Do not assume one record is dishonest because descriptions conflict. Differences may come from observation scope, terminology, incomplete access or different symptoms.

Possible outcomes:
- one recurring fault;
- two unrelated faults described similarly;
- one old repair solved the original issue and a new symptom only looks similar;
- evidence remains insufficient.

This is primarily noncombat and can run before the Minecraft adapter is complete.

## Encounter A — Active Worksite Collapse

Status: PROPOSED / NON-CANON.

Narrative premise:

A maintenance site becomes unsafe during active work. A wild or hostile actor is present, and continued conflict could worsen access to the damaged area. Workers must reach safety before tactical resolution.

### Intended full version

Desired tactical behaviors:
- active workers/noncombatants evacuating through changing safe routes;
- unstable or blocked tiles changing during the encounter;
- debris or equipment creating hazards/zones;
- push/knockback consequences near unsafe areas;
- possible interception/protection behavior;
- AI valuing withdrawal, protection or containment instead of only damage;
- Minecraft showing worksite state and resulting damage/closure.

Capability dependencies:
- targeting / footprints / range / LoS — required;
- base movement legality — required;
- complete movement including push/pull/knockback/interception/forced movement — required;
- core calculations — required;
- action economy / initiative — required;
- full turn / round lifecycle — required;
- full stateful damage pipeline — required;
- status lifecycle — required only for legal effects actually used;
- terrain / weather / hazards / zones / reactions — required;
- move-specific behavior — required for the selected legal Moves;
- abilities — required for selected legal Abilities;
- items — required only if legal Items participate;
- Trainer Features / perks — required only if relevant actors use them;
- AI legal-action infrastructure — required;
- AI tactical policy — required;
- Minecraft / Cobblemon / Craftics adapter/playback — required for embodied version.

### Reduced executable version

Before battle:
- evacuate all workers and other noncombatants through narrative world state;
- mark the damaged/unstable portion closed;
- freeze safe geometry;
- do not model dynamic debris, collapse progression, destructible props or hazard damage.

Battle:
- instantiate only legal combatants;
- use a static legal arena;
- let AutoPTU resolve the tactical result.

After battle:
- update facility/work-order state from the authoritative outcome;
- decide whether work resumes, remains suspended or triggers another assessment.

The narrative premise remains a worksite interruption, but the reduced battle does not pretend missing tactical families exist.

## Encounter B — Closed Utility Room Containment

Status: PROPOSED / NON-CANON.

Narrative premise:

A closed utility/service room contains a Pokémon or hostile actor that prevents restoration. The facility service is already shut down before combat begins.

### Intended full version

Desired tactical behaviors:
- narrow routing;
- containment/escape objective;
- protected equipment or zones;
- forced displacement consequences;
- reactions/interception where legal;
- AI that values escape, containment or equipment avoidance;
- adapter playback of service shutdown and post-battle restoration state.

Key blocking families for the intended version:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain / weather / hazards / zones / reactions;
- AI tactical policy;
- Minecraft / Cobblemon / Craftics adapter/playback.

Lifecycle, damage, statuses, move behavior, abilities, items and Trainer Features must also be verified for any specific effects selected.

### Reduced executable version

Before battle:
- shut the affected service down in world state;
- remove noncombatants;
- remove dynamic equipment interactions from tactical resolution;
- freeze room geometry or use an adjacent safe static arena.

Battle:
- resolve only legal combatants using currently supported engine rules.

After battle:
- battle outcome permits or prevents resumption of maintenance;
- actual service restoration still requires the facility work/verification state.

## Noncombat encounter — Recurring Fault Review

Status: PROPOSED / NON-CANON.

A facility displays a familiar symptom after a previous repair.

Scene loop:
- inspect current evidence;
- retrieve prior observation, assessment, work order and verification records;
- compare what changed between incidents;
- inspect material, staffing, utility, weather, ecological and route dependencies only where relevant data exists;
- distinguish symptom recurrence from confirmed cause recurrence;
- issue a new assessment, mitigation or escalation recommendation;
- preserve uncertainty.

This is executable as narrative state now and does not need tactical battle resolution.

## Canon questions before placement

The following remain deliberately unanswered:

- Which Ouros settlements already contain reusable civic, medical, transport, research, commercial, residential or workshop facilities?
- Which institutions or actors operate and maintain those places?
- Does Ouros have formal inspectors, maintenance departments, contractors, guilds or equivalent roles, and what are their actual mandates?
- What building materials, utilities and maintenance technologies are normal in each region?
- Which facilities can legally continue LIMITED service while work occurs?
- What forms of temporary relocation are culturally and operationally normal?
- Which records are public, private or institutional?
- Which Pokémon, if any, participate in maintenance work, and what authoritative evidence makes each individual task plausible/legal?
- At what point does routine maintenance escalate to a civic public-works decision?
- How much worksite change can Minecraft safely render without making block state authoritative over PTU or narrative facility state?

No answer above is promoted to canon by this proposal.