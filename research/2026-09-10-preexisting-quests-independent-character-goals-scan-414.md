# Pre-existing Quests and Independent Character Goals — Research Scan 414

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-10

## Research question

How can Ouros make optional quest offers feel like discoveries inside a persistent world rather than buttons that create a problem only when the player accepts them?

This scan also asks how recurring NPCs can retain goals that continue beside the player's current objective without becoming scripted satellites.

## Duplicate-control check

The current repository tree, canon directory, recent research/proposals and Pass 411–413 session-recovery work were inspected before this scan was written.

Sources deliberately not reused as new anchors include recent recurring material such as Lethalmon, Pokémon Knowledge, Pokémon Crystal Inheritance, Pokémon Rollout episode 139, Pixelmon Kainite, A Farfetch'd Story 2, Pokémon Sky Blue, Pokémon Synthesis, Pokémon Resonance, Pokémon Last Chance, Tectonic, Monomyth and other already indexed project references.

Repository search found no prior use of `Pokemon Diadem` and no prior use of Reddit thread id `1qj7tkd`.

## Source A — Pokémon Diadem 2.0

Source: Eevee Expo release thread, April 26, 2026
https://eeveeexpo.com/threads/9464/

Public project material presents a story-focused fangame in which the protagonist travels with recurring characters who have reasons for moving through the world beyond simply following the protagonist. One childhood acquaintance pursues his own ambitions away from home, while another recurring traveler carries his own body of knowledge and role in the setting.

Reusable structure for Ouros:

- recurring characters can intersect with a player arc while still owning independent goals;
- a companion's next destination does not need to equal the player's next destination;
- separation and later reconvergence can produce changed knowledge, obligations and relationships;
- an NPC can bring information from work performed outside the player's camera if the persistent simulation actually gave that NPC the knowledge, time, route and opportunity to perform it.

Transformation boundary:

Ouros does not import Diadem's protagonist, missing-parent plot, islands, political structure, Crest Bearers, characters, dialogue, field effects, bosses or regional forms. The source contributes only a general character-arc structure.

## Source B — PokémonRMXP side-quest design discussion

Source: Reddit /r/PokemonRMXP, `Does anyone like my first side quest so far`, January 21–22, 2026
https://www.reddit.com/r/PokemonRMXP/comments/1qj7tkd/does_anyone_like_my_first_side_quest_so_far/

The useful community feedback is structural. Commenters ask whether the endangered Pokémon exists before the player talks to the quest-giving NPC, recommend making the situation visibly real before acceptance, and point out that an optional prompt should permit refusal rather than disguising a mandatory event as a choice.

Reusable structure for Ouros:

- quest acceptance should often subscribe the player to an existing world problem rather than create that problem;
- the visible condition can predate the journal entry;
- declining or delaying an optional request should leave the world free to continue through authored or simulated state transitions;
- a later return can reveal that the issue remains, changed, was handled by another actor, or became irrelevant;
- the quest log should record the player's commitment and known information, not act as the sole owner of world truth.

Transformation boundary:

Ouros does not import the thread's Noibat scenario, map, NPC, dialogue, battle implementation or proposed staging. The source contributes only optional-quest timing and affordance lessons.

## Combined design lesson

The two sources support a useful persistent-world rule:

`QUEST OFFER != WORLD EVENT CREATION`

A named NPC can recognize a problem, decide whether to ask for help, ask one or more eligible people, continue pursuing their own goals and revise the request when circumstances change. The player may accept, refuse, postpone or discover the issue independently.

This fits the existing Ouros architecture particularly well because global agents already have goals, schedules, obligations, private knowledge, travel, communication and event-driven replanning. The new narrative value comes from using those systems to separate four moments that conventional quest design often collapses:

1. the world condition begins;
2. an actor observes or learns about it;
3. an actor offers work or requests help;
4. the player accepts or declines involvement.

Those moments can occur in different orders and can involve different people.

## Ouros candidate extracted

Proposal written from this scan:

`proposals/2026-09-10-the-request-did-not-create-the-problem-pass-414.md`

Status remains PROPOSED / NON-CANON.

The candidate uses existing Marea institutions only as possible bindings. It creates no new canonical incident, NPC, faction, species, location or rule.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked. Campaign/session structure, encounter creation, recurring rivals/villains, movement, hazards, terrain/weather, Items and Trainer Features remain source-routing categories rather than automatic Ouros permission.

This scan adds no Skill DC, Edge, Feature, Item effect, Move behavior, Ability behavior, capture rule, terrain rule, weather rule, hazard rule, reaction rule or special battle completion condition.

The proposal's reduced implementation is intentionally world-level and does not require PTU adjudication unless a concrete action crosses the structured-mechanics boundary.

## Live AutoPTU evidence

AutoPTU-Java main inspected during this pass: `5ff41b03ffb960a66ecfe0b79080638ac4ac12d4`, merge PR #436, `Add generic switch post-entry dispatcher`, dated 2026-09-10.

The change strengthens a concrete switch post-entry dispatch seam under pinned oracle coverage. It does not establish durable engine-session lookup and does not make complete movement, action economy, turn lifecycle, Abilities, Items or Trainer Features complete families.

AutoPTU Python remains `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit remains explicitly presentation-only and says battle rules/outcomes do not change.

Both engine repositories were treated read-only.

## Permanent capability posture for the candidate

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.

Base movement legality: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.

Core calculations: VERIFIED only in audited scopes.

Action economy/initiative: PARTIAL.

Full turn/round lifecycle: PARTIAL.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism.

Move-specific behavior: individually gated.

Abilities: PARTIAL / individually gated.

Items: individually gated.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED only in audited ordinary scopes. Specialized rescue, escort, carry, inspect, manipulate or interact actions need explicit admission before a tactical version can use them.

AI tactical policy: BLOCKING for rescue-first, escort-first, preserve-evidence, objective-aware withdrawal and disengage-after-objective unless separately verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative non-KO tactical objectives, specialized interactables, durable tactical recovery and any presentation that would otherwise claim PTU truth.

## Research conclusion

Ouros can make optional content feel materially more alive by letting problems, observations, requests and commitments have separate persistent identities. This requires no new battle mechanic in the reduced form and uses the existing global world-agent architecture rather than a region-specific quest script.
