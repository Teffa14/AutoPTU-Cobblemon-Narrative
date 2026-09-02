# Sendero wild approach and escalation seeds — Pass 214

Status: PROPOSED / NON-CANON
Date: 2026-09-02

## Scope

This proposal operationalizes the species-grounded wild-behavior policy using existing Marea/Sendero canon. It does not add a new town, faction, resident, wild species or canonical personality.

The existing persistent lower-shelf actor remains `ouros.marea.encounter.sendero_lower_shelf.fletchling.0`: level 5, Big Pecks, Tackle, Growl, Overland 3, Sky 5, no held item, no starting status or Injury. Its canon explicitly forbids assuming that the actor is always aggressive.

## Seed: The Same Bird, Different Approach

Premise: the same persistent Fletchling can produce different encounters because the Trainer behaves differently and because current world state differs.

Possible first observations are deliberately non-authoritative about emotion: perched, feeding, moving along the shelf, watching traffic, already departing, or absent because the actor is elsewhere. The server records position/activity facts; it does not label the Pokémon friendly, afraid or hostile without an approved behavior transition.

Trainer choices can include keeping distance, moving parallel to the bird, approaching directly, running, breaking or opening line of sight, placing a Pokémon visibly nearby, withdrawing, attempting a legal interaction, or preparing a capture/control tactic.

The response is selected from species/population prior + current Fletchling state/capabilities + observed Trainer behavior + local context. No fixed `Fletchling aggression = X` value is proposed.

## Seed: The Exit Matters

Premise: a normally viable withdrawal can become a different problem when the Trainer's position removes the preferred escape lane.

For the canonical actor, Sky 5 is an authored mechanical capability, but exact pathing, tactical movement and any interception remain engine-owned. If the Trainer unintentionally blocks a ground approach while aerial departure remains legal, the policy should consider that actual option. If no safe/legal withdrawal exists, escalation may prefer warning, evasion, obstruction or engagement according to verified policy inputs.

The narrative layer cannot declare the Fletchling trapped because it appears boxed in visually. `TRAPPED_OR_CONSTRAINED` requires an authoritative mechanical/world condition.

## Seed: Quiet Observation

Premise: the player wants information rather than capture.

The player can reduce pressure by stopping pursuit, keeping an exit open and using only source-verified observation/approach actions. Successful observation may reveal bounded facts such as location, current activity, warning display or departure direction. It does not reveal hidden stats, friendship, inner thoughts or ecological conclusions that were not observed.

This is useful for Sendero's existing fieldwork and evidence systems because wildlife can be meaningful without becoming a battle or collection opportunity every time.

## Seed: Capture Preparation Changes the Encounter

Premise: a player tries to improve a future capture opportunity instead of immediately throwing a Ball.

Potential tactics, only where PTU/AutoPTU verifies them, include concealment, positional funneling, cutting off an exit, hindering movement, trapping/restraint, applying a relevant Status Affliction, using an Item, Move, Ability or Trainer Feature, and coordinating allied participants.

The important behavioral consequence is that preparation is observable when appropriate. A wild Pokémon that detects containment or status setup can change intent before the Trainer gets the desired advantage. The AI must compare what the Pokémon can actually do against what the Trainer is actually doing.

No tactic receives a numeric bonus in this proposal.

## Rich encounter: Lower Shelf Containment Attempt

A Trainer actively tries to capture the persistent lower-shelf Fletchling while preserving its identity and world state.

Full intended form:

The Fletchling begins from an authored behavior state derived from current context. The Trainer can approach, conceal, reposition, deploy a Pokémon, use legal control/status tools or attempt capture. The Fletchling can use only its real legal options and can prioritize tolerance, warning, withdrawal, evasion, obstruction, engagement or disengagement according to tactical policy. Range/LoS and footprints matter. If the Trainer blocks escape, complete movement/interception may matter. Growl/Tackle and Big Pecks matter only to the extent their exact mechanics are implemented. Any status, Item, capture, trapping or Feature effect is resolved by AutoPTU. Final capture/escape/battle state reconciles back into the persistent world actor.

This encounter therefore depends on all permanent capability families when all tactic branches are enabled: targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions when environmental tactics use them; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

## Reduced encounter: Approach, Warn, Withdraw or Battle

The same premise can run before the rich dependencies are complete.

The server evaluates an authored behavior state from species/population context, current individual state, authoritative distance/visibility inputs and a narrow set of explicit Trainer approach choices. The Fletchling can visually tolerate, become alert, warn or withdraw through server-directed world movement only where normal world traversal is authoritative. The player may stop, back away or continue.

If continued interaction legally starts combat, create the existing normal BattleSpec using the frozen Fletchling blueprint. Do not simulate missing stealth bonuses, capture preparation, traps, statuses, interception, reactions or forced movement. Do not have Minecraft decide whether Growl, Big Pecks or a Poké Ball succeeds.

This preserves the behavioral premise: the player can influence whether the meeting escalates without requiring the adapter to duplicate PTU rules.

## Population tolerance boundary

Sendero may eventually establish a population-level human-exposure context because it is a traveled route. That fact is not yet enough to assign a numerical tolerance threshold.

A future canon record should distinguish population exposure from persistent-individual history. A repeatedly threatened individual may react differently from another member of the same local population. A single assisted encounter also cannot produce automatic friendship or domestication.

## Observable state cues

Minecraft can present behavior through movement, facing, distance change, calls, short animation and departure. These cues should map from a server-owned behavior state. They cannot create the state themselves.

Avoid floating diagnostic text such as `ALARM +2` or `TOLERANCE -1` in player-facing presentation. The player should read the Pokémon's visible behavior and world context while debug tooling can expose the full transition record when needed.

## Canon questions

Before promotion, decide whether Sendero has enough routine traffic to canonize a local habituation band; what source-backed Fletchling tendencies Ouros accepts from Caelo/Pokédex material; whether this particular persistent individual has any authored prior interaction history; and which observations are visible without a Skill check.

## Mechanical questions

Exact PTU/Caelo/Kairos review remains required for capture action/range, Stealth/detection, Charm/Command/Intuition/Survival uses, Features/Edges affecting approach or handling, trapping/restraint, movement hindrance, relevant Status Afflictions, Poké Ball modifiers, interception and reaction rules.

## Canon effect

None. This file supplies implementation-ready encounter structure while preserving the frozen Fletchling blueprint and existing Marea facts.