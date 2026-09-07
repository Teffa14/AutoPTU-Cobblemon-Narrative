# Resource inventory, allocation and field-readiness scan — Pass 338

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-09-07

## Why this pass

The current global NPC planner can gate intents by knowledge, permission, locality and AutoPTU ownership, but its core intent schema does not yet express ordinary world-resource prerequisites. `CURRENT_FOCUS.md` explicitly names resource/inventory-aware intents as an immediate next slice.

Repository-wide filename/search inspection found mature custody, evidence, cold-chain, found-property and logistics work, but no global resource-availability owner for ordinary NPC agenda selection. The new work therefore targets task readiness rather than ownership law, evidence custody or PTU Item effects.

## Public-source scan

### FEMA National Resource Hub / NIMS resource management

Sources:
- FEMA, Resource Inventorying: https://preptoolkit.fema.gov/web/national-resource-hub/resourceinventorying
- FEMA, Resource Management: https://preptoolkit.fema.gov/web/nims-toolkit/resource-management
- FEMA, Resource Typing: https://preptoolkit.fema.gov/web/national-resource-hub/resource-typing
- FEMA EMI IS-700.b accountability material: https://emilms.fema.gov/_is0700b/groups/203.html

Reusable structure:

Organizations distinguish inventory from deployment. Equipment, supplies, facilities, teams and personnel are tracked resources; resource typing defines capability; accountability includes resource tracking; and deployment follows explicit request/dispatch rather than mere existence.

Ouros abstraction:

`RESOURCE_EXISTS != RESOURCE_AVAILABLE_FOR_THIS_INTENT`

`RESOURCE_CAPABILITY != RESOURCE_IDENTITY`

`RESOURCE_KNOWN != RESOURCE_POSSESSED`

`RESOURCE_POSSESSED != RESOURCE_AUTHORIZED_FOR_USE`

`RESOURCE_AVAILABLE != RESOURCE_RESERVED_FOR_THIS_ACTOR`

A planner should be able to ask for a capability such as `FIELD_SAMPLE_KIT` without hard-coding one unique object. The selected concrete resource remains persistent world state.

### Great Basin Cache accountability

Source:
- National Interagency Fire Center, Great Basin Cache accountability: https://www.nifc.gov/resources/supplies/great-basin-cache/accountability

Reusable structure:

Consumable and durable resources have different aftermath. Returned durable equipment can be refurbished and re-enter inventory; unreturned trackable equipment remains an accountable loss. This supports a world distinction between availability, consumption, return, repair and retirement.

Ouros abstraction:

`TASK_COMPLETED != RESOURCE_CONSUMED`

`RESOURCE_USED != RESOURCE_DESTROYED`

`RESOURCE_RETURN_DUE != RESOURCE_AVAILABLE_NOW`

### Pokémon Mystery Dungeon inventory/storage

Sources:
- Pokémon Mystery Dungeon: Rescue Team DX official world page: https://mysterydungeon.pokemon.com/de-de/world/
- Bulbapedia, Toolbox: https://bulbapedia.bulbagarden.net/wiki/Toolbox
- Bulbapedia, Kangaskhan Storage: https://bulbapedia.bulbagarden.net/wiki/Kangaskhan_Storage

Reusable structure only:

Field-carried inventory and storage are operationally distinct. A team can own an item while it is not in the carried field kit. Capacity and preparation therefore affect what is usable during an expedition.

Ouros adaptation:

A named NPC may know an institution owns a tool and still need to travel, reserve, collect or receive it before an intent is ready. This is a world-planning issue, separate from any PTU combat Item rule.

No Mystery Dungeon item counts, dungeon-loss rules, characters, locations or exact mechanics are adopted.

### Pokémon Tabletop United crafting kits

Source:
- PTU community reference, Crafting Kits: https://pturpg.wikidot.com/crafting-kits

The page documents PTU equipment whose presence can be required for specific crafting functions. This confirms that some PTU-adjacent actions legitimately depend on equipment, but this pass does not import costs, checks, frequencies or crafting effects into Ouros.

Mechanical use remains subject to the project PTU/Caelo source set and AutoPTU verification. The world-agent layer may track that a kit is required or available; it may not resolve the kit's PTU mechanical effect.

## Design lessons extracted

The global planner needs two separate questions:

1. Is the NPC otherwise eligible to pursue this intent?
2. Are the required world resources currently available to that NPC for this intent?

Resource readiness should consider at least capability, quantity, operational state, current holder/location and reservation. A resource mismatch blocks or defers the world task; it does not invent the missing object, teleport it, or silently borrow it from another actor.

Shared institutional ownership must not create hive-mind inventory. Two NPCs can both know that one field kit exists and still contend for the same physical resource.

Reservations are temporal claims, not permanent ownership. A deterministic tie-break is required so replay does not change which resource is selected.

The resource layer should create no PTU battle arithmetic. If an intent becomes structured mechanics after its world prerequisites are met, AutoPTU still owns tactical legality and resolution.

## New narrative pattern

A useful recurring conflict is ordinary scarcity rather than villainy: two valid obligations need one shared resource during overlapping windows. The story can branch through negotiation, delay, substitution, borrowing, rescheduling or escalation to a resource-owning institution.

This supports mundane continuity in settlements and factions. NPCs can miss work because a tool is unavailable without becoming incompetent or omniscient.

## Copyright boundary

Only high-level structures are retained. No protected prose, dialogue, distinctive characters, plots, maps or exact game sequences are copied.

## Mechanical boundary

This research does not create PTU Item effects, inventory limits, carrying capacity, crafting checks, action costs, item-use legality or battle consumable behavior.

Any later tactical use of a resource remains gated by the permanent capability audit and exact content verification.
