import pandas as pd

# 读取CSV文件并排序
df = pd.read_csv("E:/Projects/DataSet/CSV/fhvhv_tripdata_2022-07.csv")
df = df.sort_values(by=[df.columns[3]])

# 写入新的CSV文件
df.to_csv("E:/Projects/DataSet/CSV/fhvhv_tripdata_2022-07_sort.csv", index=False)