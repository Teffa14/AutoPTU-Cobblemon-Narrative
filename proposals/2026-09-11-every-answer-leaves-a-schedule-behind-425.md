# Every Answer Leaves a Schedule Behind — Pass 425

Status: PROPOSED / NON-CANON

## Premise

A named NPC receives a legitimate request for help. The request reaches the right person, but the recipient already has a life, obligations, travel constraints and incomplete knowledge.

The important story beat is the answer the recipient chooses to give.

Ouros can preserve four first-class outcomes: accept, defer, reject or counterpropose. Each belongs to the recipient. Each can change what happens next without retroactively rewriting the request or silently mutating another actor.

## Existing canon surfaces that could host the pattern

Marea already contains suitable roles without adding new canon facts.

Mara Veyra coordinates field reports, route checks, wildlife incidents and practical assistance from the Marea Field Office.

Teo Lark maintains ordinary equipment and field instruments at repair row.

Nerea Sol owns longitudinal ecological and weather observations at Estación Mirador.

Oren Vale handles routine Trainer/Pokémon care and local care administration.

These roles are possible regression surfaces only. This proposal does not canonize a new incident, request, obligation, relationship state or schedule.

## Reduced version

A route observation reaches Mara. Mara decides that a damaged field instrument should be checked before a later route inspection and sends Teo a request.

Teo receives the message. His planner evaluates the request together with his current schedule, travel, obligations, relationship state, permissions and knowledge.

Possible outcomes:

`ACCEPT_ASSISTANCE_REQUEST`
Teo chooses to help. The answer becomes a durable world action. A later owner must still create any actual commitment, reservation or travel plan.

`DEFER_ASSISTANCE_REQUEST`
Teo agrees that the issue matters but cannot take it now. The durable response can later support a specific time window or condition. No future wake is invented until such a condition exists.

`REJECT_ASSISTANCE_REQUEST`
Teo declines. The request remains historically true, and the rejection remains historically true. Mara can seek another solution after she actually receives the reply.

`COUNTERPROPOSE_ASSISTANCE_REQUEST`
Teo offers another contribution or timing. He might propose repairing the equipment if someone else brings it to repair row, suggest a later inspection window, or identify another actor who could handle the immediate need. The counterproposal must travel back as explicit information before it can affect Mara.

The core story works without AutoPTU.

## Why this adds useful narrative texture

A helper can care about the same problem while disagreeing about method or timing.

Repeated requests can expose relationship and institutional pressure without forcing automatic obedience.

A refusal can create a new search for alternatives instead of a dead quest state.

A counterproposal can split one broad objective into several smaller responsibilities.

A delayed answer can make travel and communication timing matter while preserving the agency of both actors.

## Mechanically rich version

The request can originate from a field situation where one team is already handling a mixed objective: observation, retrieval, evacuation, route protection or environmental pressure.

A helper who accepts may later join a structured AutoPTU encounter. A helper who counterproposes may instead support preparation, equipment, records or another non-combat lane.

The narrative premise survives when the tactical version is unavailable. The reduced version simply resolves the assistance decision at world level and keeps any structured mechanics behind the normal AutoPTU handoff.

## Exact capability dependencies for the full version

Targeting/footprints/range/LoS: required if the assistance encounter uses ranged protection, line-dependent objectives or positioned interactables. VERIFIED only in audited scopes.

Base movement legality: required for ordinary tactical relocation. VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: required for dragging, interception, rescue repositioning, knockback or forced displacement. PARTIAL.

Core calculations: required for audited ordinary combat arithmetic. VERIFIED only in audited scopes.

Action economy/initiative: required when a late-arriving helper joins initiative or when response timing changes who may act. PARTIAL. AutoPTU-Java PR #443 strengthens only a narrow replacement switch-handoff oracle seam.

Full turn/round lifecycle: required for multi-round arrival windows, delayed objectives or environmental phases. PARTIAL.

Full stateful damage pipeline: required when damage consequences carry through the encounter. PARTIAL.

Status lifecycle: required for persistent or timing-sensitive tactical conditions. PARTIAL.

Terrain/weather/hazards/zones/reactions: required for unstable terrain, weather pressure, hazardous areas, reaction windows or zone-triggered effects. MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior: individually gated for every move relied upon by the encounter.

Abilities: PARTIAL and individually gated.

Items: individually gated.

Trainer Features/perks: individually gated, especially for interrupts or response-time effects.

AI legal-action infrastructure: ordinary audited actions have scoped support. Rescue, escort, protect, retrieve, carry, interact, brace and extract require explicit admission.

AI tactical policy: BLOCKING for specialized objective-aware rescue, escort, protection, extraction, withdrawal and helper-arrival policy.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative specialized objective state, specialized non-KO completion and in-flight recovery.

## Canon questions before adoption

Which Marea roles may formally request another person's assistance, and which requests are merely personal asks?

Does any institution create a duty to answer within a window, or should response timing always emerge from ordinary schedule/obligation state?

Which accepted responses should become hard commitments versus soft intentions?

How should repeated rejected requests affect relationships, if at all, without converting refusal into an automatic trust penalty?

What authored conditions can wake a deferred response again without global polling?

These remain proposal questions. No answer is canonized here.
