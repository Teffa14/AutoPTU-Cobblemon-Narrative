# AutoPTU World Observation Selective Replanning Contract — Pass 421

Status: ACTIVE IMPLEMENTATION CONTRACT

## Purpose

Pass 420 delivers one committed world observation to one explicit recipient through the ordinary private information queue. Pass 421 connects that successful delivery to the existing global world-event coordinator so the named recipient can reconsider their agenda.

The integration remains downstream of admitted AutoPTU results. It consumes only the scheduled observation-delivery identity, the communication outcome and the existing world-agent planner.

## Authority boundary

The bridge never opens the AutoPTU result payload. It does not inspect HP, Injuries, Status, positions, initiative, weather, terrain, hazards, Moves, Abilities, Items, Trainer Features or battle transcript state.

Before processing, it verifies that the scheduled delivery envelope still matches queue provenance and that the sender-side source claim preserves the committed observation transaction as its provenance root.

## Wake rule

Only a terminal `DELIVERED` result may create a `KNOWLEDGE_DELIVERED` replan trigger for the explicit receiver.

`QUEUED`, `WAITING_LOCAL_ACK` and `FAILED_CHANNEL_UNAVAILABLE` outcomes do not wake the actor.

A local-projection channel may wake the actor only after an accepted acknowledgement produces the actual delivery. A rejected acknowledgement remains a non-delivery.

## Recipient scope

The delivery envelope names exactly one receiver. Replanning remains scoped to that actor.

Shared faction membership, workplace membership, location or institutional role does not create another replan trigger. Another actor changes plan only after receiving a separate trigger through a legitimate world event.

## Provenance

Successful delivery must expose the same provenance root as the committed observation transaction ID. The world agent records that provenance through the existing information-delivery path before agenda selection.

The bridge rejects a mismatched source claim before delivery. It also rejects a delivered result whose provenance root no longer matches the scheduled observation identity.

## Agenda semantics

Delivery creates an opportunity to reconsider. It does not prescribe the resulting action.

The existing agenda resolver still evaluates goals, needs, commitments, situational intents, permissions, knowledge, continuity and structured-mechanics requirements. A recipient may change route, delay, request help, continue an existing commitment or hand structured work to AutoPTU depending on their own state.

## Budget and deferred work

A due message can remain queued when the coordinator delivery budget is exhausted. Pass 421 reports that state without manufacturing a wake.

This keeps throughput limits distinct from narrative knowledge. A due but unprocessed envelope has not yet become recipient knowledge.

## Local projection acknowledgement

For channels requiring local projection, the initial due processing yields `WAITING_LOCAL_ACK`. No replan occurs at that point.

Accepted acknowledgement performs the delivery, materializes the information in the world agent and schedules the ordinary knowledge-delivered replan. Rejected acknowledgement records failure and leaves the agent unchanged.

## Replay boundary

The underlying information queue and world-event coordinator retain their existing event and trigger identities. Pass 421 adds no second delivery path and no alternate knowledge ledger.

The scheduled observation envelope remains the provenance anchor for integration. Any mismatch fails closed.

## Capability posture

No tactical capability family is promoted by this pass.

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited paths.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: VERIFIED only for audited ordinary scopes.
AI tactical policy: BLOCKING for specialized warning-aware rescue, escort, extraction and objective policies unless explicitly implemented.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives, specialized non-KO completion and in-flight battle recovery.

## Next boundary

A later pass can persist the causal link from the replanning decision into a concrete world action or revised obligation. That transition should preserve the information provenance that caused the replan and should not treat a selected intent as completed work.

Requests for another NPC's help should travel through an explicit communication or obligation-assignment path rather than silently editing that second NPC's agenda.
