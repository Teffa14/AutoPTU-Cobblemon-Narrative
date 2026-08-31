# Private Estate, Inheritance and Legacy Stewardship Continuity Extension

Status: PROPOSED ARCHITECTURE — NON-CANON UNTIL APPROVED
Pass: 167

## Purpose

This extension gives Ouros a provenance-aware way to preserve private legacy handling after an authored death: instructions, inventories, claims, custody, review, distribution and later stewardship.

It remains dormant unless canon supplies an applicable succession rule, institution, custom or authored decision. It does not create inheritance law by default.

## Authority boundary

Death/Bereavement establishes mortality state. Family/Kinship establishes relationships. Property/Ownership owns title and ownership transitions. Material Culture owns physical-object history. Finance owns balances, debts and payment events. Agreements owns commitments. Archives owns document provenance and preservation. Residential/Household owns residence and occupancy. Civic Office owns institutional succession.

This extension links those facts into a private-estate process and records unresolved states. It does not supersede adjacent authorities.

AutoPTU remains authoritative for verified tactical outcomes. Minecraft, Cobblemon and Craftics present authored estate objects and locations but cannot infer estate state from blocks, containers, despawns or dropped items.

## Activation rule

An `estate_case` may be opened only after an authored event or canon-approved process establishes that estate handling is required. A confirmed death alone does not invent an estate system.

Every case must point to a `succession_rule_ref` or remain explicitly `RULE_UNKNOWN`. The generator may preserve uncertainty but may not synthesize a legal rule to close the case.

## Core records

### estate_case

Fields: `estate_case_ref`, `subject_ref`, `opened_at`, `opening_basis_ref`, `succession_rule_ref`, `administrator_role_ref`, `current_status`, `privacy_scope`, `source_refs`.

Suggested states: `NOT_OPENED`, `OPEN`, `INVENTORY_IN_PROGRESS`, `UNDER_REVIEW`, `DISTRIBUTION_AUTHORIZED`, `PARTIALLY_DISTRIBUTED`, `CLOSED`, `SUSPENDED`, `DISPUTED`, `RULE_UNKNOWN`.

### legacy_instruction_version

Preserves an authored instruction without deciding its controlling effect.

Fields: `instruction_ref`, `author_ref`, `created_at_or_range`, `document_or_oral_record_ref`, `witness_or_source_refs`, `stated_beneficiary_or_steward_refs`, `asset_or_duty_refs`, `status`, `supersedes_ref`, `authority_assessment_ref`.

### estate_inventory_snapshot

A dated evidence snapshot rather than omniscient truth.

Fields: `snapshot_ref`, `estate_case_ref`, `enumerated_at`, `enumerator_ref`, `location_scope`, `asset_refs`, `obligation_refs`, `missing_or_uncertain_refs`, `source_refs`, `method_notes`, `supersedes_ref`.

Two snapshots may both be correct for their dates.

### estate_asset_link

Links a candidate asset to existing Property/Ownership or Material Culture records.

Fields: `estate_case_ref`, `object_or_property_ref`, `inclusion_basis`, `inclusion_status`, `ownership_authority_ref`, `custody_ref`, `valuation_ref_if_any`, `notes`.

This link never creates ownership.

### estate_obligation_link

Links candidate debts, commitments or duties to Finance/Agreements records. Inclusion does not validate the obligation.

### succession_claim

Fields: `claim_ref`, `claimant_ref`, `claimed_asset_or_share_ref`, `claim_basis`, `submitted_at`, `evidence_refs`, `review_status`, `decision_ref`.

### estate_custody_episode

Records who physically safeguards an asset or record over a period. Custody remains separate from ownership and beneficial entitlement.

### estate_review_episode

Records authentication, rule interpretation, inventory reconciliation, claim review or dispute handling by an authored authority.

### distribution_plan

Records an authorized or proposed mapping from estate components to recipients, stewards, institutions, disposal or unresolved holding.

### distribution_episode

Records actual transfer activity. A plan can exist without execution, and execution can be partial.

### legacy_stewardship_episode

Preserves responsibilities that continue after distribution: maintaining a workshop, archive, collection, shrine object, research notebooks, family business artifact or other authored legacy.

Stewardship does not imply ownership unless Property/Ownership says so.

### estate_dispute

Stores competing claims, disputed documents, missing assets, authority questions or contested interpretations without assigning moral truth.

### estate_record_revision

Corrections supersede earlier records while retaining historical provenance.

## Permanent invariants

`DEATH_CONFIRMED != ESTATE_OPENED`

`KINSHIP != AUTOMATIC_INHERITANCE`

`NAMED_IN_INSTRUCTION != PROPERTY_TRANSFERRED`

`BENEFICIARY != OWNER`

`ADMINISTRATOR != OWNER`

`CUSTODY != OWNERSHIP`

`POSSESSION != OWNERSHIP`

`HOUSEHOLD_USE != OWNERSHIP`

`DOCUMENT_EXISTS != CONTROLLING_DOCUMENT`

`LATEST_DOCUMENT != CONTROLLING_DOCUMENT_BY_DEFAULT`

`INVENTORY_ENTRY != OWNERSHIP_PROOF`

`ASSET_LISTED != ASSET_PRESENT`

`CLAIM_FILED != CLAIM_ACCEPTED`

`DISTRIBUTION_PLANNED != DISTRIBUTION_COMPLETED`

`VALUATION != SALE_PRICE`

`MEMORIAL_OBJECT != ESTATE_ASSET_BY_DEFAULT`

`POKEMON_COMPANION != PROPERTY`

`OFFICE_SUCCESSION != PRIVATE_ESTATE_SUCCESSION`

`BATTLE_VICTORY != OWNERSHIP_TRANSFER`

`MINECRAFT_CHEST_CONTENTS != CANONICAL_ESTATE_INVENTORY`

`ITEM_DROP != INHERITANCE`

## Pokémon companion boundary

A deceased Trainer's Pokémon retain creature/relationship continuity. The system must never convert them into estate assets merely because they were associated with the Trainer.

If canon contains a specific guardianship, partnership-transfer, sanctuary or care process, model that through the appropriate creature, social, care and agreement authorities. Any Poké Ball or equipment ownership question remains distinct from the Pokémon's identity and agency.

## Generator behavior

The generator may create a proposed legacy mystery only when the underlying death, object and relationships are already permitted by canon policy. It may introduce uncertainty through incomplete inventories, contradictory testimony, missing records or multiple plausible stewardship claims.

It may not manufacture a surprise will to override established relationships, automatically make the nearest relative an heir, invent a hidden child to resolve ownership, classify a companion Pokémon as property, or turn every valuable object into a supernatural artifact.

Where rules are absent, preserve `UNKNOWN` or route the decision to authored canon.

## Chronicle integration

Chronicle records events such as an instruction being written, an inventory being conducted, a claim being submitted, a decision being issued, an asset being handed over and a later correction being made. It does not compress those into one timeless fact.

A current ownership query resolves through Property/Ownership using authoritative transfer evidence. An estate query can explain why that transfer was attempted or contested.

## Full and reduced encounter contracts

### Estate Inventory Storage Perimeter

Full intention: adversaries threaten access to a storage site while custodians protect records and estate objects. Rich implementation can include protected objects, carrying, interception, displacement, dynamic access routes and tactical protection.

Dependencies: targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; content-specific damage/status/Move/Ability/Item/Feature rules; terrain/weather/hazards/zones/reactions when site hazards matter; AI legal-action infrastructure; AI tactical policy; adapter/playback for protected-object semantics.

Full status: BLOCKED.

Reduced version: all estate records and assets remain outside BattleSpec in a pre-authored safe state. Static geometry is frozen before initiative. AutoPTU may establish only `IMMEDIATE_INVENTORY_STORAGE_APPROACH_CLEAR`. That result cannot authenticate records, inventory assets, assign ownership or close the estate.

### Legacy Transfer Route Interruption

Full intention: a steward transports a legacy object through a threatened route.

Full dependencies add escort/protected-object carrying and tactical withdrawal/protection policy, which are not covered by the current complete-movement classification.

Full status: BLOCKED.

Reduced version: the object and courier remain outside BattleSpec. The battle resolves a static chokepoint. Output is limited to `IMMEDIATE_LEGACY_TRANSFER_ROUTE_CLEAR`; delivery and title transfer require separate authored events.

### Vacant Homestead Access Incident

Full intention: parties need safe access to a residence or workshop whose estate status is unresolved.

Dynamic structures, hazards, movable contents or tactical environmental interactions require the corresponding terrain/hazard/reaction and playback families.

Full status: BLOCKED when those mechanics matter.

Reduced version: property boundaries and contents remain immutable during combat. AutoPTU may establish `IMMEDIATE_PROPERTY_APPROACH_CLEAR`. It cannot establish occupancy, ownership, abandonment or inheritance.

### Testament Record Recovery Perimeter

Full intention: a threatened archive contains a potentially relevant instruction record.

The rich version requires protected-object interaction/carrying, objective-aware AI, lifecycle and any selected hazard/reaction mechanics.

Full status: BLOCKED.

Reduced version: the record remains outside BattleSpec. AutoPTU may establish `IMMEDIATE_RECORD_STORAGE_ACCESS_CLEAR`. Archives and the estate-review process later determine whether the record exists, is authentic, accessible and relevant.

## Adapter boundary

Minecraft/Cobblemon/Craftics may render a sealed room, inherited workshop, locked chest, displayed heirloom, archive box or changed household after Narrative has established those facts.

The adapter may not inspect a deceased entity's inventory and declare it an estate inventory. It may not use item pickup as title transfer. It may not use block possession, container access, NPC proximity or player interaction to decide inheritance. It may play back an already-authorized transfer after the authoritative narrative/property event exists.

## Canon status

PROPOSED only. This file creates no heirs, estates, wills, succession rules, inheritance customs, ownership transfers or companion-Pokémon dispositions by itself.