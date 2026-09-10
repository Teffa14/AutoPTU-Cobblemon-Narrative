# The Match with No Final Bell — Encounter Seed 411

Status: PROPOSED / NON-CANON
Canon authority: NONE
Date: 2026-09-10

## Canon anchors used without alteration

Bruma Battle Yard is canonically a local battle and training institution that supports ordinary audited Trainer battles, practice and community exhibitions. It is not canonically a Gym and no badge or invented progression reward is attached to this seed.

The global world-agent foundation already requires explicit AutoPTU handoff for structured mechanics and prevents the persistent planner from competing with AutoPTU while tactical resolution is owned there.

Everything else below remains proposed.

## Premise

A scheduled training bout or small community exhibition at Bruma Battle Yard begins normally. An interruption occurs after AutoPTU has accepted the tactical handoff but before Ouros has received an authoritative final result.

The interruption can be technical, logistical or environmental. The exact cause remains unresolved and does not need to be dramatic.

When persistent world state returns, several people may have memories or records of portions of the bout. One spectator may insist that a decisive hit landed. A participant may remember conceding. Yard staff may have the schedule and the names involved. Minecraft may even have rendered an apparent final animation before disconnect.

None of those observations create the authoritative tactical result.

The Yard therefore has a real social problem without requiring a fabricated battle outcome: people must decide what obligations can continue while the formal result remains unresolved.

## Narrative use

The encounter gives Bruma Battle Yard a mundane institutional responsibility beyond staging fights. It also creates roleplay around evidence quality without turning any NPC into an omniscient referee.

Possible follow-up pressures include a later practice slot waiting for the court, a community exhibition schedule that needs adjustment, a participant who wants the result recognized, another who accepts a rematch, or a staff member who prefers to preserve uncertainty until the session can be reconciled.

These are candidate pressures, not fixed canon events.

Witness statements remain claims with source and time. They can be sincere and still conflict. An official administrative decision such as voiding or rescheduling the bout would require an authorized Yard policy that has not yet been canonized.

## Persistent-world state candidate

The world can track separate references for:

- scheduled bout or exhibition obligation;
- Ouros AutoPTU session identity;
- explicit engine-session reference if one was bound;
- participant/witness observations and communication provenance;
- authoritative result reference when one is actually received;
- later administrative decision if an authorized policy creates one.

The absence of the authoritative result must remain representable. Restart cannot collapse `ENGINE_BOUND + no result` into win, loss, draw, cancellation or retirement.

## Full version

The full version starts as an ordinary audited AutoPTU battle under a verified rules profile. Ouros creates one stable session identity before or at the authoritative handoff boundary. The engine supplies an explicit engine-session reference. If the process survives normally, an admitted semantic result returns through the existing result-ingress boundary and the session can later retire.

If a crash or transport break occurs before that result arrives, the persistent world restores the same unresolved session identity. A future recovery contract may query/reconcile the engine-owned session and accept one authoritative outcome or quarantine/abandon it through an explicit procedure.

The full story can then continue with social consequences based on what was actually resolved and what each NPC learned.

## Reduced version

The reduced version begins after the interruption and never attempts to reconstruct the unfinished fight.

The battle remains formally unresolved. The playable scene focuses on participant memory, witness reports, schedule consequences, communications and the institution's temporary response. The Yard can delay the next use of the space, separate testimony from official result state, or prepare a rematch proposal without declaring a winner.

This preserves the entire narrative premise using verified world-agent capabilities while battle-session recovery remains incomplete.

## Capability dependency map

Targeting/footprints/range/LoS — full battle depends on the exact audited scopes used by the selected battle. Current posture: VERIFIED only in audited scopes. Reduced version: not required.

Base movement legality — full battle uses only admitted ordinary movement. Current posture: VERIFIED only in audited scopes. Reduced version: not required.

Complete movement including push/pull/knockback/interception/forced movement — required only if the bout introduces those mechanics. Current posture: PARTIAL. They are excluded from the reduced version and should be excluded from a basic full regression unless individually verified.

Core calculations — full battle depends on audited calculation paths. Current posture: VERIFIED only in audited scopes. Reduced version: not required.

Action economy/initiative — exact mid-turn continuation would depend on complete authoritative action and initiative state. Current posture: PARTIAL. Pass 411 does not implement tactical resume.

Full turn/round lifecycle — needed for exact continuation from an interrupted round and for delayed/phase effects. Current posture: PARTIAL. This is a blocker for true in-flight battle resume.

Full stateful damage pipeline — needed before the world can persist authoritative HP/injury consequences from the interrupted battle. Current posture: PARTIAL. Witness descriptions never substitute for this pipeline.

Status lifecycle — required for exact continuation with ongoing conditions. Current posture: PARTIAL.

Terrain/weather/hazards/zones/reactions — only present if the selected battle explicitly includes them. Current posture: MIXED / PARTIAL / BLOCKING by mechanism. Basic regression version omits them.

Move-specific behavior — individually gated. The scenario grants no Move implementation.

Abilities — individually gated and PARTIAL as a family. Current Java evidence strengthens a Ball Fetch event-trace seam only.

Items — individually gated.

Trainer Features/perks — individually gated.

AI legal-action infrastructure — an ordinary battle may use only audited legal-action scopes. The social recovery scene runs in world-agent logic instead.

AI tactical policy — special policies such as fight-until-objective, concede-for-schedule, preserve-audience or non-KO exhibition goals remain BLOCKING unless separately verified. The reduced version needs none of them.

Minecraft/Cobblemon/Craftics adapter/playback — full presentation remains PARTIAL / BLOCKING for authoritative in-flight session recovery. The adapter may render; it cannot decide that the bout ended.

## Long-term arc potential

If the underlying session-recovery system later becomes authoritative, the same seed can test several noncombat story outcomes without changing the battle premise.

A recovered result may agree with most witnesses. It may contradict a sincere but incomplete recollection. The engine record may be unavailable, forcing an explicit administrative void/rematch policy rather than a guessed tactical conclusion. Repeated incidents could create pressure for better Yard procedure, but no such history is canonized here.

The important regional pattern is that institutions can preserve uncertainty instead of converting every missing record into certainty. That supports Ouros's broader evidence, memory and provenance design.

## Explicit unresolved questions

The exact bout participants, Pokémon, rules profile, interruption cause, spectator set, administrative authority, void/rematch policy, result-storage backend and whether this encounter ever occurs in canon all remain unresolved.
