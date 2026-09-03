# Environmental obstacles and multi-solution exploration scan — pass 217

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-03

## Why this pass exists

The repository already contains strong layers for route records, survey/cartography, incident restrictions, temporal ecology, wild behavior, alarm propagation, abandoned sites, stewardship and persistent observations. The remaining exploration gap is how a physical obstruction or difficult passage becomes gameplay without reducing every route or dungeon to one prescribed key, one Move name or one binary skill check.

This pass treats an obstacle as a world condition with observable affordances, consequences and several potentially valid responses. Exact mechanical authority still comes from PTU/Caelo/Kairos and AutoPTU. Minecraft/Cobblemon presents the physical world and performs only state transitions that the authoritative layer has approved.

## Public research reviewed

### Pokémon Ranger — Pokémon capabilities can have concrete overworld utility

The Pokémon Ranger series gives Pokémon explicit Field Moves for overworld interaction. Tackle can move heavy obstacles and knock over dead trees; Crush can break physical barriers; Tunnel can interact with soft soil; Area Moves such as Elevate or Swim can open traversal through particular spatial situations. Some targets in later Ranger games can require several Pokémon contributing compatible Field Moves.

Reusable Ouros lesson: Pokémon capabilities should matter outside battle, and cooperative environmental work can be meaningful. The Ranger implementation itself is too rigid for Ouros when it says an obstacle has one required Field Move and level. Ouros should retain the capability-to-environment relationship while allowing any solution whose exact PTU/world prerequisites are actually satisfied.

Sources:
- Bulbapedia, Field Move / Target Clear: https://bulbapedia.bulbagarden.net/wiki/Target_Clear
- Bulbapedia, Obstacle: https://bulbapedia.bulbagarden.net/wiki/Obstacle
- Bulbapedia, Tackle (Field Move): https://bulbapedia.bulbagarden.net/wiki/Tackle_(Field_Move)
- Bulbapedia, Crush (Field Move): https://bulbapedia.bulbagarden.net/wiki/Crush_(Field_Move)
- Bulbapedia, Tunnel (Field Move): https://bulbapedia.bulbagarden.net/wiki/Tunnel_(Field_Move)

### Non-linear dungeon topology — the route itself can support decisions

Justin Alexander's discussion of Jaquays-style dungeon design emphasizes multiple entrances, loops, vertical connections, secret/unusual routes and connections that skip levels. The value is not merely replayability: players can retreat, circle around, investigate a different route or approach the same destination from another direction.

Reusable Ouros lesson: an obstacle should often alter route choice rather than freeze progress. A blocked crossing can make a detour, higher ledge, maintenance route, temporary wait, negotiated access or later return meaningful. When every obstacle has a single compulsory solution, Pokémon capability diversity and world persistence matter less.

Sources:
- The Alexandrian, Xandering the Dungeon: https://thealexandrian.net/wordpress/13085/roleplaying-games/xandering-the-dungeon
- The Alexandrian, Xandering the Dungeon Part 2: https://thealexandrian.net/wordpress/13103/roleplaying-games/xandering-the-dungeon-part-2-xandering-techniques

### PTU 1.05 — traversal already belongs to character capability, not only Moves

Public PTU 1.05 reference material describes Acrobatics checks for precise movement such as balancing on perilous ledges and jumping across slippery stones, and Athletics checks for exertion such as climbing, jumping, long travel and carrying heavy loads. Terrain-oriented Features can further change what a Trainer can safely do in specific environments.

Reusable Ouros lesson: the solution space must include Trainer capability where the rules permit it. A player who can physically traverse an obstruction may solve their own access problem even if they cannot restore the route for cargo, NPCs, other Trainers or wildlife.

Sources:
- PTU skills reference: https://pturpg.wikidot.com/skills
- Public PTU 1.05 scan, relevant class/terrain material: https://anyflip.com/tcye/paot/basic/151-200

These public references are discovery/provenance aids. Exact Ouros mechanics must still be checked against the project's supplied PTU/Caelo/Kairos source set before canon approval.

### PTU community exploration — routes benefit from optional exploration

Public PTU GM discussion about travel between towns often treats the main route as a well-travelled path while allowing players to leave it, investigate explorable areas and choose whether to engage with planned encounters. This is weaker evidence than rules text but useful campaign-design feedback.

Reusable Ouros lesson: route obstructions should create choices and information, not automatically force a combat encounter or a single sequence of rooms.

Source:
- r/PokemonTabletop, “Question for Exploration” (2024): https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9/question_for_exploration/

## Derived structures for Ouros

### `OBSTACLE_STATE`

PROPOSED / NOT CANON-APPROVED.

```yaml
obstacle_state:
  obstacle_id: null
  site_ref: null
  physical_description: null
  authoritative_state: UNKNOWN | PRESENT | PARTIALLY_CLEARED | BYPASSED | STABILIZED | CLEARED | RESTRICTED
  provenance_refs: []
  observed_affordances: []
  access_effects: []
  evidence_refs: []
  hazard_refs: []
  persistence_policy: null
  public_route_status_ref: null
  last_transition_ref: null
```

`observed_affordances` are statements about the physical situation: climbable surface, gap, loose material, movable load, alternate ledge, water passage, damaged fixture, narrow opening, shelterable interval. They do not themselves authorize a Skill, Move, Ability, Feature, Item or mechanical result.

### `TRAVERSAL_OR_CLEARANCE_ATTEMPT`

PROPOSED / NOT CANON-APPROVED.

```yaml
traversal_or_clearance_attempt:
  attempt_id: null
  obstacle_ref: null
  actor_refs: []
  intent: BYPASS | CROSS | INSPECT | STABILIZE | CLEAR | REPAIR | PRESERVE_EVIDENCE | OPEN_FOR_OTHERS | WITHDRAW
  proposed_method: null
  mechanical_authority_refs: []
  required_world_preconditions: []
  verified_legal: false
  resolution_ref: null
  world_transition_ref: null
  consequence_refs: []
  provenance_refs: []
```

The record separates a proposed method from a legal method. Seeing a boulder and owning a strong Pokémon does not automatically authorize a Strength-equivalent effect. The relevant PTU capability, Skill, Move, Ability, Feature, Item or authored world mechanism must be verified first.

## Design rules derived from this research

An obstacle should describe a problem in the world before it describes a solution. Authoring `fallen material blocks the cart-width route while a narrow upper ledge remains reachable` creates several possible approaches. Authoring `requires Move X` collapses the scene before the player's team, Trainer build or observations matter.

Personal traversal and route restoration are different outcomes. Flying, climbing or jumping across can solve access for one actor while the public crossing remains unusable to Lia's deliveries, injured people, carts or another Trainer without the same capability.

Destructive clearance can have information costs. Moving debris, cutting vegetation, draining water or breaking a fixture may erase tracks, alter a wild shelter, destroy a survey reference or remove evidence relevant to a prior incident. The player should sometimes decide whether to document first, preserve part of the site or accept the information loss.

Waiting can be a legitimate method. A temporary condition may become passable after an authored world transition, maintenance action, weather change already owned by the world layer or scheduled reopening. Waiting never guarantees that an unverified hazard disappears.

Cooperation can be real without creating a generic teamwork bonus. Several Pokémon or Trainers may contribute only when their individual actions and the combined transition have explicit rules/world authority.

Minecraft block state cannot decide PTU success. Blocks, particles, animation and entity motion represent the result after authority resolves the attempt. The adapter must not infer that breaking a Minecraft block means a Trainer passed an Athletics check or that a Pokémon successfully used a Move.

## Canon cross-check

CANON-APPROVED constraints preserved:

- Sendero del Vidrio and its seasonal crossing remain established Marea anchors.
- Existing route checks, access restrictions, ecological observations and incident records retain their own provenance and authority.
- Existing persistent Pokémon identities and frozen battle blueprints are unchanged.
- AutoPTU remains mechanical authority when a proposed solution invokes PTU battle or rules behavior.
- Cobblemon/Minecraft may own ordinary overworld presentation and native world capabilities where already adopted by the project, without becoming PTU battle-state authority.

PROPOSED:

- `OBSTACLE_STATE`;
- `TRAVERSAL_OR_CLEARANCE_ATTEMPT`;
- distinction between personal bypass and route restoration;
- evidence-preserving versus destructive clearance consequences;
- multi-solution obstacle authoring.

UNCERTAIN / deliberately unresolved:

- exact PTU/Caelo/Kairos rules for lifting/pushing environmental objects outside battle;
- which Pokémon movement capabilities can directly satisfy which overworld traversal affordances;
- exact Skill DCs or opposed checks for specific Sendero obstacles;
- Features/Edges that substitute or enhance Athletics/Acrobatics/Survival in the current project ruleset;
- whether any Move/Ability can legally alter a specific world obstacle without a BattleSpec;
- exact Minecraft/Craftics contract for persistent block-world mutation and rollback.

## Anti-patterns

Do not create `requires Cut`, `requires Strength`, `requires Water Pokémon` or equivalent single-key locks unless a specific authored device truly has only that interaction and the mechanical source proves it.

Do not grant a Pokémon environmental powers from species aesthetics alone.

Do not turn every obstruction into difficult terrain, a hazard, damage or a battle.

Do not let a successful personal crossing silently reopen a public route.

Do not destroy investigative/ecological evidence automatically when the player chooses clearance.

Do not make Minecraft redstone, block hardness or client collision the final authority for a PTU Skill/Move/Ability outcome.

## Mechanical dependency boundary

A reduced obstacle scene can operate mostly in world-state space: observe the physical condition, choose a detour/wait/report/document option, use ordinary verified base traversal where legal, persist the outcome and render it in Minecraft.

A rich clearance scene can touch targeting/range/LoS, base movement, complete movement when pushing/pulling/interception/forced movement is real, core calculations for verified Skills, action economy if timing becomes structured, damage/status for actual consequences, terrain/hazards/reactions for dangerous tiles or triggers, individual Move/Ability/Item behavior, Trainer Features/perks, AI legal actions and tactical policy for autonomous helpers, and adapter/playback for the world transition.

The new AutoPTU-Java #329 tile-entry trap contract is relevant evidence for one bounded hazard path. It does not prove arbitrary environmental traps, moving obstacles, unstable terrain, zones, reactions or the whole hazard family.

## Research outcome

Ouros can make exploration depend on who the Trainer and Pokémon actually are without rebuilding the old HM gate pattern. The authored object should expose physical facts and consequences. PTU/Caelo/Kairos determines what participants can attempt mechanically, world state determines what changed, and Minecraft makes that transition tangible.