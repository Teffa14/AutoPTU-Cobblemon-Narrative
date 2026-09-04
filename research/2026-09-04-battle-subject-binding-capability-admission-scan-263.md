# Battle subject binding and capability admission scan — Pass 263

Date: 2026-09-04
Status: research/provenance only. Nothing in this file silently promotes canon.

## Repository evidence inspected first

The full Narrative repository tree was inventoried before writing. Relevant canon, design, research, implementation fixtures and regression tests through Pass 262 were cross-searched for handoff, lineage, persistent identity, semantic result, capability, Injury, status, Caelo and Kairos. `CURRENT_FOCUS.md`, the ecological encounter handoff contract, the Pass 258–262 identity/retention contracts, Pass 262 semantic-result ingress contract and readiness snapshot were inspected directly.

AutoPTU-Java and AutoPTU were inspected read-only. AutoPTU-Java remains at `136c8d9a7d124849954748c780b12a0e1faf28e0`; current direct evidence shows internal `AppliedActionResult`/event production and runtime hook composition, including AoE move-special composition. No repository evidence inspected in this pass establishes a stable public AutoPTU→Ouros persistent semantic-result API or a stable Ouros ecological subject identifier carried through battle transport. AutoPTU Python remains the read-only oracle and no current presentation-only change supplies this seam.

## New public sources

### Movebank data model

Source: Movebank, “The Movebank data model” and “Deployment Manager”.

Movebank deliberately separates an individual animal, a tag, a deployment and an event. A tag can be redeployed; a deployment is the bounded period associating a tag with an animal; events are observations made by the tag. Movebank explicitly warns that a tag is not equivalent to an animal and uses deployment periods to avoid attributing pre/post-deployment records to the wrong individual.

Reusable lesson: a transport/session identifier must not become the domain identity of the tracked individual. Ouros can own stable ecological identity while a battle-session binding is temporary and scoped.

### Enterprise Integration Patterns — Correlation Identifier

Source: Gregor Hohpe / Enterprise Integration Patterns, “Correlation Identifier” and “Correlation and Conversations”.

A correlation identifier lets the receiver associate replies with the request/conversation that caused them. The replier can treat the identifier as opaque. Correlation is messaging state, not proof of the business entity’s underlying identity.

Reusable lesson: AutoPTU can return an opaque battle subject reference that correlates with an Ouros-issued binding without learning or exposing the persistent ecological key.

### Pokémon Mystery Dungeon: Rescue Team DX official material

Source: Pokémon official Rescue Team DX site.

The game uses repeated mission requests routed through a persistent hub and sends the player into changing dungeons. The reusable structural lesson is not any protected plot or character: a stable world-facing request/aftermath ledger can coexist with volatile encounter spaces. Ouros can therefore let an ecological subject acquire durable consequences while a particular Minecraft projection or battle instance is temporary.

## CANON-ALIGNED conclusions

- Ouros remains authority for persistent ecological identity and population lineage.
- AutoPTU remains authority for battle rules and battle-derived semantic truth.
- Minecraft/Cobblemon/Craftics remains presentation/transport and cannot invent ecological or PTU identity.
- A counted unresolved source cannot acquire a durable PTU consequence through species, position, visual similarity or Minecraft UUID.
- Population conservation from Pass 258 remains mandatory when a counted source is promoted to persistent identity.

## PROPOSED structure

Introduce a private `BATTLE_SUBJECT_BINDING_V1` issued by Ouros at handoff. The binding maps an opaque, battle-session-scoped `battle_subject_ref` to one stable Ouros subject. AutoPTU only needs the opaque reference plus battle session and rules-profile context. A semantic result returns the same scoped reference; Ouros resolves it through its private binding ledger before applying any result.

The reference is a correlation capability, not the ecological actor ID. It can be retired when the battle session is finalized. A stale reference from another session must fail closed.

For an unresolved counted population source, durable battle aftermath requires either valid Pass 258/259 promotion before handoff or a reduced encounter mode that does not import persistent battle consequences.

## UNCERTAIN / blocked

- The concrete AutoPTU-Java public output API for durable semantic results does not yet appear in inspected live evidence.
- The real AutoPTU↔Ouros/Craftics transport and authentication mechanism remains undefined.
- The production Minecraft/Cobblemon/Craftics versions remain unpinned in the evidence reviewed here.
- No local Caelo source pack was found in the inspected Narrative evidence; no Caelo rule is inferred from that absence.

## FIXTURE-ONLY allowance

Pass 263 may use opaque battle session IDs, battle subject refs and prevalidated result-shaped records exclusively to test binding, replay and capability admission. These fixtures do not claim that Java can emit the record in production and do not create canon Injury/status/state.
