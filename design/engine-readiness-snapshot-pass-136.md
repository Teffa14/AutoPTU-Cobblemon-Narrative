# Engine Readiness Snapshot — Pass 136

Status: IMPLEMENTATION EVIDENCE SNAPSHOT. Not canon.
Date: 2026-08-23

## Purpose

This snapshot records live AutoPTU-Java and AutoPTU evidence relevant to the food-safety, kitchen-traceability and venue encounter concepts added in Pass 136. Both engine repositories remain read-only for this task.

A representative mechanic never promotes an entire capability family by itself.

## Inspected heads

AutoPTU-Java:

`7a657fcca6d986a1010af65faa9dc2208eaa94a6`

Latest inspected commit:

`Derive pre-damage threatened area from authoritative state (#166)`

This slice derives the threatened area for pre-damage reactions from canonical attacker/defender positions and the effective Move inside the Java core. Minecraft/Cobblemon does not supply those threatened tiles.

Immediately preceding work also includes:

- `9819146364b67da51d039c5d380c8a4aa3c378c5` — pre-damage pipeline ordering;
- `ebfdf7b29da5cdde9b7df7bd6d193ae03f5203f7` — Telepathy pre-damage reaction;
- `aefc058328a9217d634477835a4851d521aaeccb` — one authoritative reaction-movement path;
- `7de79dcd30b241d439724050fb24ee893a7c5c63` — Push/Pull instruction parsing without generic execution.

AutoPTU Python:

`8d7de9f70d301e136672b66f460f9233a463cc7a`

Latest inspected Python commit:

`Career: preserve rollback before exhausted decision dead ends (#73)`

This is Career resilience work and does not change the tactical classification below.

## PTU food evidence boundary

Current project data contains PTU 1.05 trainer/class/feature material including Chef/Food-related definitions.

That proves the mechanical concepts exist in the rules corpus. It does not prove:

- spoilage mechanics;
- foodborne disease;
- kitchen contamination simulation;
- cooking-temperature rules;
- generic poisoning through ordinary meals;
- venue inspection mechanics;
- Java parity for the full Chef/Food catalog.

The existing narrative Food layer already keeps mechanical food definitions under PTU/Caelo/AutoPTU authority.

## Java README boundary

The current AutoPTU-Java README still explicitly lists as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent reaction work narrows specific paths but does not override this repository-level boundary.

## Permanent capability map

### targeting/footprints/range/LoS — VERIFIED

Substantial parity-backed targeting geometry exists.

The latest Java slice further ensures pre-damage threatened-area geometry is derived from authoritative battle state.

This cannot be reused as a model for contamination spread, kitchen exposure radius or food-service traceability.

### base movement legality — VERIFIED

Ordinary Shift legality is substantially verified for the ported scope.

Kitchen staff movement and diner evacuation remain overworld concerns unless they are actual combatants.

### complete movement including push/pull/knockback/interception/forced movement — BLOCKING

There is narrow reaction movement and Push/Pull instruction parsing.

Complete forced movement, interception, collision and general objective movement remain unfinished.

Pass 136 FULL encounters therefore cannot run live crowd evacuation or moving route-control objectives inside AutoPTU.

### core calculations — VERIFIED

Core battle calculations are verified for the ported scope.

Food-safety risk, spoilage, temperature, pathogen growth and contamination probability do not belong in this category.

### action economy/initiative — VERIFIED

Action-budget and initiative infrastructure remain substantially verified.

Food-service state does not modify initiative unless an exact PTU mechanic says so.

### full turn/round lifecycle — PARTIAL

Round transitions, delayed-hit timing, selected temporary effects, selected status timing and reaction slices exist.

The complete lifecycle remains unfinished.

### full stateful damage pipeline — PARTIAL

Recent Java work strengthens pre-damage ordering and authoritative reaction context.

The README still marks full damage incomplete.

A kitchen incident cannot write HP damage directly unless an exact validated battle effect produces it.

### status lifecycle — PARTIAL

Selected application, prevention, suppression and timing paths exist.

Foodborne illness, spoiled food, contamination or a restaurant complaint cannot create Poisoned/Badly Poisoned or another PTU Status automatically.

### terrain/weather/hazards/zones/reactions — BLOCKING

Reaction support is progressing, including Telepathy and one reaction-movement route.

The combined family remains incomplete. Kitchen spills, heat, smoke, broken equipment or suspect food cannot become custom zones/hazards by narrative declaration.

### move-specific behavior — PARTIAL

Representative Move paths exist, but catalog coverage remains incomplete.

If a food-service encounter separately invokes a Move such as Poison Gas, Ember, Water Gun or another environmental-looking Move, that Move still needs exact Java parity evidence.

### abilities — PARTIAL

Many individual Ability hooks have concrete evidence.

No Ability creates generic food-safety authority, contamination detection, refrigeration, purification or kitchen competence.

### items — PARTIAL

Item coverage remains incomplete.

Narrative possession of kitchen tools, containers, First Aid equipment or protective gear does not execute a PTU item effect by itself.

### Trainer Features/perks — PARTIAL

Generic Feature infrastructure and selected concrete effects exist, but the catalog is incomplete.

Chef class membership does not grant narrative inspection authority or automatically resolve food-safety state.

### AI legal-action infrastructure — VERIFIED

The engine can construct/filter legal battle choices for the ported scope.

It does not understand food holds, evacuation priorities, protecting staff, securing evidence or clearing a service area as tactical goals.

### AI tactical policy — BLOCKING

No complete objective-aware policy exists for Pass 136 goals such as:

- `EVACUATE`;
- `CLEAR_ROUTE`;
- `PROTECT_STAFF`;
- `PROTECT_TECHNICIAN`;
- `WITHDRAW`;
- `REACH_EXIT`;
- `SECURE_AREA`.

### Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

No parity-safe adapter exists.

Minecraft must not infer food safety, contamination, serving identity, lot parentage, safe temperature, PTU Status or closure authority from blocks/entities/particles.

## Pass 136 encounter dependencies

### Kitchen Shutdown During Service — FULL

Requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for live evacuation/interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL if invoked by exact mechanics;
- terrain/weather/hazards/zones/reactions — BLOCKING if the environment gains tactical effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

REDUCED:

Stop service, evacuate staff/diners and place food on hold in world state. Freeze a safe arena. AutoPTU resolves only remaining combatants. Food-safety investigation resumes afterward.

### Festival Stall Traceback — FULL

The investigation itself is overworld/non-combat.

Dynamic crowd routing requires complete movement, AI tactical policy and adapter/playback. Any actual battle mechanics remain dependent on the relevant partial families.

REDUCED:

Pause/reroute affected stalls outside battle. Conduct traceback and interviews in world state. If a confrontation occurs, use one static cleared location. The battle result cannot identify a source lot.

### Remote Lodge Supplier Withdrawal — FULL

This is primarily Food Safety + Supply Chains + Travel.

If a route encounter occurs, dynamic escort/clear-route goals require complete movement, AI tactical policy and adapter/playback. Lifecycle/damage/status/move/ability/item/Feature families remain partial as invoked.

REDUCED:

Keep inventory/menu decisions outside combat. Run any independent route confrontation as a conventional static encounter. Reduced food variety creates no hunger, starvation, morale or Food Buff penalty.

## Pass 136 overworld blockers

New requirements outside AutoPTU-Java:

- `FOOD_SAFETY_CASE` persistence;
- preparation-batch identity;
- parent ingredient-lot links;
- preparation-step history;
- food-handling observations;
- service-portion aggregation/privacy;
- safety hypotheses;
- food holds and dispositions;
- withdrawals/stop-use events;
- traceback/traceforward links;
- retained-sample provenance;
- Food Safety -> Supply Chain handoff;
- Food Safety -> Drinking Water handoff;
- Food Safety -> Outbreak handoff;
- Food Safety -> Toxicology handoff;
- Food Safety -> Care handoff;
- Food Safety -> Institutional Review handoff;
- world-state -> Minecraft presentation;
- explicit gate before any battle mechanic is created from food-service fiction.

## Explicit non-inferences

Pass 136 forbids:

- illness after eating -> venue caused it;
- shared restaurant -> shared contaminated food;
- bad smell -> unsafe food;
- suspect ingredient -> exposure confirmed;
- exposure -> diagnosis;
- diagnosis -> PTU Status;
- refrigerator fault -> all stock unsafe;
- food hold -> contamination confirmed;
- withdrawal/recall -> wrongdoing;
- traceability gap -> fraud/theft;
- cooked -> permanently safe;
- clean-looking kitchen -> safe food;
- Fire-type -> cooking authority;
- Ice-type -> refrigeration authority;
- Water-type -> potable-water authority;
- Poison-type -> toxin detector;
- Chef -> food-safety inspector;
- battle victory -> kitchen reopened or batch released.

## Unresolved mechanical/canon questions

- Exact PTU/Caelo Chef and Food/Digestion Buff rules enabled by this project.
- Whether Caelo defines spoilage, contamination, cooking, poisonous food or foodborne illness.
- Exact Item/Feature support in Java for any kitchen-relevant mechanic.
- Which Ouros institutions may inspect, close or reopen food venues.
- Whether Ouros distinguishes allergens, pathogens, toxins and spoilage as separate authored hazard classes.
- How much lot-level and serving-level data the world should persist.
- What diner/worker privacy rules apply.
- Which Pokémon may perform authored kitchen roles and what capability evidence is required.
