# Pass 286 Research — Durable Bounded NPC Communication Runtime

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-05
Canon effect: none by itself.

## Research question

How should a persistent-world NPC system route selected recipients into actual communication events while remaining deterministic, restart-safe and bounded under burst load?

## New public sources reviewed

### Cutumisu & Szafron — Behavior Multi-Queues, AIIDE 2009
Source: https://ojs.aaai.org/index.php/AIIDE/article/view/12350

Reusable structure:
- queue-based game behavior can remain responsive while behaviors are interrupted and resumed;
- role/behavior decomposition avoids one monolithic control loop.

Ouros transformation:
- communication work is queued and can be deferred across bounded processing cycles;
- world-agent behavior does not require all due work to execute in one frame.

No implementation code, characters or authored game content was copied.

### eSPICE — load shedding in complex event processing
Source: https://arxiv.org/abs/2002.05896

Reusable structure:
- event systems can receive input faster than they can process it;
- overload therefore needs explicit policy tied to event importance and latency rather than accidental unbounded work.

Ouros transformation:
- Pass 286 exposes a processing budget and backlog count;
- for private NPC communication, the conservative initial policy is defer instead of drop;
- later public/broadcast channels may define separate coalescing or shedding rules, but they must be explicit because dropping information changes narrative causality.

The paper's probabilistic algorithm is not adopted.

### Nexosim / Days discrete-event architecture notes
Source: https://days.sh/docs/internals/nexosim

Reusable structure:
- actor-like models communicate through mailboxes/ports while a scheduler advances discrete simulation time.

Ouros transformation:
- selected NPC recipients receive explicit envelopes;
- semantic time and delivery queues remain separate from Minecraft render ticks.

No library dependency is introduced.

### Pokémon Mystery Dungeon: Rescue Team DX official world page
Source: https://mysterydungeon.pokemon.com/pt-pt/world/

Reusable high-level narrative structure:
- requests can enter play through different communication surfaces, including a public bulletin board and direct mailbox delivery;
- the communication surface affects how a request reaches the player without requiring the underlying need to be identical.

Ouros transformation:
- future public boards/publications should be explicit channel types with different audience expansion and persistence semantics;
- they should not be simulated by sending thousands of private messages.

No request text, characters, locations or plot beats are copied into Ouros.

### Bulbapedia — Mystery Dungeon jobs overview
Source: https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)

Reusable structure:
- job surfaces have bounded visible/accepted capacity and can refresh independently of the existence of the underlying world need.

Ouros transformation:
- bounded communication surfaces can expose a manageable subset of world information while preserving the underlying persistent state;
- this supports a future distinction between private delivery queues and public information surfaces.

Specific game limits are not adopted as Ouros rules.

## PTU / Caelo / Kairos cross-check

No PTU combat rule is required to model message scheduling, audience routing or delivery backlog.

No Caelo or Kairos mechanic is adopted. Existing project authority remains controlling:
`SOURCE_HAS_RULE != OUROS_USES_RULE`.

Communication budgets, queue persistence and channel-selection ordering are Ouros MMO simulation policy, not PTU Actions, Skill Checks, Features or combat timing.

## Design lessons carried forward

1. Explicit receiver routing must remain separate from public/broadcast audience expansion.
2. Backpressure must preserve causality by default; private messages are deferred rather than silently discarded.
3. Semantic-time queues must survive restart without early or duplicate delivery.
4. A communication surface is a world system with its own capacity and retention rules, not merely presentation flavor.
5. Local Minecraft acknowledgement remains a presentation boundary; visible proximity alone cannot create knowledge.

## Rejected shortcuts

- faction-wide automatic broadcast;
- delivering every due message in one server tick regardless of load;
- silently dropping private messages under pressure;
- using Minecraft chunk presence as delivery authority;
- using tactical AutoPTU AI to decide ordinary communication;
- copying Mystery Dungeon job-board limits or mission content as Ouros canon.
