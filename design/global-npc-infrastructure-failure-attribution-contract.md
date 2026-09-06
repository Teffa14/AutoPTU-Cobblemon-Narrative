# Global NPC infrastructure failure attribution contract — Pass 303

Status: EXECUTABLE DESIGN CONTRACT
Date: 2026-09-06

## Purpose

Pass 302 proves whether a communication opportunity existed, remained pending, failed, or completed. Pass 303 adds a separate causal investigation layer for the infrastructure behind a proven failure.

A failed channel is evidence that communication failed. It does not identify accident, tampering, sabotage or a responsible actor.

## Executable boundary

Implementation: `tools/global_npc_infrastructure_failure_attribution.py`
Regression: `tests/test_global_npc_infrastructure_failure_attribution.py`

`incident_from_communication_failure()` accepts only communication access already classified as `CHANNEL_UNAVAILABLE` or `DELIVERY_FAILED`. It produces an immutable incident reference and preserves the access provenance. It does not edit the dispatch or delivery record.

`assess_infrastructure_failure()` consumes only causal evidence present in the investigating NPC's `KnowledgeLedger`. Claims below the confidence threshold or claims from the future fail closed. Multiple claims descended from one provenance root count once.

## Causal ladder

`CAUSE_UNRESOLVED` means the failure is known but no qualifying cause is established.

`ACCIDENTAL_CAUSE_SUPPORTED` means independent evidence supports wear, design, environment, ordinary breakage or another non-malicious causal family.

`TAMPERING_CORROBORATED` means physical or equivalent evidence supports deliberate alteration. It does not identify the actor.

`SABOTEUR_LINKED` requires tampering plus an independent actor link. Access/opportunity alone cannot create this status.

`SABOTAGE_INTENT_ATTRIBUTED` requires tampering, an actor link and independent intent evidence attributable to the same actor. The runtime currently accepts actor-attributable intent evidence only when the underlying claim source is that actor.

`CAUSE_CONTESTED` preserves independent accidental-cause and tampering evidence without choosing a winner.

## Invariants

Failure history remains immutable when a later explanation appears.

Physical tampering never identifies a person by itself.

Presence, access, faction membership, rivalry or benefit from an outage never proves sabotage.

Intent evidence cannot skip the physical-cause and actor-link requirements.

Echoes sharing one provenance root cannot bootstrap multiple evidentiary stages.

Different NPCs can reach different findings because each assessment uses only that NPC's ledger.

A later stronger finding is a new assessment. It must not rewrite what an earlier investigator could know at the earlier semantic time.

## Persistence

`InfrastructureAttributionRegistry` has a versioned snapshot schema and collision guard. Registry persistence is local to this subsystem in Pass 303. It has not yet been added to the Pass 297 global world checkpoint; that remains an explicit durability gap.

## Narrative use

This contract supports failed-relay inquiries, damaged gates, disabled lifts, broken irrigation controls, weather-station outages, clinic repeaters, transport signals, observatory equipment and other infrastructure whose failure can affect NPC plans.

A scenario may stop at an accident, remain unresolved, produce conflicting explanations, prove tampering without identifying a culprit, identify a likely actor without proving intent, or eventually reach attributable sabotage. Authors should not force every infrastructure failure into the sabotage branch.

## AutoPTU boundary

The attribution layer has no tactical dependency. It reasons over world evidence.

If evidence must be acquired through structured combat, hazardous movement, weather, delayed effects, statuses, Moves, Abilities, Items or Trainer Features, those acquisition scenes inherit the exact engine families they use. The world layer must never reproduce missing PTU mechanics merely to make the investigation playable.
