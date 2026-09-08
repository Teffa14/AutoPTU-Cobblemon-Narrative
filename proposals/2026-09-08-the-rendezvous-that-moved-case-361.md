# The Rendezvous That Moved — Pass 361

Status: PROPOSED / NON-CANON
Date: 2026-09-08

Premise

A field team has an accepted request for a scarce measuring instrument and an authorized pickup at a repair row. Before the pickup window opens, the intended receiver asks to move the handoff to a field office later in the day. The provider receives the request and accepts it. A successor authorization is created for the new place and time while the original authorization remains in history as superseded.

The world is saved after acceptance but before the new rendezvous occurs.

When play resumes, one support NPC still acts from an older message and travels toward the original repair row. The provider follows the accepted successor window. The intended receiver knows the new arrangement. Nobody needs to be lying or behaving irrationally. They are operating from different versions of a real schedule.

Player-facing investigation

The player can reconstruct the original authorization, the RESCHEDULE_REQUEST notice, its communication event, the proposal, the named responder, the ACCEPT decision, the replacement link and the successor authorization. The old record remains visible as historical authority but cannot execute a current handoff.

This creates several possible consequences without predetermining blame. The player can redirect the misinformed support NPC, notify the provider, preserve the new rendezvous, negotiate another window, or allow the missed meeting to become a downstream allocation problem if another team needs the instrument.

Persistence requirement

A restart must preserve both authorization identities and the replacement lineage. Restore must never rewrite the old authorization into the new one, infer a successor only from current possession or location, or replay the acceptance decision. The successor must match the accepted proposal in participants, resource, mode, location, validity window and decision provenance.

Reduced implementation

The complete premise can run without AutoPTU. It uses semantic time, Pass 342 requests, Pass 343 handoff authorization, Pass 345 appointment/communication provenance, Pass 346 reschedule proposal/decision/replacement history, travel, memory/belief divergence and checkpoint recovery.

A missed old rendezvous can be represented through ordinary world-state and communication consequences. The player can solve it through information and travel rather than combat.

Mechanically rich version

The stale-information NPC may already be crossing a field route when the discrepancy is discovered. The player can attempt to intercept and redirect that NPC before the new pickup window closes. A wild encounter or environmental obstruction can complicate the route, but victory means preserving the rendezvous or safely rerouting the participants. Defeating every opponent is not required by the narrative premise.

Capability dependencies for the rich version

targeting/footprints/range/LoS: VERIFIED only within previously audited ordinary contracts; required if combat or spatial intervention occurs.

base movement legality: VERIFIED within audited ordinary scope; sufficient for simple grid movement.

complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for true tactical interception, forced separation or displacement.

core calculations: VERIFIED within audited deterministic arithmetic scope.

action economy/initiative: VERIFIED for audited primitives; explicit courier/intercept actions still need their own legality contracts.

full turn/round lifecycle: PARTIAL; required if the rendezvous deadline is represented in combat rounds or uses lifecycle-triggered effects.

full stateful damage pipeline: PARTIAL; required if damage outcomes materially affect the route objective.

status lifecycle: PARTIAL; any persistent condition must remain gated by its exact lifecycle support.

terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact family; only include an environmental complication when its selected mechanics have verified contracts.

move-specific behavior: PARTIAL and individually gated.

abilities: PARTIAL and individually gated. Intimidate/Mirror Armor parity from AutoPTU-Java PR #408 is evidence for that exact interaction only.

items: PARTIAL and individually gated.

Trainer Features/perks: PARTIAL and individually gated.

AI legal-action infrastructure: VERIFIED within audited ordinary scope; objective-specific intercept, redirect, pickup and cargo actions still need explicit legality contracts.

AI tactical policy: BLOCKING for intercept-to-inform, rendezvous-first, rerouting, protect-carrier and disengage-after-objective behavior.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for timed rendezvous, cargo/objective semantics and authoritative acknowledgement end-to-end.

Canon questions left open

Which Caelo institution owns or lends the instrument is deliberately unspecified. The proposal does not assume a particular settlement, ranger organization, research guild, laboratory or faction. The social consequence of missing the new rendezvous also remains policy-driven rather than automatic.
