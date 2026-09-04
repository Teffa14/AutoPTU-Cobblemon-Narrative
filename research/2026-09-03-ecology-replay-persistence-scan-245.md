# Ecology replay and persistence scan — Pass 245

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Canon effect: NONE

## Question

How should Ouros preserve a persistent Pokémon and its ecological consequences across projection, observation, battle handoff, semantic return and server lifecycle without letting Minecraft entity state or a tactical engine become ecological authority?

## Repository context inspected

This pass was checked against the repository inventory and the active ecology directive, including `CURRENT_FOCUS.md`, `design/ecology-development-program.md`, canon files, existing ecology contracts, implementation fixtures, validators, tests and CI. The directly consumed implementation source is `implementation/marea-sendero-persistent-actor-cross-fixture-trace-v1.json`. Existing Fletchling identity and mechanical profile remain governed by `canon/marea-interior-first-wild-population-v1.md`.

## New public-source scan

### PTU campaign log: environmental cause behind visible Pokémon behaviour

Source: Reddit / r/PokemonTabletop, “campaign log #22” (2022)
https://www.reddit.com/r/PokemonTabletop/comments/ug8b7t

Reusable pattern: apparently nuisance-like Pokémon behaviour can be evidence of a deeper environmental problem. The useful structure is observation -> investigation -> environmental diagnosis -> intervention -> persistent world consequence. Ouros should preserve this chain without requiring combat at every stage.

No characters, dialogue, exact plot, town, festival or disease from the campaign is imported.

### PTU encounter-design discussion: wild Pokémon as environmental actors

Source: Reddit / r/PokemonTabletop, “Pokemon Encounters (A Storytelling)” (2023)
https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5

Reusable pattern: wild encounters become more memorable when Pokémon have a local reason to be present: feeding, nesting, territorial defense, contamination, social play, relocation pressure or curiosity. Watching can itself be a valid player action. This supports persistent actor history and non-combat outcomes.

No distinctive encounter, Pokémon combination or scene is copied into Ouros canon.

### Pokémon Mystery Dungeon: world problem -> local requests -> exploration

Source: Bulbapedia, Pokémon Mystery Dungeon: Red Rescue Team and Blue Rescue Team
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Mystery_Dungeon:_Red_Rescue_Team_and_Blue_Rescue_Team

Reusable pattern: a broad environmental imbalance can manifest through many local rescue/exploration problems. Ouros can similarly derive quests from persistent world state while keeping the quest surface separate from the source event.

The Mystery Dungeon story, characters and disaster plot are not imported.

### Event Sourcing: rebuild state from an ordered event history

Source: Martin Fowler, “Event Sourcing” (2005)
https://www.martinfowler.com/eaaDev/EventSourcing.html

Reusable engineering pattern: state can be reconstructed from a sequence of domain events. This is useful for Ouros because identity, demographic state, observation history, ecological pressure and AutoPTU semantic returns can be replayed without trusting a mutable Minecraft entity snapshot.

Ouros adaptation: the event log is ecological/narrative state only. It must never reproduce hidden PTU combat internally. AutoPTU enters the stream through explicit semantic result events.

### Retroactive events and replay

Source: Martin Fowler, “Retroactive Event”
https://martinfowler.com/eaaDev/RetroactiveEvent.html

Reusable engineering pattern: replay makes it possible to test or rebuild state after event-order or input corrections. Ouros should first require deterministic ordered replay before considering retroactive correction. This pass does not authorize rewriting canon history or production event logs.

## Transformed Ouros lessons

1. Persist the actor reference independently of any current Minecraft UUID.
2. Store ecological changes as semantic domain events rather than inferred presentation facts.
3. Treat AutoPTU output as a narrow semantic input to the ecology reducer; do not rerun PTU rules in Ouros.
4. Rebuild the same final ecological snapshot from the same ordered event sequence.
5. Preserve the distinction between player-visible evidence and hidden persistent identity/history.
6. A tactical KO can append encounter history and modify later avoidance without becoming mortality, capture or emigration.
7. Server restart clears transient presentation correlation but must preserve identity, history, event state and demographic truth.
8. A quest or battle may respond to an ecology event but cannot become the authority that creates or resolves that event.

## PTU/Caelo/Kairos boundary

PTU remains authoritative for structured tactical adjudication through AutoPTU. Caelo and Kairos remain comparative living-world sources under the project source-authority policy. This pass adds no PTU rules, Moves, Abilities, Items, Features, Edges or species facts.

## Canon classification

CANON-APPROVED references used unchanged:
- Marea/Sendero site identity already present in project canon.
- existing persistent Fletchling actor reference.
- existing Fletchling mechanical profile reference.

PROPOSED implementation only:
- deterministic ecology replay reducer.
- frozen replay final snapshot.
- replay-specific restart behaviour for transient Minecraft UUID correlation.

UNRESOLVED:
- production persistence storage format and transaction boundary.
- event schema versioning and migration policy.
- whether production logs are append-only or periodically compacted behind canonical snapshots.
- how late/out-of-order adapter observations should be handled.
- which additional AutoPTU semantic result types are stable enough to enter the production ecology event vocabulary.
