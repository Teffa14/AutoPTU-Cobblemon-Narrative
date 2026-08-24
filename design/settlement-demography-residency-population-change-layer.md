# Ouros Settlement Demography, Residency & Population Change Layer

Status: PROPOSED SYSTEMS DESIGN. Not established canon.
Pass: 149

## Purpose

Ouros needs a persistent owner for human settlement population state that does not confuse loaded Minecraft actors, hotel guests, travelers, evacuees, workers or festival visitors with permanent residents.

This layer models usual residence, temporary presence, relocations, displacement/return, population estimates and versioned settlement-level demographic change. It deliberately avoids becoming a real-world census or immigration simulator.

## 1. Authority boundary

Demography owns:

- settlement population units and estimate revisions;
- residence episodes for persistent actors when such data is authorized and relevant;
- aggregate arrival/departure/relocation observations;
- temporary population episodes;
- displacement and return episodes;
- census/survey events and their methodology/provenance;
- population-estimate uncertainty;
- coarse mobility patterns between settlements;
- historical revisions to what institutions believed about settlement population.

It does not own:

- actor identity or aliases — Identity;
- family/kinship — Family;
- homes/dwellings — Homes / Architecture;
- property/access — Land Tenure;
- hotel or shelter stays — Lodging / Crisis;
- routes or trips — Travel / Rail / Road Transit / Maritime / Airspace;
- employment — Workplaces;
- births, treatment or death confirmation — Care / Family / Memorials as appropriate;
- citizenship, immigration law or legal status — undefined unless later authored;
- service capacity — Water, Food, Emergency Services, Education, Transit, etc.;
- Minecraft entity spawning.

## 2. Core separation

```text
actor identity
current physical presence
usual residence
lodging/temporary stay
workplace assignment
travel episode
displacement
return
settlement population estimate
service pressure
```

Never collapse these states.

## 3. Settlement population unit

```yaml
settlement_population_unit:
  population_unit_id: null
  settlement_id: null
  geography_revision_id: null
  valid_from: null
  valid_to: null
  estimate_revision_ids: []
  survey_event_ids: []
  temporary_population_episode_ids: []
  displacement_episode_ids: []
  notes: []
```

A settlement can retain the same identity while its administrative or physical boundary changes. Population estimates must identify which geography revision they refer to.

## 4. Residence episode

```yaml
residence_episode:
  residence_episode_id: null
  actor_id: null
  settlement_id: null
  dwelling_or_site_ref: null
  status: USUAL_RESIDENCE
  start_time_or_window: null
  end_time_or_window: null
  confidence: null
  source_refs: []
  privacy_policy_ref: null
  supersedes_id: null
```

Suggested statuses:

- USUAL_RESIDENCE
- SECONDARY_RESIDENCE if canon later needs it
- INSTITUTIONAL_RESIDENCE
- TEMPORARILY_AWAY
- DISPLACED_FROM_RESIDENCE
- RETURN_PENDING
- ENDED
- UNKNOWN

Do not derive residence from one night, one workplace, one room assignment, one map marker or current coordinates.

## 5. Presence observation

```yaml
presence_observation:
  observation_id: null
  actor_id: null
  location_id: null
  observed_at: null
  observation_method: null
  source_ref: null
  purpose_limit: null
```

Presence is evidence that an actor was there at a time. It says nothing by itself about residence, ownership, employment, family or intent.

## 6. Population estimate revision

```yaml
population_estimate_revision:
  estimate_id: null
  population_unit_id: null
  as_of_time: null
  published_at: null
  estimate_band_or_value: null
  method: null
  source_inputs: []
  coverage_notes: []
  uncertainty_notes: []
  geography_revision_id: null
  supersedes_estimate_id: null
```

Preferred early implementation uses broad bands rather than false precision:

- HAMLET_SCALE
- SMALL_SETTLEMENT
- TOWN_SCALE
- LARGE_TOWN
- CITY_DISTRICT_SCALE
- CITY_SCALE

Exact counts may be used only where authored data and gameplay value justify them.

## 7. Census / survey event

```yaml
population_survey_event:
  survey_id: null
  population_unit_id: null
  field_window: null
  method: null
  coverage_scope: null
  response_or_observation_limits: []
  source_refs: []
  resulting_estimate_ids: []
  revision_history_ids: []
```

Methods may include authored register reconciliation, direct household survey, sample survey or institution-specific count. None should be treated as omniscient.

A missed actor is not proof that the actor had left the settlement.

## 8. Temporary population episode

```yaml
temporary_population_episode:
  episode_id: null
  settlement_id: null
  episode_type: null
  start_time: null
  end_time_or_expected_end: null
  estimated_present_band: null
  source_refs: []
  linked_event_or_incident_id: null
  service_pressure_refs: []
```

Candidate types:

- FESTIVAL_VISITORS
- SEASONAL_WORKERS
- TOURNAMENT_VISITORS
- RESEARCH_EXPEDITION
- EMERGENCY_EVACUEES
- RELIEF_WORKERS
- PILGRIMAGE_VISITORS
- TRANSIT_DISRUPTION_STRANDEES

Temporary population may matter operationally without changing usual-resident counts.

## 9. Relocation and mobility

```yaml
relocation_event:
  relocation_id: null
  actor_id: null
  origin_settlement_id: null
  destination_settlement_id: null
  departure_window: null
  residence_established_window: null
  reason_claim_refs: []
  source_refs: []
  status: OBSERVED_MOVE
```

The system should not invent motives. A character can move without the generator deciding why.

Aggregate mobility patterns may be derived only from sufficient evidence and should not expose private actor-level histories unnecessarily.

## 10. Displacement and return

```yaml
displacement_episode:
  displacement_id: null
  source_residence_refs: []
  incident_id: null
  affected_population_band: null
  temporary_destination_refs: []
  began_at: null
  return_window: null
  permanently_relocated_band: null
  unresolved_band: null
  source_refs: []
```

Evacuation, displacement and permanent relocation are separate.

A person can remain a resident of the original settlement while temporarily housed elsewhere. A later return visit does not automatically re-establish residence.

## 11. Population change without moral scoring

Population growth, decline or turnover is descriptive state. The generator must not treat growth as automatically good or decline as automatically bad.

Possible causes remain hypotheses until supported:

- jobs or institutional expansion;
- housing supply;
- infrastructure change;
- environmental pressure;
- disaster displacement;
- transport changes;
- aging/role transitions;
- seasonal patterns;
- simple individual preference.

## 12. Service-pressure handoff

Demography can publish coarse demand context to other systems:

```yaml
population_pressure_snapshot:
  settlement_id: null
  resident_band: null
  temporary_present_band: null
  displacement_inflow_band: null
  confidence: null
  valid_window: null
```

Water, Lodging, Food, Transit, Emergency Services and other authorities decide operational consequences. Demography does not invent shortages.

## 13. Minecraft projection

Never use loaded entity counts as population truth.

Minecraft may project:

- crowd density bands;
- occupied-home visuals;
- temporary camp growth;
- more or fewer ambient NPCs;
- reopened or abandoned buildings;
- noticeboards about a survey or return program.

The server-owned demographic state remains authoritative across despawn, chunk unload, render-distance changes and server restarts.

## 14. Privacy and inference guardrails

Do not infer from residence or mobility:

- ethnicity, nationality, religion or political belief;
- family/romantic relationships;
- wealth or social class;
- health status;
- criminality;
- employment;
- citizenship or legal status.

Co-residence is not kinship. Shared lodging is not co-residence. Presence is not residency.

## 15. Chronicle hooks

Useful Chronicle entries include:

- settlement estimate published/revised;
- first/last observed residence window when story-relevant;
- evacuation and staged return;
- temporary population surge;
- neighborhood or settlement boundary revision;
- institution opens/closes and population pattern changes later;
- survey methodology changes;
- a previously accepted estimate is revised without retconning the old publication.

Routine actor movement should be compressed rather than logged exhaustively.

## 16. Battle boundary

Demography itself has no battle mechanics.

A population event can create a narrative context for evacuation, return, crowd management or route clearing. The battle handoff must freeze or resolve civilians and noncombatants outside AutoPTU unless the engine later has explicit objective-aware support.

Never infer:

- crowd size -> initiative modifier;
- dense settlement -> terrain;
- displacement -> morale/status;
- resident status -> Trainer Feature;
- population pressure -> wild spawn modifier.

## 17. Canon decisions still required

- Which Ouros settlements exist and their initial scale bands.
- Whether exact resident counts are ever player-facing.
- Whether formal census institutions exist.
- Whether “residence” has any legal meaning beyond descriptive usual residence.
- Which pre-player relocations/displacements are established history.
- Which population records are public, private or aggregated.
- How player-created settlements or clubs contribute to aggregate state.
- How much demographic change advances while no players are present.