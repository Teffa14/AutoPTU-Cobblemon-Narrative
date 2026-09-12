# Replacement Offer Delivery and Request-Network Scan — Pass 446

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Date: 2026-09-12

## Scope

This pass looked for structures that separate a request or offer from acceptance, execution and later acknowledgement, especially in Pokémon-adjacent quest systems and living-world RPG design. Existing Ouros research was searched first for the source names used below; no prior Mystery Dungeon, Archmage Rises or Pokémon World Tour United treatment was found.

No protected dialogue, named plot sequence or distinctive character was imported. The useful material is limited to high-level state transitions, temporal structure and encounter-design lessons.

## New public sources

### Pokémon Mystery Dungeon job/request structure

Bulbapedia documents that Mystery Dungeon jobs can appear on boards or in mail, enter a job list, and still require explicit acceptance before execution. The Friend Rescue flow is even more useful structurally: one party sends an SOS, another accepts and resolves it, then sends an A-OK response, with an optional later thank-you message.

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)
- https://bulbapedia.bulbagarden.net/wiki/Friend_Rescue
- https://bulbapedia.bulbagarden.net/wiki/Connection_Orb

Reusable lesson for Ouros: availability, receipt, acceptance, execution and acknowledgement can remain separate state transitions. A delivered replacement offer therefore should not create a replacement obligation by itself.

Additional useful pattern: Super Mystery Dungeon's Connection Orb represents requests attached to known social connections. This suggests that local work can emerge from persistent relationships while still needing a concrete request state rather than a universal quest flag.

Excluded material: Mystery Dungeon characters, named missions, dungeon layouts, reward tables, mail text and story progression.

### Archmage Rises quest-time design

A Game Developer article on Archmage Rises describes accepted quests as time-bearing commitments, distinguishes completion, quitting and failure after a due date, and notes that unresolved problems may later be handled by another actor while the world continues.

Source:
- https://www.gamedeveloper.com/design/rethinking-the-passage-of-time-in-rpgs

Reusable lesson for Ouros: a promise or offer should remain historically queryable even when its execution window passes, and downstream social consequences should consume explicit outcome evidence rather than be inferred from message transport.

Excluded material: game-specific relationship numbers, quest content, characters and exact consequence tuning.

### Pokémon World Tour United / PTU actual-play recommendation

A public Pokémon Tabletop community thread describes Pokémon World Tour United as a PTU actual play set in a recognisable Kanto whose locations have changed over time, with a recurring Team Rocket-associated character entering and leaving the party as circumstances permit.

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/oen7mx/

Reusable lesson for Ouros: familiar geography and recurring actors benefit from temporal continuity. A negotiation message can travel while locations and actor availability keep changing. A recurring NPC does not need to stay attached to the player party to remain narratively relevant.

Excluded material: named characters, specific Kanto alterations, plot beats and dialogue.

## Transformation into Ouros

Pass 445 created replacement terms only after explicit delivered consent to reopen. Pass 446 adds one further causal edge: responder-authored terms must travel to the requester through the existing information runtime. The requester may remain unaware during latency, channel failure or local acknowledgement waits.

This is deliberately narrower than a generic quest system. The world keeps its existing owners for schedule, travel, access, resources, private knowledge, relationship changes and tactical resolution.

## PTU / Caelo / Kairos cross-check

The repository's `sources/kairos/DRIVE_FOLDER_INVENTORY.md` was rechecked. It marks the current Kairos corebook, reference sheets and move/ability references as source candidates that still require rule-by-rule Ouros review; the inventory itself confers no canon or mechanics.

Pass 446 requires no PTU battle rule, Skill, Feature, Ability, Item, move, status, movement rule or species/form content. No Kairos mechanic was activated. If a later accepted proposal creates an encounter, exact mechanical dependencies must be checked against the relevant PTU/Kairos/Caelo source and current Java contract before authoring the rich behavior.

## Live read-only engine evidence

AutoPTU-Java head checked 2026-09-12: `f859888213385e313df923678b62374ac6919b22`, merged through PR #449, `Freeze Quick Switch side-effect order`. This is narrow evidence for one Quick Switch execution route. It does not verify action economy/initiative, reactions/interrupts or Trainer Features/perks as complete families.

AutoPTU Python head checked 2026-09-12: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest commit states that viewport-coordinate synchronization is presentation-only and changes no battle rules or outcomes.

## Capability posture for any rich continuation

Targeting/footprints/range/LoS: VERIFIED only in audited scopes.
Base movement legality: VERIFIED only in audited scopes.
Complete movement including push/pull/knockback/interception/forced movement: PARTIAL.
Core calculations: VERIFIED only in audited scopes.
Action economy/initiative: PARTIAL.
Full turn/round lifecycle: PARTIAL.
Full stateful damage pipeline: PARTIAL.
Status lifecycle: PARTIAL.
Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact behavior.
Move-specific behavior: individually gated.
Abilities: PARTIAL and individually gated.
Items: individually gated.
Trainer Features/perks: individually gated.
AI legal-action infrastructure: specialized objective verbs such as INSPECT, ESCORT, PROTECT, RETRIEVE, CARRY, BRACE, CONTAIN or EXTRACT require explicit admission.
AI tactical policy: BLOCKING for specialized objective policy until verified.
Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL / BLOCKING for specialized objective state, non-KO completion and interrupted structured-scene recovery.

## New design candidate

`The Offer Is Still on the Wire` is recorded separately as PROPOSED / NON-CANON.

Reduced version: replacement terms are authored, transmitted and eventually delivered through ordinary semantic-time communication. While the message is in transit, access, weather, local Pokémon activity, schedules and the underlying need may change. The requester decides only after actual receipt. No AutoPTU dependency.

Rich version: if accepted revised terms later require a hazardous survey, escort, protection task, retrieval, containment or extraction, build that scene from live world evidence at execution time. Do not pre-author weather phases, forced movement, reactions, statuses, Trainer Feature interrupts or specialized objective AI without verification of those exact capability families.

## Unresolved questions

The next durable owner should decide the delivered replacement offer without merging receipt and acceptance. It must evaluate expiry at decision time, preserve the old commitment, and distinguish acceptance from rejection. A later replacement-commitment owner should define when the old obligation ceases to be future-actionable while remaining historical evidence. Relationship/accountability consequences should consume explicit missed, abandoned, superseded or fulfilled outcomes rather than communication state.