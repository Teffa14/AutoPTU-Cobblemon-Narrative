# Marea emergency preparedness and drill seeds — pass 184

Status: PROPOSED / NON-CANON.

These candidates reuse established Marea residents, places, work relationships, communications, custody, route, observation, and field-search architecture. They do not establish an emergency service, legal authority, alarm code, disaster history, shelter network, or Caelo doctrine.

## 1. Ferry Bell Drill

Lia and Mina run a short dock-clearance rehearsal with Teo checking one physical route assumption. The exercise reveals that one copied instruction points to an older assembly location or assumes a passage that no longer works for current operations.

The interesting outcome is the correction chain: identify which plan version was used, determine who received it, replace the stale copy, inspect the route, and retest later. No disaster is required.

Preferred implementation tier: world-state only. No BattleSpec.

## 2. Mirador Instrument Safe-Down

Nerea and Ema rehearse the minimum steps required to leave Mirador quickly while preserving only the observations or instruments that can safely be secured. One checklist item takes longer than expected or assumes that a route remains available.

The scenario lets Ema prepare evidence and Nerea review it without changing their existing institutional roles. The plan learns which data can be abandoned temporarily and which custody/condition records must be updated afterward.

Preferred implementation tier: world-state only.

## 3. Tideglass Record Triage

Taro and Pia rehearse a limited response to water intrusion, smoke, or another generic access-threatening condition without canonizing that such an incident has occurred historically. They identify which current records, copies, and provenance materials can move first and which objects require custody transfer before relocation.

The drill can expose two versions of an old priority list. Correcting the list preserves the obsolete version as historical evidence instead of deleting it.

Preferred implementation tier: world-state only.

## 4. Clear the Yard

Sela and Jace rehearse stopping an ordinary Battle Yard session, clearing the active ring, accounting for visitors, and securing equipment. The exercise evaluates role scope and communication rather than combat performance.

A useful failure is that a spectator or companion Pokémon uses an exit that the written plan does not account for. The corrective item can be a route change, better signage, or a revised accounting step.

Preferred implementation tier: world-state only. An actual battle need not be running.

## 5. Route Closure Before Arrival

Mara receives a credible but uncertain warning that justifies preparation under whatever authority later becomes canon. She pre-stages a closure marker and an alternate route instruction without claiming that the hazard is already present.

The design tests the difference between forecast, watch posture, closure authority, physical barriers, and public belief. If the warning proves irrelevant, the preparation still produces evidence about how quickly the route can be changed back.

Canon question: what evidence threshold and role authority permit anticipatory restriction in Marea?

## 6. The Cache Audit

Brin participates in an inventory check for a small preparedness cache. The container is physically present. Its authoritative inventory reveals one borrowed item, one item whose condition requires inspection, and one ordinary supply that was used and never replenished.

The resulting jobs are mundane: trace custody, replace or repair material, update the inventory, and retest availability. The cache never becomes a magic emergency chest.

Preferred implementation tier: persistent inventory/custody world state.

## 7. Two Muster Points, One Old Map

A Tideglass plan copy names a gathering point that made sense under an older local layout. A current operational copy uses another point. Taro, Pia, Mara, and Teo can establish chronology and present-day physical suitability without pretending that the older record was “wrong” in its own time.

The player can inspect both records and the actual sites. The resolution is a versioned correction plus provenance note.

Preferred implementation tier: investigation/world state.

## 8. False All-Clear

A correction is issued through the authoritative communications layer, but one old printed notice or copied instruction remains visible. One resident or visitor follows the stale version.

The quest concerns circulation and revision: identify the obsolete artifact, determine who plausibly saw it, distribute the corrected state, and retain the old copy as evidence if appropriate.

No malicious actor is necessary.

## 9. Visitor Count Mismatch

A rehearsal at the ferry or Battle Yard discovers that the local expected-presence list handles residents well but handles short-term visitors poorly. The fix must respect provenance and whatever privacy policy later becomes canon.

The exercise should never query omniscient Minecraft entity coordinates to produce a perfect roster. Direct observation, arrival records when legitimately available, voluntary check-in, and current work records are valid inputs.

## 10. Next Drill Remembers

A recurring drill runs again after one or more after-action items were completed. The second edition visibly uses the revised map, moved cache, new recipient list, changed sequence, or alternate route.

At least one old weakness should disappear. A different weakness may emerge. This makes preparedness persistent without a generic readiness score.

Preferred implementation tier: recurring event + versioned plan + persistent site projection.

## 11. Companion Relocation

A rehearsal explicitly includes residents’ companion Pokémon. A route that works for a person may be awkward for a large, slow, stressed, injured, or otherwise differently mobile companion. The solution may involve timing, route choice, a wider gate, a different waiting location, or a specific handler relationship.

No new Pokémon species, disability, injury, Capability, or care rule is canonized by this seed. Concrete execution requires existing character/Pokémon data and PTU/Caelo evidence.

## 12. The Accessibility Gap

A nominal route is technically open but is unsuitable for one participant or one operational load. Teo’s inspection and a real rehearsal reveal the problem before an emergency.

This can produce a small persistent world change: move an obstruction, mark a different path, adjust a door/gate assumption, or change the plan. The story value comes from competent preparation, not catastrophe.

## Longer arc: Plans That Remember

Several small drills and inspections across Ferry Landing, Mirador, Tideglass, the Battle Yard, and the Sendero gradually create a local history of corrected assumptions. The player sees older plan versions, physical modifications, new handoff habits, and residents who become better at their existing responsibilities.

The arc should avoid a secret master plan or inevitable disaster payoff. Its payoff is that a later ordinary incident is handled differently because previous work mattered. If a larger crisis eventually occurs, existing plans can help without guaranteeing success.

## Mechanically rich candidate: Mirador Safe-Down Under Live Pressure

Full intended version: a planned safe-down exercise at Mirador overlaps with genuine wild activity and worsening environmental conditions. Residents and companion Pokémon need a usable withdrawal lane while Nerea/Ema secure only essential observation state. Wild actors may cross or contest space. Some equipment remains physically present but outside combat ownership.

Required permanent capability categories:

- targeting/footprints/range/LoS: REQUIRED
- base movement legality: REQUIRED
- complete movement including push/pull/knockback/interception/forced movement: REQUIRED when lane protection, interception, displacement, collision, forced retreat, or partial stops are tactical
- core calculations: REQUIRED
- action economy/initiative: REQUIRED
- full turn/round lifecycle: REQUIRED
- full stateful damage pipeline: REQUIRED
- status lifecycle: REQUIRED if selected content applies statuses
- terrain/weather/hazards/zones/reactions: REQUIRED if the live environmental pressure has tactical effects
- move-specific behavior: REQUIRED, exact roster audit
- abilities: REQUIRED, exact roster audit
- items: REQUIRED if selected content uses them
- Trainer Features/perks: REQUIRED if Trainers use them
- AI legal-action infrastructure: REQUIRED
- AI tactical policy: REQUIRED
- Minecraft/Cobblemon/Craftics adapter/playback support: REQUIRED for faithful live presentation

Current full-version status: BLOCKED.

Reduced version: Mirador performs the safe-down, accounting, record custody, companion relocation, and route choice entirely through authoritative world state. Participants reach a safe position before any BattleSpec. If a wild threat then prevents withdrawal, an audited ordinary battle occurs in a stable clearing with a vetted roster and no unsupported environmental mechanics.

Allowed battle facts are narrow: `IMMEDIATE_ACCESS_CORRIDOR_CLEAR`, `IMMEDIATE_WILD_THREAT_WITHDREW`, or the actual audited combat result. The battle cannot issue ALL_CLEAR, complete the drill, prove the plan effective, establish the environmental cause, account for every resident, authorize access, or decide whether Mirador reopens.

Narrative premise retained: the checklist meets conditions it did not fully predict, and the community learns from the discrepancy.

## Promotion blockers

Before any seed becomes canon, locate or decide the relevant Caelo/Marea authority for emergency activation, current communications technology and conventions, permissible use of ferry/visitor records, actual physical route suitability, companion-Pokémon handling rules, institutional custody obligations, and any PTU Features/Skills/Capabilities needed for specific field actions.

A literal Caelo search in the currently indexed Narrative, AutoPTU-Java, and AutoPTU repositories did not surface a source during pass 184. Keep those questions open.