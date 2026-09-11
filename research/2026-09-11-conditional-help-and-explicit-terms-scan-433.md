# Conditional help and explicit terms scan — Pass 433

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-11

The repository tree, current focus, canon surfaces, recent assistance passes and recorded research corpus were inspected before this scan. Searches confirmed that `Citizen Sleeper 2` contract material, the current `PokeU Panic!` PTU campaign listing and the current Valoryn PTU campaign listing had no recorded research hits under those names. Pokémon Gaia was explicitly rejected as a new source because earlier Ouros research already used it in passes 53 and 383.

No protected dialogue, named plot sequence, character or location is imported below. Only high-level structures are retained.

## Source 1 — Citizen Sleeper 2 design interviews: help can carry explicit conditions

Public references:
- GameSpot, “In Citizen Sleeper 2, Every Mechanic Strives To Have A Story-Driven Consequence”: https://www.gamespot.com/articles/in-citizen-sleeper-2-every-mechanic-strives-to-have-a-story-driven-consequence/1100-6515301/
- SUPERJUMP, interview/preview with Gareth Damian Martin: https://www.superjumpmagazine.com/citizen-sleeper-2-hands-on-preview-interview-with-gareth-damian-martin/

Reusable structure:
- a needed resource or service may be offered only under additional conditions;
- who participates can itself be one of the terms;
- a job can begin with one expected outcome and change while being carried out;
- crew availability and location matter instead of every useful person becoming a permanent party member;
- success/failure and profitability are separate judgments.

Ouros transformation:

A responder should be able to say “I can help later,” “I can help at this location,” “I can only inspect,” or “I can offer this alternative.” These are authored proposal terms. They are not equivalent to ACCEPT. The requester must actually receive the terms before planning around them, and later execution must still use current schedules, permissions, travel and mechanical authority.

Excluded:
- characters, setting, ship/crew fiction, dice systems, contract mechanics, dialogue and specific missions.

## Source 2 — PokeU Panic! PTU campaign listing: ordinary life and mystery can occupy the same schedule

Public reference:
- StartPlaying, “PokeU Panic!”: https://startplaying.games/adventure/cmr6r2xws01ecl604wm1bf5qr

The public listing describes a PTU campaign where students balance classes, friendships, rivalries, clubs and battles while a wider mystery develops.

Reusable structure:
- a persistent role or daily obligation can coexist with investigations and emergencies;
- helping with a mystery does not erase ordinary calendar demands;
- social, exploratory and tactical scenes can all contribute to the same arc.

Ouros transformation:

An NPC who proposes assistance terms keeps the rest of their life. A limited scope or delayed time can emerge because the actor has work, care, travel, institutional or personal obligations. The proposal records the offered boundary rather than pretending a named NPC is always available for the player's current quest.

Excluded:
- university, disappearances, secret-project plot, sponsors, specific rivals and all named campaign fiction.

## Source 3 — Valoryn PTU campaign listing: institutions can mediate access without becoming hive minds

Public reference:
- Warwick Tabletop Games and Role-Playing Society, “Pokémon Tabletop United: Valoryn Region Campaign”: https://www.warwicktabletop.co.uk/events/809/

The listing presents a region where an alliance of factions regulates travel and guards historical knowledge while local adventure begins on a smaller scale.

Reusable structure:
- institutional responsibilities can influence access, travel or who is appropriate to ask;
- faction context can shape a proposal without making every faction member aware of it;
- large regional tensions can coexist with small local work.

Ouros transformation:

Permissions and institutional duties may influence why a responder proposes another location, narrower scope or alternate helper. The communication remains addressed to explicit actors. Shared membership cannot substitute for delivery, consent or individual knowledge.

Excluded:
- Guild Concord, Titans, rebellion, seals, Greenglen and all campaign-specific lore.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked. It routes campaign/session structure to pp. 449+, encounter creation to pp. 470+, recurring rivals/villains to p. 477, tactical movement/terrain to pp. 382+, statuses to pp. 397+, hazards to p. 401 and terrain/weather to pp. 404+. The index also records living-world downtime, one-shot quests, faction activity and persistent character history.

These references support the separation between persistent world activity and structured encounters. They do not define Ouros communication semantics and do not prove engine implementation. Proposed assistance terms remain world-simulation data until an accepted task actually crosses an explicit `REQUEST_AUTOPTU` boundary.

## Reusable Ouros design lessons

1. Conditions belong to the offer, not to hidden planner assumptions.
2. Receiving “COUNTERPROPOSE” without receiving the terms is insufficient knowledge.
3. Location, schedule, scope, alternative and expiry should remain provenance-backed data.
4. A stale offer can still be historically informative after expiry.
5. Institutional context may justify terms, but cannot broadcast them automatically.
6. A requester accepting terms must be a later world action, not an inference from delivery.
7. An accepted proposal still needs a separate commitment owner before time or travel is reserved.

## Encounter implications

Reduced version:

A pump inspection, archive consultation, route survey or equipment diagnosis can play entirely as request → counterproposal → explicit terms delivery → requester decision → scheduled world commitment. No battle mechanics are required.

Full version:

If accepted help later enters a hazardous retrieval, escort, rescue, containment or disputed-site operation, the premise remains identical but tactical resolution may require AutoPTU. Do not simplify narrative causality merely to fit missing tactical support.

Permanent capability posture for such a future full version:
- targeting/footprints/range/LoS: VERIFIED only in audited scopes;
- base movement legality: VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL;
- core calculations: VERIFIED only in audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: VERIFIED only for audited ordinary actions;
- AI tactical policy: BLOCKING for specialized objective-aware assistance tactics;
- Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for specialized objective state and non-KO completion.

## Live engine evidence checked

AutoPTU-Java main: `2f72abe6c0e2b58533856484a1cc954f9e6648e8`, merge PR #445, “Wire replacement initiative runtime handoff.” This is material production progress for a replacement-initiative route, but it does not verify the complete action-economy/initiative family or unrelated lifecycle/reaction families.

AutoPTU Python main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head states that the viewport-coordinate change is presentation-only and changes no battle rules or outcomes.

Both repositories were treated read-only.
