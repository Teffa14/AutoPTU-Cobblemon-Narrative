# The Team That Arrived After the Window Closed — Pass 379

Status: PROPOSED / NON-CANON
Canon effect: NONE

## Premise

A field crew receives a legitimate assignment to reach a remote observation site during a narrow research window. The planner selects the trip. The crew actually leaves. The semantic travel runtime later proves that the crew reaches the destination.

The objective is still not complete.

At the site, the team discovers that the condition they were sent to observe has already ended. The cause may be ordinary timing error, an earlier-than-expected environmental change, stale information, another team's intervention, equipment delay, Pokémon activity or deliberate interference. None of those explanations is true until supported by evidence.

The important historical distinction is simple: arriving successfully does not prove that the mission succeeded.

## Player-facing investigation

The player can encounter consequences before receiving the explanation. The team is physically at the destination. Their equipment may be unpacked. Their departure and arrival can both be corroborated. Yet the expected sample, observation, handoff or rendezvous did not happen.

Useful questions include:

- Was the window already closed when the order was issued?
- Did conditions change during travel?
- Did another actor know about the change and fail to communicate it?
- Was the destination correct but the timing wrong?
- Did the team arrive and then choose another legitimate priority?
- Is there evidence worth preserving even though the original objective failed?

No answer requires an NPC to lie.

## Reduced implementation

The reduced version uses only world-agent systems:

- semantic time;
- communications when the assignment is transmitted;
- private evidence/knowledge;
- plan selection;
- action-start provenance;
- semantic travel;
- `OUROS_NPC_ACTION_TERMINAL_PROVENANCE_V1` proving destination arrival;
- later investigation and replanning.

No AutoPTU battle is required.

## Mechanically rich version

After arrival, the site can still contain a playable problem: recover abandoned instruments, find a missing observer, preserve damaged samples, escort a late courier, identify why wildlife behavior changed, or leave safely before conditions worsen.

The narrative objective remains independent from defeating every Pokémon present.

Potential full-version dependencies:

- targeting/footprints/range/LoS: needed if the site becomes spatially tactical;
- base movement legality: needed for ordinary tactical traversal;
- complete movement: needed only if the design uses interception, pushes, pulls, knockback or forced movement;
- core calculations: needed for ordinary deterministic battle arithmetic;
- action economy/initiative: needed for tactical turns;
- full turn/round lifecycle: required if timed phases or round hooks matter;
- full stateful damage pipeline: required for persistent battle-authored damage consequences;
- status lifecycle: required for persistent/complex statuses;
- terrain/weather/hazards/zones/reactions: required if closing conditions become tactical hazards, weather phases or reactive zones;
- move-specific behavior: gated per exact Move;
- abilities: gated per exact Ability;
- items: gated per exact Item;
- Trainer Features/perks: gated per exact Feature;
- AI legal-action infrastructure: needed for legal tactical choices and currently verified only in ordinary audited scope;
- AI tactical policy: BLOCKING for rescue-first, escort, protect-equipment, search, objective-aware withdrawal and disengage-after-objective unless exact policies gain evidence;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for persistent objective/equipment identity, non-KO objective acknowledgement and authoritative result playback.

## Canon questions

Before promotion, resolve against approved Ouros/Caelo material:

- which existing geography can plausibly host a time-sensitive observation site;
- which established institution or NPC group can issue the assignment;
- what communication technology and travel times are valid there;
- what environmental phenomenon is setting-consistent;
- which species, if any, belong at the site;
- whether the observation concerns ecology, weather, migration, geology or another already-approved domain.

No new location, institution, species distribution or regional fact is established by this proposal.
