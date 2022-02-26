class ErrorCommand:

    def __init__(self) -> None:
        pass

    def unknown(self, msg: str) -> None:
        print(f"UNKNOWN {msg}", flush=True)

    def error(self, msg: str) -> None:
        print(f"ERROR {msg}", flush=True)

    def message(self, msg: str) -> None:
        print(f"MESSAGE {msg}", flush=True)

    def debug(self, msg: str) -> None:
        print(f"DEBUG {msg}", flush=True)

    def suggest(self, x: int, y: int) -> None:
        print(f"SUGGEST {x},{y}", flush=True)