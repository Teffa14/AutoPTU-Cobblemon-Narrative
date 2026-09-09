# The Object That Arrived Without Its Context — Pass 388

Status: PROPOSED / NON-CANON.

## Premise

A field team recovers a portable object from a documented site and transfers it through an authorized custody chain. The object reaches the expected recipient. The accompanying context report does not.

The world can prove that the object was observed at the site, that a stable resource identity was assigned and that custody changed. It cannot infer that the receiver knows where the object came from, why it mattered or what the field team believed about it.

## Narrative value

The mystery comes from two valid histories that have become separated:

- physical custody history;
- informational/context history.

The receiver may catalogue the object conservatively because provenance is incomplete. A field researcher may assume the repository already knows the context because the object arrived. A third actor may later find the delayed report and change the interpretation without changing any earlier observation or transfer event.

Possible explanations remain hypotheses until evidence supports them:
- delayed communication;
- damaged records;
- routing error;
- staff absence;
- incorrect recipient selection;
- deliberate withholding;
- mundane administrative backlog.

No explanation is canon-approved by this proposal.

## Reduced implementation

The reduced version needs no AutoPTU battle.

Required world systems:
- `SiteEvidenceLedger` records the original `PORTABLE_FIND` observation;
- observer-private knowledge preserves what the field actor saw;
- a stable `WorldResource` represents the physical object;
- the proposed portable-find binding links that resource to the observation;
- existing resource handoff history records physical transfer;
- existing communication infrastructure carries the context report independently;
- recipient knowledge changes only if that report or another valid evidence source reaches them.

Success can mean reconnecting object and context records. It does not require combat or ownership transfer.

## Rich version

The handoff may occur during an unstable-site evacuation. The team must decide whether to spend additional time documenting context, stabilize the find, escort a specialist, recover a dropped record package or withdraw with incomplete evidence.

Combat pressure is optional. Wild Pokémon, rival field teams or environmental danger can complicate the scene without becoming the objective itself.

## Capability dependencies

Targeting/footprints/range/LoS: only if a tactical scene uses spatial interactions.

Base movement legality: required for basic tactical approach and retreat.

Complete movement: required for dragging, forced displacement, interception, push/pull or knockback around the find or personnel.

Core calculations: required only for PTU calculations actually invoked.

Action economy/initiative: required for turn-ordered recovery actions.

Full turn/round lifecycle: required for timed phases or delayed environmental changes.

Full stateful damage pipeline: required if damage persists and affects evacuation or recovery.

Status lifecycle: required if persistent conditions affect the scene.

Terrain/weather/hazards/zones/reactions: required for collapse, unstable surfaces, flooding, dust, visibility zones or reaction hazards.

Move-specific behavior: individually gated.

Abilities: individually gated.

Items: individually gated. The recovered object is not automatically a PTU battle Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: required for legal tactical action generation.

AI tactical policy: currently blocking for protect-find, retrieve-object, escort, rescue-first, documentation-first, objective-aware withdrawal and disengage-after-objective policies unless directly verified.

Minecraft/Cobblemon/Craftics adapter/playback: partial/blocking for stable object identity, pickup and handoff acknowledgement, site revision playback and authoritative non-KO objective completion.

## Canon questions

- Which Ouros institution receives the object?
- Which site produces it?
- Who has authority to remove it?
- Does Ouros model legal ownership separately from custody?
- Is the delayed context carried as a private report, public record or physical archive package?
- Which PTU/Caelo Skills or Trainer Features may matter for recovery and documentation?
