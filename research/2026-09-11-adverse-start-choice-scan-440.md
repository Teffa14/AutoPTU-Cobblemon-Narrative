# Adverse Start Choice Scan — Pass 440

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE

## Repository cross-check

The Narrative repository was inventoried before writing at `8140c65ee1dc65dadea86c9dc57fe673ef3bf431`. `CURRENT_FOCUS.md`, canon inventory, recent assistance passes, start-condition owner, viability owner, replanning surfaces, proposals and prior research anchors were checked. Exact-title searches found no previous research use of `Dead Rising` or the PTU thread `Advice to gm ptu` (`1lp99hf`). No canon file is changed by this pass.

The current architecture already separates accepted terms, pre-start viability evidence and `BLOCKED_AT_START` / `AT_RISK_AT_START`. The missing design question is what durable choice the commitment owner can make after that adverse start fact exists.

## Source A — Dead Rising timed cases and continued world play

Public sources:
- Dead Rising Wiki, `Cases (Dead Rising)`: https://dead-rising.fandom.com/wiki/Cases_(Dead_Rising)
- Wikipedia, `Dead Rising (video game)`: https://en.wikipedia.org/wiki/Dead_Rising_(video_game)

Reusable structure:

Dead Rising attaches explicit time windows to case progression. Missing a required case can close later case progression, yet the world does not simply cease to exist; the player can continue through the remaining time and other activity can still occur.

Ouros transformation:

A missed or blocked obligation should be able to change which future opportunities remain available without deleting the world, rewinding the promise or pretending the actor never committed. The useful pattern is consequence after a deadline, not Dead Rising's setting, characters, zombie premise, mall layout, missions, timers or ending structure.

For the immediate seam, the important lesson is smaller: reaching a deadline under adverse conditions should produce an explicit next choice and later consequence rather than an implicit reset.

## Source B — PTU GM discussion: objective can differ from victory

Public source:
- r/PokemonTabletop, `Advice to gm ptu`: https://www.reddit.com/r/PokemonTabletop/comments/1lp99hf/advice_to_gm_ptu/

A community response recommends structuring some gym tests around a specific objective, with an endurance example where success can mean lasting a number of rounds rather than defeating the opponent.

Reusable structure:

- encounter success criteria can be narrower than total victory;
- the scene's objective should be explicit before tactical resolution;
- an actor choosing to attempt fulfillment does not imply that the later encounter must resolve as `defeat all opponents`.

Ouros transformation:

If an assistance obligation begins while risky or blocked, `ATTEMPT_FULFILLMENT` means only that the responder chooses to try. A later structured scene might ask the party to reach an inspection marker, hold position, escort a specialist, protect equipment, retrieve one object or safely withdraw. Exact verbs remain gated by engine capability evidence.

No campaign setting, NPC, gym, dialogue or distinctive encounter is copied.

## Source C — PTU preparation discussion: route/ecology generators as preparation aids

Public source:
- r/PokemonTabletop, `Looking for Resources`: https://www.reddit.com/r/PokemonTabletop/comments/11j2p3l/looking_for_resources/

The thread points GMs toward route, encounter, site and fauna-generation resources and discusses using Pokémon lore/habitat information while preparing encounters.

Reusable structure:

World obstacles should be contextualized by route/site/ecology state rather than appearing solely because combat needs an arena.

Ouros transformation:

A blocker can remain a world fact independently from the response chosen at start. If the responder attempts fulfillment, route state, local ecology and permissions remain inputs to the next planner layer. The disposition owner does not invent a bypass or force a battle.

## Design synthesis

The reusable sequence is:

accepted obligation -> evidence of risk/blocker -> adverse start assessment -> responder choice -> separate execution/communication/consequence

The start choice needs durable identity because later actors may need to distinguish:

- the responder tried to honor the promise;
- the responder waited for conditions to improve;
- the responder sought new terms;
- the responder abandoned the obligation.

Those facts should not be inferred from an empty location, a missed timer or the absence of an AutoPTU encounter.

## Capability implications

The disposition record itself uses no battle capability family.

A rich follow-up can require any of the permanent categories depending on its exact objective. Current live evidence does not justify broad promotion. Targeting/footprints/range/LoS, base movement legality and core calculations remain verified only within audited scopes. Complete movement remains partial, especially push/pull/knockback/interception/forced movement. Action economy/initiative, full turn/round lifecycle, full stateful damage pipeline and status lifecycle remain partial. Terrain/weather/hazards/zones/reactions remains mixed/partial/blocking by exact mechanism. Move-specific behavior, abilities, items and Trainer Features/perks remain individually gated. AI legal-action infrastructure is not assumed for specialized inspect/escort/protect/retrieve/carry/extract verbs. AI tactical policy remains blocking for those specialized objectives. Minecraft/Cobblemon/Craftics support remains partial/blocking for specialized objective state, non-KO completion and in-flight recovery.

## Live engine evidence checked for this pass

AutoPTU-Java advanced to `dd5a6d342f8db202206f0becb7c6c30b7c3b67a4` (PR #448). The new runtime switch-trigger planning context derives Trainer Feature ownership, AP, active/fainted state, replacement candidates and handled-trigger guards from authoritative battle state. This strengthens one switch-trigger/Trainer Feature seam only. It does not verify the full action-economy, reactions, Trainer Features or general tactical-policy families.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its head is explicitly presentation-only and changes no battle rules or outcomes.
