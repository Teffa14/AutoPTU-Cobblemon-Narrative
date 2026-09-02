# Emergency Response, Evacuation and Recovery Scan 212

Status: RESEARCH / PROVENANCE / NON-CANON
Date: 2026-09-02

## Scope

This pass examines how Ouros can support local emergencies that create urgent work without turning every incident into a boss battle or silently granting the Minecraft layer authority over PTU rules. The focus is warning, triage, evacuation, accounting for people and Pokémon, temporary route restrictions, rescue, recovery and reopening.

Existing Ouros material already supports persistent sites, attributed observations, field assistance, public claims, handoffs and parallel fieldwork. This scan adds a missing temporal structure: a place can move through preparation, active response and recovery while preserving who knew what, what was actually observed, who remained unaccounted for and which restrictions were administrative rather than mechanical terrain effects.

No source below establishes Ouros canon. High-level structures are transformed into original project concepts.

## Public sources reviewed

### Pokémon Mystery Dungeon: Red/Blue Rescue Team

Sources:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Mystery_Dungeon:_Red_Rescue_Team_and_Blue_Rescue_Team
- https://mysterydungeonwiki.com/wiki/Pkmn:Natural_Disasters

Reusable structure: recurring natural disturbances create a durable social role for rescue work. Individual incidents can involve locating a missing target, reaching an isolated site, extracting someone, or discovering that another capable team failed and now also needs assistance. The useful Ouros lesson is escalation by changed responsibilities rather than simple enemy strength.

Do not import Mystery Dungeon cosmology, named teams, plot causes, dungeons, dialogue or disaster mythology.

### Pokémon Ranger family

Earlier project research already used Ranger for temporary Pokémon cooperation. For this pass the reusable extension is institutional field response: a trained responder can be dispatched because a physical situation needs containment, access, assistance or extraction. The field problem remains separate from ownership of the Pokémon that helps solve it.

This pass deliberately avoids assigning Ranger-like powers or converting temporary cooperation into a PTU mechanic.

### General tabletop emergency-scenario pattern

Public scenario design commonly creates pressure by placing several legitimate needs in parallel: warn people, reach a threatened location, protect access, extract targets and decide what can safely wait. The transferable lesson is that urgency becomes meaningful when actions have explicit consequences and clocks correspond to authored world processes. Ouros should not use invisible countdowns that trigger arbitrary failure merely because the player explored.

## Derived Ouros model

Candidate world records, all PROPOSED:

`INCIDENT_RECORD`
- incident_id
- affected_site_ids
- first_observed_at
- observation_sources
- known_conditions
- uncertainty
- response_state
- closure_condition

`ACCOUNTABILITY_RECORD`
- incident_id
- actor_or_pokemon_identity
- last_confirmed_site
- last_confirmed_at
- current_state: CONFIRMED_SAFE / ASSIGNED / UNCONFIRMED / LOCATED / EXTRACTED
- source

`RESPONSE_ASSIGNMENT`
- incident_id
- responsible_actor
- task_scope
- issued_at
- accepted_at
- completion_evidence

`ACCESS_RESTRICTION`
- site_or_edge
- authority
- reason
- issued_at
- review_condition
- lifted_at

`RECOVERY_RECORD`
- affected_object_or_site
- observed_damage_or_disruption
- temporary_mitigation
- permanent_repair_status
- inspection_source
- reopened_at

These records must not infer facts from presentation. A barrier block or warning sign in Minecraft can display an authoritative restriction, but its local existence does not decide route legality, incident state or PTU terrain effects.

## Narrative structure

A robust emergency episode can progress through four authored phases without requiring every phase to occur:

1. Detection: someone observes a condition and records uncertainty.
2. Response: assignments, warnings, accounting and access decisions begin.
3. Rescue/containment: unresolved people, Pokémon or infrastructure require direct action.
4. Recovery: restrictions are reviewed, repairs are documented and the site can reopen with persistent aftermath.

The causal question may remain unresolved. Successful evacuation proves only that the response objective was met.

## PTU/Caelo/Kairos boundary

This pass does not assign a Skill, Edge, Feature, Move, Ability, item or derived PTU statistic to warning, rescue, medical triage, navigation, lifting, clearing, carrying or environmental mitigation. Exact mechanical authorization must be checked against the project PTU/Caelo/Kairos source set before any such action gains rules meaning.

Narrative records can represent an assignment or observed condition now. A later PTU contract may determine whether a specific actor can perform a mechanically contested action.

## Engine dependency implications

A fully simulated emergency may touch targeting/footprints/range/LoS; base movement legality; complete movement including push/pull/knockback/interception/forced movement; core calculations; action economy/initiative; full turn/round lifecycle; full stateful damage pipeline; status lifecycle; terrain/weather/hazards/zones/reactions; move-specific behavior; abilities; items; Trainer Features/perks; AI legal-action infrastructure; AI tactical policy; and Minecraft/Cobblemon/Craftics adapter/playback support.

A reduced version can avoid most battle dependencies by using authenticated incident state, explicit access restrictions, ordinary traversal, authored accountability records, field interactions whose authority is already available, and separate optional BattleSpecs. It must not emulate weather damage, hazards, reactions, forced movement or status effects in Minecraft.

## Design lessons

Emergency response should produce persistent aftermath. A cleared route may need inspection. A temporarily relocated resident may remain away for a while. A wild Pokémon that was assisted keeps its own identity and ownership state. A public warning can later be corrected without erasing the earlier version.

Rescue success, causal truth, public interpretation and relationship consequences remain separate state families. This preserves the epistemic model established by prior Ouros research.
