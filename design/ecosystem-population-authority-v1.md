# Ecosystem population authority v1

Status: PROPOSED ARCHITECTURE
Date: 2026-09-03
Pass: 221

## Intent

Ouros needs one durable authority model connecting ecosystem-scale geography, finite wild populations, species diet provenance, Cobblemon projection and persistent individuals.

This design is proposed. It does not change the fixed Marea map anchors, canonize a new ecosystem boundary, assign a new species, or supply unverified diet values.

## 1. Spatial authority

Ouros world ecology uses this hierarchy:

```text
REGION
  ECOSYSTEM
    ECOTONE / TRANSITION BELT
    HABITAT PATCH
      MICROHABITAT / SITE
```

`ECOSYSTEM` is the primary population-accounting unit.

Minecraft biome IDs/tags, block palettes, height, water, structures, light, weather and time are physical context used inside this hierarchy. One ecosystem can span multiple Minecraft biome tags. A single biome tag can also appear in more than one authored ecosystem.

The map target is ecosystem-scale 1:1 world-space representation. Distinct ecosystems should have enough physical separation and travel space to behave as places, rather than being compressed into adjacent showcase patches.

No universal block-to-meter conversion is frozen by this document. Scale acceptance should use in-world travel time, habitat extent, resource distribution, line-of-sight, settlement footprint and population movement to verify that the geography is not compressed.

## 2. Ecosystem record

Candidate `ECOSYSTEM_STATE`:

```text
ecosystem_id
region_id
status
world_dimension
extent_geometry_ref
ecological_character
minecraft_biome_tags[]
habitat_patch_ids[]
neighbor_ecosystem_ids[]
ecotone_ids[]
resource_profile_ids[]
population_ledger_ids[]
human_land_use_context[]
seasonal_context_ref
provenance[]
last_authoritative_transition
```

The geometry reference can evolve in implementation. The important contract is that the extent belongs to Ouros and cannot be inferred solely from the Minecraft biome registry.

## 3. Population ledger

Each species/population unit in an ecosystem receives an authoritative ledger.

Candidate `ECOSYSTEM_POPULATION_LEDGER`:

```text
ledger_id
ecosystem_id
population_id
species_id
form_policy
source_status
anonymous_available_count
anonymous_reserved_count
persistent_member_ids[]
transit_member_ids[]
known_demographic_events[]
current_total
provenance
revision
```

Invariant:

```text
current_total
= anonymous_available_count
+ anonymous_reserved_count
+ count(persistent_member_ids owned here)
+ count(transit_member_ids owned here)
```

A projection event moves membership between availability states. It preserves `current_total`.

## 4. Projection reservation

Candidate `WILD_PROJECTION_RESERVATION`:

```text
reservation_id
ledger_id
member_kind: ANONYMOUS | PERSISTENT
persistent_member_id?
requested_species
requested_form
projection_site
spawn_context_snapshot
created_at
actor_uuid?
state: RESERVED | PROJECTED | RELEASED | CONSUMED_BY_WORLD_TRANSITION
```

Flow for a generic wild actor:

```text
Cobblemon native spawn candidate
-> Ouros ecosystem lookup
-> ledger availability check
-> reserve one member
-> publish complete canonical WILD blueprint
-> allow Cobblemon actor projection
-> bind actor UUID as presentation correlation
```

If no member is available, the spawn request cannot create a canon-correlated wild actor even if Cobblemon's native weight says the spawn is eligible.

When a generic actor unloads/despawns for ordinary runtime reasons, the reservation can return to availability according to persistence policy. No demographic event occurs.

For a persistent individual, unload releases only presentation state. It must not free the identity for simultaneous reuse elsewhere.

## 5. Population-changing transitions

Only explicit authoritative transitions can change the ledger total or ecosystem ownership.

Candidate event families:

`WILD_BIRTH_OR_HATCH_CONFIRMED`

`WILD_DEATH_CONFIRMED`

`WILD_CAPTURE_CONFIRMED`

`WILD_RELEASE_OR_INTRODUCTION_CONFIRMED`

`WILD_IMMIGRATION_CONFIRMED`

`WILD_EMIGRATION_CONFIRMED`

`WILD_MIGRATION_TRANSFER`

Migration between two ecosystem ledgers should be atomic or use an explicit transit owner so the same member cannot be counted twice.

Observation, rumor, spawn attempts, despawn, chunk unload, bait, time, weather and player proximity are never demographic transitions by themselves.

## 6. Persistent individuals

A persistent wild individual consumes one and only one ledger membership.

Promotion from anonymous to persistent identity is a conservation-preserving operation:

```text
anonymous member -1
persistent member +1
current_total unchanged
```

The canonical first Sendero Fletchling can therefore remain a persistent encounter identity later without increasing Fletchling abundance merely because the identity gained history.

Named Trainer/NPC partners such as Pia Min's Redline remain outside the wild ledger unless an explicit release transition places them into a wild population.

## 7. Diet and resource support

Candidate `SPECIES_DIET_PROFILE` is source-backed and species-specific. It must be extracted from approved PTU/PGU/Caelo material before use.

Candidate `ECOSYSTEM_RESOURCE_PROFILE`:

```text
resource_profile_id
ecosystem_id
resource_type
habitat_patch_ids[]
seasonal_availability
renewal_model
consumer_species_ids[]
evidence_status
source_provenance[]
```

A diet profile answers what an organism can plausibly seek or consume. A resource profile answers whether and where those resources exist in the authored ecosystem.

Neither record directly modifies a PTU battle stat.

Future demographic simulation may use sustained resource deficits/surpluses as one input to reproduction, movement or survival. Such effects require explicit demographic rules and must never be implemented as `spawn weight = population growth`.

## 8. Cobblemon responsibility

Cobblemon remains the preferred native provider for:

- natural spawn candidate generation;
- biome/time/light/weather/moon/world conditions;
- spawn rarity/weight selection;
- overworld Pokémon entity/model/animation;
- navigation and ordinary presentation lifecycle where safe;
- world entity UUID correlation.

Ouros adds the population gate and canonical identity/blueprint authority before a wild actor becomes authoritative content.

Cobblemon weights answer relative presentation/candidate selection among eligible species. They do not define abundance totals.

## 9. Bait/provisioning contract

A provisioning event can influence:

- which already-existing member becomes more likely to approach a site;
- local path/behavior intent;
- detectability;
- residence time near an observation point;
- competition among individuals/species;
- later learned/habituated behavior if evidence supports it.

A provisioning event cannot directly increase `current_total`.

Two bait locations inside one ecosystem share the same finite availability pool. If eight relevant wild members exist and six are already reserved/projected elsewhere, neither site can independently manifest eight more.

Diet relevance must come from `SPECIES_DIET_PROFILE` plus actual resource identity/provenance. A Minecraft edible tag alone is insufficient.

## 10. Observation versus authority

Characters should rarely have direct access to the ledger count.

Nerea/Ema/player-facing ecology uses observations such as:

```text
count detections
unique marked identities
tracks/calls
bait response
transect effort
absence with effort
arrival/departure evidence
nest/dependent-site evidence
```

Those observations update beliefs, reports and quests. They do not overwrite the server's ground truth.

This separation supports mysteries where an apparent population crash is actually redistribution, low detectability, migration, changed activity window or observer bias.

## 11. Marea scale rule

Current CANON-APPROVED Marea coordinates remain authoritative anchors. This proposal does not move them.

For future worldbuilding, do not create a sequence of tiny neighboring ecosystems around those coordinates merely to show more biome variety. Treat Marea Interior as a district embedded in a much larger ecological envelope unless later canon explicitly divides it.

New ecosystem design should document:

```text
physical extent
minimum traversal time
major landforms
resource gradients
settlement pressure
habitat patches
transition belts
population flows
neighbor relationships
```

If the final 1:1 spatial plan proves the current anchor distances themselves are too compressed, create an explicit coordinate migration proposal rather than silently changing canon.

## 12. Cross-pass integration

Pass 216 temporal ecology: native temporal conditions filter projection opportunities against the finite ledger.

Pass 218 migration: moves ownership through explicit transfers; observations remain separate from the transfer truth.

Pass 219 nesting: dependent-site state can precede any demographic addition; hatch/birth changes the ledger only when confirmed.

Pass 220 provisioning: bait modifies finite-member behavior and sampling, never population creation.

## 13. Battle-engine boundary

Population accounting is persistent world authority and does not become a new permanent AutoPTU battle capability family.

When a wild interaction enters PTU combat, the existing exact WILD blueprint becomes a participant under AutoPTU authority. Capture, death/injury, Items, Status, forced movement, reactions and other battle consequences can change world state only through explicit result contracts.

Minecraft/Cobblemon must not infer population transitions from entity health, entity removal or playback.

## 14. Acceptance tests for future implementation

1. Repeated chunk load/unload around Sendero never increases the authoritative Fletchling count.
2. Day/night transitions can change visible composition without changing totals.
3. Two simultaneous bait points cannot each allocate the same anonymous member.
4. A persistent Fletchling cannot be projected twice.
5. Successful authoritative capture consumes exactly one wild membership.
6. Cancelled/failed capture preserves the membership.
7. Runtime entity despawn restores projection availability without authoring death/emigration.
8. Migration transfer cannot produce origin+destination double-counting.
9. A Minecraft biome boundary does not automatically create a second ecosystem ledger.
10. A source-unverified food cannot acquire diet or PTU Item effects through presentation tags alone.

## 15. Canon status

PROPOSED until accepted by an explicit canon promotion.

Existing CANON-APPROVED Marea anchors and first Fletchling blueprint remain unchanged.