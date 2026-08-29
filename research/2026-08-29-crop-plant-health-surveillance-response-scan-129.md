# Ouros Narrative Research — Crop and Plant Health Surveillance, Response & Recovery — Pass 129

Status: RESEARCH ONLY. Provenance and design evidence. Not Ouros canon.
Date: 2026-08-29

## Research question

What reusable structures can make crop, orchard, garden and managed-plant problems persistent and investigable without turning Food/Agriculture into repetitive farm chores, treating every Bug Pokémon as a pest, importing real-world phytosanitary law, or inventing PTU environmental/status mechanics?

The useful gap is narrower than agriculture itself. Ouros already models agricultural sites, cultivation cycles, food batches, ecology, conservation, water dependencies, pollution, weather, batches and institutional handoffs. What is missing is a persistent plant-health episode that can preserve observations, samples, diagnosis, uncertain extent, actions, follow-up and recovery over time.

## Existing Ouros boundaries checked before research

The current `food-agriculture-hospitality-layer.md` already owns agricultural sites, cultivation cycles, harvest events, food provenance and broad disruptions. It explicitly allows current problems and relevant condition IDs, but it does not define a longitudinal plant-health investigation or response workflow.

`batch-traceability-recall-quarantine-extension.md` owns post-distribution problems affecting products, batches and units after production/distribution. A diseased orchard row or uncertain crop condition before harvest belongs upstream of that layer. If affected produce later enters storage or distribution, Batch Traceability can receive a handoff rather than having plant health duplicate recall logic.

Ecology and Conservation remain owners of wild populations, habitat relationships and stewardship. Water, Weather, Pollution, Air Quality and Infrastructure remain owners of their own environmental observations and causes. Plant-health continuity may consume those facts but must not rewrite them.

## Pokémon source: Kalos Berry fields

Source: https://bulbapedia.bulbagarden.net/wiki/Berry_fields_%28Kalos%29
Source: https://bulbapedia.bulbagarden.net/wiki/Berry

Pokémon X/Y's Berry-field loop separates several local care conditions: soil moisture, weeds, pest Pokémon, plant growth stage and eventual harvest. The important reusable lesson is not the exact timing or yield formula. It is that a cultivated plot can hold several independent condition tracks, and a visible problem can be local to one plant or row rather than automatically applying to the whole agricultural site.

The game also turns some pest appearances into battles. Ouros should retain only the high-level possibility that a cultivation problem can intersect a wild Pokémon encounter. It must not infer that any wild Pokémon found near a crop caused plant damage, and it must not reproduce the X/Y rule that battle automatically removes the pest condition.

Ouros transformation:
- preserve plot/row/plant scope separately from site scope;
- record weeds, visible feeding damage, discoloration, wilting or other authored observations as observations rather than diagnoses;
- let a Pokémon encounter coexist with a crop problem without declaring causality;
- make post-action observation necessary before claiming that a measure worked;
- never import game-specific growth timers or yield formulas as PTU rules.

## Pokémon source: The Apple Corp!

Source: https://bulbapedia.bulbagarden.net/wiki/EP179

This anime episode uses an orchard where missing fruit is initially attributed to the wrong subject. The eventual explanation connects hungry wild Pokémon to a reduced wild food supply, and the resolution changes the relationship between the orchard and those Pokémon.

Reusable structure:
1. visible crop loss;
2. premature attribution;
3. investigation of who or what is actually taking produce;
4. upstream ecological pressure;
5. a mitigation that changes coexistence rather than simply removing a subject.

Ouros transformation:
- `FRUIT_MISSING` is an observation, not a cause;
- a sighted Pokémon is not automatically the damaging individual;
- a crop-loss case may hand off to Settlement/Wild Pokémon Coexistence or Ecology when the underlying driver is food availability or habitat pressure;
- a negotiated or ecological mitigation can be valid if current canon and world state support it;
- no distinctive characters, dialogue or plot resolution are copied.

## Pokémon source: Three Sides to Every Story!

Source: https://bulbapedia.bulbagarden.net/wiki/DP137

The episode presents a family orchard as a lived place with temporary responsibility while usual operators are absent. The useful lesson is continuity of stewardship: the person currently observing a problem may be an acting operator rather than the person with long-term knowledge of the site.

Ouros transformation:
- preserve `observed_by`, `site_operator`, `acting_steward` and `historical_knowledge_holder` as potentially different roles;
- allow a short-term caretaker to file a valid observation without implying they know historical baseline conditions;
- let later comparison with previous seasons or previous operators change the interpretation of a current symptom.

## Public Pokémon Tabletop campaign anecdote

Source: https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5/pokemon_encounters_a_storytelling/

A public GM discussion describes wild encounters as small ecological stories: a berry tree defended by a flock, separated Pokémon reunited without mandatory combat, and creatures using the environment in recognizable ways.

Reusable lesson: wild encounters near managed land work better when they have local motives and ecological context instead of functioning only as random combat slots.

Ouros transformation:
- plant-health investigation can expose a habitat edge, nesting site, feeding route or displaced population;
- that discovery should create an Ecology/Coexistence edge rather than making the agricultural layer decide wildlife policy;
- combat remains optional unless the actual world state and actors make it necessary.

## Recent fan-community worldbuilding signal

Source: https://www.reddit.com/r/PokeMedia/comments/1vxgbvr/all_about_berries/
Source: https://www.reddit.com/r/PokeMedia/comments/1gq4h0u

Recent public Pokémon roleplay/worldbuilding discussions in 2024–2026 portray berry orchards as places where individual Pokémon participate in pruning, harvest, ripeness observation or pest response, and where growers compare cultivar behavior and local climate suitability.

These posts are fan-created and non-authoritative. Their value is structural only: agricultural work becomes richer when individual Pokémon have documented jobs, experience and limitations rather than species-wide automatic competencies.

Ouros transformation:
- any Pokémon work role must reference the existing Pokémon Work/Agency systems;
- a Pokémon can contribute an observation because the world has established a trained role or specific demonstrated behavior;
- species identity alone never grants diagnosis, pesticide competence, crop-disease detection or universal pest-control capability.

## IPPC surveillance architecture

Source: https://ippc.int/fr/archive-old-pages/phytosanitary-system/surveillance/
Source: https://www.ippc.int/en/centre-of-excellence/framework/list

The International Plant Protection Convention separates several surveillance purposes. Detection surveys ask whether a target is present. Delimiting surveys establish the boundaries of an affected area. Monitoring surveys track characteristics of a known population or condition over time.

This distinction is highly reusable for narrative provenance because the same field visit should not silently answer every question.

Ouros transformation:
- `DETECTION_SCOPE` asks whether an authored plant-health subject is present;
- `DELIMITATION_SCOPE` estimates current affected extent from bounded observations;
- `MONITORING_SCOPE` follows an already established condition through time;
- scopes must carry timestamps, methods and uncertainty;
- a negative observation at one plot does not prove absence everywhere;
- a delimitation product is an interpretation derived from observations, not a direct measurement of every cell.

No IPPC legal status, regulated-pest list, national authority, trade requirement or mandatory control power becomes Ouros canon from these sources.

## Diagnostic provenance

Source: https://www.ippc.int/en/commission/standards-committee/technical-panels/technical-panel-diagnostic-protocols/

IPPC diagnostic work emphasizes reliable identification, method selection and method characteristics such as sensitivity, specificity and reproducibility. The reusable narrative lesson is that diagnosis is a separate evidence-producing act. Symptoms and field signs can motivate testing without being equivalent to an identified cause.

Ouros transformation:
- visible symptoms remain `condition_observation` records;
- samples retain collection site, time, collector, custody and method references where relevant;
- diagnosis records identify exactly what claim was tested and what method family produced the result;
- inconclusive, conflicting and revised diagnoses remain valid historical states;
- the generator may not invent a laboratory capability or diagnostic method simply because a mystery needs one.

## FAO field-survey and early-warning material

Source: https://www.fao.org/family-farming/detail/en/c/1754882/
Source: https://www.fao.org/one-health/highlights/early-warning-systems-for-plant-health/en

Recent FAO material illustrates a sequence from field observation through sampling/diagnostics to mapped surveillance and repeated monitoring. It also shows why offline/local observations and later aggregation can coexist, and why damage level, organism life stage and intervention history are separate fields rather than one severity number.

Reusable design lesson:
- field records can arrive asynchronously;
- a map can be revised as observations are uploaded or verified;
- intervention history must remain attached to the affected scope so apparent improvement can be interpreted correctly;
- a later confirmed identification should not rewrite what observers actually knew at the earlier time.

Again, real-world legal requirements and control programs are provenance only.

## High-level narrative structures extracted

### 1. Symptom → hypothesis → sample → diagnosis → revised scope

A crop problem should rarely begin with omniscient causality. It begins with what someone actually saw. Multiple hypotheses can coexist until evidence narrows them.

### 2. The wrong culprit can be plausible without being malicious

Missing fruit, holes, wilt or discoloration can be attributed to a visible Pokémon, weather, irrigation, soil, disease, contamination or handling. A witness may be reasonable and still wrong.

### 3. Scope is a story variable

One tree, one row, one greenhouse bay, one orchard block and an entire valley are materially different claims. Players can discover that an initially broad fear is localized, or that an apparently isolated problem has a second site.

### 4. Response and effectiveness are separate

Pruning, isolation, changed watering, temporary access restrictions, altered harvest decisions, wildlife mitigation or other authored actions do not become successful merely because they occurred. Follow-up evidence decides whether the condition changed.

### 5. Recovery can be asymmetric

Visible symptoms may stop while yield remains reduced. A plot may recover before a nursery source is cleared. A harvest can fail while the perennial plants survive. A site can resume ordinary work while an investigation remains open.

### 6. Agriculture can reveal larger world systems

A field problem can reveal irrigation failure, upstream pollution, changed pollinator activity, habitat loss, contaminated planting material, a storage/distribution concern or a social conflict over wildlife. The plant-health layer should hand off rather than absorb those systems.

## Proposed Ouros data distinctions

These are research-derived design candidates, not canon facts:

- plant-health episode;
- affected site and bounded plot scope;
- condition observation;
- symptom/sign vocabulary linked to source and timestamp;
- sample record and custody lineage when applicable;
- diagnostic request/result;
- detection survey;
- delimitation survey;
- monitoring survey;
- affected-scope revision;
- competing cause hypotheses;
- plant-health action;
- action authority/mandate reference when required;
- post-action observation;
- recovery checkpoint;
- harvest/yield consequence handoff;
- Ecology/Coexistence/Water/Weather/Pollution/Batch handoffs.

## Guardrails

Do not infer:
- `POKEMON_PRESENT` therefore `CROP_DAMAGE_CAUSED_BY_POKEMON`;
- Bug Type therefore pest;
- Grass Type therefore plant-health expert;
- Poison Type therefore contamination;
- a damaged plant therefore infection;
- a visible fungus therefore a specific disease;
- one positive sample therefore every field is affected;
- one negative sample therefore the site is clear;
- treatment applied therefore condition resolved;
- rainfall after wilt therefore plants recovered;
- harvest destroyed therefore perennial planting dead;
- nearby pollution source therefore confirmed cause;
- battle victory therefore infestation removed;
- capture therefore a plant-health response was authorized or effective.

## PTU / Caelo mechanical boundary

The standing project source scan supports persistent campaigns, jobs, social play, wild encounters and exact environmental mechanics when a governing source defines them. Toxic Ravine remains a precedent for authored location mechanics, not a generic authority to invent spores, pollen, crop toxins or exposure rules.

This research does not establish:
- generic spore clouds;
- pollen accuracy or LoS penalties;
- plant-disease statuses;
- poison/exposure from diseased crops;
- infectious spread between tactical cells;
- wind-driven disease phases;
- automatic Grass/Bug/Poison Type interactions;
- universal pruning, diagnosis or treatment Moves;
- universal pest-control Abilities;
- Trainer Feature authority over agricultural quarantine;
- capture/removal as guaranteed mitigation.

Any tactical version using those effects must depend on the exact capability families and a governing rule/contract.

## Candidate encounter translations

### Orchard Survey Perimeter

Narrative premise: a survey team needs access to a bounded orchard section after conflicting observations.

Full form could include protected survey lanes, active team withdrawal, mobile wild Pokémon, reactions at row crossings, perhaps an exact governed environmental effect if one exists.

Reduced form: survey work pauses first. Staff, samples, tools and noncombatant subjects leave BattleSpec. AutoPTU receives a static reviewed orchard perimeter with explicit combatants. Winning only secures immediate access; it does not diagnose the crop or delimit the episode.

### Nursery Block Diversion

Narrative premise: a controlled planting-material block must remain undisturbed while an unrelated hostile encounter occurs nearby.

Full form could require protected-object objectives, forced movement, restricted cells, reaction ordering and tactical policy.

Reduced form: the controlled block is physically outside the tactical arena. Custody and access are resolved in world state. Battle outcome cannot clear planting material or expand/reduce the affected scope.

### Pollinator Edge Reinspection

Narrative premise: a repeat plant-health observation overlaps a habitat edge used by wild Pokémon, and the team must inspect the site without converting wildlife presence into guilt.

Full form could require moving wildlife, nonlethal objectives, environmental zones and objective-aware AI.

Reduced form: Ecology/Coexistence handles wildlife movement first. Plant-health personnel withdraw. AutoPTU resolves a conventional encounter on stable geometry. The later inspection remains a separate world-state event.

## Canon questions opened, not answered

- Which Ouros regions have formal crop/plant-health services, if any?
- Which growers rely on guilds, cooperatives, research institutions, local experts or informal knowledge instead?
- What plant/crop categories are established in each region beyond already canonical Berries/materials?
- What diagnostic technologies exist regionally?
- Who can authorize access restrictions, destruction, isolation or movement controls when those powers exist?
- Are any historical crop-health episodes already part of regional canon?
- Which Pokémon individuals have trained agricultural or diagnostic roles?
- What records are private, commercial, public or scientific?
- How does a disputed diagnosis get reviewed?

No answer is established by this research pass.

## Source-use statement

All external material above is used only for high-level structures, evidence architecture and transformed narrative patterns. No protected dialogue, distinctive characters, complete plots, exact game formulas, real-world legal powers or regulatory procedures are copied into Ouros canon.
