# Engine readiness snapshot — Pass 234

Status: CURRENT READ-ONLY CROSS-CHECK
Date: 2026-09-03

Narrative scope:
- `research/2026-09-03-wild-nesting-parental-care-disturbance-scan-234.md`;
- `design/wild-nesting-juvenile-parental-care-contract.md`;
- `proposals/2026-09-03-marea-sendero-nesting-disturbance-fixture-234.md`.

## AutoPTU-Java

Current `main` checked:
- `21e0b02e5ff17132f3a7ed04007784884323df12`;
- `Add stateful movement landing consequence executor (#334)`.

Verified bounded evidence from the commit:
- server-authoritative execution boundary for resolved movement-landing consequences;
- status application routed through the shared status-prevention pipeline;
- ordered semantic trap block/trigger events;
- deterministic trap consumption after observable trigger order.

This evidence is deliberately narrow. It does not establish:
- generic escort objectives;
- complete interception/push/pull/knockback coverage;
- arbitrary defended zones/reactions;
- weather-phase encounters;
- parental tactical AI;
- complete terrain/hazard semantics;
- end-to-end Minecraft playback/writeback.

No permanent family is promoted because of this commit.

## Python AutoPTU oracle

Current `main` checked:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.

Latest visible Python change is presentation-side Career viewport coordinate synchronization and does not change battle-rule authority or capability readiness for this ecology pass.

Python remains read-only and authoritative as the parity oracle while the Java port is incomplete.

## World-state work safe without tactical completeness

The following can advance independently in Ouros:
- persistent nest-site occupancy;
- caregiver/dependent relationship records;
- provisioning pressure;
- vigilance/protective intent;
- disturbance accumulation and decay;
- relocation/abandonment pressure;
- observation evidence;
- route-management interventions;
- population/activity/spawn projection inputs;
- delayed verification and ecological consequences.

These systems must not author HP, tactical statuses, initiative, exact positions, legal moves, forced displacement, injury or battle defeat.

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

## Nesting encounter mapping

### Observation / route management

Required tactical families: none.

World integration dependency:
- adapter/playback remains partial/blocking for rich semantic presentation.

Reduced implementation can use persistent world state, simple projection and observation packets.

### Protective caregiver battle

Basic verified foundations:
- targeting;
- base movement;
- calculations;
- action economy/initiative;
- legal-action infrastructure.

Exact dependencies if the rich version uses them:
- interception/forced displacement: category 3 PARTIAL;
- lifecycle: category 6 PARTIAL;
- stateful damage: category 7 PARTIAL;
- statuses: category 8 PARTIAL;
- defended zones/reactions/weather/hazards: category 9 MIXED/PARTIAL/BLOCKING;
- move behavior: category 10 PARTIAL;
- abilities: category 11 PARTIAL;
- items: category 12 PARTIAL;
- Trainer interrupts: category 13 PARTIAL;
- autonomous protective objective policy: category 15 BLOCKING;
- world playback/writeback: category 16 PARTIAL/BLOCKING.

Reduced version remains a simple legal AutoPTU battle on static terrain after explicit Ouros handoff, with dependents outside tactical participation.

### Evacuation / relocation under active pressure

Rich version requires exact escort/forced movement, possible hazards/weather/reactions and objective AI. Those families are not complete.

Reduced version resolves relocation as Ouros overworld state and pauses that movement for any simple supported AutoPTU battle.

## Conclusion

Pass 234 can safely implement nesting, care and disturbance as persistent ecology now.

The largest mechanical blockers for the rich combat version remain tactical AI policy, complete environmental/reaction semantics, exact escort/forced-movement breadth and end-to-end adapter playback.

No capability family is promoted in this snapshot.
