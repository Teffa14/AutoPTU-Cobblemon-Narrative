# Mutual Aid, Relief & Shared Resource Research Scan — Pass 202

Status: RESEARCH / PROVENANCE ONLY. NOT CANON.
Date: 2026-09-02

## Scope

This pass examines reusable structures for voluntary assistance, shared relief resources, community rebuilding, rescue requests, contribution tracking and post-crisis support. It does not establish Ouros welfare law, insurance, taxation, compulsory levies, charity doctrine, currency values, entitlement rules or institutional liability.

Repository inspection found adjacent coverage for crisis/rescue/recovery, service requests, transactions, custody, civic works, cooperative production, hospitality and public memory. No dedicated mutual-aid/shared-relief lifecycle was present under the current tree. The new seam therefore concerns who offers help, what resource was actually committed, what need it was linked to, who accepted responsibility for allocation, what was delivered, and what remained unresolved.

## Source findings

### Pokémon Mystery Dungeon — rescue jobs and bulletin boards

Public references:
- Bulbapedia, “Job (Mystery Dungeon)”: https://bulbapedia.bulbagarden.net/wiki/Job_%28Mystery_Dungeon%29
- Serebii, “Pokémon Mystery Dungeon — Missions”: https://www.serebii.net/mysteriousdungeon/missions.shtml

Reusable structure:
- needs can be represented as discrete requests;
- requestor, target, location and objective can remain separately identifiable;
- accepting a request does not mean the need has already been resolved;
- completion can be reported back after field work;
- rewards, when present, are a separate transaction from the rescue itself.

Ouros transformation:
- a local assistance request should keep request identity, beneficiary scope and completion evidence separate;
- helping someone does not automatically create friendship, ownership, employment or debt;
- an offered reward or reimbursement is governed separately from the social act of assistance.

Do not import:
- Mystery Dungeon rank points;
- reward tables;
- dungeon difficulty formulas;
- rescue-team hierarchy;
- automatic reputation.

### Mystery Dungeon player rescue culture — pay-it-forward pattern

Public references:
- r/MysteryDungeon Rescue/Dungeon Help Megathreads, including #13 and #15.

These community threads standardize requests with game, dungeon, floor and code/ID. They also explicitly encourage rescued players to help others later. This is useful as a social pattern because reciprocal aid can exist without one-to-one repayment.

Ouros transformation:
- `RECIPROCAL_CULTURE != PERSONAL_DEBT`;
- a resident may contribute to a shared relief effort because they previously received help without creating an enforceable bilateral obligation;
- provenance should preserve who contributed and what they intended, while allocation may legitimately benefit someone else.

Community convention is not PTU or Pokémon canon. It is used only as design evidence for asynchronous, request-driven mutual assistance.

### Pokémon Scarlet/Violet: The Teal Mask — Loyalty Plaza restoration fundraiser

Public reference:
- Gameranx summary of the post-story Loyalty Plaza restoration fundraiser: https://gameranx.com/features/id/476354/article/pokemon-scarlet-violet-teal-mask-what-happens-if-you-rebuild-loyalty-plaza/

Reusable structure:
- a damaged public place can remain damaged after the main incident;
- restoration can become a separate community-facing project;
- contributions can accumulate toward a physical change;
- the physical result can persist afterward.

Ouros transformation:
- recovery projects should outlive the crisis that caused them;
- contribution history and project completion should be separate;
- one contributor does not become sole owner of a public repair;
- a completed repair does not prove the underlying cause of damage or assign liability.

Do not import:
- exact contribution amount;
- reward thresholds;
- clothing/emote rewards;
- monument identity or Kitakami story content.

### PTU community campaigns — settlement construction/resource management

Public reference:
- r/PokemonTabletop, “I run a west marches TTRPG, and need help with city building mechanics.” (2024).

The thread shows actual Pokémon-tabletop campaign interest in persistent town construction and resource-management consequences. Suggested implementations are homebrew and include approaches that would be unsuitable for Ouros without mechanical review.

Reusable lesson:
- players value seeing contributions change a persistent settlement;
- resource allocation can create choices about which project proceeds first;
- persistent facilities can create later quest hooks.

Rejected import:
- permanently donating Pokémon as an abstract construction resource;
- invented facility bonuses;
- unverified production multipliers;
- any rule that treats Pokémon as fungible labor units.

Ouros must preserve Pokémon as individual actors and validate capability-dependent work through PTU/Caelo/AutoPTU when mechanics matter.

### Even After — community rebuilding TTRPG

Public reference:
- T.R. Grimm, “Even After”: https://grimmpathic-games.itch.io/even-after

The game describes rebuilding through time, space, resources and care rather than conquest. Its useful structural lesson is that recovery can ask what a community can currently contribute and how scarce support is shared.

Ouros transformation:
- relief scenes can revolve around competing legitimate needs rather than a villain;
- capacity, timing and stewardship can create consequences;
- recovery should be playable after immediate danger ends;
- social support can matter without becoming a universal relationship score.

No mechanics, card structure or prose are copied.

## Design synthesis

Useful reusable states:
- need reported;
- need verified or still provisional;
- aid offered;
- offer accepted, declined, redirected or expired;
- resource reserved;
- resource transferred;
- service delivered;
- partial fulfillment;
- substitute support offered;
- remaining need;
- contribution returned or released;
- recovery project complete;
- later review of whether distribution matched the available evidence.

Useful distinctions:

`NEED_REPORTED != NEED_VERIFIED`

`AID_OFFERED != AID_AVAILABLE_FOREVER`

`AID_ACCEPTED != AID_DELIVERED`

`CONTRIBUTION != OWNERSHIP_OF_PROJECT`

`CONTRIBUTION != REPUTATION_GAIN`

`RECEIVING_HELP != PERSONAL_DEBT`

`POOL_BALANCE != PTU_CURRENCY_BALANCE`

`RESOURCE_PLEDGED != RESOURCE_TRANSFERRED`

`VOLUNTEER_AVAILABLE != VOLUNTEER_AUTHORIZED_FOR_EVERY_TASK`

`POKEMON_PRESENT != LABOR_CAPABILITY_VERIFIED`

`PROJECT_COMPLETED != INCIDENT_CAUSE_RESOLVED`

## Relationship to current Marea canon

Marea already contains several natural owners for small-scale aid without creating a new institution:
- Mara can coordinate practical assistance through the Marea Field Office;
- Lia can expose transport constraints;
- Oren can identify care-related needs while governed medical effects remain outside Narrative;
- Teo can identify ordinary equipment-repair needs;
- Ivo can coordinate meal substitutions and purchasing;
- Brin can preserve cooperative lot/custody records;
- Taro/Pia can preserve contribution or project records when public documentation is appropriate.

No resident becomes a universal relief administrator.

## Thin Delivery Season opportunity

The Thin Delivery Season can produce a small mutual-aid response before its cause is known. Examples:
- one kitchen has surplus preserved ingredients while another lot is delayed;
- a producer lends reusable crates;
- Teo prioritizes repair of one shared cart;
- Lia finds a later unloading window;
- residents contribute time to sort a mixed lot.

These acts create evidence of response, not evidence of cause.

A successful relief action must not close the Thin Delivery Season investigation.

## PTU/Caelo boundary

This pass found no basis to invent:
- charity bonuses;
- morale points;
- social capital;
- automatic Loyalty changes;
- healing from narrative care;
- crafting output from volunteered labor;
- free Items created by community goodwill;
- currency duplication;
- skill-rank gains from volunteering;
- Trainer Feature effects from institutional participation.

Where assistance transfers an actual mechanical Item, currency amount, treatment, crafted object or Trainer/Pokémon capability, authoritative PTU/Caelo/AutoPTU state remains controlling.

Narrative may store the social and logistical provenance around that governed mechanical event.

## Battle-sensitive design lesson

Aid scenes do not need combat by default. If immediate danger interrupts delivery or evacuation, BattleSpec should receive only the combatants and battle-relevant geometry. Relief ownership, project priority, beneficiaries, contribution history and later distribution remain Narrative-owned.

A rich escort/withdrawal version may depend on complete movement, reactions, terrain, tactical AI and adapter support. A reduced version can secure noncombatants/resources before battle and run one ordinary audited confrontation.

## Originality boundary

No named Pokémon characters, distinctive plots, dialogue, dungeon maps, reward tables or homebrew mechanics are copied into Ouros. Sources contribute only high-level structures about requests, reciprocal assistance, contribution, persistent restoration and shared resource allocation.

## Recommended next slice

Prototype `The Shared Cart Repair` in Marea.

A cooperative cart used by several residents needs an ordinary repair. Teo can perform the work, but a replacement component and a short labor window come from separate sources. The player may help connect existing actors, contribute an already-authoritative item if one exists, or leave the work to proceed when dependencies become available.

The completed repair restores one ordinary logistical asset. It grants no stat bonus, reputation score, ownership share or Thin Delivery Season answer.