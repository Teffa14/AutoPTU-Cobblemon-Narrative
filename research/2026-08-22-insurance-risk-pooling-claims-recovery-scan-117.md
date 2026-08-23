# Ouros insurance, risk pooling, claims & recovery research scan — Pass 117

Status: RESEARCH / PROVENANCE ONLY. Not canon. No insurance institution, contract law, premium formula, liability rule or mechanical payout is established by this document.

## Why this pass exists

The existing Finance layer already anticipates `INSURANCE_OR_RISK_TRANSFER`, but explicitly keeps loan/credit/insurance disabled until Ouros establishes institutions and rules for them. That makes insurance a real architectural gap rather than a new subsystem invented over existing canon.

Relevant internal boundaries inspected before writing:

- `design/finance-sponsorship-risk-layer.md` — money commitments, funding, risk and the explicit disabled insurance category;
- `design/crisis-rescue-recovery-layer.md` — hazard truth, impact, response and long recovery;
- `design/agreements-mediation-repair-layer.md` — promises, commitments, disputes and repair;
- `design/institutional-review-adjudication-sanctions-layer.md` — bounded mandate, decisions and review;
- `design/supply-chains-procurement-inventory-layer.md` — replacement goods, reserves and shipment state;
- `design/material-culture-economy-crafting-layer.md` — persistent items and provenance;
- `design/architecture-built-environment-adaptive-reuse-layer.md` — physical condition and repair history;
- `design/pokemon-agency-partnership-release-layer.md` — Pokémon identity/agency, which must remain outside asset-loss accounting;
- recent engine snapshots through Pass 116.

The design target is narrative risk transfer, not an actuarial simulator.

## Source 1 — Pokémon Expedition public fangame

Source: Pokémon Expedition by PkmnTrainerKatelyn.

URL: https://pkmntrainerkatelyn.itch.io/pokmon-expedition

The current public project description includes a persistent financial layer with property and commercial insurance, business interruption, liability, hotel operations, repairs and insurer-specific coverage concepts.

Reusable high-level structures:

- insurance can sit beside property ownership, business operations, maintenance and repairs rather than replace them;
- one property can have a specific coverage relationship rather than a universal player-wide protection flag;
- business interruption can matter even when the building survives physically;
- preventive maintenance can matter to a risk relationship without becoming an automatic mechanical discount;
- claims can be part of a larger persistent economy instead of a one-time quest reward.

Transformation for Ouros:

Do not import the named insurers, products, prices, taxes, mortgages, formulas or exact coverages. The useful pattern is simply that persistent institutions may share or transfer financial consequences after an already-authoritative world event.

This source is fan-made and is not Pokémon canon or PTU rules evidence.

## Source 2 — PTU Campaign Seeds: The Road to Tomorrow

Source: Pokémon Tabletop RPG official community blog, “Campaign Seeds: The Road to Tomorrow.”

URL: https://pokemontabletop.com/campaign-seeds-the-road-to-tomorrow/

This PTU campaign material emphasizes rebuilding, resource shortages, restoration of technology, settlement creation and decisions whose consequences last for generations.

Reusable structures:

- recovery is a campaign layer, not the end screen after a crisis;
- players may influence which infrastructure is rebuilt first;
- reserves, replacement materials and institutional capacity can become long-term consequences;
- repeated shocks are more interesting when earlier preparation changes later options;
- communities can become more resilient through accumulated decisions rather than only through stronger combatants.

Transformation for Ouros:

Risk transfer can attach to the existing recovery graph. It should never create the hazard, determine whether a bridge physically failed or overwrite Crisis/Architecture truth. It only changes who bears some authorized financial/resource consequence after the relevant facts are established.

## Source 3 — public PTU campaign premise built around prolonged disaster recovery

Source: public r/PokemonTabletop recruitment post, “Looking for players for an ongoing PTU game” (2024).

URL: https://www.reddit.com/r/PokemonTabletop/comments/1hgbuha/

The campaign premise describes a region whose economy depended on tourism, suffered multiple worsening hazards, evacuated people into protected spaces and remained partially uninhabitable decades later.

Reusable structures:

- disasters can create multi-decade financial and settlement consequences;
- tourism-dependent regions may face indirect loss even where individual buildings remain intact;
- rebuilding decisions can differ by district and service;
- long recovery gives institutions memory of earlier failures and adaptations;
- economic effects should remain distinct from the physical hazard and from causal investigation.

Transformation for Ouros:

Use only the structural lesson. Do not copy the region, apocalypse, vaults or plot.

## Source 4 — risk pooling and mutualization as an abstract design pattern

Source: World Bank material on public-asset risk pooling and mutualization.

URL: https://documents1.worldbank.org/curated/en/099808311072326644/pdf/IDU09db7211707080045fb0afff0b631473f2aee.pdf

Reusable abstract principles:

- a pool can spread losses across multiple participants instead of requiring one actor to bear the entire shock;
- pooling works at the portfolio/community level and is separate from the underlying physical loss;
- reserves and pooled capacity can make recovery more predictable;
- several members may contribute while only some receive support after a particular event;
- pooled support needs explicit membership, scope and allocation rules.

Transformation for Ouros:

Ouros should not copy real insurance regulation, actuarial formulas, public-finance law or country-specific programs. A fictional mutual-aid pool can simply be an authored institution with contributions, coverage scope, reserves, claims and decisions.

## Source 5 — 2026 research on stable risk-sharing pools

Source: Blier-Wong & Lauzier, “Designing entry-monotone risk-sharing pools” (2026).

URL: https://arxiv.org/abs/2606.00972

Useful design lesson:

A risk-sharing pool is not automatically stable merely because pooling can reduce aggregate risk. Participation terms and allocation rules matter to whether members remain willing to participate as the pool changes.

Transformation for Ouros:

This supports long-term story material where a mutual fund grows, loses members, changes eligibility or renegotiates its rules. No equations, actuarial pricing or mathematical allocation model should be imported.

## Source 6 — community-based proportional risk sharing research

Source: Denuit, Flores-Contró & Robert, “Linear Risk Sharing in Community-Based Insurance” (2026).

URL: https://arxiv.org/abs/2603.29530

Useful design lesson:

The benefit of pooling depends on the design of how losses are shared and on assumptions about the participating risks. Pooling is therefore a governance/contract problem as well as a finance problem.

Transformation for Ouros:

A cooperative repair fund may work well for routine storm damage and poorly for a single correlated catastrophe that hits every member at once. That is a narrative capacity constraint, not a formula the game needs to simulate.

## High-value design conclusions

### 1. Loss truth comes from domain state, not the claim

A claim that “the warehouse roof was destroyed” cannot create the roof damage.

Architecture, Crisis, Manufacturing, Supply Chains, Maritime, Rail, Fisheries or another domain layer must already establish the relevant physical/operational state.

Insurance records reference those facts.

### 2. A claim is not automatically fraud because it is wrong

A claim can be:

- accurate;
- incomplete;
- based on an obsolete asset record;
- based on an honest valuation disagreement;
- duplicated accidentally;
- unsupported by available evidence;
- outside the coverage scope;
- filed too early;
- filed after another institution already repaired the asset;
- intentionally deceptive, but only when evidence supports that conclusion.

Cases/Institutional Review handle investigation and adjudication when needed.

### 3. Covered is different from paid

Preserve distinct states:

`LOSS OBSERVED → NOTICE → CLAIM FILED → EVIDENCE GATHERED → COVERAGE REVIEW → LOSS ASSESSMENT → DECISION → PAYMENT AUTHORIZED → PAYMENT SENT → PAYMENT RECEIVED → RECOVERY USE`

Do not collapse them into one `insured=true` flag.

### 4. Replacement is not restoration

A payout may help fund a replacement asset while:

- heritage value remains lost;
- ecological damage remains;
- a Pokémon habitat remains changed;
- public memory remains;
- records/provenance remain incomplete;
- the service remains offline while work continues.

### 5. Insurance does not own the recovery project

A risk-transfer institution may authorize money. Architecture, Infrastructure, Supply Chains, Conservation, Workplaces and other domain systems still own the actual recovery state.

### 6. Business interruption can exist without building destruction

Examples:

- ferry service stops because a channel closes;
- tourism drops after a smoke episode;
- a factory has power but lacks a critical input;
- a market building remains intact but the only access bridge is closed;
- a hotel remains habitable but a regional evacuation order prevents guests from arriving.

Whether any of these are covered is authored contract state, not an automatic rule.

### 7. Mutual aid is a valid alternative to commercial insurance

Ouros does not need banks and insurers everywhere.

Possible authored arrangements include:

- town repair mutual;
- harbor vessel pool;
- farm/weather reserve;
- League venue recovery pool;
- museum conservation reserve;
- craft-guild replacement fund;
- cross-settlement disaster reserve;
- club emergency equipment pool.

These are proposals until canon establishes them.

### 8. Pokémon cannot be reduced to insured property by default

A claim may concern:

- veterinary/care costs if canon later permits that concept;
- damaged equipment used by a Pokémon;
- interrupted institutional service involving a Pokémon;
- a missing cargo shipment that also carried Pokémon, handled through custody/agency rules.

But insurance does not define Pokémon ownership, value, consent or replacement. No Pokémon should be given a market replacement value by this layer.

### 9. Preparedness can change financial consequences without creating mechanical buffs

A facility with documented maintenance, backups, spare parts or redundancy may have fewer operational losses after an event because those systems actually functioned.

Do not translate “prepared” into arbitrary reduced damage. Crisis/Infrastructure determines physical outcome. Finance/Risk determines later resource consequences.

### 10. Pooled reserves create longitudinal story

A fund can remember:

- who contributed;
- what earlier events depleted it;
- what reforms followed;
- which projects were deferred;
- whether one region repeatedly receives aid;
- whether members leave or join;
- which unresolved old claims remain open.

This creates stories after the boss fight rather than another combat system.

## Mechanical guardrails

Nothing in these sources validates PTU/Caelo mechanics for:

- insurance premiums;
- claim DCs;
- property valuation;
- Pokémon valuation;
- liability damage;
- business-interruption formulas;
- fraud detection bonuses;
- catastrophe payouts;
- repair bonuses;
- reduced battle damage for insured assets;
- healing or revival through coverage;
- item replacement as a battle effect.

Those remain outside AutoPTU unless a future rules/canon source establishes them.

## Super PTU Online Helper / Caelo state

Super PTU Online Helper was not available as an invocable capability in this run.

The complete primary Caelo corpus was not reliably accessible as an invocable source in this run.

No insurance, risk-pooling, property-loss, liability or claim mechanic is attributed to either source.

## Candidate direction for the systems layer

The proposed systems design should own only:

- risk-transfer institution identity;
- policy/mutual agreement identity and versions;
- insured/covered-interest references without inventing ownership;
- coverage scope;
- exclusions/limits as authored agreement state;
- loss notice;
- claim file;
- evidence references;
- assessment;
- decision;
- reserve/pool state;
- payment commitment/event handoff to Finance;
- recovery-funding handoff;
- dispute/review handoff;
- history across renewals and catastrophes.

It should not own physical damage, Pokémon agency, legal guilt, mechanical money rules, battle damage or recovery construction.