import os

class Info:

    def __init__(self) -> None:
        self._registry = {"timeout_turn": 0,
                          "timeout_match": 60000,
                          "max_memory": 83000,
                          "time_left": 0,
                          "game_type": 0,
                          "rule": 1,
                          "evaluate": 25,
                          "folder": ""}

    def get_valid_keys(self) -> None:
        return (list(self._registry.keys()))

    def set_value(self, key: str, val: int or str) -> None:
        if key in self._registry.keys():
            if key == "timeout_turn":
                if val < 0:
                    print("ERROR Bad timeout_turn", flush = True)
            if key == "timeout_match":
                if val < 0:
                    print("ERROR Bad timeout_match", flush = True)
            if key == "max_memory":
                if val < 0:
                    print("ERROR Bad max_memory", flush = True)
            if key == "time_left":
                if val < 0:
                    print("ERROR Bad time_left", flush = True)
            if key == "game_type":
                if val not in [0, 1, 2, 3]:
                    print("ERROR Bad game_type", flush= True)
            if key == "rule":
                if val not in [1, 2, 4]:
                    print("ERROR Bad rule", flush=True)
            if key == "evaluate":
                pass
            if key == "folder":
                os.mkdir(val)

            self._registry[key] = val

    def get_value(self, key: str) -> int:
        if key in self._registry.keys():
            return (self._registry[key])
        return (-1)