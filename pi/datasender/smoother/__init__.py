from collections import deque
import time


class Smoother:
    def __init__(self, interval: float):
        self.interval = interval
        self.data = deque()

    def add_measurement(self, value: float):
        current_time = time.time()
        self.data.append((current_time, value))
        self._remove_old_measurements(current_time)

    def get_average(self) -> float:
        self._remove_old_measurements(time.time())
        return sum(value for _, value in self.data) / len(self.data) if self.data else 0.0

    def _remove_old_measurements(self, current_time: float):
        while self.data and (current_time - self.data[0][0] > self.interval):
            self.data.popleft()
