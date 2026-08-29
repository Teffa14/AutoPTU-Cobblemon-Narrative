# Ouros Narrative Research — Interregional Arrival, Inspection, Hold & Release — Pass 124

Status: RESEARCH ONLY. This file preserves provenance and design evidence. Nothing here establishes Ouros canon, law, borders, inspection authority, ecological risk, ownership or battle mechanics.
Date: 2026-08-29

## Research question

The repository already models interregional visits and recognition, ports and transport hubs, courier custody, material provenance, batch traceability, conservation, Pokémon welfare, credentials, public notices, cases and civic mandates. The remaining design question is narrower:

How can Ouros preserve the history of a scoped arrival inspection or temporary hold when canon has already established a competent institution and mandate, without silently inventing national borders, customs law, immigration law, universal biosecurity powers or a generic suspicion system?

The desired structure is:

arrival or transfer -> inspection need identified by an authored rule/mandate -> scope and subject recorded -> documentary/identity/condition observations -> clear, hold, refer or request more evidence -> downstream handoff -> historical record retained.

The inspection episode must never manufacture the authority that caused it.

## Internal repository fit

`design/interregional-mobility-recognition-layer.md` already separates physical geography, cultural region, League service area, civic authority, conservation areas, service areas, actor association, location and temporary permissions. It explicitly does not establish passports, visas, citizenship, customs law, tariffs, immigration law, national borders or extradition. Pass 124 must preserve that boundary.

`design/port-harbor-berth-cargo-passenger-operations-continuity-extension.md` owns berth and port-call operations while explicitly declining to create a legal customs regime. A vessel or shipment being physically present at a port therefore cannot imply inspection, clearance or release.

`design/batch-traceability-recall-quarantine-extension.md` owns post-distribution product/batch problems, containment, trace, recovery and correction. An arrival inspection must hand a discovered product problem to that system rather than becoming a second recall subsystem.

`design/credentials-authorizations-recognition-extension.md` owns authored credentials and recognition. An authentic credential may still have the wrong scope for a particular facility, subject or activity.

`design/conservation-protected-areas-stewardship-layer.md`, `design/wildlife-monitoring-tagging-telemetry-extension.md` and `design/interspecies-ecological-relations-layer.md` own ecological interpretation. Arrival from another region is provenance, not proof of harm.

`design/case-authority-custody-layer.md` owns allegations, evidence and investigative custody when an actual case exists. A routine inspection discrepancy must not automatically create guilt or criminal status.

## Pokémon-world precedents

### Pal Park — a designated place for Pokémon arriving from elsewhere

Source: https://bulbapedia.bulbagarden.net/wiki/Pal_Park

Pal Park is a specific facility associated with Pokémon from other regions. In Kanto it replaces the former Safari Zone after that facility closes, preserving the broader lesson that a place can change institutional function while retaining geographic continuity.

Reusable structure for Ouros:
- cross-regional movement can terminate at a named receiving facility rather than becoming an abstract instant transfer;
- arrival facility identity can persist even when its prior use changes;
- receiving a Pokémon from elsewhere does not itself define ownership, ecological release, public access or institutional permission.

Do not copy Pal Park migration mechanics, catching-show scoring, transfer restrictions or named characters into Ouros.

### Poké Transfer Lab — transfer, study and destination are separate ideas

Source: https://bulbapedia.bulbagarden.net/wiki/Poke_Transfer_Lab
Source: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9_Transfer

The Poké Transfer Lab is explicitly described as a facility that studies Pokémon from faraway regions and hosts a transfer process. This supports a high-level worldbuilding pattern in which interregional movement may involve a specialized institution and an explicit handoff point.

Ouros transformation:
- transfer authorization, physical arrival, facility intake and later placement may be separate milestones;
- a research or receiving institution may have a narrow mandate without becoming a universal border authority;
- a facility can know that a Pokémon arrived from another region without knowing every ecological consequence of that arrival.

Do not import generation-transfer rules, minigames, National Pokédex requirements or irreversible transfer behavior.

### Alola — regional origin can matter without implying harm

Source: https://bulbapedia.bulbagarden.net/wiki/Alola_region

Alola's ecology includes Pokémon whose populations or forms are associated with different regional histories and environmental conditions. The reusable lesson is provenance sensitivity: where an individual or population came from can matter to ecological interpretation.

The guardrail is stronger than the inspiration. A Pokémon being nonlocal, recently arrived or associated with another region does not prove that it is invasive, dangerous, diseased or ecologically disruptive.

## External operational research used only as process architecture

### Inspection can have distinct evidence channels

Source: https://www.ippc.int/en/publications/598/

The International Plant Protection Convention's inspection guidance describes inspection as potentially involving documentary checks, visual examination, identity checks and integrity checks. Ouros can safely abstract the separation between these evidence channels without importing phytosanitary law, regulated-article definitions, standards or compliance thresholds.

Ouros lesson:
- document state, identity state, package/container integrity and direct observation should be separate fields;
- one channel can be complete while another remains pending;
- inspection scope must identify what was actually examined.

### Receiving station, inspection and release are separate milestones

Source: https://www.aphis.usda.gov/plant-imports/how-to-import/plant-inspection-stations

APHIS describes a staged process in which a shipment is transferred to an inspection station, documents and material are examined, and release occurs after the relevant checks. Pass 124 uses only the state-machine lesson: arrival, transfer to inspecting custody, inspection, finding/referral and release can occur at different times and under different actors.

No U.S. import rule, permit requirement, pest list, treatment authority, port arrangement or enforcement power is imported into Ouros.

### Hold does not itself prove a violation

Source: https://www.aphis.usda.gov/plant-imports/shipment-hold

APHIS publicly notes that a shipment hold may be temporary and can reflect waiting for review rather than a confirmed problem. This is a useful provenance guardrail.

Ouros lesson:
- `HOLD_ACTIVE` must not imply `NONCOMPLIANT_CONFIRMED`;
- a hold reason may be `AWAITING_REVIEW`, `AWAITING_EVIDENCE`, `IDENTITY_UNRESOLVED`, `REFERRED_TO_OWNER_SYSTEM` or another authored reason;
- a later clear/release event does not erase the historical fact that the subject was held while evidence was incomplete.

### Nonnative and invasive are different classifications

Source: https://www.usgs.gov/science/science-explorer/biology/invasive-species
Source: https://www.usgs.gov/centers/wetland-and-aquatic-research-center/science/science-topics/nonindigenous-species
Source: https://pubs.usgs.gov/publication/fs20243037/full

USGS distinguishes organisms outside their historical/native range from invasive organisms associated with established harmful effects. Ouros should preserve the same conceptual separation at a high level without importing U.S. ecological classifications.

Hard guardrail:

`ORIGIN_OUTSIDE_LOCAL_REGION != ECOLOGICAL_HARM_ESTABLISHED`

Likewise:

`INTRODUCED_OR_TRANSFERRED != ESTABLISHED_POPULATION`

`ESTABLISHED_POPULATION != INVASIVE_CLASSIFICATION`

Any Ouros ecological conclusion belongs to the conservation/ecology owner systems and requires actual world evidence.

## PTU/Caelo cross-check

The project's internal PTU/Caelo source scan supports campaign structures, exploration, standard Skills, species capabilities and exact authored environmental mechanics. It does not establish a universal customs, border inspection, biosecurity, quarantine-at-entry or immigration subsystem.

The following remain UNKNOWN unless an exact governing source or future Ouros canon establishes them:
- universal right to inspect a Trainer, Pokémon, bag, shipment or vehicle;
- generic border or customs checkpoints;
- universal permit requirements for interregional Pokémon movement;
- automatic ecological danger based on species origin;
- automatic disease screening or quarantine periods;
- generic inspection Skill DCs;
- automatic contraband detection;
- species-derived ability to detect prohibited material, disease or ecological risk;
- Move, Ability, Item or Trainer Feature effects that automatically clear an inspection;
- battle victory as a substitute for inspection, release or destination admission.

If a particular PTU Skill is later used for an observation task, its actual rule and the actor's authoritative state must govern that check. Narrative state cannot manufacture a new inspection mechanic.

## Reusable design lessons

1. Inspection is a scoped episode, not a permanent suspicion label.

2. Physical arrival, intake, inspection start, hold, referral, release and destination admission are separate timestamps.

3. Every inspection episode must reference an authored mandate or explicit institutional rule. If no mandate exists, the generator cannot invent one.

4. Documentary review, identity verification, physical observation and ecological/health interpretation must remain separate evidence channels.

5. A hold can mean incomplete information. It does not prove wrongdoing.

6. A clear/release result only applies to the authored scope. It does not grant every downstream permission.

7. Regional origin is provenance. Conservation/ecology decides whether it has ecological significance.

8. Pokémon transfer does not imply ownership transfer. Use Pokémon Agency, custody and existing relationship systems.

9. A detected concern should route to the correct owner system instead of expanding this layer into Care, Conservation, Batch Traceability, Case Authority or Maintenance.

10. Historical inspection records can generate later mysteries through changed manifests, aliases, station locations, revised mandates and different scopes without requiring corruption or deception.

## Originality and exclusion note

This pass uses public Pokémon material and public operational guidance only for high-level structures. It does not reproduce protected dialogue, distinctive plots, named characters as Ouros characters, legal procedures, regulatory thresholds or jurisdiction-specific powers.

No source in this file is canon by citation. All Ouros applications remain proposed until reviewed.