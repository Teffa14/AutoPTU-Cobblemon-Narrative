# Agreements, Mediation & Repair Research — Pass 41

Status: research/provenance only. Nothing in this file is established Ouros canon or a PTU rules source.
Date: 2026-08-19

## Gap audit

The repository already has strong layers for incidents, evidence, custody, institutional mandates, faction agendas, civic proposals, public consultation, finance, social history and public memory. The missing object is what happens after parties decide to negotiate rather than simply investigate, vote, withdraw or fight.

This pass studies persistent agreements: offers, counteroffers, temporary truces, shared-access arrangements, commitments, performance, nonperformance, revision, repair and endings.

The key design target is not a universal legal system. Ouros has not established one. The useful target is a world-state representation of what specific actors explicitly agreed to do, under which conditions, and what actually happened afterward.

## Sources inspected

### Pokémon Tabletop — Tales of Visiwa retrospective

Source: https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

A late campaign confrontation with an antagonistic clone changed through non-combat action when the party convinced the clone that she was being manipulated. The scene still had tactical stakes, but social action altered who remained committed to the confrontation and forced the larger antagonist to intervene directly.

Reusable lesson:
- negotiation can alter encounter structure without deleting earlier conflict;
- a changed position should be represented as new actor state, not a retroactive rewrite;
- persuading one member does not automatically persuade their organization;
- social resolution can expose a deeper conflict rather than end the entire arc.

Do not copy the campaign's characters, clone premise, factions or plot.

### Pokémon Tabletop — Over There! retrospective

Source: https://pokemontabletop.com/over-there-a-world-war-one-pokemon-campaign-a-retrospective/

The campaign repeatedly used cooperation between actors who did not begin aligned. PCs with opposing loyalties had to cooperate for survival, and sustained conversation could change the position of an important enemy actor.

Reusable lesson:
- shared immediate goals can create bounded cooperation;
- cooperation does not erase ideological conflict;
- trust can be historical and gradual rather than a single binary flag;
- a temporary arrangement can end without either side being treated as a traitor.

Do not import the campaign's historical setting, political identities, characters or legendary roles.

### Pokémon animation — Pokémon Ranger: Deoxys' Crisis, Part 2

Source: https://www.pokemon.com/us/animation/seasons/9/episode-27-pokemon-ranger-deoxys-crisis-part-2

Team Rocket temporarily cooperates with Ash's group because both sides need to rescue missing companions during a larger crisis.

Reusable lesson:
- a truce can be purpose-limited;
- cooperation can coexist with unchanged faction identity;
- the truce can expire naturally when the shared objective ends;
- a crisis can make previous opponents temporarily interdependent.

Ouros should preserve the distinction between `temporary cooperation` and `alliance`.

### Pokémon Ranger: Guardian Signs — The Elderly Couple's Argument

Source: https://www.serebii.net/ranger3/quests.shtml

A disagreement about a supposedly moving rock is resolved by investigating the disputed event and returning with the Geodude that caused the observation.

Reusable lesson:
- some disputes should be solved by evidence before bargaining begins;
- a mediator/investigator should not force compromise when one factual question can be checked;
- the result can change actor beliefs without creating a permanent relationship label.

### Pokémon Tabletop Reunited: Evolved — Social Encounters

Source: https://2e.ptr.wiki/rules/social-encounters

This is a later Pokémon tabletop design reference, not PTU/Caelo authority. It is useful because it explicitly frames social interaction around a concrete requested goal and warns that forcing player-character behavior through persuasion risks removing player agency.

Reusable lesson only:
- state the requested outcome explicitly;
- distinguish a smaller request from a stronger one;
- do not treat surrender, withdrawal and alliance as equivalent outcomes;
- player consent needs stronger protection than NPC persuasion.

Do not import its clocks, CRs, skill names, tables or numerical mechanics into Ouros.

### Negotiation history in multiplayer games

Source: https://arxiv.org/abs/2311.08666

The study analyzes more than 10,000 chat messages from Diplomacy and finds that prior negotiation history matters for modeling longer-term outcomes. The game is not a model for Pokémon politics, but the research supports preserving negotiation provenance rather than treating every conversation as an isolated fresh state.

Reusable lesson:
- keep proposal/version history;
- preserve fulfilled and broken commitments;
- later actors may base expectations on recorded prior interactions;
- history should inform future proposals without becoming a hidden universal morality score.

## Structures worth reusing

A useful agreement system needs more than a `relationship +1` result. It should preserve:

- parties;
- subject of disagreement;
- factual claims that remain disputed;
- interests and constraints each party has actually expressed;
- offers and counteroffers;
- exact accepted commitments;
- conditions and dependencies;
- duration or expiry when relevant;
- observers/witnesses only when present;
- evidence of performance;
- claims of nonperformance;
- revisions;
- termination state;
- later public interpretation.

## Important separations

Conflict is not automatically a case.

A complaint is not world truth.

A discussion is not a negotiation.

An offer is not acceptance.

Acceptance is not friendship.

A truce is not an alliance.

An agreement is not automatically legally enforceable.

Nonperformance is not automatically bad faith.

Repair is not forgiveness.

Restitution is not ownership transfer unless the underlying ownership state supports it.

## Player agency rule

Ouros should never use a generated social roll to force one player character to accept a contract, romance, friendship, surrender, confession, alliance or other enduring personal commitment.

For PC-to-PC agreements, the authoritative source of acceptance must be explicit player-authored consent or another future rule that the project deliberately adopts after review.

A social mechanic may change information, access, credibility, NPC willingness or negotiation conditions when PTU/Caelo explicitly supports it. It must not fabricate PC consent.

## Pokémon consent boundary

Wild or nonverbal Pokémon can display observable preferences, avoidance, cooperation, refusal and repeated behavior. That does not make them contract signatories.

A proposed agreement involving a Pokémon must distinguish:
- human/institutional commitments about their own behavior;
- observed Pokémon behavior;
- ownership/custody claims;
- any mechanically or canonically supported communication route.

The generator must not invent legal consent, ownership transfer or verbal agreement for a Pokémon because doing so would produce a convenient ending.

## PTU/Caelo boundary

The Python project contains authoritative representations of social skills such as Charm, Command, Guile, Intimidate and Intuition. This is evidence that social competence matters in the PTU implementation, not a license to invent a mediation subsystem.

Before any mechanical social-resolution rule is implemented, the project still needs an exact extraction of the governing PTU/Caelo text for:
- relevant Skill Checks;
- opposed social checks;
- Command/Charm/Guile/Intimidate/Intuition interactions;
- coercion or surrender if defined;
- any Caelo-specific modifications.

Until then, agreements are persistent narrative/world state, not a replacement rules engine.

## Design lessons for Ouros

1. Evidence can precede negotiation.
2. A shared temporary goal can justify a truce without changing allegiance.
3. Parties can agree on actions while disagreeing about motives or history.
4. Agreements should contain observable commitments rather than inferred emotions.
5. Fulfillment, partial fulfillment, delay and failure need different states.
6. A broken commitment needs a cause record before assigning intent.
7. Renegotiation is a valid continuation, not automatic failure.
8. Refusal is a legitimate outcome; the generator should not force a 'good ending'.
9. Repair can be physical, informational, procedural or relational without requiring currency.
10. Agreement history should feed future world reactions while preserving provenance.

## Copyright and provenance rule

External campaigns, episodes, game quests and tabletop systems are used only for high-level structural analysis. Ouros proposals must not copy distinctive characters, dialogue, organizations, scenes or plot sequences. Source attribution remains attached to research notes, while final Ouros content must be independently authored.