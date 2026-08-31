# Engine readiness snapshot — Pass 169

Status: EVIDENCE SNAPSHOT / NON-CANON
Date: 2026-08-31

## Read-only heads inspected

AutoPTU-Java main: `45f37bbec69881825aba7cbfd6df895de5943096`.
Head message: `Compose forced movement prevention from status and temporary state (#309)`.

AutoPTU main: `729bae2d424963ff9bb3f4159c9a7ac9152128a7`.
Head remains presentation-only: renderer coordinates stay synchronized after viewport resize; the commit explicitly states that battle rules and outcomes do not change.

Neither engine repository was modified by this pass.

## Java evidence

No newer AutoPTU-Java commit exists than the evidence already inspected for Pass 168. PR #309 remains the live head. Its forced-movement work composes prevention from status and temporary state, freezes corresponding Python-oracle branches, compares results to the oracle, adds tests, and gates parity in CI.

This is material implementation evidence for selected forced-movement prevention paths. It does not establish complete coverage of Push, Pull, Knockback, every Intercept ordering, arbitrary forced movement, all terrain/weather displacement, Item/Feature sources, escort/rescue, protected-object carrying, crowd routing, vehicles/platforms, generalized reaction windows, or tactical objective policy.

No permanent category is promoted.

## Permanent capability map

VERIFIED
- targeting/footprints/range/LoS
- base movement legality
- core calculations
- action economy/initiative
- AI legal-action infrastructure

PARTIAL
- complete movement including push/pull/knockback/interception/forced movement
- full turn/round lifecycle
- full stateful damage pipeline
- status lifecycle
- move-specific behavior
- abilities
- items
- Trainer Features/perks

BLOCKING
- terrain/weather/hazards/zones/reactions
- AI tactical policy
- Minecraft/Cobblemon/Craftics adapter/playback support

## Pass 169 encounter dependency review

Inscription Chamber Under Threat full version: BLOCKED if tactical space is coupled to decipherment. It depends on complete movement where displacement/Intercept changes access; full lifecycle for multi-round puzzle state; terrain/weather/hazards/zones/reactions for active mechanisms; individually audited move-specific behavior, abilities, items, statuses, and Trainer Features; AI tactical policy; semantic adapter/playback. Reduced version is READY at narrative-contract level after individual combat-content audit because linguistic work remains outside BattleSpec.

Interpreter Withdrawal Through Ruins full version: BLOCKED by escort/protection semantics inside complete movement, lifecycle, possible hazards/reactions, AI tactical policy, and semantic playback. Reduced version removes the interpreter and records from BattleSpec before initiative and lets AutoPTU resolve only the conventional conflict controlling immediate route access.

Fragment Recovery Perimeter full version: BLOCKED by protected-object carrying, complete movement interactions, lifecycle, possible terrain/hazards/reactions, tactical objective policy, and adapter/playback. Reduced version keeps the fragment static outside BattleSpec and permits only immediate approach clearance.

Wayfinding Inscription Junction full version: BLOCKED when route interpretation changes tactical geometry or timing. It depends on complete movement, lifecycle, terrain/hazards/zones/reactions where applicable, tactical policy, and semantic playback. Reduced version resolves interpretation in Narrative and sends only a subsequent ordinary encounter to AutoPTU.

## Linguistic mechanics boundary

Public PTU material confirms General Education and Occult Education as Skills and confirms Telepathy as a concrete mechanical capability/Feature surface. The public material inspected for this pass did not establish a universal language-proficiency subsystem, automatic literacy, generic translation check, automatic ancient-script reading, universal Unown decipherment, or translator device rule.

UNKNOWN pending project-source verification:
- Caelo-specific languages, dialects, literacy, or translation rules;
- General Education uses that explicitly grant language fluency or decipherment;
- Occult Education uses that explicitly read runes/Unown/ancient scripts;
- Telepathy behavior across languages or for nonverbal concepts;
- Runemaster, Researcher, Chronicler, Sage, or other Feature interactions with inscriptions;
- Pokédex/device translation capabilities;
- Pokémon-human speech rules beyond explicitly supported Capabilities;
- Items or Features that reveal hidden/encoded text;
- mechanical consequences for solving a linguistic puzzle during combat.

A public Unown-themed universal-writing comprehension effect found during research is explicitly homebrew and therefore excluded from PTU/Caelo authority.

## Adapter boundary

Minecraft signs, books, subtitles, chat bubbles, command text, localization strings, resource-pack fonts, generated glyph textures, Cobblemon UI text, or client locale cannot create canonical source text, language identity, translation, or decipherment. Ouros must author the underlying linguistic record; the adapter may render it.

Likewise, AutoPTU battle outcomes cannot validate a translation. A victory can clear immediate access to an inscription or route. Narrative/Chronicle records what is subsequently observed and which reading is proposed.

## Promotion rule

A permanent capability category changes only when live tests/contracts demonstrate that family broadly enough to justify promotion. A single Move, Ability, state-prevention branch, linguistic puzzle, translator Feature, or presentation behavior remains representative evidence only.