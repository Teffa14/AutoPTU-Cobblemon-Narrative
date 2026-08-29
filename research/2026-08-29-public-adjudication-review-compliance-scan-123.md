# Ouros Narrative Research — Public Adjudication, Review & Compliance — Pass 123

Status: RESEARCH ONLY. Provenance and design evidence. Not Ouros canon.
Date: 2026-08-29

## Why this pass exists

The complete repository tree was inspected before writing. Existing layers already cover incident intake, investigation, evidence custody, institutional mandate, mediation, agreements, civic proposals, consultations, public records and operational response. They deliberately do not define criminal codes, universal courts, sentencing, detention powers or a universal appeal system.

The clean gap is narrower: when canon eventually gives a body authority to decide a disputed matter, Ouros needs persistent state for the decision process itself — notice, hearing/review scope, record considered, decision version, conditions, review/appeal request, remand/rehearing, implementation and later compliance — without inventing what legal system any region uses.

This pass therefore studies adjudication as a provenance and continuity problem, not as a real-world-law simulator.

## Internal boundary findings

### Case, Authority & Custody

`design/case-authority-custody-layer.md` explicitly keeps warrant systems, arrest powers, criminal codes, ownership law, sentencing, detention, search powers and real-world legal procedure undefined. It can produce evidence, custody histories, accusations, institution handoffs and case resolutions, but it does not own adjudication after a contested matter is referred.

Reusable boundary:
- investigation establishes and preserves evidence;
- adjudication evaluates a defined matter under an authored mandate;
- a finding or decision must not retroactively rewrite raw evidence or world truth.

### Agreements, Mediation & Repair

`design/agreements-mediation-repair-layer.md` explicitly separates agreement from legal enforceability and mediation from imposed outcomes. This makes voluntary settlement a sibling path, not a substitute for an authored deciding body.

Reusable boundary:
- mediation can end with no agreement;
- an adjudicative decision can exist without friendship, forgiveness or voluntary acceptance;
- later compliance is a separate event stream.

### Civic Governance

`design/civic-governance-public-works-layer.md` already models public consultation and collective future decisions. Its decision procedure contains an `appeal_or_review_route` placeholder but intentionally refuses to invent one.

Reusable boundary:
- civic consultation asks what public future state should be chosen;
- adjudication asks what a mandated body decided about a defined contested matter;
- some future canon may combine those roles in one institution, but the data objects should remain distinguishable.

## Pokémon source findings

### Detective Pikachu Returns — wrongful detention and continued investigation

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Detective_Pikachu_Returns
- https://bulbapedia.bulbagarden.net/wiki/Brad_McMaster
- https://bulbapedia.bulbagarden.net/wiki/Ryme_City_Police_Station

High-level pattern:
Detective Pikachu Returns contains an institutional accusation backed by apparently strong evidence, detention, continued investigation after detention, discovery that multiple cases share a framing mechanism, reversal of the operational conclusion and release of wrongly detained Pokémon.

Ouros transformation:
- a provisional institutional action must not freeze the case theory;
- later evidence can weaken or overturn an earlier conclusion;
- release, correction of a record, review of related cases and accountability for the bad process are distinct downstream events;
- detained or accused Pokémon remain actors with history, relationships and knowledge rather than becoming inventory objects.

Do not import Ryme City's police structure, characters, detention system, evidentiary threshold or plot.

### Sleuths for Truth! — accusation disproved by chronology

Source:
- https://bulbapedia.bulbagarden.net/wiki/Sleuths_for_Truth%21

High-level pattern:
Pikachu is treated as a prime suspect based on witness-derived evidence, but another incident occurs while Pikachu is already in custody, producing a chronology that disproves the accusation.

Ouros transformation:
A reviewable institutional record should preserve timestamps and the scope of what a conclusion actually established. A new event can contradict an old attribution without erasing the original testimony or making the witness malicious.

### Pokémon Adventures — custody and conditional release are distinct states

Source:
- https://bulbapedia.bulbagarden.net/wiki/Rood

High-level pattern:
The manga provides an example in which custody after a conflict and later release/bail are separate institutional states, while follow-up responsibilities continue.

Ouros transformation:
Do not compress `taken_into_custody`, `eligible_for_release`, `released`, `conditions_active` and `matter_closed` into one flag. Any such states require authored Ouros authority before use.

No manga-specific legal rule, character or outcome is imported.

## Public procedural-design findings

### Review works from a bounded record

Source:
- U.S. Court of Appeals for the Fourth Circuit, Rule 10 / record on appeal: https://www.ca4.uscourts.gov/rules/Rule10.html

Reusable abstraction:
A review process can operate on an identified record rather than re-reading the whole world. That record can have a stable manifest of submissions, exhibits, transcript/summary entries and earlier decisions.

Ouros use:
`review_record_manifest` should preserve exactly which evidence and decision versions were before the reviewing body. Later evidence can be added only through an explicit route rather than silently changing history.

No U.S. filing rule, evidentiary rule or procedure is imported.

### Review can affirm, alter, vacate or send a matter back

Sources:
- Fourth Circuit Rule 12.1: https://www.ca4.uscourts.gov/Rules/Rule12-1.html
- UK Upper Tribunal public decisions showing remittal for a fresh hearing when earlier findings cannot safely be preserved: https://tribunalsdecisions.service.gov.uk/utiac/ui-2026-000635

Reusable abstraction:
A later review does not always produce a new final answer. It can preserve some findings, set aside others, request more fact-finding, or return the matter for a new decision.

Ouros use:
Decision lineage needs explicit edges such as `AFFIRMED`, `MODIFIED`, `VACATED`, `REMANDED_FOR_MORE_FACTS`, `REHEARING_REQUIRED`, and a field stating which findings remain usable.

No real-world appeal grounds, standards of review or jurisdiction are imported.

### Rehearing is not the same as ordinary continuation

Source:
- Fourth Circuit Rule 40: https://www.ca4.uscourts.gov/rules/Rule40.html

Reusable abstraction:
A system can distinguish a request to reconsider/rehear from the original proceeding. Granting such a request can alter the status of the earlier decision while preserving its existence as historical provenance.

Ouros use:
Never overwrite a published decision object. Link a new review/rehearing event to it and record whether the old operative effect remains, is suspended, or is replaced according to authored local procedure.

## Tabletop/community lesson

Public Pokémon tabletop discussions repeatedly show that campaign groups use PTU for roleplay-heavy, investigation-heavy and organization-centered campaigns rather than only League progression. This supports adjudication as an occasional narrative lane, but community homebrew cannot establish legal mechanics or PTU rules.

Useful design lesson:
When a procedural scene appears, make the playable question concrete: find a missing record, establish chronology, secure a witness's safe arrival, compare two decision versions, verify whether a condition was actually completed, or discover that a review was scoped more narrowly than public rumor claims. Do not turn a hearing into a lecture about invented law.

## Reusable narrative structures

### The decision that did not close the story

A contested incident receives a formal decision. One operational question is resolved, but restitution, service restoration, public correction or case review remains open. Months later the unresolved downstream obligation becomes the quest hook.

### Two correct records with different scopes

A public notice says the matter was resolved. An internal review record says one issue was remanded. Both are authentic because they address different subjects. The mystery is solved by scope and timestamps rather than corruption by default.

### New evidence after decision

A newly recovered photograph, archive record or Pokémon observation does not automatically erase the old decision. It creates a review trigger. The player can help establish whether the evidence is authentic, relevant and linked to the correct event.

### Compliance without moral conversion

An actor or institution can perform a required repair, return an object, restore access or publish a correction without becoming friendly, remorseful or politically aligned with the player.

### Process failure without villainy

A decision can be revisited because notice failed, the record was incomplete, a scope was misunderstood or a material fact emerged later. Institutional drama does not require a conspiracy.

## Guardrails for Pokémon agency

- A Pokémon can be a witness, affected party, accused actor, protected actor or source of an observation when communication/provenance supports it.
- Species stereotypes do not establish truthfulness, guilt detection, legal competence or testimony comprehension.
- Aura, telepathy, scent, memory reading, lie detection, foresight or similar capabilities require exact PTU/Caelo evidence before they alter fact-finding mechanics.
- A battle result does not prove an allegation.
- Capture does not create legal custody.
- defeating an accused actor does not authorize punishment.
- defeating a hostile group does not complete an appeal, hearing or compliance review.

## Research exclusions

This pass does not create a universal court system, criminal code, civil code, sentencing model, bail system, detention regime, property law, warrant power, evidence-admissibility doctrine, jury system, election mechanism or professional legal class for Ouros.

It does not copy prose, dialogue, characters, distinctive plots or real-world legal rules.

Public procedural sources are used only to extract state-machine and provenance concepts: record scope, decision lineage, review, remand, rehearing and implementation separation.

## Candidate design conclusion

Ouros can safely add a generic `public_adjudication_record` continuity layer if every deciding body, mandate, available remedy and review path must be supplied by canon. The layer should store what happened procedurally; it must never infer what law applies.
