import pandas as pd

filename = "//wsl.localhost/Ubuntu/home/rjzhb/Project/OoOJoin/benchmark/datasets/sTuple.csv"
df = pd.read_csv(filename)
rows = df.head(100)

rows.to_csv(filename, index=False)