# Pass 398 Research — Four-Owner Recovery and Courier Escalation

Status: RESEARCH / PROVENANCE ONLY
Canon authority: NONE
Date: 2026-09-10

Repository inspection before writing covered the root project boundaries, current focus, design/implementation trees, recent recovery contracts, holder-transition recovery, the PTU/Caelo/Kairos source router, recent proposals and source-name searches. Prior heavily reused anchors were rejected. In particular, the existing corpus already contains repeated use of Pokémon Ashen Frost, Pokémon Conquest, The Alexandrian, Mystery Dungeon mission structure, Pokémon Ranger and earlier Dunsparce & Drampa material. The newer Harmony campaign and the Pokémon Adventures Sun/Moon arc had no matching research entry by their specific source framing.

## Source 1 — PostgreSQL backup manifest integrity

Public source:
https://www.postgresql.org/docs/17/protocol-replication.html
https://www.postgresql.org/docs/17/backup-manifest-files.html

PostgreSQL can produce a backup manifest that enumerates the files belonging to a backup and can include checksums for those files. The reusable systems lesson is narrow: a recovery selector becomes stronger when it identifies the exact component generation expected, rather than accepting any individually valid component that happens to exist.

Ouros transformation:
`OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V3` records the exact digest of the independently recovered holder-transition checkpoint alongside the other persistent-world owners. This is an engineering analogy only. PostgreSQL storage semantics are not imported into world lore.

## Source 2 — Dunsparce & Drampa: Harmony

Public source:
https://music.amazon.com.br/podcasts/ff339dda-7868-40d9-bde5-e8c6723ff4d6/episodes/c55d2566-f1f1-4329-a0fc-b4b7a4b8eaef/dunsparce-drampa-there%27s-voltorbs-in-the-lifeboats-dunsparce-drampa-harmony-ep-1

The public episode description establishes an ensemble Pokémon TTRPG campaign whose opening journey immediately produces a chain of consequential events. Later public episode descriptions show consequences and obligations persisting across episodes rather than every problem resetting after one scene.

Reusable structure:
An ordinary journey can become the causal spine for several later obligations. A field job does not need to be replaced by a separate main plot; the consequences of what happened during the job can accumulate around it.

Ouros transformation:
A courier, surveyor, medic, ranger or technician can begin with one mundane obligation and acquire additional duties because of what occurs on the route. Persistent NPC knowledge and resource custody determine who can act on each duty. No Harmony characters, locations, dialogue, Pokémon roster or plot events are copied.

## Source 3 — Pokémon Adventures: Sun, Moon, Ultra Sun & Ultra Moon arc

Public source:
https://bulbapedia.bulbagarden.net/wiki/Sun%2C_Moon%2C_Ultra_Sun_%26_Ultra_Moon_arc_%28Adventures%29

The public synopsis begins its protagonists with concrete personal/professional motives, including courier work and a delivery, before those motives intersect broader regional pressures.

Reusable structure:
A character can remain legible through a practical job even while the story scale expands. The job supplies obligations, destinations, material objects and relationships that can carry continuity into the larger arc.

Ouros transformation:
Regional escalation can grow out of persistent work rather than suspending everyday life. Deliveries, custody, appointments and professional responsibility can remain mechanically meaningful as regional events intensify. No Adventures characters, institutions, island traditions, antagonists, creatures or plot are imported.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid only. It points toward campaign/session structure, Skills/Edges/Features, utility classes, Items/Gear, movement, hazards, terrain/weather and encounter construction. It explicitly does not grant mechanics to Ouros.

This pass does not invent a courier Trainer Feature, delivery Skill bonus, custody Item rule, rescue interrupt, weather modifier or carrying mechanic. Any concrete PTU/Caelo rule must come from the underlying supplied source and receive the project’s normal mechanical verification.

## Engine evidence refreshed

Read-only AutoPTU-Java main on 2026-09-10:
`ca235409e6d317055ae4afd9008bd82156b739f7` — merge #423, “Freeze authoritative switch transition plan”.

That change verifies a narrow switch-transition planning seam: outgoing/replacement identities, active/off-field outcome, replacement destination and validity guards covered by its parity tests. It does not establish complete switching, complete movement, the full action economy, the full turn/round lifecycle or the Abilities family.

Read-only AutoPTU Python main:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — presentation-only viewport-coordinate synchronization remains the newest commit.

## Resulting Ouros candidate

See `proposals/2026-09-10-the-delivery-that-changed-hands-pass-398.md`.

The key reusable premise is an ordinary delivery that intersects an emergency. The package can change hands legally while different NPCs retain different information about that transfer. The dramatic question comes from responsibility, timing and knowledge rather than an automatic theft accusation.
