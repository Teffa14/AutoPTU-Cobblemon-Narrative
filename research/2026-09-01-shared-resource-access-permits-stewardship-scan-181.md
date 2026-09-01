# Research scan 181 — shared-resource access, permits and stewardship

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-01
Destination: Teffa14/AutoPTU-Cobblemon-Narrative
Canon impact: NONE. This file establishes no Ouros ownership law, capture quota, protected species, reserve, permit office, fishing right, gathering right or enforcement power.

## Research question

How can Ouros make access to wildlife areas, field sites and shared resources feel governed and persistent without treating every open space as unrestricted loot, every restriction as a combat barrier, or every ecological observation as proof that a quota is justified?

Repository inspection found existing layers for civic governance, ecology/phenology, wild collectives, dispatch, archives/custody, site aftermath, public memory and institutional delegation. The missing seam is narrower: a durable record that says who may enter a place or perform a resource-affecting action, during which window, for what purpose, under what conditions, and who can amend or suspend that authorization.

## Public source scan

### Nature Preserve — access earned through documented observation

Sources:
https://bulbapedia.bulbagarden.net/wiki/Nature_Preserve
https://pokemon.fandom.com/wiki/Nature_Preserve

High-level structures extracted:

- A wildlife-rich place can require explicit permission rather than being ordinary route space.
- Access can depend on demonstrated observational work rather than combat strength.
- A permit can control transport to a site without making the permit itself proof of ecological expertise.
- Remote access creates operational dependencies: transport, entry validation and return travel are separate from the ecology itself.

Ouros transformation:

Future restricted field sites may require an authored access credential or institutional invitation. The credential records permission scope; it does not prove that the holder understands every species, can capture freely, or owns what they observe.

Do not copy the Unova Pokédex completion requirement, Professor Juniper, Skyla, the remote preserve geography or its featured Pokémon.

### Great Marsh — observation before entry and changing presence

Sources:
https://bulbapedia.bulbagarden.net/wiki/Great_Marsh
https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Brilliant_Diamond_and_Shining_Pearl/Part_12

High-level structures extracted:

- The preserve exposes observation information before the player enters.
- Which Pokémon are visible changes over time.
- Entry is bounded by a defined session and a constrained capture method.
- A visitor can know that a species was reported in an area that day without that report being a guarantee of encounter.

Ouros transformation:

Observation boards, access notices and field windows can publish current evidence separately from authorization. `REPORTED_PRESENT != GUARANTEED_PRESENT`, and an access window should never overwrite the phenology/evidence system.

### Kanto/Hoenn/Johto Safari Zones — activity-specific restrictions

Sources:
https://bulbapedia.bulbagarden.net/wiki/Kant%C5%8D_Safari_Zone
https://bulbapedia.bulbagarden.net/wiki/Safari_Zone_%28Hoenn%29
https://bulbapedia.bulbagarden.net/wiki/Johto_Safari_Zone

High-level structures extracted:

- Entry permission can constrain what tools and actions are allowed inside a space.
- A protected or managed area can permit capture while prohibiting ordinary battle methods.
- Different regions can implement materially different access regimes for superficially similar facilities.
- Session boundaries can be defined by time, movement budget, supplied equipment or voluntary exit.

Ouros transformation:

Do not create one universal Ouros preserve rule. Any managed site needs its own authority, purpose, allowed verbs and termination conditions. `ACCESS_GRANTED != ALL_ACTIONS_GRANTED`.

Do not import Safari Ball mechanics, fees, step counters, bait/mud rules or franchise preserve ownership as Ouros mechanics.

### National Park Bug-Catching Contest — scheduled access and bounded take

Source:
https://bulbapedia.bulbagarden.net/wiki/Bug-Catching_Contest

High-level structures extracted:

- A recurring public event can temporarily alter normal access and allowed activity.
- Participants receive limited equipment and operate under a clear time window.
- Keeping one specimen can be distinct from observing or temporarily handling others.
- Officials retain custody over some participant resources during the event.

Ouros transformation:

A future research day, survey window or managed harvest can be calendar-driven and purpose-limited. The reusable lesson is bounded participation, not competitive capture itself.

### Pokémon Ranger — role authority and mission scope

Sources:
https://pokemonexperte.de/ranger/fiore
https://bulbapedia.bulbagarden.net/wiki/Lyra_Forest

High-level structures extracted:

- Field personnel receive tasks connected to ordinary locations and local problems.
- The same forest can support routine travel, rescue, research and later incidents without becoming a single-use dungeon.
- Operational authority can be mission-specific and temporary.

Ouros transformation:

Marea Field Office assignments can authorize a route check or observation visit without conferring permanent control of the site. A work order and a public-access permit should remain different records.

### PTU community evidence — Safari Zone authority as world rule, not class feature

Sources:
https://www.reddit.com/r/PokemonTabletop/comments/1kog0xd/
https://www.reddit.com/r/PokemonTabletop/comments/izr3b3/

High-level structures extracted:

- A public PTU campaign report treats Safari Zone rules as enforceable world constraints; one character breaking the no-Pokémon rule is framed as an in-world violation rather than a generic combat option.
- PTU community discussion explicitly distinguishes being a Ranger as a job/role from having a special PTU class. This is useful because institutional permission should not be inferred from a Trainer class label.

Ouros transformation:

`JOB_ROLE != TRAINER_CLASS` and `CLASS_FEATURE != CIVIC_AUTHORITY`. A Survivalist, Hunter or Capture Specialist build does not automatically grant access to a closed site or permission to remove wildlife/resources.

These Reddit sources are community practice, not PTU rules authority.

## PTU project cross-check

Read-only AutoPTU contains authoritative project catalogues for Capture Specialist and Hunter-related content, including capture techniques and prerequisites. This confirms that capture-relevant mechanical capabilities exist as PTU build content and must be validated separately from world permission.

Narrative boundaries:

`CAN_MECHANICALLY_ATTEMPT_CAPTURE != AUTHORIZED_TO_CAPTURE_HERE`

`SURVIVAL_SKILL != ACCESS_PERMIT`

`CAPTURE_SPECIALIST_CLASS != RESOURCE_STEWARD`

A world rule may forbid or limit an action that the character is mechanically capable of attempting. Conversely, a permit never invents mechanical competence or bypasses PTU capture legality.

No indexed Caelo source was found in the inspected repositories that defines preserve law, common-resource rights, permits, quotas, protected-species status or harvesting authority. This remains an evidence gap.

## Reusable structures for Ouros

### Access grants must have scope

Useful fields include site, holder, issuer, allowed purpose, allowed verbs, start/end window, prerequisites, reporting duty, transferability and revocation state.

### Observation and extraction are different permissions

A person may be allowed to enter and observe while being forbidden to collect specimens, remove plants, capture Pokémon, alter markers or move equipment.

### Temporary closure is world state

A route or site can become observation-only, staff-only, closed, escorted-access or open-with-conditions. Closure changes must identify the issuing authority and reason provenance.

### Quotas require evidence provenance

A quota can exist as policy, but the narrative layer must preserve what evidence supported it and when it was reviewed. `QUOTA_SET != TRUE_POPULATION_KNOWN`.

### Shared-resource disputes need multiple legitimate interests

A useful conflict can involve producers, researchers, transport workers, residents and wildlife needs without requiring a villain. Different actors may disagree about timing, evidence quality, access burden or who bears the cost of restraint.

### Removal creates custody

Anything collected for research, repair or public work should enter an existing custody/provenance system. A specimen removed under permit does not become ordinary player inventory by default.

## Anti-patterns rejected

- Treating every wilderness tile as freely harvestable.
- Giving a Trainer class automatic legal or institutional authority.
- Treating a permit as mechanical competence.
- Treating a population estimate as exact truth.
- Letting Minecraft block placement silently establish property boundaries.
- Turning every access dispute into combat.
- Creating universal Ouros capture law from Safari Zone mechanics.
- Using an expired authorization indefinitely because the item remains in inventory.
- Making a closure permanent simply because an NPC presentation actor is absent.

## Proposed vocabulary only

access_authorization_id
site_scope
holder_ref
issuer_role_ref
purpose_code
allowed_verbs
prohibited_verbs
valid_from
valid_until
condition_refs
reporting_obligation
transferability
revocation_state
closure_order_ref
resource_take_record
quota_policy_ref
evidence_review_ref

## Capability implications

Most permit, observation, custody and closure gameplay is non-tactical. A mechanically rich breach or wildlife-protection incident can require targeting/footprints/range/LoS, base movement legality, complete movement, core calculations, initiative, lifecycle, damage, statuses, terrain/weather/hazards/zones/reactions, exact Moves/Abilities/Items/Trainer Features, legal-action AI, tactical AI and Minecraft/Cobblemon/Craftics playback. Exact concepts must list only the families they actually use.

## Unresolved canon questions

Who owns or stewards land/water access in Marea, if anyone?
Which current institutions can issue temporary closures or research access?
Does Caelo define capture restrictions, protected species or conservation offices?
Can a public route contain time-limited observation-only segments?
What counts as specimen collection versus ordinary found property?
Who reviews an ecological quota or reopens a closed route?
Can residents hold customary use rights distinct from formal permits?
What records must follow a collected biological sample?

Until sourced and approved, all Marea-specific access law and resource policy remain proposed.