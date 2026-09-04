# Ecological habitat engineering and legacy contract

Status: PROPOSED contract. Pass 267. No habitat-engineering behavior, structure or facilitation edge is promoted to Marea/Sendero canon by this document.

Record: `ECOLOGICAL_HABITAT_MODIFICATION_V1`.

Required fields: stable modification id; site scope; physical-change class; physical-state; origin authority; creator-attribution state; creator source reference when admissible; created world epoch/tick; semantic-horizon policy; recipient-use evidence references; ecological-effect interpretation state; tactical-semantics state; provenance; canon status.

Allowed physical states: `PRESENT`, `DEGRADING`, `CLOSED`, `UNKNOWN`. Allowed creator-attribution states: `UNRESOLVED`, `ATTRIBUTED_INTERNAL`, `DISPUTED`, `NOT_APPLICABLE`. Allowed ecological-effect states: `NOT_EVALUATED`, `RECIPIENT_USE_OBSERVED`, `FACILITATION_HYPOTHESIS`, `COMPARATIVE_EFFECT_SUPPORTED`, `UNCERTAIN`. Tactical state is `NONE`, `PRESENTATION_ONLY`, `ADMISSION_REQUIRED`, or `ADMITTED_BY_EXACT_CAPABILITY_PATH`.

Core invariant: physical modification existence, creator identity, recipient use, ecological quality, population outcome and tactical terrain meaning are independently adjudicated facts.

A modification can outlive its creator. Source despawn, entity unload, chunk unload, non-detection, battle end or server restart cannot close the modification. Closure follows its declared semantic horizon or an authoritative physical-state transition.

Creator attribution is optional. Same site, same species, nearby Minecraft entity, model similarity, repeated appearance, nickname, UUID or NPC belief cannot establish authorship. If direct Ouros provenance supports creator attribution, it can point to an already-authoritative ecological source without changing population.

Recipient use does not imply ownership, nesting, territory, reproduction, benefit or facilitation. Repeated use may advance to `RECIPIENT_USE_OBSERVED`. A `FACILITATION_HYPOTHESIS` requires an explicit proposed interaction record. Canon `FACILITATES` promotion remains subject to evidence and canon review. Pass 266 controls claims about ecological quality; use of an engineered feature cannot bypass cue-quality separation.

A habitat modification can expose, shelter, retain, divert, obstruct or otherwise change physical resources in ecological world state. That can feed Pass 265 resource-pulse or other world-event records when independently justified. It cannot create a demographic event. Increased detections around a feature must select already-counted sources unless an independent birth/immigration transaction exists.

Minecraft/Cobblemon may render blocks, debris, cavities, water, vegetation or other visible geometry. Presentation evidence alone cannot assign biological authorship or PTU mechanical semantics. A rendered obstacle remains `PRESENTATION_ONLY` until a specific semantic mapping is admitted.

Reduced encounter: persist the modification, present it in the world, attach observation evidence and let already-counted sources use or ignore it. No AutoPTU handoff is required. No tactical blocker, cover bonus, hazard, movement cost, damage, status or forced movement is asserted.

Full encounter dependency rules: active detection or targeting of a feature/occupant requires targeting/footprints/range/LoS where applicable. Voluntary construction, approach, departure or traversal uses base movement legality. Push, pull, knockback, interception, blocking or forced displacement uses complete movement. Tactical construction/destruction sequencing requires action economy/initiative and full turn/round lifecycle. A feature that changes cover, difficult terrain, zones, hazards, reactions or weather requires terrain/weather/hazards/zones/reactions. A specific Move, Ability, Item or Trainer Feature used to create, alter or exploit the feature requires its exact family and verified behavior. Destructive damage or persistent Injury consequences require the full stateful damage pipeline; persistent status requires status lifecycle. AI legal-action infrastructure is required to generate legal autonomous actions. AI tactical policy is required for an autonomous Pokémon to decide to create, maintain, exploit, contest, avoid or abandon the feature. Minecraft/Cobblemon/Craftics adapter/playback is required for live world persistence and presentation.

Fail closed: an ecological feature with no admitted tactical mapping stays presentation/ecology only; a missing creator remains unresolved; recipient use without comparative outcome evidence remains use evidence; disappearance of the creator does not delete the feature; removal of the feature does not erase its history or prove ecological recovery.