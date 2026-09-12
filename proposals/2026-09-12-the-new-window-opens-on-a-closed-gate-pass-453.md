# The New Window Opens on a Closed Gate — Pass 453

Status: PROPOSED / NON-CANON
Canon effect: NONE
Location assignment: UNRESOLVED
NPC assignment: UNRESOLVED

## Premise

A specialist already renegotiated an obligation once. The replacement appointment is now the only active schedule. Before it begins, source-backed evidence shows that the route, permit, equipment or local condition is still unsafe or unavailable.

At the exact replacement start, the problem remains. The world records both truths: the new appointment is valid, and fulfillment is still blocked.

## Reduced version

This version requires no AutoPTU handoff.

1. A replacement commitment is the active lineage leaf.
2. Pre-start evidence records `AT_RISK` or `BLOCKED` against that leaf.
3. Pass 453 arms the replacement start watch.
4. At the exact start minute, the unresolved condition becomes `AT_RISK_AT_START` or `BLOCKED_AT_START`.
5. Later policy can choose to wait, communicate, renegotiate again, attempt ordinary world-level work or abandon the obligation.

The scene can be conveyed through a closed crossing, posted notice, missing equipment, changed Pokémon activity, damaged infrastructure or an NPC report. Historical appointments remain visible as evidence but do not become active objectives again.

## Full version

A richer continuation can turn the blocked start into a local response scene. The party or NPC may investigate an alternate entrance, protect a survey team, stabilize a temporary route, retrieve required equipment or withdraw safely when conditions worsen.

Potential environmental loop:
- observe the blocker from a safe position;
- gather evidence from two independent local sources;
- choose between waiting, an alternate route or a temporary intervention;
- update viability from new evidence;
- enter structured mechanics only if the chosen response truly requires them.

A successful social or environmental resolution can avoid combat entirely.

## Capability dependencies

Reduced version: no battle capability family required.

Full version, depending on exact implementation:
- targeting/footprints/range/LoS: required for tactical protection or ranged interaction; VERIFIED only in audited scopes.
- base movement legality: required for tactical traversal; VERIFIED only in audited scopes.
- complete movement including push/pull/knockback/interception/forced movement: required only if route hazards or protection mechanics use those effects; PARTIAL.
- core calculations: required for structured checks/damage that enter engine authority; VERIFIED only in audited scopes.
- action economy/initiative: required if the scene becomes turn-structured; PARTIAL.
- full turn/round lifecycle: required for multi-round objectives; PARTIAL.
- full stateful damage pipeline: required for damaging hazards or combat; PARTIAL.
- status lifecycle: required for persistent status effects; PARTIAL.
- terrain/weather/hazards/zones/reactions: required for dynamic hazards, weather phases, reaction zones or delayed effects; MIXED/PARTIAL/BLOCKING by behavior.
- move-specific behavior: individually gated.
- abilities: PARTIAL and individually gated.
- items: individually gated.
- Trainer Features/perks: individually gated; current Quick Switch evidence does not generalize to the family.
- AI legal-action infrastructure: explicit admission required for `INSPECT`, `PROTECT`, `BRACE`, `RETRIEVE`, `WITHDRAW`, `EXTRACT` or similar objective verbs.
- AI tactical policy: BLOCKING for specialized objectives without an admitted policy.
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Fallback design

If dynamic weather, forced movement, reactions, delayed hazards or specialized objective verbs are unavailable, keep the same narrative premise. Resolve evidence gathering and route-state changes at world level, then hand AutoPTU a static admitted encounter only if needed.

## Unresolved questions

Pass 440 disposition still consumes only the original commitment ledger. A later pass should make disposition generation-neutral after Pass 453 has produced an adverse start assessment for an active replacement.

Only after that should a second `REQUEST_RENEGOTIATION` be allowed to traverse the full communication and consent chain.
