import csv

# 合并key, te, ta三大属性

# 读入带Key, te属性的csv文件
def read_key_file(name):
    data = []
    with open("E:/Projects/DataSet/CSV/" + name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append((row[0], row[1]))

    return data


# 读入带delay的文件
def read_delay_file(name):
    data = []
    with open("E:/Projects/DataSet/CSV/delay/" + name, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append(row[0])

    return data


# 输出带有三列的csv文件，这三列属性分别是:  key , te,  ta( te + delay)
keyData = read_key_file("fhvhv_tripdata_output.csv")
delayData = read_delay_file("delay97_1.csv")

with open("TLCDataSet", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["key", "te", "ta"])
    for i in range(len(delayData)):
        writer.writerow(
            [
                keyData[i][0],
                keyData[i][1],
                float(delayData[i]) * 1000 * 1000 + float(keyData[i][1]),
            ]
        )
