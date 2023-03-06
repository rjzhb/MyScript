import os

#将delay整理成逗号隔开的形式

# 读取txt文件
with open("delay_distribution.txt", "r") as f:
    lines = f.readlines()

# 遍历每一行
for line in lines:
    # 提取i和j
    i, j = line.split(":")[0].replace("(", "").replace(")", "").split(", ")
    # 将i和j拼接成文件名
    filename = "SortOutDelay.txt"
    # 将(4, 4):0.0中的0.0写入到对应的csv文件中
    with open(filename, "a") as f:
        f.write("'delay%d_%d.csv'," % (int(i), int(j)))
