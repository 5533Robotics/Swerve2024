class BuildData:
    class Time:
        MILLISECONDS = "ms"
        SECONDS = "s"
        MINUTES = "min"
        HOURS = "h"

        def __init__(self):
            self._time = 0

        def add(self, time: int):
            self._time += time
            return self

        def remove(self, time: int):
            self._time -= time
            return self

        def get(self):
            return self._time

        def convert(self, unit: str):
            if unit == self.MILLISECONDS:
                return self._time * 1000
            elif unit == self.SECONDS:
                return self._time
            elif unit == self.MINUTES:
                return self._time / 60
            elif unit == self.HOURS:
                return self._time / 3600
            else:
                raise ValueError(f"Unsupported time unit: {unit}")

    def __init__(self):
        self._time_instance = self.Time()

    def time(self) -> Time:
        return self._time_instance
