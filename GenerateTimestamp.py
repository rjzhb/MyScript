import random
import time
import csv

timestamps = []
start_time = time.time()
for i in range(1000):
    new_timestamp = start_time + random.uniform(0, 1)
    timestamps.append(new_timestamp)
    start_time = new_timestamp

with open("timestamps.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["eventTime"])
    for timestamp in timestamps:
        timestamp_microseconds = int(timestamp * 1000000)
        writer.writerow([timestamp_microseconds])