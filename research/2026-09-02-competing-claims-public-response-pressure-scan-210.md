# Pass 210 Research — competing claims, public response pressure and visible consequences

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02

## Scope

This pass studies how a persistent Pokémon world can let several actors react publicly to the same unresolved situation without allowing headlines, faction rhetoric, popular belief or player reputation to overwrite canonical truth.

The target gap follows directly from existing Ouros work. Pass 19 established communication channels and versioned publication. Pass 208 established evidence webs for Thin Delivery Season and explicitly allowed an incomplete interpretation to become a later correction problem. Pass 209 established bounded Pokémon assistance and persistent wild identity. The missing layer is what happens when attributed claims begin to compete in public and institutions act on different subsets of the same evidence.

## Internal project review

Before writing, the current narrative repository tree at `7b09df560172ed0e15f72994baf90484d62297c2` was inspected across its top-level layers. Canon files were checked directly, recent passes 207–209 were checked, the media/communications pass was checked, the Kairos source index was checked, and repository-wide searches were run for an already-defined competing-claims/public-response layer.

Canon constraints preserved:

- Thin Delivery Season begins with smaller and less predictable deliveries, while its cause remains unresolved.
- Puerto Bruma vendors already disagree about possible causes.
- Estación Mirador records claims with provenance and revision history rather than regional truth.
- Mara Veyra, Ivo Serrat, Nerea Sol, Taro Min, Lia Morn, Brin Havel, Alba Ríos and the other established residents each own bounded observations or institutional responsibilities, not omniscience.
- the Marea Field Office is a field-service institution rather than a police force.
- battle victory cannot establish the cause of Thin Delivery Season.
- one public report cannot convert a hypothesis into canon.
- existing persistent wild identities, including the lower-Sendero Fletchling, cannot be repurposed as convenient culprits.

No new settlement, faction, villain, Pokémon species, governmental authority or communication technology is required by this pass.

## Public research

### Pokémon Black/White — rhetoric can alter public behavior before truth is settled

Sources:

- Bulbapedia, Team Plasma: https://bulbapedia.bulbagarden.net/wiki/Team_Plasma
- Bulbapedia, Ghetsis: https://bulbapedia.bulbagarden.net/wiki/Ghetsis

Inspected: 2026-09-02.

High-level reusable structure:

Team Plasma first enters public life through a persuasive claim about the relationship between people and Pokémon. The important structure for Ouros is not the faction, speech, ideology or plot. It is that a claim can be publicly framed, heard by ordinary residents and produce behavior before the audience possesses complete information. Later revelations can change how earlier statements are interpreted without erasing that those statements were heard and acted upon.

Ouros transformation:

- publication is an event with consequences, not proof;
- a claim can have an attributed speaker, evidence basis, framing and audience;
- residents may alter choices because they believe or distrust a claim;
- later correction should append to history rather than delete the earlier public state;
- an actor may make a technically supportable statement while implying more certainty than the evidence warrants;
- deceptive messaging, if ever authored, must remain an actor action and never a silent rewrite of world truth.

Do not import Team Plasma, liberation ideology, Ghetsis, N, Unova events, speeches or plot beats.

### Tales of Visiwa PTU retrospective — public identity and noncombat pressure persist across a campaign

Source:

- Pokémon Tabletop RPG, “Tales of Visiwa: A Retrospective”: https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

Inspected: 2026-09-02.

This long-running PTU campaign contains two useful structural observations. Public-facing activity such as televised competition and social-media presence became part of how characters existed in the setting rather than remaining flavor outside the campaign. The retrospective also describes a major confrontation whose trajectory changed when the PCs used a noncombat social intervention against an opponent who was being manipulated.

Ouros transformation:

- public identity can persist independently from combat statistics;
- characters and institutions may care how an event was framed or witnessed after the immediate scene ends;
- a tactical confrontation can have an authored non-damage off-ramp when the narrative premise supports it and the governing mechanical/social action is actually verified;
- defeating an actor and changing that actor's conclusion are distinct outcomes;
- public consequences should reference observable events, publication records and audience state instead of a universal hidden reputation meter.

Do not import Visiwa factions, characters, deities, custom types, social-media names, campaign plots, special Pokémon or house rules.

### Pokémon Unbound — side missions can expose consequences through existing places and follow-up state

Sources:

- Pokémon Unbound Wiki, All Missions: https://unboundwiki.com/missions/
- Pokémon Unbound Wiki, The Food Thief: https://www.unbound.wiki/wiki/The_Food_Thief

Inspected: 2026-09-02.

Reusable structure:

Unbound uses a large mission catalogue with prerequisites, recurring places, follow-up missions and aftermath that can remain visible after the immediate objective. A local problem can reveal another space or later activity instead of disappearing when the reward is claimed.

Ouros transformation:

- a public-claim episode can unlock follow-up investigation, correction, mediation or service work without creating a disconnected quest island;
- the same market, route, archive, field office and station can carry different phases of one issue;
- resolution should change persistent records and later interactions, not merely complete a journal checkbox.

Do not import Unbound characters, Borrius locations, mission numbering, rewards, bosses or ROM-hack plot lines.

### Dungeon World fronts — several actors can advance independently around one unresolved pressure

Source:

- Dungeon World SRD, Fronts: https://www.dungeonworldsrd.com/gamemastering/fronts/

Inspected: 2026-09-02.

Reusable structure:

Fronts model several dangers or actors with their own impulses and visible developments. A change in one can affect the larger situation. The useful lesson for Ouros is to give each relevant institution its own bounded response state rather than maintaining one global “crisis percentage.”

Ouros transformation:

- each responder should have a goal, current evidence basis, next plausible action and stop/revision condition;
- response state advances because of world events or explicit decisions;
- only actors relevant to the current issue should advance;
- visible developments should be authored consequences, not arbitrary timers.

Do not import Front terminology as canon, grim-portent tables, impending-doom categories or fantasy example content.

### Blades in the Dark SRD and GM community — clocks work best when they represent a specific complex process

Sources:

- Blades in the Dark SRD content, progress clocks: https://github.com/amazingrando/blades-in-the-dark-srd-content/blob/main/Blades-in-the-Dark-SRD.md
- r/bladesinthedark discussion, “Consequences of the Faction Game?”: https://www.reddit.com/r/bladesinthedark/comments/s7uo9f

Inspected: 2026-09-02.

Reusable structure:

The SRD recommends clocks for complex or layered situations rather than every task. Community practice emphasizes advancing only relevant factions and surfacing consequences through rumors, headlines or other in-world signals.

Ouros transformation:

Ouros should not create a progress clock for every NPC opinion. A response tracker is justified only when a bounded institutional process can materially change the world, such as issuing a route notice, changing a purchasing plan, requesting a verification pass or publishing a correction. Progress must remain traceable to events and decisions.

Do not import Blades faction ratings, Tier, Heat, Wanted Level, downtime rolls or dice procedures.

## Derived design distinction

The project needs four different records when a disputed situation becomes public:

1. `CLAIM_RECORD` — what an actor asserts, with evidence/provenance and confidence.
2. `PUBLICATION_RECORD` — how that claim was framed and delivered to an audience.
3. `RESPONSE_ACTION` — what an institution or person actually does because of its current knowledge, duties and priorities.
4. `WORLD_FACT` — what is canonically true independent of those assertions.

These records may refer to one another, but they must never collapse into one object.

`CLAIM_ACCEPTED_BY_AUDIENCE != WORLD_FACT_CONFIRMED`

`PUBLICATION_CORRECTED != EARLIER_PUBLICATION_NEVER_HAPPENED`

`INSTITUTION_ACTED != INSTITUTION_WAS_CORRECT`

## Candidate response-state schema

Status: PROPOSED BY RESEARCH / NON-CANON

```yaml
response_thread:
  response_thread_id: null
  subject_world_arc_id: null
  actor_or_faction_id: null
  mandate_or_interest_ref: null
  triggering_claim_refs: []
  evidence_refs_considered: []
  evidence_refs_missing: []
  current_position_claim_ref: null
  current_action_state: WATCHING | VERIFYING | ACTING | PAUSED | REVISING | CLOSED
  next_action_candidates: []
  revision_conditions: []
  publication_refs: []
  world_write_refs: []
```

The record describes a bounded response process. It does not contain an automatic truth score, ideology score or universal trust meter.

## Candidate public-claim schema extension

```yaml
claim_record:
  claim_id: null
  speaker_entity_id: null
  subject_refs: []
  asserted_propositions: []
  evidence_refs: []
  omitted_known_evidence_refs: []
  confidence_expression: null
  authored_intent: INFORM | WARN | PERSUADE | REQUEST_ACTION | DEFEND_POSITION | OTHER
  issued_world_time: null
  supersedes_claim_id: null
  status: ACTIVE | REVISED | WITHDRAWN | DISPUTED | CONFIRMED
```

`authored_intent` must only be filled when canon or authored character state establishes it. The runtime must not infer deception from disagreement.

## PTU / Caelo / Kairos boundary

This research adds no combat, social Skill, Feature, communication or persuasion rule.

The current Kairos source index routes Skill/Edge/Feature questions to chapter 3, Trainer Classes to chapter 4, movement to chapter 7, world/campaign guidance to chapter 9 and gear to chapter 10. Any future mechanical attempt to persuade an NPC, command a crowd, interrupt an opponent, use telepathy, transmit through special equipment, inspect a scene under pressure or execute a Trainer Feature must be checked against the actual supplied source pages and the production rules profile.

Narrative world state may record that a person heard a claim or that an institution issued a notice. It may not invent a bonus, DC, social status condition, compelled behavior or battle interrupt.

## Engine dependency lessons

A pure information/response episode can run without a tactical battle if world-state services support provenance, dialogue choices, publications and persistent consequences.

A mechanically rich confrontation around evidence custody, route access or a contested inspection may require:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement when push/pull/knockback/interception/forced movement is present;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle where applicable;
- terrain/weather/hazards/zones/reactions if the site itself acts tactically;
- move-specific behavior;
- abilities;
- items if field equipment is mechanically active;
- Trainer Features/perks for Orders, interrupts or social/tactical Features;
- AI legal-action infrastructure;
- AI tactical policy for objective-aware opponents/allies;
- Minecraft/Cobblemon/Craftics adapter/playback support.

No family is considered complete merely because one representative mechanic exists.

## Design conclusion

Thin Delivery Season can become more alive without deciding its cause by allowing evidence to produce competing attributed claims, those claims to produce bounded responses, and those responses to leave visible consequences. The simulation gains tension from people acting under uncertainty while canon remains separate from belief.

The next concrete Ouros candidate should therefore reuse the current Marea cast and the pass-208 evidence web to stage a first public correction/response loop, with a reduced noncombat implementation that works before advanced battle capability is ready.