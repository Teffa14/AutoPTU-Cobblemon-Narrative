# The Transfer Before the Restart — Pass 355

Status: PROPOSED / NON-CANON
Date: 2026-09-08
Research provenance: `research/2026-09-08-handoff-custody-restart-provenance-scan-355.md`
Design dependency: `design/global-npc-resource-handoff-checkpoint-contract-pass-355.md`

## Premise

A field team requests a specific measurement instrument from a shared facility. The provider accepts the request, authorizes a pickup and physically transfers the exact unit to a courier.

The world then advances through unrelated play and a server restart.

Later, another actor asks who currently has the instrument and whether the first team was actually authorized to take it.

The useful story problem is historical reconstruction rather than a scripted accusation.

## Persisted facts

The world may retain all of these independently:

- the original request;
- the provider acceptance;
- the handoff authorization;
- the permitted receiver, place and time window;
- the completed custody transfer;
- the condition recorded at transfer;
- the current resource holder and location through the resource owner;
- later memories and communications about the event.

A restart does not need a recap dialogue to recreate those facts.

## Possible investigation

The player may compare the authorization against the request, confirm that the exact unit matched the accepted offer, verify that the transfer happened inside the authorized window and inspect later custody evidence.

If the save predates Pass 355 and contains no durable handoff ledger, the game should represent the missing provenance rather than infer a transfer merely because somebody now holds the object.

That difference can matter. A person can possess an object legitimately while the surviving records are incomplete. A complete record can also show that a later memory of the handoff is wrong without declaring the speaker deceptive.

## Consequence branches

A clean chain can settle the question and allow the current work to continue.

A missing transfer record can trigger a limited audit, request for corroborating communication, or temporary caution before the next handoff.

A mismatch between current possession and durable history can become a separate investigation. Pass 355 does not decide theft, negligence or dishonesty from the mismatch alone.

Repeated record gaps could later justify procedural reform, training or better checkpoint integration. Those consequences should emerge from accumulated evidence rather than a global misconduct score.

## Reduced playable version

The reduced version needs no AutoPTU battle.

It uses persistent semantic time, Pass 342 resource requests, Pass 343 handoff authorization/custody, Pass 355 persistence, memory/belief, communication and ordinary world travel.

The core player action is reconstructing the sequence and deciding what further evidence or operational step is justified.

## Mechanically rich version

After a valid pickup, the courier must reach a field site before an observation window closes. A wild encounter or rival objective may interrupt the route.

The intended success condition is preservation and delivery of the instrument, not necessarily elimination of every opposing combatant.

Capability dependencies:

- targeting/footprints/range/LoS: required for tactical interaction and combat targeting; currently VERIFIED only within audited ordinary scopes;
- base movement legality: required for ordinary tactical positioning; VERIFIED within audited scope;
- complete movement including interception/forced movement: required if enemies can block, intercept, push, pull or displace the carrier; PARTIAL;
- core calculations: required for ordinary deterministic combat arithmetic; VERIFIED within audited scope;
- action economy/initiative: ordinary primitives VERIFIED, but explicit pickup/drop/handoff actions need their own legal contract;
- full turn/round lifecycle: required for round-bounded delivery deadlines or interrupts; PARTIAL;
- full stateful damage pipeline: required if carrier or cargo damage has tactical consequences; PARTIAL;
- status lifecycle: required for persistent conditions; PARTIAL;
- terrain/weather/hazards/zones/reactions: required only when the encounter uses them; MIXED/PARTIAL/BLOCKING by exact family;
- move-specific behavior: individually gated;
- abilities: individually gated and PARTIAL as a family;
- items: individually gated;
- Trainer Features/perks: individually gated;
- AI legal-action infrastructure: ordinary audited infrastructure VERIFIED, new cargo actions need definitions;
- AI tactical policy: BLOCKING for delivery-first, protect-carrier, intercept-to-stop and disengage-after-objective behavior;
- Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for end-to-end cargo/objective presentation.

## Fallback implementation

If tactical cargo semantics remain unavailable, the same premise runs through semantic travel and a basic encounter whose outcome only determines delay or route availability. Custody remains owned by the world resource system before and after the battle handoff. Minecraft does not invent missing PTU cargo rules.

## Canon boundary

No named NPC, faction, location or regional event in this proposal is canonized by Pass 355. Existing Marea/Puerto Bruma actors may be used later as regression bindings, but the global contract must remain region-neutral.
