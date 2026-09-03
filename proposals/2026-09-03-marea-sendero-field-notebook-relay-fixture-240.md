# Marea / Sendero — Field Notebook Relay fixture

Status: PROPOSED WORLD CONTENT
Pass: 240
Canon effect: NONE until approved

## Premise

A run of inconsistent Fletchling reports around Sendero del Vidrio creates a field-research problem rather than a combat problem.

One observer reports a small group near a creek edge. Another reports signs along a different route. A relayed story inflates the number seen. An older notebook entry may refer to the same persistent individual that has been encountered before, but the current projection carries a different Minecraft entity UUID.

The player is asked to reconcile what is actually supported, what is stale, what shares one rumor source, and what remains unresolved.

No new Fletchling population value is established by this proposal. Runtime must use the existing approved population ledger and persistent-individual records.

## Player loop

The player receives several pieces of evidence with different provenance:

- a firsthand visual sighting;
- tracks or other ecological traces;
- a copied secondhand report;
- an older field note;
- an optional new observation made by the player.

The useful choice is not simply `correct/incorrect`. The player can classify conclusions as supported, suspected, disputed or stale.

A successful investigation can improve the local field archive and NPC knowledge without changing the underlying ecology.

## Distinctive identity seam

A repeat sighting can suggest that one visible Fletchling is the same persistent individual documented previously if observable cues support the match.

The interface may show a field nickname or descriptive tag after sufficient evidence. It must never reveal the internal persistent-member ID, lease ID or Minecraft UUID.

If evidence remains incomplete, the correct output is `PROBABLE_MATCH`, not forced certainty.

## Consequences

Possible non-canon candidate consequences:

- improve an NPC's confidence in a route-use claim;
- mark a previously repeated rumor as one-source evidence rather than independent corroboration;
- reopen a stale route claim for new observation;
- unlock a follow-up survey window;
- identify a knowledge gap that becomes a later ecology-driven quest.

No reward may silently modify population abundance, migration truth, habitat state or persistent identity.

## Reduced implementation

The reduced version requires only Ouros persistent evidence/knowledge storage plus normal Minecraft presentation.

The player visits marked observation areas, receives observable events, compares records and submits conclusions. No battle begins. No hidden tactical simulation runs.

This version preserves the complete narrative premise and can ship before rich ecological pursuit mechanics.

## Rich implementation

A richer version may let the player physically follow a wary Pokémon or compare moving groups across cover, weather and route boundaries.

Potential mechanics:

- line-of-sight observation windows;
- stealth/tracking checks under the active PTU rules profile;
- an actor choosing hide/flee/regroup based on ecological intent;
- timed observation opportunities;
- weather or terrain reducing visibility;
- an optional structured encounter if the player corners or threatens wildlife.

These are enhancement layers, not requirements for the investigation story.

## Permanent engine capability dependencies

Reduced version:

- targeting/footprints/range/LoS: not required for evidence ledger itself;
- base movement legality: not required beyond ordinary Minecraft traversal;
- complete movement including push/pull/knockback/interception/forced movement: not required;
- core calculations: only if an adopted PTU skill check is invoked;
- action economy/initiative: not required;
- full turn/round lifecycle: not required;
- full stateful damage pipeline: not required;
- status lifecycle: not required;
- terrain/weather/hazards/zones/reactions: world context only, no tactical dependency;
- move-specific behavior: not required;
- abilities: not required;
- items: conditional on observation tools;
- Trainer Features/perks: conditional on explicit PTU Feature use;
- AI legal-action infrastructure: not required;
- AI tactical policy: not required;
- Minecraft/Cobblemon/Craftics adapter/playback support: required to automatically capture/present real overworld observation events.

Rich version:

- targeting/footprints/range/LoS: required for structured visibility/targeting;
- base movement legality: required;
- complete movement: required if pursuit/interception/forced retreat is authoritative;
- core calculations: required;
- action economy/initiative: required if observation becomes structured encounter turns;
- full turn/round lifecycle: required for timed windows;
- full stateful damage pipeline: only if damaging combat occurs;
- status lifecycle: only if statuses affect the encounter;
- terrain/weather/hazards/zones/reactions: required when weather, dangerous terrain or reaction zones have tactical effects;
- move-specific behavior / abilities / items / Trainer Features: each required only if the encounter explicitly uses that family;
- AI legal-action infrastructure: required for generated legal choices;
- AI tactical policy: required for purposeful hide/flee/regroup/guard behavior in structured play;
- Minecraft/Cobblemon/Craftics adapter/playback: required for end-to-end presentation and observation capture.

## Canon questions left open

- Which existing Marea NPC or institution, if any, owns the first formal field archive?
- Whether the first persistent Fletchling already has enough approved observable distinguishing cues for reliable recognition.
- What field terminology players see for confidence and staleness.
- Which PTU skill checks and DC policy Ouros will adopt for active interpretation versus passive observation.

Until answered, fixture observers and archive owners remain generic fixture actors.