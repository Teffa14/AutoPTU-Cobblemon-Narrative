# The Orchard That Bloomed Out of Sequence — Pass 322

Status: PROPOSED / NON-CANON
Date: 2026-09-06

## Premise

A managed orchard district expects a normal flowering window, but one block reports poor pollinator visitation and a weakening harvest forecast while a nearby wild margin still shows activity. Old survey notes, grower observations, maintenance records, and current field evidence do not line up cleanly.

The mystery is not “where did all the pollinators go?” The player must establish whether the relevant plants and pollinators were actually available to one another at the same places and times.

## Spatial structure

The reduced authored version uses four persistent features:

- Upper orchard block: warmer exposure; bloom may open and pass earlier.
- Low pocket: cooler or wetter microclimate; bloom may lag.
- Wild margin / hedgerow: alternate forage, shelter, or monitoring reference.
- Service strip: irrigation, pruning, mowing, access, transport, or maintenance history can be inspected without assuming it caused the problem.

Each feature keeps identity across revisits. Reports and observations always attach to a feature and a time window.

## Investigation loop

The player receives conflicting reports, then inspects at least two orchard patches and one independent reference area. Useful evidence can include flower stage, fallen petals, unopened buds, nectar-foraging observations, old calendars, field logs, weather notes, irrigation or mowing records, market forecasts, and later fruit-set observations.

The player then revisits after a meaningful interval. The second visit can confirm that a patch entered or left bloom, show pollinator activity at another hour, reveal a changed management schedule, or demonstrate that an early interpretation was too broad.

## Valid resolution families

The authored truth can be selected later without changing the premise:

- microclimate shifted flowering between blocks;
- observers sampled the wrong hours or dates;
- an alternative forage patch temporarily drew activity elsewhere;
- pruning, irrigation, mowing, or access timing changed overlap indirectly;
- weather compressed one useful visitation window;
- the historical calendar was generalized from another block;
- the initial harvest forecast was based on incomplete evidence;
- multiple small causes overlapped.

Sabotage and a singular villain are unnecessary.

## NPC / faction dynamics

A grower cooperative wants predictable yield and may be under contract pressure. A habitat steward wants the wild margin protected. A pollinator monitor wants repeatable evidence before causal claims. Grounds or water staff can defend legitimate operational decisions. A buyer or local market organizer reacts to expected supply rather than hidden ecological truth. Residents or older workers may remember earlier bloom timing but still possess incomplete local knowledge.

Each actor can be correct about the evidence they actually received while disagreeing about what it means.

## Consequence model

Resolution is feature-scoped. Possible consequences include changing a monitoring window, delaying or relocating mowing, protecting one refuge strip, adjusting irrigation review, keeping one orchard block under observation, revising a harvest forecast, changing a buyer commitment, or publishing a corrected notice.

These consequences should use the existing decision, review, and selective-consequence-repair systems. A later correction must not erase the historical decision or unrelated economic/social effects.

## Reduced implementation

This version preserves the full narrative premise without tactical pollination simulation.

Authored world descriptors may include `BLOOM_NOT_YET`, `BLOOM_OPEN`, `BLOOM_PAST`, `VISITATION_OBSERVED`, `VISITATION_NOT_OBSERVED`, `ALTERNATIVE_FORAGE_OBSERVED`, `MONITORING_REQUIRED`, and ordinary route/access states. These are evidence or world descriptors, not PTU statuses.

Changes happen between scenes or through explicit world events. There are no pollen radii, pollination percentages, wind vectors, automatic species behavior, custom statuses, environmental damage, or fabricated PTU bonuses.

## Full mechanically rich version

A later verified version could make changing weather, vegetation zones, pollen-producing actions, tactical visibility, timed environmental changes, or Pokémon-assisted pollination relevant during an encounter. Every such behavior must be backed by the exact PTU/Caelo contract and engine capability that implements it.

Potential battle-facing dependencies:

- targeting/footprints/range/LoS for ordinary targeting only; vegetation or pollen obscurement needs separate verification;
- base movement legality for standard traversal;
- complete movement for any wind-driven displacement, push/pull, interception, or rescue;
- core calculations for verified deterministic arithmetic;
- action economy/initiative for verified action ordering;
- full turn/round lifecycle for timed bloom/weather/environment transitions during battle;
- full stateful damage pipeline only if an authored hazard can deal damage;
- status lifecycle only for an actual verified persistent condition;
- terrain/weather/hazards/zones/reactions for dynamic vegetation, wind/rain, pollen fields, or environmental reactions;
- move-specific behavior for each Move used as an ecological or tactical mechanism;
- abilities for Honey Gather or any other Ability only after its actual contract is verified;
- items and Trainer Features/perks only when individually verified;
- AI legal-action infrastructure for candidate legal actions;
- AI tactical policy for autonomous reasoning about changing environmental opportunities;
- Minecraft/Cobblemon/Craftics adapter/playback for presenting authoritative state without deciding it.

## Canon questions

Region, crop, ownership, pollinator species, resident Pokémon, wild margin composition, local climate, historical bloom baseline, commercial stakes, responsible institutions, and final cause all remain open.

No franchise species is canonically assigned by this proposal.