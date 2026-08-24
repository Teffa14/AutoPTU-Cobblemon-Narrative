# Research Scan — Oral History, Interviews, Witness Memory & Testimony — Pass 142

Status: RESEARCH / PROVENANCE ONLY. Not Ouros canon.
Date: 2026-08-23

## Why this scan exists

Ouros already has Archives, Cases, Public Memory, Languages, Research Ethics, Identity and Media. Those layers can preserve records, evidence, public stories and translations. They do not yet own the full lifecycle of a spoken recollection: who said it, under what conditions, whether it was recorded, what version was transcribed or translated, what access the narrator allowed, what changed in later retellings and how investigators distinguish memory from independent corroboration.

The useful narrative gap is therefore not "rumors" in general. It is versioned testimony and oral-history provenance.

## New-source scan

### Pokémon Legends: Arceus — inherited legends and conflicting interpretation

Official source: https://legends.arceus.pokemon.com/en-us/story/

The official story material describes Cogita as a person who tells the player legends passed down by her ancestors. The same page also presents Diamond and Pearl Clan members who share inherited beliefs about noble Pokémon while disagreeing about what current events mean.

Reusable structure:
- inherited account can be valuable without becoming direct eyewitness evidence;
- two communities can preserve different interpretations of the same place or phenomenon;
- a narrator can be authoritative about what a tradition says while the truth of the tradition remains open;
- later discoveries can change interpretation without making earlier narrators dishonest.

Do not copy Cogita, Hisui clans, Arceus lore or their specific legends into Ouros.

### Pokémon Legends: Arceus — memory loss as a provenance problem

Official source: https://legends.arceus.pokemon.com/en-us/story/

Ingo is explicitly described as having lost memory of his prior life. This is useful as a guardrail: a sincere narrator can have incomplete autobiographical access. Absence of recall should not be transformed into deception, secret guilt or a mechanical debuff unless the authored story establishes that.

Reusable structure:
- distinguish "does not remember" from "refuses to answer";
- preserve partial recollections as records with uncertainty;
- allow later corroboration to strengthen or weaken a recollection without rewriting the original interview.

### Pokémon Support — intentionally unresolved franchise history

Official source, updated 2026-01-30: https://support.pokemon.com/hc/en-us/articles/360000626593-What-are-the-origins-legends-and-histories-of-Pok%C3%A9mon-characters-or-trainers

Pokémon Support states that unanswered origins, legends and histories are intentionally left to interpretation when the games/animation have not resolved them.

Reusable structure for Ouros:
- archival completeness must not be assumed;
- some historical questions should remain genuinely unresolved;
- a generator should not fill every evidence gap with a definitive backstory merely because a narrator mentions one.

### Pokémon Tabletop United campaign logs — recap as fallible record

Public sources:
- https://www.reddit.com/r/PokemonTabletop/comments/nwtoj5
- https://www.reddit.com/r/PokemonTabletop/comments/qf2pky
- https://www.reddit.com/r/PokemonTabletop/comments/xtwhxv

Several public PTU campaign logs explicitly note that the writer does not remember everything, that another participant was going to write the recap, or that events were later summarized/retconned for playability.

Reusable structure:
- session recollection is a participant-produced source, not a perfect transcript;
- authorship of a recap matters;
- a later summary can differ from an earlier one without requiring malicious falsification;
- "what the table remembers" and "what occurred in world state" should remain separate.

Do not import these campaigns' characters, homebrew Pokémon, factions, encounters or plots.

### Tales of Visiwa retrospective — memory after a long campaign

Official PTU blog retrospective: https://pokemontabletop.com/tales-of-visiwa-a-retrospective/

The retrospective collects memories from GM and players after a long-running PTU campaign. Its value for Ouros is methodological: multiple participants can remember different facets of the same long history, and retrospective meaning can differ from what participants thought during the event.

Reusable structure:
- maintain contemporaneous records and later retrospective interviews separately;
- allow former participants to reinterpret old decisions;
- preserve disagreement rather than forcing a synthesized "correct memory" when independent evidence is insufficient.

### Oral History Association — consent, access and archival provenance

Public best-practice sources:
- https://www.oralhistory.org/wp-content/uploads/2020/06/OHA-Principles-and-Best-Practices-Original-and-Archives-updated-Oct-2019.pdf
- https://oralhistory.org/wp-content/uploads/2022/08/OHA-Principles-and-Best-Practice-Print-Version-Updated-2022.pdf
- https://oralhistory.org/wp-content/uploads/2019/11/OHA-Archives-Principles-and-Best-Practices-Complete-Manual.pdf

Reusable architecture:
- informed permission belongs to the interview process, not merely to the archive that later stores it;
- access/use restrictions should be explicit and versioned;
- narrator, interviewer, date/place, recording device, preservation state and descriptive metadata all matter;
- a recording and its transcript are related but distinct objects;
- later public access should not be inferred from the fact that an interview occurred.

Ouros should adapt the abstract provenance pattern, not real-world law or institutional policy.

## Design lessons extracted

1. Spoken recollection is an observation with an author and context, not world truth.
2. Eyewitness testimony, inherited tradition, hearsay, later retelling and institutional summary need different source classes.
3. Confidence and accuracy are separate. A confident narrator can be mistaken; a hesitant narrator can be correct.
4. Silence has multiple meanings: no memory, refusal, privacy restriction, missing recording, unavailable narrator, interruption or never asked.
5. Interview order can matter. Repeated questioning can produce later versions that are not independent evidence.
6. Translation/transcription can introduce another revision layer. The original audio should remain linked.
7. A narrator can permit private research use while withholding public release.
8. A testimony can corroborate one part of an event while conflicting on another.
9. A later correction should append to the record rather than silently replacing the earlier statement.
10. Collective oral tradition can preserve stable motifs while names, dates or causal explanations drift.
11. A memorial speech, press interview, police-style witness statement and research oral history are different contexts even if spoken by the same person.
12. Pokémon behavior observed during an interview should remain Pokémon Agency/Science evidence; the human narrator's interpretation is a separate claim.

## Candidate Ouros source classes

- FIRSTHAND_RECOLLECTION
- CONTEMPORANEOUS_WITNESS_STATEMENT
- LATER_RETROSPECTIVE
- INHERITED_ORAL_TRADITION
- HEARSAY_ACCOUNT
- PROFESSIONAL_RECOLLECTION
- COMMUNITY_MEMORY
- PUBLIC_INTERVIEW
- PRIVATE_ORAL_HISTORY
- INCIDENT_DEBRIEF
- UNSOURCED_RETELLING

These are provenance labels only. None establishes truth or legal weight.

## Anti-copy / anti-overreach rules

Do not import protected dialogue, named characters, specific plots, clan histories, Legendary myths or campaign twists from sources.

Do not treat real-world oral-history best practice as Ouros law.

Do not infer deception from inconsistent memory.

Do not infer trauma, illness, age-related decline or psychological diagnosis from an inconsistent account.

Do not use player biography, account metadata or out-of-character chat as in-world testimony unless the player explicitly creates an in-world statement.

Do not allow interview participation to imply consent for battle, research samples, publicity, employment, faction membership or further contact.

## PTU / Caelo mechanics boundary

No generic interview, testimony, memory or truth-detection mechanic was verified in the live Java engine during this scan.

Possible PTU concepts such as Guile, Charm, Command, Intuition, Perception, Telepathy or Psychic effects must only be used when exact project source text and parity-backed runtime behavior support the specific interaction.

A successful social check must never become an engine-level lie detector unless an authoritative rule explicitly says that.

Caelo primary material was not recovered reliably in this run. Super PTU Online Helper was not exposed as an invocable capability. No output is invented for either source.