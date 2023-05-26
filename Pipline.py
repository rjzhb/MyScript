import csv
import os
import numpy as np
import pandas as pd
import pyarrow.parquet as pq


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


dir_path = "E:/Projects/DataSet/CSV/"
# 遍历当前目录下的所有文件
for root, dirs, files in os.walk(dir_path):
    cnt = 0
    for file in files:
        # 如果文件是parquet文件，则进行转换
        if file.endswith(".parquet"):
            # 获取文件路径
            file_path = os.path.join(root, file)
            parquet_file = pq.read_table(file_path)
            df = parquet_file.to_pandas()
            csv_file_name = file.replace(".snappy.parquet", ".csv")
            # 将文件保存为csv文件
            csv_file_path = os.path.join(root, csv_file_name)
            df.to_csv(csv_file_path, index=False)

            # # 保留第一列数据，并将其复制给新的DataFrame
            # df_new = df.iloc[:, -2:] # 保留最后两列数据
            # df_new.columns = ['key', 'value'] # 修改列名为key和value
            # # df_new = df.iloc[:, [0]].copy()
            # # 新增名为"value"的列，其中数据随机生成
            # # df_new["value"] = np.random.rand(len(df_new))
            # # 将第一行的列名改为"key"
            # # df_new.columns = ["key", "value"]
            # csv_file_name = file.replace(".snappy.parquet", ".csv")
            # # 将文件保存为csv文件
            # csv_file_path = os.path.join(root, csv_file_name)
            # df_new.to_csv(csv_file_path, index=False)
            # cnt += 1
            # # 处理csv文件
            # directory, filename = os.path.split(csv_file_path)
            # new_filename = str(cnt) + os.path.splitext(filename)[-1]
            # csv_file_path2 = os.path.join(directory, new_filename)
            # with open(csv_file_path, "r") as file1, open(
            #     "eventTime3.csv", "r"
            # ) as file2, open(csv_file_path2, "w", newline="") as merged_file:
            #     reader1 = csv.reader(file1)
            #     reader2 = csv.reader(file2)
            #     writer = csv.writer(merged_file)

            #     header1 = next(reader1)
            #     header2 = next(reader2)

            #     writer.writerow([header1[0], header1[1], header2[0]])

            #     for row1, row2 in zip(reader1, reader2):
            #         writer.writerow([row1[0], row1[1], row2[0]])
            # # 加入arrivalTime
            # # 输出带有三列的csv文件，这三列属性分别是:  key , te,  ta( te + delay)
            # keyData = read_key_file(csv_file_path2)
            # delayData = read_delay_file("LowDelayData.csv")

            # directory, filename = os.path.split(csv_file_path2)
            # new_filename = (
            #     os.path.basename(os.path.dirname(csv_file_path2))
            #     + "LowDelay"
            #     + str(cnt)
            #     + os.path.splitext(filename)[-1]
            # )
            # csv_file_path3 = os.path.join(directory, new_filename)
            # with open(csv_file_path3, "w", newline="") as csvfile:
            #     writer = csv.writer(csvfile)
            #     writer.writerow(["key", "value", "eventTime", "arrivalTime"])
            #     j = 0
            #     for i in range(len(keyData)):
            #         if j >= len(delayData):
            #             j = 0
            #         writer.writerow(
            #             [
            #                 keyData[i][0],
            #                 keyData[i][1],
            #                 keyData[i][2],
            #                 float(delayData[j]) * 1000 * 1000 + float(keyData[i][2]),
            #             ]
            #         )
            #         j += 1
