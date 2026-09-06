# Acoustic observation and masking contract — Pass 315

Status: DESIGN CONTRACT / PROPOSED IMPLEMENTATION BOUNDARY
Date: 2026-09-06

## Purpose

This contract defines how future Ouros narrative/world systems may represent acoustic observations without making sound a hidden universal battle simulator and without treating nondetection as proof of absence.

It is derived from Pass 315 research and remains subordinate to canon and direct PTU source validation.

## Core separation

The world must keep these facts separable:

- physical occupancy or presence evidence;
- a signal-producing behavior, if one is actually source-backed;
- whether an observer or instrument detected a signal;
- local masking/disturbance conditions;
- the observer's interpretation;
- later conclusions reached from multiple observations.

A missing detection is therefore an observation outcome. It is not itself an occupancy verdict.

## Minimum durable observation record

A future typed record should contain at least:

- `observation_id`;
- `observer_id` or instrument/source identity;
- `location_id`;
- semantic observation time or window;
- observation channel, such as audible call, vibration, surface ripple, visual secondary evidence or instrument reading;
- directly observed result;
- provenance/source reference;
- known local operational state if actually available to that observer;
- confidence/quality metadata where justified;
- interpretation claim IDs stored separately from raw observations.

Species expectation, hearing range and signal identity must not be invented by the record itself. Those come from canon/source-backed definitions.

## Nondetection rule

`NO_SIGNAL_DETECTED` may support questions such as:

- Was the expected signal absent at this location and time?
- Was it masked?
- Was the observer capable of detecting it?
- Did behavior shift to another time or place?
- Was the instrument functioning?

It may not directly assert:

- the population is absent;
- the population died;
- a specific actor caused the silence;
- the signal never occurred;
- all species in the area were affected.

Those conclusions require additional evidence.

## Masking rule

Masking is an environmental relationship between a candidate signal, an observer/detector and competing sound or vibration. It is not a universal radius effect.

A future implementation should prefer authored or evidence-backed mask relationships such as:

`observer A at site B during machine state C cannot reliably detect signal family D`

rather than a generic equation that invents Pokémon hearing thresholds.

If a later PTU/Caelo/source overlay provides quantitative rules, the overlay can refine this contract without changing the provenance distinction.

## Observation triangulation

A conclusion can become stronger when independent observations disagree in an informative way. Examples:

- lower site: no signal detected;
- ridge site: signal detected during the same authored window;
- habitat edge: fresh secondary presence evidence;
- machine schedule: masking source active only during the lower-site observation.

The system should preserve each observation rather than collapse them into one `ACOUSTIC_STATE` boolean.

## Controlled experiment boundary

An authored operational test may change one world condition, such as machinery on/off or an observation post location. Results are recorded as new observations.

The experiment cannot automatically establish causation. The narrative author must define which competing explanations are actually controlled and which remain open.

## Knowledge boundary

NPCs learn acoustic findings only through direct observation, instrument access, communicated claims or other existing information-delivery mechanisms. A monitor discovering a signal does not update every ranger, operator or resident.

Raw observations and interpretations should remain separately communicable. An NPC can truthfully say that a recorder detected nothing while being wrong about why.

## Species boundary

Species-specific behavior requires provenance.

Official Pokédex material can establish candidate traits such as communication by sound, vibration or signals outside ordinary human hearing. It does not establish that every population uses the behavior in every habitat, nor does a combat Ability automatically define ecological perception.

No generic Pokémon hearing model is authorized by this contract.

## Battle boundary

Acoustic world observations do not create tactical effects by themselves.

A sound-based Move, Soundproof, a Trainer Feature, a persistent condition, forced movement, an interrupt, a zone or environmental damage requires its own verified PTU/engine contract. The narrative layer must not emulate a missing battle mechanic by changing HP, statuses or tactical positions directly.

## Reduced implementation profile

A safe near-term implementation may use authored scene states and evidence records only:

- `AUDIBLE`;
- `MASKED`;
- `QUIET_UNRESOLVED`;
- `SECONDARY_PRESENCE_EVIDENCE`.

These are scenario descriptors, not PTU statuses. Changes occur between world scenes. No wave propagation, hearing radius, damage, forced movement or status lifecycle is simulated.

## Full implementation profile

A later full encounter may combine acoustic evidence with tactical combat only after the relevant capability families are verified. Dynamic machine cycles require lifecycle support. Acoustic or structural zones require terrain/hazards/zones/reactions. Special sound Moves require move-specific behavior. Soundproof requires Ability coverage. Panic displacement or rescue requires complete movement. Environmental injury requires the full stateful damage pipeline. Autonomous responses require AI tactical policy. End-to-end representation requires Minecraft/Cobblemon/Craftics adapter/playback support.

## Persistence boundary

World acoustic observations should survive checkpoint/restart if they drive persistent investigation state. Client audio playback must not become the source of truth. A restart may reproduce presentation from world state, but it must not infer world state from what a client happened to play.

## Pass 235 compatibility

Migration Pass 235 remains authoritative for the project's proposed migration/stopover model. Acoustic observations may become evidence about a migrating or resident cohort, but this contract does not alter route progress, stopover state, temporal niches or population history.

## Canon boundary

This contract is implementation guidance. It does not canonize The Valley That Stopped Answering, any species, any facility, any cause, or any location.