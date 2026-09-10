# Legacy handoff closure and delayed ruins interpretation scan — Pass 401

Status: RESEARCH / PROVENANCE ONLY
Canon effect: NONE
Accessed: 2026-09-10

## Repository inspection and duplicate control

The recursive repository tree was inspected at narrative head `3b5f39ac9c771e0790df973b8737614c1b2bd80d` before writing. Current focus, canon governance, the playable Marea foundation, holder-transition history, handoff/reschedule execution, recovery/reconciliation material, recent Pass 391–400 research/proposals and the PTU/Caelo/Kairos routing index were checked before selecting this slice.

Repository-wide code search found the only non-test direct call from the reschedule compatibility executor to `execute_authorized_handoff()`. The holder-aware wrapper introduced in Pass 400 already provides the required current-authorization check plus `ResourceHolderTransition` emission.

Duplicate-source checks found no prior repository match for `PMD: Maelstrom` or `PUCL PTU` as named research anchors. Pokémon Nova, Elysium, Stalactite, Odyssey, Rejuvenation and the haunted-mansion campaign log were excluded because they already appear in recent research.

## Source 1 — P.U.C.L. PTU actual-play episode structure

Public source: Apple Podcasts, P.U.C.L. PTU episode listing.
URL: https://podcasts.apple.com/us/podcast/p-u-c-l-ptu/id1448567421

Additional public episode index: Podnews, P.U.C.L. PTU episode list.
URL: https://podnews.net/podcast/i5kev/episodes

Useful high-level pattern:

- Episode #8 publicly describes the party examining ruins during a broader Safari Zone visit.
- Episode #11 later describes one character sharing pictures of those ruins over dinner.
- The interesting structure is delayed interpretation: field evidence can be collected in one activity, retained, then become socially or investigatively relevant later in another context.

Transformation for Ouros:

A minor optional field observation does not need immediate explanation or reward. It can enter a provenance-backed evidence store, be shown later to an archivist/researcher, and create a new reason to revisit the original site. This fits existing Ouros rules around observations, private knowledge, archives and explicit communication.

Not imported: Belleza, episode plots, characters, dialogue, Safari Zone details, ruins identity, battles or Pokémon rosters.

## Source 2 — PMD: Maelstrom open-world dungeon progression

Public source: SkyTemple Hack Directory, `PMD: Maelstrom`.
URL: https://hacks.skytemple.org/h/maelstrom

The public project description presents an open-world exploration structure where large dungeons lead to useful treasures for future expeditions and completion can unlock additional dungeons of greater difficulty.

Reusable design lesson:

- exploration rewards can expand future expedition options rather than only increase combat power;
- discoveries can create a network of follow-up sites;
- a dungeon can have a practical expedition purpose whose value becomes clearer later.

Transformation for Ouros:

Ouros should prefer grounded capability expansion. A recovered route sketch, access key, surveying attachment, archive cross-reference or repaired field instrument may make a later expedition possible or safer. It does not grant a PTU Item effect unless authoritative rules and engine support validate that mechanic.

Not imported: dungeon layouts, type-themed dungeon structure, items, recruitment rules, patches, Pokémon composition or unlock graph.

## Source 3 — current Ouros canon and PTU/Caelo routing

Internal canon checked:
- `canon/ouros-playable-foundation-v1.md`
- `canon/README.md`

Existing canon already supplies suitable anchors without inventing a new region:
- Sendero del Vidrio is an old survey road with route-maintenance needs after heavy weather;
- Estación Mirador preserves ecological observations, route reports and specimen records;
- Tideglass Archive preserves route surveys and historical records;
- records remain attributed claims rather than omniscient truth.

PTU/Caelo/Kairos cross-check:
- `sources/kairos/KAIROS_SOURCE_INDEX.md`

The index routes expedition concepts toward Skills/Edges/Features, Researcher, Chronicler, Survivalist, Topographer, movement/terrain, hazards, weather, encounter construction and Items/Gear. The index explicitly does not authorize those mechanics by itself.

Therefore this pass grants no invented survey bonus, climbing rule, weather modifier, carrying rule, puzzle check, Item effect or Trainer Feature interrupt.

## New Ouros design synthesis

The strongest original structure is a delayed-evidence exploration loop:

1. a small optional expedition produces an observation whose significance is unknown;
2. the observation survives with source, time and collector identity;
3. later archive/research context changes what questions can be asked of the old observation;
4. a second expedition revisits the site for a different purpose;
5. the first trip remains useful even if it never contained a major battle or immediate answer.

The player does not need to perform step 1 personally. A persistent NPC team can create the observation if its schedule, access, knowledge and resources support the trip. If nobody visits the site, no retroactive evidence appears.

## Implementation finding — rescheduled handoff bypass

Pass 400 added `execute_current_authorized_handoff_with_holder_transition()`, but the older `execute_current_authorized_handoff()` could still execute a current authorization through the lower-level handoff executor without a holder journal.

Pass 401 changes the compatibility path to fail closed for a current authorization with `HOLDER_TRANSITION_LEDGER_REQUIRED`. Superseded authorizations retain `HANDOFF_AUTHORIZATION_SUPERSEDED`.

A successful rescheduled transfer must therefore use the holder-aware runtime.

This closes the known reschedule-specific bypass. It does not prove that every future holder mutation in the repository will automatically be journaled. Repository-wide mutation audits remain necessary before broad completeness claims.

## Capability dependency notes for the proposed exploration loop

Reduced implementation:
- no tactical battle required;
- semantic travel, observations, archive lookup, communications and site revision can carry the full narrative premise;
- environmental change can occur between scenes rather than as a tactical hazard.

Mechanically rich implementation:
- targeting/footprints/range/LoS if ranged protection or spatial observation matters;
- base movement legality for ordinary tactical navigation;
- complete movement for push/pull/knockback/interception/forced movement, slips, dragging or rescue reposition;
- core calculations for ordinary audited battle math;
- action economy/initiative for ordered tactical actions;
- full turn/round lifecycle for timed openings, collapse clocks or multi-phase objectives;
- full stateful damage pipeline when tactical damage must persist into world consequences;
- status lifecycle for complex persistent conditions;
- terrain/weather/hazards/zones/reactions for unstable ledges, flooding, wind, visibility changes, triggered debris or reactive areas;
- move-specific behavior, Abilities, Items and Trainer Features remain individually gated;
- AI legal-action infrastructure only within verified scopes;
- AI tactical policy is required for investigate-first, protect-evidence, rescue-first, retreat-after-objective and similar non-KO priorities;
- Minecraft/Cobblemon/Craftics support is required for stable site/evidence projection, environmental state, objective acknowledgement and authoritative non-KO playback.

## Canon questions left open

No new world fact is approved here. Open questions include:
- exact location of the optional survey structure;
- whether it is a shelter, marker station, culvert, lookout, service tunnel or another mundane survey artifact;
- what evidence is first collected;
- what later archive record changes its interpretation;
- what caused physical access to change;
- whether any wild Pokémon encounter occurs;
- which NPC or team reaches the site first;
- which Skills/Edges/Features/Items are mechanically relevant after source-level validation.
