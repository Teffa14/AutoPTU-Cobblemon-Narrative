# Engine Readiness Snapshot — Pass 202

Status: DESIGN / LIVE-EVIDENCE SNAPSHOT
Date: 2026-09-02
Narrative head before pass: `9636a0b998a2c12e9207edae841b1145ad8eb684`

Read-only engines inspected:
- AutoPTU-Java head: `f320aca406e3da87427eca32ab97943062c264ff`
- AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

## Live engine delta

AutoPTU-Java advanced after pass 201 to `f320aca406e3da87427eca32ab97943062c264ff` — `Freeze forced-movement ability semantic contract (#324)`.

The commit strengthens oracle-guard coverage around Ability-family forced-movement prevention. The exporter now requires pinned Python branches involving `push_immunity`, `Suction Cups` and `Sumo Stance`, and requires an observable semantic-event discriminator for the `ability` family.

This is useful parity-contract evidence for a specific forced-movement prevention family. It does not establish full support for every Ability, every Push/Pull/Knockback/Interception interaction, collision behavior, partial stop, chained displacement, terrain-mediated movement or all semantic-event combinations.

AutoPTU remains on `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head remains presentation-only and explicitly states that battle rules/outcomes do not change.

No permanent capability category is promoted in pass 202.

## Permanent capability classification

### VERIFIED within currently audited contracts

- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

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

## Complete movement caution

The new Ability-family oracle guard freezes evidence for selected prevention branches. It does not close:
- all Push paths;
- all Pull paths;
- all Knockback paths;
- Interception;
- collisions;
- partial displacement;
- chained displacement;
- footprint interactions during movement;
- reaction ordering;
- terrain-mediated displacement;
- all Move/Ability/Item/Feature/status combinations;
- end-to-end adapter/playback parity.

`complete movement` remains PARTIAL.

## Pass 202 PTU/Caelo boundary

Pass 202 adds no new mechanical currency, healing, crafting, social or reward rules.

Narrative may preserve:
- reported needs;
- aid offers;
- allocation decisions;
- contribution provenance;
- shared-project state;
- resource references;
- partial fulfillment;
- released/returned contributions;
- voluntary reciprocity history.

Authoritative systems continue to own:
- actual currency balances and transfers;
- PTU Item identity/effects;
- healing and Injury/status changes;
- crafting/repair mechanics;
- Pokémon and Trainer capabilities;
- Skills, Edges and Features;
- battle legality and outcomes.

No indexed Caelo material reviewed in this pass establishes welfare law, insurance, taxation, compulsory contributions, entitlement rules or automatic social rewards for aid.

## Pass 202 rich encounter

Encounter: `Relief Shipment Withdrawal at Glass Bend`.

Narrative premise:
A small shipment already allocated to a legitimate Marea need is moving through Sendero del Vidrio. Wild activity creates an immediate withdrawal problem. The shipment's social purpose and allocation history remain outside tactical authority.

### Full intended dependency matrix

- targeting/footprints/range/LoS: VERIFIED within audited contracts
- base movement legality: VERIFIED within audited contracts
- complete movement: PARTIAL; required if protected withdrawal, Interception, Push, Pull, Knockback or other displacement matters
- core calculations: VERIFIED within audited contracts
- action economy/initiative: VERIFIED within audited contracts
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL when selected content uses statuses
- terrain/weather/hazards/zones/reactions: BLOCKING if route conditions become tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL where battle Items participate
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED within audited contracts
- AI tactical policy: BLOCKING when actors must prioritize withdrawal, corridor pressure, territory or disengagement over KO
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING for faithful world -> battle -> world projection

Disposition: FULL RICH VERSION BLOCKED.

## Reduced encounter contract

Narrative retains:
- aid need;
- allocation history;
- shipment/custody;
- beneficiaries;
- transport purpose;
- noncombatants;
- later distribution and project consequences.

Before combat:
- secure noncombatants and semantic cargo in Narrative where appropriate;
- identify one immediate actor still preventing safe withdrawal;
- choose audited combatants/content;
- use stable geometry;
- omit unverified weather/hazards/zones/reactions;
- avoid forced-movement objectives unless selected interactions are separately contract-verified.

Allowed narrow handoffs:
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_PASSAGE_CLEAR`
- `IMMEDIATE_RELIEF_TEAM_CAN_WITHDRAW`

Battle output cannot determine:
- aid priority;
- beneficiary entitlement;
- ownership;
- debt/repayment;
- adequacy of relief;
- contributor reputation;
- liability;
- future obligation;
- Thin Delivery Season cause.

Disposition: REDUCIBLE USING AUDITED BASIC BATTLE CONTENT.

## AI tactical-policy caution

Legal-action infrastructure does not prove that an actor can understand a relief-withdrawal objective. A full version may require AI to retreat, stop pursuit, ignore cargo, pressure a corridor or preserve distance. Those remain tactical-policy requirements.

## Adapter/playback caution

Minecraft/Cobblemon presentation must not author shared-resource truth.

Required boundaries include:
- visible crate != available contribution;
- dropped Item entity != aid transfer;
- NPC proximity != volunteer commitment;
- Pokémon presence != verified work capability;
- block repair != project closure;
- entity unload != contribution withdrawal;
- battle animation != allocation decision.

## Narrative repository state for this pass

Pass 202 writes only to Narrative.

New files:
- `research/2026-09-02-mutual-aid-relief-shared-resource-scan-202.md`
- `design/mutual-aid-relief-shared-resource-continuity-layer.md`
- `proposals/2026-09-02-marea-mutual-aid-relief-seeds-202.md`
- `design/engine-readiness-snapshot-pass-202.md`

No AutoPTU-Java or AutoPTU write is authorized or performed.

## Implementation recommendation

Prototype `The Shared Cart Repair` first.

It requires:
- no battle;
- no new NPC;
- no new institution;
- no new currency rule;
- no welfare/insurance law;
- no mechanical crafting bonus;
- no new Pokémon species;
- no external geography.

It tests the new seam directly: multiple existing actors can contribute different dependencies to one persistent recovery task without turning contribution into ownership, reputation or debt.