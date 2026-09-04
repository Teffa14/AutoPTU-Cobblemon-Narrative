# Recurring wild individual recognition contract — Pass 253

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE until approved

## Purpose

Define how a player, NPC or research notebook may infer that separate observations probably concern the same wild Pokemon without receiving Ouros' hidden persistent identity and without merging actors in authoritative ecology state.

## Authority boundary

Ouros persistent state remains the authority for actor identity. Observer records hold hypotheses only.

`persistent_actor_id`, projection lease IDs, Minecraft UUIDs and internal population-source IDs are prohibited from player-facing observation payloads.

An identity hypothesis cannot create, delete, merge or split persistent actors. It cannot change population abundance, demographic history, capture ownership, projection eligibility, battle participants or AutoPTU state.

## Identity hypothesis model

The player-facing recognition layer may use three provisional states:

- `UNRESOLVED`
- `POSSIBLE_SAME_INDIVIDUAL`
- `PROBABLE_SAME_INDIVIDUAL`

`PROBABLE_SAME_INDIVIDUAL` is the maximum state available from ordinary unmarked field observations in this contract.

A future stronger state requires a separately approved diegetic identifier whose observability and persistence are documented. Behavioural similarity alone cannot produce certainty.

## Evidence record

Each observation considered for identity linkage should carry:

- an observer-visible species/form description appropriate to current knowledge;
- time and broad place context at the granularity actually observed;
- observable behaviour or route information when witnessed;
- an evidence-quality classification;
- a provenance root;
- optional explicit contradictions;
- no hidden actor identifier in the player-facing projection.

The authoritative reducer may retain hidden linkage solely to test whether the epistemic system made a correct or incorrect inference.

## Provenance rule

Several reports derived from one original observation count as one root. Relays may spread knowledge but cannot raise identity confidence by repetition alone.

Independent observation roots may raise confidence when their evidence is mutually compatible.

## Contradiction rule

A material contradiction cannot be discarded merely because an earlier hypothesis is convenient. The recognition layer must preserve one of these outcomes:

- reduce the existing hypothesis confidence;
- return the hypothesis to `UNRESOLVED`;
- create a competing candidate hypothesis;
- record that current evidence cannot distinguish the candidates.

Contradiction handling has no authority to alter the hidden population ledger.

## Behavioural evidence rule

Repeated perch use, retreat direction, activity window, tolerance, avoidance or other stable-looking behaviours may support a match. These observations carry less identity authority than an approved stable individual marker because real animal behaviour can vary and different individuals can converge on similar routines.

No Fletchling-specific unique behaviour is canonized here.

## Presentation continuity

Pass 252 may restore or rematerialize the same persistent actor under a different Minecraft UUID. A new UUID does not reduce hidden identity continuity and does not automatically increase player certainty.

The inverse is also required: a visually similar entity must not inherit a player's accumulated individual history merely because its species, location and current behaviour resemble an earlier sighting.

## Reduced encounter version

A player records several sightings over multiple sessions. Independent compatible evidence can promote an identity hypothesis to `POSSIBLE` and later `PROBABLE`; a relay does not help; a conflicting same-species sighting opens ambiguity. No AutoPTU battle is needed.

Dependency: Minecraft/Cobblemon/Craftics adapter/playback support for faithful repeated projections and observation capture. The knowledge reducer itself is Ouros-side state and requires no tactical capability family.

## Rich encounter version

A player may choose to follow the suspected recurring Pokemon to acquire stronger contextual evidence. If this becomes a mechanically adjudicated pursuit, dependencies are base movement legality; complete movement including interception/forced movement when used; full turn/round lifecycle; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

Targeting/footprints/range/LoS applies when perception, target selection or tactical sight lines become adjudicated. Terrain/weather/hazards/zones/reactions applies only when the route mechanically uses those systems. Damage pipeline, status lifecycle, move-specific behavior, abilities, items and Trainer Features/perks apply only when the encounter actually invokes them.

## Fail-closed requirements

The recognition subsystem must reject or downgrade a transition when:

- the only new support is a relay of an existing provenance root;
- player-facing evidence contains a hidden actor/lease/UUID field;
- contradictory evidence is silently overwritten;
- a proposed `PROBABLE` identity rests on only one ordinary observation root;
- any recognition event attempts a population or demographic mutation;
- recognition alone requests an AutoPTU handoff.

## Open canon questions

Ouros still needs a policy for approved individual markers: research bands/tags, naturally persistent visible distinctions, social knowledge, capture history or other evidence classes.

Trainer Features/perks that improve observation or Pokemon knowledge require PTU evidence and engine contracts before they can modify identity confidence.
