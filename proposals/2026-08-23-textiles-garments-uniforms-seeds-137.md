# Pass 137 — Textiles, Garments, Uniforms & Wearable Material Culture Seeds

Status: NON-CANON PROPOSALS.

These concepts use the systems layer added in Pass 137. They do not establish regional clothing norms, mechanical equipment effects, Fashionista rules, uniforms, institutions or Pokémon-material harvesting as canon.

## 30 candidate seeds

1. The Coat With Twelve Repairs — one field coat remains in use for decades; every patch records a different expedition, repairer and material source.
2. The Uniform Outlived the Institution — a retired service uniform remains common in secondhand shops long after its issuing organization disappeared.
3. Three Dyes, One Color — three workshops produce nearly identical colors through different materials and processes; a museum attribution depends on provenance rather than appearance.
4. The Tailor Refuses the Commission — a respected artisan declines an important client's request without scandal, hidden loyalty or conspiracy.
5. The Old Credential Patch — a legally purchased secondhand jacket still carries an obsolete institutional patch, causing confusion but granting no access.
6. Festival Costume Revision Seven — the same recurring observance uses a costume pattern that has changed gradually over seven editions.
7. The Weatherproof Claim — a merchant advertises a coat as excellent in rain; the claim is commercial, not a PTU environmental immunity.
8. Two Wool Batches — two Wooloo-fiber textiles look identical, but only one has complete provenance and care records.
9. Borrowed Performance Coat — a performer loans a signature coat to another artist; public attention briefly mistakes the wearer for the owner.
10. The Old Logo — staff still wear a previous uniform revision while replacements arrive through Supply Chains.
11. The Leavanny Workshop — a Leavanny repeatedly assists with leaf garments, but participation varies and is never treated as a permanent workplace obligation.
12. Costume Mistaken for Office — a visitor assumes someone in ceremonial clothing has institutional authority; Credentials proves otherwise.
13. One Coat, Three Owners — a single garment passes through sale, gift and donation while retaining one persistent item identity.
14. The Missing Sleeve — a historical garment in storage was altered decades ago; the removed material has its own uncertain provenance.
15. The Repair Became the Famous Part — a later repair becomes more recognizable than the original design.
16. The Uniform Return That Never Posted — the garment was physically returned, but the institutional record never updated.
17. Wrong Size, Right Role — a newly assigned worker has valid credentials but the issued uniform does not fit; fit and authority remain separate.
18. The Prototype Adaptive Jacket — a workshop experiments with adjustable construction for several body plans without creating mechanical movement bonuses.
19. The Coat Stored Too Brightly — a displayed textile looks intact while conservation records show cumulative light exposure concerns.
20. The Replica at the Parade — a replica of a famous garment is intentionally worn outdoors while the original remains preserved.
21. The Forgotten Laundry Mark — an old ownership/custody mark helps reconstruct the garment's history but does not prove current ownership.
22. The Dye Lot Dispute — visible shade variation is blamed on poor workmanship until batch records show an intentional revision.
23. The Pokémon Accessory Is Removed — a Pokémon repeatedly removes a decorative accessory; the institution changes presentation policy rather than forcing compliance.
24. The Burmy Misclassification — visitors treat a Burmy cloak as crafted clothing until a field guide corrects the interpretation.
25. The Wool Shortage That Was Allocation — fiber exists regionally, but most of it is reserved for another institution; no production collapse occurred.
26. The Traveling Mender — a repairer follows rail/ferry routes and becomes part of the seasonal service network without founding a guild or quest hub.
27. The Wardrobe With Two Histories — two garments are repeatedly attributed to the same public figure; only one has strong provenance.
28. The Emergency Blankets Became Ordinary — surplus emergency textile stock later enters routine community use through an authorized disposition process.
29. The Uniform Museum Loan — a historic uniform returns temporarily to its former workplace as an exhibition loan without restoring the old institution or rank.
30. Nothing Happened at the Tailor — a routine fitting, repair and pickup occur successfully; Chronicle records only the meaningful state change and creates no quest.

## Longer arcs

### Five Uniforms of Meridian Transit

Year 1: a transport service uses an old uniform pattern inherited from a predecessor institution.
Year 2: accessibility and climate feedback produce a revised design proposal.
Year 3: supply shortages create a mixed-uniform transition period.
Year 4: a retired pattern becomes popular secondhand, causing repeated visual confusion with current staff.
Year 5: the service donates representative garments and pattern records to a local collection.

The arc is about institutional continuity, manufacturing, procurement, identity and public memory. Clothing never grants authority.

### One Coat, Three Owners

A durable expedition coat begins with one field researcher, is later sold secondhand, altered for a second wearer, repaired after a route incident and eventually donated by a third custodian. The same `garment_instance_id` accumulates decades of material and social history. None of the wearers inherits the previous owner's profession, credentials or relationships.

### The Leaf Tailor Years

A settlement documents intermittent Leavanny garment-making across several years. Some garments are ephemeral; one survives long enough to become a local artifact. Researchers debate imitation, individual preference and Social Learning while Pokémon Agency preserves voluntary participation. The arc never turns Leavanny into a generic crafting station.

## Encounter contracts

### Heritage Garment Transfer

Narrative premise: a historically important garment is being transferred between two institutions when an unrelated confrontation interrupts the handoff.

FULL version dependencies:
- targeting/footprints/range/LoS — VERIFIED;
- base movement legality — VERIFIED;
- complete movement including interception/forced movement — BLOCKING for moving custodians/route control;
- core calculations — VERIFIED;
- action economy/initiative — VERIFIED;
- full turn/round lifecycle — PARTIAL;
- full stateful damage pipeline — PARTIAL;
- status lifecycle — PARTIAL only if exact mechanics invoke it;
- terrain/weather/hazards/zones/reactions — BLOCKING if environmental hazards or reaction routes matter;
- move-specific behavior — PARTIAL;
- abilities — PARTIAL;
- items — PARTIAL if the garment is ever given a validated mechanical item role;
- Trainer Features/perks — PARTIAL;
- AI legal-action infrastructure — VERIFIED;
- AI tactical policy — BLOCKING for PROTECT_CUSTODIAN/CLEAR_ROUTE/WITHDRAW;
- Minecraft/Cobblemon/Craftics adapter/playback — BLOCKING.

REDUCED version:

Complete or pause the garment handoff in world state, move the item and civilian custodians outside the tactical arena, freeze a safe static location and let AutoPTU resolve only actual combatants. Custody/provenance resumes afterward. Victory cannot transfer ownership or validate provenance.

### Festival Costume Workshop Interruption

Narrative premise: a workshop preparing recurring event costumes must shut down safely during an unrelated incident.

FULL version needs complete movement for staff evacuation, tactical AI for CLEAR_ROUTE/WITHDRAW, adapter/playback for workers/racks/workspace and any exact environmental family that a verified hazard invokes.

REDUCED version:

Stop work, secure unfinished garments and evacuate workers in world state. Use one static battle space if a confrontation remains. Production status and costume completion are resolved afterward.

### Uniform Mix-Up at Field Station

Narrative premise: two people are visually mistaken for staff because old and current uniforms coexist at the same station.

This is primarily non-combat. Resolve identity, assignment and credentials in world state. If a separate battle occurs, ordinary static combat is sufficient. Winning cannot prove employment, rank or authorization.

## Explicit non-mechanics

Do not add:

- clothing-based Charm/Command/Guile bonuses;
- generic Armor or Evasion from garments;
- weather resistance from ordinary coats;
- Fashionista effects without exact rules;
- Pokémon stat changes from costumes;
- uniform-based faction AI;
- gender/class/wealth inference from appearance;
- automatic fiber harvesting;
- repair-based item stat changes;
- Minecraft cosmetic slots as PTU equipment authority.