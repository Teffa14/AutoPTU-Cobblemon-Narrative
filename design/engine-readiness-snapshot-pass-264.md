# Engine readiness snapshot — Pass 264

Evidence date: 2026-09-04. AutoPTU-Java and AutoPTU inspected read-only.

AutoPTU-Java head remains `136c8d9a7d124849954748c780b12a0e1faf28e0`, merge of PR #347, `Route AoE move specials through runtime composition`.

Current Java evidence still strengthens runtime composition around AoE move-special handling but does not expose a stable public AutoPTU→Ouros semantic-result export surface. No live evidence found in this pass justifies promoting full lifecycle, full stateful damage, status lifecycle, move-specific behavior or adapter transport.

AutoPTU Python oracle remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit is presentation-only and explicitly changes no battle rules/outcomes.

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
- move-specific behavior: PARTIAL.
- abilities: PARTIAL.
- items: PARTIAL.
- Trainer Features/perks: PARTIAL.
- AI legal-action infrastructure: VERIFIED within audited contracts.
- AI tactical policy: BLOCKING.
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING end-to-end.

No category is promoted in Pass 264.

## Pass 264 reconciliation implications

Quarantine lifecycle is integration bookkeeping and does not increase battle-engine readiness.

A semantic result already quarantined for an unverified path cannot become durable PTU/ecology truth because time passed, transport retried, a player observed matching symptoms, or a broad capability family label improved.

Production release requires an exact admission record for the historical producing tuple: result type, producer revision, rules profile, producing path, required capabilities and exact contract/tests. A new engine revision does not automatically certify results emitted by an older revision.

The Pass 264 Injury reconciliation is fixture-only. It proves immutable-envelope review, evidence-generation gating, atomic mapping and idempotence. It does not claim that AutoPTU-Java currently exports `PERSISTENT_INJURY` or that the current damage/lifecycle path is production admissible.

Persistent status remains quarantined because status lifecycle remains PARTIAL.

Player/NPC observation belongs to the knowledge pipeline. Apparent impairment can be recorded without importing HP, Injury or status state.

## Encounter versions

Reduced aftermath-review loop: use persistent ecology, observation history, disturbance/site-use systems and Minecraft presentation. The player may revisit an individual and record apparent consequences while durable PTU aftermath remains unresolved. This version avoids reproducing missing battle rules in the adapter.

Full version: AutoPTU must export typed semantic results through a verified transport, Pass 263 must resolve the stable subject, and Pass 264 must find an exact admission record. Injury requires full turn/round lifecycle + full stateful damage for the exact historical path. Status adds status lifecycle. Forced movement adds complete movement. Terrain/weather/hazard/zone/reaction, Move, Ability, Item and Trainer Feature participation add their named families. Autonomous tactical causation adds AI tactical policy.

## PTU/Caelo/Kairos boundary

PTU remains the selected mechanical baseline under project policy. Kairos remains a living-world/reference source unless explicitly adopted. The current Narrative tree still does not provide a local Caelo source pack; no Caelo-specific mechanical rule is inferred.

## Unresolved blockers

- Stable public AutoPTU-Java semantic-result export/API and producer path identifiers.
- Exact Java evidence records that can instantiate `SEMANTIC_RESULT_ADMISSION_V1`.
- Production implementation of the private battle-subject binding ledger.
- Real AutoPTU↔Ouros/Craftics transport/authentication boundary.
- Persistent store/index for quarantine receipts and review generations.
- Archive policy for results whose historical producer revision can never be certified.
- Player-facing aftermath language that exposes uncertainty without leaking engine internals.
