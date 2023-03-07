import numpy as np
import matplotlib.pyplot as plt

# 定义网络节点数和zipf分布参数
N = 1000
s = 1.5

# 生成Zipf分布
zipf_dist = np.random.zipf(s, N)

# 归一化分布
zipf_dist = zipf_dist / float(sum(zipf_dist))

# 计算网络延迟
delays = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        delay = np.abs(zipf_dist[i] - zipf_dist[j])
        delays.append(delay)

# 绘制网络延迟分布图
plt.hist(delays, bins=50)
plt.title("Network Delay Distribution")
plt.xlabel("Delay")
plt.ylabel("Frequency")
plt.show()