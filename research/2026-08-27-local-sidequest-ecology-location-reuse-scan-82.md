# Local Sidequest Ecology, Location Reuse & Quest Density — Research Scan 82

Status: research/provenance only. Nothing in this file is Ouros canon.
Date: 2026-08-27

## Research question

How can Ouros support a dense persistent world with many optional activities without turning every settlement into a wall of unrelated quest markers, repeating identical chores, or consuming locations after a single use?

The existing repository already contains strong systems for mission assembly, World Pulse, downtime, public notices, community aid, storefront continuity, workplaces, travel, research, maintenance, public space, rumor/testimony and persistent location state. This pass therefore does not create a new generic quest system. It studies how those existing systems can be orchestrated into a local sidequest ecology.

## Existing-project boundaries inspected

Relevant existing design:

- `design/mission-dungeon-grammar.md` already requires a causal mission source, activity blocks, failure-forward outputs, request surfaces, recent-experience balancing and persistent dungeon state.
- `design/world-agency-layer.md` already owns autonomous actors, World Pulse, actor knowledge, investigation graphs and participation lanes.
- `design/downtime-hobbies-personal-projects-layer.md` already owns voluntary quiet-time activity, routine compression and anti-grind rules.
- `design/public-notices-signage-world-information-extension.md` already owns physical request/notice projection without making every problem public.
- `design/community-aid-volunteer-coordination-extension.md` already owns calls for help, offers, availability and volunteer commitments.
- `design/commercial-services-storefront-continuity-extension.md` and `design/workplaces-staffing-roles-continuity-layer.md` already own service/workplace persistence.
- `design/cobblemon-runtime-authority-boundary.md` already fixes the Ouros/AutoPTU/Cobblemon authority split.

The missing design problem is selection and coexistence: when several valid small hooks exist in the same local area, which become active scenes, which remain ambient state, which collapse into one local thread, which wait, and which should never be generated at all?

## Source A — Pokémon Burning Scales

Source:
- Eevee Expo project page: https://eeveeexpo.com/threads/9078/
- Public GitHub summary surfaced at: https://github.com/Benitex/Pokemon-Burning-Scales

Observed high-level structure:

Burning Scales explicitly describes itself as a narrative/exploration-focused Pokémon fan game built around a small open world rather than a large region-spanning route. Its pitch emphasizes many characters, numerous side quests and dense interaction within a compact map.

Reusable lesson:

A world can feel large through depth of reuse rather than geographic size. Repeated contact with the same district, street, NPC cluster and service node can create more continuity than constantly moving to new disposable towns.

Transformation for Ouros:

Do not copy Burning Scales quests, characters, plot or map. Use the structural idea that a bounded local area can support many different activity types over time when the state of that place and its people actually changes.

Design implication:

Ouros should measure local narrative density by meaningful state relationships, not by raw count of quest markers.

## Source B — Pokémon Coda

Source:
- Eevee Expo: https://eeveeexpo.com/coda/

Observed high-level structure:

Pokémon Coda is a short narrative/worldbuilding-focused fangame with a limited playtime, eight side quests, two main quests and secrets/interactions distributed across locations.

Reusable lesson:

Optional content can remain legible when the number of active authored threads is bounded relative to the size and duration of the experience. Small worlds benefit from curated optionality rather than infinite procedural task volume.

Transformation for Ouros:

Do not use Coda's plot, characters, sidequests or secrets. Use its scale relationship as a reminder that density must be curated. A settlement with 40 possible state-derived hooks does not need 40 simultaneously playable missions.

## Source C — Pokémon Birdcall

Source:
- Eevee Expo: https://eeveeexpo.com/birdcall/

Observed high-level structure:

Birdcall exposes an open structure where major boss objectives can be handled in different orders, optional bosses and sidequests coexist with the primary investigation, and additional characters appear as progression advances.

Reusable lessons:

1. Optional content can unlock through progression without becoming a linear chain.
2. New local actors can enter an existing area after meaningful milestones.
3. Side content can sit beside major goals without every task becoming prerequisite content.

Transformation for Ouros:

Do not copy boss birds, characters, map structure or encounter rules. Use only the topology pattern: independent local threads, milestone-based availability and optional ordering.

## Source D — Pokémon Legends: Arceus requests and Jubilife Village

Sources:
- Requests walkthrough 1-30: https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30
- Jubilife Village: https://bulbapedia.bulbagarden.net/wiki/Jubilife_Village
- Request introduction walkthrough: https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Section_2

Observed high-level structure:

Legends: Arceus clearly separates mandatory missions from optional requests. Requests become available after specific story requirements, knowledge, Pokémon catches or time conditions. Multiple requests originate in the same settlement and repeatedly use its residents, corps, services and surrounding field regions. Jubilife itself grows during the main story while its optional request ecology expands with it.

Reusable lessons:

1. Optionality should have explicit unlock provenance.
2. The same settlement can remain a long-term content hub while changing physically and socially.
3. Request surfaces can expose some problems while direct NPC conversation exposes others.
4. A small request can deepen an institution, species relationship or resident without needing a new location.

Important Ouros boundary:

The presence of a request marker or board entry is presentation. It does not create the underlying need. Ouros world state remains authoritative.

## Source E — PTU community downtime design

Source:
- Reddit r/PokemonTabletop, “Downtime support”: https://www.reddit.com/r/PokemonTabletop/comments/ideygf

Observed high-level structure:

A PTU GM/player discussion describes a school campaign where weekdays are divided into downtime opportunities for study, sports, social activity and other pursuits. Another participant reports that players naturally created day planners to choose between several concurrent responsibilities.

Reusable lesson:

When multiple local opportunities coexist, choice itself can be meaningful. The system does not need to instantiate every possibility as a quest. Some possibilities can remain available activity lanes or scheduled windows until the player chooses to foreground them.

Rejected mechanical import:

The Reddit discussion includes homebrew downtime units, burnout and social-capital bonuses. None of those are accepted as PTU/Caelo rules for Ouros. No point economy, fatigue meter, bonus system or skill-stunt currency is imported.

## Source F — PTU campaign log #25

Source:
- Reddit r/PokemonTabletop campaign log #25: https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

Observed high-level structure:

The group reports that a long difficult Gym battle was eventually retconned/skipped rather than repeated because replaying the same fight was not fun. The discussion also notes the management burden of long PTU battles.

Reusable lesson:

Failure-forward must include repetition control. If the exact same challenge would be replayed with no meaningful state change, the narrative system should strongly prefer a changed state, alternative route, summarized resolution where policy permits it, or a new tactical premise rather than cloning the original encounter.

Ouros application:

A failed optional battle should create a callback, blocker, changed opponent preparation, route change, opportunity cost or later reconsideration. It should not automatically respawn as an identical marker demanding another identical battle.

## Source G — PTU NPC-preparation community advice

Source:
- Reddit r/PokemonTabletop, “Help with important NPC classes”: https://www.reddit.com/r/PokemonTabletop/comments/ndootg

Observed high-level structure:

One experienced respondent recommends avoiding full mechanical class builds for most incidental NPCs and reserving heavier preparation for recurring rivals/villains or other mechanically important actors.

Reusable lesson:

Narrative density must not imply full mechanical instantiation. Most local actors can exist through identity, schedule, role, knowledge and a small set of authored facts. Full PTU combatant construction should occur only when the actor actually needs authoritative battle state.

This aligns with Ouros' existing distinction between persistent narrative actors and tactical participants.

## Source H — Pokémon Shifting Skies

Source:
- Eevee Expo: https://eeveeexpo.com/shifting-skies/

Observed high-level structure:

The fangame is built around one village and its surroundings across changing seasons, with the protagonist's home/family and local scientists remaining relevant while environmental conditions shift.

Reusable lesson:

A stable local cast and home region can support changing narrative pressure when time/environment modifies context. A location does not need a new quest identity each time; the same routine, path or resident can generate different decisions because current world state differs.

Transformation boundary:

No characters, ChronoBarometer concept, family plot, species arrangement or story secret is transferred.

## Cross-source synthesis

The strongest reusable pattern is local depth through stateful reuse.

A healthy Ouros sidequest ecology should:

- derive each hook from explicit world facts;
- keep only a small foreground set active at once;
- let several valid opportunities remain ambient or latent;
- cluster related needs into one local thread when they share actors, causes or locations;
- unlock new optional content from actual milestones rather than player level alone;
- reuse residents and locations after their first mission;
- preserve the result of completed/failed/ignored content;
- avoid identical repeated encounters;
- avoid fully statting every local NPC until battle requires it;
- permit quiet opportunities to exist as downtime choices without becoming quests;
- keep discovery surfaces separate from the underlying state;
- allow the same location to change role across seasons, institutions, ecology and player history.

## Candidate design vocabulary

Proposed design terms for Pass 82:

- `local_content_cell`: bounded place/actor cluster used for selection, not a new geography authority.
- `hook_candidate`: a valid state-derived opportunity before it is foregrounded.
- `foreground_thread`: a currently surfaced optional story thread.
- `ambient_opportunity`: a valid low-pressure possibility that remains discoverable without a formal mission.
- `latent_hook`: valid condition that should not be surfaced yet.
- `hook_merge`: combines multiple candidates that share a causal root.
- `hook_suppression_reason`: why a valid candidate is deliberately not surfaced now.
- `local_saturation_budget`: bounded number of simultaneous foreground threads.
- `revisit_delta`: what materially changed since the player last interacted with the same local thread.
- `repeatability_guard`: rejects identical re-instantiation without a state delta.
- `thread_retirement`: closes a thread while preserving history and downstream consequences.

These names are proposed architecture terms, not canon vocabulary.

## Mechanics boundary

This research does not establish any PTU/Caelo mechanic.

A local hook may reference battle only after encounter implementation review. Selection of a sidequest cannot grant:

- XP, Training Features, Skills or Edges;
- Loyalty/Friendship;
- battle bonuses;
- recovery;
- hidden reputation modifiers;
- custom encounter scaling;
- automatic Pokémon capabilities;
- custom fatigue/burnout systems.

Mechanically rich encounters must keep the permanent engine capability categories visible and use full/reduced forms when needed.

## Cobblemon boundary

This pass follows `design/cobblemon-runtime-authority-boundary.md`.

Safe reuse can include NPC/Pokémon overworld entities, signs, map markers, UI, models, animation, sounds, particles, blocks, schedules, interaction hooks, networking and persistence surfaces.

Ouros owns why a hook exists, whether it is active, who is involved and what world facts change.

AutoPTU owns tactical participants and all battle resolution.

Cobblemon battle-state or participant logic is never used as authority.

## Research conclusion

Ouros does not need more raw quest generation. It needs a local orchestration layer that decides when valid world-state hooks become foreground content and prevents density from turning into noise.

The best next design step is therefore a local sidequest ecology/location-reuse extension layered above Mission Grammar and World Agency, with no new mechanical reward system and no new canon assumptions.
