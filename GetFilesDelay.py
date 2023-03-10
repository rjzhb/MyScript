import csv
import math

std_map = {}


def merge_delays(i, j):
    delays = []
    for k in range(1, 688):
        filename = "E:/Projects/DataSet/NetLatency-Data/Seattle/SeattleData_%d" % k
        with open(filename, "r") as f:
            lines = f.readlines()
            delay = ""
            if len(lines[i].split()) > j:
                delay = lines[i].split()[j]
            else:
                print("第%d个文件第%d %d有空格" % (k, i, j))
                continue
            if delay.strip() == "":
                continue
            if delay == 0:
                print("第%d个文件里面%d行没有足够的数字" % (k, i))
            delays.append(str(float(delay) / 2))
    with open(
        "E:/Projects/DataSet/CSV/delay/delay%d_%d.csv" % (i, j), "w", newline=""
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["delay"])
        writer.writerows([[delay] for delay in delays])

    # 转化为float数组
    delaysFloat = list(map(float, delays))
    if len(delaysFloat) == 0:
        return
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

    # 打开文件
    with open("delay_distribution.txt", "w") as f:
        # 遍历字典，将每个键值对写入文件
        for key, value in sorted_dict.items():
            f.write(f"{key}:{value}\n")

    print(sorted_dict)


for i in range(1, 99):
    for j in range(1, 99):
        merge_delays(i, j)

# 将数据分布输出，方便看出delay的分布集中情况
print_data_distribution()
