# Fashion, Clothing & Visual Culture Layer

Status: proposed systems design. Not established Ouros canon.

## Purpose

Ouros already tracks material provenance, crafting, professions, performances, institutions, social history, public memory, accessibility and infiltration. This layer gives clothing and visual presentation their own persistent state without turning appearance into a hidden combat stat or a universal social score.

The system should support:

- personal wardrobes;
- garments and accessories with provenance;
- outfits assembled from several pieces;
- regional and settlement visual cultures;
- uniforms and occupational clothing;
- designers, tailors, stylists, dyers, groomers and related workplaces;
- commissions, repairs and alterations;
- fashion events and editorial/media activity;
- historical garments and replicas;
- adaptive and protective clothing;
- costumes and stagewear;
- disguises as presented identity;
- Pokémon garments or grooming when welfare and species fit are supported.

It does not grant PTU mechanics unless an authoritative PTU/Caelo rule explicitly does so.

## 1. Core separation

Keep these states distinct:

1. Physical garment state — what object exists and its condition.
2. Mechanical equipment state — any rules-authoritative effect, if one exists.
3. Appearance description — what the piece or ensemble visibly looks like.
4. Wear state — who is currently wearing it.
5. Presented identity — what the wearer is trying to communicate.
6. Observer interpretation — what another actor thinks the appearance means.
7. Institutional meaning — whether a uniform or credential is authorized.
8. Public recognition — whether the look is famous or locally recognizable.
9. Personal meaning — only what a player or authored NPC state explicitly establishes.

Appearance never writes directly into canonical motive, affiliation, personality or morality.

## 2. Garment instance

A persistent garment is an extension of the existing material-culture item instance.

```yaml
garment_instance:
  garment_id: null
  mechanical_item_ref: null
  garment_type: null
  current_owner_id: null
  current_custodian_id: null
  current_wearer_id: null
  maker_id: null
  workshop_id: null
  source_material_batch_ids: []
  design_pattern_id: null
  size_fit_profile: null
  species_fit_profile: null
  appearance_descriptor_id: null
  condition_state: serviceable
  alteration_record_ids: []
  repair_record_ids: []
  provenance_event_ids: []
  uniform_issue_record_id: null
  cultural_context_ids: []
  accessibility_tags: []
  public_memory_ids: []
  significance: ordinary
  mechanics_validation_state: cosmetic_only
```

Most generic clothing does not need a unique object row. Create a persistent garment when provenance, ownership, wear history, repair, institutional issue, personal significance or a story makes the specific piece relevant.

## 3. Appearance descriptor

Appearance should be structured enough for consistency without turning aesthetic vocabulary into mechanics.

```yaml
appearance_descriptor:
  descriptor_id: null
  silhouette_tags: []
  material_tags: []
  pattern_tags: []
  color_tags: []
  wear_tags: []
  regional_style_refs: []
  institution_mark_refs: []
  visible_damage_tags: []
  customization_notes: []
  authored_visual_ref: null
```

Avoid interpreting descriptors as personality claims.

“dark coat” does not mean secretive.

“expensive fabric” does not mean wealthy.

“old uniform” does not prove current membership.

## 4. Outfit ensemble

An outfit is an assembly state, not another physical item.

```yaml
outfit_ensemble:
  outfit_id: null
  wearer_id: null
  garment_ids: []
  accessory_ids: []
  grooming_profile_ref: null
  intended_context: everyday
  creator_ids: []
  first_worn_event_id: null
  recurring_use_count: null
  public_alias: null
  photo_refs: []
  mechanics_state: none_assumed
```

Candidate contexts:

- everyday;
- travel;
- fieldwork;
- formal;
- performance;
- battle_event;
- workplace;
- institutional;
- ceremony;
- protective;
- disguise;
- leisure.

A player can save several ensembles and change between them without implying a character-development event.

## 5. Wardrobe profile

Wardrobe state belongs to the character/world model, not to one UI screen.

```yaml
wardrobe_profile:
  actor_id: null
  owned_garment_ids: []
  borrowed_garment_ids: []
  stored_location_ids: []
  saved_outfit_ids: []
  frequently_worn_outfit_ids: []
  explicit_preference_notes: []
  privacy_scope: private
  last_changed_at: null
```

Frequently wearing an outfit may make it recognizable. It does not authorize the generator to infer why the player likes it.

## 6. Garment condition and repair

Clothing may accumulate physical history without becoming an armor durability simulator.

Candidate narrative condition states:

- pristine;
- serviceable;
- worn;
- stained;
- torn;
- damaged;
- restoration_needed;
- display_only.

The narrative condition does not alter combat unless an authoritative mechanical item definition explicitly connects to it.

Routine laundry and maintenance should compress. Expand them only when provenance, scarcity, contamination, damage, deadlines, accessibility or a relationship makes the action meaningful.

## 7. Design pattern

```yaml
design_pattern:
  pattern_id: null
  creator_ids: []
  institution_id: null
  origin_location_id: null
  garment_types: []
  material_requirements: []
  visual_motifs: []
  revision_history: []
  authorized_makers: []
  cultural_context_ids: []
  public_status: private|commission|published|institutional|traditional
  source_refs: []
```

A design pattern can be copied, adapted, taught or preserved depending on authored world rules. Do not invent intellectual-property law for Ouros until canon defines it.

## 8. Atelier / fashion workplace

Reuse the existing workplace and workshop layers rather than creating a separate economic simulator.

```yaml
fashion_workplace_profile:
  workplace_id: null
  service_types: []
  designer_ids: []
  maker_ids: []
  apprentice_ids: []
  fitting_space_state: null
  tool_refs: []
  supply_route_ids: []
  material_stock_refs: []
  current_commission_ids: []
  backlog_state: normal
  public_access_state: open
  local_style_refs: []
```

Possible services:

- tailoring;
- alterations;
- repair;
- dyeing;
- embroidery;
- footwear;
- hats;
- uniforms;
- stage costume;
- grooming;
- photography styling;
- adaptive clothing;
- protective fieldwear.

Any mechanically relevant crafted equipment still goes through the existing production validation path.

## 9. Commission record

```yaml
fashion_commission:
  commission_id: null
  client_id: null
  maker_ids: []
  requested_context: null
  requirement_notes: []
  material_batch_ids: []
  pattern_ref: null
  fitting_event_ids: []
  deadline_event_id: null
  completion_state: proposed
  delivered_garment_ids: []
  payment_obligation_ref: null
  provenance_refs: []
```

A client can reject a fit, change a request or miss a deadline without turning the maker into an antagonist.

## 10. Uniform specification

Uniforms are institutional objects, not proof of identity by appearance alone.

```yaml
uniform_spec:
  uniform_spec_id: null
  issuing_institution_id: null
  role_scope: []
  required_elements: []
  optional_elements: []
  visible_mark_ids: []
  safety_requirement_refs: []
  issue_policy_ref: null
  return_policy_ref: null
  active_version: null
  historical_versions: []
```

Keep three facts separate:

- the garment resembles a uniform;
- the garment was genuinely issued;
- the wearer currently holds the associated role.

Only records can establish the latter two.

This directly supports the existing infiltration layer: clothing may affect what observers believe, but it cannot create a free Guile or Stealth success.

## 11. Uniform issue record

```yaml
uniform_issue_record:
  issue_id: null
  institution_id: null
  recipient_id: null
  garment_ids: []
  role_ref: null
  issued_at: null
  returned_at: null
  authorization_state: current
  source_refs: []
```

Former members may possess old uniforms. Museums may own retired uniforms. Replicas may exist. An old uniform is therefore weak evidence of current affiliation.

## 12. Dress code

A dress code is an institutional policy, not a universal moral rule.

```yaml
dress_code:
  dress_code_id: null
  institution_id: null
  context_scope: []
  required_functional_elements: []
  prohibited_safety_conflicts: []
  ceremonial_elements: []
  accommodation_policy_ref: null
  current_revision: null
```

Avoid unnecessary mandatory fashion policing. Dress requirements should have authored cultural, ceremonial, safety or institutional reasons.

Accessibility accommodations override presentation assumptions when the world’s policy permits them.

## 13. Regional visual culture

```yaml
visual_culture_profile:
  culture_profile_id: null
  region_or_settlement_id: null
  common_material_refs: []
  common_silhouette_tags: []
  common_color_sources: []
  craft_tradition_ids: []
  climate_adaptation_refs: []
  occupational_influences: []
  historical_influences: []
  active_style_movements: []
  contested_claims: []
```

This profile describes trends, not mandatory dress. Individuals may ignore, mix or reinterpret local norms.

## 14. Style movement

Fashion changes over time.

```yaml
style_movement:
  movement_id: null
  origin_event_or_place_id: null
  visible_motif_refs: []
  known_creator_ids: []
  adopter_group_refs: []
  media_refs: []
  diffusion_regions: []
  current_state: emerging
```

Candidate states:

- emerging;
- local;
- spreading;
- mainstream;
- declining;
- revived;
- historic.

A movement can spread through media, travel, performers, tournaments, institutions or trade routes. It should not propagate instantly.

## 15. Public recognition of appearance

```yaml
appearance_recognition_record:
  recognition_id: null
  observer_or_audience_id: null
  subject_id: null
  observed_outfit_id: null
  recognition_claim: null
  source_event_id: null
  confidence: null
```

Examples:

- “recognizes this as the coat worn during the finals”;
- “believes this is a harbor service uniform”;
- “recognizes the maker’s stitching style”.

These are claims tied to observers. They do not become universal facts automatically.

## 16. Fashion event

Fashion events can be competitive or noncompetitive.

```yaml
fashion_event:
  event_id: null
  event_type: showcase
  venue_id: null
  host_ids: []
  designer_ids: []
  participant_ids: []
  outfit_ids: []
  theme_ref: null
  judging_rules_ref: null
  media_presence: []
  formal_results: []
  public_reception_refs: []
  archive_refs: []
```

Possible event types:

- showcase;
- runway;
- market fair;
- atelier open house;
- exhibition;
- uniform unveiling;
- historical dress exhibit;
- charity event;
- photography session;
- Contest-related styling event.

If an event uses PTU Contest mechanics, the existing Contest layer remains authoritative.

## 17. Pokémon grooming and clothing

Pokémon visual presentation needs a separate welfare boundary.

```yaml
pokemon_appearance_service:
  service_id: null
  pokemon_id: null
  service_type: grooming|trim|garment_fit|accessory_fit|cleaning
  provider_id: null
  observed_behavior_before: []
  observed_behavior_after: []
  welfare_review_ref: null
  mechanical_effect_ref: null
```

No mechanical effect is assumed.

Do not infer:

- consent from ownership;
- happiness from appearance;
- discomfort solely because the Pokémon removes an item;
- desire to perform because an outfit was prepared;
- species-wide preferences from one individual.

Persistent refusal or discomfort can become an observation and care question without inventing a diagnosis.

## 18. Adaptive and protective clothing

Connect directly to the Accessibility and Hazard layers.

An adaptive garment may exist because it:

- accommodates a mobility aid;
- reduces sensory discomfort;
- supports medical equipment;
- improves ease of dressing;
- offers visibility or tactile identification;
- meets occupational safety requirements.

No benefit is converted into PTU numbers unless rules provide it.

Protective fieldwear can exist narratively, but hazard resistance, damage reduction, weather protection and equipment slots require mechanical validation.

## 19. Disguise boundary

Clothing can change presented identity. It cannot resolve deception by itself.

A disguise interaction can produce:

```yaml
presented_identity_update:
  actor_id: null
  outfit_id: null
  claimed_role: null
  visible_credential_refs: []
  observer_ids: []
  world_context_id: null
```

The infiltration layer determines observer belief and suspicion. Any Guile, Stealth, perception or Feature interaction must come from PTU/Caelo rules and actual character state.

## 20. Historical clothing

Historic garments connect to Archives, Museums, Family/Legacy and Public Memory.

Track:

- confirmed maker;
- provenance;
- confirmed wearer history;
- uncertain wearer claims;
- repairs;
- replicas;
- exhibition history;
- conservation state;
- ownership/custody disputes.

Do not assume an old uniform or ceremonial garment has supernatural or mechanical power.

## 21. Photography and iconic looks

An outfit may become recognizable through a public event or photograph.

Store the event and publication separately.

An iconic image can make a look famous. It does not establish everything claimed in its caption.

## 22. Wear history

```yaml
wear_event:
  wear_event_id: null
  actor_id: null
  outfit_id: null
  location_id: null
  event_id: null
  world_time: null
  public_visibility: null
  source_refs: []
```

Wear history supports callbacks such as:

- a repaired expedition coat returning years later;
- a retired uniform being displayed in an archive;
- a designer recognizing their own old work;
- a recurring rival changing visual presentation over time.

## 23. Minecraft/Cobblemon presentation boundary

Minecraft may eventually render:

- cosmetic clothing slots;
- skins/model layers;
- uniforms;
- shop displays;
- atelier interiors;
- mannequins;
- wardrobe storage;
- event staging;
- grooming variants;
- per-player appearance state.

Minecraft must not become the authority for:

- PTU equipment legality;
- Contest bonuses;
- defensive values;
- disguise success;
- Skill ranks;
- social influence;
- Pokémon welfare state.

The adapter displays validated state and reports player choices back to the authoritative systems.

## 24. Storage and simulation budget

Do not persist every sock, stain or laundry cycle.

Track detail when it has narrative value:

- meaningful provenance;
- distinctive public recognition;
- active commission;
- damage/repair arc;
- institutional issue;
- historical importance;
- accessibility requirement;
- disguise relevance;
- player-marked importance.

Everything else can remain generic wardrobe inventory.

## 25. Suggested generation prompts

When fashion content is generated, ask:

- What physical garment or service exists?
- Who made or issued it?
- Where did the materials come from if provenance matters?
- Is the outfit personal, occupational, ceremonial, performance or protective?
- What does the wearer explicitly intend to communicate?
- What might specific observers reasonably recognize?
- Which meanings are only interpretations?
- Does any mechanical effect require PTU/Caelo validation?
- Does the concept respect accessibility and Pokémon welfare?
- Is this visual culture grounded in an existing place/institution rather than arbitrary decoration?

## 26. Promotion checklist

Before fashion material enters canon:

- originality reviewed;
- cultural references reviewed;
- no copied proprietary outfit design;
- provenance consistent with material-culture state;
- institution/uniform relationship validated;
- player identity implications consent-safe;
- Pokémon welfare implications reviewed;
- accessibility requirements respected;
- any PTU mechanical claim verified;
- Minecraft presentation feasibility recorded.

## 27. Hard guardrails

Narrative generation must not:

- grant combat bonuses because clothing looks protective;
- grant Contest bonuses because clothing looks stylish;
- infer wealth from one outfit;
- infer faction membership from a uniform without records;
- infer gender, sexuality, religion, ideology or morality from clothing;
- invent a player character’s emotional meaning for an outfit;
- treat cultural or ceremonial dress as generic loot;
- copy a real-world culture’s sacred clothing into Ouros as decorative fantasy;
- force a Pokémon to enjoy costumes;
- make expensive garments automatically more prestigious;
- make a disguise automatically succeed;
- create Fashionista/Coordinator mechanics without PTU/Caelo verification.

## 28. Encounter-facing dependency rule

Most fashion content is noncombat world state.

When an encounter is embedded in a fashion event, atelier, wardrobe shipment or uniform-security story, list all tactical dependencies explicitly. Do not implement missing PTU behavior through Minecraft scripts.

The encounter contracts in Pass 44 proposals follow this rule.
