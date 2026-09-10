# Full V4 Rollover and Shared-Cache Survival Scan — Pass 410

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-10

## Repository inspection and duplicate control

The recursive main-branch tree at `279929410126fed61886831841ab3c2abd743e59` was inventoried before writing. Current focus, canon governance, canon foundations, recent Pass 396–409 holder/custody/recovery work, implementation contracts, tests, research/proposals and PTU/Caelo/Kairos routing material were checked before selecting this slice.

Fresh public searches covered PTU actual plays and campaign listings, Pokémon fan games/ROM hacks, faction quests, open-world progression, survival-focused dungeon structures and environmental exploration. Frequently recurring sources such as Pokémon World Tour: United, The Reckless Rollers, Adventures in the Millennium, Tales of Visiwa, PokeU Panic, Social Ecology of Kanto, Pokémon Odyssey, Monomyth, Burning Scales and Recollection Quest were excluded from new-source extraction because repository search already showed prior coverage.

Repository search found no prior `Emerald Enhanced` source entry. Repository search also found no prior source entry named `Pokemon Cave Escape`; cave/escape concepts already exist internally, so only the external structural lesson below is retained and no claim is made that the theme itself is new to Ouros.

## Internal recovery finding

Pass 409 proves baseline rollover through owner-level snapshots, but its regression constructs a `ReconciledPersistentWorldRecoveryManifest` directly for the bootstrap path and does not exercise later rollover entirely through a real V4 manifest selection boundary.

Pass 410 closes that integration seam with `validate_exact_v4_holder_history_generation()`. The coordinator first reconciles the supplied V4 manifest against all five exact owner candidates. Only after digest and semantic-generation selection succeeds does it restore the selected WorldResource catalog and holder-transition journal and invoke post-restore reconciliation using the selected holder-history baseline checkpoint.

This preserves the order:

V4 generation selection -> selected owner restore -> bounded holder-history replay -> current-holder validation -> same-cut future baseline issuance.

A same-cut baseline remains future-facing and cannot validate the catalog that produced it. A carried baseline retains its earlier certification cut even when stored inside a later checkpoint.

The new integration regression drives two later complete V4 generations. It also proves that a valid baseline checkpoint from the wrong generation is rejected at the manifest boundary before holder-history replay.

## New public source — Pokémon Emerald Enhanced

Primary public project repository:
https://github.com/Enhanced-Projects/Emerald-Enhanced

Supplementary public feature summary used only to understand high-level systems:
https://www.pokemoncoders.com/pokemon-emerald-enhanced/

Public descriptions present an open-world Hoenn structure with branching main alignment, relationship quests and multiple factions that provide distinct work, rewards and access.

Reusable Ouros lesson: access to services, places, information or help can emerge from concrete institutional relationships and completed obligations rather than a single global reputation number. Different organizations can care about the same place or resource for different reasons, and the player can become entangled in those dependencies through ordinary work.

Transformation boundary: no Hoenn plot, Devon/Magma/Aqua branch, faction names, NPCs, rewards, alchemy, real-estate system, relationship implementation or proprietary project content is imported.

## New public source — Pokémon Cave Escape

Public project summary:
https://romhaven.com/games/pokemon-cave-escape/

The public description frames the entire adventure around one constrained traversal objective through a large cave network. Limited recovery resources, route choice, endurance and shortcuts make navigation itself the pressure source rather than treating travel as filler between conventional badge objectives.

Reusable Ouros lesson: a dungeon or hazardous route can sustain tension through finite shared resources, route uncertainty and safe-exit planning. An encounter can matter because it consumes time, supplies or access, even when defeating opponents is not the narrative goal.

Transformation boundary: no cave layout, encounter placement, item distribution, challenge tuning, maps, dialogue or distinctive plot material is imported.

## Synthesis for Ouros

The combined reusable structure is a shared emergency cache or field resource positioned on a route used by multiple parties. Its value comes from practical dependence. Different institutions may have legitimate reasons to stock, inspect, reserve, consume or replenish it. A later team that finds the cache depleted does not automatically have evidence of theft or sabotage.

Persistent custody, holder history, communications, obligations and route state can reconstruct whether supplies were borrowed during an emergency, formally transferred, consumed under standing authority, delayed in transit, reserved elsewhere or actually lost.

This structure complements the new V4 rollover seam because a long-lived field resource needs holder/custody evidence that survives more than one recovery generation without rewriting earlier history.

## PTU / Caelo / Kairos mechanical boundary

Existing project source policy remains authoritative. Kairos/Caelo material is a routing/reference layer and does not silently grant rules to Ouros. Potentially relevant source areas include Survivalist, Backpacker, Researcher, Skills/Edges/Features, movement/terrain, hazards/weather and Items/Gear. Any concrete Skill check, Item property, Feature interrupt, carrying rule, hazard effect or movement permission requires source-level verification and existing authority admission.

No new PTU mechanic is promoted by this research pass.

## Live engine evidence checked

AutoPTU-Java main remains `70b20f502e34c4d3a3130a6a661476858330543e`, merge PR #433, `Materialize generic approach Shift ability effects`, dated 2026-09-10. This is evidence for one narrow Ability-triggered legal approach-Shift plus temporary-effect seam only.

AutoPTU Python main remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`, whose latest commit is explicitly presentation-only viewport coordinate synchronization.

No representative implementation is generalized into family-wide capability.

## Capability implications for the proposed shared-cache encounter

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

Abilities: PARTIAL / individually gated; only narrow audited seams are admitted.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only for audited ordinary scopes; specialized carry, repair, interact, rescue and extraction actions need explicit admission.

AI tactical policy: BLOCKING for conserve-supplies, recover-cache, escort-carrier, rescue-first, objective-aware withdrawal and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for authoritative cache state, consumable-resource interaction, environmental objective state and non-KO completion.

## Open questions

Canon has not established the cache, its route, stocking institution, contents, depletion cause or any faction dispute.

PTU source-level adjudication remains required before assigning mechanics to carrying, exhaustion, survival checks, hazards, Items or Trainer Features.

The larger recovery gap remains stable AutoPTU battle/session identity and authoritative restart handling for tactical resolution that was in flight during a crash.
