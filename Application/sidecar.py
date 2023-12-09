# sidecar.py - Sidecar monitoring script
import time
import os

counter_file = '/app/counter.txt'

while True:
    # Monitor file metrics
    if os.path.exists(counter_file):
        with open(counter_file, 'r') as f:
            current_count = int(f.read())
            print(f"Visitor count: {current_count}")
    time.sleep(15)
