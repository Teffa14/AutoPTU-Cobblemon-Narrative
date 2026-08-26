# Pokémon Individual Behavior, Personality & Temperament Research Scan — Pass 182

Status: RESEARCH / PROVENANCE ONLY. Nothing here is established Ouros canon.
Date: 2026-08-26

## Scope and duplicate check

The full `design/`, `research/` and `proposals/` inventories were inspected before writing. Existing systems already own persistent Pokémon identity, partnership/refusal history, welfare, cognition, play, training, social learning, spatial ecology, courtship, vigilance, camouflage and group behavior. No existing authority owns repeated individual behavioral tendencies as a longitudinal evidence problem.

This pass therefore targets a narrow gap: how Ouros can remember that two individuals of the same species repeatedly behave differently, while preserving context, uncertainty and change over time.

Primary internal boundaries:

- `pokemon-agency-partnership-release-layer.md`: identity, associations, observed cooperation/refusal and facts-before-feelings.
- `pokemon-cognition-problem-solving-tool-use-layer.md`: problem solving and object use.
- `pokemon-social-learning-behavioral-traditions-layer.md`: transmission between individuals.
- `pokemon-play-enrichment-exploratory-behavior-layer.md`: play/enrichment choices.
- `pokemon-spatial-ecology-home-ranges-territoriality-layer.md`: spatial-use assessments.
- `pokemon-vigilance-alarm-signals-antipredator-behavior-layer.md`: vigilance/alarm behavior.
- `care-recovery-welfare-layer.md`: welfare and diagnosis.
- `aging-senescence-retirement-role-transition-layer.md`: age-related change.
- `pokemon-training-practice-coaching-layer.md`: trained behavior.
- `wild-collective-agency-layer.md`: group-level behavior.
- `research-ethics-consent-subject-protection-layer.md`: study authorization and subject protection.

## PTU mechanical boundary: Nature already has authoritative meaning

The project's read-only PTU 1.05 source set contains the `Pokémon Nature Chart`. Natures such as Cuddly, Proud, Patient, Lonely, Adamant, Timid, Jolly and Calm have explicit stat Raise/Lower effects; neutral Natures cancel themselves out.

Project source inspected:

- `Teffa14/AutoPTU/audit_sources/Useful Charts.txt` at inspected AutoPTU head `7e6ce7c8138273f8d45180d192e84088b9f0986f`.

Critical design consequence:

`observed shy behavior -> Timid Nature` is forbidden.

Likewise:

- calm behavior does not imply Calm Nature;
- repeated curiosity does not imply Curious Nature;
- a mechanically Timid Pokémon need not be procedurally authored as globally shy;
- narrative assessments cannot change Nature or its stat effects;
- any Mint/Nature rule remains exclusively in the authoritative PTU/Caelo path.

This boundary matters because PTU Nature labels use ordinary personality words.

## Official Pokémon material: individual characterization exists independently of species

### Pokémon Concierge

An official Pokémon article describes a tour group containing multiple Pikachu while identifying one individual as extremely shy. Haru helps that Pikachu's Trainer better understand the individual. The same article references another resort guest that was afraid of the dark.

Source:

- The Pokémon Company International, `Soak Up Some Sun with the Pokémon Concierge Quiz`.
- https://www.pokemon.com/uk/pokemon-news/soak-up-some-sun-with-the-pokemon-concierge-quiz

Reusable structure:

`same species / shared setting -> individual response differs -> caretaker notices pattern -> better observation changes handling`.

Ouros adaptation:

A persistent Pokémon can become recognizable because of repeated responses to crowds, novelty, specific places or familiar actors. One scene remains one observation. A tendency requires repeated evidence.

### Pokémon: Let's Go

The official `Let's Go for a Test Run` article describes partner Pikachu/Eevee as full of personality and notes that they interact with some objects on their own accord.

Source:

- The Pokémon Company International, `Let's Go for a Test Run`.
- https://www.pokemon.com/us/news/lets-go-for-a-test-run

Reusable lesson:

Small autonomous choices can characterize a recurring Pokémon without dialogue, a biography dump or a combat bonus.

Ouros adaptation:

Voluntary approaches, avoidance, object inspection, waiting, route preferences or disengagement can create recognizable continuity when they recur. Preserve the observations before assigning a label.

## PTU community material: individual Pokémon characterization is a major tabletop strength

A public `r/PokemonTabletop` discussion argues that PTU's narrative strength comes from unique scenarios and behaviors given to individual Pokémon. The author describes forming attachments to Pokémon because of specific encounter histories and behavior rather than species preference or optimization.

Source:

- Reddit, r/PokemonTabletop, `IMO Tabletop is the best way to experience Pokémon.`
- https://www.reddit.com/r/PokemonTabletop/comments/qcz02z/

Reusable lesson:

`encounter behavior -> memorable individual -> player interest -> durable relationship history` can outperform rarity as an attachment loop.

A separate public PTU campaign log explicitly distinguishes a Pokémon's mechanical Nature from personality traits the player was still deciding how to roleplay.

Source:

- Reddit, r/PokemonTabletop, `campaign log #5`.
- https://www.reddit.com/r/PokemonTabletop/comments/mp6jmz/

Ouros adaptation:

Mechanical Nature and characterization remain parallel records. The generator may remember observed behavior but never reverse-engineer Nature from it.

## Behavioral ecology: repeated evidence is the key

### Individual differences alone are insufficient

A review of consistent individual behavioral variation notes that personality, temperament and behavioral syndrome are frequently used inconsistently. The useful core is repeated individual variation across time and/or contexts, with explicit attention to the level of variation being measured.

Source:

- Mackay & Haskell, `Consistent Individual Behavioral Variation: The Difference between Temperament, Personality and Behavioral Syndromes`.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4598688/

Ouros consequence:

Do not store one universal `personality` flag. Preserve event-level behavior and use assessments scoped to a domain, context set and time window.

### Terminology is contested; evidence should survive labels

A systematic review and researcher survey found substantial disagreement over animal-personality terminology. The most common conceptual definition involved consistent between-individual differences across time and/or contexts, but interpretation remained non-uniform.

Source:

- `Terminology use in animal personality research: a self-report questionnaire and a systematic review`.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8808088/

Ouros consequence:

Observation history must survive vocabulary changes. Different institutions may call the same evidence `temperament`, `behavioral tendency`, `individual style` or another authored term without rewriting events.

### Context matters

Research on context-dependent behavioral syndromes shows that a behavior can be repeatable in one condition and not another. Environmental context can change both average behavior and the apparent consistency of individual differences.

Sources:

- `Context-dependent trait covariances: how plasticity shapes behavioral syndromes`.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7937033/
- `Population differences in the effect of context on personality in an invasive lizard`.
- https://academic.oup.com/beheco/article/32/6/1363/6372049

Ouros consequence:

`readily explores familiar yard` cannot automatically become `bold around predators`, `bold in battle`, `bold after Evolution` or `bold in a new settlement`.

### Consistency can change through life

Longitudinal work shows that some behavioral traits remain repeatable while others change, and correlations among traits can be unstable across life stages.

Sources:

- `Personality over ontogeny in zebra finches: long-term repeatable traits but unstable behavioural syndromes`.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4722341/
- `Developmental perspectives on personality: implications for ecological and evolutionary studies of individual differences`.
- https://pmc.ncbi.nlm.nih.gov/articles/PMC2992751/

Ouros consequence:

An assessment is versioned, not permanent. Evolution, age, injury/recovery, training, relocation, partnership change, social environment or ordinary development may justify a new assessment without making older observations false.

### Recent 2026 evidence: consistency and flexibility can coexist

A 2026 Frontiers study reports consistent individual differences in exploration while examining how individuals adjust behaviorally and physiologically to differing environments.

Source:

- Quante et al. (2026), `Personality tips the scale: how individual differences in exploration shape behavioural and hormonal adjustment to different environments`.
- https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2026.1769757/full

Ouros consequence:

The model should preserve both between-individual differences and within-individual plasticity.

### Natural-context observations are valuable but consistency is not absolute

A study of sanctuary chimpanzees examined behavior across feeding, affiliation, resting and solitude over multiple years. Some behaviors showed temporal/contextual consistency while others varied substantially.

Source:

- `Testing for personality consistency across naturally occurring behavioral contexts in sanctuary chimpanzees`.
- https://pubmed.ncbi.nlm.nih.gov/36394276/

Ouros consequence:

Naturally occurring Chronicle observations can support an assessment, but a mixed pattern is a legitimate result rather than a failure to assign a label.

## Observation method can shape conclusions

A 2025 longitudinal chimpanzee study found long-term stability in some personality measures while showing that trait ratings and direct behavioral codings do not always measure the same thing.

Source:

- `Long-term stability of chimpanzee personality: comparing trait ratings and behaviour codings over a quarter of a century`.
- Animal Behaviour 227 (2025), 123241.

Reusable lesson:

Observer labels such as `confident`, `gentle` or `stubborn` should never replace event-level evidence such as approach latency, withdrawal, exploration choice or duration of interaction.

Ouros adaptation:

An NPC researcher may publish an interpretation. Chronicle retains the observations underneath it so a later researcher can revise the assessment without deleting history.

## Design lessons extracted

1. Persist behavior before interpretation.
2. Require repeated evidence before calling a tendency stable.
3. Scope every assessment to domain, contexts and time window.
4. Preserve within-individual change rather than treating it as data failure.
5. Keep direct observations separate from observer ratings.
6. Preserve method and disturbance context.
7. Keep species-level Pokédex flavor separate from individual assessment.
8. Keep PTU Nature mechanical unless reviewed project canon explicitly says otherwise.
9. Never turn behavioral labels into stats, combat AI, capture modifiers, Loyalty, Skills or Features.
10. Allow `MIXED`, `CONTEXT_DEPENDENT`, `INSUFFICIENT_EVIDENCE` and `REVISED` as normal outcomes.

## Narrative structures worth reusing in Ouros

### Recognition through behavior

A player recognizes a recurring Pokémon because it pauses at the same doorway, investigates unfamiliar equipment before food, avoids crowds but approaches one quiet caretaker, or chooses novel routes sooner than its companions. Identity becomes legible without omniscient internal narration.

### The label that becomes outdated

An institution describes one individual as highly exploratory for several seasons. After relocation or a life-stage change the pattern changes. The old report remains historically valid for its scope while the current assessment is revised.

### Same species, different individuals

A group shares species ecology while persistent individuals develop distinguishable response histories. Attachment can grow without requiring shininess, rarity or custom mechanics.

### Same individual, different contexts

An individual investigates new objects in a familiar yard but withdraws quickly inside unfamiliar buildings. The useful story is the conditional pattern rather than a global adjective.

### Reputation versus evidence

A famous Pokémon acquires a public label such as `fearless`, `lazy`, `stubborn` or `gentle`. Public Memory may preserve that reputation while observations support a more complicated pattern.

## PTU/Caelo questions left open

The project PTU source confirms mechanical Natures and their stat effects. This pass did not recover a reliable complete Caelo source defining a separate personality/temperament subsystem.

Unresolved:

- whether Caelo adds narrative interpretation to Nature;
- whether Caelo changes Nature acquisition/modification;
- whether any Caelo Feature/Edge links repeated behavior to a rule effect;
- whether project Loyalty/Command rules create any relevant non-combat boundary;
- whether an authoritative rule defines fearfulness, boldness, temperament or behavior-change procedures.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output is attributed to it.

## Originality boundary

External sources are used only for high-level structures, methodological cautions and design lessons. No protected dialogue, distinctive plot, character arc or campaign sequence is copied. All Ouros candidates derived from this pass remain NON-CANON until review.