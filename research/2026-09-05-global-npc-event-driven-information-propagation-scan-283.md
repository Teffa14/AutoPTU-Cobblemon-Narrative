# Research Scan — Global NPC Event-Driven Information Propagation — Pass 283

Status: RESEARCH / PROVENANCE ONLY. NOT OUROS CANON.
Date: 2026-09-05

## Question

How can Ouros let information move through a large persistent NPC cast with believable delay, selective contact and provenance, without global tick scans or faction hive minds?

## Existing project baseline checked first

Pass 282 already owns per-agent claim ledgers, report attenuation, provenance roots, contradictory evidence and direct communication. Pass 280 already states that faction membership does not imply shared private knowledge. Pass 279/281 already use semantic time and off-screen world-agent progression. This pass therefore adds transport/scheduling only and does not duplicate belief logic.

`design/ouros-source-authority-and-species-policy.md` remains binding: external rules and patterns are evidence/inspiration only until explicitly adopted. No PTU/Caelo/Kairos combat rule is introduced here.

## New public sources

### SimPy core documentation — discrete-event scheduling
Source: SimPy 3.0.12 core documentation, `simpy.core`.
URL: https://simpy.readthedocs.io/en/3.0.12/api_reference/simpy.core.html

Reusable pattern: a simulation environment can maintain virtual time, schedule events with delays and process events when due. Ouros uses only this general architecture lesson. It does not adopt SimPy as a runtime dependency.

Ouros transformation: communication becomes semantic-time work queued by delivery minute. A large cast does not require every NPC to poll for every possible conversation on every Minecraft tick.

### Perrie & Li (2014) — Building a Dynamic Social Community with Non Playable Characters
Source: IEICE Transactions on Information and Systems E97.D(8), 1965–1973.
URL: https://www.jstage.jst.go.jp/article/transinf/E97.D/8/E97.D_1965/_article/

Reusable pattern: believable NPC gossip can be constrained by contact, willingness/status and long-term relationships instead of giving all agents all information.

Ouros transformation: the transport contract expects explicit sender/receiver/channel opportunities. Relationship and role systems may later decide who is eligible to receive a message. The information network itself never broadcasts because two actors share a faction.

### Kempe, Kleinberg & Tardos — Maximizing the Spread of Influence through a Social Network
Source: Cornell-hosted paper.
URL: https://www.cs.cornell.edu/~eva/diffuse.pdf

Reusable pattern: information/influence diffusion can be reasoned about as propagation through a network rather than a global instantaneous state change.

Ouros transformation: the project uses explicit communication paths and event delivery. It does not adopt independent-cascade probabilities as literal human behavior, and it does not equate influence/adoption with belief truth.

### Enßlin, Kainz & Böhm — A Reputation Game Simulation: Emergent Social Phenomena from Information Theory
Source: arXiv:2106.05414.
URL: https://arxiv.org/abs/2106.05414

Reusable pattern: repeated social communication under bounded information can generate distorted group-level outcomes. This is useful evidence against treating repeated hearsay as perfect shared knowledge.

Ouros transformation: Pass 283 preserves provenance roots through relays. Multiple paths carrying one root cannot inflate independent-source count. Deliberate deception, memory compression and opinion dynamics remain future work.

### Pokémon Tabletop community — expedition knowledge as differentiated NPC/player role
Source: r/PokemonTabletop, “Looking for players for a new campaign,” 2023.
URL: https://www.reddit.com/r/PokemonTabletop/comments/16tt7ux

Reusable pattern only: the campaign premise assigns value to characters who possess knowledge unavailable to an isolated population, showing that unequal access to outside information can itself be a meaningful Pokémon-tabletop adventure resource.

Ouros transformation: knowledge access can differentiate agents and create quest pressure. No setting, plot, characters or protected text from the campaign are copied.

### GM rumor-design community — rumor usefulness depends on source context
Source: r/DMAcademy, “How to use NPC rumours to seed hooks and generate intrigue without giving the plot away too early,” 2022.
URL: https://www.reddit.com/r/DMAcademy/comments/x3egdv

Reusable pattern: rumors become interesting when the source and the receiver's assessment of that source matter.

Ouros transformation: Pass 280 trust can affect Pass 282 report confidence, while Pass 283 preserves who transmitted what and when. The scheduler itself does not declare a rumor true.

## Design lessons adopted as proposals

- Process due communication events instead of scanning every NPC each tick.
- Keep transport, provenance and belief as separate layers.
- Make delay and channel availability world facts.
- Preserve source roots across relays.
- Treat repeated hearsay from one root as one evidentiary root.
- Require explicit recipients; organizations do not share memory automatically.
- Trigger replanning only for agents affected by delivered events.
- Keep local visible conversation behind an adapter acknowledgement boundary.

## Ideas intentionally not adopted

- automatic probabilistic viral spread;
- social-media-style universal feeds;
- repeated exposure becoming truth;
- faction-wide memory pools;
- LLM-generated claims becoming world state;
- automatic mutation of message content;
- any source-specific Pokémon plot, faction, NPC or dialogue.

## Narrative opportunities

The system supports original Ouros structures such as a warning that reaches one settlement before another, a rival acting on stale information, several witnesses repeating one source, a genuinely independent second report changing confidence, a communication outage changing who attends an event, or an investigation where the player traces a story back through its transmission chain.

These are candidates, not canon events.
