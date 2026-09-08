# Global NPC resource admission checkpoint contract — Pass 363

Status: IMPLEMENTED GLOBAL CONTRACT
Canon authority: NONE
Date: 2026-09-08

Pass 363 adds a durable history boundary for Pass 347 resource-window admission assessments.

The existing Pass 347 function remains a pure read model. A new `ResourceRescheduleAdmissionRecord` can freeze a resolved CLEAR or CONFLICT assessment at one semantic tick. `OUROS_NPC_RESOURCE_CHECKPOINT_V6` serializes that history together with Passes 339/342/343/344/345/346 resource state.

The record preserves the proposal, stable resource ID, assessment state, assessment tick, conflicting reservation IDs and same-purpose reservation IDs. It does not select priority, cancel a reservation, accept a reschedule, create a successor authorization, transfer custody, change relationships or invoke AutoPTU.

Historical admission differs from recomputation. A reservation may later be released or cancelled. That later state must not erase the fact that it was part of the conflict set when the assessment was captured. Restore therefore validates structural provenance against the preserved reservation history instead of requiring the reservation to remain ACTIVE now.

Restore fails closed when an assessment references a missing proposal or authorization, changes resource identity, predates its proposal, claims a resolved result for an unbounded window, classifies one reservation both as conflict and same-purpose evidence, references a missing reservation, uses a non-overlapping reservation, reverses same-purpose classification, contains duplicate record IDs, or originates after the restored semantic time.

V1–V5 remain readable and restore an explicit empty admission ledger. Older saves do not infer conflict history from a later allocation decision, cancelled reservation, current availability, NPC memory or dialogue.

This pass intentionally does not persist Pass 348 allocation resolutions. The next durability boundary can consume this historical conflict evidence without merging admission and institutional choice.

Encounter dependency boundary: the reduced narrative use requires no tactical engine. A mechanically rich continuation keeps the permanent capability classification conservative: targeting/footprints/range/LoS VERIFIED within audited ordinary contracts; base movement legality VERIFIED within audited ordinary contracts; complete movement PARTIAL; core calculations VERIFIED within audited ordinary contracts; action economy/initiative VERIFIED for audited primitives with objective-specific actions individually gated; full turn/round lifecycle PARTIAL; full stateful damage pipeline PARTIAL; status lifecycle PARTIAL; terrain/weather/hazards/zones/reactions MIXED/PARTIAL/BLOCKING by exact family; move-specific behavior PARTIAL; abilities PARTIAL; items PARTIAL; Trainer Features/perks PARTIAL; AI legal-action infrastructure VERIFIED for the ordinary audited scope; AI tactical policy BLOCKING for resource-first, escort, reroute and disengage-after-objective policies; Minecraft/Cobblemon/Craftics adapter/playback PARTIAL/BLOCKING end-to-end.

No representative mechanic promotes a whole capability category.
