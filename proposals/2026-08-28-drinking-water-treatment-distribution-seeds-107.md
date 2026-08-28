# Drinking-Water Treatment & Distribution Seeds — Pass 107

Status: NON-CANON PROPOSALS. These are candidates for later review, not established Ouros facts.
Date: 2026-08-28
Depends on: `design/drinking-water-treatment-distribution-continuity-extension.md`

## Design goal

Use water service as persistent world history rather than a binary utility switch. Every seed preserves scope, timestamps, provenance and authority boundaries. None assumes a specific Ouros region, institution, technology, Pokémon role or PTU environmental rule.

## Situation seeds

### The Plant Is Running, the Hill Is Dry

A treatment facility has a verified output handoff, yet one elevated service sector still reports no delivery.

Useful tensions:

- residents believe the treatment repair failed;
- operator records show the plant is functioning;
- a local distribution path or endpoint may still be isolated;
- an old map shows a connection that may no longer be active.

Resolution should come from topology and observations, not a hidden sabotage answer.

### The Water Returned Before the Notice Changed

A sector has verified delivery, but the last public restriction remains posted.

Possible causes include stale communication, a restriction with a different scope, a quality clearance still pending, or a service restoration that occurred after the notice was issued.

Communications owns the notice. Water Continuity owns the current operational evidence.

### The Notice Changed Before the Tap Did

The reverse case: a broad restoration message is correct for most of the district, but one building or branch still has a local endpoint failure.

This makes a useful low-stakes investigation because the system can be generally restored without every complaint being false.

### The Temporary Water Point Became the Square

A temporary distribution point operates long enough that food stalls, notices, informal meetings and recurring NPC routines accumulate around it. When normal service returns, removing the temporary site becomes a social decision rather than automatic cleanup.

The utility function may end while the location retains public-memory value.

### The Old Pump House Has a New Door

A decommissioned utility building is reused by another institution. Old drawings still identify it as an operational node, causing confusion during a later outage.

The mystery is documentary and temporal. The building's current owner does not inherit its former technical role automatically.

### The Tank Is Full, the Sector Is Offline

A treated-water storage asset has an adequate broad reserve state but its active distribution path is isolated.

This seed teaches the distinction between stored supply and deliverable service without requiring numeric volume or pressure simulation.

### The Treatment Stage Passed, the Handoff Did Not

A repaired stage tests successfully in isolation, yet the facility output remains unverified for handoff.

Maintenance can truthfully report a successful repair while operators truthfully refuse to resume distribution.

### The Clinic Has Water, the Procedure Is Still Paused

The clinic endpoint receives verified supply again. Care nevertheless keeps a specific service paused pending its own restart check.

Water restoration creates a handoff, not automatic normalization of downstream systems.

### The Public Fountain Works, the Homes Do Not

A familiar public water point is supplied through a different connection or temporary arrangement than nearby residences.

Residents use the fountain as evidence that “the water is back.” Their observation is real but scoped incorrectly.

### The Pokémon Drinks There Every Morning

A wild Pokémon repeatedly drinks from a visible water point. Some residents treat that behavior as proof the water is safe; others treat the Pokémon's absence one morning as evidence of contamination.

The actual story is about evidence quality, ecology and public interpretation. Pokémon behavior does not establish potability.

### The Blue Water Failed the Check

Minecraft presentation or visual clarity suggests clean water, while the authoritative clearance remains pending or restricted.

This seed exists partly as an implementation guardrail: visual appearance must never become the source of truth.

### The Ugly Water Was Cleared for Its Authored Use

The inverse case. An unusual appearance generates rumors even though the relevant authoritative evidence supports the intended use.

Do not turn this into a universal lesson that appearance never matters; it simply demonstrates that observation and diagnosis are separate.

### Two Streets, One Pipe on the Old Map

Older records show both streets under one branch. Current observations demonstrate different service states.

Investigation may reveal a later reroute, an undocumented temporary connection, a superseded map or a local endpoint issue.

### The Alternate Supply Has Outlived the Repair

Primary infrastructure is restored, but a temporary supply arrangement remains active because removal requires another decision, because one endpoint still depends on it, or because the site acquired another community function.

### The First Restored Building Was Not the Most Important One

Rumors interpret restoration order as favoritism. Technical records show that one building simply sat on the first path that could be verified.

If actual priority decisions existed, Civic/Crisis authority owns them. Water Continuity should not invent moral intent from sequence alone.

## Provenance mysteries

### Five Taps, Three Stories

Five service points produce apparently incompatible reports:

- one had delivery before the official restoration time;
- two recovered together;
- one recovered much later;
- one never actually lost local stored supply.

The investigation compares service-point IDs, sectors, active paths, fallback state and timestamps. A valid ending may show that every witness accurately described a different operational scope.

### Four Clearances, One Actual Window

Several documents use the phrase “cleared,” but refer to different subjects or intended uses: treatment-stage test, treated-water handoff, sector delivery, endpoint use. The player must reconstruct which clearance applied where and when.

No universal `water_safe=true` flag is revealed.

### Three Maps, Two Generations of Network

A historical map, a maintenance diagram and a current operator view disagree. Each is internally correct for a different period or purpose. The useful discovery is the topology history itself.

## NPC and institutional archetypes

These are role templates, not canon characters.

The Sector Operator remembers which workaround actually worked during the last outage but is careful not to claim expertise outside operations.

The Field Sampler keeps meticulous location and timestamp records and becomes valuable because eyewitness descriptions alone are ambiguous.

The Old-System Keeper knows obsolete infrastructure well but may describe historical topology as if it were still current.

The Temporary-Site Coordinator begins as an emergency assignment and becomes a social anchor because the distribution point remains active for weeks.

The Resident Recorder has a personal log of tap behavior that appears anecdotal until its timestamps help bound a sector transition.

The Ecologist tracks Pokémon use around water infrastructure but refuses to equate animal behavior with potability or technical causation.

The Downstream Manager cares less about the utility's internal milestones than about the exact handoff their clinic, workshop, inn or residence needs before resuming service.

## Faction / institutional dynamics

Possible non-canon tensions:

- central treatment operator versus local distribution operator over where a fault boundary lies;
- maintenance team versus service operator over the meaning of “repair complete”;
- public-information staff working from a broader service-sector view than residents experiencing endpoint failures;
- conservation staff asking for review before recommissioning a long-idle asset now used by wildlife;
- neighborhood groups wanting to keep a temporary water point as public space after its utility role ends;
- old-system veterans and newer staff interpreting obsolete diagrams differently.

None requires corruption, villainy or incompetence. Institutional scope alone can generate meaningful conflict.

## Long arc — A Town Learns Where Its Water Comes From

Phase 1 establishes ordinary life: public water points, households, businesses, a clinic, operator routines and a source that most residents rarely think about.

Phase 2 introduces a limited failure or restriction. Initial reports disagree because different sectors and endpoints experience it differently.

Phase 3 activates one or more temporary arrangements. A new gathering point appears. Couriers, businesses, hospitality and care adapt differently.

Phase 4 restores treatment first. Some residents reasonably believe the crisis is over while distribution verification remains incomplete.

Phase 5 restores sectors in stages. A local endpoint remains unresolved, preserving a smaller follow-up problem after the dramatic system event has ended.

Phase 6 returns months later. A temporary point has become a landmark, an old pump house has another use, Pokémon have changed their routines around a quieter corridor, and records from the earlier restoration help interpret a new problem.

The arc creates place memory without a linear infrastructure upgrade meter.

## Encounter seed — Treatment Plant Access Withdrawal

Full intended form:

Operators have isolated the treatment process but need access through a contested exterior corridor. The full encounter can support withdrawal/protection routes, Intercept, forced movement, generalized reactions, technical-zone boundaries, objective-aware AI and semantic playback.

Required capability families:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Reduced form:

Complete technical isolation first. Remove staff, process water and equipment from the battle grid. Fight in a static reviewed yard with explicit participants. Victory secures access only. Inspection, repair, testing and water verification remain post-battle world-state work.

## Encounter seed — Service Reservoir Perimeter

Full intended form can use route protection, several approaches, Intercept/forced movement, reactions, reviewed elevation/edge terrain, tactical policy and playback.

Reduced form keeps the storage asset noninteractive and protected outside BattleSpec. Combat occurs on adjacent static ground. The result does not certify stored water, tank condition, path availability or downstream service.

## Encounter seed — Temporary Water Point Perimeter

Full intended form can use civilian withdrawal, corridor protection, Intercept, forced movement, reactions, objective-aware AI and playback. Any spill, vehicle or equipment hazard additionally depends on the blocking environmental family and an exact governing rule.

Reduced form suspends distribution and evacuates residents, containers and workers before combat. Fallback state remains frozen. Winning only secures the immediate site.

## Noncombat quest — Reconstruct the Restoration

A later dispute asks when service really returned during an older outage.

Player-facing work can include:

- collecting operator logs;
- matching household observations to sectors;
- comparing a treatment verification timestamp with distribution records;
- identifying a fallback connection;
- checking whether a notice was issued before or after an endpoint observation;
- preserving bounded uncertainty when evidence cannot resolve the final minute or exact endpoint.

The reward is durable world knowledge and trust, not necessarily a culprit.

## Canon review questions

Before promoting any seed, decide the relevant region's water-source arrangement, treatment technology, operator institutions, distribution topology, public-information norms, fallback practices and individual Pokémon roles.

Also decide whether the setting recognizes distinct service categories or quality clearances for different uses. Do not inherit US terminology or standards merely because external operational sources informed the architecture.

## Mechanical review questions

Do not promote any tactical waterwork element until exact support exists for the mechanic used. Open questions include environmental water damage, current/forced movement, slipping, drowning, contamination/status effects, technical objects, rescue/carry actions, Move/Ability/Item/Trainer Feature utility effects, and objective-aware tactical policy.

Every reduced encounter above remains viable without answering those questions.