# Engine Readiness Snapshot — Pass 197

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative head before this pass: `093706bb6599e22c53c98cb17f9a6ccf63340c00`

Read-only engine repositories inspected:

- AutoPTU-Java head: `6a545eab7f70ec452a5d7dc9d67c91ce50b2288c`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live-engine delta

AutoPTU-Java advanced one commit beyond pass 196.

New commit:

`6a545eab7f70ec452a5d7dc9d67c91ce50b2288c` — `Fix forced movement semantic-event oracle guard (#321)`.

The change modifies `tools/python/export_forced_movement_observable_contract.py`. It strengthens the parity guard so the oracle check distinguishes the actual `trainer_feature` semantic-event discriminator from unrelated calls such as the `has_trainer_feature` predicate. It also separately verifies that `Insectoid Utility` and `Wallclimber` remain in the pinned Python function text.

This improves the quality of the forced-movement parity contract. It does not implement another forced-movement mechanic or establish complete Java semantic-event parity.

No permanent capability category is promoted by this commit.

AutoPTU Python remains pinned at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit is presentation-only viewport-resize coordinate synchronization and explicitly does not change battle rules or outcomes.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains scoped. It is not a claim that every combination in the family has complete coverage.

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

No category is promoted in pass 197.

## Complete-movement caution after Java #321

The new Java head strengthens an oracle-guarding tool around one exact forced-movement prevention semantic obligation.

It still does not close the complete movement matrix across:

- Push;
- Pull;
- Knockback;
- Interception;
- collisions;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering;
- terrain-mediated displacement;
- combinations with Moves;
- combinations with Abilities;
- combinations with Items;
- combinations with Trainer Features;
- combinations with statuses and temporary effects;
- complete semantic-event parity.

`complete movement` therefore remains PARTIAL.

## Pass 197 narrative-mechanics boundary

This pass introduces no new battle rule. It introduces persistent cultural evidence records for:

- repeated practice;
- individual practice instances;
- oral accounts;
- attributed meaning/origin claims;
- practice variants;
- participant scope;
- material traces linked to provenance.

These are Narrative/world-state responsibilities.

They must not author:

- PTU Skill Ranks;
- Trainer Features;
- mechanical bonuses from tradition participation;
- supernatural truth;
- battle outcomes;
- Legendary encounter rules;
- religion or spiritual authority.

## PTU Skill source evidence

The pinned AutoPTU source set contains explicit education Skills. Current repository search finds `Occult Education` in:

- class prerequisites;
- class validation/catalog data;
- source books/audit text;
- character-creation Skill lists;
- engine code that reads a combatant's Occult Education rank for governed effects.

This is sufficient to establish an authority boundary: Narrative cannot create a substitute folklore/lore Skill or grant ranks from participation.

It is not sufficient to claim a complete generic knowledge-check runtime for every narrative history/folklore situation in Java.

Disposition:

`PTU SKILL CONTENT EXISTS; NARRATIVE CULTURAL KNOWLEDGE MUST NOT BYPASS IT; COMPLETE JAVA NARRATIVE KNOWLEDGE-CHECK PIPELINE NOT VERIFIED BY THIS PASS.`

## Cultural-claim boundary

Even if a future exact PTU procedure permits an Education or Intuition check, its success must be interpreted within that procedure.

Examples:

- recognizing a commonly repeated story does not prove the story historically true;
- identifying an Occult tradition does not prove supernatural efficacy;
- recalling a local phrase does not establish region-wide adoption;
- knowing that residents attribute meaning to an object does not make the object magical;
- high Occult Education does not automatically identify a Ghost-type as a deceased person's spirit.

Narrative should preserve the mechanical result and the attributed claim separately.

## Pass 197 rich encounter

Encounter: `Community Route Walk at Glass Bend`.

Narrative premise:

A repeated practical/community walk uses part of Sendero del Vidrio. Different participants may assign different significance to it. Wild activity creates an immediate safety problem during one occurrence.

### Full intended dependency classification

- targeting/footprints/range/LoS: VERIFIED for audited contracts
- base movement legality: VERIFIED for audited contracts
- complete movement: PARTIAL; blocking if protection/withdrawal uses Interception, Push, Pull, Knockback, collisions or other forced movement
- core calculations: VERIFIED for audited contracts
- action economy/initiative: VERIFIED for audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if route conditions, zones or reactions affect tactical legality
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL; Java #321 only strengthens a guard around one exact Feature/movement oracle obligation
- AI legal-action infrastructure: VERIFIED for audited contracts
- AI tactical policy: BLOCKING for objective-aware protection, withdrawal, corridor priority or deliberate avoidance of noncombatants
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for a complete world-group -> battle -> persistent-world loop

Disposition: FULL VERSION BLOCKED.

## Reduced encounter contract

The narrative premise can run without missing rule families.

Narrative retains:

- practice identity;
- participant list;
- oral accounts and meaning claims;
- route/social purpose;
- material objects;
- noncombatants;
- interruption record;
- later continuity and recollection.

Before BattleSpec:

- move noncombatants to a safe authored world-state position;
- choose stable arena geometry;
- use only audited combatants and content;
- omit unverified tactical weather, hazards, zones and reactions;
- do not make the practice itself grant modifiers;
- do not require forced-movement objectives unless exact selected interactions are separately verified.

Allowed narrow battle outputs:

- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`

Battle output cannot establish:

- practice origin;
- age;
- belief;
- historical truth;
- supernatural efficacy;
- festival status;
- community-wide adoption;
- participant relationship change;
- future recurrence;
- truth of an oral account.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## Minecraft/Cobblemon/Craftics boundary for cultural continuity

The adapter family remains blocking for complete implementation because visible event state must project rather than author the records.

Required distinctions include:

- NPC presence at a gathering is not automatically recorded participation;
- chunk unload is not event completion;
- a decorative block is not a canonized ritual object;
- breaking a marker does not erase its provenance/history;
- wild Pokémon spawning nearby does not prove ecological or supernatural causation;
- particles/animations cannot produce blessings, morale or PTU bonuses;
- client-localized dialogue does not change in-world historical wording;
- duplicate NPC entities cannot create duplicate historical participants;
- battle playback cannot rewrite an oral account or current practice version.

## AI tactical-policy caution

The reduced encounter avoids a major unverified requirement.

Legal-action infrastructure can constrain illegal choices, but that is not evidence that wild or allied AI can reason about objectives such as:

- prioritize withdrawal over damage;
- keep distance from noncombatants;
- protect a corridor;
- avoid disrupting a gathering area;
- retreat once passage is clear;
- preserve an escort target.

Those are tactical-policy requirements and remain blocking until current tests/contracts demonstrate them.

## Caelo uncertainty

Literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed results during this pass.

Therefore no inspected evidence currently establishes:

- Caelo religions;
- Marea religious affiliation;
- official festivals/holidays;
- ritual obligations;
- sacred geography;
- priesthood/clergy;
- cultural ownership law;
- formal oral-history authority;
- supernatural efficacy standards;
- pilgrimage rules;
- region-wide etiquette around traditions.

All remain unresolved.

## Implementation recommendation

Implement `Two Tellings at Tideglass` first.

It requires no battle, no new Skill check, no supernatural content, no new institution and no religion/festival canon. It tests the essential architecture immediately:

- separate sources;
- separate tellers/provenance;
- overlapping claims;
- disagreement without villainy;
- partial corroboration;
- unresolved origin;
- durable future references.

A later slice can connect that state to community education or visitor interpretation before any mechanically rich route event is attempted.