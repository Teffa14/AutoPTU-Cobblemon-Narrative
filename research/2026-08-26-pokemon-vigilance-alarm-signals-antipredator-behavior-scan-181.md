# Research Scan — Pass 181 — Vigilance, Alarm Signals and Anti-Predator Behavior

Status: RESEARCH / PROVENANCE ONLY / NON-CANON
Date: 2026-08-26

## Scope

This pass investigates how Ouros can represent vigilance, sentinel behavior, alarm signals, false alarms, risk tradeoffs, collective warning, mobbing-like responses and predator-avoidance behavior without duplicating existing authorities or inventing PTU mechanics.

Existing authority remains with:

- `wild-collective-agency-layer.md` for persistent groups and group-scale responses;
- the Pass 51 interspecies ecological-relations layer for predator/prey and other ecological relations;
- `soundscapes-acoustic-ecology-layer.md` and passive-acoustic monitoring for acoustic observations;
- `pokemon-social-learning-behavioral-traditions-layer.md` when a response is socially transmitted;
- `pokemon-spatial-ecology-home-ranges-territoriality-layer.md` for spatial-use interpretation;
- Care for welfare/clinical interpretation;
- AutoPTU/PTU/Caelo for any tactical effect.

The missing layer is the behavioral observation and interpretation boundary between detecting possible risk and deciding what a collective actually does with that information.

## Source 1 — Watchog as an official Pokémon precedent

Pokémon's official Pokédex classifies Watchog as the Lookout Pokémon. Its current entry describes a visible defensive response when it sees an enemy, while the page separately lists Keen Eye and Illuminate as battle Abilities.

Reusable structure:

`possible threat detected -> visible alert response -> other behavior may change`

Do not import:

- automatic sentinel assignment to every Watchog group;
- free Perception checks;
- Accuracy bonuses;
- stun effects from narrative lookout behavior;
- permanent leader status.

Source: Pokémon.com, Watchog Pokédex.
https://www.pokemon.com/us/pokedex/watchog

## Source 2 — SOS battles as a call-for-help precedent

Pokémon's official description of Alola SOS battles establishes that some wild Pokémon can call for help during battle and that another wild Pokémon may answer. The game also includes species-specific and context-specific outcomes.

Reusable high-level lesson:

- warning/calling behavior can be conditional;
- a signal can recruit another actor;
- the responder need not always be the same species;
- the consequence belongs to a particular game system and cannot be generalized into ecology automatically.

For Ouros, an ecological alarm or recruitment call is world-state evidence unless an exact PTU/Caelo mechanic is validated. It must not silently reproduce the SOS battle subsystem.

Source: Pokémon.com, “Special Pokémon Answer the Call for Help in SOS Battles.”
https://www.pokemon.com/uk/features/special-pokemon-answer-the-call-for-help-in-sos-battles

## Source 3 — Group vigilance and alarm information

USGS material on black-tailed prairie dogs documents how alarm playback can increase vigilance and reduce foraging, while other call types can produce different behavioral responses. The important design lesson is that public information can change group behavior without proving that every individual detected the original threat.

Reusable structure:

`signal perceived -> receiver behavior changes -> opportunity cost appears`

Potential Ouros consequences:

- shorter foraging windows;
- delayed movement;
- increased watch behavior;
- use of shelter or cover;
- a collective becoming harder to observe;
- a temporary change in route use.

None of these are combat modifiers by default.

Sources:

- USGS, black-tailed prairie dog response to conspecific signals.
https://www.usgs.gov/publications/black-tailed-prairie-dog-cynomys-ludovicianus-sciuridae-metapopulation-response-novel
- USGS, sea otter predator-avoidance behavior summary.
https://pubs.usgs.gov/publication/70222087

## Source 4 — Sentinel systems can carry graded information

Research on meerkat sentinel systems shows that different call types can correspond to different perceived risk states and change the balance between vigilance and foraging in receivers.

Reusable structure:

`sentinel present -> signal class -> receiver response -> tradeoff`

Ouros should not reduce alarm systems to a binary `danger=true` flag. A local tradition may distinguish ordinary watch calls, elevated concern, immediate alarm and all-clear states if observation supports those distinctions.

Source: Rauber & Manser, Scientific Reports, “Discrete call types referring to predation risk enhance the efficiency of the meerkat sentinel system.”
https://www.nature.com/articles/srep44436

## Source 5 — Noise can change warning systems without changing predator presence

USGS synthesis on anthropogenic noise notes that noise can alter vigilance, foraging and acoustic communication. In some systems it can mask alarm signals or change behavioral responses without any actual increase in predator abundance.

Reusable Ouros structure:

`communication environment changes -> alarm detectability changes -> collective behavior changes -> public interpretation may blame the wrong cause`

This connects cleanly with Soundscapes, Rail/Road infrastructure and Urban Wildlife.

Source: USGS, “Effects of noise from oil and gas development on ungulates and small mammals.”
https://pubs.usgs.gov/publication/sir20235114/full

## Source 6 — Anti-predator behavior matters for conservation but should remain evidence-driven

USGS research on animal behavior in conservation highlights that anti-predator and social behavior are often underused in management despite their potential relevance.

Design lesson for Ouros:

behavior can legitimately inform conservation decisions, but a behavioral observation is not equivalent to a population trend, welfare diagnosis or causal proof.

Source: USGS, “A systematic survey of the integration of animal behavior into conservation.”
https://www.usgs.gov/publications/a-systematic-survey-integration-animal-behavior-conservation

## Source 7 — Mobbing and collective defense are not the same as battle teams

Recent behavioral literature describes mobbing-like responses in which animals approach, harass or vocalize toward predators or competitors, sometimes recruiting conspecifics or heterospecifics.

Reusable structure:

`risk source -> recruitment or approach -> local collective defense -> disengagement`

Ouros must not map this directly to Pack Mon, shared initiative, free reactions or coordinated AI. It is a behavioral interpretation layer first.

Source: Scientific Reports 2026 reference material on mobbing-like behavior and acoustic recruitment.
https://www.nature.com/articles/s41598-026-35574-7

## Source 8 — PTU community encounter design favors motive before combat

The public Pokémon Tabletop encounter-creation material emphasizes that wild Pokémon may protect eggs, vulnerable members or territory, and that external disturbance can change disposition. This supports encounters where warning and defensive behavior communicate motive before battle begins.

Reusable structure:

`world-state pressure -> warning/defensive behavior -> player interpretation -> optional escalation`

Do not import encounter difficulty math or homebrew mechanics.

Source: Pokémon Tabletop community Encounter Creation Guide.
https://pokemontabletop.fandom.com/wiki/Encounter_Creation_Guide

## Source 9 — PTU community precedent for avoiding unnecessary escalation

A public PTU campaign log records a scene where damage to a tree leads a nearby Pokémon protecting eggs to react; the party learns the reason and restores vegetation rather than treating the situation as a mandatory capture or knockout encounter.

Reusable structure:

`disturbance -> defensive signal/action -> new information -> repair/withdrawal resolution`

The specific characters, species details and plot are not imported.

Source: r/PokemonTabletop campaign log #24.
https://www.reddit.com/r/PokemonTabletop/comments/wudfhz

## Design synthesis

The strongest reusable distinctions are:

1. threat presence versus perceived risk;
2. original detector versus receivers of a signal;
3. signal emission versus signal reception;
4. reception versus interpretation;
5. vigilance versus alarm;
6. alarm versus recruitment;
7. recruitment versus coordinated combat;
8. false alarm versus deception;
9. vigilance cost versus population decline;
10. collective response versus individual future choice.

A good Ouros incident can therefore be interesting even when no predator is found. Examples include a rail-noise corridor causing repeated missed alarms, a habitual lookout leaving a group, a false alarm produced by a harmless disturbance, or two species responding differently to the same warning signal.

## Mechanical guardrails

Do not infer:

- vigilance -> Perception bonus;
- lookout role -> Keen Eye;
- alarm call -> Intimidate;
- warning display -> Frightened/Confused/Flinch;
- sentinel -> free reaction;
- mobbing -> Pack Mon;
- group warning -> shared initiative;
- signal received -> omniscient threat location;
- SOS-battle precedent -> automatic reinforcement mechanic;
- noise masking -> Accuracy penalty;
- shelter-seeking -> forced movement;
- watch behavior -> Trainer Feature/Edge;
- repeated false alarms -> stupidity or reduced intelligence.

Exact PTU/Caelo rules remain authoritative when any named Move, Ability, Status, Feature, Capability or Skill is invoked.

## Canon status

No Watchog colony, sentinel system, alarm vocabulary, predator relation, mobbing tradition, research network or noise-impact site is established as Ouros canon by this document.
