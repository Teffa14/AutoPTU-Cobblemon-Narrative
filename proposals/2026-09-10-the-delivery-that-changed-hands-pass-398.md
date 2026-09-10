# The Delivery That Changed Hands — Pass 398

Status: PROPOSED / NON-CANON
Canon approval: REQUIRED before naming a region, institution, route, NPC, item or historical incident.

## Premise

A courier starts with a routine delivery of a shared field case to a receiving specialist. During the route, an unrelated emergency creates a legitimate reason to transfer the case to another qualified actor. The transfer occurs, the courier diverts to assist with the emergency and the intended recipient later receives incomplete information.

The resulting dispute can look like failed delivery, unauthorized possession or missing equipment even when every actor made a reasonable decision from the information available at the time.

The investigation asks four separate questions: who was expected to receive the case, who physically held it at each known transition, who knew that the plan changed, and what obligation had priority when the emergency occurred.

No answer is inferred from current holder state alone.

## Reduced implementation

The complete premise can run without AutoPTU.

Use semantic time, persistent NPC schedules and obligations, explicit communication, `WorldResource`, reservation/handoff history, `ResourceHolderTransitionLedger`, `OUROS_RESOURCE_HOLDER_TRANSITION_CHECKPOINT_V1` and `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3`.

The player can reconstruct the sequence, contact the actors, redirect the item, negotiate a new delivery window, document the exception or decide that the emergency justified the missed appointment. The world can preserve uncertainty when the recovered journal does not contain the transition needed to prove a claim.

## Rich encounter version

The route can intersect an active rescue or evacuation scene. The courier may need to protect a person, preserve the case, hand the case to another actor, abandon the case temporarily, or withdraw once the rescue objective is satisfied. KO is not the default success condition.

Mechanics dependencies for the rich version:

Targeting/footprints/range/LoS: VERIFIED only for previously audited scopes; needed for ordinary ranged positioning if combat occurs.

Base movement legality: VERIFIED only for audited ordinary movement scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for body-blocking, forced carrier displacement, dragging, interception or rescue reposition.

Core calculations: VERIFIED only inside audited calculation scopes.

Action economy/initiative: PARTIAL as a family; only existing audited primitives are verified.

Full turn/round lifecycle: PARTIAL; required for timed rescue windows, staged evacuation or delayed route hazards.

Full stateful damage pipeline: PARTIAL; required when damage consequences must persist through the objective state.

Status lifecycle: PARTIAL; any complex persistent condition remains gated.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanic; smoke, flooding, unstable ground, visibility zones, delayed hazards or reaction zones require their own verified contracts.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. The current AutoPTU-Java switch/Impostor seams do not promote the whole family.

Items: INDIVIDUALLY GATED. The field case is a world resource unless a PTU Item effect is separately sourced and implemented.

Trainer Features/perks: INDIVIDUALLY GATED. No courier, rescue or custody Feature is inferred.

AI legal-action infrastructure: VERIFIED only for ordinary audited scopes.

AI tactical policy: BLOCKING for rescue-first, protect-case, transfer-object, escort-carrier, abandon-object-to-save-person, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable world-resource identity, pickup/handoff acknowledgement, rescue state, environmental objective state and authoritative non-KO completion.

## Narrative consequences

A recipient may reasonably believe the delivery failed without knowing about the emergency. A dispatcher may know that the route changed but not who received the case. The temporary holder may know the physical transfer but not the original appointment terms. The courier may know why the plan changed but lack later custody information.

This supports disagreement without omniscience and without forcing deception. Trust consequences should follow only when the world has evidence about decisions, knowledge and obligations.

## Open canon questions

No institution, route, profession, item, emergency, species or region is fixed. The project still needs canon decisions about who can authorize a custody substitution, what kinds of field cases exist, what documentation is expected after emergency diversion and which PTU/Caelo rules, if any, govern relevant professional tasks.
