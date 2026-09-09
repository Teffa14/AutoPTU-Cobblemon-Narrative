# World action terminal provenance research scan — Pass 380

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-09
Canon effect: NONE

## Internal inspection before research

Narrative baseline inspected before writing: `dcc951d3c38a2b4d8cb98ec875721ec4332b31c1` (Pass 379).

Relevant internal owners/contracts reviewed include V17 action-start recovery, standalone action-terminal provenance, semantic travel and the Pass 379 terminal contract. Existing research search was used to reject recently reused sources. The Alexandrian/Three Clue Rule and Pokémon Ashen Frost were explicitly rejected because the repository has already processed them multiple times.

Read-only engine evidence was refreshed during this pass. No engine repository was modified.

## Source 1 — Apache Airflow task-state model

Source: Apache Airflow 3.3.1 documentation, `airflow.utils.state`.
https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/utils/state/index.html

Airflow distinguishes intermediate states such as scheduled, queued and running from terminal states such as success, failed, skipped, upstream-failed and removed. Its documentation also treats “finished” as broader than “successful”: a task can have reached a terminal state without having succeeded.

Reusable Ouros lesson:

A durable world action needs an explicit terminal kind. “No longer running” must not collapse into “succeeded”. This directly supports keeping travel arrival, future failure/cancellation, objective completion and AutoPTU resolution as separate evidence families.

Transformation boundary:

Ouros imports no Airflow scheduler semantics, retry policy, software API or terminology as setting canon. The reusable material is only the state-machine distinction between progress and distinct terminal outcomes.

## Source 2 — Pokémon Golurk Rising

Source: Eevee Expo project page, Pokémon Golurk Rising.
https://www.eeveeexpo.com/golurk-rising/

The public project description combines a research-assistant role, field research, surveys of multiple ruins, rival groups and discoveries whose meaning unfolds across repeated expeditions. Repository search found no prior match for `Pokémon Golurk Rising` before this pass.

Reusable Ouros lesson:

A field site can support repeated visits with different states: assigned, reached, surveyed, interrupted, revisited and reinterpreted. Arrival can therefore be meaningful persistent evidence without being the same event as completing the scientific or institutional objective.

Transformation boundary:

Do not import Lasai, Golett partnership, the named professor, color gangs, ancient-cycle mythology, bosses, specific ruins, puzzles, dialogue or plot. The only imported structure is repeated field research at persistent sites with consequences carried between visits.

## Source 3 — PokéTaka

Source: Eevee Expo release thread, PokéTaka, published 2026-08-27.
https://eeveeexpo.com/threads/9711/

PokéTaka centers asynchronous expeditions: the player prepares a team, sends it away for a timed activity, later returns to see what happened, receives a replay and collects resulting resources/encounters. Repository search found no prior match for `PokéTaka` before this pass.

Reusable Ouros lesson:

For an off-screen or compressed expedition, submission/start, elapsed execution, terminal state, replayable evidence and resulting rewards are separable layers. A persistent simulation is clearer when recovery can identify which layer had actually happened before a restart.

Transformation boundary:

Ouros does not import PokéTaka's Kanto roster, automatic battle rules, expedition rewards, catch loop, progression, timings or browser-game economy. The reusable structure is the explicit separation between dispatching an expedition and later observing its result.

## New original Ouros structure

Working concept: `The Survey Camp With No Survey Result`.

A field team has a valid assignment to inspect a persistent site. The causal record proves that the team selected the trip, departed and reached the site. The world does not contain evidence that the survey itself completed.

On a later visit, the player can encounter evidence that is compatible with several explanations: the team established camp but was diverted locally; an instrument problem stopped work; a nearby ecological issue took priority; communications failed after arrival; an institutional order changed; the team withdrew; or another actor interfered. None becomes true merely because the team arrived.

The important scenario pattern is a missing transition after a proven terminal travel event. V18 can preserve “they reached the site” while future owners decide whether and how “the site objective ended” is represented.

## Reduced implementation version

The reduced version can run without AutoPTU:

- semantic time;
- world-agent identity and private knowledge;
- plan selection provenance;
- semantic travel action-start provenance;
- V18 travel-arrival provenance;
- communications/replanning when an update is sent;
- persistent but non-canonical placeholder site state.

The premise does not require a battle, dynamic weather, complex status or forced movement.

## Full encounter version and capability gates

A mechanically rich visit can later turn the site into a search/survey/recovery encounter. Potential objectives include locating missing field personnel, preserving equipment, checking multiple observation points, opening a safe withdrawal route, or protecting a noncombatant while evidence is collected.

Capability classification for that full version:

- targeting/footprints/range/LoS — VERIFIED only within audited ordinary scopes; required if combat or line-of-sight search pressure is used;
- base movement legality — VERIFIED within audited ordinary scopes; required for ordinary movement around the site;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL; avoid in the reduced version and gate explicitly if added;
- core calculations — VERIFIED within audited deterministic scopes;
- action economy/initiative — VERIFIED for audited primitives; Java evidence in this pass adds a specific production round-start Intimidate rollover trace, not blanket lifecycle coverage;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — MIXED/PARTIAL/BLOCKING by exact mechanic; no dynamic flood/weather phase is assumed by the reduced version;
- move-specific behavior — INDIVIDUALLY GATED;
- abilities — INDIVIDUALLY GATED; the new Java Intimidate trace is representative evidence only;
- items — INDIVIDUALLY GATED;
- Trainer Features/perks — INDIVIDUALLY GATED;
- AI legal-action infrastructure — VERIFIED for ordinary audited actions;
- AI tactical policy — BLOCKING for search, escort, protect-equipment/noncombatant, objective-aware withdrawal and disengage-after-objective unless the exact policy is verified;
- Minecraft/Cobblemon/Craftics adapter/playback — PARTIAL/BLOCKING for persistent site/objective/equipment identity and authoritative non-KO result playback.

## PTU/Caelo authority boundary

No public source in this scan establishes Ouros rules, geography, species placement, institutions, field-research procedures, Ranger authority, item availability, encounter tables or Trainer capabilities.

Any species, Skills, Edges, Features, moves, Abilities, Items, travel capability, environmental mechanic or encounter fact must be checked against the project PTU/Caelo source material before canon promotion or mechanical implementation.

## Unresolved questions

- Which approved Caelo/Ouros location can host a persistent field-research site without inventing geography?
- Which existing institution, if any, can issue the assignment?
- What world owner should represent objective completion separately from travel arrival?
- What explicit terminal kinds should represent failure, cancellation, withdrawal or reassignment?
- What replayable global-NPC event will eventually prove `AUTOPTU_RESOLVED` rather than inferring it from later ingress?
