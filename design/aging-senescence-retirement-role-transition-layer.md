# Aging, Senescence, Retirement & Role Transition Layer

Status: proposed systems design. Not established Ouros canon.
Date: 2026-08-23

## Purpose

Ouros needs actors and Pokémon to persist through years without reducing aging to a stat penalty or using retirement as a synonym for death.

This layer owns chronological aging records, age-estimation uncertainty, observed long-term functional change, competitive/professional retirement, partial withdrawal from roles, return/re-entry, and role transitions associated with long service.

It does not own:

- permanent Pokémon Evolution or form changes;
- family/kinship;
- care/treatment decisions;
- death or memorialization;
- workplace staffing details;
- institutional succession;
- Pokémon custody/ownership/partnership;
- PTU mechanical stat changes unless rules explicitly support them.

## Core separation

```text
persistent actor / pokemon identity
        ↓
chronological-age fact or estimate
        ↓
life-stage claim (optional, contextual)
        ↓
observed functional state over time
        ↓
role eligibility / participation state
        ↓
retirement or role-transition decision
        ↓
care / workplace / institution / partnership consequences
        ↓
public record and memory
```

Age does not decide capability. Capability does not decide desire. Retirement does not decide health. Health does not decide death.

## 1. Age record

```yaml
age_record:
  subject_id: null
  birth_or_origin_date: null
  date_precision: unknown
  age_estimate_min: null
  age_estimate_max: null
  estimate_method_ref: null
  estimate_confidence: unknown
  source_refs: []
  last_reviewed_at: null
```

A precise birth date is optional.

Wild Pokémon, historical NPCs, rescued individuals and old institutional partners may only have an estimated age range.

Never invent a birth date merely to make the timeline convenient.

## 2. Life-stage claim

`life_stage` is descriptive and source-bound.

```yaml
life_stage_claim:
  subject_id: null
  stage_label: null
  applies_from: null
  applies_until: null
  basis: null
  source_refs: []
  confidence: unknown
```

Possible labels may include juvenile, subadult, adult, older_adult, elderly or authored regional terms.

The label does not apply mechanics by itself.

Species-specific stages require authored/canon evidence. Do not derive them from Evolution stage.

A first-stage Pokémon can be old. A fully evolved Pokémon can be young.

## 3. Functional observations

Aging is represented through observations before interpretation.

```yaml
functional_observation:
  observation_id: null
  subject_id: null
  observed_at: null
  domain: null
  context_ref: null
  observation: null
  comparison_ref: null
  observer_id: null
  method_ref: null
  confidence: null
  source_refs: []
```

Domains can include:

- mobility;
- endurance;
- recovery routine;
- sensory behavior;
- appetite/feeding routine;
- social participation;
- travel range;
- work participation;
- competitive participation;
- task preference;
- seasonal timing;
- rest pattern;
- route memory;
- learned routine retention.

The record should prefer facts such as `stopped joining the second daily patrol` over interpretations such as `too old to work`.

## 4. Functional-change assessment

```yaml
functional_change_assessment:
  assessment_id: null
  subject_id: null
  compared_period_start: null
  compared_period_end: null
  domains_changed: []
  domains_stable: []
  proposed_explanations: []
  evidence_refs: []
  alternative_explanations: []
  status: provisional
```

Age may be one hypothesis among several.

Other possible explanations include injury, environment, workload, equipment, social change, weather, habitat change, training, preference or measurement differences.

Never write `age caused X` solely because the subject is old.

## 5. Role participation

Role participation is independent from chronological age.

```yaml
role_participation:
  participation_id: null
  subject_id: null
  role_ref: null
  institution_or_group_id: null
  status: active
  scope: null
  started_at: null
  ended_at: null
  schedule_or_limit_refs: []
  eligibility_refs: []
  decision_refs: []
```

Possible status values:

- active;
- reduced_scope;
- seasonal;
- reserve;
- advisory;
- mentoring_only;
- exhibition_only;
- inactive;
- retired_from_role;
- temporarily_withdrawn;
- returned;
- unknown.

An actor can have different states for different roles.

A Trainer may retire from sanctioned League competition while continuing to teach, travel or battle privately.

A Pokémon may retire from competitive play while remaining a partner, household member, research subject, sanctuary resident or voluntary institutional participant.

## 6. Retirement event

```yaml
retirement_event:
  retirement_event_id: null
  subject_id: null
  role_ref: null
  retirement_scope: null
  effective_at: null
  decision_kind: null
  decision_authority_ref: null
  stated_reason: null
  reason_visibility: private
  career_state_ref: null
  consent_or_agency_refs: []
  successor_ref: null
  return_possible: unknown
  chronicle_event_ref: null
```

Retirement scope must be explicit.

Examples:

- `competitive_roster`;
- `gym_leader_role`;
- `full_time_field_work`;
- `night_shift_only`;
- `long_distance_transport`;
- `public_performance`;
- `institutional_service`.

Do not create `retired=true` as a universal actor state.

## 7. Competitive Career integration

AutoPTU Career currently has an explicit Pokémon competitive-longevity policy using `career_health`, seasonal workload and Training Kit wear.

Ouros should preserve that source as a distinct integration state:

```yaml
competitive_longevity_state:
  pokemon_id: null
  source_system: autoptu_career
  career_health: null
  competitive_status: null
  retired_season: null
  retired_reason: null
  source_event_refs: []
```

Rules:

- do not rename `career_health` to biological health;
- do not use it as lifespan;
- do not apply its wear formula to wild or non-Career Pokémon;
- do not infer death at zero;
- do not infer inability to perform non-competitive activities;
- preserve the same `pokemon_id` after competitive retirement.

If future Career code allows re-entry, rehabilitation or alternative leagues, this layer should consume that authoritative result rather than invent it.

## 8. Return and re-entry

Retirement does not have to be irreversible unless its source system says so.

```yaml
role_return_event:
  return_event_id: null
  subject_id: null
  role_ref: null
  previous_retirement_event_id: null
  returned_at: null
  return_scope: null
  eligibility_ref: null
  authorization_ref: null
  conditions_ref: null
  source_refs: []
```

A return can be:

- temporary exhibition;
- emergency substitute;
- one final expedition;
- restored professional credential;
- resumed seasonal duty;
- complete competitive return when rules permit.

Do not use comeback stories to erase the retirement period.

## 9. Role transition and mentorship

Retirement may produce a new role, but never automatically.

Possible transitions:

- champion → dojo teacher;
- Gym Leader → adviser;
- field researcher → archive curator;
- ranger → dispatcher/trainer;
- courier Pokémon → local route guide;
- competitive Pokémon → demonstration partner;
- long-distance service Pokémon → local institutional resident;
- worker → safety committee member;
- performer → coach;
- guide → map/archive contributor.

The target role needs its own membership, consent, credential and staffing rules.

Age does not grant Mentor, Command, Education ranks or institutional authority.

## 10. Succession boundary

Institutional succession remains outside this layer.

This layer can emit:

- retirement effective date;
- reduced-scope availability;
- successor preference if explicitly stated;
- knowledge-transfer tasks;
- pending role vacancy.

Governance, Battle Institutions, Workplaces or another institutional layer decides appointment.

A retiring actor cannot simply name a successor unless canon grants that authority.

## 11. Knowledge and experience

Experience is not a numeric `wisdom` bonus.

Store concrete evidence:

- years using a route;
- prior response to similar floods;
- known equipment revisions;
- historical opponent records;
- recurring wildlife observations;
- previous institutional decisions;
- remembered techniques where mechanics/canon support retention.

A veteran can be wrong. A newcomer can be right.

Long service should improve the world's available history, not guarantee the actor's conclusion.

## 12. Older Pokémon in collectives

An older Pokémon may remain within a wild collective.

Possible observed changes:

- travels only part of a migration;
- uses a smaller foraging range;
- appears at different stopovers;
- leaves leadership or takes it more often;
- accompanies juveniles;
- stops competing for a resource;
- continues a known route after younger members change behavior;
- disappears from observations while the population remains present.

None of these are automatic consequences of age.

Wild Collectives, Migration, Social Learning and Diel Activity own their respective state. This layer supplies the individual age/history context.

## 13. Care and accommodation

Older age alone does not create a medical condition.

When a need is observed, hand off to Care/Accessibility:

- shorter route;
- different schedule;
- resting space;
- equipment change;
- assistance with transport;
- lower workload;
- accessible housing;
- environmental adjustment.

The accommodation is based on a documented need or choice, not age stereotype.

## 14. Death boundary

Aging never directly writes death into Chronicle.

A death event requires whatever authoritative death rules/canon Ouros eventually adopts.

Forbidden shortcuts:

- `old + missing = dead`;
- `retired + old = dead`;
- `career_health == 0 = dead`;
- `Fainted = dead`;
- `Injured = dying`;
- `not observed this season = deceased`.

Memorial systems only receive a confirmed death when the appropriate authority establishes it.

## 15. Public knowledge

Public age claims can be wrong.

A famous Trainer may have:

- an exact institutional birth record;
- a public age different from private records;
- no disclosed age;
- an approximate career-era estimate;
- contradictory biographies.

Identity/Archives/Public Memory own those records.

Do not infer private health or retirement plans from public age.

## 16. Time advancement

Chronological age can advance with world time when the underlying date is known.

Functional change must not advance procedurally from age alone.

Allowed offline progression:

- exact age increases from dates;
- known service tenure increases;
- scheduled retirement takes effect if already authorized;
- role transition starts when its date arrives;
- Career competitive wear advances only through its source-system contract.

Disallowed without evidence/canon:

- stat decline;
- movement loss;
- illness;
- cognitive decline;
- death;
- forced retirement;
- reduced fertility;
- loss of Moves or Abilities.

## 17. Minecraft projection

Minecraft may show:

- changed routine;
- a different workstation;
- an adviser room;
- a retired champion's dojo;
- a sanctuary residence;
- a slower or shorter authored patrol path;
- commemorative displays while the subject is still alive;
- historical photos and equipment.

Minecraft must not infer age from model scale, skin, movement animation or despawn frequency.

A cosmetic cane, gray hair, worn saddle or old Poké Ball does not create a mechanical penalty.

## 18. Battle handoff

The battle engine receives current authoritative combatant state.

Age metadata should not enter AutoPTU unless an exact PTU/Caelo rule explicitly requires it.

A veteran or retired actor entering an authorized battle uses the legal stats, Moves, Abilities, items and Features supplied by the authoritative mechanical source.

Never modify:

- Speed;
- HP;
- Evasion;
- Accuracy;
- damage;
- movement;
- action budget;
- initiative;
- Status susceptibility

because the narrative layer calls someone old.

## 19. Encounter pattern — Veteran Route Survey

Premise:

A long-serving route partner has stopped completing the final ridge segment of a seasonal survey. The immediate question is what changed, not whether the Pokémon is "too old."

World-state investigation can compare:

- route history;
- weather;
- injury/care records;
- surface changes;
- recent workload;
- companion/group changes;
- age history;
- personal behavior observations.

FULL version:

If a confrontation occurs while the veteran and other actors are moving through a route, objective-aware withdrawal/protection and environmental state may matter.

REDUCED version:

Resolve the survey choice and the veteran's movement outside battle. If a hostile encounter remains, freeze a conventional arena and run only that confrontation.

## 20. Encounter pattern — Exhibition Return

Premise:

A retired former competitor agrees to one exhibition while a younger institutional team handles routine duties.

The interesting state is role scope and consent, not an age handicap.

FULL version can use normal battle mechanics if the participant is mechanically legal. No special environmental subsystem is required unless the scenario adds one.

REDUCED version is the same battle with all exhibition logistics outside AutoPTU.

A victory does not cancel retirement.

## 21. Encounter pattern — Handoff at North Watch

Premise:

A veteran watch partner is completing a final scheduled season while a successor shadows the route. A separate disturbance interrupts the handoff.

FULL version may need moving protect/withdraw objectives and tactical AI.

REDUCED version resolves both actors' route positions and succession schedule in world state, then opens a static confrontation if required.

The battle result does not appoint the successor.

## 22. Non-inferences

Never infer:

- old → weak;
- old → wise;
- old → slow;
- old → sick;
- old → less social;
- old → leader;
- old → mentor;
- old → retired;
- retired → old;
- retired → incapable;
- retired → deceased;
- retirement → loss of partnership;
- retirement → transfer of ownership;
- competitive retirement → unable to work or travel;
- long tenure → authority outside the role;
- years of experience → correct conclusion;
- Career wear → biological lifespan;
- PC storage → rest home;
- lower encounter frequency → senescence;
- cosmetic age cues → mechanical penalties.

## 23. Open canon questions

- Does Ouros author exact birth dates for important NPCs, approximate eras, or both?
- Which Pokémon species have canonically known long/short lifespans?
- Does the campaign permit natural death from age, and under what source authority?
- Is AutoPTU Career competitive retirement part of Ouros canon or only one gameplay mode?
- Can competitively retired Pokémon return under any circumstances?
- Which institutions have formal retirement/succession policies?
- Can a player choose partial retirement from one circuit while remaining active elsewhere?
- How are long-lived Pokémon represented across human generations?
- Which age-related accessibility accommodations are available regionally?
- How much age information is public for PCs/NPCs in multiplayer?

Until those questions are authored, the layer stores facts, decisions and observations without inventing age mechanics.