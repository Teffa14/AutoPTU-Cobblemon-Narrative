# Research Scan — Medication Use, Dispensing, Reconciliation & Safety — Pass 154

Status: research/provenance only. NON-CANON. No rules or lore are approved by this file.
Date: 2026-08-24

## Why this scan exists

The repository already has clear owners for adjacent domains:

- Care/Recovery/Welfare owns diagnosis, care plans, recovery and welfare observations.
- Toxicology owns hazardous agents, exposure routes, toxicological evidence and source attribution.
- Supply Chains owns procurement, stock, allocation, receiving and storage availability.
- Manufacturing owns production runs, lots, release, quality disposition and production-linked recalls.
- Health Surveillance/Outbreak systems own population-level case patterns and investigations.

What remained unowned was the medication-use chain after a treatment decision exists and before/while medicine is actually used: order/indication, dispensing, possession, administration, course history, reconciliation during transfers, suspected adverse medication events, return/disposal and handoff from a recall into care.

This scan therefore proposes an operational medication layer, not a second clinical system and not a pharmacology simulator.

## Repository duplication check

The complete current inventories of `design/`, `research/` and `proposals/` were reviewed before selecting this topic. Searches for medication, prescription, pharmacy, dispensing and pharmacology did not reveal a dedicated medication-use lifecycle layer. The closest existing documents are Care, Toxicology, Supply Chains and Manufacturing; their authority boundaries are preserved below.

## Pokémon sources

### A Chip Off the Old Brock — Pokémon.com

Source: https://www.pokemon.com/us/animation/seasons/9/episode-3-a-chip-off-the-old-brock

A pharmacy manufactures Pokémon medicine with staff, a doctor and Pokémon participation. Later, medicine is prepared and delivered to injured Pokémon during an emergency.

Reusable structure:

- medicine production and medicine administration are separate moments;
- staff, facility, formula and recipient all matter independently;
- an emergency can create a last-mile medication problem after the medicine itself exists;
- Pokémon may participate institutionally without becoming generic crafting machines.

Ouros transformation: a regional clinic/pharmacy can have persistent production/source relationships and a medication-use ledger, while Manufacturing remains the authority for how a batch was made.

### The Brockster Is In! — Pokémon.com

Source: https://www.pokemon.com/uk/animation/seasons/13/episode-33-the-brockster-is-in

Multiple young Pokémon are poisoned and Brock begins treatment, but available medicine is insufficient for everyone.

Reusable structure:

- stock availability and care need can diverge;
- triage/allocation can become a logistical and ethical problem without changing item mechanics;
- “medicine exists somewhere” is different from “enough suitable medicine is available here.”

Ouros transformation: shortages should flow Supply Chains -> Care/Medication Use, never directly from a visual empty shelf.

### An Electrifying Rage! — Pokémon.com

Source: https://www.pokemon.com/us/animation/seasons/19/episode-17-an-electrifying-rage

An injured paramedic asks the protagonists to deliver medicine during a regional disturbance.

Reusable structure:

- a medicine can be clinically appropriate yet operationally unavailable until physically delivered;
- the transport mission can be narratively meaningful without turning the medicine into battle cargo HP;
- delivery completion and administration remain separate events.

### The Island of Illusions! — Pokémon.com

Source: https://www.pokemon.com/us/animation/seasons/16/episode-30-the-island-of-illusions

A closed/low-tech Pokémon Center still treats wild Pokémon, and Nurse Joy prepares medicine from berries using simple equipment.

Reusable structure:

- regional technology levels can differ while care remains institutionally recognizable;
- a facility can continue to have ecological/community significance after its formal service model changes;
- low-tech preparation should not imply improvised PTU crafting unless exact rules support it.

### A Cellular Connection! — Pokémon.com

Source: https://www.pokemon.com/us/animation/seasons/19/episode-10-a-cellular-connection

Nurse Joy identifies a medicinal plant needed for an injured Bunnelby and the group retrieves it.

Reusable structure:

- identifying a needed therapeutic resource, sourcing it and using it are distinct steps;
- medicinal flora can create exploration hooks without granting every plant a mechanical restorative effect.

### Chansey Pokédex — Pokémon.com

Source: https://www.pokemon.com/us/pokedex/chansey

Chansey is associated with sharing nutritious eggs with injured Pokémon or people.

Guardrail: species flavor may support authored institutional roles or care observations. It does not create a universal healing rate, Restorative Item, prescription authority or automatic consent to work in care.

## PTU / project mechanics evidence

### PTU 1.05 Medicine Education

Public Core mirror surfaced by search:
https://peda.net/p/josajoki/fista/ohjeet/ptu/pokemon-tabletop-united-1.05-core%3Afile/download/c109e0ecc0ac41065575a4a324183b80189a2c70/Pokemon%20Tabletop%20United%201.05%20Core.pdf

The public Core text describes Medicine Education as covering healing, first aid, diagnosis, medical research and creation of treatments. It also defines `Medic Training` as a concrete mechanical Edge affecting Restorative Item use.

Project-local evidence is more important for implementation. `Teffa14/AutoPTU/reports/trainer_runtime_coverage.md` currently reports these as `missing_runtime_mapping`:

- Medic Training;
- Medical Techniques;
- Medicinal Blend;
- Nurse;
- Field Clinic [9-15 Playtest];
- Front Line Healer;
- Restorative Science;
- Apothecary and several adjacent crafting/medical entries.

Therefore the existence of those PTU concepts in imported data cannot be treated as Java/Python runtime coverage.

Mechanical rule for narrative design:

- any in-battle Restorative Item, Medic/Nurse/Field Clinic Feature, treatment action, Status cure or medical interrupt must cite an exact implemented contract before FULL use;
- the REDUCED version should perform legitimate care outside battle through world state and then open a conventional static encounter if conflict remains.

## PTU/community campaign material

### PTU campaign anecdote: nurse PC with Chansey

Source: https://www.reddit.com/r/rpghorrorstories/comments/c0vqya

The campaign setup includes a nurse character paired with Chansey alongside other specialist PCs. The useful structure is simply that medicine/care can be a persistent player-facing profession rather than a vending-machine service.

No characters, incidents or plot from the post are imported.

### PTU Core medical institutions guidance

Public rules mirror surfaced here:
https://pokemontabletop.fandom.com/wiki/Combat

The public text notes that campaigns without standard Pokémon Centers can use hospitals, town doctors or other equivalent medical institutions for recovery access.

Reusable lesson: Ouros can vary the institutional form of care by region without changing the underlying PTU authority for healing/recovery.

## Medication-safety architecture sources

These real-world sources are used only for high-level state separation. Ouros does not import real law, doses, prescribing standards, professional licenses, drug schedules or clinical treatment advice.

### AHRQ MATCH medication reconciliation toolkit

Source: https://www.ahrq.gov/patient-safety/settings/hospital/match/chapter-3.html

AHRQ treats medication reconciliation as a workflow across transitions in care, with explicit roles, records, comparisons and handoffs. The important design lesson is that multiple medication lists can exist and need reconciliation rather than one being silently overwritten.

Source: https://psnet.ahrq.gov/primer/medication-reconciliation

The updated primer explains how admission, transfer and discharge can create unintended discrepancies between prior and intended medication regimens.

Ouros transformation:

- preserve each source list/version;
- create reconciliation events rather than editing history;
- distinguish discrepancy from harm;
- distinguish discrepancy from wrongdoing.

### WHO Medication Without Harm

Source surfaced publicly at:
https://iris.who.int/bitstream/handle/10665/255263/WHO-HIS-SDS-2017.6-eng.pdf

High-level lesson only: medication harm can arise from medicine properties, communication, labels/packaging, professional actions and system design. Ouros should therefore preserve provenance instead of reducing every incident to “bad medicine.”

### AHRQ process evaluation

Source: https://www.ahrq.gov/patient-safety/settings/hospital/match/chapter-6.html

Useful structural lesson: a process can be implemented while still needing later auditing/review. In Ouros, a new reconciliation protocol can improve over several years and still produce edge cases.

## Reusable narrative structures

### Order, possession and use diverge

A clinician/care plan can call for a medicine; a pharmacy can dispense it; a patient/Trainer can possess it; the medicine can still never be administered. Each state should remain separately observable.

### The handoff discrepancy

Two institutions can hold internally coherent medication records that disagree after a transfer. The story is reconstruction, not instant blame.

### The recall that never touched the patient

A batch may be recalled while every relevant unit is still sealed or held in inventory. The recall becomes an operational event without forcing illness or injury.

### Improvement before administration

A patient can improve before the recorded first administration. This is a useful anti-causality mystery and protects Care from assuming that every improvement proves treatment efficacy.

### Suspected adverse event

A new symptom after medicine use can trigger review without immediately proving causation, allergy, toxicity or manufacturing defect.

### Rural last-mile care

The correct resource exists but route, weather, rail/ferry schedule or courier capacity delays arrival. World systems create the challenge; the medicine itself needs no new battle rule.

### Low-tech regional care

Different areas can use herbal preparation, manufactured items or mixed practices. Each preparation must be authored and cross-checked against PTU/Caelo before gaining mechanics.

## Anti-patterns for Ouros

Do not create a universal `medication_effectiveness` stat.

Do not equate `DISPENSED` with `ADMINISTERED`.

Do not equate `ORDERED` with `POSSESSED`.

Do not equate `ADVERSE_EVENT_AFTER_USE` with `CAUSED_BY_MEDICATION`.

Do not equate an old allergy/intolerance label with verified current mechanism.

Do not infer patient consent from custody, Trainer ownership, party membership or prior treatment.

Do not allow Minecraft inventory/container state to become clinical truth.

Do not turn a visual medicine bottle into a PTU Restorative Item without an exact item mapping.

Do not use real-world dosing, prescribing or treatment recommendations.

## Candidate systems handoffs

Care -> medication order/treatment intent.

Supply Chains -> suitable stock/lot available.

Manufacturing -> lot identity/release/recall provenance.

Medication Use -> dispensing, administration, reconciliation, suspected medication-event history.

Toxicology -> suspected harmful exposure analysis when applicable.

Health Surveillance -> multi-actor clusters only when population evidence exists.

Pokémon Agency -> consent/cooperation/custody history for Pokémon patients.

Material Culture/Items -> physical object/item identity when mechanically relevant.

## Canon status

No pharmacy, medicine brand, clinical institution, standard formulary, prescribing profession, medication law, item price, dose, treatment duration or regional policy is established by this scan.

All Ouros concepts derived from it remain PROPOSED until separately approved.