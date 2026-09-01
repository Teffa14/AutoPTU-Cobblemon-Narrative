# Correspondence, Courier and Message Continuity Scan — Pass 189

Status: RESEARCH / PROVENANCE. NOT CANON.
Date: 2026-09-01
Writable destination: Narrative repository only.

## Scope

This pass examines correspondence as persistent world state: requests, letters, packets, posted messages, delivery attempts, acknowledgements, replies, stale copies, privacy, provenance and courier handoffs.

The repository inventory was inspected before choosing this seam. Existing work already covers rumor, provenance, archives, public notices, institutional authority, dispatch-like work, custody, field search, preparedness, provisioning, salvage, exhibitions and persistent consequences. The missing design problem is narrower: a message can exist as an authored record and as one or more physical copies while sender intent, custody, delivery, reading, acknowledgment, currentness and response remain different facts.

This file records source-derived structures only. It does not establish postal law, courier institutions, telecommunications, privacy law, literacy norms, regional Caelo procedure or supernatural communication in Ouros.

## Public-source findings

### Pokémon Mystery Dungeon: Red / Blue Rescue Team — official manual

Source:
https://manuals.plus/m/ae195fb54967ca670d9099843e3120c118afd3a0f12b379f93739c5a619a378b

Relevant high-level structure:

- a distressed party sends an SOS Mail;
- a rescuer separately receives that mail;
- the rescuer chooses to undertake the rescue;
- completing the physical rescue does not itself complete the communication loop;
- an A-OK Mail communicates success back to the original party;
- the original party separately receives that confirmation;
- a Thank-You Mail may follow as another message;
- an item can optionally be attached to a later message.

Reusable lesson for Ouros:

A communication chain can have several records that refer to one incident without being one mutable object. Request, acceptance, completion, acknowledgment and response should remain distinct. This supports delayed information, missing acknowledgments and autonomous institutional work without making the world omniscient.

Do not import the game's exact rescue rules, revival semantics, mail technology or rewards.

### Pokémon Mystery Dungeon: Explorers of Time — official user manual mirror

Source:
https://manualzilla.com/doc/7002536/nintendo-pokmon-mystery-dungeon-explorers-of-time-user-s-...

Relevant high-level structure:

The rescue flow again requires receiving the rescue message, carrying out the operation and sending an A-OK Mail tied to the completed SOS request. A message can also carry an attached written note.

Reusable lesson:

Completion of work and communication of completion are separate state transitions. A task can be finished while another actor still lacks current information.

### Pelipper Post Office / job board structure

Source:
https://mysterydungeonwiki.com/wiki/Rescue_Team%3APelipper_Post_Office

Relevant high-level structure:

The same physical institution supports direct rescue correspondence and a public job board. Private/direct communication and publicly posted work therefore use different visibility surfaces even when they belong to the same operational network.

Reusable lesson:

Ouros should distinguish addressed correspondence from public posting. A notice visible to everyone should not be treated as evidence that a named recipient personally received or read it.

### Friend Rescue behavior after an SOS has been distributed

Source:
https://bulbapedia.bulbagarden.net/wiki/Mystery_Dungeon%3A_Blue_rescue_team

Relevant high-level structure:

An SOS Mail can remain actionable after transmission, while the waiting party can later change what they are doing. The existence of a previously issued request therefore need not imply that every later world condition still matches the situation at send time.

Reusable lesson:

Messages need created/sent time, current status and supersession or cancellation handling. A previously genuine message can become stale without becoming fraudulent.

### Pokémon Mail as a message-bearing object

Source:
https://pokedb.org/items/tropic-mail

Relevant high-level structure:

Generation III Pokémon Mail couples a written message with a holdable physical item.

Reusable lesson:

A physical carrier can hold text, but physical possession and narrative authority remain separate questions. Ouros can use sealed letters, packets, tags or message-bearing items without treating the Minecraft item stack as the authoritative message database.

Do not import Generation III transfer restrictions, item pricing or battle interactions as PTU rules.

## Campaign and PTU search outcome

Searches were run for public PTU campaigns, actual plays and community material involving letters, couriers, delivery, messages and bulletin boards. No sufficiently clear source in this pass established a reusable PTU-specific correspondence procedure worth elevating above ordinary campaign practice.

This absence is useful. The narrative layer should not invent a `Courier Skill`, `Message Check`, `Delivery Feature` or universal roll because a campaign happened to adjudicate correspondence a certain way.

## Internal PTU / AutoPTU cross-check

The current AutoPTU repository contains Pokémon and Foundry material where the string `Mail` occurs, including general Pokémon item data. The search also produces unrelated results such as armor named Scale Mail and software email fields. These hits are not evidence of a verified PTU correspondence subsystem.

No indexed `Caelo` hit was located in Narrative, AutoPTU-Java or AutoPTU during this pass. This means the current repository evidence does not answer regional questions about postal services, courier authority, message privacy, seals, signatures, literacy, magical communication or delivery law. It does not prove that the external Caelo source material lacks such rules.

No battle engine family should be promoted because correspondence exists as world content.

## Extracted design patterns

### Message chain rather than mutable quest text

One incident can create several linked records:

- initial request;
- delivery or receipt record;
- acceptance or assignment;
- update;
- completion notice;
- acknowledgment;
- reply;
- correction or superseding instruction.

Each record keeps its own provenance.

### Delivery state has meaningful intermediate steps

Useful states include drafted, issued, in custody, in transit, delivery attempted, delivered, refused, returned, lost/unknown, superseded and archived.

A later system can use a smaller vocabulary if needed. The important point is that `sent` must never collapse every later step.

### Reading and acknowledgment are separate

Delivery to a desk, household, office or delegated staff member can be valid custody without proving that the intended decision-maker personally read the contents.

This is especially useful for Marea because established institutions already have different review and operational authorities.

### Physical copies can disagree

A copied notice, handwritten duplicate or old posted sheet can survive after a revised instruction exists. The world should preserve which version was authoritative at a given time and which version each actor could legitimately have seen.

### Authenticity is evidence-based

A visible name, seal, handwriting style or sender mark is an observation. Authentication can depend on provenance, known issuance procedure, witness, record match or explicit author confirmation. The engine should not turn a cosmetic texture into proof.

### Replies are new records

A reply should reference the earlier message and can answer, reject, correct or supersede it. The earlier record remains historically real.

### Delay creates stories without villains

A request can arrive after the problem has already been solved. A closure notice can reach a destination after another route was chosen. A resident can be absent when delivery is attempted. These outcomes create believable world friction without requiring sabotage or incompetence.

### Public posting and direct delivery differ

A board, sign or handbill creates public availability. It does not prove individual notice. Conversely, a private packet can reach an authorized recipient without becoming public knowledge.

## Worldbuilding opportunities

Correspondence can make time visible. Paper copies, returned packets, dated notes and corrected postings can reveal that the world continued between player visits.

It can also connect existing Marea institutions without centralizing them. Ferry Landing can move a packet. Tideglass can preserve provenance. Mirador can issue or receive field instructions. The Field Office can coordinate operational messages. None of these facts requires a new postal authority.

A message can generate a quest without becoming the quest itself. The world retains the correspondence record even if the task is completed by another resident, refused, superseded or rendered unnecessary.

## Risks to avoid

Do not make every NPC instantly know every posted fact.

Do not treat a courier as a universal authority over message contents.

Do not infer sender authenticity from a displayed name alone.

Do not let chunk unload, item despawn or visual duplication delete or create authoritative correspondence.

Do not convert delivery failure into proof that a resident is missing, endangered or dead.

Do not let a battle decide whether a message was authentic, current, read, accepted or acted upon.

Do not invent a PTU or Caelo mechanic for communication until exact source evidence is located.

## Recommended implementation direction

The first implementation slice should be noncombat and narrow: a packet arrives at Tideglass while its usual reviewer is unavailable. Another resident can receive and log custody without silently inheriting review authority. The player can see delivery succeed while the decision the packet requests remains pending.

That slice tests persistence, custody, recipient scope, delayed reading and later acknowledgment with almost no engine dependency.

## Provenance note

Public Pokémon material informed only high-level structures. No protected dialogue, distinctive plot sequence or character arc is copied into Ouros. All proposed Marea material remains original and non-canon until explicitly promoted.