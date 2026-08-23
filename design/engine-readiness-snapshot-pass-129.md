# Engine Readiness Snapshot — Pass 129

Status: implementation evidence snapshot for narrative design. AutoPTU-Java and AutoPTU are read-only sources for this task.

Narrative topic: memorials, remembrance and legacy continuity.

## Live repositories inspected

### AutoPTU-Java

Head inspected: `7de79dcd30b241d439724050fb24ee893a7c5c63`

Latest commit inspected: `Freeze forced movement instruction contract (#160)`.

The new slice adds a language-neutral `ForcedMovementInstruction` and parity-backed parsing for Push/Pull intent from PTU Move metadata. The contract explicitly states that it does not move a combatant; later spatial resolution still has to execute the instruction authoritatively.

Important consequence: this is evidence toward complete movement, but it does not promote the complete-movement category. Push/Pull parsing is not Push/Pull execution.

The live README still lists these large areas as incomplete:

- core combatant/grid battle state;
- full damage resolution pipeline;
- status controller;
- terrain;
- hazards;
- forced movement;
- reactions;
- full move/ability/item/perk/Trainer Feature registries;
- full BattleSpec -> BattleTranscript parity;
- AI scoring/policy;
- Craftics/Cobblemon adapter.

### AutoPTU Python

Head inspected: `1c673eb676fdeca71ee55e1de8a90b8f7d2cbcf3`.

Latest visible change is Career/deployment provenance: expose the exact deployed source commit. It does not change the tactical capability classification below.

The Java forced-movement parity workflow pins a Python oracle commit for that specific contract. That does not make Java's broader movement system complete.

## Permanent capability classification

### VERIFIED

#### targeting / footprints / range / LoS

Evidence remains sufficient for the established geometric targeting family used by static encounter reductions.

Pass 129 use: static battle arenas around memorial sites can rely on this category when normal Move targeting is sufficient.

#### base movement legality

Evidence remains sufficient for ordinary Shift/Jump legality and movement capabilities already covered by the port.

Pass 129 use: reduced encounters can use a frozen, prevalidated map with ordinary legal movement.

#### core calculations

Established calculation primitives remain verified for the ported scope.

#### action economy / initiative

Established initiative ordering, action budgets and authoritative turn-flow primitives remain verified for the permanent category used by this project.

#### AI legal-action infrastructure

Java can enumerate/filter legal choices for the supported static combat space. This does not mean it can choose strategically among non-KO objectives.

### PARTIAL

#### full turn / round lifecycle

Many lifecycle slices are parity-backed, but the full family is not complete. Memorial encounters do not require promotion here.

#### full stateful damage pipeline

Substantial slices exist, including delayed-hit paths and hooks, but the README still marks the full pipeline incomplete.

#### status lifecycle

Recent passes strengthened prevention/application/removal behavior, stacking and suppression interactions. The full controller remains incomplete.

#### move-specific behavior

Many representative Move contracts are ported. The catalog is not complete.

#### abilities

Multiple Ability families have parity evidence. The catalog and all lifecycle interactions remain incomplete.

#### items

Do not assume full item coverage. Memorial objects such as bells, plaques, candles, photographs or keepsakes are narrative/material objects unless an exact PTU Item reference says otherwise.

#### Trainer Features / perks

Java now has substantial generic infrastructure for prerequisites, context, frequency/cooldowns, resources, target scopes, bookkeeping and several generic effects. That does not prove the full Trainer Feature catalog.

PTU public material associates tomb caretaking with one possible Hex Maniac background. This does not make every memorial caretaker a Hex Maniac and does not demonstrate Hex Maniac runtime parity.

### BLOCKING

#### complete movement including push / pull / knockback / interception / forced movement

BLOCKING remains correct.

New evidence in Java:

- Push/Pull instruction intent can now be parsed into an authoritative language-neutral contract with Python parity.

Missing evidence needed before promotion includes, at minimum:

- authoritative application of the displacement to current positions;
- path/collision/fit interactions;
- legal landing resolution;
- map-boundary behavior;
- chained/recursive movement interactions where rules require them;
- interaction with occupancy and footprints;
- interception and other movement reactions;
- event/transcript parity for executed movement;
- integration with AI and Minecraft playback.

Pass 129 FULL encounters using a moving procession or dynamic evacuation therefore remain blocked by this category.

#### terrain / weather / hazards / zones / reactions

Still BLOCKING as a broad permanent family.

A memorial site being foggy, on fire, crowded, damaged, sacred, dark or unstable does not create PTU environmental mechanics without exact support.

Pass 129 uses this category only when a specific FULL version includes an actual tactical environment effect.

#### AI tactical policy

Still BLOCKING.

Legal-action enumeration does not imply objective-aware behavior for:

- `EVACUATE`;
- `PROTECT_ROUTE`;
- `CLEAR_ROUTE`;
- `WITHDRAW`;
- `PROTECT_ARCHIVIST`;
- `RECOVER_RECORD`;
- `REACH_OBJECTIVE`.

#### Minecraft / Cobblemon / Craftics adapter and playback

Still BLOCKING.

The adapter must eventually project memorial revisions, semantic objectives, civilians, protected objects and battle results without becoming a second PTU rules engine.

## Pass 129 encounter dependency table

| Encounter | Intended FULL dependencies | Reduced version available now? |
| --- | --- | --- |
| Memorial Procession Route Interruption | complete movement; AI tactical policy; adapter/playback; environment family only if a validated hazard exists | Yes. Stop procession, evacuate civilians, freeze static street, run conventional battle. |
| Archive Recovery at Old Memorial Hall | complete movement if extraction is dynamic; terrain/hazards/zones/reactions if the building actively changes; AI tactical policy; adapter/playback | Yes. Cordon unsafe areas, remove records/noncombatants, use static safe room/corridor. |
| Caretaker Succession at Lantern Hill | primarily overworld Agreements/Credentials/Land Tenure/Institutional Review; complete movement + AI policy + playback only if a separate crisis interrupts | Yes. Resolve stewardship without combat. |

## New overworld blockers introduced by Pass 129

These are not AutoPTU battle-core responsibilities:

- `MEMORIAL_IDENTITY_STATE` — stable identity independent of blocks/location;
- `MEMORIAL_REVISION_HISTORY` — inscriptions, names, rebuilds, accessibility changes and relocations;
- `LOSS_OR_ABSENCE_STATUS` — explicit separation of deceased, missing, retired, destroyed, closed and unknown;
- `MISSING_SUBJECT_MEMORIAL_STATE` — memorialization without false death assertion;
- `COMMEMORATION_HISTORY` — versioned recurring events without inferred emotions;
- `MEMORIAL_OBJECT_CUSTODY` — cross-link to Material Culture/Museums without ownership invention;
- `DIGITAL_MEMORIAL_STATE` — durable publications, privacy and platform migration;
- `LEGACY_HANDOFF_STATE` — responsibility continuity without inheritance law;
- `MEMORIAL_TO_PUBLIC_MEMORY_HANDOFF` — physical revision versus social interpretation;
- `MEMORIAL_TO_MINECRAFT_PROJECTION` — current physical revision projected without losing Chronicle history.

## Mechanical non-inferences

Pass 129 explicitly prohibits these shortcuts:

- `Fainted` -> deceased;
- Injury -> deceased;
- zero HP -> deceased without explicit authoritative rule;
- missing Pokémon -> deceased;
- release -> deceased;
- retirement -> deceased;
- memorial marker -> proof of death;
- Ghost-type near memorial -> subject's spirit;
- bell/candle/song/flower -> PTU effect;
- memorial object -> PTU Item;
- caretaker -> Hex Maniac;
- commemorative attendance -> morale/grief/belief state;
- remembrance -> Loyalty/Command/Friendship change;
- memorial garden -> Terrain;
- fog or darkness used visually -> Accuracy/LoS modifier;
- processional crowd -> forced movement;
- battle victory -> historical truth, succession, stewardship or ownership.

## PTU / Caelo evidence posture

The public PTU Hex Maniac reference provides a useful setting precedent that tomb caretaking can coexist with occult expertise, but does not make those mechanics universal.

The project already treats Loyalty/Command, Trainer Features and other mechanical states as belonging to authoritative PTU/Caelo implementation rather than narrative inference.

The complete primary Caelo corpus was not reliably available through this runtime, so no Caelo-specific death, memorial, inheritance, Ghost, burial or caretaker rule was added.

Super PTU Online Helper was not exposed as an invocable capability in this runtime. No output is attributed to it.

## Current permanent map

```text
VERIFIED
- targeting / footprints / range / LoS
- base movement legality
- core calculations
- action economy / initiative
- AI legal-action infrastructure

PARTIAL
- full turn / round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features / perks

BLOCKING
- complete movement including push / pull / knockback / interception / forced movement
- terrain / weather / hazards / zones / reactions
- AI tactical policy
- Minecraft / Cobblemon / Craftics adapter / playback
```

No category is promoted in Pass 129.

## Next validation questions relevant to this layer

1. Does the project's authoritative PTU/Caelo corpus define death at all, and if so under what optional/campaign rules?
2. Can any battle outcome authoritatively emit a death event, or must death remain narrative/GM-authored?
3. Which Hex Maniac/Occult interactions are actually implemented in Java rather than merely present in source data?
4. When forced-movement execution lands in Java, does it cover civilians/noncombatants or only battle combatants? The memorial layer should not assume either.
5. Will the Minecraft adapter support semantic protected objects/civilians, or should all memorial encounters continue using pre-battle evacuation/frozen geometry?
6. What server-side service owns memorial revisions and prevents chunk reloads from restoring obsolete inscriptions or locations?