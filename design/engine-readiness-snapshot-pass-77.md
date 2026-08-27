# Engine Readiness Snapshot — Pass 77

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/wreck-sites-salvage-recovery-preservation-extension.md` and the mechanically rich encounter candidates in Pass 77.

It also applies `design/cobblemon-runtime-authority-boundary.md`: Minecraft/Cobblemon should be reused aggressively for overworld embodiment and presentation, while Ouros/AutoPTU own participant selection, tactical state, legality and outcomes.

## Repositories inspected

Writable:

- `Teffa14/AutoPTU-Cobblemon-Narrative`

Read-only evidence:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No files were modified in the engine repositories.

## Inspected revisions

AutoPTU-Java `main`:

`c3b94bf4d4d5d0c3939bed027d3f9556b7c300e9`

Latest inspected change:

`Wire held-item START profiles into lifecycle (#238)`

AutoPTU Python `main`:

`11c4aea350193d2ed0940ec5a8ada09e44b6d291`

Latest inspected change:

`Career: train the full active squad each season`

The Python change is progression/Career behavior and does not establish a new tactical capability family relevant to wreck-site encounters.

## Live Java evidence

The current Java README explicitly describes the intended architecture:

- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events;
- the Java project is not yet the Minecraft mod;
- the Python implementation remains the oracle while the port is incomplete.

The README currently reports implemented slices for:

- targeting, areas, footprints, anchors and LoS;
- Shift and Jump movement legality;
- Damage Base and type-effectiveness tables;
- calculation primitives including stages, Accuracy, weather DB arithmetic and rounding points;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow/action budget;
- deterministic initiative;
- legal autobattler action-space generation.

It still explicitly lists these unfinished families:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- StatusController, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

Recent Java work strengthens held-item START lifecycle ownership, parsing, rule-catalog boundaries and Magic Room suppression. This remains evidence for slices of Items/lifecycle, not full-family completion.

## Permanent capability map

```yaml
capabilities:
  targeting/footprints/range/LoS: VERIFIED
  base movement legality: VERIFIED
  complete movement including push/pull/knockback/interception/forced movement: BLOCKING
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

Pass 77 does not promote any category.

## Why wreck-site content does not change the map

Wreck exploration introduces attractive mechanics such as:

- underwater movement;
- currents;
- collapse;
- flooding;
- debris;
- unstable decks;
- narrow compartments;
- visibility changes;
- withdrawal/clear-route objectives;
- territorial wild Pokémon;
- protected recovery zones.

Minecraft can depict all of those visually. That does not prove the corresponding PTU mechanic or Java runtime path.

Therefore Pass 77 treats environmental state and tactical effects separately.

## Underwater/water movement caution

`base movement legality` is VERIFIED for the ported Overland/Swim/Sky Shift and Jump slices.

That does not prove every rule required for a full underwater encounter.

Before using underwater tactical movement authoritatively, the implementation still needs exact source/runtime evidence for any additional behavior the encounter requires, including:

- depth/pressure effects;
- breath/drowning/suffocation;
- underwater LoS modifiers;
- current-driven displacement;
- water-specific attack restrictions;
- surface transition timing;
- Trainer movement underwater;
- equipment effects;
- environment-specific objective logic.

If none of those extra rules are used, a future encounter may rely only on already verified movement slices plus other required families. Pass 77 does not assume that simplification automatically applies.

## Terrain/weather/hazards/zones/reactions remains BLOCKING

The Java README includes a `weather DB` calculation primitive. That is not a battlefield weather controller.

The family remains BLOCKING because the engine still explicitly lists terrain, hazards and reactions as unfinished, and no complete environment-state runtime path is proven.

Consequences for Pass 77:

- visible water is not a tactical hazard by itself;
- corrosion does not apply damage;
- a broken floor does not create falling rules;
- debris does not apply a movement penalty unless the reviewed static map legally blocks movement;
- storm conditions can gate overworld access without becoming tactical Weather;
- currents cannot push combatants until forced movement is verified;
- underwater visibility cannot alter Accuracy/LoS without exact rules/runtime evidence.

## Complete movement remains BLOCKING

Shift/Jump legality does not prove:

- push;
- pull;
- knockback;
- interception;
- current-driven displacement;
- collision/landing after forced movement;
- forced relocation through narrow wreck geometry.

Any rich wreck encounter using those remains blocked on this permanent family.

## AI tactical policy remains BLOCKING

AI legal-action infrastructure is VERIFIED, meaning Java can generate/filter legal choices for the currently ported action space.

That does not prove an opponent can reason about:

- withdrawal;
- territorial defense;
- protecting a nest/zone;
- clearing a route;
- denying access;
- escaping a flooded compartment;
- preferring non-KO outcomes;
- preserving fragile scenery.

Those depend on AI tactical policy and objective state, which remain blocking.

## Adapter/playback remains BLOCKING

Pass 77 follows this mandatory direction:

`Ouros world state -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon presentation`

Forbidden direction:

`Cobblemon Battle/BattleState/participant/controller -> authoritative Ouros/AutoPTU fact`

Cobblemon may safely or desirably provide:

- Pokémon models/textures;
- aquatic locomotion animation;
- cries and particles;
- overworld entities;
- water and structure rendering;
- UI/networking;
- interaction hooks;
- persistent site props;
- environmental presentation.

Adapter tests are still required before production battle playback can be marked ready.

The adapter must prove at least:

- Ouros chooses participants explicitly;
- nearby Cobblemon entities do not auto-join;
- chunk unload/despawn does not remove authoritative combatants;
- AutoPTU state survives independent of entity presentation;
- HP/status/position/initiative are projected from AutoPTU only;
- world props recovered after battle change only through reviewed world-state writes;
- Cobblemon battle code is never consulted as source of truth;
- client retry/reconnect does not duplicate outcomes.

No complete adapter contract is verified yet.

## Encounter readiness — Flooded Compartment Withdrawal

Full desired version:

- survey team withdrawal;
- narrow wreck geometry;
- potential water/environment effects;
- territorial wild behavior;
- CLEAR_ROUTE/WITHDRAW objective logic;
- possible forced movement/interception;
- exact world-to-battle playback.

Dependency status:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if used;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL when relevant;
- terrain/weather/hazards/zones/reactions — BLOCKING for active flooded-environment effects;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version available now in design terms:

- withdraw survey team before tactical resolution;
- use a reviewed static ordinary arena;
- keep flooding/environment neutral tactically;
- run only supported combat behavior;
- resume survey/access review after authoritative result.

## Encounter readiness — Selective Recovery Perimeter

Full desired version:

- protected work zone;
- moving technicians/noncombatants;
- route clearing;
- fragile zones;
- possible interception/forced movement;
- territorial/withdrawal AI;
- exact recovery/playback synchronization.

Primary blockers:

- complete movement including push/pull/knockback/interception/forced movement when used;
- terrain/weather/hazards/zones/reactions when fragile/environmental rules are active;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Lifecycle/damage/status/move/ability/item/Feature families remain PARTIAL as individually required.

Reduced version:

Pause recovery and remove technicians/object from tactical state. Resolve a static battle nearby. Perform the actual recovery afterward as an authoritative world interaction. Append object provenance and custody separately.

## Encounter readiness — Exposed Deck Access Window

Full desired version may include active weather/access change during tactical play.

If so, terrain/weather/hazards/zones/reactions and adapter/playback are blocking, with complete movement and tactical AI also blocking when displacement/retreat matters.

Reduced version:

Use the access window only before battle as overworld state. Freeze a static reviewed arena once tactical resolution starts. Apply later world-state consequences after the battle.

## Noncombat content already implementable conceptually

Pass 77 can advance without new tactical families through:

- wreck-site identity;
- zone maps;
- survey records;
- structural-condition observations;
- ecological occupation observations;
- historical claims;
- object context records;
- intervention proposals;
- selective-recovery plans;
- in-place preservation decisions;
- repeated monitoring;
- provenance append on recovery;
- archive/collection handoffs;
- found-property/case handoffs;
- conservation handoffs;
- maintenance/restoration handoffs;
- public-memory callbacks.

These need persistent world-state implementation and UI eventually, but not new combat mechanics.

## PTU/Caelo mechanical questions still unresolved

Pass 77 does not answer:

- whether or how PTU/Caelo models fully submerged Trainer combat;
- any breath/drowning/suffocation rules;
- pressure/depth rules;
- exact underwater visibility rules;
- current/flow rules;
- collapse/debris hazards;
- action costs for technical recovery;
- legal uses of diving/recovery equipment;
- exact Pokémon movement/carrying capabilities for site work;
- Trainer Features that might interact with survey, diving or technical recovery.

Those must be extracted from the supplied project source set before a mechanic becomes authoritative.

## Canon questions still unresolved

- which wrecks exist in Ouros;
- who formerly operated them;
- what historical events created them;
- who surveys them;
- which are protected;
- how ownership/custody of former cargo is handled;
- whether formal salvage institutions exist;
- which recovery technologies exist;
- what credentials are required;
- which Pokémon use particular sites;
- which wrecks can become public sites or be restored.

## Read-only conclusion

AutoPTU-Java and AutoPTU were inspected only.

Java still shows meaningful incremental progress in lifecycle/items, but no permanent capability category changes classification in Pass 77.

Python's latest full-active-squad Career training work does not change tactical readiness.

The rich wreck encounters remain design-valid because reduced versions preserve the same narrative premises while avoiding unsupported rules and keeping Minecraft/Cobblemon downstream from AutoPTU authority.