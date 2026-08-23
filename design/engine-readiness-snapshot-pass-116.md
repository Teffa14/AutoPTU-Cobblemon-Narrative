# Engine Readiness Snapshot — Pass 116

Status: implementation evidence snapshot for narrative dependency labeling. AutoPTU-Java and AutoPTU are read-only from this task.

## Live heads inspected

AutoPTU-Java `main`: `cdb229db787ac93f28745f796c1d9944546676cc`

Newest relevant Java evidence:

- generic Trainer Feature effects now include parity-backed `apply_status` and `remove_status` handlers;
- tested cases include new status application, duration refresh, preserving a longer existing duration, stacked duplicate entries, named removal and removing all statuses;
- the handlers mutate canonical `BattleRuntimeState` status entries;
- previous slices already provide ordered stacked status storage, generic Trainer Feature prerequisites, context gates, frequency/cooldown gates, resources, usage bookkeeping, target scopes, trainer-target scopes, heal, Combat Stage, temporary HP and AP effect primitives.

This is meaningful evidence for Trainer Feature execution infrastructure and status-state mutation. It is not evidence for research consent, welfare state, handling rules, experimental procedures, the complete status controller or the complete Trainer Feature catalog.

AutoPTU `main`: `0db989a259f84d04e7fdcb161bb986bc6ef69275`

The newest Python commit inspected rebuilds the Career Vercel bundle when runtime inputs change. The immediately prior visible changes add Generation 9 PBS files and Career/persistence fixes. None justify tactical capability promotion.

## Java README evidence

The live Java README still lists as unfinished:

- expanded core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete move/ability/item/perk/Trainer Feature hook registries;
- semantic full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Representative mechanics remain representative only.

## Permanent capability categories

### VERIFIED

- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

### PARTIAL

- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

### BLOCKING

- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter and playback

No permanent category is promoted in Pass 116.

## Latest status/Trainer Feature evidence boundary

The Java `apply_status`/`remove_status` slice proves a narrow generic effect contract against the Python oracle.

It does not prove:

- all PTU statuses are fully implemented;
- all immunities/preventions exist;
- all durations/expiry rules exist;
- every Trainer Feature that applies or removes a status exists;
- research procedures can create statuses;
- handling can create damage/status;
- restraint/sedation exists;
- Care or research state can override battle mechanics;
- a narrative welfare observation has a mechanical status equivalent.

Therefore `status lifecycle` and `Trainer Features / perks` remain PARTIAL.

## Why research ethics is outside the battle core

Nothing inspected in Java or Python proves an authoritative subsystem for:

- research-protocol authorization;
- participant consent;
- withdrawal of consent;
- Pokémon research assent/refusal;
- human-subject privacy;
- secondary data use;
- sample-use permission;
- destructive-analysis authorization;
- field-impact review;
- institutional ethics review;
- sensitive-site publication restrictions;
- experimental modification authorization;
- protocol amendments;
- protocol deviations;
- adverse-research-event review.

Those are overworld/institutional responsibilities.

AutoPTU may supply mechanical battle or health facts when they actually occur. It does not decide whether a procedure was authorized or ethically acceptable.

## Pass 116 encounter dependency map

### Nest Survey Withdrawal — FULL

Narrative objective:

Stop a study after unexpected early nesting and withdraw researchers/visitors while preventing further intrusion into the sensitive site.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for dynamic withdrawal, interception and protected routing
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if the site uses live tactical terrain/weather/protected zones
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for `WITHDRAW`, `PROTECT_AREA`, `DO_NOT_ENTER`
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Pause the protocol in world state. Move researchers/visitors outside the sensitive zone before battle. Keep Eggs/nests entirely outside the grid. If an unrelated threat remains, use a static legal battle. Preserve the early-nesting observation and protocol stop afterward.

### Research Annex Emergency Shutdown — FULL

Narrative objective:

Stop an experimental instrument after an unexpected response, evacuate staff, secure the site and preserve evidence for later review.

Dependencies:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING for evacuation/interception
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING if any instrument effect becomes a live tactical zone/hazard
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING for shutdown/evacuate/protect behavior
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced version:

Enter `SAFE_SHUTDOWN` in overworld state before battle. Remove staff from the grid. If combat remains, use a static arena. Device logs, Pokémon behavior, any care case and protocol deviation are reviewed after combat. No custom damage, Status or field effect is fabricated.

### Consent Withdrawal During Handling

Narrative objective:

End a procedure when the relevant participation/subject-protection condition no longer holds.

Default implementation:

No battle.

No PTU capability is required merely to stop research.

A PC decline is explicit player input. A Pokémon withdrawal/cooperation observation is stored as the smallest defensible observed fact. No Charm, Command or Guile roll is invented to force continuation.

A separate threat can create a separate ordinary battle, but that battle never retroactively validates the interrupted procedure.

## New overworld blockers introduced by Pass 116

These belong outside AutoPTU-Java:

- `RESEARCH_PROTOCOL_STATE`
- `PROTOCOL_VERSION_HISTORY`
- `PROTOCOL_AUTHORIZATION_STATE`
- `RESEARCH_SITE_AUTHORIZATION_STATE`
- `PARTICIPANT_PERMISSION_STATE`
- `POKEMON_SUBJECT_PROTECTION_STATE`
- `POKEMON_ASSENT_OBSERVATION_STATE`
- `SENSITIVE_LIFE_STAGE_RESTRICTION_STATE`
- `RESEARCH_STOP_CONDITION_STATE`
- `RESEARCH_STOP_EVENT_HISTORY`
- `PROTOCOL_AMENDMENT_HISTORY`
- `PROTOCOL_DEVIATION_HISTORY`
- `ADVERSE_RESEARCH_EVENT_STATE`
- `DATA_USE_PERMISSION_STATE`
- `SAMPLE_USE_PERMISSION_STATE`
- `SECONDARY_USE_REQUEST_STATE`
- `SENSITIVE_SITE_RESTRICTION_STATE`
- `FIELD_IMPACT_LEDGER`
- `RESEARCH_ETHICS_TO_SCIENCE_HANDOFF`
- `RESEARCH_ETHICS_TO_POKEMON_AGENCY_HANDOFF`
- `RESEARCH_ETHICS_TO_CARE_HANDOFF`
- `RESEARCH_ETHICS_TO_CONSERVATION_HANDOFF`
- `RESEARCH_ETHICS_TO_PSYCHIC_PRIVACY_HANDOFF`
- `RESEARCH_ETHICS_TO_INSTITUTIONAL_REVIEW_HANDOFF`
- `RESEARCH_ETHICS_TO_MEDIA_PUBLICATION_HANDOFF`
- `RESEARCH_ETHICS_TO_MINECRAFT_PROJECTION`
- `RESEARCH_ETHICS_TO_FROZEN_BATTLE_SNAPSHOT`

## Hard non-inferences for Pass 116

Do not infer:

- scientific usefulness -> authorization;
- institution approval -> participant consent;
- site access -> sample collection authority;
- sample custody -> destructive-analysis authority;
- Trainer agreement -> Pokémon consent;
- Pokémon ownership claim -> unlimited research authority;
- capture -> research permission;
- one cooperative Pokémon interaction -> enduring consent;
- refusal/withdrawal -> hostility or disobedience;
- research role -> Researcher Class/Feature/Skill Rank;
- protocol deviation -> misconduct;
- adverse event -> negligence;
- mechanical Status -> ethical harm conclusion;
- narrative distress -> PTU Status;
- successful battle command -> consent;
- public battle record -> private medical/psychic data;
- publication -> truth;
- published location -> safe-to-disclose location;
- null result -> failed mission;
- sponsor funding -> authority over research conclusions;
- generic Trainer Feature status handler -> research-induced status subsystem;
- generic Trainer Feature execution primitives -> full Trainer Feature catalog;
- Minecraft equipment animation -> authorized procedure;
- accessible Egg/nest -> collectible research specimen;
- communicative Pokémon -> universal telepathic permission.

## PTU/Caelo validation state

The complete primary Caelo corpus was not reliably available as an invocable source during this run.

Super PTU Online Helper was not exposed as an invocable capability.

No new PTU/Caelo mechanic for research consent, handling, sampling, sedation, restraint, privacy, experimental modification, clinical research or field ethics was validated.

Potentially relevant exact rules remain pending and should be checked only when a future concept actually invokes them, especially:

- Command / Loyalty;
- Charm / Guile / Intuition;
- Researcher and Education-related Features;
- psychic/telepathic Features;
- medical/restraint/healing rules;
- capture/release/handling rules;
- sample-collection or equipment interactions if such rules exist.

No social Skill roll should be allowed to force PC participation, override a Pokémon subject-protection stop, authorize psychic access or make an invalid protocol valid.

## Summary of current implementation posture

Research ethics can be implemented substantially before the battle engine is complete because its primary state is overworld/institutional.

The reduced encounter versions are viable with the currently VERIFIED battle foundations because every ethically important state transition happens before or after the static battle.

The full versions remain blocked where they depend on moving noncombatants, withdrawal/protection objectives, dynamic hazards/zones, tactical AI and Minecraft semantic playback.