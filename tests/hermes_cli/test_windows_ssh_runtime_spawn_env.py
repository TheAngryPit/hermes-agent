"""Windows Desktop SSH spawns must retain loopback session-token auth."""

import os
from unittest.mock import patch

from hermes_cli.windows_ssh_runtime import _backend_spawn_env


def test_ssh_backend_gets_desktop_marker_without_changing_parent_environment():
    with patch.dict(os.environ, {"VIRTUAL_ENV": "foreign", "PYTHONPATH": "foreign", "HERMES_DESKTOP": "0"}):
        env = _backend_spawn_env()
        assert env["HERMES_DESKTOP"] == "1"
        assert "VIRTUAL_ENV" not in env
        assert "PYTHONPATH" not in env
        assert os.environ["HERMES_DESKTOP"] == "0"
