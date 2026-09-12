# The Offer Is Still on the Wire — Pass 446

Status: PROPOSED / NON-CANON
Canon effect: NONE
Location assignment: UNRESOLVED
Named NPC assignment: UNRESOLVED
Institution assignment: UNRESOLVED
Pokémon population assignment: UNRESOLVED

Premise

A specialist has permission to reopen an old assistance agreement and has authored concrete replacement terms. The requester has not received those terms yet. The message now has to cross the same imperfect communication world as every other private report.

Narrative value

The proposal can become stale while it travels. A route may reopen, weather may worsen, another worker may become available, the specialist may acquire a new obligation, local Pokémon may alter access conditions, or the original problem may disappear. This creates believable tension without freezing the world around a quest flag.

Reduced implementation version

The responder authors the offer and Pass 446 schedules an ordinary information envelope. Until terminal delivery, the requester has no new claim and cannot make a valid decision about the replacement terms. Failed or acknowledgement-waiting transport leaves the requester uninformed.

This version needs semantic time, private knowledge, the existing information queue and the Pass 445 proposal ledger. It does not require AutoPTU.

Possible local outcomes before receipt

The site reopens and the new proposed time becomes unnecessary. The site remains closed and the proposed alternative becomes more valuable. A second obligation consumes part of the specialist's availability. New evidence narrows the requested scope. The requester independently finds another solution. None of these facts edits the message already in transit.

Mechanically rich version

If the revised terms are later accepted and current conditions justify structured resolution, the same narrative premise can lead to a survey, escort, protection task, retrieval, containment or extraction. Build that encounter from live evidence at execution time rather than from the conditions that existed when the offer was sent.

Capability dependencies for the rich version

Targeting/footprints/range/LoS: required for spatial targeting; VERIFIED only in audited scopes.
Base movement legality: required for tactical traversal; VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: required for displacement or interception; PARTIAL.
Core calculations: required for structured combat calculations; VERIFIED only in audited scopes.
Action economy/initiative: required for turn-ordered resolution; PARTIAL.
Full turn/round lifecycle: required for duration and phase logic; PARTIAL.
Full stateful damage pipeline: required for persistent structured damage consequences; PARTIAL.
Status lifecycle: required for ongoing conditions; PARTIAL.
Terrain/weather/hazards/zones/reactions: required for dangerous access, weather, zones or reactive environmental behavior; MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: specialized INSPECT, ESCORT, PROTECT, RETRIEVE, CARRY, BRACE, CONTAIN or EXTRACT verbs require explicit admission.
AI tactical policy: BLOCKING for specialized objective policy until verified.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

Design guardrails

Sending the offer cannot count as receipt. Receipt cannot count as acceptance. An expired offer cannot be newly dispatched, while delivery latency remains an independent fact that a later decision owner must evaluate. The original promise remains historical evidence. World state continues evolving throughout communication. No battle, hazard or adapter rule is implied by the narrative setup.

Open questions

After delivery, the requester needs a durable accept/reject decision over the exact received terms. Expiry must be checked at that decision boundary. If accepted, a separate owner must create the replacement commitment and define future-action supersession without erasing the old commitment from history.