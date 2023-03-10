import csv

# 读取txt文件
with open("E:/Projects/DataSet/DataSets/rovio/1000ms_1t.txt", "r") as txt_file:
    lines = txt_file.readlines()

# 将数据写入csv文件
with open(
    "E:/Projects/DataSet/DataSets/rovio/1000ms_1t.csv", "w", newline=""
) as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["key", "value", "eventTime"])
    for line in lines:
        key = line.strip().split("|")[0]
        value = line.strip().split("|")[2]
        eventTime = line.strip().split("|")[3]
        writer.writerow([key, value, eventTime])
