# Four Flags on the Board — Pass 402

Status: PROPOSED / NON-CANON
Canon approval: REQUIRED before fixing the noticeboard, institution, exact sites, NPC participants, missing equipment, environmental cause, species, rewards or PTU/Caelo mechanics.

## Canon-safe anchors

Ouros already supports persistent institutions, explicit knowledge, schedules, obligations, world travel, resource reservations, custody history and recurring field work. Existing canon locations such as Estación Mirador, Sendero del Vidrio and Tideglass Archive can inspire the operational pattern, but this proposal does not assign the quest to any canon place automatically.

## Premise

A field office posts four small recovery or verification notices at once. Each concerns a survey flag, route marker, sample case or comparable non-combat field object that failed to return from a different ordinary job.

The notices are independent. The player may take none, one, several or all. Named NPCs can also accept work that remains available.

Each recovered object carries a small amount of provenance: where it was found, who last held it according to the best available history, which route revision was active and what local observation accompanied its use.

Three recoveries look routine. The fourth creates a discrepancy. The physical object is in a plausible place, but the associated observation conflicts with the current condition of that site.

The discrepancy does not prove theft, sabotage or false reporting. Possible explanations include a real environmental change, a delayed return, a legitimate handoff, incomplete documentation, a mistaken site reference or an observation that was accurate only at that earlier time.

## Optional progression

The office board remains useful even if the player ignores it. Other actors may complete notices under ordinary world-agent rules. Completed work changes the available evidence rather than retroactively awarding the player credit.

If all four provenance packets eventually become available, they may reveal a broader pattern worthy of a later investigation. That later thread is optional and must be authored separately. Three ordinary jobs are allowed to remain ordinary jobs.

## Disclosure pressure

The fourth recovery can create two legitimate audiences for the same evidence. One actor may need the object returned quickly for operational reasons. Another may need the discrepancy documented before the object is cleaned, recalibrated or redeployed.

The player or NPC handling the recovery may therefore face a timing and communication decision. The world should preserve who actually received which report and when.

No automatic morality flag is required. Consequences should follow from obligations, evidence handling, trust and later knowledge.

## Reduced implementation

The reduced form requires no AutoPTU encounter.

Use semantic time, public publication/receipt, explicit acceptance of obligations, world travel, resource reservation state, journal-aware checkout/return/handoff, holder/custody history, persistent observations, private knowledge and later communication.

Environmental differences can occur between visits as authored world revisions rather than tactical hazards.

This version preserves the entire mystery premise and can run while battle capabilities remain incomplete.

## Mechanically rich version

A recovery site may later include active environmental pressure or wild-Pokémon contact while the objective remains recover, observe, protect, evacuate or withdraw.

Required capability families must be declared per encounter:

Targeting/footprints/range/LoS: required if protection, ranged interaction or spatially constrained targeting matters.

Base movement legality: required for ordinary tactical navigation.

Complete movement including push/pull/knockback/interception/forced movement: required for dragging, body-blocking, forced slides, interception or displaced-object/actor handling.

Core calculations: required for ordinary resolved checks delegated to AutoPTU.

Action economy/initiative: required once actions compete inside tactical time. Current evidence covers only audited primitives.

Full turn/round lifecycle: required for timed exposure windows, phase changes, delayed collapse or multi-round extraction clocks.

Full stateful damage pipeline: required when damage/injury must persist into world consequences.

Status lifecycle: required for complex or lasting conditions.

Terrain/weather/hazards/zones/reactions: required for unstable ground, flooding, wind, reduced visibility, reactive debris, zone triggers or weather phases.

Move-specific behavior: individually gated.

Abilities: individually gated. Current switch-entry evidence does not validate the family.

Items: individually gated. A narrative survey object is not automatically an implemented PTU Item.

Trainer Features/perks: individually gated.

AI legal-action infrastructure: usable only inside currently audited ordinary scopes.

AI tactical policy: BLOCKING for recover-object-first, protect-evidence, rescue-first, preserve-site, objective-aware withdrawal and disengage-after-objective unless separately implemented.

Minecraft/Cobblemon/Craftics adapter/playback: PARTIAL/BLOCKING for stable objective-object identity, pickup/return acknowledgement, environmental objective state and authoritative non-KO completion.

## Engine evidence boundary

AutoPTU-Java head `cf1e19c2ffb07ebd044d1d36348e88a67d5e413e` strengthens the specific authoritative switch transaction ordering seam. It does not justify treating switching, movement, lifecycle, Abilities or Trainer Features as complete categories.

AutoPTU Python head `729bae2d424963ff9bb3f4159c9a7ac9152128a7` contributes no new tactical evidence in this pass.

## Unresolved canon questions

The posting institution, object type, four sites, participants, environmental discrepancy, ownership/custody authority, archival destination, reward structure and any connection to a larger regional pattern remain undecided.

No species encounter is canonized by this proposal.
