# Global NPC AI Readiness Snapshot — Pass 411

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 411 begins the stable AutoPTU battle/session recovery seam that remained open after Pass 410.

`tools/autoptu_session_identity.py` adds `OUROS_AUTOPTU_SESSION_CHECKPOINT_V1`, a durable Ouros-side owner for tactical-session correlation identity. Session IDs derive deterministically from immutable handoff inputs. The owner records explicit lifecycle states from request through engine binding, authoritative result receipt and retirement while retaining a quarantine state for uncertainty.

The owner does not serialize AutoPTU tactical state. An `ENGINE_BOUND` session with no authoritative result restores with no result. Retirement is unavailable until an explicit result reference has been recorded.

`tools/global_npc_autoptu_session_recovery.py` connects that checkpoint to existing persistent `NpcAgentState.active_autoptu_binding` references. Recovery rejects an `AUTOPTU_BOUND` agent with no session, a non-bound agent carrying a session, an unknown session reference, a participant mismatch and a reference to a retired session. It can enumerate engine-bound sessions that remain unresolved so later recovery work has an explicit queue instead of guessing completion.

`tests/test_global_npc_autoptu_session_identity.py` covers deterministic replay identity, immutable-input conflict, checkpoint tamper/future-cut rejection, unresolved restart, engine-reference conflict, result idempotency/conflict, retirement gating and world-agent/session reconciliation.

## Research and narrative progress

Fresh research used Pokémon Crystal Inheritance for the abstract pattern of revisiting the same geography under a changed contextual state and using earlier information to reinterpret the present. The supernatural/time-travel implementation, Johto content, characters, plot and exact puzzles were excluded.

The PTU actual-play source for this pass is Pokémon Rollout! episode 139, `Infiltrating the Illumine Gym, Part One`, published 2026-06-01 by Tapestry Radio Network. Its public episode description places an ongoing battle inside a larger journey. Pass 411 uses only the general lesson that tactical continuity and world-level continuity can cross an episode/session boundary without becoming the same authority.

New proposal: `The Match with No Final Bell`, status PROPOSED / NON-CANON. A Bruma Battle Yard bout is interrupted after tactical handoff but before an authoritative result reaches Ouros. Witness memories, schedules and presentation state can persist while the formal battle result remains unresolved. The reduced version plays entirely as an evidence/social/scheduling problem and never reconstructs the fight.

No source dialogue, characters, encounter sequence, map, region, gym plot, historic-world plot, puzzle or distinctive mechanic is imported.

## Canon boundary

The proposal reuses one approved foundation fact: Bruma Battle Yard supports ordinary audited Trainer battles, practice and community exhibitions. It does not promote the Yard into a Gym, create a badge, establish a formal league rule or define a void/rematch policy.

Participant identities, Pokémon, exact bout, interruption cause, result, witness set and administrative procedure remain unresolved.

## PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked for Chapter 7 combat, movement/terrain, status, hazards, terrain/weather, campaign/session structure, encounter creation and Items/Gear. The index remains a routing aid rather than an Ouros rules grant.

No Skill DC, battle-result rule, rematch rule, Move, Ability, Item, Trainer Feature, status behavior, hazard effect, terrain rule or special victory condition was granted by this pass.

## Live engine evidence

AutoPTU-Java head inspected: `2e704f13f98ef8984f156bef4e6ec4e8924db87b`, merge PR #434, `Freeze Ball Fetch AbilityEvent trace parity`, dated 2026-09-10.

The new evidence compares a structured Ball Fetch AbilityEvent trace against the pinned Python oracle, including actor, ability, effect, target, target HP, from/to coordinates, phase and round. This strengthens one Ability-triggered approach-Shift event seam. It does not supply a durable engine-session recovery store or prove the complete Ability, movement, lifecycle or action-economy families.

AutoPTU Python head inspected: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest commit remains presentation-only viewport coordinate synchronization and explicitly changes no battle rule or outcome.

Both engine repositories remained read-only.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL as a complete family. Exact continuation from a mid-turn crash remains outside Pass 411.

Full turn/round lifecycle: PARTIAL. True in-flight tactical resume remains blocked.

Full stateful damage pipeline: PARTIAL. Ouros must not rebuild HP/injury aftermath from witness or adapter presentation.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated. PR #434 strengthens one Ball Fetch event-trace seam only.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Session recovery itself is world integration, not tactical legal-action admission.

AI tactical policy: BLOCKING for special exhibition/non-KO/objective policies unless separately verified. The reduced encounter requires no new tactical policy.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative in-flight battle recovery. Presentation correlation may survive; completion cannot be inferred from entity, animation, UI, disconnect or restart state.

## Current recovery boundary

Pass 411 proves an Ouros-side session identity can survive restart and remain unresolved while a persistent NPC continues to point at it. It still does not prove that the referenced engine-owned battle state survives, resumes or exposes an authoritative final result.

The new checkpoint is not yet selected by `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V4`. Adding it silently would make legacy V4 generations claim an owner they never selected. The next coherent-persistence step therefore requires an explicit new recovery-manifest generation or equivalent exact-generation boundary that includes the AutoPTU session checkpoint digest.

After that, the larger engine-side seam remains: reconcile one `ENGINE_BOUND` Ouros session against an authoritative AutoPTU session store after crash, with explicit outcomes such as still-active, completed-with-result, unknown/quarantined or administratively abandoned. Minecraft remains outside that authority path.
