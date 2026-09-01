# Engine Readiness Snapshot — Pass 186

Status: DESIGN EVIDENCE SNAPSHOT. NOT CANON.
Date: 2026-09-01

## Scope

This snapshot records the live evidence used by recurring-rival concepts added in pass 186. AutoPTU-Java and AutoPTU are read-only from this task.

Evidence heads inspected:

- AutoPTU-Java: `1acb773545966affce865ec3f250ff02faccae57`
- AutoPTU Python oracle: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`
- Narrative base before pass 186: `27b2e236ab8bb84a2e4e3431e95fb86e4a54dbb7`

## Live Java delta

The current Java head adds `BattleRuntimeDependencies`, an immutable composition snapshot for authoritative runtime rule dependencies. `RuntimePostHitForcedMovementApplication` now resolves defender rule content through that shared dependency boundary, with regression coverage proving that defender content is selected correctly and source content is not incorrectly used for defender prevention.

This is useful architectural progress for forced-movement rule composition.

It does not prove the complete movement family.

The evidence remains narrower than:

- all Push variants;
- all Pull variants;
- all Knockback variants;
- Interception;
- collisions;
- partial stops;
- footprint-sensitive forced movement;
- chained displacement;
- ordering against reactions;
- terrain-mediated displacement;
- all Ability/Item/Feature sources of forced movement or prevention.

## Capability classification

### Targeting / footprints / range / LoS

Classification: VERIFIED for the currently audited contracts.

Rival use:

Suitable as a baseline dependency only when selected combat content stays inside verified targeting contracts.

### Base movement legality

Classification: VERIFIED for currently audited base contracts.

Rival use:

Stable-arena reduced encounters can rely on this family when they avoid unsupported advanced movement interactions.

### Complete movement including push/pull/knockback/interception/forced movement

Classification: PARTIAL.

Current evidence includes meaningful forced-movement composition and prevention slices, including runtime dependency injection.

Blocking gap:

The full family is not demonstrated. Any rival encounter selecting unsupported displacement or interception behavior must mark this family as required and blocking.

### Core calculations

Classification: VERIFIED for currently audited deterministic arithmetic contracts.

### Action economy / initiative

Classification: VERIFIED for currently audited primitives.

### Full turn / round lifecycle

Classification: PARTIAL.

A representative implemented phase or lifecycle slice cannot justify family completion. Rival battles requiring full PTU sequencing must remain capability-aware.

### Full stateful damage pipeline

Classification: PARTIAL.

Do not infer complete parity from ordinary damage examples.

### Status lifecycle

Classification: PARTIAL.

Rival roster selection for reduced encounters should avoid statuses whose complete application, persistence, cure, immunity, timing or interaction contracts are not verified.

### Terrain / weather / hazards / zones / reactions

Classification: BLOCKING as a complete family.

A Battle Yard encounter that uses environmental zones, weather phases, hazards or reaction timing must explicitly depend on this family.

Reduced rival battles should keep venue complications in world state unless exact mechanics are audited.

### Move-specific behavior

Classification: PARTIAL.

Every selected rival Move still needs exact behavior coverage. The existence of one representative Move implementation cannot stand for the catalogue.

### Abilities

Classification: PARTIAL.

Every selected Ability needs exact current coverage.

### Items

Classification: PARTIAL.

Do not permit rival Items merely because inventory presentation exists.

### Trainer Features / perks

Classification: PARTIAL.

Jace's class concepts or Sela's class concepts do not imply every Feature is implemented. Any Trainer participation contract needs exact Feature coverage.

### AI legal-action infrastructure

Classification: VERIFIED for currently audited legal-action contracts.

Important limitation:

Legality does not prove tactical quality.

### AI tactical policy

Classification: BLOCKING as a complete rival-intelligence family.

This matters especially for recurring rivals because narrative claims such as "Jace learned from the player's last match" require more than legal move generation. The policy must consume only legally known information and make an actual tactical choice from it.

Until that contract is verified, Narrative should avoid claiming adaptive rival intelligence from prior battles.

### Minecraft / Cobblemon / Craftics adapter and playback support

Classification: BLOCKING as the complete tactical adapter/playback family.

The wider RPG adapter has demonstrated useful noncombat physical surfaces in prior passes, but that does not establish complete faithful battle playback.

Rival schedules, registration boards, public records, NPC presence and noncombat world-state changes can advance independently of full tactical playback.

## Rival-specific dependency matrix

### Rival dialogue / refusal / scheduling

Battle dependencies: none.

Required narrative systems:

- persistent actor identity;
- schedule/activity state;
- challenge availability;
- institution state when relevant.

### Public battle-history review

Battle dependencies: existing authoritative result reference only.

No new combat simulation required.

### Rival offscreen training

Battle dependencies: none unless an exact battle result is claimed.

Narrative can record training attendance or completed authored activity. It cannot fabricate PTU combat outcomes or mechanical advancement not governed by policy.

### Standard audited exhibition

Required families:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- lifecycle and damage/status families to the extent selected content needs them;
- exact Moves/Abilities/Items/Trainer Features selected;
- AI legal-action infrastructure;
- AI tactical policy if credible autonomous rival tactics are required;
- playback adapter for faithful in-world presentation.

Current practical classification: REDUCIBLE, but only through audited content restrictions.

### Adaptive rematch using prior scouting

Additional requirement:

- AI tactical policy with information-boundary enforcement.

Current classification: BLOCKED for the intended strong claim of adaptive tactical learning.

A reduced rematch may happen without claiming the AI learned from history.

### Yard Circuit Test Under Pressure full version

Required families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement where displacement/interception appears;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions when venue pressure enters BattleSpec;
- move-specific behavior;
- abilities;
- items when allowed;
- Trainer Features/perks when used;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Current classification: BLOCKED.

### Yard Circuit Test Under Pressure reduced version

World-state layer first isolates the operational problem. The BattleSpec then contains only an audited stable-arena match.

Current classification: candidate for future implementation after exact roster/contract audit; no family promotion is implied by this statement.

## Python oracle evidence

Current AutoPTU head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Its latest visible commit is presentation-only Career work synchronizing viewport dimensions after resize and explicitly says battle rules and outcomes do not change.

Therefore this pass finds no Python-oracle evidence that promotes a tactical capability family.

## PTU / Caelo mechanical questions

Still unresolved for this slice:

- whether Caelo defines formal rivalry, rematch, ranking or challenge policies beyond the project's existing Narrative proposals;
- exact legal Trainer participation policy for a future Bruma Battle Yard contract;
- exact Item allowance policy;
- exact Feature set for Jace in any given encounter;
- whether any rivalry-specific reward exists in governing source material;
- how experience/significance should be resolved for repeated rival battles;
- whether any Caelo-specific public scouting restrictions apply.

No answer is invented here.

## Promotion rule

Future engine progress should promote a category only from live tests/contracts demonstrating the family breadth required by the claim.

A new representative forced-movement prevention rule, Move, Ability, status, hazard, reaction or Trainer Feature remains evidence for that slice only until broader coverage is proven.
