# Sendero Alarm-Network Seeds — Pass 215

Status: PROPOSED / NON-CANON
Date: 2026-09-02

## Purpose

This proposal applies pass 215's signal-propagation research to Sendero del Vidrio without changing established Marea canon.

The canonical lower-shelf Fletchling remains exactly the existing persistent level-5 individual with Big Pecks, Tackle, Growl and its frozen movement profile. No second species, flock membership, family relation, nest, mate, offspring, territorial claim or social hierarchy is canonized here.

## 1. A Cry Travels Up the Shelf

Premise:

The player approaches the lower-shelf Fletchling in a way that moves it from tolerant/aware behavior into ALERT or WARNING. The Pokémon produces an observable vocal or display signal only if future species-behavior review authorizes that expression.

The important event is what happens nearby.

Possible observed consequences:
- another wild actor becomes alert without approaching;
- a nearby unidentified actor withdraws from cover;
- several distant movement cues stop at roughly the same time;
- nothing answers at all;
- another actor reacts to the Trainer directly rather than to the Fletchling;
- a later field observation suggests that the apparent cascade was coincidence rather than communication.

The encounter records provenance instead of deciding immediately which interpretation is true.

Candidate records:

```yaml
signal_event:
  source: ouros.marea.encounter.sendero_lower_shelf.fletchling.0
  source_state: ALERT_OR_WARNING
  trigger_actor_id: player
  trigger_action_ref: null
  observed_channel: VOCAL_OR_DISPLAY_TBD
  receivers_confirmed: []
  receivers_possible: []
  interpretation_claims: []
```

No wild actor is spawned merely because this record exists.

## 2. Was It Warning Them or Warning You?

A later observation creates a small research question for Nerea or Ema.

The player has several hypotheses:
- the Fletchling warned conspecifics;
- nearby Pokémon were eavesdropping;
- all actors independently noticed the same Trainer behavior;
- the sound was a normal contact/display behavior unrelated to danger;
- the apparent pattern was incidental.

The quest should not use one hidden 'correct dialogue option'. Evidence can come from repeated observation, distance, timing, line of sight, direction of movement and whether the same pattern appears when no Trainer pressure exists.

Outcome:

The player may reduce uncertainty without establishing a final biological rule from one event.

## 3. The Alarm Outlives the Threat

A disturbance has ended, but one or more nearby wild actors remain alert for a short, server-authored persistence window.

This creates a different world state from permanent hostility.

Possible consequences:
- observation becomes harder because animals remain concealed;
- the player waits and the local behavior settles;
- moving farther away reduces pressure;
- another player arriving shortly afterward encounters an already-alert local context;
- the state expires without producing a quest or battle.

This is useful in multiplayer because wildlife can remember a recent event without attributing the event personally to every later Trainer.

## 4. Do Not Chase the Cascade

A Trainer notices several wild actors withdrawing after the initial Fletchling warning.

The player can:
- stop and preserve distance;
- follow one withdrawing actor;
- move laterally instead of directly pursuing;
- return after the area settles;
- attempt a legal observation/handling tactic once exact PTU support exists.

Following a receiver may increase its own alarm state even if it had no prior relationship with the original Fletchling.

This makes the player's behavior propagate through the ecology without a global aggro flag.

## 5. Proposed mixed-species response candidate

No responder species is selected yet.

Future ecology work may add a species whose official/PTU/Caelo evidence supports one of these roles:
- listens to nearby warning activity;
- reacts to sudden flock movement;
- shares the same refuge and copies withdrawal;
- actively mobs a threat;
- ignores other species and responds only to direct perception.

Species selection must occur in a separate ecology/canon review. This pass deliberately leaves the slot unresolved rather than inventing a convenient responder.

## 6. Mechanically rich encounter: Signal Chain at the Lower Shelf

Intended full version:

The Trainer pressures one wild Pokémon while other nearby actors receive partial information and make their own tactical choices.

Potential full behaviors:
- the Fletchling warns and withdraws using its actual Sky/Overland options;
- one receiver moves to a vantage point;
- another receiver opens distance;
- a species-backed defender or mobber may approach;
- the Trainer attempts to block, trap, hinder or status one actor;
- a second actor may exploit or avoid the changed route;
- a legal active-battle reinforcement could occur only if AutoPTU supports participant entry during the lifecycle.

Narrative objective:

Understand and navigate a changing wildlife situation rather than defeat every visible Pokémon.

Possible successful outcomes include:
- all wild actors leave safely;
- the player gets a clean observation without escalation;
- one actor remains while the others disperse;
- the player intentionally disengages;
- a battle occurs with only the actors actually authorized as participants.

The full encounter must never convert every receiver into an enemy.

## 7. Reduced version: Hear, React, Settle

This version can run before reinforcement and tactical-policy support is complete.

Flow:
1. Server evaluates the canonical Fletchling's current tolerance state.
2. An observed Trainer action changes the Fletchling's behavioral intent.
3. If a source-backed warning signal is authorized, the server emits a semantic signal event.
4. Nearby future wild actors may receive a simple ALERT/WITHDRAW world-policy transition.
5. Minecraft plays visible orientation, spacing, departure or concealment cues.
6. The player may stop, move away, wait or continue approaching.
7. If a normal battle starts, only the normal audited BattleSpec participants enter AutoPTU.
8. No off-screen combat, free status, free interception or phantom reinforcement is simulated.

This preserves the premise: wildlife responds to wildlife information and Trainer pressure.

## 8. Dependency classification

Targeting/footprints/range/LoS:
Required for determining who could directly perceive the Trainer or the signal and for tactical versions. Current classification: VERIFIED within audited contracts.

Base movement legality:
Required for withdrawal/repositioning. VERIFIED within audited contracts.

Complete movement including push/pull/knockback/interception/forced movement:
Required only for rich containment/interception branches. PARTIAL.

Core calculations:
Required if combat or rule-backed checks enter the scene. VERIFIED within audited contracts.

Action economy/initiative:
Required for battle-time signal/reaction behavior. VERIFIED within audited contracts, but does not itself prove dynamic participant entry.

Full turn/round lifecycle:
Required for mid-battle signaling, delayed response and reinforcement timing. PARTIAL.

Full stateful damage pipeline:
Required for arbitrary combat escalation. PARTIAL.

Status lifecycle:
Required if Trainer tactics use status to prevent signaling, movement or capture resistance. PARTIAL.

Terrain/weather/hazards/zones/reactions:
Required for reaction attacks, environmental concealment/control or hazard-mediated response. BLOCKING for those branches.

Move-specific behavior:
Required for any Move used to signal, hinder, attack, withdraw or control. PARTIAL.

Abilities:
Required for Ability-driven response/control. PARTIAL.

Items:
Required for bait, capture or tactical item branches. PARTIAL.

Trainer Features/perks:
Required for Feature/Edge-based handling, detection, containment or reaction changes. PARTIAL.

AI legal-action infrastructure:
Required to expose legal movement/action options. VERIFIED within audited contracts.

AI tactical policy:
Required for each receiver to choose independently among watch, withdraw, guard, investigate or engage. BLOCKING for the full version.

Minecraft/Cobblemon/Craftics adapter/playback support:
Required to render the signal and receiver responses and reconcile any battle/capture result. PARTIAL/BLOCKING end-to-end.

## 9. Canon boundaries

This proposal does not establish:
- that the lower-shelf Fletchling has a flock;
- that it calls for allies;
- that it has a mate, nest or dependent;
- that any specific second species inhabits the site;
- that alarm calls grant combat bonuses;
- that a receiver enters combat automatically;
- that Sendero has a universal aggression or tolerance score.

## 10. Canon-review questions

1. Which official/PTU/Caelo Fletchling behavior statements are accepted for warning/contact signaling?
2. Does Sendero canon support enough human traffic to define a local habituation context?
3. Which second wild population should be added next, and does its source-backed behavior make it a plausible signal receiver?
4. Should recent area-level disturbance persist independently from individual memory?
5. What server object owns signal events and reception records across unload/reload?
6. Can an AutoPTU battle accept a new participant after battle start, and if so under what lifecycle/initiative contract?

## Design value

Sendero can become ecologically reactive before it becomes densely populated. A single canonical wild Pokémon can create observable consequences beyond itself, while every additional biological interpretation remains proposed until evidence and future population canon support it.