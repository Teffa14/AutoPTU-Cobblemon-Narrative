# Social Bonds, Mentorship & Clubs Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros needs social persistence that can support friendships, rivalries, professional respect, mentorship, clubs, cohorts and Trainer/Pokémon bonds without flattening every relationship into one meter or taking authorship away from players.

The system should remember what people actually experienced together, let institutions connect characters over time, and use those facts to create future opportunities.

## 1. Relationship records are multidimensional

A relationship record stores several independent dimensions rather than one affection score.

Suggested dimensions:
- familiarity
- trust
- respect
- tension
- debt
- dependence
- authority
- mentorship
- cooperation_history
- conflict_history

Not every relationship uses every field.

Example:

```yaml
relationship_id: rel_001
subject_a: npc_or_pc_id
subject_b: npc_or_pc_id
relationship_kind: peer
familiarity: 3
trust: 1
respect: 4
tension: 2
debt: 0
authority: null
mentor_direction: null
shared_event_ids: []
known_preferences: []
known_boundaries: []
last_meaningful_contact: null
status_notes: []
provenance_refs: []
```

Values are implementation placeholders, not canon mechanics.

## 2. Facts before feelings

The narrative engine should separate observable social evidence from inferred internal state.

Observable facts:
- fought alongside one another
- completed a field project
- received help
- declined an invitation
- publicly disagreed
- shared confidential information
- repaid a debt
- trained together
- competed repeatedly
- rescued the other's Pokémon

Inferred states such as love, hatred, jealousy, forgiveness or betrayal should only become canon when authored or explicitly expressed by the relevant character.

NPCs may have authored internal states. PCs do not.

## 3. Player agency boundary

The system may record that two PCs:
- traveled together;
- won or lost together;
- exchanged items;
- supported opposing factions;
- participated in the same club;
- disagreed publicly.

The system must not automatically declare that those PCs:
- are friends;
- are romantic partners;
- hate each other;
- forgave each other;
- betrayed each other;
- became mentor and student.

Those labels require player action or explicit consent.

## 4. NPC memory packets

Important NPCs should carry bounded memories that can influence future interaction.

```yaml
npc_memory:
  subject_id: player_or_entity
  event_id: null
  memory_type: assistance|conflict|promise|lesson|competition|discovery|gift|warning
  confidence: high
  emotional_tag: authored_optional
  public: false
  decay_policy: persistent
  callback_weight: 3
```

The engine should prefer concrete event callbacks over generic praise or hostility.

## 5. Conversation topic graph

Dialogue options can be generated from facts known by both the player and NPC.

Topic sources:
- shared events
- known people
- known Pokémon
- institutions
- locations
- rumors
- discoveries
- public events
- current cases
- faction developments
- club projects
- unresolved promises

A new discovery can unlock new questions for several NPCs without requiring a handcrafted dialogue branch for each one.

The system should also track when an NPC refuses, cannot answer, or disagrees.

## 6. Mentorship is directional but reversible

Mentorship records should identify:
- mentor
- learner
- competency/domain
- relationship basis
- current goal
- shared exercises or field tasks
- demonstrated milestones
- unresolved disagreement
- completion or transition state

A relationship can contain multiple mentorship directions.

Example: one Trainer may mentor another in field medicine while learning competitive tactics from them.

## 7. Distributed mentorship

Do not force every character into a single master/apprentice relationship.

A Trainer may have:
- a battling coach;
- a research supervisor;
- a peer who teaches local ecology;
- a craft specialist;
- an older Ranger contact;
- a Pokémon whose behavior changes the Trainer's assumptions.

This creates a social network of expertise.

## 8. Competency opportunities, not free progression

The narrative layer may propose opportunities such as:
- supervised field practice;
- observation exercises;
- sparring;
- research assignments;
- apprenticeship work;
- joint expeditions;
- presentations;
- teaching a novice;
- solving a practical problem.

It must not directly grant PTU Skill Ranks, Edges, Features, Tutor Moves or other mechanical benefits unless the governing rules and implementation explicitly authorize them.

## 9. Clubs as persistent institutions

A club is a small institution built around a shared practice, interest or goal.

```yaml
club_id: null
name: null
purpose: null
home_location_id: null
member_ids: []
roles: []
resources: []
facilities: []
projects: []
reputation: {}
alliances: []
rivalries: []
mentor_ids: []
recruitment_state: open
history_event_ids: []
```

Possible club domains:
- battling
- contests
- ecology
- archaeology
- rescue
- photography
- breeding/care
- crafting
- cooking
- exploration
- urban service
- folklore
- journalism
- performance

These are narrative categories only until mechanics are defined.

## 10. Player-created clubs

Where implementation permits, players should be able to found or reshape clubs.

Founding inputs:
- purpose
- minimum founding members
- meeting place
- first project
- resource needs
- initial public standing

Growth should come from completed projects and social consequences rather than passive level thresholds alone.

## 11. Club projects

Projects are collaborative objectives that can combine several activity types.

Examples:
- restore a neglected training ground;
- document a migration;
- host a tournament;
- prepare a public exhibition;
- map a cave safely;
- support a local festival;
- investigate a recurring rumor;
- mentor beginner Trainers;
- build a workshop or research station.

Projects can emit persistent changes to facilities, NPC schedules, reputation, world knowledge and available jobs.

## 12. Shared spaces

A club room, workshop, common hall, field station or café can become a high-value social anchor.

Persistent state may include:
- decorations
- trophies
- notices
- contributed equipment
- guest schedule
- project board
- photographs
- memorials
- research samples

Minecraft can express these changes physically.

## 13. Cohorts and peer networks

Cohorts may form through:
- class year
- expedition intake
- guild membership
- regional program
- temporary training camp
- research cohort
- tournament circuit
- disaster-response deployment

Cohorts create repeated contact without predetermining who becomes close.

## 14. Social opportunity generation

A social event should be generated because of state, not because an NPC randomly wants to talk.

Triggers may include:
- recent shared success
- unresolved disagreement
- mentor milestone
- club project deadline
- new member arrival
- public event
- faction shift
- returning NPC
- long absence
- changed settlement state
- discovery connected to a character's expertise

## 15. Absence and distance

A relationship can cool, become uncertain or simply pause when characters stop interacting.

Do not automatically interpret absence as rejection.

Possible states:
- dormant
- waiting_on_response
- geographically_distant
- schedule_conflict
- intentionally_avoiding
- unresolved

Only authored evidence should choose among them.

## 16. Rivalries

A rivalry can combine competition and respect, or competition and hostility.

Track separately:
- competitive history
- score/history of contests or battles
- respect
- strategic adaptation
- public attention
- personal conflict

A rival should not be forced into enemy status.

Caelo's existing Rivalry rules are a potential mechanical reference but should not be copied automatically until Ouros decides which Caelo homebrew carries forward.

## 17. Trainer/Pokémon bond state

Trainer/Pokémon relationships are distinct from human social relationships.

Narrative bond state may remember:
- origin of partnership
- shared milestones
- fear or trauma triggers if authored
- preferred activities
- trust-building events
- major rescues
- separations/reunions
- training breakthroughs
- places associated with the bond

Mechanical Loyalty/Friendship effects must come from PTU/Caelo rules, not from this narrative layer.

## 18. Supporting cast agency

Trusted NPCs, clubmates or apprentices can undertake bounded operations while players are elsewhere.

Such operations need:
- explicit objective
- capabilities/resources actually available
- risk level
- possible outcomes
- world-state effects
- provenance record

They must not silently solve major player-owned arcs.

## 19. Teaching as progression content

Advanced players can eventually become mentors.

Teaching opportunities can test knowledge through:
- demonstration
- supervised practice
- field leadership
- judging
- reviewing evidence
- preparing another Trainer for a challenge

This creates late-game social progression without requiring power inflation.

## 20. Institution continuity

A school, club, guild or research team should survive staff changes.

Track:
- institutional practices
- archives
- facilities
- alumni
- open projects
- traditions
- leadership succession

A mentor leaving can create change without deleting the community around them.

## 21. Social privacy

Some information should remain scoped.

Possible visibility:
- private_to_character
- private_to_relationship
- club_only
- institution_only
- party_shared
- public

Minecraft UI, quest logs and AI generation should respect those scopes.

## 22. Multiplayer consent rules

Before implementing automated PC-to-PC social systems, define hard consent boundaries.

Recommended defaults:
- no automated romance labels;
- no generated PC internal emotions;
- no unilateral relationship-state declaration;
- no private-message inference into public state;
- shared events may be logged factually;
- player-authored labels override generated inference.

## 23. Relationship callback selection

The generator should prefer callbacks that are:
- supported by actual events;
- relevant to current context;
- not overused;
- changed by elapsed time;
- useful to current player goals.

Avoid constant NPC recognition spam.

## 24. Data integration with existing Ouros layers

This layer should connect to:
- Chronicle events from `ouros-narrative-architecture.md`;
- faction and actor state from `world-agency-layer.md`;
- public reputation from `public-memory-event-legacy-layer.md`;
- profession and workshop relations from `material-culture-economy-crafting-layer.md`;
- case roles from `case-authority-custody-layer.md`;
- research/field reports from `observation-settlement-time-layer.md`;
- tradition keepers from `myth-archaeology-sacred-sites-layer.md`.

It should not duplicate those systems.

## 25. Minecraft representation

Potential overworld expressions:
- members physically gathering in a club room;
- notice boards changing with projects;
- mentor NPC schedules;
- returning alumni;
- invited specialists;
- trophies and photographs;
- shared workshop upgrades;
- NPCs greeting or avoiding players based on validated state;
- group expedition staging areas.

## 26. AutoPTU boundary

AutoPTU may eventually expose battle outcomes and team usage as relationship evidence.

The narrative system can record:
- fought together;
- protected an ally;
- repeatedly faced one another;
- used a particular Pokémon frequently.

It must not infer hidden emotion from battle telemetry.

## 27. Promotion rules

Automated research may create social proposals, but canon promotion should verify:
1. relationship state is supported by evidence or authored intent;
2. PC agency is preserved;
3. no unsupported mechanical reward is granted;
4. institution fits established Ouros geography and culture;
5. private information remains properly scoped;
6. external inspiration has been transformed and attributed.

## Open implementation questions

- Which PTU Loyalty rules and Caelo changes are intended for Ouros?
- Does AutoPTU already persist trainer/Pokémon relationship state?
- Can players found clubs directly in Minecraft?
- Should mentor availability depend on schedules, reputation, competency or all three?
- How should multiplayer social privacy be stored and synchronized?
- What UI communicates relationship change without exposing exploitable numeric meters?
- How can supporting-cast operations resolve safely without simulating full battles off-screen?
