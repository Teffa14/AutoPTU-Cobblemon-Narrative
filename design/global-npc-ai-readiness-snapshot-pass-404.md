# Global NPC AI Readiness Snapshot — Pass 404

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE

## Concrete change

Pass 404 adds deterministic holder-history baseline issuance from an exact validated WorldResource catalog checkpoint.

`tools/global_npc_holder_history_baseline_issuance.py` validates `OUROS_WORLD_RESOURCE_CATALOG_CHECKPOINT_V1`, optionally verifies the expected catalog generation digest, and emits one stable `HolderHistoryCoverageBaseline` per catalog resource in canonical resource-id order.

Each certificate binds resource identity, holder at the checkpoint semantic minute, exact checkpoint SHA-256, schema provenance and deterministic baseline identity.

No baseline claims holder-history completeness before its own checkpoint cut.

`tests/test_global_npc_holder_history_baseline_issuance.py` covers deterministic issuance, exact-generation mismatch, content tampering and future-checkpoint rejection.

## Safety boundary

The catalog checkpoint remains the owner of current operational resource state at its semantic cut.

Pass 404 derives certificates from that owner. It does not create a competing resource owner and it does not infer missing checkout, return or handoff events.

Pass 402 still protects known production holder-mutator call sites. Pass 403 still performs bounded forward replay from an explicit baseline.

The next recovery integration should reissue certificates from the exact catalog generation selected by the outer recovery manifest rather than trust caller-authored baseline objects.

## Narrative progress

New research used a Pokémon Tabletop United one-shot description for objective-first cave investigation and Pokémon Lazarus creator release material for routes whose visible activity changes with time of day while substantial side content coexists with the main journey.

`Two Watches, One Pass` transforms those structures into an original Ouros proposal where separate observations of the same site at different semantic windows may both be correct.

Status remains PROPOSED / NON-CANON.

## PTU/Caelo/Kairos boundary

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid only. Relevant families may include Researcher, Chronicler, Climatologist, Survivalist, Topographer, movement/terrain, hazards, weather, encounter creation and campaign structure.

Pass 404 approves no Skill, Edge, Feature, Item effect, move, ability, status, hazard, weather modifier, visibility rule, carrying rule or tactical interrupt.

## Live engine evidence

AutoPTU-Java read-only head: `92661d4f2eb97d56043723c520077bea2a8ab873`, merge #427, `Materialize authoritative switch transaction`.

The new executor validates the frozen switch plan and field-presence preconditions before mutation, then materializes the audited outgoing/replacement active state, field presence and entry markers before the generic COMBATANT_ENTRY hook.

Its own contract still leaves mount/rider synchronization, send-out Trainer Features beyond registered entry hooks, hazards/zones, initiative replacement semantics and action-economy consumption outside this bounded prefix.

This strengthens only the audited switching seam. It does not complete switching, full lifecycle, complete movement, Abilities, Trainer Features, hazards/zones or action economy.

AutoPTU Python read-only head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only.

## Capability classification for Two Watches, One Pass

Targeting/footprints/range/LoS: VERIFIED only inside previously audited scopes.

Base movement legality: VERIFIED only inside previously audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only inside previously audited scopes.

Action economy/initiative: PARTIAL overall; audited primitives exist.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only inside ordinary audited scopes.

AI tactical policy: BLOCKING for investigate-first, observe-before-engage, preserve-evidence, rescue-first, protect-observer, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative time-window objective state, evidence interaction, environmental revision projection and non-KO completion.

## Next highest-value seam

Integrate Pass 404 issuance into post-restore activation so bounded baselines are reissued from the exact WorldResource catalog checkpoint selected by the recovery manifest and its catalog digest, eliminating trust in caller-authored provenance for that path.

Stable AutoPTU battle/session identity and authoritative in-flight tactical recovery remain the larger independent blocker.
