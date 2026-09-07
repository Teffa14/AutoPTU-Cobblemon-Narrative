# The Doorway Listener — Pass 337

Status: PROPOSED / NON-CANON
Date: 2026-09-07

## Canon anchors reused

This case is designed for already established Marea Interior continuity rather than a new region.

Canon anchors available from the resident/map network include Puerto Bruma, Marea Field Office, Tideglass Archive and the persistent residents Mara Veyra, Pia Min and Taro Min with their existing institutional/archive responsibilities.

The incident, document, route issue, privacy expectation and all consequences below are new candidates. None becomes canon by existing in this file.

## Premise

Mara is discussing a provisional field-service change with Pia at the Field Office. The first part of the conversation is ordinary operational information: one scheduled visit may need to move to a later window.

Taro arrives with a dated archive reference that may explain why the alternate route on an old map should not be treated as current. He is a ratified participant for that discussion.

A fourth actor pauses in the doorway while waiting for another service matter. This actor hears one useful fragment: the old alternate route name and the fact that a team may change its schedule.

The doorway listener leaves before Mara states the correction: the alternate route is not yet approved for use and the schedule change is still provisional.

Later, the listener sincerely tells another resident that the field team is moving to the old route.

Nobody needs to lie.

## Why the case matters

The mystery is small enough to happen during ordinary life but tests several persistent systems at once:

- addressee versus side participant;
- partial overhearing;
- correction history;
- subjective source attribution;
- relay sincerity;
- provisional versus approved operational state;
- public versus participant-scoped information;
- NPC memory of what was actually heard;
- consequence repair after a rumor changes someone's plan.

The player can solve the practical problem without discovering a villain.

## Initial state

Proposed state only:

`conversation_A` occurs at Marea Field Office.

Turn 1:

Mara addresses Pia. Taro is not yet present. General schedule uncertainty is discussed.

Turn 2:

Taro joins as a ratified side participant and supplies an archive reference concerning an old route label.

Turn 3:

A waiting resident reaches the doorway. The actor is not invited into the conversation. They receive only a fragment containing the old route label and schedule-change context.

Turn 4:

The doorway listener leaves.

Turn 5:

Mara clarifies that the old route is not an approved destination and that no final schedule decision has been made.

Mara, Pia and Taro ground the corrected operational proposition. The departed listener does not.

## The later relay

The listener later reports, sincerely:

A field team is moving to the old route.

The exact spoken wording is generated from the listener's own memory/belief state. The simulation record retains that the listener heard a partial earlier turn and missed the correction.

The listener is a historical relay source for the later statement. Mara remains the historical source of only the propositions Mara actually uttered. The system must not rewrite the listener's summary as a direct quote from Mara.

## Player investigation paths

The player may encounter a resident who changed plans after hearing the relay. From there, several narrow questions become useful:

What exactly was heard?

Who was addressed?

Was the listener part of the conversation?

When did the listener leave?

Was there a later correction?

Was the schedule ever finalized?

Did the old archive route label refer to a current operational route at all?

Each answer updates a separate evidence or belief state. No universal `CASE_SOLVED` clue is necessary.

## Possible resolutions

One resolution is purely communicative. The listener receives the corrected information, acknowledges the mismatch and can choose to contact actors to whom they relayed the earlier version.

Another resolution leaves some propagation unresolved. The listener remembers telling two people but one further relay has unknown reach. The world may retain a small rumor tail after the immediate operational problem is fixed.

A third resolution reveals that another resident independently drew the same wrong conclusion from a posted map or schedule. Correcting the doorway relay therefore does not erase every instance of the belief.

None of these branches changes canon unless reviewed.

## Consequences worth persisting

Possible non-canon consequences include:

- Mara changes how provisional route discussions are labeled;
- Pia separates confirmed and provisional dispatch notes more visibly;
- Taro adds a current-status note beside an old route label when a document is requested for operations;
- the doorway listener becomes more likely to mark future relays as uncertain;
- one resident retains the old belief until contacted or until contrary evidence reaches them;
- a later conversation references this incident when deciding whether a shorthand route name is safe to use.

These are candidate consequences, not automatic personality changes or permanent canon facts.

## Reduced implementation

The reduced version is preferred now.

Required world-agent state:

- persistent NPC identities and current location/schedule state;
- semantic conversation turns;
- explicit audience frames;
- per-listener partial reception;
- source attribution;
- Pass 335 belief-aware dialogue projection;
- Pass 336 grounding/repair;
- Pass 337 disclosure/overhearing contract;
- relay event history;
- selective replanning if a resident changed an ordinary task because of the rumor.

No battle is required. No hearing radius is required. The doorway reception can be an authored semantic world event with exactly the fragment received.

The case remains useful if every line is rendered through deterministic dialogue templates.

## Optional rich version

A richer version may connect the rumor to an already legitimate field-service or route event. Someone who believes the old route is active may travel toward the wrong staging point and encounter an ordinary world hazard or Pokémon encounter already generated from that location's real state.

The misunderstanding itself must not manufacture the encounter.

If the player reaches the actor during a tactical scene, the objective might include warning the actor, protecting them while they withdraw, or ending escalation after the route misunderstanding is corrected.

## Capability dependencies for the rich version

Targeting / footprints / range / LoS: required only for an actual tactical encounter; ordinary audited use is currently the safe case. Do not convert conversational hearing into tactical LoS automatically.

Base movement legality: required for ordinary tactical movement if battle occurs.

Complete movement: required if the scene needs interception, forced displacement, escort movement or rescue positioning.

Core calculations: required for ordinary battle math only.

Action economy / initiative: required for ordinary battle. If delivering a warning becomes a tactical action, that exact action needs an authoritative contract.

Full turn / round lifecycle: required if a correction arrives mid-round or changes an objective at a precise phase.

Full stateful damage pipeline: required for complete battle consequences.

Status lifecycle: required only for actual selected PTU statuses. Misunderstanding and rumor are not statuses.

Terrain / weather / hazards / zones / reactions: required only for the exact environmental complexity selected.

Move-specific behavior, Abilities, Items, Trainer Features/perks: every selected mechanic remains individually gated. No content grants perfect hearing, private-message access, truth detection or instant common ground from flavor.

AI legal-action infrastructure: ordinary audited legal-action generation can support a static fight.

AI tactical policy: required for warning, escort, withdrawal, protect-actor and de-escalation priorities that compete with maximizing damage.

Minecraft / Cobblemon / Craftics adapter/playback: required to present exact actor positions, recipient-scoped dialogue and aftermath. Entity proximity cannot create semantic reception by itself.

## PTU / Caelo boundary

This case authors no Persuasion, Guile, Intuition, Perception or Education DC; no eavesdropping roll; no hearing distance; no communication item; no Trainer Feature effect; no Move or Ability effect; and no penalty for acting on bad information.

If any of those mechanics become desirable, the exact supplied PTU/Caelo source must be inspected and the implementation verified in AutoPTU before use.

## Canon questions before promotion

The route name and actual route are intentionally unresolved.

The identity of the doorway listener is unresolved and should preferably reuse an existing resident whose schedule plausibly reaches the Field Office rather than create a disposable NPC.

The actual field-service task is unresolved.

The information scope of the provisional discussion is unresolved.

Whether any procedural change persists is unresolved.

Whether the rumor causes travel or battle is unresolved.

The case can be promoted only after those fields are reconciled against the Marea canon network and implementation owners.
