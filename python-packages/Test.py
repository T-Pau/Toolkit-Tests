import sys
import traceback
from typing import Callable

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
            self.failed += 1

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
