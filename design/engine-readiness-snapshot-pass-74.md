# Engine Readiness Snapshot — Pass 74

Status: implementation evidence snapshot. Not canon.

## Read-only sources inspected

AutoPTU-Java head: `95134b1d7089520f2e1aad917d38ce1940622318`

AutoPTU Python head: `408c3a1ca3253592dbd04d17594492439bcc90db`

Narrative repo pre-pass head: `17cde1d6d888ea7b329190babf6b04a1b5a73370`

Live Java README inspected at Pass 74.

## Java evidence since Pass 73

AutoPTU-Java advanced beyond the Pass 73 snapshot.

Relevant commits:

- `343ff74d068cf42a7db83ad706cff03117a9fbd5` — generic held-item START temporary-effect resolver with Python parity.
- `6beb908f4246eb9f2e94161e3e28e4044be8fa92` — extended generic held-item START calculation-effect families.
- `95134b1d7089520f2e1aad917d38ce1940622318` — server-owned held-item rule catalog boundary with tests, frozen ownership and Python parity gate.

Earlier live lifecycle evidence remains relevant:

- `84505214d4bca41610f36f0a178e675ef0ab26ba` — StatusController phase-envelope ordering.
- `b1dc29e3beae24f56d1106129cb1fa61db55b069` — phase-envelope dispatcher.
- `87ee4652b8d1d123f6b1180bf4f652053d40cb73` — phase envelope wired into live lifecycle.

This is meaningful additional evidence for Items and for the full turn/round + status lifecycle families. It still represents bounded rule slices rather than complete registries or complete battle state.

The live Java README still explicitly lists as pending:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- move, ability, item, perk and Trainer Feature hook registries;
- semantic battle-event emission and full `BattleSpec -> BattleTranscript` parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

## Python evidence since Pass 73

AutoPTU Python remains at `408c3a1ca3253592dbd04d17594492439bcc90db` in the live commit search used by this run.

Recent Python work remains Career robustness: preventing a Training Kit path from leaving a zero-Pokémon roster and keeping scouting available for an empty roster.

This does not change a Java tactical capability category.

## Permanent capability map

### targeting / footprints / range / LoS

Status: VERIFIED

Java explicitly supports range, areas, footprints, target anchors and line of sight in its legal action infrastructure.

### base movement legality

Status: VERIFIED

Shift/Jump legality, Overland/Swim/Sky, terrain costs, blockers, Wallrunner, sprint, water/landing-fit behavior remain implemented.

This classification excludes push/pull/knockback/interception and other forced movement.

### complete movement including push / pull / knockback / interception / forced movement

Status: BLOCKING

Forced movement remains explicitly pending in the current Java README. No Pass 74 evidence closes interception or the complete movement family.

### core calculations

Status: VERIFIED

Damage Base, type-effectiveness steps, combat stages, accuracy stages, weather DB calculation primitive, crit probability, Burn, modifier ordering and rounding primitives remain implemented.

A calculation primitive does not establish lifecycle or world-state integration.

### action economy / initiative

Status: VERIFIED

Typed turn flow, phases, action budget, deterministic initiative, Trick Room/League ordering and declared-action ordering remain implemented.

### full turn / round lifecycle

Status: PARTIAL

The StatusController phase envelope is ordered, dispatched and wired to live lifecycle, and held-item START behavior now owns more parity-tested slices. Core combatant/grid state, complete status behavior, complete hooks and transcript parity remain unfinished.

### full stateful damage pipeline

Status: PARTIAL

Core damage calculations exist. Full damage resolution remains explicitly pending.

### status lifecycle

Status: PARTIAL

The phase envelope is real live evidence and some START behavior is parity-gated. The live README still lists StatusController work as pending, so the family is not complete.

### terrain / weather / hazards / zones / reactions

Status: BLOCKING

Java has a weather DB calculation primitive and terrain-cost movement support. Tactical terrain, hazards, zones, reactions and full environmental lifecycle remain incomplete/pending. Pass 74 must not turn an overworld unsafe condition into a PTU Hazard without a verified rule/controller path.

### move-specific behavior

Status: PARTIAL

Representative rule infrastructure exists. The complete move hook registry remains pending.

### abilities

Status: PARTIAL

Representative calculations do not establish complete Ability behavior. Ability hooks remain incomplete.

### items

Status: PARTIAL

Pass 74 has stronger evidence than Pass 73: held-item START effect families plus a server-owned rule catalog boundary are parity-gated. The live README still lists the full item hook registry as pending, and complete timing/consumption/stateful behavior is not established.

### Trainer Features / perks

Status: PARTIAL

Focused Training/Chronicler Accuracy slices remain valid evidence. Complete feature/perk registry coverage remains pending.

### AI legal-action infrastructure

Status: VERIFIED

Deterministic legal-choice generation remains present for Shift, direct targets, SELF/FIELD, tile-aimed AoE, footprints, LoS and action-budget filtering.

### AI tactical policy

Status: BLOCKING

AI scoring/policy remains explicitly pending. Legal choice generation does not imply objective-aware withdrawal, protection, territorial behavior or route-clearing policy.

### Minecraft / Cobblemon / Craftics adapter and playback

Status: BLOCKING

The Java README still describes AutoPTU-Java as the rules library that a future Craftics/Cobblemon/Minecraft adapter will consume. No parity-safe adapter/playback family is complete.

## Pass 74 encounter consequences

### Scaffold-Line Evacuation

Intended full version requires:

- VERIFIED targeting/footprints/range/LoS;
- VERIFIED base movement;
- BLOCKING complete movement for knockback/interception/forced displacement and simultaneous withdrawal;
- VERIFIED core calculations;
- VERIFIED action economy/initiative;
- PARTIAL full turn/round lifecycle;
- PARTIAL full stateful damage;
- PARTIAL status lifecycle;
- BLOCKING terrain/weather/hazards/zones/reactions if dynamic unsafe cells or environmental effects matter tactically;
- PARTIAL move-specific behavior;
- PARTIAL abilities;
- PARTIAL items;
- PARTIAL Trainer Features/perks;
- VERIFIED AI legal-action infrastructure;
- BLOCKING AI tactical policy for WITHDRAW/PROTECT/CLEAR_ROUTE/territorial goals;
- BLOCKING adapter/playback for preserving worker routes, area closures and exact objective state.

Reduced version:

Work is stopped before battle. Workers and assessors leave via world state. The questionable elevated section is excluded from the tactical map. AutoPTU resolves a static conventional encounter in a safe perimeter. Assessment continues afterward. The battle transcript cannot diagnose the physical cause or authorize return to work.

### Loading-Bay Interruption

Intended full version requires complete movement, possible dynamic zones/reactions, objective-aware AI and adapter playback if workers/cargo move simultaneously with combat.

Reduced version:

The bay is emptied. Cargo, workers and equipment remain persistent world-state objects outside battle. AutoPTU resolves only the local threat on a static arena. Near-miss reconstruction then uses shift assignments, custody, maintenance records and observations.

### Wildlife at the Temporary Route

Intended full version could require dynamic access, civilian withdrawal, territorial/escape AI and adapter synchronization.

Reduced version:

The work route closes before battle and workers leave. If battle is required, it occurs on static safe terrain. Ecology/Wild Agency decides later whether timing, rerouting, monitoring or coexistence changes are appropriate. Victory does not establish historical causation.

### Five Reports, Four Events

No tactical capability is required. The mystery uses provenance, timestamps, stable event IDs, work assignments, equipment custody, testimony and maintenance history.

It can execute before the Minecraft combat adapter exists.

## Worksite-safety mechanical boundary

Pass 74 can persist:

- safety observations;
- near-miss event history;
- work-area restrictions;
- temporary operational controls;
- briefing/handoff records;
- corrective-action references;
- verification and return-to-work state;
- links to Maintenance, Staffing, Equipment, Credentials, Crisis, Care, Ecology and Case systems.

It cannot itself define or alter:

- PTU Hazards or terrain effects;
- forced movement;
- knockback/push/pull;
- reactions/intercepts;
- Accuracy or Evasion;
- damage;
- statuses;
- Moves;
- Ability behavior;
- item timing/effects;
- Trainer Feature effects;
- initiative/action budget;
- tactical AI;
- Pokémon occupational capabilities from species/type alone.

A dangerous overworld condition only becomes a tactical mechanic when PTU/Caelo rules and current implementation evidence support the exact mapping.

## Promotion decision

No permanent capability category is promoted in Pass 74.

The held-item rule catalog at `95134b1d` materially strengthens the Items family and reinforces lifecycle ownership, but the family remains PARTIAL because the live README still lists item hooks and broader battle state as incomplete.

## Open mechanical questions

- Which held-item phases beyond START are now planned after the server-owned rule catalog boundary?
- When will item consumption, END timing and complete item hook coverage reach parity?
- When will StatusController move from representative live slices to complete behavior?
- When will full combatant/grid battle state and full stateful damage land?
- When will forced movement and interception become authoritative?
- What exact representation will PTU terrain, hazards, zones, weather lifecycle and reactions use?
- Will objective semantics such as WITHDRAW, PROTECT, CLEAR_ROUTE or ESCAPE live in BattleSpec/BattleTranscript?
- When will AI policy understand those objectives rather than only receive legal choices?
- What is the first parity-safe Minecraft/Cobblemon/Craftics adapter/playback slice?
- How will world-state safety restrictions exclude cells/areas from a battle without the adapter inventing PTU rules?

Until contracts/tests answer those questions, Pass 74 mechanically rich scenes keep reduced implementations.