# Marea / Sendero marker-registry field study — Pass 254

Status: PROPOSED CONTENT
Canon effect: NONE
Date: 2026-09-04

## Premise

A local research programme maintains a small public-facing registry of individually marked wild Pokemon in Sendero. The player can contribute observations, photographs and re-sightings without capturing or battling the subjects.

No institution, researcher NPC, physical marker design or marked Fletchling is canonized by this proposal. Pass 254 uses a fixture-only colour-band example solely to exercise the evidence contract.

## Reduced playable loop

A field board or research terminal presents a request for observations of a marked local Fletchling. The player enters Sendero, finds a candidate, gets close enough for a clear view and records the visible marker code. The observation is compared against the public field registry.

A unique active registry match can confirm the player-facing hypothesis that this sighting is the same marked individual from earlier records. The game preserves location, time band, behaviour and evidence quality as research history.

A poor or partial view may only add ordinary behavioural evidence. It never guesses the unreadable part of the marker code.

If a later report establishes that the marker was lost, damaged or retired, current certainty is reduced while earlier confirmed sightings remain historically valid records of what observers knew at the time.

## Ecology consequences

Repeated sightings can expose site fidelity, shifts in activity window, changing tolerance, local resource use or avoidance pressure without increasing abundance.

Research observations may later help detect ecological changes: an individual stops using a perch, changes feeding area, appears at a different time, or repeatedly encounters the same disturbance source. Those are investigation hooks, not automatic demographic events.

## Quest/adventure structures

The field study can generate several small ecology-first tasks:

- verify whether a reported marker is still readable after a period of no sightings;
- distinguish one marked individual from an unmarked same-species confounder;
- reconcile conflicting observer reports that share the same provenance root;
- photograph a subject from a safer angle without flushing it from the area;
- compare current activity with older observations after resource pressure or disturbance changed;
- document that a marker is missing and downgrade the registry rather than pretending the individual died.

These tasks create longitudinal familiarity with local wild Pokemon while preserving uncertainty and avoiding a capture-first relationship.

## Failure and consequence design

Missing the observation window does not delete the Pokemon. A bad photograph yields weaker evidence. Disturbing the subject can increase avoidance pressure or change later projection eligibility if the existing ecology rules support that write.

A mistaken transcription can create an ambiguous registry lookup and should trigger follow-up investigation rather than a hidden automatic correction.

No quest state may create a new persistent Pokemon, reduce the population, resolve a world event or open AutoPTU by itself.

## Reduced implementation dependencies

Minecraft/Cobblemon/Craftics adapter/playback support is the main dependency. The runtime needs to present the correct visible marker for the correct projected actor and capture an observation without exposing internal actor/lease/UUID fields.

No battle capability family is required.

## Rich implementation dependencies

If the player must shadow the subject to obtain a clean view, use targeting/footprints/range/LoS, base movement legality, complete movement when interception or forced movement is possible, full turn/round lifecycle for structured pursuit, AI legal-action infrastructure, AI tactical policy, and adapter/playback.

If an adopted PTU Skill Stunt, Journey of Skill or other Trainer Feature modifies the observation roll, Trainer Features/perks becomes an exact dependency and remains blocked until live Java evidence covers that use.

Terrain/weather/hazards/zones/reactions applies only if observation conditions receive mechanical effects. Damage, status, Moves, Abilities and Items apply only when actually invoked.

## Canon questions before activation

A later canon pass must decide whether Sendero has an authorized wildlife-research institution, whether physical marking is acceptable, which species can be marked safely, how markers are applied or removed, and whether a non-invasive natural-mark registry is preferable for some Pokemon.

Until those decisions exist, the content remains a reusable field-research pattern rather than a live quest.