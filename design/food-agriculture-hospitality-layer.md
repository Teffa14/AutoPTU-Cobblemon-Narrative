# Ouros Food, Agriculture & Hospitality Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models material provenance, workshops, trade, settlements, ecology, travel, public events, care and social institutions. This layer gives food its own world-state model because food crosses all of those systems while also carrying PTU mechanics through Chef, Berries and Digestion/Food Buffs.

The design goal is to make agriculture, cooking and hospitality meaningful careers and sources of stories without adding compulsory hunger simulation or duplicating PTU item logic in Minecraft.

## 1. Six separate food concepts

Never collapse these into one field.

```yaml
food_concepts:
  mechanical_food_ref: null
  physical_batch_or_item_id: null
  prepared_dish_instance_id: null
  recipe_knowledge_ref: null
  cultural_food_practice_id: null
  meal_or_service_event_id: null
```

`mechanical_food_ref` belongs to authoritative PTU/Caelo/AutoPTU rules.

The other fields describe world provenance, who prepared or served something, where ingredients came from, who participated, and why the event matters.

A culturally important dish does not automatically gain a stronger Digestion Buff. A mechanically powerful food does not automatically become culturally important.

## 2. Food batch and provenance

Use the existing material provenance system for bulk inputs, extended with food-specific context.

```yaml
food_batch:
  batch_id: null
  mechanical_material_ref: null
  source_location_id: null
  producer_or_gatherer_ids: []
  production_method: null
  harvest_event_id: null
  season_ref: null
  ecological_context_ids: []
  storage_location_id: null
  current_quantity_state: null
  quality_claim_ids: []
  contamination_case_id: null
  transformed_into_ids: []
  rules_validation_required: true
```

`quality_claim_ids` stores claims such as "festival grade" or "best orchard harvest" as social information. It must not silently create mechanical quality tiers.

## 3. Agricultural site

```yaml
agricultural_site:
  site_id: null
  site_type: null
  location_id: null
  operator_ids: []
  steward_ids: []
  institution_id: null
  cultivated_resource_refs: []
  wild_resource_refs: []
  water_dependency_ids: []
  soil_or_habitat_state_ids: []
  transport_dependency_ids: []
  storage_dependency_ids: []
  pokemon_participant_ids: []
  capacity_state: NORMAL
  seasonal_state: null
  current_problems: []
  visitor_access: null
```

Candidate `site_type` values:
- FARM
- ORCHARD
- BERRY_GROVE
- GREENHOUSE
- APIARY
- FISHERY
- HERB_GARDEN
- MUSHROOM_CULTURE
- COMMUNITY_GARDEN
- RESEARCH_PLOT

These are narrative/infrastructure labels. They do not establish legal PTU yields.

## 4. Pokémon participation

Pokémon should feel embedded in work without becoming generic machinery.

```yaml
pokemon_work_participation:
  pokemon_entity_id: null
  site_or_kitchen_id: null
  activity_type: null
  observed_behavior_refs: []
  required_capability_refs: []
  capability_validation_state: pending
  voluntary_or_handler_directed: null
  schedule_state: null
```

Possible activities include watering, carrying, heating, cooling, scent detection, pollination support, pest warning, tracking, foraging or guarding.

The generator may propose the narrative role. Execution requires authoritative capability evidence for the individual Pokémon when the activity depends on a PTU capability or Move.

Species stereotypes are insufficient.

## 5. Crop/harvest state

Ouros should not simulate every seed unless a feature needs that resolution.

```yaml
cultivation_cycle:
  cycle_id: null
  site_id: null
  resource_ref: null
  started_at: null
  broad_stage: null
  relevant_condition_ids: []
  expected_window: null
  disruption_ids: []
  authoritative_yield_pending: true
```

Suggested broad stages:
- PLANNED
- ESTABLISHED
- GROWING
- READY_WINDOW
- HARVESTED
- FAILED
- DORMANT

These stages exist to support stories and schedules. Exact growth time and yield remain rules/implementation data when mechanically relevant.

## 6. Compression rule

Routine agriculture should disappear into background progression.

Do not create a quest for:
- watering a healthy field every day;
- feeding routine staff meals;
- harvesting a normal crop when no choice exists;
- restocking a restaurant from a functioning supply route;
- cooking a standard legal recipe with all requirements met.

Create playable content when the action intersects:
- ecological change;
- a missing or contaminated supply;
- cultural conflict;
- unusual Pokémon behavior;
- route disruption;
- a public event;
- a relationship or mentorship milestone;
- a case/investigation;
- a meaningful capacity decision;
- a player-authored professional goal.

## 7. Recipe identity versus mechanical recipe

```yaml
recipe_record:
  recipe_record_id: null
  mechanical_recipe_ref: null
  local_name: null
  creator_or_lineage_claim_ids: []
  culture_or_region_ids: []
  institution_ids: []
  ingredient_pattern_refs: []
  preparation_claim_ids: []
  history_event_ids: []
  teaching_access_state: null
  public_or_private: null
  rules_validation_required: true
```

`mechanical_recipe_ref` points to a PTU/Caelo definition if one exists.

The narrative system may track a family's version, a town's presentation style, a chef's authorship claim or a festival tradition. It may not rewrite the mechanical effect by changing flavor text.

## 8. Culinary tradition

```yaml
culinary_tradition:
  tradition_id: null
  region_or_community_ids: []
  food_or_method_refs: []
  historical_claim_ids: []
  seasonal_event_ids: []
  associated_location_ids: []
  current_practitioner_ids: []
  variation_ids: []
  contested_claim_ids: []
```

A tradition can have several legitimate variants. The generator should avoid choosing a single "authentic" version unless canon explicitly establishes one.

Food culture can produce:
- identity;
- migration history;
- trade relationships;
- intergenerational mentorship;
- festival rituals;
- local pride;
- disagreement;
- tourism;
- conservation pressure.

None of these require combat bonuses.

## 9. Kitchen and venue state

```yaml
food_venue:
  venue_id: null
  venue_type: null
  location_id: null
  operator_ids: []
  staff_ids: []
  pokemon_staff_ids: []
  menu_offer_ids: []
  kitchen_or_tool_refs: []
  supply_route_ids: []
  storage_capacity_state: null
  seating_or_service_capacity_state: null
  public_access_state: OPEN
  current_backlog: []
  current_problems: []
  reputation_claim_ids: []
  event_history_ids: []
```

Candidate venue types:
- RESTAURANT
- CAFE
- MARKET_STALL
- COMMUNITY_KITCHEN
- INN_KITCHEN
- TRAVEL_CANTEEN
- FESTIVAL_VENDOR
- SCHOOL_CANTEEN
- GYM_CANTEEN
- MOBILE_KITCHEN

A venue can become a social anchor independent of whether it sells mechanically relevant food.

## 10. Menu offers

```yaml
menu_offer:
  offer_id: null
  venue_id: null
  narrative_dish_ref: null
  mechanical_food_ref: null
  availability_requirements: []
  supply_dependency_ids: []
  seasonal_window: null
  current_availability: true
  limitation_reasons: []
```

Do not expose an unsupported mechanical food effect just because a dish exists on the menu.

A venue may serve ordinary narrative meals with no battle effect at all.

## 11. Meal/service event

```yaml
meal_event:
  event_id: null
  venue_or_site_id: null
  host_ids: []
  participant_ids: []
  pokemon_participant_ids: []
  served_dish_ids: []
  source_batch_ids: []
  public_or_private: null
  conversation_topic_ids: []
  relationship_fact_ids: []
  cultural_context_ids: []
  world_state_outputs: []
```

A meal can record who shared a table, what was discussed or what public event occurred. It must not infer friendship, romance, forgiveness or other private emotional states from co-presence.

## 12. Hospitality as access

Hospitality can change access to information and places without becoming a morality score.

Examples:
- a worker lets known regulars hear about tomorrow's delivery problem;
- an inn provides a staging room for an expedition;
- a community kitchen becomes a crisis coordination point;
- a chef introduces a player to a supplier;
- a market association invites previous helpers to a planning meeting.

These outcomes should follow relationships, institutional standing or prior events, not arbitrary "eat five meals to unlock faction" counters.

## 13. Food and ecology

Food production can alter ecology in both directions.

Possible causal links:
- flowering orchard changes pollinator activity;
- waste attracts scavengers;
- irrigation creates temporary habitat;
- pesticide/pollution concerns alter local populations;
- fishery pressure changes aquatic encounters;
- storm damage removes a food source;
- a rare migration creates unusual demand or conservation restrictions;
- a market creates predictable feeding opportunities for urban Pokémon.

The world graph must record the causal connection before encounter tables change.

## 14. Food safety and care boundary

Food-related illness belongs partly to the care and case systems.

Keep these separate:
- observed symptoms;
- suspected food/source;
- evidence chain;
- authoritative mechanical status;
- diagnosis;
- venue reputation/public rumor.

A rumor that a restaurant caused poisoning is not truth. A PTU status cannot be added because an NPC reports nausea.

## 15. Perishability policy

Perishability is potentially useful but dangerous as repetitive bookkeeping.

Default policy:
- ordinary food stock uses broad freshness/capacity state;
- exact spoilage timers are not simulated unless a validated mechanic or authored scenario needs them;
- named/significant batches may track storage incidents;
- crisis or transport delays may change availability without deleting player inventory arbitrarily.

Suggested broad states:
- FRESH
- STABLE
- LIMITED_WINDOW
- QUESTIONABLE
- SPOILED_CONFIRMED

`QUESTIONABLE` is an observation/claim state, not an automatic mechanical effect.

## 16. Seasonal and public-food events

Markets, harvest days, cooking exhibitions and communal meals can combine existing systems:
- public event layer;
- contest/performance layer;
- settlement capacity;
- travel demand;
- supply routes;
- public memory;
- hospitality venues;
- ecology.

A food festival does not automatically require a Contest or battle.

## 17. Professional progression without grind

Possible non-mechanical narrative milestones for a food-focused character:
- first commissioned event;
- trusted supplier relationship;
- apprenticeship completed;
- venue opened or restored;
- menu tradition documented;
- emergency kitchen successfully operated;
- ingredient source conserved;
- invitation to a regional event;
- apprentice trained;
- public dispute resolved;
- signature service recognized.

These are Chronicle/career states. They do not grant PTU Features or Chef effects automatically.

## 18. Integration with material culture layer

Use `design/material-culture-economy-crafting-layer.md` for generic object provenance, crafting validation, workshops, commissions, repairs and supply chains.

This food layer adds:
- cultivation cycles;
- food batches;
- kitchens/venues;
- menus;
- recipe cultural identity;
- meal events;
- broad perishability;
- agricultural/ecological feedback.

Do not duplicate the generic production model.

## 19. Engine capability mapping

Food becomes combat-relevant only when an authoritative food item or Chef interaction enters battle.

Likely categories:
- `items`: Food item identity, consumption/trade behavior and item effects.
- `abilities`: Harvest, Lunchbox, Gluttony or other validated Ability interactions.
- `Trainer Features/perks`: Chef Features and any approved food-related Trainer rules.
- `status lifecycle`: food effects that cure or interact with statuses.
- `full turn/round lifecycle`: duration, timing and once-per-scene/round interactions.
- `full stateful damage pipeline`: food or Ability effects modifying damage where applicable.
- `move-specific behavior`: only where a legal Move explicitly interacts with items/food.
- `Minecraft/Cobblemon/Craftics adapter/playback support`: presenting authoritative consumption/events in-world.

Agriculture, cooking scenes and restaurant service can exist without tactical combat support.

## 20. Encounter contract — Orchard Windbreak

Narrative premise:
A powerful wind event is driving a wild flock into an orchard while workers try to secure fragile structures and keep both Pokémon and crops safe.

FULL version:
The tactical arena includes changing wind/hazard zones, breakable/interactive windbreak positions and a PROTECT/CLEAR_ROUTE objective. Wild Pokémon AI prioritizes escape routes and shelter rather than pure defeat.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if wind forces displacement
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL if battle items are used
- Trainer Features/perks — BLOCKING if Chef/Survivalist features alter the battle
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

REDUCED version:
Workers and crops remain outside the grid. Wind is an overworld access/state problem only. Players resolve one or more ordinary legal encounters at fixed orchard chokepoints, then choose an overworld evacuation/restoration action. No forced movement, wind damage, crop HP or protected-target logic is simulated.

## 21. Encounter contract — Cellar Spill

Narrative premise:
A storage accident opens a route into a cellar used by wild Pokémon, forcing the venue to secure the area before service can resume.

FULL version:
Slippery/spill zones affect movement, interactable storage objects matter to objectives, and combatants may need to prevent further breakage.

Capability dependencies:
- terrain/weather/hazards/zones/reactions — BLOCKING
- complete movement including forced movement — potentially required if slipping/displacement is mechanical; currently BLOCKING
- AI tactical policy — BLOCKING for object-aware behavior
- adapter/playback — BLOCKING
- ordinary targeting/base movement/core/action infrastructure — VERIFIED
- lifecycle/damage/moves/abilities/items — PARTIAL as applicable to chosen opponents

REDUCED version:
The spill is represented by static blocked tiles or occurs outside the tactical grid. Players clear an ordinary legal encounter, then resolve cleanup and inventory consequences as overworld world-state actions. No scripted slip or barrel damage is added.

## 22. Encounter contract — Market Delivery Intercept

Narrative premise:
A food delivery is caught in a route dispute or wild disturbance shortly before a public event.

FULL version:
A convoy-style PROTECT or BREAK_THROUGH battle allows attackers, defenders and route geometry to matter while delivery state is preserved through authoritative events.

Capability dependencies:
- objective support for PROTECT/BREAK_THROUGH — not yet proven by core contract
- complete movement/interception — BLOCKING if physical protection matters
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING
- ordinary legal battle families — mixed VERIFIED/PARTIAL as above

REDUCED version:
The delivery remains an overworld actor outside the grid. A standard encounter decides whether the route segment becomes safe. The shipment advances only after a separate authoritative overworld transition.

## 23. Current readiness snapshot

Snapshot basis: AutoPTU-Java `main` through commit `b71a0c1887cd303b78099eed846293a9dd60ef2f`.

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: BLOCKING
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: BLOCKING
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

New evidence since the prior narrative snapshot:
AutoPTU-Java now has authoritative round-start cleanup for canonical temporary effects with Python-oracle parity. This strengthens the `full turn/round lifecycle` family but does not complete it; the category remains PARTIAL because full status, terrain, delayed-effect, Ability, Feature and other lifecycle populations/orderings are not yet verified.

Food-specific Java readiness remains insufficient for authoritative Food Buff execution. Existing Python AutoPTU food logic does not upgrade Java `items`, `abilities` or `Trainer Features/perks` by itself.

## 24. Anti-invention rules

The generator must not invent:
- hunger or starvation mechanics;
- daily calorie requirements;
- food poisoning mechanics;
- Chef recipes;
- recipe costs;
- Digestion Buff effects;
- Berry yields or growth timers;
- farming Skill checks;
- flavor bonuses;
- restaurant income formulas;
- spoilage timers;
- Pokémon work capabilities;
- crop-combat stats;
- festival scoring;
- food-based Loyalty changes.

All such mechanics require explicit PTU/Caelo and implementation review.

## 25. Promotion questions

Before a food/agriculture candidate becomes canon or executable content, confirm:
1. Does the culture/site/venue fit existing Ouros canon?
2. Are mechanical food references valid PTU/Caelo content?
3. Does Python AutoPTU encode any relevant behavior?
4. Does Java implement the exact required item/Ability/Feature/lifecycle slice?
5. Can Minecraft represent the state without duplicating PTU rules?
6. Does the scene create a meaningful decision rather than repetitive maintenance?
7. Are recipe authorship, ownership, food safety and ecological claims kept separate from canonical truth?
