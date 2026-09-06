# The Order Under Review

Status: PROPOSED / NON-CANON
Date: 2026-09-06
Pass: 311

## Premise

A route restriction was issued after a relay investigation concluded that a recovered sample had a custody gap. Weeks later, the missing handoff documentation appears and the original investigator issues a superseding assessment. The route authority receives the correction and must explicitly review the restriction.

The review can maintain, amend, rescind or defer the old order. None of those outcomes automatically rewrites what happened while the order was active.

## Narrative structure

The player can reconstruct four separate causal layers: the original evidence state, the authority's knowledge at the time, the restriction itself, and the later review.

A rescission may reopen the route while leaving compensation, reputation and missed opportunities unresolved. An amended order may reopen only part of the road because an independent landslide risk still exists. A maintained order may be legitimate for a new reason even though the original custody concern was corrected. A deferred review can create pressure from travelers, workers and local institutions without declaring the authority corrupt or irrational.

Potential NPC roles are deliberately generic: route authority, relay investigator, affected courier, maintenance representative, local trader and ranger. No named NPC or institution is canonized by this proposal.

## Reduced version

The complete loop can run without tactical combat:

custody lineage -> correction receipt -> affected-decision lookup -> explicit review event -> authored route/publication/social consequences in later scenes.

Travel uses existing world-route logic. Investigation uses authored observations and provenance-backed claims. No dynamic hazard, forced movement, damage, status or reaction mechanics are required.

## Full encounter version

The authority schedules a site inspection before deciding whether to reopen the route. The inspection crosses a damaged relay access span during unstable weather. A stranded worker or wild Pokémon creates a rescue objective while rival stakeholders pressure the inspection team to continue or withdraw.

The intended full version can use wind displacement, unstable footing, timed structural deterioration, environmental damage, persistent conditions and reaction-based rescue.

## Engine dependencies

Targeting/footprints/range/LoS: VERIFIED within audited contracts if a tactical scene starts.

Base movement legality: VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required by the full wind and rescue version.

Core calculations: VERIFIED within audited contracts.

Action economy/initiative: VERIFIED within audited contracts.

Full turn/round lifecycle: PARTIAL; required for timed structural deterioration.

Full stateful damage pipeline: PARTIAL; required for environmental injury.

Status lifecycle: PARTIAL; required only if persistent exposure or injury conditions are authored.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by subfamily; central dependency of the full inspection scene.

Move-specific behavior: PARTIAL; only required when explicit Moves are authored.

Abilities: PARTIAL; only required when explicit Abilities affect the scene.

Items: PARTIAL; only required when explicit Items affect the scene.

Trainer Features/perks: PARTIAL. The current Java engine has a verified Psionic Overload TURN_END seam, but that representative Feature does not establish general Trainer Feature coverage.

AI legal-action infrastructure: VERIFIED within audited contracts.

AI tactical policy: BLOCKING for general autonomous rescue/combat choice.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING end-to-end.

## Implementation-safe tactical fallback

Represent the span as safe, blocked and dangerous-but-static nodes. Weather remains narrative. Remove wind knockback, delayed collapse, reaction rescues and persistent status effects. A rescue becomes a deterministic travel/access objective before or after a basic tactical encounter.

The decision-review premise and all social consequences remain unchanged.

## Open canon questions

Which Ouros institution can issue route restrictions?

What authored reasons can legally or socially survive after the original evidence basis is corrected?

Which PTU/Caelo Skills or Features can inspect structural danger, authenticate records or communicate with relevant Pokémon witnesses?

How should rescission or amendment later propagate to people who relied on the old order?
