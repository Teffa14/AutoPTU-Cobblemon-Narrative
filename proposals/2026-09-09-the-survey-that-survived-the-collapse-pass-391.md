# The Survey That Survived the Collapse

Status: PROPOSED / NON-CANON.
Date: 2026-09-09

## Premise

A survey team documents a fixed feature inside an old structure. Before the team finishes its ordinary report cycle, part of the accessible route fails and exposes a second physical layer that was not visible during the first survey.

The incident triggers several independent responses at once:

- one researcher leaves with the original field notes;
- another actor begins an evacuation or rerouting action;
- a later observer documents the newly exposed layer;
- an institutional contact receives only part of the information before communications are interrupted.

The mystery is not whether one record must be false. The useful problem is reconstructing which physical revision each person saw, what they did next and which evidence had actually reached each actor at each point.

No location, institution, species, culture, historical builder, collapse cause or final interpretation is canonized by this proposal.

## Narrative value

The scenario supports a mystery that survives interruption and restart without depending on a single quest flag.

The site can remain interesting after the immediate incident because different actors carry different pieces of the history. A player can return later and still find meaningful consequences in travel plans, delayed reports, revised interpretations, custody records or institutional disagreement.

The incident can also become one thread in a larger regional mystery without requiring the local collapse to contain the whole answer.

## Reduced playable version

No AutoPTU handoff is required.

The reduced version uses:

- semantic time;
- `SiteEvidenceLedger` revisions and observations;
- direct-observation private knowledge;
- private interpretation/inference lineage;
- world travel and `TRAVEL_REPLAN_REQUIRED` when access changes after movement begins;
- explicit communication and delivery state;
- `OUROS_NPC_WORLD_CHECKPOINT_V19`;
- `OUROS_PERSISTENT_WORLD_EVIDENCE_CHECKPOINT_V2`;
- `OUROS_PERSISTENT_WORLD_RECOVERY_MANIFEST_V1` to select a coherent checkpoint pair after restart.

A successful investigation can establish a timeline such as:

1. Team A observed revision R1.
2. Access changed after Team A began leaving.
3. Team B later observed revision R2.
4. Only some reports were delivered before the interruption.
5. Later interpretation reconciled both surveys without mutating either historical observation.

That is sufficient for a meaningful objective even if the collapse cause and deeper historical meaning remain unresolved.

## Optional exploration structure

The site can be divided into a small number of functional spaces instead of a combat gauntlet:

- a safe staging area where records can be compared;
- an original survey room whose visible state changed;
- a blocked or rerouted connection;
- an alternate access point that reveals different evidence;
- one optional pressure encounter that can be avoided, delayed or solved without KO if implementation allows.

The ordering does not need to be linear. Access state and evidence availability can redirect the route.

## Rich encounter version

A richer implementation can stage the physical change while the player is present.

Possible objectives include:

- finish documenting a fixed feature before visibility is lost;
- escort a researcher carrying the only complete field record;
- reopen or bypass a route long enough for evacuation;
- recover equipment after the evidence objective is already complete;
- protect a fragile observation point without defeating every hostile Pokémon;
- withdraw once all required people and records reach the safe zone.

KO is not the narrative victory condition.

## Permanent capability dependencies

Targeting/footprints/range/LoS: VERIFIED within audited scopes only. Suitable for ordinary tactical placement only where the exact tested geometry is applicable.

Base movement legality: VERIFIED within audited scopes only.

Complete movement including push/pull/knockback/interception/forced movement: PARTIAL. Required for forced slides, rescue repositioning, dragging, knockback, pull effects or interception around evacuation lanes.

Core calculations: VERIFIED within audited scopes only.

Action economy/initiative: VERIFIED for audited primitives only.

Full turn/round lifecycle: PARTIAL. Required for timed documentation windows, staged collapse, delayed route failure or multi-round evacuation phases.

Full stateful damage pipeline: PARTIAL. Required if damage persistently alters carriers, protected evidence, structural objectives or later phases.

Status lifecycle: PARTIAL. Required for lasting conditions such as immobilization, confusion or other persistent effects used by the encounter.

Terrain/weather/hazards/zones/reactions: MIXED / PARTIAL / BLOCKING by exact mechanism. Falling debris, unstable floors, dust visibility, flooding, triggered collapse, hazard zones or reaction-driven environmental changes must be verified individually.

Move-specific behavior: individually gated.

Abilities: individually gated. AutoPTU-Java merge #420 verifies the current Impostor round-start seam only and does not grant general Ability support.

Items: individually gated. Survey equipment and archaeological finds are world resources unless an authoritative PTU/Caelo rule establishes a battle Item behavior.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: VERIFIED within ordinary audited scopes only.

AI tactical policy: BLOCKING for escort, rescue-first, documentation-first, protect-evidence, route-clearing, objective-aware withdrawal and disengage-after-objective until exact policy coverage exists.

Minecraft/Cobblemon/Craftics adapter/playback support: PARTIAL / BLOCKING for persistent site-revision projection, evidence interaction acknowledgement, route-state presentation, environmental objective state and authoritative non-KO result playback.

## Mechanical fallback

If rich hazard support is unavailable, the physical change occurs at the world-agent layer between tactical scenes rather than during one.

The player can still experience the same premise:

- inspect R1;
- leave or travel;
- receive a route-change event;
- return through another path;
- inspect R2;
- reconcile evidence and NPC accounts.

This preserves the story while avoiding local imitation of missing AutoPTU mechanics.

## Canon questions deliberately left open

- exact Ouros/Caelo location;
- responsible institution or survey group;
- cause of the physical change;
- whether the lower layer is archaeological, geological, engineered or another category;
- species present at the site;
- legal access and preservation authority;
- which PTU/Caelo Skills, Edges, Features or Items apply;
- whether the incident connects to a larger regional arc.

Nothing above becomes canon without explicit promotion.
