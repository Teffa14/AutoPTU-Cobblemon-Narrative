# Engine Readiness Snapshot — Pass 18

Status: implementation evidence snapshot. Not canon. This file records current readiness only and may be superseded by later evidence.

Snapshot basis: `Teffa14/AutoPTU-Java` main through commit `b71a0c1887cd303b78099eed846293a9dd60ef2f` (`Port round-start temporary-effect cleanup`). Python AutoPTU remains the project-designated behavior oracle while Java parity is incomplete.

## Permanent capability categories

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
  Trainer Features/perks: BLOCKING
  AI legal-action infrastructure: VERIFIED
  AI tactical policy: BLOCKING
  Minecraft/Cobblemon/Craftics adapter/playback support: BLOCKING
```

## New evidence since the earlier encounter-contract snapshot

Java now owns a canonical temporary-effect store and clears round-scoped temporary effects at round start with Python-oracle parity.

This strengthens the `full turn/round lifecycle` implementation because state cleanup now occurs through the authoritative runtime. It does not upgrade that family to VERIFIED: general status duration, terrain/weather lifecycle, delayed effects, broader Ability triggers, Trainer Feature triggers and other ordered lifecycle interactions remain incomplete or unverified.

## Food-specific interpretation

Python AutoPTU currently contains substantial Food Buff and Chef-related behavior, including item-derived Digestion/Food Buff state, Chef taste handling and interactions with Abilities such as Harvest, Gluttony and Lunchbox.

That Python evidence does not mean Java can execute food mechanics yet.

A mechanically active food encounter should therefore continue to treat these categories conservatively:
- `items`: PARTIAL overall; no general Java Food Buff parity demonstrated by this snapshot.
- `abilities`: PARTIAL overall; representative parity-backed Ability hooks do not establish Harvest/Lunchbox/Gluttony behavior.
- `Trainer Features/perks`: BLOCKING for Chef-specific Feature behavior until authoritative Java support is demonstrated.
- `full turn/round lifecycle`: PARTIAL.
- `status lifecycle`: PARTIAL where food cures or alters statuses.
- `full stateful damage pipeline`: PARTIAL where a food/Ability/Feature changes damage.
- `Minecraft/Cobblemon/Craftics adapter/playback support`: BLOCKING.

Agriculture, menus, kitchens, restaurants, ingredient provenance and meal scenes remain narrative/world-state systems and do not require food-combat support unless they attempt to grant or consume an authoritative PTU effect.

## Evidence discipline

Do not upgrade a permanent category from one representative behavior.

- temporary-effect cleanup does not prove full lifecycle;
- Mega Launcher does not prove the Ability library;
- Pink Pearl does not prove the Item library;
- one Food Buff behavior in Python does not prove Java Food Buff support;
- a `TrainerFeatureEvent` type does not prove Trainer Features/perks;
- legal action enumeration does not prove tactical AI;
- headless battle events do not prove Minecraft playback.

Future narrative passes should cite the most recent snapshot file and inspect live Java evidence again whenever a mechanically rich encounter depends on one of these families.