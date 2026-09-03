# Ecosystem-scale population conservation scan — pass 221

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03

## Purpose

This pass follows the explicit Ouros direction that wild ecology must be authored at ecosystem scale, that maps should preserve a believable 1:1 world-space scale instead of compressing many ecosystems into a theme-park patchwork, that species diets from the supplied PTU/PGU/Caelo material must constrain ecological plausibility, and that bait/lure mechanics must never create additional wild Pokémon.

The immediate gap after passes 216–220 is population authority. Those passes already separate time-dependent generic spawning, persistent individuals, migration, dependent sites and provisioning. They did not yet freeze a conservation invariant connecting those systems to one finite ecosystem population.

This document records external research and internal-source routing. It does not canonize a new species, ecosystem boundary, population number, diet table or demographic rate.

## Existing Ouros constraints inspected

The repository inventory and current canon were inspected before writing. Relevant established facts include:

- `canon/marea-interior-first-wild-population-v1.md` already states that one visible actor does not equal local abundance and that entity despawn does not mean captured or dead.
- the first Fletchling is a bounded deterministic development actor, not a global ecology model;
- `canon/marea-interior-map-resident-network-v2.md` freezes current Marea anchors and requires explicit migration if those anchors ever move;
- pass 216 delegates generic temporal/biome spawn eligibility and weights to native Cobblemon facilities while preserving Ouros authority over population, identity, provenance and behavior;
- pass 218 introduces migration/stopover evidence without equating observations with population size;
- pass 219 creates dependent-site evidence without inventing offspring automatically;
- pass 220 models provisioning/baiting as an intervention on behavior and observation, not friendship, ownership or guaranteed spawning.

Pass 221 therefore adds a conservation layer underneath those concepts rather than replacing them.

## External research

### 1. Lures change detection, and the sign of that change can differ by species

Fidino et al. (2020), `Effect of Lure on Detecting Mammals with Camera Traps`, experimentally compared lure and non-lure cameras. The lure changed detection metrics only modestly overall and produced species-specific responses: some mammals were detected more often while some prey species were detected less often or arrived later.

Source: https://wildlife.onlinelibrary.wiley.com/doi/10.1002/wsb.1122

Reusable structure for Ouros:

- lure response belongs in observation/behavior models;
- a larger count at one lure point cannot be interpreted directly as a larger population;
- bait can redistribute detectability and local presence among already-existing individuals;
- different species can respond in opposite directions to the same intervention.

This directly strengthens pass 220: bait is a sampling and behavior pressure first. It is never a population-creation command.

### 2. Attractants can sharply change the number of detections without proving more animals exist

A camera-trap study of mustelids found that bait and scent attractants increased detection probability and image counts. The study is useful precisely because its measured outcomes are observation outcomes, not instantaneous creation of extra animals.

Source: https://pubmed.ncbi.nlm.nih.gov/33266361/

A related Australian study found that bait type and microhabitat affected which taxa were detected and how often, reinforcing that detection is jointly shaped by the animal, attractant and local habitat structure.

Source: https://onlinelibrary.wiley.com/doi/full/10.1111/emr.12444

Ouros consequence:

`OBSERVED_AT_BAIT` must remain downstream evidence. It cannot mutate `ECOSYSTEM_POPULATION_TOTAL` by itself.

### 3. Population size, arrival and departure require explicit demographic inference

USGS describes mark-resight/superpopulation methods that estimate population size, stopover duration, arrival and departure probabilities from encounter histories of marked and unmarked animals.

Source: https://www.usgs.gov/publications/population-size-and-stopover-duration-estimation-using-mark-resight-data-and-bayesian

Reusable structure:

- encounter histories are observations;
- unique identities materially improve inference;
- arrivals/departures are separate latent transitions;
- raw counts are not interchangeable with the underlying population.

For Ouros, the runtime does not need to reproduce Bayesian ecology. The design lesson is the separation of ground truth from what characters can infer. The server may know the finite ledger while Nerea, Ema or a player only sees imperfect samples.

### 4. Ecosystem boundaries can be broad and mobile rather than block-sharp

USGS work on a forest–woodland ecotone documents landscape-scale movement of an ecosystem boundary under drought. The useful lesson is that an ecotone is a real transition region and can shift; it should not be reduced automatically to the boundary between two Minecraft biome IDs.

Source: https://www.usgs.gov/publications/drought-induced-shift-a-forest-woodland-ecotone-rapid-landscape-response-climate

Ouros consequence:

- an authored ecosystem can contain several Minecraft biome tags, landforms and microhabitats;
- a biome-ID edge need not create a new Ouros ecosystem;
- neighboring ecosystems may overlap through an ecotone/transition belt;
- future environmental change can move the ecological boundary without requiring a new world dimension or instant biome swap.

### 5. Feeding can eventually change demography, but that is a long-term ecological transition, not a spawn effect

Milner et al. (2014) reviewed supplementary feeding of wild ungulates and found that under some conditions prolonged feeding can change reproduction, density, behavior, vegetation and disease risk.

Source: https://wildlife.onlinelibrary.wiley.com/doi/10.1002/jwmg.798

This distinction matters. Ouros should allow long-running resource changes to influence future demographic models when the project eventually implements them. It still must not translate `placed food` into `spawn additional Pokémon now`.

A 2024 study of wildlife feeders likewise reports altered use of feeding sites and competition among co-occurring wildlife, including cases where one taxon reduced another taxon's use of the site.

Source: https://wildlife.onlinelibrary.wiley.com/doi/10.1002/jwmg.22644

This supports finite competition for local space/resources instead of independent spawn bonuses for every species.

## Cobblemon cross-check

Current Cobblemon documentation confirms that `spawn_pool_world` files control natural species spawning, rarity/weight and conditions. Conditions can use biome tags, light, coordinates, moon phase, weather-related predicates and other contextual facts. `weightMultiplier` changes relative selection weight under additional conditions.

Sources:

- https://wiki.cobblemon.com/index.php/Spawn_Pool_World
- https://wiki.cobblemon.com/index.php/Spawn_Condition
- https://wiki.cobblemon.com/index.php/Tutorials/Creating_Custom_Spawns

This is valuable projection infrastructure, but its ordinary weighted spawn process is not sufficient to represent a finite authoritative Ouros population. Pass 221 therefore treats Cobblemon spawn eligibility/weight as a candidate-selection/projection input that must be bounded by the Ouros ledger.

A native spawn attempt may request a Fletchling-shaped actor. Ouros must still decide whether an unprojected member/slot of the correct population is available before allowing that request to become a canon-correlated actor.

## Diet-source routing

The user has established that the supplied PGU/PTU-derived project material carries diet information for Pokémon species/types. The repository currently contains source inventories and routing indices, but a code search did not expose a parsed authoritative diet table that can safely be copied into canon from this pass.

The Kairos source index routes world population/ecosystem guidance to pp. 437+ and Pokémon material to Chapter 5. The first Fletchling canon also records supplied PTU 1.05 Pokédex and Caelo location/encounter material as comparative sources.

Pass 221 therefore freezes the data contract but not diet values:

`SPECIES_DIET_PROFILE` must contain exact source provenance and cannot be filled from visual intuition, Pokédex flavor memory or Cobblemon item tags alone.

Candidate fields:

```text
species_id
rules_profile_or_source_id
primary_diet_categories[]
secondary_diet_categories[]
foraging_methods[]
resource_dependencies[]
seasonal_variation[]
known_avoidances[]
confidence
source_pages[]
notes
```

Status of actual Fletchling diet in this pass: UNRESOLVED / SOURCE EXTRACTION REQUIRED.

## Population conservation invariant

The key proposed invariant is:

```text
canonical wild members in ecosystem
= unprojected available members
+ currently projected wild members
+ temporarily reserved/transit members still owned by that ecosystem
```

Rendering operations preserve this total.

The following operations do not change the total by themselves:

- Cobblemon spawn attempt;
- actor unload;
- actor despawn caused by projection/runtime lifecycle;
- player entering/leaving a chunk;
- day/night transition;
- weather change;
- lure placement;
- food consumption;
- camera/observation detection;
- an NPC saying that numbers seem high or low.

Legitimate demographic/world transitions may change ownership/count exactly once:

- verified birth/hatch/recruitment;
- confirmed death under the owning canonical system;
- successful capture/removal from the wild population;
- explicit release/introduction;
- immigration;
- emigration;
- atomic migration transfer between ecosystem ledgers.

The system must never infer one of those transitions from entity rendering state.

## Population identity versus count

Ouros needs both anonymous capacity and persistent identities.

A named or persistent wild individual consumes exactly one member of its population ledger. Its actor may unload and later re-project, but another generic spawn may not reuse that identity simultaneously.

Anonymous members can be represented through reservable slots until persistence requires promotion to a stable individual identity. Promotion must preserve the count: one anonymous slot becomes one identified member; it does not add a Pokémon.

## Ecosystem-scale geography

The intended final map should preserve ecosystem-scale space in-world rather than compress many distinct habitats into a few hundred blocks for variety.

Proposed spatial hierarchy:

```text
REGION
  -> ECOSYSTEM
      -> ECOTONE / TRANSITION BELT
      -> HABITAT PATCH
      -> MICROHABITAT / SITE
```

Minecraft biomes and block palettes are environmental substrate signals inside that hierarchy. They do not automatically create one Ouros ecosystem each.

A single ecosystem can include coastal edge, scrub, path, rocky shelf, small wet patch and settlement-modified habitat if those areas participate in one coherent ecological system. Conversely, two adjacent areas using the same Minecraft biome tag may belong to different authored systems if geography and population flows justify it.

### Marea canon constraint

Current Marea anchors are already CANON-APPROVED and explicitly fixed. Pass 221 does not move Puerto Bruma, Sendero, Loma Clara or Estación Mirador.

Their existing spacing must be treated as the current implemented district skeleton, not proof that the final ecosystem boundary is similarly compact. The ecosystem can extend far beyond these anchors. If later 1:1 design requires moving an anchor or materially rescaling the district itself, that requires the explicit migration process demanded by the existing canon file.

## Relationship to passes 216–220

Pass 216: time/weather/native spawn conditions choose when/where projection is eligible. They do not create population.

Pass 218: migration transfers population membership or transit ownership explicitly. It cannot count the same traveler in origin and destination simultaneously unless a deliberately modeled transit state owns that ambiguity.

Pass 219: a hatch/birth can eventually create a demographic transition, but the existence of a nest or egg observation does not increment the population until the authoritative lifecycle says so.

Pass 220: bait/provisioning can alter local desired distribution, detection, approach and competition. It does not increment abundance. Two lure points compete for a finite set of eligible individuals.

## Story and encounter structures unlocked

### Two Baits, One Population

Two observation teams place different species-appropriate attractants at separated sites. Both teams initially claim increased abundance. Repeated observation reveals that the same finite individuals are redistributing between stations, while some never approach either.

Narrative value: teaches provenance, imperfect detection and finite ecology without a tutorial popup.

### The Biome Edge That Wasn't

A map labels a sharp ecosystem boundary because Minecraft terrain changes palette at a biome edge. Nerea's transects, species continuity and resource evidence suggest a broad transition belt instead. The player helps remap the ecological interpretation without changing blocks merely to make the map agree.

Narrative value: separates cartographic labels from ecological ground truth.

### When the Food Runs Thin

A diet-relevant resource declines across a large habitat patch. Local distribution changes before total abundance necessarily changes. The player can investigate whether animals shifted foraging sites, migrated, experienced reproductive effects or whether the survey method simply stopped detecting them.

Full demographic decline remains unavailable until lifecycle and demographic rules are explicitly authored.

## Rejected shortcuts

- `bait -> spawn bonus`;
- `rare spawn weight -> small canonical population`;
- `common spawn weight -> large canonical population`;
- `visible actors -> ecosystem abundance`;
- `Minecraft biome -> Ouros ecosystem`;
- `chunk unload -> emigration`;
- `entity death callback -> canonical death` without authoritative confirmation;
- `nest found -> population +1`;
- `two lure sites -> two independent spawn pools`;
- filling diet data from species stereotypes instead of the supplied source hierarchy.

## Open research questions

- exact PGU/PTU/Caelo diet record and provenance fields for every species intended for Marea;
- minimum spatial dimensions and travel-time targets for the first 1:1 ecosystem implementation;
- whether the current Marea anchors remain physically plausible once the full ecosystem envelope is built;
- how many simultaneously projected anonymous actors are needed for good presentation without exposing the ledger total;
- how generic Cobblemon spawn attempts should acquire/release ledger reservations;
- how long an unloaded persistent wild actor retains a reserved world location versus returning to ecosystem availability;
- exact transfer semantics for migration, capture, release, birth/hatch and authoritative death;
- how seasonal resource budgets should eventually influence demography without becoming a hidden spawn multiplier.
