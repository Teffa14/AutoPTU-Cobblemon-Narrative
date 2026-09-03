# Engine readiness snapshot — Pass 237

Status: CURRENT READ-ONLY CROSS-CHECK
Date: 2026-09-03

Narrative scope:
- `research/2026-09-03-disturbance-succession-recovery-scan-237.md`;
- `design/disturbance-succession-recovery-contract.md`;
- `proposals/2026-09-03-marea-sendero-recovery-window-fixture-237.md`;
- `implementation/marea-sendero-disturbance-recovery-fixture-v1.json`.

## AutoPTU-Java

Current `main` checked:
- `f8ee22f957f11f56fd43cbf0ea713b25f534d6ca`;
- `Derive movement landing context from authoritative state (#335)`.

The commit derives tile-entry/landing context from server-owned battle state and canonical rule content. It strengthens the already-bounded movement landing/trap seam.

It does not establish complete support for:
- push/pull/knockback/interception/forced movement as a family;
- changing terrain during an encounter;
- spreading contamination or runoff zones;
- arbitrary timed stabilization objectives;
- full reaction semantics;
- autonomous protect-refuge/withdraw/contain tactical policy;
- end-to-end Minecraft/Cobblemon/Craftics playback plus semantic ecology writeback.

No permanent capability category is promoted by this commit.

## Python AutoPTU oracle

Current `main` checked:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`;
- latest commit is presentation-coordinate synchronization after viewport resize.

This does not change PTU mechanical coverage.

## Permanent capability audit

VERIFIED within audited contracts:
1. targeting/footprints/range/LoS;
2. base movement legality;
4. core calculations;
5. action economy/initiative;
14. AI legal-action infrastructure.

PARTIAL:
3. complete movement including push/pull/knockback/interception/forced movement;
6. full turn/round lifecycle;
7. full stateful damage pipeline;
8. status lifecycle;
10. move-specific behavior;
11. abilities;
12. items;
13. Trainer Features/perks.

MIXED / PARTIAL / BLOCKING outside verified slices:
9. terrain/weather/hazards/zones/reactions.

BLOCKING as a complete family:
15. AI tactical policy.

PARTIAL / BLOCKING end-to-end:
16. Minecraft/Cobblemon/Craftics adapter/playback support.

## Pass 237 dependency mapping

### Ambient disturbance, succession and recovery

Required AutoPTU tactical families: none.

Ouros can safely own:
- typed disturbance events;
- ecological legacy snapshots;
- recovery stage transitions;
- temporary resource pulses;
- recovery/reorganization pressures;
- repeat-disturbance compounding;
- observation evidence;
- explicit battle-escalation gates.

Minecraft/Cobblemon can project authored evidence but cannot decide recovery from block/entity state.

### Basic conflict during recovery

A reduced encounter can use the verified foundations:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

Selected Moves, Abilities, Items, statuses or Trainer Features still require exact content verification because their families remain partial.

The recovery state should be frozen or abstracted during the bounded battle. The semantic result can then return to Ouros as intervention success/failure, additional disturbance, capture/removal or another explicitly supported ecological consequence.

### Rich restoration / containment encounter

A sequence with retreat corridors, dynamic debris, spreading contamination, timed stabilization or defended refuge has these dependencies:

- category 3 complete movement: PARTIAL;
- category 6 full turn/round lifecycle: PARTIAL;
- category 7 stateful damage: PARTIAL if environmental damage or attrition is used;
- category 8 status lifecycle: PARTIAL if poison, slow, fatigue or similar mechanical conditions are used;
- category 9 terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING and the principal blocker for dynamic environmental mechanics;
- category 10 move-specific behavior: PARTIAL;
- category 11 abilities: PARTIAL;
- category 12 items: PARTIAL;
- category 13 Trainer Features/perks: PARTIAL;
- category 15 AI tactical policy: BLOCKING for protect/withdraw/contain priorities as a complete family;
- category 16 adapter/playback: PARTIAL/BLOCKING for visible dynamic environmental playback and semantic world-state writeback.

The rich version must remain reduced until tests/contracts verify the exact families required by the authored encounter.

## Safe implementation boundary now

The Pass 237 JSON fixture is ready to become ecology-runtime regression tests without waiting for AutoPTU completion. It intentionally proves that:
- habitat impact does not automatically change population count;
- time alone does not complete recovery;
- temporary resource gain can coexist with degradation;
- repeat disturbance starts from current state;
- generic spawn/despawn does not author ecology truth.

Pass 238 should consume habitat/recolonization context from this contract but remain responsible for population/demographic arithmetic.

## Unresolved mechanical questions

1. If a future encounter uses moving runoff/debris, which category-9 primitives are canonical and tested rather than simulated by the adapter?
2. What exact semantic post-battle outcomes can add disturbance without importing tactical HP/status facts into long-term ecology?
3. When category-16 writeback is available, what idempotency key prevents duplicate application of one battle/intervention result?
4. Can dynamic environmental objectives be represented with current lifecycle infrastructure, or do they require a dedicated objective scheduler?

## Unresolved canon/ecology questions

1. Which disturbances are normal components of Marea's eventual biome/terrain regime once the generated world is bound to authored sites?
2. What recovery targets should be treated as institutional goals rather than ecological inevitabilities?
3. Which existing or future authorized species benefit from early-successional resources?
4. At what evidence threshold does transient reorganization become persistent reorganization?
5. How does Pass 238 represent delayed recolonization and low-density recovery without automatic refill?

## Conclusion

Pass 237 is world-state and regression-fixture ready. Its rich tactical variant remains dependent mainly on complete movement, lifecycle, dynamic environmental/reaction semantics, tactical policy and end-to-end adapter/writeback support.