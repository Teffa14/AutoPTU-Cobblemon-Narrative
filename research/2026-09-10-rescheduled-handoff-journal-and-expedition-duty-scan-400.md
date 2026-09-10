# Rescheduled handoff journal and expedition-duty scan — Pass 400

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Accessed: 2026-09-10

## Repository inspection and duplicate control

The recursive main-branch tree was inspected at `aec7d8d1e651e21eb5b28f9b878dd7e6bf0a365a` before writing. Current focus, canon governance, the Pass 396–399 holder-history chain, handoff/reschedule implementation, existing proposals/research names and the PTU/Caelo routing boundary were checked before source selection.

Repository code search found the concrete remaining holder mutation bypass already identified in Pass 399: `tools/global_npc_resource_handoff_rescheduling.py::execute_current_authorized_handoff()` delegates to the lower-level `execute_authorized_handoff()` and therefore can change `WorldResource.holder_actor_id` without emitting `ResourceHolderTransition`.

Frequently reused recent anchors were excluded. Pokémon Burning Scales, Dreamstone Mysteries, Pokopia, Gaia, Rejuvenation, Prisme, Wastelands, Odyssey and Stalactite were not selected as primary new sources.

## Source 1 — Explorers! A PMD RPG community release

Public source: https://www.reddit.com/r/MysteryDungeon/comments/1mfvm5d/explorers_a_pmd_rpg_is_officially_released/

The public release describes a purpose-built tabletop RPG for Pokémon Mystery Dungeon play, with a large rules document plus character sheets, cheat sheets and quick-reference material. The useful high-level lesson is not any rule text. It is that expedition-oriented Pokémon play benefits when mission procedure and recurring field work are treated as first-class play structures rather than improvised exceptions.

Ouros transformation: field teams can have recurring operational duties where departure, resource custody, route changes, rescues, returns and debriefs are all meaningful world events. No rules, prose, characters, setting or distinctive scenario from the source are copied.

## Source 2 — contemporary Pokémon tabletop community advice on local conflict

Public source: https://www.reddit.com/r/DnD/comments/1dfeqfm

A public campaign-design response recommends beginning with setting and local conflicts rather than prewriting a complete plot, then allowing larger threads to emerge from player decisions.

Ouros transformation: small persistent obligations can create later arcs because named NPCs, resources, observations and unfinished work continue to exist after the player leaves. The world should preserve the actual causal chain rather than retroactively making every local hook part of a predetermined plot.

## Source 3 — Dunsparce & Drampa: Harmony, current episode index

Public source: https://podcastrepublic.net/podcast/1578571454

The public episode index shows a long-running Pokémon actual-play campaign where episodes move among institutional change, environmental protection, travel, certification and other forms of adventure. The reusable pattern is tonal and structural variety inside one continuous campaign: practical work can matter between high-stakes events.

Ouros transformation: ordinary expedition duties, certifications, custody procedures and handoffs can become causal setup for later emergencies without every scene becoming combat. No episode plot, cast member, dialogue or unique setting element is imported.

## Source 4 — engine evidence, read only

AutoPTU-Java inspected head: `16352837e09c9fe07e0d38f8942d1dec96c095bb` (merge #425, 2026-09-10), `Materialize authoritative switch field presence`.

The new `CombatantFieldPresenceStore` provides a concrete runtime store where absence means off-field and a successful switch transition removes the outgoing combatant and places the replacement at the resolved destination. Oracle parity tests compare that narrow materialization against pinned Python behavior.

Evidence consequence: this strengthens the exact switching/field-presence seam. It does not prove complete movement, generic forced movement, the full turn/round lifecycle, Abilities as a family, Trainer Features as a family, tactical objectives or Minecraft playback.

AutoPTU Python inspected head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The newest commit explicitly states that it is presentation-only viewport-coordinate synchronization and changes no battle rule or outcome.

Neither engine repository was modified.

## PTU / Caelo boundary

Existing project source routing was rechecked before proposing mechanics. Research-oriented classes, Skills/Edges/Features, Items/Gear, movement, hazards, terrain/weather and encounter construction remain source references that require original-rule verification. This pass grants no new PTU/Caelo mechanic to Ouros.

A world resource used in an expedition remains narrative/world state unless a verified PTU Item or Feature contract separately admits its tactical behavior.

## Resulting candidate

See `proposals/2026-09-10-the-relief-team-arrived-with-the-right-case-pass-400.md`.

The candidate uses a routine expedition handoff that is legitimately rescheduled during a local emergency. Its later mystery depends on whether the resource custody transition actually occurred, when it occurred, and which actors received the update. The reduced form requires no AutoPTU. The rich form exposes rescue, escort, terrain and non-KO objective dependencies explicitly.
