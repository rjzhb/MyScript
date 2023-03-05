import csv


def merge_delays(i, j):
    delays = []
    for k in range(1, 688):
        filename = "E:/Projects/DataSet/NetLatency-Data/Seattle/SeattleData_%d" % k
        with open(filename, "r") as f:
            lines = f.readlines()
            delay = lines[i].split()[j]
            delays.append(str(float(delay) / 2))
    with open(
        "E:/Projects/DataSet/CSV/delay/delay%d_%d.csv" % (i, j), "w", newline=""
    ) as f:
        writer = csv.writer(f)
        writer.writerow(["delay"])
        writer.writerows([[delay] for delay in delays])


merge_delays(50, 50)
