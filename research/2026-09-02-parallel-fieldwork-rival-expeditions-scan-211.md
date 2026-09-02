# Parallel Fieldwork and Rival Expeditions Scan 211

Status: RESEARCH / NON-CANON
Date: 2026-09-02

## Scope

This pass examines a narrative structure not covered by scans 207-210: several legitimate field parties using the same route or site during overlapping windows, sometimes cooperating and sometimes competing, without making one party an automatic villain. The goal is to support persistent expeditions, shared sites, prior visitation, handoffs, contested scheduling and recurring professional rivalry while keeping world truth separate from credit, arrival order and social interpretation.

Existing Ouros constraints were checked before deriving proposals. Marea Interior already gives Mara Veyra responsibility for route checks and practical field assistance, Dr. Nerea Sol responsibility for longitudinal ecological/weather observation, Ema Rey responsibility for transect work, and Pia Min responsibility for document courier work. Sendero del Vidrio already contains fixed lower-shelf, seasonal-crossing and upper-junction anchors. The questline taxonomy already defines EXPLORATION, RIVAL, FACTION, CHARACTER and RELATIONSHIP surfaces and requires reuse of existing entities. No new faction, settlement or resident is required for this pattern.

The canonical lower-shelf Fletchling remains one specific persistent encounter slot with a frozen PTU 1.05 blueprint. A parallel expedition may observe or pass through that location only if current world state permits it. It may never spawn a duplicate of that individual or infer that battle, capture or disappearance resolves an unrelated expedition objective.

## Public research

### Pokémon Mystery Dungeon: Explorers of Time/Darkness/Sky — guild expedition structure

Sources:
- Bulbapedia, Wigglytuff's Guild: https://bulbapedia.bulbagarden.net/wiki/Wigglytuff%27s_Guild
- Neoseeker walkthrough, Explorers of Time/Darkness expedition sequence: https://www.neoseeker.com/pokemon-mystery-dungeon-explorers-of-darkness/faqs/191827-pokemon-mystery-dungeon-dt-g.html

Reusable structure: a larger expedition can split into smaller groups for mobility, move through different legs of a route, and later converge on the same objective. Membership in the same expedition does not require every subgroup to experience the same events. The useful abstraction for Ouros is parallel progress with explicit regrouping and provenance, not the specific characters, destination or plot of Mystery Dungeon.

### Pokémon Mystery Dungeon — institutional exploration teams

Sources:
- Mystery Dungeon Franchise Wiki, Exploration Team Federation: https://mysterydungeonwiki.com/wiki/Pkmn%3AExploration_Team_Federation
- Bulbapedia, Wigglytuff's Guild: https://bulbapedia.bulbagarden.net/wiki/Wigglytuff%27s_Guild

Reusable structure: exploration can be recognized institutionally through team identity, rank, equipment and records. Ouros should use only the structural lesson: authenticated parties can leave attributable records and have continuing professional histories. Arrival order, institutional status and rank must not become truth authority or ownership of a public site.

### West Marches / living-frontier expedition play

Source:
- Rebel Raven Gaming, Edgewall living-frontier campaign description: https://rebelravengaming.com/edgewall

Reusable structure: expedition-based play becomes more legible when the world persists between outings, parties choose jobs and routes, and later groups inherit the consequences of earlier visits. Ouros can use persistent site state and authenticated visit records without importing a fantasy frontier setting, lethality assumptions or campaign procedures.

## Derived Ouros design lessons

A site should preserve who visited, when, for what declared purpose and what authenticated observations or writes resulted. `SITE_VISIT_RECORD` must not contain a hidden flag equivalent to `FIRST_VISITOR_WAS_CORRECT`.

An `ACCESS_WINDOW` can represent a tide, weather-safe period, scheduled instrument interval, ferry window, maintenance closure or authored event window. Missing a window can transform logistics, evidence quality or relationship history. It does not need to force a battle timer.

A `TASK_INTENT` belongs to the party performing the work. Two parties can stand at the same crossing while pursuing different minimum-success conditions. Mara can be checking safe passage while Nerea/Ema are protecting longitudinal measurement consistency. Neither mandate subsumes the other.

A `HANDOFF_RECORD` transfers custody of a document, sample container, instrument or message while preserving origin and provenance. Custody transfer does not transfer authorship, truth authority or ownership of the underlying observation.

A prior visit can change a location. Useful persistent traces include a signed field tag, completed measurement, replaced marker, closed path, borrowed instrument, cached note, temporary detour or a recorded absence. These effects should be explicit world writes rather than inferred from Minecraft block/entity state alone.

Professional rivalry can emerge from incompatible priorities, limited windows, credit, technique or repeated comparison. It should be earned by history. The RIVAL questline tag does not require hostility and should not be applied merely because two NPCs want the same time slot.

Parallel parties must not receive omniscient off-screen tactical simulation. Until an authoritative world-simulation contract exists, their progress should come from authored event transitions, scheduled state machines and explicit evidence-bearing writes. If a party enters battle, AutoPTU remains the only authority for battle facts.

## Candidate state contracts

```yaml
SITE_VISIT_RECORD:
  visit_id: null
  site_id: null
  actor_or_party_ids: []
  arrived_at: null
  departed_at: null
  declared_task_intent_ids: []
  authenticated_outputs: []
  world_writes: []

ACCESS_WINDOW:
  window_id: null
  site_id: null
  opens_at: null
  closes_at: null
  reason_ref: null
  requirements: []
  consequences_if_missed: []

TASK_INTENT:
  intent_id: null
  owner_ids: []
  site_id: null
  purpose: null
  minimum_success_condition: null
  authority_scope: []

HANDOFF_RECORD:
  handoff_id: null
  object_id: null
  from_id: null
  to_id: null
  provenance_refs: []
  custody_changed: true
  authorship_changed: false
  truth_authority_changed: false
```

These are proposal-level schemas. They do not modify canon or establish runtime APIs.

## PTU / Caelo / project cross-check

The project already freezes PTU mechanics only where an explicit source/profile is selected. The first wild Fletchling demonstrates the boundary: movement values, Ability and Moves come from the supplied PTU 1.05 source for that exact blueprint, while Caelo/Kairos material is comparative unless separately approved. This scan therefore assigns no new Skill, Edge, Feature, Move, Ability, equipment effect or field-action DC to expedition work.

Before a field task receives mechanical gating, the supplied PTU/Caelo/Kairos sources must be checked for the exact Skill/Feature/equipment interaction and a rules profile must select the authority. Social or professional competence in prose cannot silently grant a Trainer Feature.

## Battle-capability dependency boundary

The narrative pattern itself can run without combat. A mechanically rich shared-site encounter may depend on all permanent capability families if wild actors, tactical objectives and reactive positioning are enabled. Exact classification is recorded in `design/engine-readiness-snapshot-pass-211.md`.

A reduced version must use authenticated visits, explicit access windows, authored handoffs and ordinary world movement. Optional battles remain separate audited BattleSpecs. Their outcome cannot decide observation provenance, professional credit or the truth of a field hypothesis.

## Provenance and canon boundary

Everything in this file is research or derived design guidance. No source plot, character, dialogue, faction or distinctive location is imported. No Ouros canon file is changed by this scan. New world facts require a separate explicit canon approval.