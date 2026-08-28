# Ouros Narrative Research — Cold-Chain & Temperature-Controlled Custody Scan 112

Status: RESEARCH / PROVENANCE ONLY. This file is not Ouros canon and creates no PTU rules.
Date: 2026-08-28

## Why this pass exists

The repository already models storage, courier custody, procurement, food, care, batch traceability, electric service and infrastructure outages. The complete repository inventory was inspected before writing this pass. Searches for `cold chain`, `refrigeration`, `temperature excursion` and `cooling dependency` found no dedicated continuity layer.

Storage can label a zone `REFRIGERATED_STORAGE` or `specialized environment`, but intentionally does not decide whether a temperature-sensitive subject remained within an authored condition, whether a monitoring gap matters, whether a shipment remained valid after an interruption, or whether exposed stock must be held for review. That cross-system lifecycle is the gap researched here.

This pass uses `temperature-controlled` broadly. It does not assume that Ouros uses modern refrigeration everywhere, that every region has the same technology, or that every food/medicine/item has a temperature requirement.

## Existing Ouros authority that must remain intact

- Storage/Warehousing owns facility, zone, slot, putaway, internal movement, staging, physical-presence observations and capacity/overflow.
- Courier owns shipment legs and custody transfers.
- Procurement owns sourcing, receipt and acceptance.
- Food/Agriculture/Hospitality owns food provenance and PTU-food references without inventing Digestion effects.
- Care owns treatment and care-supply use without inventing healing.
- Batch Traceability owns hold, quarantine, recall, correction and clearance workflows.
- Technology/Energy and Infrastructure Outage own utility/service state and recovery handoffs.
- Facility Maintenance owns fault, repair and verification of equipment.
- PTU/Caelo/AutoPTU own mechanical item, Move, Ability, Feature, damage and status behavior.

A cold-chain layer therefore needs to own only continuity evidence: authored condition requirements, monitoring observations, exposure windows as evidence records, continuity segments, transfer verification, excursion hypotheses, temporary protection arrangements and downstream review handoffs.

## Public Pokémon source 1 — Unova Cold Storage

Source: https://bulbapedia.bulbagarden.net/wiki/Cold_Storage
Supporting multilingual description: https://wiki.pokemoncentral.it/Deposito_Frigo

Useful observations:

- Driftveil has a dedicated low-temperature goods-storage district associated with warehouse and port activity.
- Workers, containers, stored goods and an explorable interior coexist in one industrial place.
- The same physical area is later demolished and reused for the Pokémon World Tournament.

Reusable structures for Ouros:

1. Temperature-controlled storage can be part of ordinary settlement logistics rather than a special dungeon technology.
2. A cold facility can have workers, receiving/staging areas, restricted spaces and a social history independent of its refrigeration equipment.
3. An obsolete facility can disappear while its location history, former workforce, route habits and stored-goods stories remain available for later callbacks.
4. A visibly icy floor is presentation evidence only. It does not establish safe storage condition, a PTU Ice terrain rule, slipping, forced movement or cold damage.

Not imported:

- Driftveil, Team Plasma, Zinzolin, the container encounter, exact layout, ice-slide puzzle, items, dialogue or plot.

## Public Pokémon source 2 — The Ice Cave!

Sources:
- https://www.tvthatrocks.com/tvshow/pok-mon/season-5/episode-41/
- supporting episode summaries indexed publicly under Pokémon Master Quest episode 41.

Useful observation:

The episode describes a large refrigeration installation whose operation is tied to the cold state of a larger cave environment; disruption changes the thermal situation beyond the machine room itself.

Reusable structures for Ouros:

1. A temperature-control asset can have a wider environmental or service dependency footprint than the room containing it.
2. Machine state, zone condition and downstream ecological/operational consequence should be separate records.
3. Reversing, damaging or losing equipment does not authorize the narrative system to invent temperature arithmetic, environmental damage, status effects or species responses.
4. Restoration can require equipment repair first and independent verification of downstream spaces afterward.

Not imported:

- characters, Team Rocket action, exact mechanism, exact cave, Jynx role, illness, thermal values or episode plot.

## Public Pokémon source 3 — A Shocking Grocery Run!

Sources:
- https://bulbapedia.bulbagarden.net/wiki/SM006
- https://www.serebii.net/anime/epiguide/sunmoon/949.shtml

Useful observation:

A blackout in a shopping environment interrupts normal activity and separates actors while food retail remains a recognizable dependent service context.

Reusable structures for Ouros:

1. Upstream power failure and downstream temperature-control continuity are separate facts.
2. `POWER_LOST` does not by itself prove `CONTENTS_EXPOSED`, because backup, thermal inertia, alternate storage, unopened units or incomplete evidence may matter.
3. `POWER_RESTORED` does not by itself prove that every temperature-sensitive batch is cleared for use or sale.
4. A mundane service disruption can create social, navigation and logistics scenes without becoming a combat encounter.

Not imported:

- characters, mall layout, blackout cause, episode sequence or Pokémon-specific solution.

## External operational reference — monitoring and excursion evidence

Sources:
- CDC, Vaccine Storage and Handling / Pink Book: https://www.cdc.gov/pinkbook/hcp/table-of-contents/chapter-5-vaccine-storage-and-handling.html
- CDC, Storage and Handling of Immunobiologics: https://www.cdc.gov/vaccines/hcp/imz-best-practices/storage-handling-immunobiologics.html
- FDA, Sanitary Transportation of Human and Animal Food: https://www.fda.gov/food/food-safety-modernization-act-fsma/key-changes-fsma-final-rule-sanitary-transportation-human-and-animal-food

Only high-level workflow lessons are reused:

- condition should be observed rather than inferred from the visual state of equipment;
- delivery/receipt can include a condition check;
- a monitoring record and the physical goods are separate objects;
- an out-of-range observation can trigger isolation/hold and documentation before final disposition;
- transport preparation and transport monitoring can be separate from the later receiving decision;
- uncertainty after an excursion can be preserved until a competent owning system evaluates it.

Explicit exclusions:

No real-world temperature ranges, time limits, product stability rules, vaccine practices, food rules, legal duties, inspection frequencies, regulatory authorities, equipment standards or disposal requirements become Ouros canon. Real thresholds are product-specific and jurisdiction-specific; Ouros may only use a concrete threshold when its own authored canon/mechanical source defines one.

## Internal PTU / Caelo cross-check

The existing internal source scan identifies these governing project sources:

- CoreRulebook.pdf;
- Caelo Player's Guide 1.5.pdf;
- Caelo Region Location & Encounter List.pdf;
- character creation merged.pdf;
- Erratas and extra merged.pdf;
- Pokedex / pokedex merged.pdf.

The current project evidence supports authored location effects when an exact PTU/Caelo source defines them. It does not establish a universal cold-chain system.

This scan found no governing project evidence for automatically inventing:

- spoilage timers;
- medicine potency degradation;
- food-safety thresholds;
- refrigerator/freezer temperature bands;
- thermal inertia calculations;
- cold-room damage;
- automatic Frozen or other statuses from storage temperature;
- Ice-type immunity to occupational cold;
- cooling output by species or Type;
- a generic Move-powered refrigerator;
- refrigerated-vehicle capacity or thermal performance;
- Skill checks that universally certify temperature-controlled goods.

If a concrete PTU food, medicine, item, Move, Ability, Trainer Feature or location rule supplies a mechanical effect, it remains owned by that governing source and requires AutoPTU implementation evidence before battle use.

## Design lessons extracted

### Condition continuity needs its own evidence chain

A temperature-sensitive subject can move through several systems while keeping one continuity record:

accepted subject -> storage segment -> staging -> transport segment -> transfer -> destination storage -> use/release decision.

Custody changes do not automatically prove condition continuity. Condition continuity also does not transfer custody.

### Monitoring gaps are not automatically failures

A missing observation means `UNKNOWN_FOR_INTERVAL` unless another source proves the condition. It is not equivalent to `EXCURSION_CONFIRMED`.

### Excursion is a hypothesis before disposition

An observed condition outside an authored requirement can create an excursion record. The cold-chain layer preserves what was observed, when, where and which subjects may be affected. Batch Traceability/Care/Food/other owner decides hold, clearance, discard, correction or use according to governing canon.

### Upstream recovery and downstream clearance are separate

Power restored -> refrigeration asset may recover -> zone may stabilize -> monitoring may verify -> affected subjects may still require independent review.

### Temporary continuity can become world history

Portable cool storage, an alternate depot, a night transfer route or a borrowed clinic refrigerator can begin as a workaround and later become a recurring institution, landmark, relationship or preparedness practice.

## Candidate narrative patterns derived from the research

- The cold room is operational, but one monitoring interval is missing.
- A delivery arrives on time, but its condition evidence belongs to the previous carrier and has not been reconciled.
- Power returned hours ago, yet one batch remains held because its history is incomplete.
- A temporary cold room changes which market street receives morning deliveries.
- A clinic and restaurant compete socially for scarce temporary cooled space without the system inventing legal priority.
- An old refrigerated warehouse is demolished, while former workers still use its old bay numbers when giving directions.
- A Pokémon repeatedly rests near a cold-room door; the observation may be meaningful behavior but does not prove refrigeration capability, cold immunity or a job role.

## Research classification

CANON-APPROVED from this pass: none. This pass does not alter established Ouros lore.

PROPOSED: a narrow cold-chain continuity authority between existing storage/courier/outage/batch/care/food systems.

UNCERTAIN / requires future canon: technologies, regional prevalence, which goods are temperature-sensitive, exact authored condition requirements, institutional operators, monitoring methods, backup methods, privacy/record rules, and any individual Pokémon work roles.

MECHANICALLY UNKNOWN: all temperature thresholds, thermal hazards, cold damage/status, slippery terrain, refrigerated-vehicle effects and Move/Ability/Item/Trainer Feature interactions unless verified by exact governing rules plus live engine contracts.

## Copyright / transformation note

No protected dialogue, prose, distinctive characters, dungeon layouts or plots are copied. Public sources are used only to extract abstract continuity structures, state separations, investigation patterns and worldbuilding lessons.