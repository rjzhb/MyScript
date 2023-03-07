import pandas as pd

# 读取CSV文件并排序
df = pd.read_csv("fhvhv_tripdata_2022-07.csv")
df = df.sort_values(by=[df.columns[3]])

# 写入新的CSV文件
df.to_csv("tripdata_sort.csv", index=False)