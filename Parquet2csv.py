import pyarrow.parquet as pq
import pandas as pd

# 将Parquet格式dataset文件转化为csv文件
parquet_file = pq.read_table(
    "E:/Projects/DataSet/CSV/shunfeng/action/part-00004-b629578e-cbc1-4de8-be67-1392e73baf11-c000.snappy.parquet"
)
df = parquet_file.to_pandas()
df.to_csv(
    "E:/Projects/DataSet/CSV/shunfeng/action/part-00004-b629578e-cbc1-4de8-be67-1392e73baf11-c000.snappy.csv",
    index=False,
)
