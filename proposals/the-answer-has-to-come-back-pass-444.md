# The Answer Has to Come Back — Pass 444

Status: PROPOSED / NON-CANON
Canon effect: NONE
Location assignment: UNRESOLVED
Named NPC assignment: UNRESOLVED
Institution assignment: UNRESOLVED
Pokemon population assignment: UNRESOLVED

Premise

Two people already negotiated a local assistance window. Conditions changed, the responder asked to reopen the terms, and the requester decided whether to allow that. The important next beat is ordinary but consequential: the responder still does not know the answer until it travels back.

Narrative tension

A decision can exist while the person waiting on it remains uncertain. During that gap the original site can keep changing, the old service window can continue expiring, and both actors can make different plans based on different knowledge.

Reduced version

The scene runs entirely at world-simulation level.

1. The responder's reopen request has already reached the requester.
2. The requester records an explicit acceptance or rejection.
3. A reply is authored as a separate communicative event.
4. Channel latency, failure or local acknowledgement can delay knowledge.
5. Only terminal delivery gives the responder the requester's answer.
6. The original commitment remains unchanged.
7. No replacement proposal exists yet.

This version can produce useful story without combat. A radio repeater may be unavailable. A courier may arrive after the old window. The responder may wait, leave for another obligation, or receive the answer after the local problem has changed again. None of those possibilities require the world to pretend that the answer was known earlier.

Character use

A flexible requester can accept reopening but require a later concrete proposal. A deadline-sensitive requester can reject it. A responder may be relieved, frustrated or already committed elsewhere when the reply finally arrives. Those reactions belong to later social/policy owners rather than this proposal.

Environmental use

Communication delay creates space for visible world change. Water can recede, temporary barriers can appear, a repair crew can leave evidence, Pokemon activity can move elsewhere, or access signage can change. These observations do not rewrite what either actor previously knew.

Faction use

An individual may answer on their own authority while an institution has separate approval requirements. The reply reaches only explicit recipients. Membership in the same organization does not broadcast consent, refusal or new terms.

Longer arc hook

Repeated assistance negotiations can reveal which actors communicate reliably, which institutions require formal approval, who tends to overcommit, and which routes or channels repeatedly fail. Later relationship or institutional consequences should be derived from explicit history rather than hidden omniscient quest flags.

Full mechanically rich version

If an accepted reopening later produces new terms and a renewed field operation, the premise can become a survey, escort, protection job, retrieval, containment or extraction. The story still does not require a defeat-all objective.

Capability dependencies for that later rich version

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact requested behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: specialized verbs such as `INSPECT`, `ESCORT`, `PROTECT`, `RETRIEVE`, `CARRY`, `BRACE`, `CONTAIN` or `EXTRACT` require explicit admission.
AI tactical policy: BLOCKING for specialized objective policy.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

Reduced implementation dependency

Pass 444 itself depends only on the existing negotiated commitment, responder disposition, requester decision, private knowledge ledgers and `InformationEventQueue`. It does not require any battle capability family.

Open questions

A delivered acceptance still needs a separate proposal owner that can create new terms with lineage to the old commitment without overwriting it. A delivered rejection needs policy for what the responder does next. If the old window has already expired, generic missed-commitment/accountability systems must remain separate from the communication fact. Social consequences should consume explicit evidence rather than being assigned automatically by this scene.