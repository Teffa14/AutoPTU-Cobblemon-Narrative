# Ecosystem demographic cycle v1

Status: PROPOSED ARCHITECTURE
Date: 2026-09-03
Pass: 222

## Intent

Extend finite ecosystem population authority with a balanced demographic lifecycle.

The canonical population is dynamic. Individuals can be born or hatch, mature, die, be captured or released, immigrate or emigrate, and participate in seasonal migration. Members can also redistribute among habitat patches and Minecraft biome areas without changing ecosystem ownership.

This document does not assign population numbers, breeding rates, lifespans, migration fractions, PTU Levels or ecosystem boundaries.

## 1. Two different meanings of population state

The server owns ground truth.

Characters own estimates and observations.

Canonical demographic state must never be reconstructed from how many Cobblemon entities happen to be loaded around players.

## 2. Conservation equation

For one ecosystem population ledger over an authoritative interval:

```text
N(t+Δt)
= N(t)
+ births_or_hatches
+ immigration
+ releases_or_introductions
- deaths
- captures
- emigration
```

The following preserve total population:

```text
spawn/projection
entity despawn
chunk unload/reload
day/night eligibility
weather eligibility
bait/provisioning
observation
movement among habitat patches
movement among Minecraft biome tags inside the same ecosystem
maturation/life-stage transition
promotion from anonymous member to persistent identity
```

Cross-ecosystem migration changes ecosystem ownership but should preserve the larger regional/metapopulation total unless another demographic event also occurs.

## 3. Stage-structured population ledger

Pass 221's `ECOSYSTEM_POPULATION_LEDGER` remains the population authority. Add demographic composition without forcing every anonymous member into an individual record.

Candidate extension:

```text
ledger_id
ecosystem_id
population_id
species_id
form_policy
persistent_member_ids[]
cohort_ids[]
transit_member_ids[]
projection_reservation_ids[]
current_total
last_demographic_resolution
next_due_demographic_windows[]
revision
provenance
```

Candidate `DEMOGRAPHIC_COHORT`:

```text
cohort_id
ledger_id
species_id
form
life_stage
count
current_habitat_patch_class?
seasonal_state: RESIDENT | DEPARTING | TRANSIT | ARRIVING | STOPOVER
breeding_eligible_count?
source_status
revision
```

Keep cohort dimensions minimal. Do not add sex, exact age, genetics, family membership or other fields until an approved species source or gameplay requirement needs them.

## 4. Persistent individual versus cohort

A persistent wild Pokémon remains one exact member of the ledger.

An anonymous cohort represents interchangeable membership for demographic accounting, not a pile of pre-authored clones.

When an anonymous member becomes persistent:

```text
source cohort count -1
persistent member +1
current_total unchanged
```

When a persistent member is captured:

```text
persistent wild membership -1
captured actor ownership +1
wild current_total -1
```

No automatic anonymous replacement occurs.

## 5. Biological age, PTU Level and Evolution are separate

These are distinct state families:

```text
BIOLOGICAL AGE / LIFE STAGE
PTU LEVEL / XP
EVOLUTION STATE / ELIGIBILITY
PHYSICAL SIZE/GROWTH when species/source requires it
```

Rules:

- maturation does not grant PTU Levels unless a separate progression rule resolves that;
- Level gain does not automatically age the Pokémon;
- aging does not automatically force Evolution;
- Evolution does not silently rewrite the population count;
- any species-specific coupling must come from PTU/Caelo/PGU/Kairos or approved Ouros canon with provenance.

This prevents the demographic simulator from becoming a second combat-progression engine.

## 6. Authoritative demographic events

Candidate event families:

```text
DEMOGRAPHIC_BIRTH_OR_HATCH
DEMOGRAPHIC_STAGE_TRANSITION
DEMOGRAPHIC_DEATH
DEMOGRAPHIC_CAPTURE_REMOVAL
DEMOGRAPHIC_RELEASE_ADDITION
DEMOGRAPHIC_IMMIGRATION
DEMOGRAPHIC_EMIGRATION
DEMOGRAPHIC_MIGRATION_DEPARTURE
DEMOGRAPHIC_MIGRATION_ARRIVAL
DEMOGRAPHIC_INTERNAL_REDISTRIBUTION
DEMOGRAPHIC_RESOURCE_PRESSURE_UPDATE
DEMOGRAPHIC_DISTURBANCE_UPDATE
```

Each event records:

```text
event_id
population_id
ecosystem_id
member_or_cohort_refs[]
effective_time
cause_family
source/provenance
prior_revision
result_revision
related_ecosystem_id?
related_world_event_id?
```

Movement and migration must never be inferred from an entity disappearing from loaded chunks.

## 7. Seasonal cycle

Demographic processes execute in authored windows rather than one giant annual formula.

Candidate sequence for a species may include:

```text
resource-window update
breeding eligibility window
birth/hatch/recruitment pulse
juvenile survival window
maturation window
seasonal redistribution
migration departure
migration transit/stopover
migration arrival
non-breeding survival window
```

This sequence is only a framework. A species can omit, combine or reorder windows when its source-backed ecology requires it.

Do not assume all species breed once per year, migrate, use the same life stages or reproduce in the same way.

## 8. Recruitment and reproduction

A birth/hatch result requires an explicit demographic rule.

Candidate inputs:

```text
species reproduction profile
eligible breeders
breeding season/window
resource sufficiency
suitable habitat/dependent-site availability
density pressure
disturbance
recent survival conditions
resident/migrant status
species-specific constraints
```

No single input guarantees recruitment.

A source-backed diet helps determine resource demand. It does not directly determine birth count.

A nest observation does not itself create offspring. A confirmed birth/hatch transition does.

## 9. Effective carrying pressure, not magic carrying capacity

Ouros should not maintain balance by forcing population back to an immutable target `K`.

Candidate `DEMOGRAPHIC_PRESSURE_STATE`:

```text
population_id
resource_pressure_by_type[]
space_pressure
shelter_pressure
dependent_site_pressure
human_disturbance_pressure
competition_pressure?
predation_pressure?
disease_pressure?
low_population_fragility?
overall_recruitment_pressure
overall_survival_pressure
provenance
```

These values modify specific vital processes. They do not add/delete members directly.

Examples:

- scarce food can lower recruitment or increase dispersal pressure;
- insufficient nesting sites can reduce successful recruitment without killing existing adults;
- high density may reduce juvenile survival before adult survival;
- very low abundance may reduce breeding success where the species model supports that;
- improved resources can raise future recruitment opportunity but never immediately spawn replacements.

## 10. Movement inside an ecosystem

A member can move between habitat patches, elevations, waters, vegetation bands and Minecraft biome tags while remaining owned by the same ecosystem ledger.

Candidate `INTRA_ECOSYSTEM_DISTRIBUTION_STATE`:

```text
population_id
habitat_patch_id
life_stage?
seasonal_state?
available_members_or_share
resource_affinity_snapshot
disturbance_snapshot
revision
```

This supports:

- daily foraging shifts;
- breeding-site concentration;
- movement toward water;
- local avoidance of human traffic;
- bait-induced redistribution;
- seasonal use of different patches.

Internal redistribution is not immigration/emigration.

## 11. Cross-ecosystem movement

Permanent dispersal and seasonal migration need explicit ownership transfer.

Preferred atomic model:

```text
origin membership
-> TRANSIT ownership/reservation
-> destination membership
```

At no point can both origin and destination count the same member as resident.

For partial migration, select only the source-backed/eligible subset. Do not move 100% of a species merely because a seasonal flag is active.

If an individual uses a stopover, the stopover may hold transit presentation/access without becoming the breeding population owner.

## 12. Capture, release and human pressure

Capture is a demographic removal from the wild population only after the authoritative capture result succeeds.

A failed/cancelled attempt changes no membership.

Release is an addition to the receiving wild ecosystem only after:

```text
actor exists and ownership permits release
receiving ecosystem is resolved
species/form is permitted by world/canon policy
release transition succeeds
```

No replenishment follows capture automatically.

Sustained capture pressure may change age/stage structure and future recruitment. That consequence must emerge from ledger changes, not from a hidden difficulty scaler.

## 13. Death and mortality

Death must be a confirmed world/battle consequence before the population loses a member.

Fainted, unloaded, missing, hidden, emigrated and not observed are not synonyms for dead.

Background mortality for anonymous cohorts may eventually be resolved through demographic windows, but it must be explicit, deterministic/persisted and source-backed. It cannot be implemented as random entity deletion around players.

## 14. Cobblemon projection contract

Cobblemon continues to provide native spawn candidate conditions and physical actors.

The demographic model provides the finite source pool.

Candidate projection flow:

```text
Cobblemon eligible spawn candidate
-> ecosystem + population lookup
-> demographic availability check
-> reserve persistent member or anonymous cohort membership
-> project physical actor
-> release projection on ordinary despawn/unload
```

If cohort count is zero and no persistent/transit member is eligible, Cobblemon cannot author another canonical individual regardless of native spawn weight.

Spawn weights can affect which available members are likely to become visible. They never regenerate the cohort.

## 15. Runtime cadence

Do not simulate reproduction/survival every game tick.

Use persisted authoritative windows/events.

Recommended separation:

```text
REAL-TIME EVENTS
capture, release, confirmed death, explicit movement/transfer, persistent-individual state

SHORT WORLD WINDOWS
activity, habitat-patch redistribution, temporary disturbance, projection availability

SEASONAL/DEMOGRAPHIC WINDOWS
breeding, recruitment, maturation, migration, background survival, resource-pressure reconciliation
```

Resolution should be deterministic/seeded or persist its result immediately so multiplayer sessions cannot resolve the same interval twice.

## 16. Balance goals

A healthy cycle should be capable of all of these outcomes without cheating:

- stable population near current ecological support;
- gradual growth after favorable recruitment;
- temporary juvenile-heavy pulse;
- aging into a more adult-heavy structure;
- decline after sustained capture/resource pressure;
- local redistribution with no total change;
- seasonal emigration followed by return/immigration;
- recovery through successful recruitment or real immigration;
- severe decline or local extinction if pressures remain unresolved.

The simulator must not guarantee equilibrium. Balance means the rules produce plausible feedback, not that every population is protected from consequences.

## 17. Anti-runaway rules

1. Recruitment requires a breeding/reproduction window and eligibility.
2. Newborn/juvenile cohorts need maturation delay before breeding unless the species source explicitly says otherwise.
3. Resource surplus increases opportunity, not instant births.
4. High density can suppress recruitment/survival/dispersal through explicit pressure functions.
5. Very low abundance can remain vulnerable; do not force recovery.
6. Capture removes real membership and receives no hidden replacement.
7. Migration can alleviate pressure but cannot duplicate members.
8. Internal biome movement changes distribution only.
9. Cohort resolution must be persisted exactly once per due window.
10. Persistent individuals participate in the same demographic accounting as anonymous cohorts.

## 18. Player-facing observability

Most characters do not know canonical counts.

They can observe consequences:

- more juveniles after a breeding pulse;
- fewer adults in repeatedly harvested/captured areas;
- seasonal arrivals/departures;
- changed habitat-patch use;
- nest/dependent-site success;
- mark/resight histories;
- food/resource pressure;
- apparent recovery that may actually be immigration.

This preserves ecology as something players investigate rather than a database statistic exposed by UI.

## 19. Implementation order

Recommended order:

1. finite ledger + projection reservation from pass 221;
2. cohort representation and life-stage transitions;
3. capture/release writeback;
4. intra-ecosystem redistribution;
5. atomic migration transfer;
6. source-backed reproduction profiles;
7. resource-pressure inputs from diet/ecosystem data;
8. background survival/recruitment windows;
9. richer source/sink/metapopulation behavior.

Each step should be verifiable before adding the next.

## 20. Battle-engine dependency boundary

Demographic simulation remains world-runtime authority, not a seventeenth AutoPTU battle capability family.

When a demographic transition depends on battle results, use only existing verified result contracts. Capture, death, Status, Items, Features, Moves or other PTU effects cannot be guessed by the demographic layer.

The permanent engine capability classification therefore remains unchanged by this proposal.

## 21. Acceptance tests

1. Capture one projected anonymous wild member: cohort -1 exactly once; no replacement spawn.
2. Mature ten juveniles: juvenile cohort -10, adult cohort +10, total unchanged.
3. Move five adults from forest-like patch to grassland-like patch inside one ecosystem: total and ownership unchanged.
4. Seasonal migration transfers five members to another ecosystem: origin -5, destination +5, regional total unchanged.
5. Chunk unload of five projected members: demographic totals unchanged.
6. Place bait: local distribution/detectability may change; total unchanged.
7. Breeding window resolves zero recruitment when required habitat/resource conditions fail.
8. Favorable breeding window can add a confirmed juvenile cohort without spawning visible entities immediately.
9. PTU Level gain leaves biological stage unchanged unless an explicit source-backed rule couples them.
10. Biological maturation leaves PTU Level unchanged unless an explicit progression result also occurs.
11. Re-running the same demographic window after restart cannot double births/deaths/migration.
12. Population at zero blocks generic canonical projection until a real birth/introduction/immigration adds membership.

## 22. Canon status

PROPOSED until explicit promotion.

Existing Marea anchors, Fletchling blueprint and all previously CANON-APPROVED facts remain unchanged.