# Engine Readiness Snapshot — Pass 100

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during this pass:

`a3ae7d5211c6cb797e68155fd62704025811d7da`

Latest relevant commit:

`Own and clear declared actions during ROUND_START (#135)`

The commit adds canonical declared-action state to `BattleRuntimeState`, a lifecycle cleanup hook and tests around round-start cleanup. This strengthens ownership of battle runtime state and one specific round-start responsibility.

It does not demonstrate complete Trainer Feature execution, full lifecycle behavior or any overworld tracking system.

AutoPTU main remains:

`e4bb0ca38b7018710af476ce365d515a387de4e7`

Its recent visible work remains Career-oriented and does not justify a tactical capability promotion.

The AutoPTU-Java README continues to state that Python is authoritative while the port is incomplete and still lists full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, complete hook registries, transcript parity, tactical AI and the Minecraft/Cobblemon adapter as unfinished.

A repository search for `Tracker`, scent and Odor Sleuth did not expose a generic overworld tracking subsystem in current AutoPTU code. PTU reference material present in/around the project does mention Tracker, but that is rules-source evidence rather than runtime implementation evidence.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static battle geometry, footprints, range and geometric LoS remain verified.

Pass 100 non-inference:

- a wildlife footprint is not a battle footprint;
- following a trackway does not reveal tactical target position;
- scent does not bypass LoS;
- a field sign is not targetable unless a dedicated object-target contract exists;
- overworld trail geometry does not establish battle range.

`base movement legality`

Established Shift/Jump and known movement-mode legality remain verified.

Pass 100 non-inference:

- a known wildlife trail does not grant Naturewalk;
- a tracker does not receive free movement;
- following footprints does not bypass blockers;
- scent tracking does not prove Burrow, Swim, Sky or passenger movement;
- a route hypothesis is not a legal Shift path.

`core calculations`

Established calculation primitives remain verified.

Pass 100 adds no sign-age formula, tracking DC, scent-strength calculation, route-confidence bonus, capture modifier or surprise modifier.

`action economy / initiative`

Established action economy/initiative remain verified.

The new declared-action cleanup strengthens one specific round-start state contract.

Pass 100 non-inference:

- finding fresh tracks -> initiative bonus;
- successful tracking -> extra action;
- prey scent -> Speed bonus;
- known route -> free Shift.

`AI legal-action infrastructure`

Deterministic legal-choice generation remains verified.

This does not prove tactical goals such as:

- FOLLOW_TRAIL;
- WITHDRAW_FROM_TRACKERS;
- ESCAPE_TO_DEN;
- PROTECT_INJURED_POKEMON;
- INTERCEPT_PURSUERS;
- INVESTIGATE_SIGN;
- AVOID_SCENT_ZONE.

Those require systems outside legal action generation.

### PARTIAL

`full turn / round lifecycle`

Representative phase, round-start, initiative, temporary-effect, field-effect, delayed-hit, Trainer AP/action-reset, declared-action and Trainer Feature ordering slices now exist.

Still PARTIAL because the complete set of START/END effects, durations, interrupts, Statuses, Abilities, Features, delayed effects and transcript behavior is not proven.

Field-sign aging is an overworld clock and must not be implemented as battle-round lifecycle.

`full stateful damage pipeline`

Representative authoritative damage paths exist.

Still PARTIAL per the Java README.

A biological trace, broken branch or injured-looking trackway does not create battle damage state.

`status lifecycle`

Representative status behavior exists.

Still PARTIAL.

Pass 100 non-inference:

- limping-looking tracks -> Injury;
- blood-like residue -> Bleeding/Status;
- resting site -> Asleep;
- scent trace -> Marked;
- muddy prints -> Slowed/Tripped.

`move-specific behavior`

Representative Move slices exist.

Still PARTIAL.

Odor Sleuth or any tracking-related Move must be verified exactly before a concept depends on its mechanics.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

Do not infer:

- Run Away = overworld withdrawal AI;
- Keen Eye = tracking bonus;
- Frisk = biological evidence analysis;
- Pickup = sample discovery;
- Sand Rush = desert tracking;
- any canine-like Ability = Tracker.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Evidence bags, sample jars, tracking markers and scent-reference items are overworld objects until an exact PTU Item authorizes a mechanical effect.

`Trainer Features / perks`

Representative Feature infrastructure and several individual Features exist.

Still PARTIAL.

Ranger, detective, field biologist, tracker and surveyor are narrative roles unless exact PTU/Caelo Features are validated.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a complete family.

Pass 100 impact:

- no true in-grid chase;
- no prey automatically fleeing along a track;
- no pursuer interception corridor;
- no forced displacement around a ford/market/den;
- no movement-driven pursuit objective without a dedicated contract.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 100 impact:

- rain may degrade overworld sign but does not create battle Weather automatically;
- mud/snow/sand may preserve tracks but do not create PTU Terrain automatically;
- scent does not create a zone;
- a den does not create cover or hazard rules;
- a river washing out tracks does not imply current mechanics in battle.

`AI tactical policy`

Still BLOCKING.

This is a principal blocker for a true pursuit/escape encounter. Legal actions alone do not make a Pokémon choose routes, protect a den, withdraw, investigate evidence or evade trackers.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

There is no verified end-to-end contract for projecting persistent field signs, sign age, trackways, scent clues, evidence interaction or tracking objectives into Minecraft while preserving server/world-state authority and AutoPTU-Java battle authority.

## Pass 100 specific overworld blockers

`FIELD_SIGN_IDENTITY`
Stable identity for a sign after render changes, chunk unload or degradation.

`TRACKWAY_GRAPH`
Spatially linked sign segments with uncertainty and partial loss.

`SIGN_DEGRADATION_CLOCK`
Coarse time/environment-driven visibility updates without rewriting history.

`SIGN_OBSERVATION_PROVENANCE`
Who observed what, when, under which substrate/weather conditions.

`SIGN_CLASSIFICATION_GRAPH`
Provisional species/sign/behavior classifications and revisions.

`MAKER_IDENTITY_HYPOTHESIS`
Candidate species/group/individual without premature entity merge.

`SCENT_TRACE_STATE`
Specialized evidence state gated behind verified PTU/Caelo capability.

`BIOLOGICAL_TRACE_SAMPLE`
Sample provenance, custody and analysis links.

`TRACKING_SURVEY_EFFORT`
Search coverage and method state so nondetection is not absence.

`TRACKING_TO_SCIENCE_HANDOFF`
Field observations feed datasets without becoming world truth.

`TRACKING_TO_CASES_HANDOFF`
Last sign and route hypotheses become evidence without proving intent/guilt/current location.

`TRACKING_TO_CONSERVATION_HANDOFF`
Repeated sign can support occupancy/route assessments without generating spawns.

`TRACKING_TO_COBBLEMON_PROJECTION`
Loaded entities cannot become the source of truth for sign history or population use.

`TRACKING_TO_MINECRAFT_PROJECTION`
Visual footprints/marks are projections; chunk reload cannot refresh them.

## Encounter dependency summary

### Last Tracks at Cedar Ford — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL when exact combat content is invoked:

- full lifecycle;
- full stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:

- complete movement/interception/forced movement for a live chase/rescue;
- terrain/weather/hazards/zones/reactions if the ford has tactical environmental effects;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback;
- overworld sign and scent contracts.

REDUCED version readiness:

Tracking is resolved entirely as overworld evidence. The relevant site is selected before combat. AutoPTU receives a static map. This version can preserve the premise without implementing pursuit mechanics.

### The False Trail — FULL

Core investigation can exist without battle-engine dependencies.

If wildlife withdraws tactically, required BLOCKING families are:

- complete movement;
- AI tactical policy;
- Minecraft playback.

REDUCED version readiness:

Can be entirely noncombat and return `INCONCLUSIVE`, `SUPPORTED` or `REJECTED` hypotheses.

### Scent Lost at the Market — FULL

Additional blocker beyond permanent categories:

`EXACT_TRACKER_CAPABILITY_RUNTIME`

The public PTU text is not enough. The project's exact PTU/Caelo rule and executable runtime boundary must be verified.

Other BLOCKING dependencies:

- scent-state model;
- complete movement/interception for a chase;
- AI tactical policy;
- Minecraft playback.

REDUCED version readiness:

The known scent can be an authored clue. The clue terminates at the market and hands off to witnesses/cameras/postal/transport evidence. No pursuit battle is required.

## Mechanical/canon questions unresolved

- What exact Tracker Capability text is authoritative in the project PTU/Caelo corpus?
- Does Caelo alter Tracker, Odor Sleuth, Perception or Survival interactions?
- Does Python AutoPTU contain relevant logic under a different name not found by repository search?
- Should overworld tracking live in the narrative/world server rather than battle core?
- How coarse should sign aging be?
- Which substrates preserve signs in authored Ouros regions?
- Can players create deliberate false signs, and how is their provenance represented?
- Which analysis methods can identify a persistent Pokémon individual?
- How are sensitive nesting/den locations protected in multiplayer?
- Should scent ever become spatial geometry, or remain a route clue until exact mechanics are implemented?

## Bottom line

Pass 100 can advance immediately as persistent evidence/world-state design.

The reduced encounter versions require only ordinary static battles when combat actually occurs.

True live pursuits, target withdrawal, scent-driven tracking mechanics and changing environmental pursuit maps remain blocked by complete movement, tactical AI, environment families, adapter/playback and the missing verified overworld Tracker contract.