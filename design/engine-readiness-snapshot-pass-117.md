# Engine Readiness Snapshot — Pass 117

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `cdb229db787ac93f28745f796c1d9944546676cc`

Newest relevant Java evidence:

- generic Trainer Feature effects include parity-backed `apply_status` and `remove_status` handlers;
- stacked status entries are stored canonically and ordered;
- previous slices cover Trainer Feature prerequisite gates, context gates, frequency/cooldown gates, resources, usage bookkeeping, target scopes, trainer-target scopes, heal, Combat Stage, temporary HP and AP primitives;
- none of this establishes insurance, claim handling, asset valuation, property damage, liability, repair funding or overworld financial state.

AutoPTU `main`: `0db989a259f84d04e7fdcb161bb986bc6ef69275`

Newest visible Python work is Career/Vercel runtime packaging plus earlier Career persistence fixes. No tactical capability promotion follows from those commits.

## Java README evidence

The live Java README still lists as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative mechanics remain representative only.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 117.

## Why insurance/claims is outside the battle core

Nothing inspected in Java or Python proves an authoritative subsystem for:

- insurance institutions;
- mutual-aid risk pools;
- risk-transfer agreements;
- covered interests;
- policy/agreement versions;
- loss notices;
- claims;
- claim evidence review;
- valuation;
- coverage decisions;
- claim payments;
- business interruption;
- property liability;
- fraud adjudication;
- reserve depletion;
- recovery funding;
- insurance appeals;
- asset ownership law.

These are overworld/institutional responsibilities.

AutoPTU can provide authoritative battle facts when a battle occurs. It does not assign monetary value or decide whether a world loss is covered.

## Pass 117 encounter dependency map

### Storm-Damaged Depot Claim Survey — FULL

Narrative objective:

Allow an assessor and depot staff to document already-authoritative storm damage while a separate Pokémon disturbance makes part of the site unsafe.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for dynamic escort, inspection-point routing and withdrawal
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if damaged structures, weather or unsafe zones are tactical
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `PROTECT`, `WITHDRAW`, `REACH_INSPECTION_POINT`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Close the unsafe section in world state. Move assessor/workers off-grid. Preserve inspection observations already collected. If combat remains, run a static legal battle in a validated part of the depot. Resume claim work afterward. Battle outcome cannot decide coverage, causation or valuation.

### Mutual Relief Depot Chokepoint — FULL

Narrative objective:

Clear access so a mutual-aid reserve can dispatch pumps/generators while preserving staff and cargo.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for moving staff/cargo and protected lanes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if the depot has live tactical hazards
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `CLEAR_ROUTE`, `PROTECT`, `WITHDRAW`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Keep staff and equipment outside the grid. Run a conventional static battle to clear the lane. Supply Chains records dispatch after combat. Do not invent cargo HP, forklift physics or equipment damage.

### Harbor Claim Evidence Recovery — FULL

Narrative objective:

Recover physical records/instrument data from an already-damaged harbor while wild Pokémon also use the changed shoreline.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for movement objectives and withdrawal
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if currents, shoreline hazards or weather matter tactically
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `SEARCH`, `WITHDRAW`, `DO_NOT_DESTROY_EVIDENCE`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Resolve evidence locations/provenance in overworld state before battle. Keep documents/instruments outside battle authority. Freeze one validated shoreline geometry. Run an ordinary battle only if confrontation remains.

## New overworld blockers introduced by Pass 117

These belong outside AutoPTU-Java:

- `RISK_TRANSFER_INSTITUTION_STATE`
- `RISK_TRANSFER_AGREEMENT_STATE`
- `RISK_TRANSFER_AGREEMENT_VERSION_HISTORY`
- `COVERED_INTEREST_REFERENCE_STATE`
- `LOSS_NOTICE_STATE`
- `CLAIM_FILE_STATE`
- `CLAIM_EVIDENCE_GRAPH`
- `CLAIM_ASSESSMENT_STATE`
- `CLAIM_DECISION_STATE`
- `CLAIM_REVIEW_HISTORY`
- `CLAIM_DISCREPANCY_STATE`
- `MUTUAL_AID_POOL_STATE`
- `POOL_STRESS_EVENT_STATE`
- `BUSINESS_INTERRUPTION_COMPONENT_STATE`
- `CLAIM_TO_FINANCE_PAYMENT_HANDOFF`
- `CLAIM_TO_RECOVERY_PROJECT_HANDOFF`
- `CLAIM_TO_SUPPLY_CHAIN_HANDOFF`
- `CLAIM_TO_ARCHITECTURE_INFRASTRUCTURE_HANDOFF`
- `CLAIM_TO_CASES_REVIEW_HANDOFF`
- `CLAIM_TO_MINECRAFT_PROJECTION`
- `CLAIM_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 117

Do not infer:

- physical damage -> covered loss;
- covered loss -> approved payout;
- approved payout -> payment received;
- payment received -> recovery complete;
- pre-existing damage -> fraud;
- claim error -> deception;
- duplicate record -> theft;
- denial -> institutional corruption;
- dispute -> criminal case;
- maintenance issue -> negligence;
- mutual pool -> government authority;
- insured asset -> insurer ownership;
- battle damage -> monetary property value;
- battle transcript -> claim decision;
- Minecraft block destruction -> authoritative claim loss;
- repaired Minecraft model -> closed claim;
- captured Pokémon -> insurable inventory;
- Pokémon Injury -> depreciation;
- released Pokémon -> asset disposal;
- wild Pokémon involvement -> automatic liability;
- generic Trainer Feature status handlers -> insurance mechanics;
- generic status-state mutation -> property-damage system.

## PTU/Caelo validation state

The complete primary Caelo corpus was not reliably available as an invocable source during this run.

Super PTU Online Helper was not exposed as an invocable capability.

No new PTU/Caelo mechanic for insurance, property loss, business interruption, liability, claims, valuation, fraud, repair funding or risk pooling was validated.

Potential PTU mechanics remain relevant only where a specific encounter actually uses them, for example:

- movement/escort/interception;
- environmental hazards;
- actual Move/Ability/Item/Trainer Feature behavior;
- Capture/Command/Care rules if a scenario also involves a Pokémon.

Those mechanics never decide claim coverage or financial value.