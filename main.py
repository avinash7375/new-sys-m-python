import signal
import time

from metrics import collect_metrics
from display import display_metrics


running = True


def shutdown(sig, frame):
    global running
    running = False
    print("\nExiting...")


signal.signal(signal.SIGINT, shutdown)

UPDATE_INTERVAL = 2

print("Starting Windows System Monitor...")
print("Press Ctrl+C to exit")

time.sleep(1)

while running:
    metrics = collect_metrics()
    display_metrics(metrics)
    time.sleep(UPDATE_INTERVAL)
