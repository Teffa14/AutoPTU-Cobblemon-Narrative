# AutoPTU semantic-result capability admission matrix

Status: PROPOSED gate layered after Pass 262 envelope validation and Pass 263 subject binding.
Evidence date: 2026-09-04.

This matrix does not promote engine families. Each semantic result must name the exact capabilities used by its producing path and point to concrete Java contracts/tests before production admission.

| Result family | Minimum capability evidence | Current disposition | Notes |
| --- | --- | --- | --- |
| `BATTLE_HANDOFF_CORRELATION_RECEIPT` | Minecraft/Cobblemon/Craftics adapter/playback transport + valid subject binding | ADMIT_AS_INTEGRATION_ONLY when transport/binding contract is satisfied | May acknowledge correlation/completion. Cannot mutate HP, status, population or other PTU truth. |
| targeting observation/result | targeting/footprints/range/LoS | NARROW_ADMISSION_POSSIBLE | Only for exact audited targeting contract. Does not authorize damage or move semantics. |
| voluntary base relocation | base movement legality | NARROW_ADMISSION_POSSIBLE | Only plain verified base movement. No push/pull/interception/forced movement inference. |
| forced/disputed relocation | complete movement | QUARANTINE by default | Family remains PARTIAL. Exact verified producer may later be whitelisted without promoting family. |
| deterministic calculation receipt | core calculations | NARROW_ADMISSION_POSSIBLE | Calculation provenance only; durable state still depends on the stateful family consuming it. |
| initiative/action-spend receipt | action economy/initiative | NARROW_ADMISSION_POSSIBLE | Does not prove full turn/round closure. |
| turn/round/battle lifecycle transition | full turn/round lifecycle | QUARANTINE by default | Family PARTIAL. |
| HP delta / Injury / persistent damage aftermath | full stateful damage pipeline + full lifecycle for exact path, plus every participating move/reaction/ability/item/etc. family | QUARANTINE | Damage pipeline remains PARTIAL. An Injury-shaped fixture is not production evidence. |
| persistent status add/remove/expiry | status lifecycle + producing path capabilities | QUARANTINE | Status lifecycle remains PARTIAL. |
| terrain/weather/hazard/zone/reaction durable effect | terrain/weather/hazards/zones/reactions + lifecycle + any producing family | QUARANTINE | Current status MIXED/PARTIAL/BLOCKING. |
| move-specific durable semantic | move-specific behavior plus all subordinate capabilities | QUARANTINE | Runtime composition seams do not prove complete semantics. |
| Ability-derived persistent result | abilities plus all subordinate capabilities | QUARANTINE | PARTIAL. |
| Item-derived persistent result | items plus all subordinate capabilities | QUARANTINE | PARTIAL. |
| Trainer Feature/perk-derived persistent result | Trainer Features/perks plus all subordinate capabilities | QUARANTINE | PARTIAL. |
| legal-action provenance | AI legal-action infrastructure | NARROW_ADMISSION_POSSIBLE | Can prove an action was legal under an audited path; cannot claim tactical intent/quality. |
| autonomous tactical-intent/policy result | AI tactical policy | BLOCK | Family remains BLOCKING. |
| visible playback/correlation | Minecraft/Cobblemon/Craftics adapter/playback | PARTIAL/BLOCKING | Presentation cannot author PTU/ecology truth. |

## Cross-cutting rule

A VERIFIED family is necessary evidence, not blanket permission. Production admission is `(result_type, producer_revision, rules_profile, producing_path, required_capabilities, exact_contract_tests)`.

Any result whose provenance lists a PARTIAL/BLOCKING family that materially affected the semantic result remains quarantined unless a narrower audited path has an explicit admission record.

## Admission record

A future `SEMANTIC_RESULT_ADMISSION_V1` should contain:

- `result_type`
- `producer_revision`
- `rules_profile_id`
- `path_id`
- `required_capabilities[]`
- `evidence_contracts[]`
- `evidence_tests[]`
- `admission_state`: `ADMITTED`, `FIXTURE_ONLY`, `QUARANTINE`, `BLOCKED`
- `reviewed_at`

No admission may be inferred from a representative mechanic elsewhere in the family.
