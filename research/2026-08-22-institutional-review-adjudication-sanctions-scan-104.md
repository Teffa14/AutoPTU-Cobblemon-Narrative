# Pass 104 Research — Institutional Review, Adjudication, Sanctions & Appeals

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon. Not a PTU rules source.

Date: 2026-08-22

## Why this pass exists

The repository already has strong boundaries for incidents, evidence and custody (`case-authority-custody-layer.md`), negotiated commitments (`agreements-mediation-repair-layer.md`), prospective public decisions (`civic-governance-public-works-layer.md`), battle/contest institutions, and scoped credentials/permissions (`credentials-permissions-eligibility-layer.md`).

What it does not yet own is the institutional decision that can occur after evidence is gathered or a rule violation is alleged:

- what rule version applied;
- which body actually had mandate to review it;
- what facts the reviewer accepted, rejected or left unresolved;
- what interpretation of the rule was used;
- what consequence was ordered;
- what changed later through correction, rehearing, appeal, expiry or reinstatement.

This is deliberately narrower than a legal system. Ouros has no established universal criminal code, court hierarchy, police power, prison system, civil procedure or real-world constitutional structure. The reusable target is institutional adjudication: Gym inspections, Contest/tournament discipline, credential reviews, access suspensions, club discipline, conservation-permit review, professional/institutional complaints, grant compliance findings and similar bounded procedures where a specific institution already has an authored mandate.

## Existing-repository boundary inspected before research

### Case / authority / custody

The case layer stores reports, evidence, claims, hypotheses, participants, custody and authored institutional mandates. It explicitly states that Ouros does not have a universal legal system and that `authority` means authored mandate/responsibility.

Reusable boundary for this pass:

`CASE` answers what happened, what evidence exists and who may investigate.

It should not silently decide the institutional consequence.

### Agreements / mediation / repair

The agreements layer explicitly distinguishes negotiation from unilateral institutional action and states that an accepted agreement does not acquire legal enforceability automatically.

Reusable boundary:

`AGREEMENT` records commitments accepted by parties.

An adjudicated decision can exist when the parties do not agree, but only where an authored institution has authority to decide the bounded issue.

### Credentials / permissions / eligibility

The credential layer already supports suspension/revocation history and versioned eligibility rules.

Reusable boundary:

This pass may produce an authorized decision that tells the credential layer to suspend, restore or review a credential. It does not duplicate credential state.

### Battle institutions / contests

Those layers already preserve formal results, circuit rules, venue state and public reception. They need an external review object when a protested result, cheating allegation, unsafe venue, invalid roster or institutional breach must be reviewed after the event.

## Source register

### 1. Pokémon.com — Showdown at Dark City

URL: https://www.pokemon.com/us/animation/seasons/1/episode-39-showdown-at-dark-city

Source type: official Pokémon animation episode page.

Observed structural pattern:

Dark City contains rival would-be Gyms whose conduct has damaged the town. The broader episode/inspection context provides a useful Pokémon-world precedent for Gym legitimacy being subject to standards beyond simply winning battles.

Reusable lesson:

A battle institution can be reviewed as an institution. Competitive strength and institutional fitness are different questions.

Do not copy:

Dark City, Yas/Kaz Gyms, characters, dialogue or plot resolution.

### 2. Pokémon Inspection Agency references

URLs:
- https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Inspection_Agency
- https://bulbapedia.bulbagarden.net/wiki/DP193

Source type: secondary Pokémon reference preserving animated-series institutional details.

Observed structural pattern:

The Pokémon Inspection Agency reviews whether Gyms follow League standards, may determine whether unofficial Gyms qualify, and can threaten closure or loss of Badge-granting authority. The Pewter Gym special provides a useful sequence: notification/problem -> inspector -> institutional review -> additional evaluation -> bounded decision.

Reusable lessons:

1. Inspection is not identical to investigation.
2. An institution can review competence, safety or standards without alleging criminal wrongdoing.
3. The available remedy can be scoped: retain authorization, lose a specific institutional privilege, require another evaluation, or change leadership/operations.
4. A remedial test can be part of review when the institution's rules actually allow it.

Do not copy:

Nurse Joy as inspector, Pewter Gym facts, Latias evaluation battle, specific standards or outcomes.

### 3. Pokémon.com — Come What May!

URL: https://www.pokemon.com/us/animation/seasons/7/episode-11-come-what-may

Source type: official Pokémon animation episode page.

Observed structural pattern:

A Contest participant uses an external device to improve presentation, the device is exposed, and the participant is disqualified.

Reusable lessons:

1. Rules violations can affect an official result without creating a separate villain arc.
2. Evidence may surface during the event itself.
3. The consequence can be tied narrowly to the activity: disqualification from that event rather than universal social condemnation.
4. Formal result state and later public reputation should remain separate.

Do not copy:

Jessie, Dustox, the rainbow device, contest sequence or dialogue.

### 4. Play! Pokémon Resources and Documents

URL: https://play.pokemon.com/en-gb/resources/documents/?filter=all

Source type: official current Play! Pokémon resource index.

Observed structural pattern:

Current organized play separates tournament rules, standards of conduct, accessibility policy and penalty guidance rather than treating every problem under one undifferentiated rulebook.

Reusable lesson:

An Ouros institution should reference the exact rule family/version relevant to its decision. Safety, eligibility, event procedure, conduct and competition legality can be separate scopes.

This source is used as a design-structure reference only. Real Play! Pokémon rules do not become in-world Ouros law.

### 5. Play! Pokémon glossary and penalty guidance

URLs:
- https://www.pokemon.com/uk/play-pokemon/about/tournaments-glossary
- https://www.pokemon.com/static-assets/content-assets/cms2/pdf/play-pokemon/rules/play-pokemon-vg-rules-formats-and-penalty-guidelines-en.pdf

Source type: official organized-play documentation.

Observed structural patterns:

- organizer and judge roles are distinct;
- a Head Judge has bounded final authority for tournament rulings;
- penalties have different severity;
- penalties can be recorded across sanctioned events;
- severe/repeated issues may affect later participation;
- mistakes and intentional misconduct are not collapsed into one category;
- a consequence should be proportionate to the kind/severity of problem described by the relevant rules.

Reusable lessons:

1. Separate rule interpretation, operational decision and sanction.
2. Preserve the exact official who made the decision and their scope.
3. Record prior decisions without automatically escalating every later issue.
4. Use bounded consequences and explicit reasons rather than a generic `bad_reputation` score.
5. A decision can become final for one event while broader institutional review remains possible.

Do not import:

TPCi penalty names, exact escalation tables, player-account rules, age divisions, suspension policy, real tournament procedures or any real-world enforcement model.

### 6. Pokémon Professor Community — Seeing It Through scenario series

URLs:
- https://professorprogram.pokemon.com/news/490213
- https://professorprogram.pokemon.com/news/499939

Source type: official Professor Program scenario discussion.

Observed structural pattern:

Operational incidents at large events can require different people to own different questions. A judge may determine rules implications while an organizer decides whether an event can continue and technical staff investigate infrastructure. Information should be escalated to the correct role rather than spread as unverified certainty.

Reusable lessons:

- mandate matters more than generic rank;
- fact finding, technical diagnosis, rule interpretation and operational continuity may belong to different actors;
- procedural urgency does not justify collapsing uncertainty;
- incident communications should preserve what is known and who owns the next decision.

### 7. PTU Campaign Structure guidance

URL: https://pokemontabletop.fandom.com/wiki/Campaign_Structure

Source type: public PTU rules/advice mirror; secondary access to campaign-structure guidance.

Observed structural pattern:

PTU campaigns can be organized around law-enforcement, academies, exploration teams or other institutions, not only Gyms. The guidance also encourages modular adventures and player choice rather than forcing every campaign beat into one central plot.

Reusable lesson:

Institutional review should be a reusable world system capable of serving multiple campaign modes. It should generate bounded consequences and follow-up opportunities without forcing every dispute into combat or a master conspiracy.

Do not use this mirror as the authority for exact PTU mechanical text.

### 8. Governance-dispute research

URL: https://sms.onlinelibrary.wiley.com/doi/full/10.1002/smj.3181

Source type: open-access research on governance disputes in online communities.

Observed high-level finding:

The research distinguishes bargaining over preferred outcomes from problem solving focused on the attributes of the underlying problem. It also emphasizes preserved discussion records as valuable evidence of how governance decisions emerged.

Reusable lessons for Ouros:

- disputes about the rules themselves are different from violations under settled rules;
- governance review can produce rule revisions instead of sanctions;
- archived reasoning matters because future participants may revisit why a rule changed;
- a disagreement can end with unresolved dissent rather than a fabricated consensus.

No real software-license governance procedure is imported into Ouros.

## High-level design synthesis

### A. Four questions must stay separate

A robust institutional review asks four independent questions:

1. What happened?
2. Which authored rule/version applies?
3. What does that institution decide under that rule?
4. What consequence or remedy follows from that decision?

The engine must never compress these into `guilty = true`.

### B. Findings are scoped claims

A finding can be:

- CONFIRMED;
- NOT_ESTABLISHED;
- UNRESOLVED;
- OUTSIDE_SCOPE;
- PROCEDURALLY_INVALID;
- SUPERSEDED_BY_REVIEW.

A finding says what the reviewing body concluded for its mandate. It does not retroactively rewrite world truth.

### C. Review needs rule provenance

Every institutional decision should store:

- institution/decision maker;
- mandate reference;
- rule identifier and version;
- evidence actually considered;
- findings;
- interpretation;
- ordered consequence/remedy;
- effective date;
- review/appeal route if one exists;
- public/private summary boundaries.

If a rule changes next year, the old decision remains interpretable under the old rule version.

### D. Consequences should target the actual institution

Useful examples:

- warning/correction request;
- result amendment where the competition rules authorize it;
- event disqualification;
- temporary suspension from an activity;
- credential review;
- mandatory reinspection;
- restitution/repair obligation when an authored system supports it;
- access restriction;
- project pause;
- grant/funding review;
- institutional probation;
- no action because the allegation was not established.

Do not produce universal imprisonment, fines, arrest, criminal records or property seizure without future authored canon.

### E. Review and appeal are append-only

A successful review does not delete the original decision.

Chronicle should be able to show:

`initial decision`
→ `review request`
→ `new evidence / rule interpretation`
→ `amended or overturned decision`
→ `restoration/reinstatement event`

This prevents world history from silently rewriting itself.

### F. Institutional error is allowed

Institutions in Ouros may make reasonable mistakes.

The system may preserve:

- incomplete evidence;
- incorrect interpretation later corrected;
- procedural conflict of interest;
- outdated rule version;
- missing notice;
- unreliable sensor/log;
- disagreement among reviewers.

This creates consequences without requiring corruption as the explanation.

### G. Players need procedural agency without social mind control

A PC can:

- submit evidence;
- contest a claim;
- request review where an authored process allows it;
- accept or reject a voluntary settlement;
- comply with or defy an institutional consequence and face world-state consequences;
- expose procedural flaws;
- advocate for rule revision.

A generated social roll cannot force a PC to confess, feel remorse, accept guilt, forgive, reveal private memories, adopt an ideology or waive a review right.

### H. Battle results can be evidence, not adjudication

AutoPTU can authoritatively provide:

- who participated;
- legal actions under the battle rules;
- battle result;
- damage/status/event transcript where implemented.

It should not decide:

- whether a Gym followed its institutional mandate;
- whether an event rule was violated outside battle;
- whether a credential should be suspended;
- whether conduct was intentional;
- what remedy is proportionate.

Those remain world/institution state.

## Copyright / transformation boundary

No protected dialogue, episode scripts, named NPC arcs or distinctive plots are imported. Sources are used only for high-level institutional structures: inspection, bounded authority, documented rules, disqualification, role separation, review, proportionate consequences and persistent decision history.

## PTU / Caelo validation boundary

This pass does not create Charm, Command, Guile, Intimidate, Intuition or Education DCs for hearings. It does not create arrest, restraint, testimony, lie detection, confession, interrogation, surrender, legal authority or punishment mechanics.

The complete primary Caelo corpus was not reliably retrievable in this runtime. No Caelo rule is attributed without primary evidence. Any future adjudication interaction using a PTU Skill, Feature, Capability, Move or Pokémon power must be validated separately against project-designated PTU/Caelo sources and current AutoPTU implementation.

Super PTU Online Helper was not exposed as an invokable capability in this runtime. No validation is attributed to it.

## Candidate implementation direction

The most useful next document is an `institutional-review-adjudication-sanctions-layer` that sits after Case evidence and before Credentials/Permissions, Battle Institutions, Contests, Funding or other domain-specific consequence owners.

The layer should be generic enough for a Gym inspection or tournament protest but too narrow to become an accidental universal justice system.