# Coherent Recovery and Distributed Expedition Scan — Pass 391

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-09

## Repository inspection and duplicate avoidance

The current recursive repository tree, `CURRENT_FOCUS.md`, current canon governance, the Pass 382 V19 action-interruption checkpoint, Pass 387 persistent-evidence boundary, Pass 389 portable-find binding work and Pass 390 V2 evidence checkpoint were inspected before writing.

The research corpus was searched for the candidate names and themes used in this pass. Pokémon Xenoverse had no repository match. The PTU haunted-mansion campaign-log episode identified below had no match under its distinctive episode terms. Recovery-manifest/event-sourcing terms also produced no existing narrative-repository research result.

Recent archaeology sources and repeatedly processed fan-game anchors from Passes 383–390 were not reused.

## Source 1 — Apache Flink consistent distributed checkpoints

Sources:
- https://nightlies.apache.org/flink/flink-docs-stable/docs/learn-flink/fault_tolerance/
- https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/stateful-stream-processing/

High-level reusable structure:

Flink treats a checkpoint as a globally consistent image assembled from multiple stateful operators. Its checkpoint barriers separate events that belong before a snapshot from events that belong after it. An operator with multiple inputs aligns those boundaries rather than mixing state from different checkpoint generations.

Ouros transformation:

Independent recovery owners may each be internally valid while still representing incompatible semantic moments. A higher-level recovery selector should bind exact owner generations at one semantic boundary rather than choosing the latest available file from each subsystem independently.

Applied lesson:

`INDIVIDUALLY_VALID != GLOBALLY_COHERENT`

The Pass 391 manifest records exact digests and one semantic minute. It does not copy or replace the state owned by V19 or persistent-world-evidence V2.

No Flink code, barrier implementation or exactly-once claim is imported into Ouros.

## Source 2 — Event sourcing snapshot/replay discipline

Source:
- https://wow.ahoo.me/guide/domain/event-sourcing.html

High-level reusable structure:

The source distinguishes authoritative event history from snapshots used for recovery/load acceleration. It also stresses deterministic reconstruction and warns against using a later snapshot when reconstructing an earlier historical point.

Ouros transformation:

A recovery manifest should identify which checkpoint generation belongs to the selected world moment. It should not reinterpret current downstream state to invent what an older checkpoint must have contained.

This reinforces the existing Ouros rule used in Passes 382, 387 and 390: migration may create an explicitly empty newer ledger, but it must not infer historical provenance from present consequences.

No external event-sourcing framework, persistence backend or schema-upcasting implementation is imported.

## Source 3 — PTU campaign log: haunted-mansion exploration loop

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5

High-level reusable structures observed in the public campaign summary:

- one contained location supports a sequence of rooms with different interaction types;
- environmental clues and a riddle interrupt combat cadence;
- some spaces contain optional fights while others contain navigation or discovery;
- blocked access creates a reason to explore elsewhere before returning;
- player actions can physically alter the location rather than treating rooms as immutable backdrops.

Ouros transformation:

A ruin or emergency site can progress through exploration state, evidence discovery and access changes without requiring every room to be a battle. If the physical site changes while named NPCs are simultaneously travelling, reporting or evacuating, restart recovery must preserve a coherent combination of those histories.

Do not import the mansion, room order, riddle, Pokémon roster, characters, weapons, dialogue or encounter outcomes.

## Source 4 — Pokémon Xenoverse: layered personal and regional mystery

Source:
- https://playpile.gg/games/pokemon-xenoverse-per-aspera-ad-astra

High-level reusable structure:

The public description links a personal search with a broader regional anomaly. Environmental puzzles and exploration sit inside that larger mystery rather than operating as disconnected filler.

Ouros transformation:

A local site incident can matter simultaneously to one NPC's personal obligation, an institutional evidence trail and a wider regional investigation. The systems should preserve those perspectives as separate records that can later converge.

Do not import Eldiw, X Species, Team Dimension, interdimensional lore, named characters, family plot, locations, monsters or story resolution.

## Source 5 — PTU sandbox campaign framing

Source:
- https://startplaying.games/adventure/cmel0c8lm000dju04x52bfz7o

High-level reusable structure:

The public campaign pitch emphasizes regional mysteries, exploration and player-selected paths inside a sandbox rather than one mandatory linear chain.

Ouros transformation:

A persistent-world incident should leave several valid follow-up routes. Players may investigate the site, find the missing report, follow a custody trail, interview an NPC or ignore the incident until later consequences make it relevant. Recovery architecture should preserve those unresolved branches instead of collapsing them into one scripted quest state.

Do not import the region, NPCs, paid-game framing, campaign-specific mysteries or plot material.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was reviewed as a router only.

Relevant source families remain:

- campaign/session structure around p. 449+;
- encounter creation around p. 470+;
- recurring rivals/villains around p. 477;
- boss encounters around p. 485+;
- movement/terrain around p. 382+;
- hazards around p. 401;
- terrain/weather around p. 404+;
- utility classes such as Researcher, Chronicler, Librarian, Paleontologist and Topographer.

These references do not authorize new Skills, Features, hazards, excavation actions, puzzle checks, Items or battle effects for Ouros.

## Design synthesis

The strongest combined pattern is a location whose physical state, NPC response and evidence history evolve together but remain owned by separate systems.

A useful Ouros incident therefore needs three independent histories:

1. what physically changed at the site;
2. what named actors did because of that change;
3. what evidence each actor actually observed or received.

After restart, those histories must be selected from one coherent semantic moment. Pairing an NPC checkpoint from after an evacuation with a site-evidence checkpoint from before the triggering discovery can produce an impossible world even when each file is valid alone.

This research directly supports `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1` and the proposal `The Survey That Survived the Collapse`.

## Capability caution

The reduced narrative pattern needs no AutoPTU handoff.

A rich collapse/evacuation version may require complete movement, full turn/round lifecycle, stateful damage, status lifecycle and exact terrain/hazard/reaction behavior. Those dependencies must remain explicitly gated until live engine evidence verifies the mechanisms used.
