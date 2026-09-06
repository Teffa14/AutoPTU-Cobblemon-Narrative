# The Valley That Stopped Answering — Pass 315

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

A field team reports that a familiar dawn exchange has vanished from one managed-development basin. The disturbing detail is not that nobody has seen the local Pokémon. Tracks, feeding traces and occasional distant silhouettes still exist. The basin has become acoustically quiet at the time when observers expected a recurring exchange.

The player is asked to determine what changed without assuming that silence means disappearance.

No location, species, institution or incident in this proposal is canon until explicitly adopted.

## Core mystery

The investigation compares four kinds of evidence:

1. what is physically present;
2. what observers can hear or otherwise detect;
3. what local machinery, terrain and weather can mask or alter;
4. what behavior was actually expected, and why.

The first observation post is near a service road or utility structure. The second is elevated and farther from machinery. The third is close to habitat with secondary evidence such as movement, surface disturbance, nests, tracks or feeding remains. A fourth optional site sits beyond the apparent quiet zone.

The central design rule is that each site can answer a narrower question. No single observation produces an omniscient ecology diagnosis.

## Candidate explanations

The authored scenario should select one or combine compatible causes only after canon review. Valid candidates include:

- masking from a new or rescheduled machine while the population remains present;
- a shift in calling time caused by disturbance or another ecological pressure;
- relocation to a nearby refuge without population collapse;
- genuine local decline or departure;
- a faulty recorder or observer expectation;
- a mechanical echo or repeated rhythm misclassified as a biological signal;
- an intentional acoustic deterrent installed for a legitimate safety purpose but producing an unanticipated ecological consequence;
- concurrent factors, such as masking plus habitat degradation.

A deliberate actor is optional. The mystery does not require sabotage.

## Quest loop

The player begins with a report of silence, not a report of extinction.

They establish or revisit listening/observation posts at distinct positions and times. The player records what was directly observed separately from what an NPC thinks it means. A ridge observation can reveal a distant signal that the lower basin cannot detect. A habitat-edge observation can show secondary presence evidence during apparent silence. An infrastructure schedule can reveal a strong temporal correlation.

If the operator cooperates, a short controlled shutdown or schedule change becomes an optional experiment. If the signal becomes detectable during the quiet interval, that supports masking but still does not prove every downstream ecological consequence. If nothing changes, the investigation remains open and the player must test another explanation.

The final decision can be operational rather than punitive: alter a schedule, add a quiet interval, move an observation post, redesign a warning system, protect a refuge, continue monitoring, or escalate because genuine population loss is supported.

## NPC and faction roles

The proposal works with roles rather than fixed canon characters.

A field observer has longitudinal knowledge but can be overconfident about a familiar pattern. An infrastructure operator understands machinery and schedules but may initially interpret the issue as anecdotal. A local worker or traveler has repeated embodied experience of the route but incomplete ecological context. A researcher can provide measurement discipline without becoming an infallible oracle. A stakeholder affected by shutdowns can reasonably resist a permanent restriction while still supporting a limited test.

This creates conflict from partial knowledge and competing costs rather than requiring a villain.

## Environmental storytelling

The basin should communicate the problem before an NPC explains it. Near machinery, ambient noise or vibration dominates presentation. Higher ground reveals a different acoustic layer. Quiet habitat still contains visual evidence of recent use. Old field markers or observation notes show where previous listening occurred. A schedule board or maintenance log allows the player to compare human activity with observation windows.

If Minecraft playback cannot represent useful sound differences yet, the reduced version uses authored captions, particles, visible secondary evidence and observation records. The narrative premise stays the same.

## Full encounter version

A mechanically rich version places one observation post in an unstable echo gallery, ravine, quarry shelf or service cut where sound-sensitive behavior, environmental noise and physical danger can overlap.

Possible authored events include:

- a loud tactical action or sound-based Move disturbing a nearby group;
- a timed machine cycle changing the local acoustic state;
- falling debris after a clearly telegraphed structural disturbance;
- a rescue across uneven terrain while visibility or communication is degraded;
- a sound-producing Pokémon or Ability changing what can be heard or how a combatant is affected.

These events require explicit PTU and engine validation. They are not available merely because the story mentions sound.

## Reduced implementation version

The reduced version requires no tactical acoustic simulation.

The area uses authored observation nodes with states such as `AUDIBLE`, `MASKED`, `QUIET_UNRESOLVED` and `SECONDARY_PRESENCE_EVIDENCE`. Those labels describe scenario evidence, not universal engine statuses.

Machinery changes between scene phases rather than during combat rounds. No sound wave pushes actors. No noise applies damage. No hearing radius is calculated. No sound-based Move changes ecology unless a specific authored interaction has been verified. An unstable route is represented as open or blocked rather than using delayed collapse or forced movement.

The player can still solve the full narrative problem through repeated observation, schedule comparison, source-backed species evidence and stakeholder decisions.

## Capability dependencies for the full version

Targeting/footprints/range/LoS: required if sound-linked encounters also use tactical targeting or spatial rescue. Current project evidence: VERIFIED within audited contracts.

Base movement legality: required for navigation between observation positions. Current project evidence: VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement: required only for debris displacement, panic movement, forced repositioning or reaction rescue. Current project evidence: PARTIAL.

Core calculations: required for ordinary deterministic combat arithmetic. Current project evidence: VERIFIED within audited contracts.

Action economy/initiative: required for structured tactical scenes. Current project evidence: VERIFIED within audited contracts.

Full turn/round lifecycle: required if machine cycles, echoes or collapses change state at reliable phase boundaries. Current project evidence: PARTIAL. AutoPTU-Java PR #384 strengthens round-history pruning only and does not complete this family.

Full stateful damage pipeline: required for environmental or combat damage with all ordinary downstream consequences. Current project evidence: PARTIAL.

Status lifecycle: required if any verified sound-related condition persists or expires. Current project evidence: PARTIAL. This proposal does not invent a `deafened`, `ringing` or similar status.

Terrain/weather/hazards/zones/reactions: required for acoustic zones, unstable shelves, debris, environmental reactions or dynamically changing safe areas. Current project evidence: MIXED / PARTIAL / BLOCKING by subfamily.

Move-specific behavior: required before a sound-based Move can have special environmental or battle behavior beyond its verified PTU implementation. Current project evidence: PARTIAL.

Abilities: required before Soundproof or another Ability is allowed to alter the encounter in its full PTU-defined way. Current project evidence: PARTIAL.

Items: required only if a PTU item participates mechanically. Current project evidence: PARTIAL.

Trainer Features/perks: required if a Feature modifies observation, interrupts, communication or combat. Current project evidence: PARTIAL.

AI legal-action infrastructure: required for autonomous actors to choose only legal structured actions. Current project evidence: VERIFIED within audited contracts.

AI tactical policy: required for autonomous tactical decisions such as choosing a rescue route, exploiting acoustic cover or avoiding a hazardous sound source. Current project evidence: BLOCKING for general policy.

Minecraft/Cobblemon/Craftics adapter/playback support: required to reproduce authoritative machine state, spatial audio cues, Pokémon reactions and tactical consequences end-to-end. Current project evidence: PARTIAL / BLOCKING end-to-end.

## Canon questions before adoption

A canon pass must decide whether this occurs in Marea Interior or elsewhere. If Marea is used, the exact location must fit the approved corridor network instead of creating a new edge by implication.

A canon pass must also select a species or keep the phenomenon multispecies. Species behavior must be source-backed; no generic Pokémon hearing model is permitted.

The responsible infrastructure, its legitimate purpose, the historical baseline and any stakeholder relationships need explicit approval. The proposal should remain usable even if the final cause is ordinary operational conflict rather than sabotage.

## Mechanical questions before full implementation

Direct PTU/Caelo validation is still required for any Perception/Survival interaction, sound-based Move, Ability, hearing limitation, Trainer Feature or persistent condition used mechanically.

The world layer also needs an authoritative way to store observational acoustic state without pretending it is tactical battle state. If future Minecraft audio is presentation-only, the causal source of truth must remain in the world simulation rather than in client playback.