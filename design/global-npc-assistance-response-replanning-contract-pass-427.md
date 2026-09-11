# Global NPC assistance response replanning contract — Pass 427

Status: IMPLEMENTED ARCHITECTURE / NON-CANON CONTENT

Purpose

Pass 426 can return a durable assistance response to the original requester through the ordinary information network. Pass 427 closes the next causal seam: only a response that is actually delivered may update the requester and wake that requester's agenda.

Required lineage

The bridge requires an existing PLANNED REQUEST_ASSISTANCE action, an existing PLANNED response action owned by the original recipient, an InformationEnvelope from that responder back to the requester, and a source claim whose provenance root is the response action ID.

The source claim subject must remain `assistance_response:<request_action_id>:<response_action_id>`. Its value must equal the durable response intent kind. Sender and receiver identities must continue to match the two world actions.

Supported responses

ACCEPT_ASSISTANCE_REQUEST, DEFER_ASSISTANCE_REQUEST, REJECT_ASSISTANCE_REQUEST and COUNTERPROPOSE_ASSISTANCE_REQUEST may all wake the requester after actual delivery. The response type changes what the requester has learned. It does not by itself execute assistance.

Delivery boundary

DELIVERED may materialize private knowledge and schedule one selective KNOWLEDGE_DELIVERED wake for the requester. QUEUED, FAILED_CHANNEL_UNAVAILABLE, WAITING_LOCAL_ACK and a delivery deferred by budget cannot wake the requester. A local-projection ACK must succeed before the response is treated as delivered.

Shared institution membership does not expand the audience. A third NPC at the same site or in the same faction remains unchanged unless that actor receives a separate information event.

No implicit consequence

This bridge does not reserve time, create a commitment, start travel, alter a relationship, create a quest completion, bind another actor, or invoke AutoPTU. ACCEPT still requires a separate commitment/reservation owner. DEFER still requires an explicit future condition or window. COUNTERPROPOSE still requires an explicit proposal payload before it can alter plans.

Replay and failure policy

The ordinary information queue remains the delivery authority. The world-event coordinator remains the knowledge/replanning authority. Conflicting sender, receiver, source subject, source value or provenance fails closed before delivery-driven replanning is accepted.

Mechanical boundary

No PTU mechanic is implemented by this pass. Any later tactical assistance scene must declare its dependencies using the permanent engine capability families rather than inferring support from this communication bridge.