# Engine Readiness Snapshot — Pass 101

Status: IMPLEMENTATION-READINESS EVIDENCE. This snapshot does not create PTU rules or Ouros canon.
Date: 2026-08-28

## Scope

Pass 101 adds proposed residential/household continuity: stable residences, explicit resident links, household groups, habitability, occupancy events, temporary/permanent relocation, displacement, return review, vacancy, abandoned-house provenance and adaptive reuse.

Narrative baseline before Pass 101 writes: `545dc15b075b1ea2b018aa86355d2e25dff7d934`.

Read-only evidence inspected:
- complete recursive Narrative repository inventory at the baseline tree;
- README architecture/source-priority guidance;
- `observation-settlement-time-layer.md`;
- `commercial-services-storefront-continuity-extension.md`;
- `finance-sponsorship-risk-layer.md`;
- Pass 100 readiness snapshot;
- live AutoPTU-Java head and README;
- live AutoPTU head;
- PTU/Caelo boundaries already captured in the repository;
- new public Pokémon/tabletop research in Pass 101.

## Live engine evidence

AutoPTU-Java advanced to `df3833964e1ec7596791cf6f07dec08122598f68`, PR #257, “Preserve Python intercept attempt mutation ordering”.

The live commit records:
- composition of Intercept check and attempt mutations in oracle order;
- parity coverage for failed Intercept attempt mutation;
- parity gating of attempt mutation ordering;
- clarification that Intercept resources mutate before the success branch.

This is meaningful additional evidence for one Intercept orchestration path and for preserving Python state-mutation order.

It does not establish family-wide completion of:
- competing reactions;
- generalized reaction trigger ordering;
- broad knockback;
- every forced-movement source;
- environmental displacement;
- complete Move/Ability/Item/Trainer Feature integrations;
- objective-aware tactical AI;
- semantic Minecraft playback.

The current AutoPTU-Java README still lists these major unfinished areas:
- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- Move/Ability/Item/perk/Trainer Feature hook registries;
- full semantic event/transcript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

AutoPTU Python head inspected: `59836e29997a30bf2419c46d2e40be9f5449c4a7`, merging Career preservation of casual auth when browser storage is blocked. This is Career/client stability work and does not add tactical battle-family evidence.

No permanent capability category is promoted in Pass 101.

## PTU/Caelo residential boundary

No inspected governing evidence establishes universal PTU/Caelo rules for property ownership, leases, household membership, eviction, residential capacity, building-code checks, home-based bonuses or domestic work.

Pass 100 already confirmed the relevant recovery boundary: PTU Rest/Extended Rest is explicit mechanical state and cannot be inferred merely from being in a bedroom/home or from a Minecraft sleeping animation.

Residential continuity therefore remains nonbattle world state unless an explicit encounter is composed.

## Permanent capability map

### VERIFIED

`targeting/footprints/range/LoS`

Verified for reviewed static battlefields. A house or lane still needs explicit arena conversion.

`base movement legality`

Verified for ordinary static arena movement. It does not establish evacuation or protected-route objectives.

`core calculations`

Verified primitives remain available. They do not create structural, domestic or property semantics.

`action economy/initiative`

Verified typed action budget/order remains available.

`AI legal-action infrastructure`

Verified legal-action enumeration remains available. It does not decide who is a resident, who should withdraw, which rooms are private or which route should be protected.

### PARTIAL

`complete movement including push/pull/knockback/interception/forced movement`

PARTIAL. Java #257 adds stronger evidence for Intercept attempt mutation ordering, on top of prior push/pull/intercept slices. Broad reactions, broad knockback and all forced movement remain incomplete.

`full turn/round lifecycle`

PARTIAL. Reduced residential encounters need no new lifecycle behavior, while simultaneous evacuation/reaction scenarios still depend on broader integration.

`full stateful damage pipeline`

PARTIAL. Pass 101 introduces no residential damage rules. Family-wide completion remains unverified.

`status lifecycle`

PARTIAL. A frightened, displaced or sleeping resident cannot be assigned a PTU status from narrative language alone.

`move-specific behavior`

PARTIAL. Implemented Moves cannot be generalized into rescue, forced entry, structural repair or domestic utility.

`abilities`

PARTIAL. No Ability implies household role, structural safety, rescue authority or residential competence without exact rules.

`items`

PARTIAL. Keys, furniture, repair props and moving boxes are narrative/world objects unless governing item rules say otherwise.

`Trainer Features/perks`

PARTIAL. No broad household, rescue, construction or relocation Feature coverage is established.

### BLOCKING

`terrain/weather/hazards/zones/reactions`

BLOCKING for mechanically rich occupied-house evacuation, fragile structures, fire/flood zones, dynamic worksite hazards or generalized reaction scenes. Reduced forms keep those mechanics outside BattleSpec.

`AI tactical policy`

BLOCKING. Legal-action generation does not establish behavior for withdrawal, route protection, territorial escape, avoiding nonparticipants or keeping combat out of private rooms.

`Minecraft/Cobblemon/Craftics adapter/playback support`

BLOCKING. Minecraft/Cobblemon can represent houses, actors and Pokémon, but no adapter currently makes residence state, occupancy, household links or PTU battle state authoritative across that presentation.

## Encounter readiness — Residential Lane Withdrawal

Full intended form wants multiple safe exits, withdrawal/protection objectives, Intercept/forced movement, reactions, narrow reviewed terrain, objective-aware AI and semantic playback.

Current profile: REDUCED.

Safe reduced form:
- Crisis/Residential evacuates all nonparticipants before BattleSpec creation;
- private interiors and household goods remain outside the tactical contract;
- Ouros selects combatants explicitly;
- AutoPTU receives a static lane/courtyard;
- no dynamic evacuation objective is simulated;
- battle secures only the immediate area;
- return/occupancy/habitability remain Residential/Crisis decisions.

## Encounter readiness — Repair-Site Perimeter Conflict

Full intended form may require worker withdrawal, protected access routes, hazards/zones, reactions and objective-aware AI.

Current profile: REDUCED.

Safe reduced form:
- Maintenance suspends work before combat;
- workers and equipment leave;
- AutoPTU receives a static safe perimeter;
- battle cannot complete repair, inspection, verification or return authorization.

## Encounter readiness — Vacant House Boundary

Full intended form may require territorial/escape policy, reactions, reviewed difficult terrain and possibly fragile-space hazards.

Current profile: REDUCED.

Safe reduced form:
- Residential/Conservation first determines the observed nonbattle situation;
- explicit combatants are selected by Ouros;
- use a reviewed exterior or cleared interior;
- no collapse, forced-entry, property, capture, custody or reuse rule is inferred;
- battle result does not establish abandonment or eviction.

## Noncombat readiness

Residential continuity is usable immediately for:
- permanent and temporary residence links;
- household splits across locations;
- relocation histories;
- displacement without losing normal-home identity;
- return review after repairs/crises;
- vacancy and abandonment provenance;
- adaptive reuse history;
- neighborhood recovery callbacks;
- privacy-aware address/occupancy investigations;
- recurring neighbors and resident Pokémon observations;
- mismatched address, occupancy and public records.

## Cobblemon/Minecraft consequence

Binding architecture remains:

`Ouros encounter/world state -> explicit combatant selection -> AutoPTU BattleSpec -> AutoPTU authoritative state/result -> adapter -> Minecraft/Cobblemon presentation`

Safe presentation candidates:
- houses/apartments/interiors;
- doors, furniture, decorative beds and storage;
- repair props and moving boxes;
- signs/barriers based on authoritative access state;
- recurring actor/Pokémon models, forms, poses, animations and cries;
- neighborhood visuals;
- UI, networking, world coordinates, entity tracking and persistence hooks.

Adapter-required:
- stable residence/household/actor/Pokémon identity bindings;
- authoritative access projection;
- reviewed domestic-space tactical conversion;
- semantic playback;
- state persistence across chunk unload/reload.

Minecraft/Cobblemon must never decide:
- occupancy from physical presence;
- household membership from proximity;
- ownership from a bed, chest, key or building;
- Trainer/Pokémon ownership from cohabitation;
- vacancy from unloaded entities;
- abandonment from an empty structure;
- PTU Rest from sleeping animation;
- combatants from everyone inside a residence;
- eviction, return or relocation from KO result;
- structural safety from block appearance;
- battle result.

## Readiness conclusion

VERIFIED: targeting/footprints/range/LoS; base movement legality; core calculations; action economy/initiative; AI legal-action infrastructure.

PARTIAL: complete movement including push/pull/knockback/interception/forced movement; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; move-specific behavior; abilities; items; Trainer Features/perks.

BLOCKING: terrain/weather/hazards/zones/reactions; AI tactical policy; Minecraft/Cobblemon/Craftics adapter/playback support.

## Unresolved canon questions

- Which residence types exist by Ouros region and settlement?
- What terms distinguish household, resident, guest, tenant, owner or caretaker, if those concepts exist locally?
- Which institutions, if any, maintain addresses or occupancy records?
- What privacy expectations apply to residential information?
- How are temporary displacement, community hosting and permanent relocation distinguished culturally/institutionally?
- Which authority determines habitability/re-entry after different incidents?
- How are abandoned residences treated before reuse?
- Can independent Pokémon hold recognized residence links, and under what canon rules?
- Which Pokémon are explicitly established as household companions without assuming Trainer ownership?

## Unresolved mechanical questions

- exact nonbattle bridge, if any, between residence time and PTU Rest/Extended Rest;
- rescue/carry mechanics during occupied-building incidents;
- generic forced-entry or door/structure interactions;
- structural HP/collapse rules, if Ouros ever adopts them;
- fall/fire/flood/smoke hazards inside residences;
- exact terrain conversion for stairs, furniture and narrow interiors;
- whether any PTU/Caelo Skill/Feature has explicit building inspection, repair or evacuation use relevant to these scenes;
- adapter persistence for stable residence and household links.

No answer is invented by this snapshot.