# Engine Readiness Snapshot — Pass 195

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: `32fd056661b4793c02c4ee453864e58da8113791`

Read-only engine repositories:
- AutoPTU-Java head inspected: `c34e10a57a7c3f93dd184c09a03d87fb9a014a34`
- AutoPTU head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live-engine delta

No new AutoPTU-Java commit appeared after the head inspected in pass 194.

Latest Java evidence remains commit `c34e10a57a7c3f93dd184c09a03d87fb9a014a34`, which preserves Python defender-prevention precedence for forced movement, separates status and temporary-effect prevention paths, preserves first-blocker provenance, and prevents one resolution from simultaneously representing movement and prevention.

This is useful parity evidence inside forced movement. It still does not close the complete-movement category.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is presentation-only viewport-coordinate synchronization and explicitly does not change battle rules or outcomes.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains scoped to audited contracts rather than universal content completion.

### PARTIAL

- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

### BLOCKING when the complete family is required

- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

No category is promoted because one representative mechanic, data row, test or hook exists.

## PTU communication evidence

Read-only AutoPTU inspection found mechanical content for Channeler/Channeling and Telepathy.

Relevant constraints:

- Channeling has explicit semantics for communicating intentions, emotions and motivations while channeling a Pokémon;
- Telepathy has explicit target/range/Focus/resistance semantics in supplied PTU content;
- Channeler and Telepath exist as specific Trainer mechanical identities;
- Python career adapters include these supernatural classes in a `narrative_unlock` grouping;
- trainer-runtime coverage still contains missing runtime mappings across Trainer content.

Therefore catalog/source presence is not proof of complete executable support.

Narrative must not treat a dialogue option, interpreter record, species identity, Cobblemon animation or generic AI behavior as equivalent to Channeling or Telepathy.

## Communication-specific mechanical boundary

This pass creates no new permanent engine category.

Ordinary transcription, translation and interpretation are narrative/world-state functions.

Mechanically consequential supernatural communication depends on exact content support:

- if Channeling is required, the exact Channeler Feature path must be verified;
- if Telepathy is required, the exact Telepathy capability/Feature path must be verified;
- if either affects battle choices, Trainer Features/perks and any associated state/action lifecycle must be audited;
- if AI is expected to act on communicated tactical intent, legal-action infrastructure alone is insufficient; tactical policy also matters.

Current disposition for generic supernatural communication claims: PARTIAL / CONTENT-SPECIFIC, not globally verified.

## Pass 195 rich encounter disposition

Encounter: `Interpreter at the Seasonal Crossing`

Full version dependencies:

- targeting/footprints/range/LoS: VERIFIED for audited contracts;
- base movement legality: VERIFIED for audited contracts;
- complete movement: PARTIAL and blocking if protection depends on interception, Push, Pull, Knockback, collisions, partial stops or forced movement;
- core calculations: VERIFIED for audited contracts;
- action economy/initiative: VERIFIED for audited contracts;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL when selected content uses statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if route edges, weather, hazards, zones or reactions become tactical;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features/perks: PARTIAL, and directly relevant if Channeler/Telepath or other Trainer content participates;
- AI legal-action infrastructure: VERIFIED for audited contracts;
- AI tactical policy: BLOCKING for objective-aware withdrawal/protection/spacing behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful projection and return to persistent world state.

Disposition: FULL VERSION BLOCKED.

## Complete-movement caution

Current forced-movement work must not be generalized into complete movement readiness.

Still not demonstrated as one closed verified matrix:

- all Push behavior;
- all Pull behavior;
- all Knockback behavior;
- all Interception behavior;
- collision handling;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering across all relevant effects;
- terrain-mediated displacement;
- all combinations with Moves, Abilities, Items, Trainer Features, statuses and temporary effects.

Category remains PARTIAL.

## Reduced encounter viability

The reduced version is viable without pretending missing mechanics exist.

Narrative retains:

- source document identity;
- rendering/translation versions;
- disputed spans;
- interpreter identity and availability;
- visitor/courier status;
- route purpose;
- actor knowledge of each version;
- post-encounter interpretation workflow.

Noncombatants withdraw before BattleSpec. If one wild actor still blocks passage, compile a separate ordinary audited battle on stable geometry using only supported content.

Allowed narrow outputs:

- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`

Battle output must not establish:

- translation accuracy;
- source authenticity;
- interpreter competence;
- actor fluency;
- ancient historical truth;
- institutional acceptance;
- Pokémon thoughts or intentions outside exact PTU mechanics;
- whether an interpretation should supersede another.

## Minecraft/Cobblemon projection boundary

The adapter may display books, signs, subtitles, UI translations and Pokémon animations. None of these become authority over interpretation state.

Mandatory separation:

- client localization is accessibility/presentation;
- diegetic language state belongs to narrative world state;
- a localized subtitle does not grant character fluency;
- a book item does not become the only canonical copy;
- item duplication does not duplicate legitimate documentary provenance;
- despawn does not erase a source;
- Pokémon vocalization animation does not prove semantic content;
- Cobblemon behavior does not grant Channeling or Telepathy.

This family remains BLOCKING for full end-to-end playback where the distinction must survive projection and return.

## Caelo uncertainty

Repository search for literal `Caelo` across Narrative, AutoPTU-Java and AutoPTU returned no indexed results in this run.

No inspected live source establishes:

- Ouros/Caelo human language map;
- dialect boundaries;
- official translation standards;
- interpreter licensing;
- ancient Marea scripts;
- ordinary literacy assumptions;
- mundane language-learning mechanics;
- telepathic privacy norms;
- generic Pokémon speech rules.

All remain unresolved.

## Implementation recommendation

Implement `One Word, Two Copies` first.

It tests:

- immutable source expressions;
- separate transcription/rendering records;
- span-level uncertainty;
- competing legitimate readings;
- revision history;
- actor-specific knowledge;
- Tideglass/Pia/Taro canon reuse.

It requires no battle capability, no new language canon and no supernatural mechanics.