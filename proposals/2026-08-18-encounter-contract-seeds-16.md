# Ouros Capability-Aware Encounter Seeds — Pass 16

Status: NON-CANON proposals. These candidates preserve narrative ambition while making engine dependencies explicit.

Each seed has an intended FULL version and a REDUCED version. REDUCED never means fake the unavailable mechanic in Minecraft; it means preserve the story premise using a smaller set of reviewed capabilities.

## 1. Storm Signal Tower

Premise:
A coastal warning tower fails during severe weather while territorial Pokémon occupy its maintenance decks. Nearby settlements depend on the signal for safe travel.

FULL:
Electrical danger zones migrate across the arena between round boundaries, forcing repositioning while players secure access to tower controls.

REDUCED:
The storm controls overworld access and visuals only. The platform is a static legal battlefield; after a standard encounter, players repair the tower through an authoritative overworld interaction.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING

Current profile: REDUCED DESIGNABLE; end-to-end Minecraft execution still blocked by adapter support.

Open PTU/Caelo review: exact weather, electrical hazard and repair interactions.

## 2. Shattered Causeway

Premise:
A damaged elevated causeway has become contested by frightened wild Pokémon while repair crews attempt to reopen the route.

FULL:
Push, pull, knockback and interception matter because displacement toward damaged edges changes positioning risk.

REDUCED:
Damaged edges are hard static blockers. No combatant can be scripted off the platform. Players clear or calm the contested area before repairs continue.

Capability dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- core calculations — VERIFIED
- action economy/initiative — VERIFIED
- full stateful damage pipeline — PARTIAL
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 3. Glassworks Heat Cycle

Premise:
An old industrial glassworks has become a nesting site. Restarting one furnace changes which passages are safe and draws defensive Pokémon deeper into the facility.

FULL:
Heat zones activate and cool in a reviewed cycle; terrain state changes influence legal positioning and possibly conditions.

REDUCED:
Furnace state changes only between separate rooms. Each room uses a static arena profile. Players decide which furnace to activate in the overworld before the next encounter.

Dependencies:
- base movement legality — VERIFIED
- full turn/round lifecycle — PARTIAL
- status lifecycle — PARTIAL if heat applies conditions
- terrain/weather/hazards/zones/reactions — BLOCKING
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 4. Tidal Observatory

Premise:
A sea observatory can be reached only during a narrow tide window. Inside, rising water changes access to instruments and wild Pokémon refuges.

FULL:
Water level changes within combat, altering traversable cells and movement modes.

REDUCED:
Each water level is a separate static world/battle state. Crossing between levels happens outside combat at explicit checkpoints.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- complete movement including forced movement — not required for reduced, BLOCKING for any current-driven displacement
- terrain/weather/hazards/zones/reactions — BLOCKING for dynamic flooding
- lifecycle — PARTIAL
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 5. Hanging Orchard Rescue

Premise:
Workers and Pokémon are stranded on suspended orchard platforms after support lines fail.

FULL:
Players defend vulnerable actors, intercept threats and manage forced displacement between narrow platforms while rescue lines are secured.

REDUCED:
Stranded actors remain outside the tactical grid. Players clear predefined safe platforms in ordinary encounters, then perform rescue interactions in the overworld.

Dependencies:
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING
- terrain/weather/hazards/zones/reactions — BLOCKING if falling hazards are tactical
- AI tactical policy — BLOCKING for protect-target behavior
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 6. Relay Station Breach

Premise:
A remote communications relay is being disabled node by node while a local faction tries to isolate the valley.

FULL:
Players fight while protecting or activating battlefield objects. Both sides can alter node state through legal actions.

REDUCED:
Each relay node is an overworld interaction guarded by a separate ordinary battle. No object receives hidden HP or scripted damage inside AutoPTU.

Dependencies:
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- items — BLOCKING if tools are battle items
- objective interaction support — requires adapter/playback, BLOCKING
- AI tactical policy — BLOCKING for node-aware opponents

Current profile: REDUCED DESIGNABLE.

## 7. Market Procession Escort

Premise:
A regional cultural procession passes through a crowded district while several groups have incompatible reasons to stop or redirect it.

FULL:
Escort positions, interception and protected actors matter throughout a moving battle.

REDUCED:
The procession reaches a predetermined shelter before combat begins. Players resolve the confrontation at that stop; later route decisions depend on the result.

Dependencies:
- complete movement including interception/forced movement — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 8. Burrower at the Switchyard

Premise:
A rail or freight switchyard repeatedly loses service because burrowing Pokémon alter the ground beneath key junctions.

FULL:
The encounter changes traversable terrain as tunnels open and collapse, modifying cover and routes.

REDUCED:
Burrow locations become static arena geometry generated before battle. After resolution, the overworld updates route availability based on observed tunnel state.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- base movement legality — VERIFIED
- terrain/weather/hazards/zones/reactions — BLOCKING for live terrain mutation
- move-specific behavior — PARTIAL if a Move causes terrain changes
- abilities — PARTIAL where relevant
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 9. Weather Observatory Guardian

Premise:
An isolated observatory's instruments have begun attracting or aggravating a powerful resident Pokémon during extreme atmospheric conditions.

FULL:
Weather phases affect the battle and may change legal tactics as instruments activate.

REDUCED:
Weather remains narrative/visual. The tactical arena is neutral; instrument activation happens before or after battle and can change future world state.

Dependencies:
- core calculations — VERIFIED does not by itself satisfy battlefield weather
- terrain/weather/hazards/zones/reactions — BLOCKING
- abilities — PARTIAL
- move-specific behavior — PARTIAL
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 10. The Archive Doors

Premise:
A historical archive is threatened during a civic dispute. Different actors want records protected, seized, copied or destroyed for different reasons.

FULL:
The tactical objective includes protecting multiple interactable archive stations while opponents choose between fighting and damaging/using objects.

REDUCED:
The archive is secured behind a single chokepoint. The battle decides whether attackers gain physical access; actual record interactions occur only after combat through world-state actions.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING for object-aware choices
- items — BLOCKING if item use matters tactically
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 11. Rival With Footage

Premise:
A recurring rival has access to public recordings of previous formal matches and deliberately prepares for patterns they have actually observed.

FULL:
The AI policy consults permitted scouting memory, adapts target/action preferences and still operates under legal-action constraints.

REDUCED:
A human-authored or preapproved static roster/policy reflects only publicly known preparation. The narrative may say the rival studied footage, but the engine does not claim dynamic tactical learning.

Dependencies:
- AI legal-action infrastructure — VERIFIED
- AI tactical policy — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- items — BLOCKING if the roster depends on battle items
- Trainer Features/perks — BLOCKING if the rival plan depends on them
- adapter/playback — BLOCKING

Current profile: STATIC REDUCED ONLY.

## 12. Roost Evacuation

Premise:
A construction emergency forces conservation workers to move through a nesting area while defensive Pokémon react to noise and intrusion.

FULL:
The battle supports protected noncombatants, escape lanes, calming/capture choices and potentially reaction/interception behavior.

REDUCED:
Evacuation is a noncombat phase. Any unavoidable battle occurs only after workers reach shelter; success writes back to the nesting/route state separately.

Dependencies:
- complete movement including interception/forced movement — BLOCKING for full
- status lifecycle — PARTIAL if calming depends on status mechanics
- terrain/weather/hazards/zones/reactions — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 13. Command Nest

Premise:
A dangerous nesting complex is defended by several coordinated groups around one persistent guardian.

FULL:
Supporting units and guardian behavior interact through a reviewed command structure without inventing hidden bonuses.

REDUCED:
Players encounter outer groups as separate ordinary battles. The guardian battle is normal initiative with no extra actions, shared buffs or command traits unless the actual Pokémon rules provide them.

Dependencies:
- action economy/initiative — VERIFIED
- full lifecycle — PARTIAL
- abilities — PARTIAL
- Trainer Features/perks — BLOCKING if any human command interaction is used
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: SEQUENTIAL REDUCED.

## 14. Ancient Guardian Wake Cycle

Premise:
An archaeological mechanism activates a guardian system in stages as deeper chambers regain power.

FULL:
A continuous phase boss changes behavior or arena state at reviewed thresholds.

REDUCED:
Use several separate approved encounters with explicit world-state checkpoints. No hidden extra turns, arbitrary HP resets or direct damage between battles.

Dependencies:
- full turn/round lifecycle — PARTIAL
- full stateful damage pipeline — PARTIAL
- status lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- move-specific behavior — PARTIAL
- abilities — PARTIAL
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: SEQUENTIAL REDUCED.

## 15. Healing Spring Dispute

Premise:
Several communities and wild Pokémon rely on a mineral spring whose changing flow has created conflict over access.

FULL:
A confrontation around the spring uses reviewed terrain or restorative interactions when legal.

REDUCED:
The spring has no tactical effect. Battle, negotiation or capture happens on neutral terrain; access consequences are applied afterward by the narrative/world-state layer.

Dependencies:
- terrain/weather/hazards/zones/reactions — BLOCKING for battlefield spring effects
- items — BLOCKING if restorative items are used in battle
- abilities — PARTIAL
- status lifecycle — PARTIAL
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 16. Museum Security Drill

Premise:
A museum conducts a public response exercise after a series of artifact-security incidents. Staff want a realistic drill without risking exhibits or visitors.

FULL:
The scenario supports nonlethal objectives, object protection, Trainer Feature interrupts, reviewed item use and surrender/withdrawal states.

REDUCED:
Run a standard exhibition battle in an empty training annex. Security choices, route blocking and artifact handling are evaluated outside combat as separate simulation steps.

Dependencies:
- Trainer Features/perks — BLOCKING
- items — BLOCKING
- terrain/weather/hazards/zones/reactions — BLOCKING if security zones react tactically
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 17. The Last Safe Platform

Premise:
A mine or cavern route is destabilizing while workers and Pokémon retreat toward the final reinforced platform.

FULL:
A survival encounter uses collapsing zones, forced movement and timed safe areas.

REDUCED:
Collapse state advances only between encounters. The final platform battle uses static geometry; if the party wins or safely withdraws, the route state updates afterward.

Dependencies:
- complete movement including forced movement — BLOCKING
- full lifecycle — PARTIAL
- terrain/weather/hazards/zones/reactions — BLOCKING
- AI tactical policy — BLOCKING
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## 18. Signal Through the Marsh

Premise:
Researchers need to place several beacons across a marsh to understand an unusual migration pattern while wild Pokémon react to the equipment.

FULL:
Beacon placement is part of tactical action economy and changes zones or information during encounters.

REDUCED:
Beacon placement occurs only in the overworld at validated locations. Encounters near each beacon are ordinary legal battles or noncombat observations, and the migration model updates from completed placements.

Dependencies:
- base movement legality — VERIFIED
- action economy/initiative — VERIFIED
- items — BLOCKING if beacon is a battle item
- terrain/weather/hazards/zones/reactions — BLOCKING if beacon creates tactical zones
- adapter/playback — BLOCKING

Current profile: REDUCED DESIGNABLE.

## Portfolio rule

These seeds are intentionally distributed across different blocked families. They should not all be chosen for production simultaneously.

Near-term content should favor premises whose REDUCED forms use already verified geometry, base movement, calculations, initiative and legal-action generation while keeping world-state interactions outside the battle runtime. More advanced FULL forms can be promoted as the exact Java and adapter categories gain tests.

No seed in this file establishes PTU/Caelo legality, Pokémon Moves, Abilities, item effects, Trainer Features, hazard effects, boss action rules, objective scoring or rewards.