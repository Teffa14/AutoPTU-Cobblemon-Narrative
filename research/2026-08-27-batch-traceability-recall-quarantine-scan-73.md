# Batch traceability, recall, quarantine & correction research — Pass 73

Status: research/provenance only. Nothing in this file is canon.

## Research question

Ouros already has physical item instances and material batches, supplier fulfillment, storefront availability, courier distribution, care, facility maintenance, public notices, case/custody and found-property systems.

The missing operational question is narrower:

How does a persistent world represent a product, medicine, component, ingredient or equipment batch that has already entered circulation when new evidence suggests a defect, counterfeit substitution, labelling problem, contamination risk, compatibility issue or other reason to pause use, trace distribution, correct, quarantine or recover affected stock?

This pass deliberately begins after procurement acceptance or ordinary distribution. It does not replace Procurement, Material Culture, Courier, Storefront, Care, Maintenance or Case/Authority.

## Repository gap confirmed before external research

The full repository tree was inspected before this pass. Relevant existing layers include:

- `material-culture-economy-crafting-layer.md`: physical item instances, material batches, provenance, workshops and market state;
- Pass 72 procurement/commissioning extension: need, sourcing, supplier response, order, fulfillment, receipt, discrepancy and acceptance;
- `commercial-services-storefront-continuity-extension.md`: customer-facing availability and service continuity;
- `courier-parcel-last-mile-logistics-extension.md`: physical shipment/custody after dispatch;
- `care-recovery-welfare-layer.md`: health/care authority and privacy;
- `facility-maintenance-repair-inspection-extension.md`: technical condition, repair, verification and reopening;
- `public-notices-signage-world-information-extension.md`: projection of authoritative notices into the world;
- `case-authority-custody-layer.md`: formal evidence/custody when an event escalates into a case;
- `found-property-recovery-restitution-extension.md`: ordinary lost property before formal escalation.

None of these owns a general affected-batch identification -> distribution trace -> hold/quarantine -> notification -> recovery/correction -> effectiveness review lifecycle.

## Source 1 — Pokémon anime: Pokétch withdrawal during counterfeit crisis

Sources:

- Pokémon.com, “Not On My Watch Ya Don't”: https://www.pokemon.com/us/animation/seasons/10/episode-10-not-on-my-watch-ya-dont
- Bulbapedia, DP010: https://bulbapedia.bulbagarden.net/wiki/DP010

Observed structure:

- a desired consumer device is suddenly unavailable in normal shops;
- the manufacturer has withdrawn its legitimate merchandise because counterfeit devices are circulating;
- ordinary customers can encounter fake products outside the normal retail channel;
- a physical inspection provides evidence that a specific device is counterfeit;
- resolving the counterfeit source allows legitimate distribution to resume.

Reusable Ouros lesson:

A market withdrawal can be precautionary. The authentic stock itself does not need to be proven defective before a supplier pauses distribution. The world can temporarily distinguish `AUTHENTIC_BUT_HELD`, `SUSPECT_IDENTITY`, `CONFIRMED_COUNTERFEIT`, and `CLEARED_FOR_DISTRIBUTION` rather than collapsing everything into “bad product”.

Transformation rule:

Do not copy Jubilife, the Pokétch Company, Landis, Team Rocket, Psyduck signalling, device functions or plot beats. Reuse only the structure of counterfeit signal -> precautionary withdrawal -> item-level identification -> source investigation -> controlled return.

## Source 2 — Pokémon Support: counterfeit merchandise identification

Source:

- Pokémon Support, “Did I purchase fake or counterfeit cards?”: https://support.pokemon.com/hc/en-us/articles/360002068953-Did-I-purchase-fake-or-counterfeit-cards

Observed structure:

- counterfeit risk is not resolved by price alone;
- visual/material comparison can provide evidence;
- specialist shops may evaluate uncertain examples;
- official reference images help establish expected presentation;
- suspicious channel or price is a warning sign rather than proof.

Reusable Ouros lesson:

Claimed authenticity and verified provenance should remain separate. Packaging, markings, seller channel, serial/batch data and physical properties can all contribute evidence without any single heuristic automatically deciding truth.

## Source 3 — Pokémon anime: medicine production as a traceable process

Sources:

- Pokémon.com, “A Chip Off the Old Brock”: https://www.pokemon.com/us/animation/seasons/9/episode-3-a-chip-off-the-old-brock
- Pokémon.com, “A Better Pill to Swallow”: https://www.pokemon.com/us/animation/seasons/4/episode-13-a-better-pill-to-swallow

Observed structure:

- medicine can be produced by identifiable practitioners in a specific facility;
- ingredients/process and people involved in production are narratively legible;
- medicine availability and treatment can depend on production conditions rather than abstract shop stock.

Reusable Ouros lesson:

When canon eventually allows local production of a mechanically defined medicine or a narrative care product, provenance can refer to a production episode, facility, ingredient batch and custodian chain. This does not authorize the narrative system to invent medicine effects, recipes, dosage, healing amounts or Pokémon-powered production bonuses.

## Source 4 — Pokémon anime: medicine scarcity after a multi-patient incident

Source:

- Pokémon.com, “The Brockster Is In!”: https://www.pokemon.com/uk/animation/seasons/13/episode-33-the-brockster-is-in

Observed structure:

- a sudden poisoning event creates demand beyond the available medicine supply;
- ordinary passengers can contribute existing stock;
- insufficient quantity becomes an operational problem distinct from diagnosis or treatment rules.

Reusable Ouros lesson:

A recall or quarantine can create downstream scarcity even when the affected product is not the cause of the current crisis. Care owns treatment decisions; Storefront/Procurement owns replacement access; this new layer should expose how much usable stock is held, cleared, recovered or still untraceable without inventing healing mechanics.

## Source 5 — TGA market-action distinctions

Sources:

- Therapeutic Goods Administration, “Recalls and other market actions”: https://www.tga.gov.au/safety/recalls-and-other-market-actions
- TGA, “Procedure for recalls, product alerts and product corrections (PRAC)”: https://www.tga.gov.au/safety/recalls-and-other-market-actions/procedure-recalls-product-alerts-and-product-corrections-prac

Observed real-world structure used only as workflow inspiration:

- recall, product alert, product correction and quarantine are distinct actions;
- affected goods may be identified by product, batch/lot, serial, manufacture date or other identifiers;
- action depth depends on how far the goods have travelled through distribution;
- a suspected problem can justify action before every detail is known;
- distribution history matters because affected stock can sit with wholesalers, institutions, retailers or end users;
- finalisation requires more than issuing the first notice.

Reusable Ouros lesson:

The useful design structure is `emerging signal -> affected-scope hypothesis -> containment action -> trace -> notification -> correction/recovery -> effectiveness review -> closure`. Ouros must not import Australian law, deadlines, regulatory authority, medical terminology or mandatory obligations unless separately approved as canon.

## Source 6 — ACCC product-recall traceability

Sources:

- ACCC Product Safety, “Identify affected products and assess the risk”: https://www.productsafety.gov.au/business/recall-an-unsafe-product/identify-affected-products-and-assess-the-risk
- ACCC Product Safety, “Supplier checklist for conducting a recall”: https://www.productsafety.gov.au/business/recall-an-unsafe-product/recall-tools-and-guidelines/supplier-checklist-for-conducting-a-recall

Observed workflow structure:

- identify product, model, serial/batch and production date;
- stop further distribution when warranted;
- determine how many affected units remain in the chain or reached users;
- identify where the defect entered the chain;
- correct the root cause and verify the fix.

Reusable Ouros lesson:

A persistent world benefits from exact `batch_id`/`item_instance_id` references and distribution edges. A recall should not magically know where every unit is unless records or observations support that knowledge.

## Source 7 — TGA contamination/shortage interaction

Source:

- TGA, “Reporting a shortage or discontinuation of a medicine you supply”: https://www.tga.gov.au/resources/guidance/reporting-shortage-or-discontinuation-medicine-you-supply

Observed workflow pattern:

A contamination finding can trigger withdrawal of multiple batches and create a separate shortage problem while replacement stock is arranged.

Reusable Ouros lesson:

One event can create two different world states:

1. a traceability/containment problem for affected stock;
2. a service/supply problem for replacement availability.

The first belongs here. The second is handed to Procurement, Storefront, Care, Events or another owning system.

## High-level structures extracted

### Signal is not diagnosis

A complaint, failed inspection, unusual outcome, mismatched label, counterfeit report or damaged package starts an investigation. It does not automatically establish defect, contamination, fraud or causation.

### Scope must be versioned

Early action may cover a broad family because the exact affected lots are uncertain. Later evidence may narrow or expand the scope. Earlier notices remain historical evidence rather than being silently rewritten.

### Hold, quarantine, correction and recall are different

A unit can be held before distribution, quarantined at a location, corrected in place, recovered from circulation, destroyed/disposed of under an owning system, or cleared after review. Those states should not be collapsed.

### Traceability follows actual evidence

Distribution knowledge comes from procurement receipts, courier handoffs, storefront sales/issue records, shared-equipment checkout, care usage records where privacy permits, found-property evidence, or direct observation.

### Unknown location is a valid state

If eight units were distributed but only six are located, the system should represent two `UNLOCATED` units. It must not teleport them back into inventory or spawn them in a convenient chest.

### Correction does not erase exposure history

A repaired device, relabelled container, replaced component or corrected instruction remains linked to the original market-action episode and item history.

### Recall success needs effectiveness evidence

Issuing a notice does not prove everyone saw it. A recovery target may remain incomplete because a user is travelling, a shop is closed, a parcel was forwarded, a unit was consumed, an item changed custodian, or records disagree.

### Supply continuity is a separate problem

Removing affected stock may create shortages, delayed repairs, cancelled services or substitutions. Those consequences hand off to the systems that own supply and service availability.

## Patterns deliberately rejected

Do not add by default:

- a universal Ouros regulator;
- mandatory legal recall powers;
- product-liability law;
- warranties;
- negligence/fraud presumptions;
- fixed risk classes;
- mandatory public disclosure rules;
- serial numbers for every ordinary object;
- guaranteed perfect distribution records;
- contamination percentages;
- spoilage clocks;
- medicine dosage;
- mechanical adverse-effect tables;
- automatic compensation/refunds;
- automatic destruction authority;
- automatic criminal investigation;
- universal barcode technology.

Any of these require explicit canon and/or mechanics.

## PTU/Caelo mechanical boundary

This layer may track a mechanically defined item or medicine by stable reference. It may not invent or modify that item's battle behavior.

If a narrative signal is “this held item appears to behave incorrectly in battle”, the authoritative evidence is the actual AutoPTU rule implementation/transcript for that exact item behavior. The narrative layer cannot create a defective mechanical variant unless PTU/Caelo plus the engine explicitly support such a variant.

If a suspect product would create poison, Burn, slowed movement, reduced Accuracy, terrain, weather, delayed damage, reactions or any other tactical effect, those exact capabilities must be verified before the battle implementation can use them.

## Encounter-design implications

Rich versions may involve:

- retrieving marked stock while actors move through a warehouse;
- isolating a spill or unstable container;
- protecting staff while they identify storage locations;
- containing a Pokémon disturbed by a storage-area incident;
- keeping civilians out of a temporarily restricted sales area.

These can require complete movement/interception/forced movement, terrain/hazards/zones/reactions, tactical AI and adapter/playback.

Reduced versions should remove civilians and affected goods from tactical resolution first, freeze the site into a safe static arena, resolve only the actual combat threat, then return to traceability/quarantine state afterward.

## Canon status

All Ouros-specific regulators, product categories, recall powers, lot-marking practices, notification duties, destruction rules, liability rules, compensation, medicine governance and technology remain UNDECIDED unless already established elsewhere.

This pass proposes a workflow vocabulary and original story candidates only. It does not promote any external element to Ouros canon.
