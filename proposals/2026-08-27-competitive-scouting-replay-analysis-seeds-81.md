# Competitive Scouting & Replay Analysis Seeds — Pass 81

Status: PROPOSED / NON-CANON.

These candidates are original Ouros material derived from the high-level structures documented in `research/2026-08-27-competitive-scouting-replay-analysis-scan-81.md`. They do not establish institutions, technology, regional policy or PTU mechanics.

## The Replay Everyone Studied

A high-profile formal match has a widely circulated replay. Weeks later, several challengers arrive prepared for the same highly visible opening pattern.

The original Trainer has not gained a secret counter-bonus. They simply know their old pattern is public and may choose a different legal plan if their current authoritative state permits it.

Useful consequences:
- commentators debate whether the old opening was ever fundamental to the Trainer's style;
- a junior challenger copies the counter without understanding why it worked;
- the institution's analysts begin distinguishing “frequently observed” from “guaranteed.”

No canon location or circuit is assigned.

## One Move, Once

A Trainer used a distinctive Move in one public match months ago. The Move was mechanically confirmed in that battle and therefore legitimately enters scouting history.

The next opponent plans around it heavily.

Possible outcomes:
- the Move remains legal but is never selected;
- the Pokémon is not in the new roster;
- a different legal tactic becomes more important;
- the analyst correctly identifies the old threat but overweights it.

The scenario demonstrates that a confirmed historical reveal can still be a poor prediction.

## Old Footage, New Team

A rival has access to several authentic old replays. All of them predate a visible change in the player's current team composition.

The rival's preparation packet therefore contains reliable historical information and explicit stale markers.

The story can explore whether the rival trusts the old evidence, seeks newer public information or chooses a general-purpose legal roster instead of trying to counter an uncertain current team.

## The Analyst Who Wasn't There

An analyst produces a confident report about a battle they did not witness. Their sources are:
- one public result summary;
- a short commentary clip;
- a secondhand description from an attendee.

The report may still contain useful insight, but its provenance is weaker than direct replay review.

A later full recording exposes which conclusions were well supported and which were extrapolation.

## Public Result, Missing Turns

An institution publishes the result and participating Trainers but no replay.

A recurring opponent knows who won and which Pokémon were publicly announced, but cannot legally reconstruct the full turn sequence.

This seed is useful when Ouros wants a competitive world with public records without assuming universal surveillance.

## The Commentator Names It Wrong

A public commentator confidently labels a visible effect as a particular Move or Ability. The authoritative battle event only confirms the effect, not that identity.

Later, another public source corrects the interpretation.

Persistent outputs:
- original commentary remains historically available;
- correction becomes a separate publication;
- actors who heard only the first version may retain stale information;
- the tactical record itself never changes.

## Two Cameras, One Blind Spot

Two recordings cover the same match from different angles. Each misses a different portion of the arena.

Combining them improves coverage but still leaves one decisive interaction ambiguous.

Possible gameplay:
- compare timestamps;
- identify which Trainer or Pokémon is actually visible in each frame;
- distinguish a confirmed switch from an assumed one;
- decide whether the remaining uncertainty matters for preparation.

The scene is evidence analysis, not a hidden truth meter.

## Closed Practice, Open Match

A Trainer practices privately at an institution before a public match. Several NPCs know practice occurred. The content of the practice remains private.

Only tactics actually revealed in the formal battle become available to normal public scouting.

This creates a clean privacy boundary even when the backend possesses the complete training state.

## Mock Battle Overfit

An institution builds a practice opponent from a famous replay. Trainees become very good at beating that historical synthetic profile.

When they later face the real Trainer, they discover that the mock model represented one old battle, not the person's complete decision process.

The scenario should never punish players through arbitrary hidden bonuses. Its point is epistemic: a useful model can still be limited.

## The Rival Watches One Match

A recurring rival attends one of the player's public battles.

The next callback packet records exactly what the rival could observe there. If the rival later challenges the player, any preparation must trace back to those observations or other legitimate sources.

The rival may remember:
- Pokémon that actually appeared;
- confirmed Moves that were used;
- public arena interactions;
- visible tactical patterns.

The rival may not suddenly know:
- unused Moves;
- private held items;
- reserve Pokémon never shown;
- private training plans.

## The Strategy Everyone Attributes to the Wrong Person

A well-known tactical pattern becomes associated publicly with one Trainer after a memorable match. Archive review later shows that a different participant initiated the relevant sequence and the famous Trainer merely responded well.

This can generate:
- a correction in public memory;
- an awkward interview;
- a rival who prepared for the wrong tendency;
- a historian or analyst interested in how competitive myths form.

No cheating or deliberate deception is required.

## Four Replays, Three Matches

Mystery seed.

An analyst archive contains four replay files apparently showing four separate meetings between the same two Trainers. Their metadata and visual details do not line up.

Possible explanation families:
- one replay is a documented derivative with alternate commentary;
- one upload is a duplicate re-encoded from another source;
- two files cover the same battle from different cameras;
- an old mock-battle recording was cataloged as a formal match;
- one file genuinely belongs to a different event.

Resolution depends on provenance, battle IDs, timestamps and visual coverage. It should not default to forgery.

## A Circuit Learns What Becomes Public

Long-form institutional arc.

Phase 1: a circuit has an existing but limited battle-record practice.

Phase 2: a major match attracts wider media attention and independent recordings circulate.

Phase 3: participants disagree over what should count as official replay material versus commentary or fan footage.

Phase 4: the institution changes its publication workflow after a concrete incident, such as misleading commentary, incomplete footage or a privacy concern.

Phase 5: months later, challengers operate under the revised system while older matches remain under their historical access rules.

This arc is deliberately policy-neutral. It can end with more openness, more restriction, tiered access or no universal replay archive depending on canon review.

## Analyst Cohort Instead of One Omniscient Expert

A battle institution has several people who watch matches for different purposes.

Possible roles:
- arena technician notices spatial patterns;
- coach focuses on decision sequencing;
- registrar knows only formal records;
- commentator knows public narrative;
- medical staff observes welfare-relevant events but keeps private details protected.

No single NPC automatically receives the union of all information. Handoffs require actual communication state.

## Replay Room Social Scene

A review room becomes a recurring social space before an event. Trainers pause, rewind, disagree, take notes and leave to pursue different preparation plans.

The scene can generate:
- mentorship requests;
- rival encounters without combat;
- media interviews;
- arguments about evidence quality;
- training hooks;
- requests for access to older public records.

It gives competitive culture playable texture without forcing another battle.

## Scouted Rematch

Mechanically rich candidate.

Narrative premise:

A recurring opponent has genuinely watched selected public battles and prepared for confirmed patterns. The player knows that some prior information is public, but not exactly how the opponent will use it.

Intended full version:

Ouros compiles a `competitive_knowledge_packet` for the opponent. AutoPTU tactical AI receives only that packet plus information revealed during the current battle. The opponent reasons tactically within an approved policy and current legal roster.

Capability dependencies:
- targeting/footprints/range/LoS — required;
- base movement legality — required;
- complete movement including push/pull/knockback/interception/forced movement — required only where the selected legal roster uses those mechanics;
- core calculations — required;
- action economy/initiative — required;
- full turn/round lifecycle — required;
- full stateful damage pipeline — required;
- status lifecycle — required where relevant;
- terrain/weather/hazards/zones/reactions — required only if the approved arena/roster uses them;
- move-specific behavior — required;
- abilities — required;
- items — required where allowed;
- Trainer Features/perks — required where allowed;
- AI legal-action infrastructure — required;
- AI tactical policy — central requirement;
- Minecraft/Cobblemon/Craftics adapter/playback support — required for full in-world execution.

Current reduced version:

The same legal scouting packet exists in world state. Before battle, a reviewed static opponent roster/profile is selected using only information that could legally motivate that choice. No dynamic tactical “learning” claim is made. AutoPTU resolves an ordinary approved encounter. Post-battle reveals update future history.

The reduced version preserves the premise that the opponent prepared without pretending current tactical AI can exploit scouting dynamically.

## Analysis Between Rounds

Mechanically rich event candidate.

Narrative premise:

An invitational has multiple separate matches. Between matches, participants can review footage that the event has actually published.

Intended full version:

Later autonomous opponents receive new reveal information after each publication/access checkpoint and alter tactical decisions through an approved AI policy.

Dependencies:
- full turn/round lifecycle;
- semantic battle-event/reveal output;
- move-specific behavior;
- abilities/items/Trainer Features as used;
- AI legal-action infrastructure;
- AI tactical policy;
- adapter/playback;
- arena-specific movement/environment families when selected.

Reduced version:

Each round is an independent ordinary battle. Between rounds, Ouros records and distributes only reviewed authoritative public reveals. Later opponents use a curated static preparation profile rather than dynamic AI adaptation.

## Film Review Disagreement

Noncombat encounter.

Two analysts disagree over the turning point in a public match.

One emphasizes positioning. The other thinks an earlier switch created the decisive sequence. The player can review the footage, authoritative reveal events and commentary history.

Possible outcomes:
- both identify different valid causal layers;
- one relied on a cropped derivative;
- the replay cannot settle the question;
- a later match provides stronger comparative evidence.

No tactical capability family is required for the review scene itself.

## Preparation Without a Battle

A Trainer learns that a future opponent has a strong public record but decides not to study footage. Instead they spend the preparation window on travel, recovery, a personal project or another priority.

This seed keeps scouting optional. Competitive systems should create choices rather than compulsory chores before every important fight.

## Canon questions carried forward

These proposals intentionally leave unresolved:
- which Ouros institutions record battles;
- whether public replays are common;
- who owns or controls recordings;
- spectator recording norms;
- analyst/coaching professions;
- privacy expectations;
- replay retention periods;
- whether mock opponents exist technologically;
- how official challengers are allowed to scout one another;
- what exact PTU/Caelo mechanics, if any, can turn preparation into mechanical progression.
