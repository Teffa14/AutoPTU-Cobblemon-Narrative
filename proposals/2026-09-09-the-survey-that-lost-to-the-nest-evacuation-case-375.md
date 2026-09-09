# The Survey That Lost to the Nest Evacuation

Status: PROPOSED / NON-CANON
Date: 2026-09-09
Canon impact: NONE until explicit promotion

## Premise

A field team receives a valid reroute instruction after a route hazard is reported. The message reaches the team and wakes replanning correctly.

At the same semantic moment, three other pressures exist:

- a scheduled survey window is already due;
- the team leader is under meaningful fatigue pressure;
- a local habitat emergency creates a hard commitment to help evacuate exposed Pokémon nests before water reaches them.

The planner processes the same batch and selects the habitat emergency. The reroute message was neither ignored nor forgotten. It lost arbitration to a higher-scoring obligation.

Hours later, an office observer sees that the team did not follow the requested reroute and may infer disobedience. A field worker may instead remember that the team discussed the message before choosing the evacuation. Recovery should be able to preserve the actual decision-time alternatives.

## Reusable roles

Names and institutions remain unresolved.

Possible roles:

- field-team leader;
- remote scheduler or dispatcher;
- habitat specialist who reports the emergency;
- local resident or worker who knows the threatened nesting site;
- later investigator who reconstructs why the expedition deviated.

These are archetypes only.

## Reduced implementation

The reduced version does not require AutoPTU.

Required world systems:

- semantic time;
- Communications and delivery provenance;
- private knowledge;
- replan-trigger provenance;
- plan-selection provenance;
- scheduled commitments;
- needs/pressure;
- semantic travel and replanning.

Outcome can be represented as world-state transitions:

1. reroute delivery materializes;
2. habitat emergency trigger enters the same replan batch;
3. survey, fatigue, reroute and emergency candidates are evaluated;
4. emergency assistance wins;
5. travel destination changes toward the nesting site;
6. later actors can inspect only the evidence available to them.

The narrative premise survives without tactical combat.

## Full encounter version

The nesting site sits in terrain threatened by rising water and unstable access. The objective is to move vulnerable Pokémon, personnel or protective equipment to safe ground before the local window closes.

Potential tactical pressures:

- limited safe approach lanes;
- line-of-sight interrupted by terrain;
- water or mud increasing movement difficulty;
- frightened wild Pokémon occupying evacuation paths;
- optional rescue targets with different priorities;
- environmental changes between rounds;
- equipment that must remain protected while the team moves.

Success conditions should prioritize evacuation and route safety. Defeating every Pokémon is not required.

## Permanent engine capability dependency classification

Targeting / footprints / range / LoS: REQUIRED for the full version. Current evidence supports ordinary verified scope, but scenario-specific obstruction geometry still needs adapter admission.

Base movement legality: REQUIRED. Ordinary movement legality is currently VERIFIED within audited scope.

Complete movement, including push/pull/knockback/interception/forced movement: OPTIONAL in the reduced tactical version; REQUIRED only if evacuation uses forced displacement, interception or carrier displacement. Current status remains PARTIAL.

Core calculations: REQUIRED for ordinary structured combat. Current status remains VERIFIED within audited deterministic scope.

Action economy / initiative: REQUIRED for a structured rescue encounter. Audited primitives remain VERIFIED within known scope.

Full turn/round lifecycle: REQUIRED if water level or evacuation phases change on round boundaries. Current status remains PARTIAL.

Full stateful damage pipeline: REQUIRED if combat damage can affect evacuation participants. Current status remains PARTIAL.

Status lifecycle: OPTIONAL unless fear, immobilization, persistent conditions or similar PTU statuses become encounter-critical. Current status remains PARTIAL.

Terrain / weather / hazards / zones / reactions: REQUIRED for the intended rich rising-water version. Current status remains MIXED / PARTIAL / BLOCKING by exact mechanism. A reduced structured version should use static terrain only until exact hazard contracts are verified.

Move-specific behavior: REQUIRED only for moves actually admitted into the encounter. Individually gated.

Abilities: REQUIRED only for participating abilities that matter to resolution. Individually gated; representative round-start work does not verify the whole family.

Items: REQUIRED only for items used mechanically. Individually gated.

Trainer Features / perks: REQUIRED only when a Trainer Feature changes rescue or battle resolution. Individually gated.

AI legal-action infrastructure: REQUIRED for autonomous structured participants. Ordinary audited legal-action infrastructure remains VERIFIED within known scope.

AI tactical policy: REQUIRED for autonomous rescue-first, protect-vulnerable-target, preserve-equipment, withdraw-after-objective and route-clearing behavior. Current status remains BLOCKING for those policies.

Minecraft / Cobblemon / Craftics adapter and playback: REQUIRED for physical nest identity, rescue target persistence, changing hazard presentation, cargo/equipment identity and authoritative end-to-end playback. Current status remains PARTIAL / BLOCKING.

## Reduced tactical version

Keep terrain static. Do not use forced movement, delayed hazards, complex statuses, reaction interrupts or ability-driven terrain changes.

Use ordinary movement, targeting and basic legal actions. Represent the water deadline as an Ouros semantic objective timer outside AutoPTU. The adapter only needs to present the objective and return admitted structured results.

This preserves the same premise while avoiding duplication of missing PTU mechanics in Minecraft.

## Canon questions before promotion

- Which approved Ouros location can support the habitat and access pattern?
- Which species are locally canon-compatible at that site?
- Which existing institution owns the field team and survey obligation?
- What environmental event creates the evacuation pressure without contradicting established ecology?
- Is the team leader an existing recurring NPC or a new candidate?

No answer is assumed in this proposal.
