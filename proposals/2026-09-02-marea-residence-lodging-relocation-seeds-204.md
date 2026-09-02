# Marea Residence, Lodging and Relocation Seeds — Pass 204

Status: PROPOSED / NON-CANON
Date: 2026-09-02

All entries below reuse current Marea people, places and institutions where possible. None establishes rent, property ownership, leases, family relationships, housing law or PTU rest effects.

## 1. Room Assigned, Room Empty

Recommended first implementation slice.

Mara's canonical boarding room near the Field Office remains assigned while she spends an afternoon on route review. A routine document or small non-mechanical delivery reaches the boarding row first.

The player can:
- leave it through an already authorized handoff route;
- find Mara at her workplace;
- return later after her schedule changes.

The room being empty never means Mara moved out. Minecraft unload never ends the record.

Dependencies: no battle. Existing identity, schedule, information-delivery and residence continuity only.

## 2. Nerea's Work Quarters Are Not Mirador Ownership

A visitor sees that Nerea has quarters at Estación Mirador and casually describes the station as "her place." Tideglass preserves the wording as a statement but Mirador records retain only that she has institutional quarters and works there.

Purpose: teach `RESIDENCE_AT_INSTITUTION != OWNERSHIP_OF_INSTITUTION` through ordinary conversation.

Dependencies: no battle.

## 3. Taro's Archive Room and the Late Interview

One of Taro's evening interview sessions runs later than expected. Pia needs to deliver a document after public archive hours.

The problem is not solved by assuming access to Taro's residence room. A valid work handoff or later delivery remains available.

Purpose: separate professional access from residential privacy.

Dependencies: identity/access and information delivery; no new authority rule.

## 4. The Boarding Row Directory Is Stale

A small public directory still points to a room assignment that ended or changed through an authored event. The underlying residence record and the displayed directory version diverge.

Pia can trace the update provenance and correct the public copy without rewriting the historical version.

Purpose: integrate pass 200 information circulation with residential continuity.

Dependencies: no battle.

## 5. One Night Near the Dock

A legitimate late ferry operation leaves an existing worker or visitor with temporary accommodation close to the landing rather than their ordinary residence.

The temporary record has a start, expected end and purpose. It does not replace the person's primary home.

Purpose: demonstrate simultaneous ordinary and temporary accommodation.

Dependencies: ferry/service continuity. No price or labor rule is invented.

## 6. Teo's Repair Makes a Room Temporarily Unusable

An ordinary non-structural fixture problem in a boarding room requires Teo's attention. A separately authored assessment establishes that the room cannot be used for a limited period.

A temporary room can be assigned through existing service/capacity state. When the repair closes, returning to the original room is a separate residential event.

Purpose: connect repair/service state to residence without letting repair completion silently move a person.

Dependencies: service request; no mechanical crafting effect.

## 7. Forwarded to the Old Address

A notice or parcel addressed to a resident reaches their previous lodging after an explicit move. The old location's current custodian does not automatically know where the person moved.

A forwarding reference can exist only if the world established one.

Purpose: make relocation leave information consequences.

Dependencies: information/custody continuity. No postal law.

## 8. Pia's Temporary Archive Stay

A bounded archive project may justify temporary accommodation close to Tideglass for an existing actor. The record contains purpose and end condition.

The stay never creates family relation with Taro, permanent archive membership, ownership or a change to the actor's ordinary residence.

Purpose: reinforce current canon's explicit boundary around the Min surname and professional mentorship.

Dependencies: existing identities only.

## 9. Jace Leaves Equipment at the Yard, Not at Home

A piece of ordinary personal training equipment is stored at Bruma Battle Yard while Jace lives elsewhere in Puerto Bruma.

Its physical location cannot be used to infer residence. If it is moved, material custody history changes without changing Jace's home.

Purpose: separate personal effects from residency inference.

Dependencies: item/custody continuity; no battle required.

## 10. Temporary Displacement after a Verified Route Event

A separately established event interrupts access for a specific actor returning to their ordinary residence or destination. Marea Field Office coordinates a temporary safe lodging option through existing world capacity.

The event records who stayed where and for how long. It does not create a generic refugee mechanic, housing entitlement or permanent relocation.

Purpose: connect crisis/route state to lived consequences at small scale.

Dependencies: crisis/service/residence state. No battle necessary.

## 11. The Guest Who Keeps Returning

A recurring visitor receives separate temporary lodging records across multiple visits. Staff recognize the person through persistent identity/history, but each stay has its own access window.

An old room assignment cannot be reused merely because the visitor has stayed before.

Purpose: combine visitor continuity with pass 201 identity/access boundaries.

Dependencies: no battle.

## 12. Moving the Boxes Is Not Moving the Person

During a planned relocation, a bounded group of ordinary belongings arrives before the resident. The destination room may contain the person's effects while their residence record remains `PREPARING` or `IN_TRANSIT`.

Purpose: prove `PERSONAL_EFFECT_PRESENT != PERSON_CURRENTLY_PRESENT` and `POSSESSIONS_ARRIVED != MOVE_COMPLETED`.

Dependencies: custody/transport continuity.

## 13. What the Old Room Remembers

After an explicit future relocation, an old room retains authored physical traces such as a repaired fixture, archived room record or public-memory reference. The scene can acknowledge continuity without assigning nostalgia, regret or attachment to the former resident.

Purpose: make place history persistent without forcing private emotion.

Dependencies: public memory and environment persistence.

## Longer arc — Addresses Change, Histories Do Not

A slow settlement arc tracks small residential changes across Marea:
- temporary work quarters;
- rooms unavailable for repair;
- visitors returning;
- explicit moves;
- stale directories;
- forwarded notices;
- old rooms receiving new occupants;
- physical improvements that persist across occupants.

The payoff is a district whose residential geography accumulates history. No universal housing market, rent system or legal regime is required.

The arc should eventually allow a resident to move because of an authored Character, Settlement or Faction development. The relocation must be an actual state transition with provenance rather than an NPC teleport caused by changing Minecraft coordinates.

## Mechanically rich encounter — Return Route to the Boarding Row

Premise:
A resident is temporarily lodged in Puerto Bruma after a separately established disruption. They need to recover a bounded piece of field equipment from an accessible prior site. A localized wild confrontation blocks immediate withdrawal on Sendero del Vidrio.

### Full version

Requires the permanent capability families as follows:
- targeting/footprints/range/LoS — required;
- base movement legality — required;
- complete movement including push/pull/knockback/interception/forced movement — required if protected withdrawal or displacement matters;
- core calculations — required;
- action economy/initiative — required;
- full turn/round lifecycle — required for sustained objective handling;
- full stateful damage pipeline — required;
- status lifecycle — required when selected content uses statuses;
- terrain/weather/hazards/zones/reactions — required if route conditions become tactical;
- move-specific behavior — required;
- abilities — required for selected actors;
- items — required if battle Items participate;
- Trainer Features/perks — required if selected Trainers use them;
- AI legal-action infrastructure — required;
- AI tactical policy — required for objective-aware withdrawal/territorial behavior;
- Minecraft/Cobblemon/Craftics adapter/playback support — required for faithful world/battle/world projection.

Disposition: FULL VERSION BLOCKED under pass-204 evidence.

### Reduced version

Narrative establishes residence, temporary lodging, equipment custody, purpose and noncombatant safety first. AutoPTU then receives one ordinary audited battle on stable geometry against the specific actor preventing withdrawal.

Allowed outputs:
- `IMMEDIATE_RECOVERY_ROUTE_CLEAR`
- `IMMEDIATE_ROUTE_THREAT_WITHDREW`
- `IMMEDIATE_RESIDENT_CAN_WITHDRAW`

Battle cannot decide residence, ownership, payment, household membership, relocation motive, future lodging, address validity, relationship change or PTU rest/healing.

## Canon questions deliberately left open

- Who owns or operates Puerto Bruma boarding rooms?
- Are Mara's quarters paid, assigned through work or obtained another way?
- What exact homes do secondary residents occupy?
- Can multiple actors formally share a room or household, and under what local rules?
- What residential access practices exist after hours?
- What Caelo rules govern property, tenancy, guardianship or lodging?
- Do any PTU/Caelo mechanics attach benefits or costs to accommodation quality?
- How should player housing eventually work, if it exists at all?

No seed answers these questions by implication.