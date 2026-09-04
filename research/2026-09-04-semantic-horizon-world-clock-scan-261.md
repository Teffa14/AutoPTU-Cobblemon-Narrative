# Semantic horizon and restart-safe world clock scan — Pass 261

Status: RESEARCH / PROVENANCE. No canon promotion.
Date: 2026-09-04

## Question

Pass 260 requires semantic retention horizons and a restart-safe clock, but intentionally leaves their evaluator model open. This pass asks how Ouros can expire or retain ecological consequences without using one arbitrary TTL and without allowing Minecraft presentation time to author ecological or PTU truth.

## Repository boundary inspected

Current focus remains `design/ecology-development-program.md`.

Relevant existing contracts inspected before writing:
- `design/provisional-ecology-retention-policy-contract.md`
- `design/provisional-counted-source-state-contract.md`
- `design/counted-source-resolution-contract.md`
- `design/individual-disturbance-response-contract.md`
- `design/site-use-identity-separation-contract.md`
- `design/ouros-source-authority-and-species-policy.md`
- `implementation/marea-sendero-provisional-retention-trace-v1.json`
- `tests/test_ecology_provisional_retention.py`
- `design/engine-readiness-snapshot-pass-260.md`

The repository already forbids restart, chunk unload, non-detection and generic despawn from implying expiry. Pass 261 does not reopen that decision.

## New public sources

### Real ecology: recovery is mechanism-specific

U.S. Geological Survey, Mebane 2022, "The capacity of freshwater ecosystems to recover from exceedances of aquatic life criteria":
https://www.usgs.gov/publications/capacity-freshwater-ecosystems-recover-exceedances-aquatic-life-criteria

Reusable lesson: recovery time depends on disturbance magnitude, recurrence and life history. Pulse and press disturbances do not share one recovery schedule. A universal cooldown would erase meaningful ecological differences.

U.S. Geological Survey, Mesa & Schreck 1989, "Electrofishing mark-recapture and depletion methodologies evoke behavioral and physiological changes in cutthroat trout":
https://www.usgs.gov/publications/electrofishing-mark-recapture-and-depletion-methodologies-evoke-behavioral-and

Reusable lesson: different measured consequences returned toward baseline on different timescales. Observable behavior and physiological indicators did not provide one interchangeable recovery clock. Ouros should therefore attach horizon semantics to the state being retained rather than to the observation event generically.

U.S. Geological Survey, Smith & Johnson 2004, "Modeling the effects of human activity on Katmai brown bears through the use of survival analysis":
https://www.usgs.gov/index.php/publications/modeling-effects-human-activity-katmai-brown-bears-ursus-arctos-through-use-survival

Reusable lesson: human presence changes time spent in a resource area and repeated exposure can change response. Duration, context and overlap matter independently from simple presence/absence.

### Minecraft/Fabric time semantics

Fabric Yarn 1.21 `ServerWorld` documentation:
https://maven.fabricmc.net/docs/yarn-1.21%2Bbuild.1/net/minecraft/server/world/ServerWorld.html

The documentation distinguishes world "time" from time-of-day. Time-of-day drives the day/night presentation and may be changed or frozen; the ordinary time counter is used for scheduled ticks and advances separately. This is useful evidence for rejecting time-of-day as an ecological monotonic clock.

Fabric Yarn 1.21 `ServerWorldProperties` documentation:
https://maven.fabricmc.net/docs/yarn-1.21%2Bbuild.1/net/minecraft/world/level/ServerWorldProperties.html

This exposes world time/time-of-day properties. It is adapter evidence only. Ouros must verify the exact pinned Minecraft/loader version before binding implementation to these names or persistence guarantees.

### PTU wilderness information

Pokemon Tabletop United community rules reference, Skills / Survival:
https://pturpg.wikidot.com/skills

Reusable lesson: Survival supports scouting, tracking, resource knowledge and ecological information gathering. It does not establish a universal duration for ecological consequences. PTU skill checks can later affect evidence acquisition when the corresponding Trainer Feature/perk path is verified; they should not control the private world clock.

### Fan-game / living-world structures surveyed

Pokémon Living World public project page:
https://www.pokeliving.com/

Reusable high-level idea only: persistent worlds gain narrative value when state continues independently from a single encounter screen. The public page is promotional evidence, not a mechanical authority and not proof of a particular implementation.

Pokémon Gaia overview surveyed through public fan-game material: its ruins/history-driven exploration is a useful reminder that environmental evidence can persist longer than the immediate event that produced it. No plot, characters, dialogue, dungeon sequence or proprietary prose is imported into Ouros.

## Derived design lessons

### CANON-ALIGNED

- Expiry is an explicit semantic transaction.
- Presentation lifecycle, day/night display, chunk lifetime and observation count cannot author expiry.
- Public observation history and private ecological consequence state remain distinct.
- Minecraft/Cobblemon remains presentation/integration authority, not PTU mechanical authority.

### PROPOSED

Use a typed semantic-horizon registry instead of one TTL field.

Candidate evaluator families:
- `PROJECTION_LIFECYCLE_BOUND`
- `DURATION_SINCE_AUTHORITY_EVENT`
- `CONDITION_STABLE_FOR`
- `VALIDITY_RECORD_BOUND`
- `AUTHORITY_EVENT_BOUND`
- `MANUAL_REVIEW_REQUIRED`

Use a project-owned monotonic ecological clock abstraction. A Minecraft game-time counter may back that abstraction only after the pinned runtime proves persistence and non-regression properties. Time-of-day must never be the monotonic basis.

Persist a clock epoch plus tick/value checkpoint. If a restore, rollback or migration presents a lower raw clock value than the last committed checkpoint, fail closed by opening a new epoch or quarantining horizon evaluation. Do not silently expire states because time appeared to move backward.

### UNCERTAIN

- Whether Ouros world time should advance while the server is offline. Minecraft game time generally represents running-world ticks; a persistent MMO may eventually need a separate calendar service for offline progression.
- Exact Minecraft/Cobblemon/Craftics version and API names used by the production adapter.
- Species-specific disturbance/recovery durations. No value is promoted by this research.
- Which future AutoPTU semantic results should be duration-bound versus event-bound.

### FIXTURE-ONLY

Pass 261 may use synthetic world ticks and synthetic horizon definitions only to prove ordering, restart and rollback behavior. Those numbers are test vectors, not ecology canon.

## Copyright / transformation note

Sources are used for general structures and factual design lessons. Ouros does not copy protected dialogue, characters, plots, quest text or distinctive scenario sequences from campaigns, fan games or official Pokémon media.
