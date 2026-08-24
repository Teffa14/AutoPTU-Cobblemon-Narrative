# Ouros Oral History, Interviews, Witness Memory & Testimony Layer

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.

## Purpose

Ouros already preserves records, evidence, public memory, translations, identities and research permissions. This layer owns the lifecycle of spoken recollection and interview-derived claims.

Its core rule is simple: a person can sincerely remember, repeat, reinterpret, correct, restrict or forget information without the narrative engine rewriting the event that originally occurred.

The layer separates:

world event -> narrator experience -> later recollection -> interview context -> recording -> transcript/translation -> claim extraction -> corroboration -> institutional/public use.

No stage automatically proves the next.

## Authority boundaries

Archives owns long-term preservation and collection state.

Cases owns evidentiary use, custody and investigative hypotheses.

Public Memory owns broad public narratives and reputation effects.

Languages owns language, transcription/translation relationships and terminology.

Research Ethics owns permission for research interviews and secondary use.

Identity owns persistent actor identity and aliases.

Media owns publication/broadcast.

This layer owns the interview/recollection object, provenance and version history.

## Interview record

```yaml
interview_record:
  interview_id: null
  narrator_actor_id: null
  interviewer_actor_ids: []
  interview_context: null
  project_or_case_refs: []
  occurred_at: null
  location_ref: null
  language_refs: []
  recording_ref: null
  permission_ref: null
  access_state: PRIVATE
  session_number: 1
  prior_interview_ids: []
  subsequent_interview_ids: []
  interruption_refs: []
  notes_ref: null
  canon_status: proposed
```

Suggested contexts:
- ORAL_HISTORY
- WITNESS_INTERVIEW
- INCIDENT_DEBRIEF
- PUBLIC_INTERVIEW
- RESEARCH_INTERVIEW
- FAMILY_OR_COMMUNITY_HISTORY
- PROFESSIONAL_RECOLLECTION
- ARCHIVAL_INTERVIEW
- INFORMAL_RECOLLECTION

Context does not create truth or authority.

## Recollection claim

```yaml
recollection_claim:
  recollection_claim_id: null
  interview_id: null
  narrator_actor_id: null
  source_span_ref: null
  claim_type: null
  subject_refs: []
  asserted_time_ref: null
  asserted_location_ref: null
  asserted_event_ref: null
  certainty_as_expressed: null
  memory_access_state: RECALLED
  directness: FIRSTHAND
  prompted_by_ref: null
  correction_of_claim_id: null
  superseded_by_claim_id: null
  access_restrictions: []
```

Possible directness values:
- FIRSTHAND
- HEARD_FROM_PARTICIPANT
- HEARD_FROM_NONPARTICIPANT
- INHERITED_TRADITION
- INSTITUTIONAL_RETELLING
- SOURCE_UNCLEAR

Possible memory access states:
- RECALLED
- PARTIAL
- UNCERTAIN
- DOES_NOT_RECALL
- DECLINES_TO_ANSWER
- INTERRUPTED
- NOT_ASKED

These must not collapse into one another.

## Recording and transcript graph

```yaml
interview_recording:
  recording_id: null
  interview_id: null
  medium: AUDIO
  device_ref: null
  raw_file_ref: null
  start_timestamp_raw: null
  end_timestamp_raw: null
  timekeeping_ref: null
  integrity_ref: null
  preservation_copy_refs: []
  redaction_refs: []
```

```yaml
transcript_revision:
  transcript_id: null
  interview_id: null
  source_recording_id: null
  language_ref: null
  created_by_refs: []
  created_at: null
  method: HUMAN
  correction_refs: []
  narrator_review_state: NOT_REQUESTED
  supersedes_transcript_id: null
  access_state: PRIVATE
```

A transcript is a derivative record. It never replaces the original recording.

A translation is another derivative and must use the Languages layer.

## Narrator permission

Research Ethics controls formal research permission. This layer stores the interview-specific handoff.

```yaml
interview_permission:
  permission_id: null
  narrator_actor_id: null
  interview_id: null
  record_allowed: true
  transcript_allowed: true
  archive_allowed: false
  public_access_allowed: false
  quotation_scope: null
  attribution_preference: null
  embargo_until: null
  withdrawal_or_revision_refs: []
  granted_at: null
```

Interview participation does not imply publication permission.

Public access to one interview does not imply access to later interviews.

## Corroboration graph

```yaml
recollection_assessment:
  assessment_id: null
  recollection_claim_id: null
  assessor_ref: null
  independent_source_refs: []
  related_claim_refs: []
  consistency_state: UNASSESSED
  scope_notes: null
  confidence_band: null
  created_at: null
  supersedes_assessment_id: null
```

Suggested states:
- UNASSESSED
- CONSISTENT_WITH_AVAILABLE_EVIDENCE
- PARTIALLY_CORROBORATED
- CONFLICTING_EVIDENCE
- CONTRADICTED_ON_SPECIFIC_POINT
- CANNOT_BE_TESTED
- SOURCE_DEPENDENT

Never use TRUE/FALSE as the only institutional state for complex testimony.

Two people repeating the same story are not independent corroboration if both received it from the same source.

## Repeated interviews

Later interviews must retain their own identity.

A narrator may:
- remember more;
- remember less;
- change interpretation;
- correct a date;
- become less certain;
- repeat a stable account;
- withdraw permission for a use allowed earlier where authored policy permits;
- distinguish what they saw from what they later learned.

The engine should record these changes rather than merge them into one canonical quote.

## Oral tradition

```yaml
oral_tradition:
  tradition_id: null
  community_or_network_ref: null
  topic_refs: []
  earliest_attested_ref: null
  retelling_record_ids: []
  motif_refs: []
  variant_refs: []
  known_transmission_links: []
  contested_origin_claim_ids: []
  public_access_state: null
  canon_truth_status: UNRESOLVED
```

An oral tradition can be historically important even if its supernatural or causal claim is false, unresolved or metaphorical.

The generator must preserve the distinction between "this community tells this story" and "this story is cosmologically true".

## Interview contamination and dependency

The layer tracks when accounts may not be independent.

```yaml
source_dependency:
  dependency_id: null
  downstream_claim_id: null
  upstream_source_refs: []
  mechanism: null
  known_before_interview: false
  confidence_band: null
```

Candidate mechanisms:
- SHARED_MEDIA_REPORT
- PRIOR_GROUP_DISCUSSION
- PRIOR_INTERVIEW
- FAMILY_RETELLING
- OFFICIAL_BRIEFING
- PUBLIC_RUMOR
- UNKNOWN

This prevents five people who heard the same radio report from becoming five independent eyewitnesses.

## Memory and actor privacy

Do not infer medical, neurological or psychological diagnoses from memory inconsistency.

Do not infer dishonesty from hesitation, contradiction, changed wording or refusal.

Do not infer relationship, ideology, faction membership or culpability from being interviewed together.

Interview history should be private by default when it contains private subjects, care records, sensitive locations or personally identifying context.

## Pokémon testimony boundary

Pokémon Agency owns observed communication and persistent Pokémon identity.

If an authored rule or communication capability permits a Pokémon to communicate propositional information, the resulting account can enter this layer with provenance.

Do not transform species flavor, body language, Friendship/Loyalty, obedience or a high Perception score into human-language testimony.

Do not use Psychic, Telepathy or Aura as universal truth detection.

## World-generation uses

This layer can produce:
- conflicting recollections of an old route;
- an elder who remembers a bridge before a flood;
- workers whose recollections expose a maintenance pattern;
- former Trainers remembering the same tournament differently;
- a community tradition whose stable motif survives while dates drift;
- an interview that clarifies provenance without solving the mystery;
- a later correction that changes a museum label;
- a debrief that improves an emergency-service procedure;
- a missing interview whose absence becomes archival, not conspiratorial, evidence.

The system should also allow interviews that reveal nothing new.

## Minecraft projection

Minecraft may display:
- an interview room;
- a recorder object;
- subtitles or dialogue UI;
- archival terminals;
- NPC availability;
- public listening stations;
- sealed collection areas.

Minecraft must not decide:
- whether the narrator is truthful;
- whether a memory is accurate;
- whether two statements corroborate each other;
- whether a person has consented to publication;
- whether a translation is authoritative;
- whether an account proves guilt;
- whether a rumor is true.

## Battle boundary

Interview and testimony state stays outside AutoPTU.

If violence interrupts an interview, the world first freezes the interview and preserves its current provenance. AutoPTU receives only the actual combatants and battle state.

Winning the battle does not make the interrupted statement complete or accurate.

## Encounter contracts

### Evacuation During Community History Recording

FULL version:
A public oral-history event is interrupted by a distinct threat. Narrators, archivists and recording equipment must exit while the confrontation continues.

Primary capability dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL if exact supported effects are used;
- terrain/weather/hazards/zones/reactions — BLOCKING if a tactical environmental effect is required;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:
Pause the interview. Move narrators, archivists and recording equipment to safety in world state. Preserve the last completed statement boundary. Open a static AutoPTU arena only if a separate confrontation remains. Resume or reschedule the interview afterward.

### Witness Route Reconstruction

FULL version:
A witness physically walks investigators through an old route while changing landmarks, wildlife and access constraints test parts of the recollection.

Primary blockers are complete movement, objective-aware AI and adapter/playback. Environmental families enter only for exact validated tactical effects.

REDUCED version:
Resolve the walkthrough as overworld navigation and observation. At each stop, create versioned recollection claims and compare them with maps/photographs. If a battle occurs, freeze location and use a conventional static encounter.

### Archive Interview Handoff

Primarily non-combat.

The narrator authorizes a recording for restricted archival use while withholding public release. Archives, Research Ethics, Languages and this layer execute the handoff. No social Skill roll can override the narrator's authored permission state.

## Hard non-inferences

Do not infer:
- confidence -> accuracy;
- inconsistency -> lie;
- old age -> unreliable memory;
- emotion -> falsehood;
- calmness -> truth;
- multiple matching stories -> independent corroboration;
- interview -> consent to publication;
- transcript -> original recording;
- translation -> original words;
- oral tradition -> literal world truth;
- absence of testimony -> evidence of guilt;
- successful Charm/Guile/Command check -> mind reading;
- battle victory -> reliable testimony.

## Canon questions left open

- Which Ouros institutions conduct formal oral histories?
- Which communities maintain authored oral traditions at campaign start?
- What interview records are public, private, embargoed or restricted?
- What rules govern witness statements inside Cases?
- Can narrators revise access later, and under which institutional policies?
- Which languages/scripts require translation during interviews?
- Can a Pokémon ever provide propositional testimony, and by what exact PTU/Caelo capability?
- Which social Skills affect cooperation without becoming truth-detection mechanics?

No answer is silently canonized here.