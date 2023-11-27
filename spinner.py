import sys
import threading
import time


class Spinner:
    def __init__(self, delay=0.1):
        self.spinner = self.spinning_cursor()
        self.delay = delay
        self.stop_running = threading.Event()
        self.spin_thread = threading.Thread(target=self.init_spin)

    def spinning_cursor(self):
        while not self.stop_running.is_set():
            yield from '|/-\\'

    def init_spin(self):
        while not self.stop_running.is_set():
            sys.stdout.write(next(self.spinner))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def start(self):
        self.spin_thread.start()

    def stop(self):
        self.stop_running.set()
        self.spin_thread.join()

# # # Usage:
# spinner = Spinner()
# spinner.start()
# time.sleep(10)
# spinner.stop()
