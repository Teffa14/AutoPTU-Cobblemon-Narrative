# Research scan 289: public information revisions

Status: RESEARCH / PROVENANCE ONLY. Nothing in this file is canon by itself.

## Question

How should Ouros represent a public report that is later updated or corrected without making every NPC instantly share the new version or erasing the historical effect of the earlier version?

## Sources reviewed

Jon Doyle, “A Truth Maintenance System” (MIT AI Laboratory, 1979). Public record: http://hdl.handle.net/1721.1/5733

Reusable design lesson: keep reasons and dependencies for beliefs so later contradictory discoveries can revise current conclusions without deleting the explanation of how the earlier conclusion was reached.

Nathan Walter and Riva Tukachinsky, “A Meta-Analytic Examination of the Continued Influence of Misinformation in the Face of Correction,” Communication Research 47(2), 2020. DOI: https://doi.org/10.1177/0093650219854600

Reusable design lesson: receiving a correction should not be modeled as guaranteed deletion of the earlier information's influence. The implementation therefore records receipt and lineage rather than forcing a universal belief flip.

TV Mauville / Hoenn TV documentation, Bulbapedia: https://bulbapedia.bulbagarden.net/wiki/TV_Mauville

Reusable Pokémon-world structure: broadcasts can be triggered by world events, interviews, achievements, and player actions. Ouros uses only the high-level idea that public media can report changing world state. It does not import programs, reporters, dialogue, locations, or plots.

Pokémon Tabletop community material was searched for campaign uses of rumor/news/investigation. No source found in this pass was strong enough to justify importing a distinct PTU-specific rule or canonical assumption. That negative result is recorded to avoid manufacturing provenance.

## Transformation into Ouros

The source material supports three high-level patterns:

1. Public information has history and provenance.
2. A later correction is a new informational event, not a retroactive deletion.
3. Different receivers can remain on different versions because receipt itself is contingent.

Pass 289 transforms those patterns into a region-neutral revision registry. No protected dialogue, characters, plots, program names, or source-specific mechanics are copied.

## Authority boundary

The resulting code is proposed Ouros simulation infrastructure. It is not a PTU/Caelo/Kairos rule and does not establish any canon medium, broadcaster, city, technology, or faction.
