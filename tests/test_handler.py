import json
from unittest import mock

from notifier import handler


def test_pushes_gate_changes_only():
    event = {"Records": [
        {"body": json.dumps({"type": "gate_changed", "flight": "OA123", "day": "2026-11-20"})},
        {"body": json.dumps({"type": "boarded", "flight": "OA123", "day": "2026-11-20"})},
    ]}
    with mock.patch.object(handler.requests, "post") as post:
        assert handler.handle(event, None) == {"pushed": 1}
        post.assert_called_once()
