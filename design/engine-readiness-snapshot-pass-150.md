# Engine Readiness Snapshot — Pass 150

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only inputs.
Date: 2026-08-24

## Live revisions inspected

AutoPTU-Java `main`: `ab29df99b0ac884805cb90d115818ad92c62a35d` — `Freeze PRE-damage follow-up execution policy (#178)`.

AutoPTU Python `main`: `65702f3816162c804a926c228d54d405f3236a97` — Career postbattle video review persistence; no tactical promotion implied.

Java still states that Python AutoPTU is authoritative while the port is incomplete. Its README continues to list full combatant/grid state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, AI scoring/policy and Minecraft/Cobblemon adapter work as incomplete.

## Permanent capability map

| Capability family | Pass 150 status | Evidence boundary |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README documents range, areas, footprints, anchors and LoS as implemented. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers, fit and related base rules are documented as ported. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Specific Sway and reaction movement primitives exist, but README still lists forced movement incomplete. Narrow primitives do not constitute a generic subsystem. |
| core calculations | VERIFIED | Damage Base/type chart/stages/accuracy/weather DB/crit/Burn/modifier primitives are documented as implemented. |
| action economy / initiative | VERIFIED | Typed action budgets and initiative/order variants have parity-backed implementations. |
| full turn / round lifecycle | PARTIAL | Multiple ROUND_START, delayed-hit, temporary-state and reaction-ordering slices exist; full lifecycle/transcript parity is incomplete. |
| full stateful damage pipeline | PARTIAL | Meaningful normal/delayed/reaction slices exist; README explicitly leaves full damage incomplete. |
| status lifecycle | PARTIAL | Status application/prevention/mutation slices exist; full status controller remains incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Field-state and several PRE-damage reaction contracts exist, but the family remains incomplete in README. Use only individually verified narrow contracts when exact behavior matches. |
| move-specific behavior | PARTIAL | Delayed, multi-target and reaction-related Move behavior exists in slices; the full Move catalog is not ported. |
| abilities | PARTIAL | Multiple parity-backed Abilities exist; the complete registry does not. |
| items | PARTIAL | Item behavior exists in slices; complete item hook parity is incomplete. |
| Trainer Features / perks | PARTIAL | Generic gates/effects plus selected concrete interactions exist; catalog parity remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal `BattleChoice` action-space contract is documented as implemented. |
| AI tactical policy | BLOCKING | README still lists scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback | BLOCKING | Java explicitly remains a library rather than a Minecraft mod and adapter work is pending. |

## New Java evidence: PRE-damage follow-up policy remains narrow

Commit `ab29df99` freezes a policy around PRE-damage follow-up execution. It follows the recent work on Sway and the generic PRE-damage follow-up Move seam.

Narrative implication:

- individually verified PRE-damage reaction behavior may be used only when an encounter needs that exact contract;
- this does not verify arbitrary reactions, escort interrupts, overwatch, interception, collision or general forced movement;
- the broader `terrain/weather/hazards/zones/reactions` family remains BLOCKING;
- complete movement remains BLOCKING.

## Pass 150 encounter dependency mapping

### Orchard Threshold Survey — FULL

Required:

- complete movement — BLOCKING for moving scouts, withdrawal/crossing objectives and protected lanes;
- AI tactical policy — BLOCKING for `WITHDRAW`, `CROSS`, `PROTECT_SCOUT`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING only if orchard/environment features become actual tactical mechanics.

REDUCED: resolve scouting and ecological movement in world state. If a confrontation remains, use a static arena relying on verified targeting, base movement, core calculations, action economy and legal-action generation.

### Greenhouse Exclusion Breach — FULL

Required:

- complete movement — BLOCKING for staff/organism movement objectives;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if glass, chemical, crop or environmental hazards are retained mechanically.

REDUCED: secure compartments and workers first, then use a dry static arena with no invented glass/toxin/crop effects.

### Beneficial Edge Conflict — FULL

Required:

- complete movement — BLOCKING for non-hostile withdrawal and protected routes;
- AI tactical policy — BLOCKING for `WITHDRAW`, `PROTECT_MONITOR`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED: ecological actors withdraw in world state. A static independent confrontation may occur, while ecological interpretation remains outside battle.

### Threshold Review Meeting

No battle family is inherently required. A valid outcome is `NO_ACTION_MONITOR_ONLY`.

## Pass 150 world-state blockers

These are overworld/narrative contracts rather than AutoPTU battle capabilities:

- persistent pest-management program state;
- crop-pressure observation provenance;
- scouting effort and coverage;
- scoped target/beneficial/non-target assessments;
- versioned action thresholds;
- intervention history;
- non-target follow-up;
- management-effectiveness review;
- Biosecurity handoff for translocation/biological control;
- Toxicology/environment handoff for chemical proposals;
- Food/Agriculture consequence writeback;
- authoritative management state -> coarse Minecraft presentation;
- safeguards against loaded Cobblemon count becoming infestation truth.

## Mechanical non-inferences

Pass 150 does not authorize:

- Bug Type as a pest classification;
- crop blocks as HP objects;
- wild Pokémon near crops as hostile AI;
- Sweet Scent as a spawn-control command;
- Bug Bite as overworld crop consumption;
- Harvest/Honey Gather as agricultural-yield simulation;
- Poison Type as pesticide immunity/resistance;
- narrative chemical treatment as Poisoned, damage, Weather or a hazard zone;
- biological-control Pokémon as automatic predator AI;
- capture/KO/despawn as long-term pest-control success;
- specific PRE-damage reaction slices as a general reaction or forced-movement engine.

## PTU / Caelo source status

Public PTU 1.05 resources remain the broad rules reference and Python AutoPTU remains the implementation oracle while Java is incomplete.

No reliable primary Caelo rule defining agricultural pest management, crop scouting, pesticide effects or a generic farming-combat subsystem was recovered in this run.

Super PTU Online Helper was not exposed as an invocable capability. No output is invented or attributed to it.

## Open questions

- Does Caelo establish any agricultural institutions, crops or management traditions that should be authored before procedural use?
- Are any chemical controls canonically present in Ouros, or should the system initially emphasize exclusion, monitoring and coexistence?
- Which Pokémon/crop relationships are authored regional ecology versus emergent observations?
- What exact rules govern Honey Gather, Harvest, Sweet Scent, Naturewalk and agriculture-adjacent Features in the project’s final PTU/Caelo ruleset?
- How much crop loss should be modeled quantitatively versus qualitatively?
- When should an agricultural conflict enter AutoPTU at all, rather than resolving entirely through world-state investigation and management?