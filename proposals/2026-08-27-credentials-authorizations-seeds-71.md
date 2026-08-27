# Ouros Credentials & Authorizations Seeds — Pass 71

Status: PROPOSED / NON-CANON.

These candidates use the Pass 71 credential lifecycle. They do not establish a universal Trainer license, government ID, passport, professional licensing system or legal code for Ouros.

## 1. The Badge That Still Scans

An old institutional access token still verifies as physically authentic, but the underlying authorization was superseded months ago.

Possible explanations:
- replacement completed but old token never recovered;
- local reader cache is stale;
- actor never received the replacement notice;
- token was found after being reported lost;
- institution changed scope without changing the visual design.

Core play: provenance, communication history, verification and administrative repair.

No automatic fraud accusation.

## 2. Valid Elsewhere, Supervised Here

A visiting field worker presents a genuine completion credential from another institution. The host authenticates it but grants only supervised local access until a site-specific orientation is completed.

Useful consequences:
- creates a host contact;
- produces a short field-practice hook;
- avoids resetting an experienced NPC or PC to “unqualified”;
- preserves regional standards without inventing national borders.

## 3. The Temporary Scope That Expires Tomorrow

A research team’s authorization ends before the project does. The party can help finish documentation, arrange renewed supervision, reduce project scope or hand the work to another authorized team.

The clock comes from existing credential state, not random urgency.

## 4. Replacement Found in Lost Property

A credential reported missing was replaced. Weeks later, the original turns up at a found-property desk.

The physical item is authentic and historically important, but current access checks reject it as superseded.

This ties Pass 71 directly to Found Property without treating found possession as authority.

## 5. Emergency Access, Ordinary Morning

During a crisis, several workers received temporary expanded access. The crisis is now over, but some routines formed around that temporary scope.

The story is about unwinding emergency state:
- who returns keys/tokens/equipment;
- which access ends;
- which role changes require separate staffing decisions;
- which work remains unfinished;
- which shortcuts should not become permanent merely because they were useful.

## 6. The Public Credential Shows Less Than Everyone Thinks

A well-known competitor carries a public-facing credential. Residents assume it contains full battle history, current team and private ranking data. It does not.

The hook supports media/privacy stories and teaches the information boundary through world interaction rather than exposition.

## 7. Two Authentic Records, Different Scope

Two actors hold genuine credentials from the same institution. One permits archive reading-room access; the other permits supervised handling of a specific collection.

A staff member initially treats them as interchangeable because the visible cards look similar.

The correction creates procedural friction without requiring malice.

## 8. The Site Token Was Never the Qualification

A character loses the physical token used to enter a work site and believes the project is over. Verification reveals that the token was only a representation of an authorization stored elsewhere.

The institution issues a replacement after identity verification.

This gives Minecraft a visible item without making item loss erase character history.

## 9. The Credential That Outlived the Role

A former staff member still has a genuine professional completion credential but no longer holds the workplace role that once granted facility access.

The distinction matters when someone assumes the historical credential is equivalent to current employment.

No wrongdoing is required.

## 10. Orientation Completed, Access Still Pending

A visitor completes all requested orientation steps, but the host still has not finished the actual authorization decision because one dependency record is missing.

Potential outcomes:
- alternate evidence accepted;
- supervised provisional access;
- delay until verification;
- activity moved to a public-access location.

Completion of a prerequisite does not force approval.

## 11. The Superseded Format

An institution changes the physical format of its credentials. Older credentials remain valid until naturally replaced.

A local venue mistakenly rejects an older-looking but active credential.

The story becomes a recognition/verification problem, not a counterfeit plot.

## 12. The Access List and the Card Disagree

A physical card shows an actor as authorized, while the current registry does not.

Possible causes:
- registry sync delay;
- recent suspension;
- duplicate identity record;
- incorrect card printing;
- legitimate old scope that never included this site;
- administrative error.

The system should preserve both observations until resolved.

## Persistent arc: An Institution Learns Its Credentials

Visit 1: the institution uses a simple credential and manual verification process.

Visit 2: a lost representation reveals the difference between physical token and underlying authorization.

Visit 3: a visiting partner institution creates a recognition dispute.

Visit 4: a crisis causes temporary scopes to proliferate.

Visit 5: post-crisis review retires some temporary scopes and exposes ambiguous old records.

Visit 6: the institution revises its process. Old credentials remain in historical state and some NPCs still remember the earlier procedure.

The arc creates institutional memory without requiring corruption or a giant conspiracy.

## Mystery: Five Credentials, Four Current Records

Premise:

Five physical credential representations appear genuine. The issuer registry has four current credentials for those actors.

Investigation tracks:
- serial or instance history;
- replacement events;
- lost-property reports;
- issued timestamps;
- public projections;
- role changes;
- recognition events;
- notification delivery.

Possible resolutions:
- one token was replaced and later recovered;
- one actor has two representations of one underlying authorization;
- one old credential is genuine but superseded;
- registry migration missed an archived record;
- evidence remains insufficient.

Do not force forgery as the answer.

## Encounter concept A — Restricted Facility Evacuation

Narrative premise:

An incident occurs inside a facility where some people have full access, some temporary access and some are visitors. Authorization controls who should have been in each area before the incident; it does not modify combat stats.

Full intended version:
- civilians move toward multiple exits;
- access-controlled doors change legal routes;
- responders may need PROTECT/CLEAR_ROUTE behavior;
- environmental hazards can close zones;
- hostile/wild AI may prefer escape or territorial defense over KO;
- post-battle playback preserves who was where and which doors were open.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement with push/pull/knockback/interception/forced movement: BLOCKING
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- full turn/round lifecycle: PARTIAL
- full stateful damage pipeline: PARTIAL
- status lifecycle: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move-specific behavior: PARTIAL
- abilities: PARTIAL
- items: PARTIAL
- Trainer Features/perks: PARTIAL, exact-feature dependent
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- Minecraft/Cobblemon/Craftics adapter/playback: BLOCKING

Reduced executable version:

World state resolves authorization, door access and civilian evacuation before battle. All noncombatants are removed. AutoPTU receives a static legal room/corridor arena. After authoritative battle resolution, facility and credential systems decide reopening and access review separately.

## Encounter concept B — Field Authorization Interrupted

Narrative premise:

A temporarily authorized survey team encounters territorial wild Pokémon while documenting a site.

Full intended version:
- current terrain/weather can matter;
- retreat routes remain important;
- interception/forced movement may threaten withdrawal;
- wild AI can protect territory rather than seek KO;
- protected zones remain mechanically meaningful;
- exact authorization state is visible in playback but grants no combat bonus.

Capability dependencies:
- targeting/footprints/range/LoS: VERIFIED
- base movement legality: VERIFIED
- complete movement: BLOCKING when interception/forced movement matters
- core calculations: VERIFIED
- action economy/initiative: VERIFIED
- lifecycle: PARTIAL
- damage/status: PARTIAL
- terrain/weather/hazards/zones/reactions: BLOCKING
- move behavior/abilities/items/Trainer Features: PARTIAL per exact content
- AI legal-action infrastructure: VERIFIED
- AI tactical policy: BLOCKING
- adapter/playback: BLOCKING

Reduced executable version:

Survey and authorization remain overworld state. If a battle is unavoidable, participants enter a static reviewed arena using supported mechanics. The authoritative result may alter site safety or project timing, but cannot broaden or renew anyone’s authorization.

## Noncombat scene — Recognition Desk Review

A visiting actor asks a host institution to recognize an external credential. Gameplay uses records, provenance, source contacts, public publications and optional supervised demonstration.

Possible outcomes:
- full recognition;
- limited local scope;
- provisional recognition;
- additional orientation;
- alternative evidence accepted;
- not sufficient for this activity;
- verification still pending.

No combat implementation dependency is required.

## Canon blockers

Before any candidate can be promoted, Ouros must establish the relevant issuer, scope, institution, technology, privacy rules and recognition policy. None of these seeds decides those questions.
