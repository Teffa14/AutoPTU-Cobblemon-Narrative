# Engine Readiness Snapshot — Pass 103

Status: implementation evidence snapshot for narrative planning. Not a claim of complete engine coverage.

## Live evidence inspected

AutoPTU-Java head observed during this pass:

`4c75dc082ae7848bdfa9c4e385e08ffde6760d9e`

Latest relevant commit:

`Port generic Trainer Feature context gates (#138)`

This slice adds a Python-parity `TrainerFeatureContextResolution` primitive. The resolver now evaluates context gates including:

- required actor presence;
- actor scope such as self/team, enemy, Trainer or Pokémon;
- battle phase;
- action type;
- Move name;
- Move category;
- active/inactive actor state;
- minimum/maximum round;
- minimum/maximum damage values from the event payload;
- once-per-actor-per-round usage checks;
- chance gates using the authoritative Python-compatible battle RNG.

The implementation explicitly excludes other contracts. The Java source states that prerequisites, frequency/cooldowns, resource/AP spending, usage mutation, target scopes and effect application remain separate. Prerequisite checks were added in the immediately preceding Java slice (#137), but that still does not imply complete Feature execution.

The parity workflow also reinforces the authority boundary: context observations must come from authoritative battle state rather than Minecraft/Cobblemon.

This is meaningful progress for `Trainer Features / perks` infrastructure.

It does not prove:

- the complete Trainer Feature catalog;
- Feature frequency/cooldown enforcement as a family;
- full AP/resource/usage accounting for arbitrary Features;
- target-scope resolution for arbitrary Features;
- interrupt/reaction timing;
- effect application;
- Musician Songs;
- Voice Lessons;
- Drown Out;
- Sonic keyword behavior;
- Soundproof behavior;
- instrument or performance mechanics;
- audio playback integration.

AutoPTU Python evidence inspected for this pass:

The repository exposes structured PTU Trainer-class data including Musician through its Trainer class catalogs/source datasets. This establishes that Musician is represented in the Python-side project data/oracle corpus.

A current Java code search did not surface a concrete Musician/Song implementation. Therefore Musician-specific execution remains unverified even though generic Trainer Feature prerequisite and context gates now exist.

The Java README continues to state that the Python implementation remains authoritative while the port is incomplete and continues to list large unfinished areas including full damage/status behavior, terrain/hazards/forced movement/reactions, complete hook registries/transcript parity, tactical AI and Minecraft/Cobblemon integration.

## Permanent capability map

### VERIFIED

`targeting / footprints / range / LoS`

Static targeting geometry, footprint overlap, range and geometric LoS remain verified.

Pass 103 non-inference:

- hearing a song does not create a target;
- a stage edge is not a targeting boundary unless its physical geometry is projected;
- an instrument is not a targetable combat object by default;
- audience position does not modify LoS unless representative physical geometry actually exists in the frozen battle snapshot;
- acoustic propagation is not LoS.

`base movement legality`

Established Shift/Jump and known movement-mode legality remain verified.

Pass 103 non-inference:

- rhythm does not change movement speed;
- a dance floor does not create a movement mode;
- an ensemble arrangement does not define tactical formation;
- moving to music does not grant Shift distance;
- performer role does not create movement permissions.

`core calculations`

Established calculation primitives remain verified.

Pass 103 adds no:

- music quality score;
- harmony bonus;
- audience morale formula;
- rehearsal modifier;
- instrument power value;
- cultural authenticity score;
- composition rarity multiplier.

`action economy / initiative`

Established action economy and initiative remain verified.

Pass 103 non-inference:

- conductor -> initiative bonus;
- tempo -> turn order;
- drummer -> extra action;
- audience applause -> priority;
- musical cue -> free interrupt;
- ensemble membership -> shared initiative.

`AI legal-action infrastructure`

Legal-choice generation remains verified.

It does not prove tactical goals such as:

- PROTECT_INSTRUMENTS;
- CLEAR_AUDIENCE_EXIT;
- WITHDRAW_FROM_STAGE;
- PRESERVE_RECORDING;
- AVOID_CIVILIANS;
- PROTECT_PERFORMER;
- DEESCALATE;
- CONTINUE_PERFORMANCE.

### PARTIAL

`full turn / round lifecycle`

Representative phase ordering, cleanup, delayed hits, temporary effects, initiative rebuilding, Trainer AP/action reset, declared-action cleanup and Feature ordering/context slices exist.

Still PARTIAL because complete START/END effects, durations, all Status/Ability/Feature interactions, interrupts and transcript behavior are not proven.

Pass 103 distinction:

A musical performance timeline is overworld/event state. It is not battle-round lifecycle.

`full stateful damage pipeline`

Representative authoritative damage paths exist.

Still PARTIAL.

Pass 103 non-inference:

- loudness -> damage;
- amplifier -> damage bonus;
- falling instrument -> damage;
- broken speaker -> electrical damage;
- crowd surge -> damage;
- dissonance -> HP loss.

`status lifecycle`

Representative Status slices exist.

Still PARTIAL.

Pass 103 non-inference:

- lullaby -> Asleep;
- loud concert -> Confused;
- frightening music -> Fear;
- uplifting anthem -> status cure;
- soothing rehearsal -> Injury recovery;
- ordinary singing -> any PTU Status.

If an exact Move such as Sing is used, its own PTU/Caelo definition and Java behavior must be verified.

`move-specific behavior`

Representative Move slices exist.

Still PARTIAL.

Music-related non-inference:

An audible sound is not automatically a Sonic Move. Ordinary singing, instruments, recordings and PA systems do not inherit behavior from Sing, Supersonic, Hyper Voice, Relic Song, Perish Song or any other Move.

`abilities`

Representative Ability hooks exist.

Still PARTIAL.

Pass 103 non-inference:

- Soundproof does not automatically block conversation, ambience, alarms or client music;
- a species associated with music does not automatically possess a sound-related Ability;
- Toxtricity sound behavior does not prove electrical stage-equipment interactions;
- an Ability that modifies Sonic Moves does not modify ordinary overworld audio.

`items`

Representative held-item behavior exists.

Still PARTIAL.

Instruments, microphones, speakers, recordings, cases, sheet music, stands and repair tools remain world/material objects unless an exact PTU Item definition exists.

`Trainer Features / perks`

Still PARTIAL, with stronger infrastructure evidence this pass.

The two latest Java slices now provide generic parity-tested prerequisite gates (#137) and context gates (#138). The latter handles actor scope, phase, action type, Move identity/category, active state, rounds, event damage, once-per-actor-per-round conditions and chance/RNG.

This is substantial infrastructure progress but remains below complete Feature execution because frequency/cooldowns, resources/AP, usage mutation, target scopes and effect application remain separate contracts.

Music-specific blocker:

`MUSICIAN_FEATURE_EXECUTION_PARITY` remains unverified. Python project data contains Musician material, but current Java search did not surface implementation for Musician Songs or the class-specific effect family.

Pass 103 non-inference:

- musician profession = PTU Musician class;
- ensemble member = mechanical ally scope;
- composer = Trainer Feature;
- rehearsal = Feature use;
- performance event = Scene use;
- ordinary song = Musician Song;
- Musician data catalog = runtime implementation.

### BLOCKING

`complete movement including push / pull / knockback / interception / forced movement`

Still BLOCKING as a complete family.

Pass 103 impact:

- no true in-grid audience evacuation;
- no escorting performers through moving crowds;
- no interception around a stage or archive object;
- no dynamic pursuit through backstage areas;
- no movement-aware protection of instruments or recordings.

`terrain / weather / hazards / zones / reactions`

Still BLOCKING as a complete family.

Pass 103 impact:

- a stage does not create a zone automatically;
- speaker stacks do not create hazards;
- electrical equipment does not create shock zones;
- loud areas do not create Sonic terrain;
- rain at an outdoor concert does not create tactical Weather unless battle rules initialize it authoritatively;
- a Musician Song cannot be modeled as a custom Minecraft aura/zone.

`AI tactical policy`

Still BLOCKING.

Legal actions alone do not make actors protect instruments, evacuate, withdraw, avoid audiences, preserve recordings, honor a ceasefire or pursue non-KO goals.

`Minecraft / Cobblemon / Craftics adapter and playback`

Still BLOCKING.

There is no verified end-to-end contract for:

- semantic music/event state -> Minecraft audio presentation;
- authorized original audio assets;
- per-player accessible captions/visual rhythm cues;
- persistent ensemble/venue state;
- instrument custody;
- battle-safe stage geometry;
- PTU Musician/Sonic effects -> semantic playback;
- preventing client audio from becoming rules authority.

## Pass 103 specific overworld blockers

`MUSICAL_WORK_IDENTITY`
Stable identity for a work independent of one title, arrangement, recording or performance.

`MUSIC_VERSION_GRAPH`
Relationships among arrangements, regional variants, translations and revival reconstructions.

`MUSIC_AUTHORSHIP_CLAIMS`
Evidence-backed authorship/origin claims without forced certainty.

`MUSIC_TRADITION_STATE`
Living repertoire, performance contexts, transmission practices and change history.

`ENSEMBLE_IDENTITY_AND_MEMBERSHIP`
Persistent group identity and dated membership/role history without ownership or social inference.

`INSTRUMENT_INSTANCE_PROVENANCE`
Physical instrument identity, materials, maker, custody, repairs and performance history.

`MUSIC_REHEARSAL_STATE`
Attendance, timing, participant comfort, equipment issues and arrangement decisions.

`MUSIC_RECORDING_PROVENANCE`
Capture context, source medium, edits/copies, archive custody, access and publication state.

`MUSIC_TRANSMISSION_GRAPH`
Teacher/source -> learner -> learned variant without assuming exact copying.

`MUSIC_RESTRICTED_ACCESS`
Private, community-only, ceremony-only or archive-restricted content protected from procedural disclosure.

`MUSICIAN_FEATURE_EXECUTION_PARITY`
Exact PTU/Caelo Musician Song/Feature behavior implemented and parity-tested in Java before mechanical use.

`MUSIC_TO_MEDIA_AND_ARCHIVE`
Circulation and preservation handoff without collapsing custody, publication, rights or truth.

`MUSIC_TO_SOUNDSCAPE`
A performance may emit sound events, but propagation/observation remain under Soundscapes.

`MUSIC_TO_MINECRAFT_PROJECTION`
Semantic state, authorized original audio and accessibility presentation without client authority.

`MUSIC_TO_BATTLE_SNAPSHOT`
A music venue can freeze a safe arena without inventing stage/audio mechanics.

## Encounter dependency summary

### Rehearsal Hall Interruption — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL if invoked:

- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior for exact Sonic Moves;
- abilities for exact sound-related Ability interactions;
- items;
- Trainer Features/perks, with Musician specifically unverified.

BLOCKING:

- complete movement/interception/forced movement for live evacuation;
- terrain/weather/hazards/zones/reactions for interactive stage damage/hazards;
- AI tactical policy for withdraw/protect/avoid-civilian goals;
- Minecraft/Cobblemon/Craftics adapter/playback.

REDUCED viability:

Viable with current foundations if rehearsal stops, civilians and instruments leave the grid first, no unverified Musician/Sonic effects are used and AutoPTU receives a conventional static arena.

### Missing Archive Recording — FULL

Predominantly overworld.

VERIFIED combat foundations are sufficient for an optional conventional confrontation.

BLOCKING only if the intended version requires:

- live pursuit/escort under complete movement;
- non-KO preserve/recover policy under tactical AI;
- semantic custody/object playback in Minecraft.

REDUCED viability:

High. Resolve provenance/custody outside battle, secure the recording outside the grid and use a static encounter only if conflict remains.

### Bridge Ensemble Night — FULL

Predominantly overworld and currently highly viable.

Dependencies:

- Soundscapes for acoustic observations;
- Diel Activity for time-linked wildlife observations;
- Music layer for ensemble/repertoire state;
- battle capabilities only if a real confrontation occurs.

Actual Musician/Sonic mechanics remain dependent on PARTIAL move/Ability/Feature families and specific Java parity.

REDUCED viability:

Very high. Keep the entire music/ecology investigation outside combat and use a standard static battle only if independently justified.

### Music Club Gym Showcase — FULL

VERIFIED foundations:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL as actually invoked:

- lifecycle;
- damage;
- statuses;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks, including Musician-specific uncertainty.

BLOCKING:

- audience/civilian movement;
- dynamic stage zones/hazards/reactions;
- venue-specific non-KO tactical policy;
- adapter/playback.

REDUCED viability:

Clear the audience/stage perimeter and run the formal battle normally. Musical accompaniment remains nonmechanical presentation. Record battle result, musical performance and audience reception separately.

## Promotion decision

No permanent category is promoted in Pass 103.

The latest Java commit materially strengthens `Trainer Features / perks` infrastructure by freezing generic context-gate behavior against Python, on top of the immediately preceding prerequisite-gate slice. The family remains PARTIAL because context/prerequisite selection is not complete execution and the implementation explicitly leaves frequency/cooldowns, resources/AP, usage mutation, target scopes and effect application to separate contracts.

For music specifically, no concrete Java Musician/Song implementation was surfaced. Therefore any mechanically meaningful Musician build or encounter remains gated on exact class-specific parity rather than generic Feature infrastructure.

The music-culture layer itself can advance extensively as overworld state today. Works, versions, ensembles, instruments, rehearsals, recordings, archives, oral transmission and public memory do not require the battle engine to pretend ordinary sound is a PTU mechanic.