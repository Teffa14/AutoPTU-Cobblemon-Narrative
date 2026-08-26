# Pokémon Individual Behavior, Personality & Temperament Layer

Status: PROPOSED SYSTEMS DESIGN / NON-CANON
Pass: 182
Date: 2026-08-26

## Purpose

Ouros needs persistent individual Pokémon to be recognizable for more than species, level, moveset or ownership history. The world should be able to remember repeated behavioral differences between individuals while avoiding a hidden personality stat, anthropomorphic mind-reading or accidental duplication of PTU Nature.

This layer owns evidence and assessments of recurring individual behavioral tendencies. It does not own mechanical Nature, welfare diagnosis, cognition, Loyalty, social learning, training, spatial ecology, courtship, vigilance or group behavior.

## Core separation

Use this chain:

```text
persistent Pokémon identity
        ↓
behavior observation in a defined context
        ↓
repeated observations across time
        ↓
context comparison
        ↓
behavioral-tendency assessment
        ↓
assessment revision / stability review
        ↓
public or institutional interpretation if published
```

Do not collapse it into:

```text
one event -> personality label -> combat behavior/stat bonus
```

## 1. Authority boundaries

Pokémon Agency owns:

- `pokemon_entity_id`;
- association history;
- custody/partnership state;
- observed cooperation/refusal when relevant to a request;
- player authority boundaries.

This layer owns:

- repeated behavioral observations tied to contexts;
- cautious individual-tendency assessments;
- evidence of consistency, flexibility or change;
- comparison across contexts and time windows;
- observer-rating provenance when institutions use ratings.

Care owns:

- diagnosis;
- welfare interpretation;
- pain, illness, distress and treatment decisions.

Cognition owns:

- problem-solving performance;
- strategy changes;
- object manipulation/tool-use interpretation.

Play owns:

- play episodes and enrichment choices.

Training owns:

- drills, cues, practice and transfer of trained behavior.

Social Learning owns:

- transmission between individuals;
- behavioral traditions.

Spatial Ecology owns:

- home range, core-use area, excursions, territorial assessments.

Vigilance owns:

- lookout/alarm/antipredator episodes.

Wild Collectives owns:

- group-level state and collective behavior.

Research Ethics owns:

- authorization of structured assays, handling or intrusive observation.

PTU/Caelo owns:

- mechanical Nature;
- Loyalty/Command;
- Skills, Edges, Features;
- stats and combat rules.

## 2. Behavioral observation record

Record the smallest defensible event.

```yaml
behavior_observation:
  observation_id: null
  pokemon_id: null
  timestamp_ref: null
  location_ref: null
  behavior_domain: novelty_response|exploration|social_approach|human_approach|resource_approach|threat_response|persistence|handling_response|activity|other
  context_tags: []
  stimulus_ref: null
  opportunity_set_ref: null
  observed_behavior: null
  latency: unknown
  duration: unknown
  termination: completed|withdrew|interrupted|stimulus_removed|observer_lost|unknown
  observer_id: null
  method: direct|video|camera_trap|structured_assay|caretaker_log|other
  disturbance_refs: []
  welfare_case_ref: null
  training_session_ref: null
  confidence: direct|supported|uncertain
  provenance_refs: []
```

A behavior observation is not a trait label.

Examples of valid observations:

- approached an unfamiliar crate after 18 seconds;
- remained outside the yard while three other individuals entered;
- explored a new corridor before returning to the known route;
- accepted food only after the crowd dispersed;
- withdrew from a handling station before contact;
- returned to inspect the same new object on three mornings;
- ignored a novel object during a storm but approached it on a quiet day.

Avoid records such as:

- shy;
- brave;
- lazy;
- stubborn;
- friendly;
- aggressive personality.

Those are interpretations unless directly authored as character canon.

## 3. Opportunity matters

Absence of behavior is meaningful only when the behavior could reasonably have occurred.

```yaml
behavior_opportunity_set:
  opportunity_id: null
  pokemon_id: null
  domain: null
  opportunity_present: true
  access_state: available|restricted|unknown
  observation_window_ref: null
  competing_stimuli: []
  observer_coverage: null
```

`did not approach` requires an actual opportunity to approach.

`did not explore` is weak evidence if the route was closed.

`did not interact socially` is not evidence when no other Pokémon were present.

## 4. Behavioral tendency assessment

An assessment is a versioned interpretation of repeated evidence.

```yaml
behavioral_tendency_assessment:
  assessment_id: null
  pokemon_id: null
  domain: null
  assessment_term: null
  status: insufficient_evidence|provisional|supported_for_scope|context_dependent|mixed|revised|retired
  valid_from: null
  valid_until: null
  context_scope: []
  evidence_refs: []
  contradictory_evidence_refs: []
  comparison_group_ref: null
  repeatability_basis: descriptive|quantitative|unknown
  assessor_id: null
  method_revision_ref: null
  public_label_ref: null
  notes: null
```

Recommended institutional language should be descriptive:

- `approaches novel objects earlier than the other monitored individuals in this yard`;
- `withdrawal around large visitor groups has been repeatedly observed`;
- `exploration tendency differs strongly between familiar and unfamiliar structures`;
- `current evidence is mixed`.

Avoid pretending the system has measured an eternal essence.

## 5. No universal trait dictionary required

Ouros may later author institutional vocabularies such as boldness, exploration or sociability, but this layer does not require one global taxonomy.

Different institutions can use different terminology if:

- definitions are versioned;
- underlying observations remain accessible according to privacy rules;
- mappings between terms are explicit rather than assumed.

This prevents terminology changes from rewriting Chronicle.

## 6. Context is first-class state

At minimum preserve relevant context dimensions when known:

- familiar versus unfamiliar place;
- alone versus group;
- familiar versus unfamiliar human;
- familiar versus unfamiliar Pokémon;
- food/resource present or absent;
- crowd size;
- time of day;
- season;
- current training session;
- recent relocation;
- current care/recovery state;
- breeding/courtship season if established elsewhere;
- threat present or absent;
- weather/environmental disruption when actually observed;
- observer presence and method.

Do not infer causal significance merely because a context tag exists.

## 7. Within-individual plasticity is expected

A persistent individual can change.

```yaml
behavior_change_review:
  review_id: null
  pokemon_id: null
  prior_assessment_refs: []
  later_observation_refs: []
  candidate_change_interval: null
  coincident_world_events: []
  interpretation: stable|shift_supported|context_shift|mixed|insufficient_evidence
  causal_claims: []
  assessor_id: null
```

Possible coincident events include:

- Evolution;
- age/life-stage transition;
- relocation;
- release or rehoming;
- new social group;
- training history;
- recovery from injury;
- infrastructure/environment change;
- change in observation method.

Coincidence does not prove cause.

## 8. PTU Nature firewall

PTU Nature is mechanical authoritative state.

This layer must never:

- infer Nature from behavior;
- modify Nature;
- change a Nature's stat effects;
- add a roleplay requirement to a Nature;
- claim that a Timid Nature means the individual is fearful in Chronicle;
- claim that a Brave Nature means the individual approaches danger;
- treat neutral Natures as personality absence;
- use behavioral evidence to justify a Mint or equivalent mechanical change.

The narrative system may display authoritative Nature when the game normally exposes it, but it must not reinterpret the behavioral layer through the label.

## 9. Species-lore firewall

Pokédex flavor may propose questions. It does not establish an individual's behavior.

`species described as friendly -> this individual is friendly` is invalid.

`species described as territorial -> this individual owns/defends this exact space` is invalid.

`species described as curious -> exploration assessment supported` is invalid without observations.

Species lore can inform assay design or NPC expectations, which themselves can become part of the story.

## 10. Observer labels and bias

Institutions, Trainers and communities may use informal labels.

```yaml
behavior_rating:
  rating_id: null
  pokemon_id: null
  rater_id: null
  term_used: null
  definition_ref: null
  rating_value: null
  observation_window_ref: null
  evidence_refs: []
  publication_scope: private|institutional|public
```

A caretaker saying `stubborn` is useful social history. It is not automatically scientific evidence.

Multiple raters may disagree without one being dishonest.

## 11. Public personality reputation

Public Memory may preserve labels such as:

- the cautious ferry Pokémon;
- the fearless old battler;
- the curious orchard visitor;
- the quiet Gym partner.

The public label can survive after the behavior changes.

This layer should link the reputation to current evidence but never rewrite Public Memory automatically.

## 12. Player-owned Pokémon boundary

Procedural narrative must not impose a private personality on a player's Pokémon.

Allowed:

- record actions actually produced by player choices or authoritative systems;
- note repeated observable behavior if the player has allowed autonomous behavior in that context;
- offer a researcher assessment as an in-world interpretation;
- let the player reject or ignore that interpretation.

Forbidden:

- decide the Pokémon secretly hates a teammate;
- impose fear, jealousy or trauma;
- override player-declared characterization;
- generate disobedience because an assessment says cautious;
- change battle AI based on a narrative tendency without explicit player/system authority.

## 13. Wild Pokémon individuality

This layer is especially valuable for persistent wild Pokémon.

A wild individual can become recognizable because it:

- consistently approaches observation blinds before conspecifics;
- avoids one crowded crossing but uses it at night;
- investigates new structures repeatedly;
- withdraws earlier than others under a particular disturbance;
- uses an unusual but recurring resting place;
- changes its behavior after a landscape revision.

None of those observations imply capture willingness.

## 14. Institutional and working Pokémon

Working Pokémon may show individual response patterns relevant to scheduling or welfare, but qualification remains with Working Pokémon/Care/PTU capabilities.

`repeatedly hesitates at loud machinery` may prompt a review.

It does not mean:

- unqualified;
- disloyal;
- afraid by mechanical Status;
- lower Command;
- permanently unable to work.

## 15. Structured assays

Ouros can support research assays only when Research Ethics permits them.

Potential non-mechanical assay structures:

- familiar versus novel object choice;
- two-route exploration opportunity;
- voluntary approach distance;
- latency to enter an unfamiliar but safe space;
- response to changed object placement;
- voluntary return after disengagement.

The subject must be able to stop or withdraw where project ethics requires it.

No assay grants XP, stats, Skills, Edges, Features or Nature changes.

## 16. Welfare firewall

Behavioral change can trigger a Care handoff when appropriate.

It cannot diagnose:

- pain;
- anxiety;
- illness;
- depression;
- trauma;
- cognitive decline;
- hunger;
- fatigue.

Care can later establish a diagnosis. Until then, the behavioral layer records the change.

## 17. Cognition firewall

Exploration is not intelligence.

Persistence is not intelligence.

Rapid approach is not intelligence.

Novel-object manipulation belongs to Cognition when the question concerns problem solving or tool use.

A cautious Pokémon may solve a problem quickly after choosing to engage; an exploratory Pokémon may inspect many objects without solving anything.

## 18. Social-learning firewall

Similar behavior between individuals does not prove transmission.

A juvenile matching an adult's behavior may reflect:

- independent response to the same environment;
- developmental change;
- prior training;
- social learning;
- coincidence.

Only Social Learning may promote a transmission claim.

## 19. AI boundary

Narrative tendency does not automatically become battle policy.

Forbidden mappings:

`boldness -> always attack`

`caution -> always withdraw`

`persistence -> never switch`

`sociality -> protect ally`

`aggression -> target nearest`

`exploration -> random movement`

`shyness -> lower Initiative`

`confidence -> Accuracy bonus`

If future tactical AI intentionally uses character profiles, that requires a separately reviewed contract describing which authored traits are input, how they affect choices and how player authority works.

## 20. Minecraft/Cobblemon boundary

Minecraft may render authored behavioral state:

- approach/withdrawal animation already selected by world state;
- preferred resting positions;
- inspection of an authored object;
- a callback to a known routine;
- an NPC research note.

Minecraft must not derive personality from:

- random pathfinding;
- idle animation count;
- aggro radius;
- entity facing;
- despawn;
- failure to load a chunk;
- collision avoidance;
- movement noise;
- vanilla AI target selection.

The direction is world state -> presentation, never presentation -> personality truth.

## 21. Compression rule

Do not log every ordinary action forever.

Persist detail when:

- a behavior differs from prior expectation;
- a new context is sampled;
- an assessment may change;
- a significant actor notices the behavior;
- the behavior affects care, research, work or a relationship decision;
- an unusual response creates a future callback;
- a long-running study needs another scheduled observation.

Routine repeated behavior may be summarized with links to representative observations.

## 22. Longitudinal value

This layer should support stories measured in years.

Example:

Year 1: a wild individual consistently avoids visitors but explores equipment after closing.

Year 2: a quiet research routine produces repeated voluntary approaches.

Year 3: the site becomes a public attraction and avoidance increases again.

Year 5: relocation to a quieter habitat produces a new exploration pattern.

Year 8: an old public article still calls the individual `the shy one`.

No retcon is required. Different context, current assessment and public memory coexist.

## 23. Encounter implementation contracts

### Crowded Yard Withdrawal — FULL

Narrative premise:

A persistent Pokémon known from a care/research yard repeatedly withdraws during a suddenly crowded public event. The scene goal is to clear space and avoid converting the animal's response into a hostile encounter.

Dependencies:

- targeting / footprints / range / LoS: VERIFIED for any independent battle actors;
- base movement legality: VERIFIED;
- complete movement including interception/forced movement: BLOCKING for dynamic withdrawal, crowd crossing and safe-route movement;
- core calculations: VERIFIED;
- action economy / initiative: VERIFIED;
- full turn / round lifecycle: PARTIAL;
- full stateful damage pipeline: PARTIAL;
- status lifecycle: PARTIAL if an exact Status is invoked;
- terrain / weather / hazards / zones / reactions: BLOCKING if crowd buffers or environmental areas become tactical mechanics;
- move-specific behavior: PARTIAL;
- abilities: PARTIAL;
- items: PARTIAL;
- Trainer Features / perks: PARTIAL;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for `WITHDRAW`, `AVOID_CROWD`, `REACH_SAFE_AREA` and non-KO behavior;
- Minecraft / Cobblemon / Craftics adapter/playback: BLOCKING.

REDUCED:

Suspend the event, clear visitors and resolve the Pokémon's withdrawal entirely in world state. Preserve the behavior observation. If an unrelated hostile pressure remains, run a separate static AutoPTU encounter afterward.

### Novel Corridor During Evacuation — FULL

Narrative premise:

An institution must evacuate several resident Pokémon through a newly opened corridor. Individuals respond differently to the unfamiliar route, producing a useful observation while responders manage the emergency.

Dependencies:

- targeting / range / LoS: VERIFIED for combatants;
- base movement legality: VERIFIED;
- complete movement: BLOCKING for multiple moving non-hostile objectives, crossing, withdrawal and interception;
- core calculations and action economy: VERIFIED;
- lifecycle / damage / Status / Move / Ability / Item / Feature families: PARTIAL when invoked;
- terrain / weather / hazards / zones / reactions: BLOCKING if the emergency changes the tactical environment;
- AI legal-action infrastructure: VERIFIED;
- AI tactical policy: BLOCKING for `EVACUATE`, `FOLLOW_ROUTE`, `HESITATE`, `WITHDRAW`, `REJOIN_GROUP`;
- adapter/playback: BLOCKING.

REDUCED:

Evacuation routing and individual responses resolve before combat. Record who entered, hesitated, withdrew or used an alternate safe path. Once residents and staff are out, any remaining confrontation uses a static legal arena.

### Former Partner Behavior Review — FULL

Narrative premise:

A released former partner is observed repeatedly near an old shared site but behaves differently around the former Trainer than around other visitors. Researchers want to document the pattern without assuming reunion, Loyalty or capture willingness.

Dependencies:

Ordinary static battle primitives can use VERIFIED targeting/base movement/core/action/legal-choice infrastructure if a separate confrontation occurs. Any autonomous approach/withdrawal, former-Trainer tactical relationship, escort or non-hostile goal requires complete movement, AI tactical policy and adapter/playback, all BLOCKING. Exact Loyalty/Command interactions remain mechanically unresolved.

REDUCED:

All approach/avoidance observations occur outside battle. The former Trainer cannot issue battle commands based on history alone. If an independent threat appears, run a separate static battle while the observed Pokémon withdraws through world state.

### Is This Individual Actually Consistent? — NON-COMBAT

A multi-year research review compares caretaker logs, camera records and structured observations across several contexts. `CONTEXT_DEPENDENT`, `MIXED` or `INSUFFICIENT_EVIDENCE` are successful outcomes. No battle-engine capability is required.

## 24. Capability promotion guardrail

This layer does not change the permanent engine map.

Recent Java Accuracy work is unrelated to behavioral tendency. A representative calculation primitive never authorizes a personality-driven modifier.

No battle category can be promoted because a narrative behavior is easy to describe.

## 25. Promotion gate for canon

Before any individual behavioral tendency becomes established canon, reviewers should know:

1. whose Pokémon/entity the assessment concerns;
2. which observations support it;
3. which contexts are covered;
4. whether contradictory evidence exists;
5. whether Care or another authority offers a better explanation;
6. whether the label conflicts with player-authored characterization;
7. whether the term accidentally resembles a PTU Nature or other mechanical state;
8. whether the material should remain private rather than public.

## Design objective

Ouros should make recurring Pokémon feel like individuals because the world remembers what they actually did.

The system should be comfortable saying:

`this individual often behaves this way under these conditions`.

It should resist saying:

`this is what the Pokémon essentially is forever`.