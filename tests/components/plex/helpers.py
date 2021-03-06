"""Helper methods for Plex tests."""
from plexwebsocket import SIGNAL_DATA


def trigger_plex_update(mock_websocket):
    """Call the websocket callback method."""
    callback = mock_websocket.call_args[0][1]
    callback(SIGNAL_DATA, None, None)
