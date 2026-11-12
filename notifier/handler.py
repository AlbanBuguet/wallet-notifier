"""Pushes the gate changes and the delays of flights to the passes."""

import json
import logging
import os

import requests

log = logging.getLogger(__name__)
SIGNER_URL = os.environ.get("PASS_SIGNER_URL", "")


def handle(event, _context):
    """Handles a batch of flight events from flight-status-events."""
    pushed = 0
    for record in event.get("Records", []):
        change = json.loads(record["body"])
        if change.get("type") not in ("gate_changed", "delayed"):
            continue
        requests.post(f"{SIGNER_URL}/push", json={"flight": change["flight"], "day": change["day"]}, timeout=3)
        pushed += 1
    log.info("pushed updates", extra={"count": pushed})
    return {"pushed": pushed}
