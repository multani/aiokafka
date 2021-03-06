from typing import Any

class Heartbeat:
    DEFAULT_CONFIG: Any = ...
    config: Any = ...
    last_send: Any = ...
    last_receive: Any = ...
    last_poll: Any = ...
    last_reset: Any = ...
    heartbeat_failed: Any = ...
    def __init__(self, **configs: Any) -> None: ...
    def poll(self) -> None: ...
    def sent_heartbeat(self) -> None: ...
    def fail_heartbeat(self) -> None: ...
    def received_heartbeat(self) -> None: ...
    def time_to_next_heartbeat(self): ...
    def should_heartbeat(self): ...
    def session_timeout_expired(self): ...
    def reset_timeouts(self) -> None: ...
    def poll_timeout_expired(self): ...
