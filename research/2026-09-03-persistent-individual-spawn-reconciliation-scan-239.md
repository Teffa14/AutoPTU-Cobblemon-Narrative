# Persistent individual / generic spawn reconciliation scan — Pass 239

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Pass: 239

## Question

How can Ouros let Minecraft/Cobblemon show wild Pokémon naturally while guaranteeing that visible entities do not clone, delete or silently mutate canonical population members?

This pass follows `design/population-demography-contract.md` and the ecology programme. It does not change established Marea canon.

## Repository context inspected

The repository tree, current ecology directive, source-authority policy, Pass 238 demographic contract/fixture, current engine-readiness snapshot and the canon first Sendero Fletchling population were inspected before this note was written.

Existing invariants already require:

- Ouros owns population truth;
- Minecraft/Cobblemon owns presentation, not abundance;
- the first persistent Sendero Fletchling has a canonical encounter/member identity separate from any entity UUID;
- `population_total = known_persistent_members + unresolved_member_pool`;
- generic spawn/despawn cannot alter demographic totals.

Pass 239 therefore needs a reconciliation contract rather than a new encounter table.

## New public-source findings

### 1. Detection is not identity or abundance

USGS capture-recapture work shows that individual detection probability can differ substantially between animals. This matters because observed animals are a biased sample of the population; repeated sightings cannot safely be converted directly into population truth.

A related mark-resight study shows that even marked individuals may be incompletely identified during later observations. Ouros should therefore preserve uncertainty when a visible actor is not explicitly bound to a known member.

Sources:

- U.S. Geological Survey, “Individual heterogeneity and identifiability in capture-recapture models” (2004): https://www.usgs.gov/publications/individual-heterogeneity-and-identifiability-capture-recapture-models
- U.S. Geological Survey, “Mark-resight abundance estimation under incomplete identification of marked individuals” (2014): https://www.usgs.gov/publications/mark-resight-abundance-estimation-under-incomplete-identification-marked-individuals
- PubMed, “Genotyping validates the efficacy of photographic identification in a capture-mark-recapture study...” (2020): https://pubmed.ncbi.nlm.nih.gov/33391717/

Reusable lesson: a sighting can be `KNOWN_MEMBER`, `PROVISIONALLY_MATCHED`, or `UNRESOLVED_POOL_REPRESENTATION`. Uncertain visual similarity must not merge canonical identities automatically.

### 2. Pokémon supports ecology through observation without exposing hidden truth

New Pokémon Snap explicitly frames field play as an ecological survey based on photographing Pokémon in their environments and recording behavior. Pokémon Legends: Arceus likewise asks the player to seek and observe wild Pokémon and notes that behavior and availability vary with conditions.

Sources:

- New Pokémon Snap official site: https://newpokemonsnap.pokemon.com/en-au/
- New Pokémon Snap Photodex official page: https://newpokemonsnap.pokemon.com/en-us/create-photodex/
- Pokémon Legends: Arceus official gameplay page: https://legends.arceus.pokemon.com/en-gb/gameplay/

Reusable lesson: repeated visible encounters can improve knowledge without giving the observer direct access to population state or hidden identity.

### 3. Pokémon data can preserve identity while presentation changes by context

Pokémon HOME support documents that presentation of some fields can differ depending on the connected game while the Pokémon's underlying data is not thereby altered. This is a useful high-level precedent for separating canonical identity/state from a context-specific presentation surface.

Source:

- Pokémon Support, Pokémon HOME data display article, updated 2026-01-30: https://support.pokemon.com/hc/es/articles/7963042951444

Reusable lesson: a presentation adapter may omit or transform visible fields without becoming authority over the underlying record.

### 4. Cobblemon entity lifecycle is not safe as population lifecycle

Cobblemon's changelog states that Pokémon save to the world by default, allowing the same Pokémon entity to remain after logout/login, while also noting that wild Pokémon still despawn over time. Current Cobblemon issue reports also show entity discard/despawn paths and cases where Pokémon in a chunk can disappear due to spawn/despawn behavior.

Sources:

- Cobblemon changelog: https://github.com/Cobblemon-Global/Cobblemon/blob/main/CHANGELOG.md
- Cobblemon issue #1971, entity discarded on recall warning: https://gitlab.com/cable-mc/cobblemon/-/work_items/1971
- Cobblemon issue #1686, forced despawn behavior: https://gitlab.com/cable-mc/cobblemon/-/work_items/1686

Reusable lesson: Minecraft entity persistence is a cache/presentation concern. Canonical population membership requires a separate server-authoritative record.

### 5. Existing community tooling independently converges on projection semantics

A public Cobblemon habitat project describes owned Pokémon shown through pasture tethering as world projections whose underlying Pokémon remains in storage, specifically to avoid loss/duplication across unloads or crashes. This is implementation inspiration only, not an Ouros dependency or authority source.

Source:

- Cobblemon Pokopia Habitats README: https://github.com/A00826925/Cobblemon-Pokopia-Habitats

Reusable lesson: lease/tether semantics are a practical pattern for preventing a presentation entity from becoming the sole owner of canonical state.

## Proposed Ouros interpretation

Ouros should treat each visible wild actor as a temporary presentation lease.

Lease classes:

```text
PERSISTENT_MEMBER_LEASE
UNRESOLVED_POOL_LEASE
TRANSIENT_COHORT_LEASE
EXTERNAL_ASSOCIATED_LEASE
```

A lease binds exactly one canonical source slot to at most one active Minecraft actor.

For a known persistent member:

```text
member_id -> active lease -> minecraft_entity_uuid
```

For an unresolved member:

```text
population_id + unresolved_slot_token -> active lease -> minecraft_entity_uuid
```

The unresolved slot token represents one already-counted member. Creating the lease never increments population abundance.

## Identity promotion

An unresolved pool representation may later become a named/persistent member when the world has reason to retain individual history, for example:

- repeated meaningful player interaction;
- capture attempt or structured battle;
- distinctive injury or ecological event;
- research tagging/marking;
- nest/parental role;
- migration leadership/sentinel role;
- authored story relevance.

Promotion must be atomic:

```text
unresolved_member_pool_count -= 1
known_persistent_member_ids += new_member_id
population_total unchanged
active lease rebinds to new_member_id
```

A promotion is identity resolution, not recruitment.

## Lease lifecycle

Recommended states:

```text
AVAILABLE
RESERVED
MATERIALIZED
ENGAGED
SUSPENDED
RELEASE_PENDING
RELEASED
INVALIDATED_WITH_AUDIT
```

Important transitions:

- chunk unload: `MATERIALIZED -> SUSPENDED` or `RELEASED`, canonical member remains;
- ordinary despawn: release lease only;
- server restart: reconstruct lease index from canonical state and surviving entity correlations when valid;
- battle handoff: lease becomes `ENGAGED`, preventing a second presentation actor for the same source slot;
- capture/removal semantic result: close lease and emit the correct demographic event;
- KO without removal: return member to ecology state; no abundance delta;
- entity UUID missing/reused: invalidate correlation, never delete the member.

## Anti-duplication invariants

```text
one_source_slot <= one_active_presentation_lease
one_minecraft_entity_uuid <= one_active_lease
lease_creation_delta_population = 0
lease_release_delta_population = 0
chunk_unload_delta_population = 0
minecraft_despawn_delta_population = 0
vanilla_death_delta_population = 0
identity_promotion_delta_population = 0
```

If a second entity appears for a source slot that already owns an active lease, the duplicate presentation must be quarantined/rejected rather than interpreted as another Pokémon.

## Observation implications

Pass 240 should not expose lease IDs or member IDs directly to players.

A player observation can produce:

```text
recognized_known_individual
possible_repeat_individual
unresolved_individual
species_only_sighting
```

The observation system may become more confident over repeated evidence but should keep false-match risk explicit.

## Canon boundary

This scan does not:

- set the actual abundance of Sendero Fletchling;
- name additional Fletchling;
- change Redline's external status;
- authorize new species;
- define capture rules;
- assume every visible wild Pokémon deserves permanent identity;
- require Minecraft entity UUIDs to survive forever.

## Mechanical dependency interpretation

Basic lease/reconciliation is Ouros + adapter state and does not require battle mechanics.

If a leased actor enters a structured encounter, the encounter uses the exact permanent capability categories and only those currently verified for its chosen mechanics. Rich retreat/interception/terrain-driven encounters remain dependent on their incomplete families.

## Next implementation target

Create a deterministic Marea/Sendero fixture proving:

1. the canon persistent Fletchling cannot have two active actors;
2. unresolved pool leases consume existing population slots without changing abundance;
3. ordinary despawn/chunk unload releases presentation without demographic loss;
4. identity promotion preserves population total;
5. a battle lease prevents concurrent respawn;
6. KO alone returns the member without removal;
7. semantic capture/removal is the only tested path that can emit `CAPTURE_REMOVAL`;
8. stale UUID correlation can be repaired without deleting canonical state.
