# Pokémon Social Learning & Behavioral Traditions Research — Pass 125

Status: research/provenance only. Nothing in this file is established Ouros canon or a PTU/Caelo rules source.

## Why this pass exists

The repository already has strong layers for persistent wild collectives, migration, diel activity, soundscapes, field signs, urban wildlife, Pokémon agency, taxonomy and research. The remaining gap is how a population can acquire and preserve a learned behavior that is not merely species-typical, genetically fixed, a mechanical Ability, or the private habit of one individual.

This pass researches a conservative architecture for:

- individual innovation;
- social learning;
- local behavioral traditions;
- population-specific repertoires;
- long-term memory of learned solutions;
- transmission between experienced and naïve individuals;
- disruption, disappearance and reappearance of traditions;
- distinguishing environmental convergence from social transmission;
- distinguishing learned behavior from PTU mechanics.

Primary design rule: repeated behavior is not enough to establish a social tradition. The system needs evidence that a behavior is learned socially and persists beyond one individual or one moment.

## Internal overlap review

Before external research, the current `design/`, `research/` and `proposals/` inventories were reviewed.

Relevant existing authorities:

- `design/wild-collective-agency-layer.md` owns persistent groups, group identity, evidence-based leadership, home range and collective knowledge.
- `design/pokemon-agency-partnership-release-layer.md` owns persistent individual Pokémon identity, partnership and observed cooperation/refusal.
- `design/soundscapes-acoustic-ecology-layer.md` owns acoustic observations and call profiles.
- `design/language-translation-symbolic-systems-layer.md` owns language/symbol interpretation and translation claims.
- `design/diel-activity-circadian-rhythms-layer.md` owns time-of-day activity patterns.
- `design/wildlife-migration-stopovers-corridors-layer.md` owns population migration episodes and route history.
- `design/field-signs-tracking-spoor-layer.md` owns physical signs and route hypotheses.
- `design/urban-wildlife-synanthropy-coexistence-layer.md` owns habituation, attractants and repeated urban behavior.
- `design/science-research-discovery-layer.md` owns observations, hypotheses and evidence.

No current layer owns population-specific socially learned behavior as a first-class persistent object.

## Source 1 — Chatot: a direct Pokémon precedent for shared learned vocal behavior

Source: Pokémon official Pokédex, Chatot.

URL: https://www.pokemon.com/us/pokedex/chatot

Useful high-level facts:

- Chatot can learn human words.
- When Chatot gather, the group can converge on the same saying.
- Chatot can imitate the cries of other Pokémon.

Reusable structure:

A local group may share a learned vocal repertoire that differs from another group of the same species. Repeated recordings can document change over time.

Ouros transformation:

- local Chatot groups may become candidates for `VOCAL_REPERTOIRE_REVISION` records;
- a repeated phrase can be documented as an observed repertoire item without assuming full human-language competence;
- a phrase can spread, disappear or change without changing species, Type, Move list or Ability;
- a recording can preserve an older version after the current group changes.

Hard guardrail:

Chatot flavor does not grant Chatter, Mimic, language fluency, translation ability, social Skill ranks, command authority or any other PTU effect unless the governing rules explicitly provide it.

## Source 2 — Passimian: social organization is evidence, not automatic culture

Source: Pokémon official Pokédex, Passimian.

URL: https://www.pokemon.com/us/pokedex/passimian

Useful high-level facts:

- Passimian can form organized groups.
- A boss selects a hunting party.
- Food can be shared with the larger group.
- Hard berries can be used in battle behavior.

Reusable structure:

Species-grounded social organization can make social transmission plausible, but organization itself does not prove a learned tradition.

Ouros transformation:

A Passimian group can have a persistent collective identity and observed roles under Wild Collective Agency. A distinct local berry-handling or route-selection practice becomes a behavioral-tradition candidate only if evidence shows transmission and persistence.

Hard guardrail:

Do not infer `Pack Mon`, tactical bonuses, Receiver behavior, leadership Skill ranks, shared initiative, synchronized battle AI or a culture label from the Pokédex description alone.

## Source 3 — PTU GM advice: Pokémon should exist as characters outside battle

Source: Pokémon Tabletop RPG, “GM Advice: Your First PTU Session.”

URL: https://pokemontabletop.com/gm-advice-your-first-ptu-session/

Relevant design lessons:

- PTU explicitly recommends establishing Pokémon as characters rather than only battle tools.
- Wild Pokémon interactions can be non-violent.
- Befriending can sometimes occur without a fight.
- Wild Pokémon may have reasons to flee instead of fighting until one side is fully defeated.

Ouros transformation:

Behavioral traditions should primarily live in overworld observation, ecology and relationship state. A learned foraging technique, call repertoire or crossing behavior should not require a battle to become meaningful.

Encounter consequence:

A reduced implementation can preserve the entire narrative premise by observing or protecting a learned behavior outside AutoPTU, then opening a conventional static battle only if a separate confrontation occurs.

## Source 4 — Social learning can produce behavior individuals do not discover alone

Source: Bridges et al., Nature, 2024, “Bumblebees socially learn behaviour too complex to innovate alone.”

URL: https://www.nature.com/articles/s41586-024-07126-4

High-level finding:

Naïve bumblebees learned a multi-step foraging solution from trained demonstrators despite failing to solve it independently in control conditions.

Reusable structure:

Social transmission is stronger evidence when naïve observers acquire a behavior after exposure to experienced demonstrators and comparable unexposed individuals do not independently produce it.

Ouros transformation:

A `TRANSMISSION_OBSERVATION` should preserve:

- demonstrator identity when known;
- observer identity or cohort;
- prior experience state;
- behavior observed;
- later independent performance;
- alternative explanations;
- observation confidence.

The system must not conclude “teaching” merely because one individual acted while another was nearby.

## Source 5 — Animal Culture Database: population, behavior and transmission should be separate records

Source: Scientific Data, 2025, “Mapping nonhuman cultures with the Animal Culture Database.”

URL: https://www.nature.com/articles/s41597-025-05315-y

Useful architecture lessons:

- socially transmitted behavior can be recorded separately from species identity;
- populations/groups can differ within one species;
- useful behavior domains include communication, foraging, migration, defense and habitat alteration;
- transmission modes may be described as vertical, horizontal or oblique when evidence supports them;
- human/environmental disturbance may alter behavioral traditions.

Ouros transformation:

Use `behavioral_tradition_id` attached to a population/collective, never to the species definition itself unless canon explicitly says the behavior is species-typical.

Candidate domains:

- VOCAL_REPERTOIRE
- FORAGING_TECHNIQUE
- ROUTE_OR_STOPPING_PRACTICE
- OBJECT_USE
- SHELTER_OR_SITE_USE
- RESOURCE_HANDLING
- DISPLAY_PATTERN
- HUMAN_INTERFACE_BEHAVIOR
- GROUP_COORDINATION
- OTHER_OBSERVED_TRADITION

Transmission mode should remain `UNKNOWN` unless evidence supports a stronger claim.

## Source 6 — experienced individuals can preserve local knowledge for years

Source: Scientific Reports, 2023, “Long-term memory of experienced jays facilitates problem-solving by naïve group members in the wild.”

URL: https://www.nature.com/articles/s41598-023-46666-z

High-level finding:

Experienced wild jays retained a complex foraging solution for several years, and their behavior affected the attempts and success of naïve group members.

Reusable structure:

A small number of persistent experienced individuals can matter disproportionately to whether local knowledge survives between cohorts.

Ouros transformation:

The disappearance, migration, release, death only when canonically confirmed, or relocation of an experienced Pokémon can create a `TRADITION_CONTINUITY_QUESTION`. The system must observe whether the behavior persists rather than automatically deleting the tradition.

This supports long arcs where:

1. one Pokémon is documented using a technique;
2. later observers acquire it;
3. the original demonstrator disappears from the site;
4. the technique persists, changes or fades;
5. years later an archive can reconstruct the sequence.

## Source 7 — learned vocal traditions can evolve over decades

Source: Nature Communications, 2022, “Cumulative cultural evolution and mechanisms for cultural selection in wild bird songs.”

URL: https://www.nature.com/articles/s41467-022-31621-9

High-level finding:

A wild sparrow population showed long-term change in a socially learned song feature over decades, followed by further elaboration in later generations.

Reusable structure:

A tradition should be versioned rather than treated as a permanent binary flag. A repertoire may drift, split, merge or be replaced while the population identity remains continuous.

Ouros transformation:

A Chatot chorus, route call, object-use sequence or other learned practice can have:

- first observation;
- revision history;
- geographic variants;
- old archived recordings;
- contemporary repertoire;
- uncertain transition periods.

No change in learned tradition implies Evolution or mechanical stat change.

## Source 8 — social information does not always produce direct copying

Source: Scientific Reports, 2022, “Social behavior mediates the use of social and personal information in wild jays.”

URL: https://www.nature.com/articles/s41598-022-06496-x

High-level lesson:

Animals can use social information in different ways, including avoiding rather than copying what others do.

Ouros transformation:

Observation of another Pokémon can change behavior without producing imitation. The system should distinguish:

- COPY_OR_EMULATION_HYPOTHESIS
- AVOIDANCE_LEARNING_HYPOTHESIS
- LOCAL_ENHANCEMENT_HYPOTHESIS
- STIMULUS_ENHANCEMENT_HYPOTHESIS
- INDEPENDENT_INNOVATION_HYPOTHESIS
- ECOLOGICAL_CONVERGENCE_HYPOTHESIS
- UNKNOWN

These are scientific interpretations, not mechanical AI modes.

## Design synthesis

### A. Species behavior, individual behavior and local tradition need separate authorities

A species Pokédex entry can make a behavior plausible. It does not prove every local population performs it.

An individual repeatedly performing a technique establishes an individual habit. It does not establish transmission.

A group repeatedly performing a behavior establishes a local pattern. It still does not by itself establish social learning.

A behavioral tradition requires evidence for persistence plus social acquisition or another strong basis approved by canon/research review.

### B. Tradition is not a Trainer Feature

A learned wild behavior never creates by itself:

- a Move;
- an Ability;
- an Edge;
- a Trainer Feature;
- a Skill rank;
- an Accuracy modifier;
- a damage bonus;
- Pack Mon;
- Receiver;
- command authority;
- tactical AI coordination;
- a capture bonus;
- Loyalty.

If a behavior intersects a real PTU mechanic, the mechanic must be validated independently.

### C. Loaded entities are observations, not population truth

Cobblemon may render only a visible subgroup. One loaded group cannot prove adoption across a whole population.

Offline progression should update coarse tradition state from world rules and confirmed events, not by simulating every individual.

### D. Human contact can create traditions without implying domestication

Examples that Ouros may explore as proposals:

- local wild Pokémon learn a ferry timetable and forage after unloading;
- a group learns to use a safe wildlife crossing;
- urban Pokémon learn which bins open easily;
- a Chatot group incorporates a recurring market phrase;
- a wild collective learns that one warning signal predicts a temporary closure.

These remain wild behavior unless Pokémon Agency state says otherwise.

### E. Tradition loss should be evidence-based

A tradition is not erased because:

- one season has no observation;
- one experienced individual disappears;
- a habitat changes;
- a group splits;
- the behavior becomes less common.

Use monitoring effort and adoption snapshots before declaring decline or loss.

## PTU/Caelo mechanical validation state

This pass did not find an authoritative generic “social learning” or “behavioral tradition” mechanic in the inspected AutoPTU-Java/AutoPTU code search.

The latest AutoPTU-Java evidence remains implementation of specific battle rules, not overworld cognition. No generic rule is claimed for:

- imitation;
- teaching;
- local tradition;
- shared repertoire;
- learned migration route;
- learned tool use;
- group knowledge transfer;
- tradition-based battle bonuses.

The complete primary Caelo corpus was not exposed reliably in the runtime. Super PTU Online Helper was not available as an invocable capability. No output is invented for either source.

## Provenance and originality note

The scientific sources are used only for abstract design principles about evidence, transmission, persistence and uncertainty. Ouros does not copy real animal species, field sites or experimental tasks.

Official Pokémon sources are used only for species-grounded behavioral possibilities. No protected dialogue, plot or distinctive story sequence is copied.

PTU sources provide campaign-design guidance and mechanical boundaries. They do not establish new Ouros canon.

## Sources

- Pokémon — Chatot Pokédex: https://www.pokemon.com/us/pokedex/chatot
- Pokémon — Passimian Pokédex: https://www.pokemon.com/us/pokedex/passimian
- Pokémon Tabletop RPG — GM Advice: Your First PTU Session: https://pokemontabletop.com/gm-advice-your-first-ptu-session/
- Bridges et al. (2024), Nature — Bumblebees socially learn behaviour too complex to innovate alone: https://www.nature.com/articles/s41586-024-07126-4
- Animal Culture Database (2025), Scientific Data: https://www.nature.com/articles/s41597-025-05315-y
- Jo et al. (2023), Scientific Reports — Long-term memory of experienced jays facilitates problem-solving by naïve group members in the wild: https://www.nature.com/articles/s41598-023-46666-z
- Williams et al. (2022), Nature Communications — Cumulative cultural evolution and mechanisms for cultural selection in wild bird songs: https://www.nature.com/articles/s41467-022-31621-9
- McCune et al. (2022), Scientific Reports — Social behavior mediates the use of social and personal information in wild jays: https://www.nature.com/articles/s41598-022-06496-x
