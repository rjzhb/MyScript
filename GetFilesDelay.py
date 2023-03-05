import csv
import math

std_map = {}


def merge_delays(i, j):
    delays = []
    for k in range(1, 688):
        filename = "E:/Projects/DataSet/NetLatency-Data/Seattle/SeattleData_%d" % k
        with open(filename, "r") as f:
            lines = f.readlines()
            delay = lines[i].split()[j]
            if(delay.strip() == ""):
                continue
            delays.append(str(float(delay) / 2))
    with open(
        "E:/Projects/DataSet/CSV/delay/delay%d_%d.csv" % (i, j), "w", newline=""
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["delay"])
        writer.writerows([[delay] for delay in delays])

    # 转化为float数组
    delaysFloat = list(map(float, delays))
    write_data_distribution(delaysFloat, i, j)


def write_data_distribution(data, i, j):
    mean = sum(data) / len(data)
    std = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    std_map[(i, j)] = std


def print_data_distribution():
    # 将字典中的键值对展开成元组 (key, value) 列表
    items = std_map.items()

    # 对元素按照值排序，排列顺序按从小到大的顺序
    sorted_items = sorted(items, key=lambda x: x[1])

    # 将排序后的元素转化为字典
    sorted_dict = {k: v for k, v in sorted_items}

    print(sorted_dict)


for i in range(1, 98):
    for j in range(1, 2):
        merge_delays(i, j)

print_data_distribution()