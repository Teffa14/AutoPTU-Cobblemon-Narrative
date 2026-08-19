# Pass 27 — Language, translation & symbolic-system seeds

Status: NON-CANON. Original Ouros candidates derived from high-level research patterns.

## 1. The Same Word, Three Maps

Three route maps from different decades use the same old place-name for visibly different locations. The quest is not to choose which map is "wrong" immediately, but to discover whether the name migrated, the settlement moved, or the copies were mislabeled.

## 2. The Missing Reading Direction

A ruin inscription has already been transcribed correctly, but every published translation assumes left-to-right reading. A repeated symbol sequence at another site suggests the orientation may be wrong.

## 3. The Tourist Translation

A famous public plaque offers a confident translation of a local inscription. Researchers later discover that the plaque simplified several uncertain lines for visitors. Correcting it becomes a public-memory question, not merely an academic one.

## 4. Two Honest Translators

Two respected scholars produce incompatible readings because one treats a glyph as a number and the other as a title marker. Neither is dishonest. Players need new evidence rather than a social skill check to declare a winner.

## 5. The Bilingual Workshop Ledger

An abandoned workshop contains repetitive inventory marks beside modern annotations from a later occupant. Those parallels help decode practical terms such as material, amount and destination before any ceremonial or historical passages become readable.

## 6. The Song That Keeps the Grammar

A regional children's song has changed words across generations but retains a strange repeated structure. The structure turns out to preserve the ordering convention needed to understand a set of old wayfinding markers.

## 7. Unown Resemblance Dispute

Researchers find a script whose symbols resemble several Unown forms. One institution argues for direct historical connection; another argues that both derive from a third symbolic tradition. Ouros does not resolve the issue until evidence exists.

## 8. The Broken Numeral System

A dungeon puzzle looks like a substitution cipher but only begins to make sense when players realize a subset of glyphs are numerals. Partial decoding opens utility rooms while the main chamber remains inaccessible.

## 9. The False Friend

A modern word resembles an ancient one but has changed meaning. An early translation sends expeditions searching for a "crown" when the contextual meaning may have been "summit" or "highest place."

## 10. The Copyist Error

Three historical copies of an inscription disagree at one glyph. The original is damaged exactly at that point. The difference has propagated into maps, museum labels and one faction's historical claim.

## 11. Archive of Alternative Readings

A library deliberately preserves superseded translations instead of replacing them. Players can trace how interpretation changed as new sites were discovered.

## 12. The Interpreter Is Missing

A remote community can communicate with visitors, but one technical ritual vocabulary is understood by only a few elders and specialists. The resulting quest centers on documenting context responsibly before knowledge is lost, not on treating the community as a puzzle box.

## 13. The Mechanical Phrasebook

Old maintenance panels repeat a limited command vocabulary. Players can safely learn OPEN, STOP, RESET and DRAIN from context without understanding the civilization's broader language.

## 14. The Incorrect Password

A translated phrase appears to be a door password, but the door is actually responding to the sequence of symbols rather than their meaning. This distinguishes decipherment from mechanism behavior.

## 15. The Stone That Changes Context

A portable tablet discovered far from its original location makes an inscription appear religious. Provenance research later suggests it was moved from a civic building, changing the interpretation without changing the literal translation.

## 16. The Translator's Reputation

A scholar with a poor public reputation produces a translation that is technically strong. Players must decide whether to publish, independently replicate or seek additional review while media systems track the controversy separately from truth.

## 17. The Field Notebook Cipher

A missing researcher's notes use a personal shorthand rather than an ancient language. Decoding it can recover route observations, but the shorthand also contains private material that should not automatically become public record.

## 18. Signs for Pokémon, Not Humans

Repeated visual markers along an old route seem linguistic until behavior observations show certain Pokémon responding to them spatially. Whether they are commands, landmarks, learned associations or coincidence remains open.

## 19. The Incomplete Emergency Signage

A crisis damages several markers in an old tunnel network. Modern responders must combine surviving symbols, route knowledge and physical evidence to identify which passages were originally evacuation routes.

## 20. The Translation That Starts a Dispute

A newly translated inscription appears to support one settlement's claim over a historical site. The design forces separation between literal reading, historical context, modern law and political use of the text.

## 21. Living Dialect Survey

Researchers discover that nearby villages use different names for the same seasonal Pokémon behavior. The variation helps reveal migration history but should not be ranked as "correct" versus "corrupt" speech.

## 22. The Resettable Observatory

A ruined observatory contains a symbolic control panel. Incorrect input resets the mechanism rather than destroying it, allowing players to experiment and refine a model through feedback.

## 23. The Fragment Exchange

Two museums each possess half of what was once one inscription, but neither institution realized the connection because the fragments were catalogued under different periods. Cooperation creates a new decipherment opportunity.

## 24. The Public Cipher Craze

A newspaper publishes a harmless fragment of an undeciphered script and the region starts submitting amateur solutions. Most are noise, but a few independent pattern observations are useful. The science layer records contribution provenance.

## 25. The Deliberate Ambiguity

A legal or ceremonial text may have been written to allow multiple readings. The correct resolution is not necessarily to eliminate ambiguity; players may need to understand why ambiguity itself mattered.

## 26. The Unreadable Warning

Players encounter a warning inscription before anyone can translate it. Environmental evidence gives them reasons for caution without relying on a magically convenient translation.

## 27. The Parallel Ruins Arc

Long arc: several sites share fragments of one symbolic system. Early sessions establish repeated forms and numbers; middle expeditions reveal regional variants and a bilingual parallel; later findings force revision of the first accepted historical model. The climax is an interpretive choice with world consequences, not necessarily a boss battle.

## 28. The Lost Standard Arc

Long arc: infrastructure across several old settlements uses inconsistent symbols because a once-central standard fragmented into local conventions. Restoring old systems requires understanding those differences, while modern institutions debate whether to standardize again or preserve local practice.

## 29. The Living Language Arc

Long arc: players initially treat an unusual vocabulary as an archaeological subject, then discover that descendants of the speech community still use related forms. The campaign shifts from decoding dead artifacts to collaborating with living people and revising earlier assumptions.

## 30. The Cipher Race Arc

Long arc: multiple factions hold different pieces of an old technical notation system. No faction has the whole solution. Espionage, publication, exchange, misinformation and independent discovery change who can understand which mechanisms. Mechanical battle objectives use reduced encounter versions until interception/objective-aware AI and adapter support exist.

## Encounter implementation notes

The symbolic-system layer does not require new PTU combat mechanics by itself. When a seed puts interpretation inside a tactical battle, use the permanent capability categories in `design/encounter-implementation-contracts.md`.

Current safe design assumption:

- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement including push/pull/knockback/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: BLOCKING
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Therefore translation, investigation and puzzle manipulation should remain overworld/world-state actions unless an exact tactical dependency is already verified.