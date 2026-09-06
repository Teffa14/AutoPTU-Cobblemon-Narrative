# Nocturnal light observation contract — Pass 316

Status: DESIGN / NON-CANON IMPLEMENTATION BOUNDARY
Date: 2026-09-06

## Purpose

This contract keeps nocturnal ecology and tactical visibility from collapsing into one ambiguous `darkness` flag.

Pass 316 requires the world layer to represent authored lighting conditions and observations without claiming that AutoPTU already implements dynamic illumination, glare, night vision or species-specific visual ecology.

## Required separation

The following facts must remain distinct:

- world light-state source: what infrastructure/environment is authored to be doing;
- physical/ecological state: where an entity or population actually is, when that information is authoritative;
- source-backed signal production: whether an authored biological/environmental signal exists;
- observer context: actor, place and semantic time;
- detection result: what the actor actually detects;
- secondary evidence: tracks, feeding traces, silhouettes or other independent observations;
- interpretation claim: what the observer concludes from the available evidence;
- provenance: which observations support that conclusion.

A failed detection cannot mutate physical presence. A detected signal cannot automatically reveal its meaning. World truth cannot be copied wholesale into an ordinary NPC ledger.

## Reduced world-state vocabulary

Reduced-version scenarios may use authored scenario descriptors such as:

- `LIGHTS_ON`;
- `LIGHTS_REDUCED`;
- `LIGHTS_OFF`;
- `SIGNAL_DETECTED`;
- `SIGNAL_NOT_DETECTED`;
- `SECONDARY_PRESENCE_EVIDENCE`;
- `OBSERVATION_INCONCLUSIVE`.

These labels are not PTU conditions, battle statuses, universal perception rules or Minecraft block-light thresholds.

## Observation record minimum

A durable observation should be able to identify:

- observation ID;
- observer/producer actor;
- semantic time;
- location/observation node;
- authored light-state reference;
- directly observed phenomenon;
- source/provenance root;
- optional instrumentation/source reference;
- confidence or uncertainty if the world knowledge model already supports it.

Interpretations should be separate claims that reference one or more observations. The raw record must survive later reinterpretation.

## Comparative observation

A scenario can support stronger conclusions when observations differ by controlled context. Examples include the same time window from shielded and exposed viewpoints, or the same viewpoint before/after an authorized lighting change.

A comparison can support a narrower causal claim. It must not silently generalize to every species, season, location or long-term ecological outcome.

## Authority boundary

Ouros/world simulation owns persistent infrastructure state, ecological state and authored observations.

AutoPTU owns instantiated tactical legality and battle outcomes.

Minecraft/Cobblemon/Craftics may display fixtures, light levels, particles, animations and visual contrast. Presentation cannot independently decide that an actor can target through darkness, that a species is attracted/repelled, or that a biological signal was produced.

## Tactical visibility boundary

Current audited targeting/range/LoS support must not be interpreted as a verified illumination system.

Before a full tactical version uses darkness or glare to alter legal targets, cover, accuracy, reactions or AI choices, there must be an explicit contract for how illumination enters target legality and how that contract maps to PTU authority.

The reduced version therefore changes lighting only between scene states and uses authored observation outcomes.

## Species behavior boundary

No generic rule such as `nocturnal Pokémon avoid light`, `Bug-types are attracted to lamps`, or `Dark-types see in darkness` is permitted.

Species-specific reactions require one of:

- official/source-backed franchise behavior that is compatible with Ouros canon;
- directly validated PTU/Caelo/Kairos material with appropriate authority;
- explicit new Ouros canon adoption.

Battle Abilities and Move names cannot be promoted into ecological facts by analogy.

## PTU / Caelo boundary

No PTU or Caelo numeric illumination mechanic is adopted by Pass 316. Direct source validation is required for any Perception/Survival check structure, concealment/visibility modifier, Flash interaction, Illuminate interaction, Trainer Feature, Item or species sensory capability.

Repository inspection did not locate a Caelo artificial-light/nocturnal-visibility overlay. That family remains `UNVERIFIED`.

## Capability dependency rules

Ordinary targeting/footprints/range/LoS remains VERIFIED only within its existing audited contracts. Illumination-sensitive target legality is a new dependency on terrain/zones/visibility plus adapter support unless separately verified.

Base movement legality can support navigation through static authored nodes. Complete movement remains required for forced movement, interception or moving-hazard interactions.

Exact in-round lighting changes require full turn/round lifecycle. Persistent consequences require the appropriate stateful damage/status lifecycle. Dynamic light fields and electrical/environmental hazards require the corresponding terrain/weather/hazards/zones/reactions subfamilies.

Special Move, Ability, Item or Trainer Feature interactions each require their own verified implementation family. AI legal-action infrastructure can constrain already-defined legal actions, but AI tactical policy is required before autonomous actors can reason generally about exploiting light/shadow state.

Minecraft/Cobblemon/Craftics playback remains presentation until an authoritative adapter contract synchronizes world light state, battle state and client effects end-to-end.

## Failure modes this contract forbids

- treating no visual detection as proof of absence;
- treating Minecraft brightness as ecology truth;
- treating ordinary LoS as verified night vision;
- using an Ability's name/flavor as an unverified field rule;
- applying a generic nocturnal preference to all Pokémon;
- allowing a later interpretation to overwrite the original observation;
- giving every NPC a corrected conclusion because the simulator learned it;
- inventing a tactical status solely to make the narrative concept work.

## Canon boundary

This design contract creates no place, species, facility, incident, NPC, faction or historical fact. `The Ridge That Never Got Dark` remains a proposal until explicitly adopted.