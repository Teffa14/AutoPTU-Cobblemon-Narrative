# Dreams, Aura & Psychic Information Layer — Pass 25

Status: proposed systems design. Not canon. This document governs narrative/world-state representation only. It does not create PTU mechanics.

## Purpose

Ouros needs a safe way to represent dreams, Aura readings, telepathy, psychic residue, hypnosis reports and similar subjective phenomena without turning them into omniscience or bypassing the existing knowledge/evidence architecture.

The central rule is simple: supernatural perception produces a typed observation, not automatic canonical truth.

## Relationship to existing systems

This layer extends, rather than replaces:

- `world-agency-layer.md` for actor knowledge and evidence graphs;
- `case-authority-custody-layer.md` for evidentiary use;
- `media-communications-information-layer.md` for transmission and publication;
- `myth-archaeology-sacred-sites-layer.md` for interpretation of extraordinary phenomena;
- `care-recovery-welfare-layer.md` for sleep-related care cases;
- `science-research-discovery-layer.md` for reproducible study;
- `public-memory-event-legacy-layer.md` for long-term community interpretation.

## Core separation

Never collapse these into one field:

1. Objective world fact.
2. Subjective experience.
3. Capability-produced observation.
4. Observer interpretation.
5. Target-reported experience.
6. Shared public belief.
7. Mechanically verified battle state.

A dream can contain a true memory, a distorted memory, metaphor, another actor’s influence, random imagery or an unknown combination. The system must preserve that ambiguity until independent evidence resolves it.

## New world-state objects

### SUBJECTIVE_EVENT

Represents an experience whose content cannot be assumed to describe objective reality.

Suggested schema:

```yaml
subjective_event_id: null
kind: DREAM | NIGHTMARE | VISION | HYPNOTIC_EXPERIENCE | SHARED_DREAM | OTHER
participant_ids: []
start_time: null
end_time: null
anchor_location_id: null
reported_content_refs: []
common_perception_refs: []
private_perception_refs: []
external_observation_refs: []
possible_causes: []
confirmed_causes: []
mechanical_state_refs: []
canon_status: observed_subjective_event
```

`reported_content_refs` should point to player/NPC-authored records rather than rewriting intimate dream content into a global summary.

### PERCEPTION_PACKET

Stores exactly what one actor perceived through one channel.

```yaml
perception_id: null
observer_id: null
target_id: null
channel: DREAM | AURA_READER | AURA_PULSE | TELEPATHY | THOUGHT_DETECTION | PSYCHIC_ANALYSIS | ORDINARY_SENSE
source_capability_or_feature: null
raw_observation: null
interpretation: null
confidence: unknown
consent_state: UNKNOWN | CONSENTED | NONCONSENSUAL | NOT_APPLICABLE
awareness_state: UNKNOWN | TARGET_AWARE | TARGET_UNAWARE | BLOCKED
blocker_refs: []
corroboration_refs: []
privacy: PRIVATE | SHARED_WITH_PARTY | INSTITUTIONAL | PUBLIC
created_at: null
```

Important: `raw_observation` must not contain information outside the exact governing rule scope.

### PSYCHIC_RESIDUE_RECORD

Represents an observable supernatural trace when the rules/runtime actually produce one.

```yaml
residue_id: null
subject_id: null
location_id: null
observed_by: []
source_actor_id: null
source_type: null
created_at: null
expires_at: null
analysis_records: []
mechanical_source_ref: null
```

Narrative generation may never fabricate residue only to make an investigation easier.

### DREAM_ANCHOR

Represents a stable connection between a subjective space and world state.

```yaml
anchor_id: null
real_location_id: null
associated_actor_ids: []
access_observations: []
validated_access_requirements: []
linked_dream_region_ids: []
active_state: UNKNOWN | DORMANT | OBSERVED_ACTIVE | CONFIRMED_ACTIVE
```

### DREAM_REGION

A persistent dream-space region may exist as explorable content while remaining epistemically separate from physical geography.

```yaml
dream_region_id: null
stable_landmarks: []
unstable_features: []
known_anchor_ids: []
associated_memories: []
associated_world_events: []
contradictions: []
access_history: []
return_visit_changes: []
```

A dream-region landmark does not create a real-world location unless separately confirmed.

## Mental privacy policy

This layer needs stronger privacy rules than ordinary NPC knowledge.

### Player characters

The generator must not invent:

- hidden thoughts;
- secret desires;
- trauma;
- romantic feelings;
- fears;
- memories;
- dreams;
- consent to telepathic access.

PC private mental content can enter state only from explicit player-authored input or an authorized game mechanic whose output is itself mechanically defined.

### NPCs

NPC mental content can be authored, but access must still respect capability limits and established blockers. A Telepath cannot receive a full biography because the plot would benefit from it.

### Disclosure

Learning something psychically does not automatically make it party knowledge. The recipient chooses whether to disclose it unless a separate rule or event makes it public.

## Dream reliability model

Dream content should use evidentiary labels instead of a truth score.

Suggested labels:

- UNVERIFIED_IMAGE
- SELF_REPORTED_MEMORY
- RECURRING_SYMBOL
- SHARED_ELEMENT
- EXTERNAL_TRACE_MATCH
- INDEPENDENTLY_CORROBORATED
- CONTRADICTED
- CAUSE_CONFIRMED

The system should avoid a generic `dream_accuracy=72%` field. Different elements of the same dream can have different evidentiary status.

## Shared dream model

A shared dream should not force all participants to perceive identical content.

Store:

- common scene state;
- participant-specific perception packets;
- voluntarily shared information;
- mechanically confirmed shared effects;
- post-event recollections.

This enables cooperative play without erasing individual perspective.

## Aura handling

Aura is a rules-defined supernatural sense/power family. The narrative system should expose only what the actor’s validated capability permits.

Examples of safe design behavior:

- if an authoritative Aura capability reveals a limited personality/mood signal, store that signal only;
- if an Aura capability permits communication, store the communicated content as a message packet rather than inferred truth;
- if no validated Aura capability is present, an NPC’s statement that they “feel a bad aura” is flavor/belief, not a mechanical reading;
- interference, concealment or blockers must be represented only when supported by rules or authored world-state phenomena.

## Telepathy handling

Telepathic communication should reuse the information-delivery architecture.

A telepathic message has:

- sender;
- recipient;
- content;
- governing Feature/Capability;
- delivery success/failure when mechanically relevant;
- privacy state;
- target awareness;
- possible blockers;
- provenance.

Telepathy does not make the sender truthful.

## Psychic investigation integration

Psychic observations can contribute to a CASE or RESEARCH_PROGRAM but should not automatically satisfy external evidentiary standards.

Possible workflow:

```text
subjective report
→ authorized psychic observation
→ typed perception packet
→ independent physical/social evidence search
→ corroboration or contradiction
→ case/research conclusion
```

This keeps psychic specialists valuable without letting them solve every mystery alone.

## Dream ecology

Dream-related Pokémon can participate in ecology without making every appearance a quest.

Potential world-state signals:

- repeated sleeping locations;
- dream-mist observations;
- changes in local sleep reports;
- concentration of dream-associated Pokémon;
- changes correlated with moon phase, season or infrastructure state;
- abandoned buildings or institutions associated with historical dream research.

These are correlations until causal evidence exists.

## Dream-space design principles

### Reuse and persistence

Persistent dream regions should support return visits. A later visit should reflect at least one of:

- changed dreamer state;
- new participant;
- newly understood landmark;
- external world change;
- removed/added anchor;
- new corroborating evidence;
- altered access conditions.

### No free progression bypass

Dream travel must not silently bypass:

- locked routes;
- settlement access;
- Gym/League requirements;
- dungeon state;
- custody restrictions;
- faction-controlled areas;
- Minecraft traversal requirements.

If dream travel intentionally bypasses one of these, that exception must be authored as canon and represented as an explicit access edge.

### Objective vs symbolic obstacles

A locked dream door may be symbolic. It must not be translated into a PTU Skill DC or Minecraft key requirement unless authored and validated.

## Sleep and care boundary

A nightmare report is not automatically a PTU Sleep status, Bad Sleep, Injury or medical diagnosis.

Likewise:

- mechanical Sleep can exist without meaningful dream content;
- a narrative nightmare can occur without tactical Sleep status;
- a clinic can treat sleep disruption without proving psychic causation;
- a dream-related Pokémon can be nearby without causing every symptom.

## Legendary/Mythical boundary

Dream phenomena must not escalate automatically to Darkrai/Cresselia or another Legendary/Mythical Pokémon.

Valid progression:

```text
symptom cluster
→ observations
→ competing explanations
→ evidence
→ possible Legendary-associated hypothesis
→ explicit canon approval
→ physical appearance only if approved
```

A Legendary may remain an indirect causal possibility, historical association, rumor or ecological presence.

## AutoPTU integration boundary

Python AutoPTU currently contains concrete psychic Trainer Feature actions including Telepath, Thought Detection, Suggestion and Psionic Analysis. Java does not currently show an equivalent Trainer Feature registry implementation.

Therefore narrative concepts depending on these mechanics require the permanent capability family:

`Trainer Features/perks`

Other likely dependencies include:

- `status lifecycle` for Sleep/Bad Sleep or related mechanical conditions;
- `move-specific behavior` for Dream Eater, Hypnosis and other move interactions;
- `abilities` for Bad Dreams, Insomnia, Forewarn or other relevant abilities;
- `items` for any sleep/dream item interaction;
- `full turn/round lifecycle` for timed bindings/residue/durations;
- `terrain/weather/hazards/zones/reactions` only when a dream battlefield has changing zones or environment effects;
- `Minecraft/Cobblemon/Craftics adapter/playback support` for dream-world presentation, portals, private views and transition playback;
- `AI tactical policy` only when enemies must understand dream-specific tactical objectives.

Do not infer Trainer Feature support merely because Java now has generic temporary-effect payloads and lifecycle hooks.

## Encounter contract A — Dreamyard Containment

Narrative premise: an abandoned research site begins producing observable dream-related disturbances. Players investigate the facility while a wild encounter occurs around unstable equipment.

Full version dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- status lifecycle — PARTIAL;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- Trainer Features/perks — BLOCKING if psychic Features are allowed;
- terrain/weather/hazards/zones/reactions — BLOCKING if machinery creates timed zones;
- AI tactical policy — BLOCKING if Pokémon react to equipment/objectives intelligently;
- adapter/playback — BLOCKING.

Reduced version:

The facility disturbance exists entirely as overworld/world-state presentation. The tactical encounter uses a reviewed static map and ordinary legal battle. Equipment shutdown happens before or after battle. No dream-zone effects, forced Sleep, psychic Feature shortcut or invented hazard damage occurs.

## Encounter contract B — Shared Nightmare Exit

Narrative premise: several participants report the same repeating location and discover a common exit point linked to a real-world anchor.

Full version dependencies:

- full lifecycle — PARTIAL if dream-specific timed state matters;
- status lifecycle — PARTIAL if mechanical Sleep matters;
- terrain/weather/hazards/zones/reactions — BLOCKING for changing dream geometry;
- move-specific behavior — PARTIAL;
- Trainer Features/perks — BLOCKING for Dream Reader/Telepath-style mechanics;
- AI tactical policy — BLOCKING for non-DEFEAT behavior;
- adapter/playback — BLOCKING for private/shared dream views.

Reduced version:

Dream exploration is narrative/Minecraft world-state only. If a battle occurs, the combat transitions to a static legal arena representing one stable dream location. The exit is resolved outside the grid after battle state writes back.

## Encounter contract C — Aura Trail Interception

Narrative premise: an actor with a validated Aura-related capability follows a limited supernatural signal toward a missing party while ordinary hostile Pokémon occupy the final route.

Full version dependencies:

- Trainer Features/perks — BLOCKING if the sensing effect comes from a Trainer Feature;
- movement/targeting/core/action economy — VERIFIED for ordinary battle;
- AI tactical policy — BLOCKING only if opponents use nonstandard objectives;
- adapter/playback — BLOCKING for overworld Aura visualization.

Reduced version:

The Aura result is resolved outside combat through an authoritative PTU/Caelo capability check or authored nonmechanical clue. The final encounter is an ordinary static battle. Aura never grants combat bonuses or hidden moveset knowledge.

## Encounter contract D — Psychic Residue Dispute

Narrative premise: two institutions disagree about the source of psychic residue left after an incident.

Full version dependencies:

- Trainer Features/perks — BLOCKING for Psionic Analysis/Telepath family;
- full lifecycle — PARTIAL where temporary residue lifetime matters;
- move-specific behavior/abilities/items — PARTIAL depending on source;
- adapter/playback — BLOCKING for residue presentation.

Reduced version:

The residue remains a narrative evidence object based on a previously validated Python result or authored case state. Players collect ordinary corroborating evidence. Any battle uses only verified basic combat families.

## Promotion checklist for dream/psychic content

Before a proposal enters canon, review:

1. Does the concept preserve objective fact vs subjective experience?
2. Does every supernatural observation cite a valid actor capability/Feature or remain clearly nonmechanical flavor?
3. Does it protect PC mental privacy and consent?
4. Does it avoid turning dreams into prophecy by default?
5. Does it avoid using a Legendary as an automatic explanation?
6. Are CASE/RESEARCH conclusions independently supportable?
7. Are battle dependencies classified using the permanent capability families?
8. Does a reduced version exist when full mechanics are blocking?
9. Does Minecraft presentation avoid implementing missing PTU rules locally?
10. Is all external inspiration transformed and attributed in `research/`?
