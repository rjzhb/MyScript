import csv
import sys
import time

# 读取csv文件的第一列和第四列
with open("E:/Projects/DataSet/CSV/fhvhv_tripdata_2022-07.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    col1 = []
    col4 = []
    for i, row in enumerate(reader):
        if i >= 1000:
            break
        col1.append(row[0])
        col4.append(row[3])


# 对第四列的数据这种格式”2020-01-01 00:00:00"转化为以微秒为单位的时间戳
new_col4 = []
min_value = sys.maxsize

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
            writer.writerow([col1[i], int(new_col4[i]) - min_value])
        except ValueError:
            writer.writerow([col1[i], new_col4[i]])
    writer.writerow([0, min_value])
