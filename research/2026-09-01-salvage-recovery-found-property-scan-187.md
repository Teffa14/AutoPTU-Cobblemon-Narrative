# Salvage, Recovery, Found Property and Displaced Material Research Scan — Pass 187

Status: RESEARCH / PROVENANCE ONLY. NOT CANON.
Date: 2026-09-01

## Purpose

This pass examines objects, cargo, equipment and debris that are found after displacement, weather, accident, abandonment, loss or infrastructure failure. The design problem is not merely how the player picks an item up. It is how Ouros records discovery, hazard assessment, physical recovery, provenance, custody, condition, claim uncertainty, repairability and eventual disposition without silently deciding property law.

The scan deliberately avoids importing protected dialogue, distinctive external plots, exact rewards, maritime-law rules, insurance doctrine or unverified Caelo property regimes.

## Repository overlap check

The current Narrative repository already contains mature adjacent systems for:

- item demand, consumption and resolution;
- courier chains and custody handoffs;
- field provisioning, stock, reserves, substitution and replenishment;
- after-sale returns, warranty, repair and replacement;
- material-culture and workshop audits;
- portable evidence and information provenance;
- emergency preparation and field response;
- shared-resource permits and stewardship;
- search/recovery of people;
- restoration and public works;
- Ferry Landing, Tideglass Archive, Loma Clara storehouse and Marea Field Office continuity.

The missing seam begins before commercial repair or ordinary inventory management. A displaced object may be physically present yet unsafe to touch, may still belong to somebody, may be evidence of an earlier event, may contain multiple identifiers, may require inspection before reuse, and may move through custody before any claim is resolved.

This layer should therefore feed existing custody, repair, archive, provisioning and restoration systems rather than replace them.

## Public sources reviewed

### Sea Mauville: failed infrastructure becoming a different place

Source: Bulbapedia, Sea Mauville.
https://bulbapedia.bulbagarden.net/wiki/Sea_Mauville

Reusable structure:

- a former industrial facility survives after its original operation ends;
- closure does not erase physical traces of work, documents or equipment;
- environmental change gives the site a later function distinct from its original purpose;
- records found on site provide attributed historical evidence rather than a clean omniscient exposition dump.

Ouros lesson:

A damaged or disused site can accumulate several valid histories. Recovery content should preserve where an object was found, what layer it came from, who documented it and whether moving it destroys useful context.

### Abandoned Ship: access, keys and recovery with a destination

Source: Bulbapedia, Abandoned Ship.
https://bulbapedia.bulbagarden.net/wiki/Abandoned_Ship

Reusable structure:

- physical deterioration changes traversal;
- access to some spaces requires capability and sequential discovery;
- a valuable device is recovered from a wreck and then taken to a knowledgeable external recipient;
- the recovered object matters because of where it came from and who can interpret or use it, not merely because it entered player inventory.

Ouros lesson:

A recovery quest can have distinct phases: locate, document, make access safe, recover, transfer, inspect and decide what happens next. The item pickup itself need not be the climax.

### NOAA: abandoned, derelict and displaced material require hazard assessment

Sources:
https://marinedebris.noaa.gov/what-marine-debris/abandoned-and-derelict-vessels
https://marinedebris.noaa.gov/where-does-marine-debris-come/disaster-debris
https://marinedebris.noaa.gov/where-does-marine-debris-come/ocean-based-marine-debris

Reusable structure:

- storms, collisions and accidents can displace vessels, containers, equipment and other material;
- large or unfamiliar debris may pose navigation, environmental or human-safety hazards;
- an identifiable owner and physical neglect can coexist;
- physical presence on a shore does not by itself explain origin or status;
- hazardous material should be assessed before casual handling.

Ouros lesson:

Recovery should begin with observation and safety state. A Minecraft item entity appearing on the ground must not automatically mean the player is authorized to collect it or that it is safe to use.

Real-world legal definitions are not imported into Caelo. NOAA is used here only for operational separation of discovery, hazard, ownership uncertainty and removal.

### NOAA monitoring: classification before interpretation

Source: NOAA Marine Debris Monitoring and Assessment Project item categorization guide.
https://marinedebris.noaa.gov/protocol/mdmap-marine-debris-item-categorization-guide

Reusable structure:

- field observations become more comparable when material and item type are recorded consistently;
- classification can precede a confident explanation of source or event.

Ouros lesson:

A resident may correctly record material, dimensions, marks, damage and location while leaving origin unresolved. This supports Mirador and Tideglass provenance without forcing every recovered object into a mystery with one correct answer.

### Mystery Dungeon retrieval structure

Public community documentation and player discussion around Mystery Dungeon jobs repeatedly distinguishes finding a requested item, carrying it and delivering or using it for the intended recipient. One example is a rescue-mission discussion where the item must be found on the assigned dungeon floor and then given to a specified Pokémon.

Source:
https://www.reddit.com/r/MysteryDungeon/comments/y9zy2l/

This is community evidence, not rules authority for Ouros.

Reusable structure:

- discovery can happen away from the recipient;
- possession is an intermediate state;
- mission completion can depend on the correct handoff rather than collection alone.

Ouros lesson:

Found-object gameplay should expose custody and destination where relevant. Inventory possession alone cannot close an authored recovery case.

### PTU community campaign evidence

Searches across public PTU campaign material found many exploration-heavy and living-world campaigns, but no source strong enough to justify importing a specific salvage procedure. This absence is itself useful: this pass does not pretend community adjudication establishes a PTU property subsystem.

A public PTU campaign log does show a party taking possession of unusual objects and homebrew capture/property effects during exploration. Those rulings are campaign-specific and are not used as system authority here.

## PTU / AutoPTU mechanical boundary

The read-only AutoPTU source set contains canonical mechanical concepts including the Move Thief, the Ability Frisk, Pickup references and effects involving removal or retention of Held Items.

These mechanics can alter, reveal or interact with battle items under their actual PTU rules. They do not define civil ownership, institutional custody, abandoned-property law, evidence handling or salvage rights in Ouros.

A battle effect that removes an Item from a target cannot silently write a narrative claim such as `player_owns_item = true`.

Likewise, a Pokémon with Pickup producing or obtaining an item under a verified mechanic does not establish where that item came from in the narrative world unless an authoritative adapter event provides that provenance.

## Caelo boundary

Literal indexed searches for `Caelo` in the current Narrative, AutoPTU-Java and AutoPTU repositories returned no source file defining regional salvage, found-property, maritime, cargo-claim, abandonment, insurance or evidence law.

The canon README still names Caelo source material as authoritative when it becomes available to implementation review.

No Caelo rule is invented in this pass.

## Structural synthesis

A durable recovery case needs independent records for:

- discovery observation;
- exact or bounded find location;
- initial hazard status;
- physical object identity or provisional identity;
- marks, labels and damage observations;
- provenance claims and their sources;
- custody chain;
- condition assessment;
- whether the object is safe to move;
- whether it is safe to use;
- owner or claimant assertions when any exist;
- institutional hold or evidence relevance when any exists;
- transfer to repair, archive, storage or disposal;
- unresolved questions.

The system must support closure without forcing ownership certainty. A site can be cleaned while one object remains held for review. A recovered object can be returned without proving why it was displaced. A damaged tool can be repaired while the cause of damage remains unresolved.

## Important boundaries

- Finding an object does not by itself transfer title.
- Physical recovery does not settle a claim.
- Visible damage does not prove abandonment.
- A recognizable mark is evidence toward identity, not automatic proof of current ownership.
- A repairable object may still be unsafe or unsuitable for immediate use.
- A functioning scientific instrument may still require calibration or verification.
- A historical object can remain evidence even when it has low material value.
- A battle result cannot decide ownership, provenance, compensation or abandonment.
- Minecraft pickup cannot be the authority for legal or institutional transfer.
- Entity despawn cannot mean that a recorded object was destroyed.
- Item duplication bugs or adapter resync cannot create legitimate additional stock.

## Design lessons for Ouros

Recovery content becomes richer when the player must answer practical questions rather than a generic ownership prompt:

- Is the area safe enough to approach?
- What should be documented before moving anything?
- Which object can be removed immediately and which should stay in place?
- Who can inspect this type of equipment?
- Which mark identifies a lot, route, institution, maker or previous repair rather than an owner?
- Does the object need ordinary storage, evidence hold, specialist care or disposal?
- Can the current custodian transfer it without deciding the ultimate claim?
- What can be repaired now?
- What remains unresolved after the physical problem is solved?

## Candidate implementation direction

Marea already has strong anchors without new institutions:

- Ferry Landing can surface displaced freight, damaged loading equipment and tide-carried material;
- Lia Orren can contribute arrival/departure and freight-window records without becoming universal property authority;
- Mina Orren and Teo Marr can assess ordinary structural or equipment condition within their established work scopes;
- Brin Hale can identify storehouse containers, returnables or dispatch marks within his own records;
- Tideglass can preserve historical labels, manifests and contradictory records;
- Marea Field Office can coordinate practical safety and field response without becoming police;
- Mirador can document environmental location and condition without deciding ownership.

The first implementation should use an ordinary displaced container or piece of equipment whose custody can be resolved while its deeper provenance remains optional.

## Provenance status

All public sources in this file are research input only.

No external named character, external plot, exact item reward, legal doctrine, property right, maritime rule, insurance mechanic or Pokémon-specific battle rule is promoted into Ouros canon by this scan.