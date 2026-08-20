# Ouros Interspecies Ecological Relations Layer

Status: Proposed systems design. Not established Ouros canon.

## Purpose

Ouros already tracks populations, persistent wild collectives, individual Pokémon, habitats, migration, conservation, observation, seasonality and player-caused disturbance.

This layer adds persistent relationships between species, populations and collectives.

The goal is to let ecology produce believable consequences without turning every route into a full biological simulator or converting ecological behavior into unsupported PTU mechanics.

## 1. Core separation

Ouros should keep these states separate:

1. species-lore claim;
2. local ecological observation;
3. inferred ecological relationship;
4. population response;
5. tactical encounter;
6. mechanical battle result.

A Pokédex claim may support an authored species tendency.

A local observation may show the same behavior in Ouros.

Neither one automatically grants a combat bonus, a forced AI action or a permanent population change.

## 2. Ecological relationship schema

```yaml
ecological_relation:
  relation_id: null
  status: PROPOSED
  relation_type: UNKNOWN_ASSOCIATION
  source_actor_scope: null
  target_actor_scope: null
  location_scope_ids: []
  season_or_time_conditions: []
  environmental_conditions: []
  resource_refs: []
  observed_behavior_refs: []
  supporting_evidence_ids: []
  contradicting_evidence_ids: []
  confidence_band: unknown
  first_confirmed_event_id: null
  last_confirmed_event_id: null
  current_state: ACTIVE
  world_state_effect_refs: []
  mechanics_refs: []
  provenance_refs: []
  unresolved_questions: []
```

Possible actor scopes:

- species;
- regional population;
- persistent collective;
- persistent individual Pokémon;
- temporary aggregation.

The narrowest supported scope should be preferred.

## 3. Relation taxonomy

Candidate narrative relation types:

- PREDATION_OBSERVED
- PREDATION_PRESSURE_SUSPECTED
- SCAVENGING
- RESOURCE_COMPETITION
- SHARED_RESOURCE_USE
- HOST_PARASITE_RELATION
- SHELTER_ASSOCIATION
- FOLLOWING_ASSOCIATION
- MIXED_SPECIES_FORAGING
- HABITAT_ENGINEERING
- PROTECTIVE_ASSOCIATION
- DISTURBANCE_RESPONSE_LINK
- TEMPORARY_ASSOCIATION
- UNKNOWN_ASSOCIATION

Terms such as MUTUALISM, COMMENSALISM or PARASITISM should be used only when the evidence actually supports the scientific interpretation.

If the system only knows that two species repeatedly appear together, `UNKNOWN_ASSOCIATION` is better than pretending to know why.

## 4. Direction matters

Relationships can be directional.

```yaml
source: species_a
target: species_b
relation_type: SCAVENGING
```

This does not automatically create the inverse relation.

A predator/prey relation is also not a permanent label attached to a species.

The same species may:

- hunt one species;
- be hunted by another;
- scavenge from a third;
- compete with a fourth;
- share shelter with a fifth.

## 5. Evidence before inference

Every persisted ecological relation should point to evidence.

Useful evidence classes:

- direct field observation;
- repeated observation;
- camera record;
- acoustic record;
- tracks/sign;
- remains or feeding evidence;
- historical record;
- trusted Pokédex/species lore;
- researcher report;
- local testimony;
- observed co-movement;
- habitat/resource correlation.

A researcher may infer a relation before the world treats it as confirmed.

```yaml
ecological_claim:
  claim_id: null
  relation_id: null
  claimant_id: null
  claim_type: null
  confidence: null
  evidence_ids: []
  alternative_explanations: []
  review_state: OPEN
```

## 6. Species lore versus Ouros observation

Some relationships are strongly established by official Pokémon species descriptions.

Examples from research include:

- Mantine/Remoraid association;
- Heatmor/Durant predation;
- Paras/Parasect host-fungus relationship;
- Arrokuda participating in both hunting and being hunted.

Ouros may use those as authored species baselines where appropriate.

However:

- a species tendency is not proof that every individual behaves the same way;
- local habitat may change the relation;
- absence of the expected partner may create a research question;
- unusual behavior should remain possible if it has an explicit cause.

## 7. Sparse ecological network

Do not build a complete food web for every species in every route.

Persist only meaningful edges.

A relation becomes persistent when at least one condition applies:

- official species lore establishes it;
- repeated local observation establishes it;
- it changes encounter ecology;
- it changes a settlement, route or protected area;
- it produces a research program;
- a player-caused action changes it;
- it anchors a recurring quest/arc;
- it involves a persistent Pokémon or collective.

This keeps the world legible and computationally bounded.

## 8. Ecological pressure

A relation may generate pressure without immediately changing population size.

```yaml
ecological_pressure:
  pressure_id: null
  relation_id: null
  pressure_type: null
  affected_scope_id: null
  location_ids: []
  observed_signs: []
  severity_band: unknown
  trend: unknown
  cause_confidence: unknown
  active_since_event_id: null
```

Candidate pressure types:

- altered feeding location;
- changed activity time;
- nesting displacement;
- route avoidance;
- shelter competition;
- resource depletion;
- scavenger concentration;
- increased defensive behavior;
- changed aggregation size;
- temporary local absence.

Pressure is a world-state signal. It is not a combat modifier.

## 9. Trophic cascades need causal proof

Ouros may eventually model a chain such as:

resource decline -> prey relocation -> predator relocation -> scavenger redistribution -> settlement sightings change.

But the graph must preserve each causal edge separately.

The system must not generate large ecosystem cascades from one weak correlation.

A useful causal record:

```yaml
ecological_causal_edge:
  cause_state_id: null
  effect_state_id: null
  evidence_ids: []
  confidence: null
  reversible: unknown
  competing_cause_ids: []
```

## 10. Battle outcomes are not ecological outcomes

Hard guardrails:

- Fainted does not mean dead.
- Injury does not mean eaten.
- Captured does not automatically create population decline.
- Losing one tactical encounter does not erase a collective.
- Retreat does not prove permanent displacement.
- A Trainer defeating a predator does not make the prey population safe forever.
- A Pokémon using a damaging Move during an ecological encounter does not prove predation.

Ecological writeback requires a separate world-state decision based on the actual encounter context.

## 11. Predation should not moralize species

Predators are not villains because they hunt.

Prey species are not automatically victims requiring rescue.

A conservation actor may choose not to intervene in ordinary ecological behavior.

Intervention becomes justified by authored context such as:

- human-caused disturbance;
- artificial confinement;
- introduced hazards;
- a protected individual under active care;
- a settlement safety conflict;
- a research protocol;
- an abnormal population pressure;
- a crisis event.

The generator should present the situation and relevant stakes rather than assign moral alignment to ecological roles.

## 12. Association is not friendship

Two Pokémon repeatedly traveling together may have a stable ecological association.

Ouros must not infer:

- affection;
- friendship;
- ownership;
- loyalty;
- command hierarchy;
- family relation;
- consent to capture;
- battle-team coordination.

Those belong to other systems and require their own evidence.

## 13. Mixed-species collectives

The existing wild-collective layer already permits mixed-species associations.

This layer explains why such an association may persist.

```yaml
mixed_species_association:
  association_id: null
  collective_ids: []
  relation_ids: []
  shared_resource_ids: []
  observed_coordination_ids: []
  persistence_conditions: []
```

A mixed group can share a resource without acting as one tactical team.

## 14. Ecological opportunities

Ecological change can generate content without forcing combat.

Possible activities:

- field observation;
- trail-camera deployment;
- population survey;
- tracking;
- habitat restoration;
- route redesign;
- temporary access closure;
- resource supplementation only when authored/validated;
- rescue after artificial disturbance;
- investigation of unusual remains/sign;
- mapping a feeding or migration corridor;
- mediation between settlement needs and conservation goals;
- monitoring after a player intervention.

## 15. Research loop

A good ecological investigation follows:

observation -> hypothesis -> additional evidence -> competing explanation -> provisional conclusion -> monitoring.

Examples:

- fewer prey observed does not prove predator increase;
- more scavengers does not prove more deaths;
- a predator appearing near a town does not prove aggression toward people;
- a species disappearing from a survey does not prove local extinction.

This reuses the science, observation and photography layers.

## 16. World Pulse integration

Ecological relations can participate in World Pulse only at coarse granularity.

A pulse may update:

- activity band;
- location band;
- pressure trend;
- resource availability band;
- aggregation state;
- survey freshness;
- relation confidence after new evidence.

It should not simulate every hunt or every meal.

## 17. Seasonal integration

Relations may change by season or time.

Examples:

- predator pressure concentrated around nesting windows;
- scavenger association around seasonal fisheries;
- competition only during drought;
- shared shelter during storms;
- different day/night interactions.

Seasonal state modifies when the relation is plausible. It does not automatically apply battle modifiers.

## 18. Settlement integration

Human activity can alter relation edges.

Possible causes:

- waste availability;
- lighting;
- agriculture;
- construction;
- transport schedules;
- fishing;
- restoration;
- tourism;
- protective barriers;
- artificial water sources.

A player may therefore change ecology indirectly by changing infrastructure.

## 19. Conservation integration

Protected-area management can react to relation evidence.

Examples:

- move a visitor path away from a feeding corridor;
- close one zone during a vulnerable seasonal window;
- monitor an introduced resource competitor;
- preserve a habitat-forming species;
- avoid intervening in ordinary predation despite public pressure.

The conservation layer remains responsible for policy/stewardship state.

## 20. Persistent Pokémon integration

A specific persistent Pokémon may participate in an ecological relation.

```yaml
individual_ecological_role:
  pokemon_entity_id: null
  relation_ids: []
  observed_events: []
  current_role_claims: []
```

The record describes observed behavior.

It does not fix the Pokémon's personality or future choices.

## 21. Encounter-generation gate

Before generating an ecological combat encounter, answer:

- What relation or pressure exists before battle?
- Why are these exact actors here?
- What outcome would make sense besides KO?
- Which actors can withdraw?
- What persists if the players do nothing?
- What world-state change follows each plausible resolution?
- Which battle mechanics are actually implemented?

If the encounter cannot answer those questions, keep it as observation/world-state content or use a simpler battle.

## 22. Encounter contract — Feeding Corridor Disturbance

### Narrative premise

A transport project has concentrated one wild species into a narrow feeding corridor already used by another species. Repeated conflict is now observed near the same chokepoint.

### Full intended version

The battle space supports two wild groups with distinct goals. One group attempts to cross toward a resource. The other attempts to hold or use the same area. Players may separate, redirect, protect, withdraw or engage.

### Reduced version

Resolve route/resource pressure in world state. If a fight occurs, instantiate only the immediate hostile participants on a static grid. Other animals and the resource remain outside the tactical scene. After battle, update the ecological relation based on the actual player action rather than the KO result alone.

### Capability dependencies

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING for live corridor crossing and interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when exact statuses are used;
- terrain/weather/hazards/zones/reactions — BLOCKING if corridor hazards or environmental zones are active;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for CROSS/PROTECT/WITHDRAW goals;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

## 23. Encounter contract — Opportunistic Scavengers

### Narrative premise

After a storm or battle elsewhere, scavenger Pokémon begin arriving around a damaged location. Residents interpret the concentration as a new threat.

### Full intended version

Scavengers enter over time, investigate resources, withdraw if displaced and react to other wild actors. The objective may be to protect specific supplies or create distance rather than defeat every Pokémon.

### Reduced version

Keep arrival waves and resource interaction in world state. If one subgroup becomes hostile, use a single static encounter. Do not make low HP, Injuries or fainted combatants automatically attract scavengers.

### Capability dependencies

- targeting/range/LoS — VERIFIED;
- base movement — VERIFIED;
- complete movement — BLOCKING for autonomous approach/withdrawal and interception;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle — PARTIAL for timed arrivals;
- damage/status — PARTIAL;
- terrain/hazards/zones/reactions — BLOCKING if storm debris matters tactically;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for investigate-resource/withdraw behavior;
- adapter/playback — BLOCKING.

## 24. Encounter contract — Nest Defense Survey

### Narrative premise

Researchers need to survey a route where a persistent collective is defending a nesting site from another species. The goal is information and safe passage, not elimination.

### Full intended version

Actors can guard zones, approach/withdraw, block access and react to threats. Players may choose a longer route, wait, deter one group or retreat.

### Reduced version

Keep the nest, eggs/young and most wildlife outside the tactical grid. If battle becomes unavoidable, use a conventional encounter against only the immediate aggressive subgroup. Survey progress is resolved before/after battle through world state and validated PTU checks.

### Capability dependencies

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception — BLOCKING for live passage/zone defense;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- damage/status — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for guarded zones or environmental effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for defend-nest/withdraw/pass-through objectives;
- adapter/playback — BLOCKING.

## 25. Mechanics boundary

This layer must never invent:

- ecological damage;
- hunger meters;
- predator bonuses;
- prey penalties;
- morale;
- pack tactics;
- fear checks;
- flee thresholds;
- death/consumption;
- Injury-based targeting;
- feeding heals;
- scavenger bonuses;
- parasitic status effects;
- capture restrictions;
- Ability behavior.

If a species relationship is mechanically expressed through an existing Move, Ability, Capability, Item or Trainer Feature, that exact mechanic must be verified against PTU/Caelo and the engine before use.

## 26. Canon promotion gate

An ecological relation may enter canon only when:

- the involved species/populations are canon for the location;
- the relation has authored or evidence-backed support;
- contradictory evidence is represented where relevant;
- it does not silently overwrite existing encounter ecology;
- it does not create unsupported mechanics;
- its consequences are compatible with conservation, science and seasonal state;
- multiplayer-visible information respects knowledge boundaries.

## Design conclusion

The important object is a sparse graph of evidence-backed ecological relationships.

That graph gives Ouros more living encounters, better research stories and stronger environmental consequences while keeping PTU mechanics authoritative and keeping Minecraft from inventing ecology-driven combat rules.