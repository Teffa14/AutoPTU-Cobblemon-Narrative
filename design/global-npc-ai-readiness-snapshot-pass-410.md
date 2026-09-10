# Global NPC AI Readiness Snapshot — Pass 410

Status: ACTIVE IMPLEMENTATION SNAPSHOT
Canon effect: NONE
Date: 2026-09-10

## Slice completed

Pass 410 closes the holder-history recovery seam identified by Pass 409.

`tools/global_npc_holder_history_v4_generation.py` adds `validate_exact_v4_holder_history_generation()`. The coordinator requires a real V4 manifest plus all five selected owner checkpoint candidates. It reconciles exact generation digests before restoring the selected WorldResource catalog and holder-transition journal and before admitting bounded holder-history replay.

Fresh same-cut holder baselines are still issued only after safe post-restore reconciliation. They remain future-facing evidence and cannot certify the catalog that produced them.

`tests/test_global_npc_holder_history_full_v4_rollover.py` drives two complete later V4 generations and verifies holder continuity across intervening handoffs. It also proves that a valid holder-baseline checkpoint from the wrong generation is rejected at the manifest boundary.

## Research and narrative progress

Fresh searches covered PTU campaigns/actual plays, fan games, faction progression, survival dungeons and environmental exploration. Repository duplicate checks excluded recurring sources already represented in research.

New research anchors are Pokémon Emerald Enhanced for the abstract pattern of several organizations providing different work, relationships and access in an open world, plus Pokémon Cave Escape for the abstract pattern of finite resources and route/escape pressure making traversal itself consequential.

New proposal: `The Cache Was Empty for a Reason`, status PROPOSED / NON-CANON. A shared emergency field cache is unexpectedly depleted. Persistent custody, holder history, reservations, obligations and communications allow the world to distinguish legitimate prior use, delayed replenishment, stale records and actual loss without declaring a conspiracy in advance.

No source characters, plots, maps, faction identities, rewards, layouts or distinctive mechanics are imported.

## PTU / Caelo / Kairos boundary

Kairos/Caelo material remains a routing/reference surface rather than automatic rules authority. Potentially relevant areas include Survivalist, Backpacker, Researcher, Skills/Edges/Features, movement/terrain, hazards/weather and Items/Gear.

Pass 410 grants no new Skill DC, carrying mechanic, exhaustion rule, Item effect, Trainer Feature, Move behavior, Ability behavior, hazard effect or special movement permission.

## Live engine evidence

AutoPTU-Java head inspected: `70b20f502e34c4d3a3130a6a661476858330543e`, merge PR #433, `Materialize generic approach Shift ability effects`, dated 2026-09-10.

The evidence remains narrow: Ability-triggered legal approach-Shift execution plus one temporary-effect materialization seam. It does not complete Abilities, complete movement, forced movement, action economy, initiative, lifecycle, status lifecycle, hazards/zones/reactions, Trainer Features or tactical policy.

AutoPTU Python head remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only viewport coordinate synchronization and explicitly changes no battle rule or outcome.

## Capability posture

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL as a complete family.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes. Tactical carry, interact, repair, rescue, use-cache and extraction actions need explicit admission.

AI tactical policy: BLOCKING for conserve-supplies, recover-cache, protect-carrier, rescue-first, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative cache state, consumable-resource interaction, persistent environmental objective state and non-KO completion.

## Next seams

The holder-history path now validates successive recovery through an exact V4 generation boundary. The next persistence step should concentrate on durable storage/selection orchestration for successive complete owner generations rather than weakening the historical proof rules.

The larger independent blocker remains stable AutoPTU battle/session identity and authoritative recovery for tactical resolution that was in flight during a crash. Persistent-world code and Minecraft must not infer that result.
