# Sendero del Vidrio observation seeds — pass 207

Status: PROPOSED / NON-CANON
Date: 2026-09-02

These candidates extend the fixed Marea Interior route without replacing established canon. During this pass, main advanced with `canon/marea-interior-first-wild-population-v1.md`, which canon-approved the first lower-shelf visible wild slot as a level-5 standard Fletchling with a frozen PTU 1.05 blueprint. These proposals now treat that Fletchling as fixed canon while leaving later ecological roles and the broader Sendero encounter table unresolved.

## 1. Fresh Marks at the Seasonal Crossing

Premise: route workers report new scrape marks and disturbed ground near the seasonal crossing. The first objective is inspection, not combat.

Player-visible sequence:

- notice physical traces before any Pokemon actor is revealed;
- inspect recency and direction;
- decide whether to follow, warn travelers, leave the area or request local expertise;
- if followed, reveal one already-provisioned visible wild individual tied to the clue chain;
- allow observation/disengagement before any battle request.

Persistent consequences:

- the route record remembers that the marks were inspected;
- Mara Veyra may receive a field report if the player submits one;
- repeated disturbance may later justify a route-maintenance or wildlife-stewardship task;
- the clue must not falsely identify Fletchling merely because Fletchling is the first canon wild slot; clue identity follows authored evidence.

Full version dependencies: targeting/footprints/range/LoS; base movement; complete forced movement if crossing displacement matters; core calculations; action economy; lifecycle; stateful damage; selected status/move/ability/item/Feature paths; terrain/hazard/reaction family if the crossing is mechanically active; AI legal-action infrastructure; AI tactical policy for protective behavior; Minecraft adapter/playback.

Reduced version: static trace objects + one authoritative observation interaction + one visible individual + simple ordinary arena if engaged. No tactical hazard, group tactics, forced movement or delayed status objective.

## 2. Lower-Shelf Fletchling Observation Layer

Premise: the canon-approved lower-shelf Fletchling should have a peaceful observation surface before the player chooses engagement.

Allowed proposed clues, subject to implementation review:

- distant wingbeats or movement;
- a direct sighting from outside interaction range;
- ordinary feeding/perching evidence if authored for this specific individual/context;
- a Field Office sighting entry after direct observation.

The proposal does not change its level, stats, Big Pecks Ability, Tackle/Growl loadout, HP, movement or encounter identity. Those remain frozen by the canon population record and authoritative runtime contracts.

Reduced dependencies: Minecraft presentation plus persistent observation provenance. Battle mechanics are needed only if the player explicitly engages.

## 3. The Quiet Patch

Premise: one section of Sendero is unusually quiet compared with the surrounding route. The absence of normal calls becomes the clue.

Possible explanations remain deliberately open until content approval: recent disturbance, a resting territorial Pokemon, human activity, weather displacement, or a harmless temporary movement pattern.

Design value:

- teaches that absence can be information;
- creates suspense without requiring an enemy spawn;
- lets Perception/Survival-style interpretation matter without inventing a new skill system;
- can end peacefully with a better field report rather than a reward chest.

Reduced version dependencies: Minecraft world observation/presentation plus an authoritative field-check boundary. No battle dependency if the player leaves after inspection.

## 4. Feeding Trail, Not Loot Trail

Premise: scattered plant remains and repeated feeding traces lead away from the main path. They are ecological evidence, not automatically harvestable loot.

Player choices:

- document and leave the site intact;
- follow the signs;
- ask a resident researcher or ranger to interpret them;
- disturb the area, creating a persistent `site_disturbed` fact if world interaction allows it.

If a Pokemon appears, it may continue feeding, retreat, watch or warn. Those presentation states cannot grant combat bonuses or decide capture legality.

Longer-term use: observation history can establish seasonal use of the route without simulating a fully autonomous ecosystem.

## 5. Shared Sighting Ledger

Premise: Marea Field Office maintains a practical sighting ledger for route safety and ecology work.

The player may submit only facts they actually observed or clearly mark reported/uncertain claims. Nerea Sol and Mara Veyra can use the same record for different institutional purposes.

Information classes:

- direct sighting;
- physical trace;
- interpreted clue;
- third-party report;
- unresolved contradiction.

This is not a Pokedex replacement and grants no automatic mechanical bonuses. It is a persistent world-memory surface that can later drive quest generation, route advisories and research dialogue.

## 6. Protective Distance

Premise: an authored territorial clue is deliberately placed before a resting/nesting zone so the player receives fair warning before escalation.

Required narrative rule:

`warning evidence -> choice to withdraw -> escalation only after continued approach or another authoritative trigger`

This avoids arbitrary ambush design and supports wildlife that protects space without being framed as villainous.

Full version may use group positioning, terrain, reactions or forced movement and therefore inherits those capability blockers.

Reduced version uses a boundary volume and warning presentation only. Crossing it requests an authoritative encounter transition; it does not calculate aggro or PTU legality in Minecraft.

## Canon questions before promotion

- Which official species fill later Sendero ecological roles beyond the already-approved lower-shelf Fletchling.
- What Marea's climate/vegetation facts are at the fixed route anchors.
- Which observation records are private Trainer knowledge versus shared Field Office records.
- Which active Ouros rules profile governs deliberate tracking and field interpretation checks.
- Whether any nesting/breeding clue requires separate Egg/nursery authority safeguards.
- What route-disturbance facts can be changed by ordinary Minecraft interaction without undermining authored world state.

No item reward, new encounter level, capture rate, Skill DC, species rarity, weather rule or combat modifier is canonized by this file.
