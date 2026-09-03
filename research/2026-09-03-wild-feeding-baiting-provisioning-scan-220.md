# Wild feeding, baiting and anthropogenic provisioning — pass 220

Status: RESEARCH / PROVENANCE — NOT CANON
Date: 2026-09-03

## Scope and non-duplication check

The repository was inspected before this pass. Ouros already has separate layers for agriculture and food supply, fisheries, waste, wildlife coexistence, conservation, wild behavior/tolerance, interspecies ecological relations, temporal ecology, migration, nesting, welfare, death/remains and persistent wild encounters.

Most importantly, `design/interspecies-ecological-relations-layer.md` already covers predation, scavenging, resource competition, shared-resource use, trophic evidence and the rule that battle outcomes do not automatically become ecological outcomes.

This pass therefore does not create another trophic-ecology system. It addresses a narrower missing intervention: food or food-like resources made available by humans to wild Pokémon intentionally or accidentally, including observation bait, capture preparation, welfare supplementation, discarded food and repeated provisioning.

## Public material reviewed

### New Pokémon Snap — food as an observation intervention

The official New Pokémon Snap site describes Fluffruit as a tool that can catch a wild Pokémon's attention or let the researcher watch it eat. Nintendo's product page likewise presents throwing a Fluffruit as a way to attract attention while observing wild behavior.

Reusable Ouros lesson: food can alter what becomes observable without implying friendship, ownership, obedience or a universal capture modifier. The observation record must remember that behavior occurred under provisioning rather than pretending it was an undisturbed baseline.

Sources:
- https://newpokemonsnap.pokemon.com/en-us/create-photodex/
- https://www.nintendo.com/us/store/products/new-pokemon-snap-110735/

### Pokémon Legends: Arceus — species-sensitive lure structure

Public gameplay documentation for Pokémon Legends: Arceus describes wild Pokémon approaching preferred foods and being distracted while eating, with different foods preferred by different Pokémon. Ouros should not import those capture-rate values or food tables as PTU mechanics. The reusable structure is narrower: the resource offered can matter to the recipient, and the recipient still has to detect and choose to approach it.

This is useful as a design contrast with a generic `bait attracts Pokémon` flag. In Ouros, species evidence, individual state, context, perception and actual capabilities remain upstream of behavior.

Reference reviewed:
- https://game8.co/games/Pokemon-Legends-Arceus/archives/353693

### Anthropogenic provisioning can change aggregation quickly

A 2024 Journal of Urban Ecology study of American white ibis found that flock density more than doubled during short periods of active human food provisioning. The study did not find that every measured behavior changed in the same way, which is equally important.

Reusable Ouros lesson: provisioning can produce an immediate concentration without proving population growth, permanent habituation or a stable ecological relationship. A feeding event and a long-term site-use shift require different evidence.

Source:
- https://academic.oup.com/jue/article/10/1/juae017/7746142

### Food supplementation has context-dependent ecological and disease effects

A 2024 Journal of Animal Ecology commentary on broad-scale citizen-science work describes anthropogenic food supplementation as capable of changing nutritional intake, inter- and intraspecific interactions and disease-transmission dynamics. It also stresses that outcomes vary through time and space.

Reusable Ouros lesson: do not encode `feeding = beneficial` or `feeding = harmful` as a universal rule. Persist the intervention, exposure and observations; later evidence can support a local consequence.

Sources:
- https://besjournals.onlinelibrary.wiley.com/doi/abs/10.1111/1365-2656.14208
- https://pubmed.ncbi.nlm.nih.gov/39482745/

### Feeding stations can create crowding and cross-species contact

A peer-reviewed review of anthropogenic bird feeding identifies risks associated with repeated congregation, interspecific mixing, contamination and competition at feeding stations.

Reusable Ouros lesson: a food source can become a shared focal point. Multiple Pokémon appearing around it must remain independent actors unless a separate collective/relationship record is justified.

Source:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5882997/

### Human food can condition wildlife toward people and infrastructure

The U.S. National Park Service describes food conditioning as wildlife learning to seek human food and notes that intentional feeding and unsecured waste can alter where animals spend time and how they approach people. A USGS raven study similarly found that anthropogenic food subsidies influenced movement and landscape use without making animals exclusively dependent on subsidized landscapes.

Reusable Ouros lesson: repeated provisioning may become a causal candidate for altered tolerance, approach distance or site use, but it needs history and evidence. An individual accepting food once does not become tame.

Sources:
- https://www.nps.gov/subjects/watchingwildlife/animals.htm
- https://www.usgs.gov/publications/influence-anthropogenic-subsidies-movements-common-ravens

### PTU community signal — capture does not need to begin with combat

Public PTU community discussion includes tables using social approaches to wild Pokémon instead of requiring every capture attempt to become a full battle. This is table practice rather than rules authority, but it reinforces the value of a non-combat interaction layer before BattleSpec creation.

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/xgemb5
- https://www.reddit.com/r/PokemonTabletop/comments/1fttnse/pokemon_catching/

## PTU / Kairos cross-check

The project Kairos index routes Skills/Edges/Features to Chapter 3, Pokémon management to Chapter 5, capture to pp. 365–366, playing/combat to Chapters 6–7 and Items/Gear/Crafting to pp. 495+ of the supplied Kairos core compilation. Those references are routing aids, not automatic Ouros acceptance.

Public PTU 1.05 text also confirms that food can have explicit mechanics. Snacks, including Berries, can grant Digestion/Food Buff effects; Refreshments have their own consumption timing and healing effects; Chef features create further food mechanics. Therefore the narrative layer must never invent a generic food effect merely because an object is edible.

For pass 220 the rule is:

- ordinary world food/resource availability may influence authored wild behavior only through the Ouros behavior/ecology layer;
- a PTU Food Buff, Berry, Refreshment, Chef product or other mechanically meaningful Item must use its exact verified rule and engine contract;
- a capture modifier from feeding cannot be imported from Pokémon video games into PTU;
- if Kairos/Caelo adds an applicable rule, it must be separately verified and recorded before activation.

Exact source questions still requiring direct rule audit include wild-target use of edible Items, action/range requirements for offering or throwing them, whether any Feature/Edge modifies wild feeding/capture, and whether an Item can legally be consumed by an unwilling or uncontrolled wild target.

## Proposed data: `WILD_PROVISIONING_EVENT`

Proposed, not canon-approved.

```yaml
wild_provisioning_event:
  event_id: null
  site_ref: null
  actor_ref: null
  resource_ref: null
  resource_class: NATURAL_FOOD | TRAINER_ITEM | PREPARED_FOOD | WASTE | UNKNOWN
  intent: OBSERVATION | LURE | CAPTURE_PREPARATION | WELFARE | DISPOSAL | ACCIDENTAL | UNKNOWN
  placed_at: null
  quantity_band: null
  retrieval_or_cleanup_due: null
  target_claim_ref: null
  observed_recipient_refs: []
  response_observation_refs: []
  leftovers_state: null
  provenance_refs: []
  mechanics_refs: []
```

`target_claim_ref` is deliberately only a claim. Putting food out “for Fletchling” does not make Fletchling the recipient.

## Proposed data: `PROVISIONING_RESPONSE_OBSERVATION`

```yaml
provisioning_response_observation:
  observation_id: null
  event_ref: null
  subject_ref: null
  evidence_quality: null
  trainer_distance: null
  trainer_visible: null
  response: IGNORED | ORIENTED | APPROACHED | INSPECTED | CONSUMED | CARRIED | GUARDED | DISPLACED | WITHDREW | ALERTED | UNKNOWN
  latency_band: null
  other_actor_refs: []
  disturbance_refs: []
  mechanics_resolution_ref: null
  interpretation_refs: []
```

This keeps observed response separate from interpretation. `CONSUMED` does not mean befriended. `APPROACHED` does not mean consent to capture. `GUARDED` does not prove territoriality outside that event.

## Provisioning decision boundary

For a wild Pokémon already present in authoritative world state:

```text
species/population evidence
+ persistent individual state/history
+ site/time/human-pressure context
+ provisioning-event properties
+ whether the resource was perceived
+ actual Pokémon capabilities
+ observed Trainer position/actions
+ verified PTU effects, if any
-> legal behavior options
-> tactical/behavior selection
-> authoritative consequence
```

Generic Cobblemon spawn eligibility stays native to Cobblemon. A food marker must not force-spawn a canonical individual or duplicate a persistent Pokémon merely because the resource exists.

## Evidence and habituation

Repeated provisioning can support a future habituation or food-conditioning claim only when history supports it. Useful evidence includes repeated approach to the same site, reduced avoidance specifically around provisioners, changed activity window, repeated aggregation, food-seeking near infrastructure or altered response after the resource disappears.

Competing explanations must remain available: ordinary habitat use, another natural resource, weather, migration, nesting, observation bias or individual variation.

A single successful feeding event cannot write a permanent tolerance modifier.

## Welfare boundary

Supplementary feeding may sometimes be justified by authored welfare or conservation context, but it is not automatically benevolent. The project must distinguish emergency care from routine habituation, and must preserve who authorized the intervention, what resource was used and when reassessment occurs.

Feeding a wild Pokémon does not grant ownership, loyalty, friendship, command authority or capture consent.

## Research-method boundary

Provisioned behavior is valid evidence, but it is evidence under an intervention. Nerea or another field researcher should be able to distinguish:

- undisturbed observation;
- passive observation near existing anthropogenic food;
- deliberate baited observation;
- welfare supplementation;
- accidental food exposure.

This prevents a researcher from baiting a Pokémon into a site and later publishing the baited location as its ordinary habitat use.

## Canon status

CANON-APPROVED constraints preserved:

- existing Marea geography, institutions and residents are unchanged;
- the first Sendero Fletchling blueprint and identity are unchanged;
- no new wild species/population is introduced;
- Cobblemon retains generic spawn/environment projection responsibilities without battle authority;
- AutoPTU remains authoritative for PTU mechanics;
- feeding does not establish ownership or friendship.

PROPOSED:

- `WILD_PROVISIONING_EVENT`;
- `PROVISIONING_RESPONSE_OBSERVATION`;
- evidence-backed food-conditioning/habituation consequences;
- methodological separation between baited and unbaited observations.

UNCERTAIN:

- which ordinary foods are ecologically meaningful to which Ouros populations;
- whether Marea institutions permit research baiting and under what authorization;
- exact PTU/Kairos rules for offering/throwing food to wild Pokémon;
- mechanically meaningful edible Item coverage in AutoPTU;
- whether the canonical Sendero Fletchling has any authored food preference.

## Design outcome

Human-provided food becomes a traceable intervention rather than a magic friendliness button. It can create useful observation, capture preparation, welfare, cleanup and coexistence stories while preserving individual agency, scientific provenance and PTU authority.