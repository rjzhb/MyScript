import csv
import sys
import time

# 出租车TLC DataSet提取脚本

# 需要提取的数据行数
data_count = 100000

min_value = sys.maxsize

# 读取csv文件的第一列和第四列
with open("E:/Projects/DataSet/CSV/fhvhv_tripdata_output_2.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    col1 = []
    col4 = []
    for i, row in enumerate(reader):
        if i >= data_count:
            break
        col1.append(row[0])
        col4.append(row[1])
        if row[1].isdigit():
            min_value = min(min_value, int(row[1]))



# 将最终数据输出到一个csv文件里
with open(
    "E:/Projects/DataSet/CSV/fhvhv_tripdata_output_3.csv", "w", newline=""
) as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(col1)):
        try:
            if col1[i] == "HV0003":
                col1[i] = "1"
            if col1[i] == "HV0005":
                col1[i] = "2"
            writer.writerow([col1[i], int(col4[i]) - min_value])
        except ValueError:
            writer.writerow([col1[i], col4[i]])
