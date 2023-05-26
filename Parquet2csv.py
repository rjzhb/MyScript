import pyarrow.parquet as pq
import pandas as pd

# 将Parquet格式dataset文件转化为csv文件
parquet_file = pq.read_table(
    "E:/Projects/DataSet/CSV/walmart/action/part-00000-d5356145-8989-482f-a5cc-0280f05af750-c000.snappy.parquet"
)
df = parquet_file.to_pandas()
df.to_csv(
    "E:/Projects/DataSet/CSV/walmart/action/part-00000-d5356145-8989-482f-a5cc-0280f05af750-c000.csv",
    index=False,
)
