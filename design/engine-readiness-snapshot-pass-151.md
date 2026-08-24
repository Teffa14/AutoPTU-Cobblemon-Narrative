# Engine Readiness Snapshot — Pass 151

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only inputs.
Date: 2026-08-24

## Live revisions inspected

AutoPTU-Java `main`: `ab520743d8d99f06fa28fd4d6fa06a0c4ecd3fee` — `Port Shell Shield pre-damage reaction (#180)`.

AutoPTU Python `main`: `60fbd177ddb3c62628acf00fea78163a56608746` — Career compact-battle rival-progression presentation; no tactical promotion implied.

Java still states that Python AutoPTU is authoritative while the port is incomplete. Its README continues to list core battle state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, AI scoring/policy and Minecraft/Cobblemon adapter work as incomplete.

## Permanent capability map

| Capability family | Pass 151 status | Evidence boundary |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README documents range, areas, footprints, anchors and LoS as implemented. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers and fit are documented as ported. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Narrow Sway/reaction movement primitives exist, but README still lists forced movement incomplete. |
| core calculations | VERIFIED | Damage Base/type chart/stages/accuracy/weather DB/crit/Burn/modifier primitives are documented as implemented. |
| action economy / initiative | VERIFIED | Typed action budgets and initiative/order variants have parity-backed implementations. |
| full turn / round lifecycle | PARTIAL | Multiple ROUND_START, delayed-hit, temporary-state and reaction-ordering slices exist; full lifecycle/transcript parity remains incomplete. |
| full stateful damage pipeline | PARTIAL | Normal/delayed/multi-target/reaction slices exist; README explicitly leaves full damage incomplete. |
| status lifecycle | PARTIAL | Application, prevention, stacking/removal and selected status-related interactions exist; full status controller remains incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Several PRE-damage reaction contracts and field-state slices exist, but the family remains incomplete. Use only exact verified contracts. |
| move-specific behavior | PARTIAL | Delayed, multi-target and reaction-related behavior exists in slices; full Move catalog parity is incomplete. |
| abilities | PARTIAL | Multiple parity-backed Abilities now exist, including Shell Shield; complete registry parity does not. |
| items | PARTIAL | Item behavior exists in slices; complete item hook parity is incomplete. |
| Trainer Features / perks | PARTIAL | Generic gates/effects plus selected concrete interactions exist; catalog parity remains incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal `BattleChoice` action-space contract is documented as implemented. |
| AI tactical policy | BLOCKING | README still lists scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback | BLOCKING | Java remains a library rather than a Minecraft mod and adapter work is pending. |

## New Java evidence — Shell Shield is an exact narrow reaction contract

Commit `ab520743` ports Shell Shield into the PRE-damage reaction registry.

The tested contract includes readiness owned by runtime state, an optional out-of-turn decision, consumption of that readiness, adding `Withdrawn`, raising Defense by one Combat Stage and emitting the ability event. The contract also confirms that the reaction does not cancel the hit or zero damage.

Narrative implication:

- Shell Shield can only be relied upon when an encounter actually uses that exact verified ability contract;
- it does not prove generic withdrawal AI, generic defensive reactions, general Status completeness or complete forced movement;
- it has no relevance to contaminated-land remediation unless an actual combatant in a battle uses Shell Shield;
- the broader reaction/environment family remains BLOCKING.

The immediately prior Java commit `b6701fcc` executes PRE-damage follow-up Moves through the authoritative runtime. That strengthens reaction ordering and move execution but likewise does not complete the family.

## Pass 151 encounter dependency mapping

### Brownfield Survey Perimeter — FULL

Required:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for technicians or wildlife dynamically withdrawing/crossing threatened space;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL only if exact supported statuses occur;
- terrain/weather/hazards/zones/reactions — BLOCKING if contaminated zones, debris, dust or protected lanes become tactical mechanics;
- move-specific behavior — PARTIAL as required by chosen Moves;
- abilities — PARTIAL;
- items — PARTIAL if PPE/equipment is represented mechanically;
- Trainer Features/perks — PARTIAL if invoked;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `WITHDRAW`, `PROTECT_TECHNICIAN`, `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED: resolve sampling, access restrictions and ecological withdrawal in world state. Use a static arena outside the contaminated work zone. Do not project contamination, dust, PPE or cleanup state into PTU.

### Cap Inspection After Storm — FULL

Required:

- complete movement — BLOCKING for worker evacuation/rerouting;
- AI tactical policy — BLOCKING for `PROTECT_WORKER`, `WITHDRAW`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if rain, mud, cap damage or restricted lanes have tactical effects.

REDUCED: close the suspect sector in world state, move workers to a safe staging area and use a dry static battle map with no storm/cap/toxic effects.

### Redevelopment Utility Trench — FULL

Required:

- complete movement — BLOCKING for dynamic evacuation from the trench;
- AI tactical policy — BLOCKING for `EVACUATE` and `CLEAR_ROUTE`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING only if trench geometry, buried material or unstable surfaces become mechanical.

REDUCED: stop work, secure material and evacuate workers before battle. Resolve any independent confrontation on adjacent stable ground. Investigation resumes afterward.

### Site Reuse Review

No battle family is inherently required.

A valid result is `REUSE_DECISION_DEFERRED_PENDING_DATA`.

## Pass 151 world-state blockers

These are overworld/narrative contracts rather than battle capabilities:

- persistent contaminated-site identity;
- historical-use provenance;
- investigation-area geometry and data gaps;
- source/pathway hypotheses;
- conceptual site model revisions;
- medium-specific observation handoffs;
- remediation project state;
- residual-condition history;
- land-use/access controls;
- verification programs;
- long-term monitoring;
- reuse/redevelopment state;
- ecological occupation of legacy sites;
- contaminated-site -> Toxicology exposure handoff;
- contaminated-site -> Architecture/Land Tenure reuse handoff;
- authoritative site revision -> coarse Minecraft presentation;
- safeguards against blocks/entities becoming contamination truth.

## Mechanical non-inferences

Pass 151 does not authorize:

- Poisoned or Badly Poisoned from environmental description;
- contamination damage;
- Poison/Steel Type environmental immunity;
- Factory Terrain from industrial history;
- Rough Terrain from stained soil or debris;
- accuracy penalties from dust;
- custom toxic zones;
- Gas Mask/PPE effects without exact validated rules;
- Grimer/Muk/Trubbish/Garbodor/Koffing/Weezing as automatic contamination sources;
- any Pokémon as automatic cleanup infrastructure;
- KO/capture/despawn as remediation;
- removed barrels/blocks as cleanup completion;
- player block placement as verification;
- narrow PRE-damage reaction support as a complete reaction or forced-movement engine.

## PTU / Caelo source status

Public PTU 1.05 material and Python AutoPTU remain the broad mechanical reference/oracle while Java is incomplete.

No reliable primary Caelo rule defining contaminated-land cleanup, brownfields, remediation, generic pollution hazards or site-reuse mechanics was recovered in this run.

Super PTU Online Helper was not exposed as an invocable capability. No output is invented or attributed to it.

## Open questions

- Which legacy industrial sites already exist in Ouros canon?
- Which institutions can investigate, restrict access, approve cleanup or verify reuse?
- Does Caelo define exact environmental protection equipment or toxic-environment rules relevant to specific sites?
- How much contaminant identity should be qualitative rather than chemical/numeric?
- Which Pokémon have authored regional relationships with waste, polluted places or cleanup work?
- How should ecological habitat that develops on abandoned industrial land affect remediation planning?
- What level of long-term monitoring should advance offline?
- When should a contaminated-site scene enter AutoPTU at all rather than remain a world-state investigation?