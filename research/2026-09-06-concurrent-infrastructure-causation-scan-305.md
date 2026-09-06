# Concurrent infrastructure causation scan — Pass 305

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-06
Canon effect: NONE

## Research question

Can an Ouros infrastructure failure preserve more than one contributing cause without collapsing independent evidence into either a single cause or an unresolved contradiction?

This pass follows Pass 303, which separated accidental failure, tampering, actor linkage and intent, and Pass 304, which made those findings durable. Existing executable behavior treated independent accidental-cause evidence plus tampering evidence as `CAUSE_CONTESTED`. That remains correct when the evidence supports competing explanations. It is incomplete when an additional independent analysis supports that both factors materially contributed to the same failure.

## New public sources

### NIST — Surfside Champlain Towers South investigation briefing

Source: NIST presentation, `CTS2_BELL_NCSTAC_June2022_CTS.pdf`.
Public URL: https://www.nist.gov/system/files/documents/2022/06/21/CTS2_BELL_NCSTAC_June2022.pdf

Reusable lesson:
- a failure investigation can retain multiple potential causes and contributors while hypotheses are tested;
- initiation and progression of a failure can require separate causal questions;
- the existence of several supported factors does not itself establish how those factors combine.

Ouros transformation:
- accidental deterioration and deliberate tampering may coexist as evidence families;
- they remain contested until a distinct evidence claim supports a combined causal explanation;
- the combined explanation is stored as a later epistemic finding, not retroactively written into the original failure event.

Not imported:
- building details;
- engineering conclusions;
- thresholds or forensic methods;
- any real-world casualty narrative.

### NTSB-hosted incident investigation material — contributing factors

Source: public NTSB docket document describing root, primary, secondary and contributing causes.
Public URL: https://data.ntsb.gov/Docket/Document/docBLOB?FileExtension=pdf&FileName=3+-+Engineering+BBC+AFRICA+Class+Damage+Survey+Post+Casualty+Actions+8+OCT+24_Redacted-Rel.pdf&ID=19109346

Reusable lesson:
- an incident can be explained by a combination of equipment, procedural, human and external factors;
- identifying one cause does not require erasing other contributing conditions.

Ouros transformation:
- `cause_structure` records whether the current investigator understands the incident as unresolved, accident-only, tampering-only, contested, or concurrent;
- actor responsibility remains a separate axis from causal composition.

Not imported:
- maritime procedures;
- vessel facts;
- regulatory conclusions;
- real-world blame assignments.

### Pokémon Stalactite

Source: public project site.
Public URL: https://pokemon-stalactite.fr/

The project presents a region whose geography, climate, regional forms, side quests and mystery are designed as one connected setting rather than independent content islands.

Reusable lesson for Ouros:
- environmental conditions can be persistent contributors to a mystery instead of decorative backdrop;
- a location-specific mystery becomes stronger when the same regional condition affects travel, ecology, infrastructure and local interpretations.

Ouros transformation:
- a relay can have accumulated ice/corrosion/fatigue before a deliberate intervention;
- the environmental contributor remains part of the later repair problem even if sabotage is proven.

Not imported:
- Citados;
- Team Yunaï;
- regional forms;
- characters, plot or locations.

### Pokémon Rollout! — PTU actual play

Sources:
- https://www.podchaser.com/podcasts/pokemon-rollout-238076
- https://moon.fm/itunes/1178659383

The public episode index confirms a long-running Pokémon Tabletop United actual play with continuing investigations, infiltrations and recurring consequences alongside battles.

Reusable lesson:
- PTU campaigns can sustain an investigation across multiple scenes while tactical encounters remain only one part of the arc;
- infiltration or confrontation does not need to be the first or only interpretation of suspicious evidence.

Ouros transformation:
- a failure inquiry can begin as maintenance work, become a contested investigation, and only later expose deliberate intervention;
- the same evidence chain can support social, travel and tactical consequences at different times.

Not imported:
- episode plots;
- player characters;
- dialogue;
- named organizations or locations.

## Design conclusion

Ouros needs two independent axes:

1. Causal composition: unresolved, accident-only, tampering-only, contested, concurrent.
2. Responsibility attribution: unresolved, tampering corroborated, actor linked, intent attributed.

A later `CONTRIBUTION_LINK` claim is required before the runtime can classify accidental and deliberate factors as concurrent. The claim must have an independent provenance root from the evidence families it combines. Repetition of one report cannot bootstrap a combined-cause conclusion.

## PTU / Caelo authority boundary

This pass adds no PTU combat rule, Skill rule, Trainer Feature, species capability, environmental damage formula or forensic procedure. Any future authored clue that depends on a Pokémon capability, Trainer Feature or PTU Skill must be checked against project PTU/Caelo authority before canonization.

## Canon boundary

Everything here remains research provenance. The relay, corrosion, sabotage, investigators and later repair loop are proposal material only. No place, faction, NPC, species behavior or incident is canon-approved by this note.
