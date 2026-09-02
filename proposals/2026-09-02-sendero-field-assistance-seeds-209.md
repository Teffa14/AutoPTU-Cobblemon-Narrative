# Pass 209 Proposal — Sendero field assistance and return-to-wild seeds

Status: PROPOSED / NON-CANON
Date: 2026-09-02
Research provenance: `research/2026-09-02-field-assistance-return-identity-scan-209.md`

## Canon anchors preserved

This proposal reuses Marea Field Office, Sendero del Vidrio, Estación Mirador and the existing Thin Delivery Season world arc. It does not establish a cause for Thin Delivery Season. It creates no new faction and does not modify the approved Fletchling blueprint.

The existing lower-shelf Fletchling may appear only if its current persistent world state places that individual in the scene. The story remains valid if it is absent.

## Seed A — Marker Line Down

Questline types: EXPLORATION / FACTION / SECONDARY.

Premise: a routine Field Office route report notes that one survey-marker line on Sendero no longer gives a reliable sightline after ordinary debris and vegetation shift. The immediate problem is route documentation, not a monster attack or regional crisis.

Player-facing progression:

1. verify the marker and record the obstruction;
2. determine whether the route remains safely usable without intervention;
3. choose among available authored solutions;
4. record what changed and whether follow-up is needed.

Possible solutions remain contracts rather than assumptions. A Trainer may clear a lightweight obstruction through a verified mundane action, use a verified Pokémon capability, request appropriate help, document an alternate sightline or leave the marker unchanged and report the limitation.

World writes are bounded: marker visibility/access state, report provenance and follow-up requirement. Completion never proves anything about Thin Delivery Season.

### Full mechanical version

A richer version can allow an active Pokémon to manipulate a route object while other actors occupy the same tactical space. If unstable footing, collision, reactive protection, forced displacement or timed hazards matter, the encounter requires the corresponding complete engine families rather than Minecraft-side simulation.

Capability requirements:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when displacement or interception participates;
- core calculations when a PTU calculation is required;
- action economy/initiative if resolved inside structured combat time;
- full turn/round lifecycle for multi-round/timed work;
- full stateful damage pipeline if damage can occur;
- status lifecycle if a legal status can occur;
- terrain/weather/hazards/zones/reactions if footing, hazard areas or reactive field rules are mechanical;
- move-specific behavior when a Move supplies the action;
- abilities when an Ability changes legality/effect;
- items when equipment has a mechanical effect;
- Trainer Features/perks when a Feature supplies or modifies the action;
- AI legal-action infrastructure for non-player actors taking legal actions;
- AI tactical policy if autonomous actors must choose among objective-aware actions;
- Minecraft/Cobblemon/Craftics adapter/playback support for physical projection and authoritative result playback.

### Reduced version

Run the entire episode as authored world interaction. Geometry is presentation. The obstruction has explicit interaction choices. Only already verified noncombat/world-service actions may change it. No collision damage, hazard, reaction, forced movement, weather effect or improvised Move effect occurs. The narrative premise and route-state consequence remain intact.

## Seed B — The Patient Leaves First

Questline types: POKEMON / FACTION / SECONDARY.

Premise: a wild Pokémon already represented by a valid persistent identity receives or has recently received bounded field assistance. Once mechanically safe release conditions are verified through the existing care authority, the important scene is the return to ordinary wild agency.

The player may help transport, observe the release site, keep distance, document behavior or leave before the Pokémon departs. The Pokémon can leave without a capture prompt. Later re-sighting uses the same persistent identity only when world persistence says it is the same individual.

This seed intentionally tests a Pokémon-centered payoff that does not end in ownership.

Narrative milestones may include `accepted_transport`, `entered_release_area`, `departed_without_assistance`, `re_sighted_at_known_site` and `returned_to_group_observed`. These are observations/events, not friendship values or mechanical healing.

### Mechanical boundary

Any HP, Injury, status, treatment, item use, Skill, Feature or movement-capability change remains PTU/AutoPTU-owned. The narrative layer may reference the verified result but cannot write healing or readiness by prose.

The reduced version requires no battle. Minecraft needs only persistent actor identity, controlled spawn/projection, bounded observation and world-state writeback.

## Seed C — Help Without Joining

Questline types: POKEMON / EXPLORATION / CLASS.

Premise: during a route task, a wild Pokémon is in a position to perform one useful bounded action. The system may expose cooperation only after authored observable behavior indicates willingness and only if an authoritative action contract exists. The Pokémon assists once and then resumes its own activity.

Examples of abstract task shapes are reaching a marker, carrying a line across a gap, moving a light natural obstruction or signaling from a vantage point. No species or Move is assigned here. Exact actor/action pairing requires later source and mechanics validation.

This seed supports Capture Specialist, Survivalist, Researcher, Rider, Commander or other class identity only through verified permissions. Current class identity can change available approaches without turning the story into a permanent class lock.

### Full mechanical version

If cooperation happens during combat or alongside hostile actors, all relevant movement, reactions, initiative, damage, status, Move, Ability, Feature and AI families must be implemented. Objective-aware autonomous wild behavior specifically needs AI tactical policy.

### Reduced version

Outside battle, the world service validates one bounded action contract. The Pokémon actor performs a presentation animation only after the authoritative world action succeeds. No battle participant/control relationship is created.

## Seed D — Return Visit, Different Meaning

Questline types: POKEMON / EXPLORATION / RELATIONSHIP only if an actual NPC relationship is involved.

A later Sendero visit may show the consequence of Seed A, B or C through persistent state: the marker remains usable, the obstruction returned, a repair was replaced, a previously assisted wild individual is observed elsewhere, or no special callback occurs.

The important rule is asymmetry. Player attention does not guarantee a dramatic reward. A persistent world can remember an intervention without making every intervention the start of a personal bond.

## Proposed runtime boundaries

`FIELD_ASSISTANCE_CASE` owns the practical problem and result.

`CARE_CASE` owns care observations/treatment continuity when applicable.

The Pokémon entity registry owns persistent wild identity.

PTU/AutoPTU owns mechanical legality and battle state.

Minecraft/Cobblemon/Craftics owns presentation, interaction surface and playback, never authoritative battle truth.

Quest/world-state services own authored consequences after consuming bounded authoritative results.

## Live engine evidence on 2026-09-02

Read-only AutoPTU-Java advanced from `496f7e15dbc4bb547449727cd60cd397d8d9005a` to `ee794c04014f87740703bc73d5929c15360e0840` in commit `Freeze forced-movement prevention traces for area and delayed hits (#327)`.

The new evidence adds regression coverage showing forced-movement prevention traces for multi-target/area and matured delayed-hit execution. It is meaningful evidence inside the forced-movement family, especially interaction between delayed/area hits and a Trainer Feature that blocks displacement. It does not prove that complete push/pull/knockback/interception/forced-movement semantics are finished. Therefore the permanent category remains PARTIAL rather than being promoted.

AutoPTU remains at `729bae2d424963ff9bb3f4159c9a7ac9152128a7`; its latest change is presentation-only battle-coordinate synchronization and provides no new gameplay-family authority.

Capability classification for the rich variants:

- targeting/footprints/range/LoS — VERIFIED within audited contracts;
- base movement legality — VERIFIED within audited contracts;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL, with new prevention-trace coverage but no whole-family proof;
- core calculations — VERIFIED within audited contracts;
- action economy/initiative — VERIFIED within audited contracts;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING as a complete family;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL; the new forced-movement prevention trace is representative evidence, not complete Feature coverage;
- AI legal-action infrastructure — VERIFIED within audited contracts;
- AI tactical policy — BLOCKING for autonomous objective-aware cooperation or opposition;
- Minecraft/Cobblemon/Craftics adapter/playback support — PARTIAL/BLOCKING for complete end-to-end rich encounters.

## Questions requiring source/mechanics resolution

Before any capability-based field assistance becomes canon or implementation data, verify which PTU/Caelo/Kairos Skills, Moves, capabilities, Features and equipment can legally perform specific noncombat tasks; whether those actions consume time/frequency/resources; how voluntary wild participation is represented without creating Trainer control; and which authoritative world service owns noncombat legality.

For release/re-sighting, verify the exact persistence/writeback contract after treatment or battle, including HP/Injury/status state, capture outcome, escape/disengagement and whether the Minecraft actor can be safely reprojected from canonical identity after unload/reload.

## Acceptance intent

The slice succeeds when Ouros can tell a small Sendero story where a practical problem, a Pokémon actor and a persistent place interact without forcing combat or capture, while any mechanically meaningful action remains traceable to an authoritative rules contract and every richer tactical dependency stays explicit.
