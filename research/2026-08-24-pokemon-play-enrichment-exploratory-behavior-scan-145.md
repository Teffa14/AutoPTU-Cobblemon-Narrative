# Pokémon play, enrichment and exploratory behavior research — pass 145

Status: external-source research and provenance. Not Ouros canon.

## Why this scan exists

The narrative repository already has authoritative boundaries for Pokémon welfare, agency, training, cognition, social learning, wild collectives, juvenile care and downtime. Care mentions enrichment as a welfare concern, but the repository does not yet have a dedicated model for voluntary play, exploratory recreation, play partners, toys, choice among enrichment options, interruption/disengagement, or long-term changes in how an individual uses recreational opportunities.

This scan therefore asks a narrow question: how can Ouros represent play and enrichment as persistent observable behavior without turning it into free XP, Loyalty, friendship, training progression, species stereotypes or a hidden welfare score?

External stories remain inspiration sources. They do not define PTU mechanics.

## Existing Ouros boundaries inspected before research

### Care / recovery / welfare

`design/care-recovery-welfare-layer.md` already owns welfare observations, diagnosis, treatment, recovery and care-facility state. It explicitly includes enrichment among non-combat welfare concerns.

Implication: the new play layer may supply observations and opportunity history to Care. It must not diagnose welfare from play frequency alone.

### Pokémon training / practice / coaching

`design/pokemon-training-practice-coaching-layer.md` owns goal-directed practice with an objective, setup, cues, attempts, feedback and transfer evidence.

Implication: an activity remains play when it has no required performance criterion. The same ball or obstacle may later be used in training, but that creates a training-session record rather than retroactively redefining earlier play.

### Social learning / behavioral traditions

`design/pokemon-social-learning-behavioral-traditions-layer.md` owns evidence that a behavior spreads between Pokémon.

Implication: several Pokémon joining the same game is an observed social episode. It is not proof of teaching, imitation or cultural transmission.

### Cognition / problem solving / tool use

`design/pokemon-cognition-problem-solving-tool-use-layer.md` owns interpretation of problem-solving and tool use.

Implication: manipulating a toy or loose object during play does not automatically qualify as tool use.

### Pokémon Agency

`design/pokemon-agency-partnership-release-layer.md` owns individual identity, partnership/custody and observed cooperation or disengagement.

Implication: play invitations and responses must remain observational. A Pokémon can stop participating without a Loyalty penalty or a hidden disobedience flag.

## Pokémon sources

### Pokémon Camp — official Sword/Shield material

Source: Pokémon Sword and Pokémon Shield official site, “Play with Pokémon in your Pokémon Camp.”
https://swordshield.pokemon.com/en-ca/gameplay/pokemon-camps/

Source: Pokémon.com strategy guide, “Top Tips to Begin Your Pokémon Sword or Pokémon Shield Adventure.”
https://www.pokemon.com/uk/strategy/top-tips-to-begin-your-pokemon-sword-or-pokemon-shield-adventure

Reusable structure:

- a party can spend time outside battle in an open camp context;
- individual Pokémon can be observed walking, approaching and interacting;
- toys include balls and other simple objects;
- Pokémon can interact with the Trainer and with one another;
- the same camp is a social/rest context rather than a combat encounter.

Important mechanical boundary:

Sword/Shield awards game-specific benefits including Exp for some camp interactions. Ouros must not import those rewards. A `PLAY_EPISODE` can never award XP, Levels, Tutor Points, Edges, Moves, Friendship/Loyalty changes or battle bonuses unless an authoritative PTU/Caelo mechanic explicitly performs that transaction.

Design lesson:

A persistent world benefits from quiet optional interactions where a player can observe a different side of a known Pokémon. The useful state is the history of choices and interactions, not a grindable numerical affection meter.

### The Lonely Deino! — individual variation inside the same care setting

Source: Pokémon.com, Season 15 Episode 8.
https://www.pokemon.com/us/animation/seasons/15/episode-8-the-lonely-deino

The episode places three Deino in the same Day Care. Two are described as playful while another is frightened, withdrawn and refusing food.

Reusable structure:

- same species + same location does not imply same current behavior;
- low or absent play can coexist with another observable welfare concern;
- behavior should be recorded at individual level when identity is known;
- care decisions should consume a bundle of observations rather than a single `playfulness` variable.

Guardrail:

Absence of play is not itself a diagnosis. Ouros may record `did_not_join_observed_play_episode`; Care decides whether that matters in context.

### Unrest at the Nursery! — play and conflict can coexist

Source: Pokémon.com, Season 15 Episode 47.
https://www.pokemon.com/us/animation/seasons/15/episode-47-unrest-at-the-nursery

The nursery contains recurring friction between Rufflet and Vullaby, a period where the group plays together, then another conflict during lunch.

Reusable structure:

- social play does not erase rivalry or incompatible preferences;
- one successful group session does not establish permanent harmony;
- apparent rough play and actual conflict may require contextual interpretation;
- transitions between interaction modes matter more than a permanent relationship label.

Guardrail:

A play episode does not prove friendship. A conflict after play does not prove betrayal. Social Bonds can reference shared events only when the evidence supports a player-authored or otherwise established relationship.

### Pikachu’s Winter Vacation — environmental and mixed-participant recreation

Source: Pokémon.com, Pokémon Chronicles Episode 22.
https://www.pokemon.com/us/animation/seasons/chronicles/episode-22-pikachus-winter-vacation

The story includes Pokémon using snow, thrown snow and a sled-like object in recreational interaction, with another Pokémon joining an activity after observing it.

Reusable structure:

- temporary environmental conditions can open recreational opportunities;
- objects can have a recreational use without becoming equipment;
- a mixed-species activity may happen once without establishing a permanent social relationship;
- observing another participant before joining is not enough by itself to prove social-learning transmission.

Ouros transformation:

Use seasonal surfaces, loose natural materials and persistent objects as play affordances. Keep environmental state authoritative in the relevant ecology/weather layer. The play layer records interaction with that state.

## PTU community and campaign-design sources

### Campaign log #25 — repetition can become bad pacing

Source: r/PokemonTabletop campaign log #25.
https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

The recap describes a group deciding not to replay a long battle after training because the repeated encounter had become exhausting.

Reusable lesson for play/enrichment:

Routine repeated recreation should compress. The player should not have to manually throw the same toy fifty times to maintain welfare or relationship state. Detailed interaction is valuable when a preference changes, a new participant joins, an object acquires history, or the activity intersects another world system.

### PMJ playtest discussion — camp/downtime as narrative beats

Source: Pokémon Tabletop forum, “Playtest materials for PMJ!”
https://www.tapatalk.com/groups/pokemon_tabletop/playtest-materials-for-pmj-t5994-s50.html

The discussion frames camp and downtime phases as narrative beats that can reflect access to local amenities and resources rather than requiring literal simulation of every minute.

Reusable lesson:

Ouros can treat play/enrichment the same way. Routine access may be compressed into a short persistent record. A full scene appears only when the activity reveals a meaningful choice, change, interruption or relationship with the environment.

No PMJ rule is imported into PTU/Caelo.

## Animal behavior and welfare research

### Play has multiple forms and should not be reduced to one meter

Source: St John Wallis, Mendl, Lecorps & Held, 2025, “From welfare indicator to welfare contributor: the role of play in building flexibility and resilience in captive animals.” Proceedings of the Royal Society B.
https://pmc.ncbi.nlm.nih.gov/articles/PMC12651949/

The review distinguishes forms including locomotor, social and object play and argues that play can be relevant both as an observed welfare correlate and as an activity that may contribute to flexibility/resilience.

Reusable structure:

- record play domain rather than one scalar score;
- allow adult as well as juvenile play when observed;
- keep occurrence, frequency and interpretation separate;
- preserve uncertainty about causal welfare effects.

Guardrail:

Play frequency cannot become a universal welfare score. Species, age/life stage, context and individual history matter.

### Choice and control matter independently of which option is selected

Source: Englund & Cronin, 2023, “Choice, control, and animal welfare: definitions and essential inquiries to advance animal welfare science.” Frontiers in Veterinary Science.
https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2023.1250251/full

The review emphasizes opportunities for choice and control, notes that preferences can change over time and warns against assuming humans already know which option is best for an animal.

Reusable structure:

- enrichment is an opportunity, not a forced activity;
- record which options were available, not only which one was selected;
- preserve `NO_INTERACTION_OBSERVED` separately from refusal;
- allow preferences to change by context and date;
- removal of an unselected option can still reduce future choice.

Ouros implication:

An enrichment yard should expose several legal options when appropriate. The system records availability and observed use. It should not optimize every Pokémon toward the same toy or interaction.

### Interspecific social play exists, but evidence is often observational and context-heavy

Source: Brooks & Burghardt, 2023, “A review of interspecific social play among nonhuman animals.” Neuroscience & Biobehavioral Reviews.
https://pubmed.ncbi.nlm.nih.gov/37182799/

The review documents interspecific social play across several taxa while stressing that reports are often brief and systematic interpretation benefits from participant history and context.

Reusable structure:

- permit one-off mixed-species play observations;
- record identities, life-stage context and previous contact where known;
- avoid promoting one interaction into a stable cross-species bond;
- keep play classification confidence explicit.

This is especially valuable for Pokémon because mixed-species facilities, parties and wild aggregations are common.

## Proposed design conclusions

### 1. Play is an observed behavioral episode

It should be possible to record:

- who participated;
- who was nearby but did not participate;
- what objects or environmental affordances were available;
- whether the episode was solitary, social, locomotor, object-oriented or mixed;
- invitations/approaches and observable responses;
- pauses, disengagement and restart;
- whether the activity became training, conflict, feeding or another state;
- recordings/photographs and observer confidence.

The record must not infer internal emotion beyond what is directly authored or otherwise established.

### 2. Enrichment is an opportunity set

A facility or caretaker can provide several options. The important state is both availability and observed interaction.

Candidate statuses:

`AVAILABLE`, `OFFERED`, `APPROACHED`, `INTERACTED`, `IGNORED_DURING_WINDOW`, `DISENGAGED`, `UNAVAILABLE`, `REMOVED_FOR_SAFETY`, `RETIRED`.

`IGNORED_DURING_WINDOW` is not equivalent to dislike.

### 3. Recreational objects remain Material Culture objects

A ball, rope, floating object, puzzle feeder, loose branch or sled-like object may have a persistent `item_instance_id` when important.

The play layer records use. Material Culture owns physical identity, repair, ownership/custody and provenance.

A toy never becomes a PTU Item solely because Minecraft can render or pick it up.

### 4. Play and training need an explicit handoff

If a Trainer begins measuring success criteria, issuing repeatable performance cues or trying to change a task-specific behavior, the activity may create a `TRAINING_SESSION` reference.

Earlier free play remains free play in Chronicle.

### 5. Rough-and-tumble play needs uncertainty, not a binary aggression detector

Candidate interpretations can include:

- PLAY_LIKELY;
- CONFLICT_LIKELY;
- MIXED_OR_TRANSITIONAL;
- UNRESOLVED.

The system should store observations such as role reversal, voluntary re-engagement or withdrawal only when observed. It must not invent ethological rules for a species without authored or researched evidence.

### 6. Play can stop being content

Routine successful access should compress. The system can record periodic summaries while exposing only meaningful changes to the player.

This prevents enrichment from becoming a mandatory maintenance minigame.

## PTU/Caelo mechanical boundary

No source reviewed here establishes a PTU rule where ordinary recreational play grants:

- XP or Levels;
- Tutor Points;
- Poke Edges;
- Moves;
- Skill ranks;
- Loyalty/Friendship changes;
- Accuracy/Evasion bonuses;
- Initiative bonuses;
- temporary HP;
- healing;
- Injury recovery;
- Status removal;
- Contest bonuses;
- Trainer Features;
- species-wide behavioral modifiers.

Sword/Shield Camp has video-game-specific Exp behavior. It is not a PTU rule and must not be imported.

The project's Care and Training layers already require authoritative PTU/Caelo transactions before mechanical state changes.

A complete authoritative Caelo corpus defining enrichment/play mechanics was not recovered in this run. Super PTU Online Helper was not exposed as an invocable capability. No output is invented for either source.

## Engine implications

Most play/enrichment content should remain overworld world state and does not need AutoPTU.

Mechanically rich scenes become battle-dependent only when they require movement under pressure, dynamic escape/withdrawal, protected noncombatants, object interaction, hazards or objective-aware AI.

The intended encounter design should therefore provide both FULL and REDUCED forms.

Current permanent categories remain:

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: complete movement including push/pull/knockback/interception/forced movement; terrain/weather/hazards/zones/reactions as a complete family; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback.

## Sources retained for provenance

Pokémon Camp official site: https://swordshield.pokemon.com/en-ca/gameplay/pokemon-camps/

Pokémon.com Sword/Shield camp tips: https://www.pokemon.com/uk/strategy/top-tips-to-begin-your-pokemon-sword-or-pokemon-shield-adventure

The Lonely Deino!: https://www.pokemon.com/us/animation/seasons/15/episode-8-the-lonely-deino

Unrest at the Nursery!: https://www.pokemon.com/us/animation/seasons/15/episode-47-unrest-at-the-nursery

Pikachu’s Winter Vacation: https://www.pokemon.com/us/animation/seasons/chronicles/episode-22-pikachus-winter-vacation

PTU campaign log #25: https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

PMJ camp/downtime discussion: https://www.tapatalk.com/groups/pokemon_tabletop/playtest-materials-for-pmj-t5994-s50.html

St John Wallis et al. 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12651949/

Englund & Cronin 2023: https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2023.1250251/full

Brooks & Burghardt 2023: https://pubmed.ncbi.nlm.nih.gov/37182799/
