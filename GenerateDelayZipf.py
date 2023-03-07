import csv
import random
import numpy as np

# 设置Zipf分布参数
alpha = 1.5
xmin = 1
N = 100000

# 生成Zipf分布数据
zipf_data = np.random.zipf(alpha, size=N)

# 将生成的网络延迟写入CSV文件
with open('network_delay.csv', mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['delay'])
    for delay in zipf_data:
        writer.writerow([delay])

print("网络延迟生成完毕并保存到文件：network_delay.csv")