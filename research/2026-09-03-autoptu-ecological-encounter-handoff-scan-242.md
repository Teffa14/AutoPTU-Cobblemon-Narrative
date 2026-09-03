# AutoPTU ecological encounter handoff research scan — Pass 242

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-03
Canon effect: NONE

## Question

When should visible ecological behavior in the Minecraft/Cobblemon overworld cross into an authoritative AutoPTU encounter, and what information can safely cross that boundary?

This pass does not change PTU rules, species canon, Marea geography or engine readiness. It extracts reusable design structures and records provenance for an Ouros-owned handoff contract.

## Existing Ouros constraints inspected

The active ecology program explicitly requires an `AutoPTU handoff for ecological encounters` before the ecology workstream can be complete.

Existing project architecture already fixes the authority direction:

`persistent ecology -> Minecraft/Cobblemon projection -> Ouros encounter decision -> AutoPTU authoritative mechanics -> semantic result -> persistent ecology`

The current Cobblemon runtime boundary also requires Ouros to freeze combatants and reviewed tactical facts before battle creation. Nearby Minecraft entities cannot join automatically. Despawn, vanilla damage and Cobblemon battle callbacks cannot create tactical outcomes.

Pass 241 already permits ecology-driven events to remain entirely in world-state and calls AutoPTU only for optional structured conflict. Pass 242 therefore owns the missing transition contract rather than another event generator.

## New public-source scan

### Pokémon Legends: Arceus — official gameplay

Source: https://legends.arceus.pokemon.com/en-gb/gameplay/

Official material describes wild Pokémon being present and interactable in the field while a battle begins when the player deliberately throws a Pokémon at a wild Pokémon. The game presents the transition seamlessly rather than moving to a detached battle screen.

Reusable structure for Ouros:

- overworld contact and tactical engagement are separate states;
- the visual transition can be seamless while authority changes explicitly;
- world coordinates and actor identity can seed presentation without making the renderer the tactical authority.

Do not import Legends: Arceus turn rules into Ouros.

### Pokémon Legends: Z-A — official wild-zone behavior

Source: https://legends.pokemon.com/en-us/news/adventure

Official material describes wild Pokémon that may flee immediately after detecting the player. Players can hide, approach from behind, throw a ball or battle first.

Reusable structure:

- detection can produce avoidance instead of combat;
- pursuit/capture intent does not imply that every nearby Pokémon joins a battle;
- ecological behavior remains meaningful before structured engagement.

No Z-A combat mechanics are imported.

### Pokémon Ranger — official mission structure

Source: https://www.pokemon.com/uk/pokemon-video-games/pokemon-ranger

Official material frames some dangerous wild encounters around restoring calm and using Pokémon abilities to solve field problems. The important reusable structure is that a wild-Pokémon crisis can have a non-KO objective and can return to exploration after the immediate problem is handled.

For Ouros, `CALMING_WINDOW_CREATED` or `IMMEDIATE_THREAT_CONTAINED` should remain narrow semantic results. A tactical win does not automatically mean a Pokémon is permanently calm.

### New Pokémon Snap — official ecological observation

Sources:
- https://newpokemonsnap.pokemon.com/en-au/explore/
- https://newpokemonsnap.pokemon.com/en-us/create-photodex/

The official game makes repeated observation of natural behavior a primary interaction loop. The same location can expose different behavior over repeated research visits.

Reusable structure:

- observation and elicited behavior do not require combat;
- repeated contact can enrich knowledge while keeping the actor in ecological state;
- player tools can change visible behavior without automatically creating tactical state.

### PTU community practice — encounter escalation

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/xgemb5
- https://www.reddit.com/r/PokemonTabletop/comments/1bcto7a
- https://www.reddit.com/r/PokemonTabletop/comments/1gx1cz9

Community GMs repeatedly describe separating ordinary route observation/capture attempts from larger grid encounters. Several reports note that resolving every wild contact as full tactical combat becomes slow, while important, group-scale or objective-rich encounters benefit from the grid and PTU's spatial rules.

Reusable structure:

- tactical resolution should be proportional to the mechanical question;
- minor observation/avoidance can remain overworld behavior;
- rich encounters should enter the grid when range, movement, initiative, targets, objectives or damage actually matter;
- failure can mean flight, hiding or lost opportunity rather than forced KO.

These are community practices, not PTU rules authority.

### Recent PTU community discussion — groups and reinforcements

Source: https://www.reddit.com/r/PokemonTabletop/comments/1vs58fn/have_you_used_sos_and_horde_battles_in_your/

A recent community discussion highlights group wild encounters, reinforcements and the normal PTU problem of multiple actors. The key lesson for Ouros is not to infer a tactical roster from visible crowd size. Reinforcements require explicit encounter-entry legality, initiative and playback contracts.

## PTU / Kairos cross-check

The local Kairos source index routes combat to Chapter 7, movement/terrain to pp. 382+, statuses to pp. 397+, hazards to p. 401, terrain/weather to pp. 404+, encounter creation to pp. 470+ and boss encounters to pp. 485+.

Kairos is evidence that encounter creation and world population/ecosystem guidance are separate concerns. Ouros must preserve that separation. `SOURCE_HAS_RULE != OUROS_USES_RULE` remains binding.

The approved Marea first-wild-population record already freezes an exact level-5 Fletchling blueprint before Minecraft presentation and requires that the published blueprint, rather than the Cobblemon Pokémon payload, enters the encounter handoff. Pass 242 extends this from one vertical-slice actor into a general ecological transition contract.

## Reusable handoff principles

1. Detection is not battle.
2. Proximity is not battle.
3. Aggression animation is not battle.
4. Chase presentation is not automatically structured pursuit.
5. Capture intent is not automatically combat.
6. Structured PTU mechanics begin only after Ouros opens an encounter and freezes a manifest.
7. Every tactical participant must have a persistent or explicitly generated authoritative identity.
8. Noncombatants stay in ecology state unless an explicit entry transition is legal.
9. Tactical environment facts are opt-in mappings from world observations.
10. AutoPTU returns narrow semantic facts; Ouros decides ecological meaning.

## Proposed trigger families

These are design candidates, not canon rules.

`DIRECT_HOSTILE_ENGAGEMENT`
A world actor's declared behavior requires authoritative attacks, targets, range or damage.

`PLAYER_STRUCTURED_ENGAGEMENT`
The player deliberately requests a PTU action that requires initiative/action economy or tactical legality.

`CONTESTED_CAPTURE`
Capture becomes mechanically contested in a way that the active rules profile assigns to AutoPTU.

`TACTICAL_PURSUIT_OR_ESCAPE`
Success depends on footprints, movement legality, distance, interception or forced movement.

`DEFENSE_OR_ESCORT_OBJECTIVE`
Protecting an actor/area requires turn order, target legality or objective-aware tactical play.

`HAZARD_STRUCTURED_CONFLICT`
Terrain/weather/hazard/zone behavior becomes rule-critical rather than presentational.

## Stay-overworld families

Normally remain outside AutoPTU unless another trigger appears:

`OBSERVE`
`TOLERATE`
`WARN`
`HIDE`
`FLEE_WITHOUT_CONTEST`
`FORAGE`
`REST`
`NEST_ATTENDANCE`
`ROUTE_SHIFT`
`SOCIAL_SIGNAL`
`PLAYER_BACKS_AWAY`
`NONCONTESTED_WORLD_SERVICE_INTERVENTION`

Minecraft navigation may express these only within Ouros-authorized world behavior and may not fabricate PTU results.

## Handoff data-minimization lesson

The BattleSpec should receive only facts whose tactical meaning has been reviewed:

- stable participant references;
- frozen mechanical profiles;
- side/team assignment;
- approved initial positions/footprints;
- approved static geometry;
- reviewed tactical weather/terrain/hazard facts;
- declared objective/result vocabulary;
- active rules-profile identifier;
- source event/context references.

Do not forward every Minecraft fact. Visible rain may remain presentation-only. Nearby entities may remain spectators. Block collision may remain visual geometry when no PTU terrain rule is mapped.

## Return-path lesson

AutoPTU result examples safe for ecology consumption include narrow facts such as:

`TACTICAL_KO_CONFIRMED`
`TACTICAL_WITHDRAWAL_FORCED`
`ESCAPE_ROUTE_CLEARED`
`OBJECTIVE_AREA_HELD`
`CAPTURE_MECHANIC_SUCCEEDED` only if the active rules contract actually owns capture
`COMBATANT_FINAL_POSITION` only if writeback support is verified
`FINAL_HP_STATUS_INJURY_SNAPSHOT` only where persistence/writeback is verified

Unsafe direct conclusions include:

`DEAD`
`PERMANENTLY_CALMED`
`POPULATION_REDUCED`
`NEST_ABANDONED`
`EVENT_RESOLVED`
`SPECIES_DRIVEN_OUT`

Those require Ouros world-state evaluation and, when abundance changes, the demographic ledger.

## Design consequence

Ouros should implement an explicit encounter-intent evaluator before BattleSpec construction. Its job is to answer whether the current ecological interaction can remain overworld behavior or has crossed into a capability-backed tactical question.

This evaluator must fail closed. If a requested rich mechanic depends on an unverified engine family, Ouros should select an authored reduced version or keep the interaction outside combat. It must never delegate the missing rule to Cobblemon.

## Unresolved questions

- Which player intents map to structured PTU actions under the eventual active Ouros rules profile?
- When does a wild attempt to flee require tactical pursuit rather than ordinary overworld separation?
- Which capture pathways are battle-owned versus world-service-owned?
- How much HP/status/position state is safe to serialize back today?
- How should a participant re-enter overworld presentation if its Minecraft entity disappeared during battle?
- Which tactical objective result names should become stable cross-repository schemas?
