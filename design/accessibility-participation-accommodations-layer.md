# Accessibility, Participation & Accommodations Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

This layer lets Ouros represent barriers, access information, accommodations and equivalent participation paths across travel, buildings, education, competitions, research, workplaces, public events, multiplayer communication and exploration.

It does not create diagnoses, disabilities, medical records, PTU mechanics or character weaknesses.

## Core separation

Keep these states separate:

- actor identity;
- player-facing accessibility settings;
- self-described access preferences;
- observed functional requirement for a specific activity;
- environmental or interface barrier;
- offered accommodation;
- accepted accommodation;
- actual participation result;
- PTU mechanical state;
- medical/care state.

A player enabling captions does not create a hearing-related character trait. A character using a mobility aid does not gain Slowed. A person declining stairs does not prove an Injury.

## Access profile

```yaml
access_profile:
  actor_id: null
  owner_controlled: true
  disclosed_preferences: []
  preferred_communication_channels: []
  preferred_information_formats: []
  timing_preferences: []
  mobility_support_preferences: []
  sensory_preferences: []
  privacy: private
  provenance_refs: []
```

For PCs, this record is player-authored or explicitly consented. The generator must not infer it from behavior.

NPC profiles may be authored as canon, but the system should store only what is useful for participation and characterization.

## Barrier record

A barrier belongs primarily to an interaction between a person and an environment/task.

```yaml
access_barrier:
  barrier_id: null
  context_type: route|building|event|interface|communication|puzzle|workplace|education|competition|expedition
  context_id: null
  affected_requirement: null
  barrier_kind: mobility|vision|hearing|speech|timing|input|cognitive_load|communication|sensory|other
  observed_effect: null
  start_time: null
  end_time: null
  temporary: false
  source_refs: []
```

Avoid universal claims such as `actor cannot explore`. Record the specific boundary: `east stair entrance has no step-free route while lift B is offline`.

## Accommodation record

```yaml
accommodation:
  accommodation_id: null
  context_id: null
  requested_by: null
  provided_by: null
  accommodation_kind: alternate_route|alternate_format|caption|narration|extended_time|rest_break|seating|quiet_space|input_remap|visual_signal|text_signal|support_person|equipment|remote_participation|other
  preserves_core_requirement: true
  changes_mechanical_resolution: false
  accepted: null
  start_time: null
  end_time: null
  privacy: private
  source_refs: []
```

An accommodation should normally preserve the meaningful objective while removing an incidental barrier.

Example:
- core objective: identify the correct migration pattern from evidence;
- incidental barrier: evidence is encoded only by red/green markers;
- accommodation: add shapes/text labels;
- result: the reasoning problem remains unchanged.

## Functional requirement

```yaml
participation_requirement:
  requirement_id: null
  activity_id: null
  essential_outcome: null
  current_presentation_methods: []
  alternate_methods: []
  PTU_mechanic_ref: null
  implementation_ref: null
```

Before creating an alternate path, identify what the activity is actually testing.

A battle institution may require legal battle decisions. It should not require tiny text. A field survey may require observation and reasoning. It need not require hearing a cue if the same phenomenon can be represented another way.

## Multi-channel information

Important information can expose semantic meaning independently from presentation.

```yaml
semantic_cue:
  cue_id: null
  event_type: null
  meaning: null
  presentation_channels:
    audio: null
    caption: null
    visual: null
    haptic: null
    text_log: null
  required_for_progression: false
```

This integrates directly with the soundscape layer. Sound events should be semantic enough for Minecraft captions or other client-side presentation.

Never assume Soundproof, deafness, Blinded or any PTU effect changes access to overworld semantic cues unless an authoritative rule says so.

## Accessible route state

Travel and building access should use existing route/building graphs.

```yaml
access_route_variant:
  route_variant_id: null
  connection_id: null
  access_features: []
  restrictions: []
  service_dependencies: []
  current_state: open|degraded|closed|unknown
  information_last_verified: null
```

Examples of access features:
- step_free;
- lift;
- rest_points;
- wide_clearance;
- low_gradient;
- staffed_assistance;
- alternate_boarding;
- remote_service.

These are narrative/world properties. They do not redefine PTU movement rates.

## Institution access plan

```yaml
institution_access_plan:
  institution_id: null
  public_access_info: []
  contact_channel_ids: []
  physical_access_routes: []
  communication_options: []
  quiet_space_ids: []
  seating_options: []
  alternate_format_resources: []
  event_adjustment_policy_refs: []
  temporary_outage_ids: []
  review_history: []
```

A Gym, museum, academy, clinic or Contest venue may publish this information before arrival.

Published information can become stale. The communications layer owns delivery and corrections.

## Event participation plan

```yaml
event_access_plan:
  event_id: null
  venue_id: null
  essential_requirements: []
  available_accommodations: []
  request_deadline: null
  on_site_contact_ids: []
  communication_channels: []
  evacuation_access_plan_ref: null
  accessibility_incident_refs: []
```

Competitive accommodation should be explicit. Do not secretly alter PTU outcomes in the name of access.

## Accessibility incident

```yaml
accessibility_incident:
  incident_id: null
  context_id: null
  barrier_ref: null
  affected_actor_ids: []
  observed_consequence: null
  immediate_response: null
  follow_up_project_refs: []
  public_summary_ref: null
  status: open
```

An incident can become a public-works, staffing, maintenance, communications or event-design issue.

It should not become a medical case unless a separate care event actually exists.

## Temporary outages

Access can change even when the underlying facility normally supports it.

Examples:
- lift offline;
- accessible ferry boarding unavailable during repairs;
- caption display failure;
- quiet room repurposed during crisis response;
- step-free route blocked by construction;
- accessible map terminal disconnected.

These should be ordinary infrastructure/service state, not proof of malicious exclusion.

## Assistive devices

```yaml
assistive_device_instance:
  item_instance_id: null
  owner_or_user_id: null
  device_category: null
  provenance_ref: null
  maintenance_state: null
  mechanical_effect_ref: null
```

A mobility aid, hearing device, communication aid or other support can exist as an ordinary item.

`mechanical_effect_ref` remains null unless PTU/Caelo/AutoPTU explicitly defines a mechanical effect.

Narrative generation may not create Speed penalties, accuracy modifiers, movement modes, sensing bonuses or other combat effects from the presence or absence of the device.

## Support persons and co-piloting

A player or character may choose support without losing agency.

```yaml
support_arrangement:
  arrangement_id: null
  primary_actor_id: null
  support_actor_id: null
  permitted_support_actions: []
  prohibited_decisions: []
  context_id: null
  consent_state: explicit
```

Support can include navigation assistance, reading text, carrying equipment, interpreting communication or handling an input channel.

The support actor does not automatically make story decisions for the primary actor.

## Multiplayer communication

Critical coordination should not require voice chat.

Preferred tools:
- pings;
- map markers;
- contextual emotes;
- structured intent messages;
- text chat;
- captioned system events;
- optional text-to-speech/speech-to-text where the client supports it.

Personal accessibility preferences remain private by default.

## Puzzles and dungeons

Mandatory puzzles need:
- clear discoverability of the puzzle state;
- no reliance on color alone;
- no reliance on sound alone;
- no required rapid repeated inputs unless an equivalent path exists;
- a reset/recovery path after failed manipulation;
- objective reminders when state is complex;
- alternate presentation that preserves the reasoning problem.

Do not use a real-world accessibility system, language or aid merely as an exotic cipher unless the cultural/world context justifies it and the player-facing implementation remains accessible.

## Accessible difficulty versus game difficulty

Accessibility options and challenge level are separate.

Examples:
- larger text does not make a battle easier;
- captions do not lower enemy stats;
- longer UI reading time does not change PTU initiative;
- alternate puzzle presentation does not reveal the answer;
- input remapping does not change the action budget.

If an assist mode changes mechanical challenge, record that separately and make the effect transparent.

## Worldbuilding rule for disability

Disabled characters can be Trainers, rivals, researchers, workers, leaders, performers, criminals, historians, parents, antagonists, mentors, athletes or background residents.

Do not generate a mandatory cure arc.
Do not make disability the explanation for morality.
Do not treat ordinary assistance as a heroic sacrifice.
Do not infer suffering, dependence, inspiration or bitterness from an aid or diagnosis.

A character may have an access-related story when authored, but their role should not collapse into that single dimension.

## Minecraft/Cobblemon translation

Useful adapter-facing state includes:
- semantic captions for world events;
- high-contrast/symbol-redundant markers;
- text/list alternatives for map objectives;
- configurable UI size where technically possible;
- step-free route metadata;
- temporary access outages;
- alternative interaction prompts;
- accessible event information;
- server-side pings and structured communication;
- preserved player-specific accessibility settings.

Minecraft's own accessibility features should be used when available rather than recreated server-side.

## PTU/Caelo boundary

This layer cannot grant or alter:
- Overland, Swim, Sky, Jump, Burrow or other movement values;
- Naturewalk or movement capabilities;
- Blinded, Slowed, Vulnerable, Injury or other statuses;
- Perception or Skill modifiers;
- Trainer Features or Edges;
- Ability effects;
- initiative;
- action economy;
- item effects.

Those remain source-gated.

## Battle encounter boundary

Most access state belongs outside AutoPTU.

When access is part of a mechanically rich encounter, the FULL version must identify exact capability dependencies. A REDUCED version should move access logistics outside the grid rather than duplicate unfinished mechanics in Minecraft.

## Promotion checklist

Before any accessibility-related proposal enters canon:
1. Is the character state authored rather than inferred?
2. Is the barrier specific to the context?
3. Does the accommodation preserve the meaningful objective?
4. Does it avoid granting unverified PTU mechanics?
5. Does the player-facing implementation expose required information through more than one channel?
6. Are privacy and consent preserved?
7. Is the representation doing more than turning disability into tragedy, cure or inspiration?
8. Does Minecraft already provide a feature that should be used instead of reimplemented?