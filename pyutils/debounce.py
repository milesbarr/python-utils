from functools import wraps
import threading
import time
from typing import Any


def debounce(wait_seconds: float):
    """Decorator that debounces a function.

    When the decorated function is called multiple times in succession,
    only the last call will be executed after `wait_seconds` seconds
    have passed. This is useful for scenarios such as handling rapid
    user input events.

    Args:
        wait_seconds (float): Seconds to wait after the last call.

    Returns:
        Callable: A debounced version of the original function.

    Example:
        @debounce(0.5)
        def on_change(value):
            print(f"Value changed to {value}")
    """
    def decorator(func):
        timer = None
        lock = threading.Lock()

        @wraps(func)
        def debounced(*args: Any, **kwargs: Any):
            nonlocal timer

            def execute_func():
                with lock:
                    func(*args, **kwargs)

            with lock:
                if timer:
                    timer.cancel()
                timer = threading.Timer(wait_seconds, execute_func)
                timer.start()

        return debounced
    return decorator
