# Ouros Narrative Research — Alarm Propagation, Social Information & Cascading Wild Response — Pass 215

Status: RESEARCH ONLY / NON-CANON
Date: 2026-09-02

## Scope

Pass 11 already established persistent wild collectives, group lifecycle, territory/resource use and collective-scale disturbance. Pass 214 established species-grounded individual tolerance and tactical response to Trainer behavior. This pass addresses a narrower missing layer: one wild Pokémon can change the behavior of nearby Pokémon by producing or relaying information about danger.

The design problem is not simply `call ally -> spawn combatant`. Ouros needs to distinguish direct perception, same-species warning, mixed-species eavesdropping, group aggregation, dispersal and false or stale alarm propagation.

Nothing here grants a Move, Ability, Pack Mon effect, reaction, intercept, summon or free action. Exact mechanics remain PTU/Caelo/Kairos + AutoPTU authority.

## 1. Pokémon Sun/Moon SOS Battles — assistance depends on species and current pressure

Sources:
- https://bulbapedia.bulbagarden.net/wiki/SOS_Battle
- https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_call_rate

Generation VII explicitly represents some wild Pokémon calling for assistance. The baseline likelihood differs by species, and current battle pressure can increase calling probability. Some species never call at all.

Reusable structural lesson:

`wild Pokémon under pressure` does not imply `automatic reinforcements`.

Ouros translation:
- species/population behavior can include a source-backed tendency to signal or seek nearby support;
- whether anyone can hear/observe the signal is a separate world fact;
- whether another Pokémon responds is a separate decision;
- responding does not automatically mean entering combat;
- a responder may warn, withdraw, gather, guard, observe, move vulnerable members or engage depending on its own species/individual/context policy;
- main-series call rates and numeric multipliers are not imported as Ouros rules.

## 2. Horde encounters — co-presence is not proof of coordinated social structure

Source:
- https://bulbapedia.bulbagarden.net/wiki/Horde_encounter

Horde encounters show several wild Pokémon appearing simultaneously, usually of one species but sometimes with another species mixed in. Their game representation creates tactical numerical pressure, but it does not by itself prove persistent hierarchy, kinship or a permanent collective.

Reusable lesson:

A signal can produce local co-presence without proving a pack/flock identity.

Ouros should keep separate:
- pre-existing collective membership;
- temporary aggregation;
- signal responders;
- tactical encounter participants.

## 3. Real-world alarm calls — signals can trigger coordinated defensive behavior

Source:
- https://www.nature.com/articles/srep34471

Research on Hainan gibbons documents alarm calls followed by group defensive/mobbing responses. The signal changes what nearby group members do before any physical attack occurs.

Reusable lesson:

An alarm is information that can change policy state. It does not need to be modeled as damage, status or combat initiative.

Potential Ouros response transitions include:
- tolerant -> alert;
- feeding -> watch;
- exposed -> concealed;
- dispersed -> clustered;
- adult/independent movement -> move vulnerable member;
- passive observation -> warning display;
- withdrawal -> coordinated withdrawal;
- local avoidance -> mobbing/harassment only where species evidence supports it.

## 4. Public information and eavesdropping — the receiver can distinguish signal provenance

Source:
- https://www.nature.com/articles/s41467-020-14414-w

Nuthatch research shows that animals can react to direct predator information differently from alarm information obtained indirectly from another species. This is especially useful for Ouros because it supports provenance-aware wildlife knowledge without anthropomorphic reasoning.

Reusable lesson:

A receiver should be able to know `another animal signaled danger here` without knowing exactly what the danger is.

Candidate signal evidence:

```yaml
wild_signal_event:
  signal_event_id: null
  source_pokemon_id: null
  source_collective_id: null
  signal_class: ALARM | WARNING | CONTACT | GATHER | OTHER_OBSERVED
  trigger_fact_refs: []
  source_directly_perceived_trigger: unknown
  location_id: null
  timestamp: null
  observable_channel: null
  audience_candidate_ids: []
  mechanics_refs: []
```

Candidate reception evidence:

```yaml
wild_signal_reception:
  signal_event_id: null
  receiver_id: null
  reception_state: HEARD_OR_SEEN | NOT_CONFIRMED
  receiver_knows_source: unknown
  receiver_knows_trigger: unknown
  resulting_behavior_intent: null
  resulting_action_ref: null
```

The receiver's interpretation remains bounded. A warning signal can raise alarm without transferring omniscient knowledge of the Trainer's Moves, inventory or intent.

## 5. Disturbance type can change collective response

Source:
- https://www.nature.com/articles/srep28641

Pilot-whale research reports different social responses to different disturbance types. Grouping, synchrony, spacing and vocal response were not one fixed panic behavior.

Reusable lesson:

Signal response should remain species/context dependent. `ALARM` is not a universal command to attack.

A locally habituated population may respond to a running human differently from an unfamiliar predator, violent battle, capture attempt or repeated pursuit. This extends pass 214's human-density tolerance model to social information.

## 6. PTU community experience — ecological scenes become stronger when several Pokémon have their own reason to be there

Sources:
- https://www.reddit.com/r/PokemonTabletop/comments/11tn2q5
- https://www.reddit.com/r/PokemonTabletop/comments/vsv8xg
- https://www.reddit.com/r/PokemonTabletop/comments/jivcud

Public PTU discussions describe territory conflicts, predation, groups surrounding a target, defensive areas and encounters where players can avoid alarming a group rather than simply starting combat. They also warn that repeated individual capture scenes can consume session time and stall the campaign.

Reusable lesson:

A cascading response should create a world situation, not automatically create N sequential capture battles.

Good outcomes can include:
- the original Pokémon escapes because nearby warning activity creates confusion;
- multiple wild actors retreat together;
- a route becomes temporarily difficult to cross;
- the player stops pursuit and watches the group settle again;
- another species reacts to the alarm but never joins the fight;
- the player discovers that the apparent 'reinforcement' was independently fleeing the same threat.

Community reports are practice evidence, not rules authority.

## 7. Design distinction from Wild Collective Agency

Pass 11 already owns persistent group identity and collective state. This pass adds signal flow between actors.

A signal may travel:
- individual -> individual;
- individual -> persistent collective;
- collective member -> visible subgroup;
- one species -> another species that eavesdrops;
- environment/actor -> multiple independent receivers without any inter-animal signal.

The final case matters. If three Pokémon flee after the Trainer uses a loud Move, Ouros should not infer that Pokémon A warned B and C unless the signal itself was observed or source-backed.

## 8. Anti-anthropomorphism and provenance guardrails

Do not convert alarm propagation into human-style communication unless species/setting evidence supports it.

A receiver may infer:
- disturbance nearby;
- direction/source of a signal;
- urgency band;
- familiar caller identity if established;
- a species-specific meaning supported by evidence.

A receiver should not automatically infer:
- the Trainer's private motive;
- exact HP or Stats;
- exact inventory;
- hidden Move/Feature availability;
- canonical cause of an unexplained event;
- moral intent;
- friendship/loyalty between caller and receiver.

## 9. Engine-aware implementation lesson

The world-policy layer can create semantic `wild_signal_event` and `wild_signal_reception` records before full tactical AI exists.

Full tactical consequences require exact capability families depending on the response:
- simple alert/withdraw presentation: targeting/range/LoS, base movement legality, AI legal actions, adapter/playback;
- route blocking/interception/containment: complete movement + AI tactical policy;
- status/control responses: status lifecycle + move/ability/item/Feature behavior;
- reactive warning attacks or interrupts: terrain/weather/hazards/zones/reactions plus relevant Move/Feature contracts;
- multiple new battle participants joining an active BattleSpec: full lifecycle, initiative, participant/reinforcement contract, AI policy and adapter reconciliation.

No narrative signal may insert a combatant into AutoPTU unless an audited engine contract authorizes that transition.

## 10. Main design conclusions

1. Alarm signals are provenance-bearing world events, not automatic combat summons.
2. Species behavior controls whether signaling is plausible; current individual state controls whether the actor can/does signal.
3. Receivers run their own behavior policy after receiving information.
4. Direct observation and second-hand wild information remain distinct.
5. Mixed-species eavesdropping can exist without friendship, symbiosis or collective membership.
6. Local human habituation can influence response thresholds without producing domestication.
7. Several Pokémon reacting together does not prove one persistent collective.
8. Social response can create withdrawal, concealment, clustering, warning or route change instead of extra attackers.
9. A signal may be ignored, missed, misunderstood or become stale.
10. Active-battle reinforcement remains blocked until AutoPTU exposes an audited participant/lifecycle contract.

## Copyright/provenance guardrail

This file extracts high-level structural lessons only. No copyrighted dialogue, distinctive characters, plots, maps or source mechanics are copied into Ouros. Main-series numerical call rates and encounter formulas are not imported.