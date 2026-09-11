# The Window Survives the Cut — Pass 431

Status: PROPOSED / NON-CANON
Date: 2026-09-11

## Premise

An NPC receives a request, chooses DEFER and creates a future reconsideration window. The world is saved or the relevant area unloads before that window opens. When the world resumes, the original decision, optional expiry and one future wake still belong to the same causal chain.

The dramatic premise is simple: leaving the scene does not reset time or erase another person's unresolved decision.

## Reduced version

A requester asks a specialist for help. The specialist defers until semantic minute 180 with an optional expiry at 240. The world checkpoint is taken at minute 150.

After restore, the same deferral identity and provenance return with the same pending wake. At minute 180 only the responder becomes eligible for reconsideration. The planner evaluates current knowledge, goals, needs, commitments, permissions, risk and travel state.

No battle occurs. If the wake was already processed before the checkpoint, restore preserves that completed state and does not schedule a duplicate reconsideration.

## Full version

The bounded incident may concern a route inspection, damaged equipment, a missing field team, a retrieval, an escort or another local problem. The request can exist as one modular episode inside a longer Region, Faction, Character, Relationship, Exploration or Secondary questline without becoming a new runtime quest engine.

If the restored world later selects a tactically rich response, the world layer creates the ordinary explicit `REQUEST_AUTOPTU` handoff. The saved deferral does not encode a frozen battle specification because the tactical situation may have changed while the request was waiting.

## Capability dependencies for a mechanically rich continuation

targeting/footprints/range/LoS: required only if the resumed incident needs tactical targeting or visibility. VERIFIED only in audited scopes.

base movement legality: required for ordinary tactical movement. VERIFIED only in audited scopes.

complete movement including push/pull/knockback/interception/forced movement: required for forced displacement, interception, carrying or movement-sensitive rescue behavior. PARTIAL.

core calculations: required for ordinary audited combat arithmetic. VERIFIED only in audited scopes.

action economy/initiative: required for structured tactical sequencing. PARTIAL. Current replacement-initiative evidence does not verify the whole family.

full turn/round lifecycle: required for round-bound objectives, delayed effects or multi-phase timing. PARTIAL.

full stateful damage pipeline: required when damage and resulting state persist through the tactical scene. PARTIAL.

status lifecycle: required for persistent, expiring or phase-sensitive statuses. PARTIAL.

terrain/weather/hazards/zones/reactions: required only where the resumed incident uses those behaviors. MIXED / PARTIAL / BLOCKING by exact mechanic.

move-specific behavior: individually gated.

abilities: PARTIAL and individually gated.

items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for ordinary audited actions. Specialized rescue, escort, protect, retrieve, carry, interact, brace or extract actions require explicit admission.

AI tactical policy: BLOCKING for specialized objective-aware rescue, escort, protection, extraction and withdrawal policy.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for specialized authoritative objective state, non-KO completion and in-flight recovery.

## Expiry boundary

The optional expiry remains descriptive until a later pass owns late-processing policy. Restoring an already expired record must not invent success, failure, travel or battle. The future runtime must define whether an unprocessed stale trigger is consumed silently, produces an explicit closure wake or follows another reviewed transition.

## Questline compatibility

This proposal uses the canonical composable quest graph. One bounded assistance incident may contribute to several existing questline families, but the underlying world event remains singular. A modular episode does not justify inventing a parallel quest runtime.

## Canon boundary

No incident, named participant, location, faction rule, relationship change or outcome is canonized here. Existing canon entities may later host this pattern only through reviewed authored content. The implementation described here is global NPC architecture, not a Marea special case.
