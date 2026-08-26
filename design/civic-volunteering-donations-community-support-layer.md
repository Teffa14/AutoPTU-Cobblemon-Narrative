# Civic Volunteering, Donations & Community Support Layer

Status: proposed systems design. Not established Ouros canon.

Research basis: `research/2026-08-25-civic-volunteering-donations-community-support-scan-175.md`.

## Purpose

Ouros already has clubs, workplaces, worker associations, emergency services, finance, supply chains and community science. It still needs a general authority for civic participation that is not employment, club membership or formal emergency command.

This layer controls:

- standing volunteer programs;
- spontaneous offers of help;
- community-service assignments;
- volunteer intake and bounded screening;
- orientation and supervision handoff;
- service sessions and completion records;
- donation offers and donor intent;
- acceptance, redirection or refusal of donated goods;
- fundraising/campaign records only at the pledge/allocation intent level;
- community support drives;
- transition from civic support into the authoritative receiving system.

It does not create labor law, charity law, tax rules, nonprofit status, emergency powers, professional credentials or PTU progression.

## Authority boundaries

The following separations are mandatory.

- volunteer != employee;
- volunteer != club member;
- volunteer != responder;
- volunteer != credentialed professional;
- offered help != accepted help;
- accepted volunteer != assigned volunteer;
- assignment != unrestricted site access;
- completed service != future obligation;
- completed service != reputation bonus;
- donation offered != donation accepted;
- donation accepted != inventory available for use;
- donor intent != recipient operational authority;
- fundraising target != money received;
- money received != goods purchased;
- goods purchased != goods delivered;
- public praise != canonical motive;
- repeated service != friendship;
- repeated service != employment;
- emergency participation != permanent emergency authority;
- Pokémon accompanying volunteer != working-Pokémon assignment.

Authoritative handoffs:

- Clubs: `social-bonds-mentorship-clubs-layer.md`
- Worker-created mutual aid/representation: `worker-associations-collective-representation-layer.md`
- Paid work and staffing: Workplaces
- Crisis objectives: `crisis-rescue-recovery-layer.md`
- Operational responder coordination: `emergency-services-dispatch-incident-coordination-layer.md`
- Credentials/access: `credentials-permissions-eligibility-layer.md`
- Money settlement: `currency-accounts-payments-settlement-layer.md`
- Finance commitments/grants: Finance
- Physical goods/inventory after acceptance: `supply-chains-procurement-inventory-layer.md`
- Persistent item identity: Material Culture
- Pokémon institutional assignments: `working-pokemon-institutional-roles-layer.md`
- Pokémon identity/agency: Pokémon Agency
- Public narrative/recognition: Public Memory / Media

## 1. Civic support organization

```yaml
civic_support_organization:
  support_org_id: null
  public_name: null
  organization_kind: volunteer_service|community_support|relief_group|stewardship_group|donation_network|informal
  founded_at: null
  dissolved_at: null
  home_location_ids: []
  service_domains: []
  intake_channel_ids: []
  host_institution_ids: []
  standing_program_ids: []
  archive_id: null
  status: active
  history_event_ids: []
```

A civic support organization can be informal. It does not need a legal status unless future canon defines one.

## 2. Volunteer program

A recurring program stores what work can actually be offered.

```yaml
volunteer_program:
  program_id: null
  support_org_id: null
  host_institution_id: null
  domain: trail_stewardship|festival_support|shelter_logistics|library_support|community_science|care_support|public_information|other
  purpose: null
  assignment_types: []
  minimum_requirements_refs: []
  restricted_tasks: []
  supervision_model_ref: null
  intake_policy_revision_id: null
  active_window: null
  status: active
```

The program points to real credentials when required; it never creates them.

## 3. Need signal

Volunteer activity should originate from an actual need.

```yaml
community_support_need:
  need_id: null
  requesting_authority_id: null
  related_world_state_refs: []
  need_type: labor|transport|sorting|information|stewardship|distribution|hosting|other
  requested_quantity_or_band: null
  required_skill_or_credential_refs: []
  prohibited_assignment_conditions: []
  location_ids: []
  active_from: null
  active_until: null
  priority_claim: null
  status: open
```

Suggested statuses:

- DRAFT
- OPEN
- PARTIALLY_FILLED
- FILLED
- PAUSED
- WITHDRAWN
- EXPIRED
- SUPERSEDED

Need priority is an institutional decision, not world truth.

## 4. Volunteer offer

```yaml
volunteer_offer:
  offer_id: null
  actor_id: null
  offered_at: null
  availability_window: null
  stated_preferences: []
  claimed_skills: []
  credential_refs: []
  mobility_constraints_authored: []
  requested_program_ids: []
  privacy_scope: institution_only
  status: submitted
```

Claimed skill stays separate from verified qualification.

Do not infer health, disability, age suitability or private constraints unless the actor provides that information or another authoritative system permits access.

## 5. Intake and scope review

```yaml
volunteer_intake_review:
  intake_id: null
  offer_id: null
  reviewed_by_id: null
  reviewed_at: null
  relevant_requirement_refs: []
  verified_credential_refs: []
  permitted_assignment_types: []
  excluded_assignment_types: []
  referral_ids: []
  result: accepted_for_pool|more_info_needed|redirected|declined|withdrawn
  notes: null
```

A declined assignment is not a judgment of character.

## 6. Assignment

```yaml
volunteer_assignment:
  assignment_id: null
  need_id: null
  volunteer_actor_id: null
  host_institution_id: null
  assignment_type: null
  location_id: null
  supervisor_or_host_id: null
  starts_at: null
  expected_end_at: null
  access_scope_refs: []
  equipment_issue_refs: []
  instructions_revision_id: null
  status: assigned
```

Suggested status lifecycle:

`OFFERED -> ACCEPTED -> ORIENTED -> ACTIVE -> PAUSED/TRANSFERRED -> COMPLETED/CANCELLED/WITHDRAWN`

No status grants PTU actions.

## 7. Orientation record

```yaml
volunteer_orientation:
  orientation_id: null
  assignment_id: null
  completed_at: null
  topics: []
  site_rules_revision_refs: []
  hazard_information_refs: []
  escalation_contact_refs: []
  confirmed_restrictions: []
```

Orientation records what information was provided. It does not prove comprehension, safety or qualification.

## 8. Service session

```yaml
volunteer_service_session:
  session_id: null
  assignment_id: null
  started_at: null
  ended_at: null
  actual_location_ids: []
  task_event_ids: []
  interruptions: []
  handoff_refs: []
  outcome: completed|partial|redirected|stopped|withdrawn
  supervisor_observation_refs: []
```

Hours may be stored if a future system needs them, but this layer does not turn time served into XP, wages or prestige points.

## 9. Deactivation and closure

Programs need a normal end state.

A volunteer may leave because:

- the need is filled;
- the event ended;
- the shift ended;
- weather/access changed;
- another institution assumed responsibility;
- the volunteer withdrew;
- the assignment was no longer suitable;
- the organization paused operations.

None of these imply conflict.

## 10. Donation offer

```yaml
donation_offer:
  donation_offer_id: null
  donor_actor_or_org_id: null
  offered_at: null
  offer_kind: goods|equipment|space|transport|service|money_pledge
  item_or_batch_refs: []
  described_quantity: null
  condition_claim: null
  intended_purpose: null
  proposed_recipient_id: null
  delivery_constraints: []
  privacy_scope: recipient_only
  status: offered
```

For money, this record stops at intent/pledge. Currency/Finance owns authorization and settlement.

## 11. Donation review

```yaml
donation_review:
  review_id: null
  donation_offer_id: null
  recipient_authority_id: null
  current_need_refs: []
  storage_capacity_refs: []
  compatibility_refs: []
  safety_or_quality_hold_refs: []
  decision: accept|accept_partial|redirect|decline|more_info_needed
  reason_codes: []
  decided_at: null
```

A decline can be correct even when the item is valuable.

## 12. Donation receipt and handoff

After acceptance:

```yaml
donation_receipt:
  receipt_id: null
  donation_offer_id: null
  accepted_item_or_batch_refs: []
  accepted_quantity: null
  physical_receipt_event_id: null
  recipient_custody_ref: null
  inventory_handoff_ref: null
  provenance_update_ref: null
  received_at: null
```

Supply Chains becomes authoritative for stock availability. Material Culture remains authoritative for persistent item identity.

`RECEIVED` is not `AVAILABLE_FOR_USE`.

## 13. Community support drive

```yaml
community_support_drive:
  drive_id: null
  organizer_id: null
  need_refs: []
  accepted_support_types: []
  excluded_support_types: []
  active_window: null
  public_message_revision_ids: []
  donation_offer_ids: []
  volunteer_need_ids: []
  status: open
```

A drive should tell the world what is actually useful. It can be closed early when needs are filled.

## 14. Unsolicited surge

A major event can generate more goodwill than the receiving system can safely process.

Possible world-state consequences:

- intake backlog;
- storage congestion;
- traffic at a collection point;
- duplicate goods;
- volunteers waiting without assignments;
- stale public messaging;
- recipient organizations redirecting offers elsewhere.

These are operational problems, not evidence that donors or volunteers acted badly.

## 15. Community-service projects outside crises

The layer should be useful during quiet periods.

Examples:

- repair signage under an authorized Public Works project;
- staff a library event;
- assist with a BioBlitz intake table;
- maintain a community garden without taking authority from Flora/Botanical Gardens;
- sort museum outreach material without handling restricted collections;
- support a festival information desk;
- help distribute approved supplies;
- repaint authorized public furniture;
- organize archival scanning where Archives permits it.

Quiet service prevents the system from becoming “disaster volunteering only.”

## 16. Transition from volunteer to another role

A volunteer can later become:

- employee;
- club member;
- worker-association member;
- credentialed responder;
- recurring contractor;
- institutional officer;
- donor;
- mentor.

That transition requires a separate authored event in the governing system. Repeated service alone does not make it happen.

## 17. Pokémon participation

If a Pokémon assists:

1. Pokémon Agency confirms identity/custody/agency context;
2. Working Pokémon determines whether an institutional assignment exists;
3. relevant PTU Capabilities/Features are validated if the task depends on them;
4. the civic layer stores only the assignment/handoff context.

A volunteer cannot lend an institution authority over a Pokémon they do not control.

A Pokémon may decline, withdraw or stop participating without creating Loyalty loss.

## 18. Public recognition

Recognition is optional and separate.

Possible records:

- thank-you event;
- named volunteer roster when consented;
- aggregate service totals;
- historical plaque;
- archive collection;
- annual reunion.

Public Memory owns how those events are remembered. This layer does not assign fame points.

## 19. Privacy

Volunteer records may reveal schedules, contact routes, restrictions or emergency participation. Donation records may reveal finances or private intentions.

Recommended default scopes:

- offer/intake: institution-only;
- assignment: host + participant;
- service completion: host + participant, public only if opted in or institutionally appropriate;
- donation amount/value: private unless explicitly public;
- aggregate community totals: public if safe.

## 20. Multiplayer rules

- one player cannot volunteer another PC;
- accepting a group assignment does not create friendship labels;
- shared donation chests do not create permission to dispose of another player’s property;
- a player-founded club may run a drive only within the authority/resources it actually has;
- access to a volunteer staging area does not grant access to nearby restricted facilities;
- player absence never counts as abandonment of an assignment unless the game has an explicit opt-in scheduling rule.

## 21. Minecraft projection

Minecraft is presentation, not authority.

Forbidden writebacks:

- entering a marked area -> assignment accepted;
- wearing a vest/skin -> credentialed volunteer;
- placing an item in a chest -> donation accepted;
- breaking/repairing blocks -> service completed;
- standing at a desk -> intake complete;
- following an NPC -> authorized access;
- loaded players -> volunteer headcount;
- despawn -> volunteer departure.

Allowed direction:

`authoritative civic-support state -> Minecraft signs/NPC schedules/collection bins/staging areas/visual progress`.

## 22. Encounter handoff rules

Volunteers and donated goods should normally be removed from battle authority before AutoPTU begins.

The battle spec receives only combatants and geometry currently supported by AutoPTU.

World-state objectives such as evacuating volunteers, protecting a donation warehouse or reopening a route remain outside the grid unless exact tactical support exists.

## 23. Failure-forward

Service projects should fail forward.

Examples:

- too many volunteers arrive -> some are redirected to another legitimate project;
- donated goods mismatch the need -> provenance is preserved and another recipient is sought;
- a storm cancels the workday -> the project remains open with a new access dependency;
- a volunteer discovers they lack the needed qualification -> they take a nonrestricted assignment instead;
- a collection drive fills early -> public messaging changes and the event closes successfully.

No forced villain is required.

## 24. Generator rules

Generate civic-support content only from explicit state:

- open institutional need;
- active event or recovery project;
- known backlog;
- public campaign;
- available civic organization;
- player-authored desire to help;
- documented donation offer;
- recurring stewardship schedule.

Do not create a crisis solely to justify volunteering.

Routine service should compress once the system is mature.

## 25. Open canon decisions

Ouros still needs authored decisions for:

- which regions have formal volunteer organizations;
- whether Pokémon Ranger-like institutions exist and what authority they have;
- whether recurring rescue associations are public, private or mixed;
- how fundraising works culturally;
- whether any formal charitable entities exist;
- what donated goods are common;
- how player-founded service groups are recognized;
- what emergency assignments require actual credentials;
- what privacy expectations apply to service histories;
- whether any institutions publish aggregate service statistics.

Until reviewed, all structures in this file remain proposed.
