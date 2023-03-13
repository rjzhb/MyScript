import csv
import csv
import random
import numpy as np

# 合并key, te, ta三大属性


# 读入带Key, value, te属性的csv文件
def read_key_file(name):
    data = []
    with open(name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append((row[0], row[1], row[2]))

    return data


# 读入带delay的文件
def read_delay_file(name):
    data = []
    with open(name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append(row[0])

    return data


# 设置Zipf分布参数
alpha = 1.5
xmin = 1
N = 10000000

# 生成Zipf分布数据
zipf_data = np.random.zipf(alpha, size=10000000)


# 输出带有三列的csv文件，这三列属性分别是:  key , te,  ta( te + delay)
keyData = read_key_file("E:/Projects/DataSet/DataSets/YSB/ad_events.csv")
delayData = read_delay_file("MidDelayData.csv")

with open(
    "E:/Projects/DataSet/DataSets/YSB/ad_eventsMidDelayData.csv", "w", newline=""
) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["key", "value", "eventTime", "arrivalTime"])
    j = 0
    for i in range(len(keyData)):
        if i < len(delayData):
            writer.writerow(
                [
                    keyData[i][0],
                    keyData[i][1],
                    keyData[i][2],
                    float(delayData[i]) * 1000 * 1000 + float(keyData[i][2]),
                ]
            )
        else:
            writer.writerow(
                [
                    keyData[i][0],
                    keyData[i][1],
                    keyData[i][2],
                    float(zipf_data[j]) * 1000 * 1000 + float(keyData[i][2]),
                ]
            )
            j += 1
