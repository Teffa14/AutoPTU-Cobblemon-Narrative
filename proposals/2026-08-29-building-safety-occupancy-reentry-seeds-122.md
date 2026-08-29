# Ouros Proposals — Building Safety, Occupancy & Reentry Seeds — Pass 122

Status: NON-CANON PROPOSALS. These are reusable story candidates. They do not establish locations, institutions, laws, professions or mechanical rules.
Date: 2026-08-29

## Design target

Use post-damage buildings as persistent places whose access, use and meaning can change over time. Prefer scope, provenance and institutional handoffs over a single safe/unsafe switch.

## Situation seeds

### The Ground Floor Opened First

A familiar public building resumes one ordinary service at ground level while the upper floors remain under review. Residents begin treating the temporary arrangement as normal. The player later needs information stored upstairs, but the restriction remains authoritative until the appropriate review occurs.

Useful systems: building assessment, service owner, archives, public notices, accessibility, maintenance.

### The Sign Is Older Than the Repair

A restrictive notice remains physically posted after a repair milestone. A newer decision exists in the records, but the public-facing sign was never replaced.

Mystery value comes from distinguishing presentation, publication and governing state. Do not make the old sign secretly correct unless evidence supports it.

### The Plaza Reopened, the Tower Did Not

Cleanup makes an exterior civic space usable again while the adjacent landmark remains restricted. Vendors and Pokémon routines return around the perimeter, creating a new temporary social geography.

A later restoration proposal can reuse the same location without undoing the history of the restricted period.

### The Building Has Two Front Doors Now

A temporary entrance created during repairs becomes the preferred entrance after partial reopening. Older maps, delivery routines and NPC memories still refer to the previous front door.

This can generate courier errors, accessibility questions and route-history mysteries without requiring any combat.

### The Pokémon Returned Before the People

An individual or known local group of Pokémon begins using an exterior or vacant section of a structure while human use remains restricted.

Their presence is an ecological/social observation only. It does not prove structural safety, immunity or an ability to detect hidden damage.

### The Repair Finished Friday, the Review Is Monday

Maintenance records show a repair complete, but the next required assessment has not occurred. Staff and residents disagree about whether the delay feels reasonable.

The system should preserve `WORK_COMPLETED`, `REEVALUATION_REQUIRED` and current use restriction independently.

### The Archive Moved Downstairs and Stayed There

A temporary archive desk established during a closure becomes useful enough that the institution keeps it after broader reopening. Recovery permanently changes information access and NPC routines.

### The Building Was Never Closed Everywhere

Years later, oral histories say the whole structure “closed” after an incident. Contemporary records reveal that one wing, one exterior service window and a rear courtyard remained usable.

This supports historical nuance without treating memory as a lie.

### The New Event Makes the Old Review Obsolete

A structure had already passed a scoped review when a second authored event affects the site. The old assessment remains valid evidence about the earlier moment, but a new decision is required.

Possible triggers must come from existing world state: aftershock, nearby slope event, fire, flood, impact, excavation or another governed event.

### The Ruin Became a Landmark

A structure never returns to its previous function. Its stabilized exterior becomes part of a public space, habitat edge, memorial route or research context while entry remains restricted.

Civic Governance, Public Memory, Conservation and Building Assessment can each own separate parts of the outcome.

### Everyone Says “Reopened” and Means Something Different

One NPC means the public plaza. Another means staff access. A third means the service counter. A fourth means full ordinary occupancy.

Use this as a dialogue/provenance problem instead of a semantic trick.

### The Assessment Covered the Old Floor Plan

Renovation changed internal geometry after an old incident. A current dispute references an assessment scope described using room names that no longer exist.

Players reconcile archived plans, persistent structure IDs, door alignments and later modifications before any new physical conclusion is drawn.

## Mystery — Five Dates on One Door

A door carries evidence of five apparently incompatible dates: incident, first restriction, repair completion, reevaluation and public reopening notice.

Resolution structure:
- identify what each date records;
- separate physical work from review;
- identify notice publication lag;
- map each record to a spatial scope;
- reconstruct which state was authoritative at each moment.

Possible conclusion: every record is genuine and no one falsified anything.

Implementation: READY as world-state/provenance content.

## Mystery — Three Inspectors, Two Authorities

Three technical assessments exist for the same site. Two were advisory; one was tied to the locally authored decision authority. Their technical conclusions also cover different scopes.

The player must discover roles and mandates from canon-backed institutional records. The generator must not invent a legal hierarchy.

Implementation: READY if the relevant authority relationships are authored first.

## Exploration — The Closed Floor Above the Market

Current state:
- the ground floor operates as a market or public service;
- an upper level remains restricted;
- a renovation changed stairs and room numbers;
- an older plan references a now-hidden access route;
- a known Pokémon has been observed near an exterior opening.

Playable sequence:
1. compare map editions;
2. identify old/new structure geometry;
3. trace assessment scopes and revisions;
4. locate the former access from an authorized stable area;
5. determine which question requires a fresh assessor rather than player inference;
6. preserve the result as a new handoff.

Reduced implementation:
Only currently authorized stable spaces are traversable. The restricted level remains outside encounter geometry. The premise works without collapse, falling debris or dynamic hazards.

## Long arc — A District Learns to Reopen in Pieces

Phase one establishes normal use of several recurring buildings before any crisis.

Phase two introduces one bounded event affecting different structures differently. Crisis handles immediate response. Building assessments then produce scoped restrictions rather than a blanket district state.

Phase three follows partial return: one shop uses an alternate entrance, a clinic moves a desk, residents return unevenly, a public building opens only its exterior space, and a Pokémon group begins using a quiet restricted edge.

Phase four allows repairs and reevaluations to change states at different times. Some temporary arrangements disappear. Others remain because they proved useful.

Phase five revisits the district months or years later. A new incident, archive discovery, renovation proposal or returning character makes the old assessment history relevant again.

No universal `recovery_percentage` is required.

## Faction and NPC candidates

### The Scope-Obsessed Assessor

A technical character who repeatedly states exactly what area was and was not reviewed. Their usefulness comes from precision rather than mystical certainty.

Status: proposed archetype only. Qualification and institution require canon.

### The Service Manager Who Can Open Less Than the Building Allows

Their facility has permission to use a space, but staffing or equipment limitations keep service reduced. This creates friction without requiring corruption or incompetence.

### The Resident Historian

An NPC preserves old floor plans, photos and notices. They know how the building changed but do not have technical authority to declare it safe.

### The Pokémon With a Routine Around the Restricted Edge

A recurring individual becomes a useful timestamp witness because its documented routine changed when barriers moved. Behavior can support chronology while remaining non-diagnostic.

## Encounter concept — Assessment Team Withdrawal

Full version:
An assessment team must leave an exterior review zone while a Pokémon conflict develops. The encounter supports withdrawal/protection, Intercept, forced movement and possibly a restriction boundary that changes after a secondary event.

Required capability families:
- targeting/footprints/range/LoS — VERIFIED baseline;
- base movement legality — VERIFIED;
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL if timing windows matter;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL;
- terrain/weather/hazards/zones/reactions — BLOCKING when changing restriction cells or generalized reactions matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:
Ouros completes the team's withdrawal first. Restricted areas and equipment remain outside BattleSpec. AutoPTU resolves a static legal encounter on reviewed exterior ground. Victory secures immediate access only; it does not complete inspection or authorize occupancy.

## Encounter concept — Partial Reopening Perimeter

Full version:
Players protect a boundary between an authorized public area and a still-restricted scope while civilians withdraw. Crossing the boundary may matter tactically.

Rich implementation depends on complete movement, generalized reactions, zone semantics, lifecycle, objective-aware AI and semantic playback.

Reduced version:
The service closes the public area temporarily before combat. All civilians leave. The restricted scope is excluded from the arena. A conventional battle occurs in an authorized static perimeter. Building and service owners decide subsequent reopening.

## Encounter concept — Reinspection After a Secondary Event

Full version:
A previously reviewed structure experiences a new event and an encounter occurs while access is being regained. Falling debris, unstable cells, delayed changes or environmental effects could matter if exact governed rules exist.

Direct dependencies:
- complete movement including push/pull/knockback/interception/forced movement — PARTIAL;
- full turn/round lifecycle — PARTIAL for delayed phases;
- full stateful damage pipeline — PARTIAL if an exact environmental damage rule is present;
- status lifecycle — PARTIAL if exact status rules apply;
- terrain/weather/hazards/zones/reactions — BLOCKING;
- AI tactical policy — BLOCKING for protection/withdrawal;
- Minecraft/Cobblemon/Craftics adapter/playback support — BLOCKING.

Reduced version:
The secondary event ends before BattleSpec creation. All newly uncertain scopes stay inaccessible. Combat uses a stable reviewed exterior or adjacent space. Success can restore approach access, while reevaluation remains a separate world-state requirement.

## Safe immediate content

The following can run without new tactical capability:
- compare old and new notices;
- reconcile scope between floor plans;
- trace a repair-to-review handoff;
- discover that “reopened” referred to only one use;
- document persistent ruins;
- follow a temporary entrance becoming permanent;
- reconstruct a building's adaptive reuse;
- compare Pokémon routine observations across closure/reopening;
- find an evidence gap that requires a new assessment;
- resolve historical contradictions through timestamps and spatial scope.

## Canon questions intentionally left open

- Which Ouros institutions can issue use restrictions or reentry authorization?
- Are technical assessors and decision authorities normally the same actors anywhere?
- Which regions use formal public notices and which rely on other communication methods?
- What vocabulary does each jurisdiction use for limited use, restricted access or reassessment?
- Which structures have important damage/reopening histories?
- Can any Pokémon individuals hold trained inspection/maintenance roles, and under what explicit canon?
- Which historical ruins were restored, reused, stabilized, abandoned or preserved?

No answer is assumed by these proposals.