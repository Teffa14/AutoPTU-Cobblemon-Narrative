# Ouros Civic Governance & Public Works Seeds — Pass 20

Status: NON-CANON proposals. These are original Ouros candidates derived from high-level research patterns. No external character, plot or dialogue is transplanted.

## 1. The Bridge Nobody Agrees About

A river crossing has become unreliable. Merchants want a stronger permanent bridge, conservation workers want a seasonal crossing farther downstream, nearby residents want repairs to the old footbridge, and the transport operator prefers a ferry upgrade.

The players can collect traffic observations, survey ecological effects, inspect current infrastructure and present alternatives. No option is framed as obviously correct.

Future world outputs can include changed route traffic, altered market access, wildlife disturbance, a new service, deferred repairs or a later review after new evidence appears.

## 2. The Hearing Before the Storm

A public consultation about a new shelter is scheduled on the same day that credible severe-weather evidence starts arriving.

The body must decide whether to continue the meeting, convert it into an emergency coordination session, postpone it or authorize a temporary measure.

The interesting choice is procedural and practical rather than ideological: people who came to speak about the project still deserve a later route into the decision.

## 3. The Road That Solves the Wrong Problem

A settlement approves a road upgrade to improve market access. Field observation later shows that the true bottleneck is a failing dock connection, not road capacity.

Players can prove the mismatch before construction starts, after materials arrive or after phase one is complete. Each timing creates different sunk costs and political pressure.

## 4. One Crew, Three Repairs

A region has only one specialist construction crew available this season. A bridge, irrigation system and clinic roof all need major work.

Players can investigate urgency, dependencies and temporary mitigations. The final decision may sequence projects rather than select a permanent loser.

## 5. The Habitat Crossing

A busy route intersects a recurring Pokémon movement corridor. A proposed crossing structure could reduce conflict, but nobody yet knows which location the wild group actually uses consistently.

The civic body funds a field study before approving construction. Research players can shape public works directly without a battle requirement.

## 6. The Pilot Ferry

A remote settlement wants permanent ferry service. The operator refuses to invest without evidence of demand, while residents cannot create demand without transport.

A temporary seasonal pilot becomes the compromise. Players can help map demand, coordinate schedules, investigate ecological limits and document which services become viable during the trial.

## 7. The Empty Clinic Annex

A clinic expansion was completed years ago, but the expected specialist never moved to town. The building exists; the capability does not.

A new proposal asks whether to recruit the missing specialist, repurpose the annex or share it among rotating providers.

This reinforces the rule that infrastructure alone does not create a service.

## 8. The Market Relocation

A growing market wants to move into a larger square. The proposed space is also the main gathering point during festivals and a reliable resting place for a familiar wild Pokémon population.

The problem supports phased use, timed zoning, alternate layouts or refusal. The generator should preserve the competing uses instead of reducing the issue to merchant greed versus nature.

## 9. The Rejected Trail

Years ago, a proposed mountain trail was rejected after an incomplete hazard report. New survey evidence suggests the original route was dangerous but an alternate line is now feasible.

The historical rejection is not erased. It becomes evidence of why the new proposal must answer old concerns.

## 10. The Popular Wrong Map

A settlement has repeatedly invested in maintenance based on a public route map that is outdated. The actual traffic pattern shifted after an earlier world event.

Players can combine observation, transport records and resident testimony to establish current use before the next budget window.

## 11. The Gym Leader's Letter

A respected Gym Leader publicly supports a civic project. Their endorsement affects attention, but the Gym has no authored formal power over the decision.

The scenario explores influence versus mandate. The Leader may also have a legitimate institutional interest, such as training access or event traffic.

## 12. The Quiet Conflict of Interest

A civic member has a financial or family connection to a service provider bidding to implement a project. The relationship is not secret, but the settlement has never needed a formal disclosure process before.

The central problem is how to preserve a fair decision without automatically treating the actor as corrupt.

## 13. The Construction Season

Two projects are both approved, but seasonal weather makes it impossible to complete both before access closes.

The players can investigate whether one project has a viable temporary workaround. The decision changes which service remains vulnerable through the season.

## 14. The Public Garden Vote Without a Vote

Residents disagree about how to use a recovered vacant lot. Ouros canon has not established an election or voting procedure for this settlement.

The generator must not invent one. Instead, the settlement's authored decision procedure determines how proposals, consultations or leadership decisions work.

This seed exists partly as a guardrail test.

## 15. The Water Report

A farm district asks for irrigation expansion. Researchers report uncertain downstream effects on a wetland habitat.

The civic body can approve monitoring, a limited pilot, another study or a phased project. A single research roll cannot magically decide the ecological truth.

## 16. The Contract That Outlived Its World

A transport contract was written before a route was destroyed and rebuilt differently. Both the service provider and settlement believe the agreement still supports their position.

The players can document actual current dependencies and help define a replacement arrangement. No real-world contract law is assumed.

## 17. The Construction Camp

A major public project creates a temporary camp of workers, suppliers, food vendors and visiting Pokémon.

The camp changes local demand, traffic and ecology before the project is even finished. It can become a temporary hub with its own jobs and social scenes.

## 18. The Project Nobody Uses

A well-intentioned public facility is completed, but few residents use it. Instead of declaring the project a failure immediately, players can investigate access, location, communication, hours, trust and competing services.

The output may be redesign, new staffing, a new use or closure.

## 19. The Council Archive Gap

A controversial old decision is frequently cited in public debate, but the archive only contains the final notice. Meeting notes, evidence and objections are missing or were never preserved.

The absence is historical uncertainty, not automatic evidence of a cover-up.

## 20. The Neighboring Town's Shortcut

One settlement wants to improve a road that would redirect heavy traffic through a smaller neighboring community.

The project creates cross-settlement negotiation. Benefits and burdens are geographically separated, which makes the compromise problem more interesting than a local yes/no decision.

## 21. The Work Site Encounter

A public-works crew pauses after wild Pokémon repeatedly enter a survey zone.

Narrative objective: understand whether the equipment, food, noise or route change is causing the interaction, then decide whether work can resume safely.

Full tactical version:
- protection/retreat objective;
- unstable-bank or work-zone hazards;
- objective-aware wild AI;
- dynamic protected markers.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- move-specific behavior — PARTIAL;
- abilities/items as selected — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:
- static legal battle if an actual encounter occurs;
- survey markers remain outside battle state;
- no custom terrain damage;
- post-battle observation determines whether work resumes, reroutes or pauses.

## 22. Depot Chokepoint

Construction materials are stranded because the only depot exit has become unsafe.

Full tactical version:
- BREAK_THROUGH/PROTECT objective;
- interception around a narrow exit;
- possible push/pull consequences;
- tactical AI understands the objective.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — BLOCKING;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- full damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- move-specific behavior — PARTIAL;
- abilities/items — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:
- standard battle at a static depot entrance;
- success creates `route_access_restored` world state;
- delivery movement happens afterward in Minecraft rather than as an escort battle.

## 23. Pump House Shutdown

A damaged civic pump needs to be shut down while a Pokémon encounter is active nearby.

Full tactical version:
- REACH_LOCATION/ACTIVATE_OBJECT objective;
- periodically changing safe zones;
- battle events and infrastructure objective run together.

Dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- action economy/initiative — VERIFIED;
- full lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:
- legal static battle first or second;
- pump interaction remains overworld-only;
- no custom hazard or interaction action is duplicated in Minecraft scripts.

## 24. Hearing Interrupted

A public consultation is interrupted by a genuine safety event.

The civic process pauses rather than converting testimony into battle bonuses. Civilians are represented through overworld evacuation state unless a future encounter contract explicitly supports protected entities.

Full tactical version dependencies:
- complete movement including interception/forced movement if exits matter — BLOCKING;
- full lifecycle — PARTIAL;
- full damage/status behavior — PARTIAL;
- terrain/hazards/reactions if the incident needs them — BLOCKING;
- tactical AI — BLOCKING;
- adapter/playback — BLOCKING.

Reduced version:
- civilians evacuate outside the tactical engine;
- AutoPTU receives only the legal static combatants;
- the hearing resumes, relocates or defers based on world state after the incident.

## 25. Long Arc — The River Compact

Act 1: several settlements independently complain about the same river corridor for different reasons: transport reliability, erosion, habitat pressure and market access.

Act 2: field reports reveal that no single project solves every problem. Different bodies and factions propose a bridge, ferry upgrade, bank reinforcement, seasonal closure and habitat crossing.

Act 3: a temporary pilot changes traffic patterns and produces new evidence. Some predicted problems fail to occur; an unexpected secondary effect appears elsewhere.

Act 4: the final settlement agreement becomes a bundle of smaller measures rather than one megaproject. Years later, public memory may simplify the decision into a mythic 'great compromise', while the archive preserves the messier process.

## 26. Long Arc — Rebuilding the East Ward

Act 1: a damaged urban district has several missing capabilities after a prior crisis.

Act 2: residents, businesses, care providers, transport operators and conservation actors advance different priorities.

Act 3: players can participate through profession-specific work: surveys, logistics, hearings, repairs, research, media corrections, protection or fundraising if the world's economic model supports it.

Act 4: the rebuilt district does not return to its old snapshot. It becomes a new configuration shaped by which services and routes were restored first.

## 27. Long Arc — The Institution That Learns

Act 1: a civic body approves a project using reasonable but incomplete evidence.

Act 2: implementation reveals an unexpected failure. No villain is required.

Act 3: an institutional review identifies where assumptions, communication or dependencies broke down.

Act 4: the body changes its process. Future proposals require a new kind of field evidence or consultation. This altered procedure becomes persistent institutional memory and can later be challenged if it becomes too rigid.

## Canon questions intentionally left unresolved

- Which Ouros settlements have formal civic bodies?
- Are any offices elected, appointed, inherited, professional, rotating or informal?
- What relationship does the Pokémon League have to local administration?
- What ownership/property rules exist?
- Who can authorize route closures, construction or ecological restrictions?
- Which services are public, private, guild-run, faction-run or mixed?
- How are inter-settlement disputes resolved?
- What records are public by default?
- Which civic procedures are regional standards versus local custom?

No answer should be generated automatically merely because a seed requires a decision.
