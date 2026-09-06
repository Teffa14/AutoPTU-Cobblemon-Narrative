# Global NPC evidence custody contract — Pass 306

Status: DESIGN / EXECUTABLE FOUNDATION
Date: 2026-09-06

## Purpose

Ouros investigations can now distinguish what an NPC believes about the handling history of a physical evidence item from what the item substantively proves.

A documentation gap is not proof that an artifact was altered. A conflicting record is not proof of sabotage. A complete custody history does not prove that an interpretation of the artifact is correct.

## Runtime

`tools/global_npc_evidence_custody.py` owns the reusable world-simulation seam.

`PhysicalEvidenceArtifact` gives an evidence item durable identity, a subject reference, semantic creation time and provenance reference.

`CustodyRecord` records one handling event with an explicit holder, semantic time, action, documentation claim and predecessor. Supported handling actions are collection, transfer, storage, examination and release.

The record itself does not become knowledge automatically. An investigator can use a record only when the corresponding documentation claim exists in that investigator's `KnowledgeLedger` and passes the configured confidence/time gates.

`CustodyIntegrityStatus` separates five meanings:

- `UNASSESSED`: the investigator lacks usable custody material;
- `CONTINUITY_SUPPORTED`: the known records form one time-consistent chain from collection onward;
- `DOCUMENTATION_GAP`: a known record depends on a handoff the investigator cannot currently document;
- `RECORD_CONFLICT`: known records cannot all describe one linear custody history;
- `COMPROMISE_CORROBORATED`: independent provenance-backed evidence supports alteration/compromise while in custody.

## Epistemic boundaries

`DOCUMENTATION_GAP != COMPROMISE_CORROBORATED`

`RECORD_CONFLICT != SABOTAGE_INTENT`

`CONTINUITY_SUPPORTED != SUBSTANTIVE_TRUTH`

Custody is about handling integrity. The existing infrastructure-attribution layer remains responsible for reasoning about accident, tampering, concurrent causes, actor links and intent.

Repeated reports with the same provenance root cannot manufacture independent support. Compromise evidence sharing a root with a custody record is ignored as an independent corroboration.

The runtime is investigator-relative. Different NPCs can hold different documentation and therefore reach different custody assessments without either being overwritten by global omniscience.

## Persistence

`EvidenceCustodyRegistry` has a versioned V1 snapshot containing custody records and assessments. Pass 306 does not yet add the registry to the global atomic world checkpoint. That integration remains a follow-up requirement before custody findings are considered globally crash-durable.

## PTU / Caelo authority boundary

Pass 306 adds no PTU Skill check, Trainer Feature, Move, Ability, Item or Pokémon capability rule.

Authored scenes may say that a record, sample, damaged component, seal or transfer receipt exists. Any mechanical method used to discover, inspect, authenticate, preserve or alter such evidence must be validated against the PTU/Caelo sources available to the project before canonization.

## Battle capability boundary

The custody runtime itself requires no AutoPTU tactical category.

A mechanically active recovery scene may separately depend on targeting/footprints/range/LoS, movement, lifecycle, damage, statuses, terrain/weather/hazards/zones/reactions, specific Moves/Abilities/Items/Trainer Features, AI tactical policy and adapter playback according to the mechanics actually authored.
