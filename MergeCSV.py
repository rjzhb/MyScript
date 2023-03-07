import pandas as pd

# 读取第一个CSV文件
df = pd.read_csv("E:/Projects/DataSet/CSV/merge/file1.csv", encoding="utf-8-sig")

# 依次读取后续的CSV文件，并合并到df中
for i in range(2, 6):
    df_new = pd.read_csv(f"E:/Projects/DataSet/CSV/merge/file{i}.csv")
    df = pd.concat([df, df_new], ignore_index=True)

# 将合并后的数据写入新的CSV文件
df.to_csv(
    "E:/Projects/DataSet/CSV/merge/merged_file.csv", index=False, encoding="utf-8-sig"
)
