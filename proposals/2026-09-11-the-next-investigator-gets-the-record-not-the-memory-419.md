# The Next Investigator Gets the Record, Not the Memory — Pass 419

Status: PROPOSED / NON-CANON

## Premise

A field problem can outlast the person who first investigates it.

One named actor begins the work, produces bounded observations and leaves behind a report. Another actor later continues the investigation. The second actor receives the report and any explicitly transferred evidence. They do not automatically receive the first actor's private memory, suspicions, unrecorded context or confidence.

This preserves continuity without turning institutional recordkeeping into shared consciousness.

## Candidate Ouros surfaces

This pattern can reuse existing canon without adding a new location or institution:

- Marea Field Office can transfer a route or wildlife case between duty holders;
- Estación Mirador can hand observation records between Nerea Sol and Ema Rey;
- Tideglass Archive can preserve earlier reports and later corrections;
- Sendero del Vidrio can provide a location whose physical condition changes between visits.

No specific handoff, incident or conclusion is canonized by this proposal.

## Example structure

An investigator records that a route marker was displaced, a crossing was noisy, a shipment container was found open or a wild population was absent from an expected observation window.

The record contains what was observed, when, where and by whom. It may also contain an attributed hypothesis if the investigator wrote one down.

A second investigator arrives later after a site revision. They can compare the inherited record with present conditions. They may confirm part of it, find contradictory evidence or decide that the original hypothesis no longer explains the available facts.

The game should not retroactively alter the first report merely because a later explanation becomes stronger.

## Persistent state

Useful identities include:

- `investigation_ref`;
- `observation_id`;
- `observer_actor_id`;
- `observed_at_minute`;
- `site_revision_ref`;
- `evidence_ref`;
- `report_ref`;
- `transfer_event_ref`;
- `receiver_actor_id`;
- `receiver_knowledge_ref`;
- `hypothesis_claim_ref`;
- `provenance_root`.

`TRANSFERRED_RECORD != TRANSFERRED_MEMORY`

`LATER_HYPOTHESIS != RETROACTIVE_WORLD_TRUTH`

## Reduced version

The reduced implementation requires no AutoPTU battle.

It uses semantic time, persistent observations, private knowledge, provenance, communication, archive access, travel, schedules, obligations, permissions and site revisions.

The handoff itself can create useful play:

- decide which records to request;
- verify whether the original observer is reachable;
- compare old and current site state;
- identify which statements were observations and which were interpretations;
- send a correction or supplemental report;
- decide whether more field work is justified.

Minecraft may display authored physical evidence and changed site presentation. The adapter cannot infer hidden historical truth from blocks.

## Full version under tactical pressure

A richer version can place the continuation scene under pressure. Examples include reaching a known observation point while a wild confrontation is active, protecting a witness long enough to withdraw, retrieving a record from a dangerous area or disengaging after enough evidence has been secured.

Required capability families depend on the exact implementation:

- ordinary ranged or positional attacks: targeting/footprints/range/LoS;
- ordinary legal relocation: base movement legality;
- escort interception, dragging, knockback, pull or rescue reposition: complete movement including push/pull/knockback/interception/forced movement;
- damage and checks: core calculations;
- timing who may act and when: action economy/initiative;
- survive-N-rounds, delayed collapse or staged extraction: full turn/round lifecycle;
- persistent post-battle harm: full stateful damage pipeline;
- continuing afflictions: status lifecycle;
- unstable ground, flooding, visibility/weather phases, triggered hazards or reaction windows: terrain/weather/hazards/zones/reactions;
- any thematic Move: move-specific behavior for that exact Move;
- Ability-triggered field behavior: abilities for that exact Ability;
- special equipment use: items for that exact Item;
- interrupt or perk behavior: Trainer Features/perks for that exact Feature;
- specialized inspect/protect/retrieve/extract actions: AI legal-action infrastructure;
- evidence-first, protect-witness or objective-aware withdrawal decisions: AI tactical policy;
- authoritative non-KO objective presentation or resumed battle playback: Minecraft/Cobblemon/Craftics adapter/playback support.

## Current readiness

Verified only in audited scopes:

- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- ordinary AI legal-action infrastructure already covered by tests/contracts.

Partial:

- complete movement;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- abilities as a family.

Mixed, partial or blocking by exact mechanism:

- terrain/weather/hazards/zones/reactions;
- move-specific behavior;
- items;
- Trainer Features/perks;
- Minecraft/Cobblemon/Craftics adapter/playback support.

Blocking for this proposal's specialized rich-version behavior unless separately implemented:

- AI tactical policy for evidence-first movement, witness protection, retrieval-first behavior, objective-aware withdrawal and disengage-after-objective.

## Narrative value

This pattern lets investigations survive absences, schedule changes and long world arcs while preserving non-omniscient NPCs. It also makes archives and reports useful without making them perfect. The player can inherit work from another person, improve it and still disagree with that person for legitimate evidence-based reasons.
