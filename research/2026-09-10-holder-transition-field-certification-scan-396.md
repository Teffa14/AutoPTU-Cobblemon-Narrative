# Holder-transition and field-certification research scan — Pass 396

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-10
Narrative baseline inspected before writing: `115b3f59cf33c2bc6ef1204b8d3cf197b8558c4a`

Nothing in this file is canon. Public sources are used only for high-level structural lessons. Names, plots, dialogue, locations, characters and proprietary mechanics are not imported.

## Repository duplicate check

The repository tree was inspected recursively before this pass. The recent Pass 338–395 resource, handoff, recovery, evidence and post-restore chain was rechecked together with canon/governance boundaries, proposals, research history, `sources/kairos/KAIROS_SOURCE_INDEX.md`, and the current holder mutation sites.

Repository code search found three production holder mutations: reserved checkout and return in `tools/global_npc_resource_reservations.py`, plus authorized handoff in `tools/global_npc_resource_handoffs.py`. Pass 394 correctly treated holder disagreement as indeterminate because those mutations did not share a complete event journal. Pass 395 therefore could not strengthen that result without inventing missing history.

Source-name searches were also used to avoid repeating heavily processed references. Pokémon Conquest, Pokémon Flux, Pokémon Burning Scales, Pokémon Living World, PTU Night Rangers/Hollow Underdeep, The Reckless Rollers and several recent archaeology/logistics sources already have prior research entries and were not selected as primary inspiration here.

## Source 1 — GS1 EPCIS visibility events

Source:
https://support.gs1.org/support/solutions/articles/43000755325-what-is-electronic-product-code-information-services-epcis-

Related GS1 explanation:
https://support.gs1.org/support/solutions/articles/43000734385-what-is-the-link-between-epc-and-epcis-

Accessed: 2026-09-10.

Reusable structure:
EPCIS models real-world events around tracked objects and separates questions such as what happened, when, where and in what business context. The standard is designed for assets that move through processes and organizations rather than assuming current location explains the full past.

Ouros transformation:
A `WorldResource` can retain its current holder and location while a separate append-only holder-transition record preserves the causal sequence of checkout, return and handoff. Each event needs stable identity, semantic time, resource identity, prior holder, next holder and an optional source reference to the transaction that caused it.

The Ouros implementation does not adopt EPCIS schemas, identifiers, vocabulary, network architecture or compliance requirements.

## Source 2 — PTU campaign listing: Pokémon Rainbow Wing

Source:
https://startplaying.games/adventure/cmtllycv60020js04gedayb8z

Accessed: 2026-09-10.

The public campaign description presents a trainer selection process where finalists use unfamiliar or shared laboratory Pokémon and are judged on adaptation, command, treatment of partners and conduct, then continue into exploration, research and recurring relationships.

Reusable structure:
A field qualification can evaluate process and stewardship rather than only final victory. Shared institutional equipment or temporary responsibility can become part of character assessment. A candidate can achieve the immediate task while still creating later consequences through poor documentation, care or handoff practice.

Ouros transformation:
A proposed field-certification exercise can rotate a mundane survey kit among several candidates. The meaningful state is who held the kit at each observation and whether the handoff was documented, not a battle score. No Johto locations, Professor Elm variant, finalists, rental-Pokémon scenario, encounters or campaign plot are imported.

## Source 3 — Pokémon Climate Redux fan project

Source:
https://pokemon-climate-redux.fandom.com/wiki/Pok%C3%A9mon_Climate_Redux_Wiki

Accessed: 2026-09-10.

The public project description uses environmental change as a regional theme and places communities inside ongoing ecological disruption.

Reusable structure:
Environmental conditions can convert an ordinary field assignment into a consequential world-state problem. The useful narrative pivot is escalation of context rather than automatic escalation into combat.

Ouros transformation:
A certification survey may begin as routine equipment rotation and later become useful evidence after an unexpected environmental change. The earlier readings, who collected them and which physical instrument was in use become important. No Morinet setting, project-specific disasters, characters, educational material, creatures or plot are imported.

## PTU / Caelo / Kairos cross-check

`sources/kairos/KAIROS_SOURCE_INDEX.md` was rechecked as a routing aid only. Relevant routes include campaign/session structure, encounter creation, movement, hazards, terrain/weather, Items/Gear, Skills/Edges/Features and utility/research-oriented classes. The index does not grant mechanics to Ouros and does not replace the supplied PTU/Caelo material.

The field kit in this pass remains a mundane `WorldResource` unless an exact PTU Item mapping is later approved. Possession, checkout or custody does not prove legal item use, item effect support, a Trainer Feature, a Skill check or a tactical interrupt.

## Read-only engine evidence

AutoPTU-Java main inspected 2026-09-10: `f4c5c9172e82f7ba01210cb130d982bb1971a992`, merge #422, “Add authoritative combatant-entry ability hook”. This is new evidence beyond Pass 395 for the exact combatant-entry / Impostor Ability path. It does not establish complete Ability coverage, complete switching, or the full turn/round lifecycle.

AutoPTU Python main inspected 2026-09-10: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its latest change remains presentation-only and grants no additional tactical capability.

No engine repository was modified.

## Reusable Ouros lessons

Current state and transition history should remain separate authorities with explicit reconciliation.

A shared tool can create social and investigative consequences without becoming a PTU battle Item.

Routine fieldwork can become retrospectively important when later environmental evidence changes the meaning of earlier observations.

Disagreement over who held a resource should remain uncertainty until a causal event record proves the sequence. Once an authoritative journal exists for a covered path, a direct contradiction should fail recovery rather than become accidental in-world mystery.

## Canon boundary

No institution, certification system, survey technology, environmental incident, location, NPC, faction, species or legal authority is approved here. Those remain proposed or unresolved until explicit canon promotion.
