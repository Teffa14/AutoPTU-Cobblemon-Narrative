# Resource Status, Accountability and Expedition Scan — Pass 392

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-09

## Repository audit before research

The recursive repository tree at narrative head `35a7a81e23a2ffd4c006c62827ca9d6434da3725` was inspected before selecting this slice. Current focus, canon/governance boundaries, the resource request/reservation/handoff chain, portable-find work in Passes 388–390, persistent-world recovery in Pass 391 and recent research filenames were checked before writing.

The selected implementation gap is the absence of a dedicated recovery owner for the complete mutable `WorldResource` catalog. Existing ledgers describe reasons and histories around resources, but no existing owner was found that can restore the whole current catalog without reconstructing it from those histories.

Previously processed anchors were not deliberately reused. Repository search also showed that Pokémon Rejuvenation had already been processed in multiple earlier research passes, so it was excluded despite current search results surfacing it again.

## Source 1 — FEMA / NIMS resource management

Sources:
- https://www.usfa.fema.gov/a-z/nims/managing-resources.html
- https://training.fema.gov/emiweb/is/icsresource/assets/ics_training_reference_guide.pdf
- https://preptoolkit.fema.gov/web/national-resource-hub/resourceinventorying

Reusable structure:

Incident logistics benefits from a maintained inventory plus a current status picture. Resource records carry capabilities, availability/state and location, while status changes must be reported so the operational picture does not remain stale.

Transformation for Ouros:

A resource can be a stable world object while its current operational state changes repeatedly. A record saying that equipment was available earlier and another saying it is assigned or unavailable later can both be correct. Recovery therefore needs one explicit snapshot generation rather than guessing current state from an old request or transfer record.

This source informs system structure only. Ouros does not import FEMA organizations, terminology as canon, forms, jurisdiction or emergency doctrine.

## Source 2 — public PTU campaign premise: Raist expedition teams

Source:
- https://www.reddit.com/r/PokemonTabletop/comments/16tt7ux/

This publicly posted Pokémon Tabletop United campaign pitch describes a region isolated after severe environmental disasters where communities eventually send expedition teams out because stored supplies are running low.

Reusable structure:

A settlement-level scarcity problem can create expeditions whose success depends on obtaining and returning useful supplies rather than defeating one antagonist. Resource availability becomes a driver for exploration, route choice and social pressure.

Transformation for Ouros:

Use shortages or temporarily unavailable infrastructure as a reason for independent actors and factions to seek the same capability. Keep the specific disaster, region, vault premise, time span and plot out of Ouros.

## Source 3 — Pokémon Tabula Rasa

Source:
- https://www.rebornevo.com/forums/topic/53355-pok%C3%A9mon-tabula-rasa/

The public project description presents a sparsely settled tundra region with extensive routes and forests, limited civilization and encounters with people during travel.

Reusable structure:

Low-density geography increases the narrative value of depots, field equipment, transport links and local supply decisions. A single operational resource can matter across multiple locations because replacement capacity is distant.

Transformation for Ouros:

Use geographic remoteness to make resource state consequential without copying the fan game's regions, creatures, characters, maps or story.

## Source 4 — PTU supplies boundary

Sources:
- https://pturpg.wikidot.com/character-creation
- https://pturpg.wikidot.com/consumables

PTU explicitly treats supplies and specialized equipment as part of preparation for travel, while consumables and other Items have their own mechanical effects.

Boundary for Ouros:

The world-agent `WorldResource` abstraction must not silently turn arbitrary logistical equipment into a mechanically implemented PTU Item. If a resource later gains a tactical Item effect, that exact Item behavior remains individually gated against AutoPTU evidence.

## Design lessons extracted

Stable identity and mutable status should be separate concerns.

Current status requires an authoritative operational image; historical request or custody records cannot safely substitute for it.

Remote geography makes capability scarcity narratively useful without requiring permanent scarcity everywhere in the region.

Two actors can possess conflicting but historically accurate resource information when they learned it at different semantic times.

Expedition objectives can revolve around locating, requesting, transporting or restoring a capability while combat stays optional or subordinate.

## Candidate consequence patterns

A field repeater is listed as available in an early dispatch record, but by the time a second team arrives it has been assigned elsewhere.

A pump remains physically present at a depot while being out of service, so location knowledge alone is insufficient to plan around it.

A resource is reserved for one mission while another actor has a more urgent need, creating an institutional conflict that can be resolved through communication, reprioritization or alternate sourcing rather than theft.

A returned resource changes from `IN_USE` to `AVAILABLE` after one expedition, reopening options for actors whose earlier plans were blocked.

## Canon boundary

No Ouros institution, settlement, disaster, resource type, faction, route, species or historical event is established here.

All examples are design candidates until promoted through the repository's normal research → proposal → design → canon authority chain.
