import pyarrow.parquet as pq
import pandas as pd

# 将Parquet格式dataset文件转化为csv文件
parquet_file = pq.read_table(
    "E:/Projects/DataSet/CSV/shunfeng/bo_shunfeng_sell/part-00000-ced299d3-0f12-403d-a7f7-68ad87085667-c000.snappy.parquet"
)
df = parquet_file.to_pandas()
df.to_csv(
    "E:/Projects/DataSet/CSV/shunfeng/bo_shunfeng_sell/part-00000-ced299d3-0f12-403d-a7f7-68ad87085667-c000.snappy.csv",
    index=False,
)
