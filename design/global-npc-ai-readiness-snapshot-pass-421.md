# Global NPC AI readiness snapshot — Pass 421

Status: IMPLEMENTED NARRATIVE-REPO SLICE / NON-CANON CONTENT

Repository baseline

Pass 421 starts from narrative main `88c4c699f229fead12fad3c9fd9ba28ffcbada09` after Pass 420. The recursive repository tree was inventoried before writing. Canon governance, the Pass 418–420 consequence/observation/delivery chain, private information queues, world-event coordination and replanning, recent research/proposals and the PTU/Caelo/Kairos source router were reviewed. Canon files remain unchanged. AutoPTU-Java and AutoPTU were inspected read-only.

Implemented seam

`tools/autoptu_world_observation_replanning.py` connects a Pass 420 `ScheduledObservationDelivery` to the existing `GlobalNpcWorldEventCoordinator`.

The bridge validates that the queue still owns the exact scheduled envelope and that the sender-side source claim retains the committed observation transaction as provenance root. It then uses the ordinary coordinator cycle. Successful delivery adds knowledge to the named receiver, creates the existing `KNOWLEDGE_DELIVERED` trigger and resolves that receiver's agenda through the standard planner.

Queued, budget-deferred, failed and waiting-for-local-ack states do not wake the receiver. An accepted local acknowledgement can complete delivery and trigger replanning. A rejected acknowledgement cannot.

The bridge does not read the original AutoPTU result payload or tactical state. Shared organizational membership does not broaden the audience.

Regression

`tests/test_global_npc_autoptu_world_observation_replanning.py` covers terminal delivery, explicit-recipient isolation, queued delivery, zero-budget deferral, unavailable channels, local ACK acceptance/rejection and tampered provenance binding.

Research and proposal

Research: `research/2026-09-11-selective-warning-replanning-event-scan-421.md`

Proposal: `proposals/2026-09-11-the-warning-changes-one-assignment-421.md`

Both remain outside canon.

New public sources

Aipom's Great Pirate Adventure, Eevee Expo project thread by PikachuMazzinga, August 11, 2026. Reusable high-level structure: objective composition can depend on which recruits/resources are available instead of assuming a permanently fixed party.

Event-Driven Storytelling with Multiple Lifelike Humans in a 3D Scene, Lim et al., arXiv:2507.19232. Reusable high-level structure: temporal scenes can be decomposed into events involving the relevant characters and objects rather than synchronously changing every actor.

No characters, plots, dialogue, locations, encounter rosters, relics, generated motions or distinctive scenes were imported.

Live AutoPTU-Java evidence

Inspected main: `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merge PR #441, `Freeze replacement initiative insertion oracle`, committed September 11, 2026 UTC.

The oracle strengthens one bounded replacement-initiative seam. Action economy/initiative remains PARTIAL because the evidence does not establish the complete family.

Live AutoPTU evidence

Inspected main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains presentation-only viewport coordinate synchronization and explicitly states that battle rules and outcomes do not change.

Capability posture

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
AI legal-action infrastructure: VERIFIED only for audited ordinary actions.
AI tactical policy: BLOCKING for specialized warning-aware rescue, escort, extraction, protect-carrier and objective-aware withdrawal policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objective state, specialized non-KO completion and in-flight recovery.

PTU / Caelo / Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing aid to combat, movement/terrain, status, hazards/weather, encounter construction, Items, Trainer capabilities and living-world structure. Its references do not grant Ouros mechanics. Pass 421 adds no PTU/Caelo rule.

Next implementation seam

Persist the causal link between a delivered-information replan and any concrete world action, revised commitment or explicit request for assistance. A selected agenda intent must remain distinct from completed action. If the recipient wants another actor to change course, that effect should require a real communication or obligation-assignment event.

Separate unresolved paths

Engine authority `UNKNOWN` and `EXPLICITLY_ABANDONED` still require separate durable policies. Persistent Injury and Status consequences remain deferred until their producing AutoPTU paths are sufficiently verified.
