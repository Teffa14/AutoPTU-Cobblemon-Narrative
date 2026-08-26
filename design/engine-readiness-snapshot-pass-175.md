# Engine Readiness Snapshot — Pass 175

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU remain read-only in this task.

## Live heads inspected

AutoPTU-Java: `453210d46a04ebc52babc675ce7824f83991da5d`

Latest inspected Java work: `Run secondary status move specials for area targets (#210)`.

The integration test exercises an authoritative area Move over two targets, applies Poisoned to one target, respects Immunity on the other, spends the Standard Action once and records Move frequency use once. This is meaningful evidence that the live multi-target pipeline can now run the generic secondary-Status path per target for that contract.

It does not prove every area Move, secondary effect, Status, Ability interaction or timing edge case.

AutoPTU Python: `68427feebcc1728fd6bcb53b6520a82595ab956b`

Latest inspected Python change keeps Career trainer dialogue neutral on draws. It explicitly concerns presentation/Career behavior and does not change tactical readiness.

## Java README boundary

The current Java README still lists these as unfinished full systems:

- core combatant/grid battle state;
- full damage resolution pipeline and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

The latest secondary-Status integration is therefore a verified slice inside larger PARTIAL families.

## Permanent capability map

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING as complete families

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

## Pass 175 system boundary

Civic volunteering and donations are primarily world-state systems. They do not require battle mechanics for intake, assignment, donation review, receipt, service completion or institutional handoff.

The battle engine is required only when a separate confrontation intersects an active service project or staging site.

Volunteers, donors, staff, donated goods, forklifts, staging tables, collection bins and similar objects must remain outside AutoPTU battle authority unless an exact supported contract exists.

## Encounter dependency — Volunteer Staging Area Evacuation

FULL version:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if exact Status effects are used
- terrain/weather/hazards/zones/reactions — BLOCKING if evacuation lanes, environmental effects or reaction mechanics are tactical
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for `EVACUATE`, `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_STAFF`
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

REDUCED version:

Civic Support/Crisis evacuates volunteers and resolves wildlife movement before battle. AutoPTU receives a static arena with legal combatants only. Reopening the staging site remains world state.

## Encounter dependency — Donation Warehouse Route Blockage

FULL version:

- basic targeting/movement/action infrastructure — VERIFIED where used conventionally;
- complete movement — BLOCKING for a live clear-route/escort objective;
- AI tactical policy — BLOCKING for `CLEAR_ROUTE`, `WITHDRAW`, `PROTECT_WORKER`;
- adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if shelving, spills, moving equipment or blocked lanes have tactical effects;
- items — PARTIAL if a donated PTU Item is used mechanically;
- remaining combat families — PARTIAL according to the permanent map.

REDUCED version:

Stop loading, remove workers, freeze authoritative inventory state and resolve any battle in a clear static exterior/loading-yard arena. Supply Chains decides stock usability afterward.

## Encounter dependency — Trail Stewardship Workday Interruption

FULL version:

- complete movement — BLOCKING for simultaneous worker withdrawal, wildlife withdrawal/crossing or interception;
- AI tactical policy — BLOCKING for non-hostile withdrawal and corridor goals;
- Minecraft/Cobblemon/Craftics playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING only if slope, falling debris, unstable surfaces or dynamic route state have tactical effects;
- targeting/base movement/core/action/AI legality — VERIFIED;
- lifecycle/damage/status/move/ability/item/Trainer Feature families — PARTIAL when invoked.

REDUCED version:

The work session ends and all workers/equipment are accounted for first. Wildlife movement resolves in world state where possible. AutoPTU handles only the independent static confrontation that remains.

## Noncombat dependency — Donation Review Dispute

No battle engine required.

Relevant authorities:

- Civic Volunteering & Donations
- Supply Chains
- Material Culture
- Finance / Currency Settlement
- Agreements
- relevant safety/quality authority for the item type

Possible results include acceptance, partial acceptance, redirection, more information needed or refusal.

No social Skill roll is invented by this layer.

## PTU/Caelo guardrails

Pass 175 adds no mechanical service progression.

Forbidden inferences include:

- volunteer history -> XP / Trainer Level / Skill Rank / Edge / Feature;
- volunteer vest -> credential;
- repeated participation -> Command or Charm bonus;
- donated item -> immediately usable PTU Item;
- money pledge -> settled funds;
- worker presence -> rescue qualification;
- Pokémon accompanying a volunteer -> institutional working role;
- Pokémon helping once -> future willingness or Loyalty change;
- crowd enthusiasm -> morale mechanics;
- donation amount -> Influence or prestige mechanics.

The accessible PTU corpus recognizes Skills such as Command, Charm, General Education, Medicine Education, Pokémon Education, Survival and Technology Education. None creates a generic volunteer qualification or donation mechanic.

No reliable Caelo primary material recovered in this run defined charitable organizations, volunteering, fundraising, donations or service-based progression. Super PTU Online Helper was not available as an invocable capability.

## Unresolved rules/canon questions

- Which Ouros settlements have standing civic-support organizations?
- Does any Ranger-like institution exist, and what authority separates it from volunteers and emergency services?
- Which assignments require authored credentials?
- How are spontaneous helpers handled during large incidents?
- Are formal charitable entities part of regional canon or are most support networks informal?
- How does Ouros culturally handle public recognition, anonymous giving and donor conditions?
- Can player-founded clubs create volunteer programs or donation drives, and under what governance?
- What privacy is expected for service histories and donation records?
- Which donated goods need quality/safety review before entering inventory?
- What Pokémon service roles, if any, are established canon rather than generated from species flavor?

No answer is promoted to canon by this snapshot.
