# Wild nesting, parental care and disturbance scan — Pass 234

Status: RESEARCH / PROVENANCE. Not Ouros canon.
Date: 2026-09-03

## Research question

How should Ouros model wild Pokémon nesting, juvenile dependence, parental provisioning, nest defence, human disturbance and abandonment risk without importing captive breeding mechanics or turning every nest contact into a battle?

This pass is intentionally separate from `design/breeding-eggs-nursery-lineage-layer.md`, which governs persistent Eggs, custody, nursery services, mechanically resolved hatching and institutional juvenile care. The subject here is wild ecology.

## Existing Ouros constraints checked

Relevant internal material inspected before writing:
- `CURRENT_FOCUS.md`;
- `design/ecology-development-program.md`;
- `design/global-species-interaction-graph.md`;
- `design/breeding-eggs-nursery-lineage-layer.md`;
- `design/ouros-source-authority-and-species-policy.md`;
- `design/engine-readiness-snapshot-pass-226.md`;
- recent ecological pulse, observation/intervention and interspecies-information passes;
- current Marea canon and the global-worldgen migration constraint through the repository tree and recent history.

The ecology programme explicitly requires nesting, juveniles and parental behaviour, human disturbance, succession/recovery, population state and deterministic fixtures. Wild nesting therefore belongs in the active workstream rather than the general breeding subsystem.

## Public source set

### Official Pokémon species evidence

1. Pokémon.com — Mandibuzz Pokédex
   https://www.pokemon.com/es/pokedex/mandibuzz

   Reusable evidence:
   - explicit provisioning of Vullaby;
   - prey can be transported to a nest;
   - nest location is therefore an ecological centre that changes adult foraging routes and prey pressure.

   Ouros lesson:
   parental care can alter trophic pressure and travel radius. A nesting adult should not be simulated as an ordinary free-ranging individual with identical priorities.

2. Pokémon.com — Bombirdier Pokédex
   https://www.pokemon.com/it/pokedex/bombirdier

   Reusable evidence:
   - explicit transport of food to a nest;
   - nest provisioning can be represented through repeated resource-transfer behaviour rather than a generic `parental=true` flag.

3. Pokémon.com — Leavanny Pokédex
   https://www.pokemon.com/us/pokedex/leavanny

   Reusable evidence:
   - strong protective response toward young Pokémon is explicit species identity;
   - defence of juveniles can cross species boundaries.

   Ouros lesson:
   `CARES_FOR` and `DEFENDS_YOUNG` cannot be assumed to mean genetic parentage. Caregiver, juvenile and parentage relationships must remain separate facts.

4. Pokémon.com — Kangaskhan Pokédex
   https://www.pokemon.com/br/pokedex/kangaskhan

   Reusable evidence:
   - close physical juvenile association is part of species identity;
   - protective/care behaviour can remain attached to a mobile adult rather than a fixed nest site.

   Ouros lesson:
   the system needs both site-centred dependency and caregiver-centred dependency.

### PTU community / campaign evidence

5. r/PokemonTabletop — “Pokemon Encounters (A Storytelling)” (17 March 2023)
   https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5/

   Reusable encounter structures reported by GMs/players:
   - a nesting pair occupies a human structure and attacks close approaches, with relocation as the actual solution;
   - a flock protects a resource/home tree;
   - interspecies encounters can be solved through observation or reunion instead of combat;
   - a visible Egg can reward curiosity without making capture the only interaction verb.

   Ouros lesson:
   a nest encounter is stronger when the objective is spatial or ecological: reduce disturbance, relocate safely, restore access, observe, wait, escort or change human behaviour. “Defeat the parent” should be only one possible escalation and often an ecologically bad one.

6. r/PokemonTabletop — “Catching Pokemon” (30 December 2022)
   https://www.reddit.com/r/PokemonTabletop/comments/zyqpgz/

   Reusable structure:
   - helping a wild Pokémon in danger or finding an abandoned nest can lead to later voluntary association/adoption-style outcomes in campaigns.

   Ouros lesson:
   rescue does not automatically grant ownership. Any later persistent relationship requires an explicit world event and must obey Ouros capture/ownership rules.

### Pokémon Ranger mission structure

7. Pokémon Ranger — Manaphy Egg mission summary
   https://www.psypokes.com/ranger/manaphy.php

   Reusable structure:
   - an Egg can be a protected object moving through a route;
   - obstacles and encounters can be framed around recovery/transport rather than possession or ordinary trainer combat;
   - the protected object can remain outside ordinary battle state.

   Ouros lesson:
   when a wild-care story requires transport, the Egg/juvenile should remain world-state unless the active rules profile explicitly supports it as a tactical participant.

### Real ecology analogues

8. U.S. Geological Survey — ground-nesting marine birds and human disturbance
   https://www.usgs.gov/publications/ground-nesting-marine-birds-and-potential-human-disturbance-glacier-bay-national-park

   Reusable ecological pattern:
   - nesting sites can be highly vulnerable to human access;
   - repeated disturbance can reduce parental attendance and reproductive success;
   - management can protect breeding areas by changing visitor access rather than manipulating the animals directly.

9. Oxford Academic, Ornithology — facultative nest vigilance under perceived risk
   https://academic.oup.com/auk/article/132/2/359/5149036

   Reusable ecological pattern:
   - defence/vigilance can scale with perceived threat rather than remaining permanently maximal;
   - costly defensive behaviour can turn on and off with local risk.

10. Quarterly Review of Biology — risks and rewards of nest defence by parent birds
    https://www.journals.uchicago.edu/doi/10.1086/415838

    Reusable ecological pattern:
    - nest defence intensity can depend on offspring vulnerability, accessibility, parent capability and risk to the adult;
    - parental defence is therefore a decision under competing pressures, not an unconditional aggression switch.

11. U.S. Geological Survey — parental activity and nest predation
    https://www.usgs.gov/publications/nest-predation-increases-parental-activity-separating-nest-site-and-parental-activity

    Reusable ecological pattern:
    - nest-site quality itself can strongly affect predation risk;
    - increased parental movement does not alone explain all predation outcomes.

    Ouros lesson:
    nest quality, cover and location must be first-class habitat facts. Do not calculate nesting outcome from caregiver activity alone.

12. U.S. Geological Survey — disturbance responses in nesting seabirds
    https://www.usgs.gov/publications/small-boats-disturb-fish-holding-marbled-murrelets

    Reusable ecological pattern:
    - disturbance can produce alarm, reduced attendance and, at higher pressure, abandonment.

    Ouros lesson:
    repeated approaches should accumulate disturbance state even when no battle starts.

## High-level synthesis for Ouros

### 1. Nest state is more than an Egg coordinate

A useful wild nesting record needs:
- site suitability and cover;
- caregiver identities or candidate caregiver roles;
- dependent juvenile/Egg identities when persistent;
- stage of dependence;
- provisioning requirements;
- vigilance/defence pressure;
- disturbance history;
- predator pressure;
- human-route overlap;
- abandonment/relocation pressure;
- observation confidence.

### 2. Caregiver role is separate from parentage

Official Pokémon material supports nontrivial care behaviour, including protection of young Pokémon without an explicit genetic relationship.

Required relationship distinction:
- `PARENT_OF` — only when mechanically/canonically established;
- `CARES_FOR` — observed care relationship;
- `PROVISIONS_FOR` — repeated resource delivery;
- `DEFENDS_YOUNG` — protective behavioural relationship;
- `NESTS_AT` — site occupancy;
- `DEPENDENT_ON` — juvenile dependence;
- `MOVED_NEST_TO` — relocation event.

Do not infer one edge from another.

### 3. Defence should be risk-sensitive

Candidate defence pressure:

```text
species protective prior
+ individual condition/capabilities
+ dependent-young vulnerability
+ distance to nest/young
+ available escape/relocation options
+ recent disturbance
+ predator/Trainer threat evidence
+ cover/site accessibility
+ alternative caregiver presence
= candidate protective intent
```

Possible intents:
- remain concealed;
- watch;
- alarm;
- shadow intruder;
- display/threaten;
- block access;
- move juveniles;
- relocate nest;
- flee with dependent young;
- engage;
- disengage after separation is restored.

These remain ecological intentions, not PTU Status Afflictions.

### 4. Repeated disturbance matters even without combat

One accidental approach should not equal abandonment.

The ecological ledger needs accumulated disturbance with decay. Repeated route traffic, construction, harvesting, observation pressure, failed relocation attempts or frequent player visits can increase local nest risk and change attendance/visibility.

### 5. Nesting changes resource and predator networks

Provisioning adults can:
- increase visits to specific feeding sites;
- change foraging time windows;
- increase prey/resource extraction near a route;
- expose nest location through repeated travel;
- attract scavengers/predators;
- increase territorial overlap with neighbours.

The global species interaction graph therefore needs nesting-context modifiers rather than a disconnected breeding table.

### 6. Abandonment is a consequential ecological result

A nest can become:
- active;
- temporarily unattended;
- threatened;
- relocating;
- abandoned;
- failed;
- successfully fledged/independent;
- unknown/unconfirmed.

Do not infer death, injury or hatch failure from absence alone. Those require evidence or governing mechanics.

## Provenance grading recommendations

Use `PROVENANCE_EXPLICIT` only where official Pokémon material directly states species-specific care/nest behaviour.

Use `BIOLOGICAL_ANALOGUE` for general nest-defence, disturbance and parental-investment mechanisms until Ouros reviews a species/context implementation.

Use `OUROS_AUTHORED` for local nesting-site and management scenarios after worldgen/habitat compatibility is checked.

## Worldgen dependency

Do not freeze Marea nesting coordinates, nest substrate, exact resident species or breeding-season windows until the global world substrate is generated and the selected location is checked against actual Minecraft biome IDs/tags, terrain, cover, structures and Cobblemon native spawn envelopes.

Legacy Marea coordinates remain migration-sensitive under the global-world-generation programme.

## Mechanical boundary

Persistent nesting, care, disturbance accumulation, provisioning, abandonment pressure, relocation intent, observations and spawn/activity projection are Ouros world-state responsibilities.

If protective behaviour enters structured combat, AutoPTU becomes authoritative.

Current live AutoPTU-Java head checked for this pass:
- `21e0b02e5ff17132f3a7ed04007784884323df12`
- `Add stateful movement landing consequence executor (#334)`.

This commit adds a server-authoritative executor for ordered movement-landing consequences, status application through the existing status-prevention pipeline, semantic trap events and trap consumption. It strengthens a bounded trap/landing slice. It does not verify the complete terrain/hazard family, generic escort objectives, parental AI, interception breadth or full tactical policy.

Python AutoPTU remains the read-only oracle. No change to Python authority is proposed here.

## Design consequences

The next design artifact should define a wild-nesting lifecycle with explicit caregiver/dependent/site state, disturbance accumulation, provisioning, relocation and AutoPTU handoff rules.

A Marea fixture should remain species-agnostic until worldgen compatibility is known, while still testing:
- route pressure near a nesting site;
- evidence of provisioning;
- escalating vigilance;
- a noncombat intervention;
- optional simple battle fallback;
- persistent post-intervention consequence.
