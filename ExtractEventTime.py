import pandas as pd

# 读取原始csv文件
df = pd.read_csv('E:/Projects/DataSet/DataSets/ALL/sb_1000ms_1tHighDelayData.csv')

# 提取eventtime列并保存为新的csv文件
eventtime = df['eventTime']
eventtime.to_csv('eventTime4.csv', index=False)
