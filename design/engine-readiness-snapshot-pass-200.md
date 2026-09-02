# Engine Readiness Snapshot — Pass 200

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `31fdaca38fc616a2216e5d8321a8dc77cc874ab5`

Read-only engines inspected:
- AutoPTU-Java head: `fbd38166b664eafe148950bfaaf915aa956e9195`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

AutoPTU-Java advanced one commit since pass 199:

`fbd38166b664eafe148950bfaaf915aa956e9195` — `Compose forced movement prevention semantics at post-hit boundary (#323)`.

The commit composes forced-movement prevention semantic events at the post-hit boundary and adds tests around that composition. Its parent is the pass-199 head `dd8097910da62f98d07047cd0603fa8d858f4c67`.

This is meaningful evidence for one increasingly complete integration path: an already-resolved forced-movement prevention result can now carry its semantic projection through the post-hit boundary.

It is not evidence that the complete movement family is complete.

AutoPTU remains on `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, whose head message explicitly describes presentation-only coordinate synchronization after viewport resize and states that no battle rules or outcomes change.

No permanent capability category is promoted in pass 200.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

`VERIFIED` remains contract-scoped, not a claim of exhaustive combinatorial coverage.

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

## Why complete movement remains PARTIAL

The new Java commit closes composition for a specific semantic path at a post-hit boundary. The live evidence still does not close the full matrix across:

- Push;
- Pull;
- Knockback;
- Interception;
- collision behavior;
- partial stops;
- chained displacement;
- footprint interactions during displacement;
- reaction ordering;
- terrain-mediated displacement;
- every Move path;
- every Ability path;
- every Item path;
- every Trainer Feature/perk path;
- status and temporary-effect interactions;
- semantic-event parity for all prevention/movement outcomes.

Representative integration cannot promote the family.

## PTU social/information boundary

Read-only AutoPTU evidence confirms PTU Skills including Guile and Perception in the project Skill model, while trainer-class catalog/validation material references Charm, Command, Guile, Intimidate, Intuition and Perception in prerequisites/effects.

Pass 200 therefore does not invent a parallel social-resolution layer.

Narrative may preserve claims, speakers, recipients, source lineage, publications and correction history. Mechanically meaningful attempts to detect deception, conceal information, persuade, intimidate, read intent or notice hidden information remain delegated to authoritative PTU/Caelo/AutoPTU rules when mechanics are required.

A fresh literal `Caelo` search across Narrative, AutoPTU-Java and AutoPTU returned no indexed results in this pass.

Unresolved Caelo surfaces include:
- social Skill adjudication differences from baseline PTU;
- formal reputation mechanics;
- supernatural truth/intent-reading rules;
- publication/privacy rules;
- institutional notice authority.

## Pass 200 narrative-mechanics boundary

Pass 200 adds proposed Narrative records for:
- information claims and versions;
- transmission events;
- source lineage;
- bounded reception history;
- public information surfaces;
- corrections and their reach;
- unresolved contradictions;
- distributed actor impressions based on concrete events/claims.

Hard boundary:

`CLAIM_REPEATED_MANY_TIMES != CLAIM_MECHANICALLY_OR_CANONICALLY_TRUE`

and:

`CORRECTION_PUBLISHED != EVERY_NPC_UPDATED`

Narrative confidence fields describe provenance. They do not replace PTU Skill checks.

## Pass 200 rich encounter

Encounter: `Field Check after the Glass Bend Warning`.

Narrative premise:
A circulating warning says wild Pokémon have taken over the seasonal crossing. Marea Field Office or Mirador authorizes a bounded field check because the report is operationally relevant. The field team can establish only facts actually observed at that time.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required if protected withdrawal, Interception, Push, Pull, Knockback, collisions or other displacement matter
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL where selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if route surface, weather, protected zones or reactions have tactical consequences
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL where battle Items participate
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING if wild actors must prioritize territory, withdrawal, corridor pressure, observer avoidance or any non-KO objective
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful world -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

Narrative retains:
- original warning;
- every known version and transmission lineage;
- field-check mandate;
- observers/noncombatants;
- ecology observation records;
- route-advisory state;
- later correction/publication state.

Before combat:
- withdraw observers/noncombatants to a safe semantic state;
- identify one immediate actor still preventing passage;
- select only audited combatants/content;
- use stable geometry;
- omit tactical weather/hazards/zones that lack complete contracts;
- avoid forced-movement objectives unless every chosen interaction is verified.

Allowed narrow handoffs:
- `IMMEDIATE_ROUTE_THREAT_CONFIRMED_AT_TIMESTAMP`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR_AT_TIMESTAMP`

Battle output cannot determine:
- rumor origin;
- whether a speaker lied;
- population size;
- ecological cause;
- permanent route safety;
- future recurrence;
- whether every previous version was true/false;
- who heard the later correction;
- reputation or relationship changes.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI tactical-policy caution

Legal-action infrastructure does not prove an actor understands the narrative objective of a field verification encounter.

A rich version could require AI to:
- hold or abandon a crossing;
- withdraw after pressure instead of pursuing a KO;
- avoid observers;
- prioritize territorial distance;
- stop pursuit once passage opens;
- respond to protected corridor geometry.

Those are policy requirements and remain BLOCKING until verified by live tests/contracts.

## Adapter/playback caution

Information circulation creates another hard separation from Minecraft presentation.

Required boundaries include:
- rendered chat != canonical hearing by every nearby NPC;
- speech bubble visible != recipient understood/retained it;
- sign present != notice current;
- duplicated book/entity != duplicated authoritative publication;
- chunk unload != claim withdrawn;
- NPC proximity != information transfer;
- client language/localization != in-world fluency or interpretation;
- battle animation != broad public report;
- player seeing debug text != character knowledge.

The complete adapter/playback family remains BLOCKING.

## Narrative repository state for this pass

Pass 200 writes only to Narrative.

New files:
- `research/2026-09-02-information-circulation-hearsay-correction-scan-200.md`
- `design/information-circulation-hearsay-correction-continuity-layer.md`
- `proposals/2026-09-02-marea-information-circulation-seeds-200.md`
- `design/engine-readiness-snapshot-pass-200.md`

No AutoPTU-Java or AutoPTU write is authorized or performed.

## Implementation recommendation

Prototype `Mirador Heard It Twice` first.

It requires:
- no battle;
- no new NPC;
- no new Pokémon species;
- no new institution;
- no external geography;
- no PTU Skill adjudication;
- no reputation score.

It verifies the main new behavior: two reports can remain separate historical records while source-lineage analysis shows that they derive from one upstream account. This directly strengthens Mirador, Tideglass, Mara, Nerea and Pia without resolving any existing canon mystery.
