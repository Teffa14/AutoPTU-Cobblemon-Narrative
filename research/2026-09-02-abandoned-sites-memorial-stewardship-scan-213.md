# Ouros Narrative Research — Abandoned Sites, Memorial Stewardship & Adaptive Reuse — Pass 213

Status: RESEARCH ONLY / NON-CANON
Date: 2026-09-02

This pass follows the existing Public Memory, Myth/Archaeology, Care, Crisis/Recovery and recent Marea passes. It does not add canon. It addresses a narrower gap: places that have stopped serving their original function but still matter because of memory, ecology, records, mourning, risk, or later reuse.

The design target is not “haunted dungeon” as a genre shortcut. Ouros needs locations whose physical state, remembered use, current occupation and stewardship can diverge without one layer automatically explaining the others.

## 1. Pokémon Tower / Lavender — memorial function changes without erasing the dead

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Lavender_Town
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Tower

Lavender Town establishes a rare explicit Pokémon-world burial and remembrance institution. In later Kanto chronology, the original tower changes civic function while graves are moved to the Soul House / House of Memories rather than simply disappearing.

Reusable structure:
- a site can change use while its memorial obligation persists elsewhere;
- relocation of a memorial function is itself historical state;
- access policy, custodianship and public meaning can change independently from the physical structure;
- remembrance does not require combat, a supernatural reveal or a collectible reward.

Ouros translation:
Track the old function, closure reason, successor location, transferred records/objects and unresolved obligations separately.

Candidate object:

```yaml
retired_site_record:
  site_id: null
  former_function: null
  closure_event_id: null
  closure_reason_claim_ids: []
  confirmed_closure_facts: []
  successor_site_ids: []
  transferred_object_ids: []
  transferred_record_ids: []
  retained_obligations: []
  current_access_policy_id: null
  current_steward_ids: []
```

## 2. Memorial Pillar — a small physical act can carry memory without exposition

Source:
- https://bulbapedia.bulbagarden.net/wiki/Memorial_Pillar

Memorial Pillar uses a concrete place and a simple offering associated with a deceased Pokémon. The useful pattern is not the specific object or reward. It is that remembrance is expressed through a physical action at a specific site, with meaning supplied by local knowledge.

Reusable structure:
- memorial interaction can be optional and quiet;
- the act can be legible even without a cutscene;
- local memory may attach to an individual Pokémon rather than a legendary or famous Trainer;
- a memorial should not become a loot dispenser by default.

Ouros translation:
A `MEMORIAL_PRACTICE` may record customary actions and source claims while granting no PTU effect unless separately validated.

## 3. Sea Mauville — industrial ruin becomes ecological preserve

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Sea_Mauville
- https://bulbapedia.bulbagarden.net/wiki/Hoenn_Route_108

Sea Mauville is especially useful because abandonment does not freeze the site. A former industrial facility becomes ecologically significant after closure, and that later ecological value changes the decision about demolition.

Reusable structure:
- disuse creates new habitat and new stakeholders;
- preservation can happen for present ecological reasons rather than nostalgia alone;
- old workplace records and physical remains can reveal institutional history;
- a location can be simultaneously unsafe, historically important and ecologically valuable;
- “restore it to original condition” is not always the desirable outcome.

Ouros translation:
A retired site should support multiple current-value layers:

```yaml
site_current_value:
  site_id: null
  heritage_value_claim_ids: []
  ecological_value_observation_ids: []
  active_service_value_ids: []
  memorial_value_ids: []
  research_value_ids: []
  safety_concern_ids: []
  reuse_proposal_ids: []
```

No value field is canonical truth about what policy should win.

## 4. Old Chateau — environmental clues can sustain uncertainty

Source:
- https://bulbapedia.bulbagarden.net/wiki/Old_Chateau

The Old Chateau communicates abandonment through architecture, room function, objects, restricted access and unusual encounters. The game does not provide one complete administrative explanation for every detail.

Reusable structure:
- incomplete evidence can be stronger than a terminal lore dump;
- room-by-room traces can imply former use without proving every historical claim;
- current Pokémon occupation may be real even when stories about the place are unreliable;
- a site can support revisits after new access or knowledge becomes available.

Ouros translation:
Environmental storytelling should emit observations first: damaged fixture, sealed room, obsolete sign, archived roster, nest, repaired wall, missing equipment, later addition. Interpretation belongs in claim records.

## 5. Tales of Visiwa — long-abandoned places can remain part of a living region

Source:
- https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

The PTU retrospective describes a region where dangerous wilderness and long-abandoned shrines coexist with contemporary society and institutional exploration. The transferable lesson is structural: old places remain active components of a present campaign because access, interpretation, danger and institutional interest continue to change.

Ouros translation:
Do not isolate old places as one-shot lore dungeons. Their access, records, stewardship, ecology and public interpretation should connect to current residents and institutions.

## 6. Public PTU campaign log — ruins become meaningful when later actors occupy them

Source:
- https://forums.giantitp.com/archive/index.php/t-527075.html

A public PTU campaign log uses a familiar town encountered in a ruined state and immediately repopulates it with current actors and conflict. The important reusable pattern is temporal contrast: players understand that a place had a prior function, but the current inhabitants and current problem determine play.

No violence, characters or plot from that campaign are imported.

Ouros translation:
A retired location should answer four different questions:
1. What was this place?
2. Why did its original use end?
3. What occupies or uses it now?
4. Who currently has reason to care?

## 7. Community reaction to cemetery-as-active-play-space — respect is a design constraint

Source:
- https://www.reddit.com/r/LegendsZA/comments/1tm0rqe/how_would_you_feel_about_your_city_or_town_making/

A 2026 community discussion about cemetery space becoming a Wild Zone repeatedly raises access, mourning, safety and disrespect concerns. This is useful as reception evidence rather than lore authority.

Reusable lesson:
If a memorial or burial place becomes a battle, tourism or wild-encounter space, Ouros should model that as a social decision with stakeholders and consequences. It should not assume that gameplay convenience overrides the place's existing human meaning.

## 8. Separation model

For retired, memorial or abandoned sites, preserve these layers independently:

```yaml
site_time_layers:
  site_id: null
  original_function_facts: []
  closure_facts: []
  closure_claims: []
  physical_remains: []
  memorial_practices: []
  current_ecology_observations: []
  current_occupants: []
  current_stewards: []
  active_access_rules: []
  reuse_proposals: []
  unresolved_history_questions: []
```

Hard rules:
- abandoned does not mean ownerless;
- old does not mean archaeological;
- memorial does not mean supernatural;
- Ghost-type presence does not prove a haunting or death cause;
- current wild occupation does not erase prior human meaning;
- restoration, demolition, preservation and adaptive reuse are policy choices, not automatic quest endings;
- a Minecraft structure state cannot author historical truth.

## 9. Encounter design implications

Rich encounters at such sites may involve navigation through damaged spaces, protected rooms, escort, custody, forced movement, environmental hazards, reactions, wild Pokémon behavior or multi-party objectives.

Those concepts require explicit capability classification. A reduced version should use world-state access, documented observations, ordinary traversal and separate audited BattleSpecs where necessary.

Narrative code must never invent collapse damage, difficult terrain, weather penalties, Ghost immunities, possession, curse effects, forced movement, interrupt rules or Trainer Feature behavior.

## 10. PTU / Caelo compatibility

This pass does not assign mechanical effects to remembrance, grief, heritage status, old machinery, spiritual claims or site access.

Before any executable concept uses a Pokémon Move, Ability, Feature, Skill, item, sensing capability, traversal effect, environmental condition or supernatural interaction, validate it against the supplied PTU/Caelo/Kairos source set and the current AutoPTU implementation.

The existing Ouros deep-history rule remains controlling: observation, interpretation, mythic claim, ritual practice, anomalous phenomenon and canonical truth stay separate.

## 11. Design conclusions

1. Ouros should model retirement of places, not only creation and destruction.
2. Closure creates successor obligations: records, memorial functions, maintenance, access and ecology can move elsewhere.
3. Adaptive reuse should preserve a traceable relationship to prior use.
4. A ruin can acquire ecological value after abandonment.
5. Quiet memorial interaction deserves equal support to combat-oriented content.
6. Environmental clues should remain observations until a supported interpretation exists.
7. Current occupants and historical meaning may coexist without one explaining the other.
8. Reopening a site can be partial, conditional and reversible.
9. The “best” future of a place should come from actors, mandates and evidence rather than a universal preservation score.
10. Minecraft presents the site's current physical state; Ouros world state remains authoritative for history, access and consequences.

## Copyright and provenance guardrail

No protected dialogue, distinctive characters, complete plots, map layouts or custom mechanics are copied. External sources are used only to derive general narrative and world-state structures.