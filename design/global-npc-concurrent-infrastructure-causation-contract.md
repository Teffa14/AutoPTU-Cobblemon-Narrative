# Global NPC concurrent infrastructure causation contract

Status: ACTIVE DESIGN CONTRACT
Pass: 305
Date: 2026-09-06

## Purpose

Allow persistent Ouros investigators to distinguish competing explanations from genuinely concurrent causes while preserving non-omniscient evidence, provenance and responsibility boundaries.

## Core invariant

`MULTIPLE_EVIDENCE_FAMILIES != CONCURRENT_CAUSATION`

Independent evidence for an accidental condition and independent evidence for tampering remain `CONTESTED` until a third, provenance-independent claim supports that both contributed to the same incident.

## Executable surface

Implementation:
- `tools/global_npc_infrastructure_failure_attribution.py`

Regression:
- `tests/test_global_npc_infrastructure_failure_attribution.py`

Existing durability boundary:
- `tools/global_npc_world_checkpoint.py`

## Causal composition

`InfrastructureCauseStructure` is an epistemic classification owned by one investigator finding:

- `UNRESOLVED`: current evidence does not support an accident or tampering cause;
- `ACCIDENT_ONLY`: supported accidental/material cause with no supported tampering trace;
- `TAMPERING_ONLY`: supported tampering trace with no supported accidental contributor;
- `CONTESTED`: both evidence families exist, but their relationship is unresolved or competing;
- `CONCURRENT`: both evidence families exist and an independent `CONTRIBUTION_LINK` supports a combined explanation.

The classification describes what the discoverer can support at that semantic time. It is not omniscient world truth.

## Contribution-link evidence

`InfrastructureEvidenceKind.CONTRIBUTION_LINK` represents evidence that connects already-supported accidental and tampering cause families into one combined causal explanation.

Admission rules:
- the claim must exist in the discoverer's `KnowledgeLedger`;
- it must meet the configured confidence threshold;
- it cannot come from the future;
- its provenance root must be independent from the roots already counted for the accident and tampering evidence;
- it cannot name a responsible actor;
- it is invalid unless independent accidental and tampering evidence are also present.

A single report repeated through multiple relays still counts once by provenance root.

## Responsibility remains separate

Concurrent causation does not erase actor attribution.

A finding can simultaneously state:
- `cause_structure = CONCURRENT`, and
- `status = SABOTEUR_LINKED` or `SABOTAGE_INTENT_ATTRIBUTED`.

This permits an incident such as pre-existing material fatigue plus a deliberate cut. The material condition can remain causally relevant even after deliberate intervention and intent are established.

Conversely, proving concurrent causes does not itself identify a saboteur.

## Historical compatibility

The infrastructure attribution snapshot schema remains V1 for this additive field. New snapshots include `cause_structure` per finding. Restore accepts older rows without that field and derives the compatible structure from their existing status.

This prevents Pass 305 from invalidating the V3 world checkpoints created by Pass 304.

## Investigation progression example

At semantic minute 120 an engineer's report supports corrosion.

At minute 121 a direct scene inspection supports deliberate cutting.

At this point the finding is `CAUSE_CONTESTED / CONTESTED`.

At minute 140 an independent load reconstruction supports that corrosion lowered the remaining margin and the cut then caused the failure under ordinary operating load.

A new finding may become `CONTRIBUTING_CAUSES_CORROBORATED / CONCURRENT`.

If a later access record and attributable admission connect an actor to the intervention, responsibility can advance without deleting the concurrent material contributor.

## Narrative consequences

This contract supports:
- investigations where an accused maintenance crew was negligent but did not perform sabotage;
- sabotage that exploits an existing defect;
- natural damage that amplifies a deliberate act;
- repair plans that must address both the malicious intervention and the neglected condition;
- institutional disputes over responsibility where different actors possess different subsets of evidence;
- later exculpation on one allegation without erasing another failure of duty.

## Tactical boundary

The causal investigation itself requires no AutoPTU capability family.

A mechanically rich incident site may separately require:
- targeting/footprints/range/LoS for tactical spatial actions;
- base movement legality for ordinary traversal;
- complete movement for push/pull/knockback/interception/forced movement;
- core calculations for deterministic PTU arithmetic;
- action economy/initiative for structured turns;
- full turn/round lifecycle for timed collapses, surges or phase transitions;
- full stateful damage pipeline for authoritative environmental damage;
- status lifecycle for persistent conditions;
- terrain/weather/hazards/zones/reactions for active environmental threats;
- move-specific behavior for mechanically active Moves;
- abilities for Ability-driven interactions;
- items for mechanically active Items;
- Trainer Features/perks for interrupts or Feature effects;
- AI legal-action infrastructure for legal candidate generation;
- AI tactical policy for autonomous tactical selection;
- Minecraft/Cobblemon/Craftics adapter/playback support for authoritative visible execution.

No representative mechanic promotes an entire capability category.

## Canon boundary

This is a reusable world-simulation contract. It canonizes no relay, accident, faction, NPC, regional condition or culprit.
