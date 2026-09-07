# The Timber Without a Wreck — Pass 334

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Premise

After severe coastal conditions, a heavy weathered structural timber is found on a shore or working edge reachable from Puerto Bruma. The object has joinery, fastener scars and an old painted or stamped fragment that may correspond with material in the Tideglass Archive.

No wreck is canonically established by the discovery.

The timber could have come from a vessel, an old landing, waterfront infrastructure, a previously disturbed site, transferred construction material or another source not yet known. Its current location proves only where it was observed now.

## Why Puerto Bruma fits

Puerto Bruma is already canon as Marea Interior's coastal service hub. Tideglass Archive, Marea Field Office, ferry activity and repair work already place records, practical maritime observations and material maintenance in the same settlement.

This proposal reuses those facts without creating a new port authority, salvage law, maritime archaeology profession, named vessel or offshore site.

Useful existing actors:

- Taro Min can own archive-custody and historical-comparison work without owning the final truth.
- Pia Min can retrieve or deliver copies while retaining explicit receipt/provenance boundaries.
- Lia Morn can supply dock/arrival observations within what she actually recorded.
- Mina Cors can contribute practical coastal observations from trips she actually made.
- Mara Veyra can coordinate a field response based on received evidence.
- Dr. Nerea Sol can document ecological use if the evidence reaches an offshore or shoreline feature.
- Teo Lark can identify ordinary tool/material characteristics only within knowledge the character plausibly has; he does not become an omniscient archaeologist.

No listed NPC gains expertise or knowledge merely because this proposal names them.

## Opening state

A persistent object ID is created for the timber after authoritative discovery.

Initial observations may include:

- current position;
- dimensions and visible construction features without converting them into invented mechanical statistics;
- condition;
- attached organisms or other ecological traces where observed;
- marks, paint layers or fastener patterns;
- whether the object appears recently deposited at this feature;
- witness statements about when it first appeared.

The system records observations. It does not jump directly to `OLD_SHIPWRECK_COMPONENT`.

## Investigation loop

The player can photograph/document the object, request archive comparison, ask who observed the shoreline before and after the weather event, compare historical maps or waterfront records, revisit after another tide/weather window, and support a later remote or specialist survey if world state justifies one.

Tideglass may find several plausible matches rather than a single answer. A historical drawing might show similar joinery on a landing. A vessel repair ledger might record replacement timbers with comparable marks. An older shoreline plan may show structures that no longer exist.

A useful branch is that the first archive match is genuine but incomplete: the mark belongs to a workshop, contractor, fleet, district or repair practice rather than one unique vessel. The evidence becomes more useful without becoming magically conclusive.

## Possible explanation families

The final authored explanation may use one or several of these, but none is canonized here:

- the timber detached from an old coherent submerged site;
- it came from waterfront infrastructure that was dismantled or lost;
- it was reused between structures before entering the water;
- it detached from one site long ago and was redeposited repeatedly;
- previous recovery or construction moved it before the current event;
- several archive records describe the same material tradition, causing an early false uniqueness assumption;
- a newly detected debris field is related but not the timber's original context;
- no parent site can be established with current evidence.

Sabotage, theft and illegal salvage are not default explanations.

## The possible submerged site

If later evidence justifies one, the world may author a coherent submerged feature with its own stable ID and survey history.

Its first meaningful state should be `SITE_OBSERVED_WITH_EVIDENCE`, not `DUNGEON_UNLOCKED` or `TREASURE_AVAILABLE`.

Possible content surfaces:

- structural remains mapped in place;
- scattered material whose distribution matters;
- ecological occupation that developed after abandonment;
- erosion or storm exposure changing what can be observed;
- archival claims that fit some parts of the site and conflict with others;
- public interest that creates pressure for a fast conclusion;
- stewardship decisions about access, documentation or specialist recovery.

## Character and faction dynamics

Taro may prefer preserving source context before making a confident public identification. Lia may care about keeping current harbor operations clear of hazards. Nerea may argue that ecological occupation must be documented before intervention. Mara may need a practical access decision before historical interpretation is complete.

Those are potential role pressures, not prewritten conflicts. Actual beliefs must derive from each NPC's goals and received evidence.

The player can improve cooperation by moving precise information between actors. The world-agent system must preserve who received which version and when.

## Consequence structure

A successful investigation can produce durable outcomes without solving every historical question:

- the timber receives an evidence-backed catalog identity;
- a speculative public label is corrected;
- a shoreline feature gets monitoring status;
- a remote survey is commissioned or postponed;
- a site map gains a new revision;
- one object is conserved after a justified recovery event;
- a possible parent site remains protected from casual disturbance;
- ecological observations become part of the site's record;
- Tideglass gains a documented uncertainty rather than a fabricated certainty;
- later storms expose or move additional material and reopen the case.

## Reduced implementation — usable before aquatic parity

The reduced version keeps all meaningful progress above water or between scenes.

Use:

- persistent object IDs;
- observation/provenance events;
- archive lookup and document delivery;
- interviews and contradictory but honest testimony;
- shoreline revisits;
- remote-survey results authored as semantic world events;
- map revisions;
- feature-scoped access states;
- specialist recovery/conservation resolved between scenes when later canon permits it;
- ordinary static AutoPTU encounters only when conflict naturally occurs.

The player can complete the narrative premise by determining what is justified, what remains uncertain and what should happen next. Underwater traversal is not required.

## Full intended version — capability gated

A later full version may allow a physical survey/dive into a coherent submerged site.

Potential encounter objectives:

- document marked structural nodes without disturbing them;
- reach a survey station and return;
- protect a specialist while an observation completes;
- withdraw when environmental state crosses a safe threshold;
- respond to a Pokémon encounter without treating every resident as an enemy;
- preserve mapped context rather than maximize object pickup;
- recover one threatened item only when world/canon authorization exists.

Potential environmental elements include water-limited LoS, Swim-capable traversal, current or forced movement, unstable structure, timed environmental phases, debris hazards, rescue/interception, persistent conditions and non-defeat objectives.

None may be implemented by Minecraft approximation when the corresponding AutoPTU capability is absent.

## Capability dependency matrix

Targeting/footprints/range/LoS: ordinary static combat is currently usable; underwater visibility, water-mediated sight and unusual obstruction need exact additional verification.

Base movement legality: ordinary audited movement is usable; swimming, diving, climbing wreck structure or other aquatic traversal are not assumed.

Complete movement including push/pull/knockback/interception/forced movement: required for currents, rescue, interception, drifting debris or displacement near unsafe structure. Current rating remains PARTIAL.

Core calculations: ordinary audited calculations are usable. No pressure, oxygen, salvage, survey or structural-integrity formula is invented.

Action economy/initiative: ordinary battle primitives are usable. Custom document/recover/stabilize actions require an authoritative contract.

Full turn/round lifecycle: required for timed current changes, visibility phases, collapses, survey countdowns or delayed environmental events. Current rating remains PARTIAL.

Full stateful damage pipeline: required for impact, collapse, crushing, fall or environmental damage. Current rating remains PARTIAL.

Status lifecycle: required for any real persistent restraint, exposure or other tactical condition. Current rating remains PARTIAL.

Terrain/weather/hazards/zones/reactions: required for dynamic water, unstable wreck zones, debris, reactive collapse, shelter/air pockets or equivalent tactical terrain. Current state remains mixed/partial/blocking by subfamily.

Move-specific behavior: every Move interacting with water, structure, debris, rescue or sensing remains individually gated.

Abilities: every Ability proposed to assist aquatic movement, sensing, breathing, protection or recovery remains individually gated.

Items: dive gear, ropes, lights, survey devices, lifting equipment or conservation tools receive no tactical effects without rules evidence.

Trainer Features/perks: no Researcher, Chronicler, Survivalist or other Feature gains a custom archaeology/diving benefit. Family remains PARTIAL.

AI legal-action infrastructure: ordinary audited legal battle choices are usable.

AI tactical policy: full protect-specialist, withdraw, preserve-site and non-defeat objective reasoning remains BLOCKING in the general case.

Minecraft/Cobblemon/Craftics adapter/playback: may render authoritative world and battle results; end-to-end support remains PARTIAL/BLOCKING for the rich version.

## Canon questions deliberately left open

No answer is authored here for:

- exact shoreline feature;
- whether the timber is from a vessel;
- whether a submerged site exists;
- age or historical period;
- vessel/structure name;
- cause of loss;
- ownership;
- recovery authority;
- salvage law;
- cultural significance;
- ecological occupants;
- what records Tideglass ultimately contains;
- whether the incident becomes a dungeon;
- whether combat occurs.

The proposal becomes stronger when those answers emerge through future canon decisions rather than being smuggled in through a research pass.