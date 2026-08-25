# Seasonal Dormancy, Torpor and Hibernation Research Scan — Pass 171

Status: RESEARCH ONLY. Not canon. Not a PTU rules source.
Date: 2026-08-25

## Why this pass exists

The repository already has strong ownership for diel activity, seasonality, rest/roost sites, care, cryosphere, migration and wildlife monitoring. It does not yet have a dedicated authority for prolonged or repeated low-activity physiological/ecological states such as torpor, hibernation or other seasonal dormancy.

This pass therefore extends the existing activity/seasonality architecture instead of treating dormancy as ordinary Sleep.

## Internal repository guardrails

`design/diel-activity-circadian-rhythms-layer.md` already separates biological rest from PTU Sleep and records rest/roost sites, activity profiles, sampling effort and seasonal/local shifts.

Pass 171 must not overwrite that authority. It adds a longer-timescale state contract for extended inactivity and seasonal transitions.

Care remains authoritative for medical/welfare assessment.

Seasonality remains authoritative for recurring annual windows.

Cryosphere/Meteorology remain authoritative for snow, cold and weather.

Pokémon Agency remains authoritative for persistent individual identity and custody/partnership.

## Pokémon precedents

### Jirachi — very long dormancy as authored species lore

Bulbapedia's current Jirachi biology summary records the recurring franchise premise that Jirachi spends most of its life dormant and awakens for a short interval on a thousand-year cycle.

Source: https://bulbapedia.bulbagarden.net/wiki/Jirachi

Reusable lesson:

- a long dormant interval can be part of a species' authored history;
- awakening can be a rare world event without becoming a general status mechanic;
- an individual can retain identity through an enormous inactive interval;
- dormancy can carry cultural expectations that remain separate from verified causal rules.

Do not copy Jirachi's thousand-year schedule into Ouros populations unless canon explicitly authors it.

### Ursaring — hibernation identity in franchise material

Ursaring has repeatedly been called the Hibernate/Hibernator Pokémon in anime Pokédex material and TCG material.

Source: https://bulbapedia.bulbagarden.net/wiki/Ursaring_(Pok%C3%A9mon)

Reusable lesson:

- a species can carry a strong public association with hibernation while local populations still need evidence-based timing;
- species labels do not prove every individual is dormant in every winter;
- habitat use before, during and after the dormant interval can become a longitudinal field-study hook.

Do not infer PTU Sleep, reduced Speed, helplessness, encounter immunity or automatic winter absence from this label.

## Comparative ecology

### Torpor and hibernation are dynamic states, not simply 'sleeping all winter'

A review of mammalian torpor and hibernation describes torpor as regulated metabolic suppression with reduced body temperature and metabolic rate. Hibernation commonly contains repeated torpor bouts interrupted by arousals rather than one uninterrupted state.

Sources:
- https://pubmed.ncbi.nlm.nih.gov/27755687/
- https://pubmed.ncbi.nlm.nih.gov/10757457/

Reusable lesson for Ouros:

- dormancy should allow state transitions such as ENTRY, TORPOR_BOUT, INTERBOUT_AROUSAL and EXIT;
- a midwinter observation of activity does not automatically prove dormancy ended;
- one missed observation does not prove an individual stayed continuously inactive.

### Dormancy is not always a simple winter calendar

A comparative review reports substantial diversity in the seasonal expression of torpor and hibernation, including tropical/subtropical use and non-winter expression in some species.

Source: https://pubmed.ncbi.nlm.nih.gov/32508673/

Reusable lesson:

- Ouros should not encode `winter = hibernate` as a universal rule;
- local food/water availability, climate, energetic demands and predation context may matter in authored ecological interpretations;
- season windows should be evidence-backed and versioned by population/location.

### Den-site history can matter

The U.S. National Park Service describes brown-bear den sites as important to energy conservation and reports repeated GPS-based den studies in Arctic Alaska.

Source: https://www.nps.gov/articles/beardens.htm

Reusable lesson:

- den/hibernaculum identity can be persistent world state;
- repeated use can matter without implying ownership;
- den selection can create long-term overlap with roads, mining, tourism, forestry or conservation;
- exact locations can be sensitive information.

### Monitoring can disturb dormant wildlife

USGS has used non-invasive thermal and near-infrared monitoring across full winters at bat hibernacula, partly because disturbance itself matters when studying dormant animals.

Source: https://www.usgs.gov/centers/fort-collins-science-center/science/non-invasive-surveillance-bat-hibernacula-investigate

Current USGS winter 2025–2026 white-nose syndrome guidance also distinguishes active hibernacula surveys, passive reports and spring trapping as different evidence streams.

Source: https://www.usgs.gov/media/files/bat-white-nose-syndromepd-surveillance-submission-guidelines

Reusable lesson:

- monitoring effort, method and disturbance risk need provenance;
- a hibernaculum survey can be intentionally incomplete;
- missing detections do not automatically mean mortality or abandonment;
- health surveillance belongs to Care/Outbreak authority, not to the dormancy layer itself.

## PTU / AutoPTU cross-check

Project search confirms PTU-derived data includes concrete concepts such as Sleep/Asleep and sleep-related Abilities/Moves. That evidence does not provide a general overworld hibernation subsystem.

Read-only project search surfaced PTU data for sleep-related Moves/Abilities in AutoPTU, including source tables for `Insomnia`, `Vital Spirit`, `Early Bird` and sleep-related Move data. These are tactical/mechanical concepts, not a license to equate biological dormancy with PTU Sleep.

AutoPTU-Java current head inspected during this pass: `d64d6417dc89c1aca878d0a8fd6b526921b8e193` — `Route move-special secondary statuses through canonical prevention (#205)`.

That slice improves a narrow secondary-Status path and canonical prevention routing. It does not establish a world-state dormancy system or complete the Status family.

AutoPTU Python current head inspected: `54edaa5377589d8d182f91260845389ae694300c` — Career persistence hardening. It does not alter battle readiness.

## Narrative structures worth importing

### The den that opens late

A historically reliable emergence window passes without activity. The immediate story should not assume death. Possible evidence classes include incomplete coverage, altered snow/temperature, a changed entrance, an alternate exit, a later seasonal shift or genuine welfare concern.

### Arousal is not awakening

Researchers observe midwinter movement. The public assumes the dormant period ended. Longitudinal evidence later shows a brief arousal followed by renewed dormancy.

### The famous winter route becomes quiet

A species associated with a winter hiking region is rarely visible for several months. Tourism pressure, conservation closure and local rumor can coexist without changing population truth.

### Den-site inheritance without family inference

The same shelter is used across multiple years or generations. Ouros can preserve site history while leaving kinship unresolved unless independent evidence exists.

### The monitoring blackout

A camera or sensor fails during the exact period players care about. The gap becomes a legitimate uncertainty rather than an invitation for the generator to invent what happened.

## Anti-patterns

Do not use:

- dormancy as PTU Sleep by default;
- hibernation as a guaranteed winter spawn suppression formula;
- one cold day as an automatic trigger;
- absence from loaded chunks as evidence of dormancy;
- awakening as automatic aggression;
- dormant Pokémon as automatically capturable or helpless;
- disturbance as automatic damage;
- warming trends as instant early-emergence truth without observations;
- species names/flavor as universal mechanical behavior.

## Research conclusion

Ouros can gain substantial Chronicle value by modeling dormancy as a persistent ecological state with uncertain entry/exit timing, episodic arousal, protected sites, monitoring effort and long-term change.

The key architectural protection is simple: ecological dormancy belongs to world state; PTU Sleep belongs to the battle engine.