import sys
import traceback
from typing import Any, Callable

class Test:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def run(self):
        try:
            self.execute_sub()
        except Exception as e:
            self.failure(f"Test failed with uncaught exception {type(e)}: '{str(e)}'")
            traceback.print_exc()
            sys.exit(1) # TODO: return different code for execution errors

        if self.failed > 0:
            sys.exit(1)

    def execute_sub(self):
        raise NotImplementedError("Subclasses must implement execute_sub method.")

    def failure(self, msg: str) -> None:
        print(msg, file=sys.stderr)
        self.failed += 1

    def ok(self, test: str, function: Callable[[], None]) -> None:
        try:
            function()
            self.passed += 1
        except Exception as e:
            self.failure(f"{test} raised an unexpected exception of type {type(e)}: '{str(e)}'.")
            traceback.print_exc()

    def raises(self, test: str, function: Callable[[], None], exception_type: type, exception_message: str) -> None:
        try:
            function()
            self.failure(f"{test} did not raise an exception.")
        except Exception as e:
            if not isinstance(e, exception_type):
                self.failure(f"{test} raised wrong type of exception: expected {exception_type}, got {type(e)}.")
            elif str(e) != exception_message:
                self.failure(f"{test} raised exception with wrong message: expected '{exception_message}', got '{str(e)}'.")
            else:
                self.passed += 1

    def equals(self, test: str, result: Any, expected: Any) -> None:
        if result == expected:
            self.passed += 1
        else:
            self.failure(f"{test} failed: expected {self._pretty(expected)}, got {self._pretty(result)}.")
        
    def _pretty(self, value: Any) -> str:
        if isinstance(value, list):
            return "[" + ", ".join(self._pretty(v) for v in value) + "]"
        elif isinstance(value, dict):
            return "{" + ", ".join(f"{self._pretty(k)}: {self._pretty(v)}" for k, v in value.items()) + "}"
        elif isinstance(value, bytes):
            return "b'" + ''.join(f'\\x{b:02x}' for b in value) + "'"
        else:
            return str(value)
