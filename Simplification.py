import pandas as pd

# 读取CSV文件
df = pd.read_csv('GenerateDataSetMidDelay.csv')

# 计算eventTime列的最小值
min_val = df['eventTime'].min()


# 将eventTime列的数据减去最小值
df['eventTime'] = df['eventTime'] - min_val
df['arrivalTime'] = df['arrivalTime'] - min_val

# 将处理后的数据写回CSV文件
df.to_csv('GenerateDataSetMidDelay.csv', index=False)