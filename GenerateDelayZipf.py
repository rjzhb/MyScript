import csv
import random
import numpy as np
import time

# 设置Zipf分布参数
alpha = 1.5
xmin = 1
N = 100000

# 生成Zipf分布数据
zipf_data = np.random.zipf(alpha, size=N)

# 获取当前时间戳
current_timestamp = int(time.time() * 1000)

# 将生成的网络延迟写入CSV文件
with open('network_delay.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['delay'])
    for delay in zipf_data:
        # 计算生成的时间戳，确保在1秒以内
        timestamp = current_timestamp + delay
        if timestamp > current_timestamp + 1000:
            timestamp = current_timestamp + 1000 - random.randint(1, 100)
        
        # 将延迟和时间戳写入CSV文件
        writer.writerow([delay, timestamp])
        
print("网络延迟生成完毕并保存到文件：network_delay.csv")