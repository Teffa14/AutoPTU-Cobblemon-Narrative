# Shared-resource access, permit and stewardship layer

Status: DESIGN / NON-CANON ARCHITECTURE
Date: 2026-09-01

Purpose: define how Ouros can represent conditional access to shared spaces, observation windows, temporary closures, specimen collection, limited extraction and stewardship without duplicating ecology, custody, civic governance or PTU mechanical authority.

## Core boundary

This layer answers a narrow world question: who is currently authorized to do which resource-affecting action, where, why and until when?

It does not decide ecological truth, item ownership, battle legality, capture probability, faction reputation or Minecraft collision.

The main invariants are:

`ACCESS_GRANTED != ALL_ACTIONS_GRANTED`

`MECHANICALLY_CAPABLE != INSTITUTIONALLY_AUTHORIZED`

`OBSERVATION_PERMISSION != EXTRACTION_PERMISSION`

`PERMIT_ITEM_PRESENT != PERMIT_CURRENTLY_VALID`

`CLOSURE_ORDER != PHYSICAL_WALL`

`QUOTA_POLICY != TRUE_POPULATION_COUNT`

`COBBLEMON_ENTITY_PRESENT != RESOURCE_AVAILABLE_FOR_TAKE`

## Reuse existing Ouros systems

Ecological evidence remains owned by phenology, population and observation layers.

Physical samples and removed objects enter existing custody/provenance systems.

Institutional roles and delegation determine who may issue, review or revoke an authorization.

Calendar/event systems own scheduled windows.

Local knowledge and communication systems own who knows about a closure or rule change.

Site aftermath owns physical damage or recovery that may motivate restrictions.

Quest/dispatch layers may ask the player to perform authorized work but do not mint authority themselves.

## Authorization record

A proposed authorization record should contain at minimum:

- stable authorization_id;
- holder_ref;
- issuer_role_ref;
- site_scope or route segment;
- purpose_code;
- allowed verbs;
- prohibited verbs when needed for clarity;
- valid_from and valid_until;
- prerequisites or credential refs;
- supervision requirement;
- reporting obligation;
- transferability state;
- revocation/suspension state;
- source decision or policy ref.

Examples of verbs are ENTER, OBSERVE, PHOTOGRAPH, SAMPLE, HANDLE, REMOVE_SAMPLE, REPAIR, INSTALL_MARKER, ESCORT, OPERATE_EQUIPMENT and CAPTURE_IF_MECHANICALLY_LEGAL. None of these verbs should be globally enabled by this file.

## Site access states

A site can project a public access state derived from current authorizations and closure decisions. Useful proposed states are OPEN, OPEN_WITH_CONDITIONS, OBSERVATION_ONLY, ESCORT_REQUIRED, STAFF_ONLY, TEMPORARILY_CLOSED and EMERGENCY_ACCESS_ONLY.

The public state is a projection for usability. The underlying records remain authoritative so exceptions can exist without rewriting the whole site.

## Closure orders

A closure must identify the scope, issuing role, reason claim/evidence ref, start, review point and termination rule.

A closure may be precautionary while evidence is uncertain. Later evidence can narrow, extend or lift it. Revision history should persist.

A Minecraft barrier, sign or NPC line is presentation. Destroying the sign cannot revoke the closure. Conversely, a closure can remain valid even if no barrier is loaded.

## Observation-only access

Observation-only windows are useful when the world wants player involvement without normalizing capture or extraction. Activities can include repeated counts, photographs, route notes, behavior records, sound logs or equipment checks.

Observation output should feed existing evidence systems and preserve method, effort and uncertainty.

## Specimen and sample collection

Collection requires an explicit allowed verb and scope. A collection record should capture what was taken, quantity/extent if meaningful, source location, time, collector, authorization ref, intended destination and custody handoff.

The collected object should not silently become unrestricted inventory. Research samples, maintenance parts, evidence and public-property removals already have other ownership/custody semantics.

## Quotas and limits

If future canon uses quotas, they should be policies with provenance, review windows and scope rather than magic numbers derived directly from spawn tables.

A policy can be conservative because evidence is weak. A later review can change it. The system should preserve the historical decision and evidence state.

## Customary and institutional access

Future canon may distinguish resident/customary access from visitor permits, but this architecture does not assume such rights exist. If adopted, customary authority needs an explicit source and scope rather than being inferred from residence alone.

`LIVES_NEAR_SITE != MAY_REMOVE_RESOURCE`

## Player-facing loops

Useful non-combat loops include checking current access notices, receiving a scoped work authorization, validating that a permit is still current, performing a field task, logging what was observed or removed, returning samples/equipment, recording completion and seeing the access state change later.

The player may also discover that two records conflict: a field office closure was issued, but a market notice is stale; a permit expired before the weather delay ended; an observation-only instruction was copied as a general opening. These are information/correction problems first.

## Conflict without villainy

Shared-resource disputes can arise because actors bear different costs. A producer may lose access to a shortcut. A researcher may want a longer observation window. Ferry staff may need shoreline space for safety. A resident may rely on a seasonal resource. Mara may prefer a precautionary closure while evidence is incomplete.

The system should record interests, claims and authorized decisions separately. It should not infer bad faith from disagreement.

## Battle handoff boundary

A permit or closure can determine whether a battle should be avoided, delayed or moved. It cannot alter PTU mechanics inside BattleSpec.

If a tactical encounter begins, AutoPTU owns positions, legal actions, initiative, damage, statuses and results. World authority can provide only the pre-battle context and receive narrow outcome events afterward.

A battle victory cannot automatically issue a permit, lift a closure, prove ecological safety or authorize capture.

## Minecraft/Cobblemon projection

Useful visible surfaces include signs, notice boards, tagged gates, check-in desks, temporary ropes/fences, observation markers, sample containers and NPC dialogue.

All are projections. Server-owned world records decide validity.

A Cobblemon spawn inside a restricted area does not imply capture permission. A missing entity does not imply a quota is available.

## Mechanically rich pattern and reduced form

Full pattern: a route closure is challenged during an active wildlife passage while unauthorized entrants are present. The tactical version may need moving non-combat actors, protected corridors, interception, forced movement, terrain/hazard cells, exact move/ability behavior and AI that understands withdrawal/protection goals.

Reduced form: the closure and wildlife movement remain world state outside BattleSpec. The player reports or escorts civilians to a safe boundary through ordinary world movement. Any battle occurs separately on a stable clearing with an audited roster. Its output can only describe the immediate threat outcome, not the validity of the closure or the ecological conclusion.

## Promotion requirements

Before any access rule becomes canon, identify the institution or social authority that creates it, the geographical scope, its relationship to existing resident responsibilities, any Caelo precedent, and whether it affects capture/resource mechanics that require PTU validation.

No file in this design layer creates a protected species, reserve, quota, property regime or enforcement office by itself.