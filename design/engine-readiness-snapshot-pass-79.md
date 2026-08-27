# Engine Readiness Snapshot — Pass 79

Status: implementation evidence snapshot, not canon.

Date: 2026-08-27

## Scope

This snapshot supports `design/wildlife-monitoring-tagging-telemetry-extension.md` and the mechanically rich Pass 79 candidates.

The narrative repository is the only writable destination for this pass.

Read-only evidence repositories:

- `Teffa14/AutoPTU-Java`
- `Teffa14/AutoPTU`

No engine repository was modified.

## Authority boundary

The binding project architecture remains:

- Ouros owns persistent world facts, monitoring subjects, research records and explicit encounter composition;
- AutoPTU owns combatants once instantiated, tactical legality, tactical state and battle resolution;
- Minecraft/Cobblemon provides overworld entities, visual embodiment, interaction, networking and playback;
- Cobblemon battle-state/participant/controller logic never becomes authoritative for Ouros combat.

Required tactical flow:

`Ouros world/monitoring state -> explicit encounter decision -> AutoPTU BattleSpec/state/result -> adapter -> Minecraft/Cobblemon projection`

A monitored Pokémon does not become a combatant because:

- its Cobblemon entity is loaded;
- it is near the player;
- a telemetry device reports it;
- it appears in a camera record;
- it belongs to a monitored collective;
- Cobblemon’s own battle code would include it.

Ouros explicitly selects encounter participants. AutoPTU then owns the tactical facts.

## Current revisions inspected

AutoPTU-Java `main`:

`a2a2b7fc040bacd0242de615b774d63890952225`

Latest inspected commit:

`Freeze held-item START slot ordering (#239)`

Recent Java sequence relevant to readiness also includes:

- server-owned held-item rule catalog boundary;
- held-item START rule-profile extraction with Python parity;
- held-item START profile lifecycle wiring;
- Magic Room suppression for that hook;
- deterministic START slot-order ownership and parity.

AutoPTU Python `main`:

`28eb7429135e8748f1e495cbaecc7f969da360e4`

Latest inspected merge:

`Career: show player progression in battle trainer strip`

The Python work after Pass 78 is Career UI/presentation. It does not establish a new tactical capability family.

## Current Java architecture evidence

The live Java README continues to state:

- AutoPTU-Java is a clean Java battle-core port, not a Minecraft mod;
- Python AutoPTU remains the oracle while parity is incomplete;
- AutoPTU-Java decides legal actions and battle results;
- Minecraft/Cobblemon/Craftics adapt world state and render resulting events.

The README currently marks these broad slices as implemented:

- targeting, areas, footprints, anchors and LoS;
- Shift movement legality with Overland/Swim/Sky and reviewed costs/blockers;
- Jump movement legality;
- Damage Base/type-effectiveness tables;
- calculation primitives;
- invariant d20 accuracy resolution;
- combat-stat resolution;
- typed turn flow/action budget;
- deterministic initiative/order variants;
- deterministic legal autobattler action-space generation.

The README still explicitly marks these as unfinished:

- core combatant/grid battle state;
- full damage resolution and remaining stateful accuracy modifiers;
- status controller, terrain, hazards, forced movement and reactions;
- complete Move/Ability/Item/perk/Trainer Feature hook registries;
- semantic battle-event emission and full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

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

Pass 79 makes no category promotion.

## Why held-item progress does not promote Items

The current Java head strengthens a real server-owned held-item START path:

- rules can be represented in a catalog boundary;
- START profiles can be extracted/parity-tested;
- profiles can be wired into the lifecycle;
- Magic Room suppression exists for that path;
- slot order is deterministic.

This is meaningful progress.

The Item family remains PARTIAL because the live README still does not establish the complete item registry, full behavior coverage, all lifecycle phases, all interactions or end-to-end BattleTranscript parity.

A research tracking device introduced by Pass 79 is also a world/material item unless PTU/Caelo explicitly defines it as a tactical Item. It must never receive battle behavior merely because held-item infrastructure exists.

## Monitoring state does not require battle capability

Most Pass 79 gameplay can execute entirely as overworld/world-state systems:

- create or review a monitoring subject;
- record a natural visual identifier;
- install/maintain a receiver station;
- begin/end a deployment record;
- record a detection;
- review a data gap;
- compare re-sightings;
- recover a detached device;
- revise a route hypothesis;
- publish an approximate movement summary;
- create a Conservation or Science handoff.

None of these actions prove or require a tactical capability family.

This lets the narrative/world simulation advance while AutoPTU-Java and the Minecraft battle adapter continue their parity work.

## PTU tracking versus telemetry world state

PTU publicly documents Survival as a wilderness scouting/tracking Skill.

Pass 79 does not replace that rule with a custom subsystem.

The monitoring layer can store device detections and observations as world evidence. Any gameplay that converts those facts into:

- a Skill check;
- a DC;
- a mechanical bonus;
- guaranteed discovery;
- Trainer Feature interaction;
- Pokémon-assisted tracking benefit

must be reviewed against the project’s governing PTU/Caelo source set and current AutoPTU implementation.

No “Telemetry” skill or research bonus is added by this pass.

## Cobblemon reuse profile

SAFE_REUSE candidates for Pass 79 include:

- wild Pokémon overworld entities;
- species/forms/models/textures;
- animations, poses and cries;
- safe observed world coordinates;
- vanilla/Cobblemon entity interaction hooks;
- blocks/items/entities for monitoring-station presentation;
- particles and sounds;
- UI surfaces;
- networking/client synchronization;
- persistence hooks;
- spawn/ecology presentation when directed by the owning Ouros ecology state;
- visual cosmetic markers when technically reviewed.

ADAPTER_REQUIRED:

- mapping an observed Cobblemon entity to an Ouros persistent Pokémon ID;
- protecting identity continuity across load/despawn/reload behavior;
- projecting a reviewed research-device cosmetic state;
- converting a player interaction into an Ouros observation/deployment action;
- creating an AutoPTU BattleSpec when Ouros decides a monitored encounter becomes tactical;
- playback of AutoPTU battle events into Cobblemon entities.

BATTLE_AUTHORITY_FORBIDDEN:

- Cobblemon choosing combatants;
- Cobblemon participant/side/controller authority;
- Cobblemon HP/status as Ouros tactical truth;
- Cobblemon initiative/current turn;
- Cobblemon move legality or target legality;
- Cobblemon tactical positions;
- Cobblemon win/loss/capture resolution;
- changing Ouros research identity because Cobblemon battle code spawned/despawned a participant.

## Persistent identity warning

A Cobblemon entity UUID or runtime entity reference is useful implementation provenance while an entity exists.

It is insufficient as the sole durable wildlife identity contract.

Pass 79 needs an adapter-owned identity mapping because:

- an Ouros Pokémon may remain narratively persistent while unloaded;
- the same individual may be observed months later;
- a device deployment can outlive one entity-loading session;
- a world entity can disappear without the Pokémon becoming dead or absent canonically;
- multiple observation sources can support identity independently of the current entity instance.

This is an implementation requirement, not a new tactical rule.

## Encounter readiness — Receiver Ridge Withdrawal

Intended full version:

- a field team is initially present at a receiver site;
- noncombatants withdraw toward explicit exits;
- exact battle participants are chosen by Ouros;
- territorial wild opponents may prefer denial/withdrawal behaviors;
- narrow terrain can matter;
- selected Moves may create forced movement/interception interactions;
- active weather/environment may matter if explicitly supported;
- AI reasons about WITHDRAW/CLEAR_ROUTE rather than pure KO;
- Minecraft/Cobblemon renders AutoPTU-owned state.

Dependency status:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if selected;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if active tactical environment is selected;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:

- field researchers leave the tactical space first through Ouros world state;
- the receiver station remains outside targeting;
- Ouros explicitly chooses the Pokémon/Trainer combatants;
- AutoPTU receives a static legal arena and standard objective compatible with current verified slices;
- no active ridge hazard/weather/forced movement/object protection is scripted in Minecraft;
- after authoritative battle resolution, Ouros updates receiver access and research state separately.

The reduced version preserves the premise: secure access to a research site without pretending that the current engine supports a live escort/withdrawal objective.

## Encounter readiness — Tag Recovery at the Waterline

Intended full version:

- a detached monitoring device exists as a persistent world object;
- the original subject is not assumed present;
- recovery can occur amid wild territorial behavior;
- shore/water movement and environment can matter when supported;
- AI can value territorial withdrawal/denial;
- the device remains outside combatant HP/status logic;
- AutoPTU outcome and world-object recovery are synchronized through the adapter.

Dependency status:

If implemented as a dynamic recovery objective, the full version depends on:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED for current reviewed movement slices;
- complete movement — BLOCKING when forced displacement/interception is relevant;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full stateful damage — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING for active shoreline/weather state;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:

Recover the device as an overworld action before or after a conventional static battle. Do not make the tag targetable, destructible or a battle Item. Water remains reviewed static geometry unless exact movement capability applies. Recovery updates custody/deployment evidence after the action; it does not locate the monitored subject.

## Quiet Re-sighting readiness

The intended primary version is noncombat.

Required systems are narrative/world-state:

- Observation;
- Photography/visual evidence where used;
- Science;
- Pokémon persistent identity;
- Pass 79 identity assessment;
- actor knowledge;
- time/location state.

No battle capability category is required unless a separate combat event begins.

If battle begins, Ouros must author that BattleSpec separately. The monitored/re-sighted Pokémon does not become a participant merely because it was the research subject.

## No telemetry-powered tactical knowledge

Research data cannot silently improve combat AI.

A recurring rival, NPC or autonomous opponent may use only information permitted by the project’s actor-knowledge/scouting rules.

A scientific database containing:

- movement tracks;
- home-range estimates;
- behavior observations;
- device measurements

must not grant tactical knowledge of:

- Moves;
- Abilities;
- held Items;
- HP/status;
- tactical position;
- action choice;
- private Trainer plan

unless an independent governing rule and evidence permits that knowledge.

## No signal-to-battle shortcut

A receiver detection can create a search area or research lead.

It cannot force-spawn the monitored Pokémon at the recorded coordinate for battle convenience.

A proper overworld path can produce:

- no observation;
- trace evidence;
- receiver malfunction;
- another Pokémon;
- a collective subgroup;
- the intended individual;
- a changed habitat;
- a new research question.

Only after Ouros resolves the world facts does an AutoPTU encounter exist.

## Unresolved mechanical questions

- Which PTU/Caelo rules govern direct handling or restraint if a proposed tagging method requires contact?
- Does the chosen source set define any equipment suitable for wildlife tracking?
- Can any existing Item/Feature/Move legally support re-identification or field tracking, and is that slice implemented in AutoPTU?
- How should actor Survival tracking interact with device evidence without inventing bonuses?
- What exact Cobblemon persistence hooks can safely map overworld entities to durable Ouros IDs?
- How will the adapter represent a monitored Pokémon that is temporarily unloaded?
- Can cosmetic marker state be represented without mutating Cobblemon battle data?
- What event contract will synchronize an Ouros world entity with an AutoPTU combatant if that individual is deliberately selected for battle?

## Unresolved canon questions

- Whether artificial wildlife tags exist in Ouros;
- technology by region;
- monitoring authorization;
- welfare requirements;
- sensitive-location access policy;
- public versus precise track data;
- device recovery norms;
- research-subject naming conventions;
- protected/sacred-site restrictions;
- institutional responsibility for receiver networks.

No answer is promoted by Pass 79.