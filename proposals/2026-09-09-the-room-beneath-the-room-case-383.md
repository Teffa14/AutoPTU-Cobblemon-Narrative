# The Room Beneath the Room — case 383

Status: PROPOSED / NON-CANON
Canon effect: NONE

## Premise

A field team enters a previously documented ruin or historical structure. The visible chamber appears internally consistent, and an older site sketch supports that interpretation.

A new disturbance exposes a narrow section of masonry beneath the current floor. The newly visible feature does not match the alignment of the room above it.

The first conclusion is tempting: a hidden chamber exists below.

That conclusion is not yet evidence.

The actual discovery is narrower: the site contains at least two structural phases, or one phase reused an earlier foundation. The meaning of the lower feature remains unresolved.

## Narrative value

This creates progression through reinterpretation rather than through a newly spawned magical clue.

Earlier observations remain useful:
- an old sketch can be correct about the room that was visible then;
- a researcher can have documented the site carefully and still have missed a buried phase;
- a later visitor can discover genuinely new evidence without proving that the earlier researcher was incompetent or deceptive;
- moving one portable object may preserve the object while losing the relationship that explained why it mattered.

The mystery can expand outward by comparing other sites, maps, construction materials, drainage features, inscriptions, repaired walls or reused foundations.

## Reduced implementation

The reduced version uses no AutoPTU handoff.

1. Create a persistent site with two physical-state revisions.
2. Preserve an earlier observation/context record for the visible chamber.
3. Apply an explicit site-state change that exposes one fixed lower feature.
4. Create a new observation record tied to that later semantic minute.
5. Let NPCs form interpretations from the evidence they actually know.
6. A researcher who has both records can propose a multi-phase construction hypothesis.
7. Another actor with only the old record can sincerely reject that hypothesis until the new evidence is communicated or inspected.

No explanation for the lower feature becomes true merely because the player discovers it.

## Quest hooks

A survey task can ask the player to document several alignment points before weather, work crews or natural site change make them inaccessible again.

A custody task can involve a portable object removed years earlier whose original context was poorly recorded. Recovering it helps, but reconstructing where it came from requires old notes, witnesses or fixed-site evidence.

A rivalry can emerge between two researchers whose interpretations differ because their evidence sets differ. The player can resolve part of the dispute by collecting missing observations rather than by choosing a dialogue side arbitrarily.

A faction or institution may want the site opened quickly for access, tourism, construction, research or safety, while another actor wants a slower documentation pass. The conflict can remain procedural and material rather than requiring a villain.

## Mechanically rich version

A later canonized site can place the exposed feature inside a tactically dangerous environment.

Possible objectives:
- document several fixed features while territorial Pokémon create pressure;
- escort a specialist to observation points;
- protect fragile equipment or a portable find;
- withdraw after enough evidence is collected rather than defeating all opponents;
- reach an exit before a verified environmental phase makes the area inaccessible;
- recover a separated team member without disturbing a marked evidence zone.

The full version must not assume unsupported knockback, reactions, dynamic weather, complex statuses, delayed effects or objective-aware AI.

## Permanent engine dependency classification

Targeting/footprints/range/LoS: VERIFIED within audited ordinary contracts if ordinary tactical visibility/targeting is used.

Base movement legality: VERIFIED within audited ordinary contracts.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for displacement, drag/rescue, collapse slides or interception.

Core calculations: VERIFIED within audited deterministic contracts.

Action economy/initiative: VERIFIED for audited primitives; documenting or protecting evidence as a tactical action still requires an explicit admitted action contract.

Full turn/round lifecycle: PARTIAL; required for timed exposure/collapse phases or multi-round environmental sequencing.

Full stateful damage pipeline: PARTIAL.

Status lifecycle: PARTIAL.

Terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING by exact mechanism.

Move-specific behavior: INDIVIDUALLY GATED.

Abilities: INDIVIDUALLY GATED. The live Java Transform/Impostor state-copy parity seam does not generalize to unrelated abilities.

Items: INDIVIDUALLY GATED.

Trainer Features/perks: INDIVIDUALLY GATED. Researcher/Paleontologist/Topographer relevance must be checked against authoritative PTU/Kairos/Caelo mechanics before a Feature becomes required.

AI legal-action infrastructure: VERIFIED for ordinary audited actions.

AI tactical policy: BLOCKING for protect-evidence, escort, search, rescue-first, area-documentation, objective-aware withdrawal and disengage-after-objective.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL/BLOCKING for persistent site-feature identity, evidence-zone acknowledgement, non-KO objectives and authoritative end-to-end playback.

## Canon questions

No ruin, culture, location, institution, historical phase, species or cause of exposure is canonized here.

Before promotion, internal Ouros/Caelo authority must resolve:
- which approved location can support the site;
- who built or reused it, if that history is already established;
- which institution or local actors care about it;
- what communications and access controls exist;
- which species are valid for the habitat;
- whether the lower feature is natural, constructed or still intentionally unresolved.

## Provenance boundary

The exposed lower feature proves a physical relationship at a specific site revision.

It does not by itself prove a hidden chamber, treasure, civilization, disaster, conspiracy or specific chronology.

`NEW_FEATURE_OBSERVED != MYSTERY_SOLVED`

A later interpretation can become stronger as evidence accumulates without rewriting the original observations.
