# Engine Readiness Snapshot — Pass 152

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only inputs.
Date: 2026-08-24

## Live revisions inspected

AutoPTU-Java `main`: `ab520743d8d99f06fa28fd4d6fa06a0c4ecd3fee` — `Port Shell Shield pre-damage reaction (#180)`.

Immediately preceding Java work includes authoritative PRE-damage follow-up Move execution through runtime state (`b6701fcc`) and a parity-backed policy for those follow-ups (`ab29df99`). These are narrow reaction/move-execution slices.

AutoPTU Python `main`: `03321a2eba42437180fddf5c4b2570c50ba429a6` — Career sponsor-history renewal-market behavior. Recent Python work remains Career/presentation/persistence oriented and does not promote battle capability families.

Java continues to state that Python AutoPTU is authoritative while the port is incomplete. The live README still lists core battle state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, transcript parity, AI scoring/policy and Minecraft/Cobblemon adapter work as incomplete.

## Permanent capability map

| Capability family | Pass 152 status | Evidence boundary |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README marks range, areas, footprints, anchors and LoS implemented. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers and fit are documented as ported. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Narrow reaction movement/push primitives exist, but forced movement remains explicitly incomplete. |
| core calculations | VERIFIED | DB/type/stage/accuracy/weather/crit/Burn/modifier primitives are documented as implemented. |
| action economy / initiative | VERIFIED | Typed action budgets and deterministic initiative/order variants are implemented. |
| full turn / round lifecycle | PARTIAL | Multiple lifecycle slices exist; complete battle-state/transcript parity does not. |
| full stateful damage pipeline | PARTIAL | Normal, delayed, multi-target and reaction-related slices exist; full damage remains incomplete. |
| status lifecycle | PARTIAL | Selected application/prevention/stacking/removal contracts exist; full status controller remains incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | More PRE-damage reaction contracts exist, but the family is explicitly incomplete. Use only exact verified contracts. |
| move-specific behavior | PARTIAL | Multiple representative Move paths are ported; catalog parity is incomplete. |
| abilities | PARTIAL | Shell Shield and other selected Abilities have parity evidence; full registry parity does not. |
| items | PARTIAL | Selected item behavior exists; complete item registry/hook parity does not. |
| Trainer Features / perks | PARTIAL | Generic gates/effects and selected concrete interactions exist; catalog parity is incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal `BattleChoice` action-space is documented as implemented. |
| AI tactical policy | BLOCKING | Java README still lists scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback | BLOCKING | Java remains a standalone rules library; adapter integration is pending. |

## New Java evidence — do not promote reactions

`ab520743` adds the exact Shell Shield PRE-damage reaction contract. Runtime state owns readiness, the optional decision and the state mutation. Under its tested contract Shell Shield can add Withdrawn and raise Defense without cancelling the incoming hit.

`b6701fcc` routes supported PRE-damage follow-up Moves through the authoritative runtime rather than allowing an adapter to fabricate their execution.

These are useful architecture milestones. They do not prove generic reaction dispatch, all defensive reactions, complete forced movement, hazards, zones or tactical AI.

For botanical encounters they are relevant only if an actual combatant uses one of those exact supported rules. They do not create glasshouse hazards, evacuation movement or plant-protection mechanics.

## Pass 152 encounter dependency mapping

### Glasshouse Utility Failure — FULL

Required:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement — BLOCKING for moving staff, withdrawal lanes, interception or forced displacement;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL only if exact supported statuses are invoked;
- terrain/weather/hazards/zones/reactions — BLOCKING if heat, water, broken glass, equipment or protected beds have tactical effects;
- move-specific behavior — PARTIAL as required by the selected Moves;
- abilities — PARTIAL;
- items — PARTIAL if protective or technical equipment has battle effects;
- Trainer Features/perks — PARTIAL if invoked;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `WITHDRAW`, `PROTECT_STAFF`, `CLEAR_ROUTE`, `REACH_EXIT`;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED: Technology enters safe mode and staff relocates vulnerable accessions before battle. Freeze one static safe arena. Plants and greenhouse systems have no mechanical effects. Collection outcome is resolved afterward from authoritative world state.

### Seed Bank Transfer Chokepoint — FULL

Required:

- targeting/LoS — VERIFIED for ordinary combat;
- base movement — VERIFIED;
- complete movement — BLOCKING if a custodian/cargo objective physically traverses threatened space;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- lifecycle/damage/status/move/ability/item/Feature families — PARTIAL as used by combatants;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for `PROTECT_CUSTODIAN`, `CLEAR_ROUTE`, `WITHDRAW`;
- adapter/playback — BLOCKING;
- items — PARTIAL and exact validation required if the seed container itself becomes a mechanical item/object.

REDUCED: keep the seed lot under world-state custody outside the grid. Resolve a conventional static encounter, then complete transfer through Supply Chains/Postal. Battle does not alter viability or provenance.

### Storm-Damaged Conservation Nursery — FULL

Required:

- complete movement — BLOCKING for staff/wildlife withdrawal and crossing;
- AI tactical policy — BLOCKING for `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT_STAFF` and non-hostile movement objectives;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING if stormwater, debris, glass or unstable structures become tactical mechanics;
- remaining standard battle categories retain VERIFIED/PARTIAL status above.

REDUCED: resolve storm state, assessment and noncombatant movement in overworld. Freeze a stable adjacent arena only if an independent confrontation remains.

### Accession Provenance Review

No battle family is inherently required.

A valid outcome may remain `MULTIPLE_PLAUSIBLE` or `UNRESOLVED`.

## Pass 152 world-state blockers

These belong outside AutoPTU-Java:

- botanical institution identity;
- living accession identity;
- accession provenance graph;
- living specimen history;
- acquisition/collection events;
- propagation history;
- seed-bank lot state;
- viability observation history;
- duplicate holding network;
- collection-program strategy/history;
- horticultural care state;
- living-collection risk register;
- public display label revisions;
- Taxonomy -> accession determination handoff;
- Biosecurity -> material transfer authorization handoff;
- Conservation/Flora -> restoration-source and establishment handoff;
- Museums/Archives -> preserved voucher/record handoff;
- Supply Chains/Postal -> transferred material custody handoff;
- authoritative collection state -> Minecraft presentation;
- collection state -> frozen battle snapshot.

## Mechanical non-inferences

Pass 152 does not authorize:

- Grassy Terrain from botanical beds;
- plant-derived cover or Rough Terrain;
- healing zones from Florges lore;
- environmental Flower Veil;
- Comfey-generated healing items;
- Honey production from flower abundance;
- Eldegoss-driven accession propagation;
- Seed Sower as an overworld ecology write;
- viability as guaranteed germination;
- germination as successful restoration;
- greenhouse climate control as battle Weather;
- glasshouse heat/cold/water damage;
- plant HP;
- Naturewalk from being inside a garden;
- Berry yield changes;
- pollen Status effects;
- rare-spawn changes based on collection contents;
- block placement, bone meal or Minecraft growth as propagation;
- block destruction as accession death;
- narrow PRE-damage reaction support as generic reactions or complete movement.

## PTU / project evidence

AutoPTU contains PTU-derived data for mechanics such as Honey Gather and Flower Veil. Their presence is evidence that those concepts have exact mechanical definitions, not permission to generalize them into institutional horticulture.

The live Java port still treats whole ability/item/Feature catalogs as incomplete. A botanical encounter using a specific Ability or Item requires current evidence for that exact mechanic.

No reliable primary Caelo source defining botanical-garden accessioning, seed banking, horticultural care, wild-collection procedures or ex-situ conservation was recovered in this run.

Super PTU Online Helper was not exposed as an invocable capability. No output is invented or attributed to it.

## Open mechanical/canon questions

- Which Ouros institutions maintain living collections or seed banks before campaign start?
- What technology exists for greenhouse control and long-term seed storage?
- Does Caelo define relevant Researcher, Pokémon Education, Survival, Naturewalk, Berry, Honey Gather, horticultural or collection mechanics?
- Which exact plant taxa are established Ouros canon rather than proposals?
- Which wild-origin accessions may reveal sensitive locations?
- Who may collect, propagate, transfer or deaccession material?
- Which Pokémon have authored voluntary roles in horticulture or research?
- How should restoration material hand off from an institution to a wild population without creating spawn exploits?
- How much accession-level detail should ordinary players see versus curators/researchers?
- When should a botanical incident enter AutoPTU at all rather than remain a world-state problem?
