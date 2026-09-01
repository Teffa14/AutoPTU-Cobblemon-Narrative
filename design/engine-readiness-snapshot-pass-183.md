# Engine readiness snapshot — pass 183

Status: READ-ONLY EVIDENCE SNAPSHOT
Date: 2026-09-01
Narrative theme: field search, wayfinding and missing-person continuity

Writable repository: Teffa14/AutoPTU-Cobblemon-Narrative.
Read-only evidence: Teffa14/AutoPTU-Java and Teffa14/AutoPTU.

## Live heads

AutoPTU-Java: `6afb2d95c1de0fcc5b8e6a6c72b361370b3eeb80`.

Newest visible commit remains `Bind forced movement content through canonical registry seam (#315)`.

That work strengthens canonical content ownership around forced displacement and builds on candidate-step constraints, Shadow Tag-related checks and content-backed prevention. It remains evidence for a subset of complete movement rather than the entire family.

AutoPTU: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Newest visible commits remain Career/presentation/roster-recovery oriented. They provide no new evidence to promote tactical capability categories.

## PTU/Caelo boundary relevant to this pass

Read-only AutoPTU search confirms PTU-facing data and extracted trainer content include Survival and related field-oriented concepts. This means Narrative must not create a free universal tracking mechanic that bypasses PTU Skills, Features or Pokémon Capabilities.

The Marea canon currently gives Mara Commander / Survivalist concepts and responsibility for route checks, wildlife incidents and practical assistance. Ema is Researcher / Backpacker and works on the Mirador transect. These are canonized character concepts and responsibilities, not proof that every tracking or rescue action is mechanically implemented.

Permanent rules for this pass:

`NARRATIVE_SEARCH_PROCEDURE != PTU_TRACKING_FEATURE`

`CLASS_CONCEPT_PRESENT != EXACT_FEATURE_IMPLEMENTED`

`POKEMON_SPECIES_THEME != VERIFIED_SENSORY_CAPABILITY`

No indexed Caelo source was located in the inspected repositories that establishes regional search-and-rescue authority, ranger jurisdiction, emergency signaling, navigation law, missing-person definitions or special tracking practices. Those fields remain unresolved.

## Permanent capability categories

VERIFIED for currently covered contracts:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:

- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

Recent Java evidence proves meaningful forced-movement components. It does not establish the full Push/Pull/Knockback/Interception matrix, collision handling, partial stops, arbitrary footprint interactions, reaction ordering or every content-specific movement override.

BLOCKING when a concept requires the complete family:

- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Non-tactical Minecraft world-state and persistent quest-object support can still be used for search journals, found objects, route markers and notices. That does not promote complete tactical playback.

## Pass-183 non-tactical candidates

The following proposals can progress without tactical-family completion:

- The Walker Who Returned Another Way;
- Found Equipment, Unknown Owner Status;
- Two Search Teams, One Old Map;
- Three Flags from the Same Morning;
- Margin's Repeated Turn;
- Mirador Timing Window;
- The Check-In That Never Arrived;
- Search Paused at the Crossing;
- Found, But Not Ready to Walk;
- The Search That Ends Without the Player;
- Marea Search Ledger.

They depend mainly on world state, schedules, communications, provenance, route segments, location triggers, ordinary NPC movement, archive records and access/closure state.

## Mechanically rich candidate: The Upper Bend Search

Full intended dependency audit:

- targeting/footprints/range/LoS: required; VERIFIED for covered contracts, exact roster audit still required;
- base movement legality: required; VERIFIED for covered contracts;
- complete movement: required if searchers, a vulnerable subject, interception or forced displacement are tactical; PARTIAL and blocking for that intended form;
- core calculations: required; VERIFIED for covered contracts;
- action economy/initiative: required; VERIFIED for covered contracts;
- full turn/round lifecycle: required for sustained escort/protection/search objective handling; PARTIAL;
- full stateful damage pipeline: required; PARTIAL;
- status lifecycle: PARTIAL when selected content applies statuses;
- terrain/weather/hazards/zones/reactions: BLOCKING if unstable route cells, weather pressure, hazards or reaction protection are tactical;
- move-specific behavior: PARTIAL, exact move set audit required;
- abilities: PARTIAL, exact set audit required;
- items: PARTIAL, exact set audit required;
- Trainer Features/perks: PARTIAL, exact set audit required;
- AI legal-action infrastructure: VERIFIED for covered contracts;
- AI tactical policy: BLOCKING for objective-aware rescue, protection, retreat and path reasoning;
- Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING for faithful full in-world projection.

The full version remains BLOCKED.

## Reduced implementation

Keep search sectors, trace interpretation, route restrictions, the located subject and search-team coordination in authoritative world state outside BattleSpec.

If a genuine hostile encounter prevents safe withdrawal, place the subject and noncombatants outside combat authority and resolve one separate ordinary battle on stable terrain using an exact audited roster selected to avoid unsupported forced movement, complex statuses, tactical hazards, weather phases and unverified feature interrupts.

Allowed battle handoff:

`IMMEDIATE_WILD_THREAT_WITHDREW`

or

`IMMEDIATE_CLEARING_SECURED`

Forbidden battle-authored outcomes:

- `SUBJECT_FOUND` unless contact was already established by world evidence;
- `SUBJECT_SAFE`;
- `SEARCH_COMPLETE`;
- route reopened;
- trace ownership established;
- cause of disappearance/delay proved;
- care need resolved;
- search authority expanded.

## Current implementation opportunity

The strongest first playable slice is `The Walker Who Returned Another Way`.

It can use:

- Marea Field Office and canonical Sendero anchors;
- Mara as route/incident coordinator;
- ordinary arrival/check-in expectation state;
- Lia or another legitimate source to eliminate one explanation;
- communications corrections;
- case closure and relationship consequences;
- autonomous subject self-return.

It deliberately tests whether the world can resolve a search without making the player the sole causal actor.

A second strong slice is `Found Equipment, Unknown Owner Status`, because it composes server-owned quest objects with provenance and teaches that physical evidence can be real while its interpretation remains uncertain.

## Unresolved mechanics/canon questions

- Does Caelo define formal search-and-rescue roles, Ranger authority or emergency field jurisdiction?
- What check-in or trip-plan practices actually exist in Marea?
- Which role can formally open, suspend, transfer and close a field-search case?
- Does Mirador maintain a field movement/check-in log or only scientific observation records?
- Which ferry records can be consulted during an active concern and by whom?
- Which PTU Skills, Features, Capabilities or Pokémon senses can legitimately narrow a search, and are they represented in Java parity?
- What signaling tools exist in the setting and what are their exact PTU/Caelo rules?
- What privacy and archive rules apply to active and historical missing-person records?
- Which transport/care pathways apply once a subject is contacted but cannot safely travel?

## Snapshot conclusion

Field-search content can advance now as evidence-driven world state, route exploration, communication and institutional continuity. The first implementations should remain non-tactical and avoid omniscient target coordinates. The full Upper Bend rescue encounter remains blocked until complete movement, lifecycle, damage/status content, zones/reactions, tactical AI and faithful adapter/playback are verified for the exact mechanics selected.