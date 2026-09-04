# Projection arbitration and environmental sign contract — Pass 249

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE until separately approved

## Purpose

Pass 248 determines whether ecology pressure makes a population source eligible for presentation. Pass 239 controls direct entity leases. Pass 240 controls observation and knowledge. This contract defines the missing seam between them.

The contract does not implement a Cobblemon adapter and does not change PTU rules.

## Authority boundary

Ouros owns population, persistent identity, ecological state, projection eligibility and the decision that a presentation may exist.

Minecraft/Cobblemon owns rendering, entity lifecycle and player-facing interaction surfaces. A native entity, animation, sound or despawn event cannot create or delete canonical population truth.

AutoPTU remains the authority for PTU tactical adjudication after a valid Pass 242 handoff.

## Arbitration input

The presentation arbiter consumes an already-evaluated projection envelope plus current adapter context.

Minimum input:

- habitat/location key;
- eligible time/window state;
- eligible microhabitats;
- visibility/exposure policy;
- simultaneous presentation budget;
- candidate source class when direct presentation is requested;
- current active leases;
- adapter correlation state;
- sanitized observer context when an indirect sign could be useful.

The arbiter must not recalculate abundance, population membership, PTU legality or battle outcomes.

## Allowed decisions

### DIRECT_ENTITY

Use only when an already-counted source can be reserved.

Required order:

1. verify envelope eligibility;
2. select an already-counted source;
3. reserve a Pass 239 projection lease atomically;
4. request Cobblemon materialization;
5. correlate returned Minecraft entity UUID to the lease;
6. expose only sanitized observation fields to observers.

If reservation fails, direct materialization must not proceed.

A successful materialization cannot change population count.

### INDIRECT_SIGN

Use when ecological presence can be communicated without materializing a Pokemon actor.

An indirect sign:

- has its own evidence/provenance ID;
- has no Minecraft Pokemon entity UUID;
- has no projection lease;
- exposes no persistent actor/member ID;
- exposes no exact hidden population total;
- exposes no hidden resource quantity;
- cannot independently create a BattleSpec or AutoPTU handoff;
- may feed a sanitized Pass 240 observation;
- may support a population/species/location claim at an appropriate confidence level.

A sign can be acoustic, visual environmental evidence or another non-actor presentation form. Species-specific signs require a validated behavior profile before canon use.

### NO_PRESENTATION

An eligible envelope does not guarantee a visible event. The adapter may validly present nothing while leaving ecological state unchanged.

This outcome must not be interpreted as evidence that the population is absent.

### QUARANTINE_UNCORRELATED_ENTITY

Use when a Cobblemon Pokemon entity appears without an Ouros-approved source/lease correlation.

The entity may exist on the presentation layer, but until reconciliation succeeds it must not:

- create a persistent individual;
- consume or create an unresolved population slot;
- change abundance;
- create demographic history;
- become trusted evidence of a specific persistent individual;
- enter an AutoPTU combatant manifest automatically;
- create capture, KO, mortality, immigration or emigration truth.

The concrete adapter response—hide, suppress, despawn, isolate from interaction, or another implementation—is deliberately left open. Narrative code may require quarantine semantics but must not pretend an unverified adapter operation already exists.

## Evidence-root rule

Every indirect presentation receives a provenance root.

Independent observations can corroborate a claim. Relays or copies of one root cannot increase independent-source count.

The presentation layer must not derive a second root merely because the same underlying sign was rendered twice after chunk reload or player reconnect.

## Direct and indirect coexistence

Indirect evidence is not a substitute population member. It does not occupy the direct-entity lease budget.

However, presentation policy should avoid obviously duplicative output. If a directly materialized actor is already visibly producing the same observable behavior in the observer’s context, the adapter should not create a second artificial sign that implies an additional unseen Pokemon.

This anti-duplication rule concerns player-facing evidence, not demographics.

## Restart and rematerialization

On restart or chunk unload:

- runtime Minecraft UUID correlation may disappear;
- the persistent Ouros member remains;
- a direct projection lease follows Pass 239 reconciliation rules;
- indirect evidence already recorded remains in observation provenance/history;
- a later direct materialization may use a new UUID without creating a new individual;
- an old indirect sign must not replay as a new independent evidence root unless a new world event actually generated it.

## AutoPTU boundary

INDIRECT_SIGN and NO_PRESENTATION always remain outside AutoPTU.

QUARANTINE_UNCORRELATED_ENTITY cannot enter AutoPTU until an authoritative source is reconciled and Pass 242 independently chooses OPEN_AUTOPTU or a supported reduced path.

DIRECT_ENTITY does not itself open AutoPTU. Pass 242 encounter intent still decides whether the interaction stays overworld, opens tactical resolution, uses a reduced version or is blocked as unsupported.

## Reduced encounter contract

A reduced investigation encounter can run entirely through:

projection envelope → INDIRECT_SIGN → Pass 240 observation → later projection reevaluation → optional DIRECT_ENTITY sighting.

This preserves the narrative premise of following evidence toward a living Pokemon without requiring battle rules.

## Rich encounter dependencies

If the player later pursues or intercepts a directly projected actor, dependencies are explicit:

- targeting/footprints/range/LoS: required only if the authored scene uses tactical targeting or visibility/range adjudication;
- base movement legality: required for tactical movement;
- complete movement: required for interception, push/pull/knockback, forced movement or other advanced movement interactions;
- core calculations: required when PTU calculations enter the encounter;
- action economy/initiative: required for tactical turns;
- full turn/round lifecycle: required for timed tactical sequence;
- full stateful damage pipeline: required only if damage occurs;
- status lifecycle: required only if statuses occur;
- terrain/weather/hazards/zones/reactions: required only when the authored scene uses those mechanics;
- move-specific behavior: required for the exact Moves used;
- abilities: required for exact Abilities used;
- items: required for exact Items used;
- Trainer Features/perks: required for exact Features/perks used;
- AI legal-action infrastructure: required for autonomous tactical actors;
- AI tactical policy: required for rich autonomous pursuit/evasion behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: required end-to-end for presentation and reconciliation.

A representative implementation in any one family never upgrades the whole family.

## Invariants for executable fixtures

- population totals cannot change without a demographic-authority event;
- direct materialization cannot precede lease reservation;
- one persistent member cannot hold multiple active direct leases;
- indirect signs cannot carry persistent identity or exact hidden counts;
- an indirect sign cannot open AutoPTU;
- an uncorrelated native entity cannot mutate ecology;
- despawn cannot imply death, capture, emigration or absence;
- rematerialization under a new UUID preserves persistent identity;
- repeated rendering of one sign cannot create independent corroboration;
- restart clears runtime correlation without erasing canonical state.

## Open implementation questions

The exact Cobblemon hook used to suppress or quarantine native uncontrolled entities remains unresolved.

The first runtime implementation should keep indirect signs population/location scoped unless a separate validated contract proves that individual attribution can be retained internally without leaking identity or producing duplicate actor semantics.
