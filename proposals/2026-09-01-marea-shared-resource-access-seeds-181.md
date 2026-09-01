# Marea shared-resource access candidates — pass 181

Status: PROPOSAL / NON-CANON
Date: 2026-09-01
Canon impact: NONE. These seeds do not establish protected species, property law, capture restrictions, harvesting rights, permits, quotas or new institutions.

These candidates reuse existing Marea places and residents. They are designed to add world continuity through access conditions, observation windows, custody and policy revision rather than by introducing another quest island.

## 1. The Observation-Only Morning

Nerea proposes a short observation window on one existing Mirador transect segment after an unusual pattern appears in recent notes. The candidate rule is entry for observation and instrument checks only; no specimen removal or capture authorization is implied.

Participants: Nerea, Ema, Mara, Pia.

Gameplay: receive scoped field instructions, visit marked stations, record comparable observations, return notes. The published notice can later be revised when the evidence window closes.

Implementation value: high. Uses existing Mirador, evidence, document and quest-object surfaces with no battle requirement.

## 2. One Sample Too Many

Ema discovers that two sample containers were prepared for a collection authorization that, according to the copied instruction, allowed only one. The discrepancy may be a preparation mistake, an outdated copy or a changed decision.

Participants: Ema, Nerea, Pia, Taro.

Gameplay: compare the authorization version, container labels, courier copy and archive record before anything is removed from the site.

Outcome branches: second container cancelled; authorization corrected; collection postponed; discrepancy unresolved pending issuer review.

No ecological conclusion is inferred from the paperwork mismatch.

## 3. The Crossing Notice Arrived Late

Mara issues a proposed temporary restriction for one segment near the seasonal crossing. Lia receives the update promptly, while a copied notice near another service point remains stale.

Participants: Mara, Lia, Pia, Mina.

Gameplay: identify which notice is current, replace the stale projection, record who received the correction and preserve the old notice version in communications history.

The closure itself remains proposed until canon defines who has authority to issue it.

## 4. Brin's Returnable Crates

A cooperative shipment uses containers that are supposed to return to Loma Clara. Market activity makes the empty crates look like abandoned free inventory.

Participants: Brin, Ivo, Lia.

Gameplay: identify custody markings, separate reusable cooperative property from ordinary packaging, route empties back through the ferry/road logistics chain and correct a mistaken inventory count.

This seed tests shared-use objects without creating land or wildlife law.

## 5. The Edge Plot Question

Alba and Jo notice repeated gathering activity along the edge of a cultivated/uncultivated boundary. The current canon does not say who may collect there or whether the material is cultivated, wild, communal or privately managed.

Participants: Alba, Jo, Mara, Brin.

Gameplay: gather maps, cultivation records and local statements. Valid conclusion may be `AUTHORITY_UNRESOLVED` rather than inventing a right.

Canon purpose: exposes exactly which land-use facts must be decided before adding harvest gameplay.

## 6. The Permit That Expired During the Delay

A hypothetical field authorization expires while weather or transport prevents the holder from reaching the site. The player must return to the issuer rather than assuming the old item remains valid.

Participants: Nerea or Mara as candidate issuer depending future canon; Mina as transport witness; Pia as document courier.

Gameplay: validate date/window, request extension or accept rescheduling, preserve both versions.

This is a clean test of `PERMIT_ITEM_PRESENT != PERMIT_CURRENTLY_VALID`.

## 7. Observation Board Without Promise

Mirador posts a board showing recent detections or expected observation windows based on the phenology ledger. Players repeatedly misread it as a guaranteed encounter board.

Participants: Nerea, Ema, Taro.

Gameplay: compare forecast/evidence status, visit one field point, record non-detection correctly, update explanatory text if needed.

Invariant: `REPORTED_PRESENT != GUARANTEED_PRESENT`.

## 8. The Ferry Shoreline Work Window

Teo needs access to a small section near the ferry landing for maintenance while Lia needs the same space kept clear for safe loading. A temporary work window must be scheduled rather than one actor simply taking precedence.

Participants: Lia, Mina, Teo, Mara.

Gameplay: inspect schedules, choose a bounded maintenance slot, place/remove presentation barriers and record completion.

No battle requirement. Good candidate for visible server-calendar integration.

## 9. Return What Was Logged

A research or maintenance object removed from Mirador reaches Puerto Bruma but its custody record still shows it at the station.

Participants: Ema, Teo, Pia, Taro.

Gameplay: trace transport, distinguish movement from ownership, update custody after physical confirmation and return/redeposit the object.

This reuses archive/custody architecture and prevents sample collection from becoming ordinary loot.

## 10. Closure Line Breach

A proposed full tactical scenario. During an active wildlife passage, a route segment is under temporary restriction. Unauthorized entrants move beyond the marked line at the same time a hostile or panicked Pokémon encounter develops.

Narrative purpose: protect people and keep the corridor clear while preserving uncertainty about the wildlife event's cause.

Full version dependency classification:

- targeting/footprints/range/LoS: required; currently verified for covered contracts, exact participants still need audit;
- base movement legality: required; verified for covered contracts;
- complete movement including push/pull/knockback/interception/forced movement: required if the scenario permits interception, shoves, displacement or corridor blocking; currently partial and blocking for those rich interactions;
- core calculations: required; verified for covered contracts;
- action economy/initiative: required; verified for covered contracts;
- full turn/round lifecycle: required; partial;
- full stateful damage pipeline: required; partial;
- status lifecycle: conditional on selected content; partial;
- terrain/weather/hazards/zones/reactions: required for an active protected corridor/hazard version; blocking;
- move-specific behavior: exact roster audit required; partial;
- abilities: exact roster audit required; partial;
- items: exact roster audit required; partial;
- Trainer Features/perks: exact roster audit required; partial;
- AI legal-action infrastructure: required; verified for covered contracts;
- AI tactical policy: required if NPCs independently protect, retreat or maintain corridor goals; blocking;
- Minecraft/Cobblemon/Craftics adapter/playback support: blocking for faithful full tactical projection.

Reduced version:

The route restriction, wildlife passage and civilian positions remain world state outside BattleSpec. The player warns or escorts entrants back to the safe boundary using ordinary Minecraft movement and dialogue. If a battle is still necessary, it occurs on a separate stable clearing after civilians are removed. Only an audited roster is compiled. The battle may emit `IMMEDIATE_THREAT_WITHDREW` or `IMMEDIATE_CLEARING_SECURED`. It cannot lift the restriction, prove the corridor safe, authorize capture, establish population status or explain the wildlife movement.

## 11. A Limit Without a Population Claim

A future institution considers a conservative temporary collection limit because evidence quality is low. The gameplay focus is reviewing why the limit exists and when it expires, not proving an exact population.

Participants: Nerea, Mara, Taro, a future authorized decision-maker if canon creates one.

Invariant: `QUOTA_POLICY != TRUE_POPULATION_COUNT`.

This seed stays dormant until Marea has a canon authority capable of making such a policy.

## 12. The Boundary Marker Drift

An old route or work-area marker no longer matches newer survey references. Moving it casually could change perceived access boundaries even if no formal boundary changed.

Participants: Mara, Teo, Taro, Ema.

Gameplay: compare survey record, physical marker, repair history and current coordinates; preserve uncertainty until an authorized correction exists.

Minecraft rule: block position alone cannot create or revise jurisdiction.

## Recommended implementation order

First: The Ferry Shoreline Work Window. It is physical, visible, calendar-friendly, connected to four existing residents and mechanically simple.

Second: The Observation-Only Morning. It strengthens Mirador's research identity and the phenology/evidence systems without requiring new species canon.

Third: One Sample Too Many. It stress-tests document versioning and custody before resource extraction is allowed anywhere.

Closure Line Breach should remain reduced until the exact battle capability families are verified.

## Canon questions exposed by these seeds

Which Marea role can restrict access to a route segment?
Can Mirador authorize specimen collection, or only request it?
Who owns/maintains reusable cooperative containers?
What are the formal boundaries between Loma cultivation and uncultivated land?
Can the ferry landing temporarily reserve shoreline/work space?
Does Caelo define protected wildlife, capture licensing, preserves or customary use rights?

No seed should answer these questions silently.