# Engine readiness snapshot — Pass 236

Status: CURRENT READ-ONLY CROSS-CHECK
Date: 2026-09-03
Narrative scope:
- `research/2026-09-03-human-disturbance-habituation-gradient-scan-236.md`;
- `design/human-disturbance-habituation-gradient-contract.md`;
- `proposals/2026-09-03-marea-sendero-human-disturbance-fixture-236.md`;
- `implementation/marea-sendero-human-disturbance-fixture-v1.json`.

## AutoPTU-Java

Current `main` checked:
- `f8ee22f957f11f56fd43cbf0ea713b25f534d6ca`;
- `Derive movement landing context from authoritative state (#335)`.

This adds a bounded authoritative-state factory for movement landing context on top of the previously verified landing hook/trap slice.

It does not verify:
- complete interception/push/pull/knockback/forced movement;
- arbitrary retreat-corridor objectives;
- full turn/round objective lifecycle;
- complete weather/hazard/zone/reaction semantics;
- autonomous defend-withdraw/flee/protect-young tactical policy;
- end-to-end Minecraft/Cobblemon/Craftics playback and semantic world-state writeback.

No permanent capability family is promoted by this commit.

## Python AutoPTU oracle

Current `main` checked:
- `729bae2d424963ff9bb3f4159c9a7ac9152128a7`;
- presentation-coordinate synchronization only.

No broad tactical capability changes are established by that commit.

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

## Pass 236 dependency mapping

### Ambient habituation / avoidance / activity shifting

Required AutoPTU tactical families: none.

This can run entirely as Ouros persistent ecology state plus Minecraft/Cobblemon projection. Category 16 remains relevant for rich projection and persistence plumbing, but no battle rule needs to be invented in the adapter.

### Basic escalation to ordinary battle

Verified foundations:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

Content-specific move, Ability, item, status and Trainer Feature behavior still requires exact verification for selected combatants.

Reduced implementation:
- ecology chooses explicit combatants;
- ordinary bounded AutoPTU battle begins;
- noncombatants and population state remain outside tactical authority;
- semantic result returns as disturbance/capture/conflict pressure.

### Retreat corridor / guarded withdrawal encounter

Rich-version blockers/partials:
- interception and forced displacement: category 3 PARTIAL;
- timed withdrawal objective: category 6 PARTIAL;
- injury/attrition consequences: category 7 PARTIAL;
- fear/fatigue-like mechanical statuses if used: category 8 PARTIAL;
- corridor zones, environmental hazards and reactions: category 9 MIXED/PARTIAL/BLOCKING;
- selected move behavior: category 10 PARTIAL;
- selected Abilities: category 11 PARTIAL;
- support/repellent/rescue items: category 12 PARTIAL;
- Trainer interrupts: category 13 PARTIAL;
- defend-withdraw tactical prioritization: category 15 BLOCKING;
- visible multi-actor playback/writeback: category 16 PARTIAL/BLOCKING.

## World-state implementation safe now

Pass 236 can safely implement:
- per-site human disturbance vectors;
- harmless/harmful exposure memory;
- tolerance/avoidance pressure;
- activity-window shifts;
- welfare cost independent from approach tolerance;
- anthropogenic resource subsidy pressure;
- observation evidence and survey quests;
- explicit escalation gates into AutoPTU.

These systems must never directly author PTU HP, statuses, initiative, move legality, displacement or battle results.

## Conclusion

Pass 236 is world-state ready. The machine-readable fixture can be implemented against the ecology runtime without waiting for battle-engine completion. A rich guarded-retreat encounter remains dependent on exact complete-movement, lifecycle, environmental/reaction, tactical-policy and adapter families.
