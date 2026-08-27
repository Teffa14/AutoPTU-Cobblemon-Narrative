# Pokémon Evolution & Identity Continuity Extension

Status: proposed systems design. Not established canon.

Pass: 76

## Purpose

Ouros already preserves one Pokémon's identity through capture, transfer, temporary partnership, release, rehoming, institutional care, migration and retirement. Evolution must follow the same rule.

A permanent Evolution changes authoritative species/mechanical projection while preserving the same persistent Pokémon identity and history.

This extension does not define Evolution legality. PTU/Caelo plus the authoritative AutoPTU runtime own that decision.

## Authority boundary

The write path is:

`Ouros persistent pokemon_id + world state -> reviewed Evolution intent/context -> AutoPTU authoritative Evolution transition -> committed persistent identity revision -> Cobblemon projection/playback`

Cobblemon provides embodiment and presentation wherever useful. It does not author the mechanical transition.

Minecraft/Cobblemon must never decide:

- whether the Pokémon is mechanically eligible to evolve;
- which branch is selected;
- whether a required mechanical item is consumed;
- authoritative stat recalculation;
- Ability or Move consequences;
- current HP/max HP consequences;
- Trainer Feature consequences;
- battle-state mutation;
- whether a mid-battle Evolution is legal;
- whether the persistent transition committed successfully.

## 1. Persistent identity rule

The existing `pokemon_id` survives Evolution.

Do not:

- delete the old persistent Pokémon and create a new one;
- reset relationship history;
- reset public memory;
- reset care history;
- reset custody/ownership claims;
- reset battle history;
- reset provenance;
- replace observation history with only the newest species state.

Instead append an identity revision.

```yaml
pokemon_identity_revision:
  revision_id: null
  pokemon_id: null
  effective_at: null
  revision_type: EVOLUTION | FORM_CHANGE | OTHER_REVIEWED_TRANSITION
  prior_species_ref: null
  new_species_ref: null
  prior_form_ref: null
  new_form_ref: null
  authoritative_transition_ref: null
  source_rule_refs: []
  witness_refs: []
  projection_status: PENDING | APPLIED | FAILED_RETRYABLE | FAILED_REVIEW
  notes: null
```

Permanent Evolution and temporary/battle-only transformation must remain different transition types.

## 2. Evolution expectation claims

Characters may predict, hope for, fear or misunderstand an Evolution outcome.

```yaml
evolution_expectation_claim:
  claim_id: null
  pokemon_id: null
  claimant_id: null
  predicted_result_ref: null
  basis_refs: []
  recorded_at: null
  visibility: PRIVATE | SHARED | PUBLIC
  status: CURRENT | CORRECTED | OUTDATED | WITHDRAWN
```

The claim never controls the result.

If the authoritative branch differs, preserve the old claim and append the correction. This creates usable continuity for later dialogue and public memory.

## 3. Mechanical eligibility reference

Narrative state can point to mechanical eligibility but cannot calculate it independently.

```yaml
evolution_eligibility_ref:
  pokemon_id: null
  authoritative_engine_ref: null
  inspected_rule_revision: null
  evaluated_at: null
  eligible: null
  legal_result_options: []
  required_choice_owner_ref: null
  unresolved_requirements: []
```

`eligible: true` must come from the authoritative rules/runtime path.

The narrative generator cannot infer eligibility from:

- visible level alone;
- species familiarity;
- friendship-like prose;
- location name;
- weather visible in Minecraft;
- carrying an item that merely resembles a required object;
- winning a battle;
- reaching a story beat;
- an NPC saying the Pokémon looks ready.

## 4. Evolution intent

Where governing rules permit postponement or choice, actor intent is separate from eligibility.

```yaml
evolution_intent:
  intent_id: null
  pokemon_id: null
  actor_ref: null
  requested_at: null
  desired_result_ref: null
  decision_scope_ref: null
  status: PROPOSED | CONFIRMED | DECLINED | SUPERSEDED | EXPIRED
```

The system must not assume every eligible Pokémon should evolve immediately.

No hidden desirability score ranks evolved forms as inherently superior characters.

## 5. Authoritative transition packet

```yaml
evolution_transition_packet:
  transition_id: null
  pokemon_id: null
  from_species_ref: null
  from_form_ref: null
  requested_result_ref: null
  eligibility_ref: null
  actor_intent_ref: null
  governing_rule_refs: []
  authoritative_runtime_ref: null
  started_at: null
  committed_at: null
  result_species_ref: null
  result_form_ref: null
  mechanical_write_refs: []
  consumed_resource_refs: []
  transcript_ref: null
  rollback_ref: null
  status: PENDING | REJECTED | COMMITTED | ROLLED_BACK | NEEDS_REVIEW
```

The transition should be atomic from the narrative world's perspective. A failed visual animation cannot create a second Evolution. A client reconnect cannot replay the mechanical transition.

## 6. Mechanical changes remain external

The transition packet can reference changes but this layer does not compute them.

Potential externally owned consequences include:

- base/stat changes;
- max/current HP handling;
- Ability identity/slot changes;
- Move access or legal known-Move changes;
- movement Capabilities;
- size/weight or footprint data where governing sources establish them;
- held-item consumption;
- Trainer Feature interactions;
- battle initiative/action-state consequences if Evolution is ever legal during combat.

Each consequence requires PTU/Caelo and runtime evidence.

## 7. Actor knowledge

The world can know an Evolution occurred while a distant NPC still believes the Pokémon is in its previous stage.

```yaml
evolution_observation:
  observation_id: null
  pokemon_id: null
  observer_ref: null
  observed_species_ref: null
  observed_form_ref: null
  observed_at: null
  location_ref: null
  evidence_refs: []
```

A later message, photograph, battle record or direct encounter may update actor knowledge.

This creates legitimate callbacks without omniscient NPCs.

## 8. Public identity continuity

Names, nicknames and established social references remain attached to `pokemon_id` unless separately changed.

Examples of valid continuity:

- a shopkeeper remembers the same partner after its silhouette changes;
- an old photograph remains linked to the current Pokémon;
- a battle institution's prior result references the same participant identity;
- a care record remains continuous across the transition;
- a tagged wild individual can be recognized after Evolution if the tag/provenance link is real.

Do not infer:

- a personality change;
- greater maturity;
- greater Loyalty;
- new ownership;
- new friendship/romance/family labels;
- new institutional rank;
- new working qualification;
- permission to ride, carry, fly, swim or perform a task merely from species change.

Those require their own authoritative state.

## 9. Post-Evolution review handoffs

Evolution may create reasons for other systems to review their state.

### Shared equipment

A harness, uniform, carrier, issued tool or protective fit may need inspection.

The equipment remains under its existing ownership/custody rules. A new body shape does not automatically destroy, replace or authorize equipment.

### Residential/accessibility

Physical routes, doors, sleeping areas or fixtures may need a practical review if authoritative physical metadata changed.

Do not invent exact dimensions from visual scale alone.

### Travel and mobility

New movement capabilities may matter only when PTU/Caelo and AutoPTU confirm the individual Pokémon's legal capability state.

Evolution alone does not grant a narrative mount permission.

### Workplaces

A changed capability profile may trigger assignment review. It does not automatically promote, disqualify or assign the Pokémon.

### Care

Care history remains continuous. Evolution itself does not establish illness, injury or recovery.

### Ecology

A known wild individual's new stage may update observations. One individual's transition cannot establish population-wide abundance or migration conclusions.

### Credentials/registrations

Any public record that projects species/form may need a revision. The underlying authorization remains owned by the credential system.

## 10. Branching Evolutions

Branch selection is a mechanical/source question.

Narrative authoring rules:

- never select a branch because it fits an NPC arc better;
- never reveal a hidden determinant without an authoritative observation/source;
- preserve actor predictions as claims;
- when a player-controlled choice is legally available, record who owns that choice;
- when the rules make a branch non-volitional, do not fake a choice UI;
- do not reroll/retry an unwanted branch unless governing rules explicitly allow it.

## 11. Temporary transformations

Mega Evolution, temporary forms, battle forms and other reversible transformations must not be stored as permanent Evolution revisions unless the governing source explicitly defines them that way.

They require separate lifecycle and rollback semantics.

Cobblemon's own codebase is also moving toward explicit transformation/form concepts. That reinforces the need for an adapter boundary rather than treating every species/form mutation as the same event.

## 12. Wild Pokémon Evolution

For a persistent wild individual:

- retain the same `pokemon_id`;
- preserve territory/collective observations that are still valid;
- review rather than assume any changed ecological role;
- keep ownership null unless separately established;
- do not auto-capture or auto-partner after a witnessed Evolution;
- do not infer the entire collective transformed.

If the individual was not previously identity-resolved, an observer can only claim continuity when evidence supports it.

## 13. Cobblemon integration profile

### SAFE_REUSE

Prefer Cobblemon for:

- species/form asset lookup;
- models and textures;
- scale/render projection where useful;
- cries/audio;
- Evolution animation/display components;
- particles;
- entity tracking;
- UI panels;
- networking;
- persistence hooks;
- event observation hooks;
- visual species/form refresh;
- overworld spawning/embodiment after Ouros has already selected the actor.

### ADAPTER_REQUIRED

Use an Ouros/AutoPTU adapter for:

- stable `pokemon_id` <-> Cobblemon entity identity mapping;
- presenting legal result choices returned by the authoritative layer;
- collecting player intent without resolving it;
- applying a committed species/form projection to the existing entity;
- replaying Evolution visuals exactly once after commit;
- client reconnect/replay reconciliation;
- restoring the authoritative projection after Cobblemon-side drift.

### FORBIDDEN AUTHORITY

Do not let Cobblemon:

- run its server Evolution resolver as the canonical Ouros rule authority;
- decide the PTU branch/result;
- consume an authoritative held item before AutoPTU commits the transition;
- mutate authoritative Moves/Abilities/stats;
- write battle state from its own Battle classes;
- decide battle participants because nearby entities exist;
- decide whether an Evolution is legal in battle;
- conclude that visual animation completion means the transition committed.

## 14. Evolution projection transaction

Recommended adapter transaction:

```yaml
evolution_projection_transaction:
  transition_id: null
  pokemon_id: null
  authoritative_commit_seen: false
  target_species_ref: null
  target_form_ref: null
  cobblemon_entity_ref: null
  projection_applied: false
  visual_playback_started: false
  visual_playback_completed: false
  client_ack_refs: []
  retry_count: 0
  reconciliation_status: CLEAN | RETRY | RESYNC | REVIEW
```

Only `authoritative_commit_seen: true` permits projection.

A projection retry may replay only presentation-safe state. It cannot reapply mechanical consequences.

## 15. Encounter contract — Evolution During a Challenge

Status: PROPOSED / source legality unresolved.

Narrative premise:

A known partner reaches a story moment where Evolution could plausibly become available during an ongoing formal challenge.

Important rule:

Pass 76 does not assume PTU/Caelo allows this timing.

### Intended full version

If source review and runtime tests eventually establish legal mid-encounter Evolution:

- the same `pokemon_id` remains the combatant;
- the authoritative engine performs the transition atomically;
- current battle state is preserved according to exact rules;
- any stat, HP, Ability, Move, item and lifecycle consequences come from AutoPTU;
- AI and legal-action generation see the new authoritative state after commit;
- Cobblemon plays the change as downstream presentation only.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED, but a changed footprint would need specific transition tests;
- base movement legality — VERIFIED, but changed movement capability needs specific tests;
- complete movement including push/pull/knockback/interception/forced movement — not required by premise unless the challenge uses it;
- core calculations — VERIFIED, while Evolution-specific recalculation remains unverified;
- action economy/initiative — VERIFIED, while transition timing inside initiative needs exact tests;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL, especially current/max HP continuity;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — optional to premise, BLOCKING if used;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for autonomous adaptation;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Additional explicit blocker:

- authoritative Evolution transition runtime: UNKNOWN/BLOCKING pending PTU/Caelo source review and engine implementation evidence.

### Reduced version

Finish the current ordinary legal encounter first. Exit tactical resolution. Evaluate Evolution through a separate authoritative progression/world-state transaction. Apply the Cobblemon visual projection only after commit. If the story needs another confrontation afterward, start a second normal encounter from the new authoritative state.

This preserves the narrative arc without pretending mid-battle Evolution exists.

## 16. Encounter contract — Protected Observation Window

Status: PROPOSED.

Narrative premise:

Researchers or caretakers are observing a known wild individual whose current state makes Evolution a subject of interest. A local disturbance forces the observers to withdraw.

### Intended full version

- noncombatants move toward safe exits;
- the party protects/clears a route;
- wild actors can withdraw rather than seek KO;
- environmental state may matter only when authoritative mechanics exist;
- the target Pokémon evolves only if its own authoritative requirements are independently satisfied.

Capability dependencies:

- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING if interception/displacement protects routes;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING if active environmental effects matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL where relevant;
- Trainer Features/perks — PARTIAL where relevant;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for territorial/withdrawal objectives;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

### Reduced version

Observers withdraw through world state before combat. The known Pokémon and any civilians are kept outside the tactical grid unless they are actual legal combatants. AutoPTU resolves a static ordinary encounter. Afterward, observation resumes only if the world state still allows it. Winning the battle never forces Evolution.

## 17. Noncombat mystery profile — Three Photos, One Pokémon

Three images taken weeks apart appear to show different species/stages. The investigation uses timestamps, stable markings, custody/registration records, care history and witness provenance to determine whether they document one persistent individual across Evolution.

No battle mechanic is required.

The answer may remain uncertain if identity evidence is insufficient.

## 18. Failure and rollback

A safe implementation must distinguish:

- mechanical transition committed, visual playback failed;
- visual playback started, mechanical transition rejected;
- client disconnected during projection;
- entity unloaded during animation;
- adapter received duplicate commit event;
- Cobblemon entity species drifted from authoritative projection;
- battle rollback restored a pre-transition tactical state.

The persistent record is authoritative. Presentation reconciles to it.

## 19. Anti-false-completion rules

- A Cobblemon Evolution animation does not prove PTU Evolution legality.
- A Cobblemon species JSON does not prove Ouros may use the same condition.
- A level threshold alone does not prove all Evolution rules are implemented.
- One branch resolver does not prove all branch families.
- One Ability change after Evolution does not prove complete Ability-transition support.
- A persistent species swap does not prove HP/status/Move continuity.
- A visual model change does not prove new movement capability.
- An evolved Pokémon does not automatically become a stronger worker, mount, leader or social partner.
- A battle won near an eligible Pokémon cannot force its Evolution.
- A new Cobblemon BattleState must never become the source of truth for this transition.

## 20. Promotion gate

Full executable Evolution support requires all of the following:

- PTU/Caelo Evolution source review completed;
- branch and eligibility ownership documented;
- authoritative AutoPTU transition contract implemented;
- stat/HP/Ability/Move/item consequences tested;
- rollback/replay semantics tested;
- persistent stable identity tested;
- Cobblemon adapter can apply projection without using Cobblemon battle authority;
- visual retry cannot duplicate mechanical effects;
- relevant encounter capability families meet their own readiness gates.
