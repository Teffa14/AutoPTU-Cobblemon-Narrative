# Replacement Commitment and Consequence Continuity Research — Pass 449

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Research date: 2026-09-12
Narrative baseline inspected before writing: `e40dc381626f0593bdc3c968bb2cbe2a8c09adb1`

## Repository cross-check

The recursive repository tree was inventoried before writing. Current focus, canon inventory, recent assistance Passes 422–448, communication/private-knowledge owners, counterproposal commitments, renegotiation proposals, replacement-offer decisions, tests, proposal history and prior research anchors were checked before selecting this slice. No canon file is changed.

Recent anchors including Citizen Sleeper, Roadwarden, Stoneshard, Archmage Rises, Pokémon Mystery Dungeon, Wartales, 80 Days, A Highland Song, Dead Rising, Long Live the Queen, Suzerain and the already reused April 2026 PTU rival-team thread were not reused as primary sources.

Exact-title search found no prior source-level use of `The Life and Suffering of Sir Brante` and no prior source-level match for the r/PokemonTabletop thread `Some inspiration` (`12nnpzb`).

## Source 1 — The Life and Suffering of Sir Brante

Public sources:
- https://store.playstation.com/en-au/product/EP5036-CUSA31131_00-8779315563592274
- https://www.gog.com/en/game/the_life_and_suffering_of_sir_brante

Observed high-level structure:
- the game tracks earlier deeds, acquired capabilities and overlapping circumstances across long spans;
- later options and consequences depend on accumulated prior state rather than only the latest scene;
- accountability is a later consequence of recorded choices, not the same event as making the choice.

Transformation for Ouros:
- an old assistance promise remains part of history after replacement terms become executable;
- a replacement commitment changes future schedule ownership without deleting the superseded agreement;
- later accountability systems should consume the full lineage rather than infer blame from the mere fact of renegotiation.

Excluded:
- setting, social order, named characters, plot, resurrection structure, dialogue, statistics and specific endings.

## Source 2 — PTU community one-session exploration advice

Public source:
- r/PokemonTabletop, `Some inspiration`, 2023-04-15: https://www.reddit.com/r/PokemonTabletop/comments/12nnpzb/

Observed high-level structure:
- advice recommends choosing a clear main hook for a bounded session;
- if the endpoint is a boss encounter, earlier locations can foreshadow and support it;
- if the focus is exploration or roleplay, preparation can center on a small number of important points rather than overbuilding every possibility.

Transformation for Ouros:
- accepting replacement terms should schedule the obligation, not pre-author a complete tactical scene;
- the reduced version can preserve the narrative premise with communication, travel/access evidence and a few meaningful locations;
- the rich version may later add a structured boss, hazard or escort sequence only after current world state and engine capability admission are known.

Excluded:
- the poster's island, Moltres worship structure, specific encounter content and any distinctive plot details.

## Live engine evidence

AutoPTU-Java `main` inspected at `1ff22f2bb1495527ca6aea08d40ce87f38f4a9d5`, merge of PR #452, `Dispatch guarded switch triggers from authoritative runtime`.

The change adds a server-authoritative runtime dispatcher for reactive switch-trigger planning and Feature-specific pre-dispatch guards. It strengthens the narrow Quick Switch / switch-trigger seam and deterministic Feature dispatch. It does not demonstrate generic reactions/interrupts, complete action economy, complete Trainer Feature coverage, complete movement, terrain/weather systems or specialized non-KO objectives.

AutoPTU Python `main` remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is explicitly presentation-only and does not alter battle rules or outcomes.

## Capability posture for concepts derived from this scan

- targeting/footprints/range/LoS — VERIFIED only inside audited scopes;
- base movement legality — VERIFIED only inside audited scopes;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED only inside audited scopes;
- action economy/initiative — PARTIAL;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED / PARTIAL / BLOCKING by requested behavior;
- move-specific behavior — individually gated;
- abilities — PARTIAL and individually gated;
- items — individually gated;
- Trainer Features/perks — individually gated; PR #452 strengthens one switch-trigger path only;
- AI legal-action infrastructure — specialized objective verbs require explicit admission;
- AI tactical policy — BLOCKING for specialized nonstandard objectives unless separately verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## Reusable design lesson

A changed agreement should affect future execution while preserving old evidence. Narrative consequences can then distinguish a good-faith renegotiation, a missed promise, a changed site condition and later social interpretation without collapsing them into one mutable quest state.
