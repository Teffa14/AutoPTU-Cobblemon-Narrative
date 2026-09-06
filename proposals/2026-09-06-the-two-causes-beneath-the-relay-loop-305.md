# The Two Causes Beneath the Relay — Pass 305

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

A communications relay fails during a period of difficult regional weather. Early evidence splits the investigation. Maintenance records and material inspection support long-term deterioration. Scene evidence also supports deliberate interference.

The initial question is framed incorrectly by several NPCs: accident or sabotage?

The deeper investigation can establish that both contributed. The relay was already vulnerable. A deliberate intervention exploited that vulnerability and converted a degraded system into an outage.

## Why this matters for Ouros

The loop lets the world preserve partial responsibility instead of collapsing the incident into one culprit flag.

A maintenance office may have failed to address a known defect. A saboteur may still have intentionally interfered. A dispatcher may have acted correctly with the information available. A traveler may have suffered consequences without any one actor being responsible for every part of the chain.

Different NPCs can retain different conclusions because they receive different evidence at different times.

## Investigation structure

Opening state:
- a warning fails to arrive because the relay is unavailable;
- Pass 302 can establish the communication failure without assigning blame;
- Pass 303 can create the infrastructure incident and evaluate initial evidence;
- Pass 304 keeps those findings durable across restart.

First evidence family:
- maintenance log or inspection supports deterioration, corrosion, fatigue or another non-deliberate contributor;
- result can become `ACCIDENTAL_CAUSE_SUPPORTED`.

Second evidence family:
- physical scene evidence supports deliberate cutting, bypassing or interference;
- result can become `CAUSE_CONTESTED` if both families are present but their relationship is unknown.

Third evidence family:
- an independent reconstruction supports that both factors materially contributed;
- result can become `CONTRIBUTING_CAUSES_CORROBORATED` with `cause_structure = CONCURRENT`.

Responsibility branch:
- access evidence may link a person to the site;
- attributable intent evidence may later support deliberate sabotage;
- proving sabotage does not erase the maintenance contributor.

## NPC and faction dynamics

Suggested archetypes, all non-canon placeholders:

A field maintainer wants the defect understood because a simplistic sabotage finding could hide systemic neglect.

A security investigator wants to identify deliberate interference before another site is targeted.

A local administrator is under pressure to restore service quickly and may prefer a single clean explanation.

A rival technical contractor benefits commercially if the incumbent maintenance organization receives all blame.

A witness possesses useful access information but has weak knowledge of the physical failure.

None of these roles knows the full truth by default.

## Consequences

If only deterioration is established, security risk can remain hidden.

If only sabotage is established, the repaired site may still be structurally vulnerable because the underlying degradation remains.

If concurrent causation is established, the repair objective expands: restore the damaged component, correct the material weakness, review nearby infrastructure and decide how responsibility should be distributed.

If actor intent is later established, social and institutional consequences can target deliberate conduct without converting every earlier maintenance failure into intentional complicity.

## Full encounter version

The relay sits on a weather-exposed ridge. Investigation and repair involve unstable access, active wind, loose debris, an intermittent electrical or energy hazard, a stranded technician and the possibility that whoever interfered with the site returns.

Mechanical dependency categories:
- targeting/footprints/range/LoS: needed for tactical spatial actions at the site;
- base movement legality: needed for ordinary traversal;
- complete movement: needed for wind displacement, forced movement, rescue interception or knockback;
- core calculations: needed for ordinary deterministic combat arithmetic;
- action economy/initiative: needed if the site enters structured tactical resolution;
- full turn/round lifecycle: needed for timed surges, collapsing supports or phase changes;
- full stateful damage pipeline: needed for authoritative environmental damage;
- status lifecycle: needed for persistent shock, exposure or other conditions if authored;
- terrain/weather/hazards/zones/reactions: needed for active ridge weather, debris zones and reaction rescues;
- move-specific behavior: needed if individual Moves interact mechanically with the site;
- abilities: needed for Ability-triggered environment effects;
- items: needed for mechanically active equipment;
- Trainer Features/perks: needed for Feature interrupts or special resolution;
- AI legal-action infrastructure: needed for legal tactical candidate generation;
- AI tactical policy: needed for autonomous tactical choice;
- Minecraft/Cobblemon/Craftics adapter/playback support: needed for authoritative visible execution.

## Reduced encounter version

Keep the same relay, suspects, evidence and consequences.

Represent the ridge as stable route nodes with explicit blocked/open state. Weather remains visible and narratively relevant but does not push combatants. Debris becomes an access gate rather than a dynamic hazard zone. Rescue occurs through deterministic travel and ordinary interaction checks outside tactical combat. No delayed collapse, persistent status, reaction rescue or environmental damage is required.

This version preserves the investigation premise while depending primarily on world simulation and verified base movement rather than incomplete tactical families.

## Environmental storytelling

Evidence should appear through the site itself rather than only through dialogue:
- old repair marks beside newer interference;
- weathering on one component and a clean recent break on another;
- archived service intervals that conflict with physical condition;
- Pokémon activity that may have altered or exposed part of the scene only if species behavior is later validated against project authority;
- replacement parts that reveal what maintainers previously expected to fail.

Environmental clues are evidence candidates, not automatic truth. Their mechanical or species-specific interpretation requires separate authority checks before canonization.

## Canon questions

Unresolved before adoption:
- which Ouros region, if any, has infrastructure suitable for this loop;
- whether a relay network of this kind exists in approved canon;
- which institution owns maintenance and security duties;
- which PTU/Caelo Skills or Features can legitimately support inspection or reconstruction;
- whether any Pokémon species can provide mechanically meaningful clues at the site;
- whether the rich tactical ridge can be admitted under current engine capabilities.
