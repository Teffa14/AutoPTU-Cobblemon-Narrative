# Electoral Selection, Candidacy & Results Continuity Extension

Status: PROPOSED SYSTEMS DESIGN. Not established Ouros canon.
Date: 2026-08-31

## Purpose

This extension preserves the lifecycle of an electoral selection only when an existing canon rule already states that a bounded office or public choice uses such a procedure.

It does not make Ouros a democracy, create elected offices, define suffrage, invent political parties, impose secret ballots, determine term lengths or grant civic authority from popularity.

Civic Governance owns the body, mandate and decision context. Civic Office owns the office-holder episode and handover after a result becomes effective. Public Notices owns official publication. Media owns reporting. Supporter/Fandom owns informal organized support. Archives owns preserved records. This extension owns the procedural continuity between an authored electoral rule and its confirmed result.

## Activation gate

No electoral object may exist without:

```yaml
electoral_activation_gate:
  governing_rule_ref: null
  selecting_scope_ref: null
  selected_office_or_question_ref: null
  authority_source_ref: null
  canon_status: REQUIRED
```

If `governing_rule_ref` is absent, the generator must not infer an election from genre, settlement size, civic-office title, popularity or player expectation.

## Selection process

```yaml
electoral_process:
  process_id: null
  governing_rule_ref: null
  office_ref: null
  question_ref: null
  jurisdiction_ref: null
  electorate_rule_ref: null
  eligibility_rule_ref: null
  nomination_rule_ref: null
  ballot_rule_ref: null
  counting_rule_ref: null
  tie_rule_ref: null
  confirmation_rule_ref: null
  challenge_or_review_ref: null
  nomination_opens_at: null
  nomination_closes_at: null
  voting_opens_at: null
  voting_closes_at: null
  status: ANNOUNCED
  source_refs: []
```

Candidate states may include:

ANNOUNCED, NOMINATION_OPEN, OPTIONS_PENDING, OPTIONS_CONFIRMED, CAMPAIGNING, VOTING_OPEN, VOTING_CLOSED, COUNTING, RESULT_REPORTED, REVIEW_PENDING, RESULT_CONFIRMED, TRANSITION_LINKED, CLOSED, DEFERRED, CANCELLED, DISPUTED.

These labels describe workflow only. Local canon defines legal meaning.

## Candidate episode

```yaml
candidate_episode:
  candidate_episode_id: null
  process_id: null
  actor_id: null
  declared_at: null
  nomination_source_ref: null
  eligibility_assessment_ref: null
  ballot_option_ref: null
  affiliation_ref: null
  platform_claim_refs: []
  endorsement_refs: []
  campaign_appearance_refs: []
  withdrawal_at: null
  status: DECLARED
```

Possible states:

DECLARED, ELIGIBILITY_PENDING, ELIGIBLE, INELIGIBLE_UNDER_RULE, OPTION_CONFIRMED, WITHDRAWN, ACTIVE, RESULT_PENDING, SELECTED, NOT_SELECTED.

Required separations:

`CANDIDATE_DECLARED != ELIGIBLE_CANDIDATE`

`ELIGIBLE_CANDIDATE != BALLOT_OPTION_CONFIRMED`

`WITHDRAWN != NEVER_RAN`

`NOT_SELECTED != PUBLIC_IRRELEVANCE`

## Ballot or selection option

```yaml
selection_option:
  option_id: null
  process_id: null
  option_type: CANDIDATE
  candidate_episode_ref: null
  question_choice_ref: null
  display_label_ref: null
  valid_from: null
  valid_until: null
  status: CONFIRMED
```

The layer does not assume every process uses paper ballots, one-person-one-vote, ranked choice, plurality or any other method.

## Electorate snapshot

Do not instantiate every resident merely to simulate an election.

```yaml
electorate_snapshot:
  snapshot_id: null
  process_id: null
  governing_rule_ref: null
  snapshot_at: null
  eligibility_scope_ref: null
  aggregate_eligible_count: null
  explicit_member_refs: []
  completeness: UNKNOWN
  privacy_mode: AGGREGATE_DEFAULT
```

Named eligible voters appear only when canon and privacy rules require them.

`RESIDENT != ELIGIBLE_VOTER`

`SUPPORTER_MEMBER != ELIGIBLE_VOTER`

`ELIGIBLE_VOTER != BALLOT_CAST`

## Endorsement

```yaml
endorsement_record:
  endorsement_id: null
  process_id: null
  endorser_ref: null
  option_ref: null
  announced_at: null
  source_ref: null
  withdrawn_at: null
  status: ACTIVE
```

`ENDORSEMENT != VOTE`

`GROUP_ENDORSEMENT != MEMBER_VOTES`

`FACTION_SUPPORT != ELECTORATE_CONTROL`

## Campaign appearance

Campaign events are links into owner systems rather than a new event engine.

```yaml
campaign_appearance_link:
  appearance_id: null
  candidate_episode_ref: null
  event_ref: null
  media_ref: null
  performance_ref: null
  supporter_ref: null
  public_notice_ref: null
  claim_refs: []
```

A speech can create attributed claims. A rally can create attendance observations. Neither creates votes.

`PUBLIC_ATTENDANCE != ELECTORAL_SUPPORT`

`MEDIA_COVERAGE != OFFICIAL_RESULT`

`CAMPAIGN_PROMISE != FUTURE_POLICY_FACT`

## Poll or opinion estimate link

Polling stays evidence, never a shadow election.

```yaml
opinion_estimate_link:
  estimate_id: null
  process_id: null
  source_ref: null
  population_scope_ref: null
  sampling_method_ref: null
  field_window_ref: null
  reported_values: []
  uncertainty_ref: null
```

`POLL_RESULT != ELECTION_RESULT`

`POLL_SAMPLE != ELECTORATE`

`LEADING_IN_POLL != WINNER`

## Voting window

```yaml
voting_episode:
  voting_episode_id: null
  process_id: null
  opened_at: null
  closed_at: null
  authorized_method_refs: []
  authorized_site_refs: []
  interruption_refs: []
  resumed_at: null
  status: CLOSED
```

The ordinary narrative layer should record aggregate procedural state, not individual choices.

`BALLOT_CAST != VOTER_IDENTITY_DISCLOSED`

`VOTING_INTERRUPTED != ALL_PRIOR_VOTES_VOID`

`POLLING_SITE_CLOSED != PROCESS_CANCELLED`

## Count episode

```yaml
count_episode:
  count_id: null
  process_id: null
  governing_count_rule_ref: null
  started_at: null
  completed_at: null
  input_batch_refs: []
  reconciliation_refs: []
  discrepancy_refs: []
  aggregate_totals: []
  status: IN_PROGRESS
```

A discrepancy is a state requiring review. It does not establish misconduct.

`DISCREPANCY_FOUND != FRAUD_PROVEN`

`LEADING_DURING_COUNT != WINNER`

`COUNT_COMPLETE != RESULT_CONFIRMED`

## Result report and confirmation

```yaml
electoral_result_record:
  result_id: null
  process_id: null
  reported_at: null
  reporting_authority_ref: null
  result_kind: UNOFFICIAL
  aggregate_totals_ref: null
  selected_option_refs: []
  supersedes_result_ref: null
  source_refs: []
```

```yaml
result_confirmation:
  confirmation_id: null
  process_id: null
  governing_rule_ref: null
  confirmed_result_ref: null
  confirmed_at: null
  confirming_authority_ref: null
  challenge_window_ref: null
  status: CONFIRMED
```

Required boundaries:

`PROJECTED_WINNER != CONFIRMED_WINNER`

`UNOFFICIAL_RESULT != FINAL_RESULT`

`RESULT_CONFIRMED != OFFICE_AUTHORITY_EFFECTIVE`

`WINNER != UNIVERSAL_SUPPORT`

## Recount, review and challenge

```yaml
result_review_episode:
  review_id: null
  process_id: null
  trigger_ref: null
  governing_rule_ref: null
  review_type: AUTHORED
  scope_ref: null
  opened_at: null
  closed_at: null
  finding_refs: []
  resulting_result_ref: null
  status: OPEN
```

`RECOUNT != FRAUD_PROVEN`

`REVIEW_OPENED != PRIOR_RESULT_ERASED`

`DISPUTED_RESULT != INVALID_RESULT`

The extension never invents a right to recount or appeal.

## Handoff to Civic Office

After the local rule produces the required result state:

```yaml
electoral_transition_link:
  link_id: null
  process_id: null
  confirmed_result_ref: null
  office_transition_ref: null
  result_known_at: null
  authority_effective_at: null
```

Civic Office then owns acting coverage, effective dates, credentials, records, pending matters and holder episodes.

`RESULT_KNOWN != AUTHORITY_EFFECTIVE`

`RESULT_CONFIRMED != HANDOVER_COMPLETE`

## Player-facing investigation grammar

An election story should usually be about evidence and consequences rather than hidden morality scores.

Possible questions:

- Which version of the reported result was current at a particular time?
- Was a poster printed before a withdrawal?
- Did a remote district report later without anything improper occurring?
- Does an endorsement represent one leader or a whole group?
- Are two turnout totals using different eligibility snapshots?
- Was a candidate's promise made before a project dependency changed?

The answer should come from provenance and authored rules.

## Pokémon and PTU boundary

No Pokémon species, Type, Move, Ability, Loyalty value, Trainer class, Skill Rank, Feature, Badge, Contest result or battle win creates electoral eligibility, votes or civic mandate unless exact canon explicitly establishes a local rule and the mechanic is validated.

`CHARM_CHECK_SUCCESS != VOTE_GAINED`

`COMMAND_SUCCESS != ELECTORATE_CONTROL`

`BATTLE_WON != ELECTION_WON`

`BADGE_EARNED != CIVIC_MANDATE`

`POKEMON_POPULARITY != CANDIDATE_ELIGIBILITY`

## Minecraft/Cobblemon boundary

SAFE presentation can include posters, candidate desks, meeting venues, polling-place props, sealed containers, public result boards, NPC schedules and crowds after Ouros has established those states.

Minecraft/Cobblemon must not decide:

- who is eligible;
- who is a candidate;
- whether a ballot is valid;
- voter choice from NPC movement;
- turnout from loaded entities;
- result totals from scoreboard state;
- winner from crowd size;
- civic authority from BattleState;
- handover completion from an NPC skin change.

Authority flow remains:

`Ouros civic/electoral state -> explicit BattleSpec only if a separate tactical incident exists -> AutoPTU -> adapter -> Minecraft/Cobblemon presentation`

## Encounter contract — Polling Place Access Perimeter

Narrative premise: an unrelated current incident blocks safe physical access near an authorized voting site.

Full intended version may include protected access routes, civilian withdrawal, Intercept/forced displacement, timed reopen/closure state and tactical AI that understands route protection.

Permanent dependencies:

- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL where combat content uses it
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING when dynamic hazards/protected zones matter
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Full status: BLOCKED.

Reduced status: READY at narrative-contract level with individually audited combat content.

Before initiative, Ouros pauses the voting site, secures all election material and moves voters/staff outside BattleSpec. A static legal battle can return only `IMMEDIATE_POLLING_PLACE_APPROACH_CLEAR`.

`IMMEDIATE_POLLING_PLACE_APPROACH_CLEAR != VOTING_RESUMED`

`BATTLE_WON != BALLOTS_CAST`

`BATTLE_WON != ELECTION_RESULT`

## Encounter contract — Ballot Transport Chokepoint

Full intended version requires escort/object-carrying semantics, complete movement, lifecycle, objective-aware tactical policy and semantic adapter playback. It is BLOCKED.

Reduced version: the authorized container is secured outside BattleSpec and custody is frozen before initiative. Players may clear a static corridor. Courier and electoral layers resume transport afterward.

Permitted tactical output: `IMMEDIATE_BALLOT_ROUTE_CLEAR`.

`IMMEDIATE_BALLOT_ROUTE_CLEAR != BALLOTS_DELIVERED`

`BALLOTS_DELIVERED != COUNTED`

## Encounter contract — Count Center Evacuation Perimeter

Full version may need active civilian withdrawal, protected rooms, hazards/zones/reactions and tactical policy. It is BLOCKED.

Reduced version pauses the count, removes staff and election material from the tactical slice and runs a static perimeter battle.

Permitted output: `IMMEDIATE_COUNT_CENTER_PERIMETER_CLEAR`.

`BATTLE_WON != COUNT_RESUMED`

`BATTLE_WON != RESULT_AUTHENTICATED`

## Encounter contract — Campaign Event Incident Separation

Full version may require crowd routing, dynamic barriers, protect/withdraw objectives, lifecycle and adapter playback. It is BLOCKED.

Reduced version adjourns the event and removes attendees before initiative. Any later campaign effect comes only from ordinary Media, Supporter, Public Memory or authored campaign records.

`BATTLE_WON != SUPPORT_GAINED`

`BATTLE_LOST != CANDIDATE_WITHDRAWN`

## Promotion gate

Before any concrete electoral process becomes canon, answer:

- Which exact office or question uses an election?
- What authored rule creates the process?
- Who is eligible to stand?
- Who is eligible to participate?
- What options appear and how are they confirmed?
- What method records choices?
- What privacy rules apply?
- How is the count performed?
- What result states are official or preliminary?
- What confirmation, recount or review routes exist?
- When does the result become effective for Civic Office?
- Which public records and notices exist?
- Which PTU/Caelo mechanics, if any, have exact validated relevance?

Until those are answered, all content generated by this extension remains proposed and procedure-neutral.