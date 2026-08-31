# Engine readiness snapshot — Pass 168

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-31

## Read-only heads inspected

AutoPTU-Java main: `45f37bbec69881825aba7cbfd6df895de5943096`
Head message: `Compose forced movement prevention from status and temporary state (#309)`.

AutoPTU main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.
Head remains presentation-only: battle renderer coordinates are synchronized after viewport resize; commit explicitly states no battle rules or outcomes change.

Neither engine repository was modified by this pass.

## New Java evidence since Pass 167

Pass 167 had inspected PR #307, where selected defender Abilities could prevent PUSH. Current main has advanced through additional forced-movement work to PR #309.

PR #309 composes forced-movement prevention from status and temporary state, applies those state-backed prevention rules, freezes relevant Python branches, compares them against the Python oracle, adds coverage, and gates parity in CI. This is material evidence that the forced-movement runtime is gaining additional authoritative prevention sources beyond representative Ability cases.

This evidence is still local to specific forced-movement behavior. It does not establish complete coverage of all Push, Pull, Knockback, Intercept ordering, arbitrary forced movement, terrain/weather-generated displacement, Items, Trainer Features, escort/rescue, protected-object carrying, vehicles/platforms, crowd routing, generalized reaction windows, or tactical objective policy.

No permanent category is promoted on the basis of this representative progress.

## Permanent capability map

VERIFIED
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL
- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Pass 168 encounter dependency review

Claims Archive Recovery Perimeter full version: BLOCKED by complete movement where displacement/route control matters; full lifecycle; possible terrain/weather/hazards/zones/reactions; audited move-specific behavior, abilities, items, and Trainer Features; AI tactical policy; semantic adapter/playback. Reduced static-perimeter version is READY at narrative-contract level after individual content audit.

Damaged Workshop Assessment Perimeter full version: BLOCKED if unstable terrain, ongoing hazards, escort, environmental phases, generalized reactions, or objective-aware AI are present. Reduced static conflict is READY at narrative-contract level after individual content audit.

Mutual Aid Treasury Transfer Chokepoint full version: BLOCKED by protected-object carrying/escort semantics plus potentially complete movement, Intercept/displacement, lifecycle, reactions, AI tactical policy, and semantic playback. Reduced version keeps transfer objects/couriers outside BattleSpec and resolves immediate access only.

Relief or Compensation Distribution Access Incident full version: BLOCKED where crowd routing, queues, escort, hazards, reactions, or objective-aware AI are needed. Reduced version keeps civilians, supplies, funds, and queue state outside BattleSpec and resolves immediate access only.

## PTU/Caelo boundaries for this pass

Public PTU material confirms money and purchasable Items are concrete campaign resources. This pass found no authoritative evidence for a universal insurance, claim, premium, indemnity, property-liability, reimbursement, or risk-pool subsystem.

UNKNOWN pending project-source confirmation:
- any Caelo-specific coverage, compensation, guild-guarantee, disaster-aid, or mutual-fund rules;
- Skill Checks that mechanically decide claims or ownership;
- Features/perks that create reimbursement rights;
- battle damage rules for persistent buildings or privately owned overworld property;
- automatic replacement of destroyed/lost Items;
- liability rules for Trainer/Pokémon collateral damage;
- coverage of Pokémon medical/care costs, if any;
- any rule where battle victory establishes ownership, compensation, debt, or claim validity.

Narrative must not invent these outcomes.

## Adapter boundary

Minecraft block breakage, entity destruction/despawn, chest inventory state, dropped items, Cobblemon fainting, visual explosions, or playback omissions are not canonical loss/claim facts unless Ouros authority explicitly records the underlying world event. The adapter must present authoritative outcomes rather than create economic consequences.

## Promotion rule

A permanent capability category changes only when live tests/contracts demonstrate the family broadly enough to justify promotion. One new prevention source, one status branch, one Ability, one Move, or one runtime seam remains representative evidence only.