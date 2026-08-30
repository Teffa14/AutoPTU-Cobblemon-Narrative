# Recurring Companion, Guide & Mentor Continuity Scan — Pass 150

Status: RESEARCH / PROVENANCE ONLY. This document is not Ouros canon. Any candidate NPC, institution, location, custom practice, encounter or rule described here remains NON-CANON unless separately approved.

Date: 2026-08-30

## Research question

Ouros already has strong layers for social bonds, mentorship, journeys and expeditions, recurring rivals, actor autonomy and campaign convergence. The remaining gap is narrower: how should a recurring non-rival NPC participate alongside the player for a bounded part of a journey or adventure, leave for a causal reason, continue existing independently, and plausibly return later without becoming a permanent party slot, a GM-controlled protagonist, or an automatic tactical combatant?

This scan looks for reusable high-level structures around temporary companions, guides, mentors, specialists, reunion, departure and role change. It does not copy dialogue, scene prose, distinctive characters or full plots.

## Internal repository inspection

The complete Narrative repository tree was inspected before this pass. The recursive GitHub tree at Pass 149 head `f7c27693b44fa47eb313e075de1dda73507a4380` reported `truncated: false`. No Pass 150 file and no dedicated recurring-companion continuity extension existed.

Relevant existing owners were then read directly.

### `social-bonds-mentorship-clubs-layer.md`

This layer already owns relationship dimensions, mentorship direction, NPC memory, social absence, supporting-cast agency and relationship callbacks. It explicitly warns against inferring hidden emotion and treats absence as potentially dormant, distant, schedule-related or unresolved rather than automatic rejection.

Pass 150 must therefore not create a second friendship, trust, affection, mentorship-progression or social-memory model.

### `travel-transport-expedition-layer.md`

Travel already owns journey participants, expedition participants, role assignments, route knowledge, local-guide roles, crew availability, staging and extraction. Named crew remain characters rather than equipment slots.

Pass 150 must therefore not create a second travel graph, journey roster or expedition-role system. It can reference a journey or expedition and preserve why one recurring NPC participated in a bounded episode and how that episode ended.

### `world-agency-layer.md`

World Agency already owns autonomous NPC goals, resources, reach, actor knowledge and off-screen action. Supporting characters must remain agents who can be unavailable, busy, wrong or pursuing another objective.

Pass 150 must not make companions passive inventory attached to the player.

### `rivalry-recurring-peer-progression-extension.md`

Rivalry already owns recurring competitive history, independent peer agendas and plausible recontact. A rival may temporarily cooperate, but competitive continuity remains there.

Pass 150 should handle a rival only when the same actor also has a separately evidenced companion episode. It must not duplicate rivalry state.

### `campaign-arc-convergence-pressure-payoff-extension.md`

Campaign convergence already requires every returning actor to pass knowledge, reach, motivation, resource and availability checks. It explicitly rejects teleporting a familiar rival, mentor or faction leader into a finale for spectacle.

Pass 150 should reuse those checks for reunion eligibility rather than inventing a companion summon mechanic.

### `2026-08-18-source-scan.md`

The internal PTU/Caelo source scan records PTU support for central plots, character-centric arcs and sandbox play, and Caelo activity containers such as Social, Job, Raid, Contest, Gym and Dojo. No universal follower slot, generic companion AI, automatic NPC battle inclusion or generic mentor authority was identified there.

## Public Pokémon research

### Cheryl and Eterna Forest — bounded accompaniment

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Cheryl
- https://bulbapedia.bulbagarden.net/wiki/Eterna_Forest

Reusable structure:

A temporary partner can join because of a concrete local concern, accompany the protagonist only through a particular environment, and separate at an explicit route boundary. Eterna Forest also demonstrates temporary separation when the player exits in a way that does not complete the shared route.

Ouros transformation:

A companion episode should have a scope and an end condition. `travels_with_player` should not be a permanent character property. A guide may accompany one forest, one district, one cave level or one expedition leg, then remain a persistent NPC after the episode closes.

Do not import Cheryl, her dialogue, Chansey, Team Galactic events or Eterna Forest geography into Ouros.

### Riley and Iron Island — specialist participation with a destination boundary

Source:
- https://bulbapedia.bulbagarden.net/wiki/Iron_Island

Reusable structure:

A recurring-capable NPC can offer to travel through a bounded section, provide assistance while that local objective remains active, then leave when a physical destination or task boundary is reached.

Ouros transformation:

The episode can be keyed to `scope_end_location`, `shared_objective_completed`, `role_no_longer_needed` or another world-state fact. Departure does not require interpersonal conflict.

Do not import Riley, Lucario, Iron Island plot content or reward structure.

### Stat Trainers — personal goals can end shared travel

Source:
- https://bulbapedia.bulbagarden.net/wiki/Stat_Trainers

Reusable structure:

Temporary partners have their own reasons for being present. When the NPC's personal objective is satisfied, the shared route can end even if the protagonist continues elsewhere.

Ouros transformation:

Companion presence should depend on the actor's agenda. A shared goal may overlap only partially with the player's goal. `shared_goal != shared_loyalty` and `shared_route != permanent_party`.

### Scarlet/Violet Area Zero — temporary ensemble convergence and role splitting

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Area_Zero
- https://bulbapedia.bulbagarden.net/wiki/The_Way_Home

Reusable structure:

Previously independent recurring characters can form a temporary expedition group for one major location and then split roles at a local boundary. The ensemble matters because each character arrives from prior state, not because the narrative permanently merges them into one party.

Ouros transformation:

A convergence may instantiate several companion episodes that overlap in time. Presence can then diverge by scene: one NPC remains at an access point, another continues to the next node, another leaves because their role is complete. This should be represented through explicit episode state and current world location.

Do not import Area Zero, its characters, revelations, facilities or encounter sequence.

## Public PTU/community research

### Long-form character-focused PTU campaign

Source:
- https://startplaying.games/adventure/cm4sf8asu000611fuo3rv1ewj

The public campaign description for `Pokémon Tabletop United: The Social Ecology of Kanto` describes a long-running character-focused PTU campaign built around mystery, camaraderie, battles and personal subplots over a large number of sessions.

Reusable lesson:

Long-running PTU play can sustain recurring character relationships and personal subplots alongside battle and exploration. A recurring support character therefore benefits from durable state and independent goals rather than one-off quest scripting.

Use boundary:

This is community design evidence, not PTU rules authority. No setting facts, characters, encounter details or house rules are imported.

## General RPG / game-design research

### NPC allies and player agency

Source:
- https://thealexandrian.net/wordpress/40349/roleplaying-games/ptolus-running-the-campaign-npc-allies

Reusable lesson:

A recurring NPC ally can easily become a spotlight or decision-making problem when the NPC starts functioning like a GM-owned player character. The useful design constraint is to keep the NPC's role bounded and avoid making the companion the route through which the world tells players what decision to make.

Ouros transformation:

A companion may provide information that the actor plausibly knows, perform a role they are actually qualified and available to perform, or pursue their own agenda. They do not become an oracle for the intended plot solution.

### Escort design and unsupported mechanics

Source:
- https://www.gamedeveloper.com/design/can-we-fix-escort-mission-game-design-

Reusable lesson:

Escort scenarios become frustrating when a game asks its existing mechanics to support protection and follower behavior they were not designed to execute reliably. Companion AI, pace, survivability and objective behavior need explicit support rather than assumptions.

Ouros transformation:

A narrative concept that requires escort behavior must declare complete-movement, lifecycle, reaction and tactical-policy dependencies as applicable. Until those are verified, use a reduced contract where the semantic NPC leaves BattleSpec before initiative and the battle only clears an approach or withdrawal route.

## Cross-check against PTU / Caelo material available to the project

The governing internal source scan supports social play, character arcs, jobs, expeditions and varied campaign structures. It does not establish any of the following as universal rules:

- an NPC companion slot;
- a permanent follower roster;
- automatic battle participation for an NPC who travels with the party;
- a generic ally AI package;
- automatic obedience to the player;
- universal escort movement;
- generic companion HP protection rules beyond ordinary governed combat state;
- automatic information sharing among co-travelers;
- a universal mentor bonus;
- a generic mentor progression reward;
- a universal loyalty threshold for joining or leaving;
- a generic Skill Check that forces an NPC to accompany the player.

All remain UNKNOWN until exact PTU/Caelo evidence or an approved Ouros rule establishes them.

## Reusable structural findings

A useful companion model needs at least four independent questions.

First, relationship: what social or mentorship relationship exists? Existing Social Bonds owns this.

Second, world agency: what does the NPC currently want, know and have capacity to do? World Agency owns this.

Third, travel/activity participation: is the NPC actually part of the current journey, expedition or scene? Travel and owning activity systems control this fact.

Fourth, recurring episode continuity: why did this NPC join this bounded stretch, what role did they have, what event ended that participation, and under what current conditions might another episode become plausible? Pass 150 can own this fourth question.

## Candidate invariants

The following are design guards, not PTU mechanics:

- `TRAVELS_WITH_PARTY != COMBATANT`
- `PRESENT_IN_SCENE != PRESENT_IN_BATTLESPEC`
- `FRIEND != AVAILABLE`
- `AVAILABLE != WILLING`
- `WILLING != ABLE_TO_REACH`
- `LEFT_PARTY != RELATIONSHIP_BROKEN`
- `DEPARTURE_EVENT != DISAPPEARANCE`
- `RETURNED != SAME_ROLE`
- `SAME_NPC_RETURNED != SAME_KNOWLEDGE_STATE`
- `SHARED_GOAL != SHARED_LOYALTY`
- `MENTOR != AUTHORITY`
- `ABSENT != INACTIVE`
- `REUNION_EXPECTED != REUNION_GUARANTEED`
- `SUPPORTS_PLAYER != OBEYS_PLAYER`
- `JOINED_FOR_ONE_JOURNEY != PERMANENT_PARTY_MEMBER`

## Encounter dependency implications

Companion stories can remain implementation-light when companionship is represented outside tactical state. They become mechanically rich when the player must escort, protect, coordinate with, extract or withdraw alongside the NPC during combat.

Typical full-version dependencies include:

- targeting/footprints/range/LoS for explicit tactical relationships;
- base movement legality for ordinary movement;
- complete movement including push/pull/knockback/interception/forced movement for escort body positioning, interception and forced displacement;
- full turn/round lifecycle for timed extraction, arrival, reinforcement or withdrawal windows;
- terrain/weather/hazards/zones/reactions for danger areas and protection reactions;
- AI legal-action infrastructure for legal NPC actions;
- AI tactical policy for objective-aware protection, withdrawal and coordinated movement;
- Minecraft/Cobblemon/Craftics adapter/playback for authoritative presentation of tactical departure or arrival.

Reduced versions should remove the companion from BattleSpec before initiative and restrict AutoPTU to a static explicit combatant set.

## Live engine evidence observed during this pass

AutoPTU-Java `main` was observed at:

`c5b2a34ff23887770268bfe4108dfc86e9a796fb`

Commit: `Compose Intercept position from server-owned Shift legality (#288)`.

The new runtime resolver composes Intercept line geometry with legal Shift destinations from authoritative `BattleRuntimeState`. The adapter is not allowed to select the intercept destination. Tests cover remaining in the current position when already on the attack line, choosing the nearest reachable attack-line tile from server-owned legal Shift destinations and returning no position when the line is unreachable.

This is strong localized evidence for server ownership of another Intercept/Shift-legality slice. It does not verify universal escort movement, all Push/Pull/Knockback sources, all forced movement, generalized reactions, objective-aware companion movement or tactical AI.

AutoPTU `main` remained at:

`729bae2d424963ff9bb3f4159c9a7ac9152128a7`

Its latest commit remains presentation-only and explicitly says battle rules and outcomes do not change.

## Research conclusion

The strongest reusable pattern is not a universal follower system. It is an event-sourced series of bounded participation episodes around persistent NPCs.

A character can accompany the player for one segment, leave because their local objective or obligation ends, continue acting elsewhere, and later return under a different role. Relationship state, world agency, travel state and battle authority remain with their existing owners.

This gives Ouros durable companions without converting NPCs into inventory, without forcing a permanent party, and without asking Minecraft/Cobblemon to invent escort or combat rules that AutoPTU has not verified.