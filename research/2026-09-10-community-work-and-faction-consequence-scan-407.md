# Community Work and Faction Consequence Scan — Pass 407

Status: RESEARCH / NON-CANON
Accessed: 2026-09-10
Canon effect: NONE

## Internal inspection and duplicate avoidance

The repository tree and current focus were inspected before writing. Canon governance, playable foundation, recent recovery/resource passes, persistent observations, obligations, travel, institutional layers, faction material, quest taxonomy, recent proposals and the Kairos/PTU routing index were cross-checked. Candidate sources were searched against the repository. `Super Pokémon Online`, `Pokémon Lazarus`, `Pokémon Mystère Exploration`, `PMD: Maelstrom`, `Pokémon World Tour: United`, `Pokémon Synthesis Version` and several other recent anchors were rejected because they already appear in prior research.

## New public source: Pokémon Resonance development brief

Public source: r/PokemonRMXP development post, published 2026-07-03.
URL: https://www.reddit.com/r/PokemonRMXP/comments/1umq2s7/pokemon_resonance_is_looking_for_a_mapper_side/

The public development brief describes a story-driven fan game using community notice boards in Pokémon Centers to offer local jobs. The stated design purpose is to express the region through ordinary community work, with more demanding jobs becoming available as the player advances.

Reusable structure for Ouros: local institutions can expose practical needs through diegetic public boards. A small job can reveal how a settlement functions, who depends on whom, which resources are scarce and what risks residents consider normal. Progression can widen the responsibility of available work without requiring every assignment to belong to a single central quest chain.

No Australian setting material, indigenous stories, fakemon, attacks, towns, progression numbers or specific jobs are imported.

## New public source: Pokémon Last Chance

Public source: HackHaven public project listing.
URL: https://hack-haven.com/pokemon-last-chance/

The public synopsis describes a region with three competing factions, side quests and choices whose consequences can backfire. The relevant reusable structure is not the faction identities or plot. It is the combination of local optional work with multiple organized actors who can interpret the same intervention differently and react according to their own interests.

Reusable structure for Ouros: completing a practical task for one institution can change access, obligations, expectations and information flow among other institutions without relying on a universal alignment meter. A beneficial repair can still create a new dependency. A rescue can strengthen one group's operational position. Refusing a task can leave another actor to solve it off-screen.

No Hiraeth setting, government conflict, armies, characters, romance system, battles or story events are imported.

## Ouros synthesis

A settlement can maintain one shared public board whose jobs originate from several institutions rather than one quest authority. The visible request is concrete: inspect a damaged crossing, recover survey equipment, escort a technician, verify a water source or document repeated Pokémon interference.

The deeper consequence comes from who performs the work and what evidence they produce. If a cooperative completes a repair, it may gain practical leverage because others now depend on its schedule. If a ranger team documents the cause first, later safety policy may be based on its evidence. If an independent resident solves the problem, institutions may have to negotiate with someone they previously ignored. These outcomes follow from world state and communication instead of an omniscient faction score.

The same job can remain alive when the player ignores it. Another NPC team may accept it, the problem may worsen, or the request may be withdrawn after conditions change. The world should preserve who knew the original request, who acted, what resource changed hands and which later claims are supported by provenance.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` remains a routing reference only. Potentially relevant families include Skills/Edges/Features, Researcher, Survivalist, Chronicler, movement/terrain, hazards/weather, encounter construction and Items/Gear. This research grants no Skill DC, Feature effect, faction bonus, reputation mechanic, carrying rule, weather effect, hazard rule or Item behavior.

## Engine dependency discipline

A reduced version can run through persistent obligations, public request state, NPC schedules, travel, communications, relationships, permissions, resource custody and evidence provenance. No AutoPTU battle is required.

A rich version involving a dangerous repair or rescue uses targeting/footprints/range/LoS and base movement only within verified scopes. Push/pull/knockback/interception/forced movement depend on complete movement. Timed repair windows and staged collapse depend on full turn/round lifecycle. Persistent injury depends on the full stateful damage pipeline. Complex conditions depend on status lifecycle. Weather, unstable terrain, hazards, zones and reactions depend on the exact terrain/weather/hazards/zones/reactions mechanics used. Move behavior, abilities, items and Trainer Features remain individually gated. Objective-aware NPC choices require AI tactical policy. Minecraft/Cobblemon/Craftics must not synthesize missing PTU rules or decide non-KO outcomes.

## Live engine evidence

AutoPTU-Java `main` was inspected at `0b03b2716141fe94c2fbf85fdca1ba4548d080a2`, merge PR #430, `Add reusable Ball Fetch approach Shift resolver`, dated 2026-09-10. The new resolver chooses a legal Shift destination that strictly reduces distance to a target using the already existing legal Shift destination resolver, plus the pinned Ball Fetch occupancy filter and deterministic tie-breaking. This strengthens one approach-movement policy used by Ball Fetch. It does not establish complete movement, forced movement, interception, switching, abilities as a family, action economy, lifecycle or AI tactical policy.

AutoPTU Python remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains presentation-only and explicitly states that battle rules and outcomes do not change.
