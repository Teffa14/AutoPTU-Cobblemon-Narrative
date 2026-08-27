# Found Property, Custody & Restitution Scan — Pass 66

Status: research/provenance notes. Not Ouros canon.
Date: 2026-08-26

## Scope

This pass studies ordinary lost property, recovery, temporary custody, claimant verification and return as a source of persistent world stories.

The repository already has several adjacent systems, so the research target is deliberately narrow.

- `material-culture-economy-crafting-layer.md` owns significant physical item identity, provenance, owner/custodian references and transformation history.
- `case-authority-custody-layer.md` owns formal incidents, evidence custody and institution mandates when an object becomes evidence or suspected theft/crime is involved.
- `courier-parcel-last-mile-logistics-extension.md` owns intended shipments, delivery legs, delivery attempts, redirects, lost shipments and recovery inside a delivery chain.
- `libraries-publications-editions-circulation-extension.md` owns circulation state for significant copies.
- `residential-life-household-relocation-layer.md`, transit, events and storefront systems own the places/routines that can explain where an object was lost or later found.

The uncovered design gap is the ordinary object that becomes separated from its holder outside an intended shipment and before any formal case exists.

## New-source duplicate check

Repository code search found no prior use of:

- Kofu / Kofu's Wallet;
- Lost Satchel;
- Pokémon Unbound's Lost Hanky mission.

These sources therefore add a new reference family rather than repeating a prior scan.

## Source 1 — Pokémon Scarlet and Violet: Kofu's Wallet

Sources:

- Bulbapedia walkthrough, Scarlet/Violet Part 12: https://bulbapedia.bulbagarden.net/wiki/Walkthrough:Pok%C3%A9mon_Scarlet_and_Violet/Part_12
- Kofu's Wallet: https://bulbapedia.bulbagarden.net/wiki/Kofu%27s_Wallet

Observed high-level structure:

Kofu leaves a personal wallet behind when he departs Cascarrafa. A Gym staff member notices the mistake, explicitly entrusts the wallet to the player and directs the player toward Kofu's current destination. The player carries the exact object across locations and returns it before the next part of Kofu's activity continues.

Reusable design lessons:

1. A mundane personal object can redirect travel without needing a villain, mystery conspiracy or combat.
2. The person who notices the object does not become its owner; they become a temporary custodian and can explicitly hand custody onward.
3. The object's return can intersect with an institution's schedule. This makes everyday continuity visible without treating the object itself as mechanically powerful.
4. A current location can differ from the owner's normal workplace, creating a small pursuit/search problem using existing world schedules.
5. Explicit entrustment is stronger than proximity. The player should know why they may carry the object.

Transformation for Ouros:

Do not copy the wallet, Gym Leader, auction or route. Use the custody pattern: a named person leaves a meaningful but ordinary object behind; a credible finder records the recovery; a temporary custodian must locate the holder using current world state; return creates a callback later.

## Source 2 — Pokémon Legends: Arceus: Lost Satchels / Lost & Found

Sources:

- Bulbapedia Lost Satchel: https://bulbapedia.bulbagarden.net/wiki/Lost_Satchel
- Nintendo update/support material confirming the Lost Satchel feature: https://www.nintendo.com/au/support/articles/how-to-update-pokemon-legends-arceus/

Observed high-level structure:

When a player loses items after blacking out, a distinct lost satchel can be recovered by another player. Returning that lost property restores the contents to the original player's storage, while the finder receives a separate reward.

Reusable design lessons:

1. Recovery and reward can be separated from ownership. The finder can benefit without acquiring the recovered contents.
2. A lost bundle can have exact identity and a known origin event.
3. Recovery can happen asynchronously and after the original holder has left the location.
4. The return can be mediated by a system rather than requiring both actors to stand in the same room.
5. The recovered bundle should remain linked to the original loss event so that duplication and accidental reassignment are impossible.

Transformation for Ouros:

Ouros can use an ordinary `find_event` plus a holding desk, institution or approved proxy where canon supports one. The system should remember the loss event, current custodian and restitution outcome. It should never infer that the finder owns the contents because Minecraft put the prop in their inventory.

## Source 3 — Pokémon Mystery Dungeon: item jobs

Source:

- Bulbapedia Job (Mystery Dungeon): https://bulbapedia.bulbagarden.net/wiki/Job_(Mystery_Dungeon)

Observed high-level structure:

Mystery Dungeon mission grammar distinguishes jobs that ask the team to find a specified item from jobs that ask the team to bring an item to a client.

Reusable design lessons:

1. Locating an object and transferring it to a claimant are separate stages.
2. A mission can remain object-centered rather than becoming combat-centered.
3. Retrieval can be completed through exploration, route knowledge and search rather than a mandatory boss fight.
4. The return stage can produce its own social consequence even after the search itself is finished.

Transformation for Ouros:

Model `recovery` and `restitution` independently. Finding the object should not automatically resolve the owner's claim, and verifying the claimant should not imply the object has physically reached them.

## Source 4 — Pokémon Unbound: Lost Hanky

Source:

- Pokémon Unbound Wiki, Mission #037: https://unboundwiki.com/missions/mission-037/

Observed high-level structure:

A handkerchief is found at Magnolia Cafe on one day, while its owner is associated with a different recurring day at the same location. The player must use the schedule to return when the likely owner is present.

Reusable design lessons:

1. A found object can encode a temporal clue rather than a spatial one.
2. A recurring public place can have different regulars across days/times.
3. The finder may need to wait for the world schedule instead of receiving an omniscient quest marker.
4. Reusing the same cafe at a different time makes the settlement feel persistent rather than generating a disposable quest location.

Transformation for Ouros:

Use existing calendar, routine and visitor systems. A recovery record can reference where and when an object was found; actor schedules may narrow plausible claimants. Schedule evidence is still not proof of ownership.

## Source 5 — Pokémon Reborn: missing furniture sidequest

Source:

- Pokémon Reborn community wiki: https://pokemon-reborn.fandom.com/wiki/Missing_Furniture_Sidequest

Observed high-level structure:

A set of missing household objects is distributed through an altered town. During the recovery, one returned object is explicitly acknowledged as probably not belonging to the original requester.

Reusable design lesson:

A multi-object recovery should allow mismatches. “It was found near the other missing things” cannot establish identity or ownership. A claimant may be mistaken, indifferent, opportunistic or simply operating with incomplete information.

Transformation for Ouros:

Do not reproduce the teleporting-furniture premise. Use the verification problem: a batch recovery can contain objects from several owners, so each significant item keeps its own provenance and claimant record.

## Community tabletop inspiration — recurring-town lost object

Source:

- r/PokemonTabletop thread on Mystery Dungeon tabletop hooks: https://www.reddit.com/r/PokemonTabletop/comments/10acj35

A community suggestion uses a small personally meaningful lost object to deepen a relationship with a recurring town service/NPC.

Usefulness:

The important pattern is scale. A minor possession can matter because of who made it, who gave it or the routine it anchors. The reward can be relationship/service continuity instead of item value.

Authority note:

This is community inspiration only. It supplies no PTU/Caelo rules and establishes no Ouros canon.

## Reusable narrative grammar

A robust found-property story can use this sequence:

1. `LOSS OR SEPARATION` — an object becomes separated from a holder, or someone reports it missing.
2. `RECOVERY` — another actor finds a physical object and creates a traceable find event.
3. `IDENTIFICATION` — the object is matched provisionally to a report or remains unattributed.
4. `HOLDING` — an actor/institution has custody while ownership/claim remains unresolved.
5. `CLAIM` — one or more actors assert a connection to the object.
6. `VERIFICATION` — claims are compared against nonpublic details, provenance, witnesses, records or other evidence.
7. `RESTITUTION` — the object reaches the verified holder or an authorized proxy.
8. `CALLBACK` — the recovered object can affect a later routine, relationship, service or memory without becoming a combat bonus.

Not every story needs every stage. The separation is valuable because it prevents “player picks up item -> quest flag says returned” shortcuts.

## Claim verification patterns

Useful evidence can include:

- description of a nonpublic mark, repair or contents;
- maker/commission record;
- prior photograph showing the exact object;
- witness to a prior handoff;
- known repair history;
- circulation or shipment record where relevant;
- a credible timeline connecting holder, location and loss;
- a matching unique serial/catalog/instance identifier if Ouros canon supports one.

Weak evidence can include:

- being physically near the find location;
- being the first person to ask;
- knowing a public description;
- matching a common color/model;
- saying “that's mine”;
- defeating a Pokémon near the object;
- possessing the object after finding it.

Ouros should not reduce this to a hidden numeric truth score. Evidence remains attributable and inspectable.

## Worldbuilding opportunities

Found property can make existing systems feel connected:

- a transit hub accumulates umbrellas, bags and tools from recurring passenger cohorts;
- a public event teardown produces a temporary holding backlog;
- a library discovers an insert that belongs to a reader rather than the book;
- a relocated household leaves an object at the former address;
- a workshop recognizes its own repair mark on a found item;
- a route worker finds a field notebook after an expedition has already moved on;
- a storefront keeps a small object behind the counter until its regular returns;
- an old object is found after a memorial/absence record has changed, requiring careful handoff rather than inheritance inference.

## Important boundaries

### Found does not mean owned

Possession created by a recovery event is custody until another governed rule says otherwise.

### Missing does not mean stolen

A loss report is a claim about absence. Theft requires independent evidence and, if formal handling is needed, a handoff to the Case/Authority layer.

### Returned does not mean ownership was legally adjudicated

Ouros currently has no universal legal/property code. A return record can say which actor received the object and why the handoff was authorized. It must not fabricate property law.

### An item prop is not an authority source

Minecraft inventory state, dropped-item state or container placement cannot silently rewrite narrative ownership, provenance or evidence custody.

### A battle result cannot prove a claimant

Winning a battle near a recovered item can make the area safe. It cannot authenticate a receipt, prove prior possession or determine who should receive the object.

## Encounter implications

Mechanically rich recovery scenes commonly tempt unsupported rules:

- an object treated as a protected combat objective;
- moving civilians/finder parties;
- pursuit or interception;
- knockback around fragile property;
- dynamic weather/terrain during a search;
- AI that prioritizes escape, protection or object access;
- synchronized Minecraft pickup/playback.

These must be mapped to the permanent capability categories instead of being simulated by narrative shortcuts.

A reduced version can usually preserve the premise by separating tactical safety from the noncombat recovery/claim process.

## Canon questions left open

This pass does not establish:

- whether Ouros has formal lost-and-found offices;
- which institutions accept found property;
- how long ordinary items are held;
- whether anonymous claims are allowed;
- what happens to unclaimed property;
- whether identity documents, serial systems, receipts or signatures are common;
- whether different settlements use different customs;
- whether finders receive rewards;
- who can authorize return to a proxy;
- whether any category of property requires mandatory escalation.

Those are setting decisions, not details to infer from real-world practice.

## Research conclusion

The strongest reusable insight is that lost property creates a small but powerful continuity loop: exact object identity, temporal/spatial provenance, temporary custody, a claim that can be wrong, and a visible return. It gives settlements reasons to remember earlier visits and makes ordinary routines matter without manufacturing a combat or world crisis.