import csv
import sys
import time

# 出租车TLC DataSet提取脚本

# 需要提取的数据行数
data_count = 200000

# 读取csv文件的第一列和第四列
with open("E:/Projects/DataSet/CSV/fhvhv_tripdata_2022-07.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    col1 = []
    col4 = []
    for i, row in enumerate(reader):
        if i >= data_count:
            break
        col1.append(row[0])
        col4.append(row[3])


# 对第四列的数据这种格式”2020-01-01 00:00:00"转化为以微秒为单位的时间戳
new_col4 = []
min_value = 2**63-1

for item in col4:
    try:
        timestamp = int(time.mktime(time.strptime(item, "%Y-%m-%d %H:%M:%S"))) * 1000000
        new_col4.append(timestamp)
        min_value = min(min_value, timestamp)
    except ValueError:
        new_col4.append("request_time")
        continue

# 将最终数据输出到一个csv文件里
with open(
    "E:/Projects/DataSet/CSV/fhvhv_tripdata_output.csv", "w", newline=""
) as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(col1)):
        try:
            if col1[i] == "HV0003":
                col1[i] = "1"
            if col1[i] == "HV0005":
                col1[i] = "2"
            if int(new_col4[i]) - min_value == 0:
                print("%d有一个0" % i)
            writer.writerow([col1[i], int(new_col4[i]) - min_value])
        except ValueError:
            writer.writerow([col1[i], new_col4[i]])
