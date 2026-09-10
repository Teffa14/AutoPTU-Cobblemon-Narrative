# Holder-journal recovery and expedition research scan — Pass 397

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-10
Narrative baseline inspected before writing: `95882dab741538fd59bebec1812db65997bf6e6b`

Nothing in this file is canon. Public material is used only for reusable structures and implementation lessons. Protected prose, dialogue, named characters, proprietary plots and distinctive mechanics are not imported.

## Repository-first inspection and duplicate control

The repository tree was inspected recursively before writing. Current focus, canon governance, design contracts, proposals, tests, tools, implementation fixtures, source indexes and the recent Pass 338–396 recovery/resource chain were checked before selecting this slice.

Pass 396 established a holder-transition journal for checkout, return and authorized handoff, but its own contract explicitly left deterministic snapshot/restore as the next recovery seam. Pass 394 and Pass 395 therefore still have to treat some holder disagreements as `INDETERMINATE` after restart because the new journal is not yet a recovered owner.

Source-name searches rejected heavily reused material including Pokémon Ashen Frost, Tales of Visiwa, Putuland, The Reckless Rollers, Pokémon Ranger, Mystery Dungeon mission structure and the Azure Event Sourcing reference already used by Pass 304.

## Source 1 — AWS Prescriptive Guidance: event sourcing and point-in-time recovery

Source:
https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/event-sourcing-pattern.html

Accessed: 2026-09-10.

Reusable structure:
AWS describes an append-only chronological event store in which state changes are retained as individual events. A known snapshot plus subsequent ordered events supports reconstruction of point-in-time state. It also warns that event ordering matters because incorrect ordering can produce incorrect system state.

Ouros transformation:
`ResourceHolderTransitionLedger` should survive restart as its own deterministic recovery owner instead of being reconstructed from current holder, reservation history or custody history. The checkpoint stores the exact ordered holder events that existed at one semantic cut. Restore revalidates event shape and per-resource continuity rather than trusting a digest alone.

Ouros does not adopt AWS services, delivery guarantees, infrastructure or cloud architecture.

## Source 2 — PTU campaign listing: The Trifecta Discovery

Source:
https://www.reddit.com/r/lfgpremium/comments/11lvr14/

Accessed: 2026-09-10.

The public PTU campaign pitch centers a newly observed Pokémon phenomenon and sends recently graduated trainers into the world to gather data and investigate its cause.

Reusable structure:
A regional mystery can begin as repeated field observations rather than a single exposition scene. Different expeditions may gather pieces of a larger pattern, and the reliability of mundane field records can become narratively important before anyone understands the phenomenon.

Ouros transformation:
A proposed expedition chain can use one shared survey instrument across several teams. A later anomaly makes the earlier readings important, while recovery records determine which holder transitions are actually proven after an infrastructure failure. No campaign-specific starter concept, phenomenon, characters, setting or plot is imported.

## Source 3 — Pokémon Eon Guardians: Nameless Island exploration

Source:
https://sites.google.com/view/pokemon-eon-guardians/playthrough/nameless-island

Accessed: 2026-09-10.

The public walkthrough describes a newly appeared island that becomes an explicit exploration objective.

Reusable structure:
A newly accessible place can justify a bounded expedition whose first purpose is observation and mapping. The uncertainty of the place itself can create progression without requiring every discovery to be a combat encounter.

Ouros transformation:
A proposed temporary shoal, exposed cave mouth or newly reachable survey zone may receive several short expeditions. Shared equipment, route notes and holder history can link those visits. No Terre region, Nameless Island, quest title, reward, encounters, map or story content is imported.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid only. Relevant source routes include campaign/session structure, research-oriented Trainer Classes, movement, hazards, terrain/weather, Items/Gear and encounter creation. The index explicitly does not grant rules to Ouros.

The survey instrument used by the proposal remains a mundane `WorldResource` unless an exact PTU/Caelo Item mapping is separately approved. Holding it does not grant a Skill result, Trainer Feature, action interrupt, tactical item effect or environmental immunity.

## Read-only engine evidence

AutoPTU-Java main inspected 2026-09-10: `ca235409e6d317055ae4afd9008bd82156b739f7`, merge #423, “Freeze authoritative switch transition plan”. The new evidence freezes one successful combatant replacement plan against pinned Python behavior: outgoing active/off-field state, replacement active state and replacement destination, plus validity guards in the Java plan. This strengthens evidence for that exact switching seam. It does not establish complete switching, complete movement, complete Ability coverage, full action economy or the full turn/round lifecycle.

AutoPTU Python main inspected 2026-09-10: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. The latest change remains presentation-only.

No engine repository was modified.

## Capability implications for the proposed expedition encounter

Reduced implementation:
The expedition and recovery mystery can run entirely in persistent-world systems. It needs semantic time, travel, explicit NPC knowledge, communication, `WorldResource`, reservations/handoffs when used, holder transitions and the new holder-transition checkpoint. AutoPTU is not required.

Mechanically rich implementation:
Targeting/footprints/range/LoS: required only if threats use tactical spatial targeting.
Base movement legality: required for ordinary combat-grid navigation.
Complete movement: required for push, pull, knockback, interception, dragging, rescue reposition or other forced movement.
Core calculations: required for ordinary battle resolution.
Action economy/initiative: required when actors compete inside tactical time.
Full turn/round lifecycle: required for timed survey windows, delayed collapse, weather phases or round-bound evacuation.
Full stateful damage pipeline: required when damage creates persistent tactical consequences.
Status lifecycle: required for complex or lasting conditions.
Terrain/weather/hazards/zones/reactions: required for flooding, unstable ground, reduced visibility, triggered hazards, weather phases or reaction zones.
Move-specific behavior: individually gated for any selected Move.
Abilities: individually gated for any selected Ability.
Items: individually gated for any PTU Item effect.
Trainer Features/perks: individually gated for interrupts, special actions or bonuses.
AI legal-action infrastructure: ordinary audited scopes are usable only where current contracts prove them.
AI tactical policy: still blocking for survey-first, rescue-first, protect-equipment, escort-carrier, objective-aware withdrawal and disengage-after-objective behavior.
Minecraft/Cobblemon/Craftics adapter/playback: still partial/blocking for persistent equipment interaction, authoritative pickup/handoff acknowledgement, environmental objective state and non-KO encounter completion.

## Reusable Ouros lessons

A recovered current holder and a recovered holder history answer different questions and should remain separately queryable.

Checkpoint durability can itself support mystery design: facts inside the recovered semantic cut are proven, while the interval after that cut remains legitimately unknown until another source provides evidence.

Repeated expeditions can build a regional mystery from mundane measurements, route notes and handoffs without requiring an escalating sequence of battles.

A newly accessible environment can support mapping, observation, rescue and logistics as primary objectives. Tactical richness stays optional and capability-gated.

## Canon boundary

No survey site, expedition program, institution, equipment model, environmental phenomenon, NPC, faction, species, legal authority or regional mystery is approved here. All remain proposed or unresolved until explicit promotion in `canon/`.
