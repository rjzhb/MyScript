import csv

with open("E:/Projects/DataSet/CSV/shunfeng/action/2.csv", "r") as file1, open("timestamps.csv", "r") as file2, open("E:/Projects/DataSet/CSV/shunfeng/action/merge2.csv", "w", newline="") as merged_file:
    reader1 = csv.reader(file1)
    reader2 = csv.reader(file2)
    writer = csv.writer(merged_file)

    header1 = next(reader1)
    header2 = next(reader2)

    writer.writerow([header1[0], header1[3], header2[0]])

    for row1, row2 in zip(reader1, reader2):
        writer.writerow([row1[0], row1[3], row2[0]])