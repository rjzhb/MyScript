import datetime
import random
import time
import csv

timestamps = []
start_time = time.time()
for i in range(1000):
    new_timestamp = time.time() + random.uniform(0, 1)
    timestamps.append(new_timestamp)

with open("timestamps.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["eventTime"])
    for timestamp in timestamps:
        timestamp_microseconds = int(timestamp * 1000000)
        # 将微秒时间戳转换为datetime对象
        dt = datetime.datetime.fromtimestamp(timestamp)
        # 格式化输出
        print(dt.strftime('%Y-%m-%d %H:%M:%S'))
        writer.writerow([timestamp_microseconds])