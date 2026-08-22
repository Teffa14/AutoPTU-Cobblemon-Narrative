# Sacred Sites, Pilgrimage, Belief, and Practice Layer

Status: PROPOSED SYSTEMS DESIGN. NON-CANON unless a later canon document explicitly promotes specific places, traditions, institutions, or claims.

## Purpose

This layer gives Ouros a safe persistent model for sacred places, culturally significant journeys, custodianship, observances tied to place, supernatural claims, and long-term change.

It must preserve three separations:

1. a community can treat something as sacred without the system declaring its cosmology objectively true;
2. a supernatural event can be mechanically or canonically real without proving every interpretation built around it;
3. access, custody, belief, authority, and PTU mechanics are different systems.

## Core entities

### `SACRED_SITE`

Persistent identity for a place treated as sacred, spiritually significant, ritually important, or cosmologically meaningful by at least one authored community or institution.

Suggested fields:
- `sacred_site_id`
- `physical_location_id`
- `recognized_by`
- `recognition_basis`
- `first_attested_at`
- `current_status`
- `access_policy_ref`
- `custodian_refs`
- `associated_observance_refs`
- `associated_claim_refs`
- `artifact_refs`
- `archaeology_refs`
- `ecology_refs`
- `notes`

Sacred status does not create PTU Terrain, Weather, Aura, healing, spawn modifiers, or Legendary presence.

### `SACRED_SITE_REVISION`

Versioned physical/social state of the site.

Examples:
- functioning sanctuary;
- damaged but active;
- ruin still used by visitors;
- archaeological site with restricted ritual zone;
- rebuilt structure preserving older foundations;
- access suspended for ecological reasons;
- multiple communities maintaining different sections.

Never overwrite older revisions.

### `BELIEF_CLAIM`

Stores an attributed proposition about cosmology, sacred history, ritual efficacy, omen, taboo, origin, guardian, Legendary, spirit, or supernatural causation.

Fields:
- `claim_id`
- `proposition`
- `claimant_actor_or_group`
- `claim_type`
- `first_recorded_at`
- `evidence_refs`
- `counterclaim_refs`
- `public_visibility`
- `canon_truth_status`

`canon_truth_status` should normally be one of:
- `UNASSESSED`
- `CULTURAL_CLAIM_ONLY`
- `PARTIALLY_CORROBORATED`
- `CORROBORATED_EVENT_NOT_INTERPRETATION`
- `CANON_CONFIRMED`
- `CANON_REFUTED`

Most generated traditions remain `CULTURAL_CLAIM_ONLY` or `UNASSESSED`.

### `CUSTODIANSHIP_ROLE`

A role maintaining a site, practice, artifact, route, archive, or visitor relationship.

Custodianship can include:
- maintenance;
- access coordination;
- preservation of oral/history records;
- stewardship of objects;
- hosting visitors;
- scheduling observances;
- ecological protection;
- explaining known practice.

Custodian does not imply owner, government officer, clergy, combat authority, historian, scientist, or supernatural expert unless separately authored.

### `PILGRIMAGE_ROUTE`

A culturally meaningful route or sequence of stops.

Fields may include:
- route identity;
- origin/destination;
- customary stops;
- season/time windows;
- accessibility variants;
- historical revisions;
- transport options;
- current route condition;
- visitor pressure;
- optional practices at stops.

Completing a route does not automatically grant a reward, blessing, badge, Feature, reputation, or Legendary encounter.

### `PILGRIMAGE_JOURNEY`

One actor/group’s actual journey.

Records:
- participant consent;
- chosen route edition;
- stops reached;
- deviations;
- assistance received;
- accessibility accommodations;
- observations;
- artifacts carried or delivered;
- whether the journey was completed, paused, abandoned, or changed.

The system never infers belief from participation. A participant may travel for faith, family, scholarship, tourism, curiosity, obligation, escort duty, history, or reasons they choose not to disclose.

### `RITUAL_PRACTICE`

A documented practice associated with a place, date, object, community, or journey.

Keep separate:
- description;
- practitioners;
- participation rules;
- historical versions;
- required objects;
- access/consent;
- claimed meaning;
- confirmed physical effects;
- confirmed PTU effects.

Default confirmed PTU effects: none.

### `SACRED_OBJECT_RELATION`

Connects a persistent item/artifact to a site or practice without changing item mechanics.

Possible relations:
- displayed;
- carried on journey;
- deposited;
- loaned;
- replicated;
- recovered archaeologically;
- maintained by custodian;
- retired from use;
- missing;
- contested provenance.

### `OMEN_OR_ANOMALY_OBSERVATION`

Observation that participants interpret as meaningful.

Store separately:
- physical observation;
- observer;
- instrumentation if any;
- environmental conditions;
- Pokémon present;
- media record;
- interpretation;
- later corroboration.

Examples include unusual light, bells ringing, migration timing, weather coincidence, repeated Pokémon appearance, dreams, Aura readings, or genuinely anomalous events.

Nothing becomes supernatural truth at observation time.

## Relationships to existing layers

### Festivals / Observances

Festivals owns recurring public-event identity and editions.

This layer owns sacred meaning, place-linked practice, pilgrimage, and attributed cosmological claims.

A festival can include a sacred observance. A sacred observance can occur with no festival at all.

### Mythology / Public Memory / Archives

Mythology owns narrative traditions and mythic claims.

Archives owns documentary custody.

Public Memory owns what populations remember or believe publicly.

This layer links those records to particular sacred sites/practices without replacing them.

### Archaeology / Language

Archaeology owns physical excavation/context.

Language owns decipherment/translation.

A sacred inscription can therefore have:
- archaeological context;
- transcription;
- translation;
- religious interpretation;
- later scientific interpretation;
- disputed modern use.

None automatically overwrites the others.

### Conservation / Ecology

A sacred site can also be habitat.

Custodial practice may reduce or increase visitor pressure, but ecological outcomes need evidence. Sacred status never grants ecological immunity.

### Land Tenure / Credentials

Access can be restricted through authored policies, custodianship, safety, stewardship, or institutional permission.

Sacredness itself does not create ownership or legal enforcement power.

### Tourism

A sacred place may attract tourists and pilgrims simultaneously. These are different participation contexts and may create different pressures.

### Pokémon Agency

A Pokémon associated with a sacred site keeps individual agency. It is not owned by the site, worshippers, custodians, or visitors.

Repeated presence is not consent to capture, ritual participation, or command.

## World-state principles

### Sacredness is attributed

Store “Group A regards Site X as sacred.” Do not convert it to “Site X is objectively sacred” unless canon explicitly defines what that means.

### Genuine anomalies stay narrow

If a real anomaly occurs at one site:
- record the event;
- record who witnessed it;
- record mechanics if any;
- do not promote every traditional explanation surrounding it.

### Absence can be meaningful without being a failure state

A pilgrimage may finish with no omen, apparition, blessing, Legendary, or extraordinary event. The journey and its social consequences still happened.

### Competing interpretations are first-class state

Two communities can interpret the same ruin differently. A scholar can disagree with both. Later evidence may modify one claim without deleting the others.

### Syncretic history is allowed

A site can accumulate traditions from multiple groups. The generator must not collapse them into a fake pure origin.

### No procedural conversion of PCs

Do not infer or assign to a PC:
- faith;
- atheism;
- devotion;
- doubt;
- spiritual identity;
- obligation to participate;
- private interpretation of an omen.

Record only explicit player-authored choices and mechanics.

## Cultural-safety guardrail

Do not reskin living real-world religions, Indigenous traditions, sacred objects, sacred landscapes, initiation rites, funeral practices, prayers, regalia, or restricted knowledge into Ouros by changing names.

Original Ouros practices must grow from authored regional history, Pokémon-world phenomena, local ecology, institutions, and prior Chronicle events.

## Sacred-site change over years

Example timeline:

Year 0: a hillside stone enclosure is used by a small local community.

Year 1: researchers identify older foundations underneath it.

Year 2: a widely circulated photograph increases visitors.

Year 3: nesting Pokémon begin using an outer wall.

Year 4: access is rerouted during nesting season.

Year 5: a rare atmospheric event occurs during an observance. Some interpret it as confirmation; meteorologists record a plausible physical explanation; one separate unexplained observation remains.

Year 6: the route is restored with an accessible alternate path.

All seven revisions remain true history.

## Minecraft projection

Minecraft may render:
- structures;
- paths;
- gates;
- offerings or display items where culturally appropriate and authored;
- signage;
- archives;
- visitor density;
- route variants;
- restoration work;
- ecological buffers;
- lighting and sound presentation.

Minecraft must not decide:
- sacred status;
- belief;
- ritual efficacy;
- supernatural truth;
- access authority;
- item powers;
- Legendary spawn conditions;
- blessings/curses;
- morality.

## Encounter implementation policy

Sacred-site stories should prefer world-state resolution for:
- interpretation;
- ritual participation;
- custodianship;
- pilgrimage progress;
- artifact handling;
- access disputes;
- research;
- visitor management.

Open AutoPTU only when a real combat conflict exists.

Mechanically rich sacred-site encounters must name exact dependencies using the permanent capability categories.

### Encounter contract: Shrine Approach Evacuation

Narrative premise:
A sudden noncombat incident blocks part of a sacred approach while visitors and wild Pokémon are present.

FULL version:
- dynamic evacuation routes;
- moving noncombatants;
- wildlife withdrawal;
- protected zones;
- possibly changing environmental conditions;
- tactical AI understands `WITHDRAW`, `CLEAR_ROUTE`, `PROTECT`, `REACH_EXIT`.

REDUCED version:
- evacuate visitors and resolve wildlife movement in world state;
- freeze a safe static arena;
- battle only combatants who remain;
- pilgrimage/site consequences update afterward.

### Encounter contract: Relic Custody Interruption

Narrative premise:
A historically important object is being transferred between custodians when a separate conflict occurs.

FULL version:
- moving object/custodian objective;
- interception/protection;
- tactical AI understands custody objective;
- semantic playback.

REDUCED version:
- secure object outside grid;
- resolve battle separately;
- custody transfer resumes or is delayed based on world-state consequences, not on who dealt most damage.

### Encounter contract: Bell Ridge Night Watch

Narrative premise:
Visitors gather for a traditional observation window; an unexpected wildlife conflict occurs nearby.

FULL version:
- moving wildlife with retreat priorities;
- crowd evacuation;
- possibly light/weather visibility if validated;
- tactical AI for withdrawal/avoidance.

REDUCED version:
- site staff pause the observance and clear visitors;
- weather/light remain presentation/world state unless exact mechanics are supported;
- conventional static battle occurs separately if necessary;
- whether an omen occurred remains an evidence question independent of combat.

## Permanent capability dependency policy

Use current engine snapshot labels:

VERIFIED:
- targeting/footprints/range/LoS;
- base movement legality;
- core calculations;
- action economy/initiative;
- AI legal-action infrastructure.

PARTIAL:
- full turn/round lifecycle;
- full stateful damage pipeline;
- status lifecycle;
- move-specific behavior;
- abilities;
- items;
- Trainer Features/perks.

BLOCKING:
- complete movement including push/pull/knockback/interception/forced movement;
- terrain/weather/hazards/zones/reactions;
- AI tactical policy;
- Minecraft/Cobblemon/Craftics adapter/playback.

## Hard non-inferences

Never infer:
- shrine -> Legendary spawn;
- temple -> religion defined;
- sacred object -> magical item;
- ritual -> buff/debuff;
- prayer -> healing;
- blessing -> mechanical bonus;
- curse -> status condition;
- bell/chime -> Sonic Move;
- incense -> terrain/weather/status;
- sacred fire -> Fire-type damage;
- pilgrimage completed -> XP/reputation/Feature;
- restricted site -> owner has universal authority;
- visitor -> believer;
- custodian -> priest;
- elder -> infallible historian;
- old claim -> true claim;
- anomaly observed -> traditional interpretation proven;
- Legendary seen once -> guaranteed reappearance;
- site damaged -> sacred status ended;
- site rebuilt -> old history erased;
- battle victory -> theological, archaeological, ownership, or custodianship conclusion.

## Unresolved canon questions

- Does Ouros begin with authored sacred sites, or should most emerge from regional history documents later?
- Which communities recognize which sites?
- Which practices are public, private, invitation-only, seasonal, or discontinued?
- Which sites have known supernatural events versus only attributed claims?
- How often should Legendary-linked places exist?
- Which custodians have actual access authority?
- Can a sacred route change because of ecology or infrastructure without changing its identity?
- What kinds of sacred objects exist, and which are replicas, heirlooms, archaeological finds, or ordinary symbolic objects?
- How should multiplayer handle private belief and voluntary participation?
- Which exact PTU/Caelo rules govern Occult Education, Aura, Legendary interaction, ritual-like Features, relic effects, or supernatural perception?