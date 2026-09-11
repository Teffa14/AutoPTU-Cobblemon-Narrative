# Investigation handoff and inherited evidence scan — Pass 419

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note is canon.

## Repository-first deduplication

The recursive repository inventory, canon governance, current global-NPC focus, recent Pass 411–418 AutoPTU recovery/result work, existing observation/evidence tools and recent research/proposals were inspected before source selection. Previously processed anchors including Pokémon Starwish, Pokémon Unchosen, Outer Wilds, Pokémon Shadowside, Pokémon Hollow Woods, Pokémon Lithic Veil, Lethalmon, Pokémon Knowledge, Pokémon Crystal Inheritance, Pokémon Rollout!, Pokémon Diadem, A Short Hike, Pokémon Aragonite, Reckless Rollers material and The Roaring Trainers were excluded.

Repository search found no prior use of the 2026 fangame `Pokémon Memories` under that title and no prior use of `The Case of the Golden Idol` / `Golden Idol`.

## New source: Pokémon Memories

Public source: Eevee Expo thread by AppleRowlet, started April 16, 2026: https://eeveeexpo.com/threads/9452/

The public project description presents two playable viewpoints separated by time. One character returns to Kalos and travels with a local professor; one month later the professor becomes the playable viewpoint in a damaged Lumiose and tries to determine what happened. The project also advertises a semi-open structure with side quests.

Reusable structure for Ouros:

A later investigator can inherit a changed world and selected records from an earlier participant without inheriting that participant's complete knowledge. The handoff itself can become play: compare old records with current conditions, distinguish what was actually documented from what was only privately believed, and decide which old leads are still actionable.

Ouros does not import Kalos, Lumiose, the named characters, memory-loss plot, catastrophe, mechanics, quests, encounters or story.

## New source: The Case of the Golden Idol

Public design interview: GameDeveloper, `Pursuing the "Aha!" moment with deductive reasoning game The Case of the Golden Idol`: https://www.gamedeveloper.com/design/case-of-the-golden-idol

Public game description and design material describe a deduction loop where players inspect concrete scene details, build hypotheses and eliminate or revise them as evidence accumulates. The developer interview specifically discusses players forming incorrect theories and gradually eliminating them rather than receiving a single authoritative explanation immediately.

Reusable structure for Ouros:

Evidence records and conclusions should remain separate. An archive, field report or prior investigator can transfer observed facts while leaving the receiving actor free to form a different hypothesis. A later correction should add evidence or revise a claim with provenance instead of silently replacing history.

Ouros does not import the game's deaths, characters, visual scenes, word-bank interface, cases, chronology or solutions.

## Derived Ouros direction

A named NPC begins an investigation or field assignment, records a bounded set of observations and then becomes unavailable, leaves the district, changes duty or simply hands the work to another actor. The receiving investigator gets only the records actually transferred. Private recollections remain with their owner unless communicated.

The receiving actor may revisit the same location after a site revision and legitimately reach a different hypothesis because the world changed or because they possess different evidence. The runtime must preserve:

- original observation identity;
- observer identity;
- semantic time;
- provenance;
- current site revision;
- transferred record identity;
- receiver knowledge state;
- later hypothesis or claim identity.

A handoff therefore transfers evidence, not omniscience and not a pre-approved conclusion.

## Mechanics boundary

The reduced form needs persistent observations, private knowledge, provenance, semantic time, communications, archives, travel, schedules, obligations, permissions and site revisions. It requires no tactical battle.

A rich form may place evidence retrieval, witness protection or withdrawal under tactical pressure. Such a scene must gate exact capability families rather than assuming generic combat support.

Current live engine evidence inspected for this pass:

- AutoPTU-Java `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merged September 11, 2026 UTC, freezes a replacement-initiative insertion oracle. This strengthens one initiative seam but does not verify the entire action-economy/initiative family.
- AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its newest commit explicitly states presentation-only viewport-coordinate synchronization with no battle-rule or outcome change.

Permanent capability posture remains conservative:

- targeting/footprints/range/LoS: VERIFIED only in audited scopes;
- base movement legality: VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only in audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: VERIFIED only for audited ordinary scopes;
- AI tactical policy: BLOCKING for specialized evidence-first/protect/withdraw objectives;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objectives and in-flight battle recovery.

## PTU/Caelo cross-check

The internal PTU/Kairos source router remains a locator for skills/features, combat, movement/terrain, status, hazards/weather, encounter construction and related rules. No new PTU or Caelo mechanic is promoted by this research note. Evidence handoff and hypothesis ownership remain Ouros persistent-world narrative structures unless a future mechanic explicitly invokes an audited PTU rule.
