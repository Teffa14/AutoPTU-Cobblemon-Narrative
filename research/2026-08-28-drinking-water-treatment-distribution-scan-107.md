# Ouros Narrative Research — Drinking-Water Treatment & Distribution — Pass 107

Status: RESEARCH / PROVENANCE ONLY. This file creates no Ouros canon and no PTU rules.
Date: 2026-08-28
Baseline inspected before write: `bb24cb2820dfbc80814150a987ceac268ff86dca`

## Why this pass exists

The complete recursive Narrative repository tree was inspected before selecting this topic and returned `truncated=false`.

The nearest governing layers were then read directly:

- `design/water-management-dams-reservoirs-canals-continuity-extension.md` already owns managed freshwater source/control assets, reservoirs, intakes, channels, operating regimes, diversions and broad raw-water availability.
- `design/waste-sanitation-recycling-pollution-layer.md` already owns wastewater, contamination observations, treatment of waste streams, pollution-source claims and cleanup.
- `design/infrastructure-outage-restoration-extension.md` already owns multi-service outage propagation, fallback and staged restoration.
- `design/engine-readiness-snapshot-pass-106.md` preserves the current permanent battle-capability map.

The remaining operational gap is narrower: what happens between an authored source-water handoff and an actual drinking-water service point. Ouros needs continuity for treatment facilities, treatment stages, treated-water storage, distribution nodes/links, service sectors, endpoint/service-point observations, alternate supply, verification and staged restoration without becoming a chemistry or hydraulic simulator.

This research therefore does not reopen dams/canals, wastewater, pollution, utility-outage orchestration or generic infrastructure repair.

## Public Pokémon / fangame sources

### Pokémon Reborn — Water Treatment Center

Source: https://pokemon-reborn.fandom.com/wiki/Water_Treatment_Center

Observed high-level structure:

- a treatment facility has multiple chambers and controllable water states;
- access and traversal change when water is drained or refilled;
- restoration is sectional rather than one global instant switch;
- a central problem can make water visibly unusable while the physical plant still exists;
- after the central obstruction is removed, individual sections still need to be worked through before the facility is broadly restored.

Reusable Ouros lesson:

A treatment plant should preserve identity across degraded, isolated, testing and restored states. Removing the initiating problem should not automatically mean every treatment stage, storage asset, distribution path or service sector is verified.

Transformation boundary:

Do not copy the dungeon layout, characters, Team Meteor plot, PULSE system, one-way gates, trash-stack puzzle, TM rewards, battle sequence, Murkwater Surface rules or the game's clean/dirty-water mechanics. In particular, Reborn Field Effects are not PTU 1.05 mechanics and must never be imported into AutoPTU as environmental rules.

### Pokémon Reborn — Azurine Lake / downstream city continuity

Source: https://pokemon-reborn.fandom.com/wiki/Azurine_Lake
Source: https://pokemon-reborn.fandom.com/wiki/Coral_Ward

Observed high-level structure:

- degraded water conditions persist across a broad area for a substantial portion of the story;
- industrial and treatment-site events connect to downstream environmental state;
- affected districts develop social and economic consequences while the problem persists;
- restoration can make old locations newly useful without erasing their history.

Reusable Ouros lesson:

Water-system consequences should be scoped by authored dependency paths and timestamps. A source/treatment problem can affect downstream service or ecology, but one visible symptom does not establish its cause. Recovery should create later callbacks rather than reset the district to an ahistorical baseline.

Transformation boundary:

Do not import Reborn's causal chain, villain organization, pollution plot, exact locations, field mechanics or restoration rewards. Ouros must require its own evidence edges between source state, treatment state, distribution state, service availability and ecological consequences.

### Pokémon animation — Lake Lucid / The Joy of Water Pokémon

Source: https://bulbapedia.bulbagarden.net/wiki/Lake_Lucid

Observed high-level structure:

- a water body can remain degraded over a long period;
- multiple generations can study and work on recovery;
- restoration can be accompanied by the return of Pokémon and creation of new local institutions;
- ecological recovery and care infrastructure can become part of a place's identity after the original problem changes.

Reusable Ouros lesson:

Water restoration can be a multi-season or multigenerational story rather than a one-quest repair. The meaningful persistent state includes observations, interventions, institutional memory, ecological response and later monitoring.

Transformation boundary:

Lake Lucid is environmental restoration, not evidence for a drinking-water ruleset. It is used only for continuity and long-tail consequences. Do not infer that visible Pokémon return proves potability, that Water-types purify water, or that a care institution owns water-quality authority.

## External operational references used only for abstraction

### CDC — How Water Treatment Works

Source: https://www.cdc.gov/drinking-water/about/how-water-treatment-works.html

The CDC describes drinking-water treatment as a sequence that can include coagulation, flocculation, sedimentation, filtration and disinfection, while noting that actual treatment differs by community and source-water quality.

Reusable Ouros lesson:

Model treatment as an authored ordered set of stages when a specific facility has them. A stage can be available, bypassed, unavailable, under maintenance, testing or verified without inventing a universal treatment recipe.

Do not import:

- US safety standards;
- chemical quantities;
- microbiology simulation;
- pH or disinfectant arithmetic;
- treatment efficiencies;
- mandatory treatment sequences;
- real-world regulatory thresholds.

### US EPA — Drinking Water Distribution System Tools and Resources

Source: https://www.epa.gov/dwreginfo/drinking-water-distribution-system-tools-and-resources

The EPA describes distribution systems as networks connecting source/treatment to customers through pipes, storage facilities, valves and pumps. It also emphasizes that distribution itself matters to water quality rather than being a neutral post-treatment pipe.

Reusable Ouros lesson:

`TREATMENT_VERIFIED` and `SERVICE_POINT_VERIFIED` must be different facts. A treatment facility can produce an acceptable handoff while a downstream link, storage asset, local connection or endpoint still has an unresolved problem.

Do not import US ownership boundaries, regulation, engineering standards or pressure requirements.

### US EPA — How Does Your Water System Work?

Source: https://www.epa.gov/ground-water-and-drinking-water/how-does-your-water-system-work-text-only

The source separates source water, treatment, storage and distribution. This is useful as an information-architecture boundary, especially because source water may originate far from the place receiving service.

Reusable Ouros lesson:

A player's current location should never make the nearest visible water body the assumed source. Source, treatment facility, storage and service sector need authored links.

## Internal PTU / Caelo cross-check

Internal source index reviewed:

- `research/2026-08-18-source-scan.md`
- PTU `CoreRulebook.pdf`
- `Caelo Player's Guide 1.5.pdf`
- `Caelo Region Location & Encounter List.pdf`
- `character creation merged.pdf`
- `Erratas and extra merged.pdf`
- project Pokédex material

The existing source scan establishes that Caelo can give locations explicit mechanical environmental state, and that PTU/Caelo rules contain terrain, weather, capability and encounter mechanics that can be authored when their actual rule supports them.

No inspected evidence establishes a universal PTU/Caelo subsystem for:

- potability;
- treatment chemistry;
- filtration efficiency;
- distribution pressure or flow;
- pipe breaks as damage zones;
- waterborne illness;
- drinking water as healing;
- generic contamination applying Poison;
- Water-type Pokémon purifying arbitrary water;
- Poison-type Pokémon being safe in contaminated water;
- Move-based treatment or pumping;
- plumbing/utility Skill checks;
- species-level water-utility jobs.

Therefore those remain UNKNOWN unless a concrete rule, Move, Ability, Item, Capability, Trainer Feature or authored Caelo effect is verified.

## Live AutoPTU evidence inspected

### AutoPTU-Java

Head during this pass: `b828913726b68ebb039cfdfead129530f2da34a6`, PR #261, `Apply pre-resolution target replacement in runtime`.

Recent Intercept/pre-resolution chain now includes:

- #256 authoritative battle RNG for the Intercept d20;
- #257 Python-oracle mutation ordering;
- #258 authoritative candidate-attempt sequence composition;
- #259 spatial-success branch composition;
- #260 ordered pre-resolution target-hook registry and parity gate;
- #261 application of pre-resolution target replacement in the runtime before subsequent resolution.

This strengthens server-owned target-replacement orchestration. It does not prove generalized reactions, every Ability redirection, every Move target replacement, broad Push/Pull, broad Knockback, all forced movement or environmental displacement.

No capability family is promoted from this evidence alone.

### AutoPTU Python

Head during this pass: `4a7d8019a11442be12aa16ba47ebe260ea4d9535`, PR #215, `Career: normalize malformed battle events at API boundary`.

This change normalizes malformed legacy battle-event collections at the Career API/cache boundary and aligns related tests. It is stability/backward-compatibility work, not new tactical mechanics.

## Reusable structures for Ouros

1. Source-to-service chain

Preserve explicit authored links:

`source-water handoff -> treatment facility -> verified treated-water handoff -> storage/distribution -> service sector -> service point`

Every edge can have independent availability and evidence.

2. Treatment-stage continuity

A plant can be available while one stage is limited. A stage can be repaired but not verified. A bypass can be authorized without proving the output is suitable for every use.

3. Quality versus quantity versus availability

Keep at least three concepts separate:

- whether water is physically available;
- whether a quality assessment/clearance supports the intended use;
- whether a particular endpoint can actually receive service.

Never derive one from appearance, taste, Pokémon presence or a Minecraft water block.

4. Scoped service sectors

A district can be normal while one elevated zone, clinic, station, farm branch or building remains degraded. Do not use a global `city_water_ok` flag.

5. Alternate supply with provenance

Temporary tanks, delivered water, alternate source connections or other canon-approved fallbacks need their own IDs, start/end windows, intended uses, service scope and verification references.

6. Staged restoration

Useful sequence:

`source available -> treatment stage restored -> treatment output verified -> storage/distribution path restored -> sector verified -> service point verified -> downstream owner resumes service`

This sequence is descriptive architecture. Individual settings may omit or reorder stages when canon supports a different system.

7. Long-tail place memory

Temporary distribution points, closed treatment halls, old reservoirs, abandoned mains, public fountains or former utility compounds can remain socially and ecologically meaningful after service topology changes.

## Encounter-design lessons

Mechanically rich water-utility encounters should avoid putting unverified hydraulic or contamination rules into AutoPTU.

A full treatment-plant access encounter might want:

- route-control or withdrawal objectives;
- moving or restricted technical zones;
- Intercept and forced movement;
- generalized reactions;
- water-edge or machinery hazards;
- objective-aware AI;
- semantic Minecraft/Cobblemon playback.

Those dependencies must be declared against the permanent capability map.

A reduced implementation can preserve the same narrative premise by isolating equipment before battle, evacuating workers, freezing water-system state and fighting in a reviewed static access area. The battle can secure access without claiming to repair, treat, verify or restore water service.

## Research exclusions

This pass does not copy protected dialogue, dungeon layouts, characters, villain plots, puzzle sequences, Field Effects or distinctive story beats from Pokémon Reborn or the animated series.

External public-health/utility sources are used only to derive clean state boundaries and operational sequencing. They do not become Ouros law, chemistry, engineering, health or PTU mechanics.

## Candidate canon questions exposed by this research

- Which Ouros settlements use centralized treatment, local treatment, wells, springs, rain collection or other arrangements?
- Which source-water systems feed which drinking-water systems?
- What institutions operate treatment and distribution where they exist?
- Which uses require distinct quality clearance in each region?
- What fallback arrangements exist during outages?
- Are public fountains, taps or water points culturally important locations?
- Which legacy waterworks remain visible after a system is replaced?
- Which individual Pokémon have authored utility roles, if any?
- What information about water quality is public, private or institutionally controlled?

No answer is canonized by this research file.