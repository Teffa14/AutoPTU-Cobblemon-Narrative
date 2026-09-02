# Memorial, Death, Remains & Belongings Research — Pass 205

Status: RESEARCH / PROVENANCE ONLY
Date: 2026-09-02
Canon effect: NONE

## Scope

This pass studies how Pokémon fiction and PTU distinguish death, mourning, burial places, personal belongings, memorial practice, Ghost-type presence and mechanical combat consequences. The purpose is to create reusable Ouros structures without canonizing a regional funerary system, afterlife model, inheritance law or Ghost metaphysics.

Repository review before research found no dedicated Narrative layer for death, memorial custody, remains, posthumous belongings or bereavement continuity. Existing adjacent layers already cover public memory, archives, material provenance, sacred sites, care/recovery, residence, claims and institutional custody. Pass 205 therefore concentrates on the transitions among those systems rather than duplicating them.

## Public Pokémon sources

### Lavender Town / Pokémon Tower

Source: Bulbapedia, Lavender Town / Pokémon Tower.
URL: https://bulbapedia.bulbagarden.net/wiki/Lavender_Town

Reusable structure:
- a burial place can remain part of ordinary civic geography rather than existing only as a horror dungeon;
- people repeatedly visit to pay respects;
- physical graves, living mourners, wild Pokémon and supernatural claims can coexist in the same location;
- later redevelopment can relocate memorial functions without deleting the historical identity of the earlier place.

Transformation rule for Ouros:
Do not copy Lavender Town, Pokémon Tower, Marowak, Mr. Fuji or Team Rocket. Preserve only the structural separation among memorial site, mourners, current ecology, historical event and later site transition.

### Hau'oli Cemetery

Source: Bulbapedia, Hau'oli Cemetery.
URL: https://bulbapedia.bulbagarden.net/wiki/Hau%27oli_Cemetery

Reusable structure:
- people and Pokémon may share a memorial landscape;
- mourners can carry persistent objects connected to the deceased;
- a surviving Pokémon can have a continuing relationship to a deceased Trainer without becoming a transferable asset by default;
- grief may affect behavior without granting a universal mechanical condition.

Transformation rule:
Ouros may model a surviving companion, an object with posthumous provenance and repeated visits. It must not infer ownership transfer, survivor guilt, inheritance, legal kinship or a mechanical grief debuff unless separately authored.

### Celestial Tower

Source: Bulbapedia, Celestial Tower.
URL: https://bulbapedia.bulbagarden.net/wiki/Celestial_Tower

Reusable structure:
- a memorial place can contain a simple repeated act such as ringing a bell;
- the act can matter socially and emotionally without needing a battle reward;
- care for a living injured Pokémon and remembrance of a deceased Pokémon can occur in the same place while remaining different states.

Transformation rule:
A remembrance action in Ouros can write social/history state, but it cannot heal, revive, communicate with spirits or grant PTU benefits unless authoritative mechanics explicitly support that effect.

### Memorial Hill / burial-ground pattern

Source: Bulbapedia, Memorial Hill; Bulbapedia, Death in the Pokémon world.
URLs:
- https://bulbapedia.bulbagarden.net/wiki/Memorial_Hill
- https://bulbapedia.bulbagarden.net/wiki/Death_in_the_Pok%C3%A9mon_world

Reusable structure:
Pokémon settings repeatedly use burial grounds as spaces where remembrance, current wild ecology, old political history and Ghost-type encounters overlap. This supports treating a memorial landscape as layered world state rather than equating it with a supernatural dungeon.

## PTU 1.05 mechanical cross-check

Source: Pokémon Tabletop United 1.05 Core, Combat: Death and Fainted rules, publicly mirrored by AnyFlip.
URL: https://anyflip.com/deia/psdg/basic/251-300

PTU 1.05 provides explicit death thresholds in non-friendly combat and separately defines Fainted/KO state. It also notes that Injury and Death rules can be adjusted or removed by campaign tone.

Design consequence:
- Narrative must never promote `fainted` to `dead` merely because a combatant reached 0 HP;
- Narrative must never infer death from actor disappearance, Minecraft death animation, despawn or chunk unload;
- if Ouros retains PTU death rules, an authoritative engine or adjudication path must write a confirmed mechanical death result before Narrative creates a death event;
- if Caelo modifies or disables those rules, Caelo governs;
- funerary or memorial content must still support deaths established by authored canon or non-combat history without inventing how they mechanically occurred.

Repository evidence check:
- AutoPTU Python has broad `fainted` state usage in battle controllers, AI and hooks;
- no indexed evidence found in this run demonstrated a complete end-to-end death adjudication contract equivalent to the PTU 1.05 threshold text;
- AutoPTU-Java returned no indexed `fainted` result in the targeted search;
- therefore death resolution itself is not promoted to VERIFIED engine support by this pass.

## PTU community signal

Public Pokémon Tabletop discussions show Ghost-focused and ruin-focused campaigns, but the examples found are highly homebrew and do not establish a shared PTU rule for memorial practice, afterlife, burial, inheritance or spirits.

One public campaign-help thread used Spiritomb and ruins as a heavily authored supernatural premise. It is useful only as a warning: table campaigns frequently layer custom metaphysics onto PTU, so Narrative must not mistake community campaign fiction for rules authority.

Source: r/PokemonTabletop, “Help writing a session”.
URL: https://www.reddit.com/r/PokemonTabletop/comments/14zlebc

## High-level design lessons

1. Mechanical death, historical death, public report of death and memorialization need separate records.
2. A grave or memorial proves a commemorative act or claim, not necessarily all details of death.
3. A deceased person's or Pokémon's belongings retain provenance; custody and ownership after death require separate authority.
4. A surviving Pokémon companion remains an individual actor. It is not automatically inherited by relatives, institutions or the player.
5. Ghost-type presence near a memorial does not prove the dead became Ghost Pokémon.
6. A ritual, bell, flower, marker or recurring visit can have social meaning without a supernatural effect.
7. A memorial site can move, close, be rebuilt or be repurposed while historical continuity persists.
8. Mourners may disagree about interpretation, disposal, display or access without either side being malicious.
9. A battle near a burial or remembrance site should resolve only the immediate tactical conflict. It cannot validate an afterlife claim.
10. Death-sensitive content should be sparse and state-driven; it should not become random tragedy generation.

## Candidate Ouros applications

These are research-derived structures, not canon:
- an archived field object whose original user is confirmed deceased but whose present custodian is unresolved;
- a small remembrance marker for a former local working Pokémon, with multiple residents preserving different memories of the same individual;
- a route-side memorial that predates current road maintenance and must be moved temporarily during repair, creating documentation and stewardship questions;
- a surviving Pokémon companion whose current care arrangement is known while ownership and future partnership remain unresolved;
- a Ghost-type sighting near a remembrance site recorded as ecology evidence, not spirit proof;
- a memorial register that preserves dates and names while a public retelling adds unsupported causal claims;
- a former resident's room or locker whose contents require inventory, custody and forwarding decisions after a confirmed death elsewhere in canon.

## Explicit rejected shortcuts

Do not generate:
- random NPC or Pokémon death for emotional impact;
- resurrection mechanics;
- automatic reincarnation as Ghost-type Pokémon;
- universal funeral religion;
- inheritance law;
- ownership transfer of Pokémon through death;
- grief meters or grief penalties;
- spirit communication from ordinary memorial interaction;
- lootable graves;
- battle rewards for disturbing burial places;
- death from Minecraft entity state;
- death from Fainted state alone.

## Caelo unresolved surface

No indexed Caelo source content was found in Narrative, AutoPTU-Java or AutoPTU during this run. Therefore unresolved:
- whether Caelo keeps, modifies or disables PTU 1.05 death thresholds;
- revival/resuscitation boundaries, if any;
- funeral or burial practices;
- treatment of human versus Pokémon remains;
- inheritance and estate rules;
- ownership/custody transfer after a Trainer dies;
- legal or institutional authority over unattended belongings;
- supernatural truth around spirits, ghosts and afterlife.

Pass 205 does not answer those questions.