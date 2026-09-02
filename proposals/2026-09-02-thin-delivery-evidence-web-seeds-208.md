# Pass 208 Ouros Candidates — Thin Delivery evidence web

Status: PROPOSED / NON-CANON
Date: 2026-09-02

This file applies pass 208 research only to already-canonical Marea Interior people, places, institutions and the unresolved `ouros.arc.thin_delivery_season`. It does not establish the cause of the arc and does not promote any proposal to canon.

## Continuity constraints

CANON-APPROVED inputs preserved:

- Puerto Bruma, Loma Clara, Sendero del Vidrio and Estación Mirador keep their current IDs and fixed coordinates;
- the Thin Delivery Season begins with smaller/less predictable deliveries and no established cause;
- Mara owns route coordination, Ivo has market/purchasing evidence, Nerea has observation evidence, Taro has historical records, Lia has arrival records, Brin has cooperative intake/dispatch records, Alba can speak only for her holding, and no one actor owns regional truth;
- battle victory cannot establish the cause;
- the lower-Sendero Fletchling remains its existing canon-approved wild identity and is not assigned causal responsibility by this proposal.

## Candidate questline: The Missing Middle

Status: PROPOSED

Suggested IDs:

`questline_id: ouros.marea.thin_delivery.missing_middle`

Types: REGION, EXPLORATION, FACTION, SETTLEMENT, CLASS.

Premise: Ivo's market notes show some lots arriving smaller than expected. Brin's cooperative records show what left storage. Lia's dock/arrival records can distinguish land-route deliveries from ferry-linked consignments. Nerea has observations that may explain conditions but not commerce. Taro can show whether the apparent irregularity is actually unusual compared with older seasons.

The player receives a question rather than a suspect: where does the information stop matching?

No single node is mandatory first.

### Evidence node A — Bruma Market Hall

Owner: Ivo Serrat.

Direct fact candidate: selected received lots differ from Ivo's expected purchasing notes.

Possible links revealed: cooperative dispatch record; arrival/handling record; historical comparison.

What this node cannot prove: why the lot changed before arrival, whether production fell region-wide, or whether wildlife caused anything.

### Evidence node B — Loma Cooperative Storehouse

Owner: Brin Havel, with Alba Ríos available only for her own holding.

Direct fact candidate: dispatch manifests identify quantity/time/source for specific tracked lots.

Possible links revealed: producer holding; Sendero route window; market receipt.

What this node cannot prove: physical condition after dispatch or the state of all producers.

### Evidence node C — Ferry Landing / arrival desk

Owner: Lia Morn.

Direct fact candidate: arrival logs establish which consignments passed through which transfer point and when.

Possible links revealed: market receipt; route report; ferry observation if relevant.

What this node cannot prove: contents that were never under dock custody or the cause of a discrepancy.

### Evidence node D — Estación Mirador

Owner: Nerea Sol and Ema Rey.

Direct fact candidate: dated weather/ecology/route observations overlap specific dispatch windows.

Possible links revealed: Sendero verification; archive comparison; Field Office report.

What this node cannot prove: that correlation caused a shipment difference.

### Evidence node E — Tideglass Archive

Owner: Taro Min, with Pia Min handling copies/courier work.

Direct fact candidate: older delivery and route records provide comparison ranges and previous explanations with explicit provenance.

Possible links revealed: Mirador record lineage; market history; older route maintenance event.

What this node cannot prove: that an old explanation applies to the present season.

### Evidence node F — Sendero seasonal crossing

Owner: no single institution. Mara coordinates safe field access; observations belong to their actual observers.

Direct fact candidate: current physical route condition and any authored trace/traffic evidence at inspection time.

Possible links revealed: Field Office report; Mirador observation; dispatch timing.

What this node cannot prove: the arc's complete cause from one inspection.

## Redundancy contract

Status: PROPOSED

The episode should remain solvable if the player skips one evidence owner. Each major conclusion must have multiple independent support paths.

Candidate conclusion families:

`C1: discrepancy exists between dispatch and receipt`
Support can come from Brin + Ivo, Brin + Lia, or another explicitly authored pair that measures the same tracked lot from different custody points.

`C2: discrepancy timing overlaps a route/condition window`
Support can come from dispatch timestamps + Field Office/Sendero observation, arrival timestamps + Mirador observation, or another explicit timestamped chain.

`C3: current pattern is unusual or ordinary relative to prior seasons`
Support can come from Tideglass comparison plus current records; one resident's memory alone remains testimony, not the comparison result.

These are candidate evidence relationships, not final truth. They should not become a hidden “collect 3 clues” counter.

## Class-aware interaction without class-locking

Status: PROPOSED / MECHANICALLY UNCERTAIN

Researcher, Chronicler, Survivalist, Backpacker, Commander, Chef and other relevant builds may eventually receive mechanically governed options from their verified PTU/Kairos Skills/Features. Until the active rules profile and engine service are verified, the base episode must expose direct inspectable facts without requiring invented checks.

Candidate advantages that do not fabricate mechanics:

- an NPC may recognize a profession/class history and offer a different explanation surface;
- an already-public record may be easier to locate through an authored dialogue shortcut;
- an expert NPC may explain the limits of a document;
- the quest log may group evidence by provenance.

Any actual roll, DC, Feature effect, reroll, bonus, time reduction or mechanical permission remains unresolved.

## Mechanically rich encounter: Crossing Under Pressure

Status: PROPOSED / FULL VERSION BLOCKED

Narrative premise: the player visits the seasonal crossing to verify a time-sensitive physical fact. A confrontation may emerge from current ecology or another authored actor state. The tactical goal is to finish or abandon the verification safely, not necessarily defeat everything present.

Possible full-version semantic objectives:

- reach an observation anchor;
- maintain access long enough for an authored inspection action;
- protect a noncombat recorder represented through a supported escort/protection contract;
- disengage through a safe boundary;
- clear an immediate obstruction without declaring ecological or investigative truth.

Required capability families: targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement where displacement/interception is used; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle where selected actions require it; terrain/weather/hazards/zones/reactions for crossing mechanics; move-specific behavior; abilities; items if mechanical field tools are allowed; Trainer Features/perks for mechanical interrupts/actions; AI legal-action infrastructure; AI tactical policy for objective-aware behavior; Minecraft/Cobblemon/Craftics adapter/playback support.

Current readiness: full version remains blocked by the complete terrain/weather/hazards/zones/reactions family, AI tactical policy and incomplete end-to-end adapter/playback; several other families remain partial.

## Reduced encounter: Observe, Record, Leave or Fight

Status: PROPOSED / IMPLEMENTATION-CANDIDATE

The same quest episode can preserve its premise with a reduced crossing scene:

1. the server exposes a fixed inspection point and current route facts;
2. the player records direct observations without tactical terrain effects;
3. an authoritative interpretation request is optional and only exists when a verified rules service exists;
4. current world ecology may expose a visible Pokémon encounter;
5. the player can observe, disengage or engage where legal;
6. if battle occurs, use only an ordinary audited BattleSpec/path;
7. battle output may update immediate encounter state but cannot write `thin_delivery_season.cause`;
8. the evidence record persists even if the player leaves before combat or loses/withdraws from a battle.

The existing lower-shelf Fletchling may appear only through its current authoritative population/encounter ownership. This proposal does not clone it, alter it, make it territorial by default or make its defeat a quest requirement.

## Candidate persistent state

Status: PROPOSED

```text
ouros.arc.thin_delivery_season.evidence_nodes_discovered[]
ouros.arc.thin_delivery_season.evidence_refs[]
ouros.arc.thin_delivery_season.published_evidence_refs[]
ouros.arc.thin_delivery_season.conclusions_supported[]
ouros.arc.thin_delivery_season.conclusions_disputed[]
ouros.arc.thin_delivery_season.open_questions[]
```

Each evidence ref should point to provenance-bearing records rather than duplicate prose blobs inside the questline.

## Failure and transformation

Status: PROPOSED

The episode should not fail permanently because one clue is missed or one battle is lost.

Useful transformations:

- a record becomes stale and requires a later observation;
- a delivery moves before inspection, changing which node now owns the next evidence;
- a participant publishes an incomplete interpretation, creating a public-memory correction task;
- a player leaves the crossing because conditions are unsafe and returns under different world state;
- a battle interrupts fieldwork, but the investigation continues through the other evidence nodes.

No transformation may silently fabricate the final cause.

## Canon questions left open

- Which specific tracked lots become the first authored evidence objects.
- Whether ferry-linked consignments belong in the first episode or should remain a later branch.
- Which direct route observations are canonical at campaign start versus generated from live world state.
- What evidence threshold or institutional decision actually permits a canonical conclusion.
- Whether Thin Delivery Season has one cause, several interacting causes, or changes cause over time.
- Which PTU/Kairos Skills and Features are allowed to interpret each evidence type under the production rules profile.

Until reviewed, every item in this file remains a candidate.