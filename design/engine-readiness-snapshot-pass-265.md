# Engine readiness snapshot — Pass 265

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU inspected read-only.

AutoPTU-Java head is `dff95c637d8b8cb4a444995c27febd9ff74685d0`, merge of PR #348. The change freezes parity for delayed-hit reentry through runtime composition and verifies the relevant move-special pre-damage, post-damage and end-action phases for that path. This is narrow evidence for that producing path. It does not establish complete move-specific behavior, complete lifecycle or a public AutoPTU→Ouros semantic-result API.

AutoPTU Python oracle remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest inspected change remains presentation-only and does not change battle rules/outcomes.

## Permanent capability audit

- targeting/footprints/range/LoS: VERIFIED within audited contracts.
- base movement legality: VERIFIED within audited contracts.
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
- core calculations: VERIFIED within audited contracts.
- action economy/initiative: VERIFIED within audited contracts.
- full turn/round lifecycle: PARTIAL.
- full stateful damage pipeline: PARTIAL.
- status lifecycle: PARTIAL.
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING.
- move-specific behavior: PARTIAL; delayed-hit reentry has additional narrow parity evidence at Java PR #348.
- abilities: PARTIAL.
- items: PARTIAL.
- Trainer Features/perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED within audited contracts.
- AI tactical policy: BLOCKING.
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

No category is promoted in Pass 265.

## Pass 265 resource-pulse implications

The reduced resource-pulse loop is ecological world-state plus projection. It requires Ouros population/source authority, event persistence, the Pass 261 semantic clock/horizon contract and adapter presentation. It does not require AutoPTU and must not route missing tactical behavior into Minecraft/Cobblemon.

The full physical-convergence version requires targeting/LoS where spatial perception/targeting matters; base movement for ordinary approach; action economy/initiative and full lifecycle for tactical sequencing; AI legal-action infrastructure for legal candidate generation; AI tactical policy for autonomous choice to approach, ignore, retreat or contest; and adapter/playback for world presentation.

Interception, push, pull, knockback or forced movement adds complete movement. A mechanically active resource patch adds terrain/weather/hazards/zones/reactions. Specific Moves, Abilities, Items or Trainer Features add their exact families. Damage and durable aftermath add the full stateful damage pipeline; persistent statuses add status lifecycle.

Java PR #348 does not change this gate. Its delayed-hit evidence matters only if a later resource encounter actually invokes that delayed-hit path and the exact producing contract is admitted.

## PTU/Caelo/Kairos boundary

PTU remains the selected mechanical baseline. Survival/Perception can support field observation only where adopted rules permit; they do not reveal private source identity or exact abundance by implication. Kairos remains a living-world/reference source unless explicitly adopted. No local Caelo source pack was found in the current project evidence used for this pass, so no Caelo-specific rule is inferred.

## Unresolved blockers and design questions

- Define authoritative sources for resource-event onset, phase transitions and closure.
- Select real Marea/Sendero resource classes before promoting any example to canon.
- Define species/context response policies without a universal attraction multiplier.
- Decide how projection can present temporary concentration without creating extra sources or misleading abundance UI.
- Define cross-species participation and competition without assuming identical response.
- Verify the production Ouros-world clock primitive and adapter persistence path from Pass 261.
- AI tactical policy remains blocking for live autonomous convergence/contest.
- Stable AutoPTU semantic-result export and subject-binding transport remain required for any tactical aftermath, independent of this ecological event contract.
