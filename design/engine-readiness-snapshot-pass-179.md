# Engine Readiness Snapshot — Pass 179

Status: READ-ONLY EVIDENCE SNAPSHOT
Date: 2026-09-01
Purpose: classify implementation dependencies for institutional-continuity encounter concepts without promoting capability families from representative mechanics.

## Repositories inspected

### AutoPTU-Java

Head inspected: `8fd11090b31d413072808662c01fc2e2316420ff`

Recent relevant sequence:

- `cc5522b72f63ad283153251db5fef4502b860db9` — freezes combatant/footprint distance geometry for Shadow Tag.
- `8e5204b19f4aa83d96c573635be52c6e0e9092a3` — binds Shadow Tag through generic forced-movement candidate-step constraints and compares outcomes with oracle evidence.
- `7cbc5aafb50a5221d4493518297f24ff3e4a960a` — freezes composite forced-movement prevention guard.
- `8fd11090b31d413072808662c01fc2e2316420ff` — composes content-backed forced-movement prevention into post-hit displacement and adds tests/gates.

Interpretation:

This is meaningful evidence that forced displacement has increasingly reusable prevention and candidate-step infrastructure. It does not prove complete movement as a family. Push, Pull, Knockback, Interception, collisions, partial stops, arbitrary displacement interactions and all relevant Move/Ability/Feature combinations must still be individually evidenced before a concept can depend on them broadly.

No AutoPTU-Java commit newer than the pass-178 evidence changes the capability classification.

### AutoPTU

Head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Recent commits are Career/presentation and roster-recovery work rather than new tactical parity evidence.

The repository contains extracted PTU 1.05 source text and validated class catalogues. For this pass, `TRAINER_CLASS_CATALOG.md` is relevant because it confirms that Mentor is a real mechanical Trainer Class with explicit prerequisites and unlockables. That source is used only to prevent a terminology collision: social mentorship or institutional supervision must not silently grant Mentor-class mechanics.

No institutional succession, workplace delegation or civic promotion rule is inferred from PTU mechanics.

### AutoPTU-Cobblemon-RPG

Recent relevant head observed: `40ef2d4af9100d5ce5a1dbc8308a350482cffff2`

Useful evidence for non-tactical narrative implementation includes:

- normal-world provision of a persistent Cedar Ranger actor;
- graphical capture of an authoritative in-world RPG scene;
- server-owned Cedar field-notes quest object;
- objective progress gated to the exact persistent physical object;
- restart proof for that object.

Interpretation:

These commits materially improve confidence in physical documents, NPC presentation and server-owned quest/world interactions. They do not establish complete battle playback parity across Minecraft/Cobblemon/Craftics.

The permanent `Minecraft/Cobblemon/Craftics adapter/playback support` family therefore remains BLOCKING for concepts that require the complete visible tactical battle path, while narrower non-tactical object/NPC/dialogue surfaces can be treated as locally evidenced.

## Permanent capability classification

The classifications below apply to the family as a whole, not one representative mechanic.

| Capability family | Pass 179 status | Evidence interpretation |
| --- | --- | --- |
| targeting/footprints/range/LoS | VERIFIED for covered contracts | Existing geometry/parity contracts support the audited surfaces. New shapes or special targeting rules still require exact audit. |
| base movement legality | VERIFIED for covered contracts | Ordinary legal movement has covered infrastructure. This does not include the complete forced-movement family. |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | Candidate-step constraints and content-backed forced-movement prevention are real progress. Full family remains unproven. |
| core calculations | VERIFIED for covered contracts | Existing calculation/oracle evidence remains sufficient for audited ordinary paths. Exact special effects still require content parity. |
| action economy/initiative | VERIFIED for covered contracts | Existing infrastructure is usable for audited basic encounters. |
| full turn/round lifecycle | PARTIAL | Representative turn behavior does not prove every phase, interrupt, delayed effect and round-bound transition. |
| full stateful damage pipeline | PARTIAL | Core damage paths exist, but the complete family and all stateful interactions are not globally verified. |
| status lifecycle | PARTIAL | Individual statuses or status paths do not prove application, duration, cures, immunities, stacking and all transition rules as a family. |
| terrain/weather/hazards/zones/reactions | BLOCKING | No evidence supports treating this combined family as complete. Concepts requiring these systems must remain gated or reduced. |
| move-specific behavior | PARTIAL | Every selected Move requires exact behavior/parity evidence. Representative Moves do not promote the family. |
| abilities | PARTIAL | Shadow Tag and other individual Ability work is useful evidence only for those audited contracts. |
| items | PARTIAL | Exact held/consumed Item behavior must be audited per encounter. |
| Trainer Features/perks | PARTIAL | PTU content exists and some runtime mappings exist, but exact Features must be checked. Mentor-class presence in the source does not imply runtime completeness. |
| AI legal-action infrastructure | VERIFIED for covered contracts | Legal candidate generation/infrastructure is available for audited paths. |
| AI tactical policy | BLOCKING | Legal actions are not equivalent to tactically correct autonomous choice. |
| Minecraft/Cobblemon/Craftics adapter/playback support | BLOCKING as full family | Non-tactical RPG presentation has strong live evidence, but complete tactical playback cannot be inferred from those slices. |

## Encounter audit — Jace Runs One Yard Session

### Intended full version

Narrative premise:

Sela gives Jace a bounded delegation to run one Battle Yard session. Institutional responsibilities are server-owned world state. One normal Trainer battle may occur during the session.

Required families for an unrestricted version:

- targeting/footprints/range/LoS — VERIFIED for covered contracts;
- base movement legality — VERIFIED for covered contracts;
- complete movement — PARTIAL if any selected content uses forced movement or interception;
- core calculations — VERIFIED for covered contracts;
- action economy/initiative — VERIFIED for covered contracts;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when selected content uses statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING when selected battlefield/content requires it;
- move-specific behavior — PARTIAL and exact-content dependent;
- abilities — PARTIAL and exact-content dependent;
- items — PARTIAL and exact-content dependent;
- Trainer Features/perks — PARTIAL and exact-content dependent;
- AI legal-action infrastructure — VERIFIED for covered contracts;
- AI tactical policy — BLOCKING for intended autonomous tactical quality;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING for unrestricted full visible battle playback.

Overall intended-version status: BLOCKED.

### Reduced version

Keep the delegation, check-in, fixture inspection, recordkeeping and institutional review outside BattleSpec.

Select a specifically parity-audited basic matchup whose Moves, Abilities and participant state avoid dependencies on:

- unsupported forced movement;
- terrain/weather/hazard/zone/reaction systems;
- unsupported complex statuses;
- unaudited Items;
- unaudited Trainer Feature interrupts;
- tactical choices that need missing AI policy to preserve encounter intent.

The battle may emit only authoritative battle facts and a narrow world event such as `YARD_SESSION_MATCH_COMPLETE`.

Institutional code can then evaluate whether Jace completed his assigned workflow. Battle outcome must not directly emit promotion, succession, retirement or expanded mandate.

Reduced-version status: CANDIDATE, pending exact roster/content audit and available presentation path.

## Non-battle institutional candidates

`Pia's First Independent Circulation Run` and `Ema Signs the Preparation Line` do not need BattleSpec.

Their likely implementation dependencies are primarily server-owned narrative/runtime surfaces:

- persistent actor identity;
- schedules/location presence;
- physical quest/document objects;
- custody/provenance state;
- dialogue/actions;
- quest/objective state;
- communication/knowledge packets;
- restart persistence.

Recent RPG evidence directly supports several of these narrow surfaces. Their implementation should not be delayed by missing tactical families.

## PTU / Caelo caution

AutoPTU's extracted PTU sources confirm the mechanical Mentor class. No inspected PTU rule grants civic/workplace authority from that class.

A repository-wide indexed search for `Caelo` across Narrative, AutoPTU-Java and AutoPTU returned no result in this pass. This absence is not treated as proof that no Caelo source exists. Any Caelo-specific succession custom, office hierarchy, certification practice or institutional title remains unresolved until a concrete source is located.

## No category promotions in pass 179

Pass 179 records no permanent capability-family promotion.

The key implementation decision is architectural instead: institutional-continuity stories can progress through non-tactical server state now, while any embedded battle is independently capability-gated and can use a reduced audited version without changing the narrative premise.
