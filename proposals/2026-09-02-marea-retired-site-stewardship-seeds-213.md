# Ouros Proposal — Marea Retired-Site Stewardship Seeds — Pass 213

Status: PROPOSED / NON-CANON
Date: 2026-09-02

This file applies pass 213 research to Marea Interior without changing established canon. Every new site, historical event and local practice below is provisional until explicitly approved.

## Canon boundaries preserved

Canonical locations remain Puerto Bruma, Sendero del Vidrio, Loma Clara and Estación Mirador with their frozen anchors and resident network.

Thin Delivery Season remains unresolved. Nothing below explains its cause.

Existing resident roles stay unchanged. Proposed material reuses Taro Min, Pia Min, Mara Veyra, Dr. Nerea Sol, Ema Rey, Teo Lark and Lia Morn only where their canon responsibilities plausibly intersect.

No resident death, kinship, former employment or personal trauma is invented.

## Proposed site: Mirador Lower Annex

Status: PROPOSED SITE / NON-CANON

Working concept:
A small weather-observation and instrument shelter below the current Estación Mirador was taken out of regular service before the present station configuration. Its exact construction date, closure date and reason are unresolved. The structure remains physically present but is not part of routine station access.

Important restrictions:
- no exact coordinates are canonized here;
- it is not automatically ancient;
- it is not automatically haunted;
- no death or disaster is attached to it;
- no hidden legendary connection exists by default;
- no item cache or loot table is assumed;
- current wild use must come from observed ecology, not genre expectation.

Candidate persistent state:

```yaml
retired_site_record:
  site_id: ouros.site.mirador_lower_annex
  former_function: weather_and_field_instrument_support
  closure_event_id: unresolved
  confirmed_closure_facts: []
  closure_reason_claim_ids: []
  successor_site_ids:
    - ouros.site.estacion_mirador
  transferred_record_ids: []
  transferred_object_ids: []
  retained_obligations: []
  current_access_policy_id: proposed_review_required
  current_steward_ids: []
```

The empty arrays are intentional. The generator must not fill historical facts merely because the site exists.

## Seed 1: The Label That Stayed Behind

Taro finds an archive reference showing that one instrument inventory label still points to the retired annex while the corresponding current ledger is incomplete.

Player-facing work can include:
- compare the archive reference with Nerea's current equipment records;
- ask Teo whether the old equipment family still exists locally;
- inspect the annex exterior if access is authorized;
- record whether the label refers to an object, fixture position or old storage designation;
- return an observation without claiming theft, loss or misconduct.

Possible outcomes:
- the label is obsolete and can be cross-referenced to a successor record;
- a fixture remains in place but no longer serves its former function;
- a record transfer happened but was poorly indexed;
- evidence remains insufficient.

No outcome implies Thin Delivery involvement.

## Seed 2: Leave the Nest, Move the Work

A later authorized inspection may establish that part of the retired structure is being used by wild Pokémon.

Species is deliberately unset.

The central choice is operational:
- postpone inspection of that section;
- use a different access point if physically legal;
- document from outside;
- move the human work rather than displace the Pokémon;
- request a wildlife assessment from Mara before proceeding.

The wild Pokémon are not quest props. Presence does not grant capture rights, ownership or hostility.

If a species-specific interaction is later desired, PTU/Caelo/Kairos legality and the persistent world entity state must be verified first.

## Seed 3: Keep, Close, Reuse

After enough verified observations exist, station and archive actors may disagree about the site's future without becoming enemies.

Candidate positions:
- Nerea may value controlled research access if current observations justify it;
- Taro may prioritize preserving records and visible traces of earlier station practice;
- Teo may care about whether any remaining fixtures are safe or maintainable;
- Mara may prioritize route and visitor safety;
- Ema may have practical evidence about current field use;
- no actor automatically has final authority unless canon later grants it.

Possible proposals:
- leave closed and document;
- limited supervised access;
- stabilize only the exterior;
- convert one safe room to equipment storage;
- preserve part as an interpretive field-history space;
- allow ecological occupation and relocate human use elsewhere.

The questline should preserve who proposed each option and the evidence they used.

## Seed 4: The Small Plaque Problem

A proposed interpretive plaque summarizes the annex's history too confidently.

The player can compare its wording against actual records and observations.

This connects pass 213 with existing claim/publication infrastructure:
- confirmed fact may be stated plainly;
- interpretation should be attributed;
- unknown closure cause stays unknown;
- current ecological use should use dated observations;
- a later correction supersedes wording without deleting the earlier publication history.

The challenge is accuracy, not exposing a villain.

## Rich encounter concept: Annex Re-entry Under Shared Constraints

Status: INTENDED FULL VERSION / BLOCKED BY MULTIPLE CAPABILITY FAMILIES

Premise:
An authorized inspection party enters a limited portion of the retired annex while current wildlife presence and a damaged interior create competing spatial objectives. The goal is to document specified fixtures and leave without unnecessary disturbance.

Potential tactical elements:
- narrow access footprint;
- line-of-sight around interior partitions;
- protected observation positions;
- ordinary movement plus difficult or blocked paths if mechanically supported;
- optional disengagement rather than defeat-all victory;
- wild Pokémon that may defend space according to verified AI policy;
- forced movement risk only if an actual Move/Ability/Feature produces it;
- environmental danger only if the engine has an audited terrain/hazard contract;
- semantic objectives such as inspect, withdraw, protect observer or preserve access lane.

Required permanent capability families:
1. targeting/footprints/range/LoS;
2. base movement legality;
3. complete movement including push/pull/knockback/interception/forced movement;
4. core calculations;
5. action economy/initiative;
6. full turn/round lifecycle;
7. full stateful damage pipeline;
8. status lifecycle;
9. terrain/weather/hazards/zones/reactions;
10. move-specific behavior;
11. abilities;
12. items;
13. Trainer Features/perks;
14. AI legal-action infrastructure;
15. AI tactical policy;
16. Minecraft/Cobblemon/Craftics adapter/playback support.

The rich version must not ship by implementing missing PTU logic in the Minecraft adapter.

## Reduced encounter: Document the Safe Edge

Status: REDUCED IMPLEMENTATION CANDIDATE

Narrative premise remains unchanged: inspect a retired site while respecting current use and uncertainty.

Reduced execution:
- server-authenticated access state;
- ordinary overworld traversal only through currently safe/presented paths;
- inspection interactions generate observation records;
- current wild presence is visible but no tactical objective is inferred from it;
- player may withdraw, defer, request another inspection window or document from outside;
- any combat occurs only through a separate audited BattleSpec;
- no collapse damage, difficult terrain, forced movement, reaction, weather phase or autonomous objective AI is simulated;
- no off-screen battle determines what happened inside.

This version advances history, ecology and stewardship without requiring capability family 9 or 15.

## Long-term arc candidate: What a Place Is For Now

Status: PROPOSED ARC / NON-CANON

The annex can support a slow arc across several visits:

Phase A: archival mismatch identifies the place as relevant.

Phase B: physical inspection establishes current condition without resolving every historical question.

Phase C: current ecological use creates a new stakeholder relationship.

Phase D: residents propose different futures based on their mandates and evidence.

Phase E: one limited policy is tried.

Phase F: the world later shows whether that policy works, needs revision or creates a new tradeoff.

There is no universal “restore” ending. The durable payoff is that a previously obsolete location acquires a new, traceable role in the district.

## Implementation notes

Minecraft should represent:
- boarded or restricted openings;
- weathered signage;
- visible but non-loot environmental remnants;
- later stabilization work;
- changed access barriers;
- current wildlife only from world state;
- a plaque or interpretation panel only after its publication record exists.

Minecraft must not decide:
- why the annex closed;
- who owns it;
- whether a memorial claim is true;
- whether a wild Pokémon is hostile;
- whether damaged flooring has PTU terrain effects;
- whether entering completes an investigation;
- whether a battle outcome authorizes reopening.

## Open canon questions

- Did a predecessor facility to Estación Mirador exist at all?
- If yes, was it one annex or several generations of field infrastructure?
- Which institution owns or stewards the retired structure?
- Does Tideglass hold complete, partial or no transfer records?
- Is public access culturally normal, restricted or simply unsafe?
- Does the location have any commemorative significance, or only operational history?

Until reviewed, all answers remain unresolved.