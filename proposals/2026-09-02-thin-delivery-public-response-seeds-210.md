# Pass 210 Ouros Candidates — Thin Delivery public response and correction loop

Status: PROPOSED / NON-CANON
Date: 2026-09-02

This proposal extends the canon-approved Marea Interior foundation and the pass-208 Thin Delivery evidence web. It does not establish a cause for Thin Delivery Season, create a new authority, promote a hypothesis to fact or rewrite any existing NPC.

## Continuity boundary

Canon inputs preserved:

- Thin Delivery Season remains unresolved.
- Ivo Serrat sees market purchasing/receipt irregularities.
- Brin Havel owns cooperative intake/dispatch records within his role.
- Lia Morn owns arrival/departure evidence within dock coordination.
- Nerea Sol and Ema Rey own dated Mirador observations within their work.
- Taro Min preserves historical comparison and contradictory testimony.
- Mara Veyra coordinates field response without police powers or omniscience.
- Alba Ríos can speak directly only for her own holding.
- the lower-Sendero Fletchling and all named companion Pokémon retain their existing identities and are not assigned blame or special knowledge.
- a battle can change immediate safety or access, but cannot prove why deliveries changed.

## Candidate episode cluster: Before the Explanation Hardens

Suggested questline linkage:

- parent arc: `ouros.arc.thin_delivery_season`
- parent candidate: `ouros.marea.thin_delivery.missing_middle`
- types: REGION, SETTLEMENT, FACTION, CLASS, CHARACTER

Premise:

The evidence web has begun producing partial answers. Different residents now have enough information to act, but not enough to close the regional question. The playable problem becomes preventing one incomplete interpretation from hardening into the district's assumed explanation while still allowing people to make practical decisions.

The player does not choose “the true faction.” The player can help actors verify, qualify, publish, correct, defer or act within their mandates.

## Episode A — The Market Board Gets Ahead of the Record

Status: PROPOSED

Location: Bruma Market Hall.

Actors: Ivo Serrat; ordinary vendors as ambient audience only.

Trigger candidate:

- player has at least one evidence ref from the pass-208 web;
- the final Thin Delivery cause remains unresolved.

Situation:

A practical market notice is being prepared because vendors need to plan substitutions and purchases. One draft explanation overstates what the current evidence can support. The exact overstatement must be authored from live evidence; this proposal does not freeze which hypothesis it favors.

Player-facing actions that require no invented mechanics:

- inspect the draft notice and its cited evidence refs;
- point Ivo toward an existing contradictory or qualifying record already known to the player;
- ask that the notice state uncertainty explicitly;
- allow the draft to be posted unchanged;
- decline involvement.

Possible persistent outputs:

```text
ouros.arc.thin_delivery_season.public_claim_refs[]
ouros.arc.thin_delivery_season.publication_refs[]
ouros.arc.thin_delivery_season.response_thread_refs[]
```

Posting a notice creates a publication record. It never writes `thin_delivery_season.cause`.

## Episode B — Verification Has a Cost

Status: PROPOSED

Locations: Marea Field Office, Sendero del Vidrio, Estación Mirador.

Actors: Mara Veyra, Nerea Sol or Ema Rey depending on current schedules and evidence ownership.

Premise:

A public claim creates demand for verification. Mara can schedule a field check, Nerea can compare observation windows, or the player can pursue another existing evidence lane. Choosing one consumes authored world time or staff availability only if those systems already support such state; this proposal does not invent action points or timers.

Useful consequences:

- a new direct observation supports part of the public statement;
- a new observation contradicts part of it;
- conditions have changed, so the earlier claim becomes stale rather than simply wrong;
- verification cannot be completed safely and the claim remains unresolved;
- another evidence lane becomes more valuable than another field visit.

No failed check may fabricate evidence. A mechanically governed Skill check, if later added, controls access, interpretation, speed or quality only according to verified PTU/Kairos rules.

## Episode C — Correction Without Erasure

Status: PROPOSED

Locations: Bruma Market Hall, Tideglass Archive, or another already-supported publication surface.

Actors: Ivo and Taro are the strongest first anchors because Ivo has operational reason to issue the notice while Taro has a canon role preserving editions and contradictory testimony.

Premise:

A later evidence record materially changes how an earlier notice should be understood.

The correction creates a new record linked to the old one. The earlier publication remains historically visible.

Candidate state transition:

```text
claim A: ACTIVE -> REVISED or DISPUTED
publication A: remains immutable historical artifact
claim B: ACTIVE, supersedes claim A
public-memory event: audience can encounter both versions according to actual channel/history state
```

This preserves the distinction between “people once believed this,” “an institution once said this,” and “this is canonically true.”

## Episode D — Different Mandates, Same Evidence

Status: PROPOSED

The same evidence may rationally produce different actions:

- Ivo changes purchasing or substitution plans because his concern is meal continuity.
- Mara requests route verification because her concern is field safety/service continuity.
- Nerea requests more observations because her concern is evidentiary quality.
- Brin reviews a tracked lot because his concern is cooperative custody and dispatch.
- Lia checks arrival records because her concern is actual movement through the dock/transfer system.
- Taro preserves both versions because his concern is future historical usability.

These differences should create cross-edges in one world graph, not separate duplicated quests.

No response is automatically rewarded with a generic reputation score. Persistent history should record concrete cooperation, disagreement, fulfilled requests, ignored warnings and corrected statements where authored.

## Candidate response thread examples

Status: PROPOSED

```yaml
response_thread:
  response_thread_id: ouros.marea.thin_delivery.response.market_substitution_01
  subject_world_arc_id: ouros.arc.thin_delivery_season
  actor_or_faction_id: ouros.npc.ivo_serrat
  triggering_claim_refs: []
  evidence_refs_considered: []
  current_action_state: VERIFYING
  next_action_candidates:
    - qualify_market_notice
    - request_specific_lot_check
    - publish_operational_notice_without_causal_claim
  revision_conditions: []
```

```yaml
response_thread:
  response_thread_id: ouros.marea.thin_delivery.response.field_verification_01
  subject_world_arc_id: ouros.arc.thin_delivery_season
  actor_or_faction_id: ouros.faction.marea_field_office
  triggering_claim_refs: []
  evidence_refs_considered: []
  current_action_state: WATCHING
  next_action_candidates:
    - schedule_existing_route_check
    - request_mirador_comparison
    - no_action_when_claim_outside_mandate
  revision_conditions: []
```

IDs are candidates only.

## Mechanically rich encounter candidate — Keep the Record Moving

Status: PROPOSED / FULL VERSION BLOCKED

Narrative premise:

A time-sensitive verification packet or field observation must reach the next evidence owner while a localized encounter or environmental condition complicates travel. The objective is delivery/withdrawal/safe passage, not defeating every opponent.

The encounter may only instantiate if current world ecology or another authored actor state supports it. It cannot spawn hostility merely because a tactical scene is desired.

Full-version semantic objectives may include:

- carry an evidence packet or maintain custody of an authenticated record;
- move between defined route anchors;
- protect an allied recorder or courier if escort contracts are supported;
- disengage through a safe boundary;
- choose between preserving the packet, assisting another actor, or continuing the route when the authored situation makes those goals genuinely incompatible;
- allow a verified noncombat or social action to change an actor's participation when governing mechanics permit it.

Required capability families:

- targeting/footprints/range/LoS;
- base movement legality;
- complete movement including push/pull/knockback/interception/forced movement when displacement or interception is authored;
- core calculations;
- action economy/initiative;
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle when selected participants/actions can create statuses;
- terrain/weather/hazards/zones/reactions when route conditions have tactical effects;
- move-specific behavior;
- abilities;
- items when the packet/tool is mechanically targetable or a held/usable item matters;
- Trainer Features/perks when Orders, interrupts, social Features or tactical Features are invoked;
- AI legal-action infrastructure;
- AI tactical policy for objective-aware allies/opponents;
- Minecraft/Cobblemon/Craftics adapter/playback support.

The evidence packet remains a semantic world object unless the battle engine has an audited object/objective contract. Minecraft item pickup or entity death must not decide evidence custody by itself.

## Reduced implementation — Publish, Verify, Correct

Status: PROPOSED / IMPLEMENTATION-CANDIDATE

The narrative premise survives without tactical richness:

1. create an attributed draft claim from already-existing evidence refs;
2. let the player inspect the cited support and known contradiction/qualification refs;
3. record the authored choice to publish, qualify, defer or request verification;
4. use ordinary world navigation to visit an existing evidence owner;
5. create a new observation or retrieve an existing record only through current authoritative world-state services;
6. issue a versioned correction or leave the earlier statement active;
7. persist both the publication history and concrete institutional response;
8. if an ordinary wild battle occurs independently through existing ecology, resolve it through the normal audited battle path and keep its output separate from the truth of the claim.

This reduced version requires no tactical terrain, forced movement, reaction, objective-aware AI, custom item custody or Trainer interrupt. Minecraft can render notice boards, dialogue, NPC movement and route travel while Ouros remains authority for claims and world state.

## Optional ordinary-battle branch

Status: PROPOSED / STRICTLY BOUNDED

If current ecology exposes the existing lower-Sendero Fletchling or a future canon-approved wild encounter during verification, the player may observe, disengage or battle according to the encounter's own contract.

Allowed world consequences can include immediate encounter resolution and any explicitly audited battle/capture output.

Forbidden inference:

```text
FLETCHLING_DEFEATED -> ROUTE_CAUSED_DELIVERY_SHORTFALL
FLETCHLING_CAPTURED -> CLAIM_CONFIRMED
BATTLE_WON -> PUBLIC_ARGUMENT_WON
```

None of those writes are permitted.

## Character pressure without hidden morality math

Status: PROPOSED

The episode can create meaningful NPC history without a generic good/bad choice:

- Ivo can remember that the player helped preserve operational usefulness while qualifying uncertainty.
- Nerea can remember whether the player cited evidence accurately.
- Taro can preserve which edition the player encountered and whether they later returned with a correction.
- Mara can remember whether the player respected a safety/verification boundary.

These are authored event histories. They do not imply friendship, trust, romance, hostility or mechanical social bonuses unless later canon explicitly establishes such effects.

## Failure and transformation

The cluster should continue if the player makes a poor informational choice.

Possible transformations:

- an overstated notice causes residents to ask the wrong follow-up question, creating a correction episode;
- a cautious notice delays action but preserves uncertainty;
- a verification attempt returns stale or inconclusive data;
- two institutions act differently from the same evidence without either becoming an antagonist;
- a later world fact confirms one part of an earlier claim while disproving another;
- the arc moves on before everyone has received the correction, leaving legitimate historical disagreement in public memory.

No branch silently determines the unresolved root cause.

## Canon questions left open

- Which exact first public statement is authored, and which current evidence refs it cites.
- Whether Bruma Market Hall already has a canonical physical notice surface or needs one added by explicit canon/implementation work.
- Which publication channels are available in the first playable slice.
- Which actors can author, approve or physically post notices within existing institutional mandates.
- What world-state service owns claim/publication versioning.
- Whether audience knowledge is tracked individually, by bounded cohort, or through another explicit model.
- What PTU/Kairos Skills/Features can mechanically affect persuasion, verification, interpretation or communication under the production rules profile.
- Which result contracts, if any, allow a noncombat intervention to change a battle participant's intent without narrative code bypassing AutoPTU.

Until review, every addition in this file remains proposed and non-canon.