# Reopened Terms and Stateful Choice Scan — Pass 445

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-12

Repository inspection

The recursive repository tree was inventoried before writing. Current focus, canon paths, assistance request/response/counterproposal/commitment chain, viability/start/disposition owners, renegotiation request/decision/reply transport, research notes, proposals, tests and source-routing material were checked before this pass. No canon file is changed.

Current seam

Pass 444 can deliver a requester's explicit acceptance or rejection of reopening to the original responder. The delivered acceptance contains no replacement terms. The missing capability is a durable responder-authored offer whose authority can be traced to the delivered consent while the old commitment remains historical fact.

New public sources

1. Failbetter Games, “Fallen London Writer Guidelines: Part II,” 2015-04-15.
   URL: https://www.failbettergames.com/news/fallen-london-writer-guidelines-part-ii
   Reusable lesson: quality-based narrative benefits from a small, explicit state vocabulary instead of proliferating near-duplicate flags. For Ouros, the negotiation chain should preserve a few durable facts—old promise, reopen consent, replacement offer—rather than mutating one opaque quest state.
   Excluded: setting, prose, characters, storylets, currencies and proprietary narrative content.

2. King of Dragon Pass, public product description and design summary.
   URL: https://store.steampowered.com/app/352220/King_of_Dragon_Pass/
   Reusable lesson: decisions can become durable obligations whose later consequences depend on both the agreement and subsequent world conditions. For Ouros, replacement terms should have lineage rather than erasing the promise that caused them.
   Excluded: Glorantha setting, clans, gods, scenes, text and event content.

3. Pokémon Tabletop community discussion, “Rival Team for Kanto based PTU Campaign,” 2026-04-04.
   URL: https://www.reddit.com/r/PokemonTabletop/comments/1sbx3kf/rival_team_for_kanto_based_ptu_campaign/
   Reusable lesson: experienced advice cautions against overbuilding distant fixed encounter content because player levels, teams and circumstances will change. For Ouros, a renegotiated assistance offer should record the changed obligation and defer encounter realization until live world state is known.
   Excluded: the poster's campaign premise, canon character lineup, teams and encounter specifics.

4. Pokémon Tabletop community discussion, “New to PTU,” 2026-01-27.
   URL: https://www.reddit.com/r/PokemonTabletop/comments/1qo26uy/new_to_ptu/
   Reusable lesson: shorter arcs, recurring characters and Pokémon-centered local problems can provide progression without locking the campaign into one monolithic plot. For Ouros, renegotiated local assistance can become a compact recurring-NPC thread whose later outcome reflects changed conditions.
   Excluded: specific suggested rivals, player characters, Pokémon choices and any authored story content.

Transformation into Ouros

The useful pattern is an explicit three-stage reopening: durable old promise; delivered permission to reopen; responder-authored replacement offer. The third stage gains its own provenance root while retaining decision lineage. This makes later consequences inspectable without claiming the new offer was already accepted.

A local assistance thread can therefore survive schedule changes naturally. A specialist can propose a later survey window after a route closure, while the surrounding site continues to evolve independently. If the proposal eventually reaches a hazardous scene, the tactical encounter should be built from current evidence at execution time rather than from frozen assumptions made when the negotiation began.

PTU/Caelo and engine caution

No source above changes PTU/Caelo rules. Narrative state records social/temporal facts only. Movement, reactions, status effects, hazards, move behavior, abilities, items and Trainer Features remain engine-owned when mechanically structured.

Live read-only engine evidence checked 2026-09-12:

AutoPTU-Java head: `f859888213385e313df923678b62374ac6919b22`, merged through PR #449. The head freezes Quick Switch side-effect order. This is narrow evidence for that path and does not prove complete action economy, reactions/interrupts or Trainer Features/perks.

AutoPTU Python head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest commit explicitly states presentation-only viewport-coordinate synchronization with no battle-rule or outcome change.

Capability posture for any mechanically rich follow-up

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated; Quick Switch evidence is not family coverage.
AI legal-action infrastructure: ordinary audited actions only; specialized objective verbs require explicit admission.
AI tactical policy: BLOCKING for specialized objective policies.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

Research conclusion

The safest next narrative/system step is to preserve replacement terms as an offer with exact lineage and no execution authority. This advances social continuity and recurring NPC arcs without forcing the adapter or battle engine to simulate mechanics that remain unverified.