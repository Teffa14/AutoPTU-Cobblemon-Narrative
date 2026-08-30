# Ouros Narrative Research — Utility Service Point, Meter Reading & Billing Continuity — Pass 141

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-29

## Research question

What reusable narrative structure appears when a public or private utility has to connect physical service, a stable service point, a meter or observation device, readings, an account relationship, billing records, corrections and eventual disconnection/reconnection without collapsing those facts into one state?

This pass deliberately avoids building an electrical, water, gas, tariff, tax, debt-collection or real-world utility simulator. It looks for continuity patterns that can make ordinary streets, businesses, institutions and post-disruption recovery feel persistent in Ouros.

The selected gap is administrative and evidentiary. Existing Ouros layers already own physical utility state, outages, maintenance, money, people and places. What was missing was a neutral record of how an institution says a particular service point was observed and billed across time.

## Repository inspection and non-duplication check

The full recursive tree of `Teffa14/AutoPTU-Cobblemon-Narrative` was inspected before topic selection and returned `truncated: false` at head:

`2ec58fd1a360fbe3d9cb6366f8109b1c5a525948`

Relevant neighboring owners were then read directly:

- `design/electric-grid-generation-distribution-continuity-extension.md`
- `design/drinking-water-treatment-distribution-continuity-extension.md`
- `design/infrastructure-outage-restoration-extension.md`
- `design/finance-sponsorship-risk-layer.md`
- `design/human-identity-name-record-continuity-extension.md`
- `design/place-name-address-location-reference-continuity-extension.md`
- `research/2026-08-18-source-scan.md`
- `design/engine-readiness-snapshot-pass-140.md`

Repository search for `insurance claim coverage policy underwriting`, `meter utility billing reading outage account`, and `estimated meter reading` produced no dedicated prior owner for this continuity problem.

### Existing owner boundaries confirmed

Electric Grid already owns generation sources, electrical topology, sectors, observations, switching and technical restoration. Its service-sector state answers whether supply is available, not who is billed or which reading supports a bill.

Drinking-Water Continuity already owns source/treatment/distribution paths and endpoints. It explicitly ends at a service point or downstream owner handoff and does not create a customer-account model.

Infrastructure Outage owns multi-service loss, cascade, backup and restoration sequence. It does not decide whether an account is open, a read was estimated or a later bill was corrected.

Finance owns monetary commitments, transfers, receipt and narratively important financial provenance. It must remain the owner of actual payment/settlement facts.

Human Identity owns continuity between actor records and names. It can link an account holder to an actor only when evidence and privacy allow.

Place Reference owns persistent place identity, address descriptors, entrances and service-point references. A changed street name or entrance must not silently create a new utility endpoint.

The new candidate layer therefore has a narrow role: preserve the administrative continuity between a utility service point and its observed/estimated usage records, account relationships and billing references.

## Public Pokémon source: New Mauville

Source:
https://bulbapedia.bulbagarden.net/wiki/New_Mauville

Supporting walkthrough source:
https://bulbapedia.bulbagarden.net/wiki/Appendix:Ruby_and_Sapphire_walkthrough/Section_10

New Mauville is useful because one site carries several different truths across versions and media: it was conceived as an underground city, exists as a power facility, can become unsafe because of a generator problem, and in animation is a decommissioned plant that became habitat for Electric-type Pokémon.

Reusable high-level lessons:

1. A utility site has a history separate from its current function.
2. Physical access to the plant, operating state of a generator, supply to a city and later reuse of the site can all change independently.
3. A decommissioned technical site can remain socially and ecologically meaningful after its utility role ends.
4. An authored intervention can change one technical state without implying every downstream account, building or service state changed at the same moment.

Ouros transformation:

- retain stable utility-site and service-point identity across technical changes;
- allow old meter boxes, labels, cabinets, conduits and records to survive after service topology changes;
- use former utility assets as exploration/history spaces without declaring them live or dangerous by appearance;
- never infer billing, ownership or account state from a plant being visibly active.

No map, plot, character, reward, generator behavior or specific New Mauville history is copied into Ouros.

## Public fangame source: Pokémon Reborn — Yureyu Power Plant

Source:
https://pokemon-reborn.fandom.com/wiki/Yureyu_Power_Plant

The publicly documented Yureyu Power Plant reuses an abandoned industrial utility site as a Gym and puzzle space. Its prior industrial identity remains legible even though its current narrative function differs.

Reusable lesson:

`FORMER_UTILITY_FUNCTION != CURRENT_SITE_FUNCTION`.

A utility asset can outlive the organization that built it. Current users can inherit rooms, gates, labels, wiring routes or public memory without inheriting the former operator's authority, records or obligations.

Ouros transformation:

A former meter room, pump house, substation office or billing counter can later become a workshop, clubroom, habitat access point, archive annex or exploration site. Historical service-point references remain provenance, not proof of present connection.

The Reborn story, puzzle sequence, characters, Gym identity and rewards are not imported.

## Current Pokémon community signal: visible utility infrastructure should have legible consequences

Public community examples:
https://www.reddit.com/r/Pokopia/comments/1sdejhf/power_plant_build/
https://www.reddit.com/r/Pokopia/comments/1s5k5k6/the_abandoned_power_plant_is_up_and_running_it/
https://www.reddit.com/r/Pokopia/comments/1vvruwj/lost_power_plant_anyone_have_any_luck_with_this/

These 2026 Pokopia discussions repeatedly distinguish a visually recognizable power-plant build from the game's actual electricity-generating mechanics. Players then build water wheels, generators, substations, conduits and industrial surroundings to make the settlement's power story feel coherent.

Reusable lesson:

Players notice when visible world infrastructure and system consequences have no understandable relationship. The correct response for Ouros is not to make Minecraft blocks authoritative. Instead, authoritative utility state should drive visible consequences and readable history.

Transformation rule:

`VISIBLE_UTILITY_PROP != AUTHORITATIVE_SERVICE_STATE`.

But when Ouros says a block has normal service, presentation should have enough consistent cues that the world does not feel arbitrary.

## Operational source: Australian Energy Regulator — records can distinguish account, premises, meter and reading

Source:
https://www.aer.gov.au/applicable-conditions-exemption-class-r7

This public regulator material requires records that separately preserve customer name, premises address, meter identifier where applicable, account creation date, bills, most recent meter-read date and the basis of estimates. It also distinguishes current and previous reading/estimate values and requires estimated values to be identified as estimates.

The useful abstraction is data separation, not Australian regulation.

Ouros lesson:

A bill can refer to:

- an actor/account relationship;
- a service location;
- a specific meter or observation device;
- an observation period;
- one or more reading records;
- a calculation/charge record;
- a later payment record owned by Finance.

Those references should not be collapsed into a single `utility_bill_status` flag.

No Australian tariffs, time limits, complaint rights, units, legal duties or regulatory institutions are imported into Ouros.

## Operational source: actual versus estimated readings

Sources:
https://www.ewon.com.au/page/customer-resources/high-and-disputed-bills/estimated-bills-and-meter-reading
https://www.aer.gov.au/system/files/JGN%20-%20Attachment%204.7j1%20-%20IT%20capex%20source%20info%20-%20IB-Metering%20-%20Mass%20market%20no%20access%20-%20January%202020.pdf

The Energy & Water Ombudsman NSW explains that an inaccessible meter can lead to an estimated read and that a later actual reading may cause an adjustment. The AER-hosted Jemena material similarly distinguishes actual observations, estimates, self-read evidence and later correction.

Reusable architecture:

`READING_ESTIMATED != READING_OBSERVED`.

`ESTIMATE_ACCEPTED_FOR_BILLING != PHYSICAL_USAGE_OBSERVED`.

`LATER_ACTUAL_READING != PRIOR_ESTIMATE_WAS_FRAUDULENT`.

`BILL_CORRECTED != ORIGINAL_BILL_DELETED`.

This is valuable for mysteries because records can disagree legitimately. A high later bill can emerge from several accumulated estimates, meter replacement, delayed data transfer or a corrected mapping without any villain.

Ouros should preserve original issued records and append corrections rather than silently rewriting history.

## Operational source: delayed, missing or amended meter data

Source:
https://www.ewon.com.au/page/publications-and-submissions/reports/spotlight-on/metering-services/delayed-missing-or-amended-meter-data

EWON documents cases where delays between a metering service provider and retailer cause estimated bills, rebills and backbills, and where updated data arrives after an earlier bill was already issued.

Reusable lesson:

Observation time, data-received time and bill-issued time can be different.

Suggested event chain:

`OBSERVED -> TRANSMITTED -> RECEIVED -> ACCEPTED_FOR_PERIOD -> USED_IN_BILL -> LATER_AMENDED`

A late record can be valid without making the earlier actor dishonest. This gives Ouros a strong source of mundane chronology mysteries.

## Operational source: meter replacement versus connection-point identity

Sources:
https://www.aemo.com.au/energy-systems/electricity/national-electricity-market-nem/market-operations/retail-and-metering/metering-procedures-guidelines-and-processes
https://www.aer.gov.au/node/82718/ausnet-legacy-meter-replacement-plan
https://www.ewon.com.au/page/customer-resources/managing-your-account/digital-meters

AEMO describes the National Metering Identifier as identifying connection points and associated metering points for registration, transfer, change control and data transfer. Separate procedural material records which meter serials were installed, removed, reconfigured or left unchanged. Current Australian replacement programs likewise treat meter exchange as a process that can occur while the customer connection continues.

Ouros transformation:

Keep a stable `utility_service_point_id` independent from any one meter device.

`METER_REPLACED != SERVICE_POINT_REPLACED`.

`METER_SERIAL_CHANGED != LOCATION_MOVED`.

`SERVICE_POINT_PERSISTS != SAME_ACCOUNT_HOLDER`.

`ACCOUNT_HOLDER_CHANGED != METER_RESET`.

Do not import NMI, market roles, national registration systems, smart-meter mandates or technical metrology rules.

## Operational source: faulty meter versus physical outage

Source:
https://www.aer.gov.au/news/articles/news-releases/aer-takes-action-against-agl-not-promptly-fixing-customers-meters

The AER example shows faulty metering producing estimated consumption and billing problems. It provides a useful separation between a device used to observe usage and the underlying utility supply.

Ouros lesson:

`METER_FAULT != SERVICE_OUTAGE`.

`SERVICE_AVAILABLE != METER_DATA_AVAILABLE`.

`METER_DATA_AVAILABLE != BILLING_DATA_ACCEPTED`.

A building may have electricity while its measurement record is disputed. Conversely, a meter can report a valid historical reading after a later outage.

## Cross-source synthesis

The strongest reusable pattern from these sources is a chain of distinct identities and events:

```text
physical utility system
  -> service point
  -> meter/observation device association
  -> reading or estimate
  -> data receipt/acceptance
  -> billing period record
  -> issued bill or correction
  -> financial settlement handoff
```

Each arrow is provenance, not automatic equivalence.

The resulting layer can create persistent everyday stories without requiring new combat mechanics.

## Candidate data invariants

The following should become design guardrails:

`PHYSICAL_SERVICE_AVAILABLE != ACCOUNT_ACTIVE`

`ACCOUNT_ACTIVE != METER_ASSOCIATION_CORRECT`

`METER_INSTALLED != METER_READ_OBSERVED`

`METER_READ_OBSERVED != READING_ACCEPTED_FOR_BILLING`

`ESTIMATED_READING != OBSERVED_READING`

`SELF_REPORTED_READING != AUTOMATICALLY_VERIFIED_READING`

`READING_ACCEPTED != BILL_ISSUED`

`BILL_ISSUED != PAYMENT_SETTLED`

`PAYMENT_SETTLED != SERVICE_RECONNECTED`

`METER_REPLACED != SERVICE_POINT_REPLACED`

`OCCUPANT_CHANGED != SERVICE_POINT_MOVED`

`PLACE_RENAMED != SERVICE_POINT_REPLACED`

`METER_FAULT != UTILITY_OUTAGE`

`OUTAGE_RESTORED != BILLING_RECORD_CORRECTED`

`SERVICE_DISCONNECTED != DELINQUENCY_PROVEN`

`BILL_DISPUTED != METER_FAULT_PROVEN`

`ONE_PERIOD_CORRECTED != ALL_HISTORICAL_PERIODS_CORRECTED`

## Narrative opportunities

This continuity can support stories where:

- a street was renumbered while service points stayed physically unchanged;
- a meter was replaced and the new serial appears only in later records;
- a closed workshop still has old utility labels that lead to a decommissioned connection;
- several estimated readings are later reconciled with an actual observation;
- a temporary market or festival connection becomes a remembered piece of neighborhood history;
- a landlord, tenant, business operator and utility each hold different but legitimate records about the same site;
- a utility restores physical supply before customer-facing records catch up;
- a new occupant inherits a location but not the prior account relationship;
- a meter reading belongs to the correct device but the wrong period or service-point linkage;
- a field crew completes a meter exchange while Finance still has a pending correction.

## Pokémon agency boundary

No species, Type, Move, Ability, Pokédex flavor, animation or Minecraft behavior automatically proves that a Pokémon can:

- read a meter;
- detect unauthorized service;
- estimate consumption;
- inspect wiring or pipes;
- authenticate a reading;
- authorize reconnection;
- determine who owes money;
- identify a customer;
- safely access technical equipment;
- generate enough utility output for a settlement.

An individual Pokémon may have an authored institutional role only when character canon and governing PTU/Caelo mechanics support the relevant physical actions.

## PTU / Caelo cross-check

The project source scan confirms that PTU supports central plots, character arcs, sandbox activity, Jobs and location-specific environmental mechanics when exact source material defines them. Caelo provides activity containers and persistent location identity.

No reviewed project source establishes a universal subsystem for:

- utility accounts;
- electricity/water/gas bills;
- meter-reading Skill Checks;
- consumption estimation;
- tariff calculation;
- disconnection/reconnection authority;
- meter tampering detection;
- meter device HP or combat statistics;
- utility debt consequences;
- service entitlement based on Trainer rank;
- automatic technical authority from Technology Education;
- automatic inspection authority from a Trainer Feature;
- Electric/Water/Fire Type utility competence.

All remain UNKNOWN unless exact PTU/Caelo evidence is found.

## Battle implementation relevance

Most of this layer is world-state continuity and can run without battle mechanics.

Mechanically rich scenes can occur near a meter room, service alley, utility cabinet, temporary connection or field crew, but the battle must never resolve administrative truth.

Potential full-version dependencies include:

- complete movement including interception/forced movement for escort and withdrawal;
- full turn/round lifecycle for staged civilian/crew movement;
- terrain/weather/hazards/zones/reactions if an authored technical or environmental zone must matter tactically;
- objective-aware AI for PROTECT/WITHDRAW/CLEAR_ROUTE behavior;
- Minecraft/Cobblemon/Craftics adapter/playback for semantic presentation.

Reduced versions can remove inspectors, customers, records and equipment from BattleSpec, freeze utility administrative state, use reviewed static geometry and let tactical victory create only a narrow physical access fact.

## Canon questions intentionally left open

- Which Ouros regions use metered utilities at all?
- Which services are household-metered, institutionally allocated, communal or unmetered?
- Which institutions operate customer accounts?
- Which meter technologies exist?
- Which records are public, private or institution-only?
- How are new occupants, businesses or temporary users linked to a service point?
- What correction and review procedures exist?
- Which situations can lead to service restriction or reconnection?
- Are prices/tariffs present in canon, and if so which owner defines them?
- Which historical utility sites, counters, meter rooms and temporary connections exist?
- Which individual Pokémon, if any, have trained utility roles?

## Research-use conclusion

The source material supports a durable continuity pattern around service-point identity, meter replacement, observed versus estimated readings, delayed data, corrected billing and independent physical-service state.

This pattern is useful precisely because it creates believable disagreement without forcing malice. A later record can correct an earlier one while both remain historically real artifacts. An old meter can be genuine while no longer being associated with the current service point. A building can have service while its account or bill is unresolved. Those distinctions give Ouros new quests, mysteries and environmental storytelling while preserving owner boundaries.