# Worker Associations, Collective Representation & Safety Voice — Research Scan 115

Status: research/provenance only. Not Ouros canon. External fiction is inspiration, not rules authority.

## Why this gap exists

The existing Workplaces layer explicitly leaves unions, guild authority, labor law, wage standards and Pokémon labor rights unresolved. Civic Governance can record stakeholder groups and practical influence, Agreements can record voluntary commitments, and Institutional Review can record bounded decisions. None of those layers currently owns persistent worker-created organizations, representation mandates, workplace safety voice, cross-workplace professional networks or collective workplace action.

Pass 115 therefore investigates a neutral systems layer that can represent worker associations without silently importing a modern real-world labor regime.

## Repository overlap reviewed before research

Relevant existing layers reviewed:

- `design/workplaces-professions-staffing-layer.md`
- `design/civic-governance-public-works-layer.md`
- `design/agreements-mediation-repair-layer.md`
- `design/institutional-review-adjudication-sanctions-layer.md`
- `design/credentials-permissions-eligibility-layer.md`
- `design/crisis-rescue-recovery-layer.md`
- `design/manufacturing-production-quality-layer.md`
- `design/supply-chains-procurement-inventory-layer.md`
- `design/social-bonds-mentorship-clubs-layer.md`

The full design/research/proposals inventories were also checked for a dedicated labor/worker-representation layer. None was found.

## Source 1 — Pokémon Horizons: Galar Mine

Source: Pokémon.com, “Charge! Galar Mine!” and the official Part 2 recap.

URLs:
- https://www.pokemon.com/us/animation/horizons/1/charge-galar-mine
- https://www.pokemon.com/us/pokemon-news/pokemon-horizons-the-series-part-2-recap-quiz

Observed pattern:

Galar Mine is simultaneously a workplace, tunnel system, Pokémon habitat and crisis site. Human workers are affected by the same unexplained situation disturbing wild Pokémon. The episode does not require the workers to become combatants or villains for the workplace to matter.

Reusable design lesson:

Workers can be important sensors of world change. Their observations should be stored as evidence from people who repeatedly occupy a site, rather than treated as generic NPC chatter. A mine crew may notice vibration, ventilation, route, Pokémon-behavior or equipment changes before an outside investigator does.

Ouros transformation:

A worker association or safety group can aggregate repeated observations from multiple shifts while preserving who observed what and when. Collective reporting should not automatically prove the reported cause.

## Source 2 — Pokémon Horizons: Exceed and former employees

Source: Pokémon.com, “The Treasure of Eternity.”

URL: https://www.pokemon.com/uk/animation/horizons/2/the-treasure-of-eternity

Observed pattern:

Friede returns to a company where he previously worked. His former employment, institutional records and access history remain narratively relevant after he leaves the organization.

Reusable design lesson:

Employment history survives a job. Former workers can retain knowledge, relationships, reputational history and legitimate or expired credentials without remaining loyal to management or sharing the goals of every current employee.

Ouros transformation:

Worker associations can preserve retired-worker or former-worker institutional memory without making those people current employees. Representation, access and employment must remain separate.

## Source 3 — Poké Ball Factory

Source: Bulbapedia summary of “A Frenzied Factory Fiasco!”

URL: https://bulbapedia.bulbagarden.net/wiki/XY079

Observed pattern:

The Poké Ball Factory contains managers, workers, storage, conveyors and public tours. When the facility is infiltrated, workers and managers are distinct actors from the attackers, and normal production infrastructure becomes part of the incident.

Reusable design lesson:

A workplace has internal roles and shared operational knowledge. An incident can affect workers collectively without making “the factory staff” a single-minded faction.

Ouros transformation:

A worker association should model membership and representation without collapsing every employee into one opinion or one political bloc.

## Source 4 — Pokémon Adventures construction workers

Source: Serebii manga summary, Chapter 481 / VS Bisharp.

URL: https://www.serebii.net/manga/bw/481.shtml

Observed pattern:

Construction workers on Route 4 have a recognizable work rhythm, shared break space and common environmental problem: sandstorms repeatedly interrupt road work. Their workplace culture includes recreation during breaks, while the construction site remains exposed to changing environmental conditions.

Reusable design lesson:

Repeated work routines can create informal communities before any formal association exists. Shared problems can generate practical coordination, traditions, safety knowledge and mutual support.

Ouros transformation:

The system should support an informal workgroup becoming a safety committee, craft association, mutual-aid network or formal representative body only when evidence/world events support that transition.

## Source 5 — Virbank Complex as an anti-pattern

Source: StrategyWiki guide for Pokémon Black 2/White 2 Virbank Complex.

URL: https://strategywiki.org/wiki/Pok%C3%A9mon_Black_2_and_White_2/Virbank_Complex

Observed game structure:

A supervisor asks the player to get workers back to work, and progress requires battling them.

Reusable warning:

This is a useful videogame abstraction but a poor default for a persistent world. A worker pausing, refusing or leaving work should not be modeled as a combat obstacle whose autonomy disappears after defeat.

Ouros transformation:

When work stops, record an observable reason if available: safety concern, schedule dispute, missing materials, fatigue, damaged equipment, conflicting instructions, weather, personal absence or collective action. Battle must never settle the legitimacy of a workplace claim.

## Source 6 — PTU public living-world guilds

Source: public Reddit recruitment post, “Super Pokémon Online - PTU Living World RPG,” August 7, 2025.

URL: https://www.reddit.com/r/PokemonTabletop/comments/1mkct0y/super_pok%C3%A9mon_online_ptu_living_world_rpg/

Observed pattern:

The living-world pitch explicitly allows player-driven institutions, including founding a guild, inside a persistent economy/world that changes through player actions.

Reusable design lesson:

Associations can be player-created durable institutions rather than prewritten factions. Their identity can persist even when membership, leaders or projects change.

Ouros transformation:

Worker/professional associations should use the same persistent-institution principle. A player-founded mechanics association, courier mutual-aid network or ranger field society can exist without automatically acquiring legal authority.

## Source 7 — PTU official Torkoal spotlight

Source: Pokémon Tabletop RPG official blog, “Pokémon Spotlight: Torkoal.”

URL: https://pokemontabletop.com/pokemon-spotlight-torkoal/

Observed pattern:

One proposed Torkoal variant is framed as the result of a specialized breeding project undertaken by a guild of blacksmiths. The same post presents a long-lived Torkoal associated with generations of smithing.

Reusable design lesson:

A craft guild can function as an intergenerational knowledge institution, not merely a shop or faction. A profession can preserve techniques, standards, tools and reputational memory across individual careers.

Ouros transformation:

Professional associations may maintain apprenticeships, shared archives, common facilities, quality norms or mutual aid. None of those functions automatically grants PTU Features or mechanical crafting bonuses.

## Source 8 — OSHA worker-participation guidance as systems inspiration

Source: U.S. Occupational Safety and Health Administration, “Safety Management - Worker Participation.”

URL: https://www.osha.gov/safety-management/worker-participation

Observed systems pattern:

The guidance emphasizes that workers often possess unique knowledge of hazards and can participate in inspections, incident review, training, hazard reporting, procedure revision and program evaluation.

Reusable design lesson:

Frontline knowledge is a distinct information source. A persistent world gains credibility when the people who repeatedly operate a machine, route, clinic, mine or ferry can generate observations that management and outsiders do not automatically know.

Ouros transformation:

Create a neutral `WORKPLACE_REPRESENTATION_BODY` / `SAFETY_VOICE_GROUP` pattern that can collect observations, submit proposals and request review. Do not import OSHA law, retaliation statutes, committee thresholds or U.S. legal rights into Ouros.

## What not to import

Do not import from real-world systems without explicit canon review:

- statutory union recognition;
- mandatory bargaining;
- strike law;
- lockout law;
- wage/hour law;
- pension systems;
- occupational-safety statutes;
- collective-agreement enforceability;
- specific election procedures;
- labor courts;
- anti-retaliation statutes;
- dues rules;
- closed-shop/open-shop concepts;
- modern national labor ministries.

These sources are used only to understand information flow, representation and organizational persistence.

## High-level patterns worth reusing

1. Workers as longitudinal observers
Repeated exposure to the same environment can produce unique knowledge.

2. Representation is scoped
A spokesperson can represent members for one issue without owning their opinions on every topic.

3. Membership is not unanimity
An association can issue a majority position while recording dissent, abstention or non-participation.

4. Workplace conflict need not imply villainy
Staffing, safety, scheduling, environmental conditions, procedures and resource allocation can create legitimate conflict among actors with compatible long-term goals.

5. Informal groups can become institutions
Break-room networks, craft circles, shift committees and mutual-aid arrangements can evolve into persistent organizations.

6. Former workers preserve history
Retirees and former employees can become archives of institutional knowledge without retaining access or decision authority.

7. Collective action is an event, not a moral label
A coordinated pause, petition, refusal, meeting or work stoppage records behavior. Its legitimacy and consequences remain separate questions.

8. Pokémon participation needs agency
An institution using Pokémon for work does not automatically authorize an association to speak for those Pokémon. Individual Pokémon identity, ownership/custody, willingness and authored routines remain separate.

## PTU/Caelo mechanical boundary

No worker-association mechanic was validated from the project’s unavailable primary Caelo corpus in this run.

Do not invent:

- Charm/Command/Guile bonuses for representation;
- collective morale bonuses;
- union/guild Features;
- strike combat effects;
- teamwork buffs;
- safety-committee rerolls;
- craft-guild crafting bonuses;
- profession-based Skill Ranks;
- Pokémon labor abilities;
- command authority over coworkers or Pokémon.

Exact PTU mechanics remain governed by authoritative project sources and current AutoPTU implementation.

## Engine-facing implication

Most worker-association stories are social/institutional world state. Combat becomes relevant only when a separate incident intersects the workplace: evacuation, sabotage, wild-Pokémon disturbance, rescue, blocked access or similar events.

When combat occurs, worker claims, votes, agreements and legitimacy remain outside AutoPTU. The battle transcript can establish tactical facts only.

## Research outcome

Recommended new layer:

`design/worker-associations-collective-representation-layer.md`

Primary design responsibility:

Persist worker-created organizations, scoped representation, membership history, workplace-safety voice, professional/craft networks, collective proposals, member voting/position records, mutual aid and coordinated workplace actions while remaining neutral about Ouros labor law.
