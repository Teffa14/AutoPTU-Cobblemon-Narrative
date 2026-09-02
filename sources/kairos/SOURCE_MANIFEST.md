# Kairos source manifest

Status: RESEARCH / RULES REFERENCE — NOT OUROS CANON BY ITSELF
Last updated: 2026-09-02

This directory registers the Kairos PTU material used as a comparative source for Ouros. Kairos is evidence of how a large PTU living-world community adapted PTU to persistent multiplayer play. Kairos rules, lore, species content and homebrew are not automatically imported into Ouros.

## Public sources

- Wiki: https://kairosptu.wiki.gg
- Public source folder supplied by project owner: https://drive.google.com/drive/folders/1hj-xdwlW1OXXJzZAh0vpKNX5L_5RKdmT

## User-supplied source files

### PTU Kairos Edition V2.1.25.1.pdf

- Supplied filename: `PTU Kairos Edition V2.1.25.1.pdf`
- SHA-256 of the supplied file: `b636541fe7fa76fb50e8bab9d8aac655b2f4b6d9f84f9f3db7eae4df5bd67340`
- Supplied file size: 16,436,548 bytes (local upload snapshot)
- Internal cover/version text observed in the supplied PDF: `Version 2.06.25`.
- Nature: Kairos homebrew PTU core compilation. The document explicitly says it includes PTU Core/Errata material plus Kairos homebrew changes.
- High-value comparison areas: character creation, Skills/Edges/Features, Trainer Classes, Pokemon management, capture, Loyalty, breeding, fishing, mounts, tactical combat, hazards, terrain/weather, injury/death/rest, Contests, League design, encounter design, bosses, items, shops/services and GM guidance.

Version labels must not be silently reconciled. When a rule is cited, record the supplied filename, the internal version text if relevant, and the page/section used.

### Kairos New Player Doc.pdf

- Supplied filename: `Kairos New Player Doc.pdf`
- SHA-256 of the supplied file: `f3072829142c72e10aa50474c65e2c2f85ed9817c714245a09b2865a3c9c58a1`
- Supplied file size: 22,722,065 bytes (local upload snapshot)
- Nature: living-world onboarding/operations document.
- High-value comparison areas: open-ended progression, quest/session structure, downtime, hunting, crafting/training/side work, real estate, prestige/post-cap play, regional exploration and concurrent player stories.

An extracted text snapshot is stored beside this manifest for repository-side search. The PDF remains the visual/source authority for tables, layout and any text extraction ambiguity.

## Source use policy

Kairos is a comparative rules/content source, not a law of Ouros.

For every imported idea, classify it as one of:

- `REFERENCE_ONLY`: useful precedent; no Ouros rule/content change.
- `OUROS_CANDIDATE`: worth adapting; not approved.
- `OUROS_APPROVED_RULE`: explicitly accepted Ouros mechanical rule/overlay.
- `OUROS_APPROVED_CONTENT`: explicitly accepted Ouros world/content fact.
- `REJECTED_FOR_OUROS`: incompatible with Ouros invariants.

Never infer approval merely because a mechanic is mature, popular, already automated by Kairos, or present in a Kairos regional Pokédex.

## Permanent content prohibition gate

The following content may not enter ordinary generation/import pipelines:

- Fakemon.
- Unofficial regional forms.
- Type Syncs, TOSIKI-style species alterations or equivalent unofficial type/form conversions.
- Custom evolutions, custom Mega forms, custom Dynamax/Z-Move/Terastal variants or other species/form gimmicks.
- Species stat, type, Ability, evolution, learnset or identity changes not explicitly approved by Ouros.
- Pokémon fusions.

Exception policy:

- Fakemon or unofficial regional/form content requires exceptional, explicit `OUROS-APPROVED` authorization from the Ouros project itself. Normal proposal approval is insufficient.
- Pokémon fusion content is prohibited by default and requires a separate explicit project-level reversal of the fusion prohibition before any individual fusion can even be proposed.
- Official Pokémon and official forms still require normal Ouros availability/canon decisions for the relevant region or content slice.

## Provenance rule

If Kairos inspires an Ouros mechanic, quest structure, MMO loop or data model, preserve the Kairos source reference in `research/` and restate the resulting Ouros rule in project-native terms. Do not copy Kairos lore, custom species, distinctive NPCs, islands or plots into Ouros as canon.
