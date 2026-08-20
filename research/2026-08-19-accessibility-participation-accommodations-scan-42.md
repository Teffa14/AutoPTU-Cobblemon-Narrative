# Accessibility, Participation & Accommodation Research — Pass 42

Status: research/provenance only. Not Ouros canon. Not a PTU rules source.
Date: 2026-08-19

## Why this pass exists

The repository already models care, housing, travel, education, sport, soundscapes, communication, public works, workplaces and institutions. It did not yet have a dedicated model for barriers to participation, accommodations, accessible communication, assistive tools or alternative-but-equivalent ways to complete an activity.

This pass treats accessibility as a world-design and product-design concern. It does not infer a diagnosis from behavior, equipment, age, appearance or player settings.

## Sources and reusable lessons

### Minecraft accessibility

Source: https://www.minecraft.net/en-us/accessibility

Minecraft documents an Accessibility menu, menu narration, multiple navigation methods, configurable chat presentation, adjustable audio channels and ore patterns designed to reduce reliance on color alone.

Reusable Ouros lesson:
- prefer platform-supported accessibility features where they already exist;
- world content should expose meaningful information through more than one channel;
- the Minecraft adapter should not duplicate accessibility logic that the host already provides well;
- server-side narrative state must remain independent from a player's personal accessibility settings.

A player enabling narration or captions must not cause the world to label their character as disabled.

### Directional captions and important sounds

Source: https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/104

Microsoft's current accessibility guidance uses Minecraft Java Edition as an example of directional captions for environmental sounds. The caption communicates both the event and broad direction.

Reusable Ouros lesson:
- any sound that conveys required gameplay information needs an alternate channel;
- the soundscape layer can emit semantic sound events that a client may render as audio, captions, icons or directional indicators;
- a puzzle should not require hearing alone unless an equivalent representation is available.

### Text, contrast and navigation

Sources:
- https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101
- https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102
- https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112

Reusable Ouros lesson:
- important text should support scaling and reflow;
- maps should have a text/list alternative for points of interest;
- critical state should not be encoded by color alone;
- UI navigation should remain consistent after text/UI scaling;
- quest journals, maps, research records and institution menus should expose semantic labels rather than rely on decorative images.

### Multiplayer communication

Sources:
- https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/120
- https://gameaccessibilityguidelines.com/provide-visual-means-of-communicating-in-multiplayer/
- https://www.sciencedirect.com/science/article/pii/S1875952123000472

Reusable Ouros lesson:
- important multiplayer coordination should have text/visual alternatives to voice;
- pings, map markers, emotes and structured intent signals can improve participation for many players, not only players with a declared disability;
- accessibility settings can be individualized rather than forcing one global server mode.

### Fangame examples

Source: https://eeveeexpo.com/fairies/

Pokémon Fairies published a separate colorblind mode, changed puzzle colors, added fast-forward and revised a box puzzle to prevent softlocking.

Reusable Ouros lesson:
- puzzle accessibility belongs in the design itself, not only in documentation after release;
- redundant symbol/shape channels are preferable to recoloring alone;
- recovery/reset paths are both accessibility and general robustness features.

Source: https://www.eeveeexpo.com/resources/1244/

Eevee Expo's game-FAQ guidance notes that repeated player questions about where to go or how to pass an obstacle may indicate unclear communication rather than player failure.

Reusable Ouros lesson:
- repeated confusion is telemetry about content clarity;
- hinting, objective reminders, landmarks and stronger state communication should be improved when many players fail at the same communication boundary.

### Pokémon and braille

Source: https://www.pokemon.com/us/pokemon-news/pokemon-firered-version-and-pokemon-leafgreen-version-braille-chart

The official Pokémon site published a Braille chart in February 2026 for FireRed/LeafGreen progression puzzles.

Reusable Ouros lesson:
- a real accessibility system can exist inside fiction or puzzles without the implementation itself being accessible;
- Ouros should not treat Braille, sign languages, mobility aids or other accessibility practices as exotic puzzle props by default;
- if a symbolic system is required for progression, equivalent presentation must exist for players who cannot perceive the original channel.

### Representation inside Pokémon fiction

Source: https://bulbapedia.bulbagarden.net/wiki/Gibeon

Pokémon Horizons depicts Gibeon using a motorized wheelchair because of severe mobility limitations.

Reusable Ouros lesson:
- mobility aids can exist as ordinary world objects used by major characters;
- use of an aid does not define a character's role, morality, competence or social importance;
- do not copy Gibeon, his device, condition or plot.

### Player-reported Pokémon accessibility barriers

Sources:
- https://community.pokemon.com/en-us/discussion/47/visibility-accessibility-features-requested
- https://community.pokemon.com/en-us/discussion/1689/ipad-version-accessibility-issues-for-disabled-players

These public reports describe barriers caused by tiny text, low readability and input/device constraints.

Reusable Ouros lesson:
- accessibility problems often come from interface assumptions rather than the game concept itself;
- text size, device layout and input flexibility should be treated as implementation requirements, not narrative difficulty.

### General game-accessibility guidance

Sources:
- https://gameaccessibilityguidelines.com/full-list/
- https://arxiv.org/abs/2301.08031
- https://arxiv.org/abs/2509.02132

Reusable Ouros lesson:
- avoid conveying required information through only sound, only color or only precise timing;
- remapping, adjustable timing and alternate input can preserve agency;
- shared-control/co-pilot patterns can help when a control action is inaccessible, but support should not silently take decision-making away from the player.

## PTU / Caelo boundary

The supplied PTU/Caelo corpus was not directly text-retrievable in this runtime, so this pass does not assert any new PTU/Caelo accommodation rule.

The governing boundary remains:
- movement capability comes from authoritative PTU/Caelo/character state;
- Blinded, Slowed, Injuries and other mechanical states remain mechanics, not narrative diagnoses;
- Skills, Edges, Features, Trainer Classes and Pokémon capabilities are not granted by an accommodation record;
- an assistive device does not gain a combat effect unless an authoritative item/rule explicitly provides it;
- an alternate route does not grant Fly, Swim, Phasing, Jump or other traversal capability;
- a UI accessibility option never changes a character sheet.

Current AutoPTU/Python evidence includes authoritative movement modes and combat statuses, but that evidence cannot be reinterpreted as an overworld disability system.

## High-level design directions

1. Model barriers at the interaction/location/event level instead of attaching a universal `disabled=true` gameplay flag to characters.
2. Store self-described access preferences separately from medical/care records.
3. Let institutions publish access information before a player arrives.
4. Let routes, venues and buildings have access variants and temporary outages.
5. Give puzzles multiple equivalent information channels.
6. Allow multiplayer coordination through voice-independent signals.
7. Keep competitive accommodations explicit and transparent without assuming they provide an advantage.
8. Preserve player privacy: personal settings and access needs are private unless the player chooses to share them.
9. Never turn an NPC's disability into a compulsory inspirational, cure or tragedy arc.
10. Make support ordinary: ramps, lifts, captions, seating, quiet spaces, readable signage, rest points, alternative formats and assistance can exist without generating quests.

## Copyright / transformation note

No prose, characters, puzzle solutions or plots from the cited works should be transplanted into Ouros. Sources are retained for provenance. The design layer should convert these findings into original data structures, institutional practices and encounter constraints.