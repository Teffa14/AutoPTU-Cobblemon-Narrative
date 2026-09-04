# Ecological cue-quality separation contract

Status: PROPOSED contract. Pass 266. No Marea/Sendero site is declared an ecological trap.

Purpose: keep environmental attractiveness and site-use evidence separate from actual ecological quality and outcomes.

Record: `ECOLOGICAL_CUE_QUALITY_DIVERGENCE_V1`.

Required fields: stable record id; site reference; cue class; cue state; selection-evidence state; quality-evidence state; trap-hypothesis state; provenance/evidence references; canon status.

Allowed selection states are `NONE`, `USE_ONLY`, `SELECTION_SUGGESTED`, `PREFERENCE_SUPPORTED`, `UNCERTAIN`. Allowed quality states are `UNKNOWN`, `OUTCOME_SIGNAL_PRESENT`, `COMPARATIVE_BENEFIT_SUPPORTED`, `COMPARATIVE_COST_SUPPORTED`, `UNCERTAIN`. Trap state is `NOT_EVALUATED`, `UNRESOLVED`, `SUPPORTED` or `REJECTED`.

Core invariant: `cue attractiveness != site quality != demographic outcome`.

Repeated detection, same-site recurrence, congregation, feeding-looking presentation, NPC belief, Minecraft identity or model similarity can support observations. They cannot by themselves establish habitat benefit, harm, population change or PTU state.

`trap_hypothesis_state = SUPPORTED` requires admissible selection/preference evidence relative to an available comparator plus comparative evidence that outcomes are worse at the selected site, matched in temporal/spatial scope and supported by adequate provenance. A cost signal alone is insufficient. Repeated use alone is insufficient. Poor outcome without selection evidence is insufficient. Incomplete evidence remains `UNRESOLVED`.

Pass 265 resource pulses can be referenced as cue/resource provenance. A pulse can explain elevated visibility of already-counted sources but does not imply benefit. Pulse lifecycle and cue-quality evidence remain separate.

The record describes site evidence. It does not decide that an individual detects, values, approaches, stays or leaves. Autonomous response requires species/individual/context policy and the relevant movement/AI authority. The adapter cannot infer intent from proximity.

Ecological observations remain separate from PTU consequences. Apparent impairment, collision, generic Minecraft damage presentation or reduced activity can enter the observation layer but cannot create HP loss, Injury or status. Durable PTU aftermath still requires the Pass 262-264 semantic-result, subject-binding and capability-admission contracts.

Reduced encounter: Ouros records cue state, observations and comparison evidence; Minecraft/Cobblemon presents environmental change and already-counted sources. No AutoPTU handoff is required.

Full encounter dependencies are explicit. Active detection/targeting requires targeting/footprints/range/LoS as applicable. Ordinary approach/retreat requires base movement legality. Push, pull, knockback, interception, blocking or forced displacement requires complete movement. Tactical sequencing requires action economy/initiative and full turn/round lifecycle. Mechanical site effects require terrain/weather/hazards/zones/reactions. Specific Moves, Abilities, Items or Trainer Features require their exact families. Damage aftermath requires the full stateful damage pipeline; persistent status also requires status lifecycle. Autonomous legal candidate generation requires AI legal-action infrastructure. Choosing whether to follow, ignore, exploit or avoid a cue requires AI tactical policy. World handoff/presentation requires Minecraft/Cobblemon/Craftics adapter/playback.

Fail closed: cue without quality evidence stays `UNKNOWN`; quality evidence without comparative selection does not justify an ecological-trap label; unverified tactical response stays in the reduced observation/projection version; cue removal does not rewrite history or prove recovery.
