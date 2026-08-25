# Research Scan 161 — Interregional Crossing Processing & Scoped Clearance

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-08-25

## Why this is a narrow extension, not a new border-law layer

Repository audit before writing found three important existing authorities:

- `design/interregional-mobility-recognition-layer.md` owns visits, regional associations, arrival/departure context and cross-region recognition, and explicitly does **not** establish passports, visas, citizenship, customs law, tariffs, immigration law or national borders.
- `design/credentials-permissions-eligibility-layer.md` already owns permission, eligibility and `access_checkpoint` decisions.
- Biosecurity, Supply Chains, Postal, Land Tenure, Illicit Networks, Institutional Review and Travel already own their respective specialist decisions.

Pass 161 therefore targets a smaller operational gap: how a bounded facility processes an actor, vehicle, Pokémon, parcel or consignment through several already-existing authorities without turning the facility itself into the source of every rule.

Proposed authority chain:

`arrival at processing point -> information/declaration state -> scoped screening -> specialist referral if needed -> bounded hold/review -> clearance decision for this crossing/scope -> physical release/handoff -> onward travel`

“Clearance” here means a recorded decision under an authored rule or permission scope. It does not create a modern nation-state, immigration service or customs regime.

## Source 1 — Pokémon League Reception Gate: one place can check bounded eligibility

The Pokémon League Reception Gate is a recurring Pokémon-world example of a physical gate where an official checks a specific progression condition before allowing onward travel. In Generations II and IV it consolidates badge checks at a facility connecting routes toward Victory Road; Kanto/Johto travel also passes through the building.

Reusable Ouros lesson:

- the facility is a physical node;
- the requirement belongs to the League rule/credential system;
- the guard/checkpoint observes or validates that requirement;
- successful validation only grants the authored route/access scope;
- failure to pass the check does not imply wrongdoing.

This is especially valuable because it keeps `checkpoint` separate from `border police` or `criminal investigation`.

Sources:

- Bulbapedia, Pokémon League Reception Gate: https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_League_Reception_Gate
- Bulbapedia, Gate overview: https://bulbapedia.bulbagarden.net/wiki/Gate

## Source 2 — PTU public campaign material: layered security checkpoints can be ordinary setting structure

The public Pokémon Tabletop forum campaign thread `Those first steps` includes a high-security laboratory reached only after security allows the party through an initial checkpoint. The useful structure is not the campaign’s vault fiction. It is that access can be layered: being allowed into a larger institution does not automatically grant every internal room or resource.

Reusable Ouros lesson:

A regional arrival, building entry, event registration and specialist-area permission can be separate checks with separate authority. The generator should avoid treating one successful checkpoint as `access_everywhere=true`.

Source:

- Pokémon Tabletop forum, `Those first steps`: https://www.tapatalk.com/groups/pokemon_tabletop/those-first-steps-t6688.html

## Source 3 — WCO Time Release Study: arrival and physical release are distinct events

The World Customs Organization’s Time Release Study Guide Version 4 (2025) measures elapsed time from arrival to physical release and treats the interval as a sequence of timestamped process events. The methodology also emphasizes process mapping, bottleneck identification, segmentation and coordination among several participating bodies.

Ouros does **not** import customs institutions or law from this source. The reusable systems lesson is procedural:

- arrival is not release;
- multiple authorities can contribute to one processing session;
- the session should preserve timestamps and handoffs;
- delays can have different causes;
- a process can be measured and improved without assuming misconduct.

This is useful for League facilities, protected-area gates, research transfer points, ferry/rail terminals, quarantine handoffs and freight depots even if Ouros never creates international customs.

Sources:

- WCO Time Release Study Guide Version 4: https://www.wcoomd.org/en/Topics/Facilitation/Instrument%20and%20Tools/Tools/Time%20Release%20Study
- WCO TRS overview, 2025 update: https://mag.wcoomd.org/magazine/wco-news-108-issue-3-2025/version-4-trs-guide/

## Source 4 — WTO/WCO release and clearance: screening, specialist review and release should stay separate

The WTO Trade Facilitation Agreement distinguishes pre-arrival information, risk-based selection, examination, release, review and cooperation among authorities. WCO material likewise separates risk assessment from the act of examination and from eventual release.

Pass 161 uses only the abstract workflow. It deliberately rejects importing tariffs, duties, national origin rules, seizure powers, broker licensing or real-world border law.

Reusable Ouros lessons:

- a declaration is information supplied by an actor/system, not automatically world truth;
- screening can decide whether more review is needed without determining guilt;
- referral to a specialist authority is not itself an adverse finding;
- release can be scoped to one object, route, activity or facility;
- post-event review can revise procedure without rewriting the original crossing event.

Sources:

- WTO Agreement on Trade Facilitation, especially Articles 7–10: https://www.wto.org/english/docs_e/legal_e/tfa_e.htm
- WCO release/clearance and risk-management overview: https://www.wcoomd.org/en/topics/wco-implementing-the-wto-atf/atf/release-and-clearance-of-goods.aspx
- WCO Risk Management Compendium overview: https://www.wcoomd.org/en/topics/facilitation/instrument-and-tools/tools/risk-management-compendium.aspx

## Source 5 — Queueing and bottlenecks should produce ordinary world history, not only crises

The 2025 WCO TRS update emphasizes measuring process stages and identifying bottlenecks. For Ouros, the valuable narrative transformation is that a crossing can accumulate operational history:

- a festival creates a temporary queue;
- one specialist desk is closed while the rest of the facility works;
- records arrive after the ferry;
- a wildlife movement pauses one lane;
- a cold-chain consignment receives priority storage while review continues;
- a new joint desk shortens a routine process over several years.

These are world consequences rather than automatic quests. A mature facility should solve most routine cases itself.

## Design lessons extracted

### A. A checkpoint is an orchestration point

The crossing facility should ask existing authorities for decisions. It should not duplicate them.

Examples:

- Credentials answers whether a badge, permit or invitation is valid.
- Biosecurity answers whether a translocation/pathway review is required.
- Supply Chains answers what consignment exists and its logistics state.
- Postal answers addressed parcel/mail state.
- Pokémon Agency answers identity/custody/partnership questions about Pokémon.
- Travel answers whether the onward service or route is operational.
- Land Tenure answers location/access rights.
- Institutional Review handles review/appeal when canon defines one.
- Illicit Networks/Cases handles allegations and evidence when independently supported.

### B. Declaration is not truth

A manifest, stated purpose, submitted identity or declared contents should be stored as a record with provenance.

It may be accurate, mistaken, incomplete, stale or deliberately false. The processing protocol must not silently choose which explanation is true.

### C. Referral is not accusation

A specialist referral may occur because:

- a live Pokémon needs a Biosecurity decision;
- a museum loan needs custody/provenance confirmation;
- a cold-chain batch needs receiving/storage coordination;
- an event credential needs host recognition;
- an unusual item needs a rules/authorization review;
- a route closure changed the intended onward connection.

None of those states creates a criminal case by itself.

### D. Hold must be scoped

A hold should say what is paused and why the facility cannot yet release it.

Possible scopes:

- one consignment;
- one parcel;
- one Pokémon transfer;
- one actor’s access to one route;
- one vehicle;
- one research sample;
- one admission event.

Avoid `everything_locked=true` unless an authored crisis truly closes the facility.

### E. Physical release and legal/administrative decision are separate

A clearance decision may exist while the onward train is cancelled.

A shipment may be physically staged while one record remains pending.

A route may reopen while an individual permission is still invalid.

### F. Pokémon must not become cargo by default

If a Pokémon crosses with a Trainer, institution or conservation project, Pokémon Agency remains authoritative for identity, partnership, custody and agency.

A declaration record may reference a Pokémon. It does not create ownership.

A specialist review may pause a translocation. It does not make the Pokémon contraband or hostile.

### G. Routine processing should compress

The generator should surface a crossing only when something meaningful changes:

- a new rule revision;
- an unusual specialist referral;
- a queue/bottleneck affecting plans;
- an outage;
- a route conflict;
- conflicting records;
- emergency operations;
- a historical callback.

Normal passage should remain background state.

## Explicit no-inferences

Do not infer:

- checkpoint -> national border;
- regional crossing -> immigration law;
- declaration mismatch -> crime;
- secondary review -> suspicion or guilt;
- Biosecurity referral -> invasive species finding;
- credential failure -> forged credential;
- cargo hold -> stolen goods;
- Pokémon listed on paperwork -> ownership;
- Pokémon refusing to proceed -> disobedience or Loyalty loss;
- successful battle -> clearance granted;
- guard defeated -> permission obtained;
- gate open in Minecraft -> access authorized;
- gate closed in Minecraft -> authorization revoked;
- item physically present -> declared/accepted/cleared;
- cleared item -> delivered to final recipient;
- faster processing -> weaker security;
- slow processing -> corruption.

## PTU/Caelo mechanical cross-check

No PTU mechanic was verified in this scan that creates a general `checkpoint`, `customs`, `border search`, `clearance`, `manifest` or `inspection` subsystem.

Badge-gated locations in Pokémon provide narrative precedent, not PTU mechanics.

Existing Ouros Credentials may eventually reference exact PTU Skills/Features when the project’s rules source authorizes them, but Pass 161 must not invent Charm, Guile, Command, Perception or Pokémon Education DCs for processing.

No complete primary Caelo corpus defining interregional clearance was accessible in the project repositories searched in this runtime. Super PTU Online Helper was not exposed as an invocable capability. No output is attributed to either.

## Candidate Ouros conclusion

The useful addition is not “customs.” It is a neutral, scoped processing protocol that lets a physical crossing coordinate existing permissions, cargo, Pokémon agency, biosecurity and travel state while preserving uncertainty and provenance. It can support League gates, protected sites, ferry/rail arrivals, research transfers and future canon-specific border institutions without forcing any of those institutions into existence now.