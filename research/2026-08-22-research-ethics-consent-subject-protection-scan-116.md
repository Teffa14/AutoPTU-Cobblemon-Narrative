# Research scan — Research ethics, consent & subject protection — Pass 116

Status: research/provenance only. Not Ouros canon. External sources are design references, never rules authorities.

## Why this pass

The repository already has a strong Science, Research & Discovery layer. It can store questions, methods, samples, datasets, hypotheses, claims, replication, review and publication. Several other layers already protect custody, private medical state, psychic information, Pokémon agency and institutional mandate.

A gap remained between those systems: the project can describe a scientifically useful study without yet having one shared contract for whether a proposed procedure is acceptable to perform, who can authorize it, what a participant agreed to, what happens when a Pokémon withdraws or becomes distressed, when fieldwork must stop, how later use of samples/data is scoped, and how protocol changes preserve history rather than silently expanding permission.

This scan therefore focuses on reusable structures for research ethics and subject protection. It does not import real-world law, human-subject regulations, animal-welfare statutes, institutional-review-board rules or permit systems into Ouros.

## Existing Ouros boundaries reviewed before research

The current Science layer already distinguishes world truth, observations, samples, datasets, hypotheses, analyses, claims, replication, institutional positions and publications. It explicitly notes that sample collection needs separate authorization and that research methods may contain ethical constraints.

The Pokémon Agency layer already prevents the narrative generator from inferring emotions, obedience, Loyalty or universal consent from custody, capture or cooperation. It also preserves explicit observed cooperation/refusal events.

The Institutional Review layer already models bounded review bodies, mandates, evidence packages, findings, decisions and review/appeal. It deliberately avoids inventing a universal court or legal system.

The Care, Conservation, Psychic Information, Case/Custody, Credentials and Land Access layers already own their respective domains. A research-ethics layer therefore should not duplicate them. Its job is to coordinate authorization and subject-protection state around a research protocol.

## Public Pokémon material

### Mewtwo: scientific capability can create a subject with interests of its own

The official Pokémon description for *Mewtwo Strikes Back—Evolution* says researchers exploit a Mew fossil to create Mewtwo for use as a destructive tool, after which Mewtwo becomes aware of its origin and resents its creators.

Reusable design lesson:

- technical success does not settle whether a procedure should have been performed;
- a created or modified Pokémon remains a persistent actor, not a research asset whose identity ends when the experiment ends;
- the institution's intended use and the subject's later agency can conflict;
- a project can produce valuable knowledge and still have unacceptable methods.

Ouros adaptation:

Research programs involving artificial creation, invasive modification, control devices or permanent alteration should require explicit authored canon and high scrutiny. Procedural generation must not invent cloning, gene editing, personality alteration or similar procedures merely because a research plot needs higher stakes.

Source: Pokémon, “Pokémon: Mewtwo Strikes Back—Evolution”
https://www.pokemon.com/us/animation/movies/pokemon-mewtwo-strikes-back-evolution

### Genesect: historical modification should preserve provenance and responsibility questions

The official Pokédex says Team Plasma altered an ancient Pokémon and attached/upgraded a cannon on its back.

Reusable design lesson:

A modified Pokémon can have at least three separate histories:

1. the Pokémon's biological/personal continuity;
2. the intervention history;
3. the institution or actors responsible for the modification.

Ouros should not collapse those histories into a species label such as `modified=true`. Historical records may disagree about what happened, but physical interventions should remain provenance-bearing events when canon establishes them.

Source: Pokémon Pokédex, Genesect
https://www.pokemon.com/us/pokedex/genesect

### Type: Null: restraint/control and research secrecy are separate problems

The official Pokédex describes Type: Null as an artificial Pokémon whose mask limits its power to keep it under control. It also preserves a rumor that stolen secret research notes enabled another instance to be created elsewhere.

Reusable design lessons:

- restraint can be a specific intervention with a stated purpose, not a generic condition of an artificial Pokémon;
- research-data access and treatment of the subject are different ethical questions;
- a rumor about leaked research remains a claim until evidence establishes what actually happened;
- copying a protocol or dataset does not copy the identity of an existing Pokémon.

Source: Pokémon Pokédex, Type: Null
https://www.pokemon.com/us/pokedex/type-null

### PTU campaign seed: researchers can shape institutions, including morally bad ones

The official Pokémon Tabletop blog's “The Road to Tomorrow” includes a Holon Institute campaign where players are researchers who can influence which facilities and specialities the expedition develops. One suggested conflict explicitly asks what happens when cruel or immoral experimentation produces discoveries with broad social value.

Reusable design lessons:

- research direction itself can be a player-facing choice;
- an institution can accumulate methods and norms over years rather than having a fixed moral alignment;
- “useful result” must remain independent from “acceptable process”;
- shutting down one procedure need not erase the discovery, evidence or institutional history already produced;
- the important consequence may be a new norm, review process or research culture rather than a boss battle.

Source: Pokémon Tabletop RPG, “Campaign Seeds: The Road to Tomorrow”
https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

## Field-research design references

The following sources are real-world institutional material. Ouros should extract only abstract design principles. It must not copy U.S. law, permit jurisdiction, committee structure, statutory ownership, protected-species lists or professional requirements.

### Minimize disturbance and allow fieldwork to stop

USGS describes animal-welfare practice that favors avoiding disturbance, using noninvasive methods when possible, limiting handling, monitoring conditions and pausing work when circumstances become unsafe. It also describes alternatives such as camera traps, acoustic recorders and environmental DNA.

Reusable design lessons:

- a research protocol should specify a disturbance level before fieldwork starts;
- teams need explicit stop conditions;
- choosing a lower-impact method can be meaningful progress rather than a weaker quest solution;
- repeated visits can themselves create impact;
- a subject-protection system should preserve why a study paused or switched methods rather than treating it as mission failure.

Source: U.S. Geological Survey, “USGS Commitment to Animal Welfare in Research,” September 8, 2025
https://www.usgs.gov/mission-areas/ecosystems/science/usgs-commitment-animal-welfare-research

### Permission should be scoped to activity, place and time

The U.S. National Park Service research overview describes permits that authorize stated activities in specified places/times and distinguishes non-manipulative studies from more intrusive work that needs greater review. It also treats specimen collection and resource disturbance as specific concerns.

Reusable design lessons:

- access to a location does not authorize every research procedure there;
- observing, deploying a sensor, handling a Pokémon, collecting a sample and destructive analysis can be separate permissions;
- a protocol can become invalid for a new cave, new species, new life stage or new procedure even when the original project remains legitimate;
- the review burden can scale with intervention level without turning Ouros into administrative paperwork simulation.

Source: U.S. National Park Service, “Research and Collecting Permit Overview”
https://www.nps.gov/subjects/science/research-and-collecting-permit-overview.htm

### Samples need continuing provenance after collection

NPS general conditions illustrate the value of recording what was collected, from where, its current state and current location. Their real ownership rules are specific to that institution and must not be imported into Ouros.

Reusable design lesson:

Collection is not the end of an ethical/provenance chain. A sample may later be transferred, consumed in analysis, destroyed, archived, returned, restricted or opened for a new analysis. Secondary use should therefore have its own authorization state.

Source: U.S. National Park Service, “General Conditions for Scientific Research and Collecting Permit”
https://www.nps.gov/subjects/science/general-conditions-for-scientific-research-and-collecting-permits.htm

## High-value abstractions for Ouros

### Scientific validity and ethical authorization need separate records

A protocol may be scientifically weak but ethically low-risk.

A protocol may be scientifically excellent but unacceptable to perform.

A protocol may be acceptable only after modification.

A null result may still justify the disturbance it caused if the method and authorization were valid.

These states should never be represented by one `approved` boolean.

### Human participant consent is not the same as location or institutional permission

A university, clinic, Gym, employer or club can authorize access to its own facility. That does not let it consent on behalf of a PC to private interviews, medical data use, psychic access or other participant-level procedures.

For PCs, intrusive/private research requires explicit player action. Party membership is not blanket consent.

### Pokémon permission cannot be reduced to a universal roll

Pokémon differ radically in communication capabilities, intelligence, relationship state and mechanical rules. Ouros should not create one universal “Pokémon consent check.”

Instead:

- preserve explicit communication when canon/rules support it;
- preserve observed approach, cooperation, hesitation, avoidance, refusal or withdrawal;
- preserve mechanical Command/Loyalty separately when authoritative;
- allow authored stewards/custodians to authorize only the scopes that Ouros canon actually gives them;
- stop a procedure when its authored welfare/withdrawal condition occurs;
- do not infer enduring consent from one cooperative event.

A Trainer agreeing to a study does not make every procedure acceptable for the Trainer's Pokémon.

### Consent is scoped and versioned

A participant may agree to:

- observation but not physical sampling;
- one sample but not destructive analysis;
- internal analysis but not public release;
- a battle study but not medical-record access;
- one visit but not repeated follow-up;
- anonymized aggregate publication but not identifiable media use.

If the method changes, the old permission may no longer cover the new procedure.

### Withdrawal creates history without requiring continued use of data

The Chronicle should preserve that participation ended and why, when that reason is known and releasable. It does not need to retain or expose data whose continued use is no longer authorized.

This is a useful distinction between audit/history state and research-content access.

### Research on Eggs, juveniles, nesting or rehabilitation deserves extra boundaries

The Breeding/Nursery, Care and Conservation layers already preserve Egg custody, nesting ecology, juvenile care and rehabilitation. Research should consume those states rather than overriding them.

A nest or juvenile becoming newly relevant can trigger a protocol stop or amendment without generating a combat encounter.

### Psychic, dream and Aura research needs private-information consent

The Psychic Information layer already prevents automatic mind-reading of PCs. Research must honor the same boundary.

A dream study can store a participant-submitted report without creating access to every private dream or memory. A telepathic researcher cannot bypass consent merely because a PTU Feature could technically obtain information in another context.

### Field sites can need protection from publication

A study may be publishable while exact coordinates remain restricted because disclosure could increase disturbance, poaching, crowding or exploitation. Media/Public Information owns the publication packet; Conservation/Land Access owns location restrictions.

“Open science” should not become a narrative excuse to expose protected nesting sites or player-private bases.

### Research misconduct and protocol deviation are not synonyms

Examples that must stay separate:

- a sensor deployed 20 metres from its planned coordinate because the site flooded;
- a participant withdrew halfway through a season;
- a researcher intentionally concealed an adverse event;
- a sample label was transcribed incorrectly;
- a procedure exceeded its permitted scope;
- a safe method produced an unexpected reaction.

Each can lead to review, but they are not morally or institutionally equivalent.

## Proposed data objects to explore

- `RESEARCH_PROTOCOL`
- `PROTOCOL_VERSION`
- `INTERVENTION_CLASS`
- `PROTOCOL_AUTHORIZATION`
- `PARTICIPATION_PERMISSION`
- `DATA_USE_PERMISSION`
- `SAMPLE_USE_PERMISSION`
- `POKEMON_ASSENT_OBSERVATION`
- `WELFARE_STOP_CONDITION`
- `RESEARCH_STOP_EVENT`
- `PROTOCOL_AMENDMENT`
- `PROTOCOL_DEVIATION`
- `ADVERSE_RESEARCH_EVENT`
- `SENSITIVE_SITE_RESTRICTION`
- `FIELD_IMPACT_LEDGER`
- `SECONDARY_USE_REQUEST`

These should reference existing Science/Agency/Care/Conservation/Institutional Review records rather than replacing them.

## PTU/Caelo boundary

This research does not establish any new PTU mechanic.

Do not invent:

- Researcher Feature effects;
- Education Skill DCs;
- Command/Charm/Guile checks for consent;
- Loyalty changes from research participation;
- restraint rules;
- sedation/anesthesia rules;
- sample-collection damage;
- capture modifiers;
- handling bonuses;
- psychic-information access;
- cloning or genetic-modification rules;
- experimental-device combat effects;
- automatic Status conditions caused by research procedures.

Any actual procedure that invokes a Move, Feature, Ability, Item, Status, healing, restraint, command or battle action must use the authoritative PTU/Caelo text and current engine implementation.

The complete primary Caelo corpus was not reliably accessible in this runtime. Super PTU Online Helper was not exposed as an invocable capability. No output is attributed to either.

## Candidate encounter implementation lessons

A research ethics layer should create fewer forced combats, not more.

A field team reaching a stop condition can simply withdraw.

A Pokémon refusing handling can end that procedure without becoming hostile.

An Egg or juvenile appearing can convert an active survey into observation-only mode.

When a separate threat creates combat, the study state should remain outside the battle engine unless current AutoPTU capabilities explicitly support the relevant objective.

This preserves both player agency and the authority boundary between narrative state and PTU mechanics.

## Sources processed in this pass

Pokémon official:
- Type: Null Pokédex — https://www.pokemon.com/us/pokedex/type-null
- Genesect Pokédex — https://www.pokemon.com/us/pokedex/genesect
- Pokémon: Mewtwo Strikes Back—Evolution — https://www.pokemon.com/us/animation/movies/pokemon-mewtwo-strikes-back-evolution

PTU:
- Pokémon Tabletop RPG, Campaign Seeds: The Road to Tomorrow — https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

Research-method / field-impact references:
- USGS Commitment to Animal Welfare in Research — https://www.usgs.gov/mission-areas/ecosystems/science/usgs-commitment-animal-welfare-research
- NPS Research and Collecting Permit Overview — https://www.nps.gov/subjects/science/research-and-collecting-permit-overview.htm
- NPS General Conditions for Scientific Research and Collecting Permit — https://www.nps.gov/subjects/science/general-conditions-for-scientific-research-and-collecting-permits.htm

## Originality note

Only abstract structures and design lessons were extracted. No protected dialogue, distinctive characters, plots or prose have been imported into Ouros. Real-world institutional requirements are not Ouros law. Pokémon and PTU sources remain provenance only until a separate canon review approves original derived material.