# Rivalry & Recurring Peer Progression Extension

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already stores multidimensional relationships, formal battle records, recurring public events, antagonistic plans and institutional progression. This extension gives recurring competitive peers a continuity model that can connect those systems without duplicating them.

A rival is treated here as an actor with persistent competitive history, independent goals and repeat contact. Rivalry may be friendly, tense, professional, ideological, temporary or mixed. It does not imply enemy status, friendship or a combat bonus.

## 1. Rivalry record

```yaml
rivalry_record:
  rivalry_id: null
  participant_ids: []
  active_domains: []
  first_contact_event_id: null
  competitive_event_refs: []
  shared_event_refs: []
  public_record_refs: []
  known_style_tags: {}
  unresolved_promises: []
  open_challenges: []
  current_contact_state: active
  current_context_ref: null
  last_meaningful_contact: null
  next_plausible_contact_windows: []
  provenance_refs: []
```

Candidate `active_domains`:
- formal battling
- informal battling
- research
- exploration
- rescue
- performance
- athletics
- institutional selection
- craft or professional work
- public problem solving

These are narrative tags only.

## 2. Rivalry does not own relationship state

Respect, trust, tension, debt, cooperation and conflict remain in `social-bonds-mentorship-clubs-layer.md`.

The rivalry record stores competitive continuity and links to those facts.

Hard rules:
- do not infer friendship from repeated battles;
- do not infer hostility from disagreement;
- do not infer jealousy from competition;
- do not convert public prestige into private emotion;
- do not award mechanics from rivalry intensity.

## 3. Independent peer agenda

```yaml
peer_agenda:
  actor_id: null
  current_goals: []
  current_location_ref: null
  institution_refs: []
  route_or_schedule_refs: []
  active_projects: []
  active_challenges: []
  blockers: []
  travel_intent: null
  player_relevance: low
```

A rival should have reasons to exist when the player is elsewhere.

A future meeting is plausible when agenda overlap occurs through:
- same institution;
- same public event;
- shared case or expedition;
- common route;
- qualification window;
- mutual contact;
- public invitation;
- unresolved challenge;
- crisis deployment;
- overlapping professional work.

Random checkpoint appearances should be avoided.

## 4. Encounter callback packet

Before generating a recurring-peer scene, compile only facts the peer can legally know.

```yaml
rival_callback_packet:
  actor_id: null
  player_id: null
  directly_observed_events: []
  public_battle_records: []
  public_media_refs: []
  shared_witness_events: []
  authored_messages_received: []
  confirmed_team_reveals: []
  stale_information: []
  rumors: []
  private_unknowns: []
```

The rival may react to stale or incorrect information if that is genuinely what they know.

## 5. Competitive history

A rivalry should reference authoritative result objects instead of storing a second combat log.

```yaml
competitive_history_entry:
  event_id: null
  format_ref: null
  domain: null
  authoritative_result_ref: null
  participant_ids: []
  observed_turning_points: []
  information_revealed: []
  public_visibility: null
  followup_hook_refs: []
```

For formal battles, use battle-institution records.
For non-battle competition, use the governing system’s result object.
For unresolved or interrupted contests, store that state explicitly.

## 6. Rival adaptation boundary

A rival may adapt narratively based on observed history.

Valid adaptation examples:
- trains a publicly revealed weakness;
- changes which legal Pokémon they choose to bring;
- seeks a mentor;
- joins a different institution;
- stops accepting a format they dislike;
- studies public footage;
- chooses a venue better suited to their stated goal;
- asks for a different approved challenge contract.

Invalid automatic adaptation:
- reading the player’s hidden moveset;
- gaining arbitrary levels or stats to preserve difficulty;
- receiving custom Moves, Abilities or items;
- counter-picking from private inventory;
- gaining unimplemented Caelo Rivalry bonuses;
- changing AI weights without an approved policy.

## 7. Rival contact states

Suggested narrative states:
- ACTIVE
- DISTANT
- OCCASIONAL
- DORMANT
- TEMPORARY_ALLY
- TEMPORARY_OPPOSITION
- SAME_TEAM
- INSTITUTIONAL_PEER
- UNAVAILABLE
- WITHDRAWN_FROM_COMPETITION
- RELATIONSHIP_REVIEW_REQUIRED

These states do not replace social or faction state.

## 8. Rivalry arc phases

A rivalry arc can use flexible phases without requiring all of them:

1. Recognition — the actors notice meaningful overlap.
2. Comparison — a first result or disagreement gives the relationship a competitive dimension.
3. Independent growth — both pursue goals elsewhere.
4. Recontact — changed circumstances produce a new meeting.
5. Adaptation — one or both respond to observed history.
6. Divergence — careers, methods or priorities separate.
7. Convergence — a major event brings them together again.
8. Transformation — rivalry changes domain, intensity or practical role.

No phase implies a required emotional outcome.

## 9. Losses and non-blocking outcomes

A recurring-peer battle should only gate progress when a reviewed contract says it does.

Otherwise a loss may produce:
- a different public record;
- a training request;
- a changed invitation;
- a later rematch opportunity;
- a peer reaching an opportunity first;
- a different conversation callback;
- a changed bracket or event position;
- no mechanical consequence beyond the actual battle result.

This keeps rivalry from becoming forced reload content.

## 10. Multiple rivals as a peer network

```yaml
peer_network:
  network_id: null
  member_ids: []
  shared_institution_refs: []
  shared_event_refs: []
  active_pairwise_rivalry_refs: []
  group_projects: []
  public_standings_refs: []
  current_convergence_reason: null
```

The player should not be the only center of competition.

Peers may:
- battle one another;
- cooperate without the player;
- share mentors;
- disagree about the player;
- enter the same tournament;
- split into different careers;
- become teammates temporarily;
- miss an event because another obligation takes priority.

Off-screen results require an approved source of authority. Do not fabricate exact PTU outcomes merely to advance a bracket.

## 11. Rivalry and antagonism

A recurring rival becomes an adversarial actor only when actual goals conflict in a way covered by `antagonist-agency-defection-escalation-layer.md`.

A hostile rival may still use this continuity layer for competitive history while the antagonist layer owns plans, escalation, resources and opposition methods.

This prevents the rivalry system from becoming a hidden villain generator.

## 12. Rivalry and mentorship

A stronger peer can teach or coach without ending rivalry.

Mentorship direction remains in the social layer.

A useful pattern is:
- rival observes a failure;
- rival offers an authored or state-supported training opportunity;
- player may accept or decline;
- training itself uses governing progression rules;
- later rematch checks only legal authoritative state.

No free Edge, Feature, Tutor Move or stat increase is created by narrative coaching.

## 13. Rivalry and public memory

Public attention belongs to the public-memory/media systems.

A rivalry can have:
- low private intensity and high media attention;
- high personal importance and little public awareness;
- a public nickname not used privately;
- conflicting media narratives;
- records that outlive current contact.

The generator should never make media framing canonical truth about private motives.

## 14. Recontact scheduler

A lightweight recontact candidate should be generated only when at least two signals align.

Candidate signals:
- same location window;
- shared event registration;
- unresolved promise or invitation;
- institution asks both actors to participate;
- public qualification milestone;
- overlapping route or expedition;
- shared mentor availability;
- crisis or public-work duty;
- new public result relevant to both;
- long absence plus plausible communication route.

Then evaluate:
- does the rival know enough to act?
- do they have time and access?
- does this callback add new information, decision or consequence?
- has this pattern been overused recently?

If not, compress or skip the scene.

## 15. Minecraft representation

Possible visible expressions:
- rival NPC appears at a shared institution because their schedule places them there;
- notice board shows both actors registered for the same event;
- trophy/archive display reflects prior authoritative results;
- peer leaves for another region or job and is physically absent;
- training ground occupancy changes before a rematch;
- rival’s publicly known team members appear only when the adapter can represent them accurately;
- letters/messages or public notices provide recontact without teleporting the NPC into the player’s path.

Until adapter/playback support is verified, these remain narrative/world-state outputs rather than authoritative Minecraft mechanics.

## 16. Encounter implementation contract — Crossroads Rematch

Narrative premise:
Two recurring peers meet again during an ordinary route overlap. Both have changed since their previous battle. The result matters to their shared history but does not gate regional progression.

Full intended version:
- approved legal teams derived from current authoritative state;
- arena reflects actual route terrain/weather if supported;
- rival AI may prioritize known tactical goals based on observed information;
- switching and move selection respond to approved tactical policy;
- public spectators may create record visibility without affecting mechanics;
- post-battle callbacks use exact revealed information.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if selected legal content requires it
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if route conditions enter tactical resolution
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced executable version:
Freeze a static legal arena and choose only Pokémon, Moves, Abilities, Items and Trainer mechanics individually verified for the current vertical slice. Ignore route weather/terrain tactically unless verified. Use legal-action infrastructure without pretending the rival has strategic adaptation. Record the authoritative result and revealed information afterward. The narrative premise remains a meaningful rematch between changed peers.

## 17. Encounter implementation contract — Rival Team-Up Under Pressure

Narrative premise:
Two competitors temporarily cooperate during a local incident because their immediate goals align.

Full intended version:
- both Trainers and their Pokémon share a tactical side;
- protect/escape or containment objective;
- interception and forced movement may matter;
- hazards or changing zones may alter priorities;
- allied AI coordinates around objectives while preserving each actor’s information limits;
- post-scene rivalry state records cooperation without inferring friendship.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING if used
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — PARTIAL
- Trainer Features/perks — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING

Reduced executable version:
Resolve evacuation, containment or route state before combat. Instantiate only a static ordinary team battle with legal verified combatants. Do not script interception, civilians, dynamic hazards or objective-aware coordination. Afterward, record that the rivals fought on the same side and keep emotional interpretation separate.

## 18. Noncombat encounter — Competing Field Claim

Narrative premise:
Two peers independently investigate the same phenomenon and disagree about interpretation or publication priority.

This can run now as narrative state if it uses:
- actual observations;
- timestamps;
- provenance;
- actor knowledge;
- institution policy if established;
- public-memory/media outputs where appropriate.

It must not invent research ownership law, publication rights, academic misconduct rules or institutional authority. If the dispute becomes formal, hand off to the relevant case/governance/agreement system.

## 19. Engine evidence boundary

Pass 59 inspected AutoPTU-Java through commit `149254ca0f54c6b8a35a25a57a7c872e50ce042e`, which ports Focused Training Accuracy bonus resolution using authoritative runtime state and parity tests.

This strengthens one exact Trainer-Feature/Accuracy slice. It does not promote the whole Trainer Features/perks family because the Java README still lists move, ability, item, perk and Trainer Feature hook registries as unfinished.

AutoPTU Python was inspected through `6f2072d308ee777b5574eb69d08bd23c85af58da`, which adds browser API timeout handling and explicitly does not change combat rules.

## 20. Promotion rules

A recurring rival concept may enter future canon only after review confirms:
- the actor fits established geography/institutions;
- repeat contact has a plausible cause;
- relationship labels are evidence-backed or authored;
- competitive results point to authoritative records;
- no hidden scaling or unsupported progression is used;
- public/private knowledge boundaries are respected;
- any Caelo Rivalry mechanics have explicit carry-over approval;
- mechanically rich scenes use verified engine capabilities or the reduced contract.

## Open questions

- Which existing Ouros institutions naturally create recurring peer cohorts?
- Is Caelo Rivalry intended to carry into Ouros mechanically?
- Should open challenges expire, persist indefinitely or depend on authored context?
- How should a rival’s public scouting packet be surfaced to players?
- What policy resolves NPC-vs-NPC formal battles when the player is absent?
- How many concurrent recurring peers can remain legible before callback density becomes noise?
