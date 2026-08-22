# Ouros Public Art, Murals, Graffiti & Visual Place-Memory Layer

Status: proposed systems design. Not established Ouros canon.

Pass: 102.

## Purpose

This layer owns persistent visual marks attached to shared places: murals, painted walls, sculpture/installations, sanctioned street art, unsanctioned marks, community art, painted wayfinding, restoration layers, temporary visual interventions and Pokémon-made markings when those markings become narratively relevant.

It connects to existing systems without replacing them:

- `architecture-built-environment-adaptive-reuse-layer.md` owns the physical structure/surface;
- `urban-public-space-street-life-layer.md` owns shared-space use;
- `material-culture-economy-crafting-layer.md` owns material/object provenance;
- `fashion-clothing-visual-culture-layer.md` owns personal visual presentation;
- `public-memory-event-legacy-layer.md` owns public memory;
- `photography-visual-evidence-layer.md` owns visual records and derivatives;
- `archives-museums-collections-preservation-layer.md` owns accession/exhibition/collection records;
- `civic-governance-public-works-layer.md` owns formal public projects and authorization;
- `case-authority-custody-layer.md` owns evidence/claims/custody disputes;
- `tourism-visitors-destination-pressure-layer.md` owns visitor pressure;
- `wild-collective-agency-layer.md`, `field-signs-tracking-spoor-layer.md` and ecology layers own wildlife state;
- AutoPTU-Java owns battle rules.

This layer does not define property law, vandalism law, censorship law, protest law, artistic merit, social Skill DCs, object HP, crowd combat, PTU Terrain or Pokémon powers.

## 1. Core separation

Keep these states distinct:

1. physical surface state;
2. mark/artwork identity;
3. current visible revision;
4. prior hidden/removed revisions;
5. creator attribution or creator hypothesis;
6. authorization/commission state;
7. material provenance;
8. depicted subject or claim;
9. actor interpretation;
10. public recognition;
11. conservation/restoration state;
12. Minecraft projection;
13. mechanical PTU state, normally none.

A mural depicting a historical battle does not prove the battle occurred.

A signature does not prove authorship.

A recurring Pokémon pattern does not prove individual identity without corroboration.

A famous artwork does not create reputation points by itself.

## 2. Visual surface

A physical support can accumulate many visual layers.

```yaml
visual_surface:
  surface_id: null
  physical_structure_ref: null
  public_space_ref: null
  surface_type: null
  geometry_ref: null
  current_condition: null
  current_visible_revision_id: null
  mark_layer_ids: []
  restoration_record_ids: []
  photo_refs: []
  access_refs: []
  stewardship_refs: []
  projection_revision_id: null
```

Candidate `surface_type` values:

- WALL
- RETAINING_WALL
- SHUTTER
- BRIDGE_FACE
- TUNNEL_WALL
- PLATFORM_WALL
- ROCK_FACE
- TREE_SURFACE
- PAVEMENT
- SIGNBOARD
- UTILITY_STRUCTURE
- FREESTANDING_PANEL
- OTHER_AUTHORED

A surface may exist before any artwork and after all visible artwork is removed.

## 3. Artwork / mark identity

```yaml
visual_mark:
  visual_mark_id: null
  surface_id: null
  mark_type: null
  created_at_or_window: null
  creator_attribution_state: UNKNOWN
  confirmed_creator_ids: []
  creator_hypothesis_ids: []
  commissioning_actor_id: null
  authorization_state: UNKNOWN
  material_batch_refs: []
  depicted_subject_refs: []
  textual_content_ref: null
  initial_revision_id: null
  current_revision_id: null
  public_memory_refs: []
  significance_state: ORDINARY
  mechanics_state: NONE_ASSUMED
```

Candidate mark types:

- COMMISSIONED_MURAL
- COMMUNITY_MURAL
- UNSANCTIONED_TAG_OR_MARK
- STENCIL
- PAINTED_SIGN
- TEMPORARY_INSTALLATION
- SCULPTURAL_PUBLIC_ART
- MEMORIAL_ARTWORK
- FESTIVAL_DECORATION
- POKEMON_MADE_PATTERN
- CHILDREN_OR_SCHOOL_PROJECT
- ARTIST_STUDY_OR_TEST
- RESTORATION_TEST_PATCH
- OTHER_AUTHORED

`UNSANCTIONED_TAG_OR_MARK` describes authorization state only when established. It does not mean criminality, malicious intent or gang affiliation.

## 4. Revision and palimpsest history

Artwork can change without becoming a new object every time.

```yaml
visual_mark_revision:
  revision_id: null
  visual_mark_id: null
  effective_from: null
  effective_to: null
  visible_extent_ref: null
  appearance_descriptor_ref: null
  condition_state: null
  alteration_type: null
  caused_by_event_refs: []
  actor_refs: []
  material_refs: []
  documentation_refs: []
  supersedes_revision_id: null
```

Candidate alteration types:

- ORIGINAL_EXECUTION
- WEATHERING
- ACCIDENTAL_DAMAGE
- INTENTIONAL_OVERPAINT
- PARTIAL_REMOVAL
- CLEANING
- CONSERVATION
- RESTORATION
- COMMUNITY_UPDATE
- TEMPORARY_COVERING
- BUILDING_MODIFICATION
- UNKNOWN_CHANGE

Chronicle remains append-only. A repaint does not delete the previous revision from history.

Minecraft normally projects only the current visible revision plus authored traces of older layers when desired.

## 5. Attribution and uncertainty

```yaml
creator_hypothesis:
  hypothesis_id: null
  visual_mark_id: null
  proposed_creator_ids: []
  basis_refs: []
  comparison_mark_ids: []
  confidence_state: null
  alternative_hypothesis_ids: []
  reviewed_at: null
```

Evidence may include:

- witnessed creation;
- commission records;
- material provenance;
- photographs;
- consistent individual Pokémon mark patterns;
- signed records;
- stylistic comparison;
- tool/material traces;
- creator admission.

Stylistic similarity alone should not silently become confirmed authorship.

## 6. Pokémon-made visual marks

Pokémon markings require a separate bridge from species lore to local evidence.

```yaml
pokemon_visual_mark_observation:
  observation_id: null
  visual_mark_id: null
  observed_at: null
  observer_ids: []
  proposed_species_id: null
  proposed_pokemon_entity_id: null
  individual_match_state: UNRESOLVED
  comparison_refs: []
  material_observation_refs: []
  location_context_ref: null
  uncertainty_notes: null
```

Valid conclusions may include:

- mark is consistent with a species behavior;
- mark likely predates current settlement use;
- repeated pattern may belong to the same individual;
- material composition changed between observations.

Do not infer:

- ownership of the marked surface;
- current territorial control;
- hostility;
- `Poisoned` exposure;
- `Sketch` use;
- Pack Mon/group mechanics;
- permanent spawn ownership of the area.

## 7. Commission, participation and authorship

A work may have several roles.

```yaml
public_art_project:
  project_id: null
  surface_ids: []
  commissioning_actor_ids: []
  funding_refs: []
  lead_artist_ids: []
  contributor_ids: []
  consultation_refs: []
  design_version_refs: []
  access_refs: []
  preparation_refs: []
  execution_window_ref: null
  completion_record_id: null
  review_record_ids: []
```

Funding does not imply authorship.

Authorship does not imply ownership of the wall.

Participation does not imply endorsement of every depicted claim.

A community work should preserve multiple contributors when known instead of collapsing credit into one celebrity NPC.

## 8. Meaning and depicted claims

```yaml
visual_depiction_claim:
  claim_id: null
  visual_mark_id: null
  subject_type: null
  subject_ref: null
  depicted_assertion: null
  source_context_ref: null
  factual_validation_state: UNASSESSED
  interpretation_refs: []
```

Examples:

- a historical scene;
- a Legendary Pokémon;
- a local founder;
- a migration route;
- an environmental warning;
- a memorial subject;
- an imagined scene.

Authenticity of the artwork and truth of the depicted claim are different questions.

## 9. Public recognition and landmark use

```yaml
visual_landmark_profile:
  visual_mark_id: null
  local_recognition_state: null
  navigation_use_refs: []
  tourism_refs: []
  media_refs: []
  event_refs: []
  business_frontage_refs: []
  observed_effect_refs: []
```

A mural can become a landmark through repeated use in directions, photos or local speech.

That does not create a formal place name automatically.

If visitor pressure rises, Tourism handles the consequence. If businesses change, Workplaces/Finance/Public Space handle it.

## 10. Conservation, restoration and removal

```yaml
visual_conservation_record:
  conservation_id: null
  visual_mark_id: null
  assessment_at: null
  condition_observations: []
  treatment_options: []
  selected_treatment: null
  authority_refs: []
  steward_refs: []
  performed_work_refs: []
  before_photo_refs: []
  after_photo_refs: []
  unresolved_questions: []
```

Possible choices include stabilizing, cleaning, repainting, exposing an older layer, covering, documenting before removal or taking no action.

The system must not assume preservation is always the correct outcome. A temporary work may be intended to disappear. A surface may need structural repair. A living community may choose to replace an old piece. Those decisions belong to authored/local governance state.

## 11. Visual marks as environmental storytelling

A visual element can be a clue only when connected to actual state.

Good generation chain:

`existing Chronicle fact or unresolved claim`
→ `surface/mark with provenance`
→ `player observes it`
→ `interpretation or investigation hook`
→ `corroboration from archives/actors/materials`
→ `updated knowledge`

Bad generation chain:

`generator wants mystery`
→ `random ominous mural`
→ `retroactively invent ancient conspiracy`.

## 12. Minecraft projection

Minecraft is presentation, not authority.

A projection may use:

- map-art/image assets;
- banners/signs;
- custom blocks/models;
- decals/particles where available;
- reconstructed painted geometry;
- temporary event decorations;
- protected interaction zones.

The server must keep `visual_mark_id`, revision and provenance outside the render artifact.

Chunk reload must not:

- restore a removed mural;
- erase a new overpaint;
- duplicate an installation;
- reset weathering/restoration state;
- lose contributor history;
- transform a temporary work into a permanent one.

## 13. Player-created work

Player artwork can become powerful shared-world state but requires moderation and consent boundaries.

Candidate lifecycle:

`player proposes / creates private draft`
→ `surface permission or owned-space validation`
→ `content moderation / multiplayer safety review`
→ `execution`
→ `persistent visual_mark_id`
→ `revision history`.

No player should be able to overwrite another player's authored work, memorial, private home surface or protected public project merely by placing blocks.

Detailed moderation policy remains a separate product decision.

## 14. Encounter contracts

### A. Underpass Mural Restoration — FULL

Narrative premise: a damaged underpass artwork is being documented and stabilized while a separate conflict develops nearby.

Desired full tactical behavior:

- protected conservation work area;
- civilians/workers with withdrawal behavior;
- object/zone preservation objective;
- possible alternate movement paths;
- tactical AI understands AVOID_WORK_ZONE / WITHDRAW / CLEAR_EXIT;
- Minecraft reflects temporary scaffolding and barriers.

Permanent capability dependencies:

- targeting/footprints/range/LoS — VERIFIED foundation;
- base movement legality — VERIFIED foundation;
- complete movement including interception/forced movement — BLOCKING for moving workers and protected routing;
- core calculations — VERIFIED foundation;
- action economy/initiative — VERIFIED foundation;
- full turn/round lifecycle — PARTIAL if timed effects are added;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL only if exact statuses are used;
- terrain/weather/hazards/zones/reactions — BLOCKING for protected work zones or temporary hazards;
- move-specific behavior — PARTIAL, exact Moves must be verified;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

Reduced version:

Workers leave the tactical area before battle. Scaffolding and the mural remain noninteractive world objects. AutoPTU receives a static arena with only legal combatants. After battle, world state records whether restoration work was delayed, resumed or changed.

### B. Grafaiai Mark Survey — FULL

Narrative premise: researchers are comparing a recurring pattern across several forest surfaces while the suspected Pokémon may still be nearby.

Desired full version:

- wildlife may withdraw rather than fight;
- moving observation objective across several marked surfaces;
- objective-aware AI avoids forcing every encounter to KO;
- if an exact poisonous-contact mechanic is ever relevant, it must come from verified PTU rules rather than the mark description.

Dependencies:

- VERIFIED: targeting/geometry, base movement, core calculations, initiative, legal-action infrastructure;
- PARTIAL: lifecycle, damage, statuses, move-specific behavior, abilities, items, Trainer Features;
- BLOCKING: complete movement if dynamic withdrawal/pursuit is required, tactical environmental zones if marks become interactable, tactical AI, Minecraft playback.

Reduced version:

Survey and identity comparison occur in overworld state. If a battle occurs, it is a conventional static encounter. Marks have no tactical poison effect. A Pokémon may leave through narrative/world-state resolution before battle begins.

### C. Plaza Overpaint Dispute — FULL

Narrative premise: two incompatible claims exist about which visual layer should remain visible while a public event creates pressure around the site.

Full version may include:

- crowd evacuation;
- protected surface objective;
- several exits;
- non-KO de-escalation goals;
- dynamic barriers or temporary event objects.

Dependencies:

- VERIFIED foundations: targeting, base movement, core calculations, initiative, legal-action infrastructure;
- PARTIAL: lifecycle/damage/statuses/Move/Ability/Item/Feature slices as actually used;
- BLOCKING: complete movement/interception, terrain/zones/reactions if barriers matter tactically, tactical AI, Minecraft playback.

Reduced version:

The dispute, evidence review and public event are resolved in overworld state. Civilians leave before any battle. AutoPTU only handles a conventional confrontation if one still occurs.

## 15. Explicit no-inference rules

Do not infer:

- mural = historical truth;
- old = sacred;
- sanctioned = popular;
- unsanctioned = malicious/criminal;
- public = owned by government;
- signature = authentic;
- overpaint = destruction of all prior evidence;
- restoration = return to original meaning;
- Pokémon mark = individual identity;
- Grafaiai mark = Poison hazard;
- Smeargle mark = Sketch use;
- artwork = morale/reputation modifier;
- painted line = tactical zone;
- statue = cover;
- famous wall = fast-travel unlock;
- visitor photos = tourism success;
- player artwork = canon automatically.

## 16. Canon questions

Before promotion, Ouros needs authored answers for:

- which settlements have longstanding public-art traditions;
- which walls/structures are legitimate shared canvases;
- what authority, if any, governs commissions/removal;
- how local customs treat unsanctioned marking;
- whether player-created shared artwork is permitted;
- which Pokémon markings are known ecological signs;
- which historic works predate the player era;
- what works are memorial, sacred, civic, commercial or temporary;
- how much old visual history Minecraft should expose physically;
- which PTU/Caelo Skills/Features can support restoration, artistic practice or visual analysis without inventing mechanics.
