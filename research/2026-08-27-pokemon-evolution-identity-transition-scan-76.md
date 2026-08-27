# Pokémon Evolution, Identity Continuity & Transition Research — Pass 76

Status: research/provenance only. Nothing in this file is automatically Ouros canon.

Date: 2026-08-27

## Research question

How can Ouros treat Pokémon Evolution as a persistent world event that changes the mechanical/species projection of one Pokémon without deleting that individual's history, relationships, observations, custody, public memory or agency?

This pass deliberately avoids inventing Evolution mechanics. Exact eligibility, branching, stat changes, Ability changes, Move changes, item consumption, timing and any battle interaction remain governed by the project's PTU/Caelo source set plus authoritative AutoPTU implementation evidence.

## Internal repository review before research

The current repository tree was inspected before authoring. The closest existing layers are:

- `design/pokemon-agency-partnership-release-layer.md`: establishes stable Pokémon identity across capture, transfer, temporary cooperation, release, rehoming, institutional care, migration and retirement. This is the primary identity boundary for Pass 76.
- `design/breeding-eggs-nursery-lineage-layer.md`: separates authoritative mechanical state from provenance, custody, ownership and care history.
- `design/interspecies-ecological-relations-layer.md`: owns ecological observations and relationships, not individual Evolution state.
- `design/care-recovery-welfare-layer.md`: owns health/care continuity and cannot infer mechanical transformation from appearance.
- `design/shared-equipment-lending-issued-assets-extension.md`: may need a post-Evolution fit/eligibility review for issued equipment but never grants capabilities because a Pokémon changed species.
- `design/credentials-authorizations-recognition-extension.md`: any institutional authorization survives or changes only through its own rules.
- `design/cobblemon-runtime-authority-boundary.md`: Cobblemon can provide embodiment and playback but cannot author Pokémon combat state or mechanical facts for Ouros.
- `design/encounter-implementation-contracts.md`: rich encounters must expose exact capability dependencies and reduced forms.

No dedicated Evolution/identity-transition layer was present in the inspected tree, so this pass fills a real gap rather than duplicating an existing subsystem.

## Source scan

### 1. Pokémon Legends: Arceus — Beauregard's Wurmple requests

Source:
https://bulbapedia.bulbagarden.net/wiki/Appendix%3ALegends%3A_Arceus_walkthrough/Requests_1-30

Relevant high-level structure:

- an NPC forms an expectation about what a specific Pokémon will become;
- the same individual persists through multiple Evolution stages;
- the NPC's earlier interpretation can be wrong while the Pokémon's identity and partnership remain continuous;
- later visits can show the same individual in another stage, creating a natural callback.

Reusable Ouros lesson:

Actor expectations about Evolution should be claims, not canonical outcomes. When the authoritative transition happens, old expectations remain in history and can be corrected without deleting the earlier belief. The Pokémon keeps the same stable identity.

Do not copy:

- Beauregard, his dialogue, the exact request chain or rewards;
- the Wurmple/Cascoon/Dustox sequence as an Ouros quest;
- the game's scripted branch outcome.

### 2. Pokémon Legends: Arceus — Wurmple branch opacity

Source:
https://bulbapedia.bulbagarden.net/wiki/Wurmple_(Pok%C3%A9mon)

Relevant high-level structure:

Some Evolution branches are not transparently selectable by an observer. A character may have a reasonable expectation and still lack access to the determining variable.

Reusable Ouros lesson:

The narrative layer must not reveal or select hidden branch determinants merely because it would produce a cleaner story. If the governing mechanical source treats a branch as opaque, the world should preserve uncertainty until the authoritative event resolves it.

### 3. Pokémon Mystery Dungeon — Luminous Cave / Evolution interfaces

Sources:
https://bulbapedia.bulbagarden.net/wiki/Luminous_Cave
https://bulbapedia.bulbagarden.net/wiki/Evolution_(Mystery_Dungeon)

Relevant high-level structure:

- Evolution can be separated into eligibility, access to a transformation process/location and the actual transition;
- an attempt can fail because requirements are not satisfied;
- different entries in the series move or alter where Evolution is accessed without changing the broad idea that eligibility and execution are distinct states;
- some NPC Pokémon can refuse Evolution in specific entries, demonstrating that a setting can preserve unevolved persistent identities without treating them as incomplete characters.

Reusable Ouros lesson:

Keep `eligibility`, `intent/access`, and `completed transition` separate. Do not treat arrival at a facility, possession of an item or a narrative desire as proof that the transformation is mechanically legal.

Do not copy:

- Luminous Cave/Spring/Tree of Life;
- Evolution Crystal costs;
- postgame gating;
- any Mystery Dungeon-specific party restrictions.

### 4. Cobblemon current Evolution implementation

Sources:
https://gitlab.com/cable-mc/cobblemon/-/tree/main/common/src/main/kotlin/com/cobblemon/mod/common/pokemon/evolution
https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/api/pokemon/evolution/Evolution.kt
https://gitlab.com/cable-mc/cobblemon/-/blob/main/common/src/main/kotlin/com/cobblemon/mod/common/pokemon/evolution/CobbledEvolutionDisplay.kt
https://gitlab.com/cable-mc/cobblemon/-/issues/723

Observed implementation surfaces:

- Cobblemon has dedicated evolution controllers/proxies and display objects;
- its server-side `Evolution` abstraction contains a result, optional/queued behavior and implementation-specific side effects;
- it exposes tested/completed Evolution event surfaces;
- it already has Evolution animation/display code;
- its own issue history shows that Evolution eligibility/options may depend on dynamic context and can become stale when conditions change.

Reusable Ouros lesson:

Cobblemon contains valuable species/evolution metadata, events, UI/networking and presentation code. Those are candidates for adapter reuse. Its server-side Evolution resolver is not allowed to become the authoritative PTU/Ouros rules engine.

Architecture consequence:

- `SAFE_REUSE`: models, textures, cries, particles, animation/display components, UI, networking, species/form metadata, event observation hooks and persistence/identity surfaces where they do not decide mechanics.
- `ADAPTER_REQUIRED`: translating an already-authorized AutoPTU/Ouros transition into a Cobblemon entity/species projection; collecting player intent; triggering visual playback after authoritative commit; reconciling stable IDs.
- `BATTLE_AUTHORITY_FORBIDDEN`: any Cobblemon Battle/BattleState/participant/controller path deciding combatants, HP, status, legality, initiative, result or Evolution consequences inside authoritative combat.
- `EVOLUTION_AUTHORITY_FORBIDDEN`: allowing Cobblemon's own Evolution resolver to choose the canonical PTU branch, consume a mechanically meaningful item, recalculate authoritative stats, change authoritative Ability/Move state or commit the persistent transition before PTU/AutoPTU approval.

### 5. Cobblemon Evolution display/animation issue history

Source:
https://gitlab.com/cable-mc/cobblemon/-/work_items/1229

Reusable Ouros lesson:

Visual playback has its own failure modes and therefore must remain downstream from authoritative state. A missing particle or repeated animation cannot duplicate or undo the persistent mechanical transition.

### 6. PTU community discussion — Ability changes after Evolution

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1s2zswq/basic_abilities_change_when_evolving_pokemon/

Classification: community discussion only; not an authoritative rules source.

Why it matters:

The discussion highlights a real implementation risk: Evolution can interact with Ability identity/slots. This is enough to flag an exact source-review requirement, but not enough to establish the rule for Ouros.

Reusable Ouros lesson:

Never implement Evolution as a cosmetic species swap. The authoritative transition packet needs room for downstream mechanical changes such as Ability or Move state when the governing PTU/Caelo rules require them.

### 7. PTU community campaign design — custom Evolution as homebrew

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1h0on8f

Classification: community campaign inspiration only.

Relevant high-level structure:

A GM can make Evolution itself a campaign-specific design lever, including custom forms or thresholds.

Ouros constraint derived from this:

That flexibility is precisely what this project must not silently import. Custom Evolution species, thresholds, branches, forms or benefits require explicit canon/rules approval. A compelling story hook does not grant permission to create a new mechanical Evolution.

## Cross-project mechanical evidence

### AutoPTU-Java

Inspected `main` head during this pass: `c3b94bf4d4d5d0c3939bed027d3f9556b7c300e9`.

New evidence since Pass 75:

- held-item START rule profiles are now wired into the live lifecycle;
- the hook is gated and respects Magic Room suppression;
- parity/tests cover the new path.

This strengthens `items`, `status lifecycle` and `full turn/round lifecycle` only as partial families. It does not prove a general Evolution transition pipeline.

The current Java README still lists major unfinished families including complete combatant/grid battle state, full damage resolution, the full StatusController, terrain, hazards, forced movement, reactions, complete registries, semantic transcript parity, tactical AI and Craftics/Cobblemon integration.

No inspected Java evidence in this pass proves an authoritative Evolution runtime, branch resolver or atomic persistent species-transition contract.

### AutoPTU Python

Inspected `main` head during this pass: `69270e5e207774bac4a3f57b002d459efaafde1f`.

Recent work connects established rivals to featured Career battles. That is useful persistence work but does not establish Evolution mechanics.

No inspected Python evidence in this pass is sufficient to make Evolution an executable Ouros transition without PTU/Caelo source review and explicit runtime support.

## PTU/Caelo source-review gates

Before any Evolution becomes mechanically authoritative in Ouros, review the supplied project source set for at least:

- legal Evolution prerequisites;
- branch-selection rules;
- whether an actor may decline/postpone an otherwise available Evolution;
- level/stat recalculation;
- current HP/max HP interaction;
- Ability changes;
- Move-list or known-Move consequences;
- Capability changes;
- held-item consumption;
- trade/location/time/environment conditions where applicable;
- Trainer Feature interactions;
- temporary transformations versus permanent Evolution;
- whether Evolution may legally occur during a tactical encounter;
- transcript/state requirements needed for rollback and replay.

Until those are resolved, narrative content may establish expectations, observations and consequences around Evolution but cannot manufacture the transition mechanically.

## High-level design conclusions

1. Evolution changes the state of one persistent Pokémon; it does not create a new character record.
2. The stable `pokemon_id` survives every permanent Evolution.
3. Prior species/form state remains historical provenance rather than being overwritten.
4. An actor's expectation about the outcome is a claim, not truth.
5. Branches are never chosen for narrative convenience.
6. Evolution does not automatically change personality, relationship labels, Loyalty, ownership, maturity, employment, institutional authority or social role.
7. Physical changes can trigger review of equipment, spaces, routes or work assignments, but those systems decide their own consequences.
8. Wild tagged/known individuals can remain recognizable after Evolution when provenance supports the identity link.
9. Actor knowledge updates only through observation/communication, even if the world state already contains the authoritative transition.
10. Cobblemon should supply as much embodiment and playback as possible while remaining downstream of AutoPTU/Ouros authority.

## Originality boundary

Pass 76 uses only abstract structures such as persistent identity, mistaken expectation, gated transformation, branch uncertainty, later callbacks and visual playback boundaries. No protected dialogue, distinctive quest sequence, named NPC, setting-specific institution or plot is imported into Ouros.
