# Three Jobs on the Same Road — Pass 394

Status: PROPOSED / NON-CANON
Date: 2026-09-09

## Premise

A travelling field team starts with one ordinary assignment whose route is already scheduled.

Before departure, a local institution asks whether the team can carry a sealed package to a stop already on the route. The request is useful but optional.

After the team is underway, a credible message reports that a surveyor failed to return from a side path near the destination. The report does not prove injury, attack or foul play. It creates a third possible objective with a different urgency profile.

The road now supports three jobs at once without becoming three separate worlds:

- complete the original field assignment;
- deliver the package if it was accepted;
- locate or establish the status of the missing surveyor.

The player may prioritize, combine, defer or refuse objectives. Persistent NPC teams may also act on tasks they actually know about and are equipped to pursue.

## Why this belongs in Ouros

The concept tests persistent world-agent behavior rather than a scripted quest chain. Schedules, knowledge, resource access and later information can change which action is reasonable without rewriting why an actor left home in the first place.

It also makes a mundane route reusable. The road can hold social, logistical, investigative and ecological meaning at the same time.

## Resource-recovery complication

A specialized field kit is relevant to the search branch.

The reservation ledger may contain an active reservation for one actor while the current catalog has not projected that reservation yet. That state is not automatically corruption.

Alternatively, the latest formal handoff may identify an earlier holder while the current catalog shows the kit back at a depot after a legal return. The handoff ledger alone is not sufficient to derive the current holder.

`tools/world_resource_history_reconciliation.py` can surface the distinction as confirmed, conflict or indeterminate without mutating either owner.

No mismatch automatically means theft, negligence or deception.

## Reduced playable version

The reduced version requires no AutoPTU battle.

The original assignment uses ordinary world travel and schedule state.

The delivery uses explicit acceptance, custody/location state and arrival acknowledgement.

The surveyor branch uses explicit information receipt, a side-route decision and a world-state contact result. If the surveyor already moved, the search can become an information problem rather than a combat encounter.

Resource reconciliation remains diagnostic and narrative evidence. It does not decide guilt or quest success.

## Rich version

A rich version may place the surveyor in a location where wild Pokémon, difficult visibility or unstable terrain complicate contact and withdrawal. The objective is still to establish safety/status and leave with the relevant people or evidence. Defeating every opponent is not the narrative success condition.

### Required capability families

Targeting/footprints/range/LoS: VERIFIED within audited scopes only for ordinary tactical geometry.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required if the encounter uses escort body-blocking, forced reposition, rescue dragging or interception.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only. New rescue/delivery actions are not implied.

Full turn/round lifecycle: PARTIAL. Required for timed rescue windows, delayed environmental changes or phase-based objectives.

Full stateful damage pipeline: PARTIAL. Required if damage has persistent consequences for the rescue/objective state.

Status lifecycle: PARTIAL. Required for complex persistent conditions.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Required for weather shifts, reduced-visibility zones, unstable terrain, delayed hazards or reaction hazards.

Move-specific behavior: individually gated.

Abilities: individually gated. AutoPTU-Java #421 provides additional Impostor negative-guard evidence only for that tested seam.

Items: individually gated. A `WorldResource` field kit is not automatically a PTU Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for rescue-first, escort-first, protect-package, objective-aware withdrawal, split-task coordination and disengage-after-objective until exact policies are verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for authoritative objective acknowledgement, persistent package/resource state, rescue state and non-KO completion playback.

## Originality boundary

Public inspiration is limited to high-level structures: overlapping job obligations in a current PTU actual play, varied mission categories sharing exploration spaces in Pokémon Mystery Dungeon, optional-area/event density in Pokémon Coral, and the warning from Pokémon Reborn that environment-changing battle premises carry substantial mechanical dependencies.

No protected characters, dialogue, maps, episode events, dungeon layouts, faction names, species variants or bespoke battle systems are copied.

## Canon decisions still required

A later canon pass must choose whether this event exists at all, and if so its region, road, institution, package, surveyor, route topology, species, cause of delay, resource authority and any PTU/Caelo mechanics.

Until that promotion, every proper detail in this file is a placeholder candidate rather than established Ouros history.
