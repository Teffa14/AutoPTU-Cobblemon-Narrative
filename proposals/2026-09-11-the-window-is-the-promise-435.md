# The Window Is the Promise — Pass 435

Status: PROPOSED / NON-CANON
Canon effect: NONE

## Premise

An NPC cannot satisfy an assistance request on the original terms, offers a narrower or later alternative, and the requester accepts it. The resulting promise is specific: one actor agreed to one time window under the proposed terms. That promise does not guarantee travel, access, equipment, success or combat capability.

The narrative value comes from allowing the world to keep moving between agreement and execution.

## Example surface

Mara Veyra and Teo Lark can remain regression actors because the existing project already uses Mara for coordination and Teo for equipment/field-instrument maintenance. This example establishes no new Marea canon.

Example only: Mara asks for immediate assistance with a field problem. Teo cannot leave current work and offers a later diagnostic window at an existing site, limited to inspection. Mara accepts the proposal. Teo now has a scheduled obligation during that exact window.

Before the appointment, several things may change without rewriting the promise: the symptom can disappear, access can close, another person can make a temporary repair, weather can make travel unsafe, or new evidence can show that the requested intervention was based on a wrong diagnosis.

## Story loop

The reusable sequence is:

request -> responder counterproposal -> explicit delivery -> requester acceptance -> durable responder commitment -> current-world reevaluation near the window -> travel/access/resource checks -> appointment or missed/changed outcome.

Each arrow has a distinct owner. This prevents a communication event from pretending that later physical work already happened.

## Reduced encounter version

The appointment can run with world simulation only.

The specialist reaches the decision point with the accepted commitment in their agenda. If ordinary travel and access permit, the visit can produce observation records, a diagnosis, advice, a reschedule or a finding that the original problem changed. If the actor cannot reach the site, the commitment can become missed work through the existing schedule semantics.

A local ecological problem can be solved through evidence and observation rather than battle. This preserves the PTU campaign lesson that Pokémon/environment interactions can create meaningful scenes without every problem becoming a tactical defeat condition.

## Mechanically rich version

The same appointment can uncover a hazardous site. The negotiated scope remains inspection, but changing conditions may create a later choice to withdraw, request help, stabilize an object, escort someone out or enter structured combat.

The accepted scope does not grant those verbs automatically. Each specialized action must be legal under its own owner. If structured mechanics become necessary, the due commitment can request AutoPTU through the existing explicit handoff.

A reduced fallback keeps the same premise by representing the hazard as world-state closure, evidence loss, access denial or forced withdrawal instead of reproducing missing PTU mechanics inside Minecraft.

## Capability dependencies for the full version

Targeting/footprints/range/LoS becomes required if actors or equipment need tactical targeting. Current status: VERIFIED only in audited scopes.

Base movement legality is required for ordinary tactical traversal. Current status: VERIFIED only in audited scopes.

Complete movement including push/pull/knockback/interception/forced movement is required only if the hazard or opponents displace/intercept actors. Current status: PARTIAL.

Core calculations are required for audited standard calculations. Current status: VERIFIED only in audited scopes.

Action economy/initiative is required once the visit becomes a structured encounter. Current status: PARTIAL.

Full turn/round lifecycle is required for round-sensitive environmental change or delayed consequences. Current status: PARTIAL.

Full stateful damage pipeline is required for persistent tactical damage. Current status: PARTIAL.

Status lifecycle is required for timed or persistent conditions. Current status: PARTIAL.

Terrain/weather/hazards/zones/reactions is required if the site changes legality, imposes zones or fires reactions. Current status: MIXED / PARTIAL / BLOCKING by exact behavior.

Move-specific behavior, abilities, items and Trainer Features/perks remain individually gated whenever a scene depends on one of them.

AI legal-action infrastructure requires explicit admission for specialized inspect, brace, protect, retrieve, carry, escort, rescue or extract verbs.

AI tactical policy remains BLOCKING for specialized objective behavior until dedicated policy evidence exists.

Minecraft/Cobblemon/Craftics adapter/playback remains PARTIAL / BLOCKING for authoritative specialized objective state, non-KO completion and recovery of an in-flight structured scene.

## Consequence hooks

A kept narrow appointment may solve only the diagnosis while leaving repair for someone else. A missed window can create a new communication need without inventing betrayal. A requester can learn that accepting a cheap or narrow alternative had a real opportunity cost. A responder can keep the promise exactly and still disappoint someone who assumed a broader scope.

A changed environment can make the correct outcome “do not proceed.” That result should be recorded as later world history rather than retroactively changing what the actors agreed to.

## Faction and relationship use

Institutions can influence availability, permissions or competing obligations, but faction membership must not become shared knowledge or automatic authorization. A supervisor may schedule a specialist; another member still learns about the appointment only through explicit information or a relevant duty owner.

Repeated kept, missed or renegotiated commitments can later feed relationship consequences through the existing social provenance system. Pass 435 does not apply those consequences itself.

## Canon boundary

Everything in this file is proposed. No incident, appointment, failure, hazard, relationship change or schedule described here is established Ouros canon.

## Open design questions

The proposal and negotiated-commitment ledgers still need atomic checkpoint integration.

A later contract should define how accepted `location_ref`, `scope_ref` and `alternative_ref` become validated travel/action inputs without broadening the promise.

The system still needs explicit policy for an appointment that becomes impossible before start because of route closure, injury, emergency or another hard commitment.
