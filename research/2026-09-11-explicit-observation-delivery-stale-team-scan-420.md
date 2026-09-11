# Explicit observation delivery and stale-team scan — Pass 420

Status: RESEARCH / PROVENANCE ONLY. Nothing in this note is canon.

## Repository-first deduplication

The recursive main-branch tree at `d2a27beb27bd11e1ad0133f21bba33424e3dd11a` was inventoried before writing. Current focus, canon governance, the Pass 418–419 consequence/observation chain, existing private information delivery, knowledge ledgers, disclosure access tests, recent research/proposals and PTU/Caelo/Kairos routing evidence were reviewed.

Previously processed anchors including Pokémon Memories, The Case of the Golden Idol, Pokémon Starwish, Pokémon Unchosen, Outer Wilds, Pokémon Shadowside, Pokémon Hollow Woods, Pokémon Lithic Veil, Lethalmon, Pokémon Knowledge, Pokémon Crystal Inheritance, Pokémon Rollout!, Pokémon Diadem, Pokémon Burning Scales and The Roaring Trainers were excluded.

Repository search found no prior use of `Pokémon Space Pog Jam` under that title and no prior use of the Antura `Discover Quest Design` documentation.

## New source: Pokémon Space Pog Jam

Public source: BoogerFace itch.io page: https://boog3rface.itch.io/space-pog-jam

The public description frames the player as part of an exploration crew investigating anomalies. A cave entrance collapses, turning the expedition into an escape problem while exploration and discovery continue.

Reusable structure for Ouros:

An expedition can create urgent information that matters to people who are not physically present. The interesting consequence is not limited to whether the trapped team escapes. A warning about route condition, collapse risk or an alternate exit becomes useful only if another actor receives it in time.

Ouros does not import the moon setting, cave layout, anomalies, secrets, specific Pokémon, escape sequence or plot.

## New source: Antura Discover Quest Design

Public developer documentation: https://antura.org/en/dev/quest-design/

The documentation separates quest content, script logic and scene implementation. It also describes Knowledge Cards as explicit content units collected during a quest rather than treating all scene state as automatically known.

Reusable structure for Ouros:

Keep world fact, recorded knowledge and presentation separate. A scene can visually represent a condition, one actor can possess a recorded observation about it and another actor can remain uninformed until a delivery event occurs. The quest layer should consume explicit knowledge state rather than infer universal awareness from shared scene or institutional context.

Ouros does not import Antura's educational content, Unity/Yarn architecture, specific activities, cards, locations or scripts.

## Derived Ouros direction

A first field team returns or reports after learning that a route, chamber, crossing or work site is unsafe or only partly usable. The report reaches an explicit custodian. A second team may already be preparing to depart.

The second team does not gain the warning because both teams serve the same institution. It gains the warning only when a concrete message arrives through a concrete channel.

This creates several legitimate world states:

- the observation exists but no custodian has received it yet;
- the custodian has the record while the field team remains stale;
- a delivery is queued but not due;
- a delivery fails because the channel is unavailable;
- a local-projection channel waits for acknowledgement;
- one named recipient receives the warning while another member does not;
- the recipient receives the warning and selectively replans before departure.

The same structure also supports non-emergency information such as partial survey results, evidence location, changed access conditions or a resource cache state.

## Reduced narrative version

The reduced version requires persistent observations, private knowledge, semantic time, communications, schedules, obligations, travel, permissions and event-driven replanning.

No AutoPTU battle is required. The dramatic question can be whether a named team departs with stale information or waits long enough to receive the warning.

## Rich encounter version

A rich version can place the original observation inside an evacuation, protection or extraction scene. The warning itself remains an ordinary world-information event after the tactical result is admitted.

Exact capability dependencies remain visible:

- targeting/footprints/range/LoS: VERIFIED only in audited scopes;
- base movement legality: VERIFIED only in audited scopes;
- complete movement including push/pull/knockback/interception/forced movement: PARTIAL, required for dragging, interception, forced reposition or collapse displacement;
- core calculations: VERIFIED only in audited scopes;
- action economy/initiative: PARTIAL;
- full turn/round lifecycle: PARTIAL, required for timed collapse phases or evacuation windows;
- full stateful damage pipeline: PARTIAL, required when tactical harm must persist after resolution;
- status lifecycle: PARTIAL;
- terrain/weather/hazards/zones/reactions: MIXED/PARTIAL/BLOCKING, required for unstable ground, falling debris, flooding, visibility changes or reactive danger zones;
- move-specific behavior: individually gated;
- abilities: PARTIAL and individually gated;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: VERIFIED only for audited ordinary scopes; rescue, escort, brace, interact and extract need explicit admission if tactical;
- AI tactical policy: BLOCKING for rescue-first, warning-aware withdrawal, protect-observer and objective-aware disengagement;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for authoritative tactical objective state, environmental hazard state, non-KO completion and in-flight battle recovery.

## Live engine evidence

AutoPTU-Java main inspected read-only at `494430a5e602652e21cf90dc3ae6f3e8ffef2cf6`, merge PR #441, `Freeze replacement initiative insertion oracle`, committed September 11, 2026 UTC. The oracle strengthens one replacement-initiative seam. It does not verify the complete action-economy/initiative family.

AutoPTU Python main inspected read-only at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`. Its newest change remains explicitly presentation-only viewport-coordinate synchronization and does not change battle rules or outcomes.

## PTU / Caelo / Kairos cross-check

The internal PTU/Kairos source index remains a locator for combat, movement/terrain, status, hazards/weather, encounter construction, Items, Abilities and Trainer Features. This pass does not promote any mechanic merely because a source category exists.

Observation delivery is an Ouros persistent-world information concern. If a future scene invokes tactical collapse, forced movement, reaction windows, weather or Trainer Feature interrupts, that scene remains gated on the exact audited capability family.