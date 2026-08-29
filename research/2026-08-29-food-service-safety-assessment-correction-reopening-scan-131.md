# Ouros Food-Service Safety Assessment, Correction & Reopening Research — Pass 131

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file establishes Ouros canon.
Date: 2026-08-29

## Research question

What reusable narrative and systems structures can Ouros use for food-service venue concerns, operational assessment, corrective work, verification and scoped reopening without inventing disease mechanics, legal inspection powers, food-code thresholds, contamination rules, universal cooking checks or new PTU mechanics?

The purpose is continuity. A restaurant, café, market counter, festival kitchen, canteen or community meal site can have an operational problem whose history persists across observation, investigation, correction and later service. The system must preserve uncertainty and owner boundaries.

## Repository inspection before research

The complete recursive repository tree was inspected before writing. The tree was not truncated. Pass 130 was the current narrative head.

Adjacent owners were then inspected directly.

`design/food-agriculture-hospitality-layer.md` already owns food venues, kitchens, menus, food batches, provenance links, hospitality operations and the distinction between food-related narrative state and authoritative PTU food mechanics. It explicitly separates rumors of illness from diagnosis and tactical status.

`design/community-health-surveillance-cluster-investigation-continuity-extension.md` owns cross-source health-signal and cluster investigation. A venue may be an exposure hypothesis, but that layer preserves cluster definitions, health evidence and public-health investigation scope.

`design/batch-traceability-recall-quarantine-extension.md` owns post-distribution product/batch tracing, holds, recalls, recoveries, corrections and disposition when a particular distributed product or batch is in scope.

`design/cold-chain-temperature-controlled-custody-continuity-extension.md` owns temperature-controlled custody and excursions.

`design/drinking-water-quality-service-continuity-extension.md`, wastewater, waste/sanitation/pollution and Facility Maintenance own their respective infrastructure and operational facts.

`design/care-recovery-welfare-layer.md` owns individual observation, diagnosis, treatment and recovery.

The missing continuity is narrower: a food-service site itself can receive a concern, be assessed in a defined scope, accumulate observations and evidence, pause or narrow service, perform corrections, undergo follow-up verification and reopen by scope. No existing owner preserves that operational lineage end to end.

This pass therefore creates research support for that bridge only.

## Rejected duplicate direction

A contaminated-site remediation layer was considered first and rejected. The existing Waste, Sanitation, Recycling & Pollution layer already owns pollution incidents, cleanup/remediation and contamination-related environmental operations broadly enough that another layer would have duplicated established ownership.

## Prior-source avoidance

Pass 18 already researched Pokémon Café ReMix, Pokémon Camp, Poké Pelago, Pokémon Pokopia, The Slowpoke Shack, Pokémon Family Restaurant, Pokémon FarmVille, Pokémon Beekeeper, Pokémon Berry Shake, Pokémon Alexandrite and PTU cooking discussions. Those sources remain valid background but are not presented here as new findings.

Pass 117 already used CDC foodborne-outbreak investigation basics as evidence for Community Health. This pass therefore focuses on the distinct venue-environment question: what was observed in the establishment, what operational factor may matter, what correction occurred, and what verification supports a later service decision.

## Internal PTU / Caelo guardrail

The governing project source scan remains `research/2026-08-18-source-scan.md`.

That source scan supports persistent campaign structures, location identity, Jobs/Social/Wild/PvP/Raid/Gym/Dojo activity containers and explicit environmental mechanics when Caelo/PTU actually defines them. Toxic Ravine remains a useful positive example because its mechanical environmental effect is source-defined.

It does not establish universal mechanics for:

- food contamination;
- foodborne illness;
- sanitation ratings;
- cooking-temperature checks;
- spoilage;
- kitchen hazards;
- cleaning chemicals;
- allergen reactions;
- customer sickness;
- inspection authority;
- venue closure/reopening authority;
- generic Chef Skill checks for safety certification.

Therefore this pass treats food-service safety as world-state/evidence continuity unless an exact PTU/Caelo rule is separately verified.

## Pokémon source 1 — Mauville Food Court

Source:
https://bulbapedia.bulbagarden.net/wiki/Mauville_Food_Court

Mauville Food Court is useful because food preparation, customer seating, timed service and Pokémon battles coexist inside one operational venue. The customer is waiting for an order while a different activity occupies the same space.

Reusable high-level structure:

A food venue can contain several simultaneous operational scopes. The kitchen, counter, dining area, battle/service area, queue and ingredient storage do not need to share one binary `OPEN/CLOSED` state.

Ouros transformation:

- a corrective action may close one preparation station while another counter remains active;
- a dining room may remain accessible while food service is paused;
- a battle or entertainment area may be closed while the kitchen continues non-public preparation;
- a venue can reopen by spatial or service scope;
- customer-facing language can simplify the state while internal records remain precise.

Rejected imports:

- turn-count meal mechanics;
- battle-for-seat rules;
- reward economy;
- named dishes or trainers;
- any inference that food-service venues normally host battles.

## Pokémon source 2 — Seven Stars Restaurant

Source:
https://bulbapedia.bulbagarden.net/wiki/Seven_Stars_Restaurant

The Seven Stars Restaurant combines hospitality, scheduled operating hours, regular customers and battles. In the animated story, a theft interrupts food service, the food is later recovered, and service resumes.

Reusable high-level structure:

An interruption, recovery of missing material and resumption of service are distinct facts. Restoring physical possession of food or equipment does not by itself prove operational readiness; a later owner decision still exists.

Ouros transformation:

A venue incident can preserve:

1. interruption time;
2. affected service scope;
3. missing/damaged/uncertain material records;
4. recovery or replacement event;
5. assessment of whether the recovered material remains usable, only if an authorized owner has a rule for that determination;
6. service resumption event.

No named plot, theft sequence or character is copied.

## Pokémon source 3 — A Recipe for Success!

Source:
https://bulbapedia.bulbagarden.net/wiki/SM121

This episode shows two food-service operations under pressure at the same time. A family restaurant loses a key ingredient supply and becomes unusually busy while a forest café serves a changing set of Pokémon customers with different preferences. Helpers temporarily change staffing capacity.

Reusable high-level structures:

- ingredient availability, staffing capacity and food-safety state are separate axes;
- increased demand can change operational pressure without proving unsafe practice;
- temporary helpers can restore capacity but do not automatically establish competence for every role;
- a Pokémon customer population can be part of venue identity without granting the venue universal cross-species dietary knowledge.

Ouros transformation:

A safety assessment must not convert `BUSY`, `UNDERSTAFFED`, `INGREDIENT_SHORTAGE`, `EQUIPMENT_FAULT`, `CUSTOMER_COMPLAINT` or `HEALTH_SIGNAL` into synonyms. They may coexist, but each belongs to its own evidence chain.

Rejected imports:

- named recipes;
- dietary assumptions for species;
- the exact café/family storyline;
- any species-derived cooking or service competence.

## Pokémon source 4 — Restaurant Le Yeah / Lumiose restaurant structure

Source:
https://bulbapedia.bulbagarden.net/wiki/Restaurant_Le_Yeah

Lumiose restaurants separate courses, preparation timing, service and battle activity. Their operation is staged rather than represented as one instantaneous transaction.

Reusable high-level structure:

A prepared-meal service event can have a chronology with separate preparation, holding/waiting, service and completion points. For narrative investigation, the important lesson is provenance of timing rather than importing the game's exact turn targets.

Ouros transformation:

When a concern affects only a time window, the venue can retain service-event references so investigators can compare what was being prepared, what equipment was in use, which station was active and what records existed then.

The narrative layer does not calculate safe temperatures or durations.

## Public operational source 1 — CDC environmental assessments

Sources:
https://www.cdc.gov/restaurant-food-safety/php/investigations/environ-assess.html
https://www.cdc.gov/restaurant-food-safety/php/investigations/factors.html

CDC describes environmental assessment as a distinct component of foodborne-outbreak investigation. Investigators can interview managers/workers, observe preparation, review records and collect samples. CDC also separates contributing factors — how a problem occurred — from underlying root causes — why the contributing factor existed.

Reusable architecture only:

- direct observation, interview, record review and sample result are different evidence channels;
- a contributing-factor hypothesis and a root-cause hypothesis should not share one field;
- multiple visits can add or revise evidence;
- an assessment can remain incomplete;
- investigation of a venue can continue even while Community Health owns the larger cluster question.

Ouros transformation:

Create `venue_assessment_episode`, `observation_record`, `interview_reference`, `record_review_reference`, `sample_reference`, `contributing_factor_hypothesis`, `underlying_cause_hypothesis` and revision history. References should point to protected/private records rather than copy them into public Chronicle state.

Rejected imports:

- pathogens;
- real thresholds;
- health-department jurisdiction;
- legal inspection authority;
- American regulatory terminology as Ouros institutions;
- disease-specific practices.

## Public operational source 2 — CDC contributing-factor categories

Sources:
https://www.cdc.gov/restaurant-food-safety/php/investigations/contributing-factor-definitions.html
https://www.cdc.gov/restaurant-food-safety/php/investigations/ea-definitions.html

CDC differentiates contamination, proliferation and survival pathways and also treats built environment, water, food, people and processes as potentially relevant parts of the environment.

Reusable lesson:

The same observed outcome can have different mechanism hypotheses. A venue model should therefore avoid a single `contamination_source` truth field selected before evidence supports it.

Ouros transformation:

Use neutral mechanism categories only when a canon institution defines them. At the generic architecture level, preserve a more conservative structure:

- `observed_condition`;
- `suspected_process_step`;
- `suspected_input_or_environment`;
- `mechanism_hypothesis`;
- `supporting_evidence_refs`;
- `contradicting_evidence_refs`;
- `confidence_or_status` only if the authoring institution defines such a scale.

A water observation hands off to Drinking Water. An equipment fault hands off to Maintenance. A batch issue hands off to Batch Traceability. A health cluster remains Community Health's authority.

## Public operational source 3 — FDA inspection/corrective-action verification

Sources:
https://www.fda.gov/food/inspections-protect-food-supply/how-help-fda-food-safety-inspection-run-smoothly
https://www.fda.gov/food/inspections-protect-food-supply/foreign-food-facility-inspection-program-questions-answers

FDA material explicitly distinguishes an observed issue, a corrective action and later verification that the correction occurred. Verification may occur during the same inspection or later through follow-up mechanisms.

Reusable architecture:

`CORRECTION_REPORTED` must remain distinct from `CORRECTION_OBSERVED_OR_VERIFIED`.

Ouros transformation:

A venue can log a correction immediately while service remains limited pending whatever follow-up its canon owner requires. Later evidence can verify only the corrected scope. One verified sink repair, for example, does not verify the whole kitchen, building or menu.

Rejected imports:

- FDA forms;
- statutory authority;
- American inspection classifications;
- mandatory timelines;
- specific regulatory outcomes.

## Public operational source 4 — Codex HACCP structure

Source:
https://www.fao.org/4/w0124e/W0124E03.htm

The Codex material separates corrective actions from verification and recordkeeping. This distinction is useful as information architecture even when Ouros does not adopt HACCP as a universal setting institution.

Reusable lesson:

A corrective action can restore a process step while verification asks whether the relevant control is functioning. Both should leave records.

Ouros transformation:

- corrective action references what condition it addresses;
- verification references what evidence was checked;
- unresolved residual issues remain open;
- service decisions cite the scope they rely on;
- older failed or superseded corrections remain in history.

Rejected imports:

- mandatory CCP systems;
- real hazard classifications;
- prescribed monitoring frequencies;
- legal applicability;
- technical thresholds.

## Synthesis — required separation of facts

The strongest reusable invariants from this pass are:

`CUSTOMER_COMPLAINT_RECEIVED != SAFETY_PROBLEM_CONFIRMED`

`HEALTH_SIGNAL_EXISTS != VENUE_CAUSED_HEALTH_SIGNAL`

`VENUE_NAMED_IN_CLUSTER != VENUE_CONFIRMED_AS_SOURCE`

`UNUSUAL_ODOR_OR_APPEARANCE != CONTAMINATION_CONFIRMED`

`EQUIPMENT_FAULT_REPORTED != FOOD_AFFECTED`

`FOOD_BATCH_SUSPECTED != VENUE_PROCESS_AT_FAULT`

`ASSESSMENT_STARTED != ASSESSMENT_COMPLETE`

`OBSERVATION_RECORDED != CAUSE_IDENTIFIED`

`SAMPLE_COLLECTED != RESULT_AVAILABLE`

`CORRECTION_REPORTED != CORRECTION_VERIFIED`

`ONE_STATION_VERIFIED != ENTIRE_VENUE_VERIFIED`

`DINING_AREA_OPEN != FOOD_PREPARATION_AUTHORIZED`

`FOOD_PREPARATION_RESUMED != ALL_MENU_ITEMS_AVAILABLE`

`SERVICE_RESUMED != HEALTH_CLUSTER_CLOSED`

`VENUE_REOPENED != REPUTATION_RECOVERED`

`NO_NEW_COMPLAINTS != CORRECTION_EFFECTIVE`

These are narrative-state invariants, not real-world legal assertions.

## Evidence chronology pattern

A generic Ouros venue-safety episode can preserve the following sequence without requiring every step:

1. concern or observation arrives;
2. owner determines whether the concern falls within a canon assessment mandate;
3. an assessment scope is created;
4. current operations are recorded;
5. observations, interviews, records and/or samples are linked;
6. venue service may continue, narrow, pause voluntarily or change according to owner authority;
7. one or more hypotheses are recorded;
8. handoffs go to Food, Batch, Cold Chain, Water, Waste, Maintenance, Community Health, Care or another owner;
9. correction actions occur;
10. follow-up evidence verifies some or all corrected scopes;
11. an authorized owner records service/reopening state;
12. later monitoring or complaints can reopen a question without deleting the previous resolution.

The architecture must also support a case that closes with no confirmed venue safety problem.

## Mystery design lessons

A good food-service mystery does not require poisoning, sabotage or a dishonest cook.

Useful uncertainty can arise from:

- two service periods using different equipment;
- a repaired refrigerator whose records predate the repair;
- a batch delivered to multiple venues but implicated at only one;
- an ingredient substitution recorded after a menu board was printed;
- a dining room that reopened before one preparation station;
- two kitchens sharing one public address;
- a complaint timestamp that refers to consumption time while an operational log records preparation time;
- a venue blamed because it was memorable even though the common exposure is elsewhere;
- a Pokémon observed in a storeroom after food had already been removed;
- a staff member who recalls normal procedure while a maintenance record shows equipment behavior changed that day.

Resolution should come from scope, chronology and provenance whenever possible.

## Pokémon-agency guardrail

Pokémon presence in a kitchen, market or café cannot silently establish:

- contamination;
- cleanliness;
- pest status;
- worker status;
- food-handler authorization;
- health risk;
- ownership;
- culpability;
- species-wide behavior.

An individual Pokémon may have an authored job or venue relationship. Any mechanical capability used to heat, cool, clean, cut, carry, detect, diagnose or sanitize must come from authoritative PTU/Caelo state and verified engine support, not species flavor.

## Encounter design implications

Most venue-safety stories should remain noncombat investigations. Combat can appear if an independent hostile situation intersects the site.

Full mechanically rich encounters might ask for:

- controlled withdrawal from a kitchen/loading yard;
- Intercept or forced movement to protect a corridor;
- active heat, steam, spill or fire zones;
- delayed machinery/environmental effects;
- reactions when crossing protected areas;
- AI objectives such as WITHDRAW, PROTECT or CLEAR_ROUTE;
- semantic playback of closures, evacuated staff and protected evidence.

Those capabilities are not broadly verified today.

Reduced encounters should therefore perform the operational transition first in Ouros world state: pause service, remove customers/workers/food/samples/records, secure controlled equipment, define static safe geometry, then create a conventional BattleSpec with explicit combatants. Tactical victory can secure immediate access or perimeter control. It cannot determine food safety, identify a cause, verify a correction or reopen a venue.

## Engine live evidence — 2026-08-29

AutoPTU-Java live head inspected read-only:
`80f08b5d66f3451f70743ac0d4717f3a3dd21a0b` — `Derive intercept Justified bonus from server state (#275)`.

Current evidence remains localized to the Intercept route. Server-owned state now derives exact `Justified [Errata]`, Acrobatics/Athletics and Coaching inputs for that route. Terrain remains an explicit internal input whose broader authority contract is not frozen.

This does not prove every Intercept timing window, broad Push/Pull, broad Knockback, every forced-movement source, generalized reactions, environmental displacement, full terrain authority, all Ability behavior or all Trainer Features.

AutoPTU live head inspected read-only:
`729bae2d424963ff9bb3f4159c9a7ac9152128a7` — `Career: keep battle coordinates synced after viewport resize (#237)`.

That commit fixes presentation-coordinate synchronization after resize and explicitly does not change battle rules or outcomes. It does not verify semantic Minecraft/Cobblemon/Craftics adapter authority.

## Permanent capability result for this research

No promotions are justified.

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- complete movement including push/pull/knockback/interception/forced movement;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

## Mechanical questions left UNKNOWN

No source inspected in this pass establishes universal PTU/Caelo mechanics for:

- kitchen heat or steam damage;
- slippery-floor movement penalties;
- grease/fire zones;
- boiling-liquid hazards;
- food contamination as a status;
- foodborne disease transmission;
- allergen mechanics;
- spoilage timers;
- sanitation scores;
- cooking-temperature DCs;
- generic cleaning/sanitizing actions;
- generic inspection Skill checks;
- Chef authority to certify safety;
- Pokémon species automatically detecting unsafe food;
- Fire-type Pokémon automatically producing safe cooking heat;
- Ice-type Pokémon automatically providing refrigeration;
- Poison-type Pokémon automatically contaminating food;
- Water-type Pokémon automatically providing potable water;
- Moves, Abilities, Items or Trainer Features that universally approve/reject service operation.

These remain source-bounded questions.

## Canon questions deliberately left open

This pass does not establish:

- whether Ouros has food-service inspectors;
- which institutions can assess or restrict a venue;
- whether any region uses formal food codes;
- what professional titles exist;
- who may order closure or authorize reopening;
- what records are public;
- how temporary stalls or festival kitchens are treated;
- what role Pokémon may formally hold in kitchens;
- whether restaurants use ratings, permits or certificates;
- which historical food-service incidents exist in any region.

Those require explicit canon decisions later.

## Copyright / transformation boundary

External Pokémon works are used only for general structures such as mixed-use venue operation, staged service, interruption/recovery and staffing pressure. No distinctive plot, dialogue, characters, recipes, puzzle economy or proprietary progression loop is copied into Ouros.

Public operational guidance is used as evidence architecture only. Ouros does not inherit real-world law, regulatory thresholds, jurisdiction, institutional powers, pathogens, health advice or compliance procedures from those sources.