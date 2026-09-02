# Engine Readiness Snapshot — Pass 208

Status: READ-ONLY ENGINE AUDIT
Date: 2026-09-02

## Live evidence checked

Narrative head at the start of pass 208: `e6204de10d4878137f2983ed80042c1be37225f1`.

AutoPTU-Java head: `496f7e15dbc4bb547449727cd60cd397d8d9005a` (`Add full project and rulebook sanity workflow (#326)`). Its parent `716687c6f8431807b91f33567cc8c9c7fd010756` remains the latest gameplay evidence referenced by the preceding forced-movement audit. The current head changes CI/sanity coverage and does not add a new gameplay family.

AutoPTU head: `729bae2d424963ff9bb3f4159c9a7ac9152128a7` (`Career: keep battle coordinates synced after viewport resize (#237)`). The change is explicitly presentation-only and does not alter battle rules or outcomes.

Therefore pass 208 has no live evidence that promotes a partial/blocking family to verified-complete.

## Permanent capability categories

| Capability category | Current state | Pass-208 consequence |
|---|---|---|
| targeting/footprints/range/LoS | VERIFIED within audited contracts | usable for reduced ordinary battle |
| base movement legality | VERIFIED within audited contracts | usable for reduced ordinary battle |
| complete movement including push/pull/knockback/interception/forced movement | PARTIAL | full crossing geometry cannot depend on displacement/interception yet |
| core calculations | VERIFIED within audited contracts | usable for individually audited battle paths |
| action economy/initiative | VERIFIED within audited contracts | usable for reduced ordinary battle |
| full turn/round lifecycle | PARTIAL | avoid timed/multi-stage tactical objectives in reduced version |
| full stateful damage pipeline | PARTIAL | only individually audited paths may be relied upon |
| status lifecycle | PARTIAL | avoid delayed/complex status objectives in reduced version |
| terrain/weather/hazards/zones/reactions | BLOCKING as a complete family | Conquest-style location mechanics remain full-version only |
| move-specific behavior | PARTIAL | each move used by a live encounter still needs exact-path verification |
| abilities | PARTIAL | ability identity does not prove full behavior parity |
| items | PARTIAL | evidence props cannot silently become mechanical battle items |
| Trainer Features/perks | PARTIAL | clue interpretation/interrupts must wait for verified governing contracts |
| AI legal-action infrastructure | VERIFIED within audited contracts | usable when the supported action space is known |
| AI tactical policy | BLOCKING for complete objective-aware behavior | do not require protect/hold/reach tactics from AI in reduced version |
| Minecraft/Cobblemon/Craftics adapter/playback support | PARTIAL/BLOCKING for complete target support | presentation can show sites/evidence; combat/world reconciliation remains capability-gated |

## Pass-208 design boundary

The evidence web is primarily world-state architecture. Direct observations, document custody, timestamps, links between records, NPC testimony and publication state do not need Minecraft to implement PTU combat rules.

Any interaction that claims a mechanical consequence must cross into an authoritative rules contract. Examples include a Skill check, Feature permission, item effect, movement capability, reaction, hazard effect, tactical terrain effect, forced movement, status or battle objective resolved by combat state.

Minecraft may project an unstable shelf, bridge, cart, gate, instrument or observation marker. Presentation does not create the PTU rule attached to that object.

## Full Seasonal Crossing Evidence Race

Readiness: BLOCKED for the complete intended tactical version.

The complete version can require all 16 families because it may combine objective geometry, timed phases, protection/interception, displacement, hazards or weather, legal moves/abilities/items/features, objective-aware AI and playback.

Primary blockers today:

- terrain/weather/hazards/zones/reactions as a complete family;
- AI tactical policy for objective-aware behavior;
- complete Minecraft/Cobblemon/Craftics battle/playback/result reconciliation.

Additional partial dependencies:

- complete forced movement/interception family;
- full lifecycle;
- stateful damage;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

## Reduced Thin Delivery evidence-web version

Readiness: NARRATIVE/WORLD-STATE IMPLEMENTATION CANDIDATE, with battle handoff still limited to audited paths.

It can progress with:

- persistent evidence records and provenance;
- free-order access to existing Marea nodes;
- direct factual observations that do not invent PTU checks;
- links from one evidence node to several productive next nodes;
- publication/correction history;
- static Minecraft site presentation;
- optional visible encounter presence controlled by current authoritative world ecology;
- ordinary battle handoff only when the exact participating Pokémon/actions are supported;
- no tactical terrain effect, reaction, forced movement objective, weather phase, delayed status objective or objective-aware AI requirement.

A battle result must not write an investigative conclusion unless an explicit world contract separately defines why that result is evidence.

## PTU/Kairos source questions requiring page-level verification before mechanics

The narrative source index identifies the relevant authoritative sections but this pass does not promote routing notes into rules. Implementation still needs exact source-page checks for:

- which Skills can discover versus interpret route/record evidence;
- whether any Feature changes investigation timing, access or information quality;
- how an escort/protect/reach objective should coexist with normal action economy;
- exact terrain, hazard, weather and status interactions for a future seasonal-crossing battlefield;
- whether any candidate field tool is a mechanical item and, if so, its exact legal effect;
- boss/advanced encounter guidance if a future dungeon uses location-authored tactical phases.

## Unresolved implementation questions

- What service owns generic authoritative Skill checks outside battle.
- Whether mandatory continuation facts should always be direct observations, with checks reserved for added interpretation.
- How `EvidenceNode` provenance is persisted and shared between players/institutions.
- How a quest conclusion names evidence relationships instead of using a hidden clue-count threshold.
- What exact battle-completion state can be reconciled back into world evidence without allowing combat to manufacture noncombat truth.
- Whether static semantic encounter objects already have an adapter contract suitable for future location-authored interactables.
- Whether Tackle, Growl and Big Pecks on the existing Sendero Fletchling are verified through the exact normal player-vs-wild path intended for first live use.

No partial capability is treated as complete in pass 208.