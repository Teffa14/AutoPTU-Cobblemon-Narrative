# Ouros Soundscapes & Acoustic Ecology Layer

Status: proposed systems design. Not established canon.

## Purpose

Ouros already models performance, communication networks, ecology, conservation, science, investigation, stealth, infrastructure, settlements and seasonal change. This layer adds persistent soundscape state and auditory observations without turning every sound into a combat mechanic or every piece of music into a Contest.

The central rule is simple: sound can be world information without automatically being PTU mechanics.

## 1. Truth boundary

Keep these concepts separate:

```text
physical source
→ emitted sound event
→ potential propagation
→ observer actually hears something
→ observer interpretation
→ recording / report
→ later actor knowledge
→ any authoritative PTU mechanical effect
```

A listener can hear correctly and interpret incorrectly.

A recording can be authentic but incomplete.

A location can be quiet without anything dangerous occurring.

A species can be known for sound-based behavior without the individual Pokémon knowing a particular Sonic Move.

## 2. Acoustic source

```yaml
acoustic_source:
  source_id: null
  source_type: null
  actor_id: null
  infrastructure_id: null
  location_id: null
  persistent: false
  authored_signature_tags: []
  operating_state_ref: null
  privacy_state: null
  source_refs: []
```

Candidate source types:
- POKEMON
- HUMAN
- MACHINE
- VEHICLE
- NATURAL_FEATURE
- WEATHER
- PUBLIC_SIGNAL
- PERFORMANCE
- BUILDING_SYSTEM
- UNKNOWN

`source_type` does not define loudness, range or mechanical effect.

## 3. Sound event

```yaml
sound_event:
  sound_event_id: null
  source_id: null
  source_known: false
  emitted_at: null
  origin_location_id: null
  event_class: null
  signature_tags: []
  intended_audience_ids: []
  authored_duration_class: null
  world_state_refs: []
  mechanics_event_ref: null
  source_refs: []
```

Possible event classes:
- CALL
- WARNING
- SONG
- MACHINERY
- IMPACT
- ALARM
- ANNOUNCEMENT
- VEHICLE
- AMBIENT
- UNKNOWN

Do not store a generic damage value, hearing radius or emotion effect here.

## 4. Acoustic observation

```yaml
acoustic_observation:
  observation_id: null
  observer_id: null
  sound_event_id: null
  observed_at: null
  observer_location_id: null
  perceived_direction: null
  perceived_distance_class: null
  perceived_signature_tags: []
  perceived_words_or_pattern: null
  certainty: null
  recording_id: null
  interpretation_claim_ids: []
  source_refs: []
```

The observer may record:
- a direction without identifying the source;
- a repeated rhythm;
- a species-like call with uncertainty;
- machinery running irregularly;
- absence of an expected signal;
- speech they could not fully understand;
- multiple overlapping sources.

The narrative layer must not silently upgrade perception into certainty.

## 5. Acoustic profile

An acoustic profile stores a learned pattern rather than a universal rule.

```yaml
acoustic_profile:
  profile_id: null
  subject_type: null
  subject_id: null
  profile_class: null
  signature_tags: []
  context_tags: []
  supporting_observation_ids: []
  contradicting_observation_ids: []
  authored_fact_ids: []
  confidence: null
  version: 1
```

Possible profile classes:
- SPECIES_CALL
- INDIVIDUAL_CALL
- COLLECTIVE_PATTERN
- MACHINE_CYCLE
- PUBLIC_SIGNAL
- NATURAL_LANDMARK
- SEASONAL_BASELINE

Example: researchers may believe a repeated three-note call is associated with a local nesting group. That belief remains a profile supported by observations until canon or authoritative data establishes more.

## 6. Soundscape state

```yaml
soundscape_state:
  soundscape_id: null
  location_id: null
  time_window_ref: null
  season_phase_ref: null
  world_state_variant_ids: []
  expected_profile_ids: []
  active_sound_event_ids: []
  ambient_tags: []
  disturbance_state_ids: []
  silence_state_ids: []
  baseline_quality: null
  last_updated_at: null
```

Soundscapes can make places recognizable without creating quest markers.

Examples of ambient identity:
- surf and harbor machinery;
- evening insect calls;
- a distant rail crossing;
- workshop hammers during business hours;
- wind through a canyon;
- public announcements at a terminal;
- a nesting colony at dawn;
- bells associated with a civic institution;
- a generator hum during emergency operation.

Ambient identity is presentation/world state. It does not need to encode a mechanical benefit.

## 7. Acoustic baseline

A baseline says what has been commonly observed under a given context.

```yaml
acoustic_baseline:
  baseline_id: null
  location_id: null
  context_tags: []
  expected_profile_ids: []
  sample_window_ids: []
  observer_or_sensor_ids: []
  confidence: null
  valid_from: null
  valid_until: null
```

Possible contexts:
- MORNING
- NIGHT
- BREEDING_SEASON
- MARKET_DAY
- FERRY_OPERATING
- STORM_SEASON
- FESTIVAL_WEEK
- WINTER

A baseline requires history. The generator must not label a first observation "abnormal" without something to compare it against.

## 8. Acoustic anomaly

```yaml
acoustic_anomaly:
  anomaly_id: null
  baseline_id: null
  observed_event_ids: []
  anomaly_type: null
  detected_at: null
  location_id: null
  severity: null
  explanation_claim_ids: []
  investigation_case_id: null
  resolved_fact_ids: []
```

Candidate anomaly types:
- EXPECTED_CALL_ABSENT
- UNEXPECTED_CALL_PRESENT
- TIMING_SHIFT
- RHYTHM_CHANGE
- MACHINE_SOUND_CHANGE
- ALARM_FAILURE
- UNEXPECTED_SILENCE
- UNEXPECTED_VOLUME_CHANGE
- REPEATING_UNKNOWN_PATTERN

An anomaly does not define its cause.

## 9. Silence as observation

```yaml
silence_observation:
  silence_id: null
  location_id: null
  observer_id: null
  observed_at: null
  expected_profile_ids: []
  absent_profile_ids: []
  environmental_context_ids: []
  confidence: null
```

Rules:
- silence requires an expectation to be informative;
- silence does not automatically mean predators, supernatural activity, danger or death;
- a shutdown, weather change, migration, maintenance closure or time-of-day shift may explain it;
- absence of a species call does not prove the species is absent from the region.

## 10. Recording

```yaml
acoustic_recording:
  recording_id: null
  captured_by_id: null
  device_or_method_id: null
  captured_at: null
  location_id: null
  source_event_ids: []
  integrity_state: null
  edit_history: []
  access_policy_id: null
  privacy_flags: []
  transcript_id: null
  derived_profile_ids: []
  chain_of_custody_ids: []
```

A recording can support Science, Case, Media or Archive layers.

It can also be:
- incomplete;
- clipped;
- noisy;
- edited;
- mislabeled;
- captured at the wrong time;
- genuine but interpreted incorrectly.

Recording authenticity and interpretation are separate.

## 11. Species-call library

```yaml
species_call_library:
  library_id: null
  species_id: null
  regional_variant_id: null
  call_profile_ids: []
  observation_ids: []
  authored_behavior_refs: []
  known_contexts: []
  unresolved_patterns: []
```

Rules:
- do not invent a universal dictionary of Pokémon language;
- do not assume every individual uses an identical call repertoire;
- do not infer emotion from a call unless evidence supports that interpretation;
- do not transform a Pokédex behavior statement into a battle Move;
- regional or collective differences may exist only after authored or observed evidence.

## 12. Collective acoustic behavior

The Wild Collective layer may link recurring group calls, but it retains ownership of collective identity and territory.

```yaml
collective_acoustic_pattern:
  collective_id: null
  profile_ids: []
  known_contexts: []
  observation_ids: []
  disturbance_response_claim_ids: []
```

A chorus, call-and-response pattern or synchronized silence can be observed without assuming hierarchy or shared mechanics.

## 13. Acoustic disturbance

```yaml
acoustic_disturbance:
  disturbance_id: null
  location_id: null
  source_ids: []
  active_window: null
  affected_actor_or_population_ids: []
  observed_response_ids: []
  public_claim_ids: []
  management_response_ids: []
  mechanics_effect_ref: null
```

Possible causes:
- construction;
- festival activity;
- traffic reroute;
- industrial machinery;
- emergency sirens;
- repeated battle activity;
- a new wild collective;
- storm damage causing equipment noise;
- a recurring public event.

The layer records observed responses. It does not invent stress, status conditions, hearing damage or encounter penalties.

## 14. Quiet zones

Quiet zones are policy/world-state objects.

```yaml
quiet_zone:
  quiet_zone_id: null
  location_id: null
  rationale_refs: []
  steward_ids: []
  active_window: null
  policy_ids: []
  public_notice_ids: []
  monitoring_ids: []
```

Possible reasons:
- nesting habitat;
- clinic recovery area;
- memorial site;
- residential night policy;
- scientific listening survey;
- ceremony;
- wildlife corridor.

A quiet zone is not the PTU Silence condition or any equivalent combat effect.

## 15. Listening sites

```yaml
listening_site:
  site_id: null
  location_id: null
  operator_ids: []
  equipment_ids: []
  target_profile_ids: []
  schedule_refs: []
  recording_ids: []
  maintenance_state_ref: null
  coverage_claim_ids: []
```

Listening sites can be:
- research stations;
- conservation monitors;
- harbor signal stations;
- cave survey posts;
- community noise monitors;
- temporary expedition equipment.

Sensor coverage must come from authored device/world rules. Do not invent perfect omnidirectional surveillance.

## 16. Acoustic landmarks and navigation

```yaml
acoustic_landmark:
  landmark_id: null
  source_id: null
  route_or_location_ids: []
  expected_profile_id: null
  known_to_actor_ids: []
  reliability_state: null
  active_window: null
```

A landmark may help orient a traveler in narrative/overworld logic.

Examples:
- waterfall;
- harbor horn;
- rail crossing;
- factory cycle;
- nesting colony;
- bell tower;
- public-address signal.

Do not infer exact distance, bearing accuracy or Navigation modifiers without PTU/Caelo or authored overworld rules.

## 17. Sound and information systems

The Media/Communications layer owns messages and publications.

This layer owns acoustic events and observations.

Example flow:

```text
warning siren emits
→ sound_event
→ nearby actor observation
→ communication system may also publish an emergency message
→ actor knowledge updates through one or both routes
```

Hearing a siren and receiving the official alert are separate facts.

## 18. Sound and performance systems

The Contest/Performance layer owns:
- performers;
- routines;
- venues;
- formal results;
- career memory;
- audiences.

This layer owns:
- what sound occurred in a place;
- how it affected the ambient soundscape;
- what observers heard;
- recordings;
- non-mechanical disturbance.

A concert can therefore change a district's temporary soundscape without receiving any generic social or emotional buff.

## 19. Sound and stealth

Battle line of sight does not prove an overworld hearing model.

The Infiltration layer may consume auditory observations when a future Minecraft perception contract exists.

Until then:
- no universal hearing radius;
- no automatic "running is heard within X blocks" rule;
- no guaranteed wall occlusion model;
- no sound-based stealth bonuses/penalties;
- no assumption that Soundproof equals mundane deafness;
- no assumption that a Silent/Stealth capability exists unless validated for the actor.

## 20. Accessibility rule

No critical progression puzzle should depend on audio alone.

For every mandatory acoustic clue, provide at least one accessible representation appropriate to the fiction:
- subtitle/caption;
- visual pulse;
- vibration/haptic cue;
- waveform or instrument display;
- NPC transcription;
- log entry;
- environmental indicator;
- alternate investigation path.

The alternate representation must preserve the same information challenge rather than simply reveal the answer.

## 21. Acoustic puzzle design

A good audio puzzle should define:
- what the player can observe;
- how repetition works;
- how mistakes are communicated;
- reset/recovery behavior;
- accessibility equivalent;
- whether ordering, direction, rhythm or classification is the actual challenge;
- how the clue fits the location's world state.

Avoid arbitrary melody passwords unless the melody has an authored cultural or mechanical reason to exist.

## 22. PTU / Caelo mechanics boundary

Exact combat effects remain outside this layer.

Before implementing any mechanical sonic interaction, extract and validate the governing project sources for:
- Sonic keyword;
- Soundproof;
- Sing;
- Uproar;
- Hyper Voice and other sound-based Moves used by a concept;
- sonic-triggered Abilities;
- Sleep and other statuses;
- sound-caused push/forced movement if present;
- Trainer Features/perks involving music, performance, Command or supernatural voice;
- any Caelo modifications.

Hard rules:
- a loud narrative sound cannot deal damage unless an authoritative mechanic resolves it;
- a song cannot apply Sleep unless the legal Move/effect does so;
- a siren cannot grant Initiative or fear penalties by narrative fiat;
- an acoustic disturbance cannot suppress Moves or Abilities;
- Soundproof behavior outside explicit rules remains unresolved.

## 23. Minecraft/Cobblemon presentation

Potential presentation hooks, pending actual adapter support:
- spatialized ambient emitters;
- per-location loops;
- per-player one-shot sounds;
- subtitle/caption events;
- visible sound indicators for accessibility;
- dynamic ambient mix by time/weather/world state;
- recording/listening-station UI;
- authored call playback for persistent Pokémon only when asset/licensing and species behavior allow it.

Minecraft audio is presentation. It must not duplicate PTU rule resolution.

## 24. Engine capability dependencies

Most acoustic-world content can advance without tactical support.

Mechanically rich encounters can depend on these permanent capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

Sound-specific combat behavior should normally touch move-specific behavior and/or abilities, and often status lifecycle. Do not create a new generic "sound combat" subsystem in the adapter.

## 25. Encounter contract A — Echo Cavern Search

Narrative premise: expedition members repeatedly hear a patterned call deeper in a cavern. Existing observations disagree about whether it is one moving Pokémon, several individuals, reflected sound or machinery from an old survey installation.

FULL version:
- players navigate using directional acoustic observations;
- cave geometry changes how sources are perceived;
- moving actors can change the apparent direction of a call;
- a later battle may involve legal Sonic Moves/Abilities if the actual combatants possess them;
- the outcome writes back which source was found, not the interpretation players held before contact.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED for battle targeting, not acoustic localization;
- base movement legality — VERIFIED;
- complete movement/interception/forced movement — only required if the authored battle uses those effects; currently BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if Sonic Moves apply statuses;
- terrain/weather/hazards/zones/reactions — BLOCKING if cave acoustics or unstable zones receive mechanical effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — BLOCKING if used;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version: acoustic localization occurs in overworld through authored observation nodes with visual/text equivalents. Once the source encounter is reached, AutoPTU receives a fixed arena and a standard legal battle. Reflections and echo do not alter PTU range or targeting.

## 26. Encounter contract B — Silent Relay Station

Narrative premise: a regional warning relay that normally produces a recognizable audible signal has gone silent. The cause is unknown: maintenance failure, power loss, damaged equipment, missing operator, nesting Pokémon or deliberate interference are all initially plausible.

FULL version:
- players investigate infrastructure and acoustic history;
- restoration may involve an interactable objective while hostiles or wild Pokémon are present;
- the signal may need to remain active for a defined objective window;
- nearby actors can react to hearing the restored signal through world-state propagation.

Dependencies beyond basic battle:
- objective handling such as ACTIVATE_OBJECT/HOLD_ZONE — not yet a verified permanent family;
- terrain/weather/hazards/zones/reactions — BLOCKING if electrical or machinery hazards matter tactically;
- AI tactical policy — BLOCKING;
- Minecraft adapter/playback — BLOCKING;
- items/Trainer Features only if authoritative repair actions use them.

REDUCED version: diagnose and restore the relay in overworld state before or after a conventional static battle. The sound event propagates narratively through known communication/world-state channels after repair.

## 27. Encounter contract C — Roost Quiet Corridor

Narrative premise: a temporary route passes near a sensitive roost. Conservation staff request reduced disturbance while travelers cross the area. Repeated loud incidents may be correlated with observed movement of the collective, but cause remains under study.

FULL version:
- overworld AI tracks noise-producing actions and species responses;
- routes may change based on collective position;
- if combat begins, players may prefer withdrawal or route clearing over KO;
- any Move-based sound interaction is resolved only through legal PTU data.

Key dependencies:
- overworld auditory perception/noise propagation — Minecraft adapter/playback BLOCKING;
- AI tactical policy — BLOCKING if opponents must prefer withdrawal/protection;
- complete movement/interception — BLOCKING for tactical escape/protection objectives;
- move-specific behavior/abilities — PARTIAL for actual Sonic mechanics;
- conservation world state — narrative-ready.

REDUCED version: noise-sensitive travel is resolved through authored overworld choices and observations, not hidden numerical noise meters. If a battle occurs, it happens in a fixed arena away from the protected roost; subsequent collective movement is updated only from explicit authored/observed events.

## 28. Encounter contract D — Fog Beacon

Narrative premise: fog reduces visual orientation along a coastal route, and travelers rely on a recurring acoustic beacon as one source of orientation. The beacon becomes intermittent during an infrastructure fault.

FULL version:
- weather/visibility changes presentation and possibly legal mechanics only if supported;
- beacon timing affects route decisions;
- hostile or wild actors may intersect the route;
- the tactical battle, if any, may use legal fog/weather effects only when Java parity exists.

Dependencies:
- terrain/weather/hazards/zones/reactions — BLOCKING for mechanical fog/weather;
- Minecraft adapter/playback — BLOCKING for spatial beacon presentation;
- AI tactical policy — BLOCKING for route/objective behavior;
- targeting/LoS — VERIFIED only for the currently implemented battle rules, not arbitrary fog modification.

REDUCED version: fog and beacon state stay in overworld travel logic with accessible visual/text cues. Any battle uses the normal fixed LoS rules of the verified arena rather than a custom fog modifier.

## 29. Generator policy

Prefer acoustic content when it emerges from existing state:
- an established baseline changes;
- a listening station records an anomaly;
- infrastructure loses a known signal;
- a wild collective changes a repeated call pattern;
- a transport service changes schedule and its acoustic landmark disappears;
- a construction project creates documented disturbance;
- a seasonal event brings a known chorus or removes it;
- an investigation has competing recordings or witness reports.

Avoid procedural noise:
- random spooky whispers with no source state;
- mandatory audio puzzles every dungeon;
- constant alarms to manufacture urgency;
- music that automatically manipulates emotions;
- generic sound damage outside PTU Moves;
- perfect species identification from one cry;
- inaccessible progression clues.

## 30. Canon questions still open

- Which regions have distinctive authored soundscapes?
- Which public warning/clock/bell systems exist?
- Are any historical Pokémon-assisted acoustic networks canon in Ouros?
- What species-call behavior is taken directly from Pokédex canon versus observed locally?
- Which records are public, private or sensitive in conservation/research contexts?
- How much ambient audio should Minecraft generate dynamically versus author by location?
- What accessibility standard is required for every acoustic clue?
- Which exact PTU/Caelo Sonic, Soundproof, hearing/perception and Trainer Feature rules are inherited?
