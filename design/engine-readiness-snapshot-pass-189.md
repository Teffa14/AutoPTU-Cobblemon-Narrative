# Engine Readiness Snapshot — Pass 189

Status: DESIGN / LIVE EVIDENCE SNAPSHOT.
Date: 2026-09-01
Narrative base before this pass: `abe1e29aa4fe4e4c197e5cf06422495041b0b2bf`
AutoPTU-Java inspected head: `1acb773545966affce865ec3f250ff02faccae57`
AutoPTU inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

This snapshot uses the project's permanent capability families. It does not infer family completeness from one representative mechanic.

## Live evidence changes

No newer AutoPTU-Java commit was present at this run than `1acb773545966affce865ec3f250ff02faccae57`.

That head routes forced-movement prevention through shared `BattleRuntimeDependencies` carrying authoritative combatant rule content. Previous recent slices also expose prevention provenance and bind content-backed prevention through the canonical registry seam.

This is useful architectural evidence for forced-movement composition and ownership. It still does not prove the complete movement family. In particular, current evidence reviewed for the narrative project does not establish full coverage of Push, Pull, Knockback, Interception, collisions, partial stops, chained displacement, footprint interactions, reaction ordering and terrain-mediated displacement in all required combinations.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest visible change synchronizes cached presentation coordinates after viewport resize and explicitly states that battle rules and outcomes are unchanged. It supplies no new reason to promote a tactical family.

## Permanent capability classification

### VERIFIED for currently audited contracts

Targeting / footprints / range / LoS.

Base movement legality.

Core calculations.

Action economy / initiative.

AI legal-action infrastructure.

`VERIFIED` here means the narrative project has sufficient live contract evidence for the covered baseline behavior used by reduced encounters. It does not mean every conceivable content interaction in the family is complete.

### PARTIAL

Complete movement including push/pull/knockback/interception/forced movement.

Full turn/round lifecycle.

Full stateful damage pipeline.

Status lifecycle.

Move-specific behavior.

Abilities.

Items.

Trainer Features / perks.

A concept depending on a specific Move, Ability, Item, Feature, state transition or displacement interaction must audit that exact content and contract before implementation.

### BLOCKING when the complete family is required

Terrain / weather / hazards / zones / reactions.

AI tactical policy.

Minecraft / Cobblemon / Craftics adapter and faithful playback support as a complete family.

Some RPG-side world representations already exist elsewhere in the broader project history. That does not verify the complete tactical adapter/playback contract required for rich battle scenes.

## Pass 189 correspondence implications

The correspondence continuity layer itself has no BattleSpec dependency.

The recommended first slices — custody of an unread packet, stale posted revision, delayed message arriving after autonomous resolution — can run entirely in narrative/world state if the RPG persistence layer supports stable records and physical projections.

`Courier at the Glass Bend` becomes mechanically expensive only when the authored scene asks the battle engine to represent route geometry, a vulnerable courier, interception, displacement, environmental pressure or objective-aware tactical behavior.

### Courier at the Glass Bend — intended full version

Required families when all proposed richness is active:

- targeting/footprints/range/LoS: required;
- base movement legality: required;
- complete movement including push/pull/knockback/interception/forced movement: required when selected content or protective positioning uses those interactions;
- core calculations: required;
- action economy/initiative: required;
- full turn/round lifecycle: required;
- full stateful damage pipeline: required;
- status lifecycle: required when selected content uses statuses;
- terrain/weather/hazards/zones/reactions: required when route or environmental conditions become tactical;
- move-specific behavior: required for every selected Move;
- abilities: required for every selected Ability;
- items: required for every mechanically active Item;
- Trainer Features/perks: required when Trainers participate mechanically;
- AI legal-action infrastructure: required;
- AI tactical policy: required if actors must reason about retreat, corridor protection, courier safety or competing tactical objectives;
- Minecraft/Cobblemon/Craftics adapter/playback support: required for faithful in-world execution and presentation.

Current classification: BLOCKED for the intended full form.

### Reduced version

The reduced contract keeps message identity, courier custody, delivery timing, noncombatant position and route decision in narrative world state.

If a wild threat remains after the courier reaches an authored safe position, compile a separate ordinary battle on stable terrain using only exact audited content.

Allowed narrow battle handoffs include:

- `IMMEDIATE_ROUTE_THREAT_WITHDREW`;
- `IMMEDIATE_PASSAGE_CLEAR`.

Narrative retains authority over:

- packet authenticity;
- current or superseded message state;
- custody;
- delivery attempt outcome;
- reading;
- acknowledgment;
- acceptance or refusal of requested work;
- public/private visibility;
- archival state;
- later reply;
- correspondence-thread closure.

Current classification: REDUCIBLE when the separated battle roster and mechanics remain inside verified or exact-audited contracts.

## PTU / Caelo evidence boundary

Searches in Narrative, AutoPTU-Java and AutoPTU did not locate indexed `Caelo` rule text during this pass.

AutoPTU search hits for `Mail` include general Pokémon item/source data and unrelated technical strings. They do not establish a verified PTU correspondence engine.

Do not infer any of the following without direct source evidence:

- a Courier Feature;
- a Delivery Skill;
- automatic message authentication;
- regional postal law;
- seals with mechanical authority;
- messenger-Pokémon rules;
- telepathic or supernatural delivery conventions;
- a communication-range mechanic;
- privacy or interception rules.

## Unresolved mechanical questions

Does the pinned PTU/Caelo source set define any mundane or supernatural communication mechanics that should constrain authored correspondence?

Are there exact Pokémon Capabilities, Moves, Abilities, Items or Trainer Features intended to transport, conceal, intercept, copy or authenticate information?

If a future scene uses a Pokémon as courier, which exact world-simulation behavior is authoritative and which, if any, PTU mechanic governs it?

Can the current Minecraft layer bind a physical book/item/packet to a stable server-side record without treating inventory ownership as institutional custody?

How will duplicated, destroyed, unloaded or restored physical projections reconcile against one authoritative message/copy record?

## Unresolved canon questions

Which Marea roles may validly receive addressed correspondence on behalf of another role?

Which institutions maintain incoming/outgoing logs, if any?

Which existing resident responsibilities permit temporary custody of sealed packets?

Does Marea have routine public posting surfaces beyond those already explicitly authored in individual content?

What communication methods exist between Marea and other settlements?

What counts as an authenticated message under Caelo practice?

What privacy expectations exist around addressed correspondence?

How common is literacy and written recordkeeping outside the already established archival/research institutions?

These remain open. Pass 189 must not answer them by implication.