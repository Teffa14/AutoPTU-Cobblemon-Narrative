# Ouros NON-CANON Proposals — Communications Network / Relay Service Continuity — Pass 105

Status: NON-CANON PROPOSALS. Nothing in this file is established Ouros lore.
Date: 2026-08-28

These seeds exercise the proposed communications-network continuity layer without deciding Ouros technology level, institutions, geography or PTU mechanics.

## Situation seeds

### The Relay Passed, the Village Did Not

A remote communications node passes its local verification after repair. A settlement downstream still cannot receive the intended service.

Possible truths include a second failed link, a stale service path, endpoint configuration, an expired access grant or a sector that was never part of the repaired route. No sabotage is required.

Useful callbacks: the same node can later become evidence that the first repair was actually successful.

### The Emergency Channel Returned First

A fallback path supports one authored priority service while ordinary public communication remains limited.

The interesting conflict belongs to established civic/crisis authority: who is allowed to define priority and whether the existing procedure still fits current needs. The communications layer only exposes technically possible states.

### The Temporary Relay Became the Meeting Place

A portable or provisional relay is established after an outage. Residents begin using its staffed area as a place to exchange notices, meet couriers and coordinate travel.

When the original network returns, the temporary technical asset can leave while its social consequences remain. Public Memory, Commercial Services or Community Aid may preserve the location's new role.

### The Map Says Covered

A published service map says a small district is served. Several current field tests fail.

The map may have been correct when published. The problem can be a new obstruction, changed path, localized fault, endpoint issue or stale version. The quest is evidence reconciliation rather than automatic fraud investigation.

### The Old Repeater Still Has Visitors

A decommissioned relay site remains a familiar landmark. Former workers, hikers, researchers or local Pokémon still use the area for reasons unrelated to its old technical function.

A later story can reveal that some current residents only know the site's informal name and have no idea what it once did.

### The Service Works Outside the Building

A public institution reports that its communications service is offline. Field testing shows the network reaches the surrounding sector normally.

The fault lies somewhere after sector delivery: local endpoint, configuration, access control, internal wiring or another dependency. Repairing the regional network would be wasted work.

### The Repair Team Cannot Prove the Repair

A node has been physically repaired, but the normal verification endpoint is unavailable because a road, power dependency, staffing issue or separate device problem remains unresolved.

The node can stay TESTING instead of being declared healthy or failed without evidence.

### The Broadcast Exists, the Receiver Cannot Tune It

A service is active and verified in the area. One actor cannot access it because their endpoint lacks an established configuration, entitlement or compatible capability.

This seed is useful for keeping infrastructure truth separate from personal access without inventing a universal subscription model.

### The Pokémon Is Always Near the Antenna

A recurring wild Pokémon is repeatedly observed near a relay before, during and after intermittent service degradation.

The Pokémon is memorable evidence of place and timing. Its presence is not proof of interference. Conservation and technical investigation can proceed in parallel.

### The Fallback Is Better Known Than the Primary

A settlement experienced a long disruption years ago. Older residents still know the fallback communication procedure better than the restored normal service, while newcomers assume the opposite.

A later outage creates a social coordination problem even when both technologies function exactly as designed.

### The Message Was Sent During the Outage

A critical message has a valid SENT timestamp while its intended sector was unavailable.

Media/Communications preserves the delivery state. Communications Network preserves the sector outage. The likely result may be delayed, queued, failed or rerouted depending on the established channel contract. The generator must not silently choose one.

### The Temporary Link Outlived Its Reason

A workaround established during a crisis remains active because it now serves an unexpected secondary community or institution.

Retiring it becomes a civic/operational decision rather than cleanup trivia.

## Provenance mysteries

### Four Signal Reports, Three Sectors

Four reports appear mutually inconsistent:

- one says normal service;
- one says intermittent service;
- one says no service;
- one says the system was restored.

Resolution can show that the observations were taken in three sectors, through two paths, at different times. All four reports may be honest and locally correct.

Required evidence:

- service ID;
- sector ID;
- path version;
- endpoint tested;
- timestamp;
- verification scope.

No hidden truth score is needed.

### Three Restoration Times, One Network

A maintenance log, network board and public notice each record a different restoration time.

They can correspond to physical repair completion, path verification and public service release. The apparent contradiction becomes a lesson in operational state rather than an accusation.

## NPC / institution patterns

### Relay technician with historical memory

A recurring operator remembers why a strange bypass exists. Their knowledge is valuable because they participated in the earlier incident, not because the job title grants omniscience.

### Local contact keeper

In a small settlement, one actor maintains the practical knowledge of which fallback path works during regional outages. Their role can become socially important without implying formal authority.

### Field verification pair

Two technicians or researchers repeatedly test remote sectors. Their reports can become recurring evidence objects and a way to revisit old routes without manufacturing a new crisis each time.

### Communications planner under uncertainty

An operator must propose fallback arrangements while several dependency claims remain unresolved. The character can be competent and still preserve uncertainty rather than supplying exposition as fact.

### Pokémon-associated work team

A particular Pokémon may assist a specific team only when its individual history and governing PTU/Caelo capability support the task. The narrative never promotes species or Type into an occupational class.

## Longer-term arc — A Region Learns Its Fallbacks

Phase 1 establishes ordinary communication habits. Different communities rely on different channels and endpoints, but the infrastructure is mostly invisible because it works.

Phase 2 introduces a bounded failure. One node or dependency affects several services differently. Field reports disagree because their scopes differ.

Phase 3 activates a temporary path. Some communities regain limited service while others remain offline. New gathering points, courier habits or travel routines appear around the workaround.

Phase 4 physical repair finishes before full communications restoration. Testing identifies a second dependency or stale topology assumption. The world therefore does not flip directly from broken to normal.

Phase 5 services return in authored stages. Temporary arrangements are retired, retained or repurposed based on actual consequences.

Phase 6 months later, a smaller incident makes the archived reports useful. A now-familiar technician, old relay site, temporary meeting place or obsolete coverage map returns with changed meaning.

The arc has no `communications_level` and no mandatory villain.

## Mechanically rich encounter concepts

### Relay Access Withdrawal

Full premise:

Technicians must leave a relay compound through one of several safe routes while combatants contest access. The intended version can use Intercept, forced movement, route protection, generalized reactions and objective-aware AI. Active technical hazards are optional and only legal when exact PTU/Caelo rules exist.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if technical/environmental zones matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced form:

Ouros isolates the relay and evacuates technicians before encounter creation. Tools, controls, cables and nonparticipant Pokémon remain outside the tactical state. AutoPTU receives a reviewed static access area. Victory secures immediate access only. Repair and network verification remain separate world-state actions.

### Temporary Relay Perimeter

Full premise:

A temporary relay supporting limited service is near a territorial confrontation. The desired tactical form protects approach routes and can require reactions/forced movement and objective policy.

Additional dependency:

If wind, energized equipment, moving machinery or other active zones matter, `terrain/weather/hazards/zones/reactions` is BLOCKING.

Reduced form:

The relay equipment and operators stay outside BattleSpec. Combat occurs in an adjacent static perimeter. Victory does not prove service continuity. A post-combat communications verification determines the actual state.

### Repeater Ridge Diversion

Full premise:

A technical crew needs access to a remote node but an encounter blocks the normal route. Full implementation could support escort/withdrawal, several routes, Intercept, forced movement, reviewed environmental effects, tactical policy and semantic playback.

Reduced form:

Travel chooses a safe static battle site before the technical location. Crew and equipment wait outside combat. After victory, the crew performs inspection using world-state systems. No radio, electricity, wind or signal mechanic is synthesized inside AutoPTU.

## Minecraft/Cobblemon presentation candidates

Possible visual reuse:

- tower and relay geometry;
- antennas and dishes as decorative or state-projected assets;
- status lights/screens;
- temporary barriers and work tents;
- technicians and vehicles as overworld entities when canon permits;
- public terminal UI showing coarse service/sector state;
- Pokémon overworld models, poses, animations and cries;
- particles, sounds and weather visuals that remain presentation unless a verified tactical contract exists.

Required authority boundary:

Minecraft never decides network topology, service availability, endpoint entitlement, message delivery, technical causation or combat outcomes. Cobblemon BattleState/controller logic never chooses combatants or owns tactical truth.

## Promotion questions

Before any seed becomes canon, determine the relevant region, technology, operator, service, sector, access policy, fallback authority, physical dependencies and source-backed Pokémon mechanics.

Before any full encounter ships, verify every currently PARTIAL/BLOCKING capability actually exercised by that encounter rather than inferring coverage from one representative mechanic.
