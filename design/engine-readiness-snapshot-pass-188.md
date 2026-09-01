# Engine Readiness Snapshot — Pass 188

Status: DESIGN EVIDENCE SNAPSHOT. NOT CANON.
Date: 2026-09-01

## Scope

This snapshot records live engine evidence used by public exhibition, judging and showcase concepts in pass 188. AutoPTU-Java and AutoPTU remain read-only.

Evidence heads inspected before writing:

- AutoPTU-Java: `1acb773545966affce865ec3f250ff02faccae57`
- AutoPTU Python oracle: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- Narrative base before pass 188: `a50ea17b2e31005a8706286d7fe36b44d8f7b04f`

## Live Java evidence

The current Java head still centers the latest relevant movement work on `BattleRuntimeDependencies`, authoritative combatant rule-content injection and forced-movement prevention composition.

This remains useful evidence for a bounded displacement slice. It does not prove the complete movement family.

No new live evidence in this pass demonstrates a dedicated PTU Contest resolver, Contest round lifecycle, Appeal Roll orchestration, Contest Effect processing, Coordinator Contest Feature execution or Contest-specific adapter playback.

Therefore a formal PTU Contest must remain an explicit future mechanical dependency rather than being approximated through battle systems or narrative scoring.

## AutoPTU Python evidence

The current Python oracle remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Repository searches confirm source/content evidence for:

- Appeal Rolls;
- Coordinator Features that trigger on Appeal Rolls;
- Features with once-per-Contest limits;
- Contest Types;
- Contest Effects attached to Moves;
- compiled Contest effect tables.

This proves that Contest semantics exist in the project's PTU source set. It does not prove that the current tactical engine executes the full Contest subsystem.

Narrative consequence:

A future formal Contest cannot use a generic `performance_score` as a replacement for source-backed PTU procedure.

## Capability classification

### Targeting / footprints / range / LoS

Classification: VERIFIED for currently audited contracts.

Battle-exhibition use:

Suitable only for selected content whose exact targeting behavior is already covered.

### Base movement legality

Classification: VERIFIED for currently audited base contracts.

A reduced Battle Yard exhibition can rely on stable-terrain ordinary movement when unsupported advanced movement effects are excluded.

### Complete movement including push/pull/knockback/interception/forced movement

Classification: PARTIAL.

Useful forced-movement prevention and dependency-composition slices exist.

Still unproven as a complete family:

- all Push behavior;
- all Pull behavior;
- all Knockback behavior;
- Interception;
- collisions;
- partial stops;
- chained displacement;
- footprint-sensitive interactions;
- reaction ordering;
- terrain-mediated displacement;
- all Move/Ability/Item/Trainer Feature sources and prevention interactions.

A crowded exhibition scene cannot treat the present forced-movement work as complete movement parity.

### Core calculations

Classification: VERIFIED for currently audited deterministic arithmetic contracts.

This classification applies to battle arithmetic. It does not imply implementation of PTU Contest scoring or Appeal Rolls.

### Action economy / initiative

Classification: VERIFIED for currently audited battle primitives.

This does not establish Contest turn order, Contest rounds or Contest action economy.

### Full turn / round lifecycle

Classification: PARTIAL.

A sustained exhibition battle cannot infer complete lifecycle parity from representative implemented slices.

A PTU Contest has its own unresolved lifecycle and must not be mapped onto battle turns without source-backed implementation.

### Full stateful damage pipeline

Classification: PARTIAL.

Relevant to battle exhibitions only. Nonbattle demonstrations and formal Contest handling should not manufacture damage merely to reuse combat infrastructure.

### Status lifecycle

Classification: PARTIAL.

Any selected battle status requires exact audit for application, timing, immunity, persistence, cure and interactions.

### Terrain / weather / hazards / zones / reactions

Classification: BLOCKING as a complete family.

A rich public event may tempt designs involving audience-safe zones, changing court areas, weather interruption, stage hazards or reactions. Keep those as world-state constraints unless exact tactical contracts are verified.

### Move-specific behavior

Classification: PARTIAL.

Battle behavior and Contest behavior must both be exact for a Move when the corresponding activity uses them.

The Python source set contains Contest Effects, but source presence alone does not demonstrate Java execution.

### Abilities

Classification: PARTIAL.

Every participating Pokémon's selected Ability requires exact implementation evidence for a battle.

Any Ability with Contest relevance also requires exact Contest-side handling before a formal Contest can depend on it.

### Items

Classification: PARTIAL.

Battle Items require exact challenge-contract and implementation review.

Props, display objects and mundane equipment remain world objects unless an authoritative PTU rule gives them mechanical meaning.

### Trainer Features / perks

Classification: PARTIAL.

This family is especially important for pass 188 because Coordinator Features explicitly interact with Appeal Rolls and Contest frequency/state in the source set.

No formal Contest should accept a mechanically active Coordinator participant until every relevant Feature is audited in the actual execution path.

### AI legal-action infrastructure

Classification: VERIFIED for currently audited battle legal-action contracts.

Limitation:

This does not provide Contest action generation or validate Contest choices.

### AI tactical policy

Classification: BLOCKING as a complete family.

Legal battle actions do not prove objective-aware behavior around interruption, safe corridors, demonstration intent or audience constraints.

Contest performance policy is a separate unresolved problem and must not be claimed as a consequence of battle AI.

### Minecraft / Cobblemon / Craftics adapter/playback support

Classification: BLOCKING as the complete tactical adapter/playback family.

The wider RPG layer can project NPCs, notices, persistent objects and ordinary world-state events in bounded slices. That evidence does not prove faithful end-to-end playback for rich battle exhibitions or formal PTU Contests.

Minecraft particles, animations, scoreboards and applause remain presentation unless an authoritative result already exists.

## Pass-188 dependency matrix

### Mirador Field-Method Demonstration

Battle dependencies: none.

World dependencies:

- event scheduling;
- persistent NPCs;
- field-note/document objects;
- provenance and revision records;
- ordinary interaction/dialogue;
- server-authoritative event state.

Current classification: suitable for narrative/RPG implementation independent of tactical parity.

### Tideglass Caption Review

Battle dependencies: none.

World dependencies:

- source records;
- draft/revision provenance;
- review authority;
- persistent public display.

Current classification: suitable for bounded implementation.

### Bruma Battle Yard Open Exhibition — simple version

Required permanent categories depend on exact matchup, but an ordinary audited battle generally requires:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- exact selected Move behavior;
- exact selected Abilities;
- exact Items if allowed;
- exact Trainer Features if used;
- damage/status/lifecycle families as selected content requires;
- AI legal-action infrastructure;
- adapter/playback for end-to-end presentation.

Current classification: conditionally reducible only after exact roster/content audit. Complete adapter/playback remains a blocker for claiming full Minecraft tactical delivery.

### Battle Yard Demonstration Under Live Disruption — intended full version

Required categories:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when present;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle for selected content;
- terrain/weather/hazards/zones/reactions if the disruption is tactical;
- move-specific behavior;
- abilities;
- items when allowed;
- Trainer Features/perks when used;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Current classification: BLOCKED.

### Battle Yard Demonstration Under Live Disruption — reduced version

World-state layer owns:

- registration;
- spectators/noncombatants;
- event procedure;
- suspension/resumption decision;
- audience response;
- posted/archived result;
- corrections;
- venue operational state.

If combat is required, AutoPTU receives only an audited ordinary battle after noncombatants are moved out of tactical responsibility.

Permitted narrow handoffs may include:

- `IMMEDIATE_YARD_THREAT_WITHDREW`
- `EXHIBITION_MATCH_COMPLETE`

Forbidden battle conclusions include:

- audience approval;
- social prestige;
- relationship changes;
- Jace rival status;
- event resumption authority;
- Caelo rank/qualification;
- Contest award;
- correctness of a public record.

Current classification: REDUCIBLE subject to exact content audit; no capability category is promoted by this design.

### Formal PTU Contest

This activity exposes an implementation gap outside the ordinary battle-capability matrix as well as touching existing permanent families such as move-specific behavior and Trainer Features/perks.

Required evidence before implementation:

- exact pinned PTU/Caelo Contest rules;
- Appeal Roll implementation;
- Contest Type and Contest Effect execution;
- Contest turn/round lifecycle;
- relevant Coordinator Feature coverage;
- exact Contest-side Move behavior;
- any Contest preparation/item rules;
- legal action/choice infrastructure for Contest participants if automated;
- Contest-specific policy if AI participants are expected to perform intelligently;
- authoritative result persistence;
- Minecraft/Cobblemon/Craftics presentation that consumes rather than recomputes the result.

Current classification: BLOCKED / UNIMPLEMENTED AS A VERIFIED COMPLETE SUBSYSTEM from evidence inspected in this pass.

Do not relabel this gap as complete merely because battle core calculations or initiative are verified for their own contracts.

## Adapter authority boundary

For pass 188:

- event IDs and authoritative status remain server-side world facts;
- posted notices and scoreboards are projections;
- client applause is presentation;
- Cobblemon animations cannot decide outcome;
- AutoPTU battle result can write only approved battle handoffs;
- PTU Contest results must come from an eventual authoritative Contest resolver or approved external rule execution;
- Narrative owns public-record provenance, not tactical recomputation;
- block break, chunk unload or NPC despawn cannot erase an event result.

## Caelo and mechanical questions still unresolved

- whether Caelo defines a Contest circuit, ranks, awards or regional judging procedure;
- whether Marea or the wider region has any canonical public exhibition tradition;
- which exact PTU Contest rules/version the project intends to execute;
- whether Contest Stats and preparation rules from the source set are in scope;
- implementation status of Appeal Rolls in Java;
- implementation status of Move Contest Effects in Java;
- implementation status of Coordinator Contest Features in Java;
- whether Contest AI belongs in AutoPTU-Java or a distinct deterministic competition module;
- how Contest outcomes persist into RPG world state;
- whether Battle Yard exhibition matches use the same challenge contract as ordinary yard battles;
- exact Item and Trainer Feature allowances for public exhibition battles;
- how Minecraft/Cobblemon/Craftics will present spectators, choreography and results without becoming rules authority.

No answer is invented here.

## Promotion rule

Capability categories advance only from live tests/contracts demonstrating the breadth required by the claim.

One Contest Feature in source data, one Appeal-related record, one Move Contest Effect, one battle animation or one forced-movement slice remains evidence for that exact slice. It cannot stand in for a complete Contest subsystem or any complete permanent battle family.