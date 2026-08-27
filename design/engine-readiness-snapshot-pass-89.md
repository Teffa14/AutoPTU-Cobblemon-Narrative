# Engine Readiness Snapshot — Pass 89

Status: implementation evidence snapshot, not canon.
Date: 2026-08-28

## Scope

Supports:
- `design/auctions-consignment-secondary-market-extension.md`;
- `proposals/2026-08-28-auctions-consignment-secondary-market-seeds-89.md`.

Writable repository:
- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence repositories:
- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Internal project review

Before writing Pass 89, the current Narrative tree and full `design/` inventory were inspected. Neighboring systems reviewed directly included:
- Material Culture, Crafting & Economy;
- Finance, Sponsorship, Patronage & Risk;
- Commercial Services & Storefront Continuity;
- Found Property, Custody & Restitution;
- Encounter Implementation Contracts;
- the Pass 88 readiness snapshot;
- the Cobblemon runtime-authority boundary.

The selected gap was secondary exchange of existing persistent objects through consignment, listings and auctions. It was kept narrow so Storefront continues to own ordinary retail, Finance owns money, Material Culture owns exact object identity/provenance and Archives/Found Property/Courier retain their established authority.

## Binding runtime authority

Ouros owns:
- venue/market world state;
- item/lot references and narrative provenance links;
- seller/consignor/bidder/principal world relationships;
- published catalogue claims;
- explicit encounter composition;
- noncombat exchange consequences and handoffs.

AutoPTU owns:
- tactical participants and teams;
- action/target legality;
- tactical positions and movement;
- initiative/action economy;
- HP, statuses, stages and temporary effects;
- damage/healing;
- Moves, Abilities, Items and Trainer Features;
- forced movement, Intercept and reactions;
- tactical AI;
- final battle result.

Minecraft/Cobblemon/Craftics may present or adapt:
- market stalls, counters, display blocks and containers;
- signs/books/catalogue UI;
- Pokémon and NPC models/animations/poses/cries used as world presentation;
- sounds/particles;
- interaction transport;
- networking/synchronization;
- semantic playback of authoritative AutoPTU events;
- reviewed world-state changes authorized by Ouros.

Required direction:

`Ouros market/world state -> explicit encounter composition -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden shortcuts:

`Cobblemon nearby entity/BattleState/controller -> participant selection, battle legality or result`

`Minecraft inventory pickup/trade GUI -> automatic Ouros ownership/provenance truth`

## PTU/Caelo market boundary reviewed

PTU 1.05 leaves starting money and item availability to campaign/GM decisions.

Pass 89 therefore does not create:
- universal market availability for every PTU item;
- price or appraisal formulas;
- auction Skills/DCs;
- bidding initiative;
- rarity multipliers;
- automatic discounts;
- new item mechanics;
- Pokémon sale values;
- mechanical bonuses from collector reputation.

Any exact Skill, Feature, item or money interaction requires governing PTU/Caelo review and eventual authoritative implementation evidence.

## Live revisions inspected

AutoPTU-Java `main`:

`4b620e5429327c5c98a99bb6dc97dce0ba9261ab`

Latest change:
`Apply intercept discovery expiry cleanup authoritatively (#251)`

AutoPTU Python `main`:

`300dac43584bc551c4dc5aacff974f789d8dccb0`

Latest Python change:
`Career: keep Full FX inside raster budget after viewport resize (#195)`

The Python change concerns renderer safety and does not establish a new tactical capability family.

## Java #251 evidence

Commit #251 adds an authoritative application that commits temporary-effect expiry cleanup discovered during Intercept candidate scanning.

The implementation:
- removes expired `no_intercept` snapshots from the attacker;
- removes expired `sentinel_stance` entries from authoritative combatants;
- preserves insertion order, multiplicity and active entries;
- uses the server-owned `BattleRuntimeState` and its current round;
- has direct Java tests and a parity gate.

The class-level contract explicitly states that Minecraft/Cobblemon never performs this cleanup.

This is meaningful progress for the Intercept/reaction pipeline and for authoritative temporary-effect lifecycle behavior. It does not prove the complete movement family, full status lifecycle or general reactions.

## README caution

The current Java README still establishes the same architecture:
- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events.

The broad incomplete checklist still includes:
- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy work;
- full status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- complete Move/Ability/Item/perk/Trainer Feature registries;
- semantic BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Later focused commits are stronger evidence for exact forced-movement/Intercept slices than that broad checklist, but those slices do not establish family-wide completion.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: PARTIAL
  core calculations: VERIFIED
  action economy/initiative: VERIFIED
  full turn/round lifecycle: PARTIAL
  full stateful damage pipeline: PARTIAL
  status lifecycle: PARTIAL
  terrain/weather/hazards/zones/reactions: BLOCKING
  move-specific behavior: PARTIAL
  abilities: PARTIAL
  items: PARTIAL
  Trainer Features/perks: PARTIAL
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

Pass 89 makes no family-level promotion.

## Why complete movement remains PARTIAL

Positive live evidence now includes:
- Shift and Jump legality;
- authoritative Push/Pull forced displacement;
- collision/bounds/occupied-footprint partial stops;
- position mutation;
- Intercept attempt policy;
- Intercept eligibility and Skill-check resolution;
- candidate geometry and attack-line placement;
- reaction movement commitment;
- one melee Intercept + Push 1 composition;
- candidate discovery for Weaponize, prepared Intercept and Sentinel;
- materialization of candidate inputs from server-owned rule content;
- authoritative cleanup of expired discovery-related temporary effects in #251.

Still missing for family-level VERIFIED:
- broad live trigger integration across all relevant attack/action families;
- full competing-reaction ordering/conflict handling;
- broad knockback coverage;
- all forced-movement sources;
- broad Move/Ability/Item/Trainer Feature integration;
- environment-driven displacement interactions;
- complete semantic transcript coverage;
- tactical AI handling;
- Minecraft/Cobblemon playback.

## Why status lifecycle remains PARTIAL

#251 proves one authoritative expiry-cleanup slice for temporary effects used by Intercept discovery.

That is insufficient to establish:
- all persistent and volatile status lifecycles;
- all duration/save checks;
- all start/end/command/action hooks;
- every interaction with Items, Abilities and Trainer Features;
- complete semantic events;
- all cleanup ordering.

## Why terrain/weather/hazards/zones/reactions remains BLOCKING

Intercept work is substantial, but the permanent family includes much more than one reaction path.

Still family-incomplete:
- general reaction registry/lifecycle;
- multiple competing reactions and conflict ordering;
- tactical terrain ownership/state;
- tactical weather controller;
- hazards and zones with lifecycle;
- environment-driven status/damage/movement;
- AI reasoning over those states;
- adapter playback.

Therefore crowd routes, blocked aisles, loose display structures, weather on transfer routes and similar world facts must remain static/visual or pre-resolved in the reduced versions unless exact authoritative mechanics are verified.

## Encounter — Auction Hall Evacuation

Full-version dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING when access changes dynamically;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced implementation profile:
- public attendees and staff evacuate before BattleSpec creation;
- persistent lots are secured outside tactical targeting;
- unsafe/blocked sections become fixed world-state exclusions;
- Ouros selects exact combatants;
- static reviewed battle arena only;
- AutoPTU returns the tactical result;
- Market/Event/Facility systems decide later reopening/custody state.

No battle result awards, transfers or authenticates a lot.

## Encounter — Consignment Transfer Interruption

Full-version dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING when route/environment is tactical;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced implementation profile:
- handlers and significant cargo leave the tactical grid first;
- transfer becomes PAUSED in world state;
- Ouros composes only actual combatants;
- AutoPTU resolves a static legal encounter;
- Courier/Market/Material Culture resume, reroute or stop transfer afterward.

No scripted escort, cargo HP, ownership mutation, automatic theft or route hazard is invented.

## Noncombat concept — Catalogue Provenance Review

This concept is executable without battle capability dependencies when it uses only:
- source/provenance comparison;
- catalogue revisions;
- actor knowledge;
- archives/photography/repair history;
- explicit uncertainty;
- authored venue authority to pause or continue a lot.

If later versions invoke PTU Skills or Features, those exact mechanics require source/runtime review.

## Cobblemon reuse classification for Pass 89

SAFE_REUSE candidates, subject to adapter-level compatibility review:
- blocks/stalls/display surfaces;
- signs/books/lecterns;
- item icons/models where appropriate;
- entities/models/forms/poses/animations/cries as world presentation;
- sounds/particles;
- generic UI/network/sync primitives;
- persistent storage hooks that do not assign narrative meaning.

ADAPTER_REQUIRED:
- catalogue UI bound to Ouros lot IDs;
- world display bound to persistent item identity;
- offer submission bound to authoritative market state;
- closeout projection after Finance/Material Culture state changes;
- semantic battle playback.

BATTLE_AUTHORITY_FORBIDDEN:
- Cobblemon participant/controller/BattleState logic;
- nearby Pokémon/entities deciding combatants;
- Cobblemon HP/status/position deciding AutoPTU state;
- Minecraft inventory movement deciding Ouros ownership/provenance.

## Current unresolved mechanical questions

- Which PTU/Caelo Skills, if any, should govern inspection/appraisal-like scenes?
- Are there governing rules for bargaining or appraisal worth using, or should most scenes remain social/informational world-state interactions?
- Which item classes are fully available in the eventual Java registry?
- When can Items themselves become tactical objects, if ever?
- What is the exact end-to-end Intercept/reaction promotion gate?
- What semantic events will the adapter need for evacuation/withdrawal playback?

## Current unresolved canon questions

- Which Ouros settlements have secondary markets?
- Are auctions recurring institutions, temporary market days or rare specialist events?
- What categories of objects can legitimately be consigned?
- What information appears publicly in a catalogue?
- What privacy exists for sellers/buyers/principals?
- Can institutions deaccession or dispose of objects?
- Are proxy purchasing mandates culturally/institutionally normal?
- What fees, commissions or payment rails exist, if any?
- Which authority can pause a lot on provenance grounds?
- What practices exist around culturally important objects entering private exchange?

All remain unresolved by Pass 89.
