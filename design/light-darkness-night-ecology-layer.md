# Light, Darkness and Night Ecology Layer

Status: PROPOSED SYSTEM DESIGN. Not canon. Not a PTU rules replacement.
Pass: 68

## Purpose

This layer gives Ouros one persistent model for environmental light, artificial illumination, biological light, darkness, visual signaling and nighttime ecological response.

The system exists because light affects several already-established layers at once:

- travel and navigation;
- settlements and infrastructure;
- astronomy;
- soundscape and perception;
- wild ecology;
- conservation;
- research;
- photography;
- tourism;
- crisis response;
- battle setup.

It must not let Minecraft lighting become an unofficial PTU rules engine.

## Core separations

Ouros must preserve these as different facts:

`physical light state`

`rendered Minecraft brightness`

`what an actor can visually perceive`

`what a player can read on screen`

`what PTU mechanics say about vision / Blinded / capabilities`

`what an observer infers from a light source`

`what ecology changes because of repeated illumination`

None of these should silently overwrite the others.

## 1. LIGHTSCAPE

A `LIGHTSCAPE` describes coarse physical illumination across a persistent location or sub-area.

Suggested fields:

```yaml
lightscape_id: null
location_id: null
revision_id: null
valid_from: null
valid_to: null
natural_light_sources: []
artificial_light_sources: []
biological_light_sources: []
coarse_zones: []
night_sky_glow_class: null
intermittency: null
observations: []
source_refs: []
confidence: null
```

A lightscape is not a battle effect.

It says what light exists in world state.

## 2. LIGHT_SOURCE

A persistent light source may be:

- celestial/natural;
- flame;
- electric;
- chemical;
- biological;
- reflected;
- temporary event lighting;
- navigational/beacon lighting;
- emergency lighting.

Suggested fields:

```yaml
light_source_id: null
source_type: null
physical_anchor_id: null
operator_id: null
source_entity_id: null
active_state: UNKNOWN
schedule: null
orientation: null
coarse_intensity: null
coarse_color_band: null
intermittency_pattern: null
service_dependency_ids: []
maintenance_dependency_ids: []
mechanics_mapping: UNRESOLVED
```

`coarse_intensity` should initially stay qualitative, for example:

- VERY_LOW
- LOW
- MODERATE
- HIGH
- VERY_HIGH

Do not invent lux thresholds unless the simulation later needs and validates them.

## 3. DARK_REFUGE

A `DARK_REFUGE` is a persistent sub-area where relative darkness matters ecologically or operationally.

Examples:

- forest interior;
- cave chamber;
- unlit shoreline;
- vegetation buffer beside a road;
- dark-sky protected zone;
- section of a harbor outside floodlights.

A dark refuge does not automatically create stealth bonuses or Blinded.

It records a world-state feature that ecology, research and management systems can reference.

## 4. LIGHT_OBSERVATION

An observation records what was measured or seen, not what caused it.

```yaml
light_observation_id: null
lightscape_id: null
time: null
observer_id: null
method: null
position_ref: null
measured_values: {}
visual_description: null
weather_context: null
moon_context: null
source_refs: []
confidence: null
```

Possible methods:

- direct visual observation;
- camera exposure;
- light meter;
- satellite/aerial record;
- instrument station;
- historical photograph;
- testimony.

A testimony that “the valley was brighter than usual” is valid evidence but not equivalent to an instrument reading.

## 5. NIGHT_VISIBILITY_CONTEXT

Ouros needs a narrative visibility context before it can safely open a battle.

Suggested fields:

```yaml
night_visibility_context_id: null
location_id: null
lightscape_revision_id: null
weather_revision_id: null
smoke_or_fog_refs: []
physical_obstructions: []
mechanical_visibility_effects: UNRESOLVED
ptu_review_required: true
```

This object exists to prevent a bad shortcut:

Minecraft block-light level -> PTU penalty.

The server must first resolve a rules-backed mechanical projection.

## 6. ACTOR_VISUAL_CAPABILITY

Mechanical perception belongs to the PTU/Caelo rules state.

Narrative state may record known capability facts only when sourced from the authoritative sheet/runtime.

Examples of potentially relevant PTU concepts include:

- Darkvision;
- Blindsense;
- Glow;
- exact Moves or Features that affect visibility.

The narrative layer must not assign them from species flavor.

Example forbidden inference:

“Umbreon is nocturnal, therefore it has Darkvision.”

Only the authoritative Pokémon state may answer that.

## 7. BIOLOGICAL_LIGHT_EVENT

Some Pokémon produce light as behavior.

The system may record:

```yaml
biological_light_event_id: null
pokemon_entity_ids: []
species_ids: []
location_id: null
time: null
observed_pattern: null
observed_duration: null
possible_function_hypotheses: []
recording_refs: []
source_refs: []
```

Possible functions remain hypotheses unless authored or supported:

- communication;
- lure;
- warning;
- navigation;
- mating display;
- predation;
- unknown.

This prevents “glowing = friendly” and “flashing = language” from becoming automatic.

## 8. LIGHT_SIGNAL_PATTERN

Repeated or structured lighting can become a signal system.

Examples:

- harbor beacon patterns;
- railway/route signal lights;
- research station codes;
- emergency strobes;
- Volbeat/Illumise displays;
- historical tower signals.

Suggested fields:

```yaml
signal_pattern_id: null
source_ids: []
pattern_version: null
intended_meaning: null
known_by_actor_ids: []
observed_by_actor_ids: []
interpretations: []
confidence: null
```

A pattern can be correctly recorded but incorrectly interpreted.

## 9. LIGHTING_INFRASTRUCTURE_PROJECT

Lighting projects connect to Public Works and Technology.

Examples:

- street-light replacement;
- harbor beacon repair;
- tunnel lighting;
- dark-sky retrofit;
- stadium lighting;
- emergency path lighting;
- hospital backup lighting.

The project should track goals independently:

- safety;
- navigation;
- operating hours;
- energy use;
- ecological impact;
- heritage appearance;
- astronomy/night-sky protection;
- accessibility.

A project can improve one objective while harming another.

## 10. ARTIFICIAL_LIGHT_PRESSURE

Artificial light at night can become an ecological pressure.

Do not model it as one universal species modifier.

Suggested object:

```yaml
artificial_light_pressure_id: null
lightscape_id: null
source_ids: []
affected_area_refs: []
observation_window: null
candidate_response_types: []
evidence_refs: []
hypotheses: []
management_actions: []
review_state: OPEN
```

Candidate response types may include:

- timing shift;
- attraction;
- avoidance;
- altered foraging;
- altered communication;
- altered navigation;
- altered predation;
- no detectable response;
- mixed response.

Do not select one without evidence or authored species ecology.

## 11. NOCTURNAL_ACTIVITY_PROFILE

A location or population may have an expected activity pattern.

```yaml
nocturnal_activity_profile_id: null
subject_ref: null
baseline_period: null
expected_activity_windows: []
season_refs: []
weather_refs: []
lightscape_refs: []
confidence: null
```

This supports anomalies such as:

“normally active after dusk, now absent for five nights.”

The anomaly should generate a question, not an automatic cause.

## 12. NIGHT_ACCESS_STATE

Night may change access without changing battle mechanics.

Examples:

- shop closes;
- ferry stops;
- ranger checkpoint activates;
- astronomy trail opens;
- protected nesting site closes;
- industrial night shift begins;
- nocturnal survey window starts.

This state belongs to schedules, credentials and travel layers.

The light layer only supplies relevant context.

## 13. LIGHT_POLLUTION_REVIEW

A settlement can periodically review its lightscape.

Potential inputs:

- astronomy measurements;
- wildlife observations;
- resident complaints;
- road/harbor safety reports;
- energy use;
- heritage concerns;
- accessibility reports;
- tourism.

Possible outcomes:

- shield fixtures;
- change direction;
- reduce operating hours;
- change intensity;
- retain current configuration;
- add task-specific light;
- create dark corridors;
- pilot a temporary change.

The system should avoid a simplistic “dark = good, light = bad” policy.

## 14. NIGHTTIME PHOTOGRAPHY AND EVIDENCE

Pass 46 already owns visual evidence.

Pass 68 adds context only:

- exposure conditions;
- artificial source location;
- glare;
- darkness;
- moon state;
- obstruction by fog/smoke.

A low-light photograph may be authentic and still unsuitable for identification.

Never boost confidence merely because an image was captured by a camera.

## 15. LIGHT AND ASTRONOMY

Pass 63 owns celestial observations.

This layer provides local sky-brightness context.

An astronomical event can occur while being unobservable locally because of:

- clouds;
- smoke;
- artificial sky glow;
- obstruction;
- equipment failure.

The event itself remains independent of visibility.

## 16. LIGHT AND FRESHWATER / MARITIME ECOLOGY

Artificial light near water may change observed predator/prey behavior.

The system should create a causal investigation chain:

new lighting -> changed lightscape -> observations -> hypothesis -> comparative observations -> possible ecological assessment.

Do not directly modify encounter tables from a lamp placement event.

## 17. LIGHT AND SETTLEMENT LIFE

Lighting can change settlement activity:

- operating hours;
- perceived landmark identity;
- visitor movement;
- night markets;
- transport windows;
- staff needs;
- maintenance burden;
- energy demand.

These are world-state effects.

Do not infer crime, safety or social mood directly from brightness.

## 18. LIGHT AND INFRASTRUCTURE POKÉMON

A Pokémon may serve a persistent institutional role where canon supports it.

The Ampharos/lighthouse pattern is a useful precedent.

Ouros should record:

- Pokémon identity;
- institutional relationship;
- voluntary/authorized role state when authored;
- care dependencies;
- service schedule;
- backup plan.

The Pokémon must never become a disposable machine component.

If it becomes unavailable, the institution reacts through staffing/technology/world state.

## 19. Accessibility rule

Mandatory progression cannot rely on “the player must literally see a dark object on a dark screen.”

Critical information should have an equivalent presentation when appropriate:

- outline;
- text cue;
- subtitle/log entry;
- accessible map marker after discovery;
- instrument reading;
- audio cue with caption;
- high-contrast interaction indicator.

Accessibility does not mean automatically revealing hidden information.

It means preserving the reasoning problem through another channel.

## 20. Anti-exploit rule for spawning

Lightscape state may influence ecological models only through reviewed rules.

Players must not be able to create a rare-spawn machine by placing thousands of torches or removing every light source.

Recommended path:

Minecraft light changes -> coarse server lightscape observation -> ecological review rule -> capped/slow population-state response -> Cobblemon projection.

Never:

Minecraft block light -> direct rare spawn multiplier.

## 21. Battle handoff contract

Before an encounter starts, the world layer may provide:

```yaml
battle_light_context:
  source_lightscape_revision_id: null
  time_context_id: null
  weather_context_id: null
  proposed_visibility_state: null
  rules_evidence_refs: []
  ptu_caelo_validated: false
```

AutoPTU-Java must decide the actual mechanical state once that family exists.

Minecraft never calculates:

- Blinded;
- Accuracy penalty;
- stealth modifier;
- vision range;
- target legality;
- Glow mechanical effect.

## 22. Encounter implementation contracts

### Encounter A — Beacon Failure at North Harbor

Narrative premise:

A navigation beacon fails during a busy night. Operators must determine whether the failure is electrical, staffing-related, weather-related or caused by damage while harbor activity continues.

Full version dependencies:

- targeting / footprints / range / LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement / interception / forced movement — BLOCKING if vessels/civilians move through active lanes
- core calculations — VERIFIED
- action economy / initiative — VERIFIED
- full turn / round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL if any rules effect appears
- terrain / weather / hazards / zones / reactions — BLOCKING for darkness/fog/light zones
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features / perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for protect/withdraw/avoid-lane goals
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced version:

Resolve beacon outage, harbor closures and navigation state in overworld. Evacuate noncombatants before combat. Freeze one static dock arena with normal readable presentation. Darkness has no tactical effect. Run a conventional battle only if a real confrontation remains.

### Encounter B — Dark Corridor Survey

Narrative premise:

Researchers compare wild activity across a newly lit service road and an adjacent dark habitat corridor.

Full version dependencies:

- static geometry and base movement — VERIFIED
- actor-specific low-light visibility — BLOCKING under terrain/weather/hazards/zones/reactions until exact PTU/Caelo mechanics are wired
- lifecycle/damage/status/Abilities/Features — PARTIAL as applicable
- tactical AI — BLOCKING for avoid-light / cross-corridor goals
- adapter/playback — BLOCKING

Reduced version:

Run survey observations entirely in overworld. If wild Pokémon become aggressive or territorial, open a static battle with standard visibility. Store the lightscape difference only as provenance for later ecological analysis.

### Encounter C — Flickerwood Signals

Narrative premise:

A forest contains recurring biological light patterns. Researchers and residents disagree about whether they are communication, feeding behavior or coincidence.

Full version dependencies:

- targeting/range/LoS — VERIFIED
- base movement — VERIFIED
- full dynamic visibility/Glow/Darkvision/Blindsense projection — BLOCKING until exact rules are implemented
- lifecycle — PARTIAL if light patterns change by round
- status — PARTIAL only if a validated Move/Ability actually applies one
- tactical AI — BLOCKING for lure/withdraw/investigate goals
- adapter/playback — BLOCKING

Reduced version:

Treat patterns as observational world state. A conventional encounter may occur separately. Do not apply Sleep, Blinded, Accuracy penalties or attraction effects because a species glows.

## 23. Permanent capability dependency summary

This layer uses the permanent capability categories exactly as defined by the engine project.

Most narrative lightscape work can proceed without battle implementation.

Mechanically dynamic darkness is primarily blocked by:

- `terrain / weather / hazards / zones / reactions` — BLOCKING;
- `AI tactical policy` — BLOCKING;
- `Minecraft / Cobblemon / Craftics adapter & playback` — BLOCKING;
- complete movement — BLOCKING when moving lanes, interception or displacement matter.

Related families remain PARTIAL:

- full lifecycle;
- full stateful damage;
- statuses;
- move-specific behavior;
- Abilities;
- items;
- Trainer Features/perks.

Static geometry, base movement, core calculations, initiative and legal-action generation are usable now where the encounter does not invent light mechanics.

## 24. Rule cautions

Do not infer or invent:

- universal vision radius from Minecraft light level;
- Accuracy penalty from darkness;
- automatic Blinded;
- stealth bonus from darkness;
- Darkvision from nocturnal species flavor;
- Glow from a glowing Pokédex description unless the authoritative PTU state has it;
- Illuminate as a universal overworld light mechanic;
- Flash as a generic torch replacement;
- light pollution causing a particular species response without evidence;
- Fire-type Pokémon as automatically valid light sources;
- Electric-type Pokémon as automatically valid infrastructure power/light sources;
- lighthouse Pokémon obedience or permanent service;
- rare-spawn changes from torch placement;
- moonlight as a battle buff;
- darkness as an excuse to hide required UI information.

## 25. Canon boundary

This layer defines structure, not Ouros canon.

Before any lightscape becomes canon, human review should establish:

- regional lighting technology;
- settlement operating norms;
- which biological-light relationships are locally true;
- night-sky and conservation institutions;
- authored night ecology;
- exact PTU/Caelo visibility rules;
- Minecraft representation policy.

## 26. Open questions

- What exact PTU/Caelo rules govern Darkvision, Blindsense, Glow, Blinded and Flash?
- Does Caelo modify vision or darkness?
- Will the Ouros server track coarse lightscape state independent of Minecraft block light?
- Can Cobblemon expose nocturnal activity without direct light-level spawn exploits?
- Can Minecraft present per-player darkness while maintaining accessibility?
- Which settlements use Pokémon as voluntary beacon/service partners?
- How should artificial light around aquatic habitat affect ecological observation without direct spawn manipulation?
- Can AutoPTU-Java eventually accept a semantic `visibility_context` independent of LoS geometry?
