import threading
import time

class CountdownTimer:
    def __init__(self, seconds, callback=None):
        self.seconds = seconds
        self.callback = callback
        self._running = False

    def start(self):
        self._running = True
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        while self.seconds > 0 and self._running:
            time.sleep(1)
            self.seconds -= 1
        if self.callback:
            self.callback()

    def stop(self):
        self._running = False

    def reset(self, seconds=None):
        if seconds is not None:
            self.seconds = seconds
        self._running = False
