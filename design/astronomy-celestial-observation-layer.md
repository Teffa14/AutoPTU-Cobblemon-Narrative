# Astronomy & Celestial Observation Layer

Status: PROPOSED SYSTEMS DESIGN. Not canon. No PTU mechanic is established here.

Pass: 63

## Purpose

Give Ouros persistent state for night-sky observation, observatories, predicted celestial events, meteor falls, physical fragments and sky-linked Pokémon observations.

This layer connects seasonality, meteorology, science, photography, cartography, conservation, tourism, media, archives, geology and mythology.

## Required separation

Keep these states independent:

- actual celestial event;
- prediction or expected window;
- local sky visibility;
- instrument availability;
- observation record;
- Pokémon behavior observed during the event;
- physical material recovered on the ground;
- scientific interpretation;
- mythic/cultural interpretation;
- publication/public belief;
- tactical PTU state.

A meteor shower can occur behind clouds. A telescope can fail while the event still happens. A Pokémon gathering during a full moon does not prove a universal lunar mechanic.

## Persistent objects

### CELESTIAL_EVENT

```yaml
celestial_event_id: null
event_type: meteor_shower|meteor_fall|eclipse|conjunction|comet|unknown_light|other
start_time: null
peak_time: null
end_time: null
prediction_refs: []
observation_refs: []
physical_recovery_refs: []
canon_status: proposed
```

### SKY_WINDOW

```yaml
sky_window_id: null
location_id: null
time_start: null
time_end: null
moon_state_ref: null
weather_state_ref: null
smoke_or_haze_state_ref: null
artificial_light_state_ref: null
horizon_constraints: []
visibility_class: excellent|good|limited|poor|obscured|unknown
```

Visibility labels are world-state abstractions. They do not grant Skill bonuses.

### OBSERVATORY

```yaml
observatory_id: null
location_id: null
operator_institution_id: null
instrument_ids: []
staff_role_ids: []
public_access_policy_ref: null
dark_sky_dependency_ids: []
archive_collection_id: null
maintenance_state_ref: null
active_program_ids: []
```

An observatory may also host meteorology, geology or education programs, but those systems retain their own state.

### ASTRONOMICAL_INSTRUMENT

```yaml
instrument_id: null
instrument_type: optical_telescope|camera|spectrograph|all_sky_monitor|manual_station|other
operational_state: normal|degraded|offline|calibrating|unknown
calibration_ref: null
coverage_claim: null
last_verified_at: null
```

Instrument output is evidence, not world truth.

### CELESTIAL_OBSERVATION

```yaml
observation_id: null
observer_ids: []
instrument_ids: []
location_id: null
observed_at: null
target_or_event_claim: null
raw_record_refs: []
measurement_summary: null
quality_flag: null
interpretation_ids: []
```

A null observation remains valid when conditions and method are known.

### EVENT_PREDICTION

```yaml
prediction_id: null
event_type: null
issued_at: null
issuer_actor_or_institution_id: null
predicted_window: null
predicted_visibility_regions: []
confidence: null
method_ref: null
supersedes_prediction_id: null
```

Never overwrite an older prediction after the event. Later players should be able to compare prediction against outcome.

### FALL_SITE / CELESTIAL_FRAGMENT

A fall site records where material may have reached the ground. A fragment is a physical instance with recovery time, location, handler, custody chain, storage state and classification history.

Finding a fragment does not automatically determine ownership, authenticity or origin.

### CELESTIAL_POKEMON_OBSERVATION

```yaml
record_id: null
pokemon_entity_id: null
species_claim: null
celestial_event_id: null
location_id: null
observed_behavior: null
recorded_at: null
observer_ids: []
media_refs: []
causal_claim_ids: []
```

Correlation stays separate from causal claims.

## Clock and visibility

The existing calendar layer owns time. Astronomy derives lunar phase, sunrise/sunset and authored recurring windows from that clock.

Local visibility can depend on cloud, precipitation, smoke, Moon brightness, artificial light, horizon obstruction and instrument state.

Example:

```text
meteor shower occurs
→ city observation poor from artificial light
→ mountain station clear but instrument offline
→ rural viewing site successful
→ three records, one event
```

## Dark-sky state

Dark-sky quality can change with settlement growth, stadium lighting, industrial lighting, shielded fixtures, wildfire smoke or seasonal events.

Consequences can appear through observatory scheduling, public outreach, tourism, wildlife observation and public-works proposals.

Do not treat darker skies as automatically better for every actor. Night work, transport and public safety can create legitimate competing needs.

## Observatory life

Observatories can cycle through routine observing, public nights, maintenance, visiting programs, calibration campaigns, weather closures and emergency observations.

Important facilities should accumulate staff history, instrument versions, archive records and public reputation.

## Meteor recovery chain

Use an explicit chain:

```text
sky observation
→ candidate fall area
→ search
→ physical recovery
→ documented custody
→ analysis
→ classification
→ publication / exhibit / storage
```

Do not shortcut bright streak → rare item.

Possible complications include false positives, contaminated recovery, multiple fragments, disputed custody, protected habitat, media leaks and illicit buyer interest.

## Pokémon associations

Species-specific authored links are valid research hooks when supported by source/canon. Examples include Minior falls, Clefairy full-moon behavior and Lunatone/Solrock day-night associations.

They do not create universal combat rules or guaranteed spawn tables.

## Myth boundary

One event may have an astronomical model, historical record, local myth, ritual calendar and public rumor. The mythology layer owns belief/tradition. This layer owns sky observations and event state.

## Minecraft projection

Minecraft may render observatory buildings, telescope props, viewing platforms, temporary visitor camps, fall-site markers, exhibits and sky-event visuals when technically possible.

Minecraft visuals cannot become the authority for lunar mechanics, impact mechanics, Pokémon behavior or battle effects.

## Encounter contract — Observatory Ridge Disturbance

Full version requires:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — BLOCKING if wildlife withdraws through lanes;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for darkness/weather/ridge hazards as mechanics;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for withdrawal/avoid-observatory goals;
- Minecraft/Cobblemon/Craftics playback — BLOCKING.

Reduced version:

Resolve visitors, instruments and habitat outside battle. If combat occurs, freeze one static ridge arena. Sky conditions remain world state/presentation unless exact PTU mechanics are verified.

## Encounter contract — Fresh Fall Recovery

Full version could include moving search actors, time pressure, protected zones, fragment interactables and environmental hazards.

Reduced version:

Run the search, recovery timestamps and custody as overworld state. Open a conventional static battle only if a real confrontation occurs. Resolve fragment custody after combat.

## Encounter contract — Dark-Sky Access Dispute

Reduced version first:

Keep crowd flow, permissions and negotiation outside AutoPTU. A future full version may use protected corridors or reach/withdraw objectives, which remain blocked by complete movement, broad reactions, tactical AI and playback.

## Rules boundary

Do not create lunar stat modifiers, gravity changes, meteor damage, magnetic hazards, telescope bonuses, automatic rare-spawn boosts, legendary encounter triggers, special capture modifiers or weather effects from celestial events.

Every tactical effect must come from PTU/Caelo plus verified Java behavior.

## Promotion checklist

Before promotion to canon:

1. Define the region/location and institution.
2. Define whether the event is predictable.
3. Separate observation from cultural interpretation.
4. Validate any species association.
5. Validate fragment provenance/custody.
6. Review conservation/tourism effects.
7. Check PTU/Caelo mechanics.
8. Check Java capability dependencies.
9. Confirm Minecraft projection cannot fabricate authoritative state.