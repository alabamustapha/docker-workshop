import sys
import pandas as pd

parameter = sys.argv[1]

print("Parameter received:", parameter)

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{parameter}.parquet")

print("DataFrame saved to output_day_{}.parquet".format(parameter))