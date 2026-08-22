# Ouros Music Traditions, Ensembles, Repertoire & Recordings Layer

Status: proposed systems architecture. Not established Ouros canon.

## Purpose

Ouros needs music to exist as durable culture rather than only as background audio, Contest content or a combat class. This layer models compositions, arrangements, regional variants, ensembles, instruments, rehearsals, recordings, archives and transmission across generations.

It complements:
- Contest/Performance, which owns formal performance events and career-facing show state;
- Soundscapes, which owns emitted sound and acoustic observation;
- Festivals, which owns recurring observances and editions;
- Archives, which owns institutional preservation/custody;
- Media, which owns publication/distribution;
- Education and Social Bonds, which own teaching relationships and consent-sensitive interpersonal state;
- Material Culture, which owns physical instrument instances and provenance;
- PTU/AutoPTU, which owns any actual Musician/Sonic mechanics.

## Core separation

Keep these states distinct:

```text
musical work identity
→ composition/authorship claims
→ arrangement/version
→ repertoire membership
→ ensemble rehearsal
→ performance event
→ recording/documentation
→ archive/publication
→ public memory
→ any authoritative PTU mechanical effect
```

A performance is one realization of a work, not the work itself.

A recording preserves one performance, not a universal correct version.

A regional variant can be legitimate without being older.

A famous performer does not automatically own or compose the music they perform.

A song about a historical event is not evidence that the event occurred as described.

## 1. Musical work

```yaml
musical_work:
  work_id: null
  working_title: null
  title_history: []
  work_type: null
  known_origin_window: null
  origin_location_claim_ids: []
  authorship_claim_ids: []
  transmission_mode_tags: []
  associated_tradition_ids: []
  associated_institution_ids: []
  sacred_or_restricted_access_ref: null
  source_refs: []
```

Possible work types:
- SONG
- INSTRUMENTAL_PIECE
- DANCE_MUSIC
- PROCESSIONAL
- WORK_SONG
- LULLABY
- CHILDREN_SONG
- SIGNAL_TUNE
- CHANT
- ENSEMBLE_SUITE
- IMPROVISATION_FRAMEWORK
- UNKNOWN

The type is descriptive. It does not define mechanics.

## 2. Authorship and origin claims

```yaml
music_origin_claim:
  claim_id: null
  work_id: null
  claim_type: null
  claimed_creator_ids: []
  claimed_location_id: null
  claimed_date_window: null
  claimant_id: null
  evidence_refs: []
  contradicting_refs: []
  confidence: null
  status: PROPOSED
```

Candidate claim types:
- COMPOSED_BY
- COLLECTIVE_ORIGIN
- ADAPTED_FROM
- FIRST_RECORDED_AT
- FIRST_DOCUMENTED_BY
- TRADITIONAL_UNATTRIBUTED
- LOCAL_ORIGIN_STORY

Do not force one definitive author when evidence is incomplete.

## 3. Arrangement / version

```yaml
music_version:
  version_id: null
  work_id: null
  version_type: ARRANGEMENT
  creator_or_editor_ids: []
  created_window: null
  region_id: null
  instrumentation_profile_id: null
  tempo_or_form_notes: []
  textual_or_language_variant_ref: null
  performance_practice_notes: []
  source_version_ids: []
  evidence_refs: []
  source_refs: []
```

Version types can include:
- ARRANGEMENT
- REGIONAL_VARIANT
- TRANSLATION
- REVIVAL_RECONSTRUCTION
- REDUCED_ENSEMBLE_VERSION
- CEREMONIAL_VERSION
- CHILDREN_VERSION
- RADIO_EDIT
- ARCHIVAL_TRANSCRIPTION
- UNKNOWN_VARIANT

A version may remain related to the same `work_id` even when several elements change.

If relationship is uncertain, store a `related_work_hypothesis` rather than forcing shared identity.

## 4. Musical tradition

```yaml
music_tradition:
  tradition_id: null
  region_or_community_refs: []
  recognized_by_refs: []
  repertoire_ids: []
  transmission_practices: []
  performance_contexts: []
  instrument_family_refs: []
  access_practice_ref: null
  continuity_notes: []
  change_history_refs: []
  source_refs: []
```

A tradition is living state.

It can:
- add new repertoire;
- lose repertoire;
- revive older works;
- change instrumentation;
- split into regional schools;
- merge influences;
- become less relevant;
- be maintained privately;
- become public later;
- stop being practiced.

Do not assign an `authenticity_score`.

## 5. Repertoire

```yaml
repertoire:
  repertoire_id: null
  owner_or_steward_refs: []
  work_or_version_ids: []
  usage_contexts: []
  active_from: null
  active_until: null
  public_access_state: null
  teaching_state: null
  notes: []
```

A repertoire can belong to:
- an ensemble;
- a venue;
- a school;
- a ceremony;
- a town tradition;
- one performer;
- a broadcaster;
- an archive program.

Repertoire membership is not ownership of copyright or legal rights unless future canon defines those systems.

## 6. Ensemble identity

```yaml
music_ensemble:
  ensemble_id: null
  public_name: null
  founded_at: null
  dissolved_at: null
  home_location_id: null
  institution_ref: null
  member_history_refs: []
  pokemon_member_history_refs: []
  repertoire_id: null
  rehearsal_site_ids: []
  performance_event_refs: []
  recording_refs: []
  public_reputation_refs: []
  source_refs: []
```

Membership history is append-only.

A lineup change does not create a new ensemble unless identity actually changes.

A Pokémon participating repeatedly may have a role without becoming owned by the ensemble.

## 7. Ensemble membership

```yaml
ensemble_membership:
  membership_id: null
  ensemble_id: null
  actor_id: null
  role_tags: []
  began_at: null
  ended_at: null
  consent_or_authorization_ref: null
  instrument_instance_ids: []
  repertoire_scope: []
  public_credit_state: null
  notes: []
```

Possible role tags:
- VOCAL
- RHYTHM
- MELODY
- BASS
- PERCUSSION
- CONDUCTOR
- ARRANGER
- COMPOSER
- TECHNICIAN
- ROAD_CREW
- APPRENTICE
- GUEST
- POKEMON_PARTNER

Role tags have no PTU combat meaning.

## 8. Instrument profile and physical instances

Instrument design belongs partly to Material Culture.

```yaml
instrument_profile:
  profile_id: null
  instrument_family: null
  regional_variant_ref: null
  construction_tradition_ref: null
  typical_material_refs: []
  normal_performance_contexts: []
  source_refs: []
```

```yaml
instrument_instance:
  instrument_id: null
  profile_id: null
  material_instance_refs: []
  maker_id: null
  created_at: null
  owner_claim_ref: null
  custody_ref: null
  condition_ref: null
  modification_history: []
  performance_history_refs: []
  source_refs: []
```

An instrument can be repaired, loaned, inherited, modified or archived while retaining identity.

Do not give instruments Weapon stats, Sonic keywords or combat bonuses unless exact PTU/Caelo definitions exist.

## 9. Rehearsal state

```yaml
music_rehearsal:
  rehearsal_id: null
  ensemble_or_actor_refs: []
  work_version_ids: []
  location_id: null
  scheduled_at: null
  completed_at: null
  attendance_refs: []
  timing_observations: []
  role_fit_observations: []
  equipment_issue_refs: []
  pokemon_comfort_observations: []
  arrangement_change_refs: []
  unresolved_questions: []
```

Rehearsal reveals information.

It does not automatically award:
- Skill ranks;
- AP;
- Combat Stages;
- Accuracy;
- Contest dice;
- Friendship/Loyalty;
- Musician Song effects;
- temporary HP;
- damage bonuses.

## 10. Musical performance reference

Formal event scheduling remains under Contest/Performance or Festivals.

This layer stores what musical material was realized:

```yaml
music_performance_ref:
  performance_ref_id: null
  event_id: null
  ensemble_or_performer_ids: []
  work_version_ids: []
  actual_lineup_refs: []
  actual_instrument_refs: []
  started_at: null
  ended_at: null
  deviations_from_plan: []
  recording_ids: []
  reception_refs: []
```

A battle inside a music club may coexist with musical accompaniment, but accompaniment is presentation unless an exact mechanic is invoked.

## 11. Music recording

```yaml
music_recording:
  recording_id: null
  captured_performance_ref: null
  recorded_at: null
  location_id: null
  recorder_actor_or_device_ref: null
  medium_type: null
  source_quality_notes: []
  performer_credit_refs: []
  work_version_hypotheses: []
  custody_ref: null
  archive_ref: null
  access_state: null
  publication_state: null
  derivative_recording_ids: []
  source_refs: []
```

A recording can be:
- authentic but miscataloged;
- incomplete;
- edited;
- copied;
- restored;
- private;
- public;
- missing provenance;
- attributed to the wrong ensemble;
- one of several versions of the same performance.

## 12. Field recording as evidence

A musical recording may later support other systems.

Potential handoffs:
- Soundscapes: machine hum or wildlife call in the background;
- Diel Activity: time-of-day activity evidence;
- Photography/Visual Evidence: synchronized footage;
- Archives: custody, catalog and access;
- Language: dialect or text variant;
- Public Memory: old civic events;
- Architecture: acoustic evidence of a lost space only as an interpretation;
- Cases: timestamp or actor-presence evidence when provenance supports it.

Never treat audio as omniscient truth.

## 13. Oral transmission and apprenticeship

```yaml
music_transmission_event:
  transmission_id: null
  teacher_or_source_refs: []
  learner_refs: []
  work_version_ids: []
  transmission_mode: null
  location_id: null
  date_window: null
  notation_or_recording_refs: []
  learner_version_ref: null
  consent_or_access_ref: null
  notes: []
```

Transmission modes can include:
- ORAL_AURAL
- NOTATED
- DEMONSTRATION
- RECORDING_LED
- GROUP_REHEARSAL
- INFORMAL_FAMILY
- SCHOOL
- APPRENTICESHIP

Do not infer family relation from informal transmission.

## 14. Regional variation without purity scoring

A musical work may have several long-lived variants.

Store:
- what differs;
- who performs each version;
- where and when each is documented;
- how performers describe the relationship;
- whether scholars agree;
- what older recordings show.

Do not rank variants as more authentic merely because one is older.

## 15. Sacred, private and restricted music

The Myth/Sacred Sites and Credentials layers govern access and authority.

Possible state:
- PUBLIC;
- COMMUNITY_ONLY;
- CEREMONY_ONLY;
- APPRENTICE_ONLY;
- ARCHIVE_RESTRICTED;
- PRIVATE_RECORDING;
- UNKNOWN_ACCESS_PRACTICE.

Generation must never expose restricted material just because it exists in a database.

A player discovering a recording does not automatically gain permission to publish it.

## 16. Pokémon musical participation

Keep these separate:

```text
species known for sound behavior
individual observed making sound
individual voluntarily participating
ensemble membership
ownership/custody
PTU Musician/Sonic mechanics
```

Examples of legal narrative state:
- a Toxtricity repeatedly joins rehearsals;
- a wild Pokémon answers a tune from outside the venue;
- an institutional Pokémon participates in ceremonies;
- an old partner refuses a performance it previously joined;
- an ensemble adapts after a Pokémon migrates.

Do not infer obedience, ownership, emotion or mechanical Song use.

## 17. Song/text claims

Lyrics or song narratives can preserve memory, myth, propaganda, humor or misunderstanding.

```yaml
song_content_claim:
  claim_id: null
  work_version_id: null
  depicted_or_asserted_fact: null
  claim_context: null
  evidence_relation: null
  interpretation_refs: []
```

A song describing a flood does not prove the flood happened exactly that way.

The content may still be useful historical evidence about what people believed or remembered.

## 18. Public circulation

Media/Communications owns circulation events.

This layer stores the musical object being circulated.

Possible paths:
- live local performance;
- radio broadcast;
- archived recording;
- touring ensemble;
- school transmission;
- festival edition;
- public-space informal performance;
- commercial release if future canon defines such systems.

Popularity does not equal quality, ownership or cultural authority.

## 19. Minecraft projection

Minecraft may represent:
- rehearsal rooms;
- stages;
- music halls;
- street performers;
- instrument props/models;
- archives/listening rooms;
- posters and schedules;
- representative audience NPCs;
- semantic currently-playing state;
- original authorized audio assets;
- subtitles/captions or equivalent cues.

Minecraft must not:
- use copyrighted external tracks as Ouros music;
- infer mechanics from audio playback;
- grant buffs because a sound is playing;
- make volume determine Sonic Move range;
- expose private/restricted recordings;
- treat a client-side audio mod as world truth.

## 20. Accessibility

Musical content cannot rely only on hearing.

Important information should have equivalent representation through:
- captions;
- performer animation;
- visual beat/rhythm cues;
- text summaries;
- waveform or pattern display when relevant;
- event logs;
- accessible UI labels.

Accessibility options change presentation, not character identity or in-world hearing state.

## 21. PTU / AutoPTU authority boundary

PTU 1.05 contains a real Musician class and explicit Musician Songs. Those mechanics are not simulated here.

Any encounter that invokes actual:
- Musician Songs;
- Sonic Move interactions;
- Sing/Supersonic/Hyper Voice/Perish Song;
- Drown Out;
- Soundproof;
- Voice Lessons;
- other Musician Features;

must validate the exact PTU/Caelo definition and current Java implementation.

Current evidence:
- Python has structured Musician data in Trainer-class catalogs;
- current Java search did not surface concrete Musician/Song implementations;
- Java has generic Trainer Feature prerequisite/context infrastructure, but not proof of complete Musician execution.

Therefore Trainer Features/perks remains PARTIAL and Musician-specific mechanical execution remains unverified.

## 22. Encounter implementation contracts

### A. Rehearsal Hall Interruption

Narrative premise:

A community ensemble is rehearsing a revived regional work when an external disturbance forces the building to clear. The objective is preserving people, instruments and continuity of the event, not protecting an abstract HP bar for music.

FULL dependencies:
- targeting/footprints/range/LoS — VERIFIED foundation;
- base movement legality — VERIFIED foundation;
- core calculations — VERIFIED foundation;
- action economy/initiative — VERIFIED foundation;
- AI legal-action infrastructure — VERIFIED foundation;
- full turn/round lifecycle — PARTIAL if mechanical Musician effects are used;
- move-specific behavior — PARTIAL if Sonic Moves are used;
- abilities — PARTIAL for Soundproof/Drown Out-like interactions where applicable;
- Trainer Features/perks — PARTIAL and specifically unverified for Musician Songs;
- complete movement/interception/forced movement — BLOCKING for in-grid evacuation;
- terrain/weather/hazards/zones/reactions — BLOCKING for interactive stage hazards;
- AI tactical policy — BLOCKING for PROTECT_EXIT/WITHDRAW/AVOID_CIVILIANS;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

Rehearsal stops. Civilians and instruments clear before battle. Any Musician Songs remain unavailable unless separately verified. AutoPTU receives a normal static arena. The rehearsal and instrument custody resume afterward through world state.

### B. Missing Archive Recording

Narrative premise:

An archival recording believed to preserve a rare regional arrangement is missing from its expected storage location. Investigation crosses archive, former performers and duplicate-copy provenance.

FULL dependencies:

Predominantly overworld. If conflict occurs:
- targeting/LoS — VERIFIED;
- base movement — VERIFIED;
- calculations — VERIFIED;
- initiative — VERIFIED;
- legal-action infrastructure — VERIFIED;
- complete movement — BLOCKING only for pursuit/escort variants;
- tactical AI — BLOCKING for non-KO recovery objectives;
- adapter/playback — BLOCKING for semantic object custody in battle.

REDUCED version:

Resolve archive provenance and custody outside battle. If confrontation occurs, secure the recording outside the grid and run a conventional static battle. Battle outcome cannot silently transfer ownership or erase evidence.

### C. Bridge Ensemble Night

Narrative premise:

Several local musicians build a layered public arrangement at a bridge. One expected performer is absent and a recurring wild Pokémon sound is also missing. The same absence may have separate social and ecological explanations.

FULL dependencies:
- no special battle dependency unless a confrontation actually occurs;
- Soundscapes and Diel Activity provide overworld evidence;
- AI tactical policy and complete movement become relevant only if wildlife withdrawal is simulated during combat;
- actual Sonic/PTU Musician mechanics require move/ability/Feature verification.

REDUCED version:

The music scene is entirely overworld. Players investigate ensemble attendance and acoustic ecology separately. Optional combat remains conventional and static.

### D. Music Club Gym Showcase

Narrative premise:

A battle institution hosts a public music night in the same venue where formal challenges normally occur. The two systems share space and audience, but not rules.

FULL dependencies:
- static targeting/base movement/core calculations/action economy — VERIFIED foundations;
- full lifecycle/damage/status/moves/abilities/items/Features — PARTIAL as actually invoked by the battle;
- Musician Songs — require exact Feature implementation;
- crowd movement/objectives — BLOCKING;
- tactical AI — BLOCKING for venue-specific non-KO objectives;
- adapter/playback — BLOCKING.

REDUCED version:

Audience and stage are cleared to a safe perimeter. AutoPTU runs the formal battle under its verified/static rules. Musical accompaniment remains nonmechanical presentation. Formal battle results and public music reception are recorded separately.

## 23. New overworld blockers

`MUSICAL_WORK_IDENTITY`
Stable work identity independent of one recording or performance.

`MUSIC_VERSION_GRAPH`
Arrangements, regional variants and reconstructions with source relationships.

`MUSIC_AUTHORSHIP_CLAIMS`
Evidence-backed creator/origin claims without forced certainty.

`MUSIC_TRADITION_STATE`
Living repertoire, practice, access and change history.

`ENSEMBLE_IDENTITY_AND_MEMBERSHIP`
Lineup history, roles and participation without ownership inference.

`INSTRUMENT_INSTANCE_PROVENANCE`
Physical instrument identity, maker/material/custody/repair history.

`MUSIC_REHEARSAL_STATE`
Attendance, timing, comfort, equipment and arrangement decisions.

`MUSIC_RECORDING_PROVENANCE`
Capture context, copies, edits, archive custody, access and publication state.

`MUSIC_TRANSMISSION_GRAPH`
Teacher/source → learner → learned version without assuming exact copying.

`MUSIC_RESTRICTED_ACCESS`
Private/sacred/community-only material protected from procedural disclosure.

`MUSIC_TO_MEDIA_AND_ARCHIVE`
Publication and preservation handoff without collapsing rights, custody or truth.

`MUSIC_TO_SOUNDSCAPE`
Performance emits sound events, but acoustic behavior remains under Soundscapes.

`MUSIC_TO_MINECRAFT_PROJECTION`
Authorized original audio, semantic playback and accessible cues without client becoming authority.

`MUSIC_TO_BATTLE_SNAPSHOT`
A musical location can freeze a safe arena without importing Musician/Sonic rules.

## 24. Generation guardrails

The generator must not infer:
- class Musician from profession or hobby;
- musical talent from species flavor;
- friendship or romance from duet performance;
- consent from prior participation;
- cultural ownership from popularity;
- authorship from first surviving recording;
- historical truth from lyrics;
- sacred status from age;
- a Sonic keyword from an audible sound;
- Soundproof immunity to ordinary conversation or ambience;
- Musician Song effects from music playback;
- healing from lullabies;
- morale buffs from an anthem;
- crowd control from a conductor;
- instrument-as-weapon behavior;
- loyalty or obedience from repeated rehearsal.

## 25. Canon questions

- Which regions have distinct authored musical cultures before play begins?
- What works are old enough to have uncertain authorship?
- Which traditions are public, restricted, sacred or private?
- Which ensembles and venues exist at launch?
- Which instruments are locally manufactured?
- What music technology exists: acoustic only, amplified, recorded, radio, digital?
- Which Pokémon participate institutionally or voluntarily in music?
- How are player-composed works persisted and moderated?
- How does multiplayer handle private rehearsals and unpublished recordings?
- Which Musician Features/Songs are enabled by PTU/Caelo canon?
- Which are implemented in Python runtime versus only cataloged?
- What Java slices are required before an actual Musician battle build is trustworthy?
