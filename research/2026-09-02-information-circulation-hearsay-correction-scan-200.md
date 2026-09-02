# Information Circulation, Hearsay & Correction Scan — Pass 200

Status: RESEARCH / PROVENANCE. Not canon.
Date: 2026-09-02

## Research question

How can Ouros preserve rumors, repeated claims, public notices, corrections and changing local impressions without turning repetition into truth, creating a global reputation meter, or duplicating PTU social/perception mechanics?

## Existing Ouros fit

The current canon already establishes several necessary facts:

- Estación Mirador keeps claims with provenance and revision history rather than owning regional truth.
- Mara reads reports rather than receiving omniscient truth.
- Nerea is willing to revise published conclusions.
- Taro is comfortable preserving contradictory testimony.
- Tideglass preserves oral-history deposits, market records and copies of ecological observations.
- the Thin Delivery Season begins with multiple attributed explanations and no established cause.
- relationship history is per actor rather than one global friendship score.

Repository inventory searches before writing found no dedicated layer named for rumor, gossip, hearsay or reputation. Existing knowledge, provenance, correspondence, public-memory, translation, visitor, market and service layers can supply source records, but none owns the transmission chain between a claim and the people who later repeat, qualify or correct it.

## Public-source findings

### Pokémon Legends: Arceus — reports that become investigations

Bulbapedia's request walkthrough documents cases where a resident reports an unusual observation and the player investigates before the phenomenon is understood. Request 19 begins from Yota's report of an unusual Ponyta. Request 20 begins with Paira's account of a will-o'-the-wisp and later identifies the observed phenomenon as a Chimchar.

Reusable structure:

`reported observation -> attributed interpretation -> field verification -> narrower corrected understanding`

The useful lesson is not the specific Pokémon or plot. It is that an honest witness can accurately report what they perceived while being wrong about the explanation.

Source:
https://bulbapedia.bulbagarden.net/wiki/Appendix:Legends:_Arceus_walkthrough/Requests_1-30

### Pokémon Mystery Dungeon — persistent public information surfaces

Pokémon News in Red/Blue Rescue Team and Rescue Team DX is a recurring newsletter delivered through the world. Issues include ordinary guidance and reports about wider events. The bulletin board separately exposes job requests.

Reusable structure:

- public information has an edition/version;
- different channels can coexist;
- a posted request or newsletter issue persists as an artifact of what was publicly stated at a given time;
- receiving an issue is different from every resident automatically knowing its contents.

Sources:
https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_News_(Mystery_Dungeon)
https://bulbapedia.bulbagarden.net/wiki/Appendix:Mystery_Dungeon_walkthrough/Chapter_11

### Pokémon Ranger — ordinary reports can be checked without becoming regional emergencies

Ranger Quests repeatedly begin from concrete local requests or reports: a Pokémon that normally visits is absent or behaving differently, someone is missing, tools have moved, or a local obstacle exists. The structure supports local verification work without treating every report as a crisis or as fact beyond its scope.

Reusable structure:

`local report -> bounded field check -> concrete result -> local follow-up`

Source:
https://bulbapedia.bulbagarden.net/wiki/Ranger_Quest

### The Alexandrian — redundant clues and source independence

Justin Alexander's Three Clue Rule argues for multiple clues supporting conclusions so an investigation does not depend on one fragile path. The related node-based design discussion emphasizes redundancy and multiple routes through an investigation.

For Ouros, the useful adaptation is narrower: apparent source count must not be confused with independent corroboration. Three residents repeating the same visitor's story are three transmission events but one origin chain unless other evidence is independent.

This is structural scenario-design research only, not setting canon or a mandatory numeric rule.

Sources:
https://www.thealexandrian.net/creations/misc/three-clue-rule.html
https://www.thealexandrian.net/creations/misc/node-design/node-design2.html

### PTU community practice — investigations commonly touch Skills

A 2025 r/PokemonTabletop discussion about a first PTU session recommends Perception, Intuition, Guile and Intimidate checks for investigation-oriented play. Community advice has no rules authority, but it reinforces the need not to create a parallel narrative truth-detection system.

Source:
https://www.reddit.com/r/PokemonTabletop/comments/1iz38d4/tips_and_ideas_for_a_first_session_ptu/

## PTU / project-source cross-check

Read-only AutoPTU source evidence contains actual PTU Skill fields including Guile and Perception, while project catalog/validation material references Charm, Command, Guile, Intimidate, Intuition and Perception in Trainer-class prerequisites and effects.

Therefore Narrative may record:

- what an actor said;
- what another actor heard;
- what source chain a later statement derives from;
- whether a correction was issued and who received it;
- authored confidence or epistemic labels;
- evidence references.

Narrative must not invent:

- automatic lie detection;
- automatic credibility scores derived from social relationships;
- Skill check outcomes without an authoritative PTU/Caelo rule path;
- universal knowledge from player dialogue;
- mechanical Charm/Guile/Intuition/Perception bonuses;
- a hidden global reputation number.

Relevant read-only evidence:
- `AutoPTU/PTUDatabase-main/PTUDatabase/Classes/Skills.cs`
- `AutoPTU/TRAINER_CLASS_CATALOG.md`
- `AutoPTU/TRAINER_CLASS_VALIDATION.md`

A fresh literal `Caelo` repository search across Narrative, AutoPTU-Java and AutoPTU returned no indexed results in this pass. Any Caelo-specific social, reputation, rumor, information-access or Skill rules remain unresolved.

## Reusable design lessons

### Preserve origin chains

If Lia tells Mara, Mara tells Ivo, and three market residents repeat Ivo's account, the system should be able to discover that those statements share an upstream origin.

Repeated transmission can establish social reach. It cannot independently establish truth.

### Preserve transformation

A statement can be shortened, qualified, generalized or exaggerated without requiring malicious intent.

Useful operations include:
- direct report;
- paraphrase;
- omission;
- qualification;
- amplification;
- contradiction;
- correction;
- withdrawal;
- uncertainty added;
- uncertainty lost.

These are descriptive provenance states, not automatic morality judgments.

### Corrections have reach

A correction can be valid and still fail to update everyone who heard the older version.

This supports persistent world consequences without forcing NPC stupidity. People can act on the best version actually available to them.

### Public surfaces need versions

Boards, handouts, market notices, ferry advisories and copied reports should reference a current publication version while older physical projections may still exist until replaced.

An outdated sign is evidence of an old statement, not evidence that the old statement remains current.

### Reputation should remain distributed

The canonical quest taxonomy permits faction reputation, but the playable foundation already rejects a generic friendship meter. This pass should therefore model attributable impressions and institutional history rather than a universal scalar.

Examples:
- Sela remembers that the player honored a yard agreement.
- Lia has heard an unverified complaint from a visitor.
- Tideglass records a public correction.

Those facts can affect later authored behavior without being collapsed into `REPUTATION = 67`.

## High-value Ouros applications

1. Thin Delivery Season: vendor explanations can spread farther than their evidence supports.
2. Mirador ecology: two reports can look independent until provenance shows a common origin.
3. Ferry operations: delay time can be verified while causal explanations remain unverified.
4. Battle Yard: an outdated schedule can create conflicting good-faith expectations.
5. Visitor layer: outside claims can circulate without canonizing outside geography or events.
6. Tideglass: corrections and editions can remain visible as history.
7. Wildlife windows: one sighting can become an exaggerated population claim unless source scope is preserved.
8. Market transactions: an observed quote can become a misleading claim about regional prices if quantity/context is stripped away.

## Candidate narrative arc

`What Bruma Thinks It Knows`

Over several ordinary weeks, small claims move through Puerto Bruma and adjacent institutions. Some are confirmed, some narrowed, some contradicted, and some simply remain unresolved. The player can learn to inspect source chains rather than treating volume as certainty. Residents also update at different times because their access to information differs.

The arc does not require a mastermind, propaganda faction or deception plot. Its main antagonist is ordinary information loss across a living community.

## Battle-aware research boundary

A circulating route warning may motivate a field check. If the field team encounters one immediate wild threat, a battle can establish only narrow timestamped facts such as:

- a specific actor was present;
- immediate passage was obstructed;
- the actor withdrew or was defeated according to battle outcome;
- passage was locally clear at the handoff moment.

The battle cannot establish:

- that the original rumor was malicious;
- population-scale presence;
- permanent route safety;
- ecological cause;
- the identity of the first speaker;
- future recurrence;
- universal public knowledge.

## Provenance status

CANON-APPROVED inputs:
- Marea locations, residents and institutions;
- Thin Delivery Season uncertainty;
- Mirador provenance/revision principle;
- Tideglass contradictory-testimony role;
- per-NPC knowledge/history principle.

PROPOSED from this research:
- information-transmission records;
- source-lineage resolution;
- correction reach;
- versioned public information surfaces;
- distributed impression records;
- Marea seeds and long arc.

UNCERTAIN / requires Caelo or later canon decision:
- formal defamation or privacy law;
- institutional publication standards beyond existing authored practice;
- mechanical social-check adjudication;
- faction reputation mechanics;
- official emergency-notice authority;
- whether any supernatural means can establish truth or memory under Caelo rules.
