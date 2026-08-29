# Ouros Narrative Research — Emergency Medical Transport & Referral Continuity — Pass 118

Status: RESEARCH ONLY. This file records provenance and design evidence. It does not establish Ouros canon.
Date: 2026-08-29

## Why this pass exists

The repository already has strong ownership for care cases and facilities, generic travel, crisis response, roads, aviation, maritime transport, communications, accessibility, custody, cold chain and community-health investigations. Full-tree inspection before writing found no dedicated continuity layer for the operational interval between a request for medical transport and accepted handoff at a receiving care service.

The missing state is not another healing system. It is the chain of request, dispatch, acceptance, access to subject, pickup, departure, transport, diversion, arrival, transfer of care, vehicle/crew turnaround and inter-facility referral or retrieval.

Existing ownership remains authoritative:

- Care owns patient/subject condition, diagnosis, treatment, facility service and legal healing writeback.
- Crisis owns emergency world state, rescue operations, staging and unresolved needs.
- Travel owns generic journey and route/service state.
- Road/Aviation/Maritime own the physical networks and transport-sector operations.
- Communications owns message delivery rather than medical priority itself.
- Accessibility owns actor-specific access requirements.
- Cold Chain/Courier/Custody own protected material and evidence movement when relevant.
- AutoPTU owns tactical legality and results when a battle actually occurs.

Pass 118 therefore targets medical-transport continuity only.

## Internal PTU/Caelo cross-check

The existing project source scan records PTU campaign guidance, Caelo activity containers, location-specific mechanical identity and the rule that environmental flavor must not become mechanics without a governing source.

Relevant internal source corpus remains:

- CoreRulebook.pdf;
- Caelo Player's Guide 1.5.pdf;
- Caelo Region Location & Encounter List.pdf;
- character creation merged.pdf;
- Erratas and extra merged.pdf;
- Pokedex / pokedex merged.pdf.

Nothing in the currently indexed source scan establishes a universal PTU ambulance subsystem, generic triage queue, dispatch roll, patient-carry rule, stretcher movement system, emergency-vehicle priority rule, transport stabilization mechanic or inter-facility referral mechanic.

Any future mechanic using carrying, lifting, escorting, forced movement, moving vehicles, timed deterioration, medical Items, Trainer Features or Pokémon capabilities must be validated against the exact governing text and current engine contracts.

## Public Pokémon material

### Ambulances exist as recurring transport, not a universal mechanic

Source: https://bulbapedia.bulbagarden.net/wiki/Land_transport

Bulbapedia's transport overview records several animated-series appearances of ambulances, including transports associated with Pokémon Centers and Nurse Joy. The reusable lesson is modest but useful: Pokémon-world care can extend beyond a stationary Center, and a medical vehicle can be an ordinary institution asset rather than a one-off magical exception.

Ouros transformation:

- medical transport may be authored as a persistent service where regional canon supports it;
- the vehicle remains an asset with availability, crew, location and service state;
- its existence does not imply universal coverage, instant response, free access, right-of-way rules or healing in transit.

No vehicle model, staffing rule or emergency-driving mechanic is imported.

### Field work, ambulance transport and facility care can belong to one institution

Source: https://bulbapedia.bulbagarden.net/wiki/A_Giga_Battle_With_Mega_Results%21

In this episode a Nurse Joy performs field work, uses an ambulance to bring travelers back to the Pokémon Center, and later participates in care at the facility. This supports a reusable institutional pattern: one care organization can have field, transport and facility roles while those remain operationally distinct stages.

Ouros transformation:

FIELD_CONTACT -> TRANSPORT_DECISION -> VEHICLE_JOURNEY -> FACILITY_HANDOFF

The same NPC may participate in several stages, but completion of one stage never proves completion of the next.

The episode's specific characters, Mega Evolution scene, dialogue and battle are not reused.

### A vehicle and uniform do not establish legitimate custody or authority

Source: https://bulbapedia.bulbagarden.net/wiki/The_Chikorita_Rescue

The episode includes an ambulance arriving at a Pokémon Center and supposed paramedics moving a patient before their identity is revealed to be deceptive. The reusable lesson is about authority verification rather than the plot: visible medical presentation is evidence of appearance, not proof that a transport request, custody transfer or receiving authorization is legitimate.

Ouros transformation:

- vehicle identity;
- crew identity;
- service affiliation;
- dispatch assignment;
- patient release authorization;
- actual custody/handoff;

must be separable records when the story makes them important.

This creates investigation hooks without assuming fraud in routine play.

### Facility capacity and overflow can redirect care

Source: https://bulbapedia.bulbagarden.net/wiki/A_Chansey_Operation

The episode depicts a Pokémon Center facing enough injured Pokémon that additional medical space is sought elsewhere. The high-level lesson is that receiving capacity can become a world-state constraint and that referral to another site can be a response to capacity pressure.

Ouros transformation:

- `DESTINATION_SELECTED` is not permanent;
- a receiving site may later become unavailable or inappropriate;
- rerouting can occur without making the original dispatch wrong;
- overflow can create temporary cooperation between institutions.

No treatment procedure, staffing assumption or medical rule is copied.

## Public operational material used only for state architecture

### Emergency and non-emergency medical transport are different service problems

Sources:

- https://www.health.vic.gov.au/patient-care/ambulance-and-non-emergency-patient-transport
- https://www.health.vic.gov.au/patient-care/non-emergency-patient-transport
- https://www.health.nsw.gov.au/pts/Pages/about-pts.aspx

These public sources distinguish time-critical emergency ambulance response from non-emergency patient transport and describe non-emergency movement between homes, hospitals, rehabilitation sites and other facilities.

Reusable structural lesson:

- urgency/priority;
- mode/service selection;
- origin;
- destination;
- required monitoring/support during movement;
- booking or dispatch;

are separate pieces of state.

Ouros does not import Australian eligibility criteria, fees, response standards, staffing requirements or transport law.

### Arrival at a facility and transfer of care are separate events

Sources:

- https://www.health.qld.gov.au/system-governance/policies-standards/health-service-directives/patient-access-to-care/protocol-for-timely-transfer-of-care-in-emergency-departments
- https://www.health.vic.gov.au/patient-care/standards-for-safe-and-timely-ambulance-and-emergency-care-for-victorians

Both operational frameworks distinguish arrival from clinical handover/transfer of responsibility. That distinction is highly reusable for Ouros even without importing real-world timing targets or legal duties.

Ouros transformation:

`VEHICLE_ARRIVED_AT_DESTINATION != CARE_HANDOFF_ACCEPTED`

A patient can physically reach a site while the operational handoff is still pending, redirected or incomplete.

### Inter-facility retrieval is its own coordinated journey

Source: https://www.ambulance.vic.gov.au/adult-retrieval-victoria-arv

The source describes a coordination service for transfer of critically ill or injured patients between hospitals using several transport modes. The reusable lesson is that a transfer can require a requesting facility, accepting destination, coordinating service, suitable transport mode and specialist team rather than being a generic taxi journey.

Ouros transformation:

- referral request;
- destination acceptance;
- transport acceptance;
- crew/asset assignment;
- pickup readiness;
- departure;
- transfer;
- receiving handoff;

remain individually auditable.

No clinical thresholds, staffing model or real-world protocol is imported.

### Transport decision does not always equal hospital transport

Source: https://esa.act.gov.au/about-esa/emergency-services/ambulance/calling-ambulance

The ACT public guidance explicitly notes that ambulance assessment does not always result in hospital transport and that a hospital performs its own triage after arrival.

Reusable lesson for Ouros:

`RESPONSE_COMPLETED != TRANSPORT_REQUIRED`

and

`TRANSPORT_TO_FACILITY != TREATMENT_PRIORITY_DECIDED`

This prevents the transport layer from silently deciding care outcomes.

## Research exclusions and non-inference rules

Pass 118 does not import:

- real-world response-time standards;
- emergency-number systems;
- clinical triage scales;
- scope-of-practice law;
- ambulance staffing requirements;
- siren/right-of-way law;
- billing or insurance rules;
- medical treatment protocols;
- stretcher weight limits;
- vehicle speed/capacity values;
- helicopter or aircraft clinical criteria;
- medical diagnosis from dispatch descriptions.

It also does not infer:

- `ambulance present -> patient transported`;
- `vehicle arrived -> crew reached subject`;
- `crew reached subject -> transport accepted`;
- `patient loaded -> vehicle departed`;
- `vehicle arrived at hospital -> care handoff complete`;
- `handoff complete -> treatment complete`;
- `medical vehicle -> verified legitimate authority`;
- `Pokémon Center -> universal emergency department`;
- `Nurse Joy -> universal mechanical Medicine qualification`;
- `large/fast Pokémon -> legal emergency mount or carrier`;
- `flying Pokémon -> legal air ambulance`;
- `healing Move -> transport stabilization`;
- `fainted -> automatically requires ambulance`.

## Reusable Ouros design lessons

1. Medical transport is a chain of independently timestamped state transitions.
2. Dispatch information is a claim about a situation, not a diagnosis.
3. The selected destination can change while the original request remains historically valid.
4. Physical arrival and transfer of care must remain separate.
5. A responding unit can become unavailable after handoff because cleanup, restock, maintenance or crew state is unresolved; exact causes remain authored.
6. Inter-facility movement should preserve both referral state and travel state.
7. Medical transport can expose a region's geography, institutional relationships and inequalities without fabricating medical mechanics.
8. Repeated diversion, a temporary pickup point or a field response post can become persistent local memory.
9. A Pokémon may participate as an individual worker/partner only through authored agency plus verified mechanical capability where mechanics matter.
10. Reduced encounter forms should move patients and active care operations outside BattleSpec before combat.

## Candidate longer-term narrative value

A transport network creates stories beyond emergencies:

- a rural clinic depends on a mountain transfer route;
- a ferry or air connection links island care to a regional specialist;
- a temporary crisis pickup point becomes permanent;
- an old ambulance station remains on maps after service reorganization;
- residents remember which route stayed viable during a past disaster;
- an inter-facility team becomes a recurring cast;
- a Pokémon partner becomes locally recognizable through repeated documented service without gaining universal species-level authority;
- conflicting arrival/handoff timestamps create investigations that can be solved through provenance rather than hidden truth scores.

## Mechanical warning for downstream design

Any encounter that keeps a patient, stretcher, medical vehicle, active loading operation or evacuation movement inside the tactical grid may depend on several permanent capability families at once.

Do not treat the existing Intercept slice as proof of generalized escort, carrying, pushing, reaction competition or vehicle movement.

A safe current fallback is:

world-state medical operation -> isolate/complete protected movement -> construct a static legal BattleSpec -> AutoPTU resolves explicit combatants -> Ouros resumes transport/care state from the authoritative battle result.
