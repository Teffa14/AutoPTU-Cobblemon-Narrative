# Shared ecological jurisdiction and co-management scan — Pass 276

Status: RESEARCH / PROVENANCE ONLY. No canon effect.
Date: 2026-09-05

## Question

How should Ouros represent an ecological decision when more than one human institution, community, landholder or operational body has legitimate but non-identical authority over the same habitat, resource, access route or intervention?

This follows Pass 275. That pass separated ecological evidence from a single decision owner's objectives and risk posture. Pass 276 addresses overlapping mandates and collective decisions without manufacturing a universal legal code or converting disagreement into ecological uncertainty.

## Existing Ouros constraints inspected

- `CURRENT_FOCUS.md` keeps all new work centered on Pokémon ecology and species behaviour.
- `design/ecology-development-program.md` requires ecology-driven quests/events, persistent consequences and explicit authority flow.
- `canon/ecosystem-conflict-managed-development-foundation.md` explicitly leaves institutional jurisdiction open for future design while canonizing that managed beginner areas can use monitoring, warnings, restrictions, deterrence, containment or relocation.
- `design/ecological-management-decision-governance-contract.md` already separates evidence, objectives, risk posture, thresholds and action selection for one decision context.
- `design/agreements-mediation-repair-layer.md` already separates disputes, negotiation, agreements, mediation and enforcement power. Pass 276 must not duplicate it. It instead defines whether a proposed ecological action has sufficient mandate across overlapping scopes before any agreement or implementation occurs.
- `design/ouros-source-authority-and-species-policy.md` keeps Caelo/Kairos as references. `SOURCE_HAS_RULE != OUROS_USES_RULE`.

## Public-source findings

### USGS — joint-jurisdiction environmental governance

Source: Flye, Sponarski, McGreavy & Zydlewski, “Leading the charge: A qualitative case-study of leadership conditions in collaborative environmental governance structures,” Journal of Environmental Management, 2023.
URL: https://www.usgs.gov/publications/leading-charge-a-qualitative-case-study-leadership-conditions-collaborative

Reusable structure:
- natural-resource management can require collaboration among federal, state and tribal agencies;
- joint-jurisdiction systems depend on shared goals, transparency and trust;
- collaboration quality is a governance property, not evidence that every participant has identical authority or objectives.

Ouros lesson: a multi-party decision record should preserve each mandate and objective separately, plus shared-goal and information-sharing state. Consensus must not be inferred from attendance at the same meeting.

### USGS — interjurisdictional ecosystem management

Source: Pope et al., “Fishing for ecosystem services,” Journal of Environmental Management, 2016.
URL: https://www.usgs.gov/publications/fishing-ecosystem-services

Reusable structure:
- ecological processes cross political boundaries;
- management therefore benefits from interjurisdictional relationships and explicit tradeoffs;
- ecosystem boundaries and administrative boundaries need not match.

Ouros lesson: habitat scope, ecological-process scope and institutional jurisdiction scope must be different fields. A migrating population or shared resource can cross several authority areas without creating one omnipotent manager.

### USGS — adaptive governance under conflict

Source: Allen et al., “Adaptive management of rangeland systems,” 2017.
URL: https://www.usgs.gov/publications/adaptive-management-rangeland-systems

Reusable structure:
- adaptive management combines monitoring, evaluation and adjustment;
- adaptive governance can require sharing power and knowledge among stakeholders;
- legal certainty and environmental uncertainty can pull in different directions.

Ouros lesson: a review horizon can be shared while action authority remains partitioned. New ecological evidence can require re-coordination without automatically voiding every existing mandate.

### USGS — multi-jurisdiction collaboration limits

Source: Lemieux et al., “Climate change collaboration among natural resource management agencies: lessons learned from two US regions,” 2015.
URL: https://www.usgs.gov/publications/climate-change-collaboration-among-natural-resource-management-agencies-lessons

Reusable structure:
- shared biophysical resources often span multiple public-land jurisdictions;
- time, funding and communication constraints can block fully integrated action;
- issue linkages and organizational tradeoffs matter.

Ouros lesson: coordination failure is not automatically bad faith. A body may lack time, budget, geographic competence or implementation capacity while still accepting the same ecological evidence.

### IUCN — overlapping conserved territories and shared governance

Source: IUCN WCPA, “Recognising territories and areas conserved by Indigenous peoples and local communities (ICCAs) overlapped by protected areas,” 2024.
URL: https://iucn.org/story/202410/iucn-wcpa-publishes-new-guidelines-indigenous-peoples-local-communities-and-protected

Reusable structure:
- protected areas can overlap pre-existing collectively managed territories and conserved areas;
- governance arrangements include government, shared, private, Indigenous/local-community and delegated forms;
- overlap can require recognition of pre-existing rights and governance rather than treating the later designation as total replacement.

Ouros lesson: `OVERLAP != SUPERSESSION`. A new conservation mandate must not silently erase an older access, stewardship or custodial mandate. Which powers are exclusive, concurrent, consultative or delegated must be authored explicitly.

### IUCN — co-management as shared functions, rights and responsibilities

Source: Borrini, “Collaborative management of protected areas: tailoring the approach to the context,” 1996.
URL: https://iucn.org/resources/publication/collaborative-management-protected-areas-tailoring-approach-context

Reusable structure:
- collaborative management shares management functions, rights and responsibilities among stakeholders;
- arrangements vary substantially by context.

Ouros lesson: do not create a single generic `CO_MANAGED=true` flag. Store the action class and who may propose, approve, veto, implement, review or receive notice for that class.

## Pokémon / tabletop design references

### Pokémon Ranger

Nintendo describes Rangers as protecting Pokémon in their natural habitats, solving natural disasters and resident problems with Pokémon cooperation, within an organized Ranger structure.
URL: https://www.nintendo.com/fr-fr/Jeux/Nintendo-DS/Pokemon-Ranger-272442.html

Reusable high-level pattern only:
- ecology-facing institutions can provide missions and operational responses;
- Pokémon abilities can help overcome environmental obstacles;
- temporary cooperation does not require trainer ownership.

Ouros transformation: an ecology mission can be issued by one body while another body controls access or infrastructure. No Ranger Union, Capture Styler, mission, character or plot is imported.

### PTU community — Orre campaign using a regional council

Source: r/PokemonTabletop, “Sharing My Orre Region Campaign,” 2022.
URL: https://www.reddit.com/r/PokemonTabletop/comments/xcgcx0

Reusable high-level pattern:
- a campaign can make a regional council and local development pressures part of ongoing world conflict;
- institutional control can change over time instead of remaining static backdrop.

Ouros transformation: use governance state as a source of quest pressure and consequence. Do not import the campaign's villain, council, region plot or distinctive events.

### PTU community — West Marches settlement building

Source: r/PokemonTabletop, “I run a west marches TTRPG, and need help with city building mechanics,” 2024.
URL: https://www.reddit.com/r/PokemonTabletop/comments/1afsyga

Reusable high-level pattern:
- persistent multiplayer campaigns create player-driven settlements and facilities;
- building decisions can become long-term shared-world state.

Ouros transformation: later player organizations may become stakeholders in habitat/access decisions only when canon gives them a real mandate. Player investment alone must not manufacture ownership or jurisdiction.

## Proposed design lessons

1. Separate ecological truth from governance truth.
2. Separate geography from ecological-process scope and legal/operational jurisdiction.
3. Store authority per action class rather than per location alone.
4. Allow concurrent authority without assuming equal power.
5. Preserve explicit veto, consultation, notice and implementation roles.
6. Treat lack of consensus as governance state, not contradictory ecology.
7. Allow a narrow emergency action when a declared mandate authorizes it, while requiring later review if another mandate is affected.
8. Never infer `SILENCE == CONSENT`, `PARTICIPATION == APPROVAL`, or `OVERLAP == SUPERSESSION`.
9. Route negotiated commitments into the existing agreements/mediation layer rather than duplicating negotiation mechanics here.
10. Minecraft signage, gates, guards and route changes remain presentation/world state; they do not create PTU blockers or forced movement.

## Canon status

CANON-ALIGNED:
- managed ecological areas and future institutional responses are allowed by the existing canon foundation;
- institutional jurisdiction details remain intentionally open;
- no institution gains new authority from this research.

PROPOSED:
- `ECOLOGICAL_JOINT_JURISDICTION_V1` as a governance/authority contract;
- a Sendero fixture involving two fixture-only authority scopes and a temporary coordinated action.

UNCERTAIN:
- which actual Marea/Sendero institutions exist;
- whether any authority is governmental, communal, private, delegated or mixed;
- exact emergency powers, veto powers, appeal routes and consultation requirements;
- whether player-created organizations can ever receive delegated ecological authority.

## Mechanical boundary

The reduced governance loop needs no AutoPTU tactical adjudication. If a disagreement becomes a structured encounter, dependencies must be declared by exact capability family. A mandate, permit, closure notice or conservation order cannot synthesize battlefield terrain, reactions, interception, damage, statuses, Moves, Abilities, Items, Trainer Features or tactical AI.
