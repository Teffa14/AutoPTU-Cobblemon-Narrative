# Ouros Pokémon Social Learning & Behavioral Traditions Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already preserves persistent Pokémon individuals, wild collectives, population observations, migration, soundscapes, diel activity, field signs, urban adaptation and ecological change. This layer adds a missing distinction: a behavior can be learned locally and transmitted between Pokémon without becoming a species-wide rule or a PTU mechanic.

The layer exists to support long-lived stories where a local group develops, preserves, modifies or loses a learned practice.

It does not define Pokémon cognition universally. It does not create a mechanical “culture” stat. It does not grant Moves, Features, Skills, Abilities or tactical bonuses.

## 1. Core separation

Keep these states separate:

1. species-typical behavior;
2. individual behavior;
3. individual innovation;
4. local repeated behavior pattern;
5. evidence of social acquisition;
6. behavioral-tradition assessment;
7. current adoption within a population or collective;
8. public/scientific interpretation;
9. PTU mechanical state.

A behavior can be real without its mechanism of acquisition being known.

Example:

A group of Pokémon repeatedly opens a particular style of container.

Confirmed fact: several identified individuals perform the sequence.

Possible explanations:

- independent learning from the same environment;
- social learning;
- one persistent demonstrator influencing others;
- a species-typical behavior expressed under local conditions;
- previous human training;
- another cause.

The generator must not choose social learning merely because it makes a better story.

## 2. Behavioral observation

```yaml
behavior_observation:
  observation_id: null
  observed_at: null
  location_id: null
  observer_actor_ids: []
  pokemon_entity_ids: []
  collective_id: null
  population_ref: null
  behavior_domain: null
  behavior_description: null
  sequence_elements: []
  object_or_resource_refs: []
  environmental_context_refs: []
  nearby_actor_ids: []
  potential_demonstrator_ids: []
  recording_refs: []
  confidence: null
  provenance_refs: []
```

Observations describe what happened. They do not establish why it happened.

Candidate domains:

- VOCAL_REPERTOIRE
- FORAGING_TECHNIQUE
- ROUTE_OR_STOPPING_PRACTICE
- OBJECT_USE
- SHELTER_OR_SITE_USE
- RESOURCE_HANDLING
- DISPLAY_PATTERN
- HUMAN_INTERFACE_BEHAVIOR
- GROUP_COORDINATION
- PREDATOR_OR_THREAT_RESPONSE
- OTHER_OBSERVED_PATTERN

Domain labels remain narrative/scientific metadata.

## 3. Innovation event

An innovation is a candidate first appearance of a behavior within the tracked local history.

```yaml
innovation_event:
  innovation_id: null
  behavior_key: null
  first_observed_at: null
  innovator_entity_ids: []
  collective_id: null
  population_ref: null
  location_id: null
  prior_observation_search_refs: []
  ecological_change_refs: []
  human_contact_refs: []
  confidence: provisional
  alternative_origin_claim_ids: []
```

Hard rule:

“First observed” never means “first ever performed.”

A behavior can predate the archive.

## 4. Local behavior pattern

A local pattern can exist before social transmission is established.

```yaml
local_behavior_pattern:
  pattern_id: null
  behavior_key: null
  collective_id: null
  population_ref: null
  geographic_scope_ids: []
  first_confirmed_at: null
  last_confirmed_at: null
  observed_individual_ids: []
  observed_count_band: null
  observation_ids: []
  persistence_state: unknown
  candidate_explanations: []
  tradition_assessment_id: null
```

Suggested persistence states:

- SINGLE_OBSERVATION
- REPEATED
- MULTI_SEASON
- MULTI_COHORT
- HISTORICALLY_DOCUMENTED
- CURRENTLY_UNCONFIRMED
- DECLINING_POSSIBLE
- LOST_UNCONFIRMED

Do not use `LOST` as a strong world-truth state without sufficient monitoring evidence.

## 5. Transmission observation

Social transmission needs stronger evidence than co-location.

```yaml
transmission_observation:
  transmission_observation_id: null
  behavior_key: null
  observed_at: null
  location_id: null
  demonstrator_entity_ids: []
  observer_entity_ids: []
  observer_prior_experience_state: unknown
  demonstration_observed: true
  later_independent_performance_observation_ids: []
  exposure_duration_band: null
  alternative_learning_explanations: []
  confidence: null
  evidence_refs: []
```

A Pokémon standing near another Pokémon while both perform the same behavior is insufficient by itself.

## 6. Behavioral tradition assessment

The preferred Ouros term is `behavioral tradition` rather than assuming a universal theory of Pokémon culture.

```yaml
behavioral_tradition_assessment:
  tradition_id: null
  behavior_key: null
  population_ref: null
  collective_ids: []
  geographic_scope_ids: []
  status: candidate
  evidence_for_social_transmission_ids: []
  evidence_for_persistence_ids: []
  counterevidence_ids: []
  alternative_explanations: []
  transmission_mode_hypotheses: []
  first_assessed_at: null
  latest_revision_id: null
  canon_reference_ids: []
  mechanical_rule_refs: []
```

Suggested assessment states:

- OBSERVED_LOCAL_PATTERN
- SOCIAL_TRANSMISSION_SUSPECTED
- CANDIDATE_TRADITION
- WELL_SUPPORTED_TRADITION
- TRANSMISSION_UNRESOLVED
- DECLINING_UNCONFIRMED
- HISTORICAL_TRADITION

Only authored canon or sufficiently strong in-world research should use `WELL_SUPPORTED_TRADITION`.

## 7. Transmission mode is a hypothesis

Candidate modes:

- UNKNOWN
- HORIZONTAL_PEER_TO_PEER
- VERTICAL_PARENT_TO_OFFSPRING only when parentage is independently established
- OBLIQUE_EXPERIENCED_TO_NAIVE
- MULTIPLE_PATHWAYS
- HUMAN_MEDIATED_EXPOSURE
- INTERSPECIES_SOCIAL_INFORMATION
- INDEPENDENT_INNOVATION_STILL_PLAUSIBLE

Never infer kinship from age difference or co-location.

Never infer teaching from demonstration alone.

## 8. Teaching requires exceptional evidence

`TEACHING_HYPOTHESIS` should require evidence that an experienced individual modifies behavior in a way plausibly facilitating learning by another individual.

```yaml
teaching_hypothesis:
  hypothesis_id: null
  demonstrator_id: null
  learner_ids: []
  behavior_key: null
  candidate_facilitation_observations: []
  cost_or_behavior_change_observations: []
  learner_outcome_refs: []
  alternative_explanations: []
  confidence: low
```

Do not make “teacher” a social role merely because an older Pokémon is nearby.

## 9. Adoption snapshot

Not every member of a group knows or uses the same tradition.

```yaml
tradition_adoption_snapshot:
  tradition_id: null
  observed_at: null
  collective_id: null
  exact_known_user_ids: []
  observed_user_count_band: null
  observed_nonuser_count_band: null
  unknown_count_band: null
  sampling_effort_ref: null
  age_or_cohort_claims: []
  confidence: null
```

Loaded Cobblemon entities must not become the denominator for the population.

## 10. Repertoire revision

Some traditions change gradually.

```yaml
tradition_revision:
  revision_id: null
  tradition_id: null
  effective_window_start: null
  effective_window_end: null
  observed_variant_ids: []
  prior_revision_id: null
  new_variant_claim_ids: []
  decline_claim_ids: []
  geographic_variant_refs: []
  evidence_refs: []
```

Use this for:

- Chatot sayings or calls;
- repeated foraging sequences;
- object-use variants;
- local crossing practices;
- shelter-opening routines;
- route rituals that are behavioral rather than sacred/cultural human practices.

A revision changes the learned repertoire, not the Pokémon’s mechanical species definition.

## 11. Vocal repertoire boundary

Soundscapes owns the acoustic event and recording.

This layer owns evidence that a local population learns and shares a vocal variant.

Language/Translation owns claims that vocalizations carry symbolic or linguistic meaning.

Therefore:

recorded repeated call → Soundscapes fact.

shared local learned call → possible Behavioral Tradition.

translated proposition or symbolic meaning → Language claim.

No layer should infer the next state automatically.

## 12. Migration boundary

Migration owns movement episodes and corridor history.

This layer may store evidence that route knowledge is socially transmitted.

A stable migration route does not prove cultural transmission. It may be ecological, inherited, individually learned or driven by environmental cues.

If an experienced individual disappears and a group changes route, that correlation is evidence for investigation, not proof.

## 13. Human-interface traditions

Wild Pokémon can learn recurring patterns around human systems without becoming owned or domesticated.

Candidate examples:

- timing for ferry unloading;
- safe use of a wildlife crossing;
- opening one type of refuse container;
- waiting outside a market after closing;
- responding to a non-threatening warning signal;
- using a public fountain at one hour;
- avoiding a train approach cue;
- visiting a restoration site after workers leave.

Urban Wildlife owns habituation/attractants/conflict.

This layer owns evidence that a technique or routine is socially transmitted within the population.

## 14. Individual persistence and tradition continuity

Persistent individuals can matter to knowledge transmission.

```yaml
tradition_key_individual_link:
  tradition_id: null
  pokemon_entity_id: null
  role_claim: innovator|experienced_user|possible_demonstrator|historical_user|unknown
  first_linked_at: null
  last_confirmed_at: null
  evidence_ids: []
```

Removing one individual does not delete the tradition.

Capturing one individual does not grant the Trainer control of the tradition.

Releasing a Pokémon can allow later observations of possible knowledge transfer, but release itself does not cause transmission.

## 15. Tradition disruption case

```yaml
tradition_disruption_case:
  disruption_id: null
  tradition_id: null
  first_detected_at: null
  change_observations: []
  monitoring_effort_refs: []
  candidate_causes: []
  experienced_individual_change_refs: []
  habitat_change_refs: []
  human_activity_refs: []
  migration_change_refs: []
  current_assessment: unresolved
```

Possible real outcomes:

- tradition remains common;
- behavior shifts to a new variant;
- behavior becomes rarer;
- behavior disappears locally;
- behavior moves with a subgroup;
- archive evidence reveals it was never as widespread as assumed;
- no meaningful change is confirmed.

## 16. Tradition and conservation

A population can retain ecological importance even when the behavior itself is not mechanically important.

Conservation may decide to protect:

- a traditional stopover;
- a site where a rare local technique is documented;
- a known demonstrator population;
- acoustic conditions needed for a vocal repertoire;
- access to materials used in local object handling.

The conservation value must be an institutional/scientific claim. It does not make the behavior sacred or legally protected automatically.

## 17. Tradition and research ethics

Researchers must not manufacture a “tradition” by repeatedly baiting or training wild Pokémon and then describe the resulting behavior as naturally occurring without documenting the intervention.

Research Ethics owns authorization and subject-protection state.

This layer records intervention provenance.

```yaml
behavior_intervention_provenance:
  intervention_id: null
  behavior_key: null
  actor_ids: []
  target_population_refs: []
  method_summary: null
  start_at: null
  end_at: null
  research_protocol_ref: null
  possible_behavioral_effects: []
```

## 18. Player-caused behavioral innovation

Players can plausibly create conditions under which a new local behavior appears.

Examples:

- building a safe crossing;
- changing a market schedule;
- leaving a public water source accessible;
- restoring a habitat feature;
- repeatedly demonstrating a harmless procedure.

The game should record the intervention and later observations.

It must not directly write “the Pokémon learned from the player” without evidence.

## 19. Multiplayer privacy and agency

A PC’s private training method, spoken phrase or routine should not automatically propagate into world public knowledge.

If a player deliberately teaches a partnered Pokémon something narratively, this does not grant a mechanical Move/Feature unless PTU rules support it.

If a released Pokémon later performs the behavior, that establishes an observation. Whether it spreads remains a separate question.

## 20. Minecraft projection

Minecraft/Cobblemon should present behavior already authorized by world state.

Possible presentation:

- animation sequence;
- object interaction;
- repeated path use;
- gathering around a site;
- local vocal playback;
- observation markers;
- camera-trap record;
- field notebook entry.

Minecraft must not become the authority for:

- whether behavior is socially learned;
- whether all members know it;
- transmission mode;
- tradition status;
- population size;
- whether an individual is a teacher;
- PTU mechanical benefit.

Chunk unload cannot mean the tradition disappeared.

## 21. Cobblemon projection

Spawn selection may reflect a world-state population where appropriate, but behavioral traditions must not become exploitable rare-spawn modifiers.

The projection should operate at coarse population/collective state.

A player repeatedly opening containers near wild Pokémon must not force a tradition or spawn change by brute repetition.

## 22. Battle boundary

AutoPTU receives battle state, not a population-culture simulation.

A behavioral tradition can explain:

- why Pokémon are at a site;
- why they avoid a route;
- why they flee when a cue happens;
- why a conflict begins;
- what world state changes afterward.

It cannot grant:

- Accuracy;
- Evasion;
- damage;
- initiative;
- coordinated actions;
- Pack Mon;
- Receiver;
- Ally mechanics;
- Orders;
- Trainer Features;
- reaction windows;
- custom AI bonuses.

Those need actual PTU/Caelo rules and implementation evidence.

## 23. Mechanically rich encounter contract A — Orchard Technique Survey

Narrative premise:

A wild collective uses a locally documented object-handling technique to access fallen or stored fruit. A recent infrastructure change may be disrupting the sequence.

FULL version:

- individual Pokémon move between resource stations;
- some withdraw instead of fighting;
- an interactable object may change access;
- players can protect the route without defeating every Pokémon;
- AI understands resource access and withdrawal.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for active crossing/interception objectives
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only if the resource area or infrastructure produces validated tactical zones/effects
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for ACCESS_RESOURCE/WITHDRAW/PROTECT_ROUTE
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

REDUCED version:

Observation, resource access and behavior transmission remain overworld state. If a confrontation occurs, workers and noncombatant Pokémon leave the immediate area and AutoPTU receives a static orchard edge with only actual combatants. The result never decides whether the behavior is a tradition.

## 24. Mechanically rich encounter contract B — Chatot Chorus Shift

Narrative premise:

A local Chatot group’s shared vocal repertoire has changed since the previous survey. A visiting subgroup, market soundscape change or individual innovation are candidate explanations.

FULL version:

The ideal scene is primarily observational and social. If a threat causes group movement, Pokémon may disperse or seek known roosts while players protect recording stations.

Dependencies if tactical conflict occurs:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING for coordinated dispersal or protected retreat lanes
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full lifecycle: PARTIAL
- full damage: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING only when an actual validated environment effect is active
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for DISPERSE/REACH_ROOST/AVOID_CONFLICT
- adapter/playback: BLOCKING

REDUCED version:

All repertoire research occurs outside combat. If an unrelated threat creates battle, the chorus disperses in overworld state first. AutoPTU resolves only the threat. Recordings before and after remain the evidence.

## 25. Mechanically rich encounter contract C — The Last Demonstrator

Narrative premise:

A persistent experienced Pokémon has not appeared during a seasonal behavior window. Naïve individuals are using the site differently. Researchers do not know whether the experienced Pokémon taught the technique, merely used it, or was irrelevant.

FULL version:

- tracking may lead to a moving individual;
- naïve group members may attempt a route or objective;
- reunion is possible without capture;
- threats can trigger withdrawal;
- AI needs REACH_GROUP/WITHDRAW/FOLLOW_SAFE_ROUTE behaviors.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full lifecycle: PARTIAL
- full damage: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING when route hazards are tactically represented
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for REACH_GROUP/WITHDRAW/FOLLOW
- adapter/playback: BLOCKING

REDUCED version:

Tracking, reunion and observed learning remain overworld state. Any battle is a separate static encounter against the actual threat. The experienced Pokémon does not become owned, allied or commandable because the players found it.

## 26. Hard non-inferences

Never infer:

- repeated behavior -> social learning;
- social group -> behavioral tradition;
- same behavior in several individuals -> imitation;
- older individual -> teacher;
- persistent individual -> leader;
- local behavior -> species-wide rule;
- learned behavior -> Move;
- learned behavior -> Ability;
- learned behavior -> Feature/Edge;
- local vocal repertoire -> human-language fluency;
- Chatot phrase -> semantic translation without Language-layer evidence;
- Passimian group -> Pack Mon;
- group coordination -> tactical AI policy;
- observation of demonstration -> obedience;
- imitation -> Loyalty;
- tradition -> Friendship;
- released partner -> demonstrator automatically;
- capture/removal of one Pokémon -> tradition erased;
- missing observation -> tradition lost;
- behavioral shift -> Evolution;
- tradition difference -> regional form;
- nearby environmental change -> confirmed cause;
- Minecraft repeated pathfinding -> canonical learned route;
- loaded entity count -> adoption rate;
- despawn -> departure or loss of knowledge;
- battle victory -> tradition restored;
- battle defeat -> tradition destroyed.

## 27. New overworld implementation blockers

- `BEHAVIOR_OBSERVATION_LEDGER`
- `LOCAL_BEHAVIOR_PATTERN_REGISTRY`
- `BEHAVIOR_INNOVATION_EVENT`
- `SOCIAL_TRANSMISSION_OBSERVATION`
- `BEHAVIORAL_TRADITION_ASSESSMENT`
- `TRADITION_ADOPTION_SNAPSHOT`
- `TRADITION_REVISION_HISTORY`
- `TRADITION_KEY_INDIVIDUAL_LINK`
- `TEACHING_HYPOTHESIS_STATE`
- `TRADITION_DISRUPTION_CASE`
- `BEHAVIOR_INTERVENTION_PROVENANCE`
- `TRADITION_TO_WILD_COLLECTIVE_HANDOFF`
- `TRADITION_TO_SOUNDscape_HANDOFF`
- `TRADITION_TO_LANGUAGE_HANDOFF`
- `TRADITION_TO_MIGRATION_HANDOFF`
- `TRADITION_TO_POKEMON_AGENCY_HANDOFF`
- `TRADITION_TO_CONSERVATION_HANDOFF`
- `TRADITION_TO_COBBLEMON_PROJECTION`
- `TRADITION_TO_MINECRAFT_PRESENTATION`
- `TRADITION_TO_BATTLE_SNAPSHOT`

## 28. Canon questions

Before promotion to canon, decide:

- which populations begin with authored behavioral traditions;
- whether “culture” is an in-world scientific term or only a research label;
- which institutions monitor learned behavior;
- whether local Chatot repertoires are widespread or exceptional;
- how much behavioral drift may be generated procedurally;
- whether player interventions can seed traditions and under what evidence threshold;
- how long an unobserved tradition remains `CURRENTLY_UNCONFIRMED`;
- how behavioral tradition interacts with conservation decisions;
- how persistent individuals survive despawn/reload and group changes;
- what information is public versus sensitive;
- which exact PTU/Caelo mechanics, if any, govern imitation, teaching, mimicry or group behavior.

Until those decisions are authored, all structures in this layer remain proposed architecture.