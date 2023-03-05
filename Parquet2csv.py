import pyarrow.parquet as pq
import pandas as pd

# 将Parquet格式dataset文件转化为csv文件
parquet_file = pq.read_table("E:/Projects/DataSet/fhvhv_tripdata_2022-07.parquet")
df = parquet_file.to_pandas()
df.to_csv("E:/Projects/DataSet/CSV/fhvhv_tripdata_2022-07.csv", index=False)
