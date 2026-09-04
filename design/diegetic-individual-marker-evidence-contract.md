# Diegetic individual marker evidence contract — Pass 254

Status: PROPOSED DESIGN CONTRACT
Canon effect: NONE until approved

## Purpose

Extend Pass 253 with a stronger but still fallible evidence path for recurring wild Pokemon. The player may confirm identity through an approved diegetic marker or validated natural-mark record without receiving Ouros' hidden `persistent_actor_id`.

## Authority boundary

Ouros owns persistent actor identity and the authoritative mapping between a field marker record and that actor.

The public research layer owns only observable evidence and marker-registry records. Minecraft/Cobblemon may render a visible marker or capture an image/observation. It cannot create, change or resolve the hidden actor mapping.

AutoPTU is not required for ordinary observation. If a Trainer Feature, Skill check or special capability is mechanically invoked, its effect requires the active rules profile and verified engine support.

## Public recognition states

Pass 253 states remain valid:

- `UNRESOLVED`
- `POSSIBLE_SAME_INDIVIDUAL`
- `PROBABLE_SAME_INDIVIDUAL`

Pass 254 proposes one stronger state:

- `CONFIRMED_BY_DIEGETIC_MARKER`

This state means that the observer has sufficient public evidence to treat the current sighting as the same marked individual represented by a field registry entry. It does not expose or equal the hidden Ouros actor ID.

## Marker registry record

A deliberate marker record should contain only field-safe data:

```text
marker_record_id
marker_type
observable_code
species_or_form_scope
application_provenance
application_time_band
validity_state
last_verified_time
welfare_clearance_ref (when applicable)
notes_visible_to_authorized_researchers
```

The hidden persistence layer separately binds `marker_record_id -> persistent_actor_id`.

Forbidden public fields remain:

```text
persistent_actor_id
projection_lease_id
minecraft_uuid
internal_population_source_id
hidden_population_slot
```

## Marker validity lifecycle

Proposed states:

- `ACTIVE`
- `OBSCURED`
- `DAMAGED`
- `REPORTED_LOST`
- `RETIRED`
- `AMBIGUOUS`

Only an `ACTIVE` marker observed at sufficient evidence quality may support `CONFIRMED_BY_DIEGETIC_MARKER`.

A confirmed identity hypothesis may be downgraded when later evidence shows the marker is lost, duplicated in transcription, unreadable, damaged or otherwise ambiguous. Historical observations remain immutable; the current epistemic state changes.

## Natural-mark path

A naturally distinctive visible feature may support stronger recognition only when a separate species-appropriate evidence profile establishes that the feature is sufficiently stable and distinguishable under the observed conditions.

Natural marks do not receive automatic permanence. Image angle, distance, lighting, occlusion, molt/form change, injury and observer competence may lower evidence quality.

No natural Fletchling individual marker is canonized by this contract.

## Trainer skill and Feature integration

PTU Survival and Perception are valid candidate skills for acquiring or interpreting field evidence. Pokemon Education may be required when species-specific interpretation is necessary.

Generic Skill Stunt and Journey of Skill can affect a qualifying Skill Check only if the active Ouros rules profile adopts the feature and AutoPTU-Java has a verified Trainer Feature/perk execution contract for this use.

Trainer Features may improve one or more of:

- observation quality;
- chance to notice a marker;
- ability to distinguish a mark from background appearance;
- interpretation quality;
- recovery from a poor observation attempt when the exact PTU Feature permits it.

They may not directly:

- reveal `persistent_actor_id`;
- create a marker registry entry;
- map an unknown visible Pokemon onto a hidden actor without evidence;
- mutate population or demographic state;
- open AutoPTU merely because identity was recognised.

Channeler-derived information, when implemented and legally used, can add behavioural evidence or recent-memory evidence. It does not automatically satisfy the marker confirmation gate.

## Confirmation gate

A recognition reducer may enter `CONFIRMED_BY_DIEGETIC_MARKER` only when all of the following hold:

1. the observer captured a new evidence record with an independent provenance root;
2. the evidence contains an observable marker code or validated natural-mark signature;
3. evidence quality meets the profile-specific threshold;
4. a public marker/natural-mark registry lookup returns exactly one active candidate;
5. no unresolved material contradiction invalidates that candidate;
6. no hidden actor identifier is copied into the public record.

If lookup yields zero or multiple candidates, remain `PROBABLE`, `POSSIBLE` or `UNRESOLVED` as appropriate.

## Marker application boundary

This contract does not authorize applying a physical tag to a wild Pokemon.

A future physical-marking procedure must separately specify:

- institutional authority and consent/governance model appropriate to Ouros;
- capture/handling requirements;
- Pokemon welfare constraints;
- species/form size compatibility;
- marker loss and removal policy;
- whether any PTU mechanics are invoked during handling;
- Minecraft/Cobblemon visual representation.

Until approved, all Pass 254 marker application events are fixture-only.

## Reduced encounter version

The player photographs a recurring wild Pokemon and reads a visible research marker already present in fixture truth. A registry lookup confirms the public marker record and promotes the hypothesis. Later, a poor sighting cannot read the marker and therefore contributes behavioural evidence only.

Dependencies: Minecraft/Cobblemon/Craftics adapter/playback support for visible marker presentation and observation capture. No AutoPTU tactical family is required.

## Rich encounter version

A researcher follows the Pokemon, positions for a clean view, uses an adopted PTU Skill/Feature to improve observation quality, and may need to avoid alarming the target.

Dependencies when mechanically adjudicated: targeting/footprints/range/LoS; base movement legality; complete movement when pursuit/interception/forced movement occurs; full turn/round lifecycle when a structured scene is opened; Trainer Features/perks for Skill Stunt/Journey of Skill or other adopted features; AI legal-action infrastructure; AI tactical policy when the Pokemon chooses legal evasive responses; Minecraft/Cobblemon/Craftics adapter/playback support. Terrain/weather/hazards/zones/reactions applies when the route or observation mechanically uses them. Damage, status, Moves, Abilities and Items apply only if invoked.

## Fail-closed requirements

Reject or downgrade a transition when:

- marker validity is not `ACTIVE`;
- public evidence contains a hidden actor or lease identifier;
- a marker code resolves to multiple active registry entries;
- the only new support is a relay of an existing provenance root;
- an ordinary behavioural observation attempts to bypass the Pass 253 `PROBABLE` ceiling;
- a Trainer Feature effect is assumed without a verified rules-profile/engine contract;
- a recognition event attempts a demographic mutation;
- confirmation alone requests AutoPTU handoff.

## Open canon questions

Ouros still needs to decide whether physical research marking exists at Sendero, which institution can issue marker records, which species are eligible, and what welfare process is required.

Natural-mark confirmation for Fletchling remains unapproved pending species-specific evidence.

Trainer Feature/perk modifiers remain implementation-blocked until the relevant AutoPTU-Java contracts are verified.