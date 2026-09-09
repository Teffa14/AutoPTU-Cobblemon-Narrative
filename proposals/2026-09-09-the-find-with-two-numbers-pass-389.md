# The Find With Two Numbers — Pass 389

Status: PROPOSED / NON-CANON.
Date: 2026-09-09

## Premise

A field team documents one portable find under a field identifier. Later, a receiving collection gives the physical object a different catalog identifier. Older notes use only the first code. Newer records use only the second.

When both record sets are reviewed together, several people conclude that the field object vanished and an unrelated object entered the collection. That conclusion is plausible from their local evidence, but it has not been established.

The investigation asks whether the two identifiers refer to one persistent physical resource and which historical records can actually be linked to it.

## Why this belongs in Ouros

Ouros already treats records, observations, private knowledge and physical world state as separate evidence-bearing systems. Pass 389 adds a stable bridge between a `PORTABLE_FIND` observation and a `WorldResource`, allowing identifier reconciliation without rewriting either the original field record or the object's later operational history.

The premise can intersect the canonical Tideglass Archive network because Ouros already has an archive role, but this file does not assign the incident to Tideglass or any named NPC. A future canon review may bind it to an existing institution rather than create a redundant one.

## Initial evidence state

The scenario should begin with facts that can coexist:

- one `PORTABLE_FIND` observation exists under a site revision;
- that observation contains its original `evidence_ref` and provenance;
- one stable `WorldResource` exists for the portable object;
- Pass 389 can bind the observation to that resource under explicit authority;
- one later record may use another human-facing catalog identifier;
- custody/location may have changed after discovery;
- not every NPC has seen both identifier systems.

The scenario does not begin with a canonical conclusion about fraud, theft, substitution, clerical error or authenticity.

## Investigation paths

An actor with access only to field notes may correctly report that the field code disappears from later paperwork.

An actor with access only to later collection records may correctly report that the catalog code has no visible field-code history in their local record set.

An actor who obtains the binding evidence can demonstrate that a particular field observation and a particular persistent world resource were explicitly associated at a specific semantic minute under a stated authority.

That still does not prove that every historical description attached to either human-facing number belongs to the same object. Additional records, custody events or direct inspections may be needed.

## Consequences without a villain

A dual-number discrepancy can delay research, trigger an inventory review, pause a loan or display, produce contradictory testimony, create a faction dispute over documentation quality, or force an expedition team to reconstruct provenance before a later decision.

If later evidence establishes deliberate substitution, theft or falsification, that should emerge from a separate evidence chain. The premise works equally well if the cause is routine renumbering combined with incomplete cross-reference.

## Reduced implementation

The reduced version needs:

- semantic time;
- `SiteEvidenceLedger` with a `PORTABLE_FIND` observation;
- `OUROS_PORTABLE_FIND_RESOURCE_BINDING_V1`;
- an explicit declared `WorldResource` mapping;
- existing resource/custody history if the object moved;
- existing archive/publication/communication/private-knowledge systems for who knows which identifier;
- ordinary world-agent replanning after new evidence arrives.

No battle is required. No Minecraft actor is required for the object while the investigation is off-screen.

## Rich implementation

A richer episode can require recovering or escorting the already-identified object during a temporary relocation, documenting it before environmental conditions worsen, or protecting a transport while the identifier dispute is unresolved.

The narrative objective remains preservation/reconciliation of evidence. A battle, if one occurs, cannot decide provenance by itself.

### Exact engine capability dependencies

Targeting/footprints/range/LoS: required only if the tactical version uses spatially explicit actors or objective zones.

Base movement legality: required for ordinary tactical travel within a battle scene.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL; required for forced displacement, interception, rescue repositioning or protected-object carrying interactions that depend on those mechanics.

Core calculations: VERIFIED only for the audited calculations actually invoked.

Action economy/initiative: VERIFIED only for audited primitives used by the scene.

Full turn/round lifecycle: PARTIAL; required for timed protection windows, phased extraction or delayed events.

Full stateful damage pipeline: PARTIAL; required if damage persistently changes an actor, carrier or protected-object objective state.

Status lifecycle: PARTIAL; required if lasting PTU statuses affect the objective.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING according to the exact mechanism. Floodwater, unstable flooring, debris, visibility zones, reactive hazards and delayed environmental effects require explicit support.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated. The portable find remains a world resource unless authoritative PTU data separately defines it as a battle Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: usable only inside verified legal-action scopes.

AI tactical policy: BLOCKING for protect-object, retrieve-object, escort, evidence-first behavior, objective-aware withdrawal and disengage-after-objective until those policies are specifically verified.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for stable resource projection, pickup/handoff acknowledgement, objective identity and authoritative non-KO result playback.

## Failure and transformation states

The story can continue if the object cannot be inspected immediately. A missing transport, closed archive, inaccessible record set or contradictory alias can turn the episode into a follow-up investigation without erasing the original field observation or binding.

A later discovery that two identifiers truly refer to different objects should create a new evidence correction and relationship consequence. It must not retroactively edit the original observation into something it never recorded.

## Open canon questions

- Which existing Ouros institution, if any, owns the local catalog process?
- Does Tideglass handle physical collections or only documentary archives in the relevant district?
- Who may create a binding between field evidence and a persistent resource?
- Which authority controls removal from a site?
- How are ownership/title and custody distinguished in Ouros law or custom?
- Which PTU/Caelo Skills, Edges or Trainer Features can affect documentation, authentication or conservation actions?
- What world evidence can establish an alias between two human-facing identifiers without making the runtime omniscient?

No answer is promoted by this proposal.
