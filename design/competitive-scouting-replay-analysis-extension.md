# Competitive Scouting, Replay Analysis & Preparation Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already has formal battle records, challenge contracts, recurring peers, public media, visual evidence and personal notes. This extension connects those systems through one narrow responsibility: represent what a Trainer, coach, rival, analyst or institution can legitimately learn from prior battles, how that information was obtained, how it becomes stale, and how later preparation may reference it without reading hidden world truth.

This layer does not own battle results, relationship state, replay media assets, progression or tactical AI. It produces bounded knowledge inputs that those systems may reference.

## 1. Core invariant

Competitive preparation follows evidence.

```text
authoritative battle/result
        ↓
reveal or public-result event
        ↓
recording / witness / report / publication
        ↓
observer actually receives source
        ↓
scouting observation
        ↓
analysis claim
        ↓
legal preparation through governing systems
        ↓
future encounter knowledge packet
```

No step may be skipped merely because the complete opponent state exists in the database.

## 2. Source record

```yaml
scouting_source:
  scouting_source_id: null
  source_kind: LIVE_WITNESS | OFFICIAL_REPLAY | PUBLIC_BROADCAST | AUTHORIZED_PRIVATE_REVIEW | RESULT_SUMMARY | MEDIA_REPORT | PERSONAL_REPORT | RUMOR
  underlying_ref: null
  created_at: null
  battle_ref: null
  event_ref: null
  publisher_or_witness_id: null
  access_policy_ref: null
  available_from: null
  available_until: null
  completeness: FULL | PARTIAL | SUMMARY | UNKNOWN
  integrity_state: PRIMARY | DOCUMENTED_DERIVATIVE | UNVERIFIED_COPY | UNKNOWN
  provenance_refs: []
```

The `underlying_ref` points to the owning system:
- visual replay -> Photography/Visual Evidence;
- broadcast/report -> Media/Communications;
- official battle result -> Battle Institutions;
- private notebook -> Personal Records;
- rumor -> Rumor/Testimony.

This extension never creates a second copy of the source object.

## 3. Observer access event

Availability and knowledge are separate.

```yaml
scouting_access_event:
  access_event_id: null
  scouting_source_id: null
  observer_id: null
  accessed_at: null
  access_mode: LIVE | VIEWED | READ | RECEIVED | BRIEFED | OTHER
  authorized: true
  viewed_extent: COMPLETE | PARTIAL | UNKNOWN
  notes_ref: null
```

A public replay that exists online is not automatically known by every rival.

An NPC can only use that replay later if the world state establishes that they viewed it, received a briefing derived from it, or otherwise gained access through an approved route.

## 4. Reveal entries

Scouting should store the strongest fact actually supported by the source.

```yaml
battle_reveal_entry:
  reveal_id: null
  subject_actor_id: null
  subject_pokemon_id: null
  battle_ref: null
  source_ref: null
  observed_at: null
  reveal_kind: SPECIES_SEEN | FORM_SEEN | MOVE_CONFIRMED | EFFECT_OBSERVED | ABILITY_CONFIRMED | ITEM_CONFIRMED | TRAINER_FEATURE_CONFIRMED | SWITCH_PATTERN_OBSERVED | POSITIONING_PATTERN_OBSERVED | OBJECTIVE_BEHAVIOR_OBSERVED | ARENA_INTERACTION_OBSERVED | OTHER
  authoritative_event_ref: null
  observation_description: null
  mechanical_identity_ref: null
  certainty: CONFIRMED | SUPPORTED | UNCERTAIN
  public_visibility: PUBLIC | RESTRICTED | PRIVATE | UNKNOWN
  superseded_by: null
```

### Confirmed mechanical identity

`MOVE_CONFIRMED`, `ABILITY_CONFIRMED`, `ITEM_CONFIRMED` or `TRAINER_FEATURE_CONFIRMED` requires one of:
- an authoritative AutoPTU semantic event that exposes the identity;
- an official battle record that explicitly publishes it;
- explicit public disclosure from the actor/institution;
- another reviewed mechanical reveal source.

A visual effect alone should normally become `EFFECT_OBSERVED`.

Example:

A spectator sees a Pokémon pushed backward after an attack. That can establish displacement occurred in the visible battle. It does not identify the exact Move, Ability or Feature unless the authoritative reveal path supports that identity.

## 5. Analysis claim

Observation and interpretation stay separate.

```yaml
scouting_analysis_claim:
  analysis_claim_id: null
  analyst_id: null
  subject_id: null
  created_at: null
  source_reveal_refs: []
  claim_text: null
  claim_tags: []
  confidence_band: LOW | MEDIUM | HIGH | REVIEWED
  contradiction_refs: []
  stale_after_event_refs: []
  status: ACTIVE | CHALLENGED | SUPERSEDED | RETIRED
```

Candidate `claim_tags`:
- opening-pattern;
- switching-tendency;
- positioning-tendency;
- common-partner;
- revealed-response;
- resource-use-pattern;
- arena-preference;
- objective-priority;
- unknown.

These tags do not directly modify AI weights or combat math.

## 6. Staleness model

Historical information remains historically true while becoming less predictive.

```yaml
scouting_staleness:
  reveal_or_claim_ref: null
  subject_change_refs: []
  age_band: CURRENT | RECENT | OLD | UNKNOWN
  predictive_status: PLAUSIBLY_CURRENT | POSSIBLY_STALE | KNOWN_SUPERSEDED | HISTORICAL_ONLY
  reviewed_at: null
```

Potential staleness triggers:
- publicly observed evolution;
- roster change;
- new public battle;
- changed institution role;
- changed challenge contract;
- new season;
- explicit statement that an old strategy was abandoned;
- a Move/Ability/Item/Feature change proven by authoritative state and publicly revealed later.

Staleness never deletes the original battle record.

## 7. Knowledge packet for an encounter

Before an opponent or autonomous Trainer enters a battle, Ouros can compile a bounded packet.

```yaml
competitive_knowledge_packet:
  packet_id: null
  observer_actor_id: null
  target_actor_ids: []
  target_pokemon_ids: []
  generated_at: null
  direct_battle_refs: []
  accessible_source_refs: []
  confirmed_reveal_refs: []
  analysis_claim_refs: []
  stale_information_refs: []
  rumor_refs: []
  current_encounter_visible_facts: []
  explicitly_disclosed_facts: []
  private_unknown_fields: []
  allowed_ai_policy_ref: null
  provenance_refs: []
```

This packet is the maximum competitive history that an approved tactical AI may consume.

Hard rule:

The AI must not query the full player Trainer record, complete roster, hidden Moves, held items, Features, inventory or future choices simply because those objects exist server-side.

## 8. Current-encounter facts are different from prior scouting

Once a battle begins, AutoPTU may reveal new information through legal tactical events.

The packet should distinguish:
- what the opponent knew before battle;
- what becomes visible during the current battle;
- what remains unknown.

This matters for tests and post-battle history.

An AI that sees a Move used on turn 4 may react afterward if its eventual policy permits that. It may not act on that Move during turn 1 unless the knowledge packet already contained a valid prior reveal.

## 9. Replay publication contract

Formal battles may optionally create a replay projection.

```yaml
battle_replay_publication:
  publication_id: null
  authoritative_battle_ref: null
  visual_record_ref: null
  publisher_id: null
  publication_scope: PUBLIC | PARTICIPANTS | INSTITUTION_ONLY | RESTRICTED
  published_at: null
  withdrawn_at: null
  redaction_refs: []
  commentary_ref: null
  version_ref: null
```

Battle Institutions owns whether a match permits or requires replay publication.
Photography/Visual Evidence owns the actual primary or derivative visual record.
Media owns broadcasts/commentary.
This extension only makes those sources usable for competitive knowledge.

## 10. Public result without replay

Ouros must support formal battles where only limited information becomes public.

Example public record:
- participants;
- winner/draw/withdrawal;
- event/format;
- qualification consequence;
- explicitly published roster members.

No turn history is inferred.

This supports institutions with different disclosure policies without inventing universal broadcast norms.

## 11. Commentary can be wrong

A commentator, journalist or analyst can misidentify what happened.

Store:
- authoritative reveal entry;
- commentary claim;
- later correction if any.

Do not mutate the battle transcript to match the commentary.

This creates useful narrative callbacks where the public narrative around a match differs from the tactical record.

## 12. Preparation plan

Scouting can motivate legal world-state actions.

```yaml
competitive_preparation_plan:
  plan_id: null
  actor_id: null
  target_event_ref: null
  source_claim_refs: []
  planned_actions: []
  started_at: null
  completed_action_refs: []
  unresolved_actions: []
  mechanics_review_required: true
```

Possible narrative actions:
- review public footage;
- ask a coach to discuss an observed pattern;
- practice a legal movement concept;
- select among Pokémon already legally available to the Trainer;
- request a permitted exhibition/scrimmage;
- learn the public arena rules;
- acquire an allowed item through normal world systems;
- schedule ordinary training under governing progression rules.

The plan itself grants no bonus.

## 13. Mock-opponent profile

A replay-derived practice opponent must be kept separate from the real actor.

```yaml
mock_opponent_profile:
  mock_profile_id: null
  based_on_actor_id: null
  source_battle_refs: []
  source_reveal_refs: []
  generated_at: null
  synthetic_roster_ref: null
  synthetic_policy_ref: null
  known_limitations: []
  writeback_to_real_actor: false
  formal_record_eligible: false
```

The synthetic profile may only contain data legitimately exposed by its source plus explicitly approved simplifications.

A mock battle cannot:
- reveal private current state;
- change the real actor's record;
- count as defeating the real actor;
- create a rivalry event with the real actor unless a separate social event actually occurs;
- certify how the real actor will behave later.

## 14. Overfitting is narratively useful

Scouting should be capable of being wrong without a random hidden deception system.

Examples:
- analyst has only one match;
- footage is old;
- opponent intentionally chose an unusual legal roster for that event;
- arena conditions shaped behavior;
- commentary omitted relevant turns;
- a tactic was situational rather than habitual.

The failure is explained through evidence provenance, not an invisible “scouting accuracy” roll.

## 15. Rival integration

`rivalry-recurring-peer-progression-extension.md` remains owner of recurring competitive continuity.

This layer supplies references such as:
- sources the rival actually watched;
- confirmed reveals;
- stale information;
- analyst notes;
- preparation plans.

A rival may choose a different legal roster because of confirmed public information if the roster choice itself is allowed by the governing encounter/challenge contract.

That still does not permit hidden counter-picking.

## 16. Battle institution integration

Battle Institutions remains owner of:
- challenge contracts;
- replay/public-record policy;
- qualification;
- formal results;
- venue rules;
- rematch policy.

Potential institution roles around scouting:
- archive public matches;
- provide a review room;
- publish only summary results;
- provide analysts to trainees;
- restrict footage for privacy or competitive integrity;
- run reviewed mock battles.

None of these roles are Ouros canon until approved.

## 17. Photography, media and personal-record integration

Photography/Visual Evidence owns:
- video source;
- capture metadata;
- derivatives;
- integrity;
- framing/coverage limitations.

Media owns:
- broadcast;
- commentary;
- publication framing;
- corrections.

Personal Records owns:
- private coach notebook;
- Trainer's own review notes;
- private correspondence about a match.

This extension owns only the competitive interpretation link.

## 18. Privacy and access

Ouros currently has no universal canon policy saying every formal battle is public footage.

Every source should therefore have explicit access state.

Do not infer access from:
- fame;
- rivalry;
- institutional membership alone;
- server administrator visibility;
- proximity to a Minecraft replay screen;
- possession of the complete AutoPTU transcript in backend storage.

## 19. PTU/Caelo boundary

This layer creates no new mechanical benefit from preparation.

It must not invent:
- a Scouting skill;
- an automatic Accuracy bonus;
- a damage bonus against a studied opponent;
- a free Move change;
- a free Tutor Move;
- a free Edge/Feature;
- a reroll from replay review;
- a hidden weakness tag;
- a rival adaptation modifier;
- a prediction action;
- special item access;
- roster legality rules.

Any mechanical preparation effect must be validated against the project's PTU/Caelo source set and implemented authoritatively in AutoPTU.

## 20. AutoPTU AI contract

The intended future tactical integration is:

```text
Ouros competitive_knowledge_packet
        + current AutoPTU-visible battle facts
        + approved AI policy
                 ↓
AutoPTU tactical decision
```

The AI policy remains mechanically authoritative inside AutoPTU.

Minecraft/Cobblemon must not:
- inspect its own battle-state representation to decide what the NPC knows;
- add hidden information;
- choose a counter because a visual entity exposes backend data;
- modify the knowledge packet.

## 21. Cobblemon reuse profile

This system should reuse Cobblemon heavily where safe.

SAFE_REUSE candidates:
- Pokémon models/forms/textures for replay presentation;
- battle-adjacent animations, poses, cries and particles;
- UI screens, menus and controls for viewing analysis;
- networking and client synchronization;
- player/NPC/Pokémon overworld entities around review rooms;
- blocks, seats, screens, projectors or display props where available;
- timestamps/world locations as contextual metadata;
- interaction hooks;
- storage hooks for references to Ouros-owned replay records.

ADAPTER_REQUIRED:
- playing an AutoPTU semantic replay through Cobblemon/Minecraft entities;
- mapping a visible replay frame to authoritative reveal events;
- converting player notes into Ouros analysis claims;
- rebuilding playback after reconnect/chunk reload;
- presenting current-versus-historical roster information without leaking private state.

BATTLE_AUTHORITY_FORBIDDEN:
- Cobblemon deciding what Move/Ability/Item/Feature was mechanically used;
- Cobblemon deciding the historical HP/status/position truth;
- Cobblemon choosing combatants in a replay or rematch;
- Cobblemon's own AI model being treated as the real opponent's tactical history;
- Cobblemon battle state supplying hidden facts to an analyst or AI.

## 22. Mechanically rich encounter concept — Scouted Rematch

Intended full version:

A recurring opponent has watched specific public matches. Their tactical AI receives only the compiled competitive knowledge packet plus facts revealed during the current fight. The opponent can recognize previously confirmed patterns but still acts through legal AutoPTU choices and an approved tactical policy.

Required capability families:
- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement where the selected roster needs it;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- terrain/weather/hazards/zones/reactions only if the approved arena uses them;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks;
- AI legal-action infrastructure;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Reduced version:

Compile the same legal scouting packet, but do not claim dynamic tactical adaptation. A reviewed static opponent roster and existing legal-action path are selected before battle. The narrative can say the opponent prepared for publicly observed information only when that preparation is reflected by legal authoritative state. AutoPTU then resolves an ordinary approved battle. The packet is preserved for future use.

## 23. Mechanically rich encounter concept — Analysis Between Rounds

Intended full version:

An invitational uses several separate matches or rounds. Between them, participants may review public footage from earlier rounds. New confirmed reveals become available only after publication and access. Later AI policy can incorporate those reveals.

Potential dependencies:
- full turn/round lifecycle;
- semantic BattleTranscript/reveal events;
- move/ability/item/Feature coverage;
- AI tactical policy;
- adapter/playback;
- any arena-specific movement/environment families.

Reduced version:

Use separate ordinary battles with an overworld checkpoint between them. After each match, Ouros records only authoritative public reveals. The next opponent may receive a curated reviewed static preparation profile. No mid-battle AI learning is claimed.

## 24. Noncombat encounter — Film Review Disagreement

Two analysts review the same public replay and disagree about why a turning point occurred.

Gameplay can use:
- source provenance;
- replay coverage;
- authoritative reveal events;
- analyst claims;
- commentary corrections;
- later comparison against another battle.

No battle capability family is required unless a separate scrimmage is launched.

This is executable before the tactical AI adapter exists.

## 25. Post-battle writeback

After an authoritative battle, this layer may receive:
- public result ref;
- replay publication ref;
- mechanically revealed Move/Ability/Item/Feature refs;
- visible participant refs;
- observed tactical pattern candidates;
- spectator/witness refs.

It must not infer:
- unrevealed loadout;
- unused Moves;
- hidden items;
- unused Features;
- current future roster;
- private training choices;
- private emotions.

## 26. Implementation tests to require later

Once the relevant AI/adapter exists, tests should prove:
- AI cannot query unrevealed opponent Moves;
- an old replay does not update itself when the real Trainer changes roster;
- current-battle reveals become available only after their event occurs;
- a public summary without replay does not expose hidden turns;
- commentary mislabeling does not change authoritative identity;
- a mock opponent cannot write battle results to the real actor;
- a private replay cannot enter another actor's packet without an access event;
- Cobblemon battle-state objects cannot populate the packet;
- reconnect/replay rebuilding cannot add extra reveals;
- two observers with different source histories can enter the same battle with different legal knowledge.

## 27. Canon review questions

Before any setting details are promoted, decide:
- which Ouros institutions publish battle replays;
- whether replay technology is common, regional or institution-specific;
- what information formal result records expose;
- whether spectators may record events independently;
- what privacy restrictions exist;
- whether analyst/coaching roles are institutionally common;
- how long public footage remains accessible;
- whether any circuits permit mock-opponent simulations;
- which information an official opponent is permitted to use when preparing for challengers.

None of these questions is answered automatically by this extension.
