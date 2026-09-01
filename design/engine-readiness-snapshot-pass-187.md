# Engine Readiness Snapshot — Pass 187

Status: DESIGN EVIDENCE SNAPSHOT. NOT CANON.
Date: 2026-09-01

## Scope

This snapshot records live engine evidence used by salvage/recovery concepts in pass 187. AutoPTU-Java and AutoPTU are read-only from this task.

Evidence heads inspected:

- AutoPTU-Java: `1acb773545966affce865ec3f250ff02faccae57`
- AutoPTU Python oracle: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- Narrative base before pass 187: `8bcd4547d7d342ea43dcf34775668eecd632e3af`

## Live Java evidence

The current Java head introduces `BattleRuntimeDependencies`, an immutable runtime composition boundary carrying authoritative combatant rule content. Runtime post-hit forced movement now resolves defender content through that shared dependency boundary, and regression tests cover selection of target rule content rather than incorrectly using source content.

This is meaningful evidence for architecture around forced-movement prevention and content composition.

It still does not prove complete movement.

The unproven breadth includes, among other interactions:

- all Push variants;
- all Pull variants;
- all Knockback variants;
- Interception;
- collisions;
- partial stops;
- footprint-sensitive forced movement;
- chained displacement;
- reaction ordering;
- terrain-mediated displacement;
- every Move, Ability, Item and Trainer Feature source of displacement or prevention.

No salvage concept may treat this one implemented composition seam as proof of the family.

## AutoPTU Python evidence

Current AutoPTU head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

The latest visible change synchronizes presentation coordinates after viewport resize and explicitly states that battle rules and outcomes do not change.

This provides no new rules evidence for promoting tactical capability categories.

## PTU item-content evidence

The current AutoPTU source set contains mechanical content references including Thief, Frisk, Pickup and Held Item removal/retention effects.

Pass 187 uses that evidence only to establish a boundary:

- mechanical possession/reveal/removal behavior must follow the exact PTU rule and engine implementation;
- narrative ownership, custody, provenance and institutional stock remain separate world facts;
- an implemented Held Item interaction cannot decide a found-property or salvage claim.

## Capability classification

### Targeting / footprints / range / LoS

Classification: VERIFIED for currently audited contracts.

Recovery encounter use:

Suitable only when the selected battle content remains inside verified targeting contracts. A recovery object itself should remain outside BattleSpec in the reduced version.

### Base movement legality

Classification: VERIFIED for currently audited base contracts.

Recovery encounter use:

A stable-terrain reduced battle can rely on this baseline when unsupported advanced movement interactions are excluded.

### Complete movement including push/pull/knockback/interception/forced movement

Classification: PARTIAL.

Current evidence includes useful forced-movement candidate constraints, prevention composition, provenance and runtime dependency injection.

Blocking gap:

The complete family is not demonstrated. A recovery encounter using carriers, corridor protection, Interception, collisions, partial stops or displacement around cargo must mark this family as required and blocking unless exact contracts are audited.

### Core calculations

Classification: VERIFIED for currently audited deterministic arithmetic contracts.

### Action economy / initiative

Classification: VERIFIED for currently audited primitives.

### Full turn / round lifecycle

Classification: PARTIAL.

A mechanically rich recovery scene with sustained objectives cannot infer full lifecycle parity from implemented slices.

### Full stateful damage pipeline

Classification: PARTIAL.

A battle around a recovery site must not assume all damage transitions, secondary effects and aftermath are complete simply because ordinary attacks work in representative tests.

### Status lifecycle

Classification: PARTIAL.

Any selected status requires exact application, persistence, timing, immunity, cure and interaction coverage.

### Terrain / weather / hazards / zones / reactions

Classification: BLOCKING as a complete family.

This category is especially relevant to salvage concepts because unstable footing, debris, water, weather phases, entanglement, hazardous zones or reaction timing are tempting design elements.

Until exact contracts exist, reduced encounters must keep those conditions in authoritative world state rather than pretending BattleSpec owns them.

### Move-specific behavior

Classification: PARTIAL.

Every selected Move requires exact behavior coverage. Thief existing in source material does not imply full engine parity for Thief, nor does one implemented displacement Move prove all movement content.

### Abilities

Classification: PARTIAL.

Frisk, Pickup or any other selected Ability requires exact current implementation evidence before a battle or world adapter may rely on it mechanically.

### Items

Classification: PARTIAL.

Held Item and inventory concepts exist, but full catalogue parity is not proven. Narrative found-property records must never be derived from generic Minecraft inventory state.

### Trainer Features / perks

Classification: PARTIAL.

A resident's PTU class concept cannot grant an unverified recovery, engineering, navigation or item-handling mechanic. Any mechanically participating Trainer requires exact Feature audit.

### AI legal-action infrastructure

Classification: VERIFIED for currently audited legal-action contracts.

Important limitation:

Legal action generation does not demonstrate objective-aware tactical policy.

### AI tactical policy

Classification: BLOCKING as a complete family.

The full recovery encounter would benefit from actors understanding corridors, workers, withdrawal routes and objective pressure. That behavior cannot be claimed merely because the AI can select a legal action.

### Minecraft / Cobblemon / Craftics adapter and playback support

Classification: BLOCKING as the complete tactical adapter/playback family.

The wider RPG adapter can support persistent objects, NPCs and world-state interactions in narrower slices, but that evidence does not prove faithful end-to-end tactical playback for a mechanically rich recovery encounter.

Pass 187 therefore keeps custody, claims, cargo and safety state outside battle authority.

## Salvage-specific dependency matrix

### Found-object documentation

Battle dependencies: none.

Required world systems:

- persistent world object identity;
- provenance/claim records;
- actor knowledge;
- location/time observation;
- server-authoritative persistence.

Current classification: suitable for narrative/RPG implementation independent of tactical parity.

### Hazard assessment without tactical hazard

Battle dependencies: none.

A resident can author an attributed condition assessment in world state. This does not create PTU damage or status mechanics.

### Custody handoff

Battle dependencies: none.

Requires explicit world-state transfer. Minecraft pickup cannot substitute for it.

### Repair handoff

Battle dependencies: none unless the repair itself invokes PTU mechanics.

The recovery layer should route to the existing repair workflow rather than duplicate repair state.

### Battle-item interaction near a recovered object

Required families depend on selected content:

- exact move-specific behavior;
- exact Ability behavior;
- exact Item behavior;
- damage/status/lifecycle families as applicable.

Narrative limitation:

Even a perfectly resolved PTU item transfer cannot decide external ownership or custody of the recovered world object.

### Recovery Line at Ferry Shore — full version

Required permanent capability categories:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when present;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected content;
- terrain/weather/hazards/zones/reactions when site conditions are tactical;
- move-specific behavior;
- abilities;
- items when allowed;
- Trainer Features/perks when used;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current classification: BLOCKED.

### Recovery Line at Ferry Shore — reduced version

World-state layer owns:

- cargo/recovery object;
- workers and noncombatants;
- shoreline access state;
- hazard assessment;
- provenance;
- custody;
- claim status;
- repairability and downstream routing.

If a wild threat prevents safe access, BattleSpec receives only an audited ordinary combat on stable terrain with exact roster/content review.

Permitted narrow battle handoffs:

- `IMMEDIATE_RECOVERY_AREA_CLEAR`
- `IMMEDIATE_WILD_THREAT_WITHDREW`

Forbidden battle conclusions:

- ownership;
- abandonment;
- provenance;
- cargo acceptance;
- repair readiness;
- historical significance;
- compensation;
- cause of displacement;
- long-term access safety.

Current classification: REDUCIBLE, subject to exact encounter-content audit. This does not promote any capability family.

## Adapter authority boundary

For pass 187 the Minecraft/Cobblemon presentation layer must obey these constraints:

- world-object ID remains server-authoritative;
- item entity or block representation is presentation/interactivity only;
- duplicate projections cannot mint duplicate authoritative objects;
- chunk unload and despawn cannot close a recovery case;
- Cobblemon battle state cannot determine object custody;
- AutoPTU battle results can write only pre-approved narrow consequences;
- world-state services decide later recovery, transfer and disposition.

## Caelo and mechanical questions still unresolved

- whether Caelo defines found-property or salvage procedures;
- whether Caelo distinguishes cargo lost in transit from abandoned goods;
- whether regional institutions have authority to hold disputed property;
- whether there is a canonical insurance or compensation model;
- whether any PTU/Caelo Feature explicitly supports appraisal, repair, evidence handling or recovery beyond existing Skill/Feature rules;
- exact implementation status of Thief, Frisk, Pickup and other item-interaction content in Java;
- exact Item transfer persistence rules after battle;
- exact adapter contract for converting legitimate PTU item changes into persistent RPG inventory when appropriate;
- whether environmental shoreline hazards will ever compile into BattleSpec or remain world-state obstacles.

No answer is invented here.

## Promotion rule

A capability category advances only when live tests/contracts demonstrate the breadth needed by the claim.

One new Move, Ability, Item interaction, displacement prevention rule, hazard, reaction or adapter animation remains evidence for that slice. It cannot stand in for the complete permanent category.