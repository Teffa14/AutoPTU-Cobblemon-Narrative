# Site-use / identity separation contract

Status: PROPOSED DESIGN CONTRACT. It does not promote new Marea canon.

Purpose: preserve the difference between a place being used, an observer detecting a Pokémon there, and Ouros knowing which already-counted source generated the presentation.

The authoritative chain is:

`counted population source -> projection eligibility -> bounded site-use episode -> observable detection/nondetection -> player-facing inference`

A `site_id` is never an `actor_id`. A site-use episode may internally reference a counted source for reconciliation, but public observation payloads must not expose that reference.

## Required invariants

1. Site vacancy or nondetection produces zero demographic delta. It cannot imply death, emigration, capture, despawn-as-ecology, or removal from the population ledger.
2. Repeated use of one site by one source does not make that site an identity token.
3. A different source already counted in the same population may later use the same site without being auto-merged with the earlier source.
4. Same-site recurrence is low-discriminative evidence under the Pass 253 recognition model. Location alone cannot promote a hypothesis to marker-confirmed identity.
5. A site-use record cannot create a source. Source selection must precede the record and must resolve to a persistent member, unresolved counted slot, or another source class already authorized by the population contract.
6. Observation and site-use histories survive restart independently from Minecraft entity UUIDs and projection leases.
7. Territory, nest, roost ownership, mate bond, breeding status, resource ownership, and defense behavior require separate canon approval. A neutral `observation_micro_site` implies none of them.
8. An observer becoming more likely to search a previously productive site may affect future detection behavior, but it cannot increase the hidden abundance or independently corroborate the identity hypothesis.

## Player-facing evidence

Allowed: species-level sight/sound evidence, approximate location, time window, observable behavior, confidence, and provenance root.

Forbidden: `persistent_actor_id`, unresolved source slot ID, projection lease, population source key, Minecraft UUID used as ecological identity, or any hidden actor-to-site mapping.

When the only compatibility evidence is repeated site use, the recognition system remains `UNRESOLVED` or at most `POSSIBLE_SAME_INDIVIDUAL` when other compatible evidence also exists. `PROBABLE_SAME_INDIVIDUAL` still requires independent discriminative evidence under Pass 253. `CONFIRMED_BY_DIEGETIC_MARKER` still requires the separate Pass 254 marker contract.

## Reduced encounter

A player surveys a familiar ledge. A Fletchling is observed there, the ledge is empty in a later window, and another already-counted Fletchling can use the same spot later. The player can form a weak hypothesis but cannot know that every sighting is the same individual. This requires Ouros ecology/persistence and Minecraft/Cobblemon/Craftics adapter/playback support; AutoPTU battle resolution is not required.

## Rich encounter

A future version may let two counted individuals approach or contest access to the same physical micro-site, or let the player follow one to distinguish it from another. That version depends on targeting/footprints/range/LoS, base movement legality, action economy/initiative, full turn/round lifecycle, AI legal-action infrastructure, AI tactical policy, and adapter/playback. Complete movement becomes an exact dependency if interception, blocking, push/pull, knockback, or forced movement is used. Terrain/weather/hazards/zones/reactions becomes an exact dependency if the ledge or environmental state changes legality or triggers reactions. Damage, statuses, Moves, Abilities, Items, and Trainer Features are dependencies only when the encounter actually invokes them.

## Authority boundary

Ouros owns population, persistent-source identity, site-use history, observation provenance, and identity hypotheses. AutoPTU owns PTU battle adjudication after a valid battle handoff. Minecraft/Cobblemon/Craftics presents world entities, animation, sound, and interaction surfaces without inventing ecological truth.
