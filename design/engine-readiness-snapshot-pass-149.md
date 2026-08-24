# Engine Readiness Snapshot — Pass 149

Status: evidence snapshot for narrative dependency planning. AutoPTU-Java and AutoPTU are read-only inputs to this document.
Date: 2026-08-24

## Live revisions inspected

- AutoPTU-Java `main`: `7a7a6d93cedf82aa16e427b166160b6e39756676` — `Port Sway pre-damage reaction (#177)`.
- AutoPTU Python `main`: `4b35bc2b37b7f3e536c3974982729025740fcd79` — Career persistence recovery for malformed season containers; no tactical promotion implied.

The Java README continues to state that Python AutoPTU is authoritative while the port is incomplete and still lists full battle state, full damage, status controller, terrain, hazards, forced movement, reactions, hook registries, AI policy and Minecraft/Cobblemon adapter work as incomplete.

## Permanent capability map

| Capability family | Pass 149 status | Evidence boundary |
|---|---|---|
| targeting / footprints / range / LoS | VERIFIED | Java README marks targeting, areas, footprints, anchors and LoS implemented; legal action space consumes them authoritatively. |
| base movement legality | VERIFIED | Shift/Jump legality, movement modes, terrain costs, blockers, fit and related base rules are documented as ported. |
| complete movement including push/pull/knockback/interception/forced movement | BLOCKING | Sway now includes a specific authoritative adjacent push primitive, but README still lists forced movement incomplete. One Sway push is not a generic forced-movement subsystem. |
| core calculations | VERIFIED | Damage Base/type chart/stages/accuracy/weather DB/crit/Burn/modifier primitives are documented as implemented. |
| action economy / initiative | VERIFIED | Typed action budget, initiative variants and ordering have parity-backed implementations. |
| full turn / round lifecycle | PARTIAL | Multiple ROUND_START, delayed-hit and temporary-state slices exist, but full lifecycle/transcript parity remains incomplete. |
| full stateful damage pipeline | PARTIAL | Normal and delayed paths cover meaningful slices, but README explicitly leaves full damage incomplete. |
| status lifecycle | PARTIAL | Status mutation/prevention slices exist; full status controller remains incomplete. |
| terrain / weather / hazards / zones / reactions | BLOCKING | Field-state lifecycle and several PRE-damage reactions exist, including Sway at this head, but README explicitly lists terrain, hazards and reactions as incomplete. Treat the family as blocking unless an encounter uses an individually verified narrow contract. |
| move-specific behavior | PARTIAL | Multi-target/delayed/reaction-specific Move paths exist, not the full Move catalog. |
| abilities | PARTIAL | Multiple parity-backed Abilities exist, not the full registry. |
| items | PARTIAL | Item effects exist in slices; full item hook registry remains incomplete. |
| Trainer Features / perks | PARTIAL | Generic execution gates/effects plus selected concrete interactions exist; catalog parity is incomplete. |
| AI legal-action infrastructure | VERIFIED | Deterministic legal `BattleChoice` action-space contract is documented as implemented. |
| AI tactical policy | BLOCKING | README still lists scoring/policy over legal choices as pending. |
| Minecraft / Cobblemon / Craftics adapter / playback | BLOCKING | Java explicitly states it is not a Minecraft mod yet and adapter work is pending. |

## New Java evidence: Sway is narrow, not a category promotion

Commit `7a7a6d9` adds a registered `sway-melee-redirect` PRE-damage reaction, once-per-scene usage state, action spending, recursive original-Move resolution and an adjacent push application. The commit also adds dedicated parity/lifecycle tests.

Narrative implication:

- a future encounter needing the exact verified Sway behavior may cite that contract after confirming all required surrounding state;
- a story needing generic shove, collision, escort displacement, knockback chains, interception or terrain-triggered movement still depends on `complete movement` and remains BLOCKING;
- a story needing arbitrary interrupts/reactions still depends on the broader `terrain/weather/hazards/zones/reactions` family and remains BLOCKING.

## Pass 149 encounter dependency mapping

### Return Day at Riverside — FULL

Required:

- complete movement — BLOCKING if civilians/responders must move tactically;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING;
- terrain/weather/hazards/zones/reactions — BLOCKING only if active flood/debris mechanics are retained.

REDUCED: resolve civilians, route reopening and flood state outside the grid, then use verified targeting/base movement/core/action economy/AI-legality in a static arena. Narrative premise is preserved.

### Seasonal Arrival at North Depot — FULL

Required:

- complete movement — BLOCKING for moving passengers/wildlife objectives;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED: passengers are unloaded/redirected in world state before a static independent encounter.

### Census Route Through a Changing Settlement

No battle capability is inherently required. If an unrelated confrontation occurs, use a normal static encounter. Demographic truth stays outside AutoPTU.

## Demography-specific world-state blockers

These are narrative/overworld contracts, not AutoPTU battle categories:

- `SETTLEMENT_POPULATION_UNIT` persistence;
- versioned population estimates and geography revisions;
- residence-episode persistence with privacy policy;
- temporary-presence episodes;
- displacement/return lifecycle;
- census/survey provenance and uncertainty;
- actor-level movement -> aggregate mobility handoff;
- Demography -> Lodging/Travel/Water/Transit/Emergency Services demand snapshot;
- authoritative demographic state -> coarse Minecraft population presentation;
- safeguards preventing loaded NPC/entity count from becoming population truth.

## Mechanical non-inferences

Pass 149 does not authorize:

- population-based wild spawn rates;
- crowd morale modifiers;
- displacement Status;
- resident-only combat bonuses;
- family/household Features;
- citizen/resident eligibility inferred from PTU class or Skill;
- loaded Minecraft NPC count as demographic evidence;
- Sway’s adjacent push primitive as generic crowd movement.

## PTU / Caelo source status

The accessible File Library search did not recover the project’s primary Caelo corpus for settlement population or residence rules. The retrieved narrative-arc package points back to PTU 1.05 and the project oracle rather than supplying a Caelo demographic rule.

Super PTU Online Helper was not exposed as an invocable capability in this run. No result is invented or attributed to it.

## Open questions

- Does Caelo establish settlement population figures or demographic history that must be authored rather than estimated?
- Does the setting define legal residence, citizenship, regional registration or none of these?
- Which demographic records should be public versus aggregate/private?
- Should population change advance only through authored events, or may low-amplitude background change occur offline?
- How should player-founded businesses/settlements contribute to population without converting online-player counts into residents?
- What minimum engine capabilities are required before civilians are ever allowed inside a tactical grid rather than evacuated before battle?